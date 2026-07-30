---
id: lore-foundation
title: "The Knox Event and the History of Project Zomboid's Builds"
version: 1.0.1
status: approved
confidence: Medium
category: Lore
topic: "Lore & history"
build: historic
document_type: overview
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [modders-foundation, players-foundation, admins-foundation, creator-foundation, meta-style-guide]
tags: [lore, knox-event, build-history, thursdoid, b41, b42, early-access, legacy41]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | lore-foundation |
| Version | 1.0.1 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Lore |
| Build | historic |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 41.78.16, 42.20 (via patch announcements; historic material verified against sources, not in-game) |

# Executive Summary

This document is the Lore-track foundation for the knowledge base. It does two jobs. First, it describes — at overview level and in original words — the fictional setting of Project Zomboid: the Knox Event, a 1993 zombie outbreak in rural Kentucky, and the radio, television and social-media devices The Indie Stone (TIS) uses to deliver that story. It deliberately does *not* retell the fiction; the narrative itself is TIS's copyrighted work, and this document only records dates, places and mechanisms with citations so that other documents can anchor lore references correctly.

Second, it records the real-world history of the game's builds: the 2011 origins and the November 2013 Steam Early Access launch [11][19], the Build 41 "animation overhaul" era that culminated in multiplayer (December 2021) and the long-lived 41.78.x patch line [5][6][15], the Build 42 era from the single-player unstable release of 17 December 2024 [3] through unstable multiplayer in 42.13.0 (11 December 2025) [4] to the stable 42.20 release of 29 July 2026 [1][2], the `legacy41` Steam branch that preserves Build 41 [1], and the shifting cadence of TIS's development blogs ("Mondoids", then "Thursdoids") [7][8][10].

Document confidence is **Medium**: the load-bearing release dates rest on official TIS blog posts and Steam records (primary sources), but several secondary dates (e.g. the exact 41.78.16 hotfix date and the 2026 maintenance patches to Build 41) are currently sourced only from pzwiki, and the blog-cadence analysis is an observation of the archive rather than a stated TIS policy.

# Key Takeaways

- The Knox Event is Project Zomboid's fictional zombie outbreak, set in July 1993 in and around Muldraugh and West Point, Kentucky; TIS itself dates the outbreak to 6 July 1993, and play begins on 9 July 1993 inside the military "Exclusion Zone" *(cited)* [9][14].
- The story is delivered indirectly: in-game radio and TV broadcasts during the first in-game weeks, environmental storytelling, and an official real-time social-media retelling (@TheKnoxEvent) launched for the outbreak's 30th anniversary in 2023 *(cited)* [9][14][16].
- Project Zomboid entered Steam Early Access on 8 November 2013 and, as of 30 July 2026, is still classed as an Early Access title *(cited)* [11][12][19].
- Build 41, "the animation overhaul", spent 2019–2021 in beta, gained multiplayer in the 41.60 test branch (December 2021), went stable on 20 December 2021, and its last patch of the active era was 41.78.16 (December 2022, date wiki-sourced) *(cited)* [5][6][15][17].
- Build 42 launched as a single-player-only unstable on 17 December 2024; multiplayer returned in unstable 42.13.0 on 11 December 2025; stable 42.20 shipped on 29 July 2026 *(cited)* [1][2][3][4][18].
- Players and server owners can stay on Build 41 via the `legacy41` Steam beta branch; B41 saves are not compatible with B42 *(cited)* [1].
- TIS dev blogs moved from Mondays ("Mondoid") to Thursdays ("Thursdoid") in September 2017; the observable cadence then slowed from weekly to roughly fortnightly (2022–2023) to monthly (2024), and paused for most of 2025 during heavy Build 42 work *(cited, cadence observed from the archive)* [7][8][10].
- A "Build 42 Support Update" focused on optimisation, modding support and polish is planned for the rest of 2026 *(cited)* [1].

# Purpose

This document exists so that every other document in the knowledge base can reference the game's fictional setting and its real-world release history without re-deriving either. It answers two questions: "What is the Knox Event, in outline, and how is that story told?" and "Which build shipped when, on which branch, and what does that mean for dating any fact about the game?" It is the anchor for the `build:` tags used across the knowledge base.

# Scope

Covered:

