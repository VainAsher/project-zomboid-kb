---
id: modders-events-callbacks
title: "Events and Callbacks: Hooking the Game Loop with Events.X.Add"
version: 0.1.0
status: in-review
confidence: Medium
category: Modders
topic: "Events & callbacks"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-05
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-lua-api-surface, modders-modoptions-pzapi, modders-item-scripts-distributions, modders-mp-networking-porting, modders-modinfo-modid-conventions, modders-first-mod-tutorial-b42, modders-porting-b41-to-b42, players-crafting-chains, admins-workshop-mod-wiring, meta-style-guide]
tags: [modding, lua, events, callbacks, umbrella, onTick, ongamestart, luaeventmanager, b41, b42]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-events-callbacks |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-05 |
| Game versions verified | 41.78.16 (Umbrella stubs), 42.20.0 (Umbrella stubs) |

# Executive Summary

Project Zomboid exposes its game loop to Lua through a global `Events`
table. Each event is an object with an `Add` and a `Remove` function; you
register a Lua function and the engine calls it when the event fires [1] [2].
The Umbrella type stubs declare 234 events for 42.20.0 and 240 events for
41.78.16 (the B41 figure includes 32 events the stubs flag as deprecated),
and every event has a `Callback_<Name>` type alias that records its parameter
list [1] [2] [3].

This document groups the full list by purpose, tabulates the events a mod
author reaches for most, explains the load-order and cost traps (OnGameBoot
versus OnGameStart versus OnNewGame, per-tick events), and diffs the two
builds' stubs. The B41 to B42 diff is concrete: 31 events were added, 37 were
dropped (32 of them were already deprecated on B41), and 54 callback
signatures differ in text, of which about a dozen are real parameter changes
rather than type-notation clean-ups [1] [2] [3].

Confidence is Medium. The facts come from pinned Umbrella stubs, which are
primary code truth for what is declared, but the stubs are community-written
type files, not a decompiled call graph, and nothing here was exercised
in-game. The verification build also trails the current stable releases (see
Build Applicability).

# Key Takeaways

- An event is registered with `Events.OnTick.Add(fn)` and unregistered with
  `Events.OnTick.Remove(fn)`; the stubs declare exactly those two functions on
  every event. *(cited)* *(both)* [1] [2]
- 42.20.0 declares 234 events, 41.78.16 declares 240 (208 current plus 32
  flagged deprecated). 203 names are common to both. *(cited)* *(both)* [1] [2] [3]
- B42 adds 31 events and drops 37 B41 names; 32 of the dropped names carry a
  deprecation flag in the B41 stubs. *(cited)* *(both)* [1] [2] [3]
- The stub descriptions label an event `(Client)`, `(Server)` or
  `(Multiplayer)`; 90 of the 234 B42 events carry no label at all, so the
  absence of a tag is not proof of where an event runs. *(cited)* *(B42)* [1]
- `OnGameBoot` fires before a client has run the files in `lua/server/`, so a
  callback added from a server-folder file is never called for that event on
  a client. *(cited)* *(both)* [1] [2]
- `OnTick` fires every game tick and `OnTickEvenPaused` fires even while the
  game is paused, so work in them is paid continuously. *(cited)* *(both)* [1] [2]
- A handful of callbacks changed shape between builds (for example
  `Events.OnMechanicActionDone` lost four parameters). Do not copy a B41
  handler to B42 without re-checking the signature. *(cited)* *(both)* [1] [2]
- Mod-defined events via `LuaEventManager.AddEvent` and
  `LuaEventManager.triggerEvent` are declared in the stubs, but how mods use
  them in practice is only community lore. *(cited stub shape; usage
  quarantined)* [4] [5]

# Purpose

Answer the question a new mod author asks right after "hello world": which
event do I hang my code on, what does the callback receive, where does it
run, and what changes if I also support the other build. It is the Modders
track's reference for the event system, going deeper than the overview in
modders-foundation, which only points at the Umbrella stubs.

# Scope

Covered: the `Events.<Name>.Add` and `.Remove` mechanism; callback signatures
as declared in the pinned Umbrella stubs; a purpose-based grouping of every
event in the stub index; the stub-level client, server and multiplayer
labels; ordering and cost pitfalls; the `LuaEventManager` API surface; and a
B41 to B42 diff of the event lists.

