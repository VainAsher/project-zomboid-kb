---
id: admins-rcon-commands
title: "RCON and Admin Commands: Operating a Live Server"
version: 0.2.0
status: in-review
confidence: Medium
category: Admins
topic: "Server operations"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [admins-foundation, admins-server-ini-reference, admins-sandboxvars-reference, meta-style-guide]
tags: [rcon, admin-commands, server-operations, moderation, rcon-cli, mcrcon, zomboid-rcon, pz-admin, b42, legacy41]
game_versions_verified: ["41.78.16", "42.17.0", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-rcon-commands |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16 (B41 page revision); 42.17.0 (B42 page revision); 42.21 (patch notes reviewed; stable is 42.21) |

# Executive Summary

This document is the operating catalogue for a live Project Zomboid server: every admin command documented on the revision-pinned pzwiki Admin commands page, organized by operational task rather than alphabetically, plus the three routes for issuing those commands — the server console, in-game chat with a leading slash, and RCON — and copy-pasteable invocations for the four open-source RCON tools this knowledge base standardises on (gorcon `rcon-cli`, Tiiffi `mcrcon`, the `zomboid-rcon` Python library, and the pz-admin desktop GUI). It goes one level deeper than `admins-foundation`, which introduced RCON and the tooling landscape at overview level; the per-key `.ini` reference (including the two RCON keys themselves) belongs to `admins-server-ini-reference`.

The command surface is pinned to two wiki revisions: the Build 41 roster at a revision explicitly verified against 41.78.16 (44 documented commands), and the current roster at a revision versioned against 42.17.0 (59 documented commands). Diffing the two pinned revisions yields a concrete delta — 17 commands appear only in the B42-era revision (among them `/banip`, `/teleportplayer`, `/removeitem`, `/reloadalllua`, `/setpassword` and the B42 world-generator control `/worldgen`) and two appear only in the B41-era revision (`/clear`, `/replay`). A load-bearing caveat runs through the whole document: that diff is a *documentation* delta, and how much of it reflects actual game-code change is quarantined rather than asserted.

Document-level confidence is **Medium**. The catalogue rests on pzwiki as a fact-only source, and the current revision is versioned 42.17.0 while the stable build is 42.21 — the 42.20.1-42.21 patch notes fix several admin-command behaviours but do not enumerate the roster, so nothing re-verifies the roster at 42.21. Tooling invocations rest on the tools' own repositories and are stronger; anything that could not be traced to a pinned source (RCON behaviour of self-targeting commands, the `godmod`/`godmode` spelling oddity, mcrcon's fitness for Zomboid) is quarantined below.

# Key Takeaways

- Admin commands run from three places: the server console (bare command name), in-game chat (leading `/`, admin status required), and RCON — configured by `RCONPort` (default 27015) and `RCONPassword` in the server `.ini` *(cited)* *(both)*
- The B41-pinned wiki revision documents 44 commands; the 42.17.0-pinned revision documents 59 — but this is a documentation diff, not a verified game-code diff *(cited; the inference is quarantined)*
- Item, XP, vehicle and horde spawning (`/additem`, `/addxp`, `/addvehicle`, `/createhorde`) all take a target username; item/module identifiers are case-sensitive (`Base.Axe`, not `base.axe`) *(cited)* *(both)*
- Staff tiers are set with `/setaccesslevel`: Admin, Moderator, Overseer, GM, Observer, plus `none` to strip elevated access — the `none` value appears only in the B42-era revision *(cited)*
- Live `.ini` changes are a three-command loop: edit or `/changeoption`, then `/reloadoptions` to re-read and push to clients, then `/showoptions` to confirm *(cited)* *(both)*
- `/quit` saves and stops the server — there is no separate no-save shutdown documented, so treat `/quit` as the only clean stop *(cited)* *(both)*
- For scripted operations use `rcon-cli` (one-shot and interactive, MIT), `mcrcon` (env-var friendly, zlib), `zomboid-rcon` (Python methods plus a raw `command()` escape hatch, GPL-3.0), or pz-admin (GUI over RCON, MIT) *(cited)* *(both)*
- Several documented commands are flagged as work-in-progress on the wiki with raw `UI_ServerOptionDesc_*` placeholder text (`/createhorde2`, `/removezombies`, `/list`, `/remove`, `/addtosafehouse`, `/kickfromsafehouse`) — do not build runbooks on them *(cited)* *(B42)*

# Purpose

This is the day-two operations reference for the Admins track. It answers: what commands exist, what does each actually do, which build documents it, how do I issue commands when I am not sitting at the server console — and which of the popular "facts" about the command surface are actually verifiable? It exists so that an admin can moderate, spawn, teleport, control weather and cycle configuration on a live server without reverse-engineering `/help` output, and so that scripted operations (restart warnings, scheduled saves, mod-update checks) have exact, tool-specific invocations to copy.

