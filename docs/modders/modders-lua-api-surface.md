---
id: modders-lua-api-surface
title: "The Project Zomboid Lua API Surface: Java-Exposed Classes, Globals and the Per-Build Differences"
version: 0.2.0
status: in-review
confidence: Medium
category: Modders
topic: "Lua API surface"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-events-callbacks, modders-modoptions-pzapi, modders-item-scripts-distributions, modders-mp-networking-porting, modders-modinfo-modid-conventions, modders-first-mod-tutorial-b42, modders-porting-b41-to-b42, players-crafting-chains, admins-workshop-mod-wiring, meta-style-guide]
tags: [modding, lua, api, umbrella, stubs, java-exposed, globals, events, b41-vs-b42, kahlua]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-lua-api-surface |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16 (stubs), 42.21.0 (stubs; 42.20.0 stubs kept for comparison) |

# Executive Summary

Mods written in Lua reach the game through two kinds of surface: Java classes
and global functions that the engine exposes to the Kahlua interpreter, and
the game's own Lua files, which are ordinary Lua tables and functions. The
community-maintained Umbrella stub library describes both. At the pinned
Build 42 commit (tagged 42.21.0) it is split into a Java-exposed tree, a vanilla-Lua tree and a
single events file; at the pinned Build 41 commit the same material is
organised differently, under `Candle`, `Lua` and `Events` folders [2] [8] [13] [14].
This document explains how to read those stubs, how inheritance and overloads
are expressed, which globals every mod leans on, and how to find the class and
method for a task.

The headline difference between builds is scale and shape. Counting stub
files at the pins, the Java-exposed tree grew from 581 files on B41 to 1429 on
B42, and the vanilla-Lua tree from 890 to 1397 [13] [14]. The symbol index
the knowledge base derived from the same stubs holds 1498 classes on B41 and
4124 on B42; 1333 classes are present in both, 165 only in B41 and 2791 only
in B42 [13] [14]. Concrete removals and renames (for example
`InventoryItemFactory` and `TraitFactory` gone from the B42 index) are listed in the
Delta section. Between the 42.20.0 and 42.21.0 stub sets the B42 index lost 155
classes (mostly generated `CraftRecipeCode.*` helper entries and debug or
tutorial Lua classes) and gained 13 [13] [22].

Confidence is Medium. Every symbol claim is pinned to a named Umbrella commit
and therefore reproducible, but the stubs are community-generated, they lag the
game (a stub absence is not proof of removal: `loadstream` vanished from the
stubs although the game re-enabled it in 42.21 [7] [15] [23]), and the B41 stubs are in an older generator
format that records inheritance for only part of the classes in our index.

# Key Takeaways

- The Umbrella B42 pin has `library/java` (Java-exposed classes and
  globals), `library/lua` (vanilla Lua) and `library/events.lua`; the B41 pin
  uses `library/Candle`, `library/Lua` and `library/Events`. *(cited)* *(both)*
- A stub class line such as `---@class IsoPlayer: IsoLivingCharacter, ...`
  encodes inheritance; methods inherited from a parent are looked up on the
  parent's stub, not repeated. *(cited)* *(B42)*
- Overloads appear as repeated function declarations, one per signature:
  `IsoGridSquare:AddWorldInventoryItem` has nine in the B42 stub. *(cited)* *(B42)*
- `getSpecificPlayer(playerIndex)` is the stub-documented, split-screen-safe
  way to get a player; `getPlayer()` is documented as the single current
  player. *(cited)* *(B42)*
- The 42.21.0 stub index has 244 events (10 more than the 42.20.0 index), versus
  240 in the B41 index; 39 are new and 35 are gone. *(cited)*
- Stubs are not the game: the 42.20.0 stubs declared `loadstream`, the 42.20.4
  hotfix removed `loadstring` and `loadstream` from the game, 42.21 re-enabled
  them, and the 42.21.0 stubs no longer declare `loadstream`. *(cited)* *(B42)*
- The 42.21.0 stubs are the verification baseline of this document (42.21 stable,
  2026-09-28). *(cited)*

# Purpose