Not covered: what each Java class passed to a callback can do (see
modders-lua-api-surface), client-to-server command networking in depth (see
modders-mp-networking-porting), and per-event semantics that the stubs leave
blank. About 17 of the 234 B42 event stubs have no description beyond the
name, and this document says "undocumented in the stub" rather than
guessing [1]. Unstable-branch behaviour is out of scope.

# Definitions

- **Event** — a named hook in the Lua-visible `Events` table; stubs declare
  it as `Events.<Name> = { Add = ..., Remove = ... }` [1].
- **Callback** — the Lua function you register; its expected parameters are
  recorded in the event's `Callback_<Name>` alias [1].
- **Tick** — one iteration of the game's update loop; `OnTick` receives the
  number of ticks since the game started [1].
- **Context label** — the `(Client)`, `(Server)` or `(Multiplayer)` prefix in
  a stub description. It is documentation text written by the stub authors,
  not an enforced runtime restriction [1] [10].
- **LuaEventManager** — the Java class the stubs expose for creating and
  firing events [4].
- **Deprecated event** — one the B41 stubs mark with `@deprecated`; all 32
  live in a separate file [3].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | Umbrella 41.78.16 stubs, commit fa2e7e19799740b57902f1cb4e989225c295c05e [2] [3] [9] | Newest B41 stub tag available; legacy41 itself has since moved on to 41.78.21 (2026-08-26) [7] |
| B42 (stable) | Yes | Umbrella 42.20.0 stubs, commit 58204fc47895ba249592519cedecc7cfbaaebd60 [1] [9] | Stable 42.21 was released 2026-09-28 [6]; this document has not been checked against a 42.21 stub set |

Verification covers 42.20.0 stubs only. Build 42.21 stable shipped after the
stubs were pinned [6] [8], and the 42.21 announcement states the stable
release followed an unstable period and links to full patch notes on the
Indie Stone forums [6]. Treat any event added, removed or re-signatured in
42.21 as unchecked. The same pin applies to B41: 41.78.21 was released after
41.78.16, and its hotfix notes describe the removal of the `loadstring` and
`loadstream` Lua methods as a security fix [7]; whether that touches any
event is not established here.

# Reference

## The mechanism: Events.Name.Add and Remove

Every event in the stubs is a table with two functions, `Add(callback)` and
`Remove(callback)`, each taking a function typed as the event's
`Callback_<Name>` alias. For instance `Callback_OnTick` is declared as a
function taking one number, `tick` [1]. Events with no parameters are
declared with the alias `function`, such as the one for `Events.OnGameStart`
[1]. The B41 stubs use the same shape, but place events in
`library/Events/Events.lua` and, for deprecated ones,
`library/Events/Events-deprecated.lua`; B42 uses one file,
`library/events.lua` [1] [2] [3].

A minimal registration, in the shape the stubs describe:

```lua
local function onTick(tick)
    -- tick is the number of ticks since the game started [1]
end

Events.OnTick.Add(onTick)
-- later, with the same function value:
Events.OnTick.Remove(onTick)
```

## How the stubs label execution context

Stub descriptions may begin with one or two bracketed labels. Counting the
B42 stubs: 90 events are labelled `(Client)` only, 9 `(Server)` only, 34
`(Multiplayer) (Client)`, 6 `(Multiplayer) (Server)`, 5 `(Multiplayer)` alone,
and 90 carry no label [1]. The B41 counts are 92, 9, 35, 4, 3 and 65 over the
208 non-deprecated events [2]. The nine server-only B42 events are
`OnClientCommand`, `OnFillContainer`, `OnSGlobalObjectSystemInit`,
`OnUpdateModdedWeatherStage`, `OnWeaponHitThumpable`,
`OnWeatherPeriodComplete`, `OnWeatherPeriodStage`, `OnWeatherPeriodStart` and
`OnWeatherPeriodStop` [1]. The labels are descriptive text; the stubs do not
say what an unlabelled event does when registered on the other side [1].

## Events by purpose

