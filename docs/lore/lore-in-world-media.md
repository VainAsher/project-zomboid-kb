---
id: lore-in-world-media
title: "In-World Media: Radio, Television, Print and Found Documents in Knox Country"
version: 1.0.0
status: approved
confidence: Medium
category: Lore
topic: "In-world media"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [lore-foundation, lore-knox-event-timeline, players-map-locations, players-b41-to-b42-transition, modders-item-scripts-distributions, modders-modinfo-modid-conventions]
tags: [lore, radio, television, newspaper, brochure, flier, skill-book, emergency-broadcast, environmental-storytelling]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | lore-in-world-media |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Lore |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16 (Umbrella stub index), 42.20 (Umbrella 42.20.0 stub index, release notes), 42.21 (Umbrella 42.21.0 stub index, stable announcement and forum change list); B42 stable is 42.21 as of 2026-09-28 [2] |

# Executive Summary

Project Zomboid tells its Knox Event story almost entirely through in-world
media: radio and television channels that the player tunes in, print items
such as newspapers, brochures and fliers that the player reads, and found
documents and books lying around the map. This document indexes that
apparatus. It records which media families exist, what the code-level
vocabulary for them looks like in the pinned Umbrella stub indexes for each
build, and what the Build 42 line changed. It does not reproduce any
broadcast, article or note: all of that text is The Indie Stone's copyright,
and the document only describes and points to it.

The headline Build 41 to Build 42 change is on the print side. The 42.21.0
stub index carries a set of print-media classes (a newspaper registry,
brochure and flier registries, print-media definitions and map classes, and
two reader UI classes) that the 41.78.16 index does not [5][6]. The earlier
42.20.0 index listed a larger reader-UI family and a print-media manager that
the 42.21.0 index no longer lists [5][13]. From 42.13 onward,
newspaper, brochure and flier identifiers are declared through a mod-facing
registry system [4]. Radio and TV share one code lineage across both builds,
with a handful of renamed or relocated members [5][6].

Confidence is **Medium**. The code-level facts rest on pinned Umbrella
indexes (primary, code truth), but no pzwiki page for radio, TV or print
media was ingested into this repository, so channel-level facts come from
navigation data on the Skill book page and the Knox Event timeline, and
broadcast scheduling behaviour is not documented by any primary source we
could open (see the quarantined claims).

# Key Takeaways

- Media reaches the player in three families: broadcast (radio and TV
  channels), print (newspapers, brochures, fliers, magazines, books) and found
  documents; Build 42 deliberately expanded the print and broadcast layers
  *(cited)* [9].
- The game's radio and TV code is organised around channels, scripts and
  broadcasts in both builds (`RadioChannel`, `RadioScript`,
  `RadioBroadCast`, `ZomboidRadio`) *(both, cited)* [5][6].
- Channels include an automated emergency broadcast service and several named
  civilian stations; the fiction has most American radio and TV programming
  cease or give way to an Emergency Broadcast on 18 July 1993 *(cited)*
  [7][8].
- Print media gained its own class family in B42: `Newspaper`, `Brochure`,
  `Flier` and reader UI classes; none appear in the B41 index. The 42.20.0
  index also listed `PrintMediaManager` and six more `ISPrintMedia*` UI
  classes that the 42.21.0 index does not *(B42, cited)* [5][6][13].
- The 42.21 change list updates the localization system, fixes crossword
  magazine and skill-book page reading, and fixes notes made in the backpack
  not saving *(B42, cited)* [14].
- From 42.13, mods declare newspapers, brochures and fliers in
  `registries.lua`; the mechanics are documented elsewhere in this KB, not
  here *(B42, cited)* [4].
- Skill books and recipe magazines are media items, but they are mechanics
  items first; the one wiki source is older than B42 stable and must be
  re-verified *(cited, with caveat)* [8].
- How a broadcast schedule is paced across in-game days is not documented in
  any primary source we could open; it is quarantined, not asserted
  *(community, unverified)*.

