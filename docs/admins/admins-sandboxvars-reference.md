---
id: admins-sandboxvars-reference
title: "SandboxVars Reference: Gameplay Rules per Server"
version: 1.0.0
status: approved
confidence: Medium
category: Admins
topic: "Server configuration"
build: both
document_type: server-setting
created: 2026-07-30
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [admins-foundation, admins-server-ini-reference, players-foundation, meta-style-guide]
tags: [sandboxvars, sandbox-options, server-config, zombie-lore, loot-rarity, xp-multiplier, b42, legacy41]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-sandboxvars-reference |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 |

# Executive Summary

Every Project Zomboid server carries its gameplay rulebook in a single Lua file, `<servername>_SandboxVars.lua`, generated next to the server's `.ini` under `Zomboid/Server` in the hosting user's home directory [9]. Where the `.ini` decides how the server runs (ports, mods, security), SandboxVars decides how the game plays: zombie behaviour and population, loot rarity, XP rates, when the water and power die, how fast crops grow, what condition the cars are in. This document is the per-key reference for that file on both supported builds, sourced from two revision-pinned wiki listings — the 42.20-era listing for Build 42 [5] and the archived Build 41 listing [6] — corroborated where possible against official patch notes [1] [2] [3].

The two builds do not speak the same dialect. The B41 file is `VERSION = 4` with a flat key set plus two nested tables; the 42.20 file is `VERSION = 6` and both larger and re-scaled [5] [6]. The operationally dangerous deltas: the zombie population scale was renumbered (a "Normal" count is `PopulationMultiplier = 0.65` on B42, where B41 used `1.0` [5] [6]), zombie respawn is zeroed out in the B42 generated defaults where B41 defaulted to respawn every 72 hours [5] [6], the B41 loot-rarity enums were replaced by per-category numeric multipliers, and the single B41 `XpMultiplier` became a per-skill `MultiplierConfig` table [5] [6]. Build 42 also adds whole new sandbox families — animals and vermin, basements, the in-game map, and firearm handling [5].

Document confidence is **Medium**: the B42 key set, defaults and ranges rest on a current, version-stamped wiki revision with several keys corroborated by official patch notes, but the B41 listing is an older example file whose enum comments conflict in places with the B41 sandbox-UI documentation, and no game-file diff has been run first-hand. Where the B41 evidence is thin this document says so instead of guessing.

# Key Takeaways

- One file per server name — `<servername>_SandboxVars.lua` beside the `.ini`; the server generates it with defaults if missing, and mods' own sandbox options live in the same `SandboxVars` namespace *(cited)* *(both)*
- The B42 population scale is renumbered: Normal = 0.65, Insane = 2.5 (`ZombieConfig.PopulationMultiplier`), against B41's Normal = 1.0, Insane = 4.0 — never copy a B41 population number onto a B42 server *(cited)*
- The 42.20 generated file disables zombie respawn (`ZombieRespawn` = None; `RespawnHours`, `RespawnUnseenHours`, `RespawnMultiplier` all 0), where B41 defaulted to respawn every 72 hours — on B42 you must opt in *(cited)*
- Loot rarity moved from B41 enum steps (`FoodLoot` etc.) to ~21 per-category numeric multipliers (`FoodLootNew` etc., 0–4) plus six tier-factor keys *(cited)*
- XP tuning moved from the single `XpMultiplier` to `MultiplierConfig` with a `Global` value, a `GlobalToggle`, and ~35 per-skill keys using internal names (`Woodwork` = Carpentry, `Doctor` = First Aid, `PlantScavenging` = Foraging) *(cited)* *(B42)*
- Basements are sandbox-controlled on B42 — `Basement.SpawnFrequency` — and animals/wildlife get a 16-key family *(cited)* *(B42)*
- Several options migrated from `server.ini` into SandboxVars between builds, including `MinutesPerPage`, `HoursForCorpseRemoval` and the loot-respawn trio *(cited)*
- Whether SandboxVars edits can be applied without a full server stop is contested; only a `.ini` live-reload path is documented — see the quarantined discussion in `admins-foundation` *(community, unverified)*

# Purpose

This is the Admins-track key reference for the gameplay half of server configuration. It answers: which key controls a given rule, what type and range it accepts, what the generated default is on each build, which keys exist on only one build, and which popular values are folklore rather than documented fact. It exists so an admin can edit `servertest_SandboxVars.lua` with a text editor and a citation, instead of a half-remembered B41 guide.

# Scope

Covered: every key present in the two revision-pinned SandboxVars listings — the full 42.20-era file documented at wiki revision 1443167 [5] and the flat-plus-nested key set in the archived B41-era revision 1393223 [6] — organized by area: population, zombie lore, loot, XP and character, world clock and utilities, nature and farming, vehicles, and the B42-only families (animals/wildlife, basements, map, firearms). Where a rule is exposed in the B41 sandbox UI but its Lua key is not pinned by a cited listing, that gap is stated, not papered over.

Not covered: the `server.ini` key set (see `admins-server-ini-reference`), spawnpoint/spawnregion Lua files, RCON/admin command operations, mod-defined sandbox options beyond how they attach to this file, and per-key gameplay deep-dives (the Players track owns mechanic behaviour). The B41 column documents the archived listing as-is; it is not a first-hand dump of a 41.78.16 install.

# Definitions

- **SandboxVars** — the Lua table serialized in `<servername>_SandboxVars.lua`; the server's gameplay-rule settings, distinct from the `.ini` server settings [5] [9].
- **Enum (coded option)** — a multiple-choice option stored as a 1-based integer code; the meaning of each code is fixed per key (e.g. `ZombieLore.Speed` code 1 means Sprinters) [5].
- **`ZombieLore`** — the nested table of zombie behaviour settings (speed, strength, transmission, senses) [5] [6].
- **`ZombieConfig`** — the nested table of population-model settings (multipliers, respawn, grouping) [5] [6].
- **`MultiplierConfig`** — the B42-only nested table of XP multipliers, one key per skill plus a global pair [5].
- **`VERSION`** — the schema stamp at the top of the file; the game uses it to migrate older files. It is 4 in the archived B41 listing and 6 in the 42.20 listing [5] [6].
- **Generated default** — the value the server writes when it creates the file itself; defaults quoted in this document are the 42.20 generated values unless tagged otherwise [5] [9].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | Archived wiki listing, page versioned 41.78.19 [6]; B41 sandbox-UI docs [7] | Served from the `legacy41` branch since 42.20 went stable [4]; B41-only keys tagged *(B41)* |
| B42 (stable) | Yes | Wiki revision versioned 42.20.0 [5]; 42.20.1-42.21 patch notes reviewed [10] [11] [12] | Key names corroborated in official 42.17–42.20 patch notes [1] [2] [3]; B42-only keys tagged *(B42)*; 42.21 has been stable since 2026-09-28 [11] |

**42.21 re-check scope.** Re-checked: the official 42.21 unstable and stable Steam notes [10] [11] and the TIS forum 42.21 changelist [12] were read for any SandboxVars key, default or range change; none is named in them, and the 42.20.1-42.20.4 hotfix notes were also read with the same result. Not re-checked: the key list, defaults and ranges are still the wiki rendering at revision 1443167 [5] and were not re-extracted from a 42.21 server install. Everything not mentioned below is carried forward from 42.20 with no contradicting change found, not re-tested.

The B42 listing is version-stamped 42.20.0 [5]. The B41 listing is an archived page revision whose SandboxVars block carries `VERSION = 4` and some enum comments that disagree with the B41 sandbox-UI documentation [6] [7]; treat its enum numbering as indicative, and its key names as the reliable part.

# Reference

## The file: location, generation, and shape

