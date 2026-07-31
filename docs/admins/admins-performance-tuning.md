---
id: admins-performance-tuning
title: "Server Performance: Memory, CPU and the Levers That Are Actually Documented"
version: 0.1.0
status: in-review
confidence: Medium
category: Admins
topic: "Server operations"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-07-31
review_due: 2026-10-31
sources_verified: 2026-07-31
supersedes: null
related: [admins-foundation, admins-server-ini-reference, admins-sandboxvars-reference, meta-style-guide]
tags: [performance, jvm, xmx, memory, cpu, tuning, monitoring, statistics, dedicated-server, b42, legacy41]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-performance-tuning |
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

This document is the Admins-track performance runbook. It goes one level below `admins-foundation`'s memory overview and inventories the *documented* performance surface of a Project Zomboid dedicated server: the JVM flags actually shipped in the launch scripts (including the ZGC garbage collector the B42 server runs with), the `-Xms`/`-Xmx` mechanics and their failure modes, the handful of `servertest.ini` and SandboxVars keys with a citable load story (player cap, packet caps, statistics period, cleanup timers, and B41's zombie-network tuning quartet), the performance-relevant items in the 42.20 stable release notes (object-pool statistics, chunk-generation hang fixes, ZNet and packet-logging improvements), and the monitoring hooks an operator can turn on today (`-statistic`, `MultiplayerStatisticsPeriod`, console-log filters).

Just as important is what this document refuses to invent. The Indie Stone publishes no RAM-per-player sizing table, no CPU or threading statement, and no chunk-cache or map-size tuning knobs for either build; the popular sizing numbers are hosting-company material. The parent document already quarantined the two biggest such claims — the "+2 GB for B42" RAM uplift and the "single-threaded main loop" CPU model (`admins-foundation`, Claims 1 and 3) — and nothing found while researching this document strengthens or weakens them, so they are referenced here, not re-argued. What this document adds to the quarantine layer is new and narrower: the mod-count RAM multiplier, the explored-map "world age" memory-growth claim, and a single-vendor zombie-population RAM figure.

Document-level confidence is **Medium**: the launch-script flags, setting defaults and release-note items rest on revision-pinned wiki snapshots and primary Steam announcements (High), but the B41-side evidence leans on a single archived page revision, the Startup parameters page is stamped against 42.17.0 rather than 42.20, and every absolute sizing number in circulation remains non-primary.

# Key Takeaways

- The B42 server ships with a bundled JRE and runs under the ZGC garbage collector: the wiki-documented `StartServer64.bat` line carries `-XX:+UseZGC`, headless mode, ZNet logging, and paired `-Xms`/`-Xmx` values you must edit down from the 16 GB default *(cited)* *(B42)*
- `-Xmx` set above physical RAM silently spills into virtual memory, and `-Xms` the server cannot actually allocate stops it from starting — both failure modes are documented, sizing tables are not *(cited)* *(both)*
- `MaxPlayers` defaults to 32 on B42 (B41-era default: 16), and the B42 settings reference explicitly warns that going above 32 risks degraded map streaming and desync — the only official-surface player-scale statement outside the 42.13 unstable advisory of at most 20 slots *(cited)*
- The strongest officially documented performance rule is negative: The Indie Stone said in the 42.13 MP release that debug mode degrades server performance and that mods should be disabled — guidance never re-stated or rescinded for 42.20 *(cited)* *(B42)*
- 42.20 shipped real server-performance work: object-pool statistics for monitoring, a fix for servers hanging during chunk generation, ZNet-logging and packet-logging improvements, a zombie-culling fix, and a faster stackable-item transfer path *(cited)* *(B42)*
- Monitoring is opt-in: `-statistic <seconds>` writes multiplayer statistics under the cache directory, and `MultiplayerStatisticsPeriod` controls the update period from the `.ini` side *(cited)*
- B41's revision documents a zombie-network tuning quartet (`ZombieUpdateMaxHighPriority` and friends) plus `PhysicsDelay` and `UseTCPForMapDownloads` that the B42-era settings revision no longer lists *(cited)* *(B41)*
- Mod count and explored-map growth as the dominant RAM drivers are consistent hosting-company claims with no primary source — quarantined below, alongside a single-vendor zombie-population RAM number *(community, unverified)*

# Purpose

