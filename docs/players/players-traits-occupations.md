---
id: players-traits-occupations
title: "Traits and Occupations: Points, Rosters and the B42 Rework"
version: 0.1.0
status: in-review
confidence: Medium
category: Players
topic: "Traits & occupations"
build: both
document_type: reference
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [players-foundation, players-skills-xp, players-crafting-chains, players-animals-husbandry, meta-style-guide]
tags: [players, traits, occupations, character-creation, points, build-42, adaptive-traits, rebalance]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-traits-occupations |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 41.78.16, 42.20 |

# Executive Summary

Every Project Zomboid character starts as three decisions: an occupation, a set of positive traits you pay points for, and a set of negative traits that pay points back. This document is the Players-track deep dive on that system across both current builds. It carries the full occupation roster for Build 41.78 and Build 42, with point values and starting skills for each, side-by-side trait tables with per-build point costs, and a primary-sourced history of the Build 42 rework — which occupations are new, which were renamed (and when, patch by patch), and how the point economy itself was rebalanced [1] [8] [11].

The headline: Build 42 did not just add occupations, it re-priced the whole menu. Across the unstable cycle The Indie Stone ran explicit "Occupation Balance Pass" and "Trait Balance Pass" waves — most visibly in 42.16 and 42.17 — with the stated aim of making starting characters feel like "professionals rather than apprentices" [7] [8] [11]. Cheap point-farming negatives from B41 were cut hard (High Thirst fell from +6 to +2, Slow Healer from +6 to +3), weight traits stopped being purchasable, Lucky and Unlucky left the list, and a family of new crafting traits and occupations (Blacksmith, Welder, Tailor, Rancher, and more) arrived to serve the B42 crafting overhaul [2] [3] [11] [21] [22].

Document-level confidence is **Medium**. The rename-and-rebalance history rests on official patch notes and Thursdoids (High), but the roster tables themselves are cited from pzwiki revisions versioned against 42.18.0 and 42.19.0 and have not been individually re-verified in-game on 42.20 — and the wiki carries some internal naming inconsistencies that only an in-game check can settle [19] [20] [21] [22].

# Key Takeaways

- Character creation must end at zero points or better in both builds; occupations shift your starting budget anywhere from +8 (no occupation) to -8 (Veteran) *(cited)* *(both)*
- B41 offers 21 occupations plus Unemployed; the pinned B42 roster revision lists 24 occupations plus a Custom Occupation option *(cited)*
- Repairman→DIY Expert, Outdoorsman→Outdoorsy and Fisher→Angler are confirmed by the official 42.0.1 patch notes; Fire Officer→Firefighter, Angler→Fishing Guide and Wilderness Knowledge→Bushcrafter by the 42.16 notes; Crop Farmer/Livestock Farmer→Farmer/Rancher by the 42.13 notes *(cited)* *(B42)*
- "Pacifist→Reluctant Fighter" and "Asthmatic→Short of Breath" circulate in the community but are **not** fully confirmed — the first is only indirectly supported by primary notes, the second not at all — see the quarantine section *(community, unverified)*
- B42's new occupations include Blacksmith, Welder, Tailor (added mid-cycle in 42.8.1) and Rancher; Metalworker's slot and description carried over to Welder *(cited)* *(B42)*
- The B41 "free points" economy was deliberately squeezed in B42: famous point-printers like High Thirst (+6→+2), Slow Healer (+6→+3) and Smoker (+4→+3) now pay far less, and Obese/Underweight-family traits are no longer purchasable *(cited)*
- New B42 traits: Artisan, Mason, Inventive (42.4), Crafty (42.12), Tinkerer, Target Shooter (42.16), plus Whittler, Blacksmith Knowledge and Bushcrafter; Fast/Slow Metabolism replace direct weight-trait purchases *(cited)* *(B42)*
- Adaptive traits (strength, fitness and weight tiers) are gained and lost in play in both builds — and losing a negative trait never refunds the points you took for it *(cited)* *(both)*

# Purpose

This document answers the question every new run starts with: what exactly can I pick, what does it cost, and is the advice I remember from Build 41 still true? It exists so a player can compare the two builds' rosters line by line, understand which renames are officially documented and which are community folklore, and see how the point economy changed — without trusting an undated guide. It goes deeper than the `players-foundation` overview, which introduced the occupation-and-traits system at map level; here we carry the full tables and the patch-by-patch rework history.

# Scope

Covered: the complete occupation roster for B41.78 (pinned pzwiki revision 626093) and for B42 (pinned revision 1391359, versioned 42.18.0, cross-checked against the 42.16–42.20 patch notes); positive, negative and occupation-exclusive trait lists with point costs per build; the B42 rename/replace picture with primary-source verification status for each rename; the trait-point economy rebalance; and adaptive ("dynamic") traits gained or lost during play.

Not covered: per-skill XP mechanics and multipliers (see `players-skills-xp`), the crafting recipes each occupation unlocks (see `players-crafting-chains`), animal husbandry mechanics behind Rancher and Animal Care (see `players-animals-husbandry`), and per-trait combat math. Written spoiler-aware: no loot locations or story content, only character-creation facts.

# Definitions

