---
id: players-foundation
title: "Surviving Knox Country: The Core Game Across Build 41 and Build 42"
version: 1.0.1
status: approved
confidence: Medium
category: Players
topic: "Player foundations"
build: both
document_type: overview
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [modders-foundation, admins-foundation, creator-foundation, lore-foundation, meta-style-guide]
tags: [players, foundation, survival-loop, moodles, character-creation, skills, knox-country, build-42, save-compatibility]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-foundation |
| Version | 1.0.1 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 41.78.16, 42.20 |

# Executive Summary

Project Zomboid is an open-ended, permadeath zombie survival sandbox: alone or in multiplayer you loot, build, craft, fight, farm and fish to postpone an ending the game itself tells you is inevitable [8]. This document is the foundation of the Players track. It maps the core survival loop, the moodle system that reports your character's needs, character creation (occupations and traits), the skills system, and the world of Knox Country — and it does so across the two builds that matter right now: Build 41.78 (the `legacy41` branch) and Build 42.20, Build 42's first stable release, shipped 2026-07-29 [1] [2] [10].

Build 42 is the largest change to the player experience since the Build 41 animation overhaul: it adds animals and animal husbandry, a much deeper crafting and building tech tree, a new lighting model, basements and true high-rise buildings on an engine that now supports 32-storey structures, a roughly doubled map surface area, and — as of 42.13 unstable and now 42.20 stable — restored multiplayer [3] [5] [7] [9] [10]. Your Build 41 saves do not migrate: Build 41 remains playable on the `legacy41` Steam beta branch [2].

Document-level confidence is **Medium**: the release-facts spine rests on official Indie Stone announcements (High), but several player-facing details (the moodle roster, XP tables, occupation lists) are cited from pzwiki page revisions written against unstable-era versions (42.3.1–42.19) and have not been individually re-verified against 42.20.

# Key Takeaways

- Project Zomboid's loop is loot, build, craft, fight, farm and fish under permadeath — the game's own framing is "how will you die?" *(cited)* *(both)*
- Build 42.20 is **Build 42's first stable release**, shipped 2026-07-29 after a 19-month unstable cycle that began 2024-12-17 *(cited)* *(B42)*
- **Build 41 saves are not compatible with Build 42**; a `legacy41` Steam beta branch keeps 41.78 playable, and a `42.19` branch exists for finishing unstable-era saves *(cited)*
- B42 headline changes for players: animals and husbandry, a crafting and building overhaul, a new lighting system, basements and 32-level buildings, muscle strain in combat, and a map with roughly double the surface area *(cited)* *(B42)*
- Multiplayer was disabled at B42's unstable launch, returned in 42.13 unstable (2025-12-11), and ships stable in 42.20 with reworked anti-cheat and a fix for the zombie-culling population bug *(cited)* *(B42)*
- Character creation still works on the occupation + traits points system in both builds, but B42 reworked the roster: new trades tied to crafting (e.g. Blacksmith, Welder), and B41's Farmer and Fisherman replaced by Crop Farmer, Livestock Farmer and Angler *(cited)*
- B42 grows the skill list with crafting families — Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding — plus Animal Care, Butchering and Tracking *(cited)* *(B42)*
- The in-game XP-boost percentages shown at character creation are reported by the community wiki to be displayed incorrectly as of 42.13.1 *(community, unverified)*

# Purpose

This is the first document a player should read in this knowledge base. It answers: what is the shape of the game I am playing, which build am I on, what changed between Build 41 and Build 42, and where do I go next? Deeper Players-track documents (moodles, combat, individual skills, occupation/trait tables, map guides) hang off this overview and will go further than it does; this document deliberately stays at the map-of-the-territory level.

# Scope

Covered: the core survival loop and death permanence; the moodle system at overview level; character creation (occupations and traits at a high level — no exhaustive tables); the skills system including B42's new crafting skill families; the world of Knox Country in both builds; the headline player-facing changes in Build 42.20 stable; and save compatibility between builds and branches.

Not covered: per-moodle mechanics and thresholds, full occupation/trait/skill tables, combat math, looting tables, map spoilers beyond town names and publicly announced locations, multiplayer server administration (see the Admins track), and modding (see the Modders track). Unstable-branch behaviour after 42.20 is out of scope. This document is written spoiler-aware: it names places and systems but avoids loot specifics and story discoveries.

