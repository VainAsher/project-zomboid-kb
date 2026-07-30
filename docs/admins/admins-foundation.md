---
id: admins-foundation
title: "Running a Project Zomboid Dedicated Server: Architecture, Branches and Hosting Choices"
version: 1.0.1
status: approved
confidence: Medium
category: Admins
topic: "Server foundations"
build: both
document_type: overview
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [modders-foundation, players-foundation, creator-foundation, lore-foundation, meta-style-guide]
tags: [dedicated-server, steamcmd, rcon, hosting, server-ini, sandboxvars, b42, legacy41]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-foundation |
| Version | 1.0.1 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 41.78.16, 42.20 |

# Executive Summary

A Project Zomboid dedicated server is a headless Java game-server process, distributed free of charge as Steam App ID 380870 and installable with an anonymous SteamCMD login on Windows or Linux [7]. This document is the foundation of the Admins track: it maps what the server is, which build branches exist and why build matching matters, where the configuration lives (`servertest.ini` vs `servertest_SandboxVars.lua`), which ports must be open, how memory is sized, how mods are wired in, and what the open-source admin tooling landscape looks like. Deeper Admins-track runbooks (installation step-by-step, settings reference, RCON operations, mod management) will hang off this overview.

The operational headline of mid-2026 is the branch split. Build 42.20 became the stable public build on 2026-07-29, the first stable release of Build 42 and the first stable build with B42 multiplayer [1] [2]. Communities that want to stay on Build 41.78 — whose saves cannot migrate — move server and players together to the `legacy41` Steam beta branch [2] [3]. Build 42's multiplayer, restored in unstable 42.13 (2025-12-11), arrives at stable with a reworked, re-enabled anti-cheat and item-handling logic moved server-side, which changes both the security posture and the resource profile of a B42 server [1] [5] [6].

Document-level confidence is **Medium**: the branch, port, file-layout and anti-cheat spine rests on official announcements and current pzwiki revisions (High), but the hardware-sizing numbers that admins most want — RAM per player tier and CPU single-thread behaviour — exist only in hosting-company and community sources with conflicting values, and are quarantined below rather than stated as fact.

# Key Takeaways

- The dedicated server is a free Steam tool: SteamCMD App ID **380870**, installed with `login anonymous` — no game purchase is needed on the host account *(cited)* *(both)*
- Build 42.20 is the stable branch since 2026-07-29; B41 communities run `app_update 380870 -beta legacy41 validate` and keep their players on the `legacy41` client beta — server and clients must be on the same build *(cited)*
- Two config surfaces per server name: `servertest.ini` (server/network/mod settings) and `servertest_SandboxVars.lua` (gameplay rules), plus spawnpoint and spawnregion Lua files, all under `Zomboid/Server` in the server user's home directory *(cited)* *(both)*
- Open **UDP 16261 and 16262** to the internet; RCON listens separately on `RCONPort` (default 27015) guarded by `RCONPassword` *(cited)* *(both)*
- Memory is set with JVM `-Xms`/`-Xmx` flags; the B42 `StartServer64.bat` ships with a 16 GB default you **must** edit down or the server can fail to start *(cited)* *(B42)*
- The claim that B42 needs roughly +2 GB RAM over B41 at each player tier is hosting-company sourced and inconsistent between vendors — treat it as planning folklore, not fact *(community, unverified)*
- 42.20 reworked and re-enabled anti-cheat, moved item anti-cheat server-side, and fixed item-spawning/XP/foraging exploits — B42 servers police more logic server-side than B41 did *(cited)* *(B42)*
- Prefer open-source RCON tooling (pz-admin, zomboid-rcon, rcon-cli) over hosting-panel lock-in; all three are maintained, permissively or copyleft licensed, and work against any PZ server *(cited)* *(both)*
- Mods are wired with the dual list `WorkshopItems=` (Workshop IDs) plus `Mods=` (mod loading IDs); the widely repeated B42 backslash-prefix convention for `Mods=` entries has no primary source and conflicting secondary ones *(community, unverified)*

# Purpose

