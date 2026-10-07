---
id: admins-modded-server-runbook
title: "Running a Modded Server: Selection, Rollout and Update Discipline"
version: 0.2.0
status: in-review
confidence: Medium
category: Admins
topic: "Server runbooks"
build: both
document_type: tutorial
created: 2026-07-31
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [admins-foundation, admins-workshop-mod-wiring, admins-ubuntu-runbook, admins-backups-migration, meta-style-guide]
tags: [dedicated-server, mods, workshop, updates, rollout, staging, troubleshooting, b42, legacy41]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-modded-server-runbook |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 |

# Executive Summary

`admins-workshop-mod-wiring` documents the mechanics of getting a mod's two
identifiers correctly paired into `servertest.ini`; `admins-foundation` maps
where mods sit in the broader server-configuration picture. Neither addresses
the discipline that keeps a modded server healthy over months of operation:
how to judge whether a mod is safe to add in the first place, how to test it
before a live audience sees it, what happens — mechanically and operationally
— when the game itself patches or a subscribed mod updates underneath a
running server, and what the common failure signatures look like when this
discipline slips. This document is that operational runbook.

The throughline across every primary and fact-only source examined is the
same: Project Zomboid's own client documents mods as version-specific and
both directions of a version change (a mod updating, or the game updating) as
carrying a real risk that "the game will not launch properly" [4]. Steam
Workshop applies mod updates automatically and with no built-in revision-pin
mechanism, so a live server's cached mod state can silently drift from what
Steam now serves a reconnecting client — a real enough operational problem
that a purpose-built Workshop mod with five-figure subscriber counts exists
specifically to detect and manage it from the server side [12]. Because no
official RAM/CPU sizing table exists (per `admins-foundation` and
`admins-performance-tuning`'s quarantines) and no official mod-compatibility
certification exists either, most of the judgement calls in this document
rest on reading a mod's own Workshop page and mod.info fields directly,
supplemented by the one documented local procedure for testing a mod in
multiplayer before it ever reaches a real server [6].

Document-level confidence is **Medium**: the mechanics this document leans on
— the mod manager's version/dependency fields, the restart-required posture
of mod-list changes, the documented MP test procedure, and the pzwiki
troubleshooting workflow — are pinned to fact-only wiki revisions and the
game's own Workshop/mod-manager surfaces (High); the cadence and staging
*recommendations* built on top of them are this document's own synthesis, and
the handful of hard operational claims about log-error text and rollout
tooling that could not be traced to a primary source are quarantined below
rather than asserted as fact.

# Key Takeaways

- Steam Workshop's build-version tags (Build 40/41/42) are an official,
  predefined category set — the `tags` parameter of `workshop.txt` is
  documented as "Predefined by Project Zomboid Workshop" *(cited)* *(both)*
  — but which tag a given mod carries is author-selected, not
  Valve/TIS-verified; treat a tag as a first filter, not a compatibility
  guarantee *(cited)* *(both)*
- The in-game mod manager surfaces the authoritative per-mod compatibility
  fields — minimum/maximum game version, dependencies, incompatibilities —
  read directly from each mod's own `mod.info` *(cited)* *(both)*
- No live-reload path covers `Mods=`/`WorkshopItems=` changes; every mod-list
  change is restart-required and should be treated as a scheduled-maintenance
  event, never a casual hot edit *(cited synthesis, deepened at
  `admins-workshop-mod-wiring`)* *(both)*
- Singleplayer testing does not exercise multiplayer-specific code paths —
  the wiki documents a dedicated local two-instance procedure for testing a
  mod in MP before it ever reaches a real server *(cited)* *(both)*
- The base game's own UI states that *either* side of a version pairing
  changing carries launch risk: a mod updating, or the game version updating,
  while a mod is active in the main menu *(cited)* *(both)*
- Steam Workshop auto-updates a subscribed item with no built-in revision pin
  — the closest thing to a documented mitigation is restart discipline, or
  vendoring a mod into the local `mods/` folder per `admins-workshop-mod-wiring`
  *(cited)* *(both)*
- A dated community bug report shows a concrete "mod won't load on the
  server" log signature (`ERROR: mods isn't a valid workshop item ID`;
  `required mod "..." not found`) traceable to the B41→B42 mod-folder
  restructuring — a real but build-transition-era data point, not a
  guaranteed-permanent signature *(community, dated)* *(B42)*
- Backing up before any mod-list change to an existing save is
  primary-documented advice, not just prudence: the wiki's own troubleshooting
  page states a save "broke" by a mod can become "permanently broken" if the
  fix doesn't hold *(cited)* *(both)*

# Purpose

This document answers the questions an admin who already knows *how* to wire
a mod into `servertest.ini` (`admins-workshop-mod-wiring`) still has to answer
for every mod, every game patch, and every Workshop update, indefinitely: is
this mod safe to add to a community server, how do I find out before my
players do, what do I do differently when the game itself patches versus when
a mod I'm running patches, and what does it look like on the console when
this goes wrong? It is the process layer sitting above the mechanical
reference documents, aimed at the admin who has to keep a modded server
healthy across seasons, not just stand one up once.

# Scope

Covered: criteria for evaluating a candidate mod before it reaches a live
server (Workshop tags, mod.info version/dependency fields, update recency,
Workshop-page signals); staging discipline (why and how to test a mod-list
change, including multiplayer-specific testing, before it reaches production);
what changes, mechanically and operationally, when the game patches versus
when a subscribed mod updates; a recommended pinning/freeze posture given that
no revision-pin mechanism exists; the common modded-server failure modes this
document could trace to a citable signature (server fails to start/load a
mod, a mod that behaves differently in multiplayer than singleplayer,
diagnosing which mod in a large list is responsible); and a recommended
update-checking cadence, including when to deliberately defer.

