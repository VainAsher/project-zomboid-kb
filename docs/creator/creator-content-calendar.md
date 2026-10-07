---
id: creator-content-calendar
title: "Post-Launch Content Calendar for Build 42: Release Rhythm, Patch Hooks and Evergreen Slots"
version: 0.2.0
status: in-review
confidence: Medium
category: Creator
topic: "Content calendar"
build: B42
document_type: guide
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [creator-foundation, creator-format-catalogue, creator-channel-competitor-map, creator-cross-promotion-funnel, players-beginner-guide-b42, players-b41-to-b42-transition, players-farming-food, players-animals-husbandry, players-vehicles, players-medical-moodles, admins-modded-server-runbook, modders-first-mod-tutorial-b42, meta-style-guide]
tags: [creator, content-calendar, patch-cadence, release-timeline, hotfix, evergreen, b42-stable, 42.21]
game_versions_verified: ["42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | creator-content-calendar |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Creator |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 42.21 (release timeline, 42.21 Steam posts and TIS forum change list read 2026-10-07) |

# Executive Summary

The launch window that creator-foundation described has closed: Build 42.20.0
reached the stable branch on 2026-07-29 [1][2], and the stable branch has since
moved to 42.21, released on 2026-09-28 [1][8]. This guide therefore builds a
post-launch calendar rather than a launch-week plan. It records the dated
release timeline from the official Steam announcement feed, computes the gaps
between releases, lists what The Indie Stone has said is still coming, and
only then turns that into a reusable set of patch-hook slots.

The headline pattern is a two-speed rhythm. During the unstable cycle, new
x.0 builds landed roughly every three weeks for most of 2026 [1]. Since stable
launch the cadence has been hotfix-driven: four hotfixes in the 28 days after
launch [2][3][4][5][6], then a 56-day gap before the next unstable build
[6][7], then a five-day unstable-to-stable promotion [7][8]. The studio now
states that unstable-first is the standard path for every release [7][8], which
gives creators a short, predictable early-warning window before each stable
patch.

Confidence is **Medium**. Dates and titles come from primary Steam
announcements, but the feed query returns only the most recent 100 items [1],
the 42.21 forum change list was read in an abridged form [14], and cadence
statistics rest on a small number of releases.

# Key Takeaways

- Stable 42.20.0 shipped 2026-07-29; hotfixes 42.20.1 and 42.20.2 followed on
  2026-08-05, 42.20.3 on 2026-08-17 and 42.20.4 on 2026-08-26 *(cited)*
  *(B42)* [2][3][4][5][6].
- 42.21 went to unstable on 2026-09-23 and to stable on 2026-09-28, five days
  later, with the studio saying no major issues were reported *(cited)*
  *(B42)* [7][8].
- The Indie Stone says every future release follows the same unstable-then-
  stable path, with the unstable gap varying by complexity *(cited)* [7][8].
  The unstable post is therefore the earliest official signal a creator gets.
- Legacy Build 41 is still receiving security-motivated hotfixes: 41.78.21
  shipped 2026-08-26 *(cited)* *(B41)* [6].
- Announced but not shipped as of the 2026-10-07 read of the feed: a late-game
  tweak patch, mapping tools plus the AnimZed animation tool, an extensive
  modding guide, and a Build 42 Support Update planned for the rest of 2026
  *(cited as announced, no release dates given)* [9][10]. The abridged 42.21
  forum change list does not mention the mapping tools, AnimZed or the modding
  guide *(cited)* [14].
- Patch hooks come from named change categories in the notes, not from
  version numbers. Section "Practical Guidance" maps 42.21 change categories
  to the KB documents that supply fact-check material *(guidance built on
  cited facts)*.
- No future release date is asserted anywhere in this document *(by design)*.

# Purpose

creator-foundation explained why the stable launch was a demand spike and
which formats suit it. This guide answers the question
that follows once the spike is over: what do you publish week to week, which
existing videos are about to be wrong, and when does the official release
rhythm hand you a reason to publish? It stays on the production-planning side
and defers game mechanics to the Players, Admins and Modders documents named
in the calendar.

# Scope

Covered: the dated B42 and B41-legacy release timeline visible in the Steam
announcement feed; computed intervals between those releases; announced but
unshipped work; a calendar template with patch-hook and evergreen slots; and
a map from patch-note categories to KB fact-check documents.

Not covered: audience analytics, platform algorithm behaviour, monetisation,
and any prediction of release dates. The feed holds at most the 100 most
recent items per query, so releases older than that window are out of range
[1]. The pre-2025-01 unstable history is already summarised in
creator-foundation. For 42.21 the TIS forum change list is used alongside the
Steam announcement bodies; that list is abridged ("selected" sections), so
absence from it is not proof that a change did not ship [14]. Earlier hotfixes
use the Steam announcement bodies only.

# Definitions

- **Patch hook** — a dated official release or announcement that gives a
  creator a legitimate, timely reason to publish.
- **Day-0 reaction** — content published within hours of a patch-note post,
  built from the notes alone.
- **Week-1 refresh** — a guide or update video recorded after a week of play
  on the new build.
- **Evergreen slot** — scheduled search-driven content whose topic does not
  depend on a specific patch.
- **Unstable-first** — the studio's stated release path: unstable beta, then
  stable [7][8].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Context only | 41.78.21 per announcement title | Only appears as a security hotfix line in the timeline [6][12] |
| B42 (stable) | Yes | 42.21; timeline read through 42.21 stable | 42.21 stable released 2026-09-28 [8]; KB fact documents referenced in the calendar were last verified on 42.20 unless they have been re-baselined since |

Release facts were read on 2026-10-07, and this revision re-checked the
timeline, the interval arithmetic, the announced-but-unshipped table and the
42.21 change table against the Steam posts [2]-[8] and the TIS forum 42.21
patch notes [14]. The interval arithmetic was recomputed from the dates in the
timeline and every figure held. The B42 stable branch is now 42.21 [8], while
the KB game-document set referenced below may still carry 42.20 as its verified
version; the calendar's staleness map exists to bridge that gap.

# Reference

## B42 release timeline since launch

All dates are the announcement dates shown in the Steam news feed [1]; the
feed does not state the time zone of its timestamps, so dates are taken as the
posted calendar day.

| Date | Release | Branch | Source |
|------|---------|--------|--------|
| 2026-07-29 | 42.20.0 | Stable (default branch) | [2] |
| 2026-08-05 | 42.20.1 hotfix | Stable | [3] |
| 2026-08-05 | 42.20.2 hotfix | Stable | [4] |
| 2026-08-17 | 42.20.3 hotfix | Stable | [5] |
| 2026-08-26 | 42.20.4 hotfix, bundled with 42.19.2 unstable and 41.78.21 legacy hotfixes | Stable, unstable, legacy41 | [6] |
| 2026-09-23 | 42.21 | Unstable | [7] |
| 2026-09-28 | 42.21 | Stable | [8] |

The hotfix posts for 42.20.1 through 42.20.3 each ask players to reproduce a
bug on a fresh save with no mods before reporting it [3][4][5]. The 42.20.4
post removed the loadstring and loadstream Lua methods as part of a security
fix and told modders to update affected mods [6]. The 42.21 unstable post
reversed that removal, re-enabling both commands [7], and the 42.21 stable post
repeats the reversal [8].

## Earlier unstable milestones

The table lists the unstable and stable x.0 announcements visible in the feed,
using titles as posted [1]. The feed window begins in January 2025, and the
42.8.0 announcement does not appear in it, so the entry for 42.8 is the later
42.8.1 post [1].

| Date | Announcement as titled in the feed |
|------|------------------------------------|
| 2025-01-21 | 42.1 Unstable [1] |
| 2025-01-27 | 42.2.0 Unstable [1] |
| 2025-02-11 | 42.3.0 Unstable [1] |
| 2025-03-04 | 42.4.0 Unstable [1] |
| 2025-03-11 | 42.5.0 Unstable [1] |
| 2025-03-24 | 42.6.0 Unstable [1] |
| 2025-04-07 | 42.7.0 Unstable [1] |
| 2025-05-20 | 42.8.1 Unstable [1] |
| 2025-06-10 | 42.9.0 Unstable [1] |
| 2025-06-30 | 42.10 Unstable [1] |
| 2025-08-04 | 42.11.0 Unstable [1] |
| 2025-09-25 | 42.12.0 Unstable [1] |
| 2025-12-11 | 42.13.0 Unstable Multiplayer [11] |
| 2026-02-16 | 42.14.0 Unstable [1] |
| 2026-03-09 | 42.15.0 Unstable [1] |
| 2026-03-31 | 42.16.0 Unstable [1] |
| 2026-04-20 | 42.17.0 Unstable [1] |
| 2026-05-11 | 42.18.0 Unstable [1] |
| 2026-06-01 | 42.19.0 Unstable [13] |

A legacy-line hotfix is also visible: an announcement titled as a combined
Stable (41.78.19) and Unstable (42.16.3) hotfix was posted on 2026-04-08 [12].

## Computed intervals

These figures are arithmetic on the dates above, not statements by The Indie
Stone.

| Interval | Days | Derived from |
|----------|------|--------------|
| 42.20.0 stable to 42.20.1 and 42.20.2 | 7 | [2][3][4] |
| 42.20.2 to 42.20.3 | 12 | [4][5] |
| 42.20.3 to 42.20.4 | 9 | [5][6] |
| 42.20.0 stable to 42.20.4 (last hotfix) | 28 | [2][6] |
| 42.20.4 to 42.21 unstable | 28 | [6][7] |
| 42.20.0 stable to 42.21 unstable | 56 | [2][7] |
| 42.21 unstable to 42.21 stable | 5 | [7][8] |
| 42.19.0 unstable to 42.20.0 stable | 58 | [13][2] |
| Median gap between consecutive x.0 unstable posts, 42.2.0 through 42.19.0 | 21 | [1][11][13] |
| Shortest and longest gaps in the same run | 6 and 77 | [1][11][13] |
| Unstable x.0 gaps from 42.15.0 to 42.19.0 (four gaps) | 22, 20, 21, 21 | [1][13] |

The gap pattern before launch held near three weeks for the five consecutive
gaps from 42.14.0 to 42.19.0, between 20 and 22 days each [1][13]. After launch, the gap from the last
hotfix to the next unstable build was 28 days, and from stable launch to that
build 56 days [2][6][7].

## Statements of intent from the studio

The 42.21 unstable and stable posts both say that, going forward, a new update
goes to unstable first, is tested by players, may be adjusted, and then moves
to stable [7][8]. The unstable post adds that the time between unstable and
stable will vary with complexity, that the aim is to move faster, and that
unstable is meant for testing rather than acting as an unofficial stable [7].
The stable post says the promotion happened because the community reported no
major issues [8].

## Announced but not shipped

The following items were announced as planned and have no matching release
announcement in the feed window read on 2026-10-07 [1]. None carries a date
in the source posts.

| Item | Announcement | Wording of commitment |
|------|--------------|------------------------|
| A patch of tweaks and adjustments from player feedback, aimed mainly at the late game | 2026-07-09 [9]; repeated 2026-07-24 [10] | Planned after necessary hotfixes [9][10] |
| Release of the latest mapping tools (WorldZed, TileZed and others) and the AnimZed animation editor | 2026-07-09 [9]; 2026-07-24 [10] | Planned once hotfixing is over [9][10] |
| An extensive modding guide | 2026-07-24 [10] | Planned alongside the tools [10] |
| A Build 42 Support Update covering optimisation, further modding support and player-requested polish | 2026-07-09 [9]; 2026-07-24 [10] | Planned for the rest of 2026 [9][10] |
| Continued multiplayer and controller improvements | 2026-07-24 [10] | Throughout B42 patching [10] |
| Remaining zombie duplication and disappearing-zombie cases | 2026-09-28 [8] | Stated to be on the radar and fixed in the next update [8]; the forum list records the cases already fixed in 42.21, including an additional multiplayer duplication case [14] |
| Further work on XXL-tree cutaway behaviour | 2026-09-23 [7]; 2026-09-28 [8]; forum list [14] | Described as a work in progress [7][8][14] |
| Further causes of black and grey boxes when travelling quickly | 2026-08-17 [5] | Still under investigation [5]; the abridged 42.21 forum list does not mention it [14] |
| Removal of the temporary percent-symbol workaround | 2026-08-05 [4] | Planned for a future unstable update [4]; the abridged 42.21 forum list mentions a fix for spaces and percentages not being visible in the game UI but does not mention removing the workaround [14] |

## What 42.21 changed, by topic

These are the changes stated in the unstable and stable announcement bodies and
in the TIS forum change list for 42.21 [7][8][14]. The forum list was retrieved
in abridged form: several sections are marked "selected", so it is a subset of
the full notes. The forum post also states that existing savegames on 42.20.4
should not be affected and should be backed up first [14].

| Topic | Stated change | Source |
|-------|---------------|--------|
| Zombies | Fix for zombies vanishing after a player leaves and re-enters a chunk, in single and multiplayer, plus fixes for multiplayer zombie duplication (including an additional case and a zombie coordinate desync) | [7][8][14] |
| Trees and driving | XXL trees cut away better for players in vehicles, no longer hide overhung houses and furniture, and have adjusted transparency; subbiomes no longer generate trees on dirt | [7][8][14] |
| Modding and servers | loadstring and loadstream re-enabled after being disabled in 42.20.4; a missing translation or recipe now raises a RuntimeException instead of a console print; Seam Editor added to the debug menu; an unset-by-default ToggleOldRenderer keybinding added | [7][8][14] |
| Occupations | Welder occupation starts with Welding recipes rather than Blacksmithing recipes | [7][14] |
| Water and cleaning | 86 more fluid containers can purify water in the appropriate oven type; washing machines clean dirty rags, strips and bandages | [7][14] |
| Refrigeration | Fridges and freezers warm gradually on the day power goes out; refrigeration applies correctly to food in a bag inside a fridge or freezer | [7][14] |
| Medical supplies | Antibiotics can be packaged with the pack-in-box recipe | [7][14] |
| Farming | Pathfinding avoids walking over farming plants where possible, which the forum list says is purely cosmetic because stepping on crops does not damage them; furrows trampled by zombies are removed from the world | [7][14] |
| Basements and explosives | Explosives work in basements | [7][14] |
| Map and UI | In-game player map updated to remove inaccuracies while exploring; Spawn Point Selection preview videos updated to match the map glow-up; in-game credits updated; fix for spaces and percentages not showing in the UI; increased brightness on several lamp tiles | [7][14] |
| Localization | Localization system updated to allow more translatable strings | [7][14] |
| Items and stashes | Floorboard stash containers found with annotated maps renamed more appropriately; a deprecated tankless SCBA no longer spawns | [7][14] |
| Quality of life | Characters re-equip items automatically after exercise | [7][14] |
| Multiplayer | Expanded anti-cheat and safehouse exploit fixes, a notification when connecting with a different game version, the server browser showing the last wipe rather than the last restart, a Steam authentication fix that restores SteamID bans, high-ping driving fixes, a fix for an infinite connection loop when the Discord API is unavailable, and a fix for the UsernameDisguises connection failure | [7][14] |
| Split screen | Fixes for a crash when local players share a moving vehicle, incorrectly shared read-book status and XP boosts, fishing, and controls after a gamepad disconnect | [7][14] |

# B41 vs B42 Delta

Not applicable — single-build document. The calendar is tagged B42 because
its release rhythm and patch hooks all concern the 42.x line [2][7][8]. Build
41 appears only as the legacy line receiving security hotfixes, for example
41.78.21 on 2026-08-26 [6]. The mechanical differences between the builds
belong to players-b41-to-b42-transition.

# Practical Guidance

This section is synthesis of the cited facts above. It adds no new facts about
the game or the release schedule, and every cadence figure it uses is
computed in the Reference section.

## A rhythm built from what has actually happened

Three observed phases suggest three production modes. During the unstable
cycle, builds arrived about every three weeks [1][13], which is a cycle short
enough that any guide recorded on unstable was likely to be superseded
quickly. Immediately after stable launch, hotfixes arrived at 7, 12 and 9 day
spacings [2][3][4][5][6], which is a cycle of small corrections where the safe
approach is to hold polished guides for the end of the run. The current phase
is the unstable-first pattern the studio has declared standard [7][8], with an
unstable post followed by a stable promotion that took five days in the one
case so far [7][8].

Treat that five-day figure as a single data point. The studio itself says the
gap will vary with complexity [7], so a calendar built on the 42.21 gap would
be a calendar built on one observation.

## Calendar template: patch-hook slots

Offsets below are planning conventions for a creator, not predictions of when
any release will occur. They key off a release that has already been announced.

| Slot | Trigger | Offset | What to publish | Fact-check material |
|------|---------|--------|-----------------|---------------------|
| U-0: unstable heads-up | Unstable post goes live [7] | Same day to day 2 | Short reaction to the highlights list; label clearly as unstable | The unstable post itself [7] |
| U-1: save-safety explainer | Unstable post warns about backups [7] | Day 1 to 3 | A "back up before testing" explainer for the audience that plays on unstable | The post's own wording on saves [7] |
| S-0: stable day-0 reaction | Stable post goes live [8] | Same day | Notes-based reaction built only from the stable post and the forum list | Stable post [8] |
| S-1: week-1 refresh | One week of play on the new stable | Day 5 to 9 | Re-record or patch the guides that the staleness map flags | KB documents in the next table |
| S-2: hotfix watch | Hotfix posts [3][4][5][6] | Same day, text only | A pinned comment or description update instead of a new video, unless a hotfix changes a mechanic the video shows | Hotfix post [3][4][5][6] |
| E-n: evergreen | None | Fixed weekly or biweekly | Search-driven guides in the evergreen list below | KB reference documents |
| A-n: announced-item slot | The studio ships an item from the "announced but not shipped" table | Reserve in advance | Showcase or tutorial for that item | The release post, once it exists |

Hold the A-n slots open without dates: the table of unshipped items in the
Reference section is a list of reasons to keep capacity free, not a forecast
[9][10]. The mapping tools, AnimZed and the modding guide are the natural
hooks for modding-tutorial content, and the Support Update is a hook for an
"is the game running better" comparison video whenever it arrives [9][10].

## Which KB documents back which slot

| Slot or topic | KB document | What it supplies | Staleness note |
|---------------|-------------|------------------|----------------|
| Beginner and returning-player guides | players-beginner-guide-b42 | Verified starter-guide facts | Verified on 42.20; check against the 42.21 change table (Welder start recipes, auto re-equip after exercise, map and spawn-selection UI) before recording [7][14] |
| Veteran migration content | players-b41-to-b42-transition | B41 versus B42 differences | Verified on 41.78.16 and 42.20; legacy41 hotfixes do not change that comparison by themselves [6] |
| Farming, food and refrigeration | players-farming-food | Crop and food-handling facts | 42.21 touched refrigeration, water purification, farm-plant pathfinding and zombie-trampled furrows [7][14]; re-verify those sections first |
| Animals | players-animals-husbandry | Husbandry facts | The Steam 42.21 posts do not list animal changes [7][8]; the abridged forum list mentions only multiplayer animal fixes in general terms [14]; the full notes were not read |
| Vehicles and driving | players-vehicles | Vehicle facts | XXL-tree cutaway changed for drivers, and high-ping driving and vehicle-sound fixes are listed [7][8][14]; any driving footage is affected visually |
| Medical content | players-medical-moodles | Medical and moodle facts | Antibiotic packaging changed [7][14] |
| Modded server content | admins-modded-server-runbook | Server and mod operations | Reversal of the loadstring removal [6][7][8], the version-mismatch connect notice, the server browser change, the Discord-loop and UsernameDisguises fixes [7][14] |
| Modding tutorials | modders-first-mod-tutorial-b42 | First-mod walkthrough | Check any use of loadstring-like methods against the 42.20.4 removal and the 42.21 reversal [6][7][8] |
| Channel strategy | creator-foundation, creator-format-catalogue, creator-channel-competitor-map, creator-cross-promotion-funnel | Format, competitor and funnel context | Audience figures are dated snapshots, not patch-bound |

## Which videos go stale, and when

Staleness follows what the footage shows, not the title. A video goes stale at
the first stable release whose notes touch something it demonstrates.

| Video type | Depends on | Goes stale when | Handling |
|------------|-----------|-----------------|----------|
| Zombie-population or horde-survival runs | Zombies persisting after chunk reloads | A fix to chunk behaviour lands, as in 42.21 [7][8]; the studio expects further fixes next update [8] | Date-stamp the build; plan a re-record after the next update |
| Driving and vehicle guides | Tree cutaway and vehicle sync | Tree or driving changes, as in 42.21 [7][8] | Replace footage that shows trees blocking the view |
| Farming and food-storage guides | Refrigeration and pathfinding behaviour | Food-storage or farm changes, as in 42.21 [7] | Re-test the specific claims on the new build |
| Welding or blacksmithing starter builds | Occupation starting recipes | An occupation recipe change, as in 42.21 [7][14] | Re-check the starting state in a new character |
| Exploration, map and character-creation walkthroughs | In-game map and spawn-selection UI | Map or UI changes, as in 42.21 [14] | Replace footage of the map screen and spawn-point preview |
| Localised or mod-translation content | Translation system and `%` handling | Localization changes, as in 42.20.1, 42.20.2 and 42.21 [2][3][14] | Re-test translated text on the current stable |
| Mod-heavy server videos | Script-execution methods and mod compatibility | A security-driven method removal or reversal [6][7][8] | Re-verify each mod on the current stable |
| Map-based content | Mapping tools | Release of the announced tools, if it happens [9][10] | Reserve an A-slot; no date is implied |
| Beginner videos | Multiple systems | Any stable release that touches an on-screen system | Use a pinned correction comment for small drifts, a re-record for large ones |
| Hotfix-era bug demos | A specific bug | The hotfix that fixes it [3][5][6] | Retire or label as historical |

## Evergreen slots

Evergreen slots exist so the calendar is not hostage to the release rhythm.
Reasonable evergreen candidates, each matched to a KB document, are the
beginner guide, the farming and food guide, the animals guide, the vehicles
guide, the medical guide, a modded-server walkthrough, and a first-mod
tutorial. Rotate them on a fixed cadence, and attach a build stamp so the
viewer can judge freshness at a glance.

## Planning under uncertainty

*Unannounced and speculative.* The studio has given no date for the next
release, and none appears here. A defensible planning stance is to prepare a
day-0 template and a week-1 refresh checklist in advance, keep two evergreen
videos in the can, and open the S-1 slot only when an unstable post appears
[7]. If an unstable post says it targets a particular topic, use the staleness
table to pre-identify the affected videos.

# Common Pitfalls & Troubleshooting

- **Treating a hotfix like a content patch.** The 42.20.x hotfix posts are
  largely multiplayer, memory and technical fixes [3][4][5][6]. Publishing a
  full new guide per hotfix over-spends production time.
- **Calendar built on one gap.** The 5-day unstable-to-stable gap [7][8] is a
  single observation, and the studio says the gap varies [7].
- **Quoting the date you saw, not the date posted.** The feed does not state a
  time zone for its timestamps [1]; a release posted late in one region can
  fall on a different calendar day elsewhere.
- **Assuming the loadstring story stayed put.** It was removed on 2026-08-26
  [6] and re-enabled by 2026-09-23 [7][8]; mod content published between
  those dates may carry advice that no longer applies.
- **Re-using 42.20 verification for 42.21 facts.** The KB game documents
  referenced above carry 42.20 as their verified version; the 42.21 change
  table flags what to re-check first [7].
- **Citing unannounced timing as fact.** The items in the unshipped table have
  no dates [9][10]; do not put a month on screen.

# Community Notes & Unverified Claims

None.

# Risks & Caveats

- **Feed window.** The feed query returns a maximum of 100 items [1], which
  mixes official posts with syndicated press. Releases outside the window,
  and any official post the feed omits, are not in the timeline.
- **Titles versus bodies.** The 42.13.0, 42.19.0 and 41.78.19 rows rest on the
  announcement titles and dates in the feed, not on a read of each post body
  [11][12][13].
- **Forum notes abridged.** The 42.21 change list was read from the TIS forum
  thread in an abridged form [14], so the 42.21 table is a subset of the full
  notes; the Steam posts link a slightly different thread slug for the same
  topic number [7][8].
- **Small sample.** The cadence statistics derive from about twenty release
  dates; the post-launch phase has only seven dated entries [2][3][4][5][6][7][8].
- **Staleness of this document.** Any new announcement could invalidate the
  "announced but not shipped" table; the Verification Steps give a
  thirty-second recheck.
- **Dating.** 42.8.0 is absent from the feed window, so the 42.7.0 to 42.8.1
  interval overstates the true gap [1].

# Verification Steps

1. Query `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0`
   and filter to the "Community Announcements" feed label [1].
2. Confirm that the newest titled release entries still read 42.21 Stable
   (2026-09-28) at the top; anything newer means this document is stale [8].
3. For each row of the unshipped table, search the feed for the item name
   (AnimZed, modding guide, Support Update, WorldZed) and move any hit into
   the timeline [9][10].
4. Recompute the interval table from the timeline rows with a date-difference
   calculator.
5. Open the forum thread for 42.21 [14] in full and extend the 42.21 table
   with any section the abridged read marked as "selected".
6. Re-run the staleness map against any new release: for each change category
   in the new notes, flag the matching KB document and video type.

# Open Questions

- When will the announced late-game tweak patch, mapping tools, AnimZed,
  modding guide and Support Update ship? The source posts give no dates
  [9][10]. Resolution: a future announcement.
- Does the five-day unstable-to-stable gap repeat? One observation exists
  [7][8]. Resolution: the next two release cycles.
- Does the full (unabridged) 42.21 forum change list touch animals, crafting or
  medical content beyond what the abridged read shows [14]? Resolution: read
  the thread in full.
- Do the KB's Players documents need a 42.21 re-verification pass? Their
  recorded verification version may still be 42.20; a fact-check worker should
  work from the 42.21 table above [14].

# References

**Primary Sources**

- [1] **Valve / The Indie Stone** — *Steam news feed for app 108600
  (ISteamNews GetNewsForApp, count=100, maxlength=0)*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0
  Accessed 2026-10-07.
- [2] **The Indie Stone** — *Build 42.20.0 Stable Released*. Steam
  announcement, 2026-07-29. https://steamcommunity.com/games/108600/announcements/detail/1839676055882259
  Date and title read via [1], 2026-10-07.
- [3] **The Indie Stone** — *42.20.1 STABLE Hotfix Released*. Steam
  announcement, 2026-08-05. https://steamcommunity.com/games/108600/announcements/detail/1840310314338766
  Read via [1], 2026-10-07.
- [4] **The Indie Stone** — *42.20.2 STABLE Hotfix Released*. Steam
  announcement, 2026-08-05. https://steamcommunity.com/games/108600/announcements/detail/1840310314339441
  Read via [1], 2026-10-07.
- [5] **The Indie Stone** — *42.20.3 STABLE Hotfix Released*. Steam
  announcement, 2026-08-17. https://steamcommunity.com/games/108600/announcements/detail/1840944183785895
  Read via [1], 2026-10-07.
- [6] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21
  LEGACY Hotfixes Released*. Steam announcement, 2026-08-26.
  https://steamcommunity.com/games/108600/announcements/detail/1842212951296601
  Read via [1], 2026-10-07.
- [7] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable
  Released*. Steam announcement, 2026-09-23.
  https://steamcommunity.com/games/108600/announcements/detail/1844751498218925
  Read via [1], 2026-10-07.
- [8] **The Indie Stone** — *Build 42.21 Stable Released*. Steam
  announcement, 2026-09-28. https://steamcommunity.com/games/108600/announcements/detail/1844751498231307
  Read via [1], 2026-10-07.
- [9] **The Indie Stone** — *NEXT STEPS*. Steam announcement, 2026-07-09.
  https://steamcommunity.com/games/108600/announcements/detail/1836506165584147
  Read via [1], 2026-10-07.
- [10] **The Indie Stone** — *BUILD 42 STABLE PLANS*. Steam announcement,
  2026-07-24. https://steamcommunity.com/games/108600/announcements/detail/1839041357029453
  Read via [1], 2026-10-07.
- [11] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released*.
  Steam announcement, 2025-12-11 (title and date only).
  https://steamcommunity.com/games/108600/announcements/detail/1818752592122972
  Listed in [1], 2026-10-07.
- [12] **The Indie Stone** — *Stable(41.78.19) + UNSTABLE(42.16.3) Hotfixes
  Released*. Steam announcement, 2026-04-08 (title and date only).
  https://steamcommunity.com/games/108600/announcements/detail/1829528821304362
  Listed in [1], 2026-10-07.
- [13] **The Indie Stone** — *Build 42.19.0 Unstable Released*. Steam
  announcement, 2026-06-01 (title and date only).
  https://steamcommunity.com/games/108600/announcements/detail/1833968530897275
  Listed in [1], 2026-10-07.
- [14] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first
  post 2026-09-23; abridged change list). https://theindiestone.com/forums/topic/101693-4221-patch-notes/
  Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)**

- None used in this document.

**Secondary & Corroborating**

- None used in this document.

**Community & Creator**

- None used in this document.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- creator-foundation, for the launch-window framing and audience data that
  this guide follows on from.
- The Indie Stone forums host the complete 42.21 update notes [14], linked from
  the Steam announcements above.

# Related Documents

- creator-foundation — the launch-window landscape this calendar follows.
- creator-format-catalogue — format choices that fill the slots.
- creator-channel-competitor-map — who else is publishing against each hook.
- creator-cross-promotion-funnel — where each slot's audience goes next.
- players-beginner-guide-b42, players-b41-to-b42-transition,
  players-farming-food, players-animals-husbandry, players-vehicles,
  players-medical-moodles — fact-check material for the slots.
- admins-modded-server-runbook, modders-first-mod-tutorial-b42 — server and
  modding fact-check material.
- meta-style-guide — the editorial rules this document follows.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: 42.21 change table completed from the TIS forum 42.21 patch notes [14] and the 42.20.1-42.21 Steam posts; announced-but-unshipped table re-checked against the forum list; interval arithmetic recomputed (no changes); staleness map and video-staleness table extended. | — |