# Definitions

- **Moodle** — the icon-based status indicator system in the top-right of the screen that reports the character's physical and emotional state (hunger, panic, tiredness, etc.) [11].
- **Knox Country** — the Kentucky-based game world, modelled partly on the real area around Fort Knox and Louisville; formerly called Knox County [16].
- **Knox Event** — the in-fiction outbreak and quarantine that frames the game world; see the Lore track for detail [16].
- **Thursdoid** — community shorthand for The Indie Stone's development blog posts, mirrored as Steam announcements.
- **legacy41** — the Steam beta branch that keeps Build 41.78 installed and playable after Build 42 became the default stable build [2].
- **Unstable** — the opt-in Steam beta branch on which Build 42 was publicly developed from 2024-12-17 until stable release [4].
- **Permadeath** — when a character dies, that character is gone; the world save continues but you re-enter it as a new survivor. The store page frames the entire game around this: "how will you die?" [8].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Reachable via the `legacy41` Steam beta branch [2]; B41-specific values tagged *(B41)* |
| B42 (stable) | Yes | 42.20 | First stable B42 release, 2026-07-29 [1] [2]; B42-specific values tagged *(B42)* |

Facts sourced from pzwiki carry the page revision they were checked at; several of those revisions were written during the 42.x unstable cycle and are flagged below where they have not been re-verified on 42.20.

# Reference

## The core loop and death permanence

Project Zomboid is an open-ended zombie-infested sandbox in which survivors loot houses, build defences, and "do their utmost to delay their inevitable death day by day" — the store page's own words — with no rescue coming [8]. The loop the game advertises is: loot, build, craft, fight, farm and fish, alone or in multiplayer, on top of "a hardcore RPG skillset, a vast map, [and a] massively customisable sandbox" [8]. Infection is the signature threat: "All it takes is a bite" [8]. Death is permanent for the character (the world save persists), and the game presents dying not as failure but as the expected ending — the wiki's moodle list even includes a **Dead** moodle and a **Zombie** moodle for the moment your story ends one way or the other [11].

## Needs and moodles

The moodle system is how the game communicates needs and states: icons in the top-right corner of the screen, with hover tooltips for detail [11]. The current wiki revision lists 26 moodles, including needs (Hungry, Thirsty, Tired, Endurance), hazards (Bleeding, Injured, Pain, Sick, Hypothermia, Hyperthermia, Wet, Windchill), emotional states (Panic, Stressed, Unhappy, Bored, Drunk, Hungover), and terminal states (Dead, Zombie) [11]. Moodles are not cosmetic: for example, the Heavy Load moodle progressively reduces movement and attack speed and can ultimately damage the character, and the Tired moodle penalises combat, the vision cone and awareness [11]. That wiki page was last versioned against 42.13.2 and its per-moodle effects have not been re-verified on 42.20 [11].

## Character creation: occupations and traits

In both builds you build a character from three choices: an occupation (pre-outbreak line of work), positive traits, and negative traits, balanced against a points budget that must end at zero or above [13] [15]. Occupations grant starting skill levels; starting levels matter beyond the levels themselves, because a skill you start with levels in earns a permanent XP boost — level 0 skills earn 25% XP, while starting levels 1, 2 and 3+ earn 100%, 133% and 166% respectively per the wiki's figures [13] [15]. Some traits can also be gained or lost during play depending on your character's lifestyle [15].

The rosters differ by build. The B41-era wiki revision lists 21 occupations plus Unemployed (8 free points) *(B41)* [14]. The B42 revision lists 23 occupations plus a "Custom Occupation" option carrying the 8 free points *(B42)* [13]. Comparing the two cited rosters: B42 adds trades tied to the crafting overhaul such as Blacksmith and Tailor; B41's Metalworker, Repairman, Farmer and Fisherman do not appear, with the B42 roster instead listing Welder, DIY Expert, Crop Farmer, Livestock Farmer and Angler [13] [14]. Deeper Players-track documents will carry the full per-occupation and per-trait tables; treat any B41-era guide's occupation advice as suspect on B42.

## Skills