To answer, for a modder who has read the foundation document, the practical
questions: what exactly is "the API" as Lua sees it, how do I read a stub
file, where do I look to find the class and method for a task, and what changed
in the exposed surface between Build 41 and Build 42.

# Scope

Covered: the structure of the Umbrella stub library at the pinned commits;
how to read class, field, overload and annotation syntax; the global function
layer; a method for locating symbols; and a computed B41 versus B42 comparison
of classes, events, globals and selected members. Not covered: the semantics
and timing of individual events (see modders-events-callbacks), script-block
syntax (see modders-item-scripts-distributions), options UIs (see
modders-modoptions-pzapi) and multiplayer command patterns (see
modders-mp-networking-porting). Anything after 42.21.0 is out of scope except
where flagged.

# Definitions

- **Stub** — a Lua file containing only declarations and EmmyLua annotations,
  with empty function bodies, whose job is to feed editor tooling [1].
- **Java-exposed class** — a game Java class whose public members Lua code can
  call; non-public members are not reachable [21].
- **Index** — the knowledge base's own machine-readable symbol list
  (classes, events, globals) extracted from the stubs at each pin; it is the
  lookup truth for this document's API gate.
- **Pin** — the exact Umbrella commit used: B42 `13d01f9ee58fa48773553920db56d06f0005e7f8`
  (release tag 42.21.0) and B41 `fa2e7e19799740b57902f1cb4e989225c295c05e`
  (release tag 41.78.16) [2] [8]. The earlier B42 pin of this document was
  `58204fc47895ba249592519cedecc7cfbaaebd60`; the upstream `42.20.0` tag now
  resolves to a different commit (`98f50ae`), so cite commits, not tags [25].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | Umbrella stubs tagged 41.78.16 (commit fa2e7e1) [8]; no newer B41 stub tag exists | Older generator format; the legacy41 line has since reached 41.78.21 (2026-08-26) [16] |
| B42 (stable) | Yes | Umbrella stubs tagged 42.21.0 (commit 13d01f9) [2]; 42.21 stable notes [15] and forum patch notes [23] | Stable moved to 42.21 on 2026-09-28 [15] [19]; the unofficial API docs site reports 42.21.0 [18] |

Re-baselined 2026-10-07 from 42.20.0 to 42.21: the stub-derived statements were
re-checked against the 42.21.0 stubs and index, and the 42.20.1 to 42.21 official
notes were read for statements that touch the Lua surface [24] [16] [15] [23].
Statements not touched by either are carried forward from the 42.20.0 review
with no contradicting change found; they were not re-tested in-game. The
42.20.0 release itself is documented in the official announcement [17].

# Reference

## How the stub library is laid out

**Build 42 pin.** The repository root carries a README and CONTRIBUTING file
plus `library/`. Inside it, the tree lists `library/events.lua` (one file),
`library/java` (1429 files) and `library/lua` (1397 files) [13]. The README
states that Umbrella is a set of EmmyLua type stubs for the Lua API, aimed at
language servers for intellisense and type checking [1]. The Java tree is
organised by Java package, for example `library/java/zombie/iso/IsoGridSquare.lua`
and `library/java/zombie/characters/IsoPlayer.lua` [4] [5]. Files whose names
begin with two underscores hold package-less material: `library/java/__global.lua`
declares the global functions, and `library/lua/__kahlua.lua` declares
interpreter-level functions [6] [7]; at 42.20.0 that file declared `loadstream`, and the 42.21.0 version does not [22] [7]. The vanilla-Lua tree
mirrors the game's own Lua folders (`client`, `server`, `shared`) and also
contains `library/lua/__definitions.lua`, which declares helper types
namespaced `umbrella.*` [13] [20].

**Build 41 pin.** The same material sits in a different arrangement:
`library/Candle` (581 files, folders named by dotted package such as
`zombie.iso` and `zombie.characters`), `library/Lua` (890 files) and
`library/Events` with two files, `library/Events/Events.lua` and `library/Events/Events-deprecated.lua` [14] [11] [12].
In B41 an event the stub authors had flagged as deprecated lives in the second
file [12].

