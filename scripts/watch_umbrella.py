#!/usr/bin/env python3
"""
Umbrella watcher: compare the Umbrella pins in sources/pins.json with the
upstream repository's release tags (git ls-remote, no clone).

Flags two kinds of drift:
  * NEWER   - upstream has a release tag newer than the pinned tag for a build
              (B42 = major 42, B41 = major 41);
  * MOVED   - the pinned release tag now points at a different commit than the
              pinned commit (this happened to 42.20.0 two days after it was
              pinned; documents cite commits, so they stay valid, but the pin
              record should be updated and the change reviewed).

Exit 0 = current, 2 = drift, 1 = could not read the remote.
Needs git and network unless --tags-file (saved `git ls-remote --tags` output)
is given. Stdlib only. Importable: requeue.py reuses check().

Usage:  python scripts/watch_umbrella.py [--tags-file FILE] [--pins PINS.json]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

TAG_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def read_tags(tags_file: str | None, repo: str) -> dict[str, str]:
    """Return {tag: commit_sha}, preferring peeled (^{}) commits for annotated tags."""
    if tags_file:
        text = Path(tags_file).read_text(encoding="utf-8")
    else:
        out = subprocess.run(["git", "ls-remote", "--tags", repo],
                             capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            raise RuntimeError(out.stderr.strip() or "git ls-remote failed")
        text = out.stdout
    tags: dict[str, str] = {}
    peeled: dict[str, str] = {}
    for line in text.splitlines():
        sha, _, ref = line.partition("\t")
        if not ref.startswith("refs/tags/"):
            continue
        name = ref[len("refs/tags/"):]
        if name.endswith("^{}"):
            peeled[name[:-3]] = sha
        else:
            tags[name] = sha
    tags.update(peeled)
    return tags


def check(pins: dict, tags: dict[str, str]) -> list[str]:
    """Return a list of human-readable drift findings (empty = current)."""
    findings: list[str] = []
    for build, pin in pins["umbrella"]["pins"].items():
        if build not in ("B41", "B42"):
            continue
        tag, commit = pin["release_tag"], pin["commit"]
        major = int(tag.split(".")[0])
        current = tags.get(tag)
        if current is None:
            findings.append(f"{build}: pinned tag {tag} no longer exists upstream")
        elif current != commit:
            findings.append(f"{build}: tag {tag} MOVED - now {current[:7]}, pinned {commit[:7]}")
        newer = sorted((t for t in tags if TAG_RE.match(t) and int(t.split(".")[0]) == major
                        and tuple(map(int, t.split("."))) > tuple(map(int, tag.split(".")))),
                       key=lambda t: tuple(map(int, t.split("."))))
        if newer:
            findings.append(f"{build}: newer upstream tag(s) {', '.join(newer)} (pinned {tag})")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tags-file")
    ap.add_argument("--pins", default="sources/pins.json")
    args = ap.parse_args()
    pins = json.loads(Path(args.pins).read_text(encoding="utf-8"))
    try:
        tags = read_tags(args.tags_file, pins["umbrella"]["repo"] + ".git")
    except Exception as e:  # noqa: BLE001
        print(f"ERROR reading Umbrella tags: {e}", file=sys.stderr)
        return 1
    numeric = sorted((t for t in tags if TAG_RE.match(t)), key=lambda t: tuple(map(int, t.split("."))))
    print(f"Upstream release tags: {len(numeric)}; newest {numeric[-1] if numeric else '-'}")
    for build, pin in pins["umbrella"]["pins"].items():
        if build in ("B41", "B42"):
            print(f"Pinned {build}: {pin['release_tag']} @ {pin['commit'][:7]}")
    findings = check(pins, tags)
    for f in findings:
        print("DRIFT:", f)
    if findings:
        print("-> re-pin with scripts/extract_api_index.py after reviewing the change.")
        return 2
    print("Umbrella pins current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
