# Master Index — Project Zomboid Knowledge Base

The document catalogue and knowledge graph. **Orchestrator-owned** — workers
never edit this file. `scripts/build_graph.py` and `scripts/build_site.py`
parse it; keep the table shape exactly.

Tiers: 1 = track foundations · 2 = core reference · 3 = guides/tutorials/runbooks
· 4 = meta, lore & creator strategy.

## Documents

| ID | Title | Topic | Tier | Build | Version | Status | Confidence | Path |
|----|-------|-------|------|-------|---------|--------|------------|------|

## Knowledge graph

Typed cross-reference edges, one bullet per source document:
`- \`source-id\` — *rel* → \`target-id\` [, \`target-id\` …]` — append
`(planned)` when the target document does not exist yet.

## Proposed taxonomy (pre-approval — no documents generated yet)

### Tier 1 — Track foundations (6 docs)

- `modders-foundation` — Modding Build 42: ecosystem, toolchain, mod.info, where the API truth lives (both)
- `players-foundation` — Surviving Knox Country: core loop, moodles, builds overview (both)
- `admins-foundation` — Running a PZ dedicated server: architecture, branches, hosting choices (both)
- `creator-foundation` — PZ content landscape: formats, channels, the B42-stable window (B42)
- `lore-foundation` — The Knox Event and historic builds (historic)
- `meta-style-guide` — How this KB is written: genre, build tags, license rules (both)

### Tier 2 — Core reference (per track, seeded per approved cluster)

- Players: skills & XP, traits & occupations, crafting chains (Knapping→Blacksmithing),
  animals & husbandry, map locations (B41 towns + B42 additions), vehicles,
  medical/moodles, farming & food
- Modders: Lua API surface per build, events & callbacks, ModOptions/PZAPI,
  item scripts & distributions, MP networking porting, mod.info & Mod ID conventions
- Admins: server.ini reference, SandboxVars reference, RCON & admin commands,
  RAM/performance tuning, backups & migration, workshop mod wiring
- Creator: format catalogue, channel/competitor map, cross-promotion funnel

### Tier 3 — Guides & runbooks

- Players: B41-veteran→B42 transition guide, beginner survival guide (42.20-stable)
- Modders: first mod tutorial (B42), porting a B41 mod to B42
- Admins: Ubuntu dedicated-server runbook (SteamCMD → systemd → UFW),
  legacy41 server runbook, modded-server runbook
- Creator: launch-window content calendar

### Tier 4 — Meta & lore depth

- Source registry companion, release/versioning policy, lore deep-dives
