---
id: modders-mp-networking-porting
title: "Multiplayer Mod Networking: Client/Server Lua, sendClientCommand and Porting for B42 MP"
version: 0.3.0
status: in-review
confidence: Medium
category: Modders
topic: "MP networking porting"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-lua-api-surface, modders-events-callbacks, modders-modoptions-pzapi, modders-item-scripts-distributions, modders-modinfo-modid-conventions, modders-first-mod-tutorial-b42, modders-porting-b41-to-b42, players-crafting-chains, admins-workshop-mod-wiring, meta-style-guide]
tags: [modding, multiplayer, networking, sendClientCommand, sendServerCommand, moddata, lua, b42, umbrella]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-mp-networking-porting |
| Version | 0.3.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16 (stubs), 42.20.0 and 42.21.0 (API stubs plus the 42.20.1 to 42.21 official notes; see Build Applicability) |

# Executive Summary

This document covers how a Project Zomboid mod talks across the client/server
boundary: the `client`, `server` and `shared` Lua folders, the paired
command functions `sendClientCommand` and `sendServerCommand` with their
receiving events `Events.OnClientCommand` and `Events.OnServerCommand`, the
`ModData` synchronisation functions, and the `isClient()` / `isServer()`
guards. Every symbol named here was checked against the pinned Umbrella type
stubs for both builds: 41.78.16 and, for B42, 42.21.0 (previously 42.20.0)
[1] [2] [3] [4] [5] [6] [23] [24].

The central fact is that the command API shape is the same on both builds:
a client sends `(module, command, args)`, the server receives
`(module, command, player, args)`, and the reverse path delivers
`(module, command, args)` to clients [1] [2] [4] [5]. What changed is the
context around it. Online multiplayer first appeared in the Build 42
unstable branch with 42.13.0 on 2025-12-11, together with an official
forum migration guide for modders [9] [10]; Build 42 stable (42.20.0,
2026-07-29) is therefore the first stable build where B42 mods can be
networked [9]. The 42.20.x line also tightened security around mod data and
removed, then restored, the Lua loaders `loadstring` and `loadstream` (removed
in 42.20.4, re-enabled in 42.21) [26] [25]. The 42.20.1 to 42.21 hotfix and
update notes add server-side anti-cheat changes that matter to MP mods:
improved Lua checksum validation (42.20.1), an expanded anti-cheat system and
server-side clothing condition (42.21) [18] [22].

Document confidence is Medium. The signatures and event shapes are High
(pinned stubs) and the Timed Action / item-sync model comes from official
TIS modder documents attached to the 42.13 forum thread [10] [14] [15] (dated
December 2025, so older than the 42.20.0 stubs); the semantics of
`ModData.transmit` are not described in any stub comment or in those
documents. This document is verified against the 42.20.0 stubs only;
The 42.21.0 stubs and the 42.20.1 to 42.21 official notes were re-read for
this revision; unchanged statements are carried forward from 42.20 and were
not re-tested in-game. 41.78.21 legacy (2026-08-26) shipped after the B41
stub pin and no newer B41 stubs exist [5].

# Key Takeaways

- A client calls `sendClientCommand(module, command, args)`; the server's
  `Events.OnClientCommand` handler receives `(module, command, player, args)`.
  The reverse direction is `sendServerCommand` and
  `Events.OnServerCommand`. *(cited)* *(both)*
- The stubs state that `sendClientCommand` does nothing when called on the
  server and `sendServerCommand` does nothing when called on the client.
  *(cited)* *(B42 stub text)*
- Only plain-old-data survives in the `args` table; non-POD elements are
  lost. *(cited)* *(B42 stub text)*
- Convention in the stubs: use your mod's name as the `module` string, and
  every handler must filter on it. *(cited)* *(B42)*
- B42 added `sendClientCommandV` / `sendServerCommandV` (array-valued
  variants) and `isMultiplayer()` to the stub surface; they are absent from
  the B41 stubs. *(cited)* *(B42)*
- Online multiplayer arrived in unstable 42.13.0 (2025-12-11) and is part of
  stable 42.20.0 (2026-07-29). *(cited)* *(B42)*
- In 42.20.4 `loadstring` / `loadstream` were removed (the notes told authors
  of server-sent code to use named handlers invoked by commands); 42.21
  re-enabled them. *(cited)* *(B42)*
- Lua checksum validation for MP anti-cheat was improved in 42.20.1, and 42.21
  expanded the anti-cheat system; the stub for `getModFileWriter` warns that
  writing into a mod's Lua or scripts directories changes the checksum.
  *(cited)* *(B42)*
- 42.21.0 stubs add `Events.RequestMedicalCheck`, `Events.AcceptedMedicalCheck`
  and three foraging events, plus the global `sendAddObjectToMap`; the command
  functions and receiving events are unchanged from 42.20.0. *(cited)* *(B42)*
- Server-authoritative design (client requests, server validates and
  mutates) is community-guide advice, not an engine rule. *(community
  guide, corroborating)*

# Purpose

To give a mod developer one place that answers: which Lua folder runs where,
what the network-facing API actually is on each build, how mod data crosses
the wire, and what the official record says changed for multiplayer mods
between Build 41 and Build 42. It goes deeper on the multiplayer item that
the foundation document only points at [modders-foundation].

# Scope