This is the first document a server administrator should read in this knowledge base. It answers: what process am I actually running, which build branch should my community be on, where do I change things, what must be open on the network, how big a machine do I need (and how much of the popular sizing advice is actually verifiable), and which tools should I administer with? It is a map, not a runbook — the deeper Admins-track documents carry the copy-pasteable procedures.

# Scope

Covered: the dedicated server as a distribution and a process; SteamCMD installation at overview level; the stable/`legacy41`/`42.19` branch picture and build matching; the configuration file surfaces and how changes are applied; required ports and RCON; memory sizing mechanics and the state of the evidence on RAM/CPU requirements; Build 42's server-side/anti-cheat shift; self-hosting (Ubuntu-first) versus managed hosting; the open-source admin tooling landscape; and mod wiring basics.

Not covered: a full step-by-step install runbook, the per-setting `server.ini` and SandboxVars reference, admin command and RCON operation catalogues, backup/migration procedures, and performance tuning — each is a deeper Admins-track document. Player-facing Build 42 changes are in `players-foundation`; mod development is in `modders-foundation`. Unstable-branch behaviour after 42.20 is out of scope.

# Definitions

- **Dedicated server** — the standalone headless server distribution of Project Zomboid (Steam App ID 380870), as opposed to the in-client "Host" option that runs a server inside a player's game session [7].
- **SteamCMD** — Valve's command-line Steam client, used to install and update server files with an anonymous login [7].
- **`servertest`** — the default server name; config files and the save folder are named after the server name, so `servertest.ini`, `servertest_SandboxVars.lua`, etc. [7] [8].
- **SandboxVars** — the Lua file of gameplay-rule settings (loot, zombies, world clock) for a server, distinct from the `.ini` server settings [7] [8].
- **RCON** — remote console: a password-protected network interface for issuing admin commands to the running server from external tools [8] [13].
- **`legacy41`** — the Steam beta branch (client and server) that keeps Build 41.78 installed after Build 42 became the default stable build [2] [7].
- **GSP** — game server provider; a company renting managed game servers. The Indie Stone runs a feedback channel for medium-to-large Zomboid GSPs [4].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Server reachable via `app_update 380870 -beta legacy41 validate` [7]; B41-only values tagged *(B41)* |
| B42 (stable) | Yes | 42.20 | Stable since 2026-07-29 [1] [2]; B42-only values tagged *(B42)* |

The pzwiki pages cited for the file layout, ports and settings are versioned against 42.20.0 [7] [8]. The same surfaces (App ID, ports, file names, dual mod lists) existed on B41, but this document's wiki verification is against the B42-era page revisions; where a value is only confirmed for one build it is tagged inline.

# Reference

## What the dedicated server is

The dedicated server hosts Project Zomboid multiplayer on either Windows or Linux [7]. It is a Java process — the launch scripts invoke `java` against the `zombie.network.GameServer` class with JVM arguments for memory and native libraries [7]. On Windows the install ships three launch scripts: `StartServer32.bat`, `StartServer64.bat` and `StartServer64_nosteam.bat`; on Linux the equivalent is `start-server.sh`, with a `-nosteam` argument for hosting non-Steam (e.g. GOG) players [7]. On first launch the server prompts for an admin-account password, then generates default config and world data [7]. Servers running in non-Steam mode require clients to also run non-Steam, via the `-nosteam` launch option [7].

## Getting the server: Steam and SteamCMD

There are two supported install paths: the "Project Zomboid Dedicated Server" tool in the Steam library's tools section, or SteamCMD [7]. The SteamCMD sequence is `force_install_dir <path>`, then `login anonymous`, then `app_update 380870 validate` — the server is App ID 380870 and needs no owned account [7]. The pzwiki Linux instructions (versioned 42.20.0) are Debian/Ubuntu-first: install `steamcmd` from apt, create a dedicated non-root `pzuser`, install to `/opt/pzserver`, and drive updates from a reusable `update_zomboid.txt` SteamCMD script [7]. The community-maintained Bobagi guide follows the same shape for Ubuntu 22.04/24.04 LTS — UFW firewall rules, a dedicated Steam user, SteamCMD install of App 380870, and `screen` for a persistent console session [14]. The wiki warns against launching the server through the Steam client UI; if that happens, file integrity should be re-verified [7].

