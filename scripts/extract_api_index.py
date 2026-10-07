#!/usr/bin/env python3
"""
Build the per-build API symbol index from an Umbrella checkout.

Reads the LuaLS stub library (library/**/*.lua) at the commit pinned in
sources/pins.json and writes sources/schemas/api-index-<BUILD>.json:

  {"build": "B42", "umbrella_commit": "...", "release_tag": "...",
   "classes": {"IsoPlayer": {"parents": [...], "members": [...]}},
   "events": ["OnTick", ...], "globals": ["AddWorldSound", ...]}

The index is the ground truth for scripts/check_api_exists.py. Offline,
stdlib only. The Umbrella checkout must already be at the pinned commit
(the script verifies HEAD when git is available).

Usage:  python scripts/extract_api_index.py --umbrella DIR --build B42
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CLASS_RE = re.compile(r"^---\s?@class\s+([A-Za-z0-9_.]+)\s*(?::\s*([^\n]*?))?(?:\s+--.*)?$")
METHOD_RE = re.compile(r"^function\s+([A-Za-z0-9_]+)([:.])([A-Za-z0-9_]+)\s*\(")
GLOBAL_RE = re.compile(r"^function\s+([A-Za-z0-9_]+)\s*\(")
LOCAL_TBL_RE = re.compile(r"^local\s+(__[A-Za-z0-9_]+)\s*=\s*\{\}")
FIELD_RE = re.compile(r"^---\s?@field\s+(?:public\s+|private\s+|protected\s+)?([A-Za-z0-9_]+)\??\s")
EVENT_RE = re.compile(r"^Events\.([A-Za-z0-9_]+)\s*=")
ASSIGN_RE = re.compile(r"^([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)\s*=")


def parse_file(path: Path, classes: dict, events: set, globals_: set) -> None:
    cur = None          # class currently being described
    local_alias = {}    # local table name -> class name
    pending = None
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.rstrip()
        m = CLASS_RE.match(line)
        if m:
            name, parents = m.group(1), m.group(2) or ""
            ent = classes.setdefault(name, {"parents": set(), "members": set()})
            ent["parents"].update(p.strip() for p in parents.split(",") if p.strip())
            pending = name
            continue
        f = FIELD_RE.match(line)
        if f and pending:
            classes[pending]["members"].add(f.group(1))
            continue
        lt = LOCAL_TBL_RE.match(line)
        if lt and pending:
            local_alias[lt.group(1)] = pending
            cur = pending
            pending = None
            continue
        mm = METHOD_RE.match(line)
        if mm:
            owner, _sep, member = mm.groups()
            owner = local_alias.get(owner, owner)
            classes.setdefault(owner, {"parents": set(), "members": set()})["members"].add(member)
            continue
        ev = EVENT_RE.match(line)
        if ev:
            events.add(ev.group(1))
            continue
        am = ASSIGN_RE.match(line)
        if am:
            classes.setdefault(am.group(1), {"parents": set(), "members": set()})["members"].add(am.group(2))
            continue
        gm = GLOBAL_RE.match(line)
        if gm:
            globals_.add(gm.group(1))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--umbrella", required=True)
    ap.add_argument("--build", required=True, choices=["B41", "B42"])
    ap.add_argument("--pins", default="sources/pins.json")
    ap.add_argument("--out-dir", default="sources/schemas")
    args = ap.parse_args()

    root = Path(args.umbrella)
    pin = json.loads(Path(args.pins).read_text(encoding="utf-8"))["umbrella"]["pins"][args.build]
    try:
        head = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
        if head != pin["commit"]:
            print(f"ERROR: checkout HEAD {head[:7]} != pinned {pin['commit'][:7]}", file=sys.stderr)
            return 1
    except (OSError, subprocess.CalledProcessError):
        print("WARN: could not verify git HEAD against the pin", file=sys.stderr)

    classes: dict = {}
    events: set = set()
    globals_: set = set()
    for p in sorted((root / "library").rglob("*.lua")):
        if not p.is_file():
            continue
        parse_file(p, classes, events, globals_)

    out = {
        "build": args.build,
        "umbrella_commit": pin["commit"],
        "release_tag": pin["release_tag"],
        "classes": {k: {"parents": sorted(v["parents"]), "members": sorted(v["members"])}
                    for k, v in sorted(classes.items())},
        "events": sorted(events),
        "globals": sorted(globals_),
    }
    dest = Path(args.out_dir) / f"api-index-{args.build}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{dest}: {len(out['classes'])} classes, {len(events)} events, {len(globals_)} globals")
    return 0


if __name__ == "__main__":
    sys.exit(main())