Covered: the folder split; the four command functions and two events; the
global and object `ModData` surfaces and the related receive events; the
`isClient` / `isServer` / `isMultiplayer` / `isCoopHost` guards; B41 vs B42
differences as far as primary sources state them.

Not covered: packet-level protocol internals; anti-cheat design; server
admin deployment (see admins-workshop-mod-wiring); registry
mechanics beyond the summary in Reference; behaviour after 42.21.0 beyond the Steam and forum release notes cited.

# Definitions

- **Module** — the first argument of a command; a string namespace for a
  mod's commands, conventionally the mod's name [1].
- **Command** — the second argument, a string naming the action [1].
- **POD** — plain old data (numbers, strings, booleans and tables of them);
  the stubs say non-POD elements of an `args` table are lost in transit [1].
- **Listen / co-op host** — a player-hosted game; `isCoopHost()` exists in
  the stub surface of both builds [1] [4].
- **Global mod data** — named tables managed by `ModData`, as opposed to the
  per-object table returned by an object's `getModData()` [3] [6].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | Umbrella stubs at tag 41.78.16 (commit `fa2e7e19799740b57902f1cb4e989225c295c05e`) [4] [5] [6] | 41.78.17 to 41.78.21 shipped later; no newer B41 stub tag exists |
| B42 (stable) | Yes | Umbrella stubs at release 42.21.0 (commit `13d01f9ee58fa48773553920db56d06f0005e7f8`) [23] [24]; earlier check at 42.20.0 (commit `58204fc47895ba249592519cedecc7cfbaaebd60`) [1] [2] [3] | Stable 42.21 was released 2026-09-28 [25]. The upstream 42.20.0 tag was later moved, so this document cites commits, not tags |

Release facts: 42.20.0 stable shipped 2026-07-29, 42.21 stable shipped
2026-09-28, and a 41.78.21 legacy hotfix shipped 2026-08-26, all announced
on Steam [9].

**42.21 re-baseline (2026-10-07).** This revision re-checked the statements
here against the official 42.20.1, 42.20.2, 42.20.3, 42.20.4, 42.21 unstable
and 42.21 stable posts [18] [19] [20] [26] [21] [25], the TIS forum 42.21
patch-note list [22] (abridged to "selected" for its long multiplayer list),
and the 42.21.0 Umbrella `__global.lua` and `events.lua` stubs [23] [24].
Recomputed against the 42.21.0 index, every function and event named in
Reference still exists, and the diff to 42.20.0 adds ten events and four
globals (listed under Release and security record). Everything not mentioned
as changed is carried forward from 42.20 with no contradicting change found;
it was not re-tested in-game. The signatures and descriptions of
`sendClientCommand`, `sendClientCommandV`, `sendServerCommand`,
`sendServerCommandV` and the two receiving events read the same in the
42.21.0 stubs as in the 42.20.0 stubs [23] [24].

**Official 42.13 documents.** The Timed Action, item-sync and registry
material in Reference comes from two TIS documents dated 2025-12-11 [14]
[15], about ten months older than 42.21. Checked against the 42.20.0
stubs and their B41 counterparts: the global sync functions, `emulateAnimEvent`,
`ISBaseTimedAction.getDuration`, `NetTimedAction`, the `register` functions,
`sendClientCommand` and `Events.OnClientCommand` [1] [2] [16] [17]. Guide-only
(not in any stub): the `getProgress` call, the base-class `complete` and
`serverStart` contracts, the supported-type list, and the relogin deletion
rule for client-made items [14]. In the 42.21.0 index the Timed Action
and item-sync symbols named in that check
(`ISBaseTimedAction`, `NetTimedAction`, `InventoryItem`, the sync globals) have
the same members as in 42.20.0 [23]. The 42.20.1 to 42.21 notes contain no
statement that contradicts the guides, but they also do not mention the guide-only
points, so those remain unconfirmed rather than re-verified [18] [22]. Any of
the guide-only statements may have moved since December 2025.

# Reference

## The three Lua folders

The Umbrella stub library mirrors the game's Lua tree and splits it into
`client`, `server` and `shared` folders on both builds [7] [8]. Vanilla
networked systems follow that split: the farming system, for example, has a
server-side class (`SFarmingSystem`) that carries an `OnClientCommand`
function and a client-side class (`CFarmingSystem`) that carries an
`OnServerCommand` function, both present in the B41 and B42 API indexes [7]
[8]. The official inventory document additionally says that a Timed Action file
must live under `media/lua/shared` to be loaded by both client and server
[14]. Other folder-level load semantics (order, host behaviour) are not
stated in any primary source I could open; see Claim 1 and Claim 2.

## Command functions

| Function | Direction | Signature (stub) | Build |
|----------|-----------|------------------|-------|
| `sendClientCommand(module, command, args)` | client to server | the stub comment says it triggers `Events.OnClientCommand` on the server and does nothing on the server [1] | *(both)* [1] [4] |
| `sendClientCommand(player, module, command, args)` | client to server, tied to a local player | the stub says nothing is sent if the player is not local [1] | *(both)* [1] [4] |
| `sendClientCommandV(player, module, command, values)` | client to server | takes an array of values instead of a table [1] | *(B42)* [1] |
| `sendServerCommand(module, command, args)` | server to all clients | triggers `Events.OnServerCommand` on every client; does nothing on a client [1] | *(both)* [1] [4] |
| `sendServerCommand(player, module, command, args)` | server to one client | only that player's client receives it [1] | *(both)* [1] [4] |
| `sendServerCommandV(module, command, values)` | server to all clients | array-valued variant [1] | *(B42)* [1] |