# Purpose

Lore readers, players and mod authors keep asking where the story actually
comes from in the game and how to find it. This document answers that at
index level: what kinds of in-world media exist, where their definitions live
in the code vocabulary, and what moved between Build 41 and Build 42. It
deliberately goes one level below `lore-foundation`, which names the
narrative-delivery devices, and stops short of retelling any of the fiction.

# Scope

Covered: radio and television as game systems and as a story channel;
print media (newspapers, brochures, fliers, magazines, skill books) at the
level of existence, taxonomy and code names; found documents as a category;
and the B41 to B42 delta for all of those. Both builds, with B41 tagged
41.78.16 (the pinned Umbrella tag) and B42 tagged 42.21 (Umbrella 42.21.0, with 42.20.0 used for comparison).

Not covered: transcripts, article text or note text of any kind (TIS
copyright); the day-by-day Knox Event timeline (see `lore-knox-event-timeline`);
where specific media can be found on the map (see `players-map-locations`);
the loot-table and registry mechanics for adding media (see
`modders-item-scripts-distributions`); mod identifier hygiene (see
`modders-modinfo-modid-conventions`); skill-book XP mechanics beyond a
pointer; and the @TheKnoxEvent social-media retelling, already summarised in
`lore-foundation`.

# Definitions

- **Channel** — a radio or TV station as the code models it, with a name, a
  frequency, a category and a TV flag [5][6].
- **Broadcast** — one airing, modelled as an object holding lines plus start
  and end stamps [5][6].
- **Print media** — in this document, the B42 family of readable newspapers,
  brochures and fliers with their own registry and reader UI classes [5].
- **Recorded media** — the code system for CDs, tapes and similar playable
  media, including a record of which lines the player has heard [5][6].
- **Found document** — any readable item placed in the world that is neither
  a broadcast nor one of the registry-based print items; this KB uses the
  term as a category label, not as a code term.
- **Registry (B42)** — a Lua-declared identifier list introduced as a
  requirement in 42.13, released 2025-12-11 [3][4].

# Build Applicability

Facts about code vocabulary were taken from the Umbrella stub indexes pinned
for this repository: tag 41.78.16 for B41 and tag 42.21.0 for B42, extracted
into the repository's `sources/schemas/` indexes [5][6]; the previous B42 pin,
tag 42.20.0, is archived at `sources/schemas/archive/api-index-B42-42.20.0.json`
and was used for comparison [13]. Release notes for 42.13.0 and 42.20.0 were
read from the ingested pzwiki snapshots at the revisions cited below. B42 went
stable at 42.20 on 2026-07-29 [1] and moved on to 42.21 on 2026-09-28 [2].
The 2026-10-07 re-baseline re-checked every class, event and global name used
in this document against the 42.21.0 index, and read the 42.21 stable
announcement [2] and the 42.21 forum change list [14] for media-related
entries. Not re-checked: the pzwiki-derived channel and skill-book facts [7][8],
which have no 42.21 equivalent in the sources opened.

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | Umbrella 41.78.16 stub index [6] | No print-media class family in the index; radio/TV classes present |
| B42 (stable) | Yes | Umbrella 42.21.0 stub index [5], compared with 42.20.0 [13]; 42.13.0 and 42.20.0 notes [10][11]; 42.21 notes [2][14] | Current stable is 42.21 [2]; wiki-derived channel facts not re-checked |

# Reference

**Evidence layer.** Names below are code symbols exactly as they appear in the
pinned stub indexes; what a symbol does is stated only when the index or a
cited note says so.

## Media families at a glance