Not covered: the `Mods=`/`WorkshopItems=` `.ini` syntax, the Mod ID vs
Workshop ID distinction, `require=`/`versionMin` mechanics in depth, and
`-modfolders` load-order semantics — all owned by `admins-workshop-mod-wiring`,
linked throughout rather than repeated; Ubuntu/systemd process setup, owned by
`admins-ubuntu-runbook`; backup mechanics and restore procedure, owned by
`admins-backups-migration` (referenced here only as "back up before a mod
change," never re-derived); and mod development itself, which belongs to the
Modders track.

# Definitions

- **Workshop tag** — a category label attached to a Steam Workshop item from
  a predefined list the game itself supplies (including build-version tags
  Build 40/41/42); author-applied, not independently verified [8] [13].
- **Staging** — running a candidate mod-list change against a non-production
  copy of the world (or a fresh throwaway world) before applying the same
  change to the live server's configuration.
- **Freeze / pin** — deliberately preventing a mod (or the game build) from
  updating on a running server, either by restart discipline or by vendoring
  a mod's files locally in place of the Workshop auto-fetch path (see
  `admins-workshop-mod-wiring`).
- **"Red mod"** — the client mod manager's visual indicator that an active
  mod is missing a dependency it declares via `require=`; the missing item is
  named on the mod's own Workshop page under "Required Items" [5].
- **Bifurcation testing** — the wiki's own documented method for isolating
  which mod among a large list causes a given problem: repeatedly halving the
  active mod set and reproducing the issue against each half [5].
- **Workshop "Update Required" state** — a per-item download-state label
  distinct from "Installed," meaning the client or server's cached copy is
  stale relative to what Steam currently serves for that item [13] [14].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | The mod-manager version/dependency fields, the restart-required posture, and the backup-before-mod-change advice are documented on wiki pages not separately versioned for B41; the underlying mechanism (mods are version-specific, main-menu mod changes are launch-risk) is generic client behaviour with no build-specific carve-out in the sources found [4] [5]; the legacy line's latest primary-attested hotfix is 41.78.21 (2026-08-26), published in a combined post with 42.20.4 [20] |
| B42 (stable) | Yes | 42.20; notes reviewed to 42.21 | 42.21 has been the stable build since 2026-09-28 [22]. The B41→B42 mod-folder restructuring (deepened in `admins-workshop-mod-wiring`) is the one build-specific fact this document leans on; the dated forum log signature [16] is from the 42.13-era unstable-MP stress-test window, not re-verified against 42.20 or 42.21 |

Re-baseline note (0.2.0): this revision re-checked the document against the six Steam announcements from 42.20.1 through 42.21 stable [17] [18] [19] [20] [21] [22] and the abridged TIS forum changelist for 42.21 [23], looking for changes to modded-server operation. Every other statement, including the wiki-derived mechanics and the quoted log lines, is carried forward from the 42.20 review with no contradicting change found in those notes; it was not re-tested on 42.21.

Several fact-only pages cited here — the `Mods` reference [4], the mod
problem-solving guide [5], and the multiplayer mod-testing walkthrough [6] —
self-flag as documenting behaviour last substantively verified for 41.78.19
or 42.14.0 even though the wiki's current stable target is 42.20.0; where
that matters, this document says so inline rather than presenting the fact
as freshly re-verified.

# Reference

## Evaluating a mod before it reaches a live server

