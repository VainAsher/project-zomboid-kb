#!/usr/bin/env python3
"""
Server-setting existence gate for Admin-track documents.

Validates that every server.ini / SandboxVars key documented in an Admin
document exists in the reference schema at sources/schemas/server-settings.json
(shape: {"ini": {"KeyName": {"build": "both|B41|B42"}}, "sandbox": {...}}).

Convention checked: a documented key is a table row whose FIRST cell is a
single code span (e.g. "| `RCONPort` | ..."). Prose code spans are ignored —
only key tables are load-bearing. The schema is extracted by the orchestrator
from the frozen server.ini / SandboxVars reference documents (which document
keys straight from revision-pinned pzwiki + first-hand server files).

If the schema file does not exist yet, the gate passes trivially with a note
(same arming pattern as the license-hygiene gate).

Exit 0 = clean or unarmed; 1 = unknown key(s). Offline, stdlib only.

Usage:  python scripts/check_server_settings.py [FILE ...]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA = Path("sources/schemas/server-settings.json")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
KEY_ROW_RE = re.compile(r"^\|\s*`([A-Za-z0-9_.]+)`\s*\|", re.MULTILINE)
CATEGORY_RE = re.compile(r"^category:\s*Admins\s*$", re.MULTILINE)
# File names appear as first-cell code spans in file-layout tables; setting
# keys never carry a file extension, so these are excluded from the check.
FILENAME_RE = re.compile(r"\.(ini|lua|bat|sh|json|txt|md|jar|log)$", re.IGNORECASE)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    if not SCHEMA.exists():
        print(f"SERVER-SETTING GATE: no schema at {SCHEMA} yet — gate passes "
              "trivially (armed once the reference docs are frozen and the "
              "schema is extracted).")
        return 0

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    known = set(schema.get("ini", {})) | set(schema.get("sandbox", {}))

    if args.paths:
        files = [Path(p) for p in args.paths]
    else:
        files = [f for f in sorted(Path(args.docs).rglob("*.md"))
                 if f.name != "index.md"]

    total = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        if not (m and CATEGORY_RE.search(m.group(1))):
            continue  # only Admin-track docs carry key tables
        body = text[m.end():] if m else text
        unknown = sorted({k for k in KEY_ROW_RE.findall(body)
                          if k not in known and not FILENAME_RE.search(k)})
        if unknown:
            total += len(unknown)
            print(f"FAIL  {f.as_posix()}")
            for k in unknown:
                print(f"        - documented key not in schema: {k}")
        else:
            print(f"ok    {f.as_posix()}")

    print("-" * 60)
    if total:
        print(f"SERVER-SETTING GATE FAILED: {total} unknown key(s)")
        return 1
    print("SERVER-SETTING GATE CLEAN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