The file lives at `%USERPROFILE%\Zomboid\Server` (Windows) or `~/Zomboid/Server` (Linux), named after the server (`servertest_SandboxVars.lua` by default), and is plain-text editable [9]. If it is absent at startup, the server writes one with default values [9]. Live values can be inspected with the `showoptions` admin command; the documented live-reload path (`reloadoptions`) is described for the `.ini` only [9]. The file is a single Lua assignment, `SandboxVars = { ... }`, opening with the schema stamp `VERSION` — 4 in the archived B41 listing, 6 at 42.20 [5] [6]. Most keys sit at the top level; behaviour families nest in sub-tables (`ZombieLore`, `ZombieConfig`, and on B42 also `Map`, `Basement`, `MultiplierConfig`), which this document writes in dotted form, e.g. `ZombieLore.Speed` [5] [6]. Mods extend the same namespace: a mod's `sandbox-options.txt` defines `option ModName.OptionName` entries that are read and written as `SandboxVars.ModName.OptionName`, with types boolean, integer, double, string and enum [8]. Enum options are stored as 1-based integer codes [5] [8].

Recurring coded scales, abbreviated in the tables below (codes in parentheses) [5]:

| Scale | Coded values |
|-------|--------------|
| S-FREQ6 | Never (1), Extremely Rare (2), Rare (3), Sometimes (4), Often (5), Very Often (6) |
| S-STORY7 | S-FREQ6 plus Always Tries (7) |
| S-RATE5 | Very Fast (1), Fast (2), Normal (3), Slow (4), Very Slow (5) |
| S-ANIM6 | Ultra Fast (1), then S-RATE5 as codes 2–6 |
| S-LEVEL5 | Very Low (1), Low (2), Normal (3), High (4), Very High (5) |
| S-ABUND5 | Very Poor (1), Poor (2), Normal (3), Abundant (4), Very Abundant (5) |

Column key for all tables in this section: **Default** is the 42.20 generated value [5] unless the Build column says B41, in which case it comes from the archived listing [6] or the B41 UI docs [7]; **Build** states where the key name is pinned by a cited listing.

## Top-level control and the population dial

The quick population controls sit at the top of the file; the fine-grained model lives in `ZombieConfig` below [5] [6].

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `VERSION` | integer | 6 | schema stamp | both | 4 in the archived B41 listing [6]; do not hand-edit |
| `Zombies` | enum | 4 | codes 1–6, most to none: Insane, Very High, High, Normal, Low, None | both | Sets the population preset; archived B41 comment describes a five-step scale [6], the B41 UI shows six counts [7] |
| `Distribution` | enum | 1 | Urban Focused (1), Uniform (2) | both | Where the population concentrates [5] [6] |
| `ZombieVoronoiNoise` | boolean | true | true/false | B42 | Adds randomization to the distribution pattern [5] |
| `ZombieRespawn` | enum | 4 | High (1), Normal (2), Low (3), None (4) | B42 | Master respawn preset; generated default is None [5] |
| `ZombieMigrate` | boolean | true | true/false | B42 | Lets zombies drift into empty cells [5] |

## Dynamic population: `ZombieConfig`

**42.21 note (B42).** The 42.21 notes record fixes for zombies disappearing after a player left and re-entered a chunk (single-player and multiplayer) and for several zombie-duplication cases in multiplayer; the stable announcement says some instances remain and are slated for the next update [10] [11] [12]. These are behaviour fixes: the notes change no population or respawn key, so the tables below are unchanged.

The multiplier-to-preset mappings differ per build. On B42 a Normal count is 0.65, with Low at 0.15, High at 1.2, Very High at 1.6, Insane at 2.5 and None at zero [5]; on B41 a Normal count is 1.0, with Low at 0.35, High at 2.0, Insane at 4.0 and None at zero [6] [7].

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `ZombieConfig.PopulationMultiplier` | double | 0.65 | 0–4 | both | B41 default 1.0 [6] [7]; scale renumbered on B42 [5] |
| `ZombieConfig.PopulationStartMultiplier` | double | 1.0 | 0–4 | both | Day-one population scaling [5] [6] |
| `ZombieConfig.PopulationPeakMultiplier` | double | 1.5 | 0–4 | both | Population scaling at the peak day [5] [6] |
| `ZombieConfig.PopulationPeakDay` | integer | 28 | 1–365 | both | In-game day the population crests [5] [6] |
| `ZombieConfig.RespawnHours` | double | 0.0 | 0–8760 | both | Hours between respawn waves per cell; 0 disables. B41 default 72 [6] [7] |
| `ZombieConfig.RespawnUnseenHours` | double | 0.0 | 0–8760 | both | Chunk must go unseen this long first. B41 default 16 [6] [7] |
| `ZombieConfig.RespawnMultiplier` | double | 0.0 | 0–1 | both | Fraction of a cell's target population returned per wave. B41 default 0.1 [6] [7] |
| `ZombieConfig.RedistributeHours` | double | 12.0 | 0–8760 | both | Intra-cell migration interval; 0 disables [5] [6] |
| `ZombieConfig.FollowSoundDistance` | integer | 100 | 10–1000 | both | How far a zombie walks toward the last heard sound [5] [6] |
| `ZombieConfig.RallyGroupSize` | integer | 20 | 0–1000 | both | Idle group size; 0 = no grouping; none indoors or in forest zones [5] [6] |
| `ZombieConfig.RallyGroupSizeVariance` | integer | 50 | 0–100 | B42 | Percent spread around the group size [5] |
| `ZombieConfig.RallyTravelDistance` | integer | 20 | 5–50 | both | Distance travelled to join a group [5] [6] |
| `ZombieConfig.RallyGroupSeparation` | integer | 15 | 5–25 | both | Spacing between groups [5] [6] |
| `ZombieConfig.RallyGroupRadius` | integer | 3 | 1–10 | both | Cohesion around the group leader [5] [6] |
| `ZombieConfig.ZombiesCountBeforeDelete` | integer | 300 | 0–5000 | B42 | Cleanup threshold; in-file warning to keep the default; ceiling raised from 500 to 5000 at 42.20 [1] [5] |

## Zombie behaviour: `ZombieLore`

