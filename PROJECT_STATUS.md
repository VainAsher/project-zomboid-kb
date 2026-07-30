# Project Status

**Stage:** 0 — bootstrapped, awaiting human approval of the taxonomy/scope
(hard stop per the factory process).

**Date:** 2026-07-30

## Done

- Chassis copied and adapted to the **reference** genre (19-section template).
- Gates live: validate (incl. the hard build-tag gate), genre audit
  (evidence/quarantine discipline), license hygiene (pzwiki n-gram overlap),
  markdownlint, link check, graph/RAG/site builders.
- Governance files generated; taxonomy proposed in `MASTER_INDEX.md`.
- Git repo initialized on `main`; CI workflows target `main`.

## Blocked on

- **Human approval** of: taxonomy, ranked source list, template/gate changes,
  and first-cluster choice (recommended: Players + Admins).

## Next (post-approval)

- Stage 1 ingestion (Umbrella pin, pzwiki snapshots, server-setting schemas),
  then seed the approved first cluster with parallel workers.

## Key context

- B42.20 went stable 2026-07-29 (multiplayer included); hotfixes expected —
  every seeded doc must record `game_versions_verified` and get re-queued on
  42.2x patches.
- Full dual coverage (B41.78 + B42.20) was chosen at bootstrap.
