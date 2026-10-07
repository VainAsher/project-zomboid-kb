---
id: modders-porting-b41-to-b42
title: "Porting a Build 41 Mod to Build 42: A Diff-Driven Checklist"
version: 0.3.0
status: in-review
confidence: Medium
category: Modders
topic: "Porting B41 mods to B42"
build: both
document_type: guide
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-lua-api-surface, modders-events-callbacks, modders-modoptions-pzapi, modders-item-scripts-distributions, modders-mp-networking-porting, modders-modinfo-modid-conventions, modders-first-mod-tutorial-b42, players-crafting-chains, admins-workshop-mod-wiring, meta-style-guide]
tags: [porting, b41, b42, api-diff, umbrella, craftrecipe, mod-structure, workshop, events, stats, traits]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-porting-b41-to-b42 |
| Version | 0.3.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16 (Umbrella stubs), 42.21.0 (Umbrella stubs; 42.20.0 figures kept for comparison) |

# Executive Summary

This guide turns a mechanical comparison of two type-stub snapshots into a
porting checklist. The snapshots are the Umbrella stubs pinned for Build 41
(release tag 41.78.16) and for Build 42 (release tag 42.21.0, commit
13d01f9) [1] [2]. The KB
reduced each snapshot to a symbol index (classes with their members and
parents, Lua events, global functions) and diffed the two. The result is a set
of "if your mod calls X, check Y" prompts, each backed by a name that appears
in one index and not the other, plus the non-API porting areas that the stubs
cannot show: the versioned mod folder layout, the new crafting script format,
multiplayer, and Workshop publishing for both builds [28] [31].

The headline findings are structural rather than cosmetic. The per-character
need and mood getters (hunger, thirst, boredom and similar) disappear from
the B41-era `Stats` class and a generic accessor plus a `CharacterStat`
constant list appears in B42 [3] [4] [5]. Trait and profession registration
moves from two factory classes to a registry plus script blocks [11] [12]
[31]. The `Recipe` class loses most of its accessors while a much larger
`CraftRecipe` class appears [8] [9]. Dozens of Lua events and global
functions are gone [13] [14].

Two limits govern everything below. First, a name missing from the B42 index
may have been renamed or moved rather than deleted, and the index records
names, not behaviour, so a name that is present may still act differently.
Second, the B42 side of this document is now verified against the 42.21.0
stubs (re-baselined from 42.20.0 on 2026-10-07), and 41.78.21 (2026-08-26)
has no matching B41 stub pin [18]. The stubs can lag behaviour: 42.21
re-enabled `loadstring` and `loadstream` [17], yet neither is declared as a
global in the 42.21.0 index. Document confidence is Medium: the symbol facts
are High-grade (pinned stubs) but the interpretation of absences, and all
behaviour, is not. Nothing here was tested in a live game.

# Key Takeaways

- The B41 and B42 stub indices share 1,333 classes; 165 B41 classes are
  absent from B42 and 2,791 classes appear only in B42 (42.20.0 figures were
  1,388 / 110 / 2,878). The large "added" figure is inflated by wider stub
  coverage in the B42 pin, so treat added counts as weak evidence. *(cited)*
  *(both)*
- Events: 240 in the B41 index, 244 in B42, 205 shared, 35 gone, 39 new
  (42.20.0: 234, 203, 37, 31).
  Gone events include `Events.OnPreGameStart` *(B41)*, `Events.OnDawn` *(B41)*,
  `Events.OnDusk` *(B41)* and `Events.OnMakeItem` *(B41)*. *(cited)*
- Globals: 83 gone and 349 new (42.20.0: 64 and 347). Example: `getSaveName` is B41-only and
  `getCurrentSaveName` is B42-only, a probable rename. *(cited)* *(both)*
- Character stats moved: B41 `Stats:getHunger` *(B41)* has no same-named
  B42 counterpart; B42 offers `Stats:get(CharacterStat.HUNGER)` *(B42)*.
  *(cited)*
- Traits: B41 `TraitFactory.addTrait` *(B41)* and
  `IsoGameCharacter:HasTrait` *(B41)* are gone; B42 has
  `IsoGameCharacter:hasTrait` *(B42)* and script-defined traits. *(cited)*
- Folder layout: B42 needs `common/` and version folders each with its own
  `mod.info`; the B41 layout can sit beside it in one mod folder. *(cited)*
- Crafting: B41 `Recipe` scripts and the B42 `craftRecipe` blocks are
  different formats; script-side detail lives in
  `modders-item-scripts-distributions`. *(cited)*
- The official 42.13 migration material adds hard requirements the stubs
  cannot show: a `registries.lua` file for new IDs, `ItemType` and tag
  registration, and the timed-action split into `perform` and `complete`.
  It is 42.13-era, older than the 42.21.0 stubs. *(cited)* *(B42)*
- Since 42.20.0: `%%` is the way to write a literal `%` in mod translation
  strings, mods may write `.json` files, and `loadstring`/`loadstream` were
  removed in 42.20.4 and re-enabled in 42.21. *(cited)* *(B42)*
- Behaviour is out of reach of this method. Use the patch notes and in-game
  tests for anything the stubs cannot show. *(guidance)*

# Purpose

A modder who owns a working B41 mod needs to know what to look at first. A
blind rewrite is wasteful and a blind "it loads, ship it" is dangerous. This
guide answers: which of the calls my mod makes no longer exist in the pinned
B42 stubs, which structural changes (folders, scripts, networking) apply to
every mod regardless of what it calls, and how to publish one Workshop item
that serves both builds.

# Scope

Covered: the symbol-level diff between the two pinned stub indices for the
most commonly used classes (`IsoPlayer`, `IsoGridSquare`, `InventoryItem`,
the `ISUIElement` family), Lua events and global functions; the folder and
`mod.info` changes; the crafting script split; distributions and
multiplayer at pointer level; Workshop publishing for both builds.

Not covered: behavioural changes (the stubs cannot show them), content and
balance changes, map and 3D asset pipelines, the field-by-field script
reference (see `modders-item-scripts-distributions`), the networking rewrite
in depth (see `modders-mp-networking-porting`), options API porting (see
`modders-modoptions-pzapi`) and anything newer than the 42.21.0 stub pin.

# Definitions

