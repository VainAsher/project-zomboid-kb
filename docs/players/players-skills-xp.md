---
id: players-skills-xp
title: "Skills and XP: Levelling, Multipliers and the B42 Skill Roster"
version: 0.2.0
status: in-review
confidence: Medium
category: Players
topic: "Skills & XP"
build: both
document_type: reference
created: 2026-07-30
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-traits-occupations, players-crafting-chains, players-animals-husbandry, meta-style-guide]
tags: [players, skills, xp, levelling, skill-books, multipliers, passive-skills, crafting-skills, build-42, sandbox-options]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-skills-xp |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 |

# Executive Summary

This document is the Players-track deep dive on the skill system: how experience points (XP) turn into skill levels, why Strength and Fitness follow a different scale from everything else, how the starting-level XP boost quietly decides which skills are worth levelling for the rest of a run, how skill books multiply your training rate in two-level bands, and exactly which skills exist on each build. Its parent, `players-foundation`, sketches the system in two paragraphs; this document carries the full numbers and the full per-build roster.

The headline change between builds is the roster itself. Build 41.78 has 26 skills in six categories [5]. The Build 42-era page for the same system lists 35, adding seven crafting skills (Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding in place of Metalworking), three animal-economy skills (Animal Care, Butchering, Tracking), and renaming Farming to Agriculture and Sprinting to Running [4] [9] [11]. The levelling mathematics — per-level XP requirements, the 25%/100%/133%/166% starting-level multipliers, and the ×3 to ×16 skill-book bands — are documented identically for both builds, but the wiki's figures were established on 41.78.16 and have not been republished as a verified B42 table [4] [5] [6].

Document confidence is **Medium**: the release spine and one 42.20 patch fact are primary-sourced, but nearly every hard number rests on pzwiki page revisions versioned against 41.78.16 or unstable-era 42.x, none individually re-verified in-game on 42.20.

# Key Takeaways

- Skills level from 0 to 10; each level needs its own (non-cumulative) XP amount, and a regular skill costs 32,775 XP total to master while a passive skill (Strength/Fitness) costs 487,500 *(cited, figures stated for 41.78.16)* *(both)*
- The starting-level XP boost is permanent: a skill you start at level 0 earns only 25% XP for the whole run, while starting levels 1, 2 and 3+ earn 100%, 133% and 166% — a level-1 start is roughly four times the XP rate of a level-0 start *(cited)* *(both)*
- Strength and Fitness are exempt from the starting-level boost system entirely *(cited)* *(both)*
- Skill books multiply XP in two-level bands — ×3 (levels 1–2), ×5 (3–4), ×8 (5–6), ×12 (7–8), ×16 (9–10) — and reading the right volume before grinding is the single biggest levelling lever *(cited)* *(both)*
- B41 only has skill books for crafting and survivalist skills; the B42-era book roster covers 24 skills, including first-ever books for Aiming, Reloading, Long Blade and Maintenance *(cited)* *(B42)*
- B42 adds nine genuinely new skills and renames three: Farming→Agriculture, Metalworking→Welding, Sprinting→Running (the internal IDs keep the old names) *(cited)* *(B42)*
- Brewing is a new B42 crafting *system*, not a skill — no Brewing skill exists in the cited roster *(cited)* *(B42)*
- The character-creation screen reportedly displays wrong boost percentages (+75/+100/+125 instead of the real 100/133/166) *(community, unverified)*
- Sandbox options include an XP Multiplier (0.001–1000, default 1) and a separate toggle for whether it touches passive skills, off by default *(cited, B41-versioned page)*

# Purpose

This document answers the questions a player asks the moment they open the skills panel: how much XP does the next level actually need, why does my carpentry crawl while my friend's flies, which books should I read before I grind, what did Build 42 do to the skill list, and can I tune XP rates in sandbox? It exists so that levelling decisions — at character creation and mid-run — can be made from numbers rather than folklore.

# Scope