The B41 stubs declare the one-player-argument overload through an overload
annotation on both `sendClientCommand` and `sendServerCommand` [4]. The B42
stubs declare it as a separate documented function [1].

## Receiving events

| Event | Callback parameters | Build |
|-------|---------------------|-------|
| `Events.OnClientCommand` | `module, command, player, args`; marked server-side [2] | *(both)* [2] [5] |
| `Events.OnServerCommand` | `module, command, args`; marked multiplayer, client-side [2] | *(both)* [2] [5] |

In the B42 stubs the `args` parameter is typed as a table or nil, with the
documentation stating that an empty table arrives as nil [2]. The B41 stubs
type `args` as a plain table with no nil note [5]. The B42 comment is
therefore the only primary statement about empty arguments, and handlers
should be written to tolerate nil on both builds (see Practical Guidance).

## Guards

`isClient()`, `isServer()`, `isCoopHost()`, `isAdmin()` and
`getOnlinePlayers()` exist in the stub surface of both builds, and
`isMultiplayer()` exists in the B42 stubs only (confirmed again in the 42.21.0
stubs) [1] [4] [23]. The stubs give no
descriptive comment for these guards, so their exact truth table on a
host, dedicated server and single-player game is not primary-sourced here
(Claim 2).

## Mod data

`ModData` exposes `add`, `create`, `exists`, `get`, `getOrCreate`,
`getTableNames`, `remove`, `request` and `transmit` in both builds' stubs
[3] [6]. Related events: `Events.OnInitGlobalModData(newGame)`, described as
the earliest event after sandbox options load [2] [5];
`Events.OnReceiveGlobalModData(key, data)`, fired when a global table is
received, with `data` equal to false when no table existed for the key [2]
[5]; `Events.SendCustomModData`, fired on the server when a client requests
server mod data [2] [5]; and `Events.onLoadModDataFromServer(square)`, fired
when a square's mod data is sent to or received by clients [2] [5].

Object-level synchronisation methods in the index of both builds include
`IsoObject.transmitModData` and `IsoGridSquare.transmitModdata` (note the
lower-case d in the grid-square name) [1] [4]. The stubs do not describe the
direction or timing of `ModData.transmit` or `ModData.request`; the pairing
of `request` with `OnReceiveGlobalModData` is an inference from the event
comment, not a documented rule.

## Server-authoritative items and Timed Actions (official 42.13 documents)

Two official documents were attached to the TIS forum thread that the 42.13.0
release notes point modders at: a "Migration Guide" and an "API for Inventory
Items" document, version 1.0, posted with the thread on 2025-12-11 [10] [14]
[15]. Their content predates the 42.20.0 stubs, so the final paragraph of this
subsection states which claims the stubs corroborate.

**Design rule.** In multiplayer all inventory-item processing moves to the
server. A modified client can still conjure an item into its own inventory,
but that item cannot be interacted with and is deleted from the inventory
after the player logs in again; items have to be created server-side and
then transferred to the client, so the item exists in both inventories [14].
The guide names two legitimate routes: a Timed Action, or a command sent
with `sendClientCommand` whose server handler checks for cheating, changes
the item, and sends the matching sync packets. It suggests the command route
for changes that do not come from player input, such as admin powers [14].

**Adapting an existing Timed Action.** The document lists five steps: move
the action's file from `media/lua/client` to `media/lua/shared` so both sides
load it; make every constructor argument match a same-named field with the
same value; add a duration function; split `perform` in two; and call the
sync functions from the new half [14].

**Constructor argument rule.** The client ships the action to the server by
sending the argument list of its `new` function, and the server rebuilds the
Lua object by looking up each argument name as a field on the object. Names
must therefore equal field names, and the incoming values must be stored
unchanged: if a constructor stores a scaled copy of an argument under the
same name, the rebuilt object is scaled a second time [14]. The base
constructor stores its character argument in a field called `character`, so
a subclass argument for the player has to use that name [14]. The execution
time must not be passed as an argument, because that let a cheater shorten
actions; the server calls the duration function instead [14].

**Supported argument types.** The guide enumerates 27 accepted types:
`BaseVehicle`, `BloodBodyPartType`, `BodyPart`, Boolean, `CraftRecipe`,
Double, `EvolvedRecipe`, `FluidContainer`, Integer, `InventoryItem`,
`IsoAnimal`, `IsoDeadBody`, `IsoGridSquare`, IsoHutch.NestBox, `IsoObject`,
`IsoPlayer`, `ItemContainer`, `KahluaTableImpl`, MultiStageBuilding.Stage,
`PZNetKahluaTableImpl`, `Recipe`, `Resource`, SpriteConfigManager.ObjectInfo,
String, `VehiclePart`, `VehicleWindow` and null; table serialisation lives in
`PZNetKahluaTableImpl` [14]. World objects are sent as lookup information and
resolved by the server, so an object created only on the client cannot be an
argument [14].

**Duration units.** `getDuration` returns the action length in cycles of
0.02 seconds, so seconds are divided by 0.02 (one second is 50). The guide
recommends 1 for an instantaneous action, -1 for an endless one, and 1
whenever the instant-timed-action cheat is on [14]. The client may reuse the
same function inside `new` to fill its own time field [14].