| Family | What the player meets | Code vocabulary (index names) | Builds |
|--------|----------------------|-------------------------------|--------|
| Radio | Receivers, HAM radios, walkie-talkies, vehicle radios | `IsoRadio`, `Radio`, `ZomboidRadio`, `RadioChannel` | both [5][6] |
| Television | TV sets tuned to TV-flagged channels | `RadioChannel` carries an `IsTv` member | both [5][6] |
| Recorded media | CDs, tapes and similar | `RecordedMedia`, `MediaData` | both [5][6] |
| Newspapers | Readable newspaper items | `Newspaper` registry, `OldNewspaper` | B42 [5] |
| Brochures and fliers | Readable paper items tied to places | `Brochure`, `Flier` registries | B42 [5] |
| Reader UI | The windows that display print items | `ISPrintMediaMap`, `ISPrintMediaTextPanel` (42.21.0); more `ISPrintMedia*` classes and `PrintMediaManager` in 42.20.0 only | B42 [5][13] |
| Literature items | Books, magazines | `Literature`, `ISLiteratureUI`, `ISLiteratureList` | both [5][6] |

## Radio and television

Both builds expose a radio core built from the same set of class names:
`ZomboidRadio`, `RadioScriptManager`, `RadioChannel`, `RadioScript`,
`RadioBroadCast`, `RadioLine`, `RadioData`, plus `DynamicRadio` and
`DynamicRadioChannel` [5][6]. A `RadioChannel` exposes members for its name,
frequency, category and a TV test (`IsTv`), together with members that read
the current script, the current script loop and the airing broadcast [5][6].
A `RadioBroadCast` exposes members for its lines and for its start and end
stamps, with setters for pre- and post-segments [5][6]. `RadioScriptManager`
exposes channel add and remove members and a `simulateScriptsUntil` member
alongside `getCurrentTimeStamp` [5][6].

Every radio and TV class named above has the same member list in the 42.20.0
and 42.21.0 indices [5][13]. Two radio-related Lua classes listed in 42.20.0,
`ISContextTelevision` and `InvContextRadio`, are not listed in 42.21.0 *(B42)*
[5][13]. Two Lua events concerning broadcast loading exist in both indexes:
`OnLoadRadioScripts` and `OnInitRecordedMedia` [5][6].

On the content side, the Skill book page's navigation block lists the media
categories the wiki recognises: devices (including Ham Radio, Radio,
Television, Walkie Talkie), TV channels, radio channels, and a long list of
recordings [8]. Radio channel names in that block include an "Automated
Emergency Broadcast System", a "Civilian Radio" channel, "KnoxTalk Radio" and
"LBMW - Kentucky Radio"; TV channel names include "WBLN News" and "KPATV"
[8]. The Knox Country page lists LBMW - Kentucky Radio as a point of interest
within Louisville [12].

## The Emergency Broadcast in the fiction

The Knox Event timeline compiled from TIS's archived real-time posts records
that on 18 July 1993 at 14:00 EDT most American radio and television
programming ceased or was replaced by an Emergency Broadcast [7]. The same
timeline records a nationally broadcast recording from a general on a
preceding day that repeats on later days, and an on-air caller to KnoxTalk
Radio claiming a military-lab origin for the outbreak [7]. These are cited here
only as index entries: the fact that such broadcasts exist and roughly when
the fiction places them. The text of the broadcasts is not reproduced.

## Scheduling and pacing: what the code names show

The indexes expose members that bear on scheduling, listed without
interpretation beyond the names: on `RadioScriptManager`, `update`, `simulateChannelUntil`, `simulateScriptsUntil` and
`getCurrentTimeStamp`; on `RadioChannel`, `getAirCounterMultiplier`,
`getCurrentScriptLoop` and `getCurrentScriptMaxLoops` [5][6]. On `ZomboidRadio`
the B41 index lists the constants `DISABLE_BROADCASTING`,
`LOUISVILLE_OBFUSCATION` and `POST_RADIO_SILENCE` (B41), and the B42 index
lists members `disableBroadcasting`, `louisvilleObfuscation` and
`postRadioSilence` instead (B42) [6][5]. No primary document we opened
states how channel scripts are paced across in-game days; that question is
quarantined below.

