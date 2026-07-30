#!/usr/bin/env python3
"""
Genre-discipline auditor for the Project Zomboid reference knowledge base.

The house rule is "never let a judgement (or hearsay) wear the costume of a
fact". This auditor makes the rule *mechanical* so quality does not depend on
model judgement:

  1. The evidence section "Reference" actually cites — it contains at least
     one [n] citation marker.
  2. "B41 vs B42 Delta" either cites its change claims ([n] marker) or
     explicitly states "Not applicable" (single-build documents).
  3. "Community Notes & Unverified Claims" is the ONLY place uncited community
     claims may live, and it is disciplined: every claim block carries the
     three parts — Claim / Why unverified / Confidence — and each Confidence
     names High | Medium | Low. A section with prose but no labelled claim
     blocks (and not marked "None") is flagged.

Read-only. Exit 0 by default (report); pass --strict to fail (exit 1) on any
finding so it can gate CI. Runs over docs/**/*.md or specific files.

Usage:  python scripts/audit_genre.py [--strict] [FILE ...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
MARKER_RE = re.compile(r"\[(\d+)\]")
CONF_RE = re.compile(r"\b(High|Medium|Low)\b", re.IGNORECASE)
NA_RE = re.compile(r"not applicable", re.IGNORECASE)
NONE_RE = re.compile(r"^\s*(none|none\.|no unverified claims\.?)\s*$",
                     re.IGNORECASE | re.MULTILINE)

REFERENCE_SECTION = "Reference"
DELTA_SECTION = "B41 vs B42 Delta"
CLAIMS_SECTION = "Community Notes & Unverified Claims"

# A claim block is introduced by "## Claim N ..." (canonical) or a
# "**Claim N — ...**" bold header (legacy). Format-agnostic on purpose.
CLAIM_HEADER_RE = re.compile(r"^\s*(?:##\s*Claim\b|\*\*\s*Claim\s+\d)",
                             re.IGNORECASE | re.MULTILINE)

# Each claim must carry these discipline-bearing bullets. *italic* or
# **bold** labels both accepted.
CLAIM_PARTS = {
    "Claim":          re.compile(r"^\s*[-*]\s*\*{1,2}\s*Claim\s*:", re.IGNORECASE | re.MULTILINE),
    "Why unverified": re.compile(r"^\s*[-*]\s*\*{1,2}\s*Why[ -]?unverified\s*:", re.IGNORECASE | re.MULTILINE),
    "Confidence":     re.compile(r"^\s*[-*]\s*\*{1,2}\s*Confidence\s*:", re.IGNORECASE | re.MULTILINE),
}
CONF_BULLET_RE = re.compile(r"^\s*[-*]\s*\*{1,2}\s*Confidence\s*:.*$",
                            re.IGNORECASE | re.MULTILINE)


def sections(body: str) -> dict[str, str]:
    """Map each top-level (#) heading to the text until the next # heading."""
    out: dict[str, str] = {}
    parts = re.split(r"^# (.+?)\s*$", body, flags=re.MULTILINE)
    # parts = [pre, h1, text, h1, text, ...]
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1] if i + 1 < len(parts) else ""
    return out


def audit_file(path: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    body = text[m.end():] if m else text
    secs = sections(body)

    # 1. the core evidence section must cite
    ref = secs.get(REFERENCE_SECTION)
    if ref is None:
        findings.append(f"missing evidence section: '{REFERENCE_SECTION}'")
    elif not MARKER_RE.search(ref):
        findings.append(f"evidence section '{REFERENCE_SECTION}' contains no "
                        "[n] citation marker")

    # 2. delta section must cite its change claims or be explicitly N/A
    delta = secs.get(DELTA_SECTION)
    if delta is None:
        findings.append(f"missing section: '{DELTA_SECTION}'")
    elif not MARKER_RE.search(delta) and not NA_RE.search(delta):
        findings.append(f"'{DELTA_SECTION}' has neither a [n] citation nor an "
                        "explicit 'Not applicable' statement")

    # 3. community-claims quarantine discipline
    claims_body = secs.get(CLAIMS_SECTION)
    if claims_body is None:
        findings.append(f"missing section: '{CLAIMS_SECTION}'")
        return findings

    n_claims = len(CLAIM_HEADER_RE.findall(claims_body))
    substantive = claims_body.strip() and not NONE_RE.search(claims_body)
    if n_claims == 0:
        if substantive and len(claims_body.strip()) > 200:
            findings.append(f"'{CLAIMS_SECTION}' has prose but no labelled "
                            "claim blocks (expected '## Claim N …' or "
                            "'**Claim N — …**', or the literal 'None.')")
        return findings

    # every claim must carry each part, so each part count >= n_claims
    for part, rx in CLAIM_PARTS.items():
        c = len(rx.findall(claims_body))
        if c < n_claims:
            findings.append(f"{n_claims} claim(s) but only {c} '**{part}:**' "
                            f"bullet(s) — {n_claims - c} claim(s) missing "
                            f"their {part}")

    # each stated Confidence bullet must name High/Medium/Low
    for line in CONF_BULLET_RE.findall(claims_body):
        if not CONF_RE.search(line):
            findings.append(f"claim Confidence not High/Medium/Low: "
                            f"'{line.strip()[:40]}'")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    if args.paths:
        files = [Path(p) for p in args.paths]
    else:
        files = [f for f in sorted(Path(args.docs).rglob("*.md")) if f.name != "index.md"]

    total = 0
    for f in files:
        fnd = audit_file(f)
        if fnd:
            total += len(fnd)
            print(f"FLAG  {f.as_posix()}")
            for x in fnd:
                print(f"        - {x}")
        else:
            print(f"ok    {f.as_posix()}")

    print("-" * 60)
    if total:
        print(f"GENRE AUDIT: {total} finding(s) across {len(files)} file(s)")
        return 1 if args.strict else 0
    print(f"GENRE AUDIT CLEAN: {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
