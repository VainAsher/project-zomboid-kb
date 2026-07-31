# Master Index — Project Zomboid Knowledge Base

The document catalogue and knowledge graph. **Orchestrator-owned** — workers
never edit this file. `scripts/build_graph.py` and `scripts/build_site.py`
parse it; keep the table shape exactly.

Tiers: 1 = track foundations · 2 = core reference · 3 = guides/tutorials/runbooks
· 4 = meta, lore & creator strategy.

## Documents

| ID | Title | Topic | Tier | Build | Version | Status | Confidence | Path |
|----|-------|-------|------|-------|---------|--------|------------|------|
| admins-foundation | Running a Project Zomboid Dedicated Server: Architecture, Branches and Hosting Choices | Server foundations | 1 | both | 1.0.1 | approved | Medium | `docs/admins/admins-foundation.md` |
| admins-sandboxvars-reference | SandboxVars Reference: Gameplay Rules per Server | Server configuration | 2 | both | 0.1.0 | in-review | Medium | `docs/admins/admins-sandboxvars-reference.md` |
| admins-server-ini-reference | server.ini Reference: The Settings That Matter, by Area | Server configuration | 2 | both | 0.1.0 | in-review | Medium | `docs/admins/admins-server-ini-reference.md` |
| creator-foundation | The Project Zomboid Content Landscape: Formats, Channels and the B42-Stable Window | Creator foundations | 1 | B42 | 1.0.0 | approved | Medium | `docs/creator/creator-foundation.md` |
| lore-foundation | The Knox Event and the History of Project Zomboid's Builds | Lore & history | 1 | historic | 1.0.1 | approved | Medium | `docs/lore/lore-foundation.md` |
| meta-style-guide | How This Knowledge Base Is Written: Genre, Build Tags and License Rules | KB governance | 1 | both | 1.0.1 | approved | High | `docs/meta/meta-style-guide.md` |
| modders-foundation | Modding Project Zomboid: Ecosystem, Toolchain and Where the API Truth Lives | Modding foundations | 1 | both | 1.0.1 | approved | Medium | `docs/modders/modders-foundation.md` |
| players-foundation | Surviving Knox Country: The Core Game Across Build 41 and Build 42 | Player foundations | 1 | both | 1.0.1 | approved | Medium | `docs/players/players-foundation.md` |
| players-animals-husbandry | Animals and Husbandry in Build 42 | Animals & husbandry | 2 | B42 | 0.1.0 | in-review | Medium | `docs/players/players-animals-husbandry.md` |
| players-crafting-chains | The B42 Crafting Overhaul: From Knapping to Blacksmithing | Crafting | 2 | both | 0.1.0 | in-review | Medium | `docs/players/players-crafting-chains.md` |
| players-skills-xp | Skills and XP: Levelling, Multipliers and the B42 Skill Roster | Skills & XP | 2 | both | 0.1.0 | in-review | Medium | `docs/players/players-skills-xp.md` |
| players-traits-occupations | Traits and Occupations: Points, Rosters and the B42 Rework | Traits & occupations | 2 | both | 0.1.0 | in-review | Medium | `docs/players/players-traits-occupations.md` |

## Knowledge graph

Typed cross-reference edges, one bullet per source document:
`- \`source-id\` — *rel* → \`target-id\` [, \`target-id\` …]` — append
`(planned)` when the target document does not exist yet.

- `meta-style-guide` — *governs* → `modders-foundation`, `players-foundation`, `creator-foundation`, `lore-foundation`, `admins-foundation`
- `players-foundation` — *complements* → `modders-foundation`, `creator-foundation`, `lore-foundation`, `admins-foundation`
- `players-foundation` — *conforms_to* → `meta-style-guide`
- `lore-foundation` — *informs* → `players-foundation`, `modders-foundation`, `creator-foundation`, `admins-foundation`
- `lore-foundation` — *conforms_to* → `meta-style-guide`
- `modders-foundation` — *relates_to* → `players-foundation`, `creator-foundation`, `lore-foundation`, `meta-style-guide`, `admins-foundation`
- `creator-foundation` — *complements* → `modders-foundation`, `players-foundation`, `lore-foundation`, `admins-foundation`
- `creator-foundation` — *conforms_to* → `meta-style-guide`
- `admins-foundation` — *related* → `players-foundation`, `modders-foundation`, `creator-foundation`, `lore-foundation`
- `admins-foundation` — *conforms_to* → `meta-style-guide`
- `players-skills-xp` — *deepens* → `players-foundation`
- `players-skills-xp` — *relates_to* → `players-traits-occupations`, `players-crafting-chains`, `players-animals-husbandry`
- `players-skills-xp` — *conforms_to* → `meta-style-guide`
- `players-traits-occupations` — *deepens* → `players-foundation`
- `players-traits-occupations` — *related* → `players-skills-xp`, `players-crafting-chains`, `players-animals-husbandry`
- `players-traits-occupations` — *conforms_to* → `meta-style-guide`
- `players-crafting-chains` — *deepens* → `players-foundation`
- `players-crafting-chains` — *relates_to* → `players-skills-xp`, `players-traits-occupations`
- `players-crafting-chains` — *complements* → `players-animals-husbandry`
- `players-crafting-chains` — *informs* → `modders-foundation`
- `players-crafting-chains` — *conforms_to* → `meta-style-guide`
- `admins-sandboxvars-reference` — *deepens* → `admins-foundation`
- `admins-sandboxvars-reference` — *complements* → `admins-server-ini-reference`
- `admins-server-ini-reference` — *deepens* → `admins-foundation`
- `admins-server-ini-reference` — *complements* → `admins-sandboxvars-reference`, `modders-foundation`, `meta-style-guide`
- `players-animals-husbandry` — *deepens* → `players-foundation`
- `players-animals-husbandry` — *relates_to* → `players-skills-xp`, `players-crafting-chains`, `players-traits-occupations`
- `players-animals-husbandry` — *conforms_to* → `meta-style-guide`
- `admins-sandboxvars-reference` — *informs* → `players-foundation`
- `admins-sandboxvars-reference` — *conforms_to* → `meta-style-guide`

## Approved taxonomy backlog (scope approved 2026-07-30)

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
