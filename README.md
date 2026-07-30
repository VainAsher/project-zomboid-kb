# Project Zomboid Knowledge Base (B41 & B42)

An evidence-based, source-cited Project Zomboid reference for four audiences —
**modders, players, server admins and content creators** — with every document
version-tagged for **Build 41.78 (legacy41)** and **Build 42.20 (stable,
released 2026-07-29)**.

> **Unofficial fan project.** Not affiliated with, endorsed by, or sponsored
> by The Indie Stone. Project Zomboid and all related content are trademarks
> and copyrights of The Indie Stone.

## What makes it different

- **Version-tagged everything.** Every document carries a hard `build:` tag
  (B41 / B42 / both / historic); dual-build documents must document the
  B41→B42 delta. CI fails otherwise.
- **Evidence over confidence.** Every factual claim cites a primary source
  (official blog/patch notes, Steam announcements, game files, the Umbrella
  API stubs). Community claims that can't be traced to a primary live in a
  labelled quarantine section with a confidence rating.
- **License-hygienic.** pzwiki.net (CC BY-NC-SA 3.0) is used as a fact source
  only; an n-gram overlap gate mechanically blocks prose reuse.
- **Deterministic QA.** Front matter, structure, citations, build tags, links,
  lint, and cross-references are all machine-checked in CI before any human
  review.

## Repo layout

| Path | Purpose |
|------|---------|
| `docs/<track>/` | Documents: `modders/`, `players/`, `admins/`, `creator/`, `lore/`, `meta/` |
| `templates/` | The 19-section reference document template |
| `prompts/` | The worker operating contract |
| `scripts/` | QA gates and export/site builders |
| `sources/pzwiki/` | Ingested pzwiki fact snapshots (license-gate corpus) |
| `exports/` | Generated knowledge graph, document matrix, coverage, RAG chunks |
| `MASTER_INDEX.md` | Document catalogue + knowledge graph |
| `SOURCE_REGISTRY.md` | Ranked source-authority list |

## Running the gates locally

```bash
pip install pyyaml
python scripts/validate.py
python scripts/audit_genre.py --strict
python scripts/check_license_hygiene.py
npx --yes markdownlint-cli2 "docs/**/*.md" "*.md"
python scripts/check_links.py        # network required
python scripts/build_graph.py && python scripts/build_rag.py && python scripts/build_site.py
```

## Status

Stage 0 — scaffolded and gated; document generation begins after scope
approval. See `PROJECT_STATUS.md` and `ROADMAP.md`.
