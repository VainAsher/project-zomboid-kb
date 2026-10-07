---
id: creator-format-catalogue
title: "Project Zomboid Content Format Catalogue: What Works, What It Costs and Which Build It Needs"
version: 1.0.0
status: approved
confidence: Medium
category: Creator
topic: "Format catalogue"
build: B42
document_type: reference
created: 2026-10-07
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [creator-foundation, creator-channel-competitor-map, creator-cross-promotion-funnel, creator-content-calendar, players-beginner-guide-b42, players-b41-to-b42-transition, players-animals-husbandry, players-crafting-chains, admins-modded-server-runbook, modders-first-mod-tutorial-b42, lore-foundation, players-foundation, admins-foundation, modders-foundation, meta-style-guide]
tags: [creator, formats, catalogue, youtube, patch-cadence, re-record, b42-stable]
game_versions_verified: ["42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | creator-format-catalogue |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Creator |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 42.21 (patch posts 42.20.0 to 42.21 and the TIS forum 42.21 change list read 2026-10-07; not re-tested in game) |

# Executive Summary

This catalogue lists thirteen video, stream and short-form formats that exist
on the Project Zomboid channel landscape, and for each one records an
observed example that was actually opened, plus the patch events that make
footage go stale. Existence evidence is limited to creator-track material:
video pages on YouTube, never game-fact sourcing. The patch history that
decides what must be re-recorded comes from the official Steam announcements:
seven dated releases (six stable-branch posts and one Unstable post) between
2026-07-29 and 2026-09-28 [1][2][3][4][5][6][7], plus the full 42.21 changelist
from the TIS forum [38].

The catalogue deliberately separates three things. The Reference section
records only checkable facts: which videos exist, when they were uploaded,
how long they run, and what each patch changed. The effort classes, the
re-record matrix and the "which format suits which goal" reading live in
Practical Guidance, because they are producer judgement. Claims that
cannot be traced to anything openable are quarantined.

Confidence is **Medium**: the patch facts are primary, but the format
evidence is a point-in-time sample found through YouTube's own search page on
2026-10-07, so it is neither exhaustive nor a ranking of what performs best.

# Key Takeaways

- Between stable release 42.20.0 on 2026-07-29 and 42.21 on 2026-09-28 there
  were four 42.20.x hotfix releases on three dates, so footage recorded in the first weeks can
  predate the current stable *(cited)* *(B42)* [1][2][3][4][5][7].
- The Indie Stone says every future release should move through Unstable
  first and then to Stable, which gives creators a published preview window
  before each stable promotion *(cited)* *(B42)* [7].
- Patch-breakdown videos for 42.21 were uploaded on 2026-09-26 and
  2026-09-27, inside the Unstable window and before the 2026-09-28 stable
  promotion *(cited)* [6][7][19][21].
- Every format in the sample table has at least one opened example; a
  vertical Shorts format has none and is quarantined *(cited / quarantined)*
  [9][35][36].
- Mod-dependent formats carry extra staleness triggers: 42.20.2 changed how
  `%` is handled in mod text, and 42.20.4 removed two Lua methods that 42.21
  then re-enabled *(cited)* *(B42)* [3][5][7].
- Not every B42 video in the sample was recorded on stable; one
  beginner-tips example was uploaded in June 2025 during the unstable cycle
  *(cited)* [14].
- View figures in this document are point-in-time watch-page counts, not
  creator analytics *(cited as snapshots)*.

# Purpose

The creator-foundation document maps channels and the launch window; this
document goes one level down and answers a planning question: which formats
exist, what footage each one burns when the game patches, and which
knowledge-base documents can supply fact-checking material for each. It is
meant to be read alongside the calendar and funnel documents, not to
replace them.

# Scope

Covered: thirteen formats, each with observed examples, upload dates, observed
runtimes, patch-sensitivity facts from the official announcements, and a
fact-check source map to sibling KB documents. Build tag is B42 because the
patch-sensitivity analysis keys off the 42.20 and 42.21 stable line. B41
appears only where a sampled video is explicitly B41.

Not covered: channel-by-channel profiling (see creator-foundation and
creator-channel-competitor-map), upload scheduling (creator-content-calendar),
platform-to-platform routing (creator-cross-promotion-funnel), monetisation
rules, editing technique, and any private analytics.

# Definitions

- **Re-record trigger** — a documented patch change that can make previously
  captured footage or narration inaccurate or visually dated.
- **Effort class** — a producer-side cost bucket (S, M, L, XL) assigned in
  Practical Guidance; it is a judgement, not a measurement.
- **Watch-page snapshot** — the view count and upload date shown on a public
  YouTube watch page on the stated retrieval date [9].
- **Unstable window** — the interval between a build reaching the opt-in
  Unstable branch and its promotion to Stable [6][7].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Context only | 41.78.21 mentioned in a hotfix post | The legacy branch received a security hotfix alongside 42.20.4 [5]; one sampled video is explicitly B41 [18] |
| B42 (stable) | Yes | 42.21 (patch notes re-read 2026-10-07) | 42.20.0 released 2026-07-29 [1]; 42.21 promoted to Stable 2026-09-28 [7] |

The `game_versions_verified` field lists 42.21 because the patch table and the
re-record matrix were re-checked against the 42.20.1 to 42.21 announcements
[2][3][4][5][6][7] and the TIS forum 42.21 patch notes [38]; the forum list was
retrieved in abridged form. The effects are as documented in those posts, not
re-tested in-game. Stable is 42.21 as of 2026-09-28 [7], so any statement here
about "current stable" has a shelf life measured in weeks.

# Reference

## Stable-line patch events that matter to footage

| Date | Release | Documented change relevant to creators |
|------|---------|----------------------------------------|
| 2026-07-29 | 42.20.0 Stable | Stable release of Build 42 [1] |
| 2026-08-05 | 42.20.1 hotfix | Multiplayer anti-cheat Lua checksum validation improved, chunk-unloading performance problem on MP servers fixed, vehicles that vanished for players after another disconnected fixed, broken B41 worlds blocked from being hosted on B42 servers, mods gained the ability to write .json files [2] |
| 2026-08-05 | 42.20.2 hotfix | Percent-symbol handling in files changed; mods should write `%%` to show `%`, and a temporary workaround accepts both forms [3] |
| 2026-08-17 | 42.20.3 hotfix | Server player-limit handling improved with support for up to 254 players; "Loading Map" hang fixed; memory leak causes addressed; fewer black and gray boxes when moving fast [4] |
| 2026-08-26 | 42.20.4 stable, 42.19.2 unstable, 41.78.21 legacy | Security fixes; the `loadstring` and `loadstream` Lua methods were removed [5] |
| 2026-09-23 | 42.21 Unstable | First incremental post-B42 update; fixes for zombies vanishing after a chunk is left and re-entered, MP zombie duplication, and a change to how XXL trees cut away [6][38] |
| 2026-09-28 | 42.21 Stable | Promoted after the Unstable test; `loadstring` and `loadstream` re-enabled; Unstable-then-Stable stated as the standard procedure for all future releases [7] |

The 42.21 change list on the TIS forum adds creator-visible items that the
Steam posts only summarise [38]: Welder-occupation characters now start with
Welding recipes instead of Blacksmithing recipes; the in-game player map was
updated to remove inaccuracies while exploring; the Spawn Point Selection
preview videos were updated to match the map glow-up; the localization system
was updated to allow more translatable strings; a fix addressed spaces and
percentages not showing in the game UI; characters automatically re-equip items
after exercise; explosives work in basements; floorboard stash containers found
with annotated maps were renamed; several lamp tiles are brighter; and the
in-game credits were updated [38]. The same list says player pathfinding now
avoids farming plants where possible, with the clarification that stepping on
crops never damaged them, so the change is cosmetic [38]. It also lists a
Discord-integration connection-loop fix and a Seam Editor added to the debug
menu [38].

The 42.21 announcement says the vanishing-zombie issue was most obvious in
large-population games, and that a few instances remain for a later update
[7]. The same announcement says the XXL tree cutaway now behaves better for
players in vehicles, no longer hides houses and furniture beneath the tree,
and has adjusted transparency [7]; the forum list calls the tree work in progress
[38].

## The format sample

All rows below were opened on 2026-10-07. Upload date and runtime were read
from the video's public watch page; the oEmbed endpoint returned the title
and uploader name for each. View counts are watch-page snapshots from that
date and are shown only to indicate that the format has been published at
scale, not as performance benchmarks [9].

| # | Format | Example (uploader, title shorthand) | Uploaded | Runtime | Snapshot views |
|---|--------|-------------------------------------|----------|---------|----------------|
| 1 | Challenge run | ThatGuyPredz, 100 days of Extinction mode in Louisville [9] | 2026-08-21 | 101 min | 949,988 |
| 1 | Challenge run | ambiguousamphibian VODs, 100-day CDDA all-negative-traits stream [10] | 2023-12-24 | 183 min | 686,818 |
| 2 | Survival series, edited | Pr1vateLime, 50 days trapped in a trailer park supercut [11] | 2024-04-27 | 291 min | 208,187 |
| 2 | Survival series, edited | Zombie-Ash-Gaming, 100 days in Build 42 Stable, Part 1 [12] | 2026-08-01 | 116 min | 186,089 |
| 2 | Survival series, edited | Mr Egg Hat, 100 days trying to live forever, B42 movie [13] | 2026-09-02 | 205 min | 200,072 |
| 3 | Beginner guide | Duckie0012, Beginner's Guide, Build 42 Stable [15] | 2026-08-03 | 32 min | 77,247 |
| 3 | Beginner guide | OVERCHARGED EGG, Ultimate Noobs Guide to B42, Day 1 [16] | 2026-08-07 | 52 min | 279,489 |
| 3 | Beginner guide | Mattsi, Beginner Tips for Build 42 [14] | 2025-06-15 | 15 min | 195,954 |
| 4 | Mechanics explainer | Retanaru, Build 42 Combat Changes Explained [17] | 2024-12-21 | 10 min | 224,763 |
| 4 | Mechanics explainer | Retanaru, Mechanic Guide B41 [18] | 2021-09-13 | 2 min | 45,076 |
| 5 | Patch-note breakdown | Awpenheimer, 42.21 update [19] | 2026-09-26 | 17 min | 103,310 |
| 5 | Patch-note breakdown | MrAtomicDuck, The Unstable Branch Is Back [21] | 2026-09-27 | 15 min | 93,029 |
| 5 | Patch-note breakdown | Awpenheimer, Build 42 Stable released, what changed [20] | 2026-07-30 | 22 min | 141,370 |
| 6 | Build-change review | MrAtomicDuck, What changed with the Stable map update [22] | 2026-08-15 | 27 min | 94,768 |
| 7 | Mod showcase / roundup | ZiubisPZ, 30 best mods for B42 Stable [23] | 2026-09-23 | 39 min | 97,019 |
| 7 | Mod showcase / roundup | MrDodgex, mods for B42.20 [24] | 2026-08-23 | 10 min | 248,787 |
| 7 | Mod showcase / roundup | MrAtomicDuck, new B42 mods April 2026 [25] | 2026-04-09 | 17 min | 169,082 |
| 8 | Modded-server series / session | Nurse VODs, 10-hour modded multiplayer B41 [26] | 2025-11-09 | 620 min | 1,900 |
| 8 | Modded-server series / session | Nurse, live: join a random multiplayer server (stream archive) [37] | 2026-09-24 | 128 min | 9,349 |
| 9 | Lore / history essay | Ricksdetrix, the entire lore of Project Zomboid [27] | 2023-09-09 | 44 min | 3,373,398 |
| 9 | Lore / history essay | SQz, What caused the Knox Event [28] | 2026-09-04 | 42 min | 417,979 |
| 10 | Multiplayer drama / RP | Rimmy Downunder, NearlyDead: RP, The Friendly Hostage Situation [29] | 2022-01-11 | 37 min | 343,278 |
| 10 | Multiplayer drama / clan event | HarvestZ, 100 players vs the deadliest clan [30] | 2026-08-21 | 37 min | 943,294 |
| 10 | Multi-creator event | Pr1vateLime, 5 YouTubers TILEMAN challenge [31] | 2023-06-25 | 23 min | 192,166 |
| 11 | Tutorial, system-specific | cosmiicsteem, in-depth animal husbandry guide, B42 [32] | 2025-05-05 | 5 min | 82,320 |
| 11 | Tutorial, system-specific | Mattsi, the best animal guide for B42 [33] | 2025-11-05 | 15 min | 56,154 |
| 12 | Clips / compilations | Top Gaming Plays, Top 100 WTF and funny moments #5 [34] | 2026-08-29 | 11 min | 114,744 |
| 13 | Scripted short film / story | Mr Sunshine, One Year in the Apocalypse (short film) [35] | 2026-03-05 | 7 min | 800,470 |
| 13 | Scripted short film / story | Pebal, Hollow, a Project Zomboid short story [36] | 2026-04-02 | 3 min | 97,687 |

Format numbers 1 to 13 in the first column are this catalogue's own labels and
are reused in the guidance tables below.

Two dating facts are worth recording because they bear on staleness. The two
42.21 patch videos [19][21] were uploaded on 2026-09-26 and
2026-09-27, after the Unstable release on 2026-09-23 and before the Stable
promotion on 2026-09-28 [6][7]. The Mattsi "Beginner Tips for Build 42" video was
uploaded on 2025-06-15 [14], more than a year before the 2026-07-29 stable
release [1].

# B41 vs B42 Delta

Not applicable — single-build document. The catalogue is tagged B42 because
its patch-sensitivity analysis concerns the 42.20.x and 42.21 stable line.
The only build-pair facts used are that a 41.78.21 legacy hotfix shipped with
42.20.4 [5] and that 42.20.1 stopped broken B41 worlds from being hosted on B42
servers [2]; the mechanical B41-to-B42 differences themselves belong to
players-b41-to-b42-transition.

# Practical Guidance

These are producer judgements built on the cited facts above. They add no
new factual claims.

## Effort classes (judgement)

| Class | Meaning | Formats |
|-------|---------|---------|
| S | Short capture, light edit | Clips and compilations (12); patch-note breakdowns (5) when the notes are short |
| M | Planned capture plus scripted narration | Beginner guide (3); mechanics explainer (4); tutorial (11); mod roundup (7) |
| L | Long capture or heavy research | Challenge run (1) edited; build-change review (6); lore essay (9); multiplayer drama (10) |
| XL | Hundreds of hours of source footage or an organised group | Survival series supercut (2) given observed runtimes of 116 to 291 minutes per uploaded entry [11][12][13]; modded-server series (8) whose single archived session ran 620 minutes [26]; multi-creator event (10) [31] |

## Re-record matrix (judgement from documented patch events)

| Format | What a patch can invalidate | Evidence it matters |
|--------|-----------------------------|---------------------|
| Challenge run, survival series | Mostly the visual and zombie-behaviour baseline; a run recorded across 42.20.x may contain the vanishing-zombie bug, MP zombie duplication, or XXL trees hiding houses and furniture | Fixes and tree-cutaway changes documented in 42.21 [6][7][38] |
| Beginner guide, tutorial | Narration claims about systems; on-screen UI; Welder starting recipes; the map screen and Spawn Point Selection previews; re-equip after exercise; the localization strings | Hotfix waves of 2026-08-05 to 2026-08-26 [2][3][4][5]; 42.21 list [38] |
| Farming, food and crafting tutorial | Fridge and freezer behaviour on power loss, water purification in ovens, washing machines cleaning rags and bandages, antibiotic packing, zombie-trampled furrows | 42.21 balance and fixes list [6][38] |
| Map and exploration walkthrough | The in-game player map as shown while exploring; map glow-up spawn-selection previews | 42.21 list [38] |
| Driving and vehicle guide | Tree cutaway for drivers, high-ping driving behaviour in MP | 42.21 [7][38] |
| Mechanics explainer | Numbers and rules; check before each stable promotion | Unstable-first policy gives a preview [7] |
| Patch-note breakdown | The video is the patch; it is dated by definition and best tied to the Unstable-to-Stable gap | Uploads fell in that gap [19][21] |
| Mod showcase | Mod text containing `%`, mods that used `loadstring` or `loadstream`, mod translations affected by the localization-system update | [3][5][7][38] |
| Modded server session | Server and client mod versions, the player limit, anti-cheat checks, the version-mismatch connect notice and server-browser wipe display | [2][4][5][38] |
| Lore essay | Least affected by the patch events listed here, because none of the sampled announcements concern lore | Judgement; see Claim 3 |
| Clips and compilations | Little beyond visible UI; date-label the build | Judgement |

## Fact-checking supply by format

- Beginner guides: players-beginner-guide-b42, players-foundation.
- Transition and build-review content: players-b41-to-b42-transition.
- Animal and crafting tutorials: players-animals-husbandry, players-crafting-chains.
- Modded-server series and mod showcases: admins-modded-server-runbook,
  modders-foundation; for a creator who wants to build a showcase mod,
  modders-first-mod-tutorial-b42.
- Lore essays: lore-foundation.
- Event and funnel structure: creator-content-calendar and
  creator-cross-promotion-funnel.

None of the videos in the sample is a source for any game fact in this KB.

## Reading the sample

- The 2026 upload dates cluster after the 2026-07-29 stable release for
  beginner guides [15][16] and Build 42 survival series [12][13], which fits the
  launch-window view in creator-foundation without proving causation.
- Event-driven formats such as patch breakdowns have a window as short as the
  gap between Unstable and Stable [19][21]; budget capture for that window.
- Narrative pieces [27][28][35][36] carry their own date risk only if they
  quote game numbers, which should be avoided.

# Common Pitfalls & Troubleshooting

- **Recording a "current stable" tutorial on 42.20.x.** Stable moved on to
  42.21 on 2026-09-28 [7]; date-stamp the build on screen.
- **Treating snapshot views as a ranking.** The counts are watch-page
  snapshots taken on one day [9], and they are affected by age: the sample
  ranges from 2021 to 2026 uploads, so older and newer entries are not
  comparable.
- **Citing a showcase or clip as a game-fact source.** All sampled videos are
  creator-track evidence only; verify game facts against the KB's primary
  sources.
- **Showcasing mods without a patch check.** Two Lua methods were removed on
  2026-08-26 and re-enabled on 2026-09-28 [5][7], so a mod that worked, broke
  and worked again within five weeks.
- **Assuming unstable-era footage still holds.** At least one beginner-tips
  example dates from the unstable cycle [14].
- **Mixing up uploader and originator.** The sample shows the same
  survival-challenge phrasing used by unrelated uploaders [9][12][13]; confirm
  the uploading channel before crediting.

# Community Notes & Unverified Claims

## Claim 1 — Patch-note breakdowns earn most of their views in the first days after a release

- **Claim:** Creator folk wisdom holds that patch-breakdown videos are a race, with most lifetime views arriving shortly after the patch.
- **Why unverified:** Only snapshot totals are observable from public watch pages; the per-day curve needs the creator's analytics, which no source here exposes.
- **Confidence:** Low. The uploads in the sample fell in the Unstable window [19][21] but that shows timing, not the view distribution.

## Claim 2 — Short vertical clips are a viable discovery route for Project Zomboid

- **Claim:** Creators and growth guides say vertical clips funnel viewers to long-form Project Zomboid content.
- **Why unverified:** No vertical-format Shorts example was opened for this catalogue and no Zomboid-specific evidence of effect exists in the sources used; the only short-duration examples found are scripted films [35][36].
- **Confidence:** Low. The claim is general platform lore, not something this sample supports.

## Claim 3 — Lore essays stay valid across patches

- **Claim:** Lore creators and viewers treat lore essays as evergreen because patch notes rarely touch lore.
- **Why unverified:** The announcements read for this document contain no lore changes, but absence in a sample of seven posts is not proof of absence across all patches or forum notes.
- **Confidence:** Medium. The sampled essays range from 2023 to 2026 [27][28] and the sampled patch posts [1][2][3][4][5][6][7] do not concern lore, which is consistent with the claim.

# Risks & Caveats

- **Sample bias.** Examples came from YouTube's own search ranking on one
  day, so they favour already popular, recent items [9].
- **Snapshot decay.** View counts and "latest" statuses drift daily; every
  figure carries the date 2026-10-07.
- **Stable moves on.** The verified build is 42.21, stable since 2026-09-28
  [7]; later hotfixes could change the re-record picture.
- **Announcements read, not retested.** Patch effects are as documented in
  posts; the 42.21 forum changelist was read in abridged form (several sections
  are marked "selected") [38].
- **Unrelated numbers excluded.** Subscriber totals are deliberately left to
  creator-foundation and creator-channel-competitor-map, which label them as
  estimates.

# Verification Steps

1. Re-run the Steam news API call (app id 108600) and confirm the seven
   patch posts and dates in the patch table [8].
2. Open each video link in References and confirm title, uploader, upload
   date and runtime; the oEmbed endpoint returns title and uploader.
3. Re-read each watch page for the current view count and compare to the
   snapshot column; large drift is expected.
4. Check whether a later hotfix or 42.22 post exists and, if so, add a row to
   the patch table and revise the matrix.
5. Search YouTube for a vertical Shorts example to retire or upgrade Claim 2.

# Open Questions

- Which formats show the highest retention for B42 content? Only creator
  analytics could answer this.
- Is a vertical short-form route measurably useful for this game (Claim 2)?
- How soon after each stable promotion do patch-breakdown uploads cease to
  draw views (Claim 1)?
- Does the Unstable-first procedure [7] remain in force for the next release,
  and how long will the Unstable window be?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released*. Steam announcement, 2026-07-29. https://steamcommunity.com/games/108600/announcements/detail/1839676055882259 Accessed 2026-10-07 via the Steam news API [8].
- [2] **The Indie Stone** — *42.20.1 STABLE Hotfix Released*. Steam announcement, 2026-08-05. https://steamcommunity.com/games/108600/announcements/detail/1840310314338766 Accessed 2026-10-07 via the Steam news API [8].
- [3] **The Indie Stone** — *42.20.2 STABLE Hotfix Released*. Steam announcement, 2026-08-05. https://steamcommunity.com/games/108600/announcements/detail/1840310314339441 Accessed 2026-10-07 via the Steam news API [8].
- [4] **The Indie Stone** — *42.20.3 STABLE Hotfix Released*. Steam announcement, 2026-08-17. https://steamcommunity.com/games/108600/announcements/detail/1840944183785895 Accessed 2026-10-07 via the Steam news API [8].
- [5] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released*. Steam announcement, 2026-08-26. https://steamcommunity.com/games/108600/announcements/detail/1842212951296601 Accessed 2026-10-07 via the Steam news API [8].
- [6] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released*. Steam announcement, 2026-09-23. https://steamcommunity.com/games/108600/announcements/detail/1844751498218925 Accessed 2026-10-07 via the Steam news API [8].
- [7] **The Indie Stone** — *Build 42.21 Stable Released*. Steam announcement, 2026-09-28. https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07 via the Steam news API [8].
- [8] **Valve** — *Steam news feed for app 108600 (ISteamNews GetNewsForApp)*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=40&maxlength=0 Accessed 2026-10-07.
- [38] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post 2026-09-23; abridged change list). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)**

