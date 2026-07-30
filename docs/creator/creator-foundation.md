---
id: creator-foundation
title: "The Project Zomboid Content Landscape: Formats, Channels and the B42-Stable Window"
version: 0.1.0
status: in-review
confidence: Medium
category: Creator
topic: "Creator foundations"
build: B42
document_type: overview
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [modders-foundation, players-foundation, admins-foundation, lore-foundation, meta-style-guide]
tags: [creator, youtube, twitch, content-strategy, b42-stable, launch-window, channel-landscape, formats, cross-promotion]
game_versions_verified: ["42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | creator-foundation |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Creator |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 42.20 |

# Executive Summary

This document maps the Project Zomboid content-creation landscape as it stands
one day after Build 42.20 reached the public stable branch (2026-07-29) [3].
It profiles the named channels that define the ecosystem's main formats —
ambiguousamphibian (themed challenge runs), Pr1vateLime (condensed
"I Survived X Days" narratives and multi-creator challenges), Retanaru
(mechanics deep-dives), Mattsi (beginner guides) and NurseVO (roleplay and
multiplayer streaming) — and records their audience sizes strictly as
third-party estimates, cited to the estimate pages actually consulted
[7][8][9][10][11][12].

The strategic core of the document is the launch window. Build 42 spent
roughly nineteen months in unstable beta between 2024-12-17 [1] and the
42.20 stable release [2][3], which means the largest wave of returning and
new players since Build 41 is arriving right now: Steam concurrency peaked at
74,959 players on release day per a SteamDB item syndicated on the official
news feed [5], and Twitch watch-hours for the game rose 46.6% month-on-month
into the release [6]. The best-positioned content in this window is
post-stable beginner material, B41-veteran transition explainers, tutorials
for the new animal husbandry and crafting systems, B42 multiplayer server
content, and visually led pieces built on the new basements and lighting
[2][3][5].

Document confidence is **Medium** and deliberately so: the game-side facts
rest on primary Steam announcements from The Indie Stone, but everything
audience-shaped — subscriber counts, view totals, watch-hours — comes from
third-party trackers with no access to creator analytics. Where a widely
repeated ecosystem belief could not be traced to a primary source, it is
quarantined below rather than asserted.

# Key Takeaways

- Build 42.20 went stable on 2026-07-29 after an unstable cycle that began
  2024-12-17, and stable B42 ships with multiplayer included *(cited)*
  *(B42)* [1][2][3].
- Release-day demand is real and measured: a 74,959 concurrent-player Steam
  peak [5] and a 46.6% month-on-month rise in Twitch hours watched [6]
  *(cited)*.
- The five channels profiled span the format spectrum — challenge runs,
  condensed narrative supercuts, mechanics analysis, beginner guides, and
  RP/MP streaming — and range from roughly 14 thousand to roughly 1.7 million
  subscribers, **all figures third-party estimates** *(cited as estimates)*
  [7][8][9][10][11][12].
- The highest-leverage launch-window formats are beginner guides verified
  against 42.20, B41-to-B42 transition content, husbandry/crafting tutorials,
  B42 MP server events, and basement/lighting showcase visuals, because each
  maps to a headline stable feature *(guidance built on cited features)*
  [2][3].
- B41 savegames do not carry into B42, and a `legacy41` branch exists — this
  single fact generates an entire transition-content category *(cited)*
  [2][3].
- The Indie Stone actively accommodates creators: broadcasters were cleared
  to publish 42.20 content hours before the official launch *(cited)* [2].
- Popular title formats get cloned by unrelated channels — at least two
  non-Pr1vateLime channels publish "I Survived N Days" Project Zomboid videos
  — so verify authorship before citing or collaborating *(cited)* [13][20].
- Mod-showcase creators carry a real supply-chain risk: fourteen malicious
  Workshop mods were removed in April 2026 after a zero-day disclosure
  *(cited)* [4].

# Purpose

This is the foundation document for the Creator track. It answers three
questions for someone producing Project Zomboid content (or planning to):
who currently occupies the landscape and with what formats; which formats
demonstrably attract audiences; and what the B42-stable launch window
uniquely rewards right now. Sibling track foundations cover the game itself
(players-foundation), the modding platform (modders-foundation), and server
operation (admins-foundation); this document deliberately covers the
*ecosystem around* the game rather than game mechanics.

# Scope

Covered: the named YouTube/Twitch channels listed above and their formats;
audience-scale estimates with explicit estimate labelling; the measured
launch-window audience data (Steam concurrency, Twitch watch-hours); the
B42.20 stable feature set *as content-opportunity raw material*; and the
cross-promotion funnel between platforms. Build tag is **B42** because every
opportunity assessed here keys off the 42.20 stable release; B41 appears only
as context (the build veterans are migrating from).

Not covered: game-mechanic depth (see players-foundation), monetisation and
platform policy, video production technique, and any claim about creators'
private analytics — none were available. Channels beyond the five named are
out of scope for profiling, though two others (Rimmy Downunder, Iceberg
Gaming) appear as format evidence [19][20].

# Definitions

- **Condensed playthrough / supercut** — a long survival run edited into a
  single narrative video, typically titled "I Survived N Days…" [13].
- **Challenge run** — a playthrough under self-imposed constraint rules
  (e.g. all negative traits, CDDA start), often themed per episode [15].
- **VOD channel** — a secondary channel where a creator archives full,
  lightly edited stream recordings, distinct from the edited main channel
  [15][16].
- **Launch window** — the weeks immediately after a major stable release,
  when search demand and returning-player traffic spike [5][6].
- **legacy41** — the Steam beta branch The Indie Stone provides for players
  staying on Build 41 after B42 went stable [2][3].
- **Unstable branch** — the opt-in Steam beta where Build 42 lived from
  December 2024 until the 42.20 stable promotion [1][2].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Context only | — | Appears solely as the build audiences are migrating from; savegames do not transfer to B42 [2][3] |
| B42 (stable) | Yes | 42.20 | All opportunity analysis keys off the 2026-07-29 stable release [3] |

The ecosystem facts (channel rosters, estimate figures, Twitch data) are
dated 2026-07-30 snapshots and decay faster than any game build; treat their
"verified against" as the access date on each reference.

# Reference

## The B42 release timeline

Build 42 first became publicly playable on the opt-in unstable beta on
2024-12-17, with The Indie Stone explicitly warning that unstable players
were "playing a work in progress" [1]. The unstable cycle ran through
version 42.19 before The Indie Stone announced that 42.20 would be promoted
to the public stable branch on Wednesday 2026-07-29 [2], and the stable
release shipped on that date alongside a security patch for Build 41 and
42.19 credited to a responsible disclosure [3]. Press syndicated on the
official Steam news feed characterised the update as introducing animals,
basements and deeper crafting [5], and the 42.20 stable patch notes
themselves reference the animal systems directly (for example, butchering
yields from large animals) [3].

## What stable 42.20 contains that creators can point a camera at

The pre-release announcement for 42.20, titled "The Big Glow Up," details a
visual overhaul: light overlays for every light source, snow overlays, new
burned-tile variations, new 30-degree roofs and additional window types,
plus substantial town-by-town map overhauls [2]. The same announcement
states that Build 42 contains 400 procedural basements and 75 unique
hand-made ones, and that the art team delivered 1,400 new unique buildings
and 20,000 new tiles while the map's surface area doubled [2]. The stable
patch notes confirm multiplayer is included, with an extensive MP fix
section covering re-worked and re-enabled anti-cheat and improved
server-join load times [3]. Localisation efforts span more than 29 languages
[3]. Both announcements state plainly that Build 41 savegames are not
compatible with Build 42 and that a legacy41 branch exists for players who
stay behind [2][3].

Two facts in the announcements speak directly to creators. First, The Indie
Stone lifted its broadcast embargo early: broadcasters were "allowed to post
and broadcast their content from 10AM BST" on release day, hours before the
official launch [2]. Second, in April 2026 the studio removed fourteen
malicious Workshop mods after patching a zero-day exploit in which mods
created files outside the game directory [4] — a documented precedent that
mod-showcase content carries supply-chain risk.

## Launch-window audience data

A SteamDB item syndicated on the official Steam news feed reported the game
peaking at 74,959 concurrent players on 2026-07-29, the stable release day
[5]. On the Twitch side, the third-party tracker SullyGnome recorded, for
the thirty days ending 2026-07-30: roughly 1.6 million hours watched (up
46.6% on the prior period), average viewership around 2.2 thousand, a peak
of 55.7 thousand viewers (up 171.1%), 64.4 thousand hours streamed, and on
the order of 7,700 active streamers with about 89 channels live on average
[6]. These are third-party measurements, not platform-official figures, but
they establish both the size of the wave and how few channels are competing
for it relative to demand [6].

## The channel landscape

All subscriber and view figures in this table are **third-party estimates**
from public tracker pages consulted on 2026-07-30; none come from creator
analytics, and different trackers disagree (see the ambiguousamphibian row).

| Channel | Signature format (evidence) | Scale — third-party estimate (source) |
|---------|-----------------------------|----------------------------------------|
| ambiguousamphibian | Themed challenge runs, e.g. a CDDA-start, all-negative-traits 100-day run archived on the companion VODs channel [15] | ~1.64M subs / ~356.9M views / 502 videos (us.youtubers.me, data through ~Apr 2026) [7]; ~1.67M subs / ~375.5M views / 514 videos (Influtrend, as of 2026-07-30) [8] |
| Pr1vateLime | Condensed "I Survived N Days" supercuts [13] and multi-creator MP challenge events such as the five-YouTuber TILEMAN challenge [14]; currently running an episodic Necroa-mod series whose recent episodes show ~38K–192K views each [9] | ~279K subs / ~78.2M views / ~1.2K videos (Influtrend, as of Jul 2026) [9] |
| NurseVO | Multiplayer and roleplay play, including ten-hour modded MP sessions archived on a "Nurse VODs" channel [16]; appeared in the TILEMAN multi-creator event [14] | ~323K subs / ~64.5M views / 301 videos + 132 shorts (Influtrend, as of Jul 2026) [10] |
| Retanaru | Mechanics deep-dives and testing-driven guides; channel self-description reads "Making mechanic analysis and guides for games. Mostly Project Zomboid for now." [11]; representative title: "Be The Cool Car Guy \| Mechanic Guide B41" [18] | ~52.3K subs / ~21.7M views (SocialCounts snapshot, 2026-07-30) [11] |
| Mattsi | Beginner guides, e.g. "Beginner Tips for Project Zomboid Build 42!" [17] | ~14.3K subs / ~3.8M views / 168 videos (SocialCounts snapshot, 2026-07-30) [12] |

Two structural notes the table implies. The ecosystem also produces
multi-creator RP server series run by channels outside this five — the
"NearlyDead: RP" Project Zomboid multiplayer roleplay playlist is published
by Rimmy Downunder [19] — and successful title formats propagate across
unrelated channels: "I Survived 1,000 Days in Project Zomboid The Complete
Series" is published by Iceberg Gaming, not Pr1vateLime [20]. Recent-upload
listings also show the two largest profiled channels currently spending most
of their slate on other simulation games, with Project Zomboid absent from
ambiguousamphibian's latest videos [8] and only intermittent on NurseVO's
[10] — the B42 window is arriving while several incumbents are pointed
elsewhere.

# B41 vs B42 Delta

Not applicable — single-build document. This overview is tagged B42 because
its subject is the content opportunity created by the 42.20 stable release;
it makes no mechanical claims that require a per-build comparison. The one
delta-shaped fact it relies on — that Build 41 saves do not transfer and a
legacy41 branch exists — is cited in the Reference section [2][3], and the
mechanical B41-to-B42 differences themselves belong to players-foundation
and its children.

# Practical Guidance

Candid producer's read of the evidence above. These are judgements built on
the cited facts; they introduce no new factual claims.

## Which formats are worth building

- **Condensed narrative supercuts** ("I Survived N Days") compress dozens of
  hours into one sitting and are the format so proven that other channels
  clone the title pattern [13][20]. Highest edit cost, best shelf life.
- **Themed challenge runs** give an infinitely repeatable premise machine —
  constraint rules make every run a new video without new game content
  [15][14].
- **Multi-creator MP events** (TILEMAN-style) bundle several audiences into
  one upload and cross-pollinate subscriber bases [14]; B42-stable MP [3]
  makes these newly filmable on current-build servers.
- **RP server recaps** sustain serialised, character-driven content that
  outlives any single patch [19][16].
- **Evergreen guides** are the search-traffic play: beginner guides [17] and
  mechanics deep-dives [11][18] serve query-driven viewers rather than
  subscription feeds, and every mechanic changed by B42 resets the clock on
  the incumbent B41-era guide catalogue.
- **Mod showcases** remain viable but now carry a vetting obligation — see
  Pitfalls and [4].

## The launch-window plays, ranked by urgency

1. **Post-stable beginner guides.** Release-day concurrency of ~75K [5] and
   a 46.6% Twitch surge [6] mean a cohort of brand-new and lapsed players is
   searching right now; guides verified against 42.20 rather than unstable
   builds win that search race [3].
2. **B41-veteran transition content.** Saves do not carry over and legacy41
   exists [2][3]; "what changed, what to relearn, whether to migrate" is a
   ready-made series for the largest single audience segment.
3. **Animal husbandry and crafting tutorials.** Animals and the crafting
   expansion are the update's headline systems in both the primary notes and
   syndicated press [3][5] — deep tutorial territory that mechanics channels
   have not yet saturated on the stable build.
4. **B42 MP server content.** Stable multiplayer with re-enabled anti-cheat
   [3] unlocks events, RP seasons and server launches on the current build;
   pair with admins-foundation for the operational side.
5. **Basement and lighting visuals.** 475 basements, light and snow
   overlays, and overhauled towns [2] are thumbnail-and-B-roll fuel;
   visually led map tours are the cheapest way to show "the game looks
   different now."

## The cross-promotion funnel

A workable single-creator funnel, stated as strategy rather than fact:
YouTube uploads (discovery) route viewers to a Discord (community capture);
the Discord feeds a public B42 server whose events become the next uploads
[3]; guide videos link out to reference material for retention; Twitch
carries the live layer — currently under-supplied relative to demand, at
roughly 89 average concurrent channels against a 55.7K viewer peak [6] —
and stream VODs feed a secondary channel as the established creators already
do [15][16]; curated Workshop collections of showcased mods close the loop
by making every mod video a durable landing page. The Indie Stone's
early-broadcast allowance on release day [2] shows the studio treats
streamers as a launch channel; expect that cooperation to continue and plan
launch-day coverage accordingly.

# Common Pitfalls & Troubleshooting

- **Shipping guides recorded on unstable footage.** Nineteen months of
  unstable iterations [1][2] mean most existing B42 guide footage predates
  42.20; values and visuals may differ from stable [2][3]. Re-verify on
  42.20 before publishing, and date-stamp builds on screen.
- **Treating tracker numbers as analytics.** The two trackers consulted for
  ambiguousamphibian differ by tens of thousands of subscribers and ~19M
  views for the same channel [7][8]. Use estimates for relative scale only.
- **Confusing format clones with the originator.** "I Survived"-pattern
  titles are published by multiple unrelated channels [13][20], and popular
  playlists are sometimes fan-compiled rather than creator-owned [19]. Check
  the uploading channel before crediting, citing or pitching a collab.
- **Showcasing unvetted mods.** The April 2026 incident — fourteen malicious
  mods removed after a zero-day patch [4] — means a mod showcase can direct
  an audience to a hostile download. Check mod provenance and update dates
  before featuring anything.
- **Building transition content that ignores legacy41.** Some of the B41
  audience will deliberately stay behind on the legacy branch [2][3];
  transition content that frames migration as mandatory will misread part of
  its own audience.

# Community Notes & Unverified Claims

## Claim 1 — ambiguousamphibian's channel growth was driven by Project Zomboid content

- **Claim:** Stat-site channel blurbs and community discussion attribute the
  channel's breakout to its Project Zomboid deep-dives, before it broadened
  into RimWorld, Kenshi and other simulation games (circulates on tracker
  pages such as Influtrend and in community threads).
- **Why unverified:** No primary source — the attribution appears in
  third-party editorial text, not in any creator statement or analytics I
  could open; the tracker pages consulted show the current slate is mostly
  other games [8].
- **Confidence:** Medium. Multiple independent trackers repeat it and the
  channel's PZ back-catalogue is consistent with it, but nothing primary
  confirms causation.

## Claim 2 — Condensed supercuts and challenge runs outperform raw VOD uploads per video

- **Claim:** Producer folk wisdom across the PZ creator community holds that
  edited narrative formats draw far more views per upload than full stream
  archives, which is why the big channels split VODs onto secondary channels
  [15][16].
- **Why unverified:** Only public view counts are observable; no creator
  analytics or controlled comparison exists, and channel-splitting itself
  confounds the comparison.
- **Confidence:** Medium. The observable pattern (dedicated VOD channels,
  clone-worthy supercut titles [13][20]) fits, but the causal performance
  claim rests on inference.

## Claim 3 — NurseVO is primarily a Twitch-first streamer whose YouTube output is VOD- and highlight-driven

- **Claim:** Community listings describe NurseVO as streaming Project
  Zomboid multiplayer on Twitch (a twitch.tv/nursevo channel surfaces in
  search) with YouTube serving archives via a "Nurse VODs" channel [16].
- **Why unverified:** I could not open the Twitch channel page or any
  primary statement of the creator's platform priorities; recent YouTube
  uploads on the main channel span several games [10].
- **Confidence:** Low. The supporting evidence is circumstantial (naming
  conventions and search listings), and "primarily" is a stronger claim than
  the evidence supports.

# Risks & Caveats

- **Estimate volatility.** Every audience figure here is a third-party
  snapshot dated 2026-07-30 [7][8][9][10][11][12]; subscriber counts drift
  daily and trackers disagree with each other, so any figure quoted onward
  should carry its date and source.
- **Launch-window decay.** The concurrency peak [5] and Twitch surge [6]
  describe release week; the opportunity analysis has a shelf life measured
  in weeks, and this document's review date should be treated as a hard
  re-verification deadline for the audience data.
- **Hotfix exposure.** 42.20 is day-one stable; hotfixes in the coming weeks
  could adjust the systems named as tutorial targets [3]. Feature
  descriptions cite the release announcements, not post-release patches.
- **Single-sourced Twitch data.** The Twitch figures rest on one tracker
  [6]; per the source rules they are rated no higher than Medium and should
  be corroborated before being quoted as fact.
- **Ecosystem sampling bias.** Five channels were profiled by assignment;
  the landscape includes significant creators not covered here, and the
  format taxonomy is only as complete as that sample plus the two
  incidentally verified channels [19][20].

# Verification Steps

1. Open the Steam announcements [1][2][3][4] directly (or via the news API
   feed [5]) and confirm the release dates, the basement/building/tile
   counts, the MP section, and the save-compatibility statements.
2. Re-query the Steam news feed [5] for items newer than 2026-07-30 to
   catch hotfixes that would stale-date the feature claims.
3. Re-load the tracker pages [7][8][9][10][11][12] and compare fresh
   subscriber/view figures against the table; deviations beyond a few
   percent mean the table needs a new snapshot date.
4. Confirm video and playlist authorship by fetching YouTube oEmbed metadata
   for the cited URLs [13]–[20] (the method used for this document), which
   returns canonical title and author without a logged-in session.
5. Re-check SullyGnome [6] for the current 30-day window to see whether the
   launch surge is holding, growing or decaying.

# Open Questions

- Does the B42-stable surge persist past the first month, and at what level
  does Twitch/YouTube demand settle? (Resolved by re-running steps 2 and 5
  after ~30 days.)
- Which of the incumbent large channels actually return to Project Zomboid
  for B42 stable, given their current non-PZ slates [8][10]? Their return or
  absence materially changes the competitive picture for new entrants.
- What does the official stance on monetised content and permissions look
  like in detail? No primary policy document was consulted for this draft;
  a child document should source The Indie Stone's media/content policy
  directly.
- Can any first-party analytics (e.g. a creator sharing dashboard data
  publicly) upgrade Claim 2 from inference to evidence?
- What share of the B41 population remains on legacy41 long-term [2][3]?
  That number, if it ever surfaces in a Thursdoid, sizes the transition-
  content audience precisely.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42 Unstable Out Now*. Steam announcement,
  2024-12-17. https://steamcommunity.com/games/108600/announcements/detail/1785774543698069
  Accessed via the Steam news API [5], 2026-07-30.
- [2] **The Indie Stone** — *42.20: The Big Glow Up*. Steam announcement,
  2026-07-27. https://steamcommunity.com/games/108600/announcements/detail/1839041357036410
  Accessed via the Steam news API [5], 2026-07-30.
- [3] **The Indie Stone** — *Build 42.20.0 Stable Released*. Steam
  announcement, 2026-07-29. https://steamcommunity.com/games/108600/announcements/detail/1839676055882259
  Accessed via the Steam news API [5], 2026-07-30.
- [4] **The Indie Stone** — *Patching a Zero Day Exploit*. Steam
  announcement, April 2026. https://steamcommunity.com/games/108600/announcements/detail/1829528821304702
  Accessed via the Steam news API [5], 2026-07-30.
- [5] **Valve** — *Steam news feed for app 108600 (ISteamNews
  GetNewsForApp)*, including syndicated SteamDB and PCGamesN items.
  https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=400
  Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)**