## Recorded media and line learning

`RecordedMedia` is present in both indexes with members for categories,
random pick from a category, and `hasListenedToLine` and
`hasListenedToAll` [5][6]. The B42 index additionally lists
`disableLineLearning`, `SAVE_FILE` and version constants *(B42)* [5].

## Print media (B42)

The 42.21.0 index lists a `Newspaper` registry class (unchanged from 42.20.0) whose constants name four
in-fiction papers (Kentucky Herald, Knox Knews, Louisville Sun Times and
National Dispatch) and which has `register`, `get` and `getIssues` members
*(B42)* [5]. A `Brochure` registry class lists constants named after
in-world places such as an airport, an art gallery in Louisville, two malls
and a sanatorium, and also has `register` *(B42)* [5]. A `Flier` class is
present as well *(B42)* [5]. Around them the 42.21.0 index lists
`PrintMediaDefinitions`, `PrintMediaMaps` and two reader UI classes,
`ISPrintMediaMap` and `ISPrintMediaTextPanel` *(B42)* [5]. The 42.20.0 index
additionally listed `PrintMediaManager`, `PrintMediaEntries`, a
`PrintMediaEntry` type and six more UI classes (`ISPrintMediaInfo`,
`ISPrintMediaListBox`, `ISPrintMediaPage`, `ISPrintMediaPanel`,
`ISPrintMediaRichText`, `ISPrintMediaSetInfo`); none of those nine names is in
the 42.21.0 index *(B42)* [5][13]. The 42.21 change list says nothing about
why; it records an updated localization system [14], and this document does
not link the two. An `OldNewspaper` class is present in both *(B42)* [5][13].

The official 42.13 modding migration guide lists Brochure, Flier and
Newspaper among eleven registries that must be declared in `registries.lua`;
the Newspaper registry takes a list of entry names *(B42)* [4]. This KB's
registry mechanics are in `modders-item-scripts-distributions`.

## Literature, skill books and recipe magazines

The Umbrella indexes list `Literature` and reader UI classes (`ISLiteratureUI`,
`ISLiteratureList`) in both builds [5][6]. The 42.21 change list includes
fixes for crossword magazine, book-reading progress bar and skill-book page
reading *(B42)* [14]. The Skill book wiki page records
that skill books are readable items that boost XP gain for one skill via a
multiplier, that each volume covers a pair of skill levels, and that a fully
read book cannot be read again [8]. The same page's navigation lists recipe
magazines and a general Literature group including Magazine, Newspaper,
Comic Book and Crossword Magazine [8]. That page's revision (1317189)
predates B42 stable, so those statements carry a B41-era caveat [8].

## Notes and found documents

No ingested source documents a distinct "note" item class in either index. The
42.21 change list records a fix for "notes made in the backpack" not saving,
without saying which in-game feature that names *(B42)* [14].
The nearest documented mechanisms are the print-media reader classes (B42)
[5] and the Literature classes (both) [5][6]. Environmental storytelling in
B42 is also described as including decorative items alongside fliers and
newspapers [9].

# B41 vs B42 Delta

**Evidence layer.**