- **Symbol index** — the KB's JSON reduction of an Umbrella checkout: for each
  class its parents and member names, plus the event names and global
  function names, built per game build [1] [2].
- **Effective removal** — a member that a class declares in the B41 index and
  neither the class nor any ancestor declares in the B42 index. This accounts
  for members that moved up to a parent class [15] [16].
- **Rename candidate** — a name absent from one index with a similar name
  present only in the other. The index cannot prove the two are the same
  function; behaviour must be checked.
- **registries.lua** — the Lua file, stored under `media/` with exactly that
  name, in which B42 mods register new IDs before scripts and other Lua load
  [34].
- **Stub noise** — differences caused by how the stub generator documents a
  class (for example listing constants or fields) rather than by a game
  change.

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | Umbrella release tag 41.78.16, commit fa2e7e1 [2] | Latest legacy hotfix is 41.78.21 (2026-08-26) [18]; no newer stub pin exists, so symbol facts are as of 41.78.16 |
| B42 (stable) | Yes | Umbrella release tag 42.21.0, commit 13d01f9 [1] | Stable is 42.21 (2026-09-28) [17]. Previously verified against 42.20.0, commit 58204fc [36] |

**What was re-checked for 42.21.** Every symbol count and every named example
in the Reference tables was recomputed or re-looked-up against the 42.21.0
index, and each example still holds with the corrections noted in the tables.
The official posts for 42.20.1, 42.20.2, 42.20.3, 42.20.4, 42.21 unstable,
42.21 stable and the forum change list were read for porting-relevant changes
[37] [38] [18] [39] [17] [40]. Statements that rest on the 42.13 PDFs, the
pzwiki pages and the 41.78.16 stubs are carried forward unchanged with no
contradicting change found in those notes; they were not re-tested in a game.

The stub pin tracks the code but can lag behaviour. 42.20.4 removed the Lua
`loadstring` and `loadstream` methods and 42.21 re-enabled them [18] [17], yet
the 42.21.0 index declares neither as a global (`loadstream` was declared in
the 42.20.0 index; `loadstring` in neither) [1] [36]. A missing stub is
therefore not proof of removal. Upstream later moved the 42.20.0 tag to a
different commit, so cite and pin commits rather than tag names [41].

# Reference

## How the diff was computed

**Evidence layer.** Each pinned Umbrella commit was reduced to a symbol index
containing class names with member and parent lists, event names and global
function names [1] [2]. The two pins are laid out differently: the B41 tree
keeps Java-side stubs under a `Candle` folder and Lua-side stubs under `Lua`
[2], while the B42 tree uses `java` and `lua` folders and a single events
file [1] [13]. The B42 tree listing holds 3,293 entries against 1,686 for
B41 (3,449 at the 42.20.0 commit), so the B42 pin documents far more classes
[1] [2] [36]. Consequently, class
and member removals are strong evidence of change, while additions are not
(a new entry might have existed unstubbed in B41).

## Totals

| Category | B41 index | B42 index | In both | Only B41 | Only B42 |
|----------|-----------|-----------|---------|----------|----------|
| Classes | 1,498 | 4,124 | 1,333 | 165 | 2,791 |
| Events | 240 | 244 | 205 | 35 | 39 |
| Globals | 664 | 930 | 581 | 83 | 349 |

These totals come from set arithmetic over the two indices built from [1]
and [2]. Across the 1,333 shared classes, 737 classes lose at least one
member by the effective-removal rule, for 5,246 member names in all. Many of
those are stub noise (see the limits below) so the per-class tables that
follow are the usable output. For comparison, the 42.20.0 index [36] gave
4,266 classes (1,388 shared, 110 B41-only, 2,878 B42-only), 234 events (203
shared, 37 B41-only, 31 B42-only), 947 globals (600 shared, 64 B41-only, 347
B42-only), and 776 shared classes losing 5,222 member names.

**Movement from 42.20.0 to 42.21.0.** Comparing the two B42 indices [36] [1]:
the event list gained ten names and lost none; the global list lost 21 names
(including `loadstream`, see Build Applicability) and gained four
(`deleteDatabase`, `getMaxUsernameLength`, `getMinUsernameLength`,
`sendAddObjectToMap`); 155 classes dropped out of the index and 13 appeared.
Of the 155, 26 are generated `CraftRecipeCode.*` helpers and 55 also exist in
the B41 index, which is why the B41-only class count rose from 110 to 165
(examples: `ISGameLoadingUI`, `ISOptionPanel`, `ISCraftingCategoryUI`,
`ISFarmingCursor`). Whether those 55 left the game or only the stub set is not
shown by the index.

## Removed classes worth checking

These classes exist in the B41 index and have no entry in the B42 index [2]
[1]. Each is a candidate for "my mod subclasses, calls or patches this".

| Area | B41-only classes | Notes |
|------|------------------|-------|
| Trait and profession registration | `TraitFactory` *(B41)*, `ProfessionFactory` *(B41)*, `Trait` *(B41)*, `Profession` *(B41)* | B42 index has `CharacterTrait`, `CharacterProfession` and a `Registries` class [11] [12] |
| Item creation | `InventoryItemFactory` *(B41)* | Its only members are `CreateItem` and the constructor [2]; the global `instanceItem` is in both indices [1] [2] |
| Multi-stage build | `MultiStageBuilding` *(B41)* | The `Multistagebuild` script block is B41-only [31] |
| Fire and furnace menus | `ISFireplaceMenu` *(B41)*, `ISBlacksmithMenu` *(B41)*, `ISBSFurnace` *(B41)* | B42 index adds `FurnaceLogic` (the 42.20.0 index also listed `ISFurnaceLogicPanel`, absent from 42.21.0); successor status is not provable from stubs [1] [36] |
| Reload and safety UI | `ISReloadManager` *(B41)*, `ISSafetyUI` *(B41)* | `ISReloadWeaponAction` is in both [1] [2] |
| Login and server list | `LoginScreen` *(B41)*, `ServerList` *(B41)*, `PublicServerList` *(B41)* | UI-shell classes; matter only to total-conversion style mods [2] |

## Most-used classes: effective member removals

All names below are present in the B41 index and absent from the B42 index
for that class and every ancestor [2] [1]. Each row is a "check before you
ship" prompt. A removed name may have a renamed or relocated successor.