B42 defaults lean on randomness: Speed and Toughness default to Random, Sight and Hearing to a Normal-to-Poor random band [5], where the B41 Apocalypse preset used fixed Fast Shamblers / Normal senses [7].

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `ZombieLore.Speed` | enum | 4 | Sprinters (1), Fast Shamblers (2), Shamblers (3), Random (4) | both | Archived B41 comment lists only codes 1–3 [6]; the B41 UI includes Random [7] |
| `ZombieLore.SprinterPercentage` | integer | 0 | 0–100 | B42 | Share of sprinters when Speed is Random [5] |
| `ZombieLore.Strength` | enum | 2 | Superhuman (1), Normal (2), Weak (3), Random (4) | both | Attack damage and skin-break odds [5] [6] |
| `ZombieLore.Toughness` | enum | 4 | Tough (1), Normal (2), Fragile (3), Random (4) | both | Kill difficulty [5] [6] |
| `ZombieLore.Transmission` | enum | 1 | Blood and Saliva (1), Saliva Only (2), Everyone's Infected (3), None (4) | both | Knox Event vector; code 3 reanimates every death [5] [6] |
| `ZombieLore.Mortality` | enum | 5 | Instant (1) through 1–2 Weeks (6), Never (7) | both | Time for infection to kill; archived B41 comment shows six codes, the B41 UI also lists Never [6] [7] |
| `ZombieLore.Reanimate` | enum | 3 | Instant (1) through 1–2 Weeks (6) | both | Corpse-rise delay [5] [6] |
| `ZombieLore.Cognition` | enum | 3 | Navigate and Use Doors (1), Navigate (2), Basic Navigation (3), Random (4) | both | Pathing intelligence [5] [6] |
| `ZombieLore.DoorOpeningPercentage` | integer | 0 | 0–100 | B42 | Share of door-capable zombies [5] |
| `ZombieLore.CrawlUnderVehicle` | enum | 5 | Crawlers Only (1), then S-FREQ6-style codes 2–6, Always (7) | B42 | B41 UI exposes the same option; Lua key not pinned for B41 [5] [7]. An "always" bug was fixed in 42.17 [3] |
| `ZombieLore.Memory` | enum | 2 | Long (1), Normal (2), Short (3), None (4), Random (5), Random Normal-to-None (6) | both | B41 listing covers codes 1–4 only [5] [6] |
| `ZombieLore.Sight` | enum | 5 | Eagle (1), Normal (2), Poor (3), Random (4), Random Normal-to-Poor (5) | both | B41 listing covers codes 1–3 [5] [6] |
| `ZombieLore.Hearing` | enum | 5 | Pinpoint (1), Normal (2), Poor (3), Random (4), Random Normal-to-Poor (5) | both | B41 listing covers codes 1–3 [5] [6] |
| `ZombieLore.Smell` | enum | — | Bloodhound (1), Normal (2), Poor (3) | B41 | Absent from the 42.20 listing [5] [6] |
| `ZombieLore.Decomp` | enum | — | Slows and weakens (1) through No Effect (4) | B41 | Decomposition effect; absent from the 42.20 listing [5] [6] |
| `ZombieLore.SpottedLogic` | boolean | true | true/false | B42 | Advanced stealth/visibility model [5] |
| `ZombieLore.ThumpNoChasing` | boolean | false | true/false | both | Idle zombies attack doors/constructions [5] [6] |
| `ZombieLore.ThumpOnConstruction` | boolean | true | true/false | both | Player builds can be damaged [5] [6] |
| `ZombieLore.ActiveOnly` | enum | 1 | Both (1), Night (2), Day (3) | both | When zombies are at full activity [5] [6] |
| `ZombieLore.TriggerHouseAlarm` | enum-or-bool | true | true/false | both | 42.20 file has it on; the B41 UI documents it default-off [5] [7] |
| `ZombieLore.ZombiesDragDown` | boolean | true | true/false | both | Group drag-down kills [5] [6] |
| `ZombieLore.ZombiesCrawlersDragDown` | boolean | false | true/false | B42 | Crawlers count toward drag-down [5] |
| `ZombieLore.ZombiesFenceLunge` | boolean | true | true/false | both | Post-climb lunge [5] [6] |
| `ZombieLore.ZombiesArmorFactor` | double | 2.0 | 0–100 | B42 | Effectiveness multiplier for zombie-worn protection [5] |
| `ZombieLore.ZombiesMaxDefense` | integer | 85 | 0–100 | B42 | Cap on zombie garment defense percent [5] |
| `ZombieLore.ChanceOfAttachedWeapon` | integer | 6 | 0–100 | B42 | Percent with a holstered/attached item [5] |
| `ZombieLore.ZombiesFallDamage` | double | 1.0 | 0–100 | B42 | Fall-damage multiplier for zombies [5] |
| `ZombieLore.DisableFakeDead` | enum | 1 | World Zombies (1), World and Combat Zombies (2), Never (3) | B42 | Which "playing dead" zombies exist; B41 UI has a three-way equivalent [5] [7] |
| `ZombieLore.PlayerSpawnZombieRemoval` | enum | 1 | Building and surroundings (1), Building (2), Room (3), Anywhere (4) | B42 | Spawn-safety clearing [5] |
| `ZombieLore.FenceThumpersRequired` | integer | 25 | -1–100 | B42 | Zombies needed to damage a tall fence [5] |
| `ZombieLore.FenceDamageMultiplier` | double | 1.0 | 0.01–100 | B42 | Tall-fence damage rate [5] |

## Loot rarity and the world loot state

Build 41 stored loot rarity as enum steps; the archived listing shows `FoodLoot`, `WeaponLoot` and `OtherLoot` with a rare-to-abundant comment scale [6], and the B41 UI documents seven steps (None through Abundant) across ten categories [7]. Build 42 replaces this with per-category numeric multipliers (`0–4`, higher = more) plus six tier-factor keys that define what each named rarity tier means numerically [5].

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `FoodLoot` | enum | — | rare (1) to abundant (5) per archived comment; the B41 UI shows 7 steps | B41 | Perishable food [6] [7] |
| `WeaponLoot` | enum | — | as `FoodLoot` | B41 | Weapons [6] [7] |
| `OtherLoot` | enum | — | as `FoodLoot` | B41 | Everything uncategorized [6] [7] |
| `LootRespawn` | enum | — | None (1), Every Day (2), Every Week (3), Every Month (4), Every Two Months (5) | B41 | All presets default None [6] [7] |
| `FoodLootNew` | double | 0.8 | 0–4 | B42 | Perishable food [5] |
| `CannedFoodLootNew` | double | 0.6 | 0–4 | B42 | Canned/dried food and drink [5] |
| `LiteratureLootNew` | double | 0.6 | 0–4 | B42 | Readables other than skill books [5] |
| `SkillBookLoot` | double | 0.6 | 0–4 | B42 | XP-multiplier books [5] |
| `RecipeResourceLoot` | double | 0.6 | 0–4 | B42 | Recipe-teaching items [5] |
| `MedicalLootNew` | double | 0.6 | 0–4 | B42 | First-aid items [5] |
| `SurvivalGearsLootNew` | double | 0.6 | 0–4 | B42 | Camping/outdoor gear [5] |
| `WeaponLootNew` | double | 0.6 | 0–4 | B42 | Melee weapons not in other tool families [5] |
| `RangedWeaponLootNew` | double | 1.2 | 0–4 | B42 | Firearms and attachments [5] |
| `AmmoLootNew` | double | 0.6 | 0–4 | B42 | Ammo, boxes, magazines [5] |
| `MechanicsLootNew` | double | 0.6 | 0–4 | B42 | Vehicle parts and their tools [5] |
| `ClothingLootNew` | double | 0.6 | 0–4 | B42 | Non-container wearables [5] |
| `ContainerLootNew` | double | 0.6 | 0–4 | B42 | Bags and wearable containers [5] |
| `KeyLootNew` | double | 0.4 | 0–4 | B42 | Keys, key rings, locks [5] |
| `MediaLootNew` | double | 0.6 | 0–4 | B42 | Tapes and discs [5] |
| `MementoLootNew` | double | 0.6 | 0–4 | B42 | Collectibles and keepsakes [5] |
| `CookwareLootNew` | double | 0.6 | 0–4 | B42 | Cooking implements [5] |
| `MaterialLootNew` | double | 0.6 | 0–4 | B42 | Crafting/building ingredients [5] |
| `FarmingLootNew` | double | 0.6 | 0–4 | B42 | Agriculture items [5] |
| `ToolLootNew` | double | 0.6 | 0–4 | B42 | General tools [5] |
| `OtherLootNew` | double | 0.8 | 0–4 | B42 | Fallback category; also scales Town/Road-zone foraging [5] |
| `InsaneLootFactor` | double | 0.05 | 0–0.2 | B42 | Numeric meaning of the Insanely Rare tier [5] |
| `ExtremeLootFactor` | double | 0.2 | 0.05–0.6 | B42 | Extremely Rare tier [5] |
| `RareLootFactor` | double | 0.6 | 0.2–1 | B42 | Rare tier [5] |
| `NormalLootFactor` | double | 1.0 | 0.6–2 | B42 | Normal tier [5] |
| `CommonLootFactor` | double | 2.0 | 1–3 | B42 | Common tier [5] |
| `AbundantLootFactor` | double | 3.0 | 2–4 | B42 | Abundant tier [5] |
| `RollsMultiplier` | double | 1.0 | 0.1–100 | B42 | Loot-table roll count; in-file warning: leave alone, performance-sensitive [5] |
| `LootItemRemovalList` | string | "" | comma-separated item types | B42 | Items barred from ordinary loot [5] |
| `RemoveStoryLoot` | boolean | false | true/false | B42 | Extends the bar to world stories [5] |
| `RemoveZombieLoot` | boolean | false | true/false | B42 | Extends the bar to zombie-carried loot [5] |
| `ZombiePopLootEffect` | integer | 0 | 0–20 | B42 | Scales loot up with nearby zombie density [5] |
| `SeenHoursPreventLootRespawn` | integer | 0 | 0 to max int | both | Blocks respawn in recently seen zones; a B41 UI option, pinned as a sandbox key at 42.20 [5] [7] |
| `HoursForLootRespawn` | integer | 0 | 0 to max int | both | Hours before looted town containers refill; 0 = never. A `server.ini` key on B41 [5] [6] |
| `MaxItemsForLootRespawn` | integer | 5 | 0 to max int | both | Containers at or above this count are skipped. A `server.ini` key on B41 (default 4) [5] [6] |
| `ConstructionPreventsLootRespawn` | boolean | true | true/false | both | Player-built/barricaded buildings excluded. A `server.ini` key on B41 [5] [6] |
| `MaximumLooted` | integer | 25 | 0–200 | B42 | Chance a found building spawns pre-looted [5] |
| `DaysUntilMaximumLooted` | integer | 90 | 0–3650 | B42 | Ramp time for the pre-looted chance [5] |
| `RuralLooted` | double | 0.5 | 0–2 | B42 | Pre-looted scaling for rural buildings [5] |
| `MaximumDiminishedLoot` | integer | 20 | 0–100 | B42 | Peak percentage of loot withheld over time [5] |
| `DaysUntilMaximumDiminishedLoot` | integer | 3650 | 0–3650 | B42 | Ramp time for diminished loot [5] |
| `MaximumLootedBuildingRooms` | integer | 50 | 0–200 | B42 | Buildings larger than this are never pre-looted [5] |