- None used in this document.

**Secondary & Corroborating**

- [6] **SullyGnome** — *Project Zomboid Twitch statistics*, 30-day window
  ending 2026-07-30. Third-party tracker. https://sullygnome.com/game/Project_Zomboid
  Accessed 2026-07-30.
- [7] **us.youtubers.me** — *ambiguousamphibian YouTuber stats*. Third-party
  estimate page. https://us.youtubers.me/ambiguousamphibian/youtuber-stats
  Accessed 2026-07-30.
- [8] **Influtrend** — *ambiguousamphibian YouTube overview*. Third-party
  estimate page. https://influtrend.com/youtube/ambiguousamphibian Accessed
  2026-07-30.
- [9] **Influtrend** — *Pr1vateLime YouTube overview*. Third-party estimate
  page. https://influtrend.com/youtube/pr1vatelime Accessed 2026-07-30.
- [10] **Influtrend** — *NurseVO YouTube overview*. Third-party estimate
  page. https://influtrend.com/youtube/nursevo Accessed 2026-07-30.
- [11] **SocialCounts** — *Retanaru live subscriber count*. Third-party
  estimate page. https://socialcounts.org/youtube-live-subscriber-count/UCRooOLENVeHLGMK8Z2adZlw
  Accessed 2026-07-30.