**perform versus complete.** Both run when the action finishes. The client
runs only `perform`, the server runs only `complete`, and single-player runs
`perform` first and `complete` second [14]. `perform` holds sound, animation
and UI work and must not touch items or objects; `complete` holds only item
and object changes and must not call anything unavailable on the server [14].
The worked example returns true from `complete` [14].

**Long-running actions.** An action that does work while running (the guide
names pouring liquids and reading) implements `serverStart`, which runs
server-side when the action starts and calls `emulateAnimEvent` to set up an
animation-event emulator. That call takes the action's network object (always
`self.netAction`), a period in milliseconds, an event name delivered to the
action's `animEvent` function, and a stock parameter [14]. On the server,
`self.netAction:forceComplete()` ends such an action, and a `getProgress`
call on the same object reports progress inside `animEvent`; single-player
uses `self:forceComplete()` instead [14]. In the guide's tree-chopping
example the same `animEvent` branches on `isClient()`: the client plays hit
effects only, while single-player and the server compute the damage [14].

**Command arguments.** `sendClientCommand` takes an optional `IsoPlayer`,
then the module string, the command string and an args table. In
single-player the server-side handler is still invoked. The server's
`OnClientCommand` handler then receives module, command, player, args in
that order [14]. The vehicle-key example registers one handler, filters on the
module string, dispatches through a table keyed by command name, and gates the
action on a permission check before creating and sending the item [14].

**Sync functions.** After changing things inside `complete`, the guide
lists the calls that push changes to clients [14]:

| Function | What it synchronises |
|----------|----------------------|
| `sendAddItemToContainer` / `sendRemoveItemFromContainer` | an item added to or removed from a container [14] |
| `syncItemFields` | a fixed set of item variables, including condition, uses, ammo count, wetness, weight, pages read, attachment slot, fluid container and mod data [14] |
| `syncItemModData` | an item's mod data [14] |
| `syncHandWeaponFields` | a fixed set of weapon variables, including chamber, magazine and jam state, ranges, damage and timing values, attachments and mod data [14] |
| `sendItemStats` | food and fluid statistics such as uses, heat, cooking and burn times, nutrition and mood values, poison, fluid amount, cooked and burnt flags and name [14] |
| `transmitCompleteItemToClients` | a new world object on the map [14] |
| `transmitRemoveItemFromSquare` | a removed world object [14] |
| `sync` | a changed world object [14] |
| `transmitUpdatedSpriteToClients` | a changed sprite [14] |

The full per-function field lists are in the source document [14].

**Corroboration against the pinned stubs.** The B42 stubs declare the global
functions `sendAddItemToContainer`, `sendRemoveItemFromContainer`,
`syncItemFields`, `syncItemModData`, `syncHandWeaponFields`, `sendItemStats`
and `emulateAnimEvent`, and the B41 stubs declare none of them [1] [4].
Also in the B42 index are `ISBaseTimedAction.getDuration` *(B42)*,
`NetTimedAction.animEvent` *(B42)*, `NetTimedAction.forceComplete` *(B42)*,
`InventoryItem.UseAndSync` *(B42)* and `IsoObject.sync` *(B42)*, none of
which appear in the B41 index [16] [17].
`IsoObject.transmitCompleteItemToClients`,
`IsoGridSquare.transmitRemoveItemFromSquare` and
`IsoGameCharacter.isTimedActionInstant` exist in both builds' indexes [16]
[17]. Many B42 vanilla Lua classes in the stub tree define `complete`,
`getDuration` or `serverStart`, for example the chop-tree, place-trap and
add-fuel actions [16]. Guide-only, with no stub counterpart found: the
`getProgress` call on the network action, `complete` and `serverStart` as
base-class contracts, the 27-type list, and the rule that client-made items
are deleted after relogin.

## Registries and script changes (migration guide)

The "Migration Guide" says that from 42.13 several identifier kinds are
added through Lua rather than by script text alone: character trait,
character profession, item tag, brochure, flier, item body location, item
type, moodle type, weapon category, newspaper and ammo type [15]. Mods
register them in a file named exactly `registries.lua` in the `media` folder,
which is loaded before scripts and before all other Lua [15]. Its examples
use namespaced ids written as `modid:name` [15]. The B42 index shows
`register` on `CharacterTrait.register`, `CharacterProfession.register`,
`ItemTag.register`, `ItemType.register`, `MoodleType.register`,
`ItemBodyLocation.register` and `AmmoType.register` *(B42)*; the B41 index
lacks most of those classes, and `ItemType` and `MoodleType` there have no
`register` [16] [17]. The guide adds that the item script field `DisplayName`
was removed (names come from the translation keyed by module and item id),
that `Type` was renamed `ItemType` and needs its registry, and that tags need
the `ItemTag` registry; it also says some Lua API was modified and advises
checking decompiled Java when something broke [15].

## Release and security record relevant to MP mods

Unstable 42.13.0 (2025-12-11) was the first Build 42 version with online
multiplayer. The release note directs modders to a linked guide on updating
mods for 42.13.0 and beyond and on making them multiplayer compatible [9]
[11]. The same-day announcement said much had changed under the hood, asked
for patience while mods were updated, and advised disabling all mods
including client ones for the stress-test period [9].

