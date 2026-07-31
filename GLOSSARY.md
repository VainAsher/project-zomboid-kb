# Glossary — Project Zomboid Knowledge Base

Shared terms. Orchestrator-owned; workers propose entries via their return
JSON, never edit this file. `Source` points at `SOURCE_REGISTRY.md` tiers.

## Game & builds

| Term | Definition | Source |
|------|------------|--------|
| B41 / legacy41 | Build 41, kept available as the `legacy41` Steam beta branch after B42 went stable on 2026-07-29, and still receiving maintenance hotfixes (41.78.19 security patch primary-attested 2026-04-08; 41.78.20 pzwiki-attested). The KB's B41 baseline is the current legacy41 maintenance line, not frozen 41.78.16. B41 saves and mods are not compatible with B42. | Tier 1 |
| B42 | Build 42: unstable branch 2024-12-17 (single-player only), multiplayer from unstable 42.13 (2025-12-11), stable as 42.20 on 2026-07-29. | Tier 1 |
| Unstable (branch) | The opt-in Steam beta branch on which Build 42 was publicly developed before the 42.20 stable release. | Tier 1 |
| IWBUMS | "I Will Back Up My Save" — the B41-era name for the opt-in public beta branch that the B42 era calls unstable. | Tier 3 |
| Thursdoid | The Indie Stone's development blog series, published Thursdays since September 2017 (previously the Monday "Mondoid"); cadence is irregular and event-driven, mirrored as Steam announcements. | Tier 1 |
| Knox Event | The in-fiction outbreak that opens the game's story, dated by The Indie Stone to 6 July 1993 in rural Kentucky. TIS's copyrighted fiction — document, don't republish. | Tier 1 |
| Knox Country | The partially fictional Kentucky game world (formerly Knox County), modelled on the real Muldraugh / West Point / Louisville area. | Tier 3 |
| Exclusion Zone | The in-fiction military quarantine area around the Knox outbreak within which the player character is trapped. | Tier 3 |
| Moodle | Icon-based status indicator reporting the character's physical and emotional state (hunger, panic, tiredness, etc.), with hover tooltips. | Tier 3 |
| Knox Infection | The fatal zombie-borne disease, transmitted only by zombie wounds (scratch 7%, laceration 25%, bite 100% by default); untreatable, invisible in the UI, and distinct from bacterial wound infection. | Tier 3 |
| Wound infection | Bacterial infection of a neglected or dirty-bandaged wound; increases pain only, is treatable, and is always survivable. | Tier 3 |
| Muscle strain | Build 42's accumulated exertion damage, applied to the specific body parts performing an action and scaled down by weapon skill and Strength; governed by the `MuscleStrainFactor` sandbox key. | Tier 1 |
| Bandage power | A per-item value governing how long a dressing stays effective before turning dirty; bandage types heal at the same rate and differ only in longevity and infection interaction. | Tier 3 |
| Launch window | The weeks immediately after a major stable release, when returning-player traffic and search demand spike; for B42 it opened 2026-07-29. | Tier 1 |
| Game mode (playstyle) | The top-level scenario chosen before spawn location and character creation, pre-filling Custom Sandbox with a themed settings preset (Apocalypse, Outbreak, Extinction, Rising on B42.20). | Tier 3 |

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
| require= (mod.info) | A `mod.info` field listing, comma-separated, the Mod IDs a mod needs to run; the documented dependency mechanism, distinct from `Mods=` list order in server.ini. | Tier 3 |
| loadModAfter= / loadModBefore= (mod.info) | `mod.info` fields that force a mod to load after or before a comma-separated list of named Mod IDs; the documented load-order lever, independent of `Mods=` position. | Tier 3 |
| Workshop tag | A category label attached to a Steam Workshop item from a predefined list the game itself supplies (including build-version tags Build 40/41/42); author-applied, not independently verified. | Tier 2 |
| Workshop "Update Required" state | A per-item Workshop download-state label distinct from "Installed," meaning the client or server's cached copy is stale relative to what Steam currently serves for that item. | Tier 2 |

