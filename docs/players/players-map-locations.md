---
id: players-map-locations
title: "Knox Country Locations: The B41 Towns and the B42 Expansion"
version: 1.0.0
status: approved
confidence: Medium
category: Players
topic: "Map & locations"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, lore-foundation, players-vehicles, meta-style-guide]
tags: [players, map, locations, towns, muldraugh, west-point, riverside, rosewood, louisville, brandenburg, ekron, irvington, echo-creek, basements, high-rises, build-42]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-map-locations |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 |

# Executive Summary

This document is the Players-track location reference for Knox Country, the Kentucky game world of Project Zomboid. It profiles the settlements Build 41 players know — Muldraugh, West Point, Riverside, Rosewood, March Ridge, Valley Station and the city of Louisville — and the areas Build 42 added in the westward map expansion: Brandenburg, Ekron, Irvington and Echo Creek, plus the smaller named regions around them [2] [5]. For each town it gives the character, the relative danger level as assessed by the community wiki, and the notable features a player can expect, deliberately staying at town level: no loot-room walkthroughs, no coordinates, no story discoveries.

Build 42 changed the map more than any update before it: the surface area was doubled, three full towns plus a new rural spawn area were added in the west, the engine's height ceiling was raised to allow basements and 32-level high-rises, and at the 42.20 stable release seven existing areas were entirely reworked by an enlarged map team [1] [2] [3]. Where a fact holds on only one build it is tagged *(B41)* or *(B42)*.

Document-level confidence is **Medium**: the map-expansion spine (which towns exist, what was reworked, the basement and high-rise numbers) rests on official Indie Stone announcements verified via the Steam news API, but the per-town character and difficulty profiles are cited from pzwiki page revisions versioned between 42.0.2 and 42.19.0 — none individually re-verified against the 42.20 rework, which explicitly touched several of these same towns.

# Key Takeaways

- Knox Country blends real northern-Kentucky places (Muldraugh, West Point, Louisville, Brandenburg, Irvington) with invented towns (Rosewood, Riverside) around the Fort Knox / Louisville area *(cited)* *(both)*
- The four "canon" starting towns with occupation-specific spawn points are Muldraugh, West Point, Riverside and Rosewood — on both builds *(cited)*
- Build 42 pushed the map west with Brandenburg, Ekron and Irvington, doubled the map's surface area, and added roughly 1,400 new unique buildings *(cited)* *(B42)*
- Echo Creek shipped as a fifth default spawn town at B42's launch and was removed from the default spawn list in 42.16.0; since 42.17, Sandbox games can start in any Exclusion Zone town *(cited)* *(B42)*
- B42 raised the old engine height limits: the build contains 400 procedural and 75 unique basements, and 32-level skyscrapers were built for Louisville *(cited)* *(B42)*
- The 42.20 stable release entirely reworked seven areas — Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron and Dixie — so pre-42.20 town guides may be stale *(cited)* *(B42)*
- The community wiki's difficulty ladder puts Riverside and Echo Creek at the gentle end, West Point at the hard end of the spawn towns, and Louisville — tens of thousands of zombies, no unmodded spawn — as the endgame destination *(community, cited to wiki; unverified on 42.20)*
- Louisville sits behind the Exclusion Zone fence with only a handful of guarded ways in, which makes reaching it a mid-game expedition rather than a starting choice *(cited)*

# Purpose

This document answers the questions a player asks before picking a spawn or planning a road trip: what are the towns of Knox Country actually like, which ones can I start in on my build, how dangerous is each one relative to the others, what did Build 42 add to the map, and what are basements and high-rises going to mean for how I play? It deepens the world-overview section of `players-foundation`, which names the towns but profiles none of them.

# Scope

Covered: town-level profiles of the seven B41-era settlements (Muldraugh, West Point, Riverside, Rosewood, March Ridge, Valley Station, Louisville); the B42 additions (Brandenburg, Ekron, Irvington, Echo Creek) and the smaller primary-sourced new areas around them; spawn availability per build; basements and high-rises as map features; and overview-level geography — rivers, highways and which towns neighbour which.

Not covered: loot tables, per-building walkthroughs, coordinates, base-spot rankings, and the story content of specific interiors — this document is written spoiler-aware and stops at town character and named landmarks. The Knox Event backstory is the Lore track's job (`lore-foundation`). Modded map additions are out of scope entirely.

# Definitions

