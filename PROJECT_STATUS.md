# Project Status

**Stage:** 2 complete — all 41 documents (Players, Admins, Modders, Creator,
Lore, Meta) approved and frozen at release `kb-release-2026.10.08`, validated
against game 42.21 + 41.78.21 and Umbrella 42.21.0. Next: Stage 3 freshness
automation (see ROADMAP.md) and the follow-ups listed below.

**Date:** 2026-10-08 (status refreshed; originally written 2026-07-30). The
sections below are dated history.

## Wave E — Modders cluster (2026-10-07)

8 docs merged `in-review` v0.1.0 (6 Tier-2 reference + first-mod tutorial +
B41->B42 porting guide); 33 docs total. All gates green on the full set
(validate, genre strict, license, API-existence 295 refs, server-settings,
links, graph/RAG/site). markdownlint still unrunnable (not installed).
Worker-found extractor bug (B41 `--- @class` with a space) fixed; B41 index
regenerated and the two diff-dependent docs recomputed.

Wave E follow-ups for a human or later pass:
- DONE 2026-10-07: TIS forum 42.13 Migration Guide + "API for Inventory
  Items" PDFs read (signed-in browser download by the user) and folded into
  modders-mp-networking-porting, -item-scripts-distributions and
  -porting-b41-to-b42 (all now v0.2.0). Guide is 42.13-era (2025-12-11); its
  rules are not re-verified on 42.20/42.21. PDFs are TIS copyright, kept
  outside the repo; citations point at the forum thread (sign-in needed).
- Verify tutorial/ModOptions/item-script example code in a live 42.20 game.
- B41 `Recipe` block syntax and `Mods=` ordering remain unsourced (quarantined).
- Add pzwiki workshop.txt rev 1598215 to the pzwiki manifest (fetched live).
- A worker reported env vars (incl. OPENAI_API_KEY) printed to a session log;
  no secret is in the repo (grep clean) - consider rotating that key.
- All Modders docs verified on Umbrella 42.20.0; 42.21 (2026-09-28) unverified.

## 42.21 re-baseline (2026-10-07)

All 41 docs reviewed against the 42.20.1-42.21 official posts (six Steam
announcements + TIS forum topic 101693, read via browser extraction) and the
Umbrella 42.21.0 index; `game_versions_verified` now includes 42.21 on all of
them. Pins: B42 Umbrella 42.21.0 @ 13d01f9 (42.20.0 @ 58204fc kept as
B42_previous; the upstream 42.20.0 tag later moved to 98f50ae - pin by
commit); legacy41 primary-attested at 41.78.21. `check_freshness.py`: pins
current. Gates green (validate/genre/license/API 349 refs/server-settings;
links 412/416 live, 0 dead). The 42.20.0 API index is archived in
sources/schemas/archive/.

Release: all 41 docs frozen/approved and tagged `kb-release-2026.10.08`
(project owner approval 2026-10-08). The six foundations were re-approved
(admins/creator/lore/meta-style-guide/modders at 1.1.0, players-foundation at
1.1.1 after its occupation-roster correction: the pinned revision 1391359
lists 24 occupations plus Custom Occupation, with Farmer, Rancher, Fishing
Guide and Firefighter - not Crop Farmer/Livestock Farmer/Angler); the other 35
docs were promoted from 0.x in-review to 1.0.0 with no content change except
the traits, animals and release-policy notes.

Re-baseline caveats / follow-ups:
- Carried-forward statements were NOT re-tested in game; the forum changelist
  was captured in abridged form (long MP/other fix lists 'selected').
- Welder is primary-confirmed as a 42.21 occupation; the Metalworker->Welder
  rename is still inference.
- Open: whether legacy41 re-enabled loadstring/loadstream after 41.78.21;
  what 41.78.20 contained (wiki-only); MaxPlayers 254 (42.20.3) vs the pinned
  1-100 range (schema not re-extracted on a 42.21 server).
- Stub-only 42.21.0 changes (new medical-check/foraging events,
  sendAddObjectToMap, dropped print/radio classes and 155 classes overall, six
  fewer Recipe members) are unexplained by the notes.
- New primary refs sit out of numeric order inside some Primary lists
  (contiguous; validator accepts).

## Wave F — Creator + Lore/meta (2026-10-07)

8 docs merged `in-review` v0.1.0: creator (format catalogue, channel map,
cross-promotion funnel, post-launch content calendar), lore (in-world media,
Knox Event timeline), meta (release/versioning policy, source-registry
companion). 41 docs total (6 frozen, 35 unfrozen). All gates green on my own
run; links 395/399 live, 0 dead. Allowlist extended (support.discord.com,
pzwiki.net, developer.valvesoftware.com).

Wave F follow-ups:
- NEXT: 42.21 re-baseline (read 42.20.1-42.21 notes incl. the forum 42.21
  changelist topic 101693, re-pin Umbrella, bump `game_versions_verified`,
  re-verify the 42.13-era MP/registry rules). ScriptsDocs is already stamped
  42.21.0.
- Lore docs rest on pzwiki pages stamped <=42.12; radio/TV/print pages are
  not ingested in sources/pzwiki/ (ingest them).
- Twitch and Valve's mod-content policy were not opened (creator docs list
  them as gaps). TIS Terms 2.2 vs 2.5 overlap is left as an open question.
- pzwiki manifest has a UTF-8 BOM (plain json.load fails) and 5 default-list
  titles without manifest keys (Farming, Animals, Husbandry, Animal care,
  Brewing).
- meta-release-versioning-policy says "27 unfrozen" as a dated snapshot;
  current count is 35.
- CI (.github/workflows/qa.yml) does not yet run check_api_exists.py or
  check_freshness.py; no LICENSE file for the KB's own prose.

## State review 2026-10-07

- 25 docs (6 foundations + 19 wave A–D). All gates green except none failing:
  validate, genre audit (strict), license hygiene (67 pzwiki snapshots),
  server-setting gate, links (0 dead), graph. Wave A–D docs were still
  `in-review` at that point (frozen 2026-10-08, see Release above).
- **Game-version drift (new, unreconciled):** Steam news shows B42 stable is
  now **42.21** (2026-09-28; hotfixes 42.20.1–42.20.4 in Aug) and legacy41 is
  **41.78.21** (2026-08-26). Every doc is verified against 42.20 / 41.78.16-19.
  Run `python scripts/check_freshness.py`. Needs a re-baseline decision.
- Coverage gaps: Modders track has only its foundation; Creator and Lore only
  foundations; Tier 3 modder tutorials and Creator calendar not started.
- Added: `scripts/extract_api_index.py`, `scripts/check_api_exists.py`
  (indices for B41 @ fa2e7e1 and B42 @ 58204fc in `sources/schemas/`),
  `scripts/check_freshness.py`. Link fixes: ModInfo doc URL moved to
  `scripts/root_files/modinfo.html`; two bot-blocking hosts allowlisted.
- Stale locked git worktrees under `.claude/worktrees/` (wave D leftovers).

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