A spring 2026 preview post said the team had added backend support for
some multiplayer mods affected by recent security updates, along with new
exposed functions [9]. The 42.20.0 stable notes list fixes for exploits
including arbitrary item spawning via mod data [9] [12]. In 42.20.4, the
`loadstring` and `loadstream` Lua methods were removed as a security fix,
and the note told mod authors who executed server-sent code to replace that
with named handlers invoked by commands [26]. The 42.21 stable post states
those two methods were re-enabled after further investigation of the security
issue, and the 42.21 forum notes list the re-enable under "big ticket items"
[25] [22]. A stub absence is not evidence either way here: the 42.21.0 index
no longer lists a global `loadstream` although TIS states the methods were
re-enabled, so stubs can lag the game on this point [23] [22].

**42.20.1 to 42.21 multiplayer changes.** The 42.20.1 hotfix lists improved Lua
checksum validation for multiplayer anti-cheat, a fix that stopped broken B41
worlds being hosted on B42 servers, and a fix for a missing menu when players
switched from B41 to B42 [18]. The 42.20.3 hotfix lists improved server player
limit handling, including support for up to 254 players and administrator
access when a server is full [20]. The 42.21 notes list an expanded anti-cheat
system (new cheats guarded against, safehouse exploits remedied), clothing
condition now handled server-side, and a notification for players who try to
connect to an MP server running a different game version [21] [22]. The
42.21 forum list is abridged here to the "selected" multiplayer items it
publishes, so it is not a complete record [22]. None of these notes describes a
change to the command functions or their events; for mod authors the stated
consequence is limited to the checksum and anti-cheat items above, and the
`getModFileWriter` stub warns that writing into a mod's Lua or scripts
directories changes the checksum [18] [22] [23].

**Mod file writes and translations.** The 42.20.1 notes state that mods can
now write `.json` files, and the 42.21.0 stubs list `json` among the allowed
extensions of `getFileWriter` (Lua cache root) and `getModFileWriter` (a mod's
common folder), alongside `ini`, `cfg`, `txt` and `log` [18] [23]. The 42.20.1
and 42.20.2 notes also say mod translation strings should use `%%` to show a
literal `%`; 42.20.2 adds that a temporary workaround accepts both ways and
"will be removed in a future unstable update" [18] [19]. The 42.21 notes add
an updated localization system that enables more translatable strings [21] [22].

**New in the 42.21.0 stubs.** Diffing the archived 42.20.0 index against the
42.21.0 index (classes 4266 to 4124, events 234 to 244, globals 947 to 930)
shows ten added events and no removed events [23] [24]. Those relevant to
multiplayer are `Events.RequestMedicalCheck` and `Events.AcceptedMedicalCheck`
(both marked multiplayer and client, each with callback parameters
`target, requester`), and three foraging events: `Events.OnForagePool`
(client; `player, zoneId, icons`, fired when a pool is received from the
server), `Events.OnForageRequestZone` (server; `player, focus`) and
`Events.OnForageSpot` (server; `player, iconID`) [24]. The global
`sendAddObjectToMap(square, sprite)` is new in the 42.21.0 stubs; the stub gives
it no description, so its behaviour is not stated here [23].

# B41 vs B42 Delta

| Aspect | B41 (41.78.16 stubs) | B42 (42.21.0 stubs; 42.20.0 identical for the command rows) |
|--------|----------------------|---------------------|
| Online multiplayer | Present in the B41 lifecycle (command events and `isClient`/`isServer` exist) [4] [5] | Returned in unstable 42.13.0 (2025-12-11), in stable from 42.20.0; 42.20.3 supports up to 254 players with administrator access when full [9] [20] |
| Command core | `sendClientCommand`, `sendServerCommand` with a one-player overload; `Events.OnClientCommand`, `Events.OnServerCommand` [4] [5] | Same four, with documented overloads, unchanged between 42.20.0 and 42.21.0 [1] [2] [23] [24] |
| Array-valued variants | Not in stubs [4] | `sendClientCommandV`, `sendServerCommandV` [1] |
| Empty args | Typed as plain table [5] | Typed table or nil; empty table arrives as nil [2] |
| `isMultiplayer()` | Not in stubs [4] | In stubs [1] |
| Extra event | Not in stubs [5] | `Events.OnServerCustomizationDataReceived` (no description in the stub) [2] *(B42)* |
| Security posture | Security-only hotfixes on legacy (see Steam record) [9] | Mod data item-spawn exploit fixed in 42.20.0 [9]; improved Lua checksum validation in 42.20.1 [18]; loaders removed in 42.20.4 and re-enabled in 42.21 [26] [25]; expanded anti-cheat in 42.21 [21] [22] |
| Cross-version connect | Not covered by any source read | 42.20.1 stops broken B41 worlds being hosted on B42 servers [18]; 42.21 adds a notification when connecting to a server with a different game version [21] |
| Medical-check and foraging events | Not in stubs [5] | `Events.RequestMedicalCheck`, `Events.AcceptedMedicalCheck`, `Events.OnForagePool`, `Events.OnForageRequestZone`, `Events.OnForageSpot` in the 42.21.0 stubs, not in 42.20.0 [24] *(B42)* |
| Modder guidance | None cited | Official forum thread with a Migration Guide and an inventory-items API document (2025-12-11) [9] [10] [14] [15]; server-authoritative items and Timed Action split, see Reference |

The practical reading of the table is that the transport functions are
stable across the break; what a B41 mod must rework is the content of its
handlers (the game objects reachable from them changed in Build 42, which
the foundation and porting documents cover) and its assumptions about who
holds authority [9].