| Area | B41 (41.78.16) | B42 (42.20 / 42.21) | Source |
|------|----------------|-------------|--------|
| Print-media classes | No `Newspaper`, `Brochure`, `Flier`, `PrintMediaManager` or `ISPrintMedia*` in the stub index | 42.21.0: `Newspaper`, `Brochure`, `Flier`, `ISPrintMediaMap`, `ISPrintMediaTextPanel` present; `PrintMediaManager` and six other `ISPrintMedia*` classes were in 42.20.0 only | [6] vs [5][13] |
| Registry declaration | Registry classes absent from the index | Newspaper, Brochure and Flier among eleven registries required from 42.13 | [6] vs [4] |
| Broadcast flags on `ZomboidRadio` | `DISABLE_BROADCASTING`, `LOUISVILLE_OBFUSCATION`, `POST_RADIO_SILENCE` listed as constants | `disableBroadcasting`, `louisvilleObfuscation`, `postRadioSilence` listed instead | [6] vs [5] |
| Transmission members | `ReceiveTransmission` listed | `DistributeTransmission` listed instead | [6] vs [5] |
| Radio interaction event | `OnRadioInteraction` listed among events | Not listed among events | [6] vs [5] |
| Recorded media | Base members only | Adds `disableLineLearning`, save-file and version constants | [6] vs [5] |
| Narrative intent | n/a | B42's feature list includes more fliers and newspapers, extra radio and TV broadcasts and channels, and findable characters from broadcasts at their workplaces and places of death | [9] |
| Emergency vehicles | n/a | Emergency vehicles with a radio get the Automated Broadcast channel in presets (42.13.0); all police vehicles get a HAM radio (42.13.0) | [10] |
| Removed Lua globals (42.21.0) | n/a | `getRadioText`, `doSurvivalGuide` and `doPrintMediaDebug` are in the 42.20.0 globals list and not in the 42.21.0 list; the survival-guide classes (`SurvivalGuideManager`, `ISSurvivalGuide*`) are likewise absent from 42.21.0 | [5][13] |
| 42.21 change list | n/a | Updated localization system, crossword magazine and skill-book page reading fixes, backpack notes saving fix, updated in-game credits | [14] |
| Map labels | n/a | Hovering brochure and flier icons on the in-game map shows labels (42.13.0) | [10] |
| Fixes | n/a | Empty brochure, flier and newspaper text under Russian localization fixed (42.13.0); a Lua crash on rereading a brochure and the map button failing to close brochures fixed (42.20.0) | [10][11] |

Absence from a stub index shows only that the symbol is not in that index,
not that the feature never existed in game code; the table records what the
pinned indexes show [5][6][13]. How B41 delivered newspaper text is left as an
open question.

# Practical Guidance

- **For lore writers and video makers:** describe and index media, then
  link out; do not transcribe broadcasts or articles. Quote at most a few
  words and credit The Indie Stone [7].
- **For players hunting story:** the print layer in B42 is tied to places
  (brochure names map to in-world locations) and the map shows labels for
  brochure and flier icons, so the in-game map is the first thing to open
  [5][10]. See `players-map-locations`.
- **For radio listeners:** tune devices that can pick up different channels;
  vehicle and emergency radios in B42 carry the automated channel in their
  presets [10]. Treat any pacing advice as unverified until the open
  questions are closed.
- **For modders:** B42 print media is registry-declared; use the registry
  pages instead of this document, and follow the identifier conventions in
  `modders-modinfo-modid-conventions` [4].
- **For anyone citing "the wiki says":** the Skill book page is older than
  B42 stable, so re-check skill-book facts in game [8].
- **For timelines:** use `lore-knox-event-timeline` for dates, and prefer
  TIS's date over a wiki convention when they disagree, as `lore-foundation`
  explains.

# Common Pitfalls & Troubleshooting

- **Treating a stub-index absence as a removal.** The B41 index lacks print
  classes, but that does not prove B41 had no newspapers; the evidence layer
  says only what the indexes list [5][6].
- **Reading B42 print facts onto legacy41.** Everything tagged *(B42)* above
  is absent from the 41.78.16 index [6].
- **Quoting broadcast text.** The text is TIS's; a transcript, even an
  attributed one, exceeds this KB's few-word quoting limit [7].
- **Assuming the wiki's media navigation is build-scoped.** The navigation
  block lists channels and items from one wiki revision with no build marker
  [8].
- **Assuming the 42.20.0 index still describes stable.** Stable is 42.21 [2],
  and its stub index drops several print-media UI classes and three Lua globals
  that the 42.20.0 index listed [5][13]. Check the current stubs before calling
  any of the removed names.

# Community Notes & Unverified Claims

## Claim 1 — Channel scripts advance on a day-by-day schedule, with the Emergency Broadcast taking over after a set in-game day