# Scope

Covered: the full admin-command roster as documented at two pinned pzwiki revisions (B41-era and B42-era), organized by task; the three command-issuing routes and their differences; RCON client setup and invocations for `rcon-cli`, `mcrcon`, `zomboid-rcon` and pz-admin; the systemd FIFO alternative to RCON on Linux; server startup parameters that shape admin access (`-adminusername`, `-adminpassword`, `-coop`, `-statistic`); and the citable B41 vs B42 command delta.

Not covered: the meaning and ranges of `.ini` keys (owned by `admins-server-ini-reference`, including `RCONPort`/`RCONPassword` semantics), SandboxVars (owned by `admins-sandboxvars-reference`), install/branch/port fundamentals (owned by `admins-foundation`), and the in-game admin panel UI beyond its chat-command surface — the pinned sources document commands, not the panel's widgets. Debug-mode client cheats are out of scope; this is the multiplayer server surface only.

# Definitions

- **Server console** — the interactive console of the running server process (the window opened by the launch scripts); takes bare command names without a slash [2] [4].
- **In-game command** — the same commands typed into the chat panel by a user with admin status, prefixed with `/` [2] [4].
- **RCON** — the password-protected remote-console listener on `RCONPort`, spoken by generic Source-RCON clients; `rcon-cli` lists Project Zomboid among its supported games [5] [7].
- **Access level** — the staff tier attached to an account, set with `/setaccesslevel`; the documented roster is Admin, Moderator, Overseer, GM, Observer and (B42-era revision) `none` [2] [3].
- **Self-targeting command** — a command whose username argument is optional in-game, defaulting to the issuing admin (e.g. `/additem`, `/godmode`, `/createhorde`); the wiki notes for several of these that the username is only optional away from the server console [2].
- **WIP command** — a command row whose wiki description is a raw `UI_ServerOptionDesc_*` localisation key or an explicit WIP marker, i.e. present in the game's command list but not meaningfully documented [2].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Roster from wiki revision 648141, whose page-version tag was checked for 41.78.16 [3] |
| B42 (stable) | Yes | 42.17.0 (page revision); stable is 42.21; 42.20.3-42.21 patch notes reviewed [8] [10] [11] | Roster from wiki revision 1385097, versioned 42.17.0 and carrying the wiki's own staleness banner against 42.20 [1] [2]; 42.21 stable since 2026-09-28 [10] |

Build 42.20.0 became stable on 2026-07-29 [1] and 42.21 on 2026-09-28 [10]. No pinned source re-verifies the command roster at 42.20 or 42.21; every B42 statement below is therefore "as documented at 42.17.0" unless otherwise tagged. **42.21 re-check scope:** the 42.20.3 and 42.21 Steam notes [8] [9] [10] and the TIS forum changelist [11] were read for admin-command changes; the fixes they name are recorded in the per-command notes below, and no added or removed command is named. The roster itself was not re-run against a 42.21 server (`help` dump); unchanged rows are carried forward from the pinned revisions with no contradicting change found, not re-tested. The RCON tooling sections are build-independent: the tools speak to the RCON listener, which both builds expose through the same two `.ini` keys [5].

# Reference

## The three ways to issue a command

The wiki documents two local entry points: the server's own console window accepts admin commands directly, and accounts holding admin status may issue the same commands from in-game chat, where a leading forward slash marks the line as a command [2] [4]. `/help` prints the full command list, and `/help <command>` prints that command's tooltip [2]. Command arguments can be case-sensitive — the wiki's example is that `Base.Axe` works where `base.axe` does not [2]. On Linux installs supervised by the wiki's systemd unit, a third local path exists: commands echoed into the FIFO control socket (`echo "command" > /opt/pzserver/zomboid.control`), with output read back via `journalctl -u zomboid -f` [4]. RCON is the remote fourth path, held open on `RCONPort` (default 27015) behind `RCONPassword` [5].

Admin identity itself is created at first launch — the server prompts for the admin account's password on its first run [4]. Two startup parameters shape this: `-adminusername <name>` makes the server create its default admin under a different name, and `-adminpassword <pass>` supplies the password non-interactively when no default admin exists yet [6]. A `-coop` server disables the default admin account entirely [6]. Further staff accounts are then promoted in-game or from the console with `/setaccesslevel` [2].