| Class | Removed members (examples) | Where to look in B42 |
|-------|----------------------------|----------------------|
| `IsoPlayer` | `IsoPlayer:getForname` *(B41)*, `IsoPlayer:getSurname` *(B41)*, `IsoPlayer:isDeaf` *(B41)*, `IsoPlayer:getStaticTraits` *(B41)* [25] | 109 effective removals (counting those inherited from `IsoLivingCharacter` and `IsoGameCharacter`); the B42 class inherits from `IsoLivingCharacter` and several interfaces [26] |
| `IsoGameCharacter` | `IsoGameCharacter:HasTrait` *(B41)*, `IsoGameCharacter:getTraits` *(B41)*, `IsoGameCharacter:getTemperature` *(B41)* [16] | `IsoGameCharacter:hasTrait` *(B42)* and `IsoGameCharacter:getCharacterTraits` *(B42)* exist [15]; no same-named temperature accessor exists |
| `IsoGridSquare` | `IsoGridSquare:explode` *(B41)*, `IsoGridSquare:smoke` *(B41)*, `IsoGridSquare:explosion` *(B41)*, `IsoGridSquare:explodeTrap` *(B41)*, `IsoGridSquare:drawCircleExplosion` *(B41)* [2] | 19 effective removals (16 against the 42.20.0 index); none of the five has a same-named B42 member [1] [36] |
| `InventoryItem` | `InventoryItem:getPlaceDir` *(B41)*, `InventoryItem:setPlaceDir` *(B41)*, `InventoryItem:isTaintedWater` *(B41)*, `InventoryItem:setTaintedWater` *(B41)* [2] | B42 adds `InventoryItem:getFluidContainer` *(B42)* and `InventoryItem:isFluidContainer` *(B42)* [1] |
| `DrainableComboItem` | `DrainableComboItem:getDelta` *(B41)*, `DrainableComboItem:setDelta` *(B41)*, `DrainableComboItem:getRemainingUses` *(B41)*, `DrainableComboItem:getUsedDelta` *(B41)* [7] | B42 declares `DrainableComboItem:setCurrentUses` *(B42)* and `DrainableComboItem:getMaxUses` *(B42)* [6]; `getCurrentUses` is reachable on both builds through the parent `InventoryItem` [6] [7] |
| `HandWeapon` | `HandWeapon:getScope` *(B41)*, `HandWeapon:getClip` *(B41)*, `HandWeapon:getCanon` *(B41)*, `HandWeapon:getSling` *(B41)*, `HandWeapon:getStock` *(B41)* [2] | `HandWeapon:getWeaponPart` *(B42)* and `HandWeapon:getAllWeaponParts` *(B42)* are in both builds [1] |
| `IsoObject` | `IsoObject:getWaterAmount` *(B41)*, `IsoObject:setWaterAmount` *(B41)*, `IsoObject:useWater` *(B41)* [2] | B42 adds `IsoObject:addFluid` *(B42)* and `IsoObject:getFluidContainer` *(B42)* [1] |
| `ItemContainer` | `ItemContainer:getWeight` *(B41)* [2] | `ItemContainer:getContentsWeight` *(B42)* is in both builds [1] |
| `BodyDamage` | `BodyDamage:getInfectionLevel` *(B41)*, `BodyDamage:getBoredomLevel` *(B41)*, `BodyDamage:getUnhappynessLevel` *(B41)*, `BodyDamage:getWetness` *(B41)*, `BodyDamage:getTemperature` *(B41)* (20 in all) [2] | `BodyDamage:getApparentInfectionLevel` *(B42)* is in both builds [1]; see the stats table below |
| `IsoZombie` | `IsoZombie:becomeCorpse` *(B41)*, `IsoZombie:getHitAngle` *(B41)* (84 in all, mostly inherited from `IsoGameCharacter`) [2] | 84 effective removals; `IsoZombie:isLocal` *(B42)* is in both builds [1] |

## Character stats: typed getters to a generic accessor

The B41 `Stats` class declares typed getters and setters such as
`Stats:getHunger` *(B41)*, `Stats:getThirst` *(B41)*, `Stats:getBoredom` *(B41)*,
`Stats:getStress` *(B41)* and `Stats:getEndurance` *(B41)* [5]. None of those
names is declared in the B42 `Stats` class, which instead exposes
`Stats:get(CharacterStat.HUNGER)` *(B42)* style access with `Stats:set` *(B42)* and
`Stats:add` *(B42)* [3]. The `CharacterStat` class lists constants such as
`CharacterStat.HUNGER` *(B42)*, `CharacterStat.STRESS` *(B42)* and
`CharacterStat.MORALE` *(B42)* [4]. The index establishes the shape of the
new API but not the value range or sign convention, which must be tested
in game.

## Events

The 35 B41-only events, listed in the B41 events file, and the 39 B42-only
events, listed in the B42 events file, are [14] [13]. (Two of the 37
B41-only events of 42.20.0, `Events.OnFillInventoryContextMenuNoItems` and
`Events.OnPreFillInventoryContextMenuNoItems`, appear in the 42.21.0 file and
so moved to the shared set [13] [36].) The table gives examples:

| Group | B41-only events *(B41)* | B42-only events *(B42)* |
|-------|------------------------|------------------------|
| Time and weather | `Events.OnDawn`, `Events.OnDusk`, `Events.OnRainStart`, `Events.OnRainStop`, `Events.OnChangeWeather` [14] | `Events.OnWarUpdate` and `Events.OnSleepingTick` appear among the new entries [13] |
| Lifecycle and render | `Events.OnPreGameStart`, `Events.OnRenderUpdate`, `Events.OnPostFloorSquareDraw`, `Events.OnPostTileDraw` [14] | `Events.OnMouseWheel`, `Events.OnContextKey` [13] |
| Characters | `Events.OnBeingHitByZombie`, `Events.OnCharacterMeet`, `Events.OnNewSurvivorGroup` [14] | `Events.OnZombieCreate`, `Events.OnDeadBodySpawn` [13] |
| Crafting and items | `Events.OnMakeItem` [14] | `Events.OnItemFound`, `Events.OnProcessAction` [13] |
| Safehouse and radio | `Events.OnPlayerSetSafehouse`, `Events.OnRadioInteraction` [14] | `Events.OnNetworkUsersReceived`, `Events.OnRolesReceived` [13] |