- The Knox Event setting at overview level: period, place, the Exclusion Zone, and the narrative-delivery devices (radio, TV, newspapers, the real-time social account). Facts and dates only, in original prose.
- Real-world build history: pre-Steam origins, Steam Early Access, Build 41 (beta, multiplayer, stable, final patches), Build 42 (unstable, multiplayer, stable 42.20), the `legacy41` branch, and the dev-blog cadence history.

Excluded:

- Any retelling or reproduction of TIS's fiction (broadcast transcripts, character dialogue, timeline prose). The lore is TIS's copyright; this document records only verifiable facts about it.
- Gameplay mechanics, modding APIs, server administration and creator topics — see the sibling foundation documents (`players-foundation`, `modders-foundation`, `admins-foundation`, `creator-foundation`).
- Per-patch changelog detail for the dozens of 41.x and 42.x releases; only era-defining milestones are recorded here.

# Definitions

- **Knox Event** — the in-fiction name for the zombie outbreak at the start of the game's story [14].
- **Knox Country** — the game's partially fictional Kentucky setting, modelled on the real Muldraugh / West Point / Louisville area [19].
- **Exclusion Zone** — the in-fiction military quarantine area around the outbreak; the player is a survivor inside it [14].
- **Mondoid / Thursdoid** — community-and-developer names for TIS's regular development blog, published on Mondays until September 2017 and on Thursdays thereafter [7].
- **IWBUMS / unstable** — TIS's opt-in public beta branch ("I Will Back Up My Save"); the term IWBUMS was used through the B41 era, with "unstable" the usual B42-era term [15][16].
- **legacy41** — the Steam beta branch that keeps an installation on Build 41 after Build 42 became the default stable build [1].

# Build Applicability

This is a `historic` document: its subject is the game's setting and release history, not a mechanic that differs between builds. Its facts were verified against the sources below as of 2026-07-30, when the current builds were 41.78.x on the `legacy41` branch and 42.20 stable [1][2].

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| Pre-B41 (2011–2019) | Background only | Official blog archive, Steam records [10][11][12] | Covered as history, not verified in-game |
| B41 (legacy41) | Yes, as background | Release announcements [5][6]; patch list wiki-sourced [15] | Setting facts and dates apply |
| B42 (stable 42.20) | Yes, as background | Release announcements [1][2][3][4] | Setting facts and dates apply; B42 added further lore broadcasts [16] |

# Reference

## The Knox Event setting

Project Zomboid's story takes place in July 1993 in "Knox Country", a partially fictional slice of rural Kentucky built around the real towns of Muldraugh and West Point and the city of Louisville [14][19]. The fiction concerns a sudden infection outbreak: TIS's own 30th-anniversary post dates the outbreak to 6 July 1993, the day the fiction has the US military blockading roads around the area [9][14]. The quarantined area is designated an Exclusion Zone, and the game itself begins on 9 July 1993, with the player as an ordinary survivor trapped inside the Zone shortly after the military evacuation of the surrounding population [14]. Over the following in-fiction days the containment fails, the infection spreads beyond Kentucky, and organised broadcasting collapses — the story frame that leaves the player alone in an emptied Knox Country [14]. The wiki's timeline additionally treats 4 July 1993 as the notional start of the incident itself, two days before the blockade; this document follows TIS's primary statement (6 July) for the outbreak date and notes the discrepancy [9][14].

## Narrative-delivery devices

The story above is never narrated directly. It is delivered through in-world media that the player can consume during the first in-game weeks: radio and television channels whose news programming tracks the outbreak day by day, and in-world newspapers [14]. Build 42 extended this apparatus with additional radio and TV broadcasts and channels, and made it possible to find characters from those broadcasts at their in-fiction places of work and death [16]. Outside the game, TIS ran an official real-time retelling for the outbreak's 30th anniversary: from 6 July 2023 the @TheKnoxEvent account on X/Twitter posted the fictional timeline "in real time", thirty years on [9]. The pzwiki lore pages archive these posts with third-party snapshots [14].

Because all of this material is TIS's copyrighted fiction, this knowledge base cites it and describes its mechanisms but does not reproduce transcripts or timeline prose.

## Early access origins (2011–2013)

Project Zomboid was announced by The Indie Stone in March 2011 and first sold as a paid pre-alpha in mid-2011, distributed outside Steam [19]. It joined Steam Early Access on 8 November 2013 — the release date shown on its Steam store page — and its oldest Steam community announcement ("PZ Launch Weekend Streams") carries the same date [11][12]. As of 30 July 2026 the store still lists the game under Early Access, meaning the game has now spent more than twelve and a half years in Early Access without a 1.0 release [11].

