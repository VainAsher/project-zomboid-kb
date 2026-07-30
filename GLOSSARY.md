# Glossary — Project Zomboid Knowledge Base

Shared terms. Orchestrator-owned; workers propose entries via their return
JSON, never edit this file. `Source` points at `SOURCE_REGISTRY.md` tiers.

## Game & builds

| Term | Definition | Source |
|------|------------|--------|
| B41 / legacy41 | Build 41 (final numbered stable: 41.78.16), kept available as the `legacy41` Steam beta branch after B42 became the default stable build on 2026-07-29. B41 saves and mods are not compatible with B42. | Tier 1 |
| B42 | Build 42: unstable branch 2024-12-17 (single-player only), multiplayer from unstable 42.13 (2025-12-11), stable as 42.20 on 2026-07-29. | Tier 1 |
| Unstable (branch) | The opt-in Steam beta branch on which Build 42 was publicly developed before the 42.20 stable release. | Tier 1 |
| IWBUMS | "I Will Back Up My Save" — the B41-era name for the opt-in public beta branch that the B42 era calls unstable. | Tier 3 |
| Thursdoid | The Indie Stone's development blog series, published Thursdays since September 2017 (previously the Monday "Mondoid"); cadence is irregular and event-driven, mirrored as Steam announcements. | Tier 1 |
| Knox Event | The in-fiction outbreak that opens the game's story, dated by The Indie Stone to 6 July 1993 in rural Kentucky. TIS's copyrighted fiction — document, don't republish. | Tier 1 |
| Knox Country | The partially fictional Kentucky game world (formerly Knox County), modelled on the real Muldraugh / West Point / Louisville area. | Tier 3 |
| Exclusion Zone | The in-fiction military quarantine area around the Knox outbreak within which the player character is trapped. | Tier 3 |
| Moodle | Icon-based status indicator reporting the character's physical and emotional state (hunger, panic, tiredness, etc.), with hover tooltips. | Tier 3 |
| Launch window | The weeks immediately after a major stable release, when returning-player traffic and search demand spike; for B42 it opened 2026-07-29. | Tier 1 |

## Modding

| Term | Definition | Source |
|------|------------|--------|
| Kahlua | Java implementation of Lua (based on Lua 5.1, with differences) that Project Zomboid embeds to run mod scripts inside the Java game process with exposed Java classes. | Tier 3 |
| Umbrella | Community-maintained EmmyLua/LuaCATS type stubs for the PZ Lua API, release-tagged per game version (41.78.16 through 42.20.0); this KB's machine-checkable API ground truth. Repo now under the PZ-Umbrella GitHub org. | Tier 2 |
| ZomboidDoc (pz-zdoc) | GPL-3.0 compiler that generates an annotated EmmyLua-ready Lua library from an installed copy of the game; dormant since May 2023 (B41-era tooling). | Tier 2 |
| Mod ID | The `id` value in `mod.info` identifying a mod to the game; duplicate loaded copies of the same Mod ID clash. Distinct from the Workshop ID. | Tier 3 |
| Workshop ID | Numeric identifier Steam assigns to an uploaded Workshop item; one Workshop item may contain several mods. | Tier 3 |
| common folder | B42 mod subfolder for shared assets, loaded before the matched version folder; a B42 mod needs at least one `common/` or version folder to be detected. | Tier 3 |
| Version folder | B42 mod subfolder named after a game version (`42/`, `42.1/`) holding build-specific files and its own `mod.info`; resolved at build.major precision. | Tier 3 |
| PZAPI.ModOptions | B42's native Lua API for per-user mod options (keybinds, tickboxes, sliders, etc.), replacing the B41-era community Mod Options framework. | Tier 3 |
| craftRecipe | The B42 script block for defining crafting recipes, replacing B41's legacy `Recipe` block. | Tier 3 |
| Spiffo's Workshop | Project Zomboid's Steam Workshop hub, the official channel for sharing mods. | Tier 3 |

## Servers & admin

| Term | Definition | Source |
|------|------------|--------|
| SandboxVars | The per-save/server gameplay-settings Lua file; edited only while the server is stopped. | Tier 4 |
| RCON | Remote console protocol used to administer a dedicated server. | Tier 4 |

## Creator ecosystem

| Term | Definition | Source |
|------|------------|--------|
| Condensed playthrough (supercut) | A long survival run edited into a single narrative video, typically titled "I Survived N Days…"; the PZ ecosystem's most-cloned format. | Tier 5 |
| Challenge run | A playthrough under self-imposed constraint rules (e.g. CDDA start, all negative traits), giving a repeatable per-episode premise without new game content. | Tier 5 |
| VOD channel | A secondary YouTube channel where a creator archives full, lightly edited stream recordings, kept separate from the edited main channel. | Tier 5 |

## KB governance

| Term | Definition | Source |
|------|------------|--------|
| Build tag | The required `build:` front-matter field (B41 \| B42 \| both \| historic) scoping a document's facts to the game build(s) they were verified on; `both` documents owe a substantive delta section. | — |
| Evidence layer | The Reference, B41 vs B42 Delta and Build Applicability sections, where every factual sentence must carry a [n] citation to a primary source. | — |
| Guidance layer | The Practical Guidance and Common Pitfalls sections; may synthesise cited facts but may not introduce new uncited facts. | — |
| Quarantine layer | The Community Notes & Unverified Claims section — the only place an uncited community claim may appear, always as a labelled Claim / Why unverified / Confidence block. | — |
| Fact-only source | A source whose facts may be cited (with URL + revision-id provenance) but whose prose and table layouts must never be copied or lightly paraphrased; in this KB, pzwiki.net (CC BY-NC-SA 3.0). | Tier 3 |