Covered: the complete skill roster for B41.78 and B42.20-era pages, as build-tagged tables; per-level XP requirements including the passive Strength/Fitness scale; the permanent starting-level XP boost multipliers and their exceptions; skill-book mechanics, volume bands and per-build book coverage; how occupations and traits feed starting levels, at overview depth only; B42's new crafting and animal skills and the three renames; and sandbox XP options at overview level.

Not covered: per-occupation and per-trait tables (see `players-traits-occupations`), per-skill levelling routes and recipe unlocks (see `players-crafting-chains` and `players-animals-husbandry`), combat damage math beyond what defines a skill's effect, and multiplayer server XP configuration (Admins track). Spoiler-aware: no loot locations or story content appear here.

# Definitions

- **XP (experience points)** — the per-skill points earned by performing that skill's activity; accumulating enough XP raises the skill level [4] [5].
- **Regular skill** — any skill outside the passive category; all share one XP-requirement scale [5].
- **Passive skill** — Strength or Fitness, the two-skill category with a far larger XP scale and special boost rules [5].
- **XP boost (starting-level boost)** — the permanent XP-rate multiplier a skill receives based on the level it had when the character was created [5] [7].
- **Skill book** — a readable item granting a temporary XP multiplier for one skill across a specific two-level band [6].
- **Skill ID** — the internal name a skill carries in game data, which several renamed B42 skills keep from their old display names [9] [10] [11].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | XP tables, boost multipliers and the 26-skill roster cited from a pzwiki revision explicitly versioned 41.78.16 [5] |
| B42 (stable) | Yes | 42.20; patch notes re-read through 42.21 | Roster and mechanics cited from pzwiki revisions versioned 42.3.1–42.19.0; the 42.20-specific fact is the skill-book XP fix in the release notes, and 42.21 adds only small fix notes (see Reference) [1] [4] [6] [7] [19] [20] [21] |

The Skill page revision used for B42 facts still carries an editors' banner stating its categorisation is Build 41-based, and its XP table is labelled for 41.78.16 even on the B42-era revision — no independently verified B42 XP table has been published [4]. Treat every number here as "documented for 41.78, believed unchanged on 42.20" unless tagged otherwise.

Revision 0.2.0 (2026-10-07) re-read the 42.20.1, 42.20.2, 42.20.3 and 42.20.4 hotfix notes [15] [16] [17] [18], the 42.21 unstable and stable announcements [19] [20] and the abridged ("selected") TIS forum 42.21 changelist [21]. The four 42.20.x hotfix notes cover multiplayer, memory, security and mod-tooling fixes and list no skill, XP-requirement, multiplier or roster changes [15] [16] [17] [18]. Statements not named as 42.21-affected are carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found in those notes; this is a patch-notes review, not an in-game re-test [21].

# Reference

## Levelling: from XP to skill levels

Every skill runs from level 0 to level 10, and the skills panel (press `L`, or open the health panel and pick the skills tab) shows current levels, with a hover tooltip revealing the XP still needed [4] [5]. XP arrives from performing the matching activity — sawing logs for carpentry, landing shots for aiming, casting a line for fishing — and each successive level demands more XP than the one before [4] [5].

Requirements are per-level, not running totals: the game asks for the level-4 chunk on its own after you have paid for levels 1–3 [5]. The table below restates the wiki's per-level figures (stated for build 41.78.16) alongside the cumulative cost, which this document computed by summation [4] [5]:

| Level reached | Regular skill XP | Regular cumulative | Passive skill XP | Passive cumulative |
|---------------|------------------|--------------------|------------------|--------------------|
| 1 | 75 | 75 | 1,500 | 1,500 |
| 2 | 150 | 225 | 3,000 | 4,500 |
| 3 | 300 | 525 | 6,000 | 10,500 |
| 4 | 750 | 1,275 | 9,000 | 19,500 |
| 5 | 1,500 | 2,775 | 18,000 | 37,500 |
| 6 | 3,000 | 5,775 | 30,000 | 67,500 |
| 7 | 4,500 | 10,275 | 60,000 | 127,500 |
| 8 | 6,000 | 16,275 | 90,000 | 217,500 |
| 9 | 7,500 | 23,775 | 120,000 | 337,500 |
| 10 | 9,000 | 32,775 | 150,000 | 487,500 |