- **Claim:** Players and modders say that radio and TV scripts are keyed to in-game days, that normal programming gives way to the automated emergency channel after the first in-game weeks, and that sandbox options influence this.
- **Why unverified:** No primary document opened for this work (Umbrella stubs, release notes, ingested pzwiki pages) states the schedule or its trigger; the stub indexes show only member names such as `simulateScriptsUntil` [5][6].
- **Confidence:** Low. The claim is plausible from the member names and the fiction timeline [7], but the mechanism and any day numbers are unsourced.

## Claim 2 — The Louisville flag degrades radio reception for the Louisville area

- **Claim:** Community explanations say the `louisvilleObfuscation` setting garbles broadcasts received near or about Louisville.
- **Why unverified:** The index lists the constant or member name only [5][6]; no source describes its effect.
- **Confidence:** Low. A name is not documentation.

## Claim 3 — Brochure and flier subjects map one-to-one to buildings that exist on the map

- **Claim:** Players report that each brochure or flier location points to a findable in-world building.
- **Why unverified:** The registry constants name places [5] and the map labels icons [10], but no source states that every entry has a placed building or item.
- **Confidence:** Medium. Partly supported by the location-style constant names, but completeness is unchecked.

# Risks & Caveats

- No pzwiki pages on radio, TV, newspapers, brochures, fliers or notes were
  ingested into `sources/pzwiki/`; channel names come from a navigation block
  and the Knox Event timeline only. Ingesting the relevant pages would
  strengthen this document.
- The Skill book page (revision 1317189) is older than any 42.x release
  notes in this document [8].
- B41 evidence is the 41.78.16 Umbrella pin, while the legacy41 line has
  since reached later maintenance releases that have no stub tag.
- Stable is 42.21 as of 2026-09-28 [2]. Code-vocabulary facts were re-checked
  on the 42.21.0 index; wiki-derived facts were last read on 42.20-era
  snapshots.
- The 42.21 forum change list was read through a browser page-text
  extraction and marks several sections as selected lists [14]; media-related
  entries it does not mention may exist.
- A headphones or radio fix was expected in the 42.21 material for this
  re-baseline but none of the 42.21 sources opened here mentions one, so none
  is stated.
- Absence from a stub index is a weak signal [5][6].
- All fiction content is TIS copyright; this document indexes it only.

# Verification Steps

1. Open the pinned Umbrella trees [5][6][13] and search for `RadioChannel`,
   `PrintMediaManager` (42.20.0 only), `Newspaper`, `Brochure` and `Flier`.
2. In the repository, inspect `sources/schemas/api-index-B42.json` (42.21.0),
   `sources/schemas/archive/api-index-B42-42.20.0.json` and `api-index-B41.json`
   for the same names and for the `ZomboidRadio` member lists.
3. Read the 42.13.0 and 42.20.0 release notes [10][11] and the migration
   guide [4] for the print-media items cited.
4. In game on each build, tune a radio and a television across several
   in-game days and record which channels air; this closes Claim 1.
5. Open the in-game map on B42 and hover brochure icons to confirm labels
   [10].

# Open Questions

- How is channel scripting paced across in-game days, and what triggers the
  emergency channel? Resolving this needs the ScriptsDocs or game script
  files for radio data, which this document did not open.
- How did B41 present newspaper content, given that the print classes are
  absent from its stub index?
- What is the effect of the `louisvilleObfuscation` setting?
- Is there a distinct note item type in B42, or are notes covered by
  Literature and print-media readers?
- Why do the 42.21.0 stubs drop `PrintMediaManager` and six `ISPrintMedia*`
  UI classes, and what replaced them in game? The 42.21 change list does not
  say [14].
- Which feature does "notes made in the backpack" name in the 42.21 change
  list [14]?
