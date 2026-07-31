#!/usr/bin/env python3
"""
Extract the server-setting schema from the two Admin reference documents.

Parses the load-bearing key tables (rows whose first cell is a single code
span) from admins-server-ini-reference.md -> "ini" and
admins-sandboxvars-reference.md -> "sandbox", writing
sources/schemas/server-settings.json. Run by the orchestrator whenever a
reference doc revision changes; the schema then powers
scripts/check_server_settings.py for every other Admin document.

Stdlib only.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SOURCES = {
    "ini": Path("docs/admins/admins-server-ini-reference.md"),
    "sandbox": Path("docs/admins/admins-sandboxvars-reference.md"),
}
OUT = Path("sources/schemas/server-settings.json")
KEY_ROW_RE = re.compile(r"^\|\s*`([A-Za-z0-9_.]+)`\s*\|", re.MULTILINE)


def main() -> int:
    schema: dict[str, dict] = {}
    for section, path in SOURCES.items():
        text = path.read_text(encoding="utf-8")
        keys = sorted(set(KEY_ROW_RE.findall(text)))
        schema[section] = {k: {} for k in keys}
        print(f"{section}: {len(keys)} key(s) from {path.as_posix()}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(schema, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
