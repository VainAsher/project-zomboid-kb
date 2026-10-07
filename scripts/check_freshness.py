#!/usr/bin/env python3
"""
Freshness watcher (Stage 3 seed): compare the KB's pinned game builds against
the Steam news feed for app 108600 (official TIS announcements).

Reports the newest announced STABLE / UNSTABLE / LEGACY build versions and
flags drift versus sources/pins.json. Network required; stdlib only.
Exit 0 = pins current, 2 = drift detected (informational for CI), 1 = fetch error.

Usage:  python scripts/check_freshness.py [--count 40]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

FEED = ("https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
        "?appid=108600&count={count}&maxlength=200&format=json&feeds=steam_community_announcements")
VER = re.compile(r"(\d{2})\.(\d{1,2})(?:\.(\d{1,2}))?")


def vkey(v: str) -> tuple:
    return tuple(int(x) for x in v.split("."))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--count", type=int, default=40)
    args = ap.parse_args()
    try:
        with urllib.request.urlopen(FEED.format(count=args.count), timeout=30) as r:
            items = json.load(r)["appnews"]["newsitems"]
    except Exception as e:  # noqa: BLE001
        print(f"ERROR fetching Steam news: {e}", file=sys.stderr)
        return 1

    latest = {"STABLE": None, "LEGACY": None, "UNSTABLE": None}
    for it in sorted(items, key=lambda i: i["date"], reverse=True):
        title = it["title"]
        # Split compound titles like "42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY ..."
        for part in re.split(r"\s*&\s*", title):
            m = VER.search(part)
            if not m:
                continue
            ver = ".".join(g for g in m.groups() if g is not None)
            for chan in latest:
                if chan in part.upper() and (latest[chan] is None or vkey(ver) > vkey(latest[chan][0])):
                    latest[chan] = (ver, date.fromtimestamp(it["date"]).isoformat(), it["url"])

    pins = json.loads(Path("sources/pins.json").read_text(encoding="utf-8"))
    pinned_b42 = pins["game_builds"]["B42_stable"]
    attested = pins["game_builds"]["B41_legacy"].get("latest_primary_attested", "")
    pinned_b41 = (VER.search(attested).group(0) if VER.search(attested) else "?")

    print("Newest announced (Steam news, app 108600):")
    for chan, v in latest.items():
        print(f"  {chan:<9} {v[0] + '  (' + v[1] + ')' if v else '-'}")
    print(f"Pinned: B42 stable {pinned_b42}; B41 legacy primary-attested {pinned_b41}")

    drift = []
    s = latest["STABLE"]
    if s and vkey(s[0]) > vkey(pinned_b42):
        drift.append(f"B42 stable {s[0]} ({s[1]}) is newer than pinned {pinned_b42}")
    l = latest["LEGACY"]
    if l and pinned_b41 != "?" and vkey(l[0]) > vkey(pinned_b41):
        drift.append(f"B41 legacy {l[0]} ({l[1]}) is newer than primary-attested {pinned_b41}")
    for d in drift:
        print("DRIFT:", d)
    if drift:
        print("-> re-queue docs whose game_versions_verified predates the new build.")
        return 2
    print("Pins current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