# Practical Guidance

- **Namespace your commands.** Use your mod id as `module`, and begin every
  handler with a module filter, as the stub comments recommend [1] [2].
- **Tolerate nil args on both builds.** Write `args = args or {}` first,
  because B42 may deliver nil for an empty table [2].
- **Keep payloads plain.** Send numbers, strings, booleans and nested tables
  of those; do not send Java objects or functions [1].
- **Client requests, server decides.** Put the receiving handler in
  `server/`, re-check the sender and the request, then change state there;
  send the result back with `sendServerCommand` [1] [2] [13].
- **Port item changes into Timed Actions.** Name constructor arguments after
  the fields they populate, store them unchanged, return the duration from
  `getDuration`, keep sound and UI in `perform`, and put item changes plus
  their sync call in `complete` [14].
- **Never create items on the client.** Create them on the server and sync
  them, because client-made items are not honoured [14].
- **Replace server-sent code with named commands.** The 42.20.4 notice asked
  for exactly this; even though 42.21 re-enabled the loaders, a fixed set of
  handlers triggered by commands does not depend on that decision [26] [25].
- **Write `%%` for a literal percent in translations.** The 42.20.2 notes say
  the tolerant workaround will be removed in a future unstable update [19].
- **Do not edit your mod's own Lua or scripts at runtime.** The
  `getModFileWriter` stub notes this changes the checksum, and checksum
  validation for MP anti-cheat was improved in 42.20.1 [23] [18].
- **Test on a dedicated server, not only in single-player or a host game.**
  Both of the receiving events are labelled for server or client contexts in
  the stubs, so a single-player run cannot prove them [2].

A minimal skeleton that uses only symbols present in both builds:

```lua
-- server/MyMod_Commands.lua
local MODULE = "MyMod"

local function onClientCommand(module, command, player, args)
    if module ~= MODULE then return end
    args = args or {}
    if command == "requestPing" then
        sendServerCommand(player, MODULE, "pong", { n = args.n })
    end
end

Events.OnClientCommand.Add(onClientCommand)
```

```lua
-- client/MyMod_Replies.lua
local MODULE = "MyMod"

local function onServerCommand(module, command, args)
    if module ~= MODULE then return end
    args = args or {}
    if command == "pong" then
        print("pong", args.n)
    end
end

Events.OnServerCommand.Add(onServerCommand)
```

# Common Pitfalls & Troubleshooting

- **Handler never fires in a solo test.** The stubs mark `Events.OnClientCommand`
  as a server event and `Events.OnServerCommand` as a multiplayer client event
  [2]; test in a hosted or dedicated session.
- **Command seems to vanish.** `sendClientCommand` does nothing on the server
  and `sendServerCommand` does nothing on the client, so a call from the wrong
  side is silently a no-op [1].
- **Data arrives missing fields.** Non-POD table elements are dropped in
  transit [1].
- **Index error on empty args.** B42 delivers nil for an empty table [2].
- **Cross-mod collisions.** Without a module filter every command reaches
  every handler registered on the event [2].
- **Server-supplied code stopped working in 42.20.4.** The loader functions
  were removed in 42.20.4 and restored in 42.21 [26] [25].
- **Literal percent signs vanish or double in mod translations.** Use `%%`;
  the temporary both-ways handling is slated for removal [19].
- **Mod data seems stale after joining.** `Events.OnReceiveGlobalModData`
  reports `false` when no table exists for the requested key; check for it
  [2].
- **Players cannot join after a version mismatch.** 42.21 added a
  notification for connecting to a server with a different game version, and
  42.20.1 blocked broken B41 worlds from being hosted on B42 servers [21] [18].
- **Mod broke when MP landed (B42).** Official notes say much changed under
  the hood in 42.13, and early MP testing advised disabling mods [9].

# Community Notes & Unverified Claims

## Claim 1 — Client Lua also runs on the listen-server host as both client and server

- **Claim:** A community modding guide (gotmayonase, pz-modding-guide,
  multiplayer.md) states that on a listen server the host machine runs both
  client and server Lua, so client files execute twice for the host, and
  recommends file placement over `isClient()` guards.
- **Why unverified:** No primary source (patch note, stub comment or dev
  post) I could open states the host's load behaviour; the guide targets
  B42.15 and later and was last pushed 2026-04-05 [13].
- **Confidence:** Medium. It matches common modder experience but is a single
  community source.

## Claim 2 — Exact truth table of isClient, isServer and isMultiplayer

- **Claim:** The same community guide says `isClient()` is true on a game
  client including the host's client, `isServer()` is true on dedicated and
  host servers, and `isMultiplayer()` is true when connected to or hosting a
  session [13].
- **Why unverified:** The Umbrella stubs list the functions with no
  description [1] [4], and no official statement was found.
- **Confidence:** Medium. Plausible and consistent with the function names,
  but not primary-sourced.

## Claim 3 — ModData.transmit pushes global mod data between server and clients, and request asks the server for a table

- **Claim:** Modders commonly describe `ModData.transmit(tag)` as sending a
  global table to the other side and `ModData.request(tag)` as asking the
  server for a table, answered through `Events.OnReceiveGlobalModData`.
- **Why unverified:** The stubs name the functions and the event but do not
  describe direction or timing [3] [6] [2]; no dev post found.