The groups below are this document's own taxonomy applied to the stub index;
membership lists are representative, and the full list is in the stub files
[1]. Names are as declared, including the lower-case `on` prefix on a few
forage and search-mode events [1].

| Group | Representative members (B42 stubs) |
|-------|-------------------------------------|
| Time and tick | `OnTick`, `OnTickEvenPaused`, `OnRenderTick`, `OnFETick`, `OnSleepingTick`, `EveryOneMinute`, `EveryTenMinutes`, `EveryHours`, `EveryDays`, `OnClimateTick` [1] |
| Lifecycle and loading | `OnGameBoot`, `OnGameStart`, `OnNewGame`, `OnLoad`, `OnSave`, `OnPostSave`, `OnInitWorld`, `OnInitGlobalModData`, `OnGameTimeLoaded`, `OnPreMapLoad`, `OnPostMapLoad`, `OnLoadMapZones`, `OnLoadedTileDefinitions`, `OnMainMenuEnter`, `OnResetLua`, `OnModsModified` [1] |
| Data and distribution setup | `OnPreDistributionMerge`, `OnDistributionMerge`, `OnPostDistributionMerge`, `OnReceiveGlobalModData`, `OnSGlobalObjectSystemInit`, `OnCGlobalObjectSystemInit`, plus the `preAdd...Defs` and `onAddForageDefs` family [1] |
| Player and character | `OnCreatePlayer`, `OnPlayerUpdate`, `OnPlayerMove`, `OnPlayerDeath`, `OnCharacterDeath`, `OnEquipPrimary`, `OnEquipSecondary`, `OnClothingUpdated`, `AddXP`, `LevelPerk`, `OnPlayerGetDamage` [1] |
| Combat and zombies | `OnWeaponSwing`, `OnWeaponHitCharacter`, `OnHitZombie`, `OnZombieCreate`, `OnZombieUpdate`, `OnZombieDead`, `OnWeaponHitXp`, `OnPlayerAttackFinished` [1] |
| World and map | `LoadGridsquare`, `LoadChunk`, `OnObjectAdded`, `OnTileRemoved`, `OnObjectAboutToBeRemoved`, `OnContainerUpdate`, `OnNewFire`, `OnGridBurnt`, `OnSeeNewRoom`, `OnWaterAmountChange`, `OnDeadBodySpawn` [1] |
| Weather and climate | `OnClimateManagerInit`, `OnInitSeasons`, `OnWeatherPeriodStart`, `OnWeatherPeriodStage`, `OnWeatherPeriodStop`, `OnWeatherPeriodComplete`, `OnThunderEvent` [1] |
| Vehicles | `OnEnterVehicle`, `OnExitVehicle`, `OnSwitchVehicleSeat`, `OnUseVehicle`, `OnVehicleDamageTexture`, `OnSpawnVehicleStart`, `OnSpawnVehicleEnd`, `OnMechanicActionDone` [1] |
| UI, input and menus | `OnCreateUI`, `OnPreUIDraw`, `OnPostUIDraw`, `OnKeyStartPressed`, `OnKeyKeepPressed`, `OnKeyPressed`, `OnMouseDown`, `OnMouseWheel`, `OnFillWorldObjectContextMenu`, `OnFillInventoryObjectContextMenu`, `OnJoypadActivate`, `OnResolutionChange` [1] |
| Multiplayer client | `OnConnected`, `OnDisconnect`, `OnConnectFailed`, `OnServerCommand`, `OnReceiveGlobalModData`, `OnAddMessage`, `OnSafehousesChanged`, `OnSteamGameJoin`, `OnScoreboardUpdate` [1] |
| Multiplayer server | `OnClientCommand`, `OnServerStarted`, `OnServerStartSaving`, `OnServerFinishSaving`, `SendCustomModData`, `OnProcessAction`, `OnProcessTransaction` [1] |
| Steam and workshop plumbing | `OnSteamServerResponded`, `OnSteamRulesRefreshComplete`, `OnSteamWorkshopItemCreated`, `OnSteamWorkshopItemUpdated`, `OnServerWorkshopItems` [1] |
| Deprecated on B41, absent on B42 | 32 events including `OnRainStart`, `OnDawn`, `OnPreGameStart` and `OnMakeItem` (listed in the Delta) [3] |