Skills level from 0 to 10 by earning XP from doing the relevant activity, with each level requiring more XP than the last [12]. The wiki sorts skills into six groupings — combat, agility, crafting, firearm, survivalist, and the passive pair — and notes that the passives (Strength, Fitness) need vastly more XP than regular skills: 1,500 XP for level 1 versus 75 for a regular skill, per figures the page states for Build 41.78.16 *(B41)* [12]. Skill books multiply XP gain for their skill across two-level bands, which is the main lever for levelling efficiently [12].

The B42 skill list on the same page adds a family of crafting skills — Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery and Welding — alongside animal-economy skills (Animal Care, Butchering) and Tracking, and lists Agriculture where B41 players knew Farming *(B42)* [12]. The page itself carries an "outdated" banner warning that its categorisation is still Build 41-based, so expect the in-game grouping on 42.20 to differ in presentation [12].

## The world: Knox Country

Knox Country is a partly real, partly fictional recreation of northern Kentucky around Fort Knox and Louisville [16]. The towns B41 players know — Muldraugh, West Point, Riverside, Rosewood, March Ridge, Valley Station and the city of Louisville, plus fictional additions — remain the backbone of the map [16]. Build 42 extended the map westward with three new towns: Brandenburg on the Ohio River, the small agricultural town of Ekron, and Irvington with its race track *(B42)* [3] [16].

The B42 world is also taller and deeper than B41's. The engine's previous height limits were raised during B42 development, demonstrated by a 32-floor skyscraper, with 32-level skyscrapers built for Louisville and basements added across the map *(B42)* [7]. By stable release, Build 42 contains 400 procedural basements and 75 unique ones, and — comparing builds — the map's surface area has been doubled, with 1,400 new unique buildings and 20,000 new tiles bringing the tile total to 35,000 *(B42)* [3].

## What Build 42.20 stable changed at headline level

Build 42.20 is Build 42's first stable release [10]. It reached the public stable branch on Wednesday 2026-07-29 [1] [2]. The wiki's release overview summarises the player-facing headline as: a heavily evolved Knox Country; deeper crafting and building systems; animals and animal husbandry; improved lighting and atmosphere; expanded lore and environmental storytelling; and broad quality-of-life work *(B42)* [10]. Features underpinning that headline were confirmed across development: a new lighting system with natural ambient light bouncing off walls and leaking through gaps; domestic and wild animals (sheep, chickens, pigs, cows, rats, rabbits, deer) providing meat, leather, eggs and milk, with wild animals trackable by prints and droppings; new crafting systems including pottery, blacksmithing and stone working; and advanced crop farming with realistic growing seasons *(B42)* [9]. The Indie Stone's pre-launch Thursdoid also cites rebalanced zombie spawns, combat that builds up muscle strain, dynamic music and player vocals among the changes testers responded to *(B42)* [6].

Specific to the 42.19→42.20 patch: seven areas of the map were entirely reworked (Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron and Dixie) [3]; two new Challenge modes replace "Cabin in the Woods" in rotation — "28 Minutes Later" and "Top of the World" [1]; anti-cheat was reworked and re-enabled for multiplayer, and the zombie-culling bug that caused severe drops in multiplayer zombie populations was fixed [1]. A small security patch shipped alongside the release for Builds 41 and 42.19 [1].

## Multiplayer across the builds

Build 41.78 has stable multiplayer *(B41)*, and Build 42 launched to unstable on 2024-12-17 with multiplayer initially disabled [4]. Multiplayer returned in unstable Build 42.13 on 2025-12-11, explicitly flagged as work-in-progress for stress testing, with guidance to prefer co-op or whitelisted servers and to keep servers to 20 players or fewer at that time *(B42)* [5]. With 42.20, multiplayer ships on the stable branch, with the anti-cheat rework and a long list of MP fixes in the release notes *(B42)* [1].

## Save compatibility and branches