## XP and character progression

Build 41 tunes XP with one key; Build 42 tunes it per skill. The B42 `MultiplierConfig` skill keys are internal identifiers, several of which differ from the UI skill names — the notes column gives the display name where they differ [5]. The B41 UI also documents an "XP Multiplier Affects Passive Skills" toggle (default off) whose Lua key is not present in the archived listing, so it is deliberately not tabled here [6] [7].

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `XpMultiplier` | double | 1 | 0.001–1000 | B41 | Single global XP rate [6] [7] |
| `MultiplierConfig.Global` | double | 1.0 | 0–1000 | B42 | Whole-game XP rate [5] |
| `MultiplierConfig.GlobalToggle` | boolean | true | true/false | B42 | When true, `Global` overrides the per-skill keys [5] |
| `MultiplierConfig.Fitness` | double | 1.0 | 0–1000 | B42 | Passive: Fitness [5] |
| `MultiplierConfig.Strength` | double | 1.0 | 0–1000 | B42 | Passive: Strength [5] |
| `MultiplierConfig.Sprinting` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Lightfoot` | double | 1.0 | 0–1000 | B42 | Display name: Lightfooted [5] |
| `MultiplierConfig.Nimble` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Sneak` | double | 1.0 | 0–1000 | B42 | Display name: Sneaking [5] |
| `MultiplierConfig.Axe` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Blunt` | double | 1.0 | 0–1000 | B42 | Display name: Long Blunt [5] |
| `MultiplierConfig.SmallBlunt` | double | 1.0 | 0–1000 | B42 | Display name: Short Blunt [5] |
| `MultiplierConfig.LongBlade` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.SmallBlade` | double | 1.0 | 0–1000 | B42 | Display name: Short Blade [5] |
| `MultiplierConfig.Spear` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Maintenance` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Woodwork` | double | 1.0 | 0–1000 | B42 | Display name: Carpentry [5] |
| `MultiplierConfig.Cooking` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Farming` | double | 1.0 | 0–1000 | B42 | Display name: Agriculture [5] |
| `MultiplierConfig.Doctor` | double | 1.0 | 0–1000 | B42 | Display name: First Aid [5] |
| `MultiplierConfig.Electricity` | double | 1.0 | 0–1000 | B42 | Display name: Electrical [5] |
| `MultiplierConfig.MetalWelding` | double | 1.0 | 0–1000 | B42 | Display name: Welding [5] |
| `MultiplierConfig.Mechanics` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Tailoring` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Aiming` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Reloading` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Fishing` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Trapping` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.PlantScavenging` | double | 1.0 | 0–1000 | B42 | Display name: Foraging [5] |
| `MultiplierConfig.FlintKnapping` | double | 1.0 | 0–1000 | B42 | Display name: Knapping [5] |
| `MultiplierConfig.Masonry` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Pottery` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Carving` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Husbandry` | double | 1.0 | 0–1000 | B42 | Display name: Animal Care [5] |
| `MultiplierConfig.Tracking` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Blacksmith` | double | 1.0 | 0–1000 | B42 | Display name: Blacksmithing [5] |
| `MultiplierConfig.Butchering` | double | 1.0 | 0–1000 | B42 | [5] |
| `MultiplierConfig.Glassmaking` | double | 1.0 | 0–1000 | B42 | [5] |
| `LevelForMediaXPCutoff` | integer | 3 | 0–10 | B42 | Skill level at which TV/VHS/media XP stops [5] |
| `LevelForDismantleXPCutoff` | integer | 0 | 0–10 | B42 | Level at which furniture-scrapping XP stops; Electrical exempt [5] |
| `StatsDecrease` | enum | 3 | S-RATE5 | both | Hunger/thirst/fatigue drain [5] [6] |
| `EndRegen` | enum | 3 | S-RATE5 | both | Endurance recovery [5] [6] |
| `StarterKit` | boolean | false | true/false | both | Spawn kit: bag, bat, hammer, water, chips [5] [6] |
| `Nutrition` | boolean | true | true/false | both | Food nutrition affects the body; off freezes weight change [5] [6] |
| `CharacterFreePoints` | integer | 0 | -100–100 | B42 | Extra creation points; B41 UI equivalent is "Free Traits" [5] [7] |
| `ConstructionBonusPoints` | enum | 3 | S-LEVEL5 | B42 | Hit points of player builds; B41 UI equivalent exists [5] [7] |
| `InjurySeverity` | enum | 2 | Low (1), Normal (2), High (3) | B42 | Injury impact and healing time [5] [7] |
| `BoneFracture` | boolean | true | true/false | B42 | Fractures from falls/impacts/zombies [5] [7] |
| `ClothingDegradation` | enum | 3 | Disabled (1), Slow (2), Normal (3), Fast (4) | B42 | Wear, dirt and blood on clothing [5] [7] |
| `RearVulnerability` | enum | 3 | Low (1), Medium (2), High (3) | B42 | Bite odds from behind [5] [7] |
| `MultiHitZombies` | boolean | false | true/false | B42 | Melee swings can strike several targets; B41 UI equivalent exists [5] [7] |
| `AttackBlockMovements` | boolean | true | true/false | B42 | Swinging slows movement; B41 UI equivalent exists [5] [7] |
| `AllClothesUnlocked` | boolean | false | true/false | B42 | Full wardrobe at creation; the B41 UI documents its equivalent default-on [5] [7] |
| `EnablePoisoning` | enum | 1 | True (1), False (2), Bleach only disabled (3) | B42 | Food poisoning rules; B41 UI equivalent exists [5] [7] |
| `NegativeTraitsPenalty` | enum | 1 | None (1) to a per-trait penalty (4) | B42 | Diminishing returns on negative-trait points [5] |
| `MinutesPerPage` | double | 2.0 | 0–60 | both | Reading speed per skill-book page; a `server.ini` key on B41 (default 1.0) [5] [6] |
| `LiteratureCooldown` | integer | 45 | 1–365 | B42 | Days before re-reading gives benefits again [5] |
| `MuscleStrainFactor` | double | 0.7 | 0–10 | B42 | Muscle-strain multiplier [5] |
| `DiscomfortFactor` | double | 0.8 | 0–10 | B42 | Worn-item discomfort multiplier [5] |
| `WoundInfectionFactor` | double | 1.0 | 0–10 | B42 | Wound-infection damage scaling; the 42.20 notes rebalance it (as "WouldInfectionFactor") for the Extinction preset [1] [5] |
| `EasyClimbing` | boolean | false | true/false | B42 | Removes climb-failure chances [5] |
| `NoBlackClothes` | boolean | true | true/false | B42 | Keeps random clothing tints out of near-black [5] |

## World clock, utilities shut-off, and world events

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `DayLength` | enum | 4 | 27 codes: 15 min (1), 30 min (2), 1 h (3), 1 h 30 (4), then hourly to 23 h, Real-time (27) | both | 42.20 default is 1 h 30 [5]; the archived B41 comment shows a nine-step scale ending in real-time [6] |
| `StartYear` | integer | 1 | 1 = first year | both | [5] [6] |
| `StartMonth` | enum | 7 | January (1) to December (12) | both | July default; affects weather, foraging, farming [5] [6] [7] |
| `StartDay` | integer | 9 | day of month | both | [5] [6] |
| `StartTime` | enum | 2 | 7 AM (1), 9 AM (2), 12 PM (3), 2 PM (4), 5 PM (5), 9 PM (6), 12 AM (7), 2 AM (8), 5 AM (9) | both | [5] [6] |
| `DayNightCycle` | enum | 1 | Normal (1), Endless Day (2), Endless Night (3) | B42 | Clock override [5] |
| `ClimateCycle` | enum | 1 | Normal (1), No Weather (2), Endless Rain (3), Endless Storm (4), Endless Snow (5), Endless Blizzard (6) | B42 | Weather override [5] |
| `FogCycle` | enum | 1 | Normal (1), No Fog (2), Endless Fog (3) | B42 | Fog override [5] |
| `NightLength` | enum | 3 | Always Night (1), Long (2), Normal (3), Short (4), Always Day (5) | B42 | Dusk-to-dawn span [5] |
| `NightDarkness` | enum | 3 | Pitch Black (1), Dark (2), Normal (3), Bright (4) | B42 | Ambient night light; B41 UI equivalent exists [5] [7] |
| `WaterShut` | enum | 2 | Instant (1), 0–30 d (2), 0–2 m (3), 0–6 m (4), 0–1 y (5), 0–5 y (6), 2–6 m (7), 6–12 m (8), Disabled (9) | both | Plumbing cutoff window; Disabled (9) is B42-listed [5] [6] |
| `ElecShut` | enum | 2 | Instant (1), 14–30 d (2), then 14-day-floored windows to 5 y (6), 2–6 m (7), 6–12 m (8), Disabled (9) | both | Grid cutoff; the B42 windows start at day 14 [5] [6] |
| `WaterShutModifier` | integer | 14 | -1 to max int | both | Day offset for the water cutoff; archived B41 comment reads it as days-until-shutoff, -1 = instant [5] [6]; key named in the 42.17 notes [3] |
| `ElecShutModifier` | integer | 14 | -1 to max int | both | As above for electricity [5] [6]; key named in the 42.17 notes [3] |
| `AlarmDecay` | enum | 2 | Instant (1), 0–30 d (2), 0–2 m (3), 0–6 m (4), 0–1 y (5), 0–5 y (6) | B42 | How long alarm batteries outlive the grid [5] |
| `AlarmDecayModifier` | integer | 14 | -1 to max int | B42 | Day offset for alarm decay [5] |
| `TimeSinceApo` | enum | 1 | 0 months (1) through 12 months (13) | both | World age at start; drives starting erosion and food age [5] [6] [7] |
| `Alarm` | enum | 4 | S-FREQ6 | both | Burglar-alarm frequency on break-ins [5] [6] |
| `LockedHouses` | enum | 6 | S-FREQ6 | both | Locked-door frequency [5] [6] |
| `FoodRotSpeed` | enum | 3 | S-RATE5 | both | Spoilage rate [5] [6] |
| `FridgeFactor` | enum | 3 | S-LEVEL5 plus No Decay (6) | both | Refrigeration strength; code 6 is B42-listed [5] [6] |
| `DaysForRottenFoodRemoval` | integer | -1 | -1 to max int | B42 | Rotten-food cleanup; -1 keeps it forever; B41 UI equivalent exists [5] [7] |
| `FireSpread` | boolean | true | true/false | B42 | Fire propagation; B41 UI equivalent exists [5] [7] |
| `HoursForWorldItemRemoval` | double | 24.0 | 0 to max int | B42 | Ground-item cleanup age; applies on chunk load [5] |
| `WorldItemRemovalList` | string | "Base.Hat,Base.Glasses,Base.Maggots,Base.Slug,Base.Slug2,Base.Snail,Base.Worm,Base.Dung_Mouse,Base.Dung_Rat" | comma-separated item types | B42 | Cleanup list; the B41 UI documents a three-item default [5] [7] |
| `ItemRemovalListBlacklistToggle` | boolean | false | true/false | B42 | Inverts the list into a keep-list [5] |
| `HoursForCorpseRemoval` | double | 216.0 | -1 to max int | B42 | Corpse cleanup; at 0 no maggots spawn; formerly a server option per the B41 UI docs [5] [7] |
| `DecayingCorpseHealthImpact` | enum | 3 | None (1), Low (2), Normal (3), High (4), Insane (5) | B42 | Corpse-sickness pressure; B41 UI equivalent has four steps [5] [7] |
| `ZombieHealthImpact` | boolean | false | true/false | B42 | Extends corpse sickness to nearby active zombies [5] |
| `BloodLevel` | enum | 3 | None (1), Low (2), Normal (3), High (4), Ultra Gore (5) | B42 | Gore decals; B41 UI equivalent exists [5] [7] |
| `BloodSplatLifespanDays` | integer | 0 | 0–365 | B42 | Blood cleanup age; 0 = permanent [5] |
| `MaggotSpawn` | enum | 1 | In and Around Bodies (1), In Bodies Only (2), Never (3) | B42 | B41 UI equivalent exists [5] [7] |
| `Helicopter` | enum | 2 | Never (1), Once (2), Sometimes (3), Often (4) | both | Event-zone flyovers [5] [6] [7] |
| `MetaEvent` | enum | 2 | Never (1), Sometimes (2), Often (3) | both | Off-screen sound events; the B41 UI shows a four-step list including Once [5] [7] |
| `SleepingEvent` | enum | 1 | Never (1), Sometimes (2), Often (3) | both | Night events while sleeping [5] [7] |
| `GeneratorSpawning` | enum | 4 | None (1), Insanely Rare (2), Extremely Rare (3), Rare (4), Normal (5), Common (6), Abundant (7) | both | 42.20 uses a rarity scale; the B41 UI shows a frequency scale defaulting Sometimes [5] [7] |
| `GeneratorFuelConsumption` | double | 0.1 | 0–100 | both | Fuel burn per hour; the B41 UI documents default 1 [5] [7] |
| `AllowExteriorGenerator` | boolean | true | true/false | both | Generators power exterior tiles (gas pumps) [5] [7] |
| `GeneratorTileRange` | integer | 20 | 1–100 | B42 | Horizontal supply radius [5] |
| `GeneratorVerticalPowerRange` | integer | 3 | 1–15 | B42 | Floors served above and below [5] |
| `LightBulbLifespan` | double | 2.0 | 0–1000 | B42 | Bulb life scaling; 0 = unbreakable; the B41 UI documents default 1.0 [5] [7] |
| `SurvivorHouseChance` | enum | 3 | S-STORY7 | B42 | Randomized-building stories; B41 UI equivalent uses S-FREQ6 [5] [7] |
| `VehicleStoryChance` | enum | 3 | S-STORY7 | B42 | Road stories such as roadblocks [5] [7] |
| `ZoneStoryChance` | enum | 3 | S-STORY7 | B42 | Zone stories such as forest camps [5] [7] |
| `AnnotatedMapChance` | enum | 4 | S-FREQ6 | both | Survivor-annotated maps [5] [7] |
| `MetaKnowledge` | enum | 3 | Fully revealed (1), Shown as unknown (2), Completely hidden (3) | B42 | Display of unseen media content [5] |
| `SeeNotLearntRecipe` | boolean | true | true/false | B42 | Station menus show unlearnt recipes [5] |
| `MaximumFireFuelHours` | integer | 8 | 1–168 | B42 | Fuel cap for campfires and stoves [5] |
| `EnableTaintedWaterText` | boolean | true | true/false | both | Tainted-water tooltip; a display bug against this option was fixed in 42.19 [2] [5] [7] |
| `EnableSnowOnGround` | boolean | true | true/false | both | Ground snow accumulation [5] [7] |
| `MaxFogIntensity` | enum | 1 | Normal (1), Moderate (2), Low (3), None (4) | both | Code 4 is B42-listed [5] [7] |
| `MaxRainFxIntensity` | enum | 1 | Normal (1), Moderate (2), Low (3) | both | Visual rain cap [5] [7] |
| `Temperature` | enum | 3 | Very Cold (1), Cold (2), Normal (3), Hot (4), Very Hot (5) | both | Global climate offset [5] [6] |
| `Rain` | enum | 3 | Very Dry (1), Dry (2), Normal (3), Rainy (4), Very Rainy (5) | both | Rainfall amount [5] [6] |

## Nature, farming, and erosion

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `ErosionSpeed` | enum | 4 | Very Fast 20 d (1), Fast 50 d (2), Normal 100 d (3), Slow 200 d (4), Very Slow 500 d (5) | both | Days to full overgrowth; 42.20 file ships Slow [5] [6] |
| `ErosionDays` | integer | 0 | -1–36500 | B42 | Exact-day override; 0 defers to `ErosionSpeed` [5] |
| `Farming` | enum | 3 | S-RATE5 | both | Crop growth speed [5] [6] |
| `FarmingSpeedNew` | double | 1.0 | 0.1–100 | B42 | Numeric growth-speed multiplier [5] |
| `FarmingAmountNew` | double | 1.0 | 0.1–10 | B42 | Numeric harvest-yield multiplier [5] |
| `PlantResilience` | enum | 3 | Very High (1), High (2), Normal (3), Low (4), Very Low (5) | both | Water loss and disease resistance; 42.20 codes run high-to-low [5] [6] |
| `PlantAbundance` | enum | 3 | S-ABUND5 | both | Harvest size [5] [6] |
| `NatureAbundance` | enum | 3 | S-ABUND5 | both | Foraging (and on B41, fishing) richness [5] [6] [7] |
| `FishAbundance` | enum | 2 | S-ABUND5 | B42 | Fish stocks split out from nature abundance [5] |
| `CompostTime` | enum | 2 | 1 wk (1), 2 wk (2), 3 wk (3), 4 wk (4), 6 wk (5), 8 wk (6), 10 wk (7), 12 wk (8) | both | Composter decay time [5] [7] |
| `KillInsideCrops` | boolean | true | true/false | B42 | Indoor crops and herbs die; houseplants exempt [5] |
| `PlantGrowingSeasons` | boolean | true | true/false | B42 | Seasonal growth rules [5] |
| `PlaceDirtAboveground` | boolean | false | true/false | B42 | Above-ground farming; in-file warning: performance risk [5] |
| `ClayLakeChance` | double | 0.05 | 0–1 | B42 | Clay-floor conversion odds at lakes [5] |
| `ClayRiverChance` | double | 0.05 | 0–1 | B42 | Clay-floor conversion odds at rivers [5] |

## Vehicles

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `EnableVehicles` | boolean | true | true/false | B42 | Vehicle spawning master switch; B41 UI equivalent exists [5] [7] |
| `CarSpawnRate` | enum | 3 | codes 1–5, none to high: None, Very Low, Low, Normal, High | B42 | The B41 UI shows a three-step scale [5] [7] |
| `VehicleEasyUse` | boolean | false | true/false | B42 | Unlocked, fuelled, keyless cars [5] [7] |
| `InitialGas` | enum | 2 | Very Low (1), Low (2), Normal (3), High (4), Very High (5), Full (6) | B42 | Tank level in found cars [5] [7] |
| `ChanceHasGas` | enum | 2 | Low (1), Normal (2), High (3) | B42 | Odds a found car has fuel at all [5] [7] |
| `FuelStationGasInfinite` | boolean | false | true/false | B42 | Bottomless pumps [5] |
| `FuelStationGasMin` | double | 0.0 | 0–1 | B42 | Pump fill floor; with max and empty-chance, replaces the B41 station-amount enum [5] [7] |
| `FuelStationGasMax` | double | 0.8 | 0–1 | B42 | Pump fill ceiling [5] |
| `FuelStationGasEmptyChance` | integer | 20 | 0–100 | B42 | Percent of pumps that start dry [5] |
| `CarGasConsumption` | double | 1.0 | 0–100 | B42 | Fuel-burn multiplier [5] [7] |
| `LockedCar` | enum | 4 | S-FREQ6 | B42 | Locked-door frequency [5] [7] |
| `CarGeneralCondition` | enum | 3 | S-LEVEL5 | B42 | Spawn condition [5] [7] |
| `CarDamageOnImpact` | enum | 3 | S-LEVEL5 | B42 | Crash damage to the car [5] [7] |
| `DamageToPlayerFromHitByACar` | enum | 1 | None (1), Low (2), Normal (3), High (4), Very High (5) | B42 | Pedestrian-strike damage [5] [7] |
| `PlayerDamageFromCrash` | boolean | true | true/false | B42 | Occupant crash injuries [5] [7] |
| `TrafficJam` | boolean | true | true/false | B42 | Wreck congestion on main roads [5] [7] |
| `CarAlarm` | enum | 3 | S-FREQ6 | B42 | Active-alarm frequency [5] [7] |
| `SirenShutoffHours` | double | 0.0 | 0–168 | B42 | Alarm-siren duration; 0 runs until the battery dies [5] [7] |
| `SirenEffectsZombies` | boolean | true | true/false | B42 | Sirens draw zombies [5] |
| `RecentlySurvivorVehicles` | enum | 2 | None (1), Low (2), Normal (3), High (4) | B42 | Maintained "survivor cars" [5] [7] |
| `ZombieAttractionMultiplier` | double | 1.0 | 0–100 | B42 | Engine-noise attraction scaling [5] [7] |

The B41 sandbox UI documents the same vehicle option family (enable, easy use, spawn rate, gas, locks, condition, alarms, sirens, crash damage) [7], but the archived B41 SandboxVars listing does not include vehicle keys, so no B41 Lua names are pinned here [6].

## Build 42 families: animals, wildlife, basements, map, firearms

Basements are confirmed sandbox-controlled on B42: random basement generation has its own nested table with a single frequency key [5].

| Key | Type | Default | Range / coded values | Build | Notes |
|-----|------|---------|----------------------|-------|-------|
| `Basement.SpawnFrequency` | enum | 4 | S-STORY7 | B42 | Random basement generation frequency [5] |
| `Map.AllowMiniMap` | boolean | false | true/false | B42 | Mini-map window [5] |
| `Map.AllowWorldMap` | boolean | true | true/false | B42 | World-map access [5] |
| `Map.MapAllKnown` | boolean | false | true/false | B42 | Full map revealed at start; an MP rejoin bug against this option was fixed in 42.19 [2] [5] |
| `Map.MapNeedsLight` | boolean | true | true/false | B42 | Reading maps requires light [5] |
| `AnimalStatsModifier` | enum | 4 | S-ANIM6 | B42 | Animal needs drain rate [5] |
| `AnimalMetaStatsModifier` | enum | 4 | S-ANIM6 | B42 | Same, for off-screen animals [5] |
| `AnimalPregnancyTime` | enum | 4 | S-ANIM6 | B42 | Gestation length [5] |
| `AnimalAgeModifier` | enum | 4 | S-ANIM6 | B42 | Aging speed [5] |
| `AnimalMilkIncModifier` | enum | 4 | S-ANIM6 | B42 | Milk accumulation rate [5] |
| `AnimalWoolIncModifier` | enum | 4 | S-ANIM6 | B42 | Wool growth rate [5] |
| `AnimalEggHatch` | enum | 4 | S-ANIM6 | B42 | Egg incubation speed [5] |
| `AnimalRanchChance` | enum | 5 | S-STORY7-style with Always (7) | B42 | Animals found at farms [5] |
| `AnimalGrassRegrowTime` | integer | 240 | 1–9999 | B42 | Hours for grazed/cut grass to return [5] |
| `AnimalMetaPredator` | boolean | false | true/false | B42 | Off-screen fox raids on open hutches [5] |
| `AnimalMatingSeason` | boolean | true | true/false | B42 | Restricts breeding to season [5] |
| `AnimalSoundAttractZombies` | boolean | true | true/false | B42 | Animal calls pull zombies [5] |
| `AnimalTrackChance` | enum | 4 | S-FREQ6 | B42 | Track generation for hunting [5] |
| `AnimalPathChance` | enum | 4 | S-FREQ6 | B42 | Huntable animal paths [5] |
| `MaximumRatIndex` | integer | 25 | 0–50 | B42 | Peak vermin infestation level [5] |
| `DaysUntilMaximumRatIndex` | integer | 90 | 0–365 | B42 | Ramp time to peak vermin [5] |
| `FirearmUseDamageChance` | enum | 2 | Disabled (1), Zombies Only (2), All Targets (3) | B42 | Chance-to-damage aiming model [5] |
| `FirearmNoiseMultiplier` | double | 1.0 | 0.2–2 | B42 | Gunshot audibility to zombies [5] |
| `FirearmJamMultiplier` | double | 1.0 | 0–10 | B42 | Jam odds; 0 disables jams [5] |
| `FirearmMoodleMultiplier` | double | 1.0 | 0–10 | B42 | Moodle penalty on hit chance [5] |
| `FirearmWeatherMultiplier` | double | 1.0 | 0–10 | B42 | Weather penalty on hit chance [5] |
| `FirearmHeadGearEffect` | boolean | true | true/false | B42 | Headgear (masks) affect aim [5] |

## Applying changes: what is actually documented

The documented workflow is: edit the file (or use the in-client Host settings editor saving under the server's name), start the server, and confirm with `showoptions` or by reading the files back [9]. The only documented while-running path is for the `.ini`: save, then run `reloadoptions` [9]. No equivalent live-reload is documented for `servertest_SandboxVars.lua` [9]. The widely repeated blanket rule that every config edit requires a full stop — and its justification that the server rewrites files at shutdown — is a contested community claim, quarantined as Claim 4 of `admins-foundation`; this document takes no position beyond what is cited here.

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Schema | `VERSION = 4`, flat keys plus `ZombieLore`/`ZombieConfig` [6] | `VERSION = 6`; adds `Map`, `Basement`, `MultiplierConfig` tables and roughly triples the key count [5] |
| Population scale | Normal = 1.0, Insane = 4.0 on `PopulationMultiplier` [6] [7] | Renumbered: Normal = 0.65, Insane = 2.5, plus a Very High step [5] |
| Respawn defaults | Respawn on by default: 72 h cycle, 16 h unseen, 0.1 fraction [6] [7] | Generated file disables respawn (`ZombieRespawn` None; hours/fraction zeroed); migration stays on at 12 h [5] |
| Loot rarity | Enum steps per category (`FoodLoot` etc.); `LootRespawn` enum; respawn modifiers in `server.ini` [6] [7] | Numeric multipliers 0–4 across ~21 categories, six tier-factor keys, roll multiplier, removal lists, density-scaled loot, and a world "already looted / diminishing loot" model; respawn keys moved into SandboxVars [5] |
| XP | Single `XpMultiplier` (0.001–1000) [6] [7] | `MultiplierConfig`: global value + toggle + ~35 per-skill keys under internal names; media/dismantle XP cutoffs added [5] |
| Zombie lore | Includes `Smell` and `Decomp`; fixed-value defaults; `TriggerHouseAlarm` documented off [6] [7] | Drops `Smell`/`Decomp`; adds sprinter/door percentages, stealth logic, zombie armor, fence-damage tuning, fake-dead and spawn-clearing controls; randomized speed/toughness/sense defaults; `TriggerHouseAlarm` on in the generated file [5] |
| Utilities | Water/electric windows with day modifiers [6] | Adds `AlarmDecay` pair; electric windows floored at day 14; both gain a Disabled code [5] |
| World clock | Nine-step day length per the archived comment [6] | 27-step day length defaulting 1 h 30; day/night, climate and fog cycle overrides; night length control [5] |
| Farming & nature | Enum speeds and abundances [6] | Adds numeric speed/yield multipliers, seasons, indoor-crop kill, clay chances, split fish abundance [5] |
| Vehicles | UI options documented; no Lua keys in the archived listing [6] [7] | Full key family pinned, including numeric pump-fill trio replacing the station-amount enum, and siren attraction [5] [7] |
| New families | — | Animals/wildlife (16 keys), vermin index, basements, in-game map table, firearm handling family, muscle strain/discomfort/wound factors [5] |
| Migrated from `server.ini` | `MinutesPerPage`, `HoursForLootRespawn`, `MaxItemsForLootRespawn`, `ConstructionPreventsLootRespawn` lived in the `.ini` [6] | All are SandboxVars keys at 42.20 [5]; corpse-removal hours likewise moved per the B41 UI docs [7] |

The short version: keep the two builds' files apart. A B41 SandboxVars pasted onto a B42 server carries wrong-scale population numbers, missing keys and stale enum meanings; the safe path is to regenerate on the target build and re-apply intent, not text [5] [6].

# Practical Guidance

- **Generate, then edit.** Let the server write its default file once, copy it, and change values from there — you inherit the correct `VERSION`, key set and per-build defaults instead of assembling a file from guides.
- **Decide respawn explicitly on B42.** The generated defaults mean a cleared block stays cleared. If you want B41-style pressure, set `ZombieRespawn` off None and give `RespawnHours` / `RespawnUnseenHours` / `RespawnMultiplier` real values — the B41 defaults (72 / 16 / 0.1) are a documented starting point.
- **Translate, don't copy, population numbers.** Convert B41 intent through the preset anchors: B41 1.0 (Normal) maps to B42 0.65; B41 4.0 (Insane) maps to B42 2.5. Setting `PopulationMultiplier = 1.0` on B42 is between Normal and High, not Normal.
- **Use internal names in `MultiplierConfig`.** The keys are `Woodwork`, `Doctor`, `PlantScavenging`, `Husbandry`, `Blacksmith`, `Lightfoot`, `Sneak`, `Blunt`, `SmallBlade` — not the UI names. And remember `GlobalToggle`: while it is true, per-skill values are overridden by `Global`.
- **Respect the in-file warnings.** `RollsMultiplier`, `PlaceDirtAboveground` and `ZombieConfig.ZombiesCountBeforeDelete` all carry explicit do-not-change or performance warnings in the generated file; treat them as support boundaries, not tuning knobs.
- **Treat SandboxVars edits as restart-required.** Only the `.ini` has a documented live-reload path. Whatever the truth of the contested shutdown-overwrite claim (admins-foundation, Claim 4), stop-edit-start is never wrong.
- **Verify after boot, not after save.** `showoptions` against the running server is the ground truth for what actually loaded; a typo in Lua can silently fall back.
- **Quote strings, comma-separate lists.** `LootItemRemovalList` and `WorldItemRemovalList` take comma-separated full item types (`Base.Hat` style) as Lua strings.

# Common Pitfalls & Troubleshooting

- **A per-skill XP value "does nothing".** Check `MultiplierConfig.GlobalToggle` — while true, `Global` wins [5]. Then check the key name: `Carpentry`, `Foraging` and `First Aid` are not keys; `Woodwork`, `PlantScavenging` and `Doctor` are [5].
- **B41 guide keys silently ignored on B42.** `XpMultiplier`, `FoodLoot`, `WeaponLoot`, `OtherLoot`, `LootRespawn`, `ZombieLore.Smell` and `ZombieLore.Decomp` are not in the 42.20 listing [5] [6]. The B42 replacements are `MultiplierConfig`, the `*LootNew` multipliers, and the loot-respawn hour keys.
- **"Zombies never come back" on a fresh B42 server.** That is the generated default, not a bug — respawn is zeroed [5].
- **Loot rarity edited but numbers feel unchanged.** On B42 the per-category multipliers interact with the world loot state — `MaximumLooted`, `DaysUntilMaximumDiminishedLoot` and friends can pre-loot or withhold loot independently of category rarity [5].
- **Population feels wrong after migrating from B41.** Re-read the multiplier mapping; the same number means a different world on each build [5] [6] [7].
- **An edit made while the server ran has vanished.** Only the `.ini` documents a live path [9]; see the quarantined shutdown-overwrite discussion in `admins-foundation` (Claim 4) before blaming the game or yourself.
- **Mid-save edits appear to half-apply.** See Claim 1 below — which keys apply retroactively to an existing world is not documented; test on a copy before promising rule changes to players.
- **Sprinter shares don't apply.** `ZombieLore.SprinterPercentage` is documented as taking effect when `Speed` is Random (4), not alongside a fixed speed [5].

# Community Notes & Unverified Claims

## Claim 1 — Some SandboxVars edits do not apply retroactively to an existing world

- **Claim:** Community guidance (hosting KBs, Reddit and Steam-forum threads) widely holds that certain sandbox values — variously named: loot already spawned, erosion progress, water/electricity countdowns, zombie population state — are baked into an existing save, so editing the file mid-campaign only affects newly generated chunks or has no effect, and only a fresh world honours every key.
- **Why unverified:** No primary source enumerates which keys are read live, which at world creation, and which persist in the save; the wiki documents the file and its defaults but not retroactivity semantics [5] [9].
- **Confidence:** Medium. The direction is plausible (world state such as spawned loot and utility-shutoff dates must live in the save) and the claim is consistent across many independent community sources, but the per-key boundary is unknown and some counterexamples (values that clearly do apply mid-save) circulate too.

## Claim 2 — Hand-editing population multipliers above the documented maximum works

- **Claim:** Server-admin threads state that values beyond the documented cap — e.g. `ZombieConfig.PopulationMultiplier` above 4.0 — can be written directly into the Lua and are honoured by the server, enabling "beyond Insane" populations.
- **Why unverified:** The pinned listings document 4.0 as the maximum on both builds [5] [6]; no primary source describes out-of-range handling (accept, clamp, or reset) for hand-edited values.
- **Confidence:** Low. Reports are anecdotal, build-version rarely stated, and the behaviour could change with any hotfix; the documented range is the only safe contract.

# Risks & Caveats

- **The B41 evidence is the weak leg.** The archived listing's SandboxVars block is stamped `VERSION = 4` and its enum comments disagree with the B41 sandbox-UI docs in places (five- vs six-step population counts, six- vs seven-step mortality) [6] [7]. B41 key names cited here are solid; B41 enum numbering and defaults should be treated as approximate.
- **Defaults quoted are generated-file values, not universal truths.** The 42.20 defaults come from one wiki revision's rendering of the generated file [5]; a hotfix can move any of them. The 42.20.1-42.21 notes name no changed sandbox default [10] [11] [12], but they are behaviour notes rather than a schema diff, and no 42.21 server was inspected.
- **UI-documented but key-unpinned options.** For a number of B41 rules (vehicles, night darkness, poisoning, multi-hit) only the UI option is documented [7]; the B41 Lua key names are asserted nowhere in the cited record and are deliberately not tabled.
- **Retroactivity is undocumented.** Nothing cited here says which keys affect an existing world (Claim 1); every mid-campaign change is an experiment.
- **Steam announcement URLs bot-block link checkers** (verified via the ISteamNews API mirror per project source policy); pzwiki citations are revision-pinned and fact-only per the license rules.

# Verification Steps

1. **Regenerate and diff:** on a scratch install of the target build, delete (after backup) `servertest_SandboxVars.lua`, start the server once, and compare the generated file against the tables above — key names, nesting and defaults.
2. **Confirm the B42 listing:** open `https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167` and check the SandboxVars section against this document.
3. **Confirm the B41 listing:** open `https://pzwiki.net/w/index.php?title=Server_settings&oldid=1393223` and check the `VERSION = 4` block.
4. **Confirm live values:** run `showoptions` as admin against a running server and match a handful of edited keys.
5. **Check a key from Lua:** in a debug/console context, `getSandboxOptions():getOptionByName("ZombieLore.Speed"):getValue()` returns the live value by dotted name [8].
6. **Corroborate patch-note keys:** query `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0` and find the 42.20 note raising the zombie-deletion cap to 5000 and the 42.17 note naming `Water/ElecShutModifier`.
7. **Probe Claim 1:** copy a live save, change one key per area (loot multiplier, respawn hours, water shutoff), restart, and record which changes manifest.
8. **Probe Claim 2:** on a throwaway world, set `PopulationMultiplier` to 5.0, boot, and read the value back via `showoptions` to see whether it is accepted, clamped or reset.