- **Occupation** — the pre-outbreak job chosen at character creation; it sets starting skill levels, may grant a free occupation trait, and adds to or subtracts from the trait-point budget [19] [20].
- **Trait points** — the budget balanced at character creation: positive traits cost points, negative traits grant points, and the character can only spawn when the total is zero or higher [21] [22].
- **Occupation-exclusive trait** — a trait that cannot be bought with points and only arrives bundled with a specific occupation (e.g. Desensitized with Veteran) [22].
- **Adaptive trait** — a trait gained or lost during play as your strength, fitness or weight changes; the community also calls these "dynamic traits" [21] [22].
- **Hobby trait** — B41-era wiki term for purchasable traits that grant skill levels and recipes, mirroring what an occupation gives [21].
- **Free points** — community shorthand for negative traits whose in-play downside is (or was) trivial relative to the points they grant; central to the B41 meta and targeted by the B42 rebalance (see quarantine section).

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Roster and costs from pzwiki revisions pinned to 41.78.16 [19] [21] |
| B42 (stable) | Yes | 42.20 | Roster from a 42.18.0-versioned revision [20]; trait list from a 42.19.0-versioned revision [22]; the 42.19 and 42.20 patch notes contain no further roster or point changes, only fixes [15] [16] |

Both cited wiki revisions were re-checked on 2026-07-30 and are the newest revisions of their pages; no post-42.20 wiki update has landed yet [20] [22]. Values were not re-verified in-game on 42.20.

# Reference

## How the points system works (both builds)

Character creation combines a name, an occupation and traits; the character can only be created once "Points to Spend" is zero or positive [19] [21] [22]. Occupations move the starting budget: taking no occupation (B41 "Unemployed", B42 "Custom Occupation") grants 8 free points, while demanding occupations like Veteran start you at -8 and force you to take negative traits to climb back to zero [19] [20]. Starting skill levels matter beyond the levels themselves because any skill you begin above level 0 earns a permanent XP boost — the mechanics of that boost (and a known tooltip display bug) are covered in `players-foundation` and `players-skills-xp` [19] [20].

## B41 occupation roster (revision 626093, versioned 41.78.16)

All values below are from the pinned pre-B42 wiki revision [19]. Skills are listed as "skill level", highest first. *(B41)*

| Occupation | Points | Starting skills | Occupation trait |
|------------|-------:|-----------------|------------------|
| Unemployed | +8 | — | — |
| Burger Flipper | +2 | Cooking 2, Maintenance 1, Short Blade 1 | Cook |
| Carpenter | +2 | Carpentry 3, Short Blunt 1 | — |
| Doctor | +2 | First Aid 3, Short Blade 1 | — |
| Farmer | +2 | Farming 3 | — |
| Nurse | +2 | First Aid 2, Lightfooted 1 | — |
| Fire Officer | 0 | Axe 1, Fitness 1, Sprinting 1, Strength 1 | — |
| Lumberjack | 0 | Axe 2, Strength 1 | Axe Man |
| Construction Worker | -2 | Short Blunt 3, Carpentry 1 | — |
| Fisherman | -2 | Fishing 3, Foraging 1 | — |
| Security Guard | -2 | Sprinting 2, Lightfooted 1 | Night Owl |
| Chef | -4 | Cooking 3, Maintenance 1, Short Blade 1 | Cook |
| Electrician | -4 | Electrical 3 | — |
| Engineer | -4 | Carpentry 1, Electrical 1 | — |
| Mechanic | -4 | Mechanics 3, Short Blunt 1 | Amateur Mechanic |
| Park Ranger | -4 | Foraging 2, Trapping 2, Axe 1, Carpentry 1 | — |
| Police Officer | -4 | Aiming 3, Reloading 2, Nimble 1 | — |
| Repairman | -4 | Maintenance 2, Carpentry 1, Short Blunt 1 | — |
| Burglar | -6 | Lightfooted 2, Nimble 2, Sneaking 2 | Burglar |
| Fitness Instructor | -6 | Fitness 3, Sprinting 2 | Nutritionist |
| Metalworker | -6 | Metalworking 3 | — |
| Veteran | -8 | Aiming 2, Reloading 2 | Desensitized |

That is 21 occupations plus Unemployed [19].

## B42 occupation roster (revision 1391359, versioned 42.18.0)

The pinned B42 revision lists 24 occupations plus Custom Occupation [20]. Occupation names below follow the official patch notes where the wiki's display text lags behind: the 42.13 notes renamed Crop Farmer and Livestock Farmer to Farmer and Rancher, and the 42.16 notes renamed Fire Officer to Firefighter and Angler to Fishing Guide, while the wiki table still displays some earlier names [5] [8] [20]. The point costs match the 42.17 patch-note changes exactly (Doctor and Nurse to 0, Electrician and DIY Expert to -2, Rancher to 0, Welder to -4), which corroborates the revision against a primary source [11] [20]. *(B42)*