The passive category — Strength and Fitness only — is the outlier by design: its level 1 alone costs twenty times a regular skill's level 1 (1,500 vs 75 XP), and mastery costs roughly fifteen times as much overall [5]. The same figures appear unchanged on the B42-era revision of the page, still labelled as 41.78.16 values [4].

## The starting-level XP boost

The occupation and traits picked at character creation set each skill's initial level, and that initial level locks in a permanent XP-rate multiplier for the skill [5] [7] [8]. Both the B41 page revision and the B42-era Trait and Occupation revisions document the same actual rates [5] [7] [8]:

| Starting level | Actual XP earned | Rate relative to a level-0 skill |
|----------------|------------------|----------------------------------|
| 0 | 25% | ×1 |
| 1 | 100% | ×4 |
| 2 | 133% | ×5.32 |
| 3 or higher | 166% | ×6.64 |

In other words, a skill you never invested in at creation earns a quarter-rate trickle forever, while one point at creation quadruples its lifetime XP rate [5] [7]. The skills panel encodes the tier in the colour of the skill's name — gold for the top boost, then white, light grey, and dark grey for an unboosted skill [5].

Documented exceptions [4] [5]:

- Strength and Fitness sit outside the boost system altogether — their XP rate is identical whatever level you start them at [5].
- The Running skill (Sprinting on B41) uses its own ladder: 100%, 125%, 133% and 166% for starting levels 0, 1, 2 and 3+, so it never suffers the 25% penalty [4] [5].
- Aiming and Reloading take a flat ×0.37037 hit to XP gain once the character reaches level 5 in the respective skill [4] [5].

The percentages the creation screen *displays* are reportedly different from these actual rates — that discrepancy is quarantined as Claim 1 below.

## Skill books: the two-level multiplier bands

Skill books are single-use readables that multiply XP earned in one skill, but only while the character is inside the volume's two-level band [6]. Five volumes exist per book-supported skill, each unlocking a successive two-level band from 1–2 (Volume I) up to 9–10 (Volume V) [6]. A volume cannot be opened below its band ("Skill level too low to read" appears in red), while reading one above your band wastes it — the character gains no boost [6]. The multiplier builds as you read: every 10% of pages completed grants 10% of the volume's maximum, sub-1.0 intermediate values are ignored, and the boost expires once the band's top level is reached [5] [6]. Boosts for several different skills can run at the same time, and active ones are marked by animated arrows in the skills panel, with the exact multiplier on hover [5] [6].

| Volume | Band (levels) | Max multiplier | Pages | Band XP at full multiplier (regular skill) |
|--------|---------------|----------------|-------|--------------------------------------------|
| I | 1–2 | ×3 | 220 | 75 instead of 225 |
| II | 3–4 | ×5 | 260 | 210 instead of 1,050 |
| III | 5–6 | ×8 | 300 | 562.5 instead of 4,500 |
| IV | 7–8 | ×12 | 340 | 875 instead of 10,500 |
| V | 9–10 | ×16 | 380 | 1,031.25 instead of 16,500 |

Multiplier and page figures are the wiki's standard values (it notes multipliers can vary by topic); the final column is this document's arithmetic combining the band multiplier with the XP table above [5] [6]. Higher volumes have more pages and take proportionally longer to read [6].

Coverage differs sharply by build. On B41, only the crafting and survivalist categories have books at all — eleven skills in total under that revision's grouping *(B41)* [5]. The B42-era Skill book page lists books for 24 skills: the whole crafting family (including all seven new B42 crafting skills), Agriculture, Animal Care, Butchering, Tracking, the survivalist set, and — new territory for the series — Aiming, Reloading, Long Blade and Maintenance *(B42)* [6]. No books exist for passive or agility skills on either build, nor for melee skills other than Long Blade and Maintenance *(B42)* [6]. Book item IDs preserve renamed skills' old identities — Agriculture volumes are `Base.BookFarming1` through `Base.BookFarming5` *(B42)* [6].