## Watching the server

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/players` | Prints the connected-player roster [2] [3] | `players` |
| `/stats` | Switches multiplayer statistics output between off, file, console or both, with a period argument [2] [3] | `/stats console 10` |
| `/log` | Sets the log level per subsystem type [2] [3] | `/log "Network" "Debug"` |
| `/checkModsNeedUpdate` | Checks whether installed Workshop mods are stale; the verdict is written to the log file, not echoed [2] [3] | `checkModsNeedUpdate` |
| `/list` | WIP: the description at the pinned revision is a raw `UI_ServerOptionDesc_List` placeholder *(B42)* [2] | — |

The statistics period can also be fixed at launch: the `-statistic <seconds>` startup parameter enables multiplayer statistics monitoring, saving results under the cache directory's `Statistic` folder [6]. The valid log levels are Trace, Debug, General, Warning and Error [2]. The valid log types at the 42.17.0-pinned revision are [2]:

```text
General, Network, Multiplayer, Voice, Packet, NetworkFileDebug, Lua, Mod,
Sound, Zombie, Combat, Objects, Fireplace, Radio, MapLoading, Clothing,
Animation, Asset, Script, Shader, Input, Recipe, ActionSystem, IsoRegion,
UniTests, FileIO, Ownership, Death, Damage, Statistic, Vehicle, Checksum
```

The B41-pinned revision's type list is identical except that it ends at `Statistic` — `Vehicle` and `Checksum` are documented only at the B42-era revision [2] [3].

## Admission, accounts and whitelist

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/adduser` | Creates a username/password account on a whitelisted server [2] [3] | `/adduser "sasha" "firstpass"` |
| `/removeuserfromwhitelist` | Deletes a username from the whitelist [2] [3] | `/removeuserfromwhitelist "sasha"` |
| `/setpassword` | Resets an account's password *(B42)* [2] | `/setpassword "sasha" "newpass"` |
| `/addsteamid` | Adds a SteamID to the server's allow-list *(B42)* [2] | `/addsteamid "76561198000000000"` |
| `/removesteamid` | Removes a SteamID from that allow-list *(B42)* [2] | `/removesteamid "76561198000000000"` |
| `/setaccesslevel` | Assigns a staff tier to an account [2] [3] | `/setaccesslevel "sasha" "moderator"` |

The access-level roster is Admin, Moderator, Overseer, GM and Observer; the B42-era revision additionally documents `none`, which returns the account to an ordinary player [2] [3]. 42.21 fixed `grantadmin` and `setaccesslevel` failing for a user who is not on the whitelist, and moved a newly created role to the bottom of the role list in the UI *(B42)* [11]. 42.20.3 added administrator access when a server is full *(B42)* [8]. Whether `Open`, `Password` and the whitelist keys admit a player in the first place is `.ini` territory — see `admins-server-ini-reference`.

## Moderation: kick, ban, mute

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/kick` | Disconnects a user; `-r` attaches a reason. The wiki's usage string spells the verb `kickuser` [2] [3] | `/kickuser "griefer01" -r "safehouse griefing"` |
| `/banuser` | Bans an account; `-ip` extends the ban to the IP, `-r` attaches a reason [2] [3] | `/banuser "griefer01" -ip -r "duping"` |
| `/unbanuser` | Lifts an account ban [2] [3] | `/unbanuser "griefer01"` |
| `/banid` | Bans a SteamID directly [2] [3]. Before 42.21 a Steam authentication exploit let players enter dedicated servers without authenticating, which prevented SteamID bans from taking effect; 42.21 fixed it *(B42)* [10] [11] | `/banid 76561198000000000` |
| `/unbanid` | Lifts a SteamID ban [2] [3] | `/unbanid 76561198000000000` |
| `/banip` | Bans an IP address *(B42)* [2] | `/banip 198.51.100.7` |
| `/unbanip` | Lifts an IP ban *(B42)* [2] | `/unbanip 198.51.100.7` |
| `/voiceban` | Blocks or restores a user's voice chat via `-true`/`-false` [2] [3] | `/voiceban "griefer01" -true` |

## Presence, movement and admin powers

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/teleport` | Moves you to a player, or (two-argument form) one player to another; after arrival, wait for the map to stream in [2] [3]. 42.21 lists the two-player form (`teleport "Player1" "Player2"`) as fixed *(B42)* [11] | `/teleport "sasha"` · `/teleport "sasha" "marek"` |
| `/teleportplayer` | Moves one player to another — the explicit two-target form *(B42)* [2] | `/teleportplayer "sasha" "marek"` |
| `/teleportto` | Moves you to absolute x,y,z coordinates [2] [3] | `/teleportto 10500,9300,0` |
| `/godmode` | Toggles invulnerability with `-true`/`-false`; username omitted = yourself. Listed under the name `godmod` — see Claim 3 [2] [3] | `/godmode "sasha" -true` |
| `/godmodeplayer` | The explicit player-targeted invulnerability form, listed as `godmodplayer` *(B42)* [2] | `/godmodeplayer "sasha" -true` |
| `/invisible` | Hides a player (or yourself) from zombies, `-true`/`-false` [2] [3] | `/invisible "sasha" -true` |
| `/invisibleplayer` | The explicit player-targeted invisibility form *(B42)* [2] | `/invisibleplayer "sasha" -true` |
| `/noclip` | Lets the target pass through solid structures; toggles when no value is given [2] [3] | `/noclip "sasha" -true` |