- **Knox Country** — the partly real, partly fictional game world modelled on northern Kentucky around Fort Knox and Louisville; called Knox County before the 2013 map remake [5].
- **Exclusion Zone** — the quarantined region established around the outbreak in the game's fiction; its fortified border separates Louisville from the rest of the map [5] [10].
- **Spawn town** — a settlement the game offers as a starting location on the new-character spawn map [4] [14].
- **Canon starting towns** — The Indie Stone's term for the four towns that support occupation-specific spawn points: Muldraugh, West Point, Riverside and Rosewood [4].
- **Map glow-up** — the developers' name for the 42.20 map overhaul that entirely reworked seven existing areas [1] [2].
- **Procedural basement** — one of the B42 basements placed by generation rather than hand-building; B42 ships 400 procedural and 75 unique basements [2].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | The B41 map lacks the western towns, basements and high-rises; B41-only statements tagged *(B41)* [2] [15] |
| B42 (stable) | Yes | 42.20, re-checked against 42.21 patch notes | Expansion and rework facts current to the 2026-07-29 stable release [1] [2]; B42-only statements tagged *(B42)* |

The 42.21 stable release (2026-09-28) was reviewed for this document by reading the official Steam announcements for 42.20.1 through 42.21 and the 42.21 forum changelist [16] [17] [18]. The map-related items are recorded in the glow-up section below; every other statement is carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found in those notes. That was a patch-note review, not an in-game re-test, and none of the town profiles was re-checked against the post-rework map.

The town-profile facts are cited from pzwiki revisions versioned between 42.0.2 (Muldraugh) and 42.19.0 (Riverside, Rosewood); the 42.20 glow-up reworked several of these towns after those revisions were written, so per-town detail should be treated as pre-rework until re-verified [1] [6] [8] [9].

# Reference

## The shape of Knox Country

Knox Country recreates a slice of northern Kentucky around Fort Knox and Louisville, mixing faithful versions of real places — Louisville, Valley Station, Muldraugh, West Point — with wholly invented towns such as Rosewood and Riverside [5]. The region was renamed from "Knox County" in 2013 when the original map was scrapped and rebuilt, and it draws on parts of the real Jefferson, Bullitt, Hardin, Meade and Breckinridge counties [5]. In the fiction, the area is ground zero for the Knox Infection and is sealed off as an exclusion zone — the reason the map's edges and Louisville's fence line look the way they do (see `lore-foundation` for the event itself) [5].

Geographically, the Ohio River defines the map's northern and western water edge, with West Point, Riverside and Brandenburg *(B42)* sitting on its banks [7] [8] [11]. The Dixie Highway (route 31W) is the north–south spine of the eastern map through Muldraugh and West Point, while Kentucky 60, 79 and 144 tie together the southern and western settlements [5] [6] [7] [12] [13]. The Salt River separates the West Point area from the map's north-eastern panhandle, where Valley Station and Louisville lie [7] [10].

## Spawning: who can start where

On both builds, occupation-specific spawn points exist only in the four canon starting towns — Muldraugh, West Point, Riverside and Rosewood [4]. Build 42 launched with Echo Creek as a fifth default spawn town *(B42)* [6] [14]; the ability to spawn there by default was removed in 42.16.0 [14]. From 42.17, Sandbox games can instead start in any Exclusion Zone town — including Brandenburg, Ekron and Irvington — with the caveats that occupational spawns are not supported outside the canon four and the spawn point is more static *(B42)* [4] [11] [12] [13]. Louisville is not spawnable without mods on either build [10].

## The B41 towns

The community wiki attaches a relative difficulty to each town; those ratings are community judgements maintained against unstable-era versions, cited here as the wiki's assessment rather than a measured value.

### Muldraugh

Muldraugh, in the map's east along the Dixie Highway, is the game's original town — the focal point of Project Zomboid since the 2011 tech demo, rebuilt from satellite imagery of the real Muldraugh for the 2013 Steam release [6]. It is written as a low-wealth commuter and ex-Army town, and it plays that way: modest housing, trailer parks, and an industrial north side of warehouses and self-storage lots that serve as the town's weapon chest [6]. Its zombie population is sizable but clustered around key areas rather than uniform, and the town's sprawl makes a vehicle far more useful than in the compact spawn towns; the wiki names exhaustion from continuous fighting as the characteristic danger here [6]. The southern outskirts of Muldraugh were the map team's testing ground for the more detailed world-building style that later became the B42 standard *(B42)* [2].

