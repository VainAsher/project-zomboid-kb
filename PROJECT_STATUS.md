# Project Status

**Stage:** 2 — foundation cluster FROZEN (kb-release-2026.07.30);
next: Stage-1 ingestion + the Players + Admins cluster.

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

## Done (2026-07-30)

- Foundation cluster (6 docs) written, gated, frozen at v1.0.0 and tagged
  `kb-release-2026.07.30`. Independent link check 107/107 live.

## Open items carried out of the foundation cluster

- No repo LICENSE file for the KB's own original prose (flagged by
  meta-style-guide worker) — needs a human licensing decision.
- Contested facts quarantined, to be settled empirically on a test server:
  B42 RAM sizing (+2 GB claim), backslash Mod-ID convention,
  live `reloadoptions` vs stop-before-editing, 42.20 challenge name
  ("28 Minutes Later" vs "28 Seconds Later").

## Next

- Stage 1 ingestion: pin Umbrella 42.20.0 release tag, snapshot pzwiki pages
  into sources/pzwiki/ (arms the license gate), extract server-setting
  schemas; then build the API-existence and server-setting gates.
- Players + Admins cluster (approved first cluster).

## Key context

- B42.20 went stable 2026-07-29 (multiplayer included); hotfixes expected —
  every seeded doc must record `game_versions_verified` and get re-queued on
  42.2x patches.
- Full dual coverage (B41.78 + B42.20) was chosen at bootstrap.
