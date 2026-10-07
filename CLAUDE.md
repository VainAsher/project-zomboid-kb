# Project Zomboid Knowledge Base — Operating Rules

Evidence-based, source-cited Project Zomboid reference for four audience
tracks (Modders / Players / Admins / Creator), fully version-tagged for
Build 41.78 (legacy41) and Build 42.20 (stable, released 2026-07-29).

## Genre: reference

- **Evidence layer** (`Reference`, `B41 vs B42 Delta`, `Build Applicability`):
  every factual sentence carries a `[n]` citation to a primary source with a
  working link. No exceptions.
- **Guidance layer** (`Practical Guidance`, `Common Pitfalls`): may synthesise
  cited facts, never introduces new uncited facts.
- **Quarantine layer** (`Community Notes & Unverified Claims`): the only place
  an uncited community claim may live, always as a labelled claim block with
  Claim / Why unverified / Confidence.

**Never let a judgement or hearsay wear the costume of a fact.**

## Hard rules (never relax)

1. **Build tag.** Every document carries `build: B41 | B42 | both | historic`.
   `both` requires a substantive `B41 vs B42 Delta` section. Single-build
   values inside a `both` document are tagged inline *(B41)* / *(B42)*.
   `validate.py` enforces this mechanically.
2. **License hygiene.** pzwiki.net is CC BY-NC-SA 3.0 and this project is
   commercially adjacent (monetized YouTube channel). pzwiki is a **fact
   source only**: cite URL + revision id, write 100% original prose, never
   copy or lightly paraphrase its sentences or tables.
   `check_license_hygiene.py` gates this against the ingested corpus.
   Site-wide disclaimer: unofficial fan project, not affiliated with The
   Indie Stone; PZ content is TIS's trademark/copyright.
3. **Sources.** Follow the priority order in `SOURCE_REGISTRY.md`. Never
   fabricate a URL. Never sole-source a hard number from a hosting-company KB.
4. **One writer per file.** Workers get `prompts/worker_contract.md` verbatim
   plus a scope; they write only their own file and never touch shared files
   or git.
5. **Human gate.** No cluster merges to `main` without human approval (or an
   explicitly granted standing "auto-approve on green QA" mandate).
6. **Freeze/version/release.** A fact change cuts a new document version with
   a revision note, never a silent edit. Each `kb-release-*` tag pins the game
   build(s) and the Umbrella commit it was validated against.

## QA gates (all green before a cluster freezes)

```
python scripts/validate.py                 # front matter + 19 sections + build gate + citations
python scripts/audit_genre.py --strict     # evidence cites; claims quarantined & labelled
python scripts/check_license_hygiene.py    # no pzwiki prose overlap
npx --no-install markdownlint-cli2 "docs/**/*.md" "*.md"
python scripts/check_links.py              # 0 dead links (orchestrator re-runs independently)
python scripts/check_api_exists.py         # Modder docs: Events.X / Class:method exist in pinned Umbrella
python scripts/check_server_settings.py    # Admin docs: setting keys exist in schema
python scripts/build_graph.py              # cross-references resolve
python scripts/build_rag.py && python scripts/build_site.py   # exports current
```

Freshness: `python scripts/check_freshness.py` (informational; exit 2 = pinned
builds behind Steam news). Server-setting range checks remain planned. See
`ROADMAP.md`.

## Repo map

- `docs/<track>/` — the documents (modders/ players/ admins/ creator/ lore/ meta/)
- `templates/document_template.md` — the 19-section reference template
- `prompts/worker_contract.md` — handed to every worker verbatim
- `scripts/` — the deterministic gates + export/site builders
- `sources/pzwiki/` — ingested pzwiki plain-text snapshots (license-gate corpus)
- `exports/` — generated knowledge graph, matrix, coverage, RAG chunks
- `MASTER_INDEX.md` — the document catalogue + knowledge graph (orchestrator-owned)
- `SOURCE_REGISTRY.md` — ranked source-authority list + ingestion notes
