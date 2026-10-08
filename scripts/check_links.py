#!/usr/bin/env python3
"""
Link checker for the Project Zomboid knowledge base.

Extracts every http(s) URL from the Markdown files (docs/ + the control files
that carry source links) and checks each with an HTTP request via `curl`,
following redirects. Reports any URL that does not return a 2xx/3xx status.

Some official sites (e.g. consilium.europa.eu) bot-block automated agents with
403 while serving the page normally in a browser; these hosts are listed in
BOT_BLOCK_HOSTS and reported as WARN rather than FAIL.

Exit code 0 = all reachable (ignoring allowlisted hosts), 1 = dead link(s).
Network access required. Intended for local runs and scheduled CI, not per-PR.

Usage:  python scripts/check_links.py [path ...]   (defaults to docs + registries)
"""
from __future__ import annotations

import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s>\]}\"'<]+")
TRAILING = ".,;:"


def clean_url(raw: str) -> str:
    """Trim trailing punctuation and any unbalanced closing parens.

    Bare URLs with balanced parens (e.g. Wikipedia '..._(European_Union)') are
    kept intact; a trailing ')' that merely closes Markdown/prose is stripped.
    """
    url = raw.rstrip(TRAILING)
    while url.endswith(")") and url.count(")") > url.count("("):
        url = url[:-1].rstrip(TRAILING)
    return url

# Hosts known to serve pages fine in-browser but 403 automated user-agents.
BOT_BLOCK_HOSTS = {
    # Sites that legitimately 403/challenge automated checkers but whose URLs
    # are real. Reported as WARN, not FAIL — a human should eyeball these
    # periodically.
    "projectzomboid.com",          # official blog — known bot detection
    "www.projectzomboid.com",
    "theindiestone.com",           # official forums — intermittent challenges
    "www.theindiestone.com",
    "store.steampowered.com",      # regional/age gates confuse plain GETs
    "steamcommunity.com",          # workshop/guide pages sometimes challenge
    "discord.com",                 # invite/channel links never 200 for bots
    "discord.gg",
    "map.projectzomboid.com",      # official community map; 403s non-browser agents
    "support.discord.com",          # Discord help centre; 403s non-browser agents
    "pzwiki.net",                  # intermittent Cloudflare challenge on API/page fetches
    "developer.valvesoftware.com", # Valve dev wiki; challenges bots
    "pzfans.com",                  # community site; 403s datacenter IPs (GitHub runners)
    "socialcounts.org",            # third-party subscriber-count site; 403s datacenter IPs
    "legionhosting.net",           # hosting-company KB; 403s bots (corroborate-only source)
}

DEFAULT_PATHS = [
    "docs",
    "SOURCE_REGISTRY.md",
    "GLOSSARY.md",
    "MASTER_INDEX.md",
]

UA = "Mozilla/5.0 (kb-link-checker)"


def gather_urls(paths: list[str]) -> dict[str, list[str]]:
    """Return {url: [files it appears in]}."""
    urls: dict[str, list[str]] = {}
    files: list[Path] = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            files.extend(sorted(pp.rglob("*.md")))
        elif pp.is_file():
            files.append(pp)
    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in URL_RE.findall(text):
            url = clean_url(m)
            urls.setdefault(url, [])
            if f.as_posix() not in urls[url]:
                urls[url].append(f.as_posix())
    return urls


def host_of(url: str) -> str:
    return url.split("/", 3)[2] if "://" in url else ""


def _curl(url: str) -> int:
    try:
        out = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "-L", "--max-time", "40", "--retry", "2", "-A", UA, url],
            capture_output=True, text=True, timeout=140,
        )
        return int(out.stdout.strip() or 0)
    except Exception:
        return 0


def check(url: str) -> tuple[str, int]:
    """Return (url, http_status). 0 means curl failed to connect.

    Uses GET (not HEAD): several official servers (e.g. nvlpubs.nist.gov) answer
    404 to HEAD while serving 200 on GET, so HEAD produces false negatives. One
    connect-failure (0) is retried once more before being reported.
    """
    code = _curl(url)
    if code == 0:
        code = _curl(url)
    return url, code


def main() -> int:
    paths = sys.argv[1:] or DEFAULT_PATHS
    urls = gather_urls(paths)
    if not urls:
        print("No URLs found.", file=sys.stderr)
        return 2

    print(f"Checking {len(urls)} unique URL(s)...\n")
    results: dict[str, int] = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, code in pool.map(check, sorted(urls)):
            results[url] = code

    dead, warn = [], []
    for url in sorted(results):
        code = results[url]
        ok = 200 <= code < 400
        if ok:
            continue
        if host_of(url) in BOT_BLOCK_HOSTS:
            warn.append((url, code))
        else:
            dead.append((url, code))

    for url, code in warn:
        print(f"WARN  {code}  {url}  (bot-block allowlist; verify in-browser)")
    for url, code in dead:
        print(f"FAIL  {code}  {url}")
        for f in urls[url]:
            print(f"          in {f}")

    print("-" * 60)
    live = sum(1 for c in results.values() if 200 <= c < 400)
    print(f"{live}/{len(results)} live; {len(warn)} allowlisted warn; {len(dead)} dead")
    return 1 if dead else 0


if __name__ == "__main__":
    raise SystemExit(main())