Steam Workshop's category tags for Project Zomboid include a predefined
build-version set — Build 40, Build 41, Build 42 — confirmed both by the
public Workshop browse page's own tag filter list and by the fact that
`workshop.txt`'s `tags` parameter is documented as "Predefined by Project
Zomboid Workshop" rather than free text [8] [13]. That predefined list is the
game's, but *which* tags a specific mod carries is chosen by its author when
uploading, and neither Valve nor The Indie Stone independently verifies the
claim. A real, dated example makes the distinction concrete: the mod "Neat
Building [B42]" (Workshop ID 3536052310) carries the tags Build 42, Building,
Interface, Multiplayer, QoL and WIP, and states directly in its own
description, outside the tag system entirely, "Build Support: B42.12 to
B42.20.x — Build 42 only," together with an explicit dependency note
("NeatUI Framework is required... and must be loaded before Neat Building")
and per-variant multiplayer guidance ("choose carefully, especially for
multiplayer saves") [11]. None of that build-support text is a tag; it is
prose the author chose to write, current only as of that mod's own last
"Updated" timestamp on the page.

The authoritative per-mod compatibility surface is not the Workshop page but
the in-game mod manager, which lists "the minimum and maximum game version,
dependencies, incompatibilities" for every mod alongside its mod ID and
Workshop ID [4]. Those minimum/maximum fields are read from the mod's own
`mod.info` [7]; at least one of them has a documented display quirk worth
knowing before trusting the error text literally — a bug logged against game
version 42.12.3 (reconfirmed for maximum-version gating at 42.13.0) shows that
setting a mod's minimum-version field to something *newer* than the running
game produces a message written for the opposite situation ("mod must be
updated to 42.0+ version"), reading as "too old" when the real cause is "too
new" [3]. Dependency and incompatibility metadata is likewise visible before
the mod ever runs: `mod.info`'s `require=` field names other Mod IDs a mod
needs [7], and the client-side symptom of a wired mod missing one of its
declared dependencies is the mod showing red in the mod menu, with the
specific missing item named on that mod's own Workshop page under "Required
Items" [5].

Recency and community-reported problems are both visible on the mod's own
Workshop page without leaving Steam: the "Posted"/"Updated" timestamps, any
build-support statement the author chose to add to the description, and the
page's own discussion/comment threads. A secondary risk-tiering framework
built specifically around Build 42's still-settling mod ecosystem recommends
recording the Workshop ID, title, author and last-update date for every mod
before enabling it, explicitly warning that a bare display name without a
Workshop ID is not verifiable — the framework's own worked example is a mod
("Become Desensitized") that exists simultaneously as a current Build 42
version, a separately-listed "OUTDATED" Build 42 fork, and an original Build
41 version, all under different Workshop IDs [14]. The existence of that
fork pattern is itself evidence for a broader, less precisely quantifiable
claim: not every Build 41 mod has been ported to Build 42, and a Build
41-only package is unsupported on B42 until its author updates it — a claim
this document's sources support directionally (the same secondary framework
states "Build 41-only packages are unsupported on B42 until updated, and
forcing unsupported mods is a deliberate risk," while also noting "many
authors already ship Build 42 builds" [14]) without a citable count of how
many mods remain unported.

## Staging discipline: proving a change before it is live

No live-reload path exists for mod-list changes. `admins-workshop-mod-wiring`
and the sibling settings reference establish this at length: only `.ini` key
changes have a documented live-apply mechanism (`reloadoptions`), and no
source found documents an equivalent path for `Mods=`/`WorkshopItems=` [9]
[10]. The operational consequence this document adds is that a mod-list
change is never a quick edit — it is a scheduled-restart event, and should be
planned and staged like one.

Changing the active mod list on an existing save carries a direct,
primary-documented warning, not just general caution: the wiki's own guidance
for changing mods in a save already in progress is to "make sure to backup
your save beforehand" [4], and its troubleshooting counterpart states the
failure mode in blunter terms — if adding a mod "broke the save," the
documented fallback is removing the mod and reloading, and "if that doesn't
help, then your save is permanently broken. Before adding mods to an old
save, it is highly recommended to make a backup save!" [5]. Paired with
`admins-backups-migration`'s cold-backup procedure, that is the entire
staging precondition in one sentence: never change a live world's mod list
without a fresh, verified backup already in hand.

Singleplayer testing does not exercise multiplayer-specific code paths, which
is exactly why a dedicated wiki procedure exists for testing a mod in
multiplayer rather than trusting a singleplayer session to stand in for it.
The documented method runs two local game instances against each other: an
admin instance launched with `-nosteam -debug`, hosting a server through the
in-client "Manage Settings" → Mods screen with the candidate mod added to the
list, and a second, non-debug `-nosteam` instance joining that host at the
loopback address as an ordinary client [6]. This costs nothing beyond a
second game launch on the same machine and is the one documented way to
confirm multiplayer-specific behaviour — server/client sync, anything gated
behind the network layer — before a mod is trusted on a real server's player
base. The same wiki page is explicitly flagged as needing a rewrite and as
last verified for 41.78.19 [6], so treat the exact menu labels as
directionally correct and re-confirm them against the current client.

The staging target itself should be a copy, never the production save:
duplicate the whole `Zomboid` data tree (per `admins-backups-migration`'s
backup unit) or start a fresh throwaway world, apply the candidate mod-list
change there, confirm the server actually starts and a client can connect and
play a meaningful session, and only then repeat the identical `Mods=`/
`WorkshopItems=` change against the production `.ini` at a scheduled restart.

## Update rollout: what changes when the game patches, and when a mod does

The base game's own mod-management surface states plainly that *either*
direction of a version pairing changing is a launch risk while a mod is
active in the main menu: "With every mod update, there is a risk that the
game will not launch properly, if the mod is active in the main menu," and
"With every game version update, there is a risk that the game will not
launch properly for each mod active in the main menu" [4]. Both sentences
point at the same operational rule: re-verify the active mod list after
*either* side of the pairing changes — a Workshop mod updating, or the server
itself moving to a new game patch — not only after whichever one an admin
happens to notice first.

Steam Workshop applies updates to a subscribed item automatically and, per
`admins-workshop-mod-wiring`'s exhaustive search of SteamCMD and `.ini`
mechanisms, with no documented way to pin an individual Workshop item to an
older revision. The practical consequence is that a long-running server's
cached copy of a mod can silently drift from what Steam now serves a
reconnecting or newly-joining client — the exact situation the Workshop's own
"Update Required" download-state label describes [13] [14], and specifically
the market a purpose-built Workshop mod exists to address: "Server Workshop
Mod Update Checker & Auto-Restart (B42) MP" (Workshop ID 3659447892; over
10,180 subscribers as of this document's research) frames its own purpose as
ending admins "waking up to 'Workshop Version Mismatch' errors," polling
Steam for item updates on a configurable timer, warning connected players
with in-game alerts, and performing a fail-safe shutdown/restart sequence so
the update lands cleanly [12]. That a tool at this scale of adoption exists
at all is itself evidence that unmanaged Workshop auto-update is a real,
recurring operational problem for modded servers, independent of whatever
this document can or cannot quantify about its frequency.

The one place The Indie Stone directly addressed mods as a rollout risk
factor is the Build 42.13 unstable multiplayer release: during that
stress-test phase, the documented guidance was to disable all mods, including
client-side ones [2] (already established at `admins-foundation` and
`admins-performance-tuning`). That guidance was written for an unstable
stress-test window and has not been restated or rescinded for 42.20 stable
[1], and the 42.21 stable announcement and unstable-release notes reviewed do not
restate it either [21] [22]; it is nonetheless the clearest official signal that the developers
themselves treat a build transition and an active mod list as a combination
worth separating rather than testing together.

A concrete, dated illustration of this exact interaction going wrong: a
community Help-forum report describes a dedicated server, running an unstable
Build 42 branch, failing to load a Workshop mod its author had already
updated for compatibility. The server console showed the item downloading
and installing successfully (`Workshop: item state CheckItemState -> Ready
ID=2544353492`) but then failing to activate it (`ERROR: mods isn't a valid
workshop item ID`; `WARN : Mod ... ZomboidFileSystem.loadModAndRequired>
required mod "P4HasBeenRead" not found`), with the full log preserved as
`DebugLog-server.txt` [16]. A reply in the same thread attributes the failure
to the mod-folder format changing between Build 41 and 42, during the same
period when multiplayer mod support itself was described as not yet in place
["We do not support mods in MP as far as I am aware at the moment..." [16]].
This is one dated, build-transition-era data point from a community forum
thread, not a confirmed-permanent signature of current 42.20 behaviour — but
it is a real example of exactly the log lines the Common Pitfalls section
below tells an admin to search for.

## What changed from 42.20.1 through 42.21 for modded servers

Six official posts sit between the 42.20.0 baseline and today's stable, and
several bear directly on how a modded server behaves. They are grouped by
operational effect rather than by date.

**Lua checksum validation.** The 42.20.1 hotfix lists "improved Lua checksum
validation for multiplayer anti-cheat" [17]. The notes do not say what the
server does when a client's mod Lua differs from the server's, so this
document treats the exact mismatch behaviour as unspecified (see Open
Questions) *(B42)*.

**Percent signs in mod translation strings.** 42.20.1 changed how percent
symbols in translation files are handled and tells mod authors to write `%%`
for a literal `%` [17]. 42.20.2 added a temporary workaround that accepts both
styles, writes error-log entries naming the offending strings, and states that
the workaround will be removed in a future unstable update [18] *(B42)*. For a
server admin, error-log lines of that kind point at a mod's translation files;
the fix belongs to the mod author (see `modders-lua-api-surface` and the
other Modders documents for the author-side detail).

**`loadstring` and `loadstream`.** The 42.20.4 hotfix removed both Lua methods
as part of a security fix. It told authors who used them to execute code sent
from the server to create the necessary methods and call them by sending the
appropriate commands instead [20]. 42.21 re-enabled both methods, with an
apology to modders and server admins for the disruption [21] [22] *(B42)*. The
42.20.4 post covers 42.20.4 stable, 42.19.2 unstable and 41.78.21 legacy
together and does not separate the Lua change by build [20], so its effect on
the legacy line is not established here.

**Connection and server-browser changes in 42.21.** 42.21 adds a notification
for players who try to connect to a multiplayer server running a different game
version [21] [23]. It also fixes an exploit that let players enter dedicated
servers without correctly authenticating through Steam, which had prevented
SteamID bans, and makes the server browser's "Server Update" column show the
last wipe rather than the last restart [21] [23] *(B42)*. 42.20.3 added support
for up to 254 players and administrator access when a server is full [19]
*(B42)*.

**Stability fixes.** 42.20.1 fixed a chunk-unloading performance problem on
multiplayer servers and a memory leak that could cause degradation and crashes
over time [17]; 42.21 fixed a further memory leak tied to eating food directly
from a vehicle trunk [23] *(B42)*.

**Release cadence.** The 42.21 stable post states that going forward a new
update goes to Unstable, is tested by the community, may change further, and
then goes to Stable [22].

## Recommended pinning / freeze posture

Because no `.ini` or SteamCMD mechanism pins a Workshop item's revision, the
only documented way to genuinely freeze a mod at a known-good version is the
one `admins-workshop-mod-wiring` establishes: vendor the mod's files into the
server's local `mods/` folder and use the `-modfolders` startup parameter to
make the game prefer that local copy over the Workshop cache. That trade
costs the server the Workshop's automatic-fetch convenience and adds a manual
re-sync obligation whenever the admin does want the update — reserve it for
mods a community depends on heavily (a shared framework, a heavily-customised
map), not as a blanket policy for an entire mod list.

Absent vendoring, the practical freeze mechanism is procedural rather than
technical: a Workshop update only reaches a running server's active world the
next time the server process restarts against the refreshed cache, so
restart discipline *is* the pin. Delaying a scheduled restart is, in effect,
delaying every mod update queued behind it — which is a deliberate lever, not
an accident, once an admin knows to treat it that way.

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 / 42.21 *(B42)* |
|------|---------------------|----------------------|
| Mod folder layout an evaluated mod must match | Flat `media/` layout (established in `admins-workshop-mod-wiring`; not re-derived here) | Versioned `common/` + `42.x` folder structure; a Build 41-only package needs author restructuring before it runs at all, which is the direct cause of the log signature this document traces in [16] |
| Workshop tag set | Same predefined tag list, including a "Build 41" category [13] | Same mechanism, with "Build 42" added as its own predefined category [13] |
| Version-gate display bug (`versionMin` read as "too old" when actually "too new") | Not verified against a B41-era mod.info revision in this document | Logged and reconfirmed against 42.12.3/42.13.0 [3] |
| Official mods-as-rollout-risk statement | None on record | 42.13 unstable MP release: disable all mods, including client-side, during the stress-test phase [2] |
| Documented MP mod support status at the time of the cited failure signature | Long-stable MP; not the subject of the cited thread | Reply in the cited 2025-12-12 thread describes MP mod support as not yet in place "at the moment," during the unstable-MP window [16] |
| Restart-required posture for mod-list changes | Same posture, same absence of a documented live-reload path [9] [10] | Same [9] [10] |
| `loadstring`/`loadstream` availability | Per-build scope of the 42.20.4 removal not stated in the combined 41.78.21 post [20] | Removed in 42.20.4 [20]; re-enabled in 42.21 [22] |
| Lua checksum validation | Not mentioned in the 41.78.21 post [20] | Improved in 42.20.1 [17] |
| Notice on connecting with a different game version | Not mentioned in the sources reviewed | Added in 42.21 [21] [23] |

The one-line version: the *discipline* this document describes — evaluate
before adding, stage before rolling out, back up before touching an existing
save, restart rather than trust a live edit — is unchanged across the build
split; what changed at the B41→B42 boundary is the mod-folder layout a
candidate mod has to satisfy, which is the single largest reason a
previously-fine B41 mod can fail the evaluation step outright on B42 until
its author restructures it [16].

# Practical Guidance

**A pre-flight checklist for adding any mod to a live server:**

1. Open the mod's own Workshop page by its numeric Workshop ID (never trust a
   bare display name — forks and renames of the same title exist under
   different IDs) [14]. Record title, author, Workshop ID and the page's own
   "Posted"/"Updated" dates.
2. Read the tags for a build-version match, but do not stop there — read the
   description itself for an explicit build-support statement and any
   multiplayer-specific guidance the author wrote [11].
3. After subscribing, open the mod in the in-game mod manager and read its
   minimum/maximum game version, dependencies and incompatibilities directly
   [4]. Cross-check every dependency it declares against your own `Mods=`/
   `WorkshopItems=` lists before assuming the server will catch a missing one
   for you (`admins-workshop-mod-wiring` establishes that the server-side
   behaviour here is undocumented; the only confirmed symptom is client-side).
4. **Back up the world** (`admins-backups-migration`) before enabling
   anything on an existing save [4] [5].
5. **Stage it.** Apply the candidate `Mods=`/`WorkshopItems=` change to a
   copy of the world or a throwaway save first, confirm the server starts,
   and run the documented two-instance multiplayer test before trusting a
   singleplayer session's results [6].
6. Add mods one at a time (or one tightly-coupled group at a time) rather
   than in bulk, and watch the console for stack traces or `ERROR`/`WARN`
   lines after each addition — bulk-adding a dozen mods at once is how one
   bad entry costs an evening of bisection later [5] [14].
7. Only once the staged test passes, apply the identical change to the
   production `.ini` at a scheduled restart.

**Update rollout guidance:**

- Treat every scheduled restart as the moment mod updates actually land —
  Steam's automatic Workshop refresh means the *server* only catches up when
  it restarts, so restart cadence is your real update cadence, whether or not
  you think of it that way.
- After a **game** patch, re-open the mod manager and re-check every active
  mod's minimum/maximum version fields before assuming nothing changed [4].
- After a **mod's own** Workshop update, re-run the staging checklist above
  before letting it reach the live server — do not assume an update from a
  trusted author is automatically safe; the base game's own UI treats every
  mod update as carrying launch risk [4].
- Consider a Workshop-update watcher (a mod in the same family as [12]) if
  your community's mod list is large enough that manually polling every
  item's Workshop page is impractical — but understand what it automates
  (detection and a scripted restart), not a guarantee that the update itself
  is safe.
- **Recommended cadence:** check the active mod list's Workshop pages for
  updates on the same cadence as your routine server-restart/maintenance
  window (weekly-to-biweekly is a common community rhythm, though this
  document found no primary source prescribing a specific interval — see
  Claim 3 below); do not let "check for mod updates" become a task with no
  schedule at all, since Workshop applies updates whether or not you looked.
- **When to defer:** hold a scheduled game-version update or a batch of
  Workshop mod updates if your community is mid-season on a long-running,
  heavily-modded save — the version-pairing risk documented above [4] and
  the restart-required posture of mod-list changes both argue for bundling
  updates at a natural break point (a planned wipe, a season boundary, a
  quiet week) rather than mid-arc on a save your players are invested in.
  This is this document's own synthesis of the cited mechanics, not an
  official recommendation — see Claim 2 below for the community version of
  this same advice and why it is quarantined rather than asserted as fact.
- Vendor and pin (per Recommended pinning/freeze posture, above) only the
  mods your community would consider a season-breaking loss if they
  disappeared or changed behaviour unexpectedly; leave everything else on
  the ordinary Workshop auto-fetch path and manage it through restart
  cadence instead.

# Common Pitfalls & Troubleshooting

- **Server won't start, or a newly-added mod silently doesn't load.** Check
  the client mod menu first — a red entry means a missing declared dependency,
  named on the dependency's own Workshop page under "Required Items" [5].
  Then check the logs: the client's `console.txt` and the server's
  `server-console.txt` are the documented locations for both sides of a
  multiplayer session [5]. A real (if build-transition-era) example of what
  a failed-to-load mod looks like in a server's `DebugLog-server.txt`:
  `ERROR: mods isn't a valid workshop item ID` paired with `required mod
  "<ModID>" not found` [16] — if you see lines in this shape, suspect a
  mod-folder-layout mismatch (a B41-only mod run unmodified on a B42 server)
  before anything else [16]. A hosting-KB troubleshooting guide
  (corroborate-only, not independently confirmed against a primary source)
  additionally names a handful of other exception strings worth grepping for
  in the same logs — `NullPointerException`/"attempt to index a nil value"
  as a signal of incorrect load order or a missing dependency, and a plain
  `FileNotFoundException` on an existing mod file as a Linux case-sensitivity
  mismatch between a mod's declared and actual filenames [15].
- **A mod that worked fine solo breaks (or behaves differently) once real
  players connect.** This is exactly the gap the documented two-instance MP
  test exists to catch before rollout [6] — if you skipped that step, run it
  now against a staged copy rather than debugging live.
- **Too many mods, unclear which one is misbehaving.** Use the wiki's own
  documented bifurcation method: reproduce the problem on a save with half
  the mod list active, then keep halving whichever half still reproduces it,
  until one mod is isolated [5]. This scales far better than removing mods
  one at a time once a list is large.
- **A mod list that worked yesterday breaks after an unrelated Workshop
  update.** Steam applied an automatic update to a subscribed item with no
  server-side warning — this is the exact failure mode a Workshop-update
  watcher mod is built to catch [12]; absent one, make "re-check Workshop
  pages for 'Update Required' items" a standing item on your restart
  checklist [13] [14].
- **Assumed reordering `Mods=` would fix a content conflict between two
  mods.** `admins-workshop-mod-wiring` already quarantines this exact claim
  (its Claim 1): the only documented order-dependent override rule is for map
  tile intersection, not general item/script conflicts — do not spend time
  reordering a mod list on the strength of hosting-guide folklore before
  reading that quarantine.
- **A save broke after a mod change and the "fix" (removing the mod) didn't
  restore it.** The wiki states this outcome plainly — the save can be
  permanently broken — which is precisely why the backup-before-changing-mods
  step in this document's checklist is not optional [5].
- **A mod that pushed code from the server stopped working at 42.20.4, or
  recovered at 42.21.** The 42.20.4 hotfix removed `loadstring`/`loadstream`
  and told authors to replace server-sent code with commands, and 42.21
  re-enabled the methods [20] [22]. Check which game build the server was on
  and whether the author shipped a replacement before blaming another mod.
- **Error-log lines about `%` in a mod's translation files.** These follow
  from the `%%` escaping rule and the temporary dual-handling workaround in
  42.20.2 [17] [18]; the correction is the author's.
- **Client and server disagree after a hotfix.** Keep both on the same game
  build and the same mod revisions; 42.20.1 improved Lua checksum validation
  [17] and 42.21 shows a notice when the game versions differ [21].
- **A version-gate error reads as "mod too old" when the mod is actually too
  new for your server.** Documented display-message bug: check the mod's
  actual `versionMin` value against your server's game version before
  assuming an update is required in the direction the message implies [3].

# Community Notes & Unverified Claims

## Claim 1 — A mod tagged with both "Build 41" and "Build 42" needs no further compatibility check

- **Claim:** It is common practice among server admins assembling a mod list
  to treat a mod carrying both build-version Workshop tags as safe to run
  unmodified on either build, since the tags themselves appear to say so.
- **Why unverified:** Workshop tags are author-applied and never
  independently verified [8] [13]; a secondary risk-tiering framework built
  around exactly this ecosystem states the point directly: "a mod that still
  shows Build 41 and Build 42 tags" is "not automatically broken... but tags
  alone never replace a short load test on your revision" [14]. No primary
  source treats a tag pair as a compatibility guarantee.
- **Confidence:** Low. The claim is a reasonable-sounding shortcut that at
  least one secondary source explicitly warns against, and no primary source
  supports treating tags as verified.

## Claim 2 — Server admins should defer any game-version update or batch of mod updates until a scheduled wipe or season boundary

- **Claim:** Community operational wisdom holds that a long-running, heavily
  modded server should bundle both game-version updates and Workshop mod
  updates at a natural break point (a planned wipe, a season boundary) rather
  than applying them mid-arc on a save the community is invested in.
- **Why unverified:** No Indie Stone statement recommends this cadence
  specifically; it is this document's own synthesis (see Practical Guidance)
  of cited mechanics — the version-pairing launch risk [4] and the
  restart-required posture of mod-list changes [9] [10] — rather than a
  claim traced to a primary or fact-only source stating the cadence itself.
- **Confidence:** Medium. The underlying mechanics it is built from are
  cited and real; the specific "defer to a season boundary" cadence is
  operational judgement, not a documented rule.

## Claim 3 — Checking a mod list's Workshop pages for updates every one to two weeks is a sufficient, standard admin cadence

- **Claim:** A weekly-to-biweekly manual check of each active mod's Workshop
  page is a commonly cited "good enough" cadence for catching updates before
  they surprise a live server.
- **Why unverified:** No primary source prescribes any specific interval;
  this document's evidence for an update-checking need at all is indirect —
  the existence and subscriber count of an automated Workshop-update-watcher
  mod [12] — which argues that *some* regular check is valuable, not that a
  particular interval is standard or sufficient for a given mod list's size
  or volatility.
- **Confidence:** Low. Directionally reasonable and consistent with the
  cited mechanics, but the specific cadence number is not traceable to any
  source examined for this document.

# Risks & Caveats

- **The clearest failure-signature example in this document is a single,
  dated community thread.** The `ERROR: mods isn't a valid workshop item ID`
  / `required mod "..." not found` log excerpt [16] is real and quoted
  verbatim, but it comes from one Help-forum report during the 42.13-era
  unstable MP stress-test window, not a primary changelog or a reproduction
  against current 42.20 or 42.21 stable. Treat it as an illustrative, not exhaustive,
  example of what a failed mod load can look like in the server console.
- **The risk-tiering and verification-checklist framing in Practical
  Guidance leans on a single secondary, marketing-adjacent source** [14].
  Its concrete facts (specific mods' Workshop IDs, tags, dates) are
  independently checkable on Steam and were partly cross-verified in this
  document [11]; its risk-tier *methodology* itself is editorial framing,
  not an official classification, and is presented here as guidance, not as
  a cited fact.
- **Several pzwiki pages this document relies on self-flag as trailing the
  current stable version.** `Resolving problems with mods` and `Testing mods
  in multiplayer` are both stamped 41.78.19-era despite 42.20.0 being
  current, and `Testing mods in multiplayer` additionally flags itself as
  needing a rewrite [5] [6]. The mechanisms described (red-mod dependency
  indicator, bifurcation testing, the two-instance MP test procedure) are
  general client behaviours with no reason found to expect a build-specific
  change, but this document did not independently re-verify them against a
  live 42.20 client.
- **The "many B41 mods remain unported" claim in Reference is directional,
  not quantified.** No source found gives a count or proportion; the
  evidence is the documented existence of forked/duplicated Workshop listings
  for the same mod concept across builds [14] and the general, primary-cited
  fact that mods are version-specific [4].
- **Recently stable.** 42.21 has been stable since 2026-09-28 [22], about nine
  days at the time of this revision; any hotfix could change mod-loading behaviour, the
  Workshop "Update Required" state's exact semantics, or the version-gate
  display bug's status before this document's next review.

# Verification Steps

1. **Confirm the tag/description gap first-hand:** open any current Build
   42 mod's Workshop page, note its tags, then read its full description for
   a build-support statement not reflected in the tags themselves (the Neat
   Building example [11] is a reproducible starting point).
2. **Confirm the mod-manager version fields:** subscribe to a mod with a
   stated `versionMin`/`versionMax`, open the in-game mod manager, and
   confirm the minimum/maximum game version display matches the mod's own
   `mod.info` [4] [7].
3. **Reproduce the version-gate display bug:** set a test mod's `versionMin`
   to a version newer than your installed game and confirm the exact
   "must be updated" message text against the logged bug report [3].
4. **Run the documented two-instance MP test** end to end on a current
   client: launch an admin host with `-nosteam -debug`, a second `-nosteam`
   client, and confirm a candidate mod's behaviour differs (or doesn't)
   between the singleplayer and this local-MP configuration [6].
5. **Reproduce the bifurcation method** on a throwaway save with a
   deliberately-introduced conflicting pair of mods, and confirm the
   halving procedure isolates the correct one [5].
6. **Probe the Workshop auto-update gap:** wire a test mod into a scratch
   server's `WorkshopItems=`, have its author (or a second account with
   upload rights) push a trivial update, and confirm whether the server's
   cached copy changes only after a restart — this is the same test
   `admins-workshop-mod-wiring`'s Verification Steps already prescribes, and
   resolving it there resolves the mechanism this document's staging
   guidance rests on.