**Format generations.** The B41 stub for `IsoGridSquare` is written in an older
generator style: a `--- @class` header, a block of `--- @field public ...`
lines, then methods declared as `function IsoGridSquare:getZ() end` with
`--- @public` and `--- @return int` annotations [9]. The B42 stub uses compact
`---@class`, `---@param` and `---@return` annotations, with the method declared
on a local table named `__IsoGridSquare` [4].

## Reading a B42 stub

| Element | What it looks like | What it tells you |
|---------|--------------------|-------------------|
| Class header | `---@class IsoPlayer: IsoLivingCharacter, IAnimalVisual, IHumanVisual, IPositional` | Parent classes and interfaces, comma-separated [5] |
| Method | `function __IsoPlayer:canSeeAll() end` with a `---@return boolean` line above | Instance method; the colon means call it on an object [5] |
| Parameters | One `---@param name type` line per argument | Argument names and types [4] |
| Overloads | The same method name declared repeatedly with different `@param` lists | Each declaration is one Java signature [4] |
| Deprecation | A `---@deprecated` line above a method | The stub authors flag the member as deprecated; `IsoPlayer:getPlayerNum` carries this flag [5] |

`IsoGridSquare:AddWorldInventoryItem` shows overloads clearly: the B42 stub
declares it nine times, with first parameters typed as `string`, `ItemKey`
and other forms, and with or without a trailing `autoAge` boolean [4]. The
B41 stub for the same class declares it once [9].

Because a child class stub does not repeat inherited methods in the compact
format, resolving a method means walking the parent chain from the `@class`
line. `IsoGameCharacter` in the B42 index names sixteen parents and
interfaces, and `IsoObject` names six [13]. The community Lua API
description gives the same idea for `IsoZombie`: it descends from the Java
object type through the entity, object and moving-object classes into the
character class, and inherits all their fields and methods [21].

## Which members are visible to Lua

Only public members of a Java class are exposed to Lua; nested classes are
written with a dot between outer and inner names, and instance versus static
members are called with a colon or a dot respectively [21]. The stubs follow
this by listing only what is callable, so a name absent from the stub is a
strong sign the member is not exposed. Absence from a stub can also mean the
stub is incomplete, which is why the unofficial JavaDocs remain the tie-breaker
for existence questions, as set out in the foundation document.

## The global function layer

The B42 file `library/java/__global.lua` declares free functions that need no
object [6]. Examples from that file:

- `getPlayer()` returns the current player, and its stub comment advises
  using `getSpecificPlayer()` instead to support split-screen [6].
- `getSpecificPlayer(player)` takes an integer player index and returns an
  `IsoPlayer` [6].
- `instanceItem(item)` has four overloads, taking an `Item`, a `string`, a
  string plus a `useDelta` number, or an `ItemKey`, and returns an
  `InventoryItem` [6].

The knowledge-base index lists 664 global names for B41 and 930 for B42 (947 at 42.20.0); the
index includes globals declared in the vanilla-Lua tree as well as the Java
global file, so it is an upper bound on the engine-provided set [13] [14].
`getSpecificPlayer`, `getPlayer`, `getCell`, `getText`, `ZombRand`,
`sendClientCommand`, `isClient` and `isServer` appear in both indexes [13] [14]. `loadstring` is in neither index, and `loadstream` is in the B41 index only, so the indexes cannot be used to tell whether either function exists in the running game [13] [14] [23].

## Events

In the B42 pin all events are declared in one file, `library/events.lua`, in
which each event is a table with `Add` and `Remove` functions and a
`Callback_*` alias describing the callback signature [3]. For instance
`Events.OnPlayerUpdate` is documented there as triggered each tick for each
local player and passing the player [3]. This document only maps how events
appear in the stubs; behaviour and ordering belong to modders-events-callbacks.

## Vanilla Lua versus Java-exposed

The `library/lua` tree (B42) and `library/Lua` tree (B41) describe the game's
own Lua classes, for example UI and timed-action classes whose names start with
`IS`. The index counts 873 classes whose names begin with `IS` on B42 (930 at 42.20.0) and 577
on B41 [13] [14]. These are ordinary Lua tables that a mod can read, override
or extend, unlike Java classes whose behaviour is fixed in the engine.