## Build 41 — the animation-overhaul era (2019–2022)

Build 41, known as the Animation Overhaul, rebuilt the game's animation, character and combat systems and added the city of Louisville; its first opt-in IWBUMS beta arrived in October 2019 [15]. Multiplayer — rebuilt from the ground up for B41 — arrived on 9 December 2021 in the dedicated 41.60 test branch [5], initially capped to 16-player servers [17]. Build 41 was then released as the stable build on 20 December 2021 [6][15].

Through 2022 the 41.x line received a steady stream of patches, ending its active development era at 41.78.16, which pzwiki dates to 12 December 2022 [15]. That version remained the de-facto stable Build 41 for over three years and is the version this knowledge base tags as B41 (41.78.16). The wiki's version table also records a later wave of 41.78.x maintenance releases during 2026 (41.78.17 through 41.78.20, the last dated 29 July 2026, the same day B42 went stable), which this document treats as legacy41-branch maintenance; no official patch notes for these have been located yet [15].

## Build 42 — the expanded crafting and balance era (2024–2026)

Build 42, themed around expanded crafting, balance, animals and engine upgrades (new lighting, basements, taller buildings, map expansion), was released to the unstable beta on 17 December 2024 as version 42.0.0 [3][16]. The unstable release plans had been set out in the preceding "WhatZ Next" blog of 28 November 2024 [13]. This initial B42 release was single-player only; online multiplayer did not return until unstable 42.13.0 on 11 December 2025, which TIS announced as the first Build 42 version with online multiplayer, recommended at the time for co-op and whitelisted servers with modest player caps while stress-testing continued [4][18].

After a further run of unstable versions (42.14 through 42.19), TIS announced on 24 July 2026 that version 42.20 would go directly to the stable public branch on Wednesday 29 July 2026 [1], and the stable release shipped on that date [2]. For the remainder of 2026 TIS has stated it will work on a "Build 42 Support Update" focused on optimisation, additional modding support, and player-requested polish, alongside continued multiplayer and controller improvements, plus releases of its mapping tools and the AnimZed animation editor [1].

## The legacy41 branch

Build 41 savegames are not compatible with Build 42 [1]. Ahead of the stable switch, TIS documented an existing Steam beta channel named `legacy41` for players and server operators who want to remain on Build 41, selected from the game's Properties → "Game Versions & Betas" menu in Steam [1]. A parallel `42.19` beta branch was provided for players finishing unstable-era saves that are incompatible with 42.20 [1].

## Thursdoid cadence history

TIS's development blog began as a weekly Monday post, community-nicknamed the "Mondoid". In September 2017 the post "Thursdoid Rising" moved the blog to Thursdays, inaugurating the "Thursdoid" era [7]. The observable cadence in the official news archive then slowed in stages [10]:

| Era | Observable cadence | Evidence |
|-----|--------------------|----------|
| 2011 – Sep 2017 | Weekly (Mondays) | Archive density; "Thursdoid Rising" announces the switch [7][10] |
| Sep 2017 – 2021 | Weekly (Thursdays) | Archive density [10] |
| 2022 – 2023 | Dev Thursdoids roughly fortnightly, interleaved with mod/community spotlights | Archive post dates [10] |
| 2024 | Dev Thursdoids roughly monthly (e.g. Leapdoid 29 Feb, Zaumby Thursday 28 Mar, …, WhatZ Next 28 Nov) | Archive post dates [10] |
| 2025 | Effectively paused: no posts between 24 Dec 2024 and 17 Oct 2025 | Archive gap; "Since Last We Spoke" opens by summarising "the past twelve months" [8][10] |
| Dec 2025 – Jul 2026 | Event-driven posts around MP and the stable release | Archive post dates [1][2][4][10] |

No blog post formally announcing the fortnightly or monthly shifts has been located; the cadence rows above are observations of dated posts in the official archive, not statements of TIS policy [10].

## Milestone table