7. **Re-run the [16] scenario on current 42.21 stable** with a mod
   restructured for the B42 `common/`+`42.x` folder layout, to confirm
   whether the specific `ERROR`/`WARN` log lines quoted here still occur on a
   properly-restructured mod, or were specific to the unstable-era report.

# Open Questions

- What does the improved Lua checksum validation [17] do when a client's mod
  Lua differs from the server's: refuse, kick or ignore? The 42.20.1 notes do
  not say.
- Did the 42.20.4 removal of `loadstring`/`loadstream` apply to the legacy41
  line as well? The combined 41.78.21 post does not separate it by build [20].
- What proportion of actively-maintained Build 41 mods have been ported to
  Build 42 as of 42.20 stable, and is there any citable tracker beyond
  individual Workshop pages and forked listings [14]? No primary source
  found quantifies this.
- Does the `ERROR: mods isn't a valid workshop item ID` log signature [16]
  still occur on 42.20 stable for a properly B42-structured mod, or was it
  specific to the 42.13-era unstable branch and/or a misconfigured
  `Mods=`/`WorkshopItems=` pairing in that report? (Verification Step 7.)
- Is there an official or semi-official Indie Stone position on a
  recommended mod-update-checking cadence for server operators, now that a
  GSP feedback channel exists (per `admins-foundation`)?