The rows above are examples, each re-confirmed against the 42.21.0 index; the
full lists come from the diff script in Verification Steps. The ten events
new in 42.21.0 relative to 42.20.0 are `Events.AcceptedMedicalCheck`,
`Events.OnFillInventoryContextMenuNoItems`, `Events.OnForagePool`,
`Events.OnForageRequestZone`, `Events.OnForageSpot`,
`Events.OnJoypadDebugRenderUIOptionSet`,
`Events.OnPreFillInventoryContextMenuNoItems`,
`Events.OptionControllerButtonStyleChanged`,
`Events.OptionGamepadBindingPresetChanged` and `Events.RequestMedicalCheck`
[13] [36]. Events common to both builds include
`Events.OnGameBoot`, `Events.OnTick`, `Events.OnClientCommand` and
`Events.OnServerCommand` [13] [14]. The three distribution-merge events
`Events.OnPreDistributionMerge`, `Events.OnDistributionMerge` and
`Events.OnPostDistributionMerge` are in both indices [13] [14].

## Global functions

Examples of B41-only globals: `getSaveName`, `getMods`,
`getPlayerCraftingUI`, `getSandboxFileWriter`, `sendBandage`, `sendStitch`
and `sendAddXp` [2]. Examples of B42-only globals: `getCurrentSaveName`,
`getBreakModGameVersion`, `isMultiplayer`, `requestMedicalCheck` and
`acceptMedicalCheck` [1]. Globals present in both include `getActivatedMods`,
`getModInfoByID`, `getGameVersion`, `instanceItem`, `isClient`, `isServer`,
`sendClientCommand` and `sendServerCommand` [1] [2].

## Crafting and recipe classes

The B41 `Recipe` class carries accessors such as `Recipe:getTimeToMake` *(B41)*, `Recipe:getCategory` *(B41)*, `Recipe:isHidden` *(B41)* and `Recipe:getSound` *(B41)*,
51 of which are absent from the B42 `Recipe` (46 against the 42.20.0 index) [9] [8]. The B42 index adds a
110-member `CraftRecipe` class with inputs, outputs, tags, required skills
and a timed-action script, including `CraftRecipe:getInputs` *(B42)*,
`CraftRecipe:getOutputs` *(B42)* and `CraftRecipe:getRequiredSkills` *(B42)* [8].
`ScriptManager:getAllCraftRecipes` *(B42)*, `ScriptManager:getCraftRecipe` *(B42)* and
`ScriptManager:getAllBuildableRecipes` *(B42)* are B42-only, while
the older `ScriptManager:getAllRecipes` and `ScriptManager:getRecipe` are in both [24].
On the interface side, the `ISCraftingUI` class shrinks from 105 declared
members to 3 and the B42 index adds `ISHandcraftWindow` [10]. The
`ISBuildMenu` class (99 members in B41, 3 in B42) loses 98 members, mostly per-furniture sprite helpers,
and B42 adds `ISBuildWindow` [1]. The script side uses the B42 `craftRecipe`
and `entity` blocks, and traits and professions are defined with
`character_trait_definition` and `character_profession_definition` blocks
[31].

## UI element classes

For the `ISUIElement` family the effective removals are small: B41
`ISUIElement:getCentreX` *(B41)* and `ISUIElement:getCentreY` *(B41)* are not
declared in B42, while B42 adds `ISUIElement:centerOnScreen` *(B42)*,
`ISUIElement:detachFromParent` *(B42)* and `ISUIElement:doLayout` *(B42)* [27] [2].
The per-class tables show much larger raw removals (for example fourteen
members of `ISInventoryPane`), but these are mostly field entries such as
the position fields, and the B42 index still declares the position field
`x` on `ISUIElement` itself, so they are probably stub noise rather than API
loss [27] [1]. `ISScrollingListBox`,
`ISModalDialog` and `ISTextEntryBox` additionally lose
`insertNewListOfButtonsList` [2] [1]. The timed-action base class gains
members: `ISBaseTimedAction:forceCancel` *(B42)*, `ISBaseTimedAction:getDuration` *(B42)*
and `ISBaseTimedAction:isStarted` *(B42)* are B42-only [1].

## Folder layout and mod.info

B41 keeps `media/` and `mod.info` at the mod root [28]. B42 requires a
`common/` folder, which may be empty, plus optional version folders named for
game versions, each able to hold its own `media/` and `mod.info` [28]. At
least one `common/` or version folder must exist for the mod to be detected
[28]. The game loads `common/` first and then the closest version folder,
whose files override matching `common/` files [28]. A folder name is read at
major-minor precision, so `42.1.5` is treated as `42.1` [28]. Both layouts
can coexist in one mod folder because the B42 layout sits one level deeper
[28]. The `mod.info` file is best placed in each version folder because
requirements tend to vary by game version, and its filename must be
lowercase for Linux and macOS [29]. In practice only `id` and `name` are
required [29].

## Workshop publishing for both builds

Uploads go through the in-game uploader or alternative tools such as
SteamCMD [30]. The uploader appends the Workshop ID and Mod ID to the page
description and overwrites the whole description on every upload [30]. Files
deleted between versions are not removed from subscribers, and the
documented workaround is to ship the file emptied [30]. Only the `Contents`
folder is uploaded, so sibling folders can hold sources and a repository
[28]. A dual-build item therefore uses one Workshop entry containing the B41
root layout and the B42 `common/` plus version folders [28].

## Official 42.13 migration material

**Evidence layer.** A moderator post on the Indie Stone forums, dated
2025-12-11 and titled for the 42.13 modding migration, attaches two PDFs
[23] [34] [35]. They are 42.13-era and were not re-checked against 42.20.0 or 42.21.

**Registries.** From 42.13 some identifiers used in scripts and recipes
must be registered from Lua [34]. The listed identifier kinds are character
trait, character profession, item tag, brochure, flier, item body location,
item type, moodle type, weapon category, newspaper and ammo type [34]. The
registration calls live in a file named `registries.lua` in the `media`
folder; the name is mandatory and the file loads before scripts and before
other Lua [34]. The B42 index has matching classes: `ItemTag.register`
*(B42)*, `ItemType.register` *(B42)* and `CharacterTrait.register` *(B42)* [1].
Registered IDs carry a mod prefix and a colon in the guide's examples [34].

