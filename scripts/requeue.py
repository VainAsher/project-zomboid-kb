#!/usr/bin/env python3
"""
Re-queue report: which documents need re-verification, and why.

Three independent signals, combined into one worklist:

  1. VERSION  - a document's game_versions_verified lags the newest announced
                build. Compared at (major, minor) precision: a hotfix inside the
                verified minor (42.20.4 vs "42.20") is not flagged here, it
                surfaces through the changelog signal. Docs tagged `historic`
                skip this check; B41 docs are compared with the legacy line.
  2. DATE     - review_due has passed.
  3. UMBRELLA - the Umbrella pins drifted (newer tag, or a pinned tag moved);
                every Modders document is flagged (they cite the stubs).

Plus CHANGELOG evidence: official Steam announcements newer than the pins (or
dated on/after --since) are split into lines and matched against the entity map
(exports/entity-map.json) to show which documents each line probably affects.
This is a heuristic pointer for the orchestrator, never proof of impact, and
the evidence lines are printed so a human can judge. A new STABLE release also
flags the release-bookkeeping documents ("always_on_release").
Forum topics linked from the posts are listed because the forum blocks bots:
read them in a browser (the 42.21 full patch notes lived there).

Exit 0 = nothing to re-queue, 2 = worklist non-empty, 1 = hard error.
Stdlib only. Network: Steam news + git ls-remote, unless --feed-file/--tags-file
(or --offline) are used.

Usage:
  python scripts/requeue.py [--markdown OUT.md] [--json OUT.json]
         [--today YYYY-MM-DD] [--since YYYY-MM-DD] [--offline]
         [--feed-file FEED.json] [--tags-file TAGS.txt] [--pins PINS.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_entity_map as bem  # noqa: E402
import check_freshness as cf  # noqa: E402
import watch_umbrella as wu  # noqa: E402

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---", re.S)
FORUM_RE = re.compile(r"https://theindiestone\.com/forums/topic/\d+[-\w]*/?")


def read_front_matter(path: Path) -> dict:
    m = FM_RE.match(path.read_text(encoding="utf-8"))
    out: dict = {}
    for line in (m.group(1) if m else "").splitlines():
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith("["):
            try:
                v = json.loads(v)
            except json.JSONDecodeError:
                pass
        elif len(v) > 1 and v[0] == v[-1] == '"':
            v = v[1:-1]
        out[k.strip()] = v
    return out


def mm(version: str) -> tuple[int, int]:
    p = re.findall(r"\d+", version)
    return (int(p[0]), int(p[1]) if len(p) > 1 else 0)


def load_docs() -> list[dict]:
    docs = []
    for p in bem.doc_files():
        fm = read_front_matter(p)
        if "id" in fm:
            fm["_path"] = str(p).replace("\\", "/")
            docs.append(fm)
    return docs


def version_reasons(doc: dict, stable: str, legacy: str) -> list[str]:
    build = doc.get("build", "")
    if build == "historic":
        return []
    verified = doc.get("game_versions_verified", [])
    if not isinstance(verified, list):
        verified = []
    out = []
    if build in ("B42", "both"):
        v42 = [mm(v) for v in verified if str(v).startswith("42.")]
        if not v42:
            out.append("no B42 version recorded in game_versions_verified")
        elif max(v42) < mm(stable):
            out.append(f"verified B42 {max(v42)[0]}.{max(v42)[1]} < current stable {stable}")
    if build in ("B41", "both") and legacy and legacy != "?":
        v41 = [mm(v) for v in verified if str(v).startswith("41.")]
        if build == "B41" and not v41:
            out.append("no B41 version recorded in game_versions_verified")
        elif v41 and max(v41) < mm(legacy):
            out.append(f"verified B41 {max(v41)[0]}.{max(v41)[1]} < legacy {legacy}")
    return out


def clean_post(text: str) -> list[str]:
    text = re.sub(r"\[url=([^\]]*)\]([^\[]*)\[/url\]", r"\2 (\1)", text)
    text = re.sub(r"\[\*\]", "\n", text)
    text = re.sub(r"\[/?h\d\]", "\n", text)
    text = re.sub(r"\[/?(?:list|p|hr|i|b|u|img)[^\]]*\]", "\n", text)
    text = re.sub(r"\[[^\]\n]{1,60}\]", "", text)
    return [ln.strip(" -•\t") for ln in text.splitlines() if len(ln.strip()) >= 12]


def new_posts(items: list[dict], pinned_b42: str, pinned_b41: str, since: date | None) -> list[dict]:
    out = []
    for it in sorted(items, key=lambda i: i["date"]):
        d = date.fromtimestamp(it["date"])
        if since is not None:
            if d >= since and cf.VER.search(it["title"]):
                out.append(it)
            continue
        newer = False
        for part in re.split(r"\s*&\s*", it["title"]):
            m = cf.VER.search(part)
            chan = cf.channel_of(part)
            if not m or not chan:
                continue
            ver = ".".join(g for g in m.groups() if g is not None)
            if chan in ("STABLE", "UNSTABLE") and cf.vkey(ver) > cf.vkey(pinned_b42):
                newer = True
            if chan == "LEGACY" and pinned_b41 != "?" and cf.vkey(ver) > cf.vkey(pinned_b41):
                newer = True
        if newer:
            out.append(it)
    return out


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pins", default="sources/pins.json")
    ap.add_argument("--feed-file")
    ap.add_argument("--tags-file")
    ap.add_argument("--offline", action="store_true", help="skip Steam and git network calls")
    ap.add_argument("--today", help="override today's date (testing), YYYY-MM-DD")
    ap.add_argument("--since", help="treat Steam posts dated on/after this day as new (testing/backfill)")
    ap.add_argument("--markdown")
    ap.add_argument("--json")
    args = ap.parse_args()

    today = datetime.strptime(args.today, "%Y-%m-%d").date() if args.today else date.today()
    since = datetime.strptime(args.since, "%Y-%m-%d").date() if args.since else None
    pins = json.loads(Path(args.pins).read_text(encoding="utf-8"))
    pinned_b42, pinned_b41 = cf.pinned_builds(pins)
    notes: list[str] = []

    # ---- feed (current builds + new posts)
    items: list[dict] = []
    stable, legacy = pinned_b42, pinned_b41
    if not args.offline or args.feed_file:
        try:
            items = cf.fetch_feed(100, args.feed_file)
            latest = cf.latest_builds(items)
            if latest["STABLE"] and cf.vkey(latest["STABLE"][0]) > cf.vkey(pinned_b42):
                stable = latest["STABLE"][0]
            if latest["LEGACY"] and pinned_b41 != "?" and cf.vkey(latest["LEGACY"][0]) > cf.vkey(pinned_b41):
                legacy = latest["LEGACY"][0]
        except Exception as e:  # noqa: BLE001
            notes.append(f"Steam news feed unavailable ({e}); version checks use the pins.")
    else:
        notes.append("offline: Steam feed and Umbrella tags not read; version checks use the pins.")

    # ---- Umbrella drift
    umbrella: list[str] = []
    if not args.offline or args.tags_file:
        try:
            umbrella = wu.check(pins, wu.read_tags(args.tags_file, pins["umbrella"]["repo"] + ".git"))
        except Exception as e:  # noqa: BLE001
            notes.append(f"Umbrella tags unavailable ({e}).")

    # ---- per-document staleness
    docs = load_docs()
    queue: dict[str, dict] = {}

    def add(doc_id: str, reason: str, kind: str) -> None:
        q = queue.setdefault(doc_id, {"id": doc_id, "reasons": [], "kinds": set()})
        if reason not in q["reasons"]:
            q["reasons"].append(reason)
        q["kinds"].add(kind)

    for d in docs:
        for r in version_reasons(d, stable, legacy):
            add(d["id"], r, "version")
        due = d.get("review_due")
        if isinstance(due, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", due):
            if datetime.strptime(due, "%Y-%m-%d").date() < today:
                add(d["id"], f"review_due {due} has passed", "date")
        if umbrella and d.get("category") == "Modders":
            add(d["id"], "Umbrella pin drift: " + "; ".join(umbrella), "umbrella")

    # ---- changelog evidence
    posts_out = []
    changelog_hits: dict[str, list[int]] = {}
    forum_topics: set[str] = set()
    emap = None
    if items:
        if not bem.OUT.exists():
            bem.OUT.parent.mkdir(parents=True, exist_ok=True)
            bem.OUT.write_text(json.dumps(bem.build(), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        emap = bem.load_map()
        known = {d["id"] for d in docs}
        new_stable = False
        for it in new_posts(items, pinned_b42, pinned_b41, since):
            evidence: dict[str, dict] = {}
            for line in clean_post(it.get("contents", "")):
                for doc_id, terms in bem.match_line(line, emap).items():
                    if doc_id not in known:
                        continue
                    e = evidence.setdefault(doc_id, {"lines": 0, "examples": []})
                    e["lines"] += 1
                    if len(e["examples"]) < 3:
                        e["examples"].append({"terms": sorted(terms), "line": line[:160]})
            forum_topics.update(FORUM_RE.findall(it.get("contents", "")))
            for doc_id, e in evidence.items():
                agg = changelog_hits.setdefault(doc_id, [0, 0])
                agg[0] += e["lines"]
                agg[1] += 1
            title_up = it["title"].upper()
            if re.search(r"(?<!UN)STABLE", title_up) and cf.VER.search(it["title"]):
                new_stable = True
            posts_out.append({"title": it["title"], "date": date.fromtimestamp(it["date"]).isoformat(),
                              "url": it["url"], "evidence": evidence})
        for doc_id, (n_lines, n_posts) in sorted(changelog_hits.items()):
            add(doc_id, f"{n_lines} patch-note line(s) across {n_posts} post(s) match", "changelog")
        if new_stable:
            for doc_id in emap["always_on_release"]:
                add(doc_id, "release bookkeeping: a new stable build was announced", "release")

    rows = sorted(queue.values(), key=lambda q: (-len(q["kinds"]), -len(q["reasons"]), q["id"]))
    for q in rows:
        q["kinds"] = sorted(q["kinds"])

    result = {
        "date": today.isoformat(),
        "pinned": {"b42_stable": pinned_b42, "b41_legacy": pinned_b41},
        "current": {"b42_stable": stable, "b41_legacy": legacy},
        "umbrella_drift": umbrella,
        "queue": rows,
        "posts": posts_out,
        "forum_topics_to_read": sorted(forum_topics),
        "notes": notes,
    }

    # ---- render
    L = [f"# Re-queue report - {today.isoformat()}", "",
         f"Pinned: B42 stable {pinned_b42}, B41 legacy {pinned_b41}. "
         f"Current announced: B42 stable {stable}, B41 legacy {legacy}.", ""]
    for n in notes:
        L.append(f"> Note: {n}")
    if notes:
        L.append("")
    if umbrella:
        L += ["## Umbrella drift", ""] + [f"- {u}" for u in umbrella] + [""]
    if rows:
        L += [f"## Documents to re-verify ({len(rows)})", "", "| Document | Signals | Why |", "|---|---|---|"]
        for q in rows:
            L.append(f"| `{q['id']}` | {', '.join(q['kinds'])} | {'; '.join(q['reasons'])[:300]} |")
        L.append("")
    else:
        L += ["## Documents to re-verify", "", "None: every document is current against the pins and the feed.", ""]
    if posts_out:
        L += ["## Changelog evidence (heuristic, read the lines)", ""]
        for p in posts_out:
            L += [f"### {p['title']} ({p['date']})", "", p["url"], ""]
            for doc_id, e in sorted(p["evidence"].items(), key=lambda kv: -kv[1]["lines"]):
                L.append(f"- `{doc_id}` - {e['lines']} matching line(s)")
                for ex in e["examples"]:
                    L.append(f"  - [{', '.join(ex['terms'][:3])}] {ex['line']}")
            L.append("")
    if forum_topics:
        L += ["## Forum topics to read in a browser (the forum blocks bots)", ""]
        L += [f"- {u}" for u in sorted(forum_topics)] + [""]
    report = "\n".join(L)

    print(report)
    if args.markdown:
        Path(args.markdown).write_text(report + "\n", encoding="utf-8")
    if args.json:
        Path(args.json).write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return 2 if rows else 0


if __name__ == "__main__":
    sys.exit(main())