- Does the base game's own client log a distinct, greppable line when a
  *game*-version update (as opposed to a mod update) invalidates an active
  main-menu mod list, beyond the general UI warning text cited here [4]?
- Would The Indie Stone consider a documented Workshop-item revision-pin
  mechanism (through `.ini` or SteamCMD) given how widely adopted
  third-party update-watcher mods like [12] have become?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam
  announcement, 2026-07-29; retrieved via the Steam news API mirror,
  ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259.
  Accessed 2026-07-31.
- [2] **The Indie Stone** — *Unstable 42 MP Released* (Steam announcement,
  2025-12-11; disable-all-mods stress-test guidance). https://steamcommunity.com/games/108600/announcements/detail/1818752592123010.
  Accessed 2026-07-31.
- [3] **The Indie Stone Forums** — *[42.12.3] [rev:31595] Mod minimum version
  shows wrong error message* (Bug Reports subforum, filed 2025-10-29,
  reconfirmed for maximum-version gating 2025-12-13). https://theindiestone.com/forums/index.php?/topic/87949-42123-rev31595-mod-minimum-version-shows-wrong-error-message/.
  Accessed 2026-07-31 (host bot-block allowlisted; page retrieved
  successfully).

- [17] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam
  announcement, 2026-08-05; Lua checksum validation, memory and chunk-unloading
  fixes, `%%` in mod translations). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [18] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam
  announcement, 2026-08-05; temporary dual-handling workaround for `%%`).
  https://steamcommunity.com/games/108600/announcements/detail/1840310314339441. Accessed 2026-10-07.