## Spawning: items, XP, vehicles, hordes

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/additem` | Gives an item (`module.item`, optional count) to a player, or to yourself when the username is omitted [2] [3] | `/additem "sasha" Base.Axe 2` |
| `/removeitem` | Strips items of a type from yourself; a count of 0 removes all of them *(B42)* [2] | `/removeitem Base.Axe 0` |
| `/addkey` | Issues a key by key id, with an optional display name, to a player or yourself *(B42)* [2] | `/addkey "sasha" "4471" "Gate key"` |
| `/addvehicle` | Spawns a vehicle by script name at a player or at x,y,z [2] [3] | `/addvehicle "Base.VanAmbulance" "sasha"` |
| `/addxp` | Grants XP as `perkname=amount` [2] [3] | `/addxp "sasha" Woodwork=2` |
| `/createhorde` | Spawns a zombie group of the given size around a player; omitting the username (possible anywhere but the console) centres the horde on you [2] [3] | `/createhorde 80 "sasha"` |
| `/createhorde2` | WIP: raw `UI_ServerOptionDesc_CreateHorde2` placeholder at both pinned revisions [2] [3] | — |
| `/removezombies` | WIP: raw `UI_ServerOptionDesc_RemoveZombies` placeholder at both pinned revisions [2] [3] | — |

## World, weather and scripted events

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/alarm` | Rings a building alarm where the admin is standing; the admin must be inside a room [2] [3] | `alarm` (in-game position matters) |
| `/chopper` | Launches the helicopter event over a randomly chosen player [2] [3] | `chopper` |
| `/gunshot` | Plays a gunshot near a randomly chosen player [2] [3] | `gunshot` |
| `/lightning` | Strikes lightning at a player; the target may only be omitted when not issuing from the console [2] [3] | `/lightning "sasha"` |
| `/thunder` | Rolls thunder at a player; same console-target rule as `/lightning` [2] [3] | `/thunder "sasha"` |
| `/startrain` | Starts rain, with an optional intensity from 1 to 100 [2] [3] | `/startrain 40` |
| `/stoprain` | Ends the rain [2] [3] | `stoprain` |
| `/startstorm` | Schedules a storm, with an optional duration in game hours [2] [3] | `/startstorm 3` |
| `/stopweather` | Cancels active weather [2] [3] | `stopweather` |
| `/worldgen` | Controls the world generator with `start`, `recheck`, `stop` and `status` subcommands; marked WIP *(B42)* [2] | `/worldgen status` |
| `/removemapsymbolsforuser` | Wipes one user's shared map annotations *(B42)* [2] | `/removemapsymbolsforuser "sasha"` |

## Safehouses

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/releasesafehouse` | Surrenders a safehouse you own [2] [3] | `releasesafehouse` |
| `/addtosafehouse` | WIP: raw `UI_ServerOptionDesc_AddToSafehouse` placeholder *(B42)* [2] | — |
| `/kickfromsafehouse` | WIP: raw `UI_ServerOptionDesc_KickFromSafehouse` placeholder *(B42)* [2] | — |

## Lifecycle, configuration and broadcast

| Command | What it does | Invocation |
|---------|--------------|------------|
| `/save` | Forces a world save [2] [3] | `save` |
| `/quit` | Saves the world, then shuts the server down [2] [3] | `quit` |
| `/servermsg` | Pushes a broadcast line to every connected client [2] [3] | `/servermsg "Restart in 10 minutes"` |
| `/changeoption` | Sets one server option to a new value at runtime [2] [3] | `/changeoption PauseEmpty "true"` |
| `/showoptions` | Dumps the current option names and values [2] [3] | `showoptions` |
| `/reloadoptions` | Re-reads the server options from disk and pushes them to connected clients [2] [3] | `reloadoptions` |
| `/reloadlua` | Re-runs one named server-side Lua file [2] [3] | `/reloadlua "filename.lua"` |
| `/reloadalllua` | Re-runs all server-side Lua *(B42)* [2] | `reloadalllua` |
| `/clear` | Clears the server console; documented only at the B41-pinned revision *(B41)* [3] | `clear` |
| `/replay` | Records or plays back a moving player's replay to a file via `-record`/`-play`/`-stop`; documented only at the B41-pinned revision *(B41)* [3] | `/replay "sasha" -record run1.bin` |

The documented live-edit loop for the `.ini` closes through two of these: you may edit and save `servertest.ini` on a running server, make the edit live with `reloadoptions`, and confirm it took with `showoptions` [4]. Per-key semantics live in `admins-server-ini-reference`.

## RCON: reaching the console remotely

The listener is configured entirely by two `.ini` keys — `RCONPort` (default 27015) and `RCONPassword` — documented in the sibling reference; the wiki's settings page tells you to choose a strong password [5]. Project Zomboid appears on the supported-games list of gorcon's `rcon-cli`, a generic Source-RCON client [7], which is the interoperability anchor for everything in this section. Commands over RCON take the console form — the forward slash is documented as the *in-game* prefix, not part of the command name [2] [4].

### rcon-cli (gorcon) — one-shots, sessions, config profiles

MIT-licensed single binary with a Docker image (`outdead/rcon`); flags: `-a/--address host:port`, `-p/--password`, `-T/--timeout` (default 10s), `-c/--config`, `-e/--env` [7]:

```bash
# one-shot command
rcon -a 203.0.113.10:27015 -p 'S3cretRc0n' players

