#!/usr/bin/env python3
"""
License-hygiene gate for the Project Zomboid knowledge base.

pzwiki.net content is CC BY-NC-SA 3.0. This knowledge base uses pzwiki as a
FACT source only — its prose and tables must never be republished (the
NonCommercial clause conflicts with the project's commercial context). This
gate makes that rule mechanical: it flags any document whose prose overlaps
the ingested pzwiki corpus by a shared word n-gram at or above the threshold.

Corpus layout: plain-text snapshots of ingested pzwiki pages live under
`sources/pzwiki/` (one .txt per page, produced by the Stage-1 MediaWiki-API
ingester). An empty or missing corpus passes trivially with a note — the gate
becomes active as soon as the first snapshot lands.

Exit code 0 = clean (or no corpus yet), 1 = overlap found. Offline, stdlib only.

Usage:  python scripts/check_license_hygiene.py [--ngram 8] [--corpus sources/pzwiki] [FILE ...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WORD_RE = re.compile(r"[a-z0-9']+")
URL_RE = re.compile(r"https?://\S+")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
# Attributed quotation is permitted by the KB's genre rules (minimal, cited).
# The gate targets UNQUOTED prose reuse, so quoted spans and blockquotes in
# OUR documents are exempt. The corpus side is never stripped.
# [^"] deliberately includes newlines — quotations wrap across lines in
# 80-column prose; the 600-char bound stops an unbalanced quote running away.
QUOTE_RE = re.compile(r'"[^"]{1,600}"|“[^”]{1,600}”')
BLOCKQUOTE_RE = re.compile(r"^\s*>.*$", re.MULTILINE)

DEFAULT_NGRAM = 8   # 8 consecutive shared words = near-verbatim reuse


def normalise(text: str, skip_quotes: bool = False) -> list[str]:
    text = CODE_FENCE_RE.sub(" ", text)
    text = URL_RE.sub(" ", text)
    if skip_quotes:
        # A quote break must also break n-gram continuity: replace with a
        # marker word that never matches corpus text.
        text = QUOTE_RE.sub(" qqquotebreakqqq ", text)
        text = BLOCKQUOTE_RE.sub(" qqquotebreakqqq ", text)
    return WORD_RE.findall(text.lower())


def ngrams(words: list[str], n: int):
    for i in range(len(words) - n + 1):
        yield " ".join(words[i:i + n])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ngram", type=int, default=DEFAULT_NGRAM,
                    help=f"shared-word run length that counts as reuse "
                         f"(default {DEFAULT_NGRAM})")
    ap.add_argument("--corpus", default="sources/pzwiki",
                    help="directory of ingested pzwiki plain-text snapshots")
    ap.add_argument("--docs", default="docs")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    corpus_dir = Path(args.corpus)
    corpus_files = sorted(corpus_dir.rglob("*.txt")) if corpus_dir.is_dir() else []
    if not corpus_files:
        print(f"LICENSE HYGIENE: no pzwiki corpus under {args.corpus}/ yet — "
              "gate passes trivially (activate it by ingesting snapshots).")
        return 0

    corpus_grams: dict[str, str] = {}
    for cf in corpus_files:
        words = normalise(cf.read_text(encoding="utf-8", errors="replace"))
        for g in ngrams(words, args.ngram):
            corpus_grams.setdefault(g, cf.name)

    if args.paths:
        files = [Path(p) for p in args.paths]
    else:
        files = [f for f in sorted(Path(args.docs).rglob("*.md"))
                 if f.name != "index.md"]

    total = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        body = text[m.end():] if m else text
        words = normalise(body, skip_quotes=True)
        hits: dict[str, str] = {}
        for g in ngrams(words, args.ngram):
            if g in corpus_grams:
                hits[g] = corpus_grams[g]
        if hits:
            total += len(hits)
            print(f"FLAG  {f.as_posix()}")
            for g, src in sorted(hits.items())[:10]:
                print(f"        - {args.ngram}-gram matches pzwiki page "
                      f"'{src}': \"{g[:80]}...\"")
            if len(hits) > 10:
                print(f"        - ... and {len(hits) - 10} more")
        else:
            print(f"ok    {f.as_posix()}")

    print("-" * 60)
    if total:
        print(f"LICENSE HYGIENE FAILED: {total} overlapping {args.ngram}-gram(s) "
              f"across {len(files)} file(s) — rewrite the flagged prose in "
              "original words before publishing")
        return 1
    print(f"LICENSE HYGIENE CLEAN: {len(files)} file(s) vs "
          f"{len(corpus_files)} pzwiki snapshot(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