## The branch picture: 42.20 stable, legacy41 and 42.19

Build 42.20.0 was released to the stable branch on 2026-07-29 [1]. Build 41 savegames are not compatible with Build 42, and The Indie Stone's guidance to B41 server owners and their players is to opt into the `legacy41` beta branch — client side via Steam Properties → "Game Versions & Betas" → `legacy41`, and server side by adding the beta flag to the SteamCMD update command: `app_update 380870 -beta legacy41 validate` [2] [3] [7]. A separate `42.19` beta branch exists for finishing unstable-era 42.19 saves, which are likewise incompatible with 42.20 [2].

Build matching between server and clients is enforced in two ways: operationally, the checklist post tells server owners to move themselves "(and your players)" to the branch together before the switch date, because a community split across builds cannot play together [2] [3]; and mechanically, the `DoLuaChecksum=true` server setting kicks clients whose game files do not match the server's [8].

## Configuration surfaces: server.ini vs SandboxVars

Four files define a server's configuration, all named after the server name (default `servertest`) and stored in the server user's home directory — `%USERPROFILE%\Zomboid\Server` on Windows, `~/Zomboid/Server` on Linux [7] [8]:

| File | Governs | Cited at |
|------|---------|----------|
| `servertest.ini` | Server, network, security and mod settings (ports, RCON, `Mods=`, `WorkshopItems=`, anti-cheat toggles, PVP, whitelist behaviour) | [7] [8] |
| `servertest_SandboxVars.lua` | Gameplay sandbox rules (the option space players know from sandbox mode) | [7] [8] |
| `servertest_spawnpoints.lua` | Custom spawn points | [7] |
| `servertest_spawnregions.lua` | Which named regions players may spawn in | [7] |

If these files do not exist on startup, the server generates them with defaults [7]. Settings can be edited either through the game client's Host → Manage Settings editor (saving under the name `servertest`) or directly in a text editor [7]. Two admin commands close the loop: `showoptions` prints the live option values, and — for `servertest.ini` specifically — the wiki documents that edits can be saved while the server runs and applied with the `reloadoptions` admin command [7]. No equivalent live-reload is documented for SandboxVars; the widely circulated blanket rule "always stop the server before editing config" is examined in the quarantine section (Claim 4). Renaming a server (`-servername`) switches which `.ini`/Lua set and which save folder is used [7] [9].

## Ports and RCON

Two UDP ports must be reachable by clients: 16261 (the default port, `DefaultPort=16261`) and 16262 (the direct-connection port, `UDPPort=16262`) [7] [8]. On a Linux host with UFW, that is `sudo ufw allow 16261/udp` and `16262/udp` followed by a reload [7]. Each additional server instance on the same machine needs its own pair of free UDP ports [7]. A `UPnP=true` option can attempt automatic port mapping on home gateways, falling back to defaults on failure [8]. Both ports can also be overridden at launch with the `-port` and `-udpport` startup parameters [9].

RCON is separate from the game ports: `RCONPort` (default 27015) with `RCONPassword`, which the settings reference tells you to pick strong [8]. Standard Source-RCON-protocol tools interoperate with it — the gorcon `rcon-cli` project lists Project Zomboid among its supported games [13]. Admin commands can equally be issued at the server console, or in-game with a leading `/` by users holding admin access [7].

## Memory: how it is set, and what is actually documented

Server heap size is controlled by the JVM `-Xms` (initial) and `-Xmx` (maximum) flags in the launch script — the same mechanism as the client's launch options [7] [9]. Two documented facts anchor sizing *(B42, wiki page versioned 42.20.0)*: the shipped `StartServer64.bat` specifies 16 GB by default, and the wiki warns that `-Xms`/`-Xmx` **must** be edited down to fit the machine's real RAM — oversized values stop the server from launching at all, exiting with memory errors [7]. The wiki's worked example runs a server at 6 GB [7]. This launch-script value is equivalent to the "Server Memory" option in the in-client Host screen [7]. The Ubuntu community guide configures the same limits via `ProjectZomboid64.json` [14]. Beyond these mechanics, The Indie Stone publishes no RAM-per-player table for either build; every such table in circulation is hosting-company or community material, and the popular "+2 GB for B42" figure is quarantined below (Claim 1).

