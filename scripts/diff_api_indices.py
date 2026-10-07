#!/usr/bin/env python3
"""
Reproduce the B41 vs B42 symbol-diff totals cited in the Modders documents.

Reads sources/schemas/api-index-B41.json and api-index-B42.json and prints
class / event / global counts (total, shared, B41-only, B42-only). Offline,
stdlib only. Counts describe the Umbrella STUBS, not the game's behaviour.

Usage:  python scripts/diff_api_indices.py [--list-events]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

D = Path("sources/schemas")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--list-events", action="store_true")
    args = ap.parse_args()
    a = json.loads((D / "api-index-B41.json").read_text(encoding="utf-8"))
    b = json.loads((D / "api-index-B42.json").read_text(encoding="utf-8"))
    print(f"B41 @ {a['umbrella_commit'][:7]} ({a['release_tag']})   "
          f"B42 @ {b['umbrella_commit'][:7]} ({b['release_tag']})")
    for kind in ("classes", "events", "globals"):
        x, y = set(a[kind]), set(b[kind])
        print(f"{kind:8} B41={len(x):5} B42={len(y):5} shared={len(x & y):5} "
              f"B41-only={len(x - y):5} B42-only={len(y - x):5}")
    if args.list_events:
        x, y = set(a["events"]), set(b["events"])
        print("B41-only events:", ", ".join(sorted(x - y)))
        print("B42-only events:", ", ".join(sorted(y - x)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