## The events most mods use

Parameters are as declared in the B42 stubs unless a row says otherwise. A
row tagged *(B42)* was not found in the B41 stubs [1] [2] [3].

| Event | Label in stub | Callback parameters | What the stub says it does |
|-------|---------------|---------------------|-----------------------------|
| `Events.OnGameBoot` | none | none | Fires after the game finishes starting up; on clients, `lua/server/` files have not run yet [1] |
| `Events.OnGameStart` | Client | none | Fires on finishing loading and entering the game [1] |
| `Events.OnLoad` | Client | none | Same description as `OnGameStart` [1] |
| `Events.OnNewGame` | Client | `player`, `square` | A local player character was created for the first time [1] |
| `Events.OnCreatePlayer` | Client | `playerIndex`, `player` | Fires every time a local player loads into the world [1] |
| `Events.OnInitGlobalModData` | none | `newGame` | Earliest event after sandbox options load; `newGame` is true on a save's first start [1] |
| `Events.OnTick` | none | `tick` | Every game tick [1] |
| `Events.OnTickEvenPaused` | none | `tick` | Every game tick including while paused; `tick` is always zero while paused [1] |
| `Events.EveryOneMinute` | none | none | Every in-game minute [1] |
| `Events.EveryTenMinutes` | none | none | Every ten in-game minutes [1] |
| `Events.EveryHours` | none | none | Start of every in-game hour [1] |
| `Events.EveryDays` | none | none | 0:00 every in-game day [1] |
| `Events.OnPlayerUpdate` | Client | `player` | Each local player's update, every tick [1] |
| `Events.OnZombieUpdate` | Client | `zombie` | Whenever a zombie updates [1] |
| `Events.OnZombieDead` | none | `zombie` | A zombie dies; loot is not yet filled and the corpse does not exist for a few seconds [1] |
| `Events.OnCharacterDeath` | none | `character` | Any character dies, including zombies, players and animals [1] |
| `Events.OnPlayerDeath` | Client | `player` | A local player dies [1] |
| `Events.OnWeaponHitCharacter` | Client | `attacker`, `target`, `weapon`, `damage` | A non-zombie character is hit by a local player's attack [1] |
| `Events.OnHitZombie` | none | `zombie`, `attacker`, `bodyPart`, `weapon` | A character hits a zombie [1] |
| `Events.OnZombieCreate` *(B42)* | none | `zombie` | A zombie is being spawned [1] |
| `Events.LoadGridsquare` | none | `square` | After a new square loads [1] |
| `Events.OnObjectAdded` | none | `object` | An object is added to the world; usually not called on a client [1] |
| `Events.OnFillWorldObjectContextMenu` | Client | `playerIndex`, `context`, `worldObjects`, `test` | After a world context menu is filled [1] |
| `Events.OnFillInventoryObjectContextMenu` | Client | `playerIndex`, `context`, `items` | After an inventory item context menu is filled [1] |
| `Events.OnKeyPressed` | Client | `key` | Stub text says it fires when a key is released; `OnKeyStartPressed` is the press-down event [1] |
| `Events.OnPreDistributionMerge` | none | none | Distribution tables merge stage hook; its stub wording duplicates the post-merge text, so confirm order in-game [1] |
| `Events.OnPostDistributionMerge` | none | none | After the distribution tables have been merged [1] |
| `Events.OnEnterVehicle` | Client | `character` | A character enters a vehicle [1] |
| `Events.OnClientCommand` | Server | `module`, `command`, `player`, `args` | Server receives a command sent with `sendClientCommand`; `args` may be nil on B42 [1] |
| `Events.OnServerCommand` | Multiplayer, Client | `module`, `command`, `args` | Client receives a command sent with `sendServerCommand` [1] |
| `Events.OnReceiveGlobalModData` | Multiplayer | `key`, `data` | Receiving a global mod data table; `data` is false when none existed [1] |
| `Events.OnServerStarted` | Multiplayer, Server | none | The server started and can be connected to [1] |
| `Events.OnConnected` | Multiplayer, Client | none | Connected to a server from the main menu, before character creation [1] |