## Multiplayer scale and Build 42's server-side shift

When B42 multiplayer shipped in unstable 42.13 (2025-12-11), it was explicitly work-in-progress for stress testing: the release guidance was to prefer Steam co-op or whitelisted servers, keep dedicated servers to at most 20 player slots "for now", disable mods (even client-side ones), and avoid debug mode during MP sessions [5] [6]. Those are unstable-era operating limits, published for 42.13 and not re-stated (either as still-current or as lifted) in the 42.20 release notes [1] [5].

At stable, 42.20's release notes describe a security-hardened server: anti-cheats were "Re-Worked and Re-Enabled"; the `antiCheatItem` mechanism was "removed as now server-side"; anti-cheat logging was improved and false positives fixed; and a series of exploits was closed — arbitrary item spawning, illegal XP gains, foraging manipulation, and a hole that let clients duplicate a dedicated server's map data *(B42)* [1]. The current server-settings reference exposes a family of `AntiCheat*` toggles — among them checksum, hit, no-clip, packet-exception, permission, player, safehouse, safety, speed and XP checks — alongside a `SteamVAC` switch *(B42, page versioned 42.20.0)* [8]. 42.20 also added server-operator conveniences: a "Show coordinates" server option, ZNet/packet-logging improvements, object-pool statistics for monitoring, and fixes for server hangs during chunk generation and for map-visited data not persisting across restarts [1]. The community claim that this server-side shift makes B42 meaningfully heavier on CPU than B41 is quarantined below (Claim 3).

## Mod wiring basics

Mods are declared in `servertest.ini` on two paired lists: `WorkshopItems=` carries the Steam Workshop item IDs the server should download, semicolon-separated (the reference example is `WorkshopItems=514427485;513111049`), and `Mods=` carries the mod loading IDs — the internal IDs found in each mod's `info.txt` under the Workshop content folder [7] [8]. The wiki's workflow is: collect the mods in a Workshop collection, extract the paired IDs (it points to a community ID-grabber tool), then paste them into the two lists [7]. Workshop mods added to a server are downloaded automatically by connecting clients [7]. On B42, mods themselves use the new versioned folder layout (a mandatory `common/` folder plus `42.x` version folders) rather than B41's flat `media/` layout, which is why B41-era mods needed restructuring for B42 servers *(B42)* [10]. The claimed B42-only backslash prefix on `Mods=` entries could not be verified against any primary source and is quarantined below (Claim 2).

## The admin tooling landscape

Three open-source tools cover most day-two administration without tying you to a hosting panel:

| Tool | What it is | License | Notes |
|------|-----------|---------|-------|
| pz-admin (beyenilmez) | Desktop app (Windows/Linux) managing servers over RCON: terminal, server options, player management, bans, XP/items/vehicles, world save | MIT | Actively developed [11] |
| zomboid-rcon (jmwhitworth) | Python library (`pip install zomboid-rcon`) wrapping PZ RCON with 30+ command methods for scripting and bots | GPL-3.0 | On PyPI [12] |
| rcon-cli (gorcon) | Generic Source-RCON CLI with explicit Project Zomboid support; single binary, Docker image | MIT | Fits cron jobs and CI [13] |

For process supervision on Linux, the wiki documents a systemd unit + FIFO socket pattern but notes that the developers explicitly discourage systemd management — the in-place shutdown safeties should save the world, but there are no guarantees — and its own baseline instructions use tmux instead [7]. The Ubuntu community guide uses `screen` for the same purpose [14].

## Self-hosting vs managed hosting