| Occupation | Points | Starting skills | Occupation trait |
|------------|-------:|-----------------|------------------|
| Custom Occupation | +8 | — | — |
| Burger Flipper | +2 | Cooking 2, Maintenance 1, Short Blade 1 | Keen Cook |
| Tailor | +2 | Tailoring 4 | — |
| Doctor | 0 | First Aid 6, Short Blade 1 | — |
| Farmer | 0 | Agriculture 4, Animal Care 1, Strength 1 | — |
| Firefighter | 0 | Axe 1, Fitness 1, Running 1, Strength 1 | — |
| Lumberjack | 0 | Axe 2, Maintenance 1, Strength 1 | Ax-pert |
| Nurse | 0 | First Aid 3, Fitness 1, Lightfooted 1 | Night Owl |
| Rancher | 0 | Animal Care 4, Butchering 3, Fitness 1 | — |
| Carpenter | -2 | Carpentry 4, Maintenance 1, Carving 1, Masonry 1, Short Blunt 1 | — |
| Chef | -2 | Cooking 4, Butchering 2, Maintenance 1, Short Blade 1 | Keen Cook |
| Construction Worker | -2 | Masonry 2, Short Blunt 2, Carpentry 1, Long Blunt 1, Maintenance 1 | — |
| DIY Expert | -2 | Maintenance 2, Carpentry 1, Masonry 1, Short Blunt 1 | Inventive |
| Electrician | -2 | Electrical 5 | — |
| Fishing Guide | -2 | Fishing 3, Butchering 1, Foraging 1 | — |
| Security Guard | -2 | Running 2, Lightfooted 1, Short Blunt 1 | Night Owl |
| Engineer | -4 | Carpentry 1, Electrical 1, Masonry 1 | — |
| Mechanic | -4 | Mechanics 4, Welding 1 | Vehicle Knowledge |
| Park Ranger | -4 | Foraging 1, First Aid 1, Knapping 1, Carving 1, Trapping 1 | Herbalist |
| Police Officer | -4 | Aiming 4, Nimble 1, Reloading 1 | — |
| Welder | -4 | Welding 4 | — |
| Blacksmith | -6 | Blacksmithing 4, Maintenance 1, Short Blunt 1 | Blacksmith Knowledge |
| Burglar | -6 | Lightfooted 2, Nimble 2, Sneaking 2 | Burglar |
| Fitness Instructor | -6 | Fitness 3, Running 2, Strength 1 | Nutritionist |
| Veteran | -8 | Aiming 2, Reloading 2 | Desensitized |

Roster notes verified against primaries: Tailor was not in the B42 launch roster — the 42.8.1 notes state "Added a Tailor profession" [3]. The 42.18 notes moved Park Ranger onto Carving (dropping Tracking) and Rancher onto Fitness (dropping Agriculture), both reflected in the pinned revision [13] [20]. The accompanying Thursdoid explains the Rancher change as better matching an athletic, physical job [12].

## The rename picture — what is confirmed, and how

Build 42's roster churned names several times, and each rename below is classed by its strongest evidence.

**Confirmed by explicit primary patch notes:**