## Setup-order facts the stubs document

The stubs give these ordering anchors and no more: `OnGameBoot` fires after
the game finishes starting up and, on a client, before `lua/server/` files
have run [1]. `OnInitGlobalModData` is the earliest event after sandbox
options are loaded [1]. `OnGameTimeLoaded` fires after `GameTime` is
initialised and `OnInitWorld` after the world has initialised [1]. `OnSave`
fires after characters and sandbox options are saved but before global mod
data and the world are saved, and `OnPostSave` fires after saving and exiting
the game [1]. `OnNewGame` fires only on first creation of a local player
character, while `OnCreatePlayer` fires every time a local player loads in
[1]. The stubs do not publish a full ordering of these events relative to
each other [1].

## LuaEventManager: custom events

The stubs expose `LuaEventManager` with `LuaEventManager.AddEvent(name)`,
returning an `Event`, and `LuaEventManager.triggerEvent(event, ...)`, which
takes the event name plus up to eight further parameters on both builds [4]
[5]. They also declare `LuaEventManager.triggerEventGarbage` (up to four
parameters on B42) and `LuaEventManager.triggerEventUnique` (one parameter)
[4] [5]. B42 additionally lists `LuaEventManager.RunQueuedEvents`,
`LuaEventManager.getEvents`, `LuaEventManager.setEvents` and an `OnTickCallbacks`
list that B41 does not list *(B42)* [4] [5]. The stubs say nothing about the
intended modder workflow for these calls, so see Claim 1 for the community
pattern [4].

# B41 vs B42 Delta

Method: the KB's index extractor read the pinned Umbrella stubs for each build
and the two event lists were compared as sets of names; callback alias text was
compared per shared event [1] [2] [3] [9].

## Counts

| Measure | B41 (41.78.16) | B42 (42.20.0) |
|---------|----------------|---------------|
| Events declared | 240 [2] [3] | 234 [1] |
| Of which current (non-deprecated) | 208 [2] | 234 [1] |
| Of which flagged `@deprecated` | 32 [3] | 0 [1] |
| Names common to both | 203 [1] [2] [3] | 203 [1] [2] [3] |

## Added in B42 (31)

`GrappleGrabCollisionCheck`, `GrapplerLetGo`, `LoadChunk`, `OnAlertMessage`,
`OnAnimalTracks`, `OnClickedAnimalForContext`, `OnContextKey`,
`OnDeadBodySpawn`, `OnDesignationZoneUpdatedNetwork`,
`OnFishingActionMPUpdate`, `OnGoogleAuthRequest`, `OnItemFound`,
`OnMouseWheel`, `OnNetworkUsersReceived`, `OnProcessAction`,
`OnProcessTransaction`, `OnQRReceived`, `OnRolesReceived`,
`OnServerCustomizationDataReceived`, `OnSleepingTick`,
`OnSourceWindowFileReload`, `OnSpawnVehicleEnd`, `OnSpawnVehicleStart`,
`OnSteamServerFailedToRespond2`, `OnWarUpdate`, `OnZombieCreate`,
`RefreshCheats`, `RenderOpaqueObjectsInWorld`, `SetDragItem`, `ViewBannedIPs`
and `ViewBannedSteamIDs` [1] [2] [3]. Several are plain thematic additions the
stubs describe: a grappler releasing its target, chunk loading, a spawning
zombie, a dead body spawning, a vehicle beginning and finishing its spawn,
and the context key being held for a duration [1]. Many others, such as
`OnWarUpdate` and `OnItemFound`, have no description in the stub [1].

## Dropped from B42 (37)