# B41 vs B42 Delta

All figures below are computed from the two pinned Umbrella commits via the
knowledge-base index (see Verification Steps for reproduction). Stub-file
counts come from the GitHub tree listings of each pin [13] [14].

## Structure and size

| Measure | B41 pin (41.78.16) | B42 pin (42.21.0) |
|---------|-------------------:|------------------:|
| Java-exposed stub files | 581 [14] | 1429 [13] |
| Vanilla-Lua stub files | 890 [14] | 1397 [13] |
| Event files | 2 [14] | 1 [13] |
| Classes in index | 1498 [14] | 4124 [13] |
| Events in index | 240 [11] [12] | 244 [3] |
| Global names in index | 664 [14] | 930 [13] |

Class comparison: 1333 names in both builds, 165 only in the B41 index and
2791 only in the B42 index [13] [14]. Counting only stub-file names in the
Java trees (excluding underscore files), 575 names exist on B41 and 1181 on
B42, with 493 shared, 688 added and 82 dropped [13] [14]. The two counting
methods differ because the index also includes Lua-side classes and nested
types.

## Added and removed classes

Present only in the B42 index, among many: `CharacterTrait`,
`FluidSample`, `FluidType`, `AnimalDefinitions` and `AnimalInventoryItem` [13].
Present only in the B41 index, among others: `InventoryItemFactory`,
`TraitFactory`, `ProfessionFactory`, `Profession`, `Trait` and
`MultiStageBuilding` [14]. Absence from the B42 index means no class with that
name is declared in the 42.21.0 stubs; it does not by itself say what replaced
it [13]. `CraftRecipeCode` itself was in the 42.20.0 index but is not in the 42.21.0
one, so it no longer appears in the B42-only list above [13] [22].

## Events

39 events are new in the B42 index and 35 left the B41 set; 205 are common [3] [11] [12]. Eight of the 39 arrived with 42.21.0, among them `OnForagePool`, `OnForageRequestZone`, `OnForageSpot`, `AcceptedMedicalCheck` and `RequestMedicalCheck`; two further 42.21.0 additions, `OnFillInventoryContextMenuNoItems` and `OnPreFillInventoryContextMenuNoItems`, existed on B41 and so shrink the B41-only list rather than extend the B42-only one [3] [22].
Examples of additions: `Events.OnZombieCreate` *(B42)* is documented as
triggered when a zombie is being spawned, with the zombie as argument [3].
Examples of events present in the B41 stubs but absent from `library/events.lua`
at the B42 pin: `Events.OnDusk` *(B41)* and `Events.OnDawn` *(B41)*, which the B41 stub
file for deprecated events carries with a `@deprecated` marker [12]. Further
B42-only names in the index include `LoadChunk`, `OnSleepingTick` and
`OnItemFound`; B41-only names include `OnRainStart`, `OnRainStop` and
`OnVehicleHorn` [13] [14].

## Members: added, removed, renamed and re-documented

Listed member counts per class (own members as stubbed, not inherited) rose
for most core classes. The B41 stub flattens differently from the B42 stub, so
treat these as indicative of stub richness, not of engine change [9] [4].

| Class | Listed members B41 | Listed members B42 |
|-------|-------------------:|-------------------:|
| IsoPlayer | 313 | 378 |
| IsoGridSquare | 336 | 560 |
| InventoryItem | 377 | 599 |
| ItemContainer | 235 | 295 |
| IsoWorld | 163 | 176 |

For the 1333 classes in both indexes, 2623 member names that the B41 stub
lists on a class are unreachable (neither on the class nor on any ancestor)
in the B42 index, spread over 355 classes [13] [14]. Verified individual
examples, one symbol per row:

| Symbol | State | Evidence |
|--------|-------|----------|
| `IsoPlayer:isCanSeeAll` *(B41)* | Declared in the B41 stub | [10] |
| `IsoPlayer:canSeeAll` *(B42)* | Declared in the B42 stub; same purpose appears under a new name | [5] |
| `IsoPlayer:getSurname` *(B41)* | Declared in B41; unreachable in the B42 index | [10] [13] |
| `IsoPlayer:getPlayerMoveDir` *(B41)* | Declared in B41; unreachable in the B42 index | [10] [13] |
| `IsoGameCharacter:HasTrait` *(B41)* | Declared in B41; the B42 index instead has the lowercase name below | [14] [13] |
| `IsoGameCharacter:hasTrait` *(B42)* | Declared in B42 only | [13] |
| `IsoGameCharacter:getCharacterTraits` | Declared in both indexes | [13] [14] |
| `SandboxOptions:getFoodLootModifier` *(B41)* | Declared in B41; unreachable in the B42 index | [14] [13] |
| `BodyDamage:getInfectionLevel` *(B41)* | Declared in B41; unreachable in the B42 index | [14] [13] |
| `IsoGridSquare:addGrindstone` *(B42)* | New in the B42 stub | [4] |
| `IsoGridSquare:addFreezer` *(B42)* | New in the B42 stub | [4] |
| `IsoPlayer:addAttachedAnimal` *(B42)* | New in the B42 index (animals) | [13] |
| `ItemContainer:getFirstFluidContainer` *(B42)* | New in the B42 index (fluids) | [13] |

`IsoPlayer:getPlayerNum` exists in both builds but is annotated deprecated in
the B42 stub only [5] [10].

## Inheritance data caveat

Parents are recorded for 1035 of the 1498 B41 classes and 1856 of the 4124
B42 classes in the index [13] [14]. `IsoPlayer` has one recorded parent on B41
(`IsoLivingCharacter`) against four on B42 [10] [5]. Inherited-member lookups
therefore work on both builds, but the B41 stubs do not list interfaces the
way the B42 headers do, so B41 ancestor chains are shorter in the stubs examined. Counting each B42 class's own listed members against everything reachable on B41 (with
inheritance), 10712 member names on the 1333 shared classes are not reachable on B41, spread over 720
classes. That figure is an upper-bound signal of growth, not a count of new
engine features, since the two stub generations document members differently [13] [14].

## After the pin

The 42.20.4 hotfix (2026-08-26), issued together with legacy 41.78.21,
removed the `loadstring` and `loadstream` methods as part of a security fix and
told mod authors to move code-from-server patterns to explicit commands [16].
Build 42.21 re-enabled both commands; the stable announcement apologises for
the disruption to modders and server admins [15], and the forum patch notes list
them as re-enabled [23]. The stub file `library/lua/__kahlua.lua` declared
`loadstream` at 42.20.0 [22] [7] and does not at 42.21.0 [7]; because the game
re-enabled the function, the stub change reflects stub lag or regeneration, not
a removal in the game [15] [23].

Other 42.20.x and 42.21 notes that touch what mods can do, none of which this
document traced into specific stub symbols: 42.20.1 added the ability for mods
to write `.json` files [24]; 42.20.1 and 42.20.2 changed percent-sign handling in
translation strings so that mods should write `%%` for a literal `%`, with a
temporary workaround accepting both forms that the notes say will be removed in
a future unstable update [24] [26]; 42.20.1 and 42.21 improved or expanded the
Lua checksum and anti-cheat validation in multiplayer [24] [23]; and 42.21
updated the localization system to allow more translatable strings [23].

# Practical Guidance

- **Find a symbol in four steps.** (1) Identify the object you have: events
  hand you typed arguments, so start from the event's `Callback_*` alias in the
  events file [3]. (2) Open that class's stub by its package path in the Java
  tree [4]. (3) If the method is not there, walk the `@class` parents [5].
  (4) If it is a free function, search the global file [6].
- **Do not treat a missing stub as a removal.** `loadstream` left the stubs
  between 42.20.0 and 42.21.0 while the game re-enabled it [22] [7] [15] [23].
- **Pin the stub version to your target build** and bump it deliberately; the
  repository layout differs between the B41 and B42 pins, so a path that works
  in one will not exist in the other [13] [14].
