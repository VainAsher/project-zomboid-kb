---
id: admins-ubuntu-runbook
title: "Ubuntu Dedicated Server Runbook: SteamCMD to systemd"
version: 0.1.0
status: in-review
confidence: Medium
category: Admins
topic: "Server runbooks"
build: both
document_type: tutorial
created: 2026-07-31
updated: 2026-07-31
review_due: 2026-10-31
sources_verified: 2026-07-31
supersedes: null
related: [admins-foundation, admins-server-ini-reference, admins-backups-migration, meta-style-guide]
tags: [ubuntu, linux, steamcmd, systemd, ufw, dedicated-server, runbook, legacy41, screen, tmux]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-ubuntu-runbook |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-07-31 |
| Review due | 2026-10-31 |
| Game versions verified | 41.78.16, 42.20 |

# Executive Summary

This is the Admins-track, start-to-finish runbook for standing up a vanilla (unmodded) Project Zomboid dedicated server on Ubuntu Linux: prerequisites, SteamCMD installation of App ID 380870, the split between the install directory and the `~/Zomboid` data directory, first-run bring-up, running the process persistently, `ufw` firewall rules, and day-to-day lifecycle (start/stop/restart, logs). Where the foundation overview (`admins-foundation`) maps that a Linux install path exists, this document is the copy-pasteable procedure — including the actual `systemd` unit file the pzwiki Dedicated server page documents, and the `tmux`/`screen` fallbacks for admins who do not want a supervised service.

Two sources anchor the procedure: the pinned pzwiki "Dedicated server" revision (1443349, versioned against 42.20.0), which documents the Debian/Ubuntu apt-based SteamCMD install, the required firewall ports, the `tmux` console pattern, and a `systemd` unit + socket pattern the wiki attributes directly to community/community-adjacent practice while noting the developers discourage it [3]; and the MIT-licensed, Ubuntu-22.04/24.04-scoped `Bobagi/Project-Zomboid-Ubuntu-Server` repository, this knowledge base's canonical Tier 4 source for the Linux self-host track, which documents an `adduser`-based non-root user, the same App ID 380870 SteamCMD sequence, `ufw` rules, and a `screen`-based persistent session [7]. The two sources agree on every mechanic they both cover; where community guides diverge — most visibly on whether extra 32-bit compatibility packages must be installed by name — this document says so and quarantines the discrepancy rather than picking a side.

The branch picture carries over unchanged from `admins-foundation`: Build 42.20 has been the stable branch since 2026-07-29, and communities keeping a Build 41.78 world alive add a beta flag to the same SteamCMD sequence [1] [2]. Document-level confidence is **Medium**: the install/service mechanics rest on a fact-only wiki page plus an open-source community repo, not on an official Indie Stone Linux guide, and one operational detail (the exact 32-bit library list) is contested between community guides and is quarantined below.

# Key Takeaways