### West Point

West Point sits on the Ohio River north of Muldraugh, close to the Salt River crossings toward Louisville, and is the easternmost spawn town [7]. The wiki rates it the hardest of the canon four: heavy zombie presence across both its western suburbs and its eastern downtown, offset by the strongest overall loot of the starting towns — notably a reliable abundance of firearms and ammunition in the residential blocks [7]. The wiki explicitly steers new players away from starting here and notes that stealth-centric characters are at a particular disadvantage in its crowds [7].

### Riverside

Riverside is a fictional town on the Ohio in the map's north-west, with Fallas Lake to its south, Brandenburg *(B42)* to its west and West Point upriver to its east [8]. The wiki calls it easy-to-medium and the go-to recommendation for first-time players: roughly 1,500–2,000 zombies on default settings by the wiki's estimate, with about two thirds concentrated in the riverfront business district and the wealthy gated community, leaving quiet suburbs to learn the game in [8]. Its weaknesses are the lack of dependable firearm spawns and the temptation to get complacent; its long-term strength is river fishing on the doorstep [8]. The wiki records that Riverside's zombie population was increased in Build 42 while remaining favourable relative to its loot *(B42)* [8].

### Rosewood

Rosewood, a fictional town with no real-world counterpart, is the smallest default spawn town, tucked into forest in the map's south with farmland to its south and the Kentucky State Prison just west [9]. Its calling cards are civic: among the default spawn towns it alone hosts a fire station and a police station together, alongside a courthouse — an axe-or-firearms starter kit if you can reach them [9]. The wiki now rates it medium: in Build 42 the town's zombies were redistributed, concentrating around the Main Street points of interest while the surrounding forest emptied, which the wiki judges makes B42 Rosewood distinctly more dangerous than its B41 reputation as a beginner haven *(B42)* [9]. The layout splits into a loot-dense, horde-dense Main Street and fenced-off eastern suburbs of two-storey houses with garages [9]. The forests make foraging and trapping convenient, but the town lacks nearby open water [9].

### March Ridge

March Ridge is a gated military settlement in the southern map: tenement-style housing surrounded by forest, with community facilities (school, community centre, medical, cinema) concentrated inside the perimeter [5]. It is not one of the canon starting towns [4] [5].

### Valley Station

Valley Station is a sparse settlement across the Salt River in the map's panhandle, on the road to Louisville [5] [10]. Its headline feature is Crossroads Mall, one of the map's large shopping destinations, alongside a drag strip and a hunting lodge [5]. Its position means travellers bound for Louisville pass through it — and through the military checkpoints beyond it [10].

### Louisville

Louisville is Knox Country's metropolis: the map's largest and most populated area, written with an in-fiction population of over 55,000 and holding, in gameplay terms, tens of thousands of zombies — moderate in density across most districts, but with a downtown the wiki describes as saturated [10]. It carries big-city infrastructure found nowhere else: two major hospitals, a mall (the Grand Ohio Mall), a university campus, an airport, refineries, corporate headquarters, and district after district of housing stock [10]. In the fiction it was fenced off from the rest of Knox Country as the Exclusion Zone border was established, and in gameplay it is genuinely hard to enter: from West Point the main Dixie Highway bridge over the Salt River is blocked (the adjacent rail bridge is the workaround), and the roads in from the Valley Station side run through military checkpoints that are among the heaviest zombie concentrations on the map [10]. There is no unmodded way to spawn there; the wiki frames the city as a destination for prepared, experienced characters [10]. In B42, Louisville is also where the new 32-level skyscrapers were built *(B42)* [3].

## The B42 expansion (all *(B42)*)