## Skills, traits & crafting

| Term | Definition | Source |
|------|------------|--------|
| XP boost (starting-level boost) | The permanent XP-rate multiplier a skill receives from its level at character creation: 25% at level 0, 100% at 1, 133% at 2, 166% at 3+; Strength and Fitness are exempt. | Tier 3 |
| Passive skill | Strength or Fitness — the two-skill category with a far larger XP scale (1,500 XP for level 1 vs 75 for a regular skill) and exemption from starting-level XP boosts. | Tier 3 |
| Skill book | A single-use readable that multiplies XP for one skill within a two-level band; the five volumes cover levels 1–2 to 9–10 at standard multipliers ×3, ×5, ×8, ×12 and ×16. | Tier 3 |
| Skill ID | A skill's internal data name; B42's renamed skills keep their old IDs (Agriculture = `Farming`, Welding = `MetalWelding`, Running = `Sprinting`, Knapping = `FlintKnapping`). | Tier 3 |
| Trait points | The character-creation budget: positive traits cost points, negative traits grant them, and the character can only spawn at zero or above. | Tier 3 |
| Occupation-exclusive trait | A trait that cannot be bought with points and only arrives bundled with a specific occupation, e.g. Desensitized with Veteran. | Tier 3 |
| Adaptive trait | A trait gained or lost during play as strength, fitness or weight changes (community: "dynamic traits"); losing a creation-time negative this way never refunds its points. | Tier 3 |
| Free points | Community shorthand for negative traits whose in-play downside is trivial relative to the points granted; a B41 meta pattern sharply reduced by B42's re-pricing. | Tier 5 |
| Crafting chain | A sequence of B42 crafting skills and stations where earlier links (e.g. Carving, Pottery) produce the tools and materials later links (e.g. Blacksmithing) require. | — |
| Workstation | A placed or built object that specific B42 recipes require and that is operated by clicking on it: pottery benches and wheels, kilns, furnaces, forges, grindstones. | Tier 3 |
| Research Craft | The B42 system (added 42.3) that reverse-engineers learnable recipes from an item via a right-click option, granting the recipe and the craft's XP. | Tier 1 |
| Fluid container | Any B42 item or entity that stores a fluid; any container can hold any fluid, tracked in millilitres, with mixing and taint propagation. | Tier 3 |
| Agriculture (skill) | Build 42's name for the crop-farming skill, renamed from B41's Farming; the internal Skill ID remains `Farming`. | Tier 3 |
| Growing season | A B42 crop's calendar profile — planting window, best/poor months, bad months and growth duration — governing when sowing is safe. | Tier 3 |
| Cursed crop | A B42 crop permanently penalised (halved recovery, doubled losses, reduced yield, doubled disease chance) for wrong-season planting, bad months, winter, or triple fertilizing; incurable. | Tier 3 |
| Search Mode | The foraging interface (default hotkey END) that blurs the screen outside a skill-scaled search radius; replaced the previous foraging system in Build 41.60. | Tier 3 |
| Evolved recipe | A cooking construction (soup, stew, salad, sandwich, etc.) accepting variable ingredients, each contributing recipe-specific hunger and nutrition; inherits age only from its base ingredient. | Tier 3 |
| Drying rack | A Build 42 food-preservation station that dries plants, herbs (one in-game day) and leather (seven days) in variable batch sizes. | Tier 1 |
| Power shutoff | The sandbox-scheduled random day within a configured window on which grid electricity stops, disabling refrigerators and lights. | Tier 3 |
| Zero-point occupation | An occupation whose creation-point cost is 0, granting starting skill levels without spending or earning points (e.g. Doctor, Farmer, Firefighter, Lumberjack, Nurse, Rancher on B42). | Tier 3 |

## Servers & admin