Self-hosting is fully supported by the free server distribution and first-class Linux instructions [7] [14]. Managed hosting outsources the machine but not the knowledge: every surface in this document (branch selection, `.ini`/SandboxVars, mod lists, RCON) still has to be operated, typically through the vendor's panel. The Indie Stone signalled at the stable release that it is engaging game server providers directly — medium-to-large GSPs are invited to a feedback channel via `it@theindiestone.com` — which is the closest thing to an official hosting-ecosystem programme [4]. Hosting-company knowledge bases are useful procedure mirrors but are marketing-adjacent; this knowledge base treats their numbers as corroborate-only (see Claims 1 and 3).

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Branch | Served from the `legacy41` beta branch; installed with `app_update 380870 -beta legacy41 validate` [2] [7] | Default stable branch since 2026-07-29 [1] [2] |
| Saves & matching | B41 worlds live only on `legacy41`; server and players must move branch together [2] [3] | B41 and 42.19-unstable saves cannot migrate to 42.20 [2] |
| Multiplayer maturity | Long-stable MP [2] | MP restored in unstable 42.13 (2025-12-11) with a 20-player-slot advisory and mods-off guidance; first stable MP in 42.20 [1] [5] [6] |
| Anti-cheat | B41-era anti-cheat model | Anti-cheat reworked and re-enabled at 42.20; item anti-cheat moved server-side; item-spawn/XP/foraging exploits and a map-data-copy exploit fixed [1] |
| Server-side surface | Fewer server-side checks | `AntiCheat*` toggle family (checksum, speed, XP, safehouse, etc.) plus improved server logging/monitoring in the 42.20-era settings reference [1] [8] |
| Mod layout served | Flat `media/` mod structure [10] | Versioned `common/` + `42.x` mod folder structure; B41 mods need restructuring [10] |
| Default launch memory | Not verified against a B41-era page revision in this document | `StartServer64.bat` defaults to 16 GB `-Xms`/`-Xmx`, must be edited to fit the host [7] |
| Config surfaces | Same four-file surface (`.ini`, SandboxVars, spawnpoints, spawnregions) — continuity implied by the `legacy41` install path sharing the workflow, verified only against the 42.20-versioned pages [7] [8] | Same, verified at 42.20.0 [7] [8] |
| Hardware appetite | Baseline reference point in community sizing tables [15] | Community and hosting sources agree B42 is heavier, disagree on magnitude — see Claims 1 and 3 [15] [16] |

The one-line version: the server you operate is recognisably the same artifact on both builds — same App ID, ports, files and mod lists — but B42 changes what runs inside it (server-side anti-cheat, heavier world simulation) and what runs beside it (versioned mod structure), and the branch split makes build matching an explicit operational duty [1] [2] [7] [10].

# Practical Guidance

- **Pick the branch before you build the server.** A community's build choice is a migration decision, not a config flag: B41 worlds stay on `legacy41`, and your players must switch their clients the same day you switch the server. Put the branch in your server's documentation and announce switch dates ahead of time.
- **Pin your update command.** Encode the branch into the SteamCMD script (`app_update 380870 validate` vs `app_update 380870 -beta legacy41 validate`) so a routine update can never silently hop builds.
- **Treat `servertest.ini` and SandboxVars as two different change classes.** `.ini` changes can be applied to a running server with `reloadoptions`; sandbox and mod-list changes should be treated as restart-required. When in doubt, schedule a restart — it is never wrong, while an edit the server ignores can be.
- **Size memory from evidence, not the shipped default.** Start from the wiki's worked 6 GB example for a small server, set `-Xms` equal to `-Xmx`, and grow based on observed usage — do not leave the 16 GB B42 default on an 8 GB VPS (it can refuse to start), and do not buy RAM off a hosting table without reading Claim 1.
- **Favour clock speed when choosing hardware,** per the corroborated-but-unofficial single-thread picture in Claim 3 — and verify with your own tick-lag observations rather than CPU marketing.
- **Standardise on RCON tooling early.** `rcon-cli` for scripts and cron, `zomboid-rcon` for anything Python, pz-admin for a GUI. All three work identically against self-hosted and rented servers, which keeps your operations portable if you change hosts.
- **Wire mods as pairs and stage them.** Every entry in `WorkshopItems=` needs its partner entries in `Mods=` (a Workshop item can contain several mod IDs). Test mod-list changes on a copy of the server first: B42's stricter server-side checks and the 42.13-era "mods off" guidance both signal that mods are the least-stable layer of a B42 server.
- **If you self-host on Linux, follow the Ubuntu-first path** — apt SteamCMD, dedicated non-root user, `/opt/pzserver`, tmux or screen — and avoid systemd supervision until the developers' discouragement changes.