- **Write once, branch where the surface differs.** Where a name was renamed
  between builds, guard on the presence of the method rather than the version
  string. For instance, the B42 name `IsoPlayer:canSeeAll` replaces the B41 name
  `IsoPlayer:isCanSeeAll` in the stubs [5] [10].
- **Prefer indexed player access** in code that may run in split-screen:
  `getSpecificPlayer(0)` rather than `getPlayer()` [6].

```lua
-- Resolve a player's square and its floor level (both stubs declare these)
local player = getSpecificPlayer(0)
local square = player and player:getSquare()
local z = square and square:getZ()
```

- **Treat overloads as a Kahlua dispatch question.** The stub lists every
  signature, so pass arguments that match exactly one declared form, for
  instance an `ItemKey` or a plain `string` to `instanceItem` [6].

# Common Pitfalls & Troubleshooting

- **A method autocompletes but errors at runtime.** The stubs describe a
  specific game build; `loadstream` was declared in the 42.20.0 stubs yet was
  removed by the 42.20.4 hotfix, and then re-enabled in 42.21 [22] [16] [15].
  If it errors, check the exact game build [16] [23].
- **A method the stubs lack still works.** After 42.21 the stubs no longer declare
  `loadstream`, yet the game re-enabled it [7] [23].
- **A B41 mod calls a method the B42 stub lacks.** Compare against the symbol
  table above: `IsoPlayer:getSurname` and `BodyDamage:getInfectionLevel` are
  declared in B41 only [10] [13] [14].
- **Case-only renames.** `HasTrait` and `hasTrait` differ only by case between
  the builds' stubs, so a grep that is case-insensitive can hide the change [13] [14].
- **Following a path from a B42 tutorial in a B41 checkout.** The B41 pin has
  no `library/java` folder; the equivalent is `library/Candle` [14].
- **Treating a missing stub entry as proof.** Stubs are community-generated;
  corroborate with the JavaDocs or game files before concluding a member does
  not exist [1].

# Community Notes & Unverified Claims

## Claim 1 — The Java-exposed surface was deliberately widened for modders in 42.20

- **Claim:** Modding-community discussion holds that The Indie Stone exposed
  many new getters and setters in 42.20 in response to modder requests.
- **Why unverified:** The wiki mod-news summary says new getters and setters
  were added and invites requests through the official Discord, but this
  document found no official changelog line quantifying it, and our stub diff
  cannot attribute intent.
- **Confidence:** Medium. The direction is consistent with the 2878 B42-only
  classes, but the stated cause is not primary-sourced.

## Claim 2 — Missing B41 methods in B42 were removed for the animal, crafting or health rewrites

- **Claim:** Community explanations attribute dropped members such as
  `BodyDamage` getters to the Build 42 health and moodle rework.
- **Why unverified:** The stubs only prove absence from the exposed surface,
  not why it happened or whether a different class now provides the data.
- **Confidence:** Low. It is inference from naming, with no developer statement.

# Risks & Caveats

- **Stub currency.** Verified against 42.21.0 stubs (42.20.0 kept for comparison);
  later hotfixes may add, remove or rename members [15] [23].
- **Tag drift.** Umbrella release tags can be moved after publication; the upstream
  `42.20.0` tag no longer points at the commit this knowledge base first pinned, so
  always cite commits [25].
- **Community-generated source.** Umbrella is volunteer-maintained; both pins
  are release tags, but declarations can be wrong or incomplete [1].
- **Two generator generations.** The B41 and B42 stubs come from different
  tooling, so raw counts are not an apples-to-apples engine comparison [9] [4].
- **Index limitations.** The index treats a class as the union of its stub
  declarations; it does not record overload counts, and it records parents for
  1035 of 1498 B41 classes, with B41 headers listing no interfaces [13] [14].
- **Wiki lag.** The community Lua API page used for conceptual facts was last
  updated for 42.17.0 at the time it was snapshotted [21].
- **B41 baseline.** The legacy41 line moved past 41.78.16, but no newer B41
  stub tag exists, so B41 facts here reflect 41.78.16 stubs [16].
- **Not re-tested in-game.** Unchanged statements are carried forward from the 42.20 review.

# Verification Steps

