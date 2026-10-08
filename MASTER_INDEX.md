# Master Index — Project Zomboid Knowledge Base

The document catalogue and knowledge graph. **Orchestrator-owned** — workers
never edit this file. `scripts/build_graph.py` and `scripts/build_site.py`
parse it; keep the table shape exactly.

Tiers: 1 = track foundations · 2 = core reference · 3 = guides/tutorials/runbooks
· 4 = meta, lore & creator strategy.

## Documents

| ID | Title | Topic | Tier | Build | Version | Status | Confidence | Path |
|----|-------|-------|------|-------|---------|--------|------------|------|
| admins-foundation | Running a Project Zomboid Dedicated Server: Architecture, Branches and Hosting Choices | Server foundations | 1 | both | 1.1.0 | approved | Medium | `docs/admins/admins-foundation.md` |
| admins-backups-migration | Backups, Saves and Migration: Protecting a Server World | Server operations | 2 | both | 1.0.0 | approved | Medium | `docs/admins/admins-backups-migration.md` |
| admins-legacy41-runbook | Keeping a Build 41 Server Alive: The legacy41 Runbook | Server runbooks | 3 | B41 | 1.0.0 | approved | Medium | `docs/admins/admins-legacy41-runbook.md` |
| admins-modded-server-runbook | Running a Modded Server: Selection, Rollout and Update Discipline | Server runbooks | 3 | both | 1.0.0 | approved | Medium | `docs/admins/admins-modded-server-runbook.md` |
| admins-performance-tuning | Server Performance: Memory, CPU and the Levers That Are Actually Documented | Server operations | 2 | both | 1.0.0 | approved | Medium | `docs/admins/admins-performance-tuning.md` |
| admins-rcon-commands | RCON and Admin Commands: Operating a Live Server | Server operations | 2 | both | 1.0.0 | approved | Medium | `docs/admins/admins-rcon-commands.md` |
| admins-sandboxvars-reference | SandboxVars Reference: Gameplay Rules per Server | Server configuration | 2 | both | 1.0.0 | approved | Medium | `docs/admins/admins-sandboxvars-reference.md` |
| admins-server-ini-reference | server.ini Reference: The Settings That Matter, by Area | Server configuration | 2 | both | 1.0.0 | approved | Medium | `docs/admins/admins-server-ini-reference.md` |
| admins-ubuntu-runbook | Ubuntu Dedicated Server Runbook: SteamCMD to systemd | Server runbooks | 3 | both | 1.0.0 | approved | Medium | `docs/admins/admins-ubuntu-runbook.md` |
| admins-workshop-mod-wiring | Wiring Workshop Mods into a Server: IDs, Load Order and Updates | Server operations | 2 | both | 1.0.0 | approved | Medium | `docs/admins/admins-workshop-mod-wiring.md` |
| creator-foundation | The Project Zomboid Content Landscape: Formats, Channels and the B42-Stable Window | Creator foundations | 1 | B42 | 1.1.0 | approved | Medium | `docs/creator/creator-foundation.md` |
| lore-foundation | The Knox Event and the History of Project Zomboid's Builds | Lore & history | 1 | historic | 1.1.0 | approved | Medium | `docs/lore/lore-foundation.md` |
| meta-style-guide | How This Knowledge Base Is Written: Genre, Build Tags and License Rules | KB governance | 1 | both | 1.2.0 | approved | High | `docs/meta/meta-style-guide.md` |
| modders-foundation | Modding Project Zomboid: Ecosystem, Toolchain and Where the API Truth Lives | Modding foundations | 1 | both | 1.1.0 | approved | Medium | `docs/modders/modders-foundation.md` |
| players-foundation | Surviving Knox Country: The Core Game Across Build 41 and Build 42 | Player foundations | 1 | both | 1.1.1 | approved | Medium | `docs/players/players-foundation.md` |
| players-beginner-guide-b42 | Starting Project Zomboid on Build 42.21: A First-Week Survival Guide | Guides | 3 | B42 | 1.0.0 | approved | Medium | `docs/players/players-beginner-guide-b42.md` |
| players-farming-food | Farming, Foraging and Food: Feeding a Survivor Long-Term | Farming & food | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-farming-food.md` |
| players-animals-husbandry | Animals and Husbandry in Build 42 | Animals & husbandry | 2 | B42 | 1.0.0 | approved | Medium | `docs/players/players-animals-husbandry.md` |
| players-b41-to-b42-transition | The B41 Veteran's Guide to Build 42: What Your Instincts Get Wrong | Guides | 3 | both | 1.0.0 | approved | Medium | `docs/players/players-b41-to-b42-transition.md` |
| players-crafting-chains | The B42 Crafting Overhaul: From Knapping to Blacksmithing | Crafting | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-crafting-chains.md` |
| players-map-locations | Knox Country Locations: The B41 Towns and the B42 Expansion | Map & locations | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-map-locations.md` |
| players-medical-moodles | Health, Injuries and Moodles: The Body Simulation | Medical & moodles | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-medical-moodles.md` |
| players-skills-xp | Skills and XP: Levelling, Multipliers and the B42 Skill Roster | Skills & XP | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-skills-xp.md` |
| players-traits-occupations | Traits and Occupations: Points, Rosters and the B42 Rework | Traits & occupations | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-traits-occupations.md` |
| players-vehicles | Vehicles: Finding, Fixing and Driving Across Both Builds | Vehicles | 2 | both | 1.0.0 | approved | Medium | `docs/players/players-vehicles.md` |
| modders-lua-api-surface | The Project Zomboid Lua API Surface: Java-Exposed Classes, Globals and the Per-Build Differences | Lua API surface | 2 | both | 1.0.0 | approved | Medium | `docs/modders/modders-lua-api-surface.md` |
| modders-events-callbacks | Events and Callbacks: Hooking the Game Loop with Events.X.Add | Events & callbacks | 2 | both | 1.0.0 | approved | Medium | `docs/modders/modders-events-callbacks.md` |
| modders-modoptions-pzapi | PZAPI.ModOptions and the B42 Mod Settings API: Building an Options Screen | ModOptions & PZAPI | 2 | both | 1.0.0 | approved | Medium | `docs/modders/modders-modoptions-pzapi.md` |
| modders-item-scripts-distributions | Item Scripts, Recipes and Loot Distributions: Defining Content Through Script Files | Item scripts & distributions | 2 | both | 1.0.0 | approved | Medium | `docs/modders/modders-item-scripts-distributions.md` |
| modders-mp-networking-porting | Multiplayer Mod Networking: Client/Server Lua, sendClientCommand and Porting for B42 MP | MP networking porting | 2 | both | 1.0.0 | approved | Medium | `docs/modders/modders-mp-networking-porting.md` |
| modders-modinfo-modid-conventions | mod.info, Mod IDs and the B42 Versioned Mod Folder Layout | mod.info & Mod ID conventions | 2 | both | 1.0.0 | approved | Medium | `docs/modders/modders-modinfo-modid-conventions.md` |
| modders-first-mod-tutorial-b42 | Your First Build 42 Mod: A Verified Step-by-Step Tutorial | First mod tutorial | 3 | B42 | 1.0.0 | approved | Medium | `docs/modders/modders-first-mod-tutorial-b42.md` |
| modders-porting-b41-to-b42 | Porting a Build 41 Mod to Build 42: A Diff-Driven Checklist | Porting B41 mods to B42 | 3 | both | 1.0.0 | approved | Medium | `docs/modders/modders-porting-b41-to-b42.md` |
| creator-format-catalogue | Project Zomboid Content Format Catalogue: What Works, What It Costs and Which Build It Needs | Format catalogue | 2 | B42 | 1.0.0 | approved | Medium | `docs/creator/creator-format-catalogue.md` |
| creator-channel-competitor-map | The Project Zomboid Creator Landscape: Channels, Niches and Gaps | Channel & competitor map | 2 | B42 | 1.0.0 | approved | Medium | `docs/creator/creator-channel-competitor-map.md` |
| creator-cross-promotion-funnel | From Video to Server to Mod: A Cross-Promotion Funnel for a Project Zomboid Creator | Cross-promotion funnel | 2 | B42 | 1.0.0 | approved | Medium | `docs/creator/creator-cross-promotion-funnel.md` |
| creator-content-calendar | Post-Launch Content Calendar for Build 42: Release Rhythm, Patch Hooks and Evergreen Slots | Content calendar | 3 | B42 | 1.0.0 | approved | Medium | `docs/creator/creator-content-calendar.md` |
| lore-in-world-media | In-World Media: Radio, Television, Print and Found Documents in Knox Country | In-world media | 4 | both | 1.0.0 | approved | Medium | `docs/lore/lore-in-world-media.md` |
| lore-knox-event-timeline | The Knox Event Timeline: What the Game Says Happened and When | Knox Event timeline | 4 | historic | 1.0.0 | approved | Medium | `docs/lore/lore-knox-event-timeline.md` |
| meta-release-versioning-policy | Release and Versioning Policy: Document Versions, kb-release Tags and Game-Build Pins | Release & versioning policy | 4 | both | 1.2.0 | approved | High | `docs/meta/meta-release-versioning-policy.md` |
| meta-source-registry-companion | Source Registry Companion: How Each Source Is Reached, What Is Ingested and What Is Blocked | Source registry companion | 4 | both | 1.0.0 | approved | Medium | `docs/meta/meta-source-registry-companion.md` |

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
- `players-map-locations` — *deepens* → `players-foundation`
- `players-map-locations` — *relates_to* → `lore-foundation`, `meta-style-guide`, `players-vehicles`
- `players-vehicles` — *deepens* → `players-foundation`
- `players-vehicles` — *related* → `players-skills-xp`, `players-map-locations`
- `players-vehicles` — *conforms_to* → `meta-style-guide`
- `admins-rcon-commands` — *deepens* → `admins-foundation`
- `admins-rcon-commands` — *complements* → `admins-server-ini-reference`, `admins-sandboxvars-reference`
- `admins-rcon-commands` — *conforms_to* → `meta-style-guide`
- `admins-backups-migration` — *deepens* → `admins-foundation`
- `admins-backups-migration` — *references* → `admins-server-ini-reference`, `admins-sandboxvars-reference`, `lore-foundation`, `meta-style-guide`
- `admins-performance-tuning` — *deepens* → `admins-foundation`
- `admins-performance-tuning` — *complements* → `admins-server-ini-reference`, `admins-sandboxvars-reference`, `meta-style-guide`
- `players-medical-moodles` — *deepens* → `players-foundation`
- `players-medical-moodles` — *cross_references* → `players-skills-xp`, `admins-sandboxvars-reference`
- `players-medical-moodles` — *conforms_to* → `meta-style-guide`
- `players-b41-to-b42-transition` — *deepens* → `players-foundation`
- `players-b41-to-b42-transition` — *cross_references* → `players-skills-xp`, `players-traits-occupations`, `players-crafting-chains`, `players-animals-husbandry`, `players-medical-moodles`, `players-map-locations`, `players-vehicles`
- `players-b41-to-b42-transition` — *conforms_to* → `meta-style-guide`
- `players-farming-food` — *deepens* → `players-foundation`
- `players-farming-food` — *complements* → `players-animals-husbandry`
- `players-farming-food` — *relates_to* → `players-crafting-chains`, `players-skills-xp`
- `players-farming-food` — *conforms_to* → `meta-style-guide`
- `admins-legacy41-runbook` — *deepens* → `admins-foundation`
- `admins-legacy41-runbook` — *cross_references* → `admins-backups-migration`, `admins-server-ini-reference`
- `admins-legacy41-runbook` — *related* → `lore-foundation`
- `admins-legacy41-runbook` — *conforms_to* → `meta-style-guide`
- `admins-sandboxvars-reference` — *informs* → `players-foundation`
- `admins-sandboxvars-reference` — *conforms_to* → `meta-style-guide`
- `admins-ubuntu-runbook` — *deepens* → `admins-foundation`
- `admins-ubuntu-runbook` — *complements* → `admins-server-ini-reference`, `admins-backups-migration`
- `admins-ubuntu-runbook` — *related* → `admins-workshop-mod-wiring`, `admins-modded-server-runbook`
- `admins-ubuntu-runbook` — *conforms_to* → `meta-style-guide`
- `admins-workshop-mod-wiring` — *deepens* → `admins-foundation`, `admins-server-ini-reference`, `modders-foundation`
- `admins-workshop-mod-wiring` — *related* → `admins-modded-server-runbook`, `admins-ubuntu-runbook`
- `admins-workshop-mod-wiring` — *conforms_to* → `meta-style-guide`
- `admins-modded-server-runbook` — *deepens* → `admins-foundation`, `admins-workshop-mod-wiring`
- `admins-modded-server-runbook` — *related* → `admins-ubuntu-runbook`, `admins-backups-migration`, `admins-performance-tuning`
- `admins-modded-server-runbook` — *conforms_to* → `meta-style-guide`
- `players-beginner-guide-b42` — *deepens* → `players-foundation`
- `players-beginner-guide-b42` — *cross_references* → `players-skills-xp`, `players-traits-occupations`, `players-medical-moodles`, `players-map-locations`
- `players-beginner-guide-b42` — *conforms_to* → `meta-style-guide`
- `modders-lua-api-surface` — *deepens* → `modders-foundation`
- `modders-lua-api-surface` — *related* → `modders-events-callbacks`, `modders-modoptions-pzapi`, `modders-item-scripts-distributions`, `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`, `modders-first-mod-tutorial-b42`, `modders-porting-b41-to-b42`
- `modders-lua-api-surface` — *conforms_to* → `meta-style-guide`
- `modders-events-callbacks` — *deepens* → `modders-foundation`
- `modders-events-callbacks` — *related* → `modders-lua-api-surface`, `modders-modoptions-pzapi`, `modders-item-scripts-distributions`, `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`, `modders-first-mod-tutorial-b42`, `modders-porting-b41-to-b42`
- `modders-events-callbacks` — *conforms_to* → `meta-style-guide`
- `modders-modoptions-pzapi` — *deepens* → `modders-foundation`
- `modders-modoptions-pzapi` — *related* → `modders-lua-api-surface`, `modders-events-callbacks`, `modders-item-scripts-distributions`, `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`, `modders-first-mod-tutorial-b42`, `modders-porting-b41-to-b42`
- `modders-modoptions-pzapi` — *conforms_to* → `meta-style-guide`
- `modders-item-scripts-distributions` — *deepens* → `modders-foundation`
- `modders-item-scripts-distributions` — *related* → `modders-lua-api-surface`, `modders-events-callbacks`, `modders-modoptions-pzapi`, `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`, `modders-first-mod-tutorial-b42`, `modders-porting-b41-to-b42`
- `modders-item-scripts-distributions` — *conforms_to* → `meta-style-guide`
- `modders-mp-networking-porting` — *deepens* → `modders-foundation`
- `modders-mp-networking-porting` — *related* → `modders-lua-api-surface`, `modders-events-callbacks`, `modders-modoptions-pzapi`, `modders-item-scripts-distributions`, `modders-modinfo-modid-conventions`, `modders-first-mod-tutorial-b42`, `modders-porting-b41-to-b42`
- `modders-mp-networking-porting` — *conforms_to* → `meta-style-guide`
- `modders-modinfo-modid-conventions` — *deepens* → `modders-foundation`
- `modders-modinfo-modid-conventions` — *related* → `modders-lua-api-surface`, `modders-events-callbacks`, `modders-modoptions-pzapi`, `modders-item-scripts-distributions`, `modders-mp-networking-porting`, `modders-first-mod-tutorial-b42`, `modders-porting-b41-to-b42`
- `modders-modinfo-modid-conventions` — *conforms_to* → `meta-style-guide`
- `modders-first-mod-tutorial-b42` — *deepens* → `modders-foundation`
- `modders-first-mod-tutorial-b42` — *related* → `modders-lua-api-surface`, `modders-events-callbacks`, `modders-modoptions-pzapi`, `modders-item-scripts-distributions`, `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`, `modders-porting-b41-to-b42`
- `modders-first-mod-tutorial-b42` — *conforms_to* → `meta-style-guide`
- `modders-porting-b41-to-b42` — *deepens* → `modders-foundation`
- `modders-porting-b41-to-b42` — *related* → `modders-lua-api-surface`, `modders-events-callbacks`, `modders-modoptions-pzapi`, `modders-item-scripts-distributions`, `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`, `modders-first-mod-tutorial-b42`
- `modders-porting-b41-to-b42` — *conforms_to* → `meta-style-guide`
- `modders-item-scripts-distributions` — *relates_to* → `players-crafting-chains`
- `modders-porting-b41-to-b42` — *relates_to* → `players-crafting-chains`, `admins-workshop-mod-wiring`
- `modders-modinfo-modid-conventions` — *relates_to* → `admins-workshop-mod-wiring`
- `modders-first-mod-tutorial-b42` — *prerequisite_for* → `modders-lua-api-surface`, `modders-events-callbacks`
- `creator-format-catalogue` — *deepens* → `creator-foundation`
- `creator-format-catalogue` — *related* → `creator-channel-competitor-map`, `creator-cross-promotion-funnel`, `creator-content-calendar`
- `creator-format-catalogue` — *fact_checks_with* → `players-beginner-guide-b42`, `players-b41-to-b42-transition`, `players-animals-husbandry`, `players-crafting-chains`, `admins-modded-server-runbook`, `modders-first-mod-tutorial-b42`, `lore-foundation`
- `creator-format-catalogue` — *conforms_to* → `meta-style-guide`
- `creator-channel-competitor-map` — *deepens* → `creator-foundation`
- `creator-channel-competitor-map` — *related* → `creator-format-catalogue`, `creator-cross-promotion-funnel`, `creator-content-calendar`
- `creator-channel-competitor-map` — *supports* → `players-beginner-guide-b42`, `players-b41-to-b42-transition`, `admins-modded-server-runbook`, `modders-first-mod-tutorial-b42`
- `creator-channel-competitor-map` — *conforms_to* → `meta-style-guide`
- `creator-cross-promotion-funnel` — *deepens* → `creator-foundation`
- `creator-cross-promotion-funnel` — *related* → `creator-format-catalogue`, `creator-channel-competitor-map`, `creator-content-calendar`, `admins-modded-server-runbook`, `admins-ubuntu-runbook`, `admins-workshop-mod-wiring`, `modders-first-mod-tutorial-b42`, `modders-modinfo-modid-conventions`, `players-beginner-guide-b42`
- `creator-cross-promotion-funnel` — *conforms_to* → `meta-style-guide`
- `creator-content-calendar` — *deepens* → `creator-foundation`
- `creator-content-calendar` — *related* → `creator-format-catalogue`, `creator-channel-competitor-map`, `creator-cross-promotion-funnel`
- `creator-content-calendar` — *draws_facts_from* → `players-beginner-guide-b42`, `players-b41-to-b42-transition`, `players-farming-food`, `players-animals-husbandry`, `players-vehicles`, `players-medical-moodles`, `admins-modded-server-runbook`, `modders-first-mod-tutorial-b42`
- `creator-content-calendar` — *conforms_to* → `meta-style-guide`
- `lore-in-world-media` — *deepens* → `lore-foundation`
- `lore-in-world-media` — *related* → `lore-knox-event-timeline`, `players-map-locations`, `players-b41-to-b42-transition`, `modders-item-scripts-distributions`, `modders-modinfo-modid-conventions`
- `lore-in-world-media` — *conforms_to* → `meta-style-guide`
- `lore-knox-event-timeline` — *deepens* → `lore-foundation`
- `lore-knox-event-timeline` — *related* → `lore-in-world-media`, `players-map-locations`, `players-b41-to-b42-transition`, `players-foundation`, `creator-foundation`
- `lore-knox-event-timeline` — *conforms_to* → `meta-style-guide`
- `meta-release-versioning-policy` — *deepens* → `meta-style-guide`
- `meta-release-versioning-policy` — *related* → `meta-source-registry-companion`, `modders-lua-api-surface`, `admins-server-ini-reference`, `players-foundation`
- `meta-source-registry-companion` — *deepens* → `meta-style-guide`
- `meta-source-registry-companion` — *related* → `meta-release-versioning-policy`, `creator-channel-competitor-map`
- `meta-source-registry-companion` — *supports* → `modders-lua-api-surface`, `modders-modinfo-modid-conventions`, `admins-server-ini-reference`

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
