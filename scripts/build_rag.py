#!/usr/bin/env python3
"""
Build a front-matter-aware RAG export from the knowledge base.

Splits every document into one chunk per top-level (`#`) section and writes
`exports/rag/chunks.jsonl` — one JSON object per line, each carrying the
section text plus the parent document's metadata (id, title, topic,
market, document_type, version, category, source path). A companion
`exports/rag/manifest.json` records counts and the field schema.

This is a retrieval-friendly export: chunks are self-describing (metadata
travels with the text) and sized to a single section, which matches how the
documents are structured (Documented Capability, Assessed Gap, References, ...).

Usage:  python scripts/build_rag.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

DOCS = Path("docs")
OUT = Path("exports/rag")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^# (.+?)\s*$", re.MULTILINE)

META_FIELDS = ["id", "title", "topic", "build", "document_type",
               "version", "status", "confidence", "category"]


def _flat(v):
    """Render a front-matter value as a clean scalar (join lists)."""
    if v is None:
        return None
    if isinstance(v, (list, tuple)):
        return ", ".join(str(x) for x in v)
    return str(v)


def split_sections(body: str) -> list[tuple[str, str]]:
    """Return [(heading, text), ...] splitting on top-level '# ' headings."""
    matches = list(H1_RE.finditer(body))
    out: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        text = body[start:end].strip()
        if text:
            out.append((heading, text))
    return out


def main() -> int:
    files = [f for f in sorted(DOCS.rglob("*.md")) if f.name != "index.md"]
    if not files:
        print("No documents found under docs/", file=sys.stderr)
        return 2

    OUT.mkdir(parents=True, exist_ok=True)
    chunks = []
    for f in files:
        raw = f.read_text(encoding="utf-8")
        m = FM_RE.match(raw)
        fm = yaml.safe_load(m.group(1)) if m else {}
        if not isinstance(fm, dict):
            fm = {}
        body = raw[m.end():] if m else raw
        meta = {k: fm.get(k) for k in META_FIELDS}
        doc_id = meta.get("id") or f.stem
        for idx, (heading, text) in enumerate(split_sections(body)):
            chunks.append({
                "chunk_id": f"{doc_id}#{idx:02d}",
                "doc_id": doc_id,
                "section": heading,
                "section_index": idx,
                "text": text,
                "tokens_estimate": max(1, len(text) // 4),
                "source_path": f.as_posix(),
                **{k: _flat(v) for k, v in meta.items()},
            })

    jsonl = OUT / "chunks.jsonl"
    with jsonl.open("w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    manifest = {
        "documents": len(files),
        "chunks": len(chunks),
        "total_tokens_estimate": sum(c["tokens_estimate"] for c in chunks),
        "chunk_fields": ["chunk_id", "doc_id", "section", "section_index",
                         "text", "tokens_estimate", "source_path"] + META_FIELDS,
        "note": "One chunk per top-level (#) section; document metadata travels "
                "with each chunk. Regenerate with scripts/build_rag.py.",
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Wrote {jsonl} — {len(chunks)} chunks from {len(files)} documents "
          f"(~{manifest['total_tokens_estimate']:,} tokens).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