32 are the B41 deprecated set: `OnAIStateEnter`, `OnAIStateExecute`,
`OnAIStateExit`, `OnAddBuilding`, `OnBeingHitByZombie`, `OnChangeWeather`,
`OnCharacterCreateStats`, `OnCharacterMeet`, `OnDawn`, `OnDoTileBuilding`,
`OnDusk`, `OnIsoThumpableLoad`, `OnIsoThumpableSave`, `OnLoginState`,
`OnLoginStateSuccess`, `OnMakeItem`, `OnMapLoadCreateIsoObject`,
`OnNPCSurvivorUpdate`, `OnNewSurvivorGroup`, `OnPlayerSetSafehouse`,
`OnPostCharactersSquareDraw`, `OnPostFloorSquareDraw`, `OnPostTileDraw`,
`OnPostTilesSquareDraw`, `OnPostWallSquareDraw`, `OnPreGameStart`,
`OnRadioInteraction`, `OnRainStart`, `OnRainStop`, `OnRenderUpdate`,
`OnVehicleHorn` and `OnWorldMessage` [3]. The remaining five were current on
B41 and are gone from the B42 stubs: `OnFillInventoryContextMenuNoItems`,
`OnPreFillInventoryContextMenuNoItems`, `OnGetDBSchema`, `OnGetTableResult`
and `OnServerStatisticReceived` [2] [1]. The B41 stub text for
`OnFillInventoryContextMenuNoItems` warns the event is not properly
registered, so a mod must register it before adding its function [2]. Absence
from the B42 stubs shows the name is no longer declared; it does not prove the
engine stopped firing a same-named event [1].

## Signature changes verified in the raw stubs

54 shared events have different alias text between builds [1] [2] [3]. Most are
notation (`float` and `double` became `number`; `short` became `integer`;
nullable `?` became `| nil`; `playerNum` renamed `playerIndex`). The changes
that alter what a handler receives:

| Event | B41 callback | B42 callback |
|-------|--------------|--------------|
| `Events.OnAmbientSound` | `x`, `y`, `z` as floats [2] | `name` (string), `x`, `y` *(B42)* [1] |
| `Events.OnMechanicActionDone` | `character`, `success`, `vehicleId`, `partType`, `itemId`, `installing` [2] | `character`, `success` only [1] |
| `Events.OnConnectionStateChanged` | `state`, `message`, optional `place` [2] | `state`, `message` [1] |
| `Events.OnServerWorkshopItems` | `type` only [2] | `type`, `items`, `error`, `maxSize` [1] |
| `Events.OnReceiveUserlog` | `username`, `logs` [2] | adds `suspiciousActivity` table [1] |
| `Events.OnPressRackButton` | `player`, `weapon` [2] | adds a third `shift` parameter [1] |
| `Events.OnWeaponHitXp` | `attacker`, `weapon`, `target`, `damage` [2] | adds a fifth `hitcount` parameter [1] |
| `Events.OnUseVehicle` | first parameter typed as a game character [2] | first parameter named `player`, typed as a player [1] |
| `Events.OnDoTileBuilding3` | cursor typed as the move cursor, optional `square` [2] | cursor typed as the building object, `square` dropped [1] |
| `Events.OnDestroyIsoThumpable` | `object` [2] | `object` plus a nil-typed `player` [1] |
| `Events.OnFETick` | no parameters [3] | one parameter `unknown`, described as always zero [1] |
| `Events.onItemFall` | no parameters [2] | `item` [1] |
| `Events.OnEquipPrimary` | `item` always an item [2] | `item` may be nil [1] |

`OnClientCommand`, `OnServerCommand` and `OnReceiveItemListNet` also gained
nilable parameters in the B42 declarations [1] [2]. The `OnFillWorldObjectContextMenu`
and inventory context-menu events keep the same four and three parameters in
both builds, with the first parameter renamed [1] [2].

# Practical Guidance

- **Choose the narrowest event.** Reach for `EveryTenMinutes`, `EveryHours` or
  `EveryDays` when the job is periodic, because `OnTick` and `OnPlayerUpdate`
  fire every tick [1].
- **Keep a handle for removal.** `Remove` takes the callback, so register a
  named local function rather than an anonymous one if you ever need to
  unregister [1].
- **Pick the right start-up event.** Use `OnGameBoot` only for things that
  must exist before gameplay and do not depend on `lua/server/` files;
  use `OnGameStart` or `OnCreatePlayer` for per-session setup; reserve
  `OnNewGame` for first-time character initialisation [1].
- **Initialise saved data on `OnInitGlobalModData`.** It is the earliest hook
  after sandbox options are loaded, and its `newGame` flag distinguishes a
  fresh save [1].