One 42.20-stable primary fact belongs here: the release patch notes fix the XP boost from skill books "not being calculated properly in some cases", so book behaviour on 42.20 differs from late-unstable builds in unspecified edge cases *(B42)* [1].

The 42.21 stable release (2026-09-28) adds three small fix notes in this area *(B42)* [20]. The forum changelist's multiplayer list records that Nimble XP was not being granted while in combat stance in multiplayer, now fixed [21]. Its split-screen list records that read-book status and XP boosts were being shared incorrectly between local players, now fixed, and the unstable announcement repeats that point [19] [21]. Its singleplayer list records a fix for PerkLog.txt not recording perk changes [21]. The changelist as retrieved lists no change to XP requirements, multipliers or the skill roster; it is abridged, so that is an absence in a partial list, not a confirmation [21].

## Where starting levels come from: occupations and traits

Occupations grant the larger starting-level packages, positive traits add smaller ones, and both feed the boost table above — which is why the wiki frames creation choices as permanent XP-rate decisions [5] [7] [8]. Two traits modify XP rates globally rather than via starting levels: Fast Learner raises a skill's XP rate to 130% and Slow Learner lowers it to 70% [11]. The full per-occupation and per-trait rosters, point costs and B41/B42 roster differences live in `players-traits-occupations`; this document deliberately stops at the mechanism.

## The skill roster, per build

Build 41.78.16 has 26 skills in six categories *(B41)* [5]:

| Category *(B41)* | Skills | Count |
|------------------|--------|-------|
| Passive | Fitness, Strength | 2 |
| Agility | Lightfooted, Nimble, Sneaking, Sprinting | 4 |
| Combat | Axe, Long Blunt, Short Blunt, Long Blade, Short Blade, Spear, Maintenance | 7 |
| Crafting | Carpentry, Cooking, Farming, First Aid, Electrical, Metalworking, Mechanics, Tailoring | 8 |
| Firearm | Aiming, Reloading | 2 |
| Survivalist | Fishing, Foraging, Trapping | 3 |

The B42-era revision of the same page lists 35 skills across seven groups — while carrying an editors' banner that the categorisation is still Build 41-based, so the shipped 42.20 grouping may present differently *(B42)* [4]:

| Group *(B42)* | Skills | Count |
|---------------|--------|-------|
| Passive | Fitness, Strength | 2 |
| Agility | Lightfooted, Nimble, Running, Sneaking | 4 |
| Combat | Axe, Long Blunt, Short Blunt, Long Blade, Short Blade, Spear, Maintenance | 7 |
| Crafting | Carpentry, Cooking, Electrical, Mechanics, Tailoring — joined by Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding | 12 |
| Farming | Agriculture, Animal Care, Butchering | 3 |
| Firearm | Aiming, Reloading | 2 |
| Survivalist | First Aid, Fishing, Foraging, Tracking, Trapping | 5 |

Note the moves as well as the additions: First Aid sits under Crafting on B41 but Survivalist on the B42-era page, and the farming skills gained a group of their own [4] [5].

## B42's new skills and renames

The seven new crafting skills back Build 42's expanded tech tree — announced around the unstable launch as new crafting systems including pottery, blacksmithing and stone working [2] [13]. In one line each, per the cited revision [4]:

- **Knapping** — shapes flint and stone into primitive tool components, up to a large stone axe head at higher levels [4] [14].
- **Masonry** — improves brick and stone construction and shares the top-end stone recipes with Knapping [4].
- **Carving** — turns wood and bone into simple tools, handles, hooks and basic weapons using a blade [4].
- **Blacksmithing** — forges metal tools, armour and weapons at dedicated workstations, rivalling looted equivalents at high level [4].
- **Welding** — builds and repairs metal structures and vehicle parts; the direct successor to B41's Metalworking, and its internal Skill ID is still `MetalWelding` [4] [5] [10].
- **Pottery** — produces clay goods such as bricks and ceramic vessels at a pottery bench or wheel [4].
- **Glassmaking** — melts sand or broken glass into workable glass for recipes [4].

