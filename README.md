# Project Zomboid Knowledge Base (B41 & B42)

An evidence-based, source-cited Project Zomboid reference for four audiences —
**modders, players, server admins and content creators** — with every document
version-tagged for **Build 41.78 (legacy41)** and **Build 42.21 (stable since
2026-09-28)**.

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
python scripts/check_license_hygiene.py   # needs the local pzwiki corpus (gitignored)
python scripts/check_server_settings.py
python scripts/check_api_exists.py
npx --yes markdownlint-cli2@0.23.3 "docs/**/*.md" "*.md"
python scripts/check_links.py             # network required
python scripts/check_freshness.py         # network; exit 2 = pinned builds behind
python scripts/build_graph.py && python scripts/build_rag.py && python scripts/build_site.py
```

CI (`.github/workflows/`) runs the offline gates on every push and pull
request, the link check weekly, and the freshness check daily.

## Status

41 documents across all six tracks are approved and released as
`kb-release-2026.10.08` (game builds 42.21 and 41.78.21, Umbrella 42.21.0).
See `PROJECT_STATUS.md`, `RELEASE_HISTORY.md` and `ROADMAP.md`.

## License

The software (`scripts/`, `.github/workflows/`) is under the MIT License
(`LICENSE`). The knowledge-base content (`docs/`, `templates/`, `prompts/`,
`exports/` and the root Markdown files) is **all rights reserved**; see
`LICENSE-CONTENT.md` for the terms and the third-party notices.