- **Branch on build when supporting both.** For `OnMechanicActionDone`,
  `OnServerWorkshopItems`, `OnAmbientSound` and the others in the Delta table,
  write the handler to tolerate both parameter lists, or ship a version folder
  per build as described in modders-foundation [1] [2].
- **Do not assume a label means safe on both sides.** For an unlabelled event,
  test on a dedicated server and a client before shipping [1].
- **Cross-reference.** Command networking and API-surface depth are in
  modders-mp-networking-porting and modders-lua-api-surface; porting the
  rest of a mod is in modders-porting-b41-to-b42.

# Common Pitfalls & Troubleshooting

- **"My OnGameBoot handler never runs on the client."** If the handler is
  added from a file in `lua/server/`, those files have not run yet when
  `OnGameBoot` fires on a client [1].
- **"OnNewGame does not fire when I load my save."** It fires only when a
  local player character is created for the first time; use `OnCreatePlayer`
  or `OnGameStart` for every load [1].
- **"The game stutters after I added my mod."** `OnTick`, `OnTickEvenPaused`,
  `OnRenderTick`, `OnPlayerUpdate` and `OnZombieUpdate` run continuously, the
  last per zombie update [1]. Move non-urgent work to an `Every...` event.
- **"A B41 handler gets nil or shifted arguments on B42."** Compare against
  the Delta table; for example `OnMechanicActionDone` has two parameters on
  B42 [1] [2].
- **"OnZombieDead gave me an empty inventory."** The stub says loot is not
  filled when it fires and the corpse does not exist for a few seconds [1].
- **"OnKeyPressed fires on release."** The stub text says exactly that;
  use `OnKeyStartPressed` or `OnKeyKeepPressed` for press and hold [1].
- **"A deprecated B41 event does nothing."** The 32 deprecated names are not
  declared on B42 [1] [3].
- **"I added an event handler on the server for a Client-labelled event."**
  Nothing in the stubs says it will be called there [1].

# Community Notes & Unverified Claims

## Claim 1 — Mod authors create custom events with LuaEventManager.AddEvent and fire them with triggerEvent

- **Claim:** Modding guides and Discord answers describe a pattern in which a
  mod registers its own event name once with `LuaEventManager.AddEvent`, other
  mods then subscribe through `Events.<YourName>.Add`, and the owner mod fires
  it with `triggerEvent`.
- **Why unverified:** The stubs declare the functions [4] [5] but no primary
  source found here shows the end-to-end pattern or confirms that a late
  `AddEvent` is visible to `Events`.
- **Confidence:** Low. It is plausible from the stub signatures but unproven
  against the game or a dev post.

## Claim 2 — OnTick handlers are the main cause of mod-induced lag

- **Claim:** Performance threads in modding communities say per-tick handlers
  are the usual culprit for FPS drops in modded games.
- **Why unverified:** No primary benchmark was found; the stubs establish only
  how often these events fire [1]. See also modders-foundation Claim 2.
- **Confidence:** Low. Widely repeated but unmeasured.

## Claim 3 — Unlabelled events run on both client and server

- **Claim:** Some community write-ups treat stub events with no
  `(Client)` or `(Server)` label as available on both sides.
- **Why unverified:** The stubs leave 90 B42 events unlabelled and do not
  state their behaviour on each side [1]; no dev statement was found.
- **Confidence:** Low. A reasonable default, not a guarantee.

# Risks & Caveats

- **Stale pin.** Stubs are 42.20.0 and 41.78.16, while 42.21 stable and
  41.78.21 legacy have shipped [6] [7]. Events or signatures may have changed.
- **Stub text is not engine truth.** Descriptions are written by
  contributors; the generator named in the stub header is a community tool
  [1] [10]. Wrong wording exists, as the `OnKeyPressed` and
  `OnPreDistributionMerge` entries show [1].
- **Blank entries.** About 17 B42 stubs have no description sentence (KB
  script count), so their semantics are undocumented here [1].
- **Counts are KB-derived.** Totals come from the KB's extraction script run
  on the pinned stubs, not from a count published by the stub maintainers.
- **Grouping is editorial.** The purpose groups are this document's taxonomy.

# Verification Steps

1. Open the pinned `library/events.lua` [1] and search for `Events.OnTick = {`
   to see the `Add`/`Remove` shape and the alias line above it.
