---
id: players-b41-to-b42-transition
title: "The B41 Veteran's Guide to Build 42: What Your Instincts Get Wrong"
version: 0.2.0
status: in-review
confidence: Medium
category: Players
topic: "Guides"
build: both
document_type: tutorial
created: 2026-07-31
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-skills-xp, players-traits-occupations, players-crafting-chains, players-animals-husbandry, players-medical-moodles, players-map-locations, players-vehicles, meta-style-guide]
tags: [players, guide, build-41, build-42, transition, veterans, muscle-strain, crafting-overhaul, traits, map-expansion, legacy41, multiplayer]
game_versions_verified: ["41.78.16", "41.78.21", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-b41-to-b42-transition |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 41.78.21, 42.20, 42.21 |

# Executive Summary

You put a thousand hours into Build 41, you stepped away, and now Steam has quietly replaced your game: Build 42.20 became Project Zomboid's stable branch on 2026-07-29, ending a nineteen-month unstable cycle that began 2024-12-17 [1] [2] [4]; the current stable build is 42.21, released 2026-09-28 [33]. This guide is written for exactly one reader — the returning Build 41 veteran — and it is organised around a blunt premise: the instincts that kept you alive in 41.78 are now, in several specific places, wrong. Your save will not load [2]. Your character-build recipe of cheap negative traits was re-priced out of existence [9] [19] [20]. Your combat habit of grinding down a horde in one long fight now injures the arms doing the swinging [6] [7]. Your looting routes cross a map that has doubled in surface area and had seven of its towns entirely rebuilt [3].

Each section below names one veteran instinct, states what actually changed with citations to primary sources, and then tells you what to do differently. Where a deeper knowledge-base document exists — and for every topic here, one does — this guide points at it rather than restating its tables. Treat this as the orientation briefing; the tier-2 documents (`players-traits-occupations`, `players-crafting-chains`, `players-medical-moodles`, `players-animals-husbandry`, `players-map-locations`, `players-skills-xp`, `players-vehicles`) are the field manuals.

Document-level confidence is **Medium**, inherited honestly from its sources: the release spine, the trait/occupation re-pricing history, the muscle-strain balance arc and the map-expansion facts are primary-sourced to Indie Stone announcements verified through the Steam news API (High), but many of the specific values it summarises come from pzwiki revisions versioned against unstable-era 42.x builds, none individually re-verified in-game on 42.20 or 42.21.

# Key Takeaways

- Your B41 saves and mods do not carry into Build 42; the `legacy41` Steam beta branch keeps 41.78 playable, and a `42.19` branch exists for finishing unstable-era saves *(cited)* *(both)*
- The B41 "free points" build meta is dead: High Thirst pays +2 instead of +6, Slow Healer +3 instead of +6, Smoker +3 instead of +4, weight traits are no longer purchasable, and Lucky/Unlucky are gone *(cited)*
- Several occupations you remember no longer exist under their old names — Repairman is DIY Expert, Metalworker's slot went to Welder, Fire Officer is Firefighter, and the fishing job is now Fishing Guide *(cited)* *(B42)*
- The crafting overhaul replaces B41's flat recipe list with progression chains from Knapping up to Blacksmithing, aimed at full settlement self-sufficiency without looting *(cited)* *(B42)*
- Combat now builds muscle strain into the limbs doing the work — long uninterrupted fights are a B41 habit that a B42 body punishes *(cited)* *(B42)*
- Animals are a new renewable food and materials economy — ten species, plus Animal Care, Butchering and Tracking skills — that simply did not exist in B41 *(cited)* *(B42)*
- The map's surface area was doubled westward (Brandenburg, Ekron, Irvington), basements and 32-level high-rises arrived, and 42.20 entirely reworked seven areas you may think you know *(cited)* *(B42)*
- Multiplayer shipped stable in 42.20 with a reworked anti-cheat after being disabled at B42's unstable launch, and has since gained a 254-player cap, further anti-cheat work and a version-mismatch notice (42.20.3 and 42.21) *(cited)* *(B42)*
- The community consensus that B42 is outright harder for returning veterans is a judgement, not a measured fact — the constituent changes are real, the difficulty conclusion is quarantined below *(community, unverified)*

# Purpose

This document answers the question every returning player asks first — "what do I actually need to unlearn?" — and answers it in one place, instinct by instinct. The Players-track foundation (`players-foundation`) maps the whole territory for any reader; this guide re-cuts the same verified facts specifically along the seam between a B41 veteran's muscle memory and Build 42's reality, and routes the reader to the deeper document for every topic it opens. It exists so that a veteran can be productively wrong for one evening of reading instead of fatally wrong for three in-game weeks.

# Scope

Covered, one instinct per section: save and mod compatibility and the escape-hatch branches; character-build economics (trait re-pricing, occupation roster changes); the crafting overhaul at chain level; muscle strain and the changed pacing of combat; animals as a food economy; the map expansion, rework and verticality; lighting and basements as looting changes; and multiplayer differences at overview level.

Not covered: full tables of anything — trait costs, occupation kits, XP curves, recipes, town profiles and strain formulas live in the tier-2 documents this guide cites by id. Also out of scope: server administration (Admins track), modding (Modders track), lore (Lore track), and unstable-branch behaviour after 42.20. Written spoiler-aware: systems and town names, no loot locations or story content.

# Definitions

- **legacy41** — the Steam beta branch that keeps Build 41.78 installed and playable now that Build 42 is the default stable build; selected via Steam library → Properties → Game Versions & Betas [2].
- **42.19 branch** — the parallel Steam beta for finishing an unstable-era 42.19 save, which is not compatible with 42.20 [2].
- **Free points** — community shorthand for B41 negative traits whose in-play cost was trivial relative to the points they granted; the pattern the B42 trait re-pricing targeted (see `players-traits-occupations`).
- **Crafting chain** — a B42 sequence of skills and workstations where earlier links produce the tools and materials later links require; the term is developed in `players-crafting-chains`.
- **Muscle strain** — Build 42's accumulated exertion damage, applied to the specific body parts performing an action rather than to overall health [25].
- **Map glow-up** — the developers' name for the 42.20 map overhaul that entirely reworked seven existing areas [3].
- **Thursdoid** — community shorthand for The Indie Stone's development blog posts, mirrored as Steam announcements; the primary-source spine of this guide.

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16; 41.78.21 hotfix notes | The "before" state of every instinct here; B41-only values tagged *(B41)*; the legacy line is primary-attested through 41.78.21 (2026-08-26, a security-fix hotfix) [31] |
| B42 (stable) | Yes | 42.20, 42.21 (patch notes) | The "after" state; B42-only values tagged *(B42)*; 42.20 stable since 2026-07-29 [1] [2], 42.21 stable since 2026-09-28 [33] |

This is a synthesis document: it reuses facts already cited in the tier-2 Players documents and re-verifies the citations, but it performs no new in-game verification of its own. Re-baseline 2026-10-07: the guide was re-checked against the official 42.20.1, 42.20.3, 42.20.4, 42.21 unstable and 42.21 stable posts and the abridged TIS forum 42.21 changelist [29] [30] [31] [32] [33] [34]; statements those notes do not touch are carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found, and were not re-tested in-game. Where a tier-2 document flags a value as unstable-era and not re-checked on 42.20, that flag travels with the fact into this guide.

# Reference

## Instinct 1 — "I'll just update and pick up my save" (wrong: nothing carries over)

What changed: Build 41 saves and mods are not compatible with Build 42 — The Indie Stone stated this in bold at the unstable launch ("Build 41 saves and mods are NOT compatible with Build 42") [4], and repeated the save half of it the week before stable release [2]. Steam switched the default branch to Build 42 with the 42.20 stable release on 2026-07-29 [1] [2]. Two escape hatches exist, both official: the `legacy41` beta branch keeps 41.78 playable (right-click Project Zomboid in the Steam library → Properties → Game Versions & Betas → `legacy41`), and a `42.19` beta branch exists because unstable 42.19 saves are also not compatible with 42.20 [2]. Build 41 was not abandoned at the switch: a security patch shipped for Build 41 and 42.19 alongside the stable release [1], and a further legacy security hotfix, 41.78.21, followed on 2026-08-26 [31]. Looking forward, The Indie Stone has announced a Build 42 Support Update for later in 2026 focused on optimisation, additional modding support and player-requested polish [2].

What to do differently: decide which game you are playing *before* launching. If the old save is the point, switch to `legacy41` first and finish your story there [2]. If you are ready for B42, start fresh and treat your Workshop mod list as gone — B41 mods do not carry over, and whether each has a B42 port is a per-mod question for its Workshop page [4]. The 42.21 notes add a safety statement: existing saves on 42.20.4 should not be affected by 42.21, and a manual backup is recommended before trying 42.21 on the unstable branch with an existing save [32]. The deeper branch-and-release picture is in `players-foundation`.

## Instinct 2 — "Smoker, High Thirst, Slow Healer, done — free points" (wrong: the menu was re-priced)

What changed: Build 42 did not just add character options, it deliberately re-priced the whole creation menu across documented balance waves — a "Trait Balance Pass" in 42.16 and occupation/trait re-pricing in 42.17, with the stated aim of adjusting costs "to better reflect their value in relation to current gameplay features" [8] [9] [15]. The famous B41 point-printers collapsed: comparing the pinned B41 and B42 trait revisions, High Thirst fell from +6 to +2, Slow Healer from +6 to +3, and Smoker from +4 to +3 — with the 42.17 notes showing High Thirst and Smoker being nudged *up* to those values from even lower B42-cycle prices [9] [19] [20]. Obese, Overweight, Underweight and Very Underweight are no longer purchasable at all (weight traits are adaptive-only in B42, with new Fast/Slow Metabolism negatives at +2 as the entry points), and Lucky and Unlucky are listed as removed [19] [20].

The occupation roster churned too. Renames confirmed by patch notes: Repairman → DIY Expert, Fisher → Angler, Outdoorsman → Outdoorsy and Can't Read → Illiterate in the 42.0.1 rename block [7]; Fire Officer → Firefighter, Angler → Fishing Guide and the Wilderness Knowledge trait → Bushcrafter in 42.16 [8]; Crop Farmer and Livestock Farmer → Farmer and Rancher in 42.13 [14]. B41's Metalworker does not appear in the pinned B42 roster; Welder occupies its role, alongside genuinely new trades — Blacksmith, Rancher, Tailor — that exist to front-load the new crafting and animal systems [21] [22]. The 42.21 notes confirm Welder as a shipped occupation name and state that Welder characters now start with Welding recipes instead of Blacksmithing recipes [32] [34]; they do not state that Welder replaced Metalworker. Several occupations were re-priced in 42.17: Doctor, Nurse and Rancher to 0 points, Electrician and DIY Expert to -2, Welder to -4 [9].

What to do differently: throw away your memorised build and rebuild it from the B42 tables in `players-traits-occupations` — every B41 "free points" guide is now actively misleading. Two habits to adopt: first, cheap utility positives are the new lever (First Aider, Iron Gut, Light Eater, Low Thirst and Nutritionist all sit at -2 in the pinned B42 revision [20]); second, if you plan to play a B42 system, pick the occupation built for it — the trades exist precisely so a Blacksmith or Rancher starts as a professional [15] [22].

## Instinct 3 — "Loot carpentry tools, grab a propane torch, plant some crops — self-sufficient" (wrong: there is a tech tree now)

What changed: Build 41 crafting was a flat recipe list; Build 42 rebuilt it into progression chains, and The Indie Stone's stated goal is that a long-lived settlement can "create everything they need without relying on looting" [10]. The B41 skill roster of 26 grew to a B42-era roster of 35: seven new crafting skills (Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding) plus the animal trio (Animal Care, Butchering, Tracking), with Farming renamed to Agriculture and Sprinting to Running *(B42)* [23] [24]. Your single B41 Metalworking skill was split in two: Welding is the propane-torch heir to what you knew, while the forge-and-anvil skill was renamed from "Metalworking" to "Blacksmithing" in patch 42.12 — so even early-B42 guides use a name the game no longer shows *(B42)* [11] [23] [24]. The primitive chain starts from foraged flint and runs Knapping → Carving → Pottery → Masonry, feeding tools, crucibles and bricks upward into the metal chains; Welder characters starting with Welding rather than Blacksmithing recipes since 42.21 fits this split *(B42)* [32] [34]; recipes now arrive through four routes including the 42.3 "Research Craft" system that reverse-engineers learnable recipes from looted items *(B42)* [10] [16] [24].

What to do differently: stop planning your base around what you can loot and start planning around what you can *chain*. Knapping and Carving are nearly free to start and quietly produce the tools every later chain assumes; Blacksmithing is the deep end, with charcoal, furnaces and forge tiers between you and forged steel. The full chain map — stations, fuels, materials, and which occupation front-loads which chain — is `players-crafting-chains`; the XP mathematics of levelling the new skills efficiently is `players-skills-xp`. And when you loot, right-click interesting tools: since 42.3, researching an item can teach you its recipe and pay the crafting XP with it [16].

## Instinct 4 — "I'll kite the horde and swing until it's done" (wrong: your arms are a resource now)

What changed: The Indie Stone deliberately changed the flow of the game — "rebalanced zed spawns, combat building up muscle strain and fresh focus on the player having to sneak by crowds" is their own summary of what internal testers responded to before B42's unstable launch [6]. Muscle strain is not a moodle: it is fatigue damage written into the specific limbs doing the work, scaling with the number of zombies a swing connects with and scaled down by the relevant weapon skill and Strength *(B42)* [25]. The system went through a documented balance arc you should know about when reading older guides: melee strain was cut to 60% of its launch value three days into unstable [7], and the 42.15 Apocalypse preset ships with explicitly reduced muscle-strain and discomfort impact as the lore-canon tuning [17]. A sandbox multiplier, `MuscleStrainFactor` (default 0.7 in the post-42.20 settings snapshot), scales the whole system *(B42)* [28].

What to do differently: fight in bursts, not marathons. Ten zombies spread across a morning cost far less than ten in one continuous brawl, because strain stacks per zombie struck into the same arms [25]. Grip two-handed weapons with both hands, treat stomps and shoves as the cheap options, and read the rebalanced spawn distribution as an invitation to sneak past what you used to grind through [6] [25]. If the system is not the game you want, `MuscleStrainFactor` is a legitimate dial [28]. A small 42.21 convenience for exercise: characters now re-equip items automatically afterwards [34]. The full strain mechanics, the moodle roster changes and the medical model are in `players-medical-moodles`.

## Instinct 5 — "Food means cans, crops and fishing" (wrong: there is a livestock economy)

What changed: Build 42 put living animals into Knox Country for the first time — the cited roster spans ten species (chickens, cows, deer, mice, pigs, rabbits, raccoons, rats, sheep and turkeys), with livestock providing renewable milk, eggs, wool, meat and hides that feed the crafting economy's leather chain *(B42)* [18] [26]. Three new skills support it: Animal Care and Butchering in the Farming family, Tracking under Survivalist for following the physical evidence (prints, droppings, broken twigs) that migrating wild deer and rabbits leave *(B42)* [24] [26]. Butchering on a butcher hook yields more meat plus the animal's unprocessed hide, and the 42.20 release notes further increased meat cuts from large animals on the hook — while roadkill butchering was deliberately nerfed during the cycle to yield significantly less than a clean kill *(B42)* [1] [27]. The Rancher occupation exists specifically to front-load this economy at 0 points [22]. For cold storage, 42.21 changed two behaviours *(B42)*: fridges and freezers now warm gradually on the day the power goes out, and refrigeration now applies correctly to food inside a bag in a fridge or freezer [32] [34].

What to do differently: rethink your food plan as a portfolio. In B41 your late game was crops, fish and traps *(B41)*; in B42 a penned flock plus a post-calving cow is a renewable calorie and materials stream that also feeds Blacksmithing's leather requirements. Start small — chickens are the classic entry — feed and water before anything else, and butcher on a hook, not the ground [26] [27]. The full system (zones, enclosures, breeding genetics, hunting) is `players-animals-husbandry`.

## Instinct 6 — "I know the map" (wrong: it doubled, and seven towns were rebuilt)

What changed: Build 42 doubled the map's surface area, pushing westward with three full towns — Brandenburg on the Ohio River, rural Ekron, and Irvington with its speedway — plus roughly 1,400 new unique buildings *(B42)* [3]. The engine's height limits fell in both directions: 32-level skyscrapers were built for Louisville after a 32-floor test structure proved the ceiling, and stable B42 contains 400 procedural and 75 unique basements *(B42)* [3] [12]. Then, at 42.20 itself, an enlarged map team entirely reworked seven existing areas — Riverside, West Point, Rosewood, Fallas Lake, Muldraugh, Ekron and Dixie — to a new art standard [3]. Your spawn options changed too: occupation-specific spawns remain limited to the canon four towns, but since 42.17 a Sandbox game can start in any Exclusion Zone town, including the new western three *(B42)* [13].

What to do differently: downgrade your route knowledge from "memorised" to "hypothesis". The towns are where you left them, but 42.20 rebuilt the interiors of seven of them — pre-42.20 video tours and your own unstable-era runs will mislead you in exactly the places you feel most confident [3]. 42.21 also updated the in-game player map to remove inaccuracies while exploring [34], so a map you drew up on 42.20 may read differently. Budget a scouting pass before committing to a base in a reworked town, and treat the western expansion as genuinely new content rather than more-of-the-same. Town-by-town profiles, difficulty ladder and the expansion geography are in `players-map-locations`; vehicle logistics for the bigger map are in `players-vehicles`.

## Instinct 7 — "Kick the door, sweep the rooms, strip the shelves" (wrong: interiors are dark and buildings grew a floor you never checked)

What changed: Build 42 replaced the lighting model — the feature list describes a new lighting system with natural ambient light bouncing off walls and leaking through gaps, and improved darkness and atmosphere as a headline of the build *(B42)* [18]. At the same time the places you loot gained volume: 475 basements across the map and true high-rises in Louisville mean structures now extend below and far above the B41 envelope *(B42)* [3] [12]. One of 42.20's two new Challenge modes, "Top of the World", starts at the top of a skyscraper — a fair signal of how seriously the build treats verticality [1]. Two 42.21 changes touch this instinct *(B42)*: explosives now work in basements, and XXL trees cut away better for players in vehicles and no longer hide the houses and furniture they overhang, which the developers describe as work in progress [32] [33] [34].

What to do differently: loot like light matters, because it now does. Carry a light source as standard kit, expect interiors — especially windowless rooms and basements — to be genuinely dark, and add "is there a basement hatch?" to your house-clearing checklist. In cities, plan vertical clears (stairwells, floors, roof access) the way you used to plan street-by-street sweeps. The map-feature side of this is covered in `players-map-locations`.

## Instinct 8 — "Multiplayer works like it did in 41.78" (wrong: it was rebuilt in public and is newly stable)

What changed: Build 41.78 has long-stable multiplayer *(B41)*; Build 42 launched to unstable on 2024-12-17 with multiplayer disabled [4]. MP returned in unstable 42.13 on 2025-12-11, explicitly flagged as work-in-progress for stress testing, with guidance at the time to prefer co-op or whitelisted servers and keep player counts to 20 or fewer *(B42)* [5]. With 42.20, multiplayer ships on the stable branch with a reworked and re-enabled anti-cheat and a fix for the zombie-culling bug that caused severe drops in multiplayer zombie populations on earlier B42 MP builds *(B42)* [1]. Later changes *(B42)*: 42.20.1 fixed a chunk-unloading performance problem on MP servers, fixed broken B41 worlds being hostable on B42 servers, and fixed a missing menu for players switching from B41 to B42 [29]; 42.20.3 added support for up to 254 players plus administrator access when a server is full [30]; 42.21 expanded the anti-cheat, added a notification for players who try to connect to a server running a different game version, made the server browser show the last wipe instead of the last restart, and fixed zombies disappearing after chunk re-entry and several MP zombie-duplication cases [32] [34].

What to do differently: expect B42 MP to feel familiar in shape but young in polish — it is the newest major code in the build, and its anti-cheat has been expanded again since 42.20 [1] [34]. If your group saw ghost-town servers on unstable MP, that was the culling bug, fixed at stable [1]; if zombies vanish when you leave and re-enter an area, 42.21 fixed that in both SP and MP, though the developers say some instances remain [33] [34]. Server communities that want zero disruption still have `legacy41` as a supported home [2]. Server-side configuration is the Admins track's territory.

# B41 vs B42 Delta

This entire document is a delta, so this section compresses it: one row per instinct, from the habit to the correction.

| Veteran instinct | B41 reality it grew from *(B41)* | B42 reality that breaks it *(B42)* | Deeper doc |
|------------------|----------------------------------|-------------------------------------|------------|
| "My save carries over" | One continuous 41.x branch, still receiving hotfixes (41.78.21) [31] | B41 saves and mods incompatible; `legacy41` and `42.19` beta branches as escape hatches [2] [4] | `players-foundation` |
| "Stack cheap negatives" | High Thirst +6, Slow Healer +6, Smoker +4, purchasable weight traits, Lucky/Unlucky [19] | +2 / +3 / +3, weight traits adaptive-only, Lucky/Unlucky removed, waves of re-pricing in 42.16–42.17 [8] [9] [20] | `players-traits-occupations` |
| "I know the job list" | 21 occupations + Unemployed; Metalworker, Repairman, Fire Officer, Fisherman [21] | Renamed and extended roster: DIY Expert, Firefighter, Fishing Guide, Farmer/Rancher; Welder, Blacksmith, Tailor added [7] [8] [14] [22] | `players-traits-occupations` |
| "Loot is the economy" | Flat recipe list; one Metalworking skill; 26 skills [23] | Crafting chains from Knapping up; Welding/Blacksmithing split; 35 skills; item research; self-sufficiency as stated design goal [10] [11] [16] [24] | `players-crafting-chains`, `players-skills-xp` |
| "Grind the horde down" | No muscle strain; combat cost was endurance and risk [23] | Per-limb muscle strain scaling with zombies struck; rebalanced spawns; sneak emphasis; `MuscleStrainFactor` dial [6] [25] [28] | `players-medical-moodles` |
| "Food = cans, crops, fish" | No living animals | Ten-species animal economy: milk, eggs, wool, meat, leather; Animal Care/Butchering/Tracking skills [24] [26] [27] | `players-animals-husbandry` |
| "I know the map" | Original Knox Country extent and height limits | Surface doubled; Brandenburg, Ekron, Irvington; basements and 32-level towers; seven areas reworked at 42.20 [3] [12] [13] | `players-map-locations` |
| "Sweep and strip interiors" | B41 lighting model; no basements | New lighting with ambient bounce and leak; 475 basements; vertical city clears [3] [18] | `players-map-locations` |
| "MP as I left it" | Stable 41.78 MP | Disabled at unstable launch; back at 42.13; stable at 42.20 with anti-cheat rework and culling fix; 254-player cap (42.20.3); further anti-cheat and version-mismatch notice (42.21) [1] [4] [5] [30] [34] | `players-foundation` (Admins track for servers) |

The one-line version: the survival loop you loved is intact, but almost every optimisation you built on top of it — build recipes, grind patterns, loot routes, food plans — was invalidated on purpose [2] [6] [9] [10].

# Practical Guidance

A returning veteran's first-session checklist, in order:

1. **Pick your branch before Steam picks for you.** Old save you care about → `legacy41` now; mid-run 42.19 unstable game → the `42.19` beta; otherwise start fresh on 42.21 stable.
2. **Re-learn character creation from the B42 tables, not from memory.** Assume every negative trait you used to take pays less and every utility positive costs less; check `players-traits-occupations` before spending a point.
3. **Pick the occupation for the system you want to learn.** Blacksmith for the forge chain, Rancher for animals, Welder for the torch — the zero-point re-priced jobs (Doctor, Farmer, Firefighter, Lumberjack, Nurse, Rancher) are strong, low-risk re-entry choices.
4. **Change your combat default from "clear it" to "thin it".** Short engagements, both hands on two-handed weapons, stomps for the dropped, and a genuine willingness to sneak past what you would once have farmed.
5. **Start the primitive crafting chain in week one.** A table, foraged flint and branches buy you Knapping and Carving levels and the tools the rest of the tree assumes; clay and charcoal are the stockpiles your future self will thank you for.
6. **Add animals to the food plan early but small.** Chickens first; feed and water are the only non-negotiables; butcher on a hook.
7. **Scout before you trust the map.** Especially in Riverside, West Point, Rosewood, Muldraugh, Ekron, Fallas Lake and Dixie — the seven 42.20-reworked areas — and check houses for basement hatches as you go.
8. **Kit for darkness.** A light source is now standard loadout, not situational equipment.
9. **Date-check every guide you read against 2026-07-29 (42.20) and 2026-09-28 (42.21).** Build 42 changed continuously across nineteen months of unstable patches; even correct-for-its-day B42 advice can describe a system that was rebalanced twice since.
10. **Use sandbox dials without shame.** Muscle strain, zombie transmission, XP rates — B42 exposes more of its difficulty as settings than B41 did, and the Apocalypse preset itself ships with reduced strain impact as the canon tuning.

# Common Pitfalls & Troubleshooting

- **"Steam updated and my save is gone."** It is not gone — it is a B41 save on a B42 install. Switch to `legacy41` via Properties → Betas and it loads again [2].
- **"My mods are broken."** B41 mods are not compatible with B42 by design; check each mod's Workshop page for a B42 version rather than troubleshooting locally [4].
- **"I can't find Farmer/Fisherman/Metalworker/Repairman."** Renamed or replaced: the current names are Farmer/Rancher (split), Fishing Guide, Welder (role successor) and DIY Expert [7] [8] [14] [22].
- **"A guide told me to take Obese for +10."** B41 advice; weight traits are adaptive-only on B42 and the closest purchasable is Slow Metabolism at +2 [20].
- **"Where did the Metalworking skill go?"** Split: your torch work is Welding; the forge skill is Blacksmithing (and was itself called Metalworking in early B42 unstable, so old B42 guides misname it too) [11] [23] [24].
- **"My character's arms hurt and my swings got worse mid-fight."** Working as designed — muscle strain accumulating in the limbs; rest, shorter fights and weapon skill are the fixes, not first aid [6] [25].
- **"This town doesn't match my mental map / my favourite video tour."** Seven areas were entirely reworked at 42.20; pre-stable layout knowledge is stale in exactly those towns [3].
- **"Our MP server's zombie population felt empty."** The culling bug on unstable B42 MP; fixed in 42.20 — update the server rather than tuning population settings around it [1].
- **"Zombies vanish when I leave an area and come back."** A chunk re-entry bug in SP and MP, fixed in 42.21; update the game before changing settings [33] [34].
- **"I can't join my friend's server."** Check both sides run the same game version; 42.21 added a notification for exactly this mismatch [34].
- **"Indoor rooms are pitch black — is my install broken?"** No: the new lighting model makes unlit interiors genuinely dark; carry light [18].

# Community Notes & Unverified Claims

## Claim 1 — Build 42 is significantly harder for returning Build 41 veterans

- **Claim:** Community discussion across the Project Zomboid subreddit, Steam forums and creator coverage broadly holds that B42's rebalanced zombie distribution, muscle strain and darker interiors make it substantially harder than B41 for players running on B41 habits.
- **Why unverified:** "Harder" is a balance judgement, not a checkable value; the constituent mechanics (rebalanced spawns, muscle strain, sneak emphasis, darkness) are primary-sourced [6] [18], but no measurable difficulty comparison exists, and The Indie Stone frames the changes as flow changes rather than difficulty increases [6].
- **Confidence:** Medium. The mechanical inputs are officially confirmed; only the aggregate difficulty conclusion is community synthesis.

## Claim 2 — The character-creation screen displays the wrong XP-boost percentages

- **Claim:** The boost values shown in-game for starting skill levels 1, 2 and 3 read +75%, +100% and +125% while the actual XP rates are 100%, 133% and 166%; pzwiki documents this consistently on its Trait and Occupation pages, stamped against 42.13.1 — relevant to veterans precisely because it makes in-game numbers untrustworthy while rebuilding a character.
- **Why unverified:** No Indie Stone patch note or dev post acknowledges the display bug, and the wiki stamp predates 42.20 — it may have been fixed at stable without a traceable note. Tracked in detail as Claim 1 of `players-skills-xp`.
- **Confidence:** Medium. Consistently documented across independently maintained wiki pages on both builds' revisions, but resting entirely on community testing.

# Risks & Caveats

- **This is a synthesis document, and it inherits its sources' staleness.** Trait and occupation values trace to pzwiki revisions versioned 42.18.0–42.19.0, the muscle-strain mechanics to a 42.15.3-stamped Health revision, the animal roster to a 42.6.0-stamped page, and the skill rosters to 42.3.1-era pages — none re-verified in-game on 42.20 [20] [22] [24] [25] [26]. The tier-2 documents carry the detailed per-source flags.
- **Patch recency.** Hotfixes 42.20.1 to 42.20.4 and the 42.21 update have landed since the original write-up [29] [30] [31] [33]; values those notes do not cover were not re-tested, and further patches may shift them.
- **Renames vs roster comparison.** Some occupation successions (notably Metalworker → Welder) rest on comparing pinned wiki revisions rather than an explicit patch-note statement (the 42.21 notes confirm the Welder name but not a rename [32] [34]); `players-traits-occupations` classes each rename by its evidence and this guide follows its classifications [21] [22].
- **The instinct framing is editorial.** Which facts are grouped under which "instinct" is this document's organisational choice; the facts themselves carry the citations, the framing does not.
- **Abridged forum changelist.** The TIS forum 42.21 list [34] was captured in abridged form; an absent item is not necessarily absent from the full list.
- **Steam announcement mirrors.** All primary citations use Steam announcement URLs per project source policy; those hosts bot-block automated link checkers (the checker warns rather than fails). Every gid cited here was re-verified against the ISteamNews API for app 108600 on 2026-07-31.

# Verification Steps

1. **Branches:** in Steam, right-click Project Zomboid → Properties → Betas and confirm `legacy41` and `42.19` appear in the dropdown [2].
2. **Trait economy:** on 42.20, open character creation and record the point values of High Thirst, Slow Healer and Smoker against the +2/+3/+3 stated here; confirm Obese and Lucky are absent from the purchasable lists [9] [20].
3. **Occupation names:** on the same screen, confirm the roster shows DIY Expert, Welder, Firefighter, Fishing Guide, Farmer and Rancher rather than their B41-era names [7] [8] [14] [22].
4. **Skill roster:** open the skills panel (`L`) and confirm the crafting family (Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding) and animal skills (Animal Care, Butchering, Tracking) are present, and that Farming/Sprinting appear as Agriculture/Running [23] [24].
5. **Muscle strain:** fight a small group on 42.20, open the health panel and observe strain accumulating in the weapon arm; compare a long fight against several short ones [25].
6. **Map rework:** visit one of the seven named reworked areas and compare against a pre-42.20 map tour or your own memory [3].
7. **42.21:** confirm the installed build reads 42.21, a Welder character starts with Welding recipes, and (in MP) a client on a different version gets the mismatch notice [32] [34].
8. **Primaries:** re-query the Steam news API — `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=300&maxlength=1` — and confirm the titles and dates of the announcements cited below.

# Open Questions

- Does the balance of muscle strain, trait pricing or animal values shift in patches after 42.21, and which sections here need re-synthesis when the tier-2 documents update?
- What will the announced Build 42 Support Update change for returning players — particularly modding support, the main remaining B41→B42 friction this guide can only wave at [2]?
- Is there a measurable basis for the "B42 is harder" consensus (Claim 1) — for example a comparable-settings survival-time comparison — that could move it out of quarantine?
- How many major B41 Workshop mods now have B42 ports, and is a per-mod compatibility reference worth a future document?
- Does the XP-boost display bug (Claim 2) persist on 42.20 or 42.21? One character-creation screenshot resolves it.

# References

**Primary Sources** — official Indie Stone Steam announcements and patch notes; every gid re-verified via the Steam news API (`ISteamNews`, app 108600) on 2026-07-31.

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-24). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453. Accessed 2026-07-31.
- [3] **The Indie Stone** — *42.20: The Big Glow Up* (Steam announcement, 2026-07-27). https://steamcommunity.com/games/108600/announcements/detail/1839041357036410. Accessed 2026-07-31.
- [4] **The Indie Stone** — *Build 42 Unstable Out Now* (Steam announcement, 2024-12-17). https://steamcommunity.com/games/108600/announcements/detail/1785774543698069. Accessed 2026-07-31.
- [5] **The Indie Stone** — *Unstable 42 MP Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592123010. Accessed 2026-07-31.
- [6] **The Indie Stone** — *WhatZ Next* (Thursdoid, Steam announcement, 2024-11-28). https://steamcommunity.com/games/108600/announcements/detail/1784506359022970. Accessed 2026-07-31.
- [7] **The Indie Stone** — *Hotfix 42.0.1 - Unstable Release* (Steam announcement, 2024-12-20). https://steamcommunity.com/games/108600/announcements/detail/1786573930668296. Accessed 2026-07-31.
- [8] **The Indie Stone** — *Build 42.16.0 Unstable Released* (Steam announcement, 2026-03-31). https://steamcommunity.com/games/108600/announcements/detail/1828441623111900. Accessed 2026-07-31.
- [9] **The Indie Stone** — *Build 42.17.0 Unstable Released* (Steam announcement, 2026-04-20). https://steamcommunity.com/games/108600/announcements/detail/1830163047266254. Accessed 2026-07-31.
- [10] **The Indie Stone** — *Crafting RamblZ* (Thursdoid, Steam announcement, 2023-04-13). https://steamcommunity.com/games/108600/announcements/detail/6539831443777817851. Accessed 2026-07-31.
- [11] **The Indie Stone** — *42.12.0 UNSTABLE Released* (Steam announcement, 2025-09-25). https://steamcommunity.com/games/108600/announcements/detail/1811772772244324. Accessed 2026-07-31.
- [12] **The Indie Stone** — *Sky High* (Thursdoid, Steam announcement, 2023-09-21). https://steamcommunity.com/games/108600/announcements/detail/5219165352624877709. Accessed 2026-07-31.
- [13] **The Indie Stone** — *Location, Location* (Thursdoid, Steam announcement, 2026-04-17). https://steamcommunity.com/games/108600/announcements/detail/1830163047261202. Accessed 2026-07-31.
- [14] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972. Accessed 2026-07-31.
- [15] **The Indie Stone** — *Balancing Time* (Thursdoid, Steam announcement, 2026-03-30). https://steamcommunity.com/games/108600/announcements/detail/1828441623110846. Accessed 2026-07-31.
- [16] **The Indie Stone** — *42.3.0 UNSTABLE Released* (Steam announcement, 2025-02-11). https://steamcommunity.com/games/108600/announcements/detail/1790848102789684. Accessed 2026-07-31.
- [17] **The Indie Stone** — *Build 42.15.0 Unstable Released* (Steam announcement, 2026-03-09). https://steamcommunity.com/games/108600/announcements/detail/1826362059930323. Accessed 2026-07-31.