- Do hotfixes after 42.21 change any of the print-media or radio items?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259 Accessed 2026-10-07; mirrored by the Steam news API; host is bot-block allowlisted.
- [2] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07; host is bot-block allowlisted.
- [3] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972 Accessed 2026-10-07; host is bot-block allowlisted.
- [4] **The Indie Stone Forums** — *Modding Migration Guide (42.13)*, first post by moderator nasKo, 2025-12-11. https://theindiestone.com/forums/topic/88499-modding-migration-guide-4213/ Accessed 2026-10-07; host bot-blocks checkers; read from a user-downloaded copy as noted in `modders-item-scripts-distributions`.
- [5] **PZ-Umbrella** — *Umbrella 42.21.0 (commit 13d01f9e)*, library tree. https://github.com/PZ-Umbrella/Umbrella/tree/13d01f9ee58fa48773553920db56d06f0005e7f8 Accessed 2026-10-07 via the repository's extracted `sources/schemas/api-index-B42.json`.
- [6] **PZ-Umbrella** — *Umbrella 41.78.16 (commit fa2e7e19)*, library tree. https://github.com/PZ-Umbrella/Umbrella/tree/fa2e7e19799740b57902f1cb4e989225c295c05e Accessed 2026-10-07 via the repository's extracted `sources/schemas/api-index-B41.json`.
- [13] **PZ-Umbrella** — *Umbrella 42.20.0 (commit 58204fc4)*, library tree, the previous B42 pin. https://github.com/PZ-Umbrella/Umbrella/tree/58204fc47895ba249592519cedecc7cfbaaebd60 Accessed 2026-10-07 via the repository's archived `sources/schemas/archive/api-index-B42-42.20.0.json`.
- [14] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first post by Rockjaw, 2026-09-23). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 via browser page-text extraction; host bot-blocks checkers.

**Fact-Only Sources (no prose reuse)**

- [7] **PZwiki** — *Knox Event* (revision 1441597). https://pzwiki.net/wiki/Knox_Event Ingested snapshot fetched 2026-07-30. Fact-only source.
- [8] **PZwiki** — *Skill book* (revision 1317189). https://pzwiki.net/wiki/Skill_book Ingested snapshot fetched 2026-07-31. Fact-only source.
- [9] **PZwiki** — *Build 42* (revision 1443663). https://pzwiki.net/wiki/Build_42 Ingested snapshot fetched 2026-07-30. Fact-only source.
- [10] **PZwiki** — *Build 42.13.0* (revision 1435679). https://pzwiki.net/wiki/Build_42.13.0 Ingested snapshot fetched 2026-07-30. Fact-only source.
- [11] **PZwiki** — *Build 42.20.0* (revision 1443641). https://pzwiki.net/wiki/Build_42.20.0 Ingested snapshot fetched 2026-07-30. Fact-only source.
- [12] **PZwiki** — *Knox Country* (revision 1439185). https://pzwiki.net/wiki/Knox_Country Ingested snapshot fetched 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none used.

**Community & Creator** — none used.

**Further Reading**

# Further Reading

- `lore-foundation` for the overview of the Knox Event and its delivery
  devices.
- `lore-knox-event-timeline` for dates.
- The pzwiki radio, television and newspaper pages, at fact-only status, once
  ingested.

# Related Documents

- `lore-foundation` — parent overview of the setting and story devices.
- `lore-knox-event-timeline` — the dated timeline these media report on.
- `players-map-locations` — where location-tied media can be found.
- `players-b41-to-b42-transition` — wider build delta for players.
- `modders-item-scripts-distributions` — registries and loot for adding media.
- `modders-modinfo-modid-conventions` — identifier conventions for namespaced IDs.
- `meta-style-guide` — the genre, build-tag and license rules followed here.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: B42 pin moved to Umbrella 42.21.0 (42.20.0 archived index kept for comparison); recorded removal of PrintMediaManager, six ISPrintMedia* classes and three Lua globals from the stubs; added 42.21 media-related change-list entries; sources [13][14]. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