This document answers the operator's question "the server is slow, or I am about to size a machine — which knobs are real?" It exists to separate three things that community guides blur together: levers that are documented with values and semantics (JVM flags, a few `.ini` keys), levers that are officially referenced but unquantified (player count, mods, debug mode), and levers that are pure community folklore (RAM tables, CPU threading models, population-to-RAM ratios). A reader should leave knowing exactly which class any given piece of tuning advice belongs to.

# Scope

Covered: the JVM flag set in the shipped launch scripts and its documented semantics; memory sizing mechanics and failure modes on both builds; the `servertest.ini` and SandboxVars keys with a plausible, citable performance effect; the performance-relevant 42.20 release-note items; official statements about player count, mods and debug mode as load factors; monitoring approaches (server console filters, the statistics subsystem, 42.20's object-pool statistics); and an explicit accounting of what is *not* documented.

Not covered: the full per-key `.ini` and SandboxVars references (see `admins-server-ini-reference` and `admins-sandboxvars-reference` — this document only re-lists keys where the performance angle adds something); installation and branch mechanics (`admins-foundation`); RCON tooling; client-side FPS tuning, which is a Players-track concern. The hardware-sizing question itself is deliberately out of scope except as quarantined claims, because no primary source answers it.

# Definitions

- **JVM heap** — the memory pool the Java virtual machine manages for the server process; bounded below by `-Xms` (initial/minimum) and above by `-Xmx` (maximum) [7].
- **ZGC** — the Z Garbage Collector, the low-pause-time JVM collector the shipped B42 server script selects with `-XX:+UseZGC` [4].
- **ZNet** — the game's network layer as named in the shipped `-Dzomboid.znetlog` property and the 42.20 release notes' logging improvements [1] [4].
- **Object pool** — a reuse pattern for allocated objects; 42.20 added statistics for the server's object pools as a monitoring surface [1].
- **Chunk** — the unit of map data the server streams to clients and saves to disk; several 42.20 fixes concern chunk generation and loading [1] [5].
- **Statistics period** — the interval, in seconds, at which the multiplayer statistics subsystem samples; set from the command line (`-statistic`) or the `.ini` (`MultiplayerStatisticsPeriod`) [5] [7].
- **cachedir** — the game's data directory (the `Zomboid` folder by default), relocatable with `-cachedir`; the statistics subsystem writes beneath it [7].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Setting defaults and the B41-only tuning keys verified against the archived Server settings revision stamped 41.78.16 [6] |
| B42 (stable) | Yes | 42.20 | Launch line and settings verified against wiki revisions versioned 42.20.0 [4] [5]; release-note items from the 42.20 announcement [1] |

One dated caveat: the Startup parameters page — the source for the per-flag JVM semantics — is marked as last updated for 42.17.0, with 42.20.0 current [7]. Its `-Xms`/`-Xmx` semantics match the 42.20-versioned Dedicated server page's launch line [4], but flag-level details cited only to [7] carry a 42.17-era verification, not a 42.20 one.

# Reference

## The shipped JVM layer

The Windows server starts through `StartServer64.bat`, which invokes the bundled JRE at `jre64\bin\java.exe` against the `zombie.network.GameServer` main class — the server does not depend on a system Java install [4]. The wiki's documented example line (its 6 GB memory variant) carries this flag set *(B42, page versioned 42.20.0)* [4]:

```text
".\jre64\bin\java.exe" -Djava.awt.headless=true -Dzomboid.steam=1
  -Dzomboid.znetlog=1 -XX:+UseZGC -XX:-CreateCoredumpOnCrash
  -XX:-OmitStackTraceInFastThrow -Xms6g -Xmx6g
  -Djava.library.path=natives/;natives/win64/;.
  -cp %PZ_CLASSPATH% zombie.network.GameServer -statistic 0
```

Reading that line as an operator [4] [7]:

| Flag | What it does (documented) | Cited at |
|------|---------------------------|----------|
| `-Djava.awt.headless=true` | Runs the JVM headless — the dedicated server renders nothing | [4] |
| `-Dzomboid.steam=1` | Steam integration on; `0`/`-nosteam` disables it for non-Steam clients | [4] [7] |
| `-Dzomboid.znetlog=1` | Enables ZNet (network-layer) logging | [4] |
| `-XX:+UseZGC` | Selects the ZGC garbage collector for the server JVM | [4] |
| `-XX:-CreateCoredumpOnCrash` | Suppresses core-dump files on JVM crash | [4] |
| `-XX:-OmitStackTraceInFastThrow` | Keeps full stack traces on repeated exceptions | [4] |
| `-Xms{size}{g\|m}` | Initial heap; launch fails if the system cannot provide it | [4] [7] |
| `-Xmx{size}{g\|m}` | Heap ceiling; above physical RAM it spills into virtual memory | [4] [7] |
| `-XX:+AlwaysPreTouch` | Not shipped, but documented: pre-touches heap pages at startup, and the wiki notes it is the officially recommended companion to ZGC as of Java 21 | [7] |
| `-statistic {seconds}` | Game argument, not a JVM flag: statistics sampling period; the shipped script passes `0` | [4] [7] |

The memory mechanics around this line are the core documented sizing facts, unchanged from the foundation document's framing [4]: the shipped `StartServer64.bat` specifies 16 GB, the values **must** be edited to fit the host or the server exits with memory errors, the wiki's worked example uses 6 GB with `-Xms` and `-Xmx` set equal, and the launch-script value is the same lever as the Host screen's "Server Memory" option. What this document adds from the Startup parameters page: the units are `g` or `m`; an `-Xms` the machine cannot satisfy prevents startup; and an `-Xmx` beyond physical RAM does not fail — it pages, which on a game server converts an out-of-memory condition into a latency problem *(flag semantics verified at 42.17)* [7].

Two placement rules matter when adding flags [7]: in client launch options, JVM arguments come first and are terminated with `--` before game arguments; in `StartServer64.bat`, JVM arguments go after the existing `-Xmx` entry and game arguments after the `%1 %2` forwarding tokens, with no `--` needed because the script already separates the two classes.

On Linux, the launch path is `start-server.sh`, and the JVM options live in the `ProjectZomboid64.json` launcher config rather than a visible batch line — the Ubuntu community guide's memory instruction is to edit the `-Xmx` entry in that file, and its crash advice is to lower it back down against `free -h` output [4] [8]. The client-side `-pzexeconfig` argument documents the same config file by name: it swaps `ProjectZomboid64.json` for an alternative launcher config [7].

## Settings with a citable load story

Only a minority of the roughly 140 `.ini` keys have any documented connection to server load. The full per-key catalogue is `admins-server-ini-reference`; the rows below are the performance-relevant subset, with the load angle spelled out.

| Key | Default | Documented performance angle | Build | Cited at |
|-----|---------|------------------------------|-------|----------|
| `MaxPlayers` | 32 (B42); 16 at the B41 revision | The B42 reference caps it at 100 and warns that counts above 32 risk degraded map streaming and desync | both | [5] [6] |
| `MaxPacketsPerSecond` | 300 (100–1000) | Per-client ceiling on network packets the server will process | B42 | [5] |
| `MultiplayerStatisticsPeriod` | 1 (0–10) | Statistics sampling period in seconds; 0 turns statistics off | B42 | [5] |
| `PauseEmpty` | true | Halts game time when nobody is online — an idle server simulates less | both | [5] [6] |
| `SaveWorldEveryMinutes` | 0 | Periodic save of loaded map areas every N real minutes; normally saves happen as clients leave an area | both | [5] [6] |
| `PingLimit` | 0 = off (B42); 250 at the B41 revision | Kick threshold in milliseconds — a lever against high-latency clients, not server load itself | both | [5] [6] |
| `ItemNumbersLimitPerContainer` | 0 = unlimited (0–9000) | Caps items per container, counting each small item individually | B42 | [5] |
| `BloodSplatLifespanDays` | 0 = never (0–365) | Ages out blood decals; cleanup runs when chunks load | B42 | [5] |
| `DenyLoginOnOverloadedServer` | true | Refuses logins when the server is overloaded; neither "overloaded" nor its metric is defined in the reference | B42 | [5] |
| `ShowCoordinates` | false | 42.20-added operator convenience: a coordinates line on connected clients | B42 | [1] [5] |

The B41-era revision additionally documents a block of network-simulation tuning keys that the 42.20-era revision no longer lists *(B41, revision stamped 41.78.16)* [6]:

| Key | B41 default | What the B41 revision shows | Cited at |
|-----|-------------|------------------------------|----------|
| `ZombieUpdateMaxHighPriority` | 50 | Cap on zombies updated at high priority per cycle | [6] |
| `ZombieUpdateDelta` | 0.5 | Zombie network-update interval factor | [6] |
| `ZombieUpdateRadiusHighPriority` | 10.0 | Radius, in tiles, of the high-priority update zone around players | [6] |
| `ZombieUpdateRadiusLowPriority` | 45.0 | Outer radius of the low-priority update zone | [6] |
| `PhysicsDelay` | 500 | Physics update delay | [6] |
| `UseTCPForMapDownloads` | false | Transport toggle for map transfers to joining clients | [6] |

The B41 revision lists these with values but little or no semantic description; the glosses above are the minimal reading of the key names and should be treated as exactly that. Whether the B42 server still reads them is undocumented in either direction [5] [6].

On the SandboxVars side, the zombie population block (`ZombieConfig.PopulationMultiplier` and its start/peak/respawn siblings) directly controls how many zombies the world carries, which is the reason every community performance guide reaches for it — but no primary source quantifies population against RAM or CPU, so the sizing half of that advice is quarantined below (Claim 3) [5]. Two documented facts are worth restating from the sibling reference: the generated B42 file warns against changing `ZombieConfig.ZombiesCountBeforeDelete` from its default, and 42.20 raised that option's permitted maximum from 500 to 5000 — the release notes name it as the "Zombie count before deletion" sandbox option *(B42)* [1] [5].

## What 42.20 changed for server performance

The 42.20 stable release notes contain a cluster of server-performance and server-observability items — this is the primary record of where The Indie Stone itself spent optimisation effort *(B42)* [1]:

- **Monitoring surface.** The notes add "object pool statistics for improved monitoring and diagnostics for servers", improve ZNet logging consistency and configurability, improve packet-logging reliability, and fix the "SERVER STARTED" console message not printing [1]. Ping values per player were added to the Players and Users list tabs [1].
- **Hang and load fixes.** A defect that could freeze the whole server while it generated chunks was fixed, as were map chunks refusing to load for driving players, individual cells inside a chunk staying unloaded for some clients, and a server-side exception possible during dedicated-server startup [1].
- **Simulation-cost fixes.** Fixed zombie culling triggering incorrectly and collapsing zombie populations; fixed every connected player stuttering when one player built or interacted with gates; fixed a performance issue in puddle geometry; improved network performance during vehicle-zombie collisions [1].
- **Throughput improvements.** Reworked stackable-item transfers to substantially cut the time large stacks take; improved the load time between clicking start and spawning in [1].
- **Map cost containment.** The heavily overhauled map areas shipped with performance optimisations named alongside them in the notes [1].

Two implications follow from the same document. First, the anti-cheat rework (item anti-cheat now server-side, NoClip and PacketException checks still work-in-progress) moves validation work onto the server — the fact is primary, its CPU cost is not quantified anywhere and remains quarantined at the parent (foundation Claim 3) [1]. Second, several of these items (culling misfires, gate-interaction stutter, chunk-generation hangs) were live defects throughout the unstable cycle: performance observations recorded on 42.13–42.19 servers predate these fixes and should not be projected onto 42.20 [1].

## Official statements about load — all of them

The complete set of Indie Stone statements connecting an operational choice to server performance is short enough to list exhaustively:

1. **Player count.** The 42.13 unstable MP release called more than 20 players on a server inadvisable, and its companion post recommended at most 20 player slots on dedicated servers "for now" [2] [3]. At stable, the B42 settings reference defaults `MaxPlayers` to 32 and warns above 32 [5]. Neither the 20-slot advisory nor its lifting appears in the 42.20 notes [1].
2. **Debug mode.** The 42.13 release states outright that using debug during multiplayer games will negatively impact server performance [2]. This is the single most direct official performance statement on record.
3. **Mods.** The same release asked players to disable all mods, including client-side ones, during the stress-test phase [2] [3]. No official statement quantifies mod cost; the community numbers are quarantined below (Claim 1).
4. **Map streaming.** The `MaxPlayers` warning ties player count above 32 to map-streaming quality and desync [5], and the `-gui` server argument is documented as unfinished and memory-hungry [7].

That is the entire official record. Every other performance rule in circulation is inference or vendor material.

## Monitoring what the server is doing

- **Multiplayer statistics.** The `-statistic {seconds}` server argument enables periodic statistics monitoring, written under `cachedir/Statistic`; the shipped script passes `0` [4] [7]. The `.ini`-side `MultiplayerStatisticsPeriod` key (default 1, 0 disables) governs the statistics update period on B42 [5]. The output format is not documented on the cited surface — see Open Questions.
- **Object-pool statistics.** Added at 42.20 explicitly for server monitoring and diagnostics [1]. Where they surface (console vs. statistics files) is likewise not documented in the notes [1].
- **Console-log control.** `-debuglog={types}` enables named log filters and `-disablelog={types}` suppresses them, both taking comma-separated filter lists; console output goes to `console.txt`, whose size cap is settable with `-Dzomboid.ConsoleDotTxtSizeKB` (JVM side) or `-console_dot_txt_size_kb` (game side) [7].
- **ZNet logging.** Shipped on (`-Dzomboid.znetlog=1`) in the documented launch line, with 42.20 improving its consistency and configuration [1] [4].
- **In-game operator views.** 42.20 added per-player ping to the player list tabs and the `ShowCoordinates` option [1] [5].

## What is NOT documented

An honest tuning runbook has to state the negative space. None of the following exists anywhere on the primary or fact-only surface cited by this document — the launch scripts and their wiki documentation [4] [7], the B42 and B41 settings references [5] [6], or the 42.20 release notes [1]:

- **No sizing table.** No official RAM-per-player, RAM-per-mod, or RAM-per-population figure for either build. Every such table is hosting-company or community material (foundation Claim 1; Claims 1–3 below).
- **No CPU guidance.** No statement on threading, core scaling, or clock-speed preference (foundation Claim 3).
- **No map/chunk tuning keys.** No documented `.ini` or SandboxVars key controls chunk cache size, streaming distance, or world-partition behaviour; the chunk layer appears in the record only as fixes [1] and as the map-streaming warning on `MaxPlayers` [5].
- **No GC tuning guidance.** The scripts select ZGC [4], and the wiki documents `-XX:+AlwaysPreTouch` as its recommended companion [7]; beyond that, no official heap-tuning or pause-time guidance exists.
- **No mod budget.** No documented per-mod cost model of any kind [2].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Default player cap | `MaxPlayers` 16 at the pinned revision [6] | 32, range 1–100, with an explicit above-32 map-streaming/desync warning [5] |
| Zombie network tuning | `ZombieUpdateMaxHighPriority` / `ZombieUpdateDelta` / radius pair documented with defaults 50 / 0.5 / 10.0 / 45.0, plus `PhysicsDelay` 500 and `UseTCPForMapDownloads` [6] | None of these keys appear in the 42.20-era settings revision; no removal note exists either [5] |
| Rate/statistics keys | Not present at the B41 revision [6] | `MaxPacketsPerSecond` (300, 100–1000) and `MultiplayerStatisticsPeriod` (1, 0–10) documented [5] |
| Launch memory default | Not verified against a B41-era script in this document | 16 GB in `StartServer64.bat`, must be edited down; 6 GB worked example [4] |
| Garbage collector | Not verified against a B41-era script | `-XX:+UseZGC` in the documented launch line [4] |
| Monitoring | `-statistic` argument predates the pinned pages' build stamps in neither direction — verified only at the 42.17-stamped revision [7] | Object-pool statistics, improved ZNet/packet logging, per-player ping columns added at 42.20 [1] |
| Server-side work | Client-trusting anti-cheat model | Item anti-cheat moved server-side at 42.20; validation cost shifted to the server, magnitude undocumented [1] |
| Known stable-cycle perf defects | Long-stable branch | 42.20 fixed chunk-generation hangs, zombie-culling collapse, gate-interaction stutter, puddle-geometry cost — all present during the unstable cycle [1] |
| Zombie cleanup ceiling | Not applicable at the pinned B41 revision | "Zombie count before deletion" maximum raised 500 → 5000 at 42.20 [1] |
| Player-scale advisory | None on record | ≤ 20 slots advised at 42.13 unstable; not re-stated or rescinded at 42.20 [1] [2] [3] |

Summary: B41's documented tuning surface is a set of low-level network-update knobs with no B42 counterpart; B42's is a higher-level surface — packet caps, statistics, warnings — plus a JVM layer (ZGC, 16 GB default) that the current wiki record only attests for B42 [4] [5] [6].

# Practical Guidance

An ops sequence built only from the cited facts:

1. **Set the heap before first boot.** Edit `-Xms`/`-Xmx` in `StartServer64.bat` (Windows) or `ProjectZomboid64.json` (Linux) down from 16 GB to fit the host, keeping the shipped shape of equal values; the wiki's 6 GB example is the documented small-server starting point. Never set `-Xmx` above physical RAM minus the OS's own needs — the documented behaviour is paging, which will present as lag long before it presents as an error.
2. **Turn monitoring on before you need it.** The shipped `-statistic 0` means no statistics. Set a nonzero period (the documented example is `-statistic 10`) on any server you intend to diagnose, and leave `MultiplayerStatisticsPeriod` at its default 1 rather than 0. After 42.20, watch the console for object-pool statistics and use the player-list ping columns as your first desync triage view.
3. **Respect the two player-count lines.** 20 slots is the last explicit official advisory (42.13, unstable-era); 32 is where the B42 settings reference itself warns of map-streaming degradation. Between them is judgement; beyond 32 is documented risk.
4. **Keep debug off in production.** The one performance rule The Indie Stone has stated plainly. If you need debug output, prefer `-debuglog` filters over debug mode, and cap `console.txt` growth with the documented size settings on busy servers.
5. **Treat mods as your least-documented load.** The official record says only "disable them" (stress-test era); the cost numbers are vendor folklore (Claim 1). Stage mod-list changes on a copy and measure, because no table will tell you.
6. **Leave the B41 quartet alone on B42.** `ZombieUpdateDelta` and its siblings are attested at B41 only. Copying a B41 tuning block into a B42 `.ini` puts you in undocumented territory twice over — unknown keys, unknown effect.
7. **Use the built-in idle and cleanup levers.** `PauseEmpty` (default on) already stops time on an empty server; `BloodSplatLifespanDays` and corpse/loot timers (see the sibling references) bound world-object accumulation; respect the in-file warning on `ZombieConfig.ZombiesCountBeforeDelete`.
8. **Re-baseline after 42.20.** Several unstable-era performance complaints (hangs during chunk generation, stutter on gate interactions, population collapse) were fixed at stable. Do not carry a 42.1x tuning workaround forward without re-testing it against 42.20.

# Common Pitfalls & Troubleshooting

- **Server will not start; memory errors in the console.** The 16 GB shipped default exceeds the host, or `-Xms` demands more than the system can allocate — both documented failure modes [4] [7]. Lower both values.
- **Server runs but everything is sluggish; the OS shows heavy swap/pagefile use.** `-Xmx` above physical RAM is documented to fall through to virtual memory rather than fail [7]. Size the heap below physical RAM.
- **Raised `MaxPlayers` past 32, now clients report missing map areas and rubber-banding.** That is the documented above-32 risk: degraded map streaming and desync [5]. Reduce the cap before touching anything else.
- **Ran a MP session with debug enabled "just to check something" and the tick rate collapsed.** Officially predicted behaviour [2]. Use `-debuglog` filters instead.
- **No statistics to look at during an incident.** The shipped script disables sampling (`-statistic 0`) [4]. Monitoring is opt-in; enable it during calm, not during the fire.
- **Copied a B41 "network optimisation" `.ini` block onto a B42 server.** The quartet is undocumented on B42 [5] [6]; at best inert, at worst untested behaviour. Remove it.
- **Diagnosing 42.20 with 42.13-era lore.** The culling, gate-stutter and chunk-hang defects that drove much unstable-era advice are fixed at 42.20 [1]; re-measure before re-applying old workarounds.
- **Buying RAM off a vendor table.** The tables conflict with each other by roughly a factor of two (foundation Claim 1; Claims 1–2 below). Size empirically: start at the documented 6 GB example and grow on observed usage.

# Community Notes & Unverified Claims

The two headline sizing claims — B42 needs ~+2 GB RAM per player tier, and server performance is single-thread-CPU-bound — are already quarantined at the parent (`admins-foundation`, Claims 1 and 3). Research for this document surfaced no new primary evidence in either direction, so they are not re-litigated here. The claims below are additional and narrower.

## Claim 1 — Mod count is the dominant RAM multiplier, with heavy mod lists adding 8 GB or more

- **Claim:** Hosting knowledge bases size modded servers far above vanilla: one vendor's tiering adds roughly 2 GB for a light mod list and 8–12 GB for 30+ mods, singling out one large weapons mod as worth 1–2 GB alone [9]; another's B42 table runs from 10 GB vanilla to 32 GB+ for heavy mod lists at high player counts [10]. The open-source Ubuntu guide points the same direction, recommending 8 GB "with mods" against a 4 GB minimum [8].
- **Why unverified:** No primary source quantifies mod cost at all — the only official mod-performance statement is the 42.13-era instruction to disable them [2] [3]. The vendor magnitudes disagree with each other substantially even while agreeing on direction.
- **Confidence:** Medium. Three independent secondary sources agree directionally and the mechanism (more content loaded per mod) is plausible, but every number is non-primary and the spread between vendors is large.

## Claim 2 — Long-term memory growth tracks explored map area: an old, well-explored world costs more than a fresh one

- **Claim:** Vendor guidance attributes baseline RAM growth to map exploration — the server holding streamed chunks for visited areas [9] — and describes long-running worlds with large built-up bases and wide exploration as heavier than fresh ones [10].
- **Why unverified:** The primary record documents chunk streaming, chunk saving and chunk-related fixes as mechanisms [1] [5], but no official source states that resident memory scales with explored area or world age, and no measurement methodology is published by the vendors making the claim.
- **Confidence:** Medium. Two independent secondary sources agree, and the claim is consistent with the documented chunk architecture — but it rests entirely on unquantified vendor assertions.

## Claim 3 — Raising zombie population multipliers materially raises RAM, roughly +20–30% for a peak multiplier of 2.0

- **Claim:** One hosting KB states that setting `ZombieConfig.PopulationPeakMultiplier` to 2.0 instead of the default 1.5 adds roughly 20–30% RAM usage [9].
- **Why unverified:** Single-sourced from a marketing-adjacent vendor; no primary source connects population settings to memory numbers, and the other vendor's B42 sizing article carries no population guidance at all [10].
- **Confidence:** Low. Direction is plausible (more simulated zombies is not free), but the specific percentage is sole-sourced and, under this knowledge base's rules, could not be stated above Medium even if corroborated.

# Risks & Caveats

- **The Startup parameters page lags stable.** Flag-level semantics cited to [7] were last updated for 42.17.0; the launch-line facts cross-check against the 42.20-versioned Dedicated server page [4], but a 42.20 revision of the flag table would strengthen several rows.
- **B41 evidence is one archived revision.** Every B41-tagged value here traces to the single archived 41.78.16-stamped Server settings revision [6]; pzwiki's live site refused automated retrieval during this document's research, so verification went through the Internet Archive copy.
- **Silence is not removal.** The absence of the `ZombieUpdate*` quartet from the B42-era revision [5] shows the documentation dropped them, not that the code did; the sibling `.ini` reference makes the same point and it bears repeating wherever tuning advice depends on it.
- **The 42.13 advisories are frozen in amber.** The ≤20-slot and mods-off guidance was written for a stress-test build [2] [3] and has been neither renewed nor withdrawn at 42.20 [1]; this document treats it as the last word only because it is the *only* word.
- **Day-two stable.** 42.20 is days old; hotfixes may alter any release-note-derived fact here, and the object-pool statistics surface in particular is new and undescribed [1].
- **All sizing numbers here are quarantined for a reason.** If a future Indie Stone post publishes sizing guidance (the GSP feedback channel makes this plausible), Claims 1–3 and the foundation's Claims 1 and 3 should be re-graded immediately.

# Verification Steps

1. **Verify the launch line:** install the dedicated server (App ID 380870), open `StartServer64.bat`, and confirm the 16 GB `-Xms`/`-Xmx` default and the flag set (`-XX:+UseZGC`, `-Dzomboid.znetlog=1`, `-statistic 0`) against the table above.
2. **Verify the memory failure modes:** on a test host, set `-Xms` above available RAM and confirm the startup failure; then set `-Xmx` above physical RAM but within virtual memory and observe paging rather than failure.
3. **Verify the Linux config path:** open `ProjectZomboid64.json` in a Linux install and locate the `-Xmx` entry the Ubuntu guide edits.
4. **Verify the statistics subsystem:** launch with `-statistic 10`, play a client in, and inspect the `Statistic` directory under the cache dir for output; flip `MultiplayerStatisticsPeriod` to 0 and confirm sampling stops.
5. **Verify the release-note items:** query the ISteamNews API (app 108600) and read the 42.20 announcement's MP section for the object-pool, ZNet-logging, chunk-hang and culling items quoted here.
6. **Verify the settings rows:** run `showoptions` on a live 42.20 server and compare `MaxPlayers`, `MaxPacketsPerSecond`, `MultiplayerStatisticsPeriod`, `PauseEmpty` defaults against the table.
7. **Probe the undocumented:** grep a B42 server's generated `.ini` for `ZombieUpdateDelta` (expected: absent) and, on a throwaway B41 server, present (defaults 0.5 etc.).
8. **Probe Claim 2:** snapshot server RSS on a fresh world, then after systematically driving the map perimeter, and compare — a cheap first datum for the world-age claim.

# Open Questions

- What do the 42.20 object-pool statistics actually emit, and where — console, `console.txt`, or the statistics directory? The release note names the feature without describing its output [1].
- What metric triggers `DenyLoginOnOverloadedServer`, and is it connected to the statistics subsystem? The B42 reference lists the key without semantics [5].
- Does the B42 server still parse the B41 tuning quartet (`ZombieUpdateDelta` et al.), and if not, when were they retired? A changelog entry or code-level check would resolve it [5] [6].
- Is the 42.13 ≤20-slot advisory considered lifted at 42.20? A single sentence from The Indie Stone would settle the largest open operational question on record [1] [2] [3].
- What is the multiplayer statistics file format, and is it stable enough for external monitoring tooling to consume?
- Will the GSP feedback channel produce the first official sizing guidance, retiring Claims 1–3 and the foundation's sizing quarantine?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; full changelist retrieved via the ISteamNews API mirror, app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *Unstable 42 MP Released* (Steam announcement, 2025-12-11; ≤20-player advisory, debug-mode performance warning, mods-off guidance). https://steamcommunity.com/games/108600/announcements/detail/1818752592123010. Accessed 2026-07-31.
- [3] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11; ≤20 dedicated player-slot recommendation). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972. Accessed 2026-07-31.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [4] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0; launch scripts, JVM line, memory defaults). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Server settings*, archived Build 41 revision (revision 157571; page stamped Version 41.78.16, last edited 2023-10-22). https://pzwiki.net/w/index.php?title=Server_settings&oldid=157571 — verified via the preserved copy at https://web.archive.org/web/20231028101749/https://pzwiki.net/wiki/Server_settings. Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *Startup parameters* (revision 1393745; page marked last updated for 42.17.0). https://pzwiki.net/w/index.php?title=Startup_parameters&oldid=1393745. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [8] **Bobagi** — *Project-Zomboid-Ubuntu-Server* (MIT; Ubuntu dedicated-server guide; `ProjectZomboid64.json` memory configuration, 4/8 GB guidance). https://github.com/Bobagi/Project-Zomboid-Ubuntu-Server. Accessed 2026-07-31.
- [9] **DoomHosting** — *Project Zomboid Server RAM Requirements (Build 41 vs Build 42)* (hosting KB; corroborate-only; mod tiers, population-RAM figure, chunk-streaming claim). https://www.doomhosting.com/help/articles/project-zomboid-server-ram-requirements. Accessed 2026-07-31.
- [10] **Pinehosting** — *How Much RAM Do You Need For Build 42 Project Zomboid Server Hosting?* (hosting KB; corroborate-only; B42 RAM table, world-age claim). https://pinehosting.com/blog/how-much-ram-do-you-need-for-build-42-project-zomboid-server-hosting/. Accessed 2026-07-31.

**Community & Creator**

- None cited.

**Further Reading**

# Further Reading

- The ISteamNews API mirror used to verify all announcement citations: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- Oracle's HotSpot garbage-collection tuning guide, which the Startup parameters page cites for the ZGC/`AlwaysPreTouch` recommendation: https://docs.oracle.com/en/java/javase/21/gctuning/
- The official blog / Thursdoid feed (bot-blocks automated checkers; read in-browser): https://projectzomboid.com/blog/
- `admins-foundation`'s Verification Steps, which include the empirical B41-vs-B42 memory comparison this document's sizing caveats depend on.

# Related Documents

- `admins-foundation` — the parent overview; owns the RAM/CPU evidence framing and the quarantined "+2 GB" and single-thread claims this document references.
- `admins-server-ini-reference` — the full per-key `.ini` catalogue behind the performance subset tabled here.
- `admins-sandboxvars-reference` — the full SandboxVars catalogue, including the zombie population block and its in-file warnings.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