- [29] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [30] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895. Accessed 2026-10-07.
- [31] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [32] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [33] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [34] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post, 2026-09-23; abridged "selected" capture retrieved 2026-10-07). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [18] **PZwiki** — *Build 42* (revision 1443663). https://pzwiki.net/w/index.php?title=Build_42&oldid=1443663. Accessed 2026-07-31. Fact-only source.
- [19] **PZwiki** — *Trait* (revision 662897, 2024-12-13; versioned 41.78.16 — the B41 trait economy). https://pzwiki.net/w/index.php?title=Trait&oldid=662897. Accessed 2026-07-31. Fact-only source.
- [20] **PZwiki** — *Trait* (revision 1442751; page versioned against 42.19.0 — the B42 trait economy). https://pzwiki.net/w/index.php?title=Trait&oldid=1442751. Accessed 2026-07-31. Fact-only source.
- [21] **PZwiki** — *Occupation* (revision 626093, 2024-11-14; versioned 41.78.16 — the B41 roster). https://pzwiki.net/w/index.php?title=Occupation&oldid=626093. Accessed 2026-07-31. Fact-only source.
- [22] **PZwiki** — *Occupation* (revision 1391359; page versioned against 42.18.0 — the B42 roster). https://pzwiki.net/w/index.php?title=Occupation&oldid=1391359. Accessed 2026-07-31. Fact-only source.
- [23] **PZwiki** — *Skill* (revision 663165, 2024-12-14; versioned 41.78.16 — the 26-skill B41 roster). https://pzwiki.net/w/index.php?title=Skill&oldid=663165. Accessed 2026-07-31. Fact-only source.
- [24] **PZwiki** — *Skill* (revision 1436755; page versioned against 42.3.1 — the 35-skill B42-era roster). https://pzwiki.net/w/index.php?title=Skill&oldid=1436755. Accessed 2026-07-31. Fact-only source.
- [25] **PZwiki** — *Health* (revision 1389265; page versioned against 42.15.3 — muscle-strain mechanics). https://pzwiki.net/w/index.php?title=Health&oldid=1389265. Accessed 2026-07-31. Fact-only source.
- [26] **PZwiki** — *Animal* (revision 1385247; page versioned against unstable 42.6.0). https://pzwiki.net/w/index.php?title=Animal&oldid=1385247. Accessed 2026-07-31. Fact-only source.
- [27] **PZwiki** — *Butchering* (revision 1435455; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Butchering&oldid=1435455. Accessed 2026-07-31. Fact-only source.
- [28] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0 — sandbox key defaults). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited. Community beliefs are quarantined above as circulating positions, not sourced to individual posts.