- [19] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam
  announcement, 2026-08-17; support for up to 254 players). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895.
  Accessed 2026-10-07.
- [20] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21
  LEGACY Hotfixes Released* (Steam announcement, 2026-08-26;
  `loadstring`/`loadstream` removal). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [21] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable
  Released* (Steam announcement, 2026-09-23; `loadstring` re-enabled,
  version-mismatch notice, Steam authentication fix, server browser). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925.
  Accessed 2026-10-07.
- [22] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement,
  2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [23] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first
  post, 2026-09-23; abridged selection of the full changelist). https://theindiestone.com/forums/topic/101693-4221-patch-notes/.
  Accessed 2026-10-07 (host bot-block allowlisted).

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL +
revision id; facts only, never prose.

- [4] **PZwiki** — *Mods* (revision 1391047; page versioned against
  42.14.0). https://pzwiki.net/w/index.php?title=Mods&oldid=1391047.
  Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Resolving problems with mods* (revision 1392779; page
  self-flagged as last substantively updated for 41.78.19). https://pzwiki.net/w/index.php?title=Resolving_problems_with_mods&oldid=1392779.
  Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Testing mods in multiplayer* (revision 1394139; page
  self-flagged as needing a rewrite, last verified 41.78.19). https://pzwiki.net/w/index.php?title=Testing_mods_in_multiplayer&oldid=1394139.
  Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *mod.info* (revision 1363935; page versioned against
  42.17.0). https://pzwiki.net/w/index.php?title=Mod.info&oldid=1363935.
  Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *workshop.txt* (revision 1395233; page versioned against
  an unstable 42.5.1-era build). https://pzwiki.net/w/index.php?title=Workshop.txt&oldid=1395233.
  Accessed 2026-07-31. Fact-only source.