# Common Pitfalls & Troubleshooting

- **Server updated to 42.20, players on `legacy41` (or vice versa).** Mismatched branches cannot play together; `DoLuaChecksum` kicks mismatched clients even on the same branch if files differ [2] [8]. Fix the branch on the SteamCMD command line, not by guesswork.
- **B42 server fails with "Assertion Failed: Illegal termination of worker thread".** Documented when B42 server files land on a machine that previously hosted a B41 server: confirm `steam_appid.txt` contains only `108600`, back up your `.ini`/Lua/saves, then remove the old `Zomboid` data folder and let the B42 server recreate it [7].
- **Server exits at startup with memory errors.** The B42 `StartServer64.bat` default of 16 GB exceeds many hosts; edit `-Xms`/`-Xmx` first, not last [7].
- **Launched the server via the Steam client and things broke.** The wiki explicitly warns against launching through Steam; verify file integrity and use the launch scripts [7].
- **Mods listed but not loading.** Check the pairing (`WorkshopItems=` and `Mods=` both populated), the separator (semicolons in the documented `WorkshopItems` example [8]), and — on B42 — whether the mod actually ships the B42 `common/` + `42.x` structure [10]. Be aware of the conflicting backslash advice in Claim 2 before copying a hosting KB's format.
- **"It worked while I edited it live, then my change vanished."** Only `.ini` + `reloadoptions` is a documented live path [7]; treat everything else as restart-required and see Claim 4 for the community rule and its status.
- **Ports open but nobody can join.** Both UDP ports (16261/16262) must be forwarded and allowed by the OS firewall; a second instance on the same box needs its own additional UDP pair [7].

# Community Notes & Unverified Claims

## Claim 1 — A B42 server needs roughly 2 GB more RAM than a B41 server at every player tier

- **Claim:** Hosting knowledge bases advise sizing B42 servers by adding about 2 GB to each B41 tier (e.g. 4 GB → 6 GB for a small vanilla server); one vendor KB states it as "add roughly 2 GB to every B41 number" [15]. Other vendor guidance is materially higher, calling 10 GB "the practical entry point" for B42 [16].
- **Why unverified:** No official Indie Stone sizing table exists for either build; all sources are hosting-company KBs (marketing-adjacent), and their absolute numbers conflict with each other by roughly a factor of two even while agreeing B42 is heavier.
- **Confidence:** Low. The direction (B42 needs more RAM than B41) is consistently reported, but the specific "+2 GB per tier" figure is effectively single-sourced and contradicted by other vendors' tables.

## Claim 2 — B42 requires a backslash before each Mod ID in the `Mods=` line

- **Claim:** Several hosting guides state that Build 42 changed the `Mods=` format to require a leading backslash per entry (`Mods=\ModOne;\ModTwo`), calling it a top cause of "installed but not loaded" mods on B42 [17].
- **Why unverified:** No primary source documents it; the pzwiki Dedicated server page (versioned 42.20.0) shows the `Mods=` workflow with no backslashes [7], and at least one other hosting KB's B42 example also omits them [18]. Secondary sources therefore conflict.
- **Confidence:** Low. The claim circulates widely enough to matter operationally, but the best fact-only source contradicts it; it may describe a transient unstable-era behaviour or a particular panel's convention.

## Claim 3 — Server performance is dominated by single-thread CPU speed, and B42's server-side logic makes it heavier on CPU than B41

- **Claim:** Hosting and community sizing guides consistently state that the PZ server's main simulation loop is effectively single-threaded, so clock speed beats core count (one KB's example: a 3.8 GHz desktop CPU outperforming a 2.4 GHz many-core Xeon), and that B42 is hungrier for CPU as well as RAM [15] [16].
- **Why unverified:** No Indie Stone statement or profiling publication confirms the threading model; the primary record confirms B42 moved anti-cheat/item logic server-side [1] but says nothing about CPU cost.
- **Confidence:** Medium. Multiple independent secondary sources agree and the mechanism is plausible given the documented server-side shift, but it rests entirely on non-primary sources.

