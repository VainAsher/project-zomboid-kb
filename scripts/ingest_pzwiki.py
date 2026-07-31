#!/usr/bin/env python3
"""
Ingest pzwiki pages as plain-text snapshots for the license-hygiene gate.

Fetches each page's rendered HTML via the MediaWiki API (action=parse),
strips tags, and writes sources/pzwiki/<safe-title>.txt with a short
provenance header (title, revid, URL, fetch date). A manifest of
title -> revid is written to sources/pzwiki/manifest.json.

IMPORTANT: the snapshot text is CC BY-NC-SA 3.0 content. It is kept as a
LOCAL verification corpus only and is gitignored — never commit or publish
it. The committed manifest records provenance without redistributing prose.

Missing pages are logged and skipped. Requests are sequential with a small
delay (be polite). Stdlib only.

Usage:  python scripts/ingest_pzwiki.py [--pages pages.txt]
        (default page list is embedded below)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

API = "https://pzwiki.net/w/api.php"
OUT = Path("sources/pzwiki")
UA = "pz-kb-license-corpus/1.0 (fact-verification snapshots; contact: repo owner)"

DEFAULT_PAGES = [
    "Build 41", "Build 42", "Build 42.20.0", "Build 41.60", "Build 42.13.0",
    "Moodle", "Skill", "Trait", "Occupation", "Knox Country", "Knox Event",
    "Project Zomboid", "PZwiki:Copyrights",
    "Dedicated server", "Server settings", "Startup parameters",
    "Multiplayer", "Admin commands",
    "Mod structure", "Mod.info", "ModOptions", "Mod Options", "Scripts",
    "JavaDocs", "Unofficial JavaDocs (Build 42)", "Uploading mods",
    "Mapping tools (official)", "Spiffo's Workshop",
    "Lua (API)", "Lua (language)",
    "Farming", "Agriculture", "First Aid", "Fishing", "Foraging",
    "Carpentry", "Cooking", "Vehicle", "Mechanics",
    "Knox Infection", "Health", "Skill book", "Custom Sandbox", "Crafting",
    "Fluid", "Fluid container", "Running", "Sandbox options", "Tech Support",
    "Animals", "Husbandry", "Animal care", "Butchering", "Tracking",
    "Blacksmithing", "Knapping", "Masonry", "Carving", "Pottery",
    "Glassmaking", "Welding", "Brewing",
    "Muldraugh", "West Point", "Riverside", "Rosewood", "Louisville",
    "Brandenburg", "Ekron", "Irvington", "Echo Creek",
]


class TextExtractor(HTMLParser):
    SKIP = {"script", "style"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)

    def text(self) -> str:
        raw = " ".join(self.parts)
        return re.sub(r"\s+", " ", raw).strip()


def api_get(params: dict) -> dict:
    qs = urllib.parse.urlencode({**params, "format": "json"})
    req = urllib.request.Request(f"{API}?{qs}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def safe_name(title: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", title).strip("_") or "page"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pages", help="optional file with one page title per line")
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()

    pages = DEFAULT_PAGES
    if args.pages:
        pages = [ln.strip() for ln in Path(args.pages).read_text(
            encoding="utf-8").splitlines() if ln.strip()]

    OUT.mkdir(parents=True, exist_ok=True)
    # Merge into the existing manifest so partial (--pages) runs never drop
    # provenance for pages ingested earlier.
    manifest_path = OUT / "manifest.json"
    manifest: dict[str, dict] = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    ok = skipped = 0
    for title in pages:
        try:
            data = api_get({"action": "parse", "page": title,
                            "prop": "text|revid", "redirects": 1})
        except Exception as e:
            print(f"skip  {title}  (fetch error: {e})")
            skipped += 1
            time.sleep(args.delay)
            continue
        if "error" in data:
            print(f"skip  {title}  ({data['error'].get('code')})")
            skipped += 1
            time.sleep(args.delay)
            continue
        parse = data["parse"]
        html = parse["text"]["*"]
        ex = TextExtractor()
        ex.feed(html)
        text = ex.text()
        revid = parse.get("revid")
        real_title = parse.get("title", title)
        fname = OUT / f"{safe_name(real_title)}.txt"
        header = (f"# pzwiki snapshot | title: {real_title} | revid: {revid} | "
                  f"fetched: {date.today().isoformat()} | CC BY-NC-SA 3.0 | "
                  f"LOCAL VERIFICATION CORPUS - DO NOT REDISTRIBUTE\n")
        fname.write_text(header + text + "\n", encoding="utf-8")
        manifest[real_title] = {"revid": revid, "file": fname.name,
                                "fetched": date.today().isoformat()}
        print(f"ok    {real_title}  (revid {revid}, {len(text):,} chars)")
        ok += 1
        time.sleep(args.delay)

    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print("-" * 60)
    print(f"Ingested {ok} page(s), skipped {skipped}; manifest written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