- [9] **PZwiki** — *Dedicated server* (revision 1443349; page versioned
  against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349.
  Accessed 2026-07-31. Fact-only source.
- [10] **PZwiki** — *Server settings* (revision 1443167; page versioned
  against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167.
  Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [11] **Steam Workshop** — *Neat Building [B42]* (Workshop ID 3536052310;
  mod page; source of the self-declared build-support string, dependency
  note and multiplayer-variant guidance). https://steamcommunity.com/sharedfiles/filedetails/?id=3536052310.
  Accessed 2026-07-31.
- [12] **Steam Workshop** — *Server Workshop Mod Update Checker &
  Auto-Restart (B42) MP* (Workshop ID 3659447892; mod page). https://steamcommunity.com/sharedfiles/filedetails/?id=3659447892.
  Accessed 2026-07-31.
- [13] **Steam Workshop** — Project Zomboid Workshop browse page filtered to
  the "Build 42" tag, confirming the predefined Build 40/41/42 tag set.
  https://steamcommunity.com/workshop/browse/?appid=108600&browsesort=trend&section=readytouseitems&requiredtags%5B%5D=Build+42.
  Accessed 2026-07-31.
- [14] **pzfans** — *Build 42 Modding (42.19): What Works, What Breaks, and
  How to Choose Safely* (hosting/community guide; corroborate-only; source
  of the risk-tier framework, verification checklist and dated Workshop
  examples). https://pzfans.com/build_42_modding_what_works_what_s_broken_and_what_s_worth_it/.
  Accessed 2026-07-31.
- [15] **Legion Hosting** — *Project Zomboid Mod Troubleshooting* (hosting
  KB; corroborate-only; source of console log-error-string examples referenced
  in Common Pitfalls research; its repeated `Mods=` backslash-format claim is
  not adopted here — see `admins-foundation` Claim 2 and
  `admins-workshop-mod-wiring`, which already quarantine it).
  https://legionhosting.net/kb/project-zomboid/project-zomboid-mod-troubleshooting.
  Accessed 2026-07-31.

**Community & Creator**

- [16] **The Indie Stone Forums** — *[B42/Dedicated] Server fails to load
  workshop mods* (Help subforum thread, posted 2025-12-12; source of the
  quoted server-console log lines and the mod-folder-restructuring
  explanation). https://theindiestone.com/forums/index.php?/topic/88653-b42dedicated-server-fails-to-load-workshop-mods/.
  Accessed 2026-07-31 (host bot-block allowlisted; page retrieved
  successfully).

**Further Reading**

# Further Reading

- The ISteamNews API mirror used to verify announcement citations:
  https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- The full Project Zomboid Workshop, browsable by tag:
  https://steamcommunity.com/workshop/browse/?appid=108600
- `admins-workshop-mod-wiring`'s Verification Steps, which include the
  empirical test of whether the server re-fetches a `WorkshopItems=` entry
  on every launch — the mechanism this document's staging guidance assumes.

# Related Documents

- `admins-foundation` — the Admins-track overview; owns the RAM/CPU
  quarantines and the mods-off 42.13 stress-test citation this document
  reuses rather than re-argues.
- `admins-workshop-mod-wiring` — the mechanical reference this document
  deepens: Workshop ID vs. Mod ID, `.ini` list syntax, `require=`/
  `versionMin`, `-modfolders` load order, and the exhaustive search for a
  Workshop version-pin mechanism this document's Recommended Pinning
  section relies on.
- `admins-ubuntu-runbook` — the Linux process/service runbook this
  document's restart-discipline guidance assumes is already in place.
- `admins-backups-migration` — the backup and restore procedure this
  document points to before every staged or live mod-list change.
- `admins-performance-tuning` — the performance-tuning sibling; mods are
  named there only as "the least-documented load," a claim this document
  does not re-litigate.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21 (stable 2026-09-28): added a Reference section on 42.20.1-42.21 changes relevant to modded servers (Lua checksum validation, %% translation escaping, loadstring/loadstream removal in 42.20.4 and re-enable in 42.21, version-mismatch notice, 254-player cap, Steam authentication fix, memory fixes); updated Build Applicability, Delta, Pitfalls, Risks, Open Questions and Verification scope. Sources: Steam posts 42.20.1, 42.20.2, 42.20.3, 42.20.4+41.78.21, 42.21 unstable, 42.21 stable; TIS forum 42.21 patch notes. Unchanged statements carried forward from 42.20, not re-tested. | — |