## Claim 4 — Always stop the server before editing any config file, or your edits will be lost

- **Claim:** Community and hosting guidance widely instructs admins to fully stop the server before touching `servertest.ini` or SandboxVars, on the basis that the running server holds settings in memory and rewrites the files; one vendor KB notes mod loading "happens at boot only" [18].
- **Why unverified:** As a blanket rule it conflicts with the wiki's documented live path — `.ini` edits saved while running and applied via `reloadoptions` [7]; no primary source states that the server overwrites on-disk edits at shutdown.
- **Confidence:** Medium. Restart-required is demonstrably the safe assumption for mod lists and anything undocumented, making the rule sound operational advice; its factual justification ("the server overwrites your edits") is the unverified part.

# Risks & Caveats

- **Day-one stable.** 42.20 is one day old at the time of writing and hotfixes are expected; any 42.20-specific behaviour cited here (anti-cheat toggles, server options) could shift within weeks [1] [3].
- **Unstable-era operating limits.** The ≤20-player and mods-off guidance was published for 42.13 unstable and has not been re-stated or rescinded for 42.20 [5] [6]; treating it as still-binding is conservative, not confirmed.
- **Wiki verification is B42-sided.** The cited Dedicated server and Server settings revisions are versioned 42.20.0 [7] [8]; B41 continuity of those surfaces is asserted from the unchanged workflow and the `legacy41` install path, not from a B41-era page revision.
- **All hardware-sizing numbers are non-primary.** Claims 1 and 3 are the load-bearing caveat of this document: no RAM table or threading statement here comes from The Indie Stone.
- **Steam announcement mirrors.** Primary citations use steamcommunity.com announcement URLs (verified via the ISteamNews API mirror per project source policy); these hosts bot-block automated link checkers.

# Verification Steps

1. **Confirm the release/branch facts:** query `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0` and read "Build 42.20.0 Stable Released" (2026-07-29) and "B42 CHECKLIST" (legacy41/42.19 instructions).
2. **Confirm the install path:** run SteamCMD `login anonymous` + `app_update 380870 validate` against a scratch directory and verify the server files (including the three StartServer scripts on Windows) appear.
3. **Confirm the config surface:** start the server once, then list `Zomboid/Server` in the server user's home directory and check for the four `servertest*` files.
4. **Confirm ports and RCON:** read `DefaultPort`, `UDPPort`, `RCONPort` in the generated `servertest.ini`; connect with `rcon-cli` against `RCONPort` using `RCONPassword` and issue `showoptions`.
5. **Test the live-reload boundary:** change a benign `.ini` value while running, run `reloadoptions`, and confirm with `showoptions`; then verify a SandboxVars edit does *not* apply until restart.
6. **Resolve Claim 2 empirically:** on a B42 test server, load the same Workshop mod with and without a backslash prefix in `Mods=` and record which variant loads (check the server console mod list at boot).
7. **Probe Claim 1's direction:** run the same small scenario on a `legacy41` server and a 42.20 server with identical `-Xmx` and compare steady-state memory in the server statistics/logs.

# Open Questions

- Do the 42.13-era MP limits (≤20 player slots, mods discouraged) still reflect The Indie Stone's guidance on 42.20 stable, or has scale headroom improved? A dev statement or Thursdoid would resolve it [5] [6].
- Is the backslash `Mods=` convention (Claim 2) real on 42.20, and if so where did it originate — game code, a specific unstable build, or hosting-panel tooling? The empirical test in Verification Steps resolves the behaviour; a changelog entry would resolve the provenance.
- What does the B42 server actually thread across cores (Claim 3)? Profiling on 42.20, or developer comment via the GSP feedback channel, would resolve it [4].
- Will The Indie Stone publish official server sizing guidance now that a GSP engagement channel exists [4]?
- Does the announced post-release Build 42 patching and support work change server resource behaviour later in 2026 [3]?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [2] **The Indie Stone** — *B42 CHECKLIST* (Steam announcement, 2026-07-28). https://steamcommunity.com/games/108600/announcements/detail/1839041357038237. Accessed 2026-07-30.
- [3] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-23). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453. Accessed 2026-07-30.
- [4] **The Indie Stone** — *NEXT STEPS* (Steam announcement, 2026-07-09; game server provider initiative). https://steamcommunity.com/games/108600/announcements/detail/1836506165584147. Accessed 2026-07-30.
- [5] **The Indie Stone** — *Unstable 42 MP Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592123010. Accessed 2026-07-30.
- [6] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972. Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [7] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-30. Fact-only source.
- [8] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-30. Fact-only source.
- [9] **PZwiki** — *Startup parameters* (revision 1393745). https://pzwiki.net/w/index.php?title=Startup_parameters&oldid=1393745. Accessed 2026-07-30. Fact-only source.
- [10] **PZwiki** — *Mod structure* (revision 1443271; page versioned against 42.14.0). https://pzwiki.net/w/index.php?title=Mod_structure&oldid=1443271. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating**

