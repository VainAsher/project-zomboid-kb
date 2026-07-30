# Project Status

**Stage:** 2 — scope approved 2026-07-30; foundation cluster in production.

**Date:** 2026-07-30

## Approved scope (human gate cleared 2026-07-30)

- Taxonomy approved as proposed in `MASTER_INDEX.md`.
- First cluster after foundations: **Players + Admins**.
- Dual coverage realized as **`build: both` + enforced delta** by default;
  paired per-build docs only where builds truly diverge.
- **Standing mandate granted:** auto-approve/merge/freeze clusters on green QA;
  pause only on gate failures or unverifiable core claims.

## Done

- Chassis copied and adapted to the **reference** genre (19-section template).
- Gates live: validate (incl. the hard build-tag gate), genre audit
  (evidence/quarantine discipline), license hygiene (pzwiki n-gram overlap),
  markdownlint, link check, graph/RAG/site builders.
- Governance files generated; taxonomy proposed in `MASTER_INDEX.md`.
- Git repo initialized on `main`; CI workflows target `main`.

## In flight

- Foundation cluster (6 docs) with parallel workers.

## Next

- Merge foundation returns → all gates green → freeze + tag.
- Stage 1 ingestion (Umbrella pin, pzwiki snapshots, server-setting schemas),
  then the Players + Admins cluster.

## Key context

- B42.20 went stable 2026-07-29 (multiplayer included); hotfixes expected —
  every seeded doc must record `game_versions_verified` and get re-queued on
  42.2x patches.
- Full dual coverage (B41.78 + B42.20) was chosen at bootstrap.