| Term | Definition | Source |
|------|------------|--------|
| Dedicated server | The standalone headless Project Zomboid server distribution, Steam App ID 380870, installable via anonymous SteamCMD login on Windows or Linux. | Tier 4 |
| SteamCMD | Valve's command-line Steam client used to install and update PZ server files (`login anonymous`; `app_update 380870 validate`; append `-beta legacy41` for a B41 server). | Tier 4 |
| SandboxVars | The per-server Lua file of gameplay-rule settings (`servertest_SandboxVars.lua`), distinct from the `.ini` server settings file. Conventionally edited with the server stopped (see the admins foundation's quarantined claim on live reload). | Tier 4 |
| RCON | Password-protected remote console interface for issuing admin commands to a running PZ server; configured via `RCONPort` (default 27015) and `RCONPassword`. | Tier 4 |
| GSP | Game server provider; The Indie Stone opened a feedback channel for medium-to-large Zomboid GSPs at the B42 stable release. | Tier 1 |
| ZombieLore | Nested SandboxVars table of zombie behaviour settings (speed, strength, toughness, transmission, senses). | Tier 3 |
| ZombieConfig | Nested SandboxVars table of the population model: multipliers, peak day, respawn cycle, migration and grouping. | Tier 3 |
| MultiplierConfig | B42-only nested SandboxVars table of XP multipliers: a Global value, a GlobalToggle, and ~35 per-skill keys under internal skill names. | Tier 3 |
| Sandbox enum coding | Multiple-choice sandbox options are stored as 1-based integer codes whose meanings are fixed per key. | Tier 3 |
| Generated default | The value the server writes into SandboxVars when it creates the file at first startup; the 42.20 generated file notably disables zombie respawn. | Tier 3 |
| Soft reset | A server wipe that forces clients to create new characters, tracked by the paired identity keys `ResetID` and `ServerPlayerID` in the server .ini. Its documented trigger, `-Dsoftreset`, is broken as of 42.20.0. | Tier 3 |
| Zomboid folder (cache folder) | The per-user data directory (`%USERPROFILE%\Zomboid` on Windows, `~/Zomboid` on Linux/macOS) holding server settings, saves, databases and logs; relocatable with `-cachedir`. | Tier 3 |
| World folder | `Zomboid/Saves/Multiplayer/<servername>` — the generated, continuously saved world state for one server, keyed to the server name. | Tier 3 |
| Account database | The SQLite file under `Zomboid/db` named after the server, holding user accounts and whitelist state. | Tier 3 |
| Cold backup | A copy of server data taken with the server stopped — the only restore-grade backup; a hot copy (server running) is best-effort. | — |
| 42.19 branch | A parallel Steam beta branch preserving unstable Build 42.19 so its saves (incompatible with 42.20) can be finished; distinct from legacy41. | Tier 1 |
| Maintenance line | This KB's term for Build 41 as it now exists: a branch receiving security/maintenance hotfixes (41.78.17 through at least 41.78.19 in 2026) but no content development. | Tier 1 |
| Branch pinning | Encoding the `-beta legacy41` flag into every SteamCMD install/update command so a routine update can never silently hop a B41 server onto the default (B42) branch. | Tier 3 |
| outdatedunstable | An official Steam branch that lags one content update behind unstable, introduced as part of the 2026 security-driven branch policy. | Tier 1 |
| ZGC | The Z Garbage Collector, the low-pause-time JVM collector the shipped B42 server launch script selects with `-XX:+UseZGC`. | Tier 3 |
| ZNet | Project Zomboid's network layer, named in the shipped `-Dzomboid.znetlog` JVM property; its server-side logging was improved at 42.20. | Tier 1 |
| Object pool statistics | A server monitoring/diagnostics surface added in Build 42.20 that reports on the server's object pools; output format undocumented. | Tier 1 |
| Statistics period | The interval in seconds at which the multiplayer statistics subsystem samples, set via the `-statistic` server argument (written under `cachedir/Statistic`) or the `MultiplayerStatisticsPeriod` ini key. | Tier 3 |
| Loading ID | A mod's internal identifier from its info.txt, used in the `Mods=` list; distinct from the numeric Steam Workshop ID used in `WorkshopItems=`. | Tier 3 |
| Safety system | The per-player PVP opt-in mechanism (`SafetySystem=true`): one player can hurt another only when at least one of the two has PVP mode engaged. | Tier 3 |
| Access level | The staff tier attached to a server account, set with `/setaccesslevel`; documented roster is Admin, Moderator, Overseer, GM, Observer, plus `none` to strip elevated access. | Tier 3 |
| Server console | The interactive console of the running dedicated-server process; accepts admin commands as bare names, without the in-game forward-slash prefix. | Tier 3 |
| Self-targeting command | An admin command whose username argument defaults to the issuing admin when omitted in-game (e.g. `/additem`, `/godmode`, `/createhorde`); several require an explicit target from the server console. | Tier 3 |
| FIFO control socket | A named pipe exposed by a systemd socket unit that lets shell commands be sent to a running Project Zomboid server without an interactive console; the wiki disclaims any shutdown-safety guarantee for this method. | Tier 3 |
| Staging (mod rollout) | Running a candidate mod-list change against a non-production copy of the world (or a fresh throwaway world) before applying the same change to the live server's configuration. | — |
| Freeze / pin (mods) | Deliberately preventing a mod from updating on a running server, either by restart discipline or by vendoring a mod's files locally in place of the Workshop auto-fetch path. | — |
| Red mod | The client mod manager's visual indicator that an active mod is missing a dependency it declares via `require=`; the missing item is named on the mod's own Workshop page under "Required Items". | Tier 3 |
| Bifurcation testing | A documented method for isolating which mod among a large list causes a given problem, by repeatedly halving the active mod set and reproducing the issue against each half. | Tier 3 |

## Animals & world

| Term | Definition | Source |
|------|------------|--------|
| Livestock zone | A map zone within which livestock feed, drink and breed; farmsteads come with these pre-drawn, and moving animals elsewhere requires drawing one manually. | Tier 1 |
| Butcher hook | A workstation for butchering hanging animals, yielding more meat plus an unprocessed hide compared with ground butchering. | Tier 3 |
| Virtual animal | The off-screen representation of a wild-animal group migrating along a path; it spawns into real animals when a player approaches and reverts when they leave. | Tier 1 |
| maxWeight gene | The gene that sets an individual animal's real weight as a multiplier (typically 0.5–0.8, breed-dependent) of its species/stage base weight range. | Tier 3 |
| Canon starting towns | The Indie Stone's term for the four towns supporting occupation-specific spawn points on both builds: Muldraugh, West Point, Riverside and Rosewood. | Tier 1 |
| Map glow-up | The developers' name for the Build 42.20 map overhaul that entirely reworked seven existing areas (Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron, Dixie) to a new per-town art standard. | Tier 1 |
| Procedural basement | A Build 42 basement placed by generation rather than hand-building; B42 ships 400 procedural and 75 unique basements. | Tier 1 |
| Engine quality | Per-vehicle reliability score (max 100) rolled at spawn; sets start-failure chance (30 / (quality + 50)) and engine power, and can never be raised, unlike repairable engine condition. | Tier 3 |
| Vehicle class | One of three service families — standard, heavy-duty, sports — applied to whole vehicles and to individual parts; parts never fit across classes. | Tier 3 |
| Recipe magazine (Laines manual) | One of three magazines (Standard, Commercial, Performance) that must be read before working on the matching vehicle class in the Mechanics menu, unless the character is a Mechanic. | Tier 3 |
| Hotwiring | Starting a vehicle without its key; requires Electrical 1 plus Mechanics 2, or the Burglar occupation. Failure damages nothing but can make noise. | Tier 3 |
| Electricity shutoff (ElecShut) | Sandbox event that permanently ends grid power (default window 14–30 days after the July 9, 1993 start date); afterwards gas pumps dispense only with generator power. | Tier 3 |

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