Build 41 savegames "clearly will not be compatible with Build 42" — The Indie Stone's own wording [2]. Build 41 players who want to keep playing 41.78 (including server communities) switch to the `legacy41` beta: right-click Project Zomboid in the Steam library → Properties → Game Version & Betas → select `legacy41` [1] [2]. Players mid-way through an unstable 42.19 game face the same wall — 42.19 saves are not compatible with 42.20 — and can finish on the dedicated `42.19` beta branch selected the same way [2]. Going forward, The Indie Stone has announced a Build 42 Support Update later in 2026 focused on optimisation, additional modding support and player-requested polish, with continued multiplayer and controller improvement through the B42 patching process [2].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Build status | Maintained on the `legacy41` beta branch; received a security patch at 42.20's release [1] [2] | Stable public branch since 2026-07-29 [1] [2] |
| Saves | B41 saves play only on `legacy41` [2] | B41 saves cannot be migrated into B42 [2] |
| Crafting | Base crafting set (carpentry, cooking, metalworking-era recipes) [12] [14] | Crafting and building overhaul: pottery, blacksmithing, stone working and more, with new workstations [9] [10] |
| Skills | Six categories; Farming, Metalworking among the roster [12] | Adds Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding, Animal Care, Butchering, Tracking; Agriculture listed in place of Farming [12] |
| Occupations | 21 occupations + Unemployed [14] | 23 occupations + Custom Occupation; Welder, DIY Expert, Crop Farmer, Livestock Farmer, Angler replace Metalworker, Repairman, Farmer, Fisherman; Blacksmith and Tailor added [13] [14] |
| Animals | None | Sheep, chickens, pigs, cows, rats, rabbits, deer; husbandry, hunting and tracking [9] |
| Map | Original Knox Country towns [16] | Surface area doubled; Brandenburg, Ekron, Irvington added; seven areas reworked in 42.20 [3] |
| Verticality | Original engine height limits | Raised height limits: 32-level skyscrapers in Louisville, basements across the map (400 procedural + 75 unique) [3] [7] |
| Lighting | B41 lighting model | New lighting system with ambient bounce and light leaking through spaces [9] [10] |
| Combat feel | No muscle strain | Combat builds up muscle strain; zombie spawns rebalanced with a heavier sneak emphasis [6] |
| Audio | B41 soundtrack | Dynamic music and character vocals [6] [9] |
| Multiplayer | Stable MP | Disabled at unstable launch (2024-12-17); returned 42.13 unstable (2025-12-11); stable in 42.20 with reworked anti-cheat [1] [4] [5] |

The one-line version: Build 42 keeps the same core loop and moodle language, but rebuilds what surrounds it — the tech tree, the animal economy, the map's size and verticality, the lighting, and the character-build roster — and none of your B41 saves come with you [2] [9] [10].

# Practical Guidance

- **Decide your build first.** New players should simply play 42.20 stable — it is the default branch and the version all future patches target. Returning B41 players with a beloved save should switch to `legacy41` *before* letting Steam update, using the Properties → Betas steps above; mid-run 42.19 unstable players should hop to the `42.19` branch to finish their story.
- **Read your moodles like a dashboard.** Almost every avoidable death traces back to an ignored moodle — hover any icon for its tooltip rather than guessing. Treat Endurance and Heavy Load with particular respect before a fight.
- **At character creation, starting levels are worth more than they look.** Because level-0 skills earn only a fraction of normal XP while boosted skills earn full rate or better, an occupation or trait that starts a skill at level 1+ pays off for the whole run. Spend your points where you plan to actually play.
- **On B42, don't trust B41 guides blindly.** Occupation names, skill lists and balance shifted; check any guide's date against 2026-07-29 (stable release) and prefer this knowledge base's build-tagged documents.
- **Expect Knox Country to surprise you on 42.20** — seven towns were reworked and the announcement itself flags its screenshot gallery with "beware of spoilers". If discovery is part of your fun, go in blind; this document deliberately stops at town names.
- **Multiplayer is newly stable.** It shipped with a fresh anti-cheat rework in 42.20; if you hit issues in the first hotfix wave, that is the newest code in the build.

# Common Pitfalls & Troubleshooting

- **"Steam updated and my save is gone."** The save is not gone — it is a B41 save on a B42 install. Switch to `legacy41` via Steam Properties → Betas and it will load again [2].
- **"My 42.19 unstable save won't load on stable."** Expected: 42.19 saves are incompatible with 42.20; use the `42.19` beta branch to finish it [2].
- **Following an unstable-era B42 guide on 42.20.** Build 42 "has seen an enormous number of changes throughout development" per the release notes' own framing of the feature list — values from early-42.x guides may be stale [1].
- **Assuming B41 occupation knowledge transfers.** Picking "Farmer" or "Fisherman" from memory will fail — those entries no longer exist under those names in the B42 roster [13] [14].
- **Dismissing moodles as flavour.** Progressive moodle stages carry real mechanical penalties (movement, combat, vision) per the wiki's per-moodle notes — the icons are the game's only warning system [11].
- **Zombie population feeling wrong in older MP versions.** The zombie-culling bug that caused severe MP population drops was fixed in 42.20; if you saw ghost-town servers on unstable MP, that was it [1].

