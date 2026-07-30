#!/usr/bin/env python3
"""
Offline QA validator for the Project Zomboid knowledge base.

Runs four checks over every knowledge-base document:
  1. Front matter   — required YAML fields present; status/confidence/build/
                      category valid.
  2. Structure      — the 19 mandatory template sections present, in order.
  3. Citations      — [n] markers contiguous; every marker resolves to a
                      reference entry; every reference entry is cited in text.
  4. Version tag    — the hard build gate: `build` is B41 | B42 | both |
                      historic, and a `both` document must carry real content
                      in its "B41 vs B42 Delta" section.

Exit code 0 = all pass, 1 = any failure. No network access (fast; CI-friendly).
Only dependency is PyYAML.

Usage:  python scripts/validate.py [--docs docs] [FILE ...]
        python scripts/validate.py docs/players/skills-overview.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

# ── Rules ────────────────────────────────────────────────────────────────────

REQUIRED_FRONT_MATTER = [
    "id", "title", "version", "status", "confidence", "category",
    "topic", "build", "document_type", "created", "updated",
    "review_due", "sources_verified",
]
VALID_STATUS = {"draft", "in-review", "approved", "frozen", "superseded"}
VALID_CONFIDENCE = {"High", "Medium", "Low"}
# category = the audience track (or shared namespace) the document lives in.
VALID_CATEGORY = {"Modders", "Players", "Admins", "Creator", "Lore", "Meta"}
# build = which game build(s) the document's facts apply to. REQUIRED on every
# document — this is the version-tag gate.
VALID_BUILD = {"B41", "B42", "both", "historic"}
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# The 19 mandatory top-level (#) sections, in required order.
# Genre = reference: the evidence layer ("Reference", "B41 vs B42 Delta") is
# fully cited fact; community hearsay is quarantined in "Community Notes &
# Unverified Claims" so an uncited claim can never wear the costume of a fact.
REQUIRED_SECTIONS = [
    "Document Control", "Executive Summary", "Key Takeaways", "Purpose",
    "Scope", "Definitions", "Build Applicability", "Reference",
    "B41 vs B42 Delta", "Practical Guidance",
    "Common Pitfalls & Troubleshooting", "Community Notes & Unverified Claims",
    "Risks & Caveats", "Verification Steps", "Open Questions", "References",
    "Further Reading", "Related Documents", "Revision History",
]

DELTA_SECTION = "B41 vs B42 Delta"
DELTA_NA = re.compile(r"not applicable", re.IGNORECASE)

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
REF_DEF_RE = re.compile(r"^- \[(\d+)\]", re.MULTILINE)
MARKER_RE = re.compile(r"\[(\d+)\]")


# ── Checks ───────────────────────────────────────────────────────────────────

def check_front_matter(text: str) -> list[str]:
    errs: list[str] = []
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return ["missing or malformed YAML front matter (must start with '---')"]
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"front matter is not valid YAML: {e}"]
    if not isinstance(fm, dict):
        return ["front matter did not parse to a mapping"]

    for field in REQUIRED_FRONT_MATTER:
        if field not in fm or fm[field] in (None, ""):
            errs.append(f"front matter missing required field: {field}")

    status = fm.get("status")
    if status is not None and status not in VALID_STATUS:
        errs.append(f"invalid status '{status}' (allowed: {sorted(VALID_STATUS)})")

    conf = fm.get("confidence")
    if conf is not None and conf not in VALID_CONFIDENCE:
        errs.append(f"invalid confidence '{conf}' (allowed: {sorted(VALID_CONFIDENCE)})")

    cat = fm.get("category")
    if cat is not None and cat not in VALID_CATEGORY:
        errs.append(f"invalid category '{cat}' (allowed: {sorted(VALID_CATEGORY)})")

    build = fm.get("build")
    if build is not None and build not in VALID_BUILD:
        errs.append(f"invalid build '{build}' (allowed: {sorted(VALID_BUILD)})")

    ver = fm.get("version")
    if ver is not None and not SEMVER.match(str(ver)):
        errs.append(f"version '{ver}' is not semver (X.Y.Z)")

    for datefield in ("created", "updated", "review_due", "sources_verified"):
        val = fm.get(datefield)
        if val is not None and not ISO_DATE.match(str(val)):
            errs.append(f"{datefield} '{val}' is not an ISO date (YYYY-MM-DD)")
    return errs


def body_after_front_matter(text: str) -> str:
    m = FRONT_MATTER_RE.match(text)
    return text[m.end():] if m else text


def front_matter_build(text: str) -> str | None:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None
    return fm.get("build") if isinstance(fm, dict) else None


def sections_map(body: str) -> dict[str, str]:
    """Map each top-level (#) heading to the text until the next # heading."""
    out: dict[str, str] = {}
    parts = re.split(r"^# (.+?)\s*$", body, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1] if i + 1 < len(parts) else ""
    return out


def check_structure(body: str) -> list[str]:
    found = H1_RE.findall(body)
    missing = [s for s in REQUIRED_SECTIONS if s not in found]
    errs = [f"missing required section: '{s}'" for s in missing]

    # Order check over the sections that ARE present.
    present_in_doc = [h for h in found if h in REQUIRED_SECTIONS]
    expected_order = [s for s in REQUIRED_SECTIONS if s in found]
    if present_in_doc != expected_order:
        errs.append(
            "sections out of order: got "
            f"{present_in_doc} expected {expected_order}"
        )
    return errs


def check_version_tag(text: str, body: str) -> list[str]:
    """The hard build gate: `both` documents must document the actual delta."""
    errs: list[str] = []
    build = front_matter_build(text)
    delta = sections_map(body).get(DELTA_SECTION, "").strip()
    if build == "both":
        if not delta or (DELTA_NA.search(delta) and len(delta) < 120):
            errs.append(
                "build is 'both' but 'B41 vs B42 Delta' has no substantive "
                "content — a dual-build document must state what changed "
                "(or explicitly cite that nothing did)"
            )
    return errs


def check_citations(body: str) -> list[str]:
    errs: list[str] = []
    # Reference definitions: lines like "- [7] **Source** ..."
    ref_nums = sorted({int(n) for n in REF_DEF_RE.findall(body)})
    if not ref_nums:
        return []  # documents without numbered references are allowed (rare)

    # In-text markers = every [n] that is NOT the leading token of a ref-def line.
    marker_nums: set[int] = set()
    for line in body.splitlines():
        if REF_DEF_RE.match(line):
            # strip the leading "- [n]" definition token, keep any later markers
            line = REF_DEF_RE.sub("", line, count=1)
        for n in MARKER_RE.findall(line):
            marker_nums.add(int(n))

    ref_set = set(ref_nums)
    # 1. contiguous 1..N
    expected = set(range(1, len(ref_nums) + 1))
    if ref_set != expected:
        errs.append(
            f"reference numbering not contiguous 1..{len(ref_nums)}: "
            f"have {sorted(ref_set)}"
        )
    # 2. every in-text marker resolves
    unresolved = sorted(marker_nums - ref_set)
    if unresolved:
        errs.append(f"in-text markers with no reference entry: {unresolved}")
    # 3. every reference is cited in text
    uncited = sorted(ref_set - marker_nums)
    if uncited:
        errs.append(f"reference entries never cited in text: {uncited}")
    return errs


# ── Runner ───────────────────────────────────────────────────────────────────

def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    body = body_after_front_matter(text)
    return (check_front_matter(text) + check_structure(body)
            + check_version_tag(text, body) + check_citations(body))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs", help="docs directory (default: docs)")
    ap.add_argument("paths", nargs="*", help="specific file(s) to validate; "
                    "if omitted, every doc under --docs is checked")
    args = ap.parse_args()

    # index.md is the generated MkDocs landing page, not a knowledge-base document.
    if args.paths:
        files = [Path(p) for p in args.paths]
        missing = [f for f in files if not f.exists()]
        if missing:
            for f in missing:
                print(f"ERROR: no such file: {f}", file=sys.stderr)
            return 2
    else:
        root = Path(args.docs)
        files = [f for f in sorted(root.rglob("*.md")) if f.name != "index.md"]
    if not files:
        print(f"No markdown files found under {args.docs}/", file=sys.stderr)
        return 2

    total_errors = 0
    for f in files:
        errs = validate_file(f)
        rel = f.as_posix()
        if errs:
            total_errors += len(errs)
            print(f"FAIL  {rel}")
            for e in errs:
                print(f"        - {e}")
        else:
            print(f"ok    {rel}")

    print("-" * 60)
    if total_errors:
        print(f"VALIDATION FAILED: {total_errors} issue(s) across {len(files)} file(s)")
        return 1
    print(f"VALIDATION PASSED: {len(files)} file(s), 0 issues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