**Script changes.** The guide says the item script `DisplayName` property is
gone, so item names now come from translation keyed by module and item ID
[34]. The item script `Type` property is renamed `ItemType` and needs the
item-type registry, and `Tags` values need the item-tag registry [34]. The
guide also says base-game script examples are generated from Java code [34].

**Lua API.** The guide says some Lua API was modified, tells modders to
check the decompiled Java when something stops working, and states that
more API changes were expected in upcoming unstable patches [34]. It adds
that future patches would include modding changes driven by modder reports
and that new API documentation would appear gradually [34].

**Timed actions.** The inventory-items document (version 1.0) says all
inventory-item handling in multiplayer moved server-side to prevent
cheating, so items made only on a client are not usable and vanish after
relogin [35]. To adapt an existing timed action it lists five steps [35]:

1. Move the file from `media/lua/client` to `media/lua/shared` so both client
   and server load it [35].
2. Make each argument of `new` match a field of the same name and value,
   because the server rebuilds the action from those fields [35].
3. Add a `getDuration` function returning the length in ticks, which is the
   time in seconds divided by 0.02; return 1 for an instant action and -1
   for an endless one [35]. The B42 index declares `ISBaseTimedAction:getDuration`
   *(B42)*, which is absent from B41 [1] [2].
4. Split `perform` (client-side effects such as sound, animation and UI,
   with no item or object changes) from a new `complete` (item and object
   changes, run on the server and, in single player, after `perform`) [35].
5. Send the changes to clients from `complete` [35].

The same document says duration must not be passed as an argument because
that allowed cheaters to shorten actions, and that an argument may not be
stored in a field under a changed value, or the rebuilt action gets a
different value [35]. Supported `new` argument types include `InventoryItem`,
`IsoObject`, `IsoGridSquare`, `IsoPlayer`, `ItemContainer`, strings,
numbers and booleans, but not objects created on the client [35]. Long
actions use a `serverStart` function with `emulateAnimEvent` and an
`animEvent` handler, and end with a forced complete [35].

**Commands and sync.** `sendClientCommand` takes an optional player, a
module name, a command name and an argument table; the server receives it
through `Events.OnClientCommand` with module, command, player and args, and
in single player the handler is also called [35]. Sync functions named in
the document are `sendAddItemToContainer`, `sendRemoveItemFromContainer`,
`syncItemFields`, `syncItemModData`, `syncHandWeaponFields`,
`sendItemStats`, `transmitCompleteItemToClients`,
`transmitRemoveItemFromSquare`, `sync` and
`transmitUpdatedSpriteToClients` [35]. The B42 index contains the first six
of these as globals and the B41 index none of them; the last four were not
found as globals in either index [1] [2].

## Changes in the 42.20.1 to 42.21 hotfix and update wave

**Evidence layer.** The notes below are the items in the official posts that
bear on a port; behaviour beyond what the posts state was not tested.

- **Translations.** Mod translation strings should use `%%` to show a literal
  `%` (42.20.1) [37]. A temporary workaround accepts both forms, error logs
  point at strings that need updating, and the workaround will be removed in
  a future unstable update (42.20.2) [38]. 42.21 updated the localization
  system to allow more translatable strings [39] [40], and its forum notes say
  a `RuntimeException` is raised when missing translations or missing recipes
  are detected, replacing a `System.err.println` message [40]. The notes do not
  say when it fires.
- **File writing.** 42.20.1 added the ability for mods to write `.json`
  files [37]. The notes do not name the function involved, so the
  `getFileWriter` extension limit cited from 42.20.0 under "Multiplayer,
  distributions and file access" may no longer be the whole picture [37] [32].
- **Multiplayer integrity.** 42.20.1 improved Lua checksum validation as part
  of multiplayer anti-cheat [37]; 42.21 expanded the anti-cheat system and
  moved clothing-condition handling server-side [39] [40]. Both mean
  client-only modifications to shared Lua are more exposed to rejection than
  before; the posts do not describe the exact checks.
- **Server-side items.** 42.20.1 fixed an issue that allowed broken B41
  worlds to be hosted on B42 servers [37].
- **Security.** `loadstring` and `loadstream` were removed in 42.20.4, with
  the instruction to replace server-sent code with explicit commands, and were
  re-enabled in 42.21 [18] [17].
- **Gameplay-data changes** that can matter to item and recipe mods: the Welder
  occupation starts with Welding recipes instead of Blacksmithing recipes, 86
  more fluid containers can purify water in the appropriate oven type, and
  antibiotics can use the "pack in box" crafting recipe [39] [40].

## Multiplayer, distributions and file access

Multiplayer was reimplemented for B42 with release 42.13.0, whereas B41
multiplayer is long established [33]. The Indie Stone published a migration
guide for existing mods at that point [23] [34] [35]. `Events.OnClientCommand` and
`Events.OnServerCommand` are in both indices [13] [14], and
`sendClientCommand` and `sendServerCommand` are globals in both [1] [2].
B42 also adds the globals `sendClientCommandV` and `sendServerCommandV`
[1]. In B42 `getFileWriter` only writes files with the extensions ini, cfg,
txt and log, while `getModFileWriter` is not limited [32]. For
distributions, `ItemPickerJava` grows from 22 to 51 members in the index
and the `VehicleDistributions` class lists 88 members in the B41 index and
none in the B42 index, which looks like a stub-format difference rather
than evidence of removal [1] [2].

# B41 vs B42 Delta

**Evidence layer.** The Indie Stone stated at the start of the B42 unstable
cycle that B41 saves and mods are not compatible with B42 [22]. The deltas
that matter for a port, in order of how often they bite:

- **Mod folder.** B41 flat layout versus B42 `common/` plus version folders
  [28]. Result: a B41-only mod is not detected by B42 [28].
- **Stats, traits and professions.** Typed stat getters are gone [5] [3];
  trait and profession factories are gone [11]; B42 uses registries and
  script blocks [12] [31].
- **Recipes.** `Recipe` accessors largely gone, `CraftRecipe` added [9] [8];
  the script block changes from `Recipe` to `craftRecipe` [31].