# Community Notes & Unverified Claims

## Claim 1 — The character-creation XP-boost tooltip shows the wrong percentages

- **Claim:** The in-game modifiers shown for starting skill levels 1, 2 and 3 display as +75%, +100% and +125%, while the actual experience rates are 100%, 133% and 166%; pzwiki flags this as a bug on both its Occupation and Trait pages, marked against version 42.13.1.
- **Why unverified:** No official Indie Stone patch note or dev post acknowledging the display bug was found, and the wiki flag predates 42.20 — it may have been fixed at stable without a traceable note.
- **Confidence:** Medium. The claim is consistently documented across two independently maintained wiki pages with a version stamp, but rests entirely on community wiki testing.

## Claim 2 — Build 42 is significantly harder for returning Build 41 players

- **Claim:** Community discussion on the Project Zomboid subreddit, Steam forums and content-creator coverage widely holds that B42's rebalanced zombie distribution, muscle strain and darker interiors make it substantially harder than B41 for players using B41 habits.
- **Why unverified:** "Harder" is a balance judgement, not a checkable value; the underlying mechanics (rebalanced spawns, muscle strain, sneak emphasis) are primary-sourced, but the difficulty conclusion is community synthesis.
- **Confidence:** Medium. The constituent mechanical changes are officially confirmed; only the aggregate difficulty judgement is unverified.

# Risks & Caveats

