#!/usr/bin/env python3
"""
Build machine-readable exports from the knowledge base.

Reads:
  - MASTER_INDEX.md  — the document catalogue table (id/title/topic/tier/
                       build/version/status/confidence/path) and the
                       "Knowledge graph" section (typed cross-reference edges).
  - each doc's YAML front matter — enrichment (category, document_type,
                       review_due, created, related).

Writes to exports/:
  - knowledge-graph.json    nodes + typed edges (edges tagged known/planned)
  - knowledge-graph.mmd     Mermaid diagram (solid = doc↔doc, dashed = planned)
  - document-matrix.csv     one row per document with key attributes
  - document-matrix.json    same, structured
  - coverage.md             topic / build / confidence summary

Also acts as a cross-reference validator: exits non-zero if a knowledge-graph
edge points at an id that is neither a real document nor listed as (planned).

Usage:  python scripts/build_graph.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = Path(".")
INDEX = ROOT / "MASTER_INDEX.md"
DOCS = ROOT / "docs"
OUT = ROOT / "exports"

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
CODE_SPAN = re.compile(r"`([a-z0-9][a-z0-9-]+)`")
ITALIC = re.compile(r"\*([^*]+)\*")
PLANNED_RE = re.compile(r"\(planned\)")


# ── Parse the catalogue table ────────────────────────────────────────────────

def parse_index_documents(text: str) -> dict[str, dict]:
    nodes: dict[str, dict] = {}
    in_docs = False
    for line in text.splitlines():
        if line.startswith("## Documents"):
            in_docs = True
            continue
        if in_docs and line.startswith("## "):
            break
        if in_docs and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 9 or cells[0] in ("ID", "") or set(cells[0]) <= {"-"}:
                continue
            nid, title, topic, tier, build, version, status, conf, path = cells[:9]
            nodes[nid] = {
                "id": nid, "title": title, "topic": topic, "tier": tier,
                "build": build, "version": version, "status": status,
                "confidence": conf, "path": path.strip("`"),
            }
    return nodes


def enrich_from_front_matter(nodes: dict[str, dict]) -> list[str]:
    warnings: list[str] = []
    for nid, n in nodes.items():
        p = ROOT / n["path"]
        if not p.exists():
            warnings.append(f"index lists {nid} but file missing: {n['path']}")
            continue
        m = FM_RE.match(p.read_text(encoding="utf-8"))
        fm = yaml.safe_load(m.group(1)) if m else {}
        for f in ("category", "document_type", "review_due", "created"):
            n[f] = fm.get(f)
        rel = fm.get("related") or []
        n["related"] = [r for r in rel if isinstance(r, str)]
    return warnings


# ── Parse the knowledge-graph edges ──────────────────────────────────────────

def parse_kg_edges(text: str, known: set[str]) -> tuple[list[dict], list[str]]:
    edges: list[dict] = []
    skipped: list[str] = []
    in_kg = False
    for line in text.splitlines():
        if line.startswith("## Knowledge graph"):
            in_kg = True
            continue
        if in_kg and line.startswith("## "):
            break
        if not (in_kg and line.lstrip().startswith("- ")):
            continue
        spans = CODE_SPAN.findall(line)
        if not spans:
            continue
        # source = leading code-span, but only if the bullet starts with "- `"
        if not re.match(r"^\s*- `", line):
            skipped.append(line.strip())
            continue
        src, targets = spans[0], spans[1:]
        if src not in known:
            skipped.append(line.strip())
            continue
        labels = ITALIC.findall(line)
        rel = "; ".join(labels) if labels else "related"
        planned = bool(PLANNED_RE.search(line))
        for tgt in targets:
            edges.append({
                "from": src, "to": tgt, "rel": rel,
                "target": "known" if tgt in known else ("planned" if planned else "unknown"),
            })
    return edges, skipped


def merge_related_edges(nodes: dict[str, dict], edges: list[dict], known: set[str]) -> None:
    seen = {(e["from"], e["to"]) for e in edges}
    for nid, n in nodes.items():
        for tgt in n.get("related", []):
            if (nid, tgt) in seen or nid == tgt:
                continue
            edges.append({
                "from": nid, "to": tgt, "rel": "related",
                "target": "known" if tgt in known else "planned",
            })
            seen.add((nid, tgt))


# ── Emit ─────────────────────────────────────────────────────────────────────

def write_json(path: Path, obj) -> None:
    path.write_text(
        json.dumps(obj, indent=2, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )


def write_mermaid(path: Path, nodes: dict[str, dict], edges: list[dict]) -> None:
    lines = ["graph LR"]
    # group nodes by tier
    by_tier: dict[str, list[str]] = defaultdict(list)
    for nid, n in nodes.items():
        by_tier[n.get("tier", "?")].append(nid)
    for tier in sorted(by_tier):
        lines.append(f'  subgraph Tier{tier}["Tier {tier}"]')
        for nid in sorted(by_tier[tier]):
            lines.append(f'    {nid.replace("-", "_")}["{nid}"]')
        lines.append("  end")
    seen_planned: set[str] = set()
    for e in edges:
        a = e["from"].replace("-", "_")
        b = e["to"].replace("-", "_")
        label = e["rel"].split(";")[0].strip()[:24]
        if e["target"] == "known":
            lines.append(f'  {a} -->|{label}| {b}')
        else:
            if e["to"] not in seen_planned:
                lines.append(f'  {b}(["{e["to"]}<br/>(planned)"])')
                seen_planned.add(e["to"])
            lines.append(f'  {a} -.->|{label}| {b}')
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


COLUMNS = ["id", "title", "topic", "tier", "build", "document_type",
           "category", "version", "status", "confidence", "review_due", "path"]


def write_matrix(nodes: dict[str, dict]) -> None:
    rows = [{c: (n.get(c) or "") for c in COLUMNS} for n in nodes.values()]
    with (OUT / "document-matrix.csv").open("w", newline="", encoding="utf-8") as f:
        # lineterminator="\n" keeps the CSV LF on every platform so the CI
        # staleness check (which regenerates on Linux) matches the committed file.
        w = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    write_json(OUT / "document-matrix.json", rows)


def write_coverage(nodes: dict[str, dict], edges: list[dict]) -> None:
    topics = defaultdict(list)
    for n in nodes.values():
        topics[n["topic"]].append(n["id"])
    builds = Counter(n["build"] for n in nodes.values())
    conf = Counter(n["confidence"] for n in nodes.values())
    tiers = Counter(n["tier"] for n in nodes.values())
    lines = [
        "# Coverage Report", "",
        "_Generated by `scripts/build_graph.py` — do not edit by hand._", "",
        f"**Documents:** {len(nodes)}  ·  **Cross-reference edges:** {len(edges)}"
        f"  ·  **Topics with a document:** {len(topics)}", "",
        "## Documents per topic", "",
        "| Topic | Docs | IDs |", "|-------|------|-----|",
    ]
    for t in sorted(topics):
        ids = ", ".join(f"`{i}`" for i in sorted(topics[t]))
        lines.append(f"| {t} | {len(topics[t])} | {ids} |")
    lines += ["", "## Build coverage", "", "| Build | Docs |", "|---|---|"]
    for k, v in sorted(builds.items()):
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Confidence distribution", "", "| Confidence | Docs |", "|---|---|"]
    for k in ("High", "Medium", "Low"):
        if conf.get(k):
            lines.append(f"| {k} | {conf[k]} |")
    lines += ["", "## Documents per tier", "", "| Tier | Docs |", "|---|---|"]
    for k, v in sorted(tiers.items()):
        lines.append(f"| {k} | {v} |")
    (OUT / "coverage.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    text = INDEX.read_text(encoding="utf-8")
    nodes = parse_index_documents(text)
    warnings = enrich_from_front_matter(nodes)
    known = set(nodes)
    edges, skipped = parse_kg_edges(text, known)
    merge_related_edges(nodes, edges, known)

    OUT.mkdir(exist_ok=True)
    write_json(OUT / "knowledge-graph.json",
               {"nodes": list(nodes.values()), "edges": edges})
    write_mermaid(OUT / "knowledge-graph.mmd", nodes, edges)
    write_matrix(nodes)
    write_coverage(nodes, edges)

    print(f"Nodes: {len(nodes)}  Edges: {len(edges)}  "
          f"(known->known: {sum(1 for e in edges if e['target']=='known')})")
    print(f"Wrote exports/: knowledge-graph.json/.mmd, document-matrix.csv/.json, coverage.md")

    problems = [e for e in edges if e["target"] == "unknown"]
    for e in problems:
        print(f"DANGLING edge: {e['from']} -> {e['to']} (not a doc, not marked planned)")
    for w in warnings:
        print(f"WARN: {w}")
    if skipped:
        print(f"(skipped {len(skipped)} group/non-source KG line(s))")
    return 1 if (problems or warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
