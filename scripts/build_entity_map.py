#!/usr/bin/env python3
"""
Build the changelog-to-document entity map -> exports/entity-map.json.

The map answers "which documents does this patch-note line probably affect?".
Two layers, merged at match time by scripts/requeue.py:

  aliases      curated phrase -> document ids from sources/entity_aliases.json
               (human judgement; ids are validated against docs/)
  identifiers  derived mechanically from the documents themselves: code spans
               that look like game identifiers (CamelCase names, Class:member,
               Events.X, ...) -> the documents that mention them. An identifier
               that appears in more than MAX_DOCS documents is too generic to
               locate anything and is dropped.

Deterministic and offline: the output depends only on docs/ and the alias
file, so CI can regenerate it and fail on stale committed output.
Stdlib only. Importable: requeue.py reuses load_map() and match_line().

Usage:  python scripts/build_entity_map.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DOCS = Path("docs")
ALIASES = Path("sources/entity_aliases.json")
OUT = Path("exports/entity-map.json")
MAX_DOCS = 6
SPAN_RE = re.compile(r"`([^`\n]{3,60})`")
IDENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*(?:[.:][A-Za-z_][A-Za-z0-9_]*)*")
HOSTNAME = re.compile(r"\.(com|net|org|gg|io|dev|tv|co|uk|app|info)$", re.I)
FILE_EXT = re.compile(r"\.(md|py|json|jsonc|txt|ini|lua|yml|yaml|sh|jar|log|png|csv|jsonl|mmd|pdf|zip)$", re.I)
FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---", re.S)


def doc_files() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.md") if p.name != "index.md")


def doc_id(text: str) -> str | None:
    m = FM_RE.match(text)
    if not m:
        return None
    i = re.search(r"^id:\s*(\S+)", m.group(1), re.M)
    return i.group(1) if i else None


def derive_identifiers(texts: dict[str, str]) -> dict[str, list[str]]:
    seen: dict[str, set[str]] = {}
    for did, text in texts.items():
        body = FM_RE.sub("", text, count=1)
        for span in SPAN_RE.findall(body):
            span = span.strip()
            if not IDENT_RE.fullmatch(span) or FILE_EXT.search(span) or HOSTNAME.search(span):
                continue
            # needs to look like a game/API identifier, not an ordinary word
            if not (re.search(r"[A-Z]", span[1:]) or "." in span or ":" in span):
                continue
            terms = {span}
            head = re.split(r"[.:]", span)[0]
            if head != span and len(head) >= 5 and re.search(r"[A-Z]", head[1:]):
                terms.add(head)  # IsoPlayer from IsoPlayer:getX
            for t in terms:
                if 5 <= len(t) <= 50:
                    seen.setdefault(t, set()).add(did)
    return {t: sorted(ids) for t, ids in sorted(seen.items()) if len(ids) <= MAX_DOCS}


def build() -> dict:
    texts: dict[str, str] = {}
    for p in doc_files():
        t = p.read_text(encoding="utf-8")
        did = doc_id(t)
        if did:
            texts[did] = t
    cfg = json.loads(ALIASES.read_text(encoding="utf-8"))
    problems = []
    for term, ids in cfg["aliases"].items():
        problems += [f"alias '{term}' -> unknown doc '{i}'" for i in ids if i not in texts]
    problems += [f"_always_on_release -> unknown doc '{i}'" for i in cfg["_always_on_release"] if i not in texts]
    if problems:
        raise SystemExit("entity_aliases.json problems:\n  " + "\n  ".join(problems))
    return {
        "_generated_by": "scripts/build_entity_map.py - do not edit by hand",
        "documents": len(texts),
        "always_on_release": sorted(cfg["_always_on_release"]),
        "aliases": {k: sorted(v) for k, v in sorted(cfg["aliases"].items())},
        "identifiers": derive_identifiers(texts),
    }


# ---------- matching helpers (used by requeue.py) ----------

def alias_regex(term: str) -> re.Pattern:
    stem = term.endswith("*")
    core = re.escape(term.rstrip("*")).replace(r"\ ", r"\s+")
    tail = r"\w*" if stem else r"s?(?!\w)"
    return re.compile(r"(?<!\w)" + core + tail, re.I)


def ident_regex(term: str) -> re.Pattern:
    return re.compile(r"(?<![A-Za-z0-9_])" + re.escape(term) + r"(?![A-Za-z0-9_])")


def load_map(path: Path = OUT) -> dict:
    m = json.loads(path.read_text(encoding="utf-8"))
    m["_alias_rx"] = [(t, alias_regex(t), ids) for t, ids in m["aliases"].items()]
    m["_ident_rx"] = [(t, ident_regex(t), ids) for t, ids in m["identifiers"].items()]
    return m


URL_RE = re.compile(r"https?://\S+")


def match_line(line: str, m: dict) -> dict[str, set[str]]:
    """Return {doc_id: {matched terms}} for one line of text (URLs are ignored)."""
    line = URL_RE.sub(" ", line)
    hits: dict[str, set[str]] = {}
    for term, rx, ids in m["_alias_rx"]:
        if rx.search(line):
            for i in ids:
                hits.setdefault(i, set()).add(term)
    for term, rx, ids in m["_ident_rx"]:
        if rx.search(line):
            for i in ids:
                hits.setdefault(i, set()).add(term)
    return hits


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}: {data['documents']} documents, {len(data['aliases'])} aliases, "
          f"{len(data['identifiers'])} derived identifiers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