The animal economy adds three more: **Animal Care** (reading animal condition and improving yields such as milk and wool), **Butchering** (meat quality when processing carcasses), and **Tracking** (identifying and following wild-animal signs in search mode) [4]. Tracking is also the one skill of the ten to appear by name in a pre-release Thursdoid, which describes following animals' droppings and broken twigs [3]. The 42.20 release notes further increase meat cuts from large animals on the butcher hook, touching Butchering's economy [1]. Deeper treatments live in `players-crafting-chains` and `players-animals-husbandry`.

Three renames, all keeping their internal IDs: B41's Farming is B42's Agriculture (Skill ID `Farming`) — the wiki records it was renamed in Build 42 [4] [5] [9]; Metalworking became Welding (`MetalWelding`) [5] [10]; Sprinting became Running (`Sprinting`) [5] [11].

One deliberate clarification: **Brewing is not a skill.** The Build 42 overview lists brewing among the new crafting *systems* alongside pottery, blacksmithing, stone working and weapon crafting, but no Brewing skill appears in the cited roster and no Brewing skill page exists on the wiki [4] [13].

## Sandbox XP options (overview)

The Custom Sandbox page documents an **XP Multiplier** option scaling all task XP, with range 0.001–1000 and default 1, plus a companion toggle, **XP Multiplier Affects Passive Skills**, default off, which decides whether Strength and Fitness ride the multiplier [12]. That page revision is versioned against 41.78.19, so treat the exact bounds as B41-verified and B42-probable *(B41)* [12]. During the unstable cycle The Indie Stone listed "XP gain adjustments" among areas of active tuning, so unstable-era XP feel is not a reliable guide to 42.20 [2]. Server-side XP configuration is Admins-track territory.

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42 *(B42)* |
|------|---------------------|------------------|
| Roster size | 26 skills, six categories [5] | 35 skills, seven listed groups (categorisation banner pending) [4] |
| New skills | — | Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Animal Care, Butchering, Tracking [4] |
| Renames | Farming, Metalworking, Sprinting [5] | Agriculture (`Farming`), Welding (`MetalWelding`), Running (`Sprinting`) [4] [9] [10] [11] |
| Category moves | First Aid and Farming under Crafting [5] | First Aid under Survivalist; farming skills in their own Farming group [4] |
| XP tables | Stated for 41.78.16 [5] | Same table republished, still labelled 41.78.16 — no verified B42 table [4] |
| Starting-level boost | 25/100/133/166%, Sprinting exception [5] | Same values documented; exception now under Running [4] [7] [8] |
| Skill books | Crafting + survivalist categories only (11 skills) [5] | 24 skills incl. Aiming, Reloading, Long Blade, Maintenance; book XP-boost bug fixed in 42.20 [1] [6]; split-screen sharing of book status and XP boosts fixed in 42.21 [19] [21] |
| Brewing | — | New crafting system, not a skill [13] |
| Sandbox XP options | XP Multiplier + passive toggle documented on a 41.78.19-versioned page [12] | Presence expected but bounds not re-verified; unstable cycle included XP tuning [2] [12] |

Summed up: the *mathematics* of levelling is documented as unchanged between builds, but the *surface* it applies to grew by a third — nine new skills, three renames, a regrouped panel, and skill books extending into combat and firearms for the first time [1] [4] [5] [6].

# Practical Guidance

