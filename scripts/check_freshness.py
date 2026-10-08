#!/usr/bin/env python3
"""
Freshness watcher: compare the KB's pinned game builds against the Steam news
feed for app 108600 (official TIS announcements).

Reports the newest announced STABLE / UNSTABLE / LEGACY build versions and
flags drift versus sources/pins.json. Network required unless --feed-file is
given; stdlib only. Also importable: requeue.py reuses fetch_feed(),
latest_builds() and pinned_builds().

Exit 0 = pins current, 2 = drift detected (informational for CI), 1 = fetch error.

Usage:  python scripts/check_freshness.py [--count 40] [--feed-file FEED.json] [--pins PINS.json]
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
        "?appid=108600&count={count}&maxlength=0&format=json&feeds=steam_community_announcements")
VER = re.compile(r"(\d{2})\.(\d{1,2})(?:\.(\d{1,2}))?")


def vkey(v: str) -> tuple:
    return tuple(int(x) for x in v.split("."))


def fetch_feed(count: int = 40, feed_file: str | None = None) -> list[dict]:
    """Return newsitems (newest first not guaranteed). Raises on network error."""
    if feed_file:
        data = json.loads(Path(feed_file).read_text(encoding="utf-8"))
    else:
        req = urllib.request.Request(FEED.format(count=count),
                                     headers={"User-Agent": "pz-kb-freshness/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
    return data["appnews"]["newsitems"]


def latest_builds(items: list[dict]) -> dict:
    """Newest announced version per channel: {chan: (version, iso_date, url)}."""
    latest: dict = {"STABLE": None, "LEGACY": None, "UNSTABLE": None}
    for it in sorted(items, key=lambda i: i["date"], reverse=True):
        # Compound titles: "42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes ..."
        for part in re.split(r"\s*&\s*", it["title"]):
            m = VER.search(part)
            if not m:
                continue
            ver = ".".join(g for g in m.groups() if g is not None)
            chan = channel_of(part)
            if chan and (latest[chan] is None or vkey(ver) > vkey(latest[chan][0])):
                latest[chan] = (ver, date.fromtimestamp(it["date"]).isoformat(), it["url"])
    return latest


def channel_of(title_part: str) -> str | None:
    """STABLE / UNSTABLE / LEGACY for one title fragment ('UNSTABLE' contains 'STABLE')."""
    up = title_part.upper()
    if "UNSTABLE" in up:
        return "UNSTABLE"
    if "LEGACY" in up:
        return "LEGACY"
    if "STABLE" in up:
        return "STABLE"
    return None


def pinned_builds(pins: dict) -> tuple[str, str]:
    """(pinned B42 stable, primary-attested B41 legacy) version strings."""
    b42 = pins["game_builds"]["B42_stable"]
    attested = pins["game_builds"]["B41_legacy"].get("latest_primary_attested", "")
    m = VER.search(attested)
    return b42, (m.group(0) if m else "?")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--count", type=int, default=40)
    ap.add_argument("--feed-file", help="read a saved ISteamNews JSON instead of the network")
    ap.add_argument("--pins", default="sources/pins.json")
    args = ap.parse_args()
    try:
        items = fetch_feed(args.count, args.feed_file)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR fetching Steam news: {e}", file=sys.stderr)
        return 1

    latest = latest_builds(items)
    pins = json.loads(Path(args.pins).read_text(encoding="utf-8"))
    pinned_b42, pinned_b41 = pinned_builds(pins)

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
        print("-> re-queue docs whose game_versions_verified predates the new build "
              "(python scripts/requeue.py).")
        return 2
    print("Pins current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