- **Hotfix-wave recency.** 42.20 stable is one day old at the time of writing; The Indie Stone has stated hotfixes will follow, and any specific value in this document could be adjusted in the first patch wave [2].
- **Unstable-era wiki citations.** The Moodle page is versioned against 42.13.2, the Skill page against 42.3.1 (and carries an outdated-categorisation banner), the Trait page against 42.19.0 and Knox Country against 42.11.0 — none re-verified against 42.20 specifically [11] [12] [15] [16]. This is the main reason the document is rated Medium.
- **Conflicting primary sources on a challenge name.** The 42.20 release notes call one new challenge "28 Minutes Later" [1], while the Big Glow Up blog three days earlier called it "28 Seconds Later" [3]. The release notes are the later and more authoritative source, but the discrepancy is unresolved in-game as far as this document has verified.
- **Roster-comparison inference.** The occupation rename/replace statements are derived by comparing two cited wiki revisions [13] [14]; The Indie Stone has not published an official rename mapping, so "replace" describes roster membership, not confirmed developer intent.
- **Steam announcement mirrors.** Primary citations use the Steam announcement mirrors of Indie Stone posts (per this project's source policy); the projectzomboid.com originals exist but bot-block automated checkers.

# Verification Steps

1. **Confirm the stable release and date:** query the Steam news API — `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25` — and locate "Build 42.20.0 Stable Released" dated 2026-07-29.
2. **Confirm the branches:** in Steam, right-click Project Zomboid → Properties → Betas and verify `legacy41` and `42.19` appear in the dropdown.
3. **Confirm the skill roster in-game (42.20):** press `L` (or open the health panel → skills tab) and compare the listed skills against the B42 list in this document.
4. **Confirm the occupation roster in-game (42.20):** start a new character and compare the occupation list with the B42 roster cited here.
5. **Confirm the challenge names (42.20):** open the Challenge menu from the main menu and record the exact titles of the two new modes.
6. **Spot-check wiki-derived values:** open the cited pzwiki revision URLs (they pin the exact revision id) and compare against the current page for post-42.20 corrections.

# Open Questions

- Is the new sprinter challenge named "28 Minutes Later" or "28 Seconds Later" in the shipped 42.20 menu? An in-game check resolves this.
- Does the XP-boost tooltip display bug (Claim 1) persist in 42.20? An in-game character-creation check resolves this.
- What is the final in-game skill categorisation on 42.20, given the wiki's outdated-categorisation banner? Needs first-hand verification for the deeper skills document.
- What exactly will the announced Build 42 Support Update contain, and when in 2026 will it land? Watch the Thursdoid feed.
- Have the moodle roster or per-moodle effects changed between 42.13.2 (the cited wiki version) and 42.20? The deeper moodles document should re-verify.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [2] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-24). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453. Accessed 2026-07-30.
- [3] **The Indie Stone** — *42.20: The Big Glow Up* (Steam announcement, 2026-07-27). https://steamcommunity.com/games/108600/announcements/detail/1839041357036410. Accessed 2026-07-30.
- [4] **The Indie Stone** — *Build 42 Unstable Out Now* (Steam announcement, 2024-12-17). https://steamcommunity.com/games/108600/announcements/detail/1785774543698069. Accessed 2026-07-30.
- [5] **The Indie Stone** — *Unstable 42 MP Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592123010. Accessed 2026-07-30.
- [6] **The Indie Stone** — *WhatZ Next* (Thursdoid, Steam announcement, 2024-11-28). https://steamcommunity.com/games/108600/announcements/detail/1784506359022970. Accessed 2026-07-30.
- [7] **The Indie Stone** — *Sky High* (Thursdoid, Steam announcement, 2023-09-21). https://steamcommunity.com/games/108600/announcements/detail/5219165352624877709. Accessed 2026-07-30.
- [8] **The Indie Stone / Valve** — *Project Zomboid* Steam store page (app 108600; description verified via the Steam appdetails API). https://store.steampowered.com/app/108600/Project_Zomboid/. Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [9] **PZwiki** — *Build 42* (revision 1443663). https://pzwiki.net/w/index.php?title=Build_42&oldid=1443663. Accessed 2026-07-30. Fact-only source.
- [10] **PZwiki** — *Build 42.20.0* (revision 1443641). https://pzwiki.net/w/index.php?title=Build_42.20.0&oldid=1443641. Accessed 2026-07-30. Fact-only source.
- [11] **PZwiki** — *Moodle* (revision 1362797; page versioned against 42.13.2). https://pzwiki.net/w/index.php?title=Moodle&oldid=1362797. Accessed 2026-07-30. Fact-only source.
- [12] **PZwiki** — *Skill* (revision 1436755; page versioned against 42.3.1, carries an outdated-categorisation banner). https://pzwiki.net/w/index.php?title=Skill&oldid=1436755. Accessed 2026-07-30. Fact-only source.
- [13] **PZwiki** — *Occupation* (revision 1391359; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Occupation&oldid=1391359. Accessed 2026-07-30. Fact-only source.
- [14] **PZwiki** — *Occupation* (revision 626093, 2024-11-14 — pre-Build 42, used for the B41 roster). https://pzwiki.net/w/index.php?title=Occupation&oldid=626093. Accessed 2026-07-30. Fact-only source.
- [15] **PZwiki** — *Trait* (revision 1442751; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Trait&oldid=1442751. Accessed 2026-07-30. Fact-only source.
- [16] **PZwiki** — *Knox Country* (revision 1439185; page versioned against 42.11.0). https://pzwiki.net/w/index.php?title=Knox_Country&oldid=1439185. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited.

**Further Reading**

# Further Reading

- The Indie Stone's Build 41→42 feature-list overview, linked from the 42.20 release notes: https://projectzomboid.com/blog/features-overview-build-42-20/ (bot-blocks automated checkers; verify in-browser).
- The official blog / Thursdoid feed: https://projectzomboid.com/blog/ — the canonical home of the Steam announcements cited above.
- The Steam news API mirror used throughout this document: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25

# Related Documents

- `modders-foundation` — the Modders-track foundation (B42's engine and script changes from a modding perspective).
- `admins-foundation` — the Admins-track foundation (servers, branches and the B42 MP rollout operationally).
- `creator-foundation` — the Creator-track foundation (covering the game as content subject matter).
- `lore-foundation` — the Lore-track foundation (the Knox Event backstory this document only gestures at).
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-07-30 | Orchestrator (KB Pipeline) | Approved and frozen — foundation cluster release kb-release-2026.07.30. | Standing mandate (2026-07-30) |
| 1.0.1 | 2026-07-30 | Orchestrator (KB Pipeline) | License-hygiene prose rewrites after arming the pzwiki n-gram gate (no factual changes). | Standing mandate (2026-07-30) |