- **Fluids and water.** The B41 tainted-water and water-amount members
  are gone from `InventoryItem` and `IsoObject` and B42 adds fluid
  container members [2] [1].
- **Drainable uses.** Delta-style accessors replaced by use-count accessors
  on `DrainableComboItem` [7] [6].
- **Events and globals.** 35 events and 83 globals are B41-only (37 and 64
  against the 42.20.0 index) [14] [13] [2] [1] [36].
- **Security.** A 42.14 security patch removed modding-API functionality that
  42.20.0 restored [21]; 42.20.4 and 41.78.21 removed `loadstring` and
  `loadstream` [18]; 42.21 re-enabled them in B42 [17]; the posts reviewed do not
  state a B41 re-enable. The earlier March 2026 security updates affected only
  mods [19].
- **Multiplayer.** New networking since 42.13.0 with a migration guide [33]
  [23].
- **Registries and script properties.** New IDs need `registries.lua`;
  `Type` became `ItemType`, `DisplayName` was removed and tags need
  registration [34].
- **Timed actions.** Shared-folder placement, matching `new` arguments,
  `getDuration` and the `perform`/`complete` split [35].
- **File writes.** `getFileWriter` extension limit from 42.20.0 [32]; 42.20.1
  added `.json` writing for mods [37].
- **Translations.** `%%` for a literal `%` from 42.20.1 [37] [38]; localization
  system updated in 42.21 [39].

# Practical Guidance

The checklist below is ordered so that cheap, mechanical checks come first.

1. **Fix the folder layout first.** Create `common/` and a version folder
   such as `42/`, move `media/` into it, and copy `mod.info` there. Keep the
   B41 root `media/` in place if you still support B41 [28] [29].
2. **Run a name census on your own code.** Extract every `Class:method`,
   event and global call from your Lua and compare each to the B42
   index; the script under Verification Steps does the lookups. A hit in the
   removed lists above means check the "where to look" column [1] [2].
3. **Treat a missing name as a question, not a verdict.** Look for a
   similarly named member on the same class, then on its parents, then in
   the unofficial JavaDocs and the game's own Lua. Example: the pair
   `getSaveName` and `getCurrentSaveName` looks like a rename [2] [1].
4. **Stats and moodles.** Replace typed getters with the generic accessor
   and constants, then test value ranges in game because the stub does not
   state them [3] [4] [5].
5. **Traits and professions.** Move to script-defined traits and the
   registry classes; calls such as `IsoGameCharacter:hasTrait` *(B42)* remain
   [31] [12] [15].
6. **Recipes.** Rewrite `Recipe` scripts as `craftRecipe` blocks and replace
   Lua that walks recipe objects with the `CraftRecipe` members [8] [31].
   Player-side recipe behaviour is in `players-crafting-chains`.
7. **Events.** Replace removed events with the nearest B42 event or a
   polling handler on `Events.OnTick`, and verify timing in game [13] [14].
8. **Multiplayer.** Port command handling before gameplay logic; see
   `modders-mp-networking-porting` for the detail [23] [35].
   - Convert every timed action: move it to `media/lua/shared`, align `new`
     arguments with field names, add `getDuration`, and split `perform` from
     `complete` [35].
   - Create and change items on the server, then sync them with the calls
     listed in the Reference [35].
   - Register new traits, professions, tags and item types in
     `registries.lua` and update item scripts (`ItemType`, no `DisplayName`);
     see `modders-item-scripts-distributions` [34].
9. **Publish.** Upload one item with both layouts, keep the description
   text outside the uploader, and ship deleted files emptied [28] [30].
10. **Guard shared code.** If one codebase serves both builds, branch on
    `getGameVersion` (present in both builds) and keep build-specific
    calls in separate version folders [1] [2] [28].

The related guides are `modders-lua-api-surface` (API orientation),
`modders-events-callbacks` (event semantics), `modders-modoptions-pzapi`
(options), `modders-item-scripts-distributions` (script and distribution
detail), `modders-modinfo-modid-conventions` (IDs) and
`modders-first-mod-tutorial-b42` (a clean B42 start).

# Common Pitfalls & Troubleshooting

- **Treating absence as deletion.** The `getSaveName` and
  `getCurrentSaveName` pair shows names do change [2] [1].
- **Trusting presence.** A name present in both indices (for example
  `Recipe:getResult` *(B42)*) may behave differently; the stubs hold
  signatures only [8] [9].
- **Reading the added counts as new features.** The B42 pin documents far
  more classes (3,293 against 1,686 tree entries) [1] [2].
- **Chasing UI field removals.** `x`, `y`, `width` and `height` on UI
  subclasses are stub noise because `ISUIElement` still declares them
  [27] [1].
- **Forgetting the post-42.20.0 changes.** 42.20.4 removed and 42.21
  restored `loadstring` and `loadstream`; code tested only on one patch can
  fail on another [18] [17]. Do not use a missing stub to decide that a
  function is gone [1] [36].
- **Literal percent signs in translations.** Use `%%`; the dual-handling
  workaround is temporary [37] [38].
- **Skipping `registries.lua`.** The guide requires it for new IDs and for
  tags and item types used in scripts [34].
- **Keeping duration as a `new` argument.** The guide says it must come from
  `getDuration` [35].
- **When something breaks.** The official guide itself says to read the
  decompiled Java [34].
- **Dropping the root `media/` too early.** B41 players still need it [28].
- **Mod options code.** The options API changed; see
  `modders-modoptions-pzapi` and the foundation delta [22].

# Community Notes & Unverified Claims

## Claim 1 — Adding a common folder to an old B41 mod is enough to make it work on B42

- **Claim:** Modding-community chatter holds that many simple B41 mods run on
  B42 after only adding `common/` and a version folder.
- **Why unverified:** No primary source tested this; the index shows
  removals that would break mods calling those names, The Indie Stone
  said B41 mods are not compatible [22], and the official migration guide
  requires registries, script changes and timed-action changes beyond the
  folder layout [34] [35].
- **Confidence:** Low. It may hold for data-only mods but the claim as
  stated is untested.

## Claim 2 — The legacy41 branch is frozen and will receive no further fixes

- **Claim:** Community discussion treats B41 as frozen, so porting the
  other direction (B42 to B41) is not worth doing.