2. Open the B41 files [2] [3] and confirm the deprecated set lives in
   `Events-deprecated.lua`.
3. Diff the two name lists yourself; expect 31 added, 37 removed, 203 shared.
4. In-game, register logging handlers on `OnGameBoot`, `OnGameStart`,
   `OnNewGame` and `OnCreatePlayer`, then start a new and a loaded save and
   record the order.
5. Re-run the diff against the 42.21 Umbrella tag when one exists [9].

# Open Questions

- What do the roughly 17 undocumented B42 events actually pass and when do
  they fire? Resolve by reading decompiled callers or in-game logging.
- Did 42.21 change any event list or signature? Resolve by diffing a
  42.21 stub set.
- Does a late `AddEvent` make `Events.<Name>` available? See Claim 1.
- Do unlabelled events fire on both client and server? See Claim 3.

# References

**Primary Sources** — pinned Umbrella stubs, official announcements.

- [1] **PZ-Umbrella** — *library/events.lua at Umbrella commit 58204fc47895ba249592519cedecc7cfbaaebd60 (release 42.20.0)*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/58204fc47895ba249592519cedecc7cfbaaebd60/library/events.lua Accessed 2026-10-07.
- [2] **PZ-Umbrella** — *library/Events/Events.lua at Umbrella commit fa2e7e19799740b57902f1cb4e989225c295c05e (release 41.78.16)*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events.lua Accessed 2026-10-07.
- [3] **PZ-Umbrella** — *library/Events/Events-deprecated.lua at commit fa2e7e19799740b57902f1cb4e989225c295c05e*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events-deprecated.lua Accessed 2026-10-07.
- [4] **PZ-Umbrella** — *library/java/zombie/Lua/LuaEventManager.lua at commit 58204fc47895ba249592519cedecc7cfbaaebd60*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/zombie/Lua/LuaEventManager.lua Accessed 2026-10-07.
- [5] **PZ-Umbrella** — *library/Candle/zombie.Lua/LuaEventManager.lua at commit fa2e7e19799740b57902f1cb4e989225c295c05e*. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.Lua/LuaEventManager.lua Accessed 2026-10-07.
- [6] **The Indie Stone** — *Build 42.21 Stable Released* (Steam Community announcement, 2026-09-28). https://steamcommunity.com/ogg/108600/announcements/detail/1844751498231307 — verified via the Steam news mirror [8]. Accessed 2026-10-07.
- [7] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam Community announcement, 2026-08-26). https://steamcommunity.com/ogg/108600/announcements/detail/1842212951296601 — verified via the Steam news mirror [8]. Accessed 2026-10-07.
- [8] **Valve** — *Steam News Web API (ISteamNews), app 108600*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=40&maxlength=0 Accessed 2026-10-07.
- [9] **PZ-Umbrella** — *Umbrella releases (per-game-version tags)*. https://github.com/PZ-Umbrella/Umbrella/releases Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — none used.

**Secondary & Corroborating**

- [10] **demiurgeQuantified** — *PZEventDoc, the generator named in the stub header*. https://github.com/demiurgeQuantified/PZEventDoc Accessed 2026-10-07.

**Community & Creator** — none.

**Further Reading** — see the Further Reading section.

# Further Reading

- Unofficial B42 JavaDocs: https://albion.codeberg.page/PZ-JavaDocs/
- LuaDocs (game-side Lua, including events): https://demiurgequantified.github.io/ProjectZomboidLuaDocs/

# Related Documents

- modders-foundation — toolchain and where the API truth lives.
- modders-lua-api-surface — what the objects passed to callbacks expose.
- modders-mp-networking-porting — client and server command flow.
- modders-porting-b41-to-b42 — wider porting checklist.
- modders-first-mod-tutorial-b42 — first mod using these events.
- modders-item-scripts-distributions — the distribution-merge events.
- modders-modinfo-modid-conventions — mod layout and IDs.
- modders-modoptions-pzapi — options API.
- players-crafting-chains — crafting content mods often hook.
- admins-workshop-mod-wiring — server-side mod deployment.
- meta-style-guide — how documents are written and gated.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
