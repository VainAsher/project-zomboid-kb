# Changelog

All notable changes to the knowledge base. A fact change always cuts a new
document version with a revision note — never a silent edit.

## [kb-release-2026.07.30] — 2026-07-30

### Added

- 2026-10-07 — Wave F: Creator (format-catalogue, channel-competitor-map,
  cross-promotion-funnel, content-calendar), Lore (in-world-media,
  knox-event-timeline) and Meta (release-versioning-policy,
  source-registry-companion) documents, v0.1.0 in-review; 41 docs total.

- 2026-10-07 — Wave E revision 0.2.0 (3 Modders docs): official TIS 42.13
  Migration Guide and "API for Inventory Items" folded into
  mp-networking-porting (server-authoritative items, Timed Action split,
  sync calls), item-scripts-distributions (registries.lua and the 11 ID
  registries) and porting-b41-to-b42 (checklist). Unread-guide claims removed;
  guide-vs-ScriptsDocs discrepancies recorded.

- 2026-10-07 — Wave E: Modders cluster (8 docs, v0.1.0 in-review):
  lua-api-surface, events-callbacks, modoptions-pzapi,
  item-scripts-distributions, mp-networking-porting,
  modinfo-modid-conventions, first-mod-tutorial-b42, porting-b41-to-b42.
  `scripts/diff_api_indices.py` reproduces the cited B41/B42 symbol diffs.
  Fixed `extract_api_index.py` to parse `--- @class` (B41 stubs); B41 index
  regenerated (1035/1498 classes now carry parents).

- 2026-10-07 — Stage 1 API-existence gate: `extract_api_index.py` builds
  per-build symbol indices from the pinned Umbrella stubs (B42 4266 classes /
  234 events; B41 1498 / 240); `check_api_exists.py` validates Modders-doc
  `Events.X` and `Class:method` code spans against them (negative-tested).
  `check_freshness.py` flags drift of pinned builds vs Steam news.
- 2026-10-07 — Link hygiene: corrected the PZ-API-Docs ModInfo URL in
  admins-workshop-mod-wiring (URL only, no fact change); allowlisted
  map.projectzomboid.com and legionhosting.net as bot-block hosts.

- Foundation cluster frozen at v1.0.0: `admins-foundation`,
  `creator-foundation`, `lore-foundation`, `meta-style-guide`,
  `modders-foundation`, `players-foundation` (6 docs, 30 knowledge-graph
  edges, 114 RAG chunks). All gates green; independent link check 107/107
  live, 0 dead. Validated against game builds 41.78.16 (legacy41) and
  42.20.0 (stable); Umbrella API-stub release tag 42.20.0.
  Approved under the standing auto-approve-on-green mandate (2026-07-30).

## [Unreleased]

### Added

- 2026-07-30 — Stage 1 ingestion: pzwiki fact corpus (58 pages, revision-
  pinned, gitignored per CC BY-NC-SA; manifest committed) arms the license-
  hygiene gate; Umbrella release tags pinned in `sources/pins.json`
  (B42 42.20.0 @ 58204fc, B41 41.78.16 @ fa2e7e1); new server-setting
  existence gate (`check_server_settings.py`, arms when the reference-doc
  schema is extracted); license gate refined to exempt attributed quotes.

### Changed

- 2026-07-31 — **B41 baseline policy** (user decision): the KB's B41
  verification target is now the legacy41 maintenance line (41.78.19
  primary-attested, security-only; 41.78.20 pzwiki-attested pending
  primary), no longer frozen 41.78.16. Existing docs' verification
  provenance stands; `game_versions_verified` moves at each doc's next
  revision. Umbrella B41 API pin remains release tag 41.78.16.
- 2026-07-30 — Five foundation docs bumped to 1.0.1: license-hygiene prose
  rewrites after the armed n-gram gate flagged 23 overlaps (no factual
  changes; creator-foundation was already clean).

- 2026-07-30 — Repo bootstrapped from the kb-factory chassis; reference-genre
  gates (validate/build-tag, genre audit, license hygiene, links, lint,
  graph/RAG/site) adapted for Project Zomboid B41/B42 dual coverage. Taxonomy
  proposed; awaiting human approval before any document generation.