| Date | Milestone | Source class |
|------|-----------|--------------|
| 2011 (March announcement; mid-2011 paid pre-alpha) | Project Zomboid announced and first sold | Fact-only wiki [19] |
| 1993-07-06 *(in fiction)* | Knox Event outbreak date per TIS | Primary [9] |
| 2013-11-08 | Steam Early Access release | Primary [11][12] |
| 2017-09-21 | Blog moves Monday → Thursday ("Thursdoid Rising") | Primary [7] |
| 2019-10 | First Build 41 IWBUMS beta | Fact-only wiki [15] |
| 2021-12-09 | B41 multiplayer test branch (41.60) released | Primary [5] |
| 2021-12-20 | Build 41 released as stable | Primary [6] |
| 2022-12-12 | 41.78.16, last patch of B41's active era | Fact-only wiki [15] |
| 2024-12-17 | Build 42 unstable released (single-player only) | Primary [3] |
| 2025-12-11 | Unstable 42.13.0 — first B42 with multiplayer | Primary [4] |
| 2026-07-29 | Build 42.20 released to stable; `legacy41` branch preserves B41 | Primary [1][2] |

# B41 vs B42 Delta

Not applicable — this is a `historic` document; the build-to-build story *is* its subject. For the full narrative of what changed between the Build 41 era and the Build 42 era, see the "Build 41" and "Build 42" subsections of the Reference section above; for mechanic-level deltas, see the sibling track foundations.

# Practical Guidance