- [11] **beyenilmez** — *pz-admin* (MIT; RCON desktop admin app for Project Zomboid servers). https://github.com/beyenilmez/pz-admin. Accessed 2026-07-30.
- [12] **jmwhitworth** — *zomboid_rcon* (GPL-3.0; Python RCON library, PyPI package `zomboid-rcon`). https://github.com/jmwhitworth/zomboid_rcon. Accessed 2026-07-30.
- [13] **gorcon** — *rcon-cli* (MIT; Source RCON CLI listing Project Zomboid support). https://github.com/gorcon/rcon-cli. Accessed 2026-07-30.
- [14] **Bobagi** — *Project-Zomboid-Ubuntu-Server* (MIT; Ubuntu 22.04/24.04 dedicated-server guide, App ID 380870). https://github.com/Bobagi/Project-Zomboid-Ubuntu-Server. Accessed 2026-07-30.
- [15] **DoomHosting** — *Project Zomboid Server RAM Requirements (Build 41 vs Build 42)* (hosting KB; corroborate-only). https://www.doomhosting.com/help/articles/project-zomboid-server-ram-requirements. Accessed 2026-07-30.
- [16] **Pinehosting** — *How Much RAM Do You Need For Build 42 Project Zomboid Server Hosting?* (hosting KB; corroborate-only). https://pinehosting.com/blog/how-much-ram-do-you-need-for-build-42-project-zomboid-server-hosting/. Accessed 2026-07-30.

**Community & Creator**

- [17] **Pinehosting** — *Project Zomboid Build 42 Mods: Install And Fix Guide* (hosting blog; source of the backslash claim). https://pinehosting.com/blog/modded-project-zomboid-server-hosting-build-42-install-steam-workshop-mods-fixes/. Accessed 2026-07-30.
- [18] **DoomHosting** — *How to Install Mods on a Project Zomboid Server (Build 42)* (hosting KB; backslash-free counter-example). https://www.doomhosting.com/help/articles/how-to-install-mods-project-zomboid-server-build-42. Accessed 2026-07-30.

**Further Reading**

# Further Reading

- The Steam news API mirror used to verify all primary announcements: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- Valve's SteamCMD documentation, referenced by the wiki install instructions: https://developer.valvesoftware.com/wiki/SteamCMD
- Tiiffi/mcrcon, a minimal C RCON client also usable with PZ: https://github.com/Tiiffi/mcrcon
- The official blog / Thursdoid feed (bot-blocks automated checkers; read in-browser): https://projectzomboid.com/blog/

# Related Documents

- `players-foundation` — the Players-track foundation (the branch split and save compatibility from the player's side).
- `modders-foundation` — the Modders-track foundation (the B42 mod structure your server's mods must follow).
- `creator-foundation` — the Creator-track foundation (multiplayer servers as content settings).
- `lore-foundation` — the Lore-track foundation (what the world you are hosting actually is).
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-07-30 | Orchestrator (KB Pipeline) | Approved and frozen — foundation cluster release kb-release-2026.07.30. | Standing mandate (2026-07-30) |
| 1.0.1 | 2026-07-30 | Orchestrator (KB Pipeline) | License-hygiene prose rewrites after arming the pzwiki n-gram gate (no factual changes). | Standing mandate (2026-07-30) |
