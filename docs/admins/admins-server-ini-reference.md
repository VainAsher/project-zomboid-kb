---
id: admins-server-ini-reference
title: "server.ini Reference: The Settings That Matter, by Area"
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
related: [admins-foundation, admins-sandboxvars-reference, meta-style-guide, modders-foundation]
tags: [server-ini, ports, rcon, mods, backups, anti-cheat, voip, pvp, whitelist, discord, dedicated-server]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-server-ini-reference |
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

This is the Admins-track per-key reference for `<servername>.ini` — the file that governs a Project Zomboid dedicated server's network identity, player admission, PVP rules, mod wiring, save/backup cadence, anti-cheat posture, VOIP, and Discord bridge. Where the parent overview (`admins-foundation`) maps *which file does what*, this document goes one level down: every key covered here appears as a table row with its type, default, documented value range, and the build(s) whose reference revision documents it. The organizing principle is functional area, so an operator can open the section that matches the change they want to make and copy the keys out.

The two anchor sources are pinned wiki revisions: the Build 42-era "Server settings" page (revision 1443167, page versioned against 42.20.0) [2] and the Build 41-era revision of the same page (revision 157571, page versioned against 41.78.16, retrieved through an Internet Archive capture) [3]. Comparing the two yields a concrete B41→B42 delta: one key renamed, a loot-respawn trio relocated out of the `.ini` into SandboxVars, several defaults shifted (player cap, ping limit, VOIP falloff), and whole families — `AntiCheat*`, `Backups*`, chat moderation, login queueing — that only the B42-era revision documents.

Document-level confidence is **Medium**: the value tables rest on a fact-only community wiki (pinned revisions, both builds), not on game files or official patch notes, and the B41-era revision self-describes as incomplete. Where the two revisions disagree, or where a key's semantics are simply not documented, this reference says so instead of guessing; genuinely unverifiable community lore (such as the numeric anti-cheat mode mapping) is quarantined at the bottom.

# Key Takeaways