- **Buy your XP rate at creation, not later.** The jump from 25% to 100% XP for one starting level is the best-value purchase in the game — put creation points into the two or three skills you actually intend to grind, and treat everything at level 0 as a quarter-speed hobby.
- **Match the book to the band before you grind.** Grinding levels 5–6 without Volume III means paying 4,500 XP at full price when 562.5 would do. The habit that separates efficient survivors: find the book, read it fully, then grind.
- **Don't burn a volume early.** Reading above your band grants nothing, and books are single-use. Check the skills panel band first.
- **Expect Strength and Fitness to be marathon projects.** At twenty times the level-1 cost of a regular skill and no starting-level boost, the passive pair rewards routine (regular exercise, encumbered living) rather than bursts — and the sandbox passive-XP toggle is off by default, so a raised XP Multiplier won't speed them up unless you flip it [12].
- **On B42, plan around the new families.** Knapping and Carving are the low-tech entry points, Masonry and Blacksmithing the high-end payoffs — if you intend a crafting run, spread starting levels accordingly and see `players-crafting-chains` for routes.
- **Returning from B41?** Look for your old skills under new names — Agriculture, Welding, Running — before concluding they were removed; the underlying IDs are unchanged [9] [10] [11].
- **Aiming and Reloading now have books on B42** — worth shelf-checking before a firearms-heavy phase, especially given their documented post-level-5 XP slowdown [4] [6].

# Common Pitfalls & Troubleshooting

- **"My unlevelled skills barely move."** Working as designed: level-0 skills earn 25% XP [5] [7]. The fix is at character creation, not in play.
- **"The creation screen said +75%, this document says 100%."** The displayed percentages are community-reported as incorrect — see Claim 1; the actual rates in the table above are the wiki's tested values [7] [8].
- **"I read the book but got no boost."** Either you were above the volume's band (the read is wasted) or below it (the game refuses the read); and on pre-42.20 builds, a now-fixed calculation bug could also under-apply book boosts [1] [6].
- **"Sandbox XP Multiplier didn't touch Strength/Fitness."** The passive pair has its own toggle, default off [12].
- **"Where did Farming/Metalworking/Sprinting go on B42?"** Renamed, not removed: Agriculture, Welding, Running [4] [9] [10] [11].
- **"Where's the Brewing skill?"** There isn't one — brewing is a crafting system without an attached skill in the cited roster [4] [13].
- **Trusting unstable-era XP feel on 42.20.** XP gain was explicitly on the tuning list during unstable, and 42.20 changed skill-book behaviour; re-test before importing habits [1] [2].

# Community Notes & Unverified Claims

## Claim 1 — The character-creation screen displays the wrong XP-boost percentages

- **Claim:** The boost values shown in-game for starting levels 1, 2 and 3 read +75%, +100% and +125%, while the real experience rates are 100%, 133% and 166%; pzwiki documents this identically on its Trait and Occupation pages, stamped as present on version 42.13.1, and its B41-era Skill page carried the same displayed-versus-actual split.
- **Why unverified:** No Indie Stone patch note or dev post acknowledges the display bug, the wiki notes it was never reported on the official forums, and the 42.13.1 stamp predates 42.20 — it may have been silently fixed at stable.
- **Confidence:** Medium. Consistently documented across multiple independently maintained wiki pages on both builds' revisions, but resting entirely on community testing.

## Claim 2 — Strength/Fitness starting boosts are displayed even when disabled in sandbox

- **Claim:** Per the pzwiki Trait page, Build 41.78.16 shows a starting boost for Strength and Fitness in the UI even when the relevant sandbox behaviour disables it.
- **Why unverified:** The wiki itself marks the statement with a "verify" flag, no primary source exists, and the exact sandbox setting involved is not named.
- **Confidence:** Low. Single-sourced from a wiki sentence that the wiki's own editors have flagged for verification.

## Claim 3 — Build 42 uses the same XP-requirement table as 41.78.16