# interactive session (omit the command)
rcon -a 203.0.113.10:27015 -p 'S3cretRc0n'

# profile-based: put servers in rcon.yaml, select with -e
rcon -e zomboid "servermsg \"Restart in 10 minutes\""
```

```yaml
# rcon.yaml
zomboid:
  address: "203.0.113.10:27015"
  password: "S3cretRc0n"
  log: "rcon-zomboid.log"
```

### mcrcon (Tiiffi) — env-var driven, multi-command batches

Zlib-licensed C client implementing Valve's Source RCON protocol; flags: `-H` host, `-P` port, `-p` password, `-t` interactive terminal mode, `-s` silent, `-w N` waits N seconds (1–600) between commands; the `MCRCON_HOST`, `MCRCON_PORT` and `MCRCON_PASS` environment variables supply defaults that flags override [8]. Its documentation is Minecraft-centric — its use against Zomboid rests on the shared protocol and is examined in Claim 2 [8]:

```bash
# batch: warn, wait, save — one process
mcrcon -H 203.0.113.10 -P 27015 -p 'S3cretRc0n' -w 5 \
  "servermsg \"Restart in 10 minutes\"" save

# interactive terminal mode, credentials from the environment
export MCRCON_HOST=203.0.113.10 MCRCON_PORT=27015 MCRCON_PASS='S3cretRc0n'
mcrcon -t
```

### zomboid-rcon (jmwhitworth) — Python automation

GPL-3.0 Python library, installed with `pip install zomboid-rcon`; exposes named methods for common commands (`players()`, `servermsg()`, `kickuser()`, `banuser()`, `adduser()`, `additem()`, `addxp()`, `godmode()`, `teleport()`, `createhorde()`, `save()`, `quit()`, `changeoption()`, `reloadoptions()`, `startrain()`, and more) and a generic `command()` for anything unlisted [9]:

```python
from zomboid_rcon import ZomboidRcon