- None used in this document.

**Secondary & Corroborating**

- None used in this document.

**Community & Creator** (YouTube video pages; title and uploader confirmed via the YouTube oEmbed endpoint, upload date, runtime and snapshot views read from the watch page; all accessed 2026-10-07; creator-track evidence only)

- [9] **ThatGuyPredz** — *I Survived 100 Days Of Project Zomboid's EXTINCTION Mode... In LOUISVILLE*. https://www.youtube.com/watch?v=IdRhC2npKKg
- [10] **ambiguousamphibian VODs** — *Surviving 100 Days in Project Zomboid: CDDA Challenge, All Negative Traits (Full Stream)*. https://www.youtube.com/watch?v=NHTfSA4BF3Y
- [11] **Pr1vateLime** — *I Survived 50 Days TRAPPED Inside A Trailer Park | Project Zomboid Supercut*. https://www.youtube.com/watch?v=HudePGY1lOI
- [12] **Zombie-Ash-Gaming** — *I Survived 100 DAYS In Build 42 Stable for Project Zomboid | Part 1*. https://www.youtube.com/watch?v=oWB7fDyOKSQ
- [13] **Mr Egg Hat** — *100 Days Trying To Live Forever - Project Zomboid Build 42 Movie*. https://www.youtube.com/watch?v=fUHXb5j95aQ
- [14] **Mattsi** — *Beginner Tips for Project Zomboid Build 42!*. https://www.youtube.com/watch?v=3poHGgZ3AnI
- [15] **Duckie0012** — *Project Zomboid Beginner's Guide | Build 42 Stable*. https://www.youtube.com/watch?v=19mLw7E-yTc
- [16] **OVERCHARGED EGG** — *The ULTIMATE NOOBS GUIDE To Project Zomboid Build 42 | Day 1*. https://www.youtube.com/watch?v=ETUHLVlcf38
- [17] **Retanaru** — *Build 42 Combat Changes Explained - Project Zomboid*. https://www.youtube.com/watch?v=4RTZPDhi1Bk
- [18] **Retanaru** — *Be The Cool Car Guy | Mechanic Guide B41*. https://www.youtube.com/watch?v=WL8wB1AlBMA
- [19] **Awpenheimer** — *NEW Quality of Life & Gameplay Improvements!! - Project Zomboid Build 42.21 Update*. https://www.youtube.com/watch?v=i-n61uL5qmo
- [20] **Awpenheimer** — *Build 42 Stable RELEASED!! - What's Changed? (Major Project Zomboid Update)*. https://www.youtube.com/watch?v=Dj5oUEuaP1Y
- [21] **MrAtomicDuck** — *The Unstable Branch Is Back - Project Zomboid Build 42 Update News!*. https://www.youtube.com/watch?v=k_YxPOoBRyI
- [22] **MrAtomicDuck** — *What Changed With The Build 42 Stable Map Update For Project Zomboid?*. https://www.youtube.com/watch?v=IERDeZfJ1Y4
- [23] **ZiubisPZ** — *30 BEST Mods For Project Zomboid Build 42 Stable*. https://www.youtube.com/watch?v=G94jb8KY0D0
- [24] **MrDodgex** — *You NEED These Mods in Project Zomboid B42.20*. https://www.youtube.com/watch?v=2MVyEPPjJn0
- [25] **MrAtomicDuck** — *NEW Build 42 Mods For Project Zomboid, April 2026! Multiplayer Mods, Quality Of Life & More!*. https://www.youtube.com/watch?v=cwpddiG1AmU
- [26] **Nurse VODs** — *Project Zomboid, 10-Hour Modded Multiplayer B41 | NurseVO*. https://www.youtube.com/watch?v=xbvkbf2zWOQ
- [27] **Ricksdetrix** — *the entire lore of project zomboid i guess*. https://www.youtube.com/watch?v=SVZNtFnFopk
- [28] **SQz** — *What Caused the Knox Event in Project Zomboid?*. https://www.youtube.com/watch?v=bWxbGfhPEd0
- [29] **Rimmy Downunder** — *The Friendly Hostage Situation | NearlyDead: RP | Project Zomboid Multiplayer*. https://www.youtube.com/watch?v=ef2_j6SrudA
- [30] **HarvestZ** — *100 Players vs the Deadliest Clan in Project Zomboid*. https://www.youtube.com/watch?v=ddyLw9mgwJQ
- [31] **Pr1vateLime** — *Can 5 Youtubers Survive The TILEMAN Challenge In Project Zomboid*. https://www.youtube.com/watch?v=0X4EiZZJ03E
- [32] **cosmiicsteem** — *In-Depth Animal Husbandry Guide For Project Zomboid Build 42!*. https://www.youtube.com/watch?v=iPWLVm5QRKA
- [33] **Mattsi** — *The BEST Animal Guide for Project Zomboid build 42*. https://www.youtube.com/watch?v=h8JO384cEnk
- [34] **Top Gaming Plays** — *Top 100 PROJECT ZOMBOID WTF & Funny Moments! #5*. https://www.youtube.com/watch?v=eFHPjOnPcyQ
- [35] **Mr Sunshine** — *One Year in the Apocalypse | Project Zomboid Short Film*. https://www.youtube.com/watch?v=ie5luU5lQVQ
- [36] **Pebal** — *Hollow | A Project Zomboid Short Story*. https://www.youtube.com/watch?v=xI2FpEJVB3s
- [37] **Nurse** — *I Joined a Random Project Zomboid Multiplayer Server and The Origin of the Creamery #LIVE*. https://www.youtube.com/watch?v=ZR4yvbUoe70

**Further Reading**

- See the Further Reading section below.

# Further Reading

- creator-foundation, for channel profiles and the launch-window audience data.
- creator-content-calendar, for when each format slots against patch rhythm.
- The Indie Stone forums host the 42.21 changelist referenced by [6][7][38].

# Related Documents

- creator-foundation — channel landscape and launch window.
- creator-channel-competitor-map — who occupies each format.
- creator-cross-promotion-funnel — routing between platforms.
- creator-content-calendar — release rhythm and patch hooks.
- players-beginner-guide-b42, players-b41-to-b42-transition,
  players-animals-husbandry, players-crafting-chains — fact-check material.
- admins-modded-server-runbook, modders-first-mod-tutorial-b42 — modded
  server and showcase fact-checking.
- lore-foundation, players-foundation, admins-foundation, modders-foundation,
  meta-style-guide.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: patch table and re-record matrix extended from the TIS forum 42.21 patch notes [38] (Welder start recipes, XXL trees, map and spawn-selection UI, localization, farming and refrigeration, MP notices); corrected "hotfix waves" count; game_versions_verified set to 42.21. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