Build 42's map work pushed Knox Country westward with three full towns plus supporting locations, doubled the map's overall surface area, and delivered 1,400 new unique buildings and 20,000 new tiles (raising the game's tile total to 35,000) [2] [15]. Beyond the premade map, B42 also introduced borderless exploration with randomly generated wilderness [15].

### Brandenburg

Brandenburg, modelled on the real Brandenburg, Kentucky, anchors the map's north-west on the Ohio River, directly west of Riverside and reachable by following the riverbank [2] [11]. The Indie Stone introduced it as a new riverbank location; the wiki fills in its character: one of the largest towns on the map, a south-eastern quarter scarred by an in-fiction 1993 tornado, a docked paddle steamer (the P.S. Delilah), a detention centre and courthouse, a shopping centre, and a military blockade at the north-western bridge [2] [11]. The wiki estimates roughly 5,600 zombies on default settings and rates the town medium-hard — harder than Muldraugh, far easier than Louisville — with the population spread comparatively evenly and thickening around points of interest [11]. It is startable only via the Sandbox town options [4] [11].

### Ekron

Ekron is the smallest of the three new towns and the westernmost settlement on the map, a rural community written with an in-fiction population under 200 [2] [12]. A fenced railway line cuts the town in two with effectively a single usable road crossing, which shapes any looting route through it [12]. The wiki rates it medium-hard for an unusual reason: total numbers are modest, but density per map cell is high, with the commercial strip along Kentucky 144 — and especially the area around the community college — packing crowds into a small space [12]. The 42.20 glow-up lists Ekron among the areas entirely reworked [1] [2].

### Irvington

Irvington, modelled on the real Irvington, Kentucky, sits in the map's south-west on Kentucky 79, ringed by crop fields and livestock farms, with the Irvington Speedway race track just north of town [2] [13]. It is about a third larger than Ekron but spread thin: the wiki rates it medium, with a fairly uniform zombie distribution across a large, open-plan town where the space between buildings cuts both ways — easier to spot and fight hordes, harder to break line of sight [13]. Its notable stops include an army-surplus store, a gun club, and the speedway complex itself [13].

### Echo Creek

Echo Creek is a small rural town between the new western towns and the old map, east of Ekron and north of Irvington on Kentucky 60, split by the creek that feeds Wadsworth Lake [14]. Surrounded by farms — including a chicken farm — it is the wiki's suggested playground for B42's animal-husbandry systems [5] [14]. The wiki rates it easy-to-medium: balanced loot against a low-to-medium population, with the caveats that strong melee weapons are scarce and that zombies migrate back in from denser neighbouring cells [14]. It was a default spawn town from 42.0.0 until 42.16.0, and remains startable through the Sandbox town options [4] [14].

### Smaller areas, old and new

Around the towns sit named smaller regions: Dixie Mobile Park on the Dixie Highway; the farmland expanse of Doe Valley with the lakeside settlement of Fallas Lake at its heart; Doe Valley Forest with scattered rural points of interest; Coalfield, a Wild-West-themed tourist replica town; trailer parks near Riverside (Scenic Grove) and Brandenburg (Bright Valley) *(B42)*; an abandoned town nicknamed Tanglewood by the community; and a pre-Knox-Event burnt town near the Louisville border [5] [8] [11]. The Big Glow Up announcement adds that B42 hides further unadvertised locations — an abandoned orphanage, a reworked logging compound, an entirely new prison, a boy-scout camp among them — which it invites players to discover unspoiled [2].

## Basements and high-rises as map features (*(B42)*)

Build 41's engine imposed height limits that kept the map shallow and low-rise *(B41)* [15]. Build 42 exceeded those limits in both directions: the first test structure was a 32-floor skyscraper, several 32-level towers were then built for Louisville, and basements were added across the map [3] [15]. At stable release, Build 42 contains 400 procedurally placed basements and 75 unique hand-built ones [2]. The engine work also underpins bunkers and panic rooms as location types [15]. One of 42.20's two new Challenge modes, "Top of the World", starts the player at the top of a skyscraper — the release notes name the pair as "28 Minutes Later" and "Top of the World", replacing "Cabin in the Woods" in rotation [1] [2].

## The 42.20 map glow-up (*(B42)*)

For the stable release, an enlarged map team entirely reworked seven areas — Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron and Dixie — to a new standard: an individual visual identity per town, every building unique, consistent landscaping between buildings, and bespoke tiles where needed [2]. The Indie Stone states the rest of the map will be brought to the same standard in future versions [2]. The 42.20 patch notes summarise the same work as a "Map Glowup" with new tiles, buildings, locations and room definitions across a wide range of areas [1].

Build 42.21 *(B42)* followed with map-adjacent changes: the in-game player map was updated to remove inaccuracies while exploring, and the Spawn Point Selection preview videos were updated to match the Map Glowup [17] [18]. The same changelist lists Road Stories not spawning in some glow-up map areas as fixed, a fix to RiversideStashMap2, floorboard stash containers found with annotated maps being named more appropriately, and subbiomes no longer generating trees on dirt [17] [18]. Explosives are also listed as now working in basements [17] [18]. The changelist further lists a fix for survivors who could spawn inside the barricaded, locked gun shop in Rosewood, and a fix for returning players seeing previously unexplored areas of the map [18]. The notes do not say which areas of the glow-up map were affected by the Road Stories fix, nor what the map inaccuracies were.

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 / 42.21 *(B42)* |
|------|---------------------|---------------------|
| Map extent | Original Knox Country; playable area ends at the old western edge [2] [5] | Surface area doubled; Brandenburg, Ekron, Irvington and Echo Creek added in the west; 1,400 new unique buildings, 20,000 new tiles [2] [15] |
| Beyond the map | Premade map only | Borderless exploration with randomly generated wilderness beyond the premade map [15] |
| Verticality | Engine height limits; no basements, no true high-rises [15] | Limits exceeded: 400 procedural + 75 unique basements; 32-level skyscrapers in Louisville [2] [3] |
| Spawn towns | Four canon towns (Muldraugh, West Point, Riverside, Rosewood) [4] | Same canon four; Echo Creek default spawn 42.0.0–42.16.0; any Exclusion Zone town startable via Sandbox since 42.17 [4] [14] |
| 42.21 map follow-ups *(42.21)* | Not covered by the 42.21 notes | Player-map accuracy update, spawn-preview videos matched to the Map Glowup, Road Stories and stash-map fixes, no trees on dirt in subbiomes [17] [18] |
| Town rework | B41-era town layouts | Seven areas entirely reworked at 42.20 (Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron, Dixie) [1] [2] |
| Zombie placement | B41 distributions; Rosewood regarded as a gentle start [9] | Wiki-documented redistribution: Riverside population increased; Rosewood concentrated around Main Street and judged notably harder [8] [9] |
| Challenge maps | "Cabin in the Woods" in rotation [1] | Replaced by "28 Minutes Later" and "Top of the World" (skyscraper start) [1] |

The short version: the towns you knew are still where you left them, but B42 doubles the canvas around them, digs under them, builds over them, and — at 42.20 — repaints seven of them entirely [1] [2] [3] [15].

# Practical Guidance

- **Match the spawn to your experience.** The wiki's ladder is a serviceable guide: Riverside or (Sandbox) Echo Creek to learn the game, Rosewood or Muldraugh for a standard run, West Point when you want pressure from minute one. Treat B41-era spawn advice for Rosewood with suspicion on B42 — the redistribution changed its early game.
- **Want the new towns? Use Sandbox.** Brandenburg, Ekron and Irvington never appear on the default spawn list; start a Sandbox game and pick the town there, accepting a generic (non-occupation) spawn point.
- **Plan Louisville as an expedition, not a spawn.** Skill up, stock a vehicle, and expect the checkpoints to be the worst fights of the trip. The rail bridge beside the blocked Dixie Highway crossing is the established way over the Salt River.
- **Let the rivers and highways navigate for you.** The Ohio riverbank strings West Point → Riverside → Brandenburg *(B42)* together; Kentucky 60 links the southern towns to Echo Creek *(B42)*; the Dixie Highway runs the eastern spine. Following infrastructure beats compass-walking through forest.
- **On 42.20, relearn the reworked towns.** Seven areas were rebuilt to the new art standard; muscle memory from unstable-era runs (or old YouTube tours) will mislead you in Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron and Dixie.
- **Check basements deliberately** *(B42)*. With 475 of them in the build, houses now have a downstairs worth checking — and high-rise Louisville adds vertical clearing to city play. Budget light sources accordingly; B42's lighting model makes interiors genuinely dark.

# Common Pitfalls & Troubleshooting

- **"I can't find Brandenburg / Ekron / Irvington on my map."** You are on Build 41 — the western expansion exists only in Build 42 [2]. Check your Steam branch before assuming a bug.
- **"Echo Creek isn't on the spawn list anymore."** Correct since 42.16.0; use the Sandbox town options added in 42.17 instead [4] [14].
- **"I picked a new town in Sandbox and my occupation spawn didn't apply."** Expected: occupational spawns exist only in the four canon starting towns [4].
- **Rolling into Louisville under-prepared.** The city is deliberately gated behind checkpoints and dense hordes; the wiki's guidance — bring supplies, bring combat skills — reflects the map design, not bad luck [10].
- **Treating Rosewood as the B41-era safe start.** The wiki's B42 revision explicitly retires that reputation after the zombie redistribution [9].
- **Trusting pre-42.20 town guides.** Any guide dated before 2026-07-29 predates the glow-up rework of seven areas [1] [2].

# Community Notes & Unverified Claims

## Claim 1 — Irvington contains a King of the Hill homage neighbourhood

- **Claim:** pzwiki's Irvington trivia (and community discussion around the B42 map) holds that a block adjacent to Irvington Elementary recreates the main setting of the TV show King of the Hill, down to individual characters' houses and episode references.
- **Why unverified:** no Indie Stone source acknowledges the homage; it rests on community pattern-matching recorded on the wiki.
- **Confidence:** Medium. The claim is specific, stable across wiki revisions and easy to check in-game, but has no developer confirmation.

## Claim 2 — Fort Knox will be added to the map close to full release

- **Claim:** pzwiki lists Fort Knox as a future location, citing a sign present in the game files, and the community expects it near the game's 1.0 release.
- **Why unverified:** game-file remnants show intent, not a commitment; no dated Indie Stone announcement schedules Fort Knox, and the current stable map does not include it.
- **Confidence:** Low. The timing half of the claim is speculation layered on a real but undated artefact.

## Claim 3 — Default-settings zombie population counts per town

- **Claim:** the wiki attaches estimated default-population figures to towns — roughly 1,500–2,000 for Riverside and about 5,600 for Brandenburg — and per-cell density comparisons between Ekron, Irvington and Brandenburg.
- **Why unverified:** these are community measurements from unstable-era versions with no official counterpart, and 42.20's rework touched several of the measured towns.
- **Confidence:** Medium. The measurement method (population inspection on default settings) is plausible and internally consistent, but the numbers are unofficial and possibly stale.

# Risks & Caveats

- **Every town profile predates the 42.20 rework it describes.** The cited town revisions are versioned 42.0.2–42.19.0, and 42.20 entirely reworked Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron and Dixie [1] [2] [6] [7] [8] [9] [12]. Layout-level statements (district splits, fence lines, which side the loot is on) are the most exposed. This is the main reason the document is Medium.
- **Difficulty ratings are community judgements.** The easy/medium/hard ladder is pzwiki's editorial assessment, reproduced here with attribution — it is not a developer-stated or file-derived value [6] [7] [8] [9] [11] [12] [13] [14].
- **42.21 follow-ups are notes-only.** The 42.21 map items [17] [18] come from patch notes with no detail; whether a given town profile here changed with them was not checked in-game.
- **Challenge-name discrepancy.** The 42.20 release notes name the sprinter challenge "28 Minutes Later" [1]; the Big Glow Up post two days earlier called it "28 Seconds Later" [2]. This document follows the later release notes; an in-game menu check would settle it.
- **Zombie counts are unofficial estimates** (see Claim 3) and additionally sensitive to sandbox settings.
- **Steam announcement mirrors.** Primary citations use the Steam announcement mirrors of Indie Stone posts, verified through the Steam news API; the projectzomboid.com originals bot-block automated checkers.

# Verification Steps

1. **Confirm the expansion towns exist (B42):** start a 42.20 Sandbox game, open the spawn-region list, and confirm Brandenburg, Ekron and Irvington are selectable while Echo Creek is absent from the default (non-Sandbox) spawn list.
2. **Confirm canon-town occupational spawns:** create a character with a distinctive occupation and verify occupation spawn buildings appear only when starting in Muldraugh, West Point, Riverside or Rosewood.
3. **Confirm the glow-up scope:** retrieve the "42.20: The Big Glow Up" announcement via the Steam news API (`https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25`) and check the seven listed reworked areas against this document.
4. **Confirm verticality:** in a 42.20 game (or debug teleport), visit downtown Louisville for the high-rise towers and any suburban house with a basement hatch; the "Top of the World" challenge start doubles as a skyscraper check.
5. **Spot-check town profiles post-rework:** open the pinned pzwiki revision URLs in the References and diff them against the current pages for post-42.20 corrections, especially Riverside, Rosewood and Ekron.
6. **Settle the challenge name:** open the Challenge menu on 42.20 and record whether the sprinter mode reads "28 Minutes Later" or "28 Seconds Later".

# Open Questions

- How much did the 42.20 rework change the district-level layouts described by the pre-rework wiki revisions for Riverside, West Point, Rosewood, Muldraugh and Ekron? Needs first-hand or post-rework wiki re-verification.
- Do the wiki's per-town zombie estimates still hold on 42.20 after the rework and the B42 population redistribution work? (Feeds Claim 3.)
- Which glow-up map areas did the 42.21 Road Stories fix affect, and what inaccuracies did the updated player map correct? The notes [17] [18] give neither.
- What is the definitive in-game name of the new sprinter challenge? (Feeds the naming discrepancy in Risks.)
- Which of the unadvertised new locations (orphanage, new prison, boy-scout camp) sit where — and how should a spoiler-aware KB reference them, if at all?
- When Fort Knox ships (if it ships), which document versions need revision? (Feeds Claim 2 and the freshness re-queue.)

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved in full via the Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *42.20: The Big Glow Up* (Steam announcement, 2026-07-27; retrieved in full via the Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1839041357036410. Accessed 2026-07-31.
- [3] **The Indie Stone** — *Sky High* (Thursdoid, Steam announcement, 2023-09-21; retrieved in full via the Steam news API). https://steamcommunity.com/games/108600/announcements/detail/5219165352624877709. Accessed 2026-07-31.
- [4] **The Indie Stone** — *Location, Location* (Thursdoid, Steam announcement, 2026-04-17, covering 42.17 Unstable; retrieved in full via the Steam news API). https://steamcommunity.com/games/108600/announcements/detail/1830163047261202. Accessed 2026-07-31.
- [16] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [17] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [18] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post, 2026-09-23). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [5] **PZwiki** — *Knox Country* (revision 1439185; page versioned against 42.11.0). https://pzwiki.net/w/index.php?title=Knox_Country&oldid=1439185. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Muldraugh* (revision 1442921; page versioned against 42.0.2). https://pzwiki.net/w/index.php?title=Muldraugh&oldid=1442921. Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *West Point* (revision 1438485; page versioned against 42.13.1). https://pzwiki.net/w/index.php?title=West_Point&oldid=1438485. Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *Riverside* (revision 1443703; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Riverside&oldid=1443703. Accessed 2026-07-31. Fact-only source.
- [9] **PZwiki** — *Rosewood* (revision 1442741; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Rosewood&oldid=1442741. Accessed 2026-07-31. Fact-only source.
- [10] **PZwiki** — *Louisville* (revision 1440857; page versioned against 42.11.0). https://pzwiki.net/w/index.php?title=Louisville&oldid=1440857. Accessed 2026-07-31. Fact-only source.
- [11] **PZwiki** — *Brandenburg* (revision 1442529; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Brandenburg&oldid=1442529. Accessed 2026-07-31. Fact-only source.
- [12] **PZwiki** — *Ekron* (revision 1436857; page versioned against 42.11.0). https://pzwiki.net/w/index.php?title=Ekron&oldid=1436857. Accessed 2026-07-31. Fact-only source.
- [13] **PZwiki** — *Irvington* (revision 1441243; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Irvington&oldid=1441243. Accessed 2026-07-31. Fact-only source.
- [14] **PZwiki** — *Echo Creek* (revision 1404467; page versioned against 42.16.1). https://pzwiki.net/w/index.php?title=Echo_Creek&oldid=1404467. Accessed 2026-07-31. Fact-only source.
- [15] **PZwiki** — *Build 42* (revision 1443663). https://pzwiki.net/w/index.php?title=Build_42&oldid=1443663. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited.

**Further Reading**

# Further Reading

- The B42 feature-list overview linked from the 42.20 release notes: https://projectzomboid.com/blog/features-overview-build-42-20/ (bot-blocks automated checkers; verify in-browser).
- The Steam news API mirror used to verify every primary citation in this document: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25
- The interactive community map project referenced across the player community, map.projectzomboid.com, is linked from official channels but was not used as a fact source here: https://map.projectzomboid.com/

# Related Documents

- `players-foundation` — the Players-track foundation this document deepens (world overview at map level).
- `lore-foundation` — the Knox Event and Exclusion Zone backstory behind the geography.
- `players-vehicles` *(planned)* — travel between these towns in practice: vehicles, fuel and road hazards.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed Steam announcements 42.20.1-42.21 and the 42.21 forum changelist [16] [17] [18]; added player-map update, Rosewood gun-shop spawn fix, spawn-preview videos, Road Stories and stash-map fixes, subbiome trees and basement explosives; version-scope statements updated. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