- **Repairman → DIY Expert.** The 42.0.1 hotfix notes list "Repairer/Repairman to DIY Expert" in a block of renames [1]. The B42 roster keeps the identical icon asset (`profession_repairman2.png`) on the DIY Expert row [20].
- **Outdoorsman → Outdoorsy**, **Can't Read → Illiterate**, **Fisher → Angler**, plus reversions of the B42-launch names Nervous, Fear of Outdoors and Fear of Indoors back to Cowardly, Agoraphobic and Claustrophobic — all in the same 42.0.1 rename block [1].
- **Crop Farmer and Livestock Farmer → Farmer and Rancher.** Stated verbatim in the 42.13 notes [5]. The wiki roster table still displays the older names while its page links use the new ones [20].
- **Fire Officer → Firefighter** and **Angler → Fishing Guide** (so the B41 Fisherman's line went Fisher → Angler → Fishing Guide across the cycle), and the trait **Wilderness Knowledge → Bushcrafter** — all in the 42.16 notes [1] [8].

**Confirmed by revision comparison plus primary name attestation:**

- **Axe Man → Ax-pert.** The B41 revision lists Axe Man as Lumberjack's occupation trait; the B42 revision lists Ax-pert as Lumberjack's occupation-exclusive trait with the same icon asset (`trait_axeman.png`) and the same in-game description ("Better at chopping trees. Faster axe swing.") [21] [22]. The 42.13 notes independently attest the new name, fixing a bug where every player benefited from "Ax-pert" rather than only lumberjacks [5]. No single patch note states the rename; the identification rests on this asset-and-description continuity across the two pinned revisions.
- **Metalworker → Welder.** No rename note was found, but the B42 Welder row keeps Metalworker's icon asset (`profession_metalworker.png`) and the same in-game description about welding foraged metal into items and barricades, with the same shape of kit (Metalworking 3 became Welding 4) [19] [20]. Method: roster-revision comparison only — treat as strongly indicated rather than officially stated.
- **Cook → Keen Cook** and **Amateur Mechanic → Vehicle Knowledge** (occupation traits): same icon assets and effects across the two trait revisions, with the new names appearing throughout the B42 revision [21] [22].

**Not confirmed** — "Pacifist → Reluctant Fighter" and "Asthmatic → Short of Breath" are quarantined below with their evidence status.

## Trait roster and point costs — positives

Costs below are per pinned revision: B41 from revision 662897 (versioned 41.78.16) [21], B42 from revision 1442751 (versioned 42.19.0) [22]. A dash means the trait does not exist (or is not purchasable) in that build. More negative = more expensive.

| Trait | B41 cost | B42 cost | Change / note |
|-------|---------:|---------:|---------------|
| Adrenaline Junkie | -8 | -4 | Halved in B42 [21] [22] |
| Angler | -4 | -4 | — |
| Artisan | — | -2 | New in 42.4: Glassmaking 1, Pottery 1 [2] [22] |
| Athletic | -10 | -10 | — |
| Baseball Player | -4 | -4 | — |
| Blacksmith Knowledge | — | -6 | Purchasable in B42: Blacksmithing 2, Maintenance 1 [22] |
| Brave | -4 | -4 | — |
| Brawler | -6 | -6 | — |
| Bushcrafter | — | -8 | Renamed from Wilderness Knowledge in 42.16; Carving 1, Foraging 1, Knapping 1, Maintenance 1, faster fire-starting [8] [22] |
| Cat's Eyes | -2 | -3 | Cost raised in 42.16 [8] [22] |
| Cook / Keen Cook | -6 | -3 | Renamed; B42 adds Butchering 1 to Cooking 2 [21] [22] |
| Crafty | — | -3 | New in 42.12: 130% XP for crafting skills only; exclusive with Fast and Slow Learner [4] [22] |
| Dextrous | -2 | -2 | — |
| Eagle Eyed | -6 | -4 | Cheaper in B42 [21] [22] |
| Fast Healer | -6 | -6 | — |
| Fast Learner | -6 | -6 | — |
| Fast Reader | -2 | -2 | — |
| First Aider | -4 | -2 | Cost cut in 42.16 [8] [22] |
| Fit | -6 | -6 | — |
| Former Scout | -6 | -6 | B42 adds Fishing 1 and fishing-rod recipes (42.13) [5] [22] |
| Gardener | -4 | -2 | Cheaper in B42; grants Agriculture 1 [21] [22] |
| Graceful | -4 | -4 | — |
| Gymnast | -5 | -5 | — |
| Handy | -8 | -8 | B42 adds Carving 1 and Masonry 1 to the kit [21] [22] |
| Herbalist | -6 | -4 | Cheaper in B42 [21] [22] |
| Hiker | -6 | -5 | Cost cut in 42.19 to broaden access [14] [15] [22] |
| Hunter | -8 | -8 | B42 swaps Trapping for Tracking (42.19) and adds Butchering 1 [14] [15] [22] |
| Inconspicuous | -4 | -4 | — |
| Inventive | — | -2 | New in 42.4: lower skill requirements for researching/auto-learning recipes [2] [22] |
| Iron Gut | -3 | -2 | Cost cut in 42.16 [8] [22] |
| Keen Hearing | -6 | -6 | — |
| Light Eater | -4 | -2 | Cheaper in B42 [21] [22] |
| Low Thirst | -6 | -2 | Big cut — the mirror of High Thirst's nerf [21] [22] |
| Lucky | -4 | — | Listed as removed in the B42 revision [21] [22] |
| Mason | — | -2 | New in 42.4: Masonry 2 and brick/stone building recipes [2] [22] |
| Nutritionist | -4 | -2 | Cut in 42.17 — "primarily provides information" [10] [11] [22] |
| Organized | -6 | -4 | Cheaper in B42 [21] [22] |
| Outdoorsman / Outdoorsy | -2 | -2 | Renamed in 42.0.1; fire-starting perk moved to Bushcrafter and Former Scout in 42.16 [1] [8] [22] |
| Resilient | -4 | -4 | — |
| Runner | -4 | -4 | — |
| Sewer | -4 | -4 | — |
| Speed Demon | -1 | -1 | — |
| Stout | -6 | -6 | — |
| Strong | -10 | -10 | — |
| Target Shooter | — | -5 | New in 42.16: Aiming 1 [8] [22] |
| Thick Skinned | -8 | -8 | — |
| Tinkerer | — | -4 | New in 42.16: Maintenance 1 [8] [22] |
| Amateur Mechanic / Vehicle Knowledge | -5 | -3 | Renamed; purchasable version grants Mechanics 1 [21] [22] |
| Wakeful | -2 | -3 | Cost raised in 42.16 [8] [22] |
| Whittler | — | -2 | B42: Carving 2 plus bone-carving recipes [22] |

## Trait roster and point costs — negatives

| Trait | B41 grant | B42 grant | Change / note |
|-------|----------:|----------:|---------------|
| Agoraphobic | +4 | +4 | B42 launch briefly called it Fear of Outdoors; reverted in 42.0.1 [1] [22] |
| All Thumbs | +2 | +2 | — |
| Asthmatic | +5 | +5 | Name dispute — see Claim 2 [21] [22] |
| Claustrophobic | +4 | +4 | — |
| Clumsy | +2 | +2 | — |
| Conspicuous | +4 | +4 | — |
| Cowardly | +2 | +2 | B42 launch briefly called it Nervous; reverted in 42.0.1 [1] [22] |
| Deaf | +12 | +12 | — |
| Disorganized | +4 | +6 | Pays more in B42 [21] [22] |
| Fast Metabolism | — | +2 | New in B42: permanent weight-loss tendency, starts with Low Weight [22] |
| Fear of Blood | +5 | +5 | — |
| Feeble | +6 | +6 | B42 strength-tier naming is inconsistent on the wiki — see Risks [21] [22] |
| Hard of Hearing | +4 | +4 | — |
| Hearty Appetite | +4 | +4 | — |
| High Thirst | +6 | +2 | Was +1 earlier in the B42 cycle, nudged to +2 in 42.17 [11] [21] [22] |
| Illiterate | +8 | +10 | Grant raised in 42.16 [8] [22] |
| Obese | +10 | — | Adaptive-only in B42; no longer purchasable [21] [22] |
| Out of Shape | +6 | +6 | — |
| Overweight | +6 | — | Adaptive-only in B42 [21] [22] |
| Pacifist | +4 | +5 | In-game B42 name disputed — see Claim 1 [8] [21] [22] |
| Prone to Illness | +4 | +4 | — |
| Puny | — | +10 | B42 name for the -5 Strength tier B41 called Weak (same icon and effect) [21] [22] |
| Restless Sleeper | +6 | +6 | — |
| Short Sighted | +2 | +2 | — |
| Sleepyhead | +4 | +4 | — |
| Slow Healer | +6 | +3 | Halved in B42 [21] [22] |
| Slow Learner | +6 | +6 | — |
| Slow Metabolism | — | +2 | New in B42: permanent weight-gain tendency, starts with High Weight [22] |
| Slow Reader | +2 | +2 | — |
| Smoker | +4 | +3 | Was +2 earlier in the B42 cycle, nudged to +3 in 42.17 [11] [21] [22] |
| Sunday Driver | +1 | +1 | — |
| Thin-skinned | +8 | +8 | — |
| Underweight | +6 | — | Adaptive-only in B42 [21] [22] |
| Unfit | +10 | +10 | — |
| Unlucky | +4 | — | Listed as removed in the B42 revision, along with Lucky [21] [22] |
| Very Underweight | +10 | — | Adaptive-only in B42 [21] [22] |
| Weak | +10 | — | The B41 -5 Strength trait; its B42 successor is Puny [21] [22] |
| Weak Stomach | +3 | +2 | Grant cut in 42.16 [8] [22] |

## Occupation-exclusive traits

These arrive only with their occupation and cost nothing [21] [22]. *(both, names per build)*

| Trait (B41 / B42) | Occupation | What it does |
|-------------------|------------|--------------|
| Axe Man / Ax-pert | Lumberjack | 25% faster axe swings in combat and tree-felling [21] [22] |
| Burglar | Burglar | Hotwire vehicles; gentler forced entry on window locks [21] [22] |
| Cook / Keen Cook | Chef (B41 also Burger Flipper's version) | Cooking knowledge; B42 version improves foraging finds [21] [22] |
| Desensitized | Veteran | No panic from any source except night terrors; 42.16 added immunity to the B42 Discomfort effect [8] [21] [22] |
| Night Owl | Security Guard (B42 also Nurse) | Better recovery while sleeping and extra alertness [20] [21] [22] |
| Amateur Mechanic / Vehicle Knowledge | Mechanic | Mechanics 3 and repair of all vehicle types without magazines [21] [22] |
| Blacksmith Knowledge | Blacksmith (B42) | Anvil use; Blacksmithing 2, Maintenance 1 [22] |

## The point-economy rebalance, patch by patch

The B42 cycle rebalanced the economy in documented waves. The 42.16 "Trait Balance Pass" raised costs for Cat's Eyes and Wakeful, cut costs for First Aider and Iron Gut, raised the grants of Illiterate and one combat-XP negative, and cut Weak Stomach's grant [8]. The companion Thursdoid framed the goal: costs adjusted "to better reflect their value in relation to current gameplay features" [7]. The 42.17 notes then re-priced occupations (Doctor, Nurse and Rancher to 0; Electrician and DIY Expert to -2; Welder to -4) and nudged Nutritionist to -2, High Thirst from +1 to +2 and Smoker from +2 to +3 [11] — those last two numbers reveal how far below their B41 values (+6 and +4) these ex-favourites had already been pushed at B42's launch [11] [21]. Even before launch, a 42-unstable tester quoted in the Hallodoid Thursdoid singled the change out: "smoker no longer OP" [18]. A related exploit was patched at 42.16.1, where Park Ranger's bundled Herbalist trait was incorrectly refunding points [9].

## Adaptive ("dynamic") traits — gained and lost in play

Both builds tie a ladder of traits to your strength, fitness and weight, gained and lost as those change; losing a negative trait this way never refunds the points it granted at creation [21] [22]. The fitness ladder is identical across builds: Unfit at levels 0–1, Out of Shape at 2–4, nothing at 5, Fit at 6–8, Athletic at 9–10 [21] [22]. The strength ladder works the same way, but B42 renamed its bottom tiers (B41's Weak/Feeble pair becomes B42's Puny/Weak per the adaptive-trait section of the pinned revision) [21] [22]. Weight bands also match across builds — Emaciated below 50 kg, then the underweight tiers up to 75, an ideal band at 76–85, and overweight tiers above 85 — but B42 renames the in-play weight traits to Low Weight, Very Low Weight, High Weight and Very High Weight [22]. The name "Low Weight" is primary-attested: a 42.14 fix note restores characters starting "with 'Low Weight' trait" to a 70 kg spawn weight [6].

B42 changes the entry points into this system. You can no longer buy Obese, Overweight, Underweight or Very Underweight directly; instead the new Fast Metabolism and Slow Metabolism negatives (+2 each) start you with Low Weight or High Weight respectively and add a permanent metabolic drift [22]. Beyond the ladders, at least one B42 trait is gainable mid-run from the world: a 42.7 fix note stopped characters gaining the Herbalist trait repeatedly from re-reading the Herbalist magazine — confirming the magazine grants the trait in play [17]. One planned negative, Motion Sensitive, was added in 42.13 and then disabled in 42.14 pending a health-balance overhaul; the pinned revision lists it as removed/future [5] [6] [22].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42 *(B42)* |
|------|---------------------|------------------|
| Roster size | 21 occupations + Unemployed [19] | 24 occupations + Custom Occupation per the pinned revision [20] |
| New occupations | — | Blacksmith, Welder, Rancher, Tailor (42.8.1), Fishing Guide/Farmer refreshes [3] [5] [8] [20] |
| Departed names | Metalworker, Repairman, Farmer (as sole farming job), Fisherman [19] | Welder carries Metalworker's kit; DIY Expert is the renamed Repairman (42.0.1); farming splits into Farmer and Rancher (named at 42.13) [1] [5] [20] |
| Occupation costs | Doctor and Nurse +2; Electrician -4 [19] | Doctor and Nurse 0 (but Doctor jumps to First Aid 6); Electrician -2 with Electrical 5 — deeper skills, tighter costs after 42.16–42.17 [8] [11] [20] |
| Occupation traits | Cook, Axe Man, Amateur Mechanic among the grants [19] [21] | Keen Cook, Ax-pert, Vehicle Knowledge, Inventive (DIY Expert), Herbalist (Park Ranger), Blacksmith Knowledge (Blacksmith) [20] [22] |
| New purchasable traits | — | Artisan, Inventive, Mason (42.4), Crafty (42.12), Tinkerer, Target Shooter (42.16), Whittler, Bushcrafter, Blacksmith Knowledge [2] [4] [8] [22] |
| Removed traits | Lucky -4, Unlucky +4 available [21] | Both listed as removed [22] |
| Point-printer negatives | High Thirst +6, Slow Healer +6, Smoker +4, weight traits purchasable up to +10 [21] | High Thirst +2, Slow Healer +3, Smoker +3, weight traits adaptive-only; Fast/Slow Metabolism (+2) are the new entry points [11] [22] |
| Utility positives | Low Thirst -6, Light Eater -4, First Aider -4, Nutritionist -4 [21] | Low Thirst -2, Light Eater -2, First Aider -2, Nutritionist -2 — information/comfort traits got cheap [8] [11] [22] |
| Adaptive traits | Strength/fitness/weight ladders; B41 names (Weak, Feeble, Overweight, Obese...) [21] | Same ladders; renamed tiers (Puny, Weak, High Weight, Low Weight...) plus metabolism drift traits [6] [22] |
| Skill vocabulary in rosters | Sprinting, Farming, Metalworking [19] | Running, Agriculture, Welding, plus crafting skills (Masonry, Carving, Knapping, Blacksmithing) and animal skills (Animal Care, Butchering) threaded through rosters [20] |

One line: B41's roster is a stable menu with famous point loopholes; B42's is a re-priced, crafting-aware menu that pays you less for fake hardship and charges you less for convenience — and several of its names changed more than once on the way to stable [1] [8] [11].

# Practical Guidance

- **Check the build before copying any character build.** A B41 guide's "free points" list (High Thirst, Slow Healer, Smoker, Obese...) collapses on B42 — those five points-printers now pay +2/+3 or cannot be taken at all. Rebuild your negative-trait stack from the B42 column above.
- **On B42, cheap utility is the new meta lever.** First Aider, Gardener, Iron Gut, Light Eater, Low Thirst and Nutritionist all cost just -2 now; two or three modest negatives cover several of them.
- **Match the occupation to the B42 system you want to play.** Blacksmith, Welder and Tailor exist to front-load the crafting chains, and Rancher front-loads Animal Care and Butchering — see `players-crafting-chains` and `players-animals-husbandry` for where those skills lead.
- **Occupation-exclusive traits are the real product.** Burglar's hotwiring, Veteran's Desensitized and Mechanic's Vehicle Knowledge cannot be bought with points in either build; if you want the effect, you must take the job.
- **Watch the zero-point sweet spots on B42.** Doctor, Farmer, Firefighter, Lumberjack, Nurse and Rancher all cost nothing after the 42.16–42.17 re-pricing, several with 4–6 levels in their core skill — historically strong openings for new players.
- **Mind adaptive traits over a long run.** Strength and fitness tiers move with training, weight tiers move with diet, and dropping a creation-time negative refunds nothing — treat adaptive negatives as a loan you repay in gameplay, not points.
- **Names in older B42 guides may be one rename behind.** "Crop Farmer", "Livestock Farmer", "Angler" (as an occupation) and "Fire Officer" are all pre-rename labels for Farmer, Rancher, Fishing Guide and Firefighter.

# Common Pitfalls & Troubleshooting

- **"I can't find Repairman / Metalworker / Fisherman on B42."** Working as documented: DIY Expert is the renamed Repairman [1], Welder occupies Metalworker's role [19] [20], and the fishing occupation is now Fishing Guide after two renames [1] [8].
- **"A guide told me to take Obese for +10 points."** B41 advice. On B42 the weight traits are adaptive-only; the closest purchasable is Slow Metabolism at +2 [21] [22].
- **"Lucky isn't in my trait list."** On B42 the pinned revision lists Lucky and Unlucky as removed; on B41 they exist but are single-player only [21] [22].
- **"Everyone in our MP game swings axes faster."** That was a real 42-unstable bug — every player benefited from Ax-pert regardless of occupation — fixed in 42.13 [5].
- **"Park Ranger seems to give points back for its Herbalist trait."** An exploit patched at 42.16.1; post-42.16.1 values are what the tables above show [9].
- **"My Organized trait does nothing on our server."** Organized/Disorganized had no effect in multiplayer until fixed in the 42.13.1 hotfix wave — and a related corpse-container fix landed as late as 42.20 [16].
- **"The XP percentages at creation look different from this doc."** Known display issue tracked in `players-foundation` (its Claim 1); the underlying boost tiers are unchanged [19] [20].

# Community Notes & Unverified Claims

## Claim 1 — B42 renamed Pacifist to Reluctant Fighter

- **Claim:** Community guides and forum threads state that B41's Pacifist trait is called Reluctant Fighter in Build 42.
- **Why unverified:** No patch note stating the rename was found. The evidence is indirect but real: the 42.16 notes list "Increased bonus for Illiterate and Reluctant Fighter" [8], and the pinned wiki revision shows the Pacifist row moving from +4 to exactly +5 with no other combat-XP negative present [21] [22] — yet that same 42.19.0-versioned revision still titles the row "Pacifist", so the primary name attestation and the pinned fact source disagree.
- **Confidence:** Medium. A primary source attests the name Reluctant Fighter and its point change maps cleanly onto the Pacifist row, but the rename itself is inferred, not stated, and the wiki has not adopted it.

## Claim 2 — B42 renamed Asthmatic to Short of Breath

- **Claim:** The rename circulates alongside Claim 1 in community trait guides and Reddit threads comparing B41 and B42 trait lists.
- **Why unverified:** No primary source found — the name "Short of Breath" appears nowhere in the 600+ official announcements checked for this document, and the pinned 42.19.0-versioned trait revision still lists Asthmatic at +5 with unchanged effects [22].
- **Confidence:** Low. Both the primary record and the pinned fact source contradict the claim as of 42.19–42.20; it may stem from a mod, a very early unstable build, or confusion with the 42.0.1 rename wave [1].

## Claim 3 — B41 lets you stack "free points" from negatives that barely matter, and B42 deliberately ended it

- **Claim:** Community build guides hold that a B41 character can bank roughly 20+ points from negatives with trivial in-play impact (Slow Healer, High Thirst, Smoker, weight traits, Sunday Driver...) and that B42's pricing was designed to kill the pattern.
- **Why unverified:** The individual numbers are fully cited above [11] [21] [22], and the direction of intent is supported by dev framing ("costs adjusted to better reflect their value" [7]) and a dev-published tester quote [18] — but "barely matter" is a balance judgement and "deliberately ended it" attributes a specific motive no primary source states outright.
- **Confidence:** Medium. The mechanical delta is primary-verifiable; only the aggregate judgement and the motive are community synthesis.

# Risks & Caveats

- **No first-hand 42.20 verification.** Every roster value here traces to pinned wiki revisions versioned 42.18.0/42.19.0 plus patch notes through 42.20; the 42.19–42.20 notes show only fixes, not roster changes [15] [16], but a stable-branch hotfix could re-price anything.
- **Wiki-internal naming inconsistencies.** The pinned B42 trait revision names the -2 Strength tier "Feeble" in its negatives table but "Weak" in its adaptive-traits section, and lists Night Owl both as purchasable-without-cost and as occupation-exclusive; the page itself carries a formatting-improvement banner [22]. In-game checks are the only resolution.
- **Display names vs patch-note names.** The pinned occupation revision's display text ("Crop Farmer", "Livestock Farmer", "Fire Officer") lags the 42.13/42.16 renames its own page links reflect [5] [8] [20]. This document follows the patch notes; the in-game 42.20 labels have not been read directly.
- **Occupation-count discrepancy with the parent document.** `players-foundation` states 23 occupations plus Custom Occupation for the same pinned revision; this document counts 24 rows. A human should recount revision 1391359 [20].
- **Two renames rest on inference.** Metalworker→Welder (roster comparison only) and Axe Man→Ax-pert (asset/description continuity plus name attestation) are argued, not quoted, from primaries [5] [19] [20] [21] [22].
- **Steam announcement mirrors.** Primary citations use Steam announcement mirrors of Indie Stone posts per project policy; those hosts bot-block automated link checkers.

# Verification Steps

1. **Re-check the pinned revisions are still current:** query `https://pzwiki.net/w/api.php?action=query&titles=Occupation%7CTrait&prop=revisions&rvprop=ids&format=json` and compare the top revision ids against 1391359 and 1442751.
2. **Recount the B42 roster (and settle the 23-vs-24 question):** open a new-character screen on 42.20 and count the occupation list, or count the table rows at the pinned revision URL for [20].
3. **Settle Claims 1 and 2 in-game:** on 42.20, open the negative-trait list and record the exact names and point values of the +5 combat-XP-penalty trait and the +5 endurance-loss trait.
4. **Spot-check the economy numbers:** compare High Thirst, Slow Healer, Smoker and Low Thirst in-game against the table above; any drift means a post-42.19 rebalance this document has not captured.
5. **Confirm the rename notes at source:** open the 42.0.1, 42.13.0 and 42.16.0 announcements ([1], [5], [8]) and locate the rename lines quoted here.
6. **Test one adaptive trait:** in a sandbox or debug game, raise fitness past 6 and confirm the Fit trait appears without a point refund or cost.

# Open Questions

- Is the in-game 42.20 label Pacifist or Reluctant Fighter (Claim 1)? One character-creation screenshot resolves it.
- Does any 42.20 in-game trait carry the name Short of Breath (Claim 2)?
- Are the in-game 42.20 occupation labels Farmer/Rancher/Fishing Guide/Firefighter, as the patch notes imply, or do any pre-rename labels survive [5] [8]?
- What is the exact 42.20 name of the -2 Strength adaptive tier (Feeble vs Weak) given the wiki's internal inconsistency [22]?
- Will the announced Build 42 Support Update touch trait or occupation balance again? Watch the Thursdoid feed.
- Does the pinned B42 roster's 24-row count match the shipped 42.20 list, and the parent document's count of 23?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Hotfix 42.0.1 - Unstable Release* (Steam announcement, 2024-12-20; trait/occupation rename block). https://steamcommunity.com/games/108600/announcements/detail/1786573930668296. Accessed 2026-07-30.
- [2] **The Indie Stone** — *42.4.0 UNSTABLE Released* (Steam announcement, 2025-03-04; Mason, Inventive and Artisan traits added). https://steamcommunity.com/games/108600/announcements/detail/1792751526173735. Accessed 2026-07-30.
- [3] **The Indie Stone** — *42.8.1 UNSTABLE Released* (Steam announcement, 2025-05-20; "Added a Tailor profession"). https://steamcommunity.com/games/108600/announcements/detail/1799817379626544. Accessed 2026-07-30.
- [4] **The Indie Stone** — *42.12.0 UNSTABLE Released* (Steam announcement, 2025-09-25; Crafty trait added at 3 points). https://steamcommunity.com/games/108600/announcements/detail/1811772772244324. Accessed 2026-07-30.
- [5] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11; Farmer/Rancher renames, Ax-pert fix, Motion Sensitive added). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972. Accessed 2026-07-30.
- [6] **The Indie Stone** — *Build 42.14.0 Unstable Released* (Steam announcement, 2026-02-16; Motion Sickness trait disabled; Low Weight spawn fix). https://steamcommunity.com/games/108600/announcements/detail/1824644522845673. Accessed 2026-07-30.
- [7] **The Indie Stone** — *Balancing Time* (Thursdoid, Steam announcement, 2026-03-30; occupation/trait rework intent). https://steamcommunity.com/games/108600/announcements/detail/1828441623110846. Accessed 2026-07-30.
- [8] **The Indie Stone** — *Build 42.16.0 Unstable Released* (Steam announcement, 2026-03-31; Occupation and Trait Balance Pass, renames). https://steamcommunity.com/games/108600/announcements/detail/1828441623111900. Accessed 2026-07-30.
- [9] **The Indie Stone** — *42.16.1 UNSTABLE Hotfix Released* (Steam announcement, 2026-04-02; Park Ranger Herbalist point exploit fix). https://steamcommunity.com/games/108600/announcements/detail/1828894815557868. Accessed 2026-07-30.
- [10] **The Indie Stone** — *Location, Location* (Thursdoid, Steam announcement, 2026-04-17; 42.17 occupation/trait tweak rationale). https://steamcommunity.com/games/108600/announcements/detail/1830163047261202. Accessed 2026-07-30.
- [11] **The Indie Stone** — *Build 42.17.0 Unstable Released* (Steam announcement, 2026-04-20; occupation and trait point updates). https://steamcommunity.com/games/108600/announcements/detail/1830163047266254. Accessed 2026-07-30.
- [12] **The Indie Stone** — *SPRING IS HERE* (Thursdoid, Steam announcement, 2026-05-08; Rancher fitness rationale). https://steamcommunity.com/games/108600/announcements/detail/1832065502816211. Accessed 2026-07-30.
- [13] **The Indie Stone** — *Build 42.18.0 Unstable Released* (Steam announcement, 2026-05-11; Park Ranger and Rancher skill changes). https://steamcommunity.com/games/108600/announcements/detail/1832065502820909. Accessed 2026-07-30.
- [14] **The Indie Stone** — *REINFORCING THE BARRICADES* (Thursdoid, Steam announcement, 2026-05-29; Hunter and Hiker trait tweaks). https://steamcommunity.com/games/108600/announcements/detail/1833968530890581. Accessed 2026-07-30.
- [15] **The Indie Stone** — *Build 42.19.0 Unstable Released* (Steam announcement, 2026-06-01; Hunter/Hiker changes, DIY Expert Inventive fix). https://steamcommunity.com/games/108600/announcements/detail/1833968530897275. Accessed 2026-07-30.
- [16] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; trait-related fixes only). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [17] **The Indie Stone** — *42.7.0 UNSTABLE Released* (Steam announcement, 2025-04-07; Herbalist magazine trait-gain fix). https://steamcommunity.com/games/108600/announcements/detail/1795917897452371. Accessed 2026-07-30.
- [18] **The Indie Stone** — *Hallodoid* (Thursdoid, Steam announcement, 2024-11-01; pre-release tester feedback on trait balance). https://steamcommunity.com/games/108600/announcements/detail/6146943657173915715. Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [19] **PZwiki** — *Occupation* (revision 626093, 2024-11-14; versioned 41.78.16 — B41 roster). https://pzwiki.net/w/index.php?title=Occupation&oldid=626093. Accessed 2026-07-30. Fact-only source.
- [20] **PZwiki** — *Occupation* (revision 1391359, 2026-05-23; page versioned 42.18.0 — B42 roster; newest revision as of access). https://pzwiki.net/w/index.php?title=Occupation&oldid=1391359. Accessed 2026-07-30. Fact-only source.
- [21] **PZwiki** — *Trait* (revision 662897, 2024-12-13; versioned 41.78.16 — B41 trait list, captured four days before B42 unstable launched). https://pzwiki.net/w/index.php?title=Trait&oldid=662897. Accessed 2026-07-30. Fact-only source.
- [22] **PZwiki** — *Trait* (revision 1442751, 2026-07-22; page versioned 42.19.0 — B42 trait list; newest revision as of access). https://pzwiki.net/w/index.php?title=Trait&oldid=1442751. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited.

**Further Reading**

# Further Reading

- The Steam news API feed used to source and verify every patch note above: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0
- The official blog / Thursdoid archive: https://projectzomboid.com/blog/ (bot-blocks automated checkers; browse manually).
- `players-foundation` in this knowledge base for the XP-boost tiers and the character-creation display bug this document deliberately does not restate.

# Related Documents

- `players-foundation` — parent overview; this document expands its character-creation section into full tables.
- `players-skills-xp` — what those starting skill levels are worth in XP terms.
- `players-crafting-chains` — where Blacksmith, Welder, Tailor and the crafting traits actually lead.
- `players-animals-husbandry` — the systems behind Rancher, Animal Care and Butchering.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
