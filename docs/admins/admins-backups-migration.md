---
id: admins-backups-migration
title: "Backups, Saves and Migration: Protecting a Server World"
version: 1.0.0
status: approved
confidence: Medium
category: Admins
topic: "Server operations"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [admins-foundation, admins-server-ini-reference, admins-sandboxvars-reference, lore-foundation, meta-style-guide]
tags: [backups, saves, migration, world-data, player-database, legacy41, soft-reset, resetid, restore, runbook]
game_versions_verified: ["41.78.16", "41.78.21", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-backups-migration |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 41.78.21, 42.20, 42.21 |

# Executive Summary

A Project Zomboid server world is a handful of directories under one `Zomboid` data folder in the server user's home directory: the world state under `Saves/Multiplayer`, the configuration under `Server`, the account database under `db`, and the log output under `Logs` and the console files [4] [8] [9]. Everything an admin needs to protect, restore or move a community lives in that one tree, which is why the officially documented disaster-recovery procedure is simply to copy or compress the whole `Zomboid` folder [8]. This document is the Admins-track runbook for that tree: what each piece is, what the four built-in `Backups*` settings actually do, how to take and restore manual backups (cold and hot), how to move a world between machines and operating systems, and what the B41→B42 boundary means for old worlds.

The migration headline is unforgiving: Build 41 savegames are not compatible with Build 42, and unstable 42.19 saves are not compatible with 42.20 — there is no conversion path, only the `legacy41` and `42.19` beta branches for keeping old worlds alive on the build that created them [1] [2]. A backup strategy therefore protects you against hardware loss, corruption and bad admin days, but not against a build upgrade; the only "migration" across the build boundary is a fresh world. Since 42.20.1, B42 servers also refuse to host broken B41 worlds, which closes off an accidental route across the boundary [14]. Within a build, worlds move freely between Windows and Linux hosts as long as the server name stays consistent across the config files, the save folder and the account database, and the files end up owned by the (non-root) user the server runs as [4] [10] [11].

Document-level confidence is **Medium**: the folder layout, backup-setting names/defaults, branch strategy and soft-reset ID mechanics rest on current primary announcements and revision-pinned wiki pages, but the pinned settings reference gives the `Backups*` keys no descriptions — their behaviour and on-disk output are corroborated only by hosting documentation that disagrees on the details, and the disagreement is quarantined rather than resolved.

# Key Takeaways

- One tree holds everything: `Zomboid/Server` (config), `Zomboid/Saves/Multiplayer/<name>` (world), `Zomboid/db/<name>.db` (accounts), `Zomboid/Logs` plus `server-console.txt` (logs) — back up the whole `Zomboid` folder and you have the server *(cited)* *(both)*
- The built-in backup surface is four `.ini` keys: `BackupsCount` (default 5, max 300), `BackupsOnStart` (true), `BackupsOnVersionChange` (true), `BackupsPeriod` (default 0 = off, max 1500) *(cited; defaults verified against the 42.20-era reference)*
- The pinned settings reference documents those keys' defaults and ranges but not their behaviour; where the automatic backups land on disk is contested between secondary sources *(community, unverified)*
- A version-change backup is not a converter: Build 41 saves "will not be compatible" with Build 42, and 42.19 unstable saves are likewise incompatible with 42.20 — keep old worlds alive on the `legacy41` / `42.19` beta branches instead *(cited)* *(both)*
- Cold backups (server stopped) are the only restore-grade backups; if you must copy hot, flush first with the `save` admin command and treat the copy as best-effort *(cited synthesis)* *(both)*
- Moving a world cross-OS is a path-and-ownership exercise: `%USERPROFILE%\Zomboid` ↔ `~/Zomboid`, identical server name everywhere, and `chown` the tree to the dedicated server user on Linux *(cited)* *(both)*
- A soft reset is signalled to clients by `ResetID` (paired with `ServerPlayerID`); back both IDs up, because a client whose IDs mismatch is forced to make a new character *(cited)* *(both)*
- The documented soft-reset trigger, the `-Dsoftreset` startup parameter, is recorded as broken on 42.20.0 *(cited)* *(B42)*
- Players' local map knowledge lives client-side in a folder keyed to your server's IP and port — change either and returning players' map data is orphaned *(cited)* *(both)*

# Purpose

This document answers the four questions every server operator eventually asks under pressure: *what exactly do I need to copy to be safe, what is the game already backing up for me, how do I put a backup (or a whole machine move) back together, and can I carry my world across the Build 41 → Build 42 boundary?* It is written as an ops runbook — the procedures are meant to be pasted into a terminal — and it goes deeper than the foundation overview, which only mapped where the configuration surfaces live.

# Scope

Covered: the on-disk anatomy of a server world (`Saves/Multiplayer`, `Server`, `db`, `Logs`, console files, the client-side map cache); the four built-in `Backups*` server settings with their pinned defaults and ranges; manual backup procedure and the cold/hot distinction; restoring from backup step-by-step; moving a world between machines including Windows↔Linux; the build-migration reality (no B41→B42 conversion; `legacy41` and `42.19` branch strategy); and soft resets via `ResetID`/`ServerPlayerID`.

Not covered: the full key-by-key `server.ini` and SandboxVars references (sibling documents `admins-server-ini-reference` and `admins-sandboxvars-reference`); installation and branch selection at overview level (`admins-foundation`); hosting-panel-specific backup buttons (vendor UIs change; the file-level truth here is what those buttons wrap); and singleplayer save management except where client-side files affect server migrations.

# Definitions

- **Zomboid folder (cache folder)** — the per-user data directory (`%USERPROFILE%\Zomboid` on Windows, `~/Zomboid` on Linux and macOS) holding settings, saves, databases and logs; relocatable with the `-cachedir` startup parameter [6] [8].
- **World folder** — `Zomboid/Saves/Multiplayer/<servername>`, the generated and continuously saved world state for one server [4].
- **Account database** — the SQLite file under `Zomboid/db` named after the server, holding user accounts and whitelist state [4] [10].
- **Cold backup / hot backup** — a copy taken with the server stopped (cold) versus running (hot). Only cold copies are guaranteed internally consistent; see Practical Guidance.
- **Soft reset** — a server-side reset event signalled to clients through `ResetID`; clients whose stored IDs no longer match are forced onto a fresh character [5].
- **`legacy41` / `42.19`** — Steam beta branches that pin the client and server to Build 41.78 or unstable 42.19 respectively, keeping saves from those builds playable after 42.20 became stable [1] [2].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16; latest primary-attested legacy release 41.78.21 (2026-08-26, security hotfix) | Same `Zomboid` tree and server-name keying; `legacy41` is the survival branch for B41 worlds [1] [4] [17] |
| B42 (stable) | Yes | 42.20; re-checked against 42.21 | Settings reference and folder layout verified against 42.20-era page revisions [4] [5]; `-Dsoftreset` non-functional as of 42.20.0 [6]; 42.21 is the current stable since 2026-09-28 [15] |

Revision note (2026-10-07): this document was re-checked against the Steam hotfix posts 42.20.1 and 42.20.4/41.78.21, the 42.21 stable post and the TIS forum 42.21 patch notes (selected items only) [14] [15] [16] [17]. Only statements those sources affect were changed (current stable branch, B41-world hosting on B42 servers, update-safety guidance). Everything else is carried forward unchanged from the 2026-07-31 review (41.78.16, 42.20) with no contradicting change found in those sources; it was not re-tested on a live server, and the pinned wiki revisions were not refreshed.

The pinned wiki revisions used here are versioned against the 42.20 era [4] [5] [8]. The `Backups*` keys, `ResetID` and `ServerPlayerID` are documented in the 42.20-versioned settings reference; their presence on B41 is consistent with the unchanged file layout but is not re-verified against a B41-era page revision in this document — treat exact B41 defaults as unconfirmed.

# Reference

## Where a server world lives on disk

The server keeps all mutable data outside the game installation, in the `Zomboid` folder of the account that runs the process: `%USERPROFILE%\Zomboid` on Windows, `~/Zomboid` on Linux (e.g. `/home/pzuser/Zomboid` under the wiki's install layout, `/home/steam/Zomboid` under the Bobagi Ubuntu guide) [4] [8] [9]. The location can be overridden with the `-cachedir=<path>` startup parameter, and on Linux equivalently with the `-Ddeployment.user.cachedir` JVM property [6]. The pieces that matter for backup and migration:

| Path (under `Zomboid/`) | What it holds | Cited at |
|-------------------------|---------------|----------|
| `Server/<name>.ini` | Server, network, security and mod settings | [4] |
| `Server/<name>_SandboxVars.lua` | Gameplay-rule settings | [4] |
| `Server/<name>_spawnpoints.lua`, `Server/<name>_spawnregions.lua` | Spawn configuration | [4] |
| `Saves/Multiplayer/<name>/` | The generated, continuously saved world state | [4] |
| `db/<name>.db` | Account database keyed to the server name | [4] [10] |
| `Logs/` | Timestamped server log files | [9] |
| `server-console.txt` | The dedicated server's console log | [8] |
| `logs.zip` (root of the tree) | Auto-collected support bundle: logs from the last five launches, server and co-op logs, settings files, mod lists and files from the last loaded save | [8] |

Every data file is keyed to the server name (default `servertest`): the `.ini`, the Lua settings files, the world folder and the `db` file all share it, and launching with `-servername <name>` switches the whole set [4]. Two independent hosting sources — corroborating secondaries, pending first-hand verification — describe the world folder's contents identically: `map_*.bin` chunk files for altered terrain and structures, `map_t.bin` for world time and metadata, `map_sand.bin` for the active sandbox settings, plus two SQLite databases, `players.db` (characters) and `vehicles.db` (vehicles) [10] [11].

One copy of world knowledge is *not* on the server: each player's discovered-map data is stored on their own machine under `Zomboid/Saves`, in a folder named from the server's IP address, port and a hash (the wiki's example has the shape `123.45.0.12_16261_<hash>`) [4]. The wiki's server-renaming instructions warn that reusing a port carries old client-side map data over, and suggest either dedicating the port to one server or having players set aside their local folder [4].

## The built-in backup settings

Four `.ini` keys govern the server's automatic backups. Defaults and ranges below are from the pinned 42.20-era settings reference; that reference lists the keys with values only and no behavioural description [5]. The behaviour column is corroborated from hosting documentation (secondary, corroborate-only) [12]:

| Key | Default | Range | Behaviour (secondary-corroborated) |
|-----|---------|-------|------------------------------------|
| `BackupsCount` | 5 | 1–300 | Maximum number of stored backups before rotation [5] [12] |
| `BackupsOnStart` | true | boolean | Take a backup each time the server starts [5] [12] |
| `BackupsOnVersionChange` | true | boolean | Take a backup when the game version changes [5] [12] |
| `BackupsPeriod` | 0 | 0–1500 | Periodic backup interval; hosting documentation describes it as minutes, with 0 meaning disabled [5] [12] |

Two honesty notes. First, the unit of `BackupsPeriod` is not stated by the pinned reference; "minutes, 0 = off" is hosting-sourced and capped at Medium confidence accordingly [5] [12]. Second, secondary sources conflict about where the automatic backups are written and in what form — see Claim 1 in the quarantine section. Do not design a retention or disk-space plan around the automatic backups until you have located them on your own host (Verification Steps, step 3).

What the automatic system covers is bounded by what it triggers on: start, version change, and an optional timer [5] [12]. It is a safety net under the live world, not an off-machine disaster-recovery plan — it lives on the same disk as the server, and no setting ships copies elsewhere.

## Manual backups: the officially documented procedure

The wiki's Tech Support page documents whole-installation backup directly: compress the `Zomboid` folder to a `.zip` (or copy it uncompressed) and store it on another drive; to restore, place the `Zomboid` folder back at the same per-user location on the target machine [8]. That procedure captures settings, saves, databases and logs in one artifact and is the basis for every migration recipe in Practical Guidance [8]. The community Ubuntu guide ships the same idea scoped to saves — `cp -r /home/steam/Zomboid/Saves/ /home/steam/Zomboid/Saves_backup_$(date +%Y%m%d)/` [9].

The minimum restore-grade set for one server, if you cannot take the whole folder, is the three name-keyed pieces: the world folder `Saves/Multiplayer/<name>`, the `Server/<name>*` configuration files, and the account database `db/<name>.db` [4] [10]. A hosting runbook that documents exactly this set also specifies the restore preconditions: server fully stopped, files replaced in both the world folder and the database location, Linux permissions sane (644 files / 755 directories in its example), and the server name identical across the `.ini` file, the SandboxVars file and the world folder — otherwise the server boots a fresh empty world beside your data instead of loading it [10]. The same name-matching requirement is stated independently by a second source [11].

Two admin commands frame the cold/hot distinction: `save` writes the current world state to disk while running, and `quit` saves the world and stops the server [7]. A stopped server is the documented precondition for restore [10]; for taking backups, the stop-first rule and the risk profile of hot copies are examined in Practical Guidance and Claim 3. Hosting-panel backup buttons wrap these same file-level operations — one vendor's documented flow is stop server → restore from the panel's backup list → start server, with selective restore of individual pieces such as the character database [13] — so the procedures in this document apply unchanged to rented servers.

## Moving a world between machines

Within the same build, a world move is a file move. The documented layout is symmetrical across operating systems — the same `Server`, `Saves/Multiplayer` and `db` structure under `%USERPROFILE%\Zomboid` (Windows) or `~/Zomboid` (Linux) — so a Windows→Linux migration is: recreate the tree under the target user's home, keep the server name identical, and start the server [4] [8]. The wiki's Linux install pattern runs the server as a dedicated non-root user (`pzuser`, with `chown pzuser:pzuser` on the install directory), so transplanted files must end up owned by that user or the server process cannot write its own world [4]. The corroborating restore runbook makes the same point as permission bits [10].

Three server-side details commonly break otherwise-clean moves:

- **Name keying.** All four config files, the world folder and the `db` file must carry the same server name on the target; a mismatch yields a generated default world, not an error [4] [10] [11].
- **Client-side map data.** Because each player's map knowledge is stored under a folder keyed to IP, port and a hash, a migration that changes the server's public IP or port silently orphans every player's local map data; the wiki documents the folder shape and the port-reuse carry-over behaviour that follows from it [4].
- **B42-on-a-B41-machine.** A known failure on machines that previously hosted a B41 server is the startup error "Assertion Failed: Illegal termination of worker thread"; the documented fix is to verify `steam_appid.txt` contains only `108600`, back up the `.ini`/Lua/save data you want to keep, then delete the whole `Zomboid` folder and let the B42 server regenerate it — the wiki adds that keeping a local copy of the old folder is cheap insurance *(B42)* [4].

The server binaries themselves are not part of the migration: reinstall them on the target with SteamCMD (`app_update 380870 validate`, or with the `legacy41` beta flag for a B41 world, below) rather than copying the installation across [4].

## The build boundary: no conversion, only branches

The primary record is explicit in both pre-release announcements: "Build 41 savegames clearly will not be compatible with Build 42", and "existing saves on Unstable 42.19 will not be compatible with 42.20" [1] [2]. No migration or conversion tool is offered; `BackupsOnVersionChange` will preserve a pre-update copy of your world when the version changes [5] [12], but nothing converts that copy across the build boundary — its only value there is rollback.

The supported strategy for keeping an old world alive is branch pinning, published ahead of the stable switch so communities could move before being auto-updated [1] [2]:

- **B41 worlds** — clients select the `legacy41` beta under Steam Properties → "Game Versions & Betas"; The Indie Stone framed this as a channel "for you (and your players) to move over to before the event", i.e. server owner and community move together [1] [2]. Dedicated servers pin the same branch in SteamCMD: `app_update 380870 -beta legacy41 validate` [4].
- **42.19 unstable worlds** — a parallel `42.19` beta branch exists for finishing those saves, selected the same way [1] [2].
- **New-world communities** — the default stable branch: 42.20.0 on 2026-07-29 [3], advanced to 42.21 on 2026-09-28 [15].

Build 42.20.1 (2026-08-05) additionally fixed an issue that allowed broken B41 worlds to be hosted on B42 servers, and a case where players switching from B41 to B42 met a missing menu [14]. The post does not describe what made a B41 world "broken" or what a B42 server now does when handed one, so treat it as a guard, not a conversion path: do not point a B42 server at a B41 world deliberately.

A pinned branch must be pinned everywhere: encode the beta flag into your SteamCMD update script so a routine update can never silently hop the server onto stable while your players sit on `legacy41` [4].

## Soft resets: ResetID and ServerPlayerID

Two `.ini` values implement the game's "keep the community, reset the world state" signalling [5]:

| Key | Default | Range | What the reference documents |
|-----|---------|-------|------------------------------|
| `ResetID` | 863866116 | 0–2147483647 | Records whether the server has soft-reset; a client whose stored ID mismatches is forced to roll a fresh character; paired with `ServerPlayerID`; the reference explicitly advises backing these IDs up [5] |
| `ServerPlayerID` | (listed empty in the reference) | — | Identifies whether a character came from another server or singleplayer; can be changed by soft resets; ID mismatch forces a new character; same backup advice [5] |

Operationally that advice means: your backups must include the `.ini` (which carries `ResetID`), because restoring world data under a *different* `ResetID` than the one clients last saw is itself a soft-reset event from the clients' perspective — their characters are invalidated by the mismatch rule the reference describes [5]. This is a synthesis of the cited mismatch behaviour, flagged here rather than silently assumed.

The one documented trigger for an actual soft reset is the `-Dsoftreset` startup parameter — and the pinned startup-parameters reference records it as broken on 42.20.0, with the issue reported for a possible future fix *(B42)* [6]. What a soft reset removes and preserves in-world has no primary documentation at all and is quarantined below (Claim 2). As of 42.20, a working soft reset is effectively not available through documented means; admins wanting a fresh map with retained accounts should plan a world-folder reset instead (Practical Guidance).

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Save-forward compatibility | B41 worlds cannot be carried into B42 — "will not be compatible", no converter [1] [2] | 42.19-unstable saves equally cannot enter 42.20 [1] [2] |
| Keeping the world alive | Pin client and server to the `legacy41` beta branch; SteamCMD `app_update 380870 -beta legacy41 validate` [1] [2] [4] | 42.20 was the stable branch from 2026-07-29 and 42.21 from 2026-09-28; a separate `42.19` branch preserves unstable-era worlds [1] [2] [3] [15] |
| Hosting a B41 world on a B42 server | Not applicable on B41 | Broken B41 worlds could be hosted on B42 servers until the 42.20.1 fix; no conversion exists [14] |
| Update safety statement | Legacy hotfix 41.78.21 (2026-08-26) is a security fix; its post makes no save-specific statement beyond the standard note that updates should not break saves [17] | Saves from 42.20.4 "should not be affected" by 42.21; the studio says to back up first [16] |
| Folder anatomy | Same name-keyed tree (`Server`, `Saves/Multiplayer`, `db`) — continuity implied by the shared instructions and the `legacy41` install path, verified in this document only against 42.20-era revisions [4] | Verified against the 42.20-era Dedicated-server revision [4] |
| `Backups*` / `ResetID` keys | Presence and defaults on B41 not re-verified against a B41-era reference in this document | Documented with defaults and ranges in the 42.20-versioned settings reference [5] |
| Soft-reset trigger | `-Dsoftreset` status on B41 unverified here (the pinned reference records only the B42-era failure) [6] | `-Dsoftreset` documented as non-functional as of 42.20.0 [6] |
| Cross-machine move hazard | Standard path/ownership/name rules [4] [8] [10] | Additional hazard: a B42 server on an ex-B41 machine can fail with the worker-thread assertion; the fix requires backing up configs and deleting the old `Zomboid` folder [4] |
| What a backup can and cannot do | Backups roll a B41 world back on B41 | Backups roll a 42.x world back on 42.x; the automatic version-change backup cannot bridge the B41→B42 or 42.19→42.20 boundaries [1] [2] [5] |

The delta in one line: inside either build, backup and migration mechanics are the same file-level craft; across the build boundary they stop working entirely, and the branch system — not the backup system — is what protects an old world [1] [2] [4].

# Practical Guidance

## Before you update a B42 server

Take a cold backup of the whole `Zomboid` tree first. The studio's own 42.21 note says saves from 42.20.4 should not be affected by 42.21 but tells players to back up first [16]; the automatic `BackupsOnVersionChange` copy is a second layer, not a replacement for an off-machine one [5] [12].

## Daily-driver backup (Linux, cold)

```bash
# 1. Stop the server cleanly (console or RCON) — 'quit' saves the world first
quit

# 2. Archive the whole data tree (config + world + db + logs in one artifact)
tar -czf ~/pz-backup-$(date +%F-%H%M).tar.gz -C ~ Zomboid

# 3. Get it off the machine
scp ~/pz-backup-*.tar.gz backup-host:/srv/backups/pz/
```

`quit` is the documented save-and-stop command [7]; the whole-folder copy is the documented backup unit [8]. Automate the schedule around your restart window — with `BackupsOnStart=true`, every scheduled restart already yields an automatic on-box backup as a second layer [5] [12].

## Daily-driver backup (Windows, cold)

```bat
rem After 'quit' at the server console:
robocopy "%USERPROFILE%\Zomboid" "D:\pz-backups\Zomboid-2026-07-31" /E
```

Same logic, same artifact: the entire `Zomboid` folder [8]. Compressing the folder to a `.zip` before moving it is the wiki's own suggested variant [8].

## Hot copies, honestly

If you cannot stop the server, run the `save` admin command first to flush the world to disk [7], then copy. Treat the result as best-effort: the world folder contains live SQLite databases, the restore procedure's documented precondition is a stopped server, and the corruption risk of copying under write load is community-attested rather than officially characterised (Claim 3) [10]. A hot copy is better than no copy; it is not a substitute for a scheduled cold one.

## Restoring from backup, step by step

1. **Stop the server completely** [10].
2. **Move the current (broken) state aside** — rename `Saves/Multiplayer/<name>` and `db/<name>.db` rather than deleting them; you may want them for forensics [10].
3. **Unpack the backup** and put the pieces back: world folder to `Saves/Multiplayer/<name>`, config files to `Server/`, database to `db/<name>.db` [4] [8] [10].
4. **Check the name keying** — `.ini`, `_SandboxVars.lua`, world folder and `db` file must all carry the same server name, or you will boot a fresh world [4] [10] [11].
5. **On Linux, fix ownership and permissions** — `chown -R pzuser:pzuser ~/Zomboid` (substitute your service user), directories traversable, files writable by that user [4] [10].
6. **Confirm the `.ini` carries the expected `ResetID`** — restoring config from a different era than the world data risks invalidating client characters via the ID-mismatch rule [5].
7. **Start the server and verify** — have one player join and confirm their character and the world state before announcing the all-clear [10].

## Machine-to-machine migration checklist

1. Install the server fresh on the target with SteamCMD — same build branch as the source (`app_update 380870 validate`, or `app_update 380870 -beta legacy41 validate` for a B41 world) [4].
2. Run it once, then stop it — this creates the target `Zomboid` tree and admin-account scaffolding [4].
3. Transfer the archived `Zomboid` folder and overlay it (or at minimum the three name-keyed pieces: world folder, `Server/<name>*` files, `db/<name>.db`) [8] [10].
4. Apply the restore steps above, including ownership on Linux [4] [10].
5. Keep the public IP and port if humanly possible; otherwise warn players their local map discovery will not follow, per the client-side `ip_port_hash` folder keying [4].
6. Re-pin the update script to the correct branch on the new machine before the first routine update [4].

## When you actually want a reset

With `-Dsoftreset` non-functional on 42.20 [6], the practical "new map, same community" play is: cold-stop, back up everything, delete (or archive) `Saves/Multiplayer/<name>` while keeping `Server/<name>*` and `db/<name>.db`, and start the server to regenerate the world. Test on a copy first: how much character state survives a world-folder reset is bound up with the unverified soft-reset folklore in Claim 2, and the `ResetID`/`ServerPlayerID` mismatch rules are the only primary-documented lever [5].

# Common Pitfalls & Troubleshooting

- **Restored the files, got a brand-new world.** Almost always name keying: the server name on the target does not match the world folder / `.ini` / SandboxVars / `db` set you restored [4] [10] [11]. Check `-servername` and the file names character-for-character.
- **Restored on Linux, server can't write or won't load the world.** Files landed owned by root or your admin login instead of the service user; re-`chown` the tree [4] [10].
- **Counted on the automatic backups, can't find them.** The pinned reference documents only the four keys' values, not their output location, and secondary sources disagree about where backups land (Claim 1) [5]. Locate them empirically before you need them.
- **Assumed `BackupsOnVersionChange=true` would carry the world into Build 42.** It cannot; the incompatibility is stated by the primary announcements, and the version-change backup is only a rollback point on the old build [1] [2] [5].
- **Migrated hosts, players "lost the map".** Nothing is lost server-side: their map-discovery data sits on their own disks keyed to your old IP/port [4]. Keep the endpoint stable, or tell players what happened.
- **Updated the server, players left behind on `legacy41` (or vice versa).** The branch pin was not encoded in the update script; the announcements' instruction is to move server and players together [1] [2] [4].
- **B42 server refuses to start on the machine that used to run B41.** The worker-thread assertion; follow the documented fix (verify `steam_appid.txt` = `108600`, back up configs, remove the old `Zomboid` folder) *(B42)* [4].
- **Restored an old `.ini` over a newer world and every client was forced to reroll.** That is the `ResetID`/`ServerPlayerID` mismatch rule doing exactly what the reference says it does; keep config and world backups paired, and back the IDs up as the reference advises [5].

# Community Notes & Unverified Claims

## Claim 1 — Automatic backups are written as zip archives under a backups directory with per-trigger subfolders

- **Claim:** Hosting knowledge bases and Steam-forum answers commonly state that the built-in system writes zip archives beneath a backups directory in the `Zomboid` tree, in subfolders per trigger (start, version change, periodic). One current hosting document instead locates backups as timestamped folders inside `Saves/Multiplayer` [12], and another vendor describes save data being copied into a temporary directory.
- **Why unverified:** The pinned settings reference lists the four `Backups*` keys with defaults and ranges but no description of behaviour or output path [5]; no primary source documents the location, and the secondary sources conflict with each other.
- **Confidence:** Low. The existence of automatic backups is primary-documented via the keys themselves [5], but every on-disk detail (path, subfolders, archive format) is contested between secondaries.

## Claim 2 — A soft reset wipes the world and loot but preserves player characters and skills

- **Claim:** Community explanations circulating in Steam General Discussions (one such thread is footnoted by the wiki's startup-parameters page itself) describe the soft reset as deleting map/world state — building alterations, loot, items on the ground — while keeping accounts and characters, with variation between tellings on whether inventories and safehouses survive.
- **Why unverified:** No primary source describes soft-reset semantics; the pinned references document only the signalling keys (`ResetID`, `ServerPlayerID`) and a trigger parameter that is non-functional as of 42.20.0 [5] [6], which also makes the behaviour untestable on current stable.
- **Confidence:** Low. The claim is B41-era folklore with internal variations, and the mechanism it describes cannot currently be exercised to check it.

## Claim 3 — Copying save files while the server is running risks a corrupt or inconsistent backup, especially the SQLite databases

- **Claim:** Community and hosting guidance consistently instructs stopping the server before copying or restoring saves, on the reasoning that the world folder's character and vehicle databases are live SQLite files and mid-write copies can be internally inconsistent; the corroborating restore runbook makes "stop the server completely" its first step [10].
- **Why unverified:** No primary source characterises the consistency guarantees (or lack of them) of copying a running server's save tree; the stop-first instruction is documented [10], but the corruption mechanism attributed to it is inferred from general SQLite behaviour, not from Project Zomboid documentation.
- **Confidence:** Medium. The advice is uniform across sources and mechanically plausible, and following it costs little; only the stated *reason* lacks a primary source.

# Risks & Caveats

- **The `Backups*` behaviour rests on secondaries.** Defaults and ranges are pinned [5], but units, output location and archive format are hosting-sourced or contested (Claim 1) — the Medium cap applies, and a hotfix or future settings-reference revision could overturn details.
- **B41-side verification is inherited, not direct.** The layout and key facts are verified against 42.20-era page revisions [4] [5] [8]; B41 continuity is asserted from the unchanged workflow, and exact B41 defaults for the backup keys were not independently pinned.
- **The world-folder file inventory is secondary-corroborated.** The chunk-file/character-database/vehicle-database breakdown comes from two agreeing hosting sources [10] [11], not from a primary; first-hand listing (Verification Steps, step 2) should replace this before any High rating.
- **42.20-era behaviours may drift.** The `-Dsoftreset` failure is documented "as of 42.20.0" with a fix possible in future versions [6]; the 42.20.1 to 42.21 notes reviewed (the forum list is a selected abridgement) do not mention it, so its status on 42.21 is unknown rather than fixed or still broken [14] [16]. The settings-reference and Dedicated-server revisions cited were not refreshed against 42.21.
- **Bot-blocked primaries.** The Steam announcement citations were verified through the ISteamNews API mirror per project source policy; the announcement URLs themselves 403 automated checkers (allowlisted as WARN in the link gate).

# Verification Steps

1. **Confirm the incompatibility and branch primaries:** query `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0` and read "B42 CHECKLIST" (2026-07-28) and "BUILD 42 STABLE PLANS" (2026-07-24) for the "will not be compatible" statements and the `legacy41`/`42.19` instructions.
2. **Confirm the tree first-hand:** start a scratch server once, stop it, and list `Zomboid/Server`, `Zomboid/Saves/Multiplayer/servertest`, `Zomboid/db` and `Zomboid/Logs`; inside the world folder, confirm (or refute) the chunk-file and database inventory currently carried on secondary sources.
3. **Locate the automatic backups (resolves Claim 1):** set `BackupsPeriod=5`, run the server past two intervals plus one restart, then search the tree — e.g. PowerShell `Get-ChildItem -Recurse $env:USERPROFILE\Zomboid -Filter *.zip | Sort-Object LastWriteTime` plus a directory diff — and record where start/period backups actually land and in what format.
4. **Verify the keys against the pinned reference:** read `BackupsCount`, `BackupsOnStart`, `BackupsOnVersionChange`, `BackupsPeriod`, `ResetID` and `ServerPlayerID` at the pinned revision (Server settings, oldid 1443167) and compare with a freshly generated `servertest.ini`.
5. **Rehearse the restore runbook:** on a scratch machine, take a cold backup, delete the world folder, restore per the step-by-step, and confirm a client reconnects to the same world with the same character.
6. **Test the `ResetID` mismatch rule:** on a scratch server with one test client, change `ResetID`, restart, and confirm the client is forced to create a new character [5].
7. **Test `-Dsoftreset` on current stable:** launch with the parameter and record the (expected non-)result against the pinned startup-parameters statement [6].

# Open Questions

- Where exactly do the automatic backups land on 42.20/42.21, in what format, and does `BackupsCount` rotate all trigger types in one pool or per trigger? (Claim 1; Verification step 3 resolves it empirically.)
- What are the actual soft-reset semantics in current code, and will the reported `-Dsoftreset` failure be fixed in a post-42.20 hotfix [6]? The notes through 42.21 reviewed here do not say [14] [16]; a full changelog entry or dev post would resolve both.
- Are the `Backups*` defaults identical on legacy41 41.78? A B41-era settings-reference revision or a first-hand `legacy41` server generation would close the delta table's open cell.
- Does the automatic backup system capture the account database and the `Server/` config files, or only the world folder? No source in either tier states its coverage precisely.
- Will The Indie Stone publish official backup/restore guidance for server operators through the GSP feedback channel now that B42 multiplayer is stable [3]?

# References

**Primary Sources**

- [1] **The Indie Stone** — *B42 CHECKLIST* (Steam announcement, 2026-07-28; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839041357038237. Accessed 2026-07-31.
- [2] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-24; retrieved via Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453. Accessed 2026-07-31.
- [3] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [4] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Startup parameters* (revision 1393745). https://pzwiki.net/w/index.php?title=Startup_parameters&oldid=1393745. Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *Admin commands* (revision 1385097). https://pzwiki.net/w/index.php?title=Admin_commands&oldid=1385097. Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *Tech Support* (revision 1442989). https://pzwiki.net/w/index.php?title=Tech_Support&oldid=1442989. Accessed 2026-07-31. Fact-only source.

- [14] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05; B41-world hosting and missing-menu fixes; retrieved via Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [15] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28; retrieved via Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [16] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, selected changes only; 2026-09-23; savegame-safety statement). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.
- [17] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26; retrieved via Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.

**Secondary & Corroborating**

- [9] **Bobagi** — *Project-Zomboid-Ubuntu-Server* (MIT; Ubuntu dedicated-server guide: Linux paths, Logs folder, saves backup command). https://github.com/Bobagi/Project-Zomboid-Ubuntu-Server. Accessed 2026-07-31.
- [10] **Supercraft** — *Project Zomboid: Back Up and Restore Server Save & Player Data* (hosting KB; corroborate-only). https://supercraft.host/wiki/project-zomboid/backup_player_data/. Accessed 2026-07-31.
- [11] **LOW.MS** — *Project Zomboid Save Location & How to Upload Your World* (hosting KB; corroborate-only). https://low.ms/knowledgebase/project-zomboid-save-location-how-to-upload. Accessed 2026-07-31.
- [12] **Wabbanode** — *How to Configure Server Backups on Your Project Zomboid Server* (hosting KB; corroborate-only; source of the minutes/retention descriptions and one of the conflicting location claims). https://wabbanode.com/help/project-zomboid/how-to-configure-server-backups-on-your-project-zomboid-server. Accessed 2026-07-31.
- [13] **XGamingServer** — *How to Back Up and Restore Your Project Zomboid Server* (hosting KB; corroborate-only; panel-level restore flow, including selective restore of the character database). https://xgamingserver.com/docs/project-zomboid/backups. Accessed 2026-07-31.

**Community & Creator**

**Further Reading**

# Further Reading

- The ISteamNews mirror used to verify all primary announcements: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- Valve's SteamCMD documentation (install/branch mechanics referenced by the wiki): https://developer.valvesoftware.com/wiki/SteamCMD
- gorcon/rcon-cli — scriptable RCON client suitable for automating `save`/`quit` around backup jobs: https://github.com/gorcon/rcon-cli

# Related Documents

- `admins-foundation` — the Admins-track overview this runbook deepens (branches, config surfaces, tooling).
- `admins-server-ini-reference` — the key-by-key `server.ini` reference, including the `Backups*` and ID keys in their full context.
- `admins-sandboxvars-reference` — the SandboxVars reference (the `_SandboxVars.lua` file this document tells you to back up).
- `lore-foundation` — what the world you are protecting actually is.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined against 42.20.1, 42.20.4/41.78.21 and 42.21 stable posts plus 42.21 forum notes [14] [15] [16] [17]: current stable 42.21, B41-world hosting guard (42.20.1), update-safety statement, soft-reset status caveat. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