**Further Reading**

# Further Reading

- The Steam news API feed used to re-verify every primary above: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25
- The Indie Stone's Build 42 feature overview, linked from the 42.20 release notes: https://projectzomboid.com/blog/features-overview-build-42-20/ (bot-blocks automated checkers; verify in-browser).
- The official blog / Thursdoid archive, the canonical home of the announcements mirrored above: https://projectzomboid.com/blog/

# Related Documents

- `players-foundation` — the Players-track overview; the release, branch and save-compatibility spine this guide leans on.
- `players-traits-occupations` — full B41/B42 trait and occupation tables behind Instinct 2.
- `players-skills-xp` — the XP mathematics and skill rosters behind Instincts 2 and 3.
- `players-crafting-chains` — the chain map behind Instinct 3.
- `players-medical-moodles` — the moodle, medical and muscle-strain deep dive behind Instinct 4.
- `players-animals-husbandry` — the animal economy behind Instinct 5.
- `players-map-locations` — the town profiles and expansion geography behind Instincts 6 and 7.
- `players-vehicles` — travel and logistics across the enlarged map.
- `meta-style-guide` — the evidence, quarantine and build-tagging rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baseline to 42.21: reviewed against the 42.20.1, 42.20.3, 42.20.4 (incl. 41.78.21), 42.21 unstable and 42.21 stable Steam posts and the abridged TIS forum 42.21 changelist (42.20.2 reviewed; modding/debug-only). Updated save-safety, legacy41 hotfix, Welder confirmation (rename still unconfirmed), MP, cold-storage, map, basement/explosives and XXL-tree statements. Unchanged statements carried forward, not re-tested in-game. | — |