1. Clone Umbrella and check out `13d01f9ee58fa48773553920db56d06f0005e7f8` (B42) and
   `fa2e7e19799740b57902f1cb4e989225c295c05e` (B41); confirm the folder layouts described above [13] [14].
2. Open `library/java/zombie/iso/IsoGridSquare.lua` at the B42 pin and count
   the declarations of `AddWorldInventoryItem` (nine) [4].
3. Open the B41 `library/Candle/zombie.iso` folder and do the same (one) [9].
4. Rebuild the index with the knowledge base's `scripts/extract_api_index.py`
   for each build, then diff the `classes`, `events` and `globals` keys to
   reproduce the counts in the Delta tables.
5. Grep `library/events.lua` (B42) and the two B41 event files for `OnDusk`
   and `OnZombieCreate` [3] [12].
6. To test the `loadstring` and `loadstream` caveat, call each on a 42.20.4 game
   (expected: removed [16]) and on a 42.21 or later game (expected: working [15] [23]).

# Open Questions

- Which of the 155 classes dropped from the index between 42.20.0 and 42.21.0
  were removed from the game, and which were only generator clean-up of stub
  helper entries? The notes do not say [13] [22] [23].
- When will the stubs declare `loadstring` and `loadstream` again, and will the
  `%%` compatibility workaround be removed in a stable build? [26] [23]
- Which of the 2623 unreachable B41 members were truly removed from the game
  and which merely moved to a different class?
- Will an official API reference replace the community stubs? The foundation
  document records TIS statements of intent only.

# References

**Primary Sources** — official announcements and the pinned Umbrella stubs.

- [1] **PZ-Umbrella project** — *Umbrella README* at commit 13d01f9 (B42 pin). https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/README.md Accessed 2026-10-07.
- [2] **PZ-Umbrella project** — *library/java tree* at commit 13d01f9 (B42 pin, release tag 42.21.0). https://github.com/PZ-Umbrella/Umbrella/tree/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java Accessed 2026-10-07.
- [3] **PZ-Umbrella project** — *library/events.lua* at commit 13d01f9. https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/events.lua Accessed 2026-10-07.
- [4] **PZ-Umbrella project** — *library/java/zombie/iso/IsoGridSquare.lua* at commit 13d01f9. https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/iso/IsoGridSquare.lua Accessed 2026-10-07.
- [5] **PZ-Umbrella project** — *library/java/zombie/characters/IsoPlayer.lua* at commit 13d01f9. https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/characters/IsoPlayer.lua Accessed 2026-10-07.
- [6] **PZ-Umbrella project** — *library/java/__global.lua* at commit 13d01f9. https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/__global.lua Accessed 2026-10-07.
- [7] **PZ-Umbrella project** — *library/lua/__kahlua.lua* at commit 13d01f9. https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/lua/__kahlua.lua Accessed 2026-10-07.
- [8] **PZ-Umbrella project** — *library/Candle tree* at commit fa2e7e1 (B41 pin, release tag 41.78.16). https://github.com/PZ-Umbrella/Umbrella/tree/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle Accessed 2026-10-07.
- [9] **PZ-Umbrella project** — *library/Candle/zombie.iso/IsoGridSquare.lua* at commit fa2e7e1. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.iso/IsoGridSquare.lua Accessed 2026-10-07.
- [10] **PZ-Umbrella project** — *library/Candle/zombie.characters/IsoPlayer.lua* at commit fa2e7e1. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.characters/IsoPlayer.lua Accessed 2026-10-07.
- [11] **PZ-Umbrella project** — *library/Events/Events.lua* at commit fa2e7e1. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events.lua Accessed 2026-10-07.
- [12] **PZ-Umbrella project** — *library/Events/Events-deprecated.lua* at commit fa2e7e1. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events-deprecated.lua Accessed 2026-10-07.
- [13] **GitHub** — *Git tree listing of PZ-Umbrella/Umbrella at the B42 pin 13d01f9 (recursive)*. https://api.github.com/repos/PZ-Umbrella/Umbrella/git/trees/13d01f9ee58fa48773553920db56d06f0005e7f8?recursive=1 Accessed 2026-10-07.
- [14] **GitHub** — *Git tree listing of PZ-Umbrella/Umbrella at the B41 pin (recursive)*. https://api.github.com/repos/PZ-Umbrella/Umbrella/git/trees/fa2e7e19799740b57902f1cb4e989225c295c05e?recursive=1 Accessed 2026-10-07.
- [15] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/ogg/108600/announcements/detail/1844751498231307 — located via the Steam news API (ISteamNews, app 108600). Accessed 2026-10-07.
- [16] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/ogg/108600/announcements/detail/1842212951296601 — located via the Steam news API. Accessed 2026-10-07.
- [17] **The Indie Stone** — *PROJECT ZOMBOID BUILD 42.20 RELEASED!* (29 July 2026). https://projectzomboid.com/blog/news/2026/07/project-zomboid-build-42-20-released/ Accessed 2026-10-07 (host bot-blocks checkers).
- [18] **PZ-Wiki-Modding project** — *PZ API Documentation* (site header states 42.21.0). https://pz-wiki-modding.github.io/PZ-API-Docs/ Accessed 2026-10-07.
- [19] **Valve** — *Steam News Web API (ISteamNews), app 108600*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=40&maxlength=0 Accessed 2026-10-07.
- [20] **PZ-Umbrella project** — *library/lua/__definitions.lua* at commit 13d01f9. https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/lua/__definitions.lua Accessed 2026-10-07.
- [22] **GitHub** — *Git tree listing of PZ-Umbrella/Umbrella at the previous B42 pin 58204fc (42.20.0 stub set; also used for 42.20.0 index comparisons)*. https://api.github.com/repos/PZ-Umbrella/Umbrella/git/trees/58204fc47895ba249592519cedecc7cfbaaebd60?recursive=1 Accessed 2026-10-07.
- [23] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, 2026-09-23). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 (host bot-blocks checkers).
- [24] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766 Accessed 2026-10-07 (host bot-blocks checkers).
- [25] **GitHub** — *Git ref of tag 42.20.0 in PZ-Umbrella/Umbrella (resolves to commit 98f50ae)*. https://api.github.com/repos/PZ-Umbrella/Umbrella/git/ref/tags/42.20.0 Accessed 2026-10-07.
- [26] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441 Accessed 2026-10-07 (host bot-blocks checkers).

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [21] **PZwiki** — *Lua (API)* (revision 1390433, page version 42.17.0). https://pzwiki.net/wiki/Lua_(API) Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating** — none used.