- **Claim:** Community guides and the wiki's B42-era Skill revision treat the 41.78.16 XP table (75→9,000 regular, 1,500→150,000 passive) as still accurate for Build 42.
- **Why unverified:** The B42-era page simply republishes the table with its B41 label rather than asserting re-verification, and The Indie Stone listed XP gain among unstable-cycle tuning targets — gain rates changing would not change requirements, but no primary source confirms the requirement table either way for 42.20.
- **Confidence:** Medium. No contradicting report has surfaced across the unstable cycle, but positive confirmation on 42.20 is absent.

# Risks & Caveats

- **Nothing here is 42.20-re-verified except the patch-note facts, and 42.21 was checked against patch notes only.** The Skill page is versioned 42.3.1 with an outdated-categorisation banner, Skill book 42.13.2, Occupation 42.18.0, Trait 42.19.0, Running 42.18.0, and Custom Sandbox 41.78.19 [4] [6] [7] [8] [11] [12]. That spread is the core reason for the Medium rating.
- **The 42.20 skill-book XP fix has an unspecified scope** ("in some cases"), and 42.21 later fixed further XP-adjacent issues (split-screen boost sharing, Nimble XP in multiplayer combat stance), so adjacent behaviour has already moved once after 42.20 [1] [19] [21].
- **The B42 grouping table may not match the in-game panel** given the wiki's own banner; the *membership* of the roster is better attested than its presentation [4].
- **Cumulative XP columns and the book-band "effective XP" column are this document's arithmetic** over cited per-level figures, not independently published numbers.
- **Rename statements combine two revisions plus internal IDs**; only Farming→Agriculture is stated outright by the wiki as a Build 42 rename [9]. Welding and Running are inferred from roster comparison plus preserved Skill IDs [5] [10] [11].
- **Skill-book multipliers "can vary between each topic"** per the wiki's own caption — the ×3/×5/×8/×12/×16 ladder is the standard case, not a guarantee for every book [6].

# Verification Steps

1. **XP table (42.20):** in-game, hover a level-0 regular skill in the skills panel (`L`) and confirm 75 XP to level 1; hover Strength and confirm 1,500.
2. **Starting-level boost:** create a character with one skill at level 1, note XP gained per action versus the same action on a level-0 skill; a 4:1 ratio confirms the 100%/25% split.
3. **Display bug (Claim 1):** at character creation on 42.20, record the boost percentages shown for starting levels 1–3 and compare with 100/133/166.
4. **Book bands:** attempt to read a Volume II at skill level 1 (expect refusal) and a Volume I at level 3 (expect no boost).
5. **Roster:** open the 42.20 skills panel and tick off the 35-skill B42 table above; note the panel's actual grouping against the wiki's B41-based categorisation.
6. **Sandbox options:** open Custom Sandbox on 42.20, locate XP Multiplier and the passive-skills toggle, and record their bounds and defaults against the 41.78.19-versioned figures.
7. **Sources:** each pzwiki citation below pins an exact `oldid` — diff against the live page for post-42.20 corrections.

# Open Questions