- **Confidence:** Low. Inferred from names and event comments, with no
  primary behavioural statement, and 42.20.0 fixed a mod-data exploit that may
  have altered server-side acceptance rules, and the expanded 42.21 anti-cheat could
  have too [9] [22].

## Claim 4 — Mods that only use script and registry changes need no further MP-specific work

- **Claim:** Some modders say that a mod limited to item scripts and
  registries is multiplayer-safe once it follows the registry rules.
- **Why unverified:** The Migration Guide describes registry and script
  changes but makes no multiplayer-safety statement for them [15]; the
  inventory document covers only Lua-driven item changes [14].
- **Confidence:** Low. Plausible but not stated by any primary source.

# Risks & Caveats

- B42 stubs re-checked at 42.21.0; the B41 stub pin is still 41.78.16, and
  41.78.21 legacy (2026-08-26) has no newer stub tag [5] [26].
- The 42.21 forum notes publish only "selected" multiplayer items [22]; the
  full list was not available, so further MP changes may exist.
- Umbrella stubs can lag the game: `loadstream` is absent from the 42.21.0
  index although TIS says it was re-enabled [23] [22].
- The stubs are community-generated type annotations, not engine
  documentation; comments such as the "does nothing if called on the server"
  statements are the stub authors' descriptions [1].
- The official 42.13 documents date from December 2025; their guide-only
  statements were not re-verified on 42.20.0 or 42.21; only the symbol-level
  check against the 42.21.0 index was repeated [14] [15] [23]. The
  attachments need a forum sign-in, so readers cannot open them anonymously.
- The loader removal and restoration (42.20.4, 42.21) shows the security
  posture of the mod API is still moving [9].
- Single community source for execution-context behaviour (Claims 1 and 2).

# Verification Steps

1. Open the Umbrella B42 commit 13d01f9ee58fa48773553920db56d06f0005e7f8 (release 42.21.0) and read `library/java/__global.lua`
   around `sendClientCommand` / `sendServerCommand`, and
   `library/events.lua` for `OnClientCommand` / `OnServerCommand` [23] [24]
   (the 42.20.0 files are [1] [2]).
2. Repeat on the B41 tag 41.78.16 in `library/Candle/__global.lua` and
   `library/Events/Events.lua` [4] [5].
3. Run `python scripts/check_api_exists.py docs/modders/modders-mp-networking-porting.md`.
4. Start a dedicated server with the skeleton mod and confirm the `pong`
   round trip; then run it host-mode and observe how often each file executes
   to settle Claims 1 and 2.
5. Pull the Steam news feed for app 108600 and read the 42.13.0, 42.20.1, 42.20.4 and
   42.21 posts [9] [18] [26] [25], and the forum patch notes [22].
6. Open the forum thread signed in, download both PDF attachments and compare
   them with the Reference subsections [10] [14] [15].

# Open Questions

- Has the Timed Action contract (`getProgress`, base `complete` and
  `serverStart`, supported types) changed between 42.13 and 42.21? The 42.21.0
  index shows no member change on the related symbols, but the guide-only points
  have no stub counterpart; resolve by decompiling the game's Java and diffing
  against [14].
- What are the direction and timing semantics of `ModData.transmit` and
  `ModData.request` on 42.20+, and did the 42.20.0 mod-data exploit fix change
  what a server accepts from clients? [9]
- What do `sendAddObjectToMap` and the medical-check events do in practice?
  The 42.21.0 stubs give a signature or one-line trigger and nothing more [23] [24].
- What exactly does the 42.20.1 and 42.21 anti-cheat reject from a mod's
  point of view? The notes name no mod-facing rule [18] [22].
- Is there an official statement of host (co-op) Lua execution behaviour?

# References

**Primary Sources**

- [1] **PZ-Umbrella** — `library/java/__global.lua` at commit 58204fc47895ba249592519cedecc7cfbaaebd60 (tag 42.20.0). https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/__global.lua Accessed 2026-10-07.
- [2] **PZ-Umbrella** — `library/events.lua` at commit 58204fc47895ba249592519cedecc7cfbaaebd60 (tag 42.20.0). https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/events.lua Accessed 2026-10-07.
- [3] **PZ-Umbrella** — `library/java/zombie/world/moddata/ModData.lua` at commit 58204fc47895ba249592519cedecc7cfbaaebd60. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/zombie/world/moddata/ModData.lua Accessed 2026-10-07.
- [4] **PZ-Umbrella** — `library/Candle/__global.lua` at commit fa2e7e19799740b57902f1cb4e989225c295c05e (tag 41.78.16). https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/__global.lua Accessed 2026-10-07.
- [5] **PZ-Umbrella** — `library/Events/Events.lua` at commit fa2e7e19799740b57902f1cb4e989225c295c05e (tag 41.78.16). https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events.lua Accessed 2026-10-07.
- [6] **PZ-Umbrella** — `library/Candle/zombie.world.moddata/ModData.lua` at commit fa2e7e19799740b57902f1cb4e989225c295c05e. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.world.moddata/ModData.lua Accessed 2026-10-07.
- [7] **PZ-Umbrella** — `library/lua` folder (client, server, shared) at commit 58204fc47895ba249592519cedecc7cfbaaebd60. https://github.com/PZ-Umbrella/Umbrella/tree/58204fc47895ba249592519cedecc7cfbaaebd60/library/lua Accessed 2026-10-07.
- [8] **PZ-Umbrella** — `library/Lua` folder (client, server, shared) at commit fa2e7e19799740b57902f1cb4e989225c295c05e. https://github.com/PZ-Umbrella/Umbrella/tree/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Lua Accessed 2026-10-07.
- [9] **The Indie Stone / Valve** — Steam News API mirror for app 108600, covering these official announcements: "Build 42.13.0 UNSTABLE Multiplayer Released" and "Unstable 42 MP Released" (2025-12-11), "SPRING IS HERE" (2026-05-08), "Build 42.20.0 Stable Released" (2026-07-29), "42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released" (2026-08-26) and "Build 42.21 Stable Released" (2026-09-28). https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0 Accessed 2026-10-07.
- [10] **The Indie Stone Forums** — thread *Modding Migration Guide (42.13)*, first post by moderator nasKo, 2025-12-11, linked from the official 42.13.0 Steam posts [9]. https://theindiestone.com/forums/index.php?/topic/88499-modding-migration-guide-4213/ Accessed 2026-10-07 (host bot-blocks automated checkers; attachments need a forum sign-in).