pz = ZomboidRcon(ip="203.0.113.10", port=27015, password="S3cretRc0n")
print(pz.players())
pz.servermsg("Restart in 10 minutes")
pz.command("checkModsNeedUpdate")   # raw escape hatch for unlisted commands
```

### pz-admin (beyenilmez) — the GUI route

MIT-licensed desktop application for Windows (amd64/arm64) and Linux (amd64), built on Go/Wails with a React front end; it authenticates with RCON credentials and wraps the command surface in UI: an RCON terminal, server-option editing and export, player roster management (ban/kick/teleport/access levels), item/XP/vehicle grants, whitelist management, broadcast messages, weather and random events, world save and server stop [10].

### The FIFO alternative (Linux, local only)

Where the wiki's systemd unit is in use, the control socket substitutes for RCON on the box itself: `echo "players" > /opt/pzserver/zomboid.control` issues the command, and `journalctl -u zomboid -f` tails the reply — with the caveat, inherited from `admins-foundation`, that the developers explicitly discourage systemd management [4].

# B41 vs B42 Delta

The citable delta is a *documented-roster* delta between two pinned revisions of the same page: revision 648141 (page-version tag checked for 41.78.16; 44 commands) and revision 1385097 (versioned 42.17.0; 59 commands) [2] [3]. How much of it is real game-code change is deliberately quarantined in Claim 1.

| Delta | Detail |
|-------|--------|
| Documented only at the B42-era revision (17) | `addkey`, `addsteamid`, `addtosafehouse`, `banip`, `godmodplayer`, `invisibleplayer`, `kickfromsafehouse`, `list`, `reloadalllua`, `remove`, `removeitem`, `removemapsymbolsforuser`, `removesteamid`, `setpassword`, `teleportplayer`, `unbanip`, `worldgen` [2] [3] |
| Documented only at the B41-era revision (2) | `clear` (console clear), `replay` (player replay record/playback) [3] |
| `/log` types | The B41-era type list ends at `Statistic`; the B42-era revision appends `Vehicle` and `Checksum` [2] [3] |
| `/setaccesslevel` roster | Five tiers at the B41-era revision; the B42-era revision adds `none` as the strip-access value [2] [3] |
| `/worldgen` | The world-generator control quartet (`start`/`recheck`/`stop`/`status`) exists only at the B42-era revision, consistent with world generation being a Build 42 system [2] |
| `/help` documentation | The B41-era revision's `help` row is a bare placeholder; the B42-era revision documents `/help` and `/help <command>` behaviour (the intro paragraph documents the same usage at both revisions) [2] [3] |
| RCON surface | Unchanged in kind: both builds expose the listener through the same two `.ini` keys; the settings revisions differ only in prose, per the sibling reference [5] |

Operationally: a B41 (`legacy41`) runbook loses `/replay` and `/clear` nothing else from this catalogue, and must not rely on the 17 B42-documented entries without first-hand testing; a B42 runbook gains explicit two-target forms (`teleportplayer`, `godmodplayer`, `invisibleplayer`), IP-level bans, `removeitem`/`addkey`, whole-Lua reloads and `worldgen` — several still WIP-flagged [2] [3].

# Practical Guidance

- **Script the restart ritual, don't type it.** The canonical sequence — `servermsg` warning, wait, `save`, `quit` — is exactly what `mcrcon -w` batching or a three-line `rcon-cli` script does reliably at 4 a.m. when you won't. Supervise the process (tmux/screen per the foundation doc) so `quit` is followed by a controlled relaunch.
- **Send bare command names over RCON.** The slash is chat syntax. If a tool seems to accept `/players`, treat that as tool tolerance, not a contract.
- **Keep one RCON tool per job.** `rcon-cli` with an `rcon.yaml` profile per server for humans and cron; `zomboid-rcon` where the logic needs Python (restart schedulers, Discord bridges — use `command()` for anything without a method); pz-admin when a moderator needs point-and-click power without console access. All three authenticate against the same two `.ini` keys, so credentials rotate in one place.
- **Bind RCON tightly.** The listener is password-only; prefer localhost or a private network for `RCONPort` and keep `RCONPassword` long and unshared — the settings source itself says to pick it strong. Key details belong to the sibling `.ini` reference.
- **Use the explicit player-targeted forms in scripts** (`teleportplayer`, `godmodeplayer`, `invisibleplayer` on B42): the self-targeting defaults are ambiguous away from an in-game avatar, and three commands are already documented as console-constrained (Claim 4 covers the generalisation).
- **Verify every config change you make live.** `/changeoption` or an `.ini` edit is not done until `reloadoptions` has run *and* `showoptions` prints the value you expect — that loop is the only documented live path, and it covers the `.ini` only, not SandboxVars.
- **Treat WIP-flagged commands as unavailable.** Placeholder-described entries (`createhorde2`, `removezombies`, `list`, `remove`, safehouse add/kick) have no documented syntax to be wrong about; if you need the behaviour, test on a scratch server and write down what you find.
- **Quote arguments the way the sources do**: usernames and multi-word values in double quotes, item and vehicle identifiers with exact case (`Base.Axe`, `Base.VanAmbulance`). Over the shell, wrap whole commands in single quotes or escape the inner doubles, as the invocation blocks above show.
- **Log first, moderate second.** Set `-statistic` at launch or `/stats file <period>` early, and raise `/log` levels per subsystem (e.g. `Network` to `Debug`) only while diagnosing — the type list is long, and blanket debug logging is noise you will pay for at incident time.

# Common Pitfalls & Troubleshooting

- **`additem` from RCON without a username.** The self-target default assumes an in-game "you"; the wiki constrains three commands to explicit targets from the console, and the safe operating rule is to always name the target from RCON (Claim 4) [2].
- **`/kick` fails while `/kickuser` works, or vice versa.** The pinned revisions list the command as `kick` but write the usage as `/kickuser` [2] [3]; try the other verb before concluding the player is unkickable.
- **`godmode` vs `godmod` confusion.** Same pattern: the page lists `godmod`/`godmodplayer` with `/godmode`/`/godmodeplayer` usage strings and flags the rows as bugged [2]; Claim 3 tracks the both-spellings report.
- **Case-sensitivity bites item grants.** `base.axe` fails where `Base.Axe` succeeds [2]; when an `/additem` silently does nothing, check capitalisation before checking the item id.
- **`checkModsNeedUpdate` "returns nothing".** It reports into the log file, not to your session [2] [3]; tail the server log (or journalctl under systemd [4]) for the verdict.
- **Editing `servertest.ini` live and skipping `reloadoptions`.** The documented flow is save-then-reload; without the reload the running server keeps its in-memory values [4].
- **Expecting `/reloadoptions` to apply SandboxVars.** The command is documented against the server options file only [2] [4]; sandbox rules follow the restart discipline in `admins-foundation` and `admins-sandboxvars-reference`.
- **Teleporting and walking into the void.** The teleport documentation says to wait for the map to appear after arrival [2] [3]; give chunk streaming a beat before moving, especially over RCON-triggered teleports of other players.
- **Running B41 runbooks against B42 WIP commands (or vice versa).** Two commands are documented only at the B41-era revision and seventeen only at the B42-era one [2] [3]; check the delta table before porting automation across the branch split.
- **RCON timeouts on slow commands.** `rcon-cli` defaults to a 10-second dial/execute timeout [7]; raise `-T` before assuming the server is down when a heavy command stalls.

# Community Notes & Unverified Claims

## Claim 1 — The 17 commands documented only at the B42-era revision are not all new in Build 42

- **Claim:** Community references and older server guides describe several of the "B42-only documented" commands (notably `banip`, `unbanip`, `teleportplayer`, `godmodplayer`, `invisibleplayer`, `setpassword`) as already present on Build 41 servers; the wiki page simply under-documented B41, having been assembled from a Multiplayer FAQ table in 2024 and substantially expanded in 2026.
- **Why unverified:** No primary changelog enumerates admin-command additions per build, and the B41-era revision was verified as a *page*, not as an exhaustive roster; absence from it is weak evidence of absence from the game.
- **Confidence:** Medium. The documentation diff itself is certain [2] [3]; treating it as a game-code diff is the unverified step, and for `worldgen` (a B42 system) the inference is strong while for the moderation commands it is weak.

## Claim 2 — mcrcon works against Project Zomboid's RCON

- **Claim:** Server communities routinely use Tiiffi's mcrcon for Zomboid restart/backup scripts, on the reasoning that mcrcon implements Valve's Source RCON protocol [8] and Zomboid's RCON accepts Source-RCON clients (as evidenced by gorcon listing the game [7]).
- **Why unverified:** mcrcon's own documentation names only Minecraft [8], and no pinned primary states protocol-level compatibility between mcrcon specifically and the Zomboid listener.
- **Confidence:** Medium. Two independently cited facts make the compatibility highly plausible, but the end-to-end pairing is community practice, not a documented contract.

## Claim 3 — Both the `godmod` and `godmode` spellings are accepted by the command parser

- **Claim:** Wiki editors report that both spellings "oddly enough" work, which is why the page lists `godmod`/`godmodplayer` while the usage strings read `/godmode`/`/godmodeplayer`, with the rows flagged as bugged [2].
- **Why unverified:** The both-spellings statement surfaces only in wiki edit-history commentary, not in the page content of either pinned revision and not in any primary source.
- **Confidence:** Low. The name/usage mismatch is documented [2]; the claim that the parser accepts both forms is single-sourced hearsay until tested (see Verification Steps).

## Claim 4 — Over RCON, every self-targeting command requires an explicit username, and position-dependent commands are in-game only

- **Claim:** Admin guides generalise that commands defaulting to "yourself" (`additem`, `godmode`, `invisible`, `removeitem`) must be given explicit targets from RCON or the console, and that commands acting on the admin's physical position (`alarm`) are meaningless without an in-game avatar.
- **Why unverified:** The pinned revisions state the console constraint only for `createhorde`, `lightning` and `thunder` ("optional except from the server console") and the in-room requirement only for `alarm` [2] [3]; the blanket generalisation to all self-targeting commands is not documented.
- **Confidence:** Medium. The documented cases establish the mechanism and the generalisation follows the same logic, but it remains an extrapolation.

# Risks & Caveats

- **The B42 roster is pinned behind stable.** Revision 1385097 is versioned 42.17.0 while stable is 42.21 [2] [10]; 42.18–42.21 may have added, removed or fixed commands without this document knowing. The 42.21 notes also record a fix for players being kicked when executing a server command [11], and the anti-cheat system was expanded in 42.21 [9] [11], so command behaviour on hardened servers may differ from the pinned page.
- **Documentation delta ≠ game delta.** The headline B41/B42 comparison inherits Claim 1's caveat wholesale; do not cite this document for "command X was added in Build 42" beyond `worldgen`-class inferences.
- **Placeholder rows conceal real behaviour.** Six-plus commands carry raw localisation keys as their only description [2]; their actual syntax on a live server is unknown to the pinned sources.
- **Tool facts are repo-README facts.** Flags, method lists and licenses for the four tools were read from their repositories on the access date [7] [8] [9] [10]; releases after that date can change invocations.
- **pzwiki is fact-only.** All command semantics here are re-expressed, and the two pinned revisions carry the wiki's own inaccuracy banners; a stale wiki row would propagate here.

# Verification Steps

1. **Roster ground truth:** on a running server (each branch), issue `help` at the console and diff the returned list against this document's tables; that single step resolves Claim 1 empirically per build.
2. **Pinned-revision check:** open `https://pzwiki.net/w/index.php?title=Admin_commands&oldid=1385097` and `...&oldid=648141` and confirm the rosters counted here (59 and 44 command rows).
3. **RCON interop:** set `RCONPort`/`RCONPassword`, then run `rcon -a 127.0.0.1:27015 -p <pass> players` [7] and the same via `mcrcon -H 127.0.0.1 -P 27015 -p <pass> players` [8]; matching output resolves Claim 2 for your build.
4. **Spelling bug:** from the console, run `godmod "name" -true` and `godmode "name" -true`; whichever succeeds resolves Claim 3.
5. **Self-target behaviour over RCON:** issue `additem Base.Axe 1` (no username) via RCON and observe the response; repeat with an explicit username. This resolves Claim 4 for the item path.
6. **Live-reload loop:** change a benign `.ini` value, run `reloadoptions`, confirm with `showoptions` [4].
7. **Log-file commands:** run `checkModsNeedUpdate` and verify the answer lands in the server log, not the session [2].

