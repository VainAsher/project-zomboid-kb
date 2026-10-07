#!/usr/bin/env python3
"""
API-existence gate for Modder-track documents.

Every API symbol a Modders document names in a code span must exist in the
pinned Umbrella index for the document's build(s)
(sources/schemas/api-index-<B41|B42>.json, built by extract_api_index.py).

Checked code-span shapes (conservative; prose code spans that match none are
ignored):
  Events.Name          -> Name must be a known event
  Class:method / Class.method(...)  -> only when Class is a known class in
                          the index; method must be a member of Class or of
                          an ancestor.
A symbol is accepted if it exists in ANY build the document's `build:` tag
covers (both -> B41 or B42). A symbol line tagged *(B41)* / *(B42)* inline is
checked only against that build.

Unarmed (passes with a note) until at least one index file exists, and only
Category Modders documents are inspected. Offline, stdlib only.
Exit 0 = clean/unarmed; 1 = unknown symbol(s).

Usage:  python scripts/check_api_exists.py [FILE ...]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMAS = Path("sources/schemas")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SPAN_RE = re.compile(r"`([^`\n]+)`")
EVENT_RE = re.compile(r"^Events\.([A-Za-z0-9_]+)")
MEMBER_RE = re.compile(r"^([A-Za-z0-9_]+)[:.]([A-Za-z0-9_]+)\s*(?:\(.*)?$")


def load_indexes() -> dict:
    out = {}
    for b in ("B41", "B42"):
        p = SCHEMAS / f"api-index-{b}.json"
        if p.exists():
            out[b] = json.loads(p.read_text(encoding="utf-8"))
    return out


def has_member(idx: dict, cls: str, member: str, seen=None) -> bool:
    seen = seen or set()
    if cls in seen or cls not in idx["classes"]:
        return False
    seen.add(cls)
    ent = idx["classes"][cls]
    return member in ent["members"] or any(has_member(idx, p, member, seen) for p in ent["parents"])


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    indexes = load_indexes()
    if not indexes:
        print("API-EXISTENCE GATE: no api-index files yet — passes trivially.")
        return 0

    files = [Path(p) for p in args.paths] or [
        f for f in sorted(Path(args.docs).rglob("*.md")) if f.name != "index.md"]
    bad = 0
    checked = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        if not m or not re.search(r"^category:\s*Modders\s*$", m.group(1), re.MULTILINE):
            continue
        bm = re.search(r"^build:\s*(\S+)", m.group(1), re.MULTILINE)
        doc_build = bm.group(1) if bm else "both"
        issues = []
        for n, line in enumerate(text.splitlines(), 1):
            builds = {"B41": ["B41"], "B42": ["B42"]}.get(doc_build, ["B41", "B42"])
            if "(B41)" in line and "(B42)" not in line:
                builds = ["B41"]
            elif "(B42)" in line and "(B41)" not in line:
                builds = ["B42"]
            builds = [b for b in builds if b in indexes]
            if not builds:
                continue
            for span in SPAN_RE.findall(line):
                span = span.strip()
                ev = EVENT_RE.match(span)
                if ev:
                    checked += 1
                    if not any(ev.group(1) in indexes[b]["events"] for b in builds):
                        issues.append((n, span, "unknown event"))
                    continue
                mm = MEMBER_RE.match(span)
                if mm and any(mm.group(1) in indexes[b]["classes"] for b in builds):
                    checked += 1
                    cls, member = mm.groups()
                    if not any(has_member(indexes[b], cls, member) for b in builds):
                        issues.append((n, span, f"{cls} has no member {member}"))
        if issues:
            bad += len(issues)
            print(f"FAIL  {f}")
            for n, span, why in issues:
                print(f"      line {n}: `{span}` — {why}")
        else:
            print(f"ok    {f}")
    if bad:
        print(f"API-EXISTENCE GATE FAILED: {bad} unknown symbol(s)")
        return 1
    print(f"API-EXISTENCE GATE CLEAN ({checked} symbol reference(s) checked, "
          f"indexes: {', '.join(sorted(indexes))})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