- [12] **SocialCounts** — *Mattsi live subscriber count*. Third-party
  estimate page. https://socialcounts.org/youtube-live-subscriber-count/UCy5itVtEtNufrD4Yd4UNXMg
  Accessed 2026-07-30.

**Community & Creator** (titles and uploading channels verified via the
YouTube oEmbed API on 2026-07-30)

- [13] **Pr1vateLime** — *I Survived 50 Days TRAPPED Inside A Trailer Park |
  Project Zomboid Supercut*. https://www.youtube.com/watch?v=HudePGY1lOI
- [14] **Pr1vateLime** — *Can 5 Youtubers Survive The TILEMAN Challenge In
  Project Zomboid*. https://www.youtube.com/watch?v=0X4EiZZJ03E
- [15] **ambiguousamphibian VODs** — *Surviving 100 Days in Project Zomboid:
  CDDA Challenge, All Negative Traits (Full Stream)*.
  https://www.youtube.com/watch?v=NHTfSA4BF3Y
- [16] **Nurse VODs** — *Project Zomboid, 10-Hour Modded Multiplayer B41 |
  NurseVO*. https://www.youtube.com/watch?v=xbvkbf2zWOQ
- [17] **Mattsi** — *Beginner Tips for Project Zomboid Build 42!*.
  https://www.youtube.com/watch?v=3poHGgZ3AnI