# Open Questions

- Which SandboxVars keys are world-creation-only versus live-per-session (Claim 1)? A developer statement or systematic save-diff testing would resolve it.
- What is the precedence between the windowed enums and their day modifiers (`WaterShut` vs `WaterShutModifier`) at 42.20? The archived B41 comment implies the modifier is the concrete day count [6]; the B42 listing documents both without stating the interaction [5].
- Does the B42 server clamp out-of-range hand-edited values (Claim 2)?
- Where is the B41 `XpMultiplierAffectsPassive`-style key actually named, if it exists — game files would pin what the wiki record does not [6] [7].
- Does 42.21 change any generated default or range? The patch notes name none [10] [11] [12]; a 42.21 server install would answer it.
- Will post-release B42 patching move the generated defaults (respawn zeroed, randomized lore) toward the B41 posture, or is this the intended stable baseline [1]?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [2] **The Indie Stone** — *Build 42.19.0 Unstable Released* (Steam announcement, 2026-06-01; sandbox-option fixes incl. map-known and tainted-water tooltip). https://steamcommunity.com/games/108600/announcements/detail/1833968530897275. Accessed 2026-07-30.
- [3] **The Indie Stone** — *Build 42.17.0 Unstable Released* (Steam announcement, 2026-04-20; names Water/ElecShutModifier and the crawl-under-vehicle sandbox setting). https://steamcommunity.com/games/108600/announcements/detail/1830163047266254. Accessed 2026-07-30.
- [4] **The Indie Stone** — *B42 CHECKLIST* (Steam announcement, 2026-07-28; legacy41 branch instructions). https://steamcommunity.com/games/108600/announcements/detail/1839041357038237. Accessed 2026-07-30.
- [10] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [11] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [12] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post 2026-09-23; abridged copy). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [5] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0; full SandboxVars listing). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-30. Fact-only source.
- [6] **PZwiki** — *Server settings*, archived Build 41 revision (revision 1393223, 2026-05-23; SandboxVars block stamped VERSION 4). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1393223. Accessed 2026-07-30. Fact-only source.
- [7] **PZwiki** — *Custom Sandbox* (revision 1442995; page versioned against 41.78.19; sandbox-UI option documentation). https://pzwiki.net/w/index.php?title=Custom_Sandbox&oldid=1442995. Accessed 2026-07-30. Fact-only source.
- [8] **PZwiki** — *Sandbox options* (revision 1442317; page versioned against 42.19.0; mod-defined options and Lua access). https://pzwiki.net/w/index.php?title=Sandbox_options&oldid=1442317. Accessed 2026-07-30. Fact-only source.
- [9] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0; file locations, generation, showoptions/reloadoptions). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-30. Fact-only source.

**Further Reading**

# Further Reading

- The Steam news API mirror used to verify the primary announcements: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- Albion's community Sandbox Options modding guide (linked from the wiki modding page): https://github.com/demiurgeQuantified/PZModdingGuides/blob/main/guides/SandboxOptions.md
- The official blog / Thursdoid feed (bot-blocks automated checkers; read in-browser): https://projectzomboid.com/blog/

# Related Documents

- `admins-foundation` — the Admins-track overview this document deepens; carries the quarantined config-editing-workflow claim (its Claim 4) referenced here.
- `admins-server-ini-reference` — the companion per-key reference for `servertest.ini`.
- `players-foundation` — the player-facing view of the B41/B42 split these settings run on.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed the 42.21 unstable and stable Steam notes [10] [11] and the TIS forum changelist [12]; added zombie-fix note, scope statement, removed stale 'days old' caveat. Key schema not re-extracted. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