- Does 42.20 or 42.21 still display the wrong starting-boost percentages (Claim 1)? The 42.21 changelist as retrieved does not mention it [21]; one character-creation screenshot resolves it.
- What is the shipped 42.20 skill-panel grouping, given the wiki's outdated-categorisation banner [4]?
- Which "cases" did the 42.20 skill-book XP fix cover, and did effective multipliers change [1]?
- Are the XP requirements per level identical on 42.20 (Claim 3)? A tooltip sweep across one regular and one passive skill resolves it.
- Do the Custom Sandbox XP options carry the same bounds and defaults on B42 [12]?
- Do any B42 books deviate from the standard multiplier ladder, and by how much [6]?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [2] **The Indie Stone** — *Build 42 Unstable Out Now* (Steam announcement, 2024-12-17). https://steamcommunity.com/games/108600/announcements/detail/1785774543698069. Accessed 2026-07-30.
- [3] **The Indie Stone** — *WhatZ Next* (Thursdoid, Steam announcement, 2024-11-28). https://steamcommunity.com/games/108600/announcements/detail/1784506359022970. Accessed 2026-07-30.
- [15] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [16] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441. Accessed 2026-10-07.
- [17] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895. Accessed 2026-10-07.
- [18] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [19] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [20] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [21] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post by Rockjaw, 2026-09-23; retrieved abridged, "selected" lists only). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [4] **PZwiki** — *Skill* (revision 1436755; page versioned against 42.3.1, carries an outdated-categorisation banner; confirmed still the latest revision on 2026-07-30). https://pzwiki.net/w/index.php?title=Skill&oldid=1436755. Accessed 2026-07-30. Fact-only source.
- [5] **PZwiki** — *Skill* (revision 663165, 2024-12-14; page versioned against 41.78.16 — the pre-Build 42 revision, used for all B41 facts). https://pzwiki.net/w/index.php?title=Skill&oldid=663165. Accessed 2026-07-30. Fact-only source.
- [6] **PZwiki** — *Skill book* (revision 1317189; page versioned against 42.13.2). https://pzwiki.net/w/index.php?title=Skill_book&oldid=1317189. Accessed 2026-07-30. Fact-only source.
- [7] **PZwiki** — *Trait* (revision 1442751; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Trait&oldid=1442751. Accessed 2026-07-30. Fact-only source.
- [8] **PZwiki** — *Occupation* (revision 1391359; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Occupation&oldid=1391359. Accessed 2026-07-30. Fact-only source.
- [9] **PZwiki** — *Agriculture* (revision 1439053; records the Build 42 rename from Farming and the `Farming` Skill ID). https://pzwiki.net/w/index.php?title=Agriculture&oldid=1439053. Accessed 2026-07-30. Fact-only source.
- [10] **PZwiki** — *Welding* (revision 1436247; records the `MetalWelding` Skill ID). https://pzwiki.net/w/index.php?title=Welding&oldid=1436247. Accessed 2026-07-30. Fact-only source.
- [11] **PZwiki** — *Running* (revision 1435413; page versioned against 42.18.0; records the `Sprinting` Skill ID and Fast/Slow Learner rates). https://pzwiki.net/w/index.php?title=Running&oldid=1435413. Accessed 2026-07-30. Fact-only source.
- [12] **PZwiki** — *Custom Sandbox* (revision 1442995; page versioned against 41.78.19). https://pzwiki.net/w/index.php?title=Custom_Sandbox&oldid=1442995. Accessed 2026-07-30. Fact-only source.
- [13] **PZwiki** — *Build 42* (revision 1443663; lists brewing among new crafting systems). https://pzwiki.net/w/index.php?title=Build_42&oldid=1443663. Accessed 2026-07-30. Fact-only source.
- [14] **PZwiki** — *Knapping* (revision 1439145; records the `FlintKnapping` Skill ID). https://pzwiki.net/w/index.php?title=Knapping&oldid=1439145. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited.

**Further Reading**

# Further Reading

- The Steam news API feed used to verify announcement primaries: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25
- The Indie Stone's Build 42 feature overview, linked from the 42.20 release notes: https://projectzomboid.com/blog/features-overview-build-42-20/ (bot-blocks automated checkers; verify in-browser).
- pzwiki's per-skill pages (Carpentry, Blacksmithing, Foraging, …) for levelling routes beyond this document's scope.

# Related Documents

- `players-foundation` — the Players-track overview this document deepens.
- `players-traits-occupations` — full occupation and trait rosters feeding the starting-level boost.
- `players-crafting-chains` — how the new B42 crafting skills chain together in practice.
- `players-animals-husbandry` — Animal Care, Butchering and Tracking in the animal economy.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | 42.21 re-baseline against the 42.20.1–42.20.4 hotfix notes, the 42.21 unstable and stable Steam posts and the abridged TIS forum 42.21 changelist: Nimble XP combat-stance (MP) fix, split-screen book-status/XP-boost fix and PerkLog.txt fix recorded; Build Applicability, Delta, Risks and Open Questions updated; no XP numbers changed. Rebase is a patch-notes review, not an in-game re-test. | — |