**Community & Creator** — none cited as evidence (see the quarantined claims).

**Further Reading** — see the Further Reading section.

# Further Reading

- The foundation document's table of API-truth artifacts (Umbrella,
  JavaDocs, LuaDocs, ZomboidDoc) and its tier order for answering API
  questions: modders-foundation.
- Albion's unofficial Build 42 JavaDocs: https://albion.codeberg.page/PZ-JavaDocs/

# Related Documents

- modders-foundation — ecosystem and where API truth lives; this document goes deeper on the stub layer.
- modders-events-callbacks — event semantics and ordering.
- modders-modoptions-pzapi — the options API.
- modders-item-scripts-distributions — script-side item definitions.
- modders-mp-networking-porting — multiplayer command patterns.
- modders-modinfo-modid-conventions — manifest and ID conventions.
- modders-first-mod-tutorial-b42 — a worked first mod.
- modders-porting-b41-to-b42 — porting checklist that consumes this delta.
- players-crafting-chains — the player-side view of crafting.
- admins-workshop-mod-wiring — server-side mod deployment.
- meta-style-guide — how documents here are written and gated.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined from 42.20.0 to 42.21: Umbrella pin moved to 13d01f9 (42.21.0) and all index counts recomputed; `loadstring`/`loadstream` removed in 42.20.4 and re-enabled in 42.21, with the stub-lag caveat; mod `.json` writing, `%%` translation escaping, Lua checksum and localization notes added; Umbrella tag-drift note. Sources: Steam 42.20.1, 42.20.2, 42.20.4, 42.21 stable; TIS forum 42.21 patch notes; Umbrella 13d01f9. | — |