- Ubuntu/Debian SteamCMD needs the `i386` architecture enabled before `apt install steamcmd` will pull a working binary — `sudo dpkg --add-architecture i386` (plus `multiverse`/`non-free` on some releases) *(cited)* *(both)*
- Run the server as a dedicated non-root user (`pzuser` in the wiki's own instructions, `steam` in the Bobagi guide) — never as root *(cited)* *(both)*
- The install directory (server binaries) and the `~/Zomboid` data directory (config, saves, logs, account database) are two different trees; only the data directory needs backing up day to day *(cited)* *(both)*
- SteamCMD's install/update sequence is `force_install_dir <path>` → `login anonymous` → `app_update 380870 validate`; add `-beta legacy41` to keep a server on Build 41.78 *(cited)* *(both)*
- Two UDP ports must be opened with `ufw`: `16261` (default game port) and `16262` (direct-connection port); RCON is a separate, unrelated port (`27015` by default) that this runbook does not tell you to expose to the internet *(cited)* *(both)*
- `systemd` (a unit plus a FIFO-backed socket unit) is the wiki's own documented persistent-service pattern, and is what this document treats as preferred — but the same wiki page states the developers explicitly discourage systemd management, since the in-place shutdown safeties "should" save the world but carry no guarantee *(cited)* *(both)*
- `tmux` (wiki-documented) and `screen` (Bobagi-guide-documented) are the fallback way to keep an interactive console alive across a dropped SSH session, for admins who skip systemd *(cited)* *(both)*
- The graceful stop is the `quit` admin command (save-and-stop); anything that kills the Java process instead (`kill -9`, a host reboot without a stop step) bypasses the documented save path *(cited synthesis)* *(both)*
- Whether extra named 32-bit compatibility packages (`lib32gcc-s1`, `lib32stdc++6`) must be installed beyond `dpkg --add-architecture i386` + `apt install steamcmd` is contested between community guides — quarantined below *(community, unverified)*

# Purpose

`admins-foundation` establishes that Ubuntu is a first-class, fully supported install target and that the wiki and the Bobagi guide both document the shape of that path. This document is the runbook itself: the exact commands, in order, from a bare Ubuntu box to a running, persistently supervised, firewalled Project Zomboid dedicated server — and the exact commands to stop, restart and inspect it afterward. It exists so an admin can follow one document start to finish without reassembling the procedure from three different wiki pages and a GitHub README.

# Scope

Covered: prerequisites and 32-bit compatibility packages for SteamCMD on Ubuntu/Debian; installing SteamCMD and pulling the dedicated server (App ID 380870) with an anonymous login; the install-directory-vs-`~/Zomboid`-data-directory split; first-run bring-up and the initial admin/RCON password prompt; running the server persistently via a `systemd` unit (primary method documented here) with `tmux`/`screen` as documented fallbacks; `ufw` firewall rules for the ports this server needs; basic lifecycle (start, graceful stop, restart, log file locations); and what differs (little, mechanically) between installing the B41 `legacy41` branch and B42 stable via SteamCMD's beta-branch flag.

Not covered: mod/Workshop wiring (`admins-workshop-mod-wiring`); backup strategy and world migration in depth (`admins-backups-migration`); the meaning of individual `server.ini`/SandboxVars values (`admins-server-ini-reference`); and the broader install/branch/hosting map, which `admins-foundation` already owns — this document goes one level deeper on the Ubuntu path specifically. Unstable-branch behaviour after 42.20 is out of scope.

# Definitions

- **SteamCMD** — Valve's command-line Steam client; on Ubuntu/Debian it is packaged as `steamcmd` in the `multiverse` (Ubuntu) or `non-free` (Debian) repository, requires the `i386` architecture enabled, and installs to `/usr/games/steamcmd` when installed via apt (hence adding `/usr/games` to `PATH`) [3].
- **App ID 380870** — the Steam application ID of the free-standing "Project Zomboid Dedicated Server" tool, distinct from the game client's own app ID (108600) [3] [7].
- **`force_install_dir`** — the SteamCMD directive that sets where the server *binaries* are installed; a separate location from the server's runtime data [3] [7].
- **`Zomboid` data directory** — the per-user data folder (`$HOME/Zomboid` on Linux) holding `Server/` (config), `Saves/` (world data), `db/` (accounts), `Logs/` (per-session logs) and the `logs.zip` support bundle — distinct from the install directory and not overwritten by a SteamCMD update [6].
- **`start-server.sh`** — the Linux launch script inside the install directory that starts the server process; takes `-servername`, `-nosteam` and other startup parameters [3].
- **FIFO control socket** — the named pipe (`zomboid.control` in the wiki's own example) that a `systemd` socket unit exposes so that shell commands (`echo "save" > .../zomboid.control`) can be sent to the running server without an interactive console [3].
- **`legacy41`** — the Steam beta branch (client and server) that keeps Build 41.78 installed after Build 42 became the default stable build; selected on the server side with SteamCMD's `-beta legacy41` flag [1] [2] [3].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Same install/service procedure, reached by adding `-beta legacy41` to the SteamCMD update sequence [1] [2] [3] |
| B42 (stable) | Yes | 42.20 | Default SteamCMD sequence installs 42.20, stable since 2026-07-29 [1] [3] |

The pzwiki pages cited here are versioned against the 42.20 era [3] [4] [5] [6], and the Bobagi repository is not build-versioned at all — it documents the install mechanics (users, SteamCMD, firewall, persistent session) that are identical regardless of which branch flag is passed to `app_update` [7]. This document's B41 coverage is therefore the same install/service procedure as B42, distinguished only by the `-beta legacy41` flag documented directly by the primary announcements and the wiki [1] [2] [3] — it is not independently re-verified against a B41-era revision of the Dedicated server page, the same caution `admins-foundation` and its siblings already carry for this page.

# Reference

## Prerequisites and the 32-bit compatibility requirement

SteamCMD on Ubuntu/Debian is a 32-bit binary even on a 64-bit host, so the `i386` architecture must be enabled before installing it: `sudo dpkg --add-architecture i386`, then `sudo apt update` [3] [7]. The wiki's own Debian/Ubuntu instructions additionally enable the `multiverse` component (`sudo add-apt-repository multiverse`) before `sudo apt install steamcmd`, and separately note that some setups need the non-free component enabled via `software-properties-common` and `apt-add-repository non-free` [3]. The Bobagi guide's prerequisite sequence is the same shape: add the `i386` architecture, `apt update`, then `apt install steamcmd -y` [7]. Neither of these two sources lists a separate, explicitly-named 32-bit compatibility library (such as `lib32gcc-s1`) as a required package beyond the architecture flag and the `steamcmd` package itself — a point some community guides handle differently (Claim 1, below).

## Installing SteamCMD and pulling the dedicated server (App 380870)

Both anchor sources use the same non-root pattern before touching SteamCMD. The wiki creates a dedicated `pzuser` account and an install directory it owns:

```bash
sudo adduser pzuser
sudo mkdir /opt/pzserver
sudo chown pzuser:pzuser /opt/pzserver
sudo -u pzuser -i
```

and then drives the install through a reusable SteamCMD script, `update_zomboid.txt`, rather than typing commands interactively [3]:

```text
// update_zomboid.txt
@ShutdownOnFailedCommand 1
@NoPromptForPassword 1
force_install_dir /opt/pzserver/
login anonymous
app_update 380870 validate
quit
```

run with:

```bash
export PATH=$PATH:/usr/games
steamcmd +runscript $HOME/update_zomboid.txt
```

The Bobagi guide's equivalent is an interactive SteamCMD session against a differently-named user and path (`steam` / `/home/steam/pzsteam`), driving the same three logical steps (`force_install_dir`, `login anonymous`, `app_update 380870 validate`) [7]. Either shape reaches the same result: the server is App ID 380870, fetched with an anonymous Steam login, and needs no owned game copy on the host account [3] [7]. Re-running the same script later (or the same three interactive commands) is also how the server is *updated* — `app_update 380870 validate` is idempotent and re-validates existing files [3].

## Directory layout: install directory vs. the `Zomboid` data directory

These are two separate trees, and conflating them is the single most common source of a broken restore or a lost mod list. The **install directory** (`force_install_dir`'s target — `/opt/pzserver` in the wiki's own example, `/home/steam/pzsteam` in Bobagi's) holds the server binaries and launch scripts (`start-server.sh`) and is fully disposable: SteamCMD can regenerate it from nothing [3] [7]. The **`Zomboid` data directory** — `$HOME/Zomboid` for whichever Linux user runs the process — holds everything that actually matters operationally: `Server/<name>.ini` and the SandboxVars/spawnpoint Lua files, `Saves/Multiplayer/<name>/` (the world), `db/<name>.db` (accounts), a `Logs/` folder of per-session logs, `server-console.txt` (the dedicated server's own console log), and a `logs.zip` support bundle (the last five launches' logs, settings and mod lists — not to be confused with the `Logs/` folder itself) [6]. Bobagi's guide places the mods folder at `Zomboid/mods/` under the same data directory [7]. `admins-server-ini-reference` and `admins-backups-migration` own the deeper detail of what lives inside `Server/` and `Saves/`; this document's job is only to establish that the two trees exist and that only the data directory needs protecting day to day.

## First-run bring-up and the admin/RCON password

Starting the server for the first time (`bash start-server.sh` from the install directory) prompts interactively for an admin-account password before generating the default `servertest.ini`, SandboxVars and world data [3]. `RCONPort` (default 27015) and `RCONPassword` are ordinary keys inside the generated `servertest.ini` — the wiki's pinned settings reference documents the default port and advises picking a strong password, but the RCON password itself is not part of the interactive first-run prompt and must be set by editing the `.ini` afterward [4]. `admins-server-ini-reference` is the authority on every other key in that file; this runbook only establishes that the file exists once the server has been launched at least once [3] [4].

## Running it persistently: a systemd unit (preferred method)

The pinned Dedicated server revision documents a complete `systemd` unit plus a FIFO-backed socket unit, meant to be created only *after* the server has been launched manually at least once (so the first-run password prompt has already been answered) and while logged in as `pzuser`, with the `systemd` commands themselves run as root [3]:

```bash
cat >/etc/systemd/system/zomboid.service <<'EOL'
[Unit]
Description=Project Zomboid Server
After=network.target

[Service]
PrivateTmp=true
Type=simple
User=pzuser
WorkingDirectory=/opt/pzserver/
ExecStart=/bin/sh -c "exec /opt/pzserver/start-server.sh </opt/pzserver/zomboid.control"
ExecStop=/bin/sh -c "echo save > /opt/pzserver/zomboid.control; sleep 15; echo quit > /opt/pzserver/zomboid.control"
Sockets=zomboid.socket
KillSignal=SIGCONT

[Install]
WantedBy=multi-user.target
EOL

cat >/etc/systemd/system/zomboid.socket <<'EOL'
[Unit]
BindsTo=zomboid.service

[Socket]
ListenFIFO=/opt/pzserver/zomboid.control
FileDescriptorName=control
RemoveOnStop=true
SocketMode=0660
SocketUser=pzuser
EOL
```

Once both units exist, the documented command surface is [3]:

```bash
systemctl start zomboid.socket   # start a server
systemctl stop zomboid           # stop a server
systemctl restart zomboid        # restart a server
systemctl status zomboid         # check server status (ctrl-c to exit)
journalctl -u zomboid -f         # follow the logs
echo "command" > /opt/pzserver/zomboid.control   # send an admin command to the running server
```

Two things about this pattern are worth stating exactly as the source states them, not softened. First, the `ExecStop` line is precisely `echo save` (flush the world), `sleep 15`, then `echo quit` (save again and stop) — the systemd stop path *is* the same graceful `save`-then-`quit` sequence an admin would type by hand [3] [5]. Second, the wiki's own text is a direct caveat on the whole pattern: **"The Zomboid Devs explicitly discourage this method, the safeties currently in place should insure a proper saving sequence on server shutdown, but there are no guarantees"** [3]. This document still treats systemd as the preferred method for a production Ubuntu box — automatic restart on crash, boot-time start, and `journalctl` integration are real operational wins — but that preference is an editorial choice by this document, not something the source itself endorses; make the tradeoff knowingly.

## Fallback supervision: tmux and screen

For admins who want to skip systemd, both sources document an interactive-console fallback, and they document two different tools. The wiki's own instructions use `tmux`: start a `tmux` session before launching the server, so an accidentally closed terminal or dropped SSH connection does not kill the process, and reattach later with `tmux a` [3]:

```bash
apt-get install tmux   # if "command not found"
tmux
cd /opt/pzserver/
bash start-server.sh
# detach: Ctrl+B then D
# reattach: tmux a
```

The Bobagi Ubuntu guide instead uses `screen` for the identical purpose [7]:

```bash
screen -S zomboid
cd /home/steam/pzsteam
./start-server.sh -servername <yourservername>
# detach: Ctrl+A then D
# reattach: screen -r zomboid
```

Functionally these solve the same problem (keep the console alive across a dropped session) and neither wraps the process in a supervisor that restarts it on crash or at boot — that is what the systemd pattern above adds. Pick one based on which tool your distribution already has or your own familiarity; this document does not have evidence that either is safer for world-saving than the other, since neither wraps `start-server.sh` in anything beyond a terminal multiplexer.

## Firewall: ufw rules

Two UDP ports must be reachable from the internet: `16261` (the default game port) and `16262` (the direct-connection port) [3] [4]. Both anchor sources give the same `ufw` commands, and the wiki adds the reload step explicitly [3] [7]:

```bash
sudo ufw allow 16261/udp
sudo ufw allow 16262/udp
sudo ufw reload
```

The Bobagi guide additionally opens SSH (`sudo ufw allow 22`) and calls `sudo ufw enable` as part of the same sequence, since a server admin who has never enabled `ufw` on the box needs that step first [7]. RCON (`RCONPort`, default 27015) is a separate listener from the two game ports and neither anchor source's firewall instructions open it [3] [4] [7] — treat that as deliberate: RCON is an administrative interface, and this runbook does not tell you to expose it to the public internet (see Practical Guidance). Running a second server instance on the same box needs its own additional pair of free UDP ports, set in that instance's `.ini` and opened the same way — the wiki's own worked example uses `16274`/`16275` for a second instance [3].

## Lifecycle: start, stop, restart, logs

Starting: `bash start-server.sh` from the install directory, optionally with `-servername <name>` (switches which `.ini`/save set is used) or `-nosteam` (for hosting non-Steam, e.g. GOG, players) [3]. Stopping gracefully is the admin command `quit`, documented as "Save and quit the server"; `save` alone ("Save the current world") flushes state without stopping [5]. Restarting is stop-then-start under `tmux`/`screen`, or `systemctl restart zomboid` under the systemd pattern, which itself performs the save-then-quit `ExecStop` sequence before relaunching [3]. Logs live inside the `Zomboid` data directory: a `Logs/` folder of per-session log files, a `server-console.txt` console log, and — distinct from both — a `logs.zip` bundle (last five launches, mod lists, settings, and files from the last loaded save) intended for sharing when asking for help, not for routine monitoring [6]. Under systemd, `journalctl -u zomboid -f` additionally captures the service's own stdout/stderr stream [3].

## Branch selection via SteamCMD: stable vs. legacy41

The install and service procedure above is identical for both builds; the only difference is one flag on the SteamCMD update line. The default sequence installs whatever is current on the stable branch — 42.20 since 2026-07-29 [1]. A community keeping a Build 41.78 world alive adds `-beta legacy41` to the same command, and the wiki gives the modified script verbatim [1] [2] [3]:

```text
// update_zomboid.txt (legacy41)
@ShutdownOnFailedCommand 1
@NoPromptForPassword 1
force_install_dir /opt/pzserver/
login anonymous
app_update 380870 -beta legacy41 validate
quit
```

Nothing else in this runbook changes: the same non-root user, the same `Zomboid` data directory shape, the same two firewall ports, the same systemd unit (pointed at the same `start-server.sh`), and the same `tmux`/`screen` fallbacks apply to a `legacy41` install unchanged [1] [2] [3] [7]. The operational discipline that matters is encoding the branch flag into your update script permanently, so a routine re-run of the same script can never silently hop the server onto the other branch — `admins-foundation` covers this same point for the general install picture [1] [2].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|----------------------|
| SteamCMD sequence | `app_update 380870 -beta legacy41 validate` [1] [2] [3] | `app_update 380870 validate` (default branch) [1] [3] |
| Prerequisites, user setup, directory layout | Same mechanics; not independently re-verified against a B41-era wiki revision in this document | Verified against the 42.20-versioned Dedicated server revision [3] |
| Firewall ports | Same two UDP ports, same `ufw` commands [3] [4] [7] | Same [3] [4] [7] |
| systemd unit / tmux / screen | Same unit file and fallback tools; no build-specific variant documented | Same [3] [7] |
| Lifecycle commands (`save`, `quit`) | Same admin commands [5] | Same [5] |

The one-line version: this entire runbook is one procedure with a single conditional branch flag — everything from prerequisites through firewall rules through the systemd unit is identical whether the SteamCMD line ends in `validate` or `-beta legacy41 validate` [1] [2] [3] [7].

# Practical Guidance

**Full sequence, condensed (Ubuntu 22.04/24.04, stable branch, systemd-supervised):**

```bash
# 1. Prerequisites
sudo dpkg --add-architecture i386
sudo apt update
sudo add-apt-repository multiverse
sudo apt install steamcmd -y

# 2. Dedicated user + install directory
sudo adduser pzuser
sudo mkdir /opt/pzserver
sudo chown pzuser:pzuser /opt/pzserver
sudo -u pzuser -i

# 3. Reusable SteamCMD update script (as pzuser)
cat > $HOME/update_zomboid.txt <<'EOL'
@ShutdownOnFailedCommand 1
@NoPromptForPassword 1
force_install_dir /opt/pzserver/
login anonymous
app_update 380870 validate
quit
EOL
export PATH=$PATH:/usr/games
steamcmd +runscript $HOME/update_zomboid.txt

# 4. First run (answer the admin-password prompt), then Ctrl+C once it's stable
cd /opt/pzserver
bash start-server.sh

# 5. Firewall (as a sudo-capable user)
sudo ufw allow 16261/udp
sudo ufw allow 16262/udp
sudo ufw reload

# 6. Persistent service — create the two unit files shown in Reference, then:
sudo systemctl daemon-reload
sudo systemctl enable zomboid.socket
sudo systemctl start zomboid.socket
```

Source basis for each numbered step: 1–4 and 6 from the pinned wiki revision [3]; 5 from both anchor sources [3] [7].

**For an internet-facing box, keep RCON off the open internet.** Neither anchor source's firewall instructions open `RCONPort` [3] [7], and this runbook does not recommend changing that: if you need remote RCON access, prefer an SSH tunnel or a source-restricted `ufw` rule (`sudo ufw allow from <admin-IP> to any port 27015 proto udp`) over a blanket `ufw allow 27015`. Pair a real `RCONPassword` with whichever exposure you choose — `admins-server-ini-reference` covers the key itself.

**Re-run the same update script to update the server.** `app_update 380870 validate` is the same command used for the initial install and every later update; keep the branch flag baked into the script permanently so a routine update can never silently switch branches [1] [2] [3].

**If you adopt systemd, rehearse the stop path before you trust it.** Take a note of a world file's timestamp, `systemctl stop zomboid`, and confirm the save actually landed before announcing the server as production-ready — the wiki's own "no guarantees" caveat is the reason to verify this yourself rather than assume it [3].

**Choose `tmux` or `screen` based on what's already on your box**, not on any documented safety difference between them — this runbook found none [3] [7].

**Route the RAM and mod-wiring pieces to their own documents.** Editing `-Xms`/`-Xmx` in `start-server.sh` and wiring `WorkshopItems=`/`Mods=` are both covered by `admins-foundation`, `admins-server-ini-reference` and `admins-workshop-mod-wiring` — this runbook only gets the process running and supervised.

# Common Pitfalls & Troubleshooting

- **`apt install steamcmd` fails or SteamCMD immediately errors out.** The `i386` architecture was not added before installing — run `sudo dpkg --add-architecture i386` and `sudo apt update` first, and confirm `multiverse` (Ubuntu) or `non-free` (Debian) is enabled [3] [7].
- **`steamcmd: command not found` even after installing the package.** The apt package installs to `/usr/games/steamcmd`; add it to `PATH` (`export PATH=$PATH:/usr/games`) before invoking `steamcmd` [3].
- **Server files owned by the wrong user after install.** Everything from `force_install_dir` through the `Zomboid` data directory should belong to the dedicated non-root account; running any step as root (or `sudo -u pzuser -i` skipped) leaves ownership wrong and the systemd unit's `User=pzuser` line will then fail to start the process [3] [7].
- **Only one UDP port opened.** `16261` and `16262` are both required; opening just the default port leaves direct connections unreachable [3] [4].
- **Second instance on the same box won't start, or the first instance stops accepting connections.** Two servers on one host each need their own UDP port pair and firewall rules — reusing the default pair for both is a documented failure mode [3].
- **Trusted systemd's stop path without checking it.** The wiki itself does not guarantee the save-then-quit `ExecStop` sequence always completes cleanly; a hard `kill -9` on the Java process (or a host power event) skips it entirely — verify your stop path, and keep the cold-backup discipline in `admins-backups-migration` regardless of which supervision method you use [3].
- **Confusing `logs.zip` with the `Logs/` folder.** They are different things at different depths of the `Zomboid` data directory; `logs.zip` is a curated support bundle, `Logs/` is the raw per-session log stream [6].
- **RCON port reachable from the open internet with a weak or empty password.** Neither anchor source's firewall guidance opens `RCONPort` — if you did so yourself, pair it with a strong `RCONPassword` or restrict the source IP [3] [4] [7].
- **B42 server fails to start on a box that previously ran a B41 server**, with "Assertion Failed: Illegal termination of worker thread": this is a documented cross-version residue issue on the same machine, not specific to the Ubuntu path, and is covered in `admins-foundation` and `admins-backups-migration`; the same pinned Dedicated server page is the source [3].

# Community Notes & Unverified Claims

## Claim 1 — Explicit 32-bit compatibility packages (`lib32gcc-s1`, `lib32stdc++6`) must be installed by name for SteamCMD to work on Ubuntu

- **Claim:** Some independent Linux setup walkthroughs list `lib32gcc-s1` (and, in other guides, `lib32stdc++6`) as a required apt package for running SteamCMD on a 64-bit Ubuntu host, and pair it with installing SteamCMD from Valve's manually downloaded tarball rather than the distro's `steamcmd` package — one such walkthrough's prerequisite line is `sudo apt install -y software-properties-common lib32gcc-s1 curl` [8].
- **Why unverified:** Neither of this document's two anchor sources for the Ubuntu path — the pinned pzwiki Dedicated server revision or the Bobagi Ubuntu-Server repository — lists a 32-bit compatibility package by name; both rely on `sudo dpkg --add-architecture i386` plus `apt install steamcmd`, and neither documents a manual-tarball install path [3] [7]. No Valve or Indie Stone primary source with an exact Ubuntu dependency list was found; Valve's own SteamCMD wiki page could not be retrieved for this document (see Risks).
- **Confidence:** Low. The two most-vetted sources for this document's scope agree with each other and omit the extra package; it is plausible the difference reflects an older/newer Ubuntu point release, or a manual-tarball install pulling in dependencies differently than the `steamcmd` apt package does, but this was not tested first-hand.

# Risks & Caveats

- **No official Indie Stone Linux install guide exists.** Every mechanic in this document rests on a fact-only community wiki page and an open-source, community-maintained GitHub repository, not on an Indie-Stone-authored Ubuntu runbook — this is the ceiling on this document's confidence rating.
- **The systemd pattern's safety is explicitly *not* vouched for by its own source.** The wiki text discouraging systemd management is quoted verbatim in Reference; this document's choice to present it as the preferred method is an editorial judgement about operational convenience, not a claim that it is safer than the fallbacks [3].
- **32-bit prerequisite packages are contested between community sources (Claim 1)** and were not tested first-hand on a clean Ubuntu 22.04/24.04 box for this document.
- **Valve's own SteamCMD documentation could not be retrieved.** `developer.valvesoftware.com/wiki/SteamCMD` served an automated bot-verification challenge page during research for this document and is listed only in Further Reading, not cited as a numbered source for any claim.
- **Wiki-page currency.** The Dedicated server, Server settings and Tech Support pages cited here are pinned at specific revisions (1443349, 1443167, 1442989) versioned against the 42.20 era; a post-42.20 hotfix could change any of the mechanics described before the wiki re-verifies them.
- **B41-side verification is inherited, not direct**, exactly as the sibling Admins documents already flag for these same wiki pages: the install/service mechanics are asserted to be build-independent from the shared `legacy41` install path, not from an independently pinned B41-era page revision.

# Verification Steps

1. **Run the condensed sequence in Practical Guidance on a fresh Ubuntu 22.04 or 24.04 VM** and confirm the server reaches the first-run admin-password prompt without a 32-bit-library error.
2. **Resolve Claim 1 empirically:** on a second clean VM, skip any explicit `lib32gcc-s1`/`lib32stdc++6` install and attempt only `dpkg --add-architecture i386` + `apt install steamcmd`; record whether SteamCMD runs.
3. **Confirm the port surface:** with the server running, verify UDP listeners on `16261` and `16262` from another host, and confirm `RCONPort` (27015 by default) is *not* reachable unless you deliberately opened it.
4. **Rehearse the systemd stop path:** note a save-file timestamp, run `systemctl stop zomboid`, and confirm the world data was flushed before the process actually exited.
5. **Confirm the `legacy41` flag installs the right build:** run the modified update script and check the installed server's reported version against 41.78.16.
6. **Confirm log locations:** after a session, check `Zomboid/Logs/`, `Zomboid/server-console.txt` and `Zomboid/logs.zip` all exist and contain what this document describes.

# Open Questions

- Does the systemd `ExecStop` save-then-quit sequence ever fail to flush the world under real load (long tick queues, an in-progress chunk write), and if so what would the failure look like in the logs? The wiki's "no guarantees" caveat is the only source touching this, and it does not elaborate [3].
- What is the precise, current 32-bit dependency list the `steamcmd` apt package expects on today's Ubuntu 22.04/24.04, and does it differ from what a manually downloaded SteamCMD tarball needs (Claim 1)? Verification Step 2 would resolve this empirically per release.
- Will The Indie Stone ever publish first-party Linux install/service guidance, given the game-server-provider engagement channel `admins-foundation` documents? That would settle both the 32-bit-package question and the systemd-safety question at the primary-source tier.
- Does `KillSignal=SIGCONT` in the documented systemd unit interact with any Java shutdown-hook behaviour in a way that differs from the process simply receiving `SIGTERM`, and is that why the FIFO/`echo quit` path is used instead of a plain `ExecStop=`? No source examined explains the design rationale.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via the Steam news API mirror, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *B42 CHECKLIST* (Steam announcement, 2026-07-28; retrieved via the Steam news API mirror). https://steamcommunity.com/games/108600/announcements/detail/1839041357038237. Accessed 2026-07-31.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [3] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-31. Fact-only source.
- [4] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Admin commands* (revision 1385097). https://pzwiki.net/w/index.php?title=Admin_commands&oldid=1385097. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Tech Support* (revision 1442989). https://pzwiki.net/w/index.php?title=Tech_Support&oldid=1442989. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [7] **Bobagi** — *Project-Zomboid-Ubuntu-Server* (MIT; Ubuntu 22.04/24.04 dedicated-server guide, App ID 380870, `screen`-based persistence). https://github.com/Bobagi/Project-Zomboid-Ubuntu-Server. Accessed 2026-07-31.

**Community & Creator**

- [8] **Shattered.io** — *Project Zomboid Dedicated Server* (independent Linux setup walkthrough; source of the Claim 1 32-bit-package and manual-tarball-install variant). https://shattered.io/project-zomboid-dedicated-server/. Accessed 2026-07-31.

**Further Reading**

# Further Reading

- The ISteamNews mirror used to verify the primary announcements: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- Valve's SteamCMD wiki page (blocked automated retrieval with a bot-verification challenge during this document's research; read in-browser): https://developer.valvesoftware.com/wiki/SteamCMD
- gorcon/rcon-cli, for scripting RCON commands against a systemd- or tmux/screen-supervised server: https://github.com/gorcon/rcon-cli

# Related Documents

- `admins-foundation` — the Admins-track overview this runbook deepens: branch picture, config surfaces, ports, memory sizing and the wider tooling landscape.
- `admins-server-ini-reference` — the key-by-key `server.ini` reference, including `RCONPort`/`RCONPassword` and every other setting this runbook's first-run and firewall sections touch only at overview level.
- `admins-backups-migration` — the deeper backup/restore/migration runbook for the `Zomboid` data directory this document only introduces.
- `admins-workshop-mod-wiring` — the mechanics of `WorkshopItems=`/`Mods=`, out of scope here.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
