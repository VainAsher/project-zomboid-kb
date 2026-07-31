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

## Open items from the Players + Admins cluster (wave A)

- Cross-doc discrepancy to reconcile at freeze: players-foundation says the
  B42 Occupation roster (pzwiki rev 1391359) lists 23 occupations + Custom
  named Crop Farmer/Livestock Farmer/Angler; BOTH the traits doc (24 rows)
  and the animals doc (local snapshot reads Farmer/Rancher/Fishing Guide)
  independently contradict that reading — players-foundation likely needs a
  1.0.2 correction at wave freeze.
- RESOLVED 2026-07-31 (user decision): the B41 baseline moves to the
  legacy41 maintenance line. Orchestrator verified 41.78.19 is a
  security-only hotfix (primary), so existing 41.78.16-era fact
  verification stands; docs bump `game_versions_verified` at their next
  natural revision. Follow-up: primary-confirm 41.78.20 (currently
  pzwiki-attested only) when TIS announces it or the legacy41 server
  reports its version.
- pzwiki intermittently Cloudflare-challenges API clients: re-check the
  Server settings revision (pinned 1443167) when access allows; ingest the
  "Husbandry" and "Animal care" pages into sources/pzwiki/ when reachable
  (they 403'd during wave A; note "Husbandry"/"Animal care" titles were
  missing at first ingestion — find the real page titles).
- AntiCheat numeric mode mapping (1=Ban/2=Kick/3=Log/4=Disable) is
  quarantined at Low — schema encodes key existence only.
- "Brewing" was briefed as a B42 crafting skill family, but no skill or
  chain could be primary-sourced (crafting SYSTEM only) — both wave-A docs
  treat it accordingly; confirm framing in-game.
- Unresolved renames quarantined pending one in-game 42.20 check each:
  Pacifist→Reluctant Fighter (Medium), Asthmatic→Short of Breath (Low),
  Metalworker→Welder (roster-inference only); occupation naming tension
  between patch notes (Farmer/Rancher/Fishing Guide) and the pinned wiki
  roster (Crop Farmer/Livestock Farmer/Fire Officer).

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