- [18] **Retanaru** — *Be The Cool Car Guy | Mechanic Guide B41*.
  https://www.youtube.com/watch?v=WL8wB1AlBMA
- [19] **Rimmy Downunder** — *NearlyDead: RP | Project Zomboid Multiplayer
  Roleplay* (playlist).
  https://www.youtube.com/playlist?list=PLXJD1gTLRfD4X3xhiEojc54I6ba4wEe2l
- [20] **Iceberg Gaming** — *I Survived 1,000 Days in Project Zomboid The
  Complete Series*. https://www.youtube.com/watch?v=avhgIsmeZDA

**Further Reading**

- See the Further Reading section below.

# Further Reading

- The Indie Stone's blog at projectzomboid.com/blog mirrors the Steam
  announcements cited above and carries the long-form Thursdoid history of
  the B42 cycle (bot-blocked for automated checkers; the Steam news API [5]
  is the reliable mirror).
- players-foundation in this knowledge base, for the mechanical substance
  behind every tutorial opportunity named here.
- admins-foundation, for the server-side reality of the MP event and public
  server plays.

# Related Documents

- modders-foundation — the Workshop/modding platform that mod-showcase
  content depends on.
- players-foundation — the game systems that guide content teaches.
- admins-foundation — server operation for MP events and community servers.
- lore-foundation — the Knox Event fiction that RP content builds on.
- meta-style-guide — the editorial rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