- [14] **The Indie Stone** — *Project Zomboid: API for Inventory Items*, document version 1.0, PDF attached to the forum thread [10] (text extracted from the signed-in download, retrieved 2026-10-07). Copyright The Indie Stone; facts only, original prose here.
- [15] **The Indie Stone** — *Migration Guide*, PDF attached to the forum thread [10] (text extracted from the signed-in download, retrieved 2026-10-07). Copyright The Indie Stone; facts only, original prose here.
- [16] **PZ-Umbrella** — `library/java` folder and `library/lua` folder at commit 58204fc47895ba249592519cedecc7cfbaaebd60 (42.20.0 stubs, class and member index). https://github.com/PZ-Umbrella/Umbrella/tree/58204fc47895ba249592519cedecc7cfbaaebd60/library/java Accessed 2026-10-07.
- [17] **PZ-Umbrella** — `library/Candle` folder at commit fa2e7e19799740b57902f1cb4e989225c295c05e (41.78.16 stubs). https://github.com/PZ-Umbrella/Umbrella/tree/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle Accessed 2026-10-07.
- [18] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766 Accessed 2026-10-07.
- [19] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441 Accessed 2026-10-07.
- [20] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895 Accessed 2026-10-07.
- [21] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925 Accessed 2026-10-07.
- [22] **The Indie Stone Forums** — *42.21 Patch Notes*, topic 101693, first post by Rockjaw, 2026-09-23 (list abridged to "selected" items for its long MP and other fix lists). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 (host bot-blocks automated checkers).
- [23] **PZ-Umbrella** — `library/java/__global.lua` at commit 13d01f9ee58fa48773553920db56d06f0005e7f8 (release 42.21.0). https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/__global.lua Accessed 2026-10-07.
- [24] **PZ-Umbrella** — `library/events.lua` at commit 13d01f9ee58fa48773553920db56d06f0005e7f8 (release 42.21.0). https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/events.lua Accessed 2026-10-07.
- [25] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07.
- [26] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601 Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)**

- [11] **PZwiki** — *Build 42.13.0* (revision 1435679). https://pzwiki.net/wiki/Build_42.13.0 Accessed 2026-10-07. Fact-only source.
- [12] **PZwiki** — *Build 42.20.0* (revision 1443641). https://pzwiki.net/wiki/Build_42.20.0 Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating**

- [13] **gotmayonase** — *pz-modding-guide: Multiplayer Architecture* (multiplayer.md; repository last pushed 2026-04-05; targets B42.15+). https://github.com/gotmayonase/pz-modding-guide/blob/main/multiplayer.md Accessed 2026-10-07. Community guide, corroborate-only.

**Community & Creator** — none beyond [13].

**Further Reading** — see below.

# Further Reading

- Umbrella repository: https://github.com/PZ-Umbrella/Umbrella
- Official Discord (the #mod_portal channel is named in the official notes): https://discord.gg/theindiestone

# Related Documents

- modders-foundation — ecosystem, toolchain and where API truth lives.
- modders-lua-api-surface — the wider Lua API surface.
- modders-events-callbacks — the event system and callbacks.
- modders-modoptions-pzapi — client-side options (not shared state).
- modders-item-scripts-distributions — item and distribution scripts.
- modders-modinfo-modid-conventions — Mod ID conventions used as module names.
- modders-first-mod-tutorial-b42 — a first B42 mod.
- modders-porting-b41-to-b42 — the general porting guide.
- players-crafting-chains — player-facing crafting chains.
- admins-workshop-mod-wiring — server-side mod deployment.
- meta-style-guide — how documents are written and gated.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (virtual agent) | Added the official 42.13 TIS documents (Timed Action split, item sync, registries); resolved the unread-guide claim; Build Applicability notes stub-checked vs guide-only statements. | — |
| 0.3.0 | 2026-10-07 | KB Pipeline (virtual agent) | Re-baselined 42.20 to 42.21: added the 42.20.1 to 42.21 MP notes (Lua checksum validation, 254-player limit, expanded anti-cheat, server-side clothing condition, version-mismatch notification, B41 worlds blocked), `%%` translation rule, `.json` writes, loader removal and re-enable chronology, and the 42.21.0 stub diff (medical-check and foraging events, `sendAddObjectToMap`). Sources: Steam posts 42.20.1 to 42.21 [18] [19] [20] [26] [21] [25], forum notes [22], Umbrella 42.21.0 [23] [24]. | — |