# Open Questions

- What did 42.18–42.21 change in the command surface beyond the fixes named in the 42.21 notes [11]? A wiki re-verification or a `help` dump on a 42.21 server would close the gap [1] [2].
- What are the real syntaxes of the WIP-flagged commands (`createhorde2`, `removezombies`, `list`, `remove`, `addtosafehouse`, `kickfromsafehouse`) [2]? First-hand `/help <command>` output on 42.20 would document them.
- Were `clear` and `replay` actually removed from the B42 server, or merely dropped from the page [2] [3]? A `help` dump on 42.20 answers it.
- Does the B42 anti-cheat rework [1] constrain any admin commands (e.g. item grants tripping server-side item checks) on hardened servers?
- Is there an official statement of Zomboid's RCON protocol version/compliance, which would upgrade Claim 2 out of quarantine?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [8] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895. Accessed 2026-10-07.
- [9] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [10] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [11] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post 2026-09-23; multiplayer list abridged to selected items in the retrieved copy). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [2] **PZwiki** — *Admin commands* (revision 1385097; page versioned against 42.17.0, current stable 42.20.0). https://pzwiki.net/w/index.php?title=Admin_commands&oldid=1385097. Accessed 2026-07-31. Fact-only source.
- [3] **PZwiki** — *Admin commands* (revision 648141; page-version tag 41.78.16, B41-era roster). https://pzwiki.net/w/index.php?title=Admin_commands&oldid=648141. Accessed 2026-07-31. Fact-only source.
- [4] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Startup parameters* (revision 1393745). https://pzwiki.net/w/index.php?title=Startup_parameters&oldid=1393745. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [7] **gorcon** — *rcon-cli* (MIT; Source RCON CLI listing Project Zomboid support; flags, rcon.yaml profiles, Docker image `outdead/rcon`). https://github.com/gorcon/rcon-cli. Accessed 2026-07-31.
- [8] **Tiiffi** — *mcrcon* (zlib license; C client for Valve's Source RCON protocol; flags and `MCRCON_*` environment variables). https://github.com/Tiiffi/mcrcon. Accessed 2026-07-31.
- [9] **jmwhitworth** — *zomboid_rcon* (GPL-3.0; Python RCON library, PyPI package `zomboid-rcon`; named command methods plus generic `command()`). https://github.com/jmwhitworth/zomboid_rcon. Accessed 2026-07-31.
- [10] **beyenilmez** — *pz-admin* (MIT; Go/Wails + React desktop RCON admin app for Windows/Linux). https://github.com/beyenilmez/pz-admin. Accessed 2026-07-31.

**Community & Creator**

**Further Reading**

# Further Reading

- The Steam news API mirror used to verify the stable-release announcement: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- gorcon's underlying Go RCON protocol library: https://github.com/gorcon/rcon
- The `zomboid-rcon` package page on PyPI: https://pypi.org/project/zomboid-rcon/
- pz-admin's website with packaged downloads: https://beyenilmez.github.io/pz-admin/

# Related Documents

- `admins-foundation` — the parent overview: branches, ports, RCON keys in context, tooling landscape at survey level.
- `admins-server-ini-reference` — the per-key `.ini` reference, including `RCONPort`/`RCONPassword` semantics and everything `/changeoption` can touch.
- `admins-sandboxvars-reference` — the gameplay-rule surface that admin commands deliberately cannot live-reload.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed 42.20.3 [8], 42.21 unstable [9] and stable [10] Steam notes and the TIS forum changelist [11]; added admin-command fix notes (teleport, grantadmin/setaccesslevel, SteamID bans), scope statement; roster not re-run on 42.21. | — |