- **Date every fact you inherit.** Any guide, video or wiki statement about Project Zomboid should be mentally stamped with an era: pre-B41 (before October 2019), B41 beta (2019–2021), B41 stable (December 2021 – December 2024 as the default branch), B42 unstable single-player (December 2024 – December 2025), B42 unstable with MP (December 2025 – July 2026), or B42 stable (from 29 July 2026). Community material written during the B42 unstable window is especially likely to describe values that changed before 42.20 [1][3][4].
- **Check the branch before checking the fact.** A player or server on `legacy41` is on 41.78.x behaviour; the default branch is B42 stable. The branch switch is in Steam library → Properties → Game Versions & Betas [1].
- **Treat lore as citable, not copyable.** When a document needs a lore anchor (a date, a place, a broadcast's existence), cite the primary TIS post or a pzwiki lore page as a fact source and paraphrase in original words — never reproduce broadcast or timeline text [9][14].
- **For "when did X arrive" questions,** reach first for the official blog archive [10] and the Steam announcement mirror [12]; use pzwiki's per-version pages to fill gaps, at fact-only status [15][16][17][18].

# Common Pitfalls & Troubleshooting

- **Conflating the B42 unstable launch with multiplayer availability.** B42 had no online multiplayer for almost a year: 17 December 2024 (42.0.0, single-player) to 11 December 2025 (42.13.0) [3][4]. Community server guides written in that window may wrongly imply B42 MP does not exist, or describe B41 MP behaviour.
- **Assuming "stable" always meant B41 41.78.16.** Since 29 July 2026 the default stable branch is B42 42.20; B41 lives on only via `legacy41` [1][2]. Conversely, sources written before that date use "stable" to mean 41.78.x.
- **Save incompatibility surprises.** B41 saves do not load in B42, and unstable 42.19 saves do not load in 42.20; TIS provided the `legacy41` and `42.19` branches specifically for this [1].
- **Outbreak-date confusion.** TIS marks the Knox Event outbreak as 6 July 1993 [9], while the community wiki's timeline treats 4 July 1993 as the incident's notional beginning with the blockade following on 6 July [14]. Documents should prefer the TIS date and say which convention they use.
- **Mondoid/Thursdoid anachronisms.** Posts before late September 2017 are Monday blogs; citing a "Thursdoid" from 2015 is a dating error [7].

# Community Notes & Unverified Claims

## Claim 1 — Early development was set back by a 2011 burglary in which code was stolen

- **Claim:** It is widely retold in press coverage and community histories (e.g. the game's Wikipedia article and gaming-press archives) that in October 2011 laptops containing recent Project Zomboid code were stolen from the developers' home, costing significant progress during the pre-Steam era.
- **Why unverified:** No primary TIS statement was opened during research for this document; the claim currently rests on secondary retellings not in this document's reference list.
- **Confidence:** Medium. The story is consistently reported across independent secondary sources and is uncontested, but it is not yet traced here to a primary post.

## Claim 2 — TIS deliberately slowed the blog to monthly (and then paused it) to avoid repetitive updates during Build 42 development

- **Claim:** Community threads (Steam discussions) attribute the 2024 monthly cadence and the 2025 pause to a deliberate TIS decision to post less often while B42 work dominated, rather than to neglect.
- **Why unverified:** No official blog post announcing a fortnightly-to-monthly policy or a pause has been located; the archive shows the cadence change and the gap [8][10], but the *stated rationale* circulates only in community threads and scattered dev replies.
- **Confidence:** Medium. The observable cadence matches the claim exactly, and "Since Last We Spoke" implicitly acknowledges the year-long gap [8], but the rationale itself is community-attributed.

# Risks & Caveats

- **Recency:** Stable 42.20 shipped on 2026-07-29, one day before this document's verification date. Hotfixes and the announced Build 42 Support Update [1] may quickly change "current version" statements; the historic milestones themselves are stable.
- **Wiki-sourced dates:** The 41.78.16 date (2022-12-12), the 2019-10 start of the B41 beta, and the 2026 41.78.17–41.78.20 maintenance patches are currently sourced only from pzwiki version pages [15]; per the source rules they are capped at Medium confidence until corroborated by official patch notes.
- **Cadence analysis is observational:** The Thursdoid cadence table is derived from post dates in the official archive [10], not from a TIS statement; a formal announcement, if found, could adjust era boundaries.
- **Steam feed gap:** The Steam community-announcement feed used for corroboration has a sparse window for 2019–2021 (Steam's announcement system changed), so that era is corroborated mainly by the blog archive itself [10][12].
- **Fiction dates are in-universe:** All 1993 dates are facts *about the fiction*, cited to TIS or the wiki's archived record of TIS material; they are not claims about real events.

# Verification Steps

1. **Stable release date:** Open the TIS posts "BUILD 42 STABLE PLANS" and "PROJECT ZOMBOID BUILD 42.20 RELEASED!" [1][2] and confirm the 29 July 2026 stable date and `legacy41` instructions.
2. **Blog cadence:** Query the official blog's WordPress API, e.g. `https://projectzomboid.com/blog/wp-json/wp/v2/posts?per_page=100&after=2024-01-01T00:00:00&_fields=date,title,link`, and inspect post dates per year against the cadence table [10].
3. **Steam history:** Query the Steam news API (`ISteamNews/GetNewsForApp`, appid 108600) and confirm the oldest community announcement is dated 8 November 2013 and that "Build 42 Unstable Out Now" is dated 17 December 2024 [12].
4. **Branches:** In a Steam client, right-click Project Zomboid → Properties → Game Versions & Betas, and confirm `legacy41` (and `42.19`) appear as selectable branches [1].
5. **Version tables:** Fetch the pzwiki pages "Build 41" and "Build 42" via the MediaWiki API (`action=parse&prop=wikitext`) at the cited revision ids and re-check the per-version dates used here [15][16].
6. **Lore dates:** Open "Knox Event: 30 Years On" [9] for the TIS-stated outbreak date, and the pzwiki "Knox Event" page (cited revision) for the timeline facts [14].

# Open Questions

- Did TIS ever formally announce the fortnightly (2022) or monthly (2024) blog cadence, and where? Locating such a post would upgrade the cadence table from observation to stated policy.
- Are there official patch notes for 41.78.17–41.78.20 (2026 maintenance releases on `legacy41`), and what do they change? Currently wiki-sourced only [15].
- Will TIS designate a "final" Build 41 version for the legacy41 branch, or does maintenance continue indefinitely alongside the B42 Support Update [1]?
- What is the official position of the July 4 vs July 6 1993 outbreak-date framing within TIS's own materials [9][14]?
- When the Build 42 Support Update ships, does the KB need a new `historic` milestone entry and re-verification of the "current stable" statements [1]?

# References

**Primary Sources** — official blog/Thursdoids, Steam announcements/patch notes, dev posts.

- [1] **The Indie Stone** — *BUILD 42 STABLE PLANS* (blog, 2026-07-24). https://projectzomboid.com/blog/news/2026/07/build-42-stable-plans/. Accessed 2026-07-30.
- [2] **The Indie Stone** — *PROJECT ZOMBOID BUILD 42.20 RELEASED!* (blog, 2026-07-29). https://projectzomboid.com/blog/news/2026/07/project-zomboid-build-42-20-released/. Accessed 2026-07-30 (listed via the site's post index; mirrored on Steam news, 2026-07).
- [3] **The Indie Stone** — *Build 42 Unstable* (blog, 2024-12-17; Steam mirror "Build 42 Unstable Out Now", same date). https://projectzomboid.com/blog/news/2024/12/build-42-unstable/. Accessed 2026-07-30.
- [4] **The Indie Stone** — *Unstable 42 MP Released* (blog, 2025-12-11). https://projectzomboid.com/blog/news/2025/12/unstable-42-mp-released/. Accessed 2026-07-30.
- [5] **The Indie Stone** — *B41 MP Test 41.60 Branch Released!* (blog, 2021-12-09). https://projectzomboid.com/blog/news/2021/12/b41-mp-test-41-60-branch-released/. Accessed 2026-07-30.
- [6] **The Indie Stone** — *Project Zomboid – Build 41 – Released!* (blog, 2021-12-20). https://projectzomboid.com/blog/news/2021/12/project-zomboid-build-41-released/. Accessed 2026-07-30.
- [7] **The Indie Stone** — *Thursdoid Rising* (blog, 2017-09-21). https://projectzomboid.com/blog/news/2017/09/thursdoid-rising/. Accessed 2026-07-30.
- [8] **The Indie Stone** — *Since Last We Spoke* (blog, 2025-10-17). https://projectzomboid.com/blog/news/2025/10/since-last-we-spoke/. Accessed 2026-07-30.
- [9] **The Indie Stone** — *Knox Event: 30 Years On* (blog, 2023-07-06). https://projectzomboid.com/blog/news/2023/07/knox-event-30-years-on/. Accessed 2026-07-30.
- [10] **The Indie Stone** — *News archive* (blog index; post dates retrieved via the site's WordPress API, 2011–2026). https://projectzomboid.com/blog/news/. Accessed 2026-07-30.
- [11] **The Indie Stone / Valve** — *Project Zomboid* Steam store page (release date 8 Nov 2013; Early Access category). https://store.steampowered.com/app/108600/Project_Zomboid/. Accessed 2026-07-30.
- [12] **Valve (Steam news, app 108600)** — Community announcements feed, queried via the ISteamNews API; oldest item "PZ Launch Weekend Streams", 2013-11-08. https://steamcommunity.com/app/108600/announcements/. Accessed 2026-07-30.
- [13] **The Indie Stone** — *WhatZ Next* (blog, 2024-11-28). https://projectzomboid.com/blog/news/2024/11/whatz-next/. Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [14] **PZwiki** — *Knox Event* (revision 1441597, 2026-07-10). https://pzwiki.net/wiki/Knox_Event. Accessed 2026-07-30. Fact-only source.
- [15] **PZwiki** — *Build 41* (revision 1443631, 2026-07-29). https://pzwiki.net/wiki/Build_41. Accessed 2026-07-30. Fact-only source.
- [16] **PZwiki** — *Build 42* (revision 1443663, 2026-07-29). https://pzwiki.net/wiki/Build_42. Accessed 2026-07-30. Fact-only source.
- [17] **PZwiki** — *Build 41.60* (revision 1435629, 2026-05-24). https://pzwiki.net/wiki/Build_41.60. Accessed 2026-07-30. Fact-only source.
- [18] **PZwiki** — *Build 42.13.0* (revision 1435679, 2026-05-24). https://pzwiki.net/wiki/Build_42.13.0. Accessed 2026-07-30. Fact-only source.
- [19] **PZwiki** — *Project Zomboid* (revision 1436299, 2026-05-25). https://pzwiki.net/wiki/Project_Zomboid. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none used.

**Community & Creator** — none used (community claims are quarantined above without citation, per the genre rules).

**Further Reading**

# Further Reading

- The official @TheKnoxEvent account on X/Twitter — TIS's real-time anniversary retelling of the outbreak timeline (see [9] for its launch context).
- The pzwiki lore portal pages (Knox Country, characters, radio and TV channels) for deeper in-fiction detail, always at fact-only status.
- The Indie Stone forums (theindiestone.com/forums) — per-version changelog threads for every 41.x and 42.x release.

# Related Documents

- `players-foundation` — the core game across B41 and B42, for the player-facing consequences of the build history recorded here.
- `modders-foundation` — modding foundations; the B42 era's modding-facing changes.
- `admins-foundation` — server administration; branch selection (`legacy41`) and MP-era differences.
- `creator-foundation` — content-creator track; the release milestones that drive audience interest cycles.
- `meta-style-guide` — the citation, build-tag and license conventions this document follows.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-07-30 | Orchestrator (KB Pipeline) | Approved and frozen — foundation cluster release kb-release-2026.07.30. | Standing mandate (2026-07-30) |
| 1.0.1 | 2026-07-30 | Orchestrator (KB Pipeline) | License-hygiene prose rewrites after arming the pzwiki n-gram gate (no factual changes). | Standing mandate (2026-07-30) |