- **Why unverified:** The Indie Stone shipped 41.78.21 on 2026-08-26 [18],
  which conflicts with the claim; no statement on a legacy end date was found.
- **Confidence:** Low. Contradicted at least partly by a primary source.

# Risks & Caveats

- **Stub, not behaviour.** The index records names only; every behavioural
  change needs a patch note or an in-game test [1] [2].
- **Coverage asymmetry.** The B41 pin documents fewer classes, so additions
  are weak evidence and a few "removed" Lua classes might be unstubbed in B41
  or B42 rather than gone [1] [2].
- **Version lag.** The B42 stubs are 42.21.0, but 41.78.21 (2026-08-26) has
  no B41 stub pin [18], and stubs can trail behaviour (`loadstring`,
  `loadstream`) [17] [1].
- **Abridged change list.** The retrieved 42.21 forum notes abbreviate the long
  multiplayer and other fix lists to "selected" items, so a change absent from
  this document may still be in the full list [40].
- **Wiki lag.** The pzwiki pages cited for layout carry page versions of
  42.14.0 (Mod structure), 42.17.0 (mod.info) and 42.15.0 (Uploading mods)
  [28] [29] [30].
- **Guide vintage.** The two official PDFs are 42.13-era (posted 2025-12-11)
  while the symbol index is 42.21.0; a rule they state may have changed
  since, and the PDFs sit behind forum sign-in [23] [34] [35].
- **Rename guesses.** Pairs presented as probable renames are inferences
  from name similarity, not documented renames.

# Verification Steps

1. Open the two pinned stub trees [1] [2] and confirm the file you care about,
   for example the B42 Stats stub [3] and the B41 Stats stub [5].
2. Re-run the diff. With the two index files from `sources/schemas/` in
   hand (the current `api-index-B42.json` is 42.21.0; the 42.20.0 index is
   archived as `sources/schemas/archive/api-index-B42-42.20.0.json`), the
   following script reproduces the totals and the effective removals:

```python
import json
a = json.load(open("sources/schemas/api-index-B41.json"))
b = json.load(open("sources/schemas/api-index-B42.json"))
A, B = a["classes"], b["classes"]

def members(idx, cls, seen=None):
    seen = seen or set()
    if cls in seen or cls not in idx:
        return set()
    seen.add(cls)
    out = set(idx[cls]["members"])
    for parent in idx[cls]["parents"]:
        out |= members(idx, parent, seen)
    return out

print(len(set(A) - set(B)), len(set(B) - set(A)))
print(sorted(set(a["events"]) - set(b["events"])))
print(sorted(members(A, "Stats") - members(B, "Stats")))
```

3. Run `python scripts/check_api_exists.py` on your own notes to confirm any
   name you plan to rely on exists in the target build.
4. Test behaviour in game on 42.21 before shipping, since this document does
   not cover it.

# Open Questions

- Which of the rename candidates (`getSaveName` to `getCurrentSaveName`,
  typed stat getters to the generic stat accessor) preserve behaviour and units? The 42.20.1
  to 42.21 posts name no renames, so this stays open: resolve with in-game
  tests.
- Which events replaced the removed weather and time events? The nearest B42
  events could be mapped by reading the game's Lua.
- Do the 42.13 rules in the official PDFs (registries, `perform`/`complete`)
  still hold unchanged on 42.21? The 42.20.1 to 42.21 notes reviewed neither
  reverse nor restate them [37] [40]; the forum thread was not re-read.
- Which function allows the `.json` writes added in 42.20.1, and does the
  `getFileWriter` extension limit still apply? [37]
- Which situations trigger the `RuntimeException` for missing translations and
  recipes in 42.21? [40]
- Resolved: whether 42.20.1 to 42.21 changed the API names. By the stub index
  it added ten events, removed none, removed 21 globals (including the
  stub-lag case `loadstream`) and added four [1] [36].

# References

**Primary Sources**

- [1] **PZ-Umbrella project** — *Umbrella at commit 13d01f9ee58fa48773553920db56d06f0005e7f8 (release tag 42.21.0)*. https://github.com/PZ-Umbrella/Umbrella/tree/13d01f9ee58fa48773553920db56d06f0005e7f8 Accessed 2026-10-07.
- [2] **PZ-Umbrella project** — *Umbrella at commit fa2e7e1 (release tag 41.78.16)*. https://github.com/PZ-Umbrella/Umbrella/tree/fa2e7e19799740b57902f1cb4e989225c295c05e Accessed 2026-10-07.
- [3] **PZ-Umbrella project** — *Stats.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/characters/Stats.lua Accessed 2026-10-07.
- [4] **PZ-Umbrella project** — *CharacterStat.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/characters/CharacterStat.lua Accessed 2026-10-07.
- [5] **PZ-Umbrella project** — *Stats.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.characters/Stats.lua Accessed 2026-10-07.
- [6] **PZ-Umbrella project** — *DrainableComboItem.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/inventory/types/DrainableComboItem.lua Accessed 2026-10-07.
- [7] **PZ-Umbrella project** — *DrainableComboItem.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.inventory.types/DrainableComboItem.lua Accessed 2026-10-07.
- [8] **PZ-Umbrella project** — *CraftRecipe.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/scripting/entity/components/crafting/CraftRecipe.lua Accessed 2026-10-07.
- [9] **PZ-Umbrella project** — *Recipe.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.scripting.objects/Recipe.lua Accessed 2026-10-07.
- [10] **PZ-Umbrella project** — *ISHandcraftWindow.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/lua/client/ISUI/Crafting/ISHandcraftWindow.lua Accessed 2026-10-07.
- [11] **PZ-Umbrella project** — *TraitFactory.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.characters.traits/TraitFactory.lua Accessed 2026-10-07.
- [12] **PZ-Umbrella project** — *Registries.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/scripting/objects/Registries.lua Accessed 2026-10-07.
- [13] **PZ-Umbrella project** — *events.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/events.lua Accessed 2026-10-07.
- [14] **PZ-Umbrella project** — *Events.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events.lua Accessed 2026-10-07.
- [15] **PZ-Umbrella project** — *IsoGameCharacter.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/characters/IsoGameCharacter.lua Accessed 2026-10-07.
- [16] **PZ-Umbrella project** — *IsoGameCharacter.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.characters/IsoGameCharacter.lua Accessed 2026-10-07.
- [17] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/ogg/108600/announcements/detail/1844751498231307 — found via the Steam news API [20]. Accessed 2026-10-07.
- [18] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/ogg/108600/announcements/detail/1842212951296601 — found via [20]. Accessed 2026-10-07.
- [19] **The Indie Stone** — *Important Security Updates* (Steam announcement, March 2026, updated 2026-03-20). https://steamcommunity.com/ogg/108600/announcements/detail/1827626365750608 — found via [20]. Accessed 2026-10-07.
- [20] **Valve** — *Steam News Web API (ISteamNews), app 108600*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=40&maxlength=0 Accessed 2026-10-07.
- [21] **The Indie Stone** — *PROJECT ZOMBOID BUILD 42.20 RELEASED!* (2026-07-29). https://projectzomboid.com/blog/news/2026/07/project-zomboid-build-42-20-released/ — verified via the Steam news mirror [20]. Accessed 2026-10-07.
- [22] **The Indie Stone** — *Build 42 Unstable* (2024-12-17). https://projectzomboid.com/blog/news/2024/12/build-42-unstable/ Accessed 2026-10-07 (host bot-blocks checkers).
- [23] **The Indie Stone Forums** — *Modding Migration Guide (42.13)*, first post by moderator nasKo, 2025-12-11. https://theindiestone.com/forums/topic/88499-modding-migration-guide-4213/ Accessed 2026-10-07 (host bot-blocks checkers; attachments need forum sign-in).
- [24] **PZ-Umbrella project** — *ScriptManager.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/scripting/ScriptManager.lua Accessed 2026-10-07.
- [25] **PZ-Umbrella project** — *IsoPlayer.lua, B41 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.characters/IsoPlayer.lua Accessed 2026-10-07.
- [26] **PZ-Umbrella project** — *IsoPlayer.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/characters/IsoPlayer.lua Accessed 2026-10-07.
- [27] **PZ-Umbrella project** — *ISUIElement.lua, B42 pin*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/lua/client/ISUI/ISUIElement.lua Accessed 2026-10-07.