- The `.ini` uses flat `Key=Value` lines; every key in this document is tabulated with type, default, range and build tag, sourced from pinned wiki revisions for 42.20.0 and 41.78.16 *(cited)* *(both)*
- Game traffic needs `DefaultPort=16261` reachable over UDP, plus `UDPPort=16262` as documented at B42; RCON listens separately on `RCONPort=27015` behind `RCONPassword` *(cited)* *(both)*
- Admission control is the trio `Open`, `Password`, and the whitelist behaviours (`DropOffWhiteListAfterDeath`, `MaxAccountsPerUser`, B41's `AutoCreateUserInWhiteList`) — an internet-facing server should not run defaults *(cited)* *(both)*
- Mods are wired as the paired lists `WorkshopItems=` (semicolon-separated Workshop IDs) and `Mods=` (loading IDs from each mod's `info.txt`); the pinned B42 revision shows no separator example for `Mods=` *(cited)* *(both)*
- Backups are a B42-documented key family: `BackupsCount` (1–300, default 5), `BackupsOnStart`, `BackupsOnVersionChange`, `BackupsPeriod`; autosave cadence is `SaveWorldEveryMinutes` on both builds *(cited)* *(B42)*
- The ten-key `AntiCheat*` family appears only in the B42-era revision, alongside 42.20's reworked, re-enabled server-side anti-cheat; the meaning of its numeric values is **not** documented in the pinned revision and is quarantined below *(cited / community, unverified)* *(B42)*
- The revision-to-revision delta shows one rename (`DisableSafehouseWhenPlayerConnected` → `DisableSafehouseWhenOwnerConnected`), a loot-respawn trio moved to SandboxVars, and default shifts including `MaxPlayers` 16→32 and `VoiceMaxDistance` 300→100 *(cited)* *(both)*
- A key absent from the B41-era revision is not proven absent from the B41 game — that page self-describes as incomplete; treat B42-only tags here as documentation facts, not changelog facts *(cited)* *(B41)*

# Purpose

This document answers the working admin's question: "which `.ini` key controls X, what may I set it to, and does it exist on my build?" It is the settings companion to the Admins-track foundation: the foundation explains where `servertest.ini` lives, how it is generated, and how edits are applied; this reference enumerates the keys themselves, grouped the way operators actually change them — network, players, PVP, mods, saves, anti-cheat, performance, voice, chat/Discord, logging. It also exists to feed the knowledge base's deterministic server-setting QA gate: the key tables below are the parseable schema surface for that gate.

# Scope

Covered: `<servername>.ini` keys in the functional areas above, as documented by the pinned B42-era revision (1443167, versioned 42.20.0) [2] and the B41-era revision (157571, versioned 41.78.16) [3] of the wiki's Server settings page, with build tags wherever the two revisions differ. Startup-parameter overrides that interact with these keys (`-port`, `-udpport`, `-servername`) are noted where relevant [5].

Not covered: `SandboxVars.lua` gameplay settings (the sibling document `admins-sandboxvars-reference` owns those), spawnpoint/spawnregion Lua files, install/branch procedure, RAM sizing, and admin/RCON command catalogues — see `admins-foundation` for the map. This document does not claim exhaustiveness over every `.ini` key ever shipped: it covers the listed areas thoroughly and tags each key's documentation status honestly. Unstable-branch behaviour after 42.20 is out of scope.

# Definitions

- **Key** — one `Name=Value` line in `<servername>.ini`; names are case-sensitive strings with no spaces around `=` in the generated file [2].
- **Documented default** — the value the pinned wiki revision states as `Default:`; for B41-only keys the revision prints a value without distinguishing "shown" from "default", and the tables below note this [3].
- **Soft reset** — a server wipe that forces clients to make new characters, tracked by the paired identity keys `ResetID` and `ServerPlayerID` [2].
- **Loading ID** — a mod's internal identifier from its `info.txt`, used in `Mods=`; distinct from the numeric Steam Workshop ID used in `WorkshopItems=` [2].
- **Safety system** — the per-player PVP opt-in mechanism: with `SafetySystem=true`, a player can hurt another only when at least one of the two has PVP mode switched on [2].
- **RCON** — the remote console interface on `RCONPort`/`RCONPassword`; compatible with generic Source-RCON tooling [2] [6].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Key facts from wiki revision 157571, page versioned 41.78.16 [3]; page self-flags as incomplete |
| B42 (stable) | Yes | 42.20, 42.21 | Key facts from wiki revision 1443167, page versioned 42.20.0 [2]; 42.20 stable since 2026-07-29 [1]; 42.21 stable since 2026-09-28 [11], with the 42.20.1-42.21 patch notes reviewed [7] [8] [9] [10] [11] [12] |

The build column in every table below records *which pinned revision documents the key*: `both`, `B41` (revision 157571 only), or `B42` (revision 1443167 only). This is deliberately a documentation claim, not a game-code claim — the B41-era page carries an explicit editorial warning that it needs improvement [3], so absence there is weak evidence of absence in the 41.78.16 binary. Where that distinction matters operationally it is called out in the notes and in the quarantine section.

**42.21 re-check scope.** What was re-checked for 42.21: the official 42.20.1, 42.20.3, 42.20.4 and 42.21 patch notes [7] [8] [9] [10] [11] and the TIS forum 42.21 changelist [12], against every statement in this document that they touch (player limit, anti-cheat, Steam authentication, safehouse, `SafetyDisconnectDelay`, `UsernameDisguises` and Discord entries). What could not be re-checked: the key names, defaults and ranges remain pinned to wiki revisions 1443167 and 157571 [2] [3] and were not re-extracted from a 42.21 server install; the patch notes name no changed default or new key. Statements not mentioned below are carried forward from 42.20 with no contradicting change found in those notes; they were not re-tested.

# Reference

## How to read the key tables

All rows in this section are sourced from the two pinned revisions: values, defaults and ranges tagged *(B42)* or listed for `both` come from revision 1443167 [2]; values tagged *(B41)* come from revision 157571 [3]. Three reading rules apply. First, **types are inferred** from the documented default and range (a `true`/`false` default ⇒ boolean; a whole-number default with integer bounds ⇒ integer; a decimal default ⇒ decimal; otherwise string or list) — the wiki does not publish a type column, so treat the type as a strong convention rather than a specification [2]. Second, **ranges come almost entirely from the B42-era revision**, which prints explicit minima and maxima; the B41-era revision generally does not, so a range on a `both` key is a B42-documented range unless tagged otherwise [2] [3]. Third, for **B41-only keys** the Default column shows the value printed in that revision, which does not separate example values from true defaults [3].

Operationally, the file is read at startup, and `.ini` edits can be applied to a live server with the `reloadoptions` admin command; the current effective values can be printed with `showoptions` [4]. The keys `DefaultPort` and `UDPPort` can be overridden per-launch by the `-port` and `-udpport` startup parameters, and the whole file is switched by `-servername` [5].

## Network, ports and server visibility

Player traffic uses the two game ports, which must be forwarded and allowed through the host firewall; RCON is a separate listener (next section) [2] [4].

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `DefaultPort` | integer | 16261 | 0–65535 | both | Primary game port; must be reachable from the internet [2]. Launch-time override: `-port` [5] |
| `UDPPort` | integer | 16262 | 0–65535 | B42 | Second game port in the B42-era revision [2]; override: `-udpport` [5]. Not listed in the B41-era revision [3] |
| `SteamPort1` | integer | 8766 | — | B41 | Steam-related port pair documented only at B41 [3] |
| `SteamPort2` | integer | 8767 | — | B41 | As above [3] |
| `UPnP` | boolean | true | — | both | Asks a UPnP gateway to map the ports automatically; reverts to default ports when mapping fails [2] |
| `UPnPLeaseTime` | integer | 86400 | — | B41 | Lease length for the UPnP mapping [3] |
| `UPnPZeroLeaseTimeFallback` | boolean | true | — | B41 | Fallback behaviour when a zero lease time is refused [3] |
| `UPnPForce` | boolean | true | — | B41 | Forces the mapping attempt [3] |
| `Public` | boolean | true *(B41)* / false *(B42)* | — | both | Listing in the in-game browser; the B42 revision notes Steam-enabled servers always show in the Steam server browser regardless [2] [3] |
| `PublicName` | string | (empty) | — | both | Display name in the browsers [2] |
| `PublicDescription` | string | (empty) | — | both | Browser description text [2] |
| `server_browser_announced_ip` | string | (empty) | — | both | Pins which IP is advertised on multi-IP hosts [2] |
| `DenyLoginOnOverloadedServer` | boolean | true | — | both | Refuses logins while the server is overloaded; the B41-era revision marks it untested [2] [3] |
| `PingLimit` | integer | 250 *(B41)* / 0 *(B42)* | 0–2147483647 | both | Kick threshold in milliseconds; 0 disables the check *(B42)* [2] [3] |
| `PingFrequency` | integer | 10 | — | B41 | Connection-check cadence, B41-era revision only [3] |
| `UseTCPForMapDownloads` | boolean | false | — | B41 | Map-transfer transport toggle, B41-era revision only [3] |
| `MaxPacketsPerSecond` | integer | 300 | 100–1000 | B42 | Per-client cap on processed network packets [2] |
| `LoginQueueEnabled` | boolean | false | — | B42 | Turns on a login queue [2] |
| `LoginQueueConnectTimeout` | integer | 60 | 20–1200 | B42 | Queue connection timeout, seconds [2] |
| `CoopServerLaunchTimeout` | integer | 20 | — | B41 | Co-op child-server launch timeout [3] |
| `CoopMasterPingTimeout` | integer | 60 | — | B41 | Co-op master ping timeout [3] |

## RCON

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `RCONPort` | integer | 27015 | 0–65535 | both | Remote-console listener, independent of the game ports [2] [3] |
| `RCONPassword` | string | (empty) | — | both | The B42 revision instructs choosing a strong value [2]; empty means no authenticated remote console. Generic Source-RCON clients such as gorcon's `rcon-cli` list Project Zomboid support [6] |

## Players, accounts and whitelist

Admission is layered: `Open` decides whether unknown accounts may join at all, `Password` gates the door, and the whitelist keys govern account lifecycle [2].

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `MaxPlayers` | integer | 16 *(B41)* / 32 *(B42)* | 1–100 *(B42, per the pinned revision)* | both | Admins are not counted against the cap; the B42 revision warns that values above 32 risk map-streaming problems and desync [2] [3]. The 42.20.3 notes describe improved player-limit handling with support for up to 254 players and administrator access when a server is full *(B42)* [8]; the pinned revision's 1–100 range predates that note and has not been re-extracted |
| `Open` | boolean | true | — | both | true = anyone may join and an account is created for them; false = an administrator must pre-create username/password pairs [2] |
| `Password` | string | (empty) | — | both | Join password; ignored when the server is run through the client's Host button [2] |
| `AutoCreateUserInWhiteList` | boolean | false | — | B41 | Auto-enrols joining users into the whitelist; B41-era revision only [3] |
| `DropOffWhiteListAfterDeath` | boolean | false | — | both | Deletes the account on character death — a permadeath device for `Open=false` servers [2] |
| `MaxAccountsPerUser` | integer | 0 | 0–2147483647 | both | Caps accounts per Steam user; 0 = unlimited; ignored for Host-button servers [2] |
| `AllowNonAsciiUsername` | boolean | false | — | both | Permits non-ASCII (e.g. Cyrillic) characters in usernames [2] |
| `AllowCoop` | boolean | true | — | B42 | Admits co-op/splitscreen players [2] |
| `DisplayUserName` | boolean | true | — | both | Renders account names over characters [2] |
| `ShowFirstAndLastName` | boolean | false | — | both | Renders character (not account) names instead [2] |
| `MouseOverToSeeDisplayName` | boolean | true | — | both | Requires hovering to reveal a name [2] |
| `UsernameDisguises` | boolean | false | — | B42 | Disguise mechanic for usernames; undescribed in the pinned revision [2]. 42.21 fixed a failure to connect to a dedicated or host server while this option was enabled *(B42)* [12] |
| `HideDisguisedUserName` | boolean | false | — | B42 | Companion to the above; undescribed [2] |
| `ServerWelcomeMessage` | string | (greeting text) | — | both | First chat-panel message after login; supports RGB colour tags and a line-break token *(B42)* [2] |
| `SpawnPoint` | coordinates | 0,0,0 | — | both | Forces all fresh spawns to fixed x,y,z; 0,0,0 disables the override [2] |
| `SpawnItems` | list | (empty) | — | both | Comma-separated item types granted to new characters, e.g. `Base.Axe,Base.Bag_BigHikingBag` [2] |
| `ResetID` | integer | 863866116 *(B42 doc default)* | 0–2147483647 | both | Soft-reset marker: a mismatch with the client forces a new character; the revision urges backing the IDs up [2] |
| `ServerPlayerID` | integer | (world-specific) | — | both | Identifies characters as belonging to this server; changes on soft reset; partner key to `ResetID` [2] [3] |
| `PlayerRespawnWithSelf` | boolean | false | — | both | Respawn at your own death location [2] |
| `PlayerRespawnWithOther` | boolean | false | — | both | Respawn at a splitscreen/Remote Play partner's location [2] |
| `SleepAllowed` | boolean | false | — | both | Sleeping possible (but optional) when tired [2] |
| `SleepNeeded` | boolean | false | — | both | Tiredness accrues and demands sleep; inert unless `SleepAllowed=true` [2] |
| `FastForwardMultiplier` | decimal | 40.0 | 1.00–100.00 | both | Clock acceleration applied while players sleep [2] |
| `PauseEmpty` | boolean | true | — | both | Freezes game time with zero players online; the B41-era revision claims the underlying default is false while printing true [2] [3] |

## PVP and player safety

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `PVP` | boolean | true | — | both | Master switch for player-versus-player harm [2] |
| `SafetySystem` | boolean | true | — | both | Per-player PVP opt-in; when false and `PVP=true`, everyone can hurt everyone at any time [2] |
| `ShowSafety` | boolean | true | — | both | Skull indicator over players who have PVP mode engaged [2] |
| `SafetyToggleTimer` | integer | 2 | 0–1000 *(B42)* | both | Delay to switch PVP mode on/off [2] |
| `SafetyCooldownTimer` | integer | 3 | 0–1000 *(B42)* | both | Cooldown before the mode can be switched again [2] |
| `SafetyDisconnectDelay` | integer | 60 | 0–60 | B42 | Disconnect-related safety delay; semantics undescribed in the pinned revision [2]. 42.21 lists the option as fixed, without saying what was wrong *(B42)* [12] |
| `PVPLogToolChat` | boolean | true | — | B42 | Mirrors PVP events to admin chat [2] |
| `PVPLogToolFile` | boolean | true | — | B42 | Writes PVP events to the server's logs [2] |
| `PVPMeleeDamageModifier` | decimal | 30.0 | 0.00–500.00 *(B42)* | both | Multiplier on player-vs-player melee damage [2] |
| `PVPFirearmDamageModifier` | decimal | 50.0 | 0.00–500.00 *(B42)* | both | Multiplier on player-vs-player ranged damage [2] |
| `PVPMeleeWhileHitReaction` | boolean | false | — | both | Lets a struck player swing again during the hit reaction [2] |
| `HidePlayersBehindYou` | boolean | true | — | both | Hides players outside your vision cone, as zombies are hidden [2] |
| `PlayerBumpPlayer` | boolean | false | — | both | Running through another player can shove/topple them [2] |
| `MapRemotePlayerVisibility` | integer | 1 | 1–4 | B42 | Who appears on the in-game map: 1 nobody, 2 friends, 3 friends plus nearby, 4 everyone [2] |
| `KnockedDownAllowed` | boolean | false | — | B42 | Flagged WIP in the revision: enabling can desynchronize player positions visually [2] |
| `SneakModeHideFromOtherPlayers` | boolean | true | — | B42 | Sneaking conceals you from other players [2] |
| `NoFire` | boolean | false | — | both | Disables fire; the B42 revision exempts campfires [2] |
| `AnnounceDeath` | boolean | false | — | both | Global chat notice on player death; the B41-era revision prints true while asserting the default is false [2] [3] |
| `AnnounceAnimalDeath` | boolean | false | — | B42 | Global chat notice on animal death [2] |

## Safehouses, factions and PVP events

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `PlayerSafehouse` | boolean | true *(B41)* / false *(B42)* | — | both | Players (and admins) may claim safehouses [2] [3] |
| `AdminSafehouse` | boolean | false | — | both | Restricts claiming to admins [2] |
| `SafehouseAllowTrepass` | boolean | true | — | both | Non-members may walk in uninvited (key name carries the game's own spelling) [2] |
| `SafehouseAllowFire` | boolean | true | — | both | Fire can damage a safehouse [2] |
| `SafehouseAllowLoot` | boolean | true | — | both | Non-members may take items inside [2] |
| `SafehouseAllowRespawn` | boolean | false | — | both | Members respawn at their safehouse after death [2] |
| `SafehouseDaySurvivedToClaim` | integer | 0 | 0–2147483647 | both | In-game days survived before claiming is allowed [2] |
| `SafeHouseRemovalTime` | integer | 144 | 0–2147483647 | both | Real-world hours of absence before a member is dropped (note the interior capital H in the key) [2] |
| `SafehouseAllowNonResidential` | boolean | false | — | B42 | Claiming of non-residential buildings [2] |
| `SafehouseDisableDisguises` | boolean | true | — | B42 | Disables disguises inside safehouse context; undescribed further [2] |
| `SafehousePreventsLootRespawn` | boolean | true | — | B42 | Claimed buildings never respawn loot [2] |
| `DisableSafehouseWhenOwnerConnected` | boolean | false | — | B42 | Protection applies only while the owner is offline; the B41-era key was `DisableSafehouseWhenPlayerConnected` [2] [3]. 42.21 fixed a conflict between this option and the sledgehammer-in-safehouse option below *(B42)* [12] |
| `MaxSafezoneSize` | integer | 20000 | 0–2147483647 | B42 | Upper bound on safezone area [2] |
| `AllowDestructionBySledgehammer` | boolean | true | — | both | Sledgehammers may demolish world objects [2] |
| `SledgehammerOnlyInSafehouse` | boolean | false | — | B42 | Restricts demolition to the player's own safehouse; requires the key above [2]. The 42.21 note on the conflict fix words the option in its own way, so the mapping to this key is inferred [12] |
| `Faction` | boolean | true | — | both | Faction creation enabled [2] |
| `FactionDaySurvivedToCreate` | integer | 0 | 0–2147483647 | both | Survival-days threshold to found a faction [2] |
| `FactionPlayersRequiredForTag` | integer | 1 | 1–2147483647 | both | Member count required before the owner may set a group tag [2] |
| `AllowTradeUI` | boolean | true | — | B41 | Direct player-to-player trade window; B41-era revision only [3] |
| `War` | boolean | false | — | B42 | Safehouse-war event toggle [2] |
| `WarStartDelay` | integer | 600 | 60–2147483647 | B42 | Seconds before a declared war begins [2] |
| `WarDuration` | integer | 3600 | 60–2147483647 | B42 | War length in seconds [2] |
| `WarSafehouseHitPoints` | integer | 3 | 0–2147483647 | B42 | Safehouse hit-point pool during a war [2] |

## Mods and map

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `Mods` | list | (empty) | — | both | Mod loading IDs, taken from each mod's `info.txt` under the Workshop content folder [2]. The pinned B42 revision gives no separator example for this key — see Pitfalls |
| `WorkshopItems` | list | (empty) | — | both | Steam Workshop IDs for the server to fetch, semicolon-separated; documented example `514427485;513111049` [2] |
| `Map` | string | Muldraugh, KY | — | both | World to load; for mod maps, the folder name under the mod's `media/maps/` directory [2] |
| `DoLuaChecksum` | boolean | true | — | both | Ejects clients whose Lua files fail the checksum comparison against the server [2]. 42.20.1 improved Lua checksum validation as a multiplayer anti-cheat measure *(B42)* [7] |

## Saves, backups and world identity

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `SaveWorldEveryMinutes` | integer | 0 | 0–2147483647 | both | Periodic save of loaded map areas, in real minutes; areas otherwise persist as clients leave them [2] |
| `BackupsCount` | integer | 5 | 1–300 | B42 | Retained backup generations [2] |
| `BackupsOnStart` | boolean | true | — | B42 | Take a backup at server start [2] |
| `BackupsOnVersionChange` | boolean | true | — | B42 | Take a backup when the game version changes [2] |
| `BackupsPeriod` | integer | 0 | 0–1500 | B42 | Interval for periodic backups; units are not stated in the pinned revision [2] |
| `Seed` | string | (generated) | — | B42 | Worldgen seed; changing it requires deleting `map_worldgen.bin` in the save directory to take effect [2] |
| `PlayerSaveOnDamage` | boolean | true | — | B41 | Persists player state on damage events; B41-era revision only [3] |
| `SaveTransactionID` | boolean | false | — | B41 | Save-transaction tracking; B41-era revision only, undescribed [3] |

`ResetID` and `ServerPlayerID` (Players table) are part of this area's operational surface: together they mark soft resets, and losing them severs clients from their characters [2].

## Anti-cheat and integrity

The B42-era revision documents ten `AntiCheat*` keys and describes four handling modes — instant ban, instant kick, log-only, and do nothing [2]. The keys take numeric values, but the pinned revision does **not** state which number selects which mode; that mapping is quarantined below (Claim 2). Note also that the revision's one-line descriptions are phrased as "disables … protection" for every key regardless of value, which is internally inconsistent with per-key numeric defaults — read the Default column as "value the file ships with", nothing more [2]. Context: 42.20's release notes state anti-cheat was reworked and re-enabled at stable, with item anti-cheat moved server-side [1].

**42.21 changes (B42).** The 42.21 notes state that the anti-cheat system was expanded ("various new cheats now guarded against") and that safehouse exploits were remedied [10] [12]. They list no new `AntiCheat*` key and no changed default or numeric meaning, so the table below is carried forward from the pinned revision unchanged. The same notes record a Steam authentication exploit, fixed in 42.21, that let players enter dedicated servers without authenticating through Steam, which had prevented SteamID bans from working [10] [12]; bans by SteamID are therefore described as effective from 42.21. Clothing condition is also handled server-side from 42.21 [12].

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `AntiCheatSafety` | integer | 2 | — | B42 | Safety-system rule [2] |
| `AntiCheatSpeed` | integer | 2 | — | B42 | Character speed rule [2] |
| `AntiCheatNoClip` | integer | 4 | — | B42 | No-clip rule [2] |
| `AntiCheatHit` | integer | 2 | — | B42 | Hit-validation rule [2] |
| `AntiCheatPacketException` | integer | 4 | — | B42 | Packet-exception rule [2] |
| `AntiCheatPermission` | integer | 2 | — | B42 | Permission rule [2] |
| `AntiCheatXP` | integer | 2 | — | B42 | XP-gain rule [2] |
| `AntiCheatSafeHouse` | integer | 2 | — | B42 | Safehouse rule (interior capital H) [2] |
| `AntiCheatPlayer` | integer | 2 | — | B42 | Player-state rule [2] |
| `AntiCheatChecksum` | integer | 2 | — | B42 | Checksum rule [2] |
| `SteamVAC` | boolean | true | — | both | Valve Anti-Cheat integration; the B41-era revision describes it as checking joiners for VAC bans [2] [3] |
| `KickFastPlayers` | boolean | false | — | B41 | Speed-kick toggle in the B41-era revision (marked untested there) [3]; the B42-era revision documents `AntiCheatSpeed` instead [2] |

## Performance-relevant keys

None of these is a magic lever; they bound work the server does per tick or per container. The parent document's hardware-sizing caveats apply.

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `ItemNumbersLimitPerContainer` | integer | 0 | 0–9000 | both | Hard cap on items per container; counts every unit (a cap of 50 means 50 nails); 0 = uncapped [2] |
| `BloodSplatLifespanDays` | integer | 0 | 0–365 | both | Age at which blood decals are culled on chunk load; 0 = never [2] |
| `CarEngineAttractionModifier` | decimal | 0.5 | 0.00–10.00 | both | Scales zombie attraction to running engines; the B42 revision notes lower values can reduce lag [2] |
| `MultiplayerStatisticsPeriod` | integer | 1 | 0–10 | B42 | Server statistics update period in seconds; 0 turns statistics off [2] |
| `SpeedLimit` | decimal | 70.0 | 10.00–150.00 | both | Undescribed in either pinned revision; range documented at B42 [2] [3] |
| `PhysicsDelay` | integer | 500 | — | B41 | Physics update delay; B41-era revision only [3] |
| `ZombieUpdateMaxHighPriority` | integer | 50 | — | B41 | Zombie network-update tuning quartet, B41-era revision only [3] |
| `ZombieUpdateDelta` | decimal | 0.5 | — | B41 | As above [3] |
| `ZombieUpdateRadiusLowPriority` | decimal | 45.0 | — | B41 | As above [3] |
| `ZombieUpdateRadiusHighPriority` | decimal | 10.0 | — | B41 | As above [3] |
| `SwitchZombiesOwnershipEachUpdate` | boolean | false | — | B42 | Zombie ownership handoff per update; undescribed in the pinned revision [2] |
| `UltraSpeedDoesnotAffectToAnimals` | boolean | false | — | B42 | Exempts animals from ultra fast-forward (key name's casing is as shipped) [2] |
| `RemovePlayerCorpsesOnCorpseRemoval` | boolean | false | — | both | Extends the sandbox corpse-removal timer to player bodies [2] |
| `TrashDeleteAll` | boolean | false | — | both | Enables the bin "delete all" action [2] |

## VOIP

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `VoiceEnable` | boolean | true | — | both | Voice chat master switch [2] |
| `VoiceMinDistance` | decimal | 10.0 | 0.00–100000.00 | both | Tile distance at which voice starts attenuating [2] |
| `VoiceMaxDistance` | decimal | 300.0 *(B41)* / 100.0 *(B42)* | 0.00–100000.00 *(B42)* | both | Tile distance beyond which voice is inaudible [2] [3] |
| `Voice3D` | boolean | true | — | both | Directional (positional) audio [2] |
| `VoiceComplexity` | integer | 5 | — | B41 | Codec quality quartet documented only at B41 [3] |
| `VoicePeriod` | integer | 20 | — | B41 | As above [3] |
| `VoiceSampleRate` | integer | 24000 | — | B41 | As above [3] |
| `VoiceBuffering` | integer | 8000 | — | B41 | As above [3] |

## Chat, Discord bridge and moderation

The Discord bridge relays global text chat to a Discord channel via a bot token; the B42-era key set splits chat, log and command channels, where the B41-era set had a single channel plus a channel ID [2] [3].

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `GlobalChat` | boolean | true | — | both | Server-wide `/all` chat [2] |
| `ChatStreams` | list | "s,r,a,w,y,sh,f,all" | — | both | Enabled chat channels (say, radio, admin, whisper, yell, safehouse, faction, global); deleting an entry disables that stream [2] |
| `ChatMessageCharacterLimit` | integer | 200 | 64–1024 | B42 | Per-message length cap [2] |
| `ChatMessageSlowModeTime` | integer | 3 | 1–30 | B42 | Minimum seconds between messages [2] |
| `BanKickGlobalSound` | boolean | true | — | both | Audible cue on ban/kick [2] |
| `DiscordEnable` | boolean | false | — | both | Bridge master switch [2]. 42.21 fixed an endless connection loop that occurred when the Discord API was unavailable *(B42)* [12] |
| `DiscordToken` | string | (empty) | — | both | Bot access token — treat as a secret [2] |
| `DiscordChatChannel` | string | (empty) | — | B42 | Chat relay channel, by name [2] |
| `DiscordChannel` | string | (empty) | — | B41 | B41-era chat channel key [3] |
| `DiscordChannelID` | string | (empty) | — | B41 | B41-era numeric channel ID key [3] |
| `DiscordLogChannel` | string | (empty) | — | B42 | Log relay channel [2] |
| `DiscordCommandChannel` | string | (empty) | — | B42 | Command channel [2] |
| `WebhookAddress` | string | (empty) | — | B42 | Slack incoming-webhook URL [2] |
| `BadWordListFile` | string | (empty) | — | B42 | Path to a one-word-per-line blocklist [2] |
| `GoodWordListFile` | string | (empty) | — | B42 | Allowlist overriding blocklist substrings [2] |
| `BadWordPolicy` | integer | 3 | — | B42 | Response to a blocked word: 1 ban, 2 kick, 3 record to database, 4 mute [2] |
| `BadWordReplacement` | string | [HIDDEN] | — | B42 | Substitution text for filtered words [2] |
| `DisableRadioStaff` | boolean | false | — | both | Radio-transmission suppression family for staff access levels [2] |
| `DisableRadioAdmin` | boolean | true | — | both | As above, admin level [2] |
| `DisableRadioGM` | boolean | true | — | both | As above, gm level [2] |
| `DisableRadioOverseer` | boolean | false | — | both | As above, overseer level [2] |
| `DisableRadioModerator` | boolean | false | — | both | As above, moderator level [2] |
| `DisableRadioInvisible` | boolean | true | — | both | Suppresses transmissions from invisible players [2] |
| `DisableScoreboard` | boolean | false | — | B42 | Turns the scoreboard off entirely [2] |
| `HideAdminsInPlayerList` | boolean | false | — | B42 | Removes admins from the player list [2] |
| `SteamScoreboard` | boolean | true *(B41)* / false *(B42)* | — | both | Shows Steam names/avatars in the player list [2] [3] |
| `ShowCoordinates` | boolean | false | — | B42 | Prints the character's coordinates on screen [2] |

The B41-era revision also records that a `LogLocalChat` key existed and was deleted by patch 41.66, citing the official patch notes for the removal [3].

## Server logging keys

| Key | Type | Default | Range | Build | Notes |
|-----|------|---------|-------|-------|-------|
| `ClientCommandFilter` | list | "-vehicle.*;+vehicle.damageWindow;+vehicle.fixPart;+vehicle.installPart;+vehicle.uninstallPart" | — | both | Semicolon-separated rules for the `cmd.txt` log: a `-` prefix suppresses a command pattern, `+` re-includes one [2] |
| `ClientActionLogs` | list | "ISEnterVehicle;ISExitVehicle;ISTakeEngineParts;" | — | B42 | Actions mirrored to `ClientActionLogs.txt` [2] |
| `PerkLogs` | boolean | true | — | B42 | Writes perk-level changes to `PerkLog.txt` [2] |

`PVPLogToolChat` / `PVPLogToolFile` (PVP table) complete the logging surface [2].

# B41 vs B42 Delta

This delta compares the two pinned revisions of the same reference page — 157571 (versioned 41.78.16) [3] against 1443167 (versioned 42.20.0) [2]. It is therefore a *documentation* delta: precise about what each revision records, deliberately silent about when the game binary actually changed (see Risks, and Claim 1).

**Renamed or restructured keys** [2] [3]:

| B41-era key(s) | B42-era key(s) | Change |
|----------------|----------------|--------|
| `DisableSafehouseWhenPlayerConnected` | `DisableSafehouseWhenOwnerConnected` | Rename; semantics documented at B42 as owner-presence-based |
| `DiscordChannel`, `DiscordChannelID` | `DiscordChatChannel`, `DiscordLogChannel`, `DiscordCommandChannel`, `WebhookAddress` | Bridge expanded from one channel (plus ID) to three named channels plus a Slack webhook |

**Keys that left the `.ini`** [2] [3]: the loot-respawn trio `HoursForLootRespawn`, `MaxItemsForLootRespawn`, `ConstructionPreventsLootRespawn` and the reading-speed key `MinutesPerPage` are `.ini` keys in the B41-era revision but appear under `SandboxVars.lua` in the B42-era revision (with `MinutesPerPage` moving from 1.0 to 2.0 and `MaxItemsForLootRespawn` from 4 to 5 along the way). On B42 those values belong to the sibling SandboxVars document's territory.

**Documented defaults that differ between revisions** [2] [3]: `MaxPlayers` 16 → 32 (with an explicit 1–100 range and a >32 desync warning at B42); `PingLimit` 250 → 0 (check disabled); `VoiceMaxDistance` 300.0 → 100.0; `SteamScoreboard` true → false; `PlayerSafehouse` true → false; `Public` true → false.

**Families documented only in the B42-era revision** [2]: `UDPPort`; the ten `AntiCheat*` keys; `Backups*` (four keys); safehouse war (`War`, `WarStartDelay`, `WarDuration`, `WarSafehouseHitPoints`); chat moderation (`BadWordListFile`, `GoodWordListFile`, `BadWordPolicy`, `BadWordReplacement`, `ChatMessageCharacterLimit`, `ChatMessageSlowModeTime`); login queueing (`LoginQueueEnabled`, `LoginQueueConnectTimeout`); `MaxPacketsPerSecond`; `MapRemotePlayerVisibility`; `ShowCoordinates`; `Seed`; towing toggles (`DisableVehicleTowing`, `DisableTrailerTowing`, `DisableBurntTowing` — not tabulated above); the disguise keys; `SafetyDisconnectDelay`; `MaxSafezoneSize`; `SledgehammerOnlyInSafehouse`; `SafehouseAllowNonResidential`; `SafehousePreventsLootRespawn`; `PVPLogToolChat`/`PVPLogToolFile`; `PerkLogs`; `ClientActionLogs`; `AllowCoop`; `AnnounceAnimalDeath`; `KnockedDownAllowed`; `SneakModeHideFromOtherPlayers`; the animal-adjacent toggles (`UltraSpeedDoesnotAffectToAnimals`, `SwitchZombiesOwnershipEachUpdate`).

**Keys documented only in the B41-era revision** [3]: `nightlengthmodifier` (night-length scaling, the page's first key); `AutoCreateUserInWhiteList`; `PingFrequency`; `SteamPort1`/`SteamPort2`; the extra UPnP keys; the co-op timeouts; the VOIP codec quartet (`VoiceComplexity`, `VoicePeriod`, `VoiceSampleRate`, `VoiceBuffering`); `PhysicsDelay`; `UseTCPForMapDownloads`; `PlayerSaveOnDamage`; `SaveTransactionID`; `AllowTradeUI`; the `ZombieUpdate*` quartet; `KickFastPlayers`. One key is positively recorded as removed from the game rather than merely undocumented: `LogLocalChat`, deleted in 41.66 per the official patch notes cited by that revision [3].

**Context for the anti-cheat family**: the 42.20 stable release notes describe anti-cheat as reworked and re-enabled, with item anti-cheat now server-side and several exploits (item spawning, XP, foraging) closed [1] — which is why the B42-era `.ini` surface polices more than the B41-era one did. Later notes extend this: Lua checksum validation was improved in 42.20.1 [7], and the anti-cheat system was expanded again in 42.21 [10] [12].

**42.20.1 to 42.21 (B42)**: none of those notes renames, adds or re-defaults a documented `.ini` key; they change the behaviour of existing options (see the per-key notes above) [7] [8] [9] [10] [11] [12]. The pinned wiki revision was not re-extracted, so absence of a mention is not proof that no default moved.

# Practical Guidance

Copy-paste blocks below use `servertest.ini` names verbatim; after saving a live edit, apply with `reloadoptions` and confirm with `showoptions` (both documented on the Dedicated server page [4]).

**Network baseline (internet-facing B42 server):**

```ini
DefaultPort=16261
UDPPort=16262
UPnP=false
Public=false
PingLimit=0
```

Forward/allow both game ports as UDP on the host firewall; on Ubuntu that is `sudo ufw allow 16261/udp` and `sudo ufw allow 16262/udp` [4]. Set `UPnP=false` on any professionally hosted box — you have real port forwarding, so silent gateway mapping is only a failure mode. Leave `PingLimit=0` until you have a latency problem you can measure.

**First-boot hardening checklist (before advertising the server):**

```ini
Open=false
Password=<join-password-or-empty-if-whitelist-only>
RCONPassword=<long-random-secret>
MaxAccountsPerUser=1
AllowNonAsciiUsername=false
DoLuaChecksum=true
```

`Open=false` turns the whitelist into an allowlist you control; `RCONPassword` must never ship empty on a reachable `RCONPort`. If you keep `Open=true`, set `Password` and decide deliberately whether `DropOffWhiteListAfterDeath=true` (hardcore permadeath) fits your community.

**Mod wiring (pair every entry):**

```ini
WorkshopItems=514427485;513111049
Mods=<LoadingID1>;<LoadingID2>
```

Workshop IDs are the numbers in the Workshop URL; loading IDs come from each mod's `info.txt` [2]. The pinned reference only demonstrates semicolons for `WorkshopItems` — mirror that for `Mods` but verify at boot by reading the loaded-mod list in the console, because the `Mods` separator is undocumented at B42 (and see the parent document's quarantined backslash claim before copying a hosting panel's format).

**Backups and saves (B42):**

```ini
SaveWorldEveryMinutes=15
BackupsCount=10
BackupsOnStart=true
BackupsOnVersionChange=true
BackupsPeriod=60
```

`BackupsOnVersionChange=true` is your cheapest insurance across patch days — keep it on. Treat `BackupsPeriod`'s units as unverified (the revision does not state them); observe timestamps on produced backups before trusting a rotation schedule. In-game backups are not offsite backups: also archive `Zomboid/Server` (`.ini` plus Lua) and the save folder externally, and record `ResetID`/`ServerPlayerID` somewhere safe — losing them orphans every character [2].

**Discord bridge (B42):**

```ini
DiscordEnable=true
DiscordToken=<bot-token>
DiscordChatChannel=<channel-name>
DiscordLogChannel=<channel-name>
DiscordCommandChannel=<channel-name>
```

The token is a credential: keep the `.ini` out of world-readable paths and out of pastebins when asking for help. B41 configs use `DiscordChannel`/`DiscordChannelID` instead — do not copy a B42 snippet onto a legacy41 server unedited.

**PVE server quick-set:** `PVP=false` alone is the master switch; keep `SafetySystem=true` anyway so a future PVP event needs only one key flipped, and pre-stage `PVPMeleeDamageModifier`/`PVPFirearmDamageModifier` values you have play-tested.

**Anti-cheat stance (B42):** leave every `AntiCheat*` key at its shipped value until you have a false-positive report you can reproduce; the numeric mode mapping is not primary-documented (Claim 2), so any tuning is experimentation. If modded Lua trips checksum kicks, the documented lever is `DoLuaChecksum` — change it knowingly, since it is also your file-integrity gate [2].

# Common Pitfalls & Troubleshooting

- **Editing the wrong file for the change.** Loot respawn and reading speed are `.ini` keys on B41 but SandboxVars keys on B42 [2] [3]; a copied B41 guide will have you editing lines a B42 server ignores.
- **B41 key names in a B42 file (and vice versa).** `DisableSafehouseWhenPlayerConnected`, `DiscordChannelID` and `VoiceComplexity` do not exist in the B42-era documentation; `UDPPort`, `BackupsCount` and the `AntiCheat*` keys have no B41-era documentation [2] [3]. An unrecognized key fails silently — the server simply never behaves as intended.
- **`MaxPlayers` raised past 32.** The documented range runs to 100, but the same revision warns of map-streaming degradation and desync above 32 [2]; the 42.20.3 notes say up to 254 players are supported *(B42)* [8], and neither source gives a tested recommendation. Raise it in steps and observe; do not jump to the maximum.
- **RCON port open with a blank password.** The default `RCONPort=27015` plus an empty `RCONPassword` on a public IP is an unauthenticated admin console; any Source-RCON client can speak to it [2] [6].
- **`Open=true` with no `Password` "temporarily".** That is a public server. If you must, set `MaxAccountsPerUser=1` so one Steam user cannot mass-create accounts [2].
- **Backslashes, semicolons and the `Mods=` line.** Only `WorkshopItems` has a documented separator example [2]; if mods install but never load, verify pairing (both lists populated) and check the boot console before restructuring the line to match any single hosting KB.
- **Soft-reset IDs treated as disposable.** Regenerating or losing `ResetID`/`ServerPlayerID` forces every client onto a new character [2]. Record them with your backups.
- **Key-name typos that look correct.** `SafehouseAllowTrepass` (the game's spelling), `SafeHouseRemovalTime` (capital H), `UltraSpeedDoesnotAffectToAnimals` (lowercase "not") are all as-shipped [2]; "fixing" the spelling creates a new, meaningless key.
- **Expecting `reloadoptions` to cover everything.** The documented live path is `.ini` plus `reloadoptions` [4]; mod-list and sandbox changes should be treated as restart-required (the parent document's Claim 4 covers the community's stricter folklore).
- **Welcome message renders as one line.** A multi-line `ServerWelcomeMessage` needs the documented line-break token; RGB colour tags are also available *(B42)* [2].

# Community Notes & Unverified Claims

## Claim 1 — Keys documented only at B42 were introduced by Build 42

- **Claim:** Hosting KBs and community changelists commonly present B42 server configuration as having "added" the backups keys, anti-cheat keys, chat moderation and the other families this document tags B42.
- **Why unverified:** The tag here records presence in wiki revision 1443167 versus absence from revision 157571 [2] [3] — and the B41-era revision carries an explicit editorial banner that it is incomplete. No per-key trace against official patch notes was performed; some "B42" keys may have existed in late B41 builds undocumented.
- **Confidence:** Medium. The pattern is directionally right (42.20's notes confirm the anti-cheat family's context [1]), but any individual key's introduction date is unproven.

## Claim 2 — The `AntiCheat*` numeric values map 1=Ban, 2=Kick, 3=Log, 4=Disable

- **Claim:** Server-admin guides and Discord/forum discussions circulate a fixed mapping from the integers in `AntiCheatXP=2`-style lines to the four documented handling modes, most commonly 1=Ban, 2=Kick, 3=Log, 4=Disable — which would make the shipped defaults "kick" for most rules and "disable" for the no-clip and packet-exception checks.
- **Why unverified:** The pinned revision lists the four modes and the numeric defaults but never states which number selects which mode [2]; no official source for the mapping was found, and the revision's own per-key descriptions ("disables … protection" on every key) muddy rather than confirm it.
- **Confidence:** Low. The mapping is plausible and widely repeated, but it is exactly the kind of copy-propagated community fact this knowledge base refuses to promote without a primary source.

# Risks & Caveats

- **The core source is a community wiki, not the game.** Both anchor revisions are fact-only pzwiki citations [2] [3]; no key in this document was verified against a generated `servertest.ini` from a live 42.20 or 41.78.16 install. The Verification Steps below close that gap mechanically.
- **The B41 column inherits an incomplete page.** Revision 157571 self-flags as needing improvement and mixes example values with defaults [3]; B41-only rows are correspondingly weaker than B42 rows.
- **Wiki-revision delta ≠ game delta.** Every "B42-only"/"B41-only" tag is a statement about two page revisions (see Claim 1). Only `LogLocalChat` carries a patch-note-backed removal [3].
- **Hotfix drift.** 42.20 went stable on 2026-07-29 [1] and 42.21 on 2026-09-28 [11]; the wiki revisions pinned here predate 42.21, and the patch notes cover behaviour rather than a key-by-key schema, so a key could have been added or re-defaulted without a note.
- **Server-side verification gap.** The 42.21 re-check was against patch notes only; no key was re-verified on a 42.21 server install.
- **Undescribed keys are listed, not explained.** Where a revision documents a key without semantics (`SpeedLimit`, `SafetyDisconnectDelay`, `UsernameDisguises`, `SwitchZombiesOwnershipEachUpdate`, `SaveTransactionID`), this document says "undescribed" rather than inventing behaviour.
- **Live-check asymmetry.** pzwiki currently serves interactive challenges to some automated clients; the citation URLs below were verified reachable at access time, and the B41 revision is doubly anchored via an Internet Archive capture in case the origin hardens further.

# Verification Steps

1. **Regenerate ground truth (B42):** install the server (SteamCMD App 380870, stable branch), start it once, and diff the generated `Zomboid/Server/servertest.ini` key list and values against the B42 rows above; repeat with the `legacy41` beta for the B41 rows.
2. **Re-extract on 42.21:** the key schema is pinned to wiki revisions, so repeat step 1 on a 42.21 install and re-run the server-settings gate.
3. **Confirm the live-reload boundary:** change one benign key (e.g. `PublicDescription`), run `reloadoptions`, then `showoptions`, and confirm the new value is live [4].
4. **Probe Claim 2 empirically:** on a disposable B42 server, set `AntiCheatSpeed` to each of 1/2/3/4, trip the speed rule with a debug client, and record ban/kick/log/nothing per value.
5. **Check the port surface:** with the server up, verify UDP listeners on `DefaultPort` and `UDPPort` and the RCON listener on `RCONPort` from another host; confirm an RCON login fails with a wrong password [2] [6].
6. **Verify backup behaviour:** set `BackupsPeriod` to a small value, run for an hour, and timestamp the produced backups to resolve the undocumented units.
7. **Confirm the citation pins:** both Server settings revisions are permalinked below; the B41 revision can additionally be read via its 2023-10-28 Internet Archive capture if the origin blocks you [3].

# Open Questions

- What is the authoritative numeric-to-mode mapping for the `AntiCheat*` keys, and will The Indie Stone document it now that anti-cheat is a stable-branch feature [1] [2]? (Claim 2; Step 4 resolves behaviour, not provenance.)
- Which "B42-only" keys actually exist and function on a 41.78.16 server despite being missing from the B41-era page (Claim 1)? Step 1's legacy41 diff answers this per key.
- What are `BackupsPeriod`'s units, and how does it interact with `SaveWorldEveryMinutes` [2]? (Step 6.)
- What do the undescribed keys (`SpeedLimit`, `SafetyDisconnectDelay`, `SwitchZombiesOwnershipEachUpdate`, `UsernameDisguises`) actually govern, and on which builds are they read?
- Does the 42.20.1-42.21 wave change any documented default in this table? The patch notes name none [7] [8] [9] [10] [11] [12]; confirm against a 42.21 server's generated `.ini` and the wiki's revision history at the next review.
- What `MaxPlayers` range does a 42.21 server accept, given the 254-player statement [8] and the 1–100 range in the pinned revision [2]?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via the ISteamNews API mirror, app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [7] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [8] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895. Accessed 2026-10-07.
- [9] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [10] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [11] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [12] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post 2026-09-23; multiplayer list abridged to selected items in the retrieved copy). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [2] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [3] **PZwiki** — *Server settings* (revision 157571; page versioned against 41.78.16, last edited 2023-10-22). https://pzwiki.net/w/index.php?title=Server_settings&oldid=157571 — also preserved at https://web.archive.org/web/20231028101749/https://pzwiki.net/wiki/Server_settings. Accessed 2026-07-31. Fact-only source.
- [4] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Startup parameters* (revision 1393745). https://pzwiki.net/w/index.php?title=Startup_parameters&oldid=1393745. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [6] **gorcon** — *rcon-cli* (MIT; Source RCON CLI listing Project Zomboid support). https://github.com/gorcon/rcon-cli. Accessed 2026-07-31.

**Community & Creator**

- None cited. Claim attributions above name where the claims circulate; no community URL met the citation bar.

**Further Reading**

# Further Reading

- The ISteamNews mirror used to verify the primary announcement: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- beyenilmez's pz-admin (GUI over RCON, edits server options remotely): https://github.com/beyenilmez/pz-admin
- jmwhitworth's zomboid_rcon (Python RCON, scriptable option queries): https://github.com/jmwhitworth/zomboid_rcon

# Related Documents

- `admins-foundation` — the parent overview: file locations, branches, ports, memory, tooling; this document deepens its configuration-surface section.
- `admins-sandboxvars-reference` — the sibling per-setting reference for `SandboxVars.lua`, including the keys that migrated there from the B41 `.ini`.
- `modders-foundation` — Workshop/mod structure context behind `Mods=`/`WorkshopItems=`.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed against the 42.20.1, 42.20.3, 42.20.4, 42.21 unstable and stable Steam notes [7] [8] [9] [10] [11] and the TIS forum 42.21 changelist [12]; added per-key 42.21 notes, player-limit and anti-cheat updates, Applicability scope. Key schema not re-extracted. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