- [34] **The Indie Stone** — *Migration Guide.pdf*, attachment to [23] (registries, script and Lua changes for 42.13). Retrieved 2026-10-07 from the forum thread [23]; no direct file URL.
- [35] **The Indie Stone** — *Project Zomboid: API for Inventory Items*, document version 1.0, attachment to [23]. Retrieved 2026-10-07 from the forum thread [23]; no direct file URL.

- [36] **PZ-Umbrella project** — *Umbrella at commit 58204fc47895ba249592519cedecc7cfbaaebd60 (previous B42 pin, release 42.20.0)*; the archived 42.20.0 symbol index in `sources/schemas/archive/` was built from it. https://github.com/PZ-Umbrella/Umbrella/tree/58204fc47895ba249592519cedecc7cfbaaebd60 Accessed 2026-10-07.
- [37] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766 Accessed 2026-10-07 (host bot-blocks checkers).
- [38] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441 Accessed 2026-10-07 (host bot-blocks checkers).
- [39] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925 Accessed 2026-10-07 (host bot-blocks checkers).
- [40] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first post, 2026-09-23; the long fix lists are abridged to "selected" in the retrieved copy). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 (host bot-blocks checkers).
- [41] **PZ-Umbrella project** — *Umbrella release list* (the 42.20.0 tag now points at a later commit than the 58204fc pin; see `sources/pins.json`). https://github.com/PZ-Umbrella/Umbrella/releases Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [28] **PZwiki** — *Mod structure* (revision 1443271, page version 42.14.0). https://pzwiki.net/wiki/Mod_structure Accessed 2026-10-07. Fact-only source.
- [29] **PZwiki** — *mod.info* (revision 1363935, page version 42.17.0). https://pzwiki.net/wiki/Mod.info Accessed 2026-10-07. Fact-only source.
- [30] **PZwiki** — *Uploading mods* (revision 1442321, page version 42.15.0). https://pzwiki.net/wiki/Uploading_mods Accessed 2026-10-07. Fact-only source.
- [31] **PZwiki** — *Scripts* (revision 1442815, page version 42.17.0). https://pzwiki.net/wiki/Scripts Accessed 2026-10-07. Fact-only source.
- [32] **PZwiki** — *Build 42.20.0* (revision 1443641). https://pzwiki.net/wiki/Build_42.20.0 Accessed 2026-10-07. Fact-only source.
- [33] **PZwiki** — *Multiplayer* (revision 1336919, page version 42.13.0). https://pzwiki.net/wiki/Multiplayer Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating** — none.

**Community & Creator** — none.

# Further Reading

- The Umbrella repository README and release list for newer stub pins.
- The unofficial B42 JavaDocs (see `modders-foundation`) for the Java-side
  signatures behind the stubs.

# Related Documents

- `modders-foundation` — ecosystem, toolchain and where API truth lives.
- `modders-lua-api-surface`, `modders-events-callbacks`,
  `modders-modoptions-pzapi`, `modders-item-scripts-distributions`,
  `modders-mp-networking-porting`, `modders-modinfo-modid-conventions`,
  `modders-first-mod-tutorial-b42`.
- `players-crafting-chains` (player-side crafting), `admins-workshop-mod-wiring`
  (server-side mod wiring), `meta-style-guide`.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft from the pinned B41/B42 Umbrella symbol diff. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (virtual agent) | Added checklist items and a Reference section from the official TIS 42.13 migration guide and inventory-items API PDFs; softened Claim 1; noted guide vintage. | — |
| 0.3.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined from 42.20 to 42.21: all index totals and named examples recomputed against Umbrella 42.21.0 (13d01f9), 42.20.0 figures kept for comparison; corrected `ISFurnaceLogicPanel`, `DrainableComboItem:getCurrentUses` and `ItemPickerJava` (13 to 22) statements; added 42.20.1-42.21 changes (`%%`, .json writes, localization, Lua checksum and anti-cheat, loadstring/loadstream stub lag). Sources: Steam posts 42.20.1, 42.20.2, 42.20.4, 42.21 unstable and stable, TIS forum 42.21 notes. | — |
