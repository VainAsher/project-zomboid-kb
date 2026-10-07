---
id: players-crafting-chains
title: "The B42 Crafting Overhaul: From Knapping to Blacksmithing"
version: 0.2.0
status: in-review
confidence: Medium
category: Players
topic: "Crafting"
build: both
document_type: reference
created: 2026-07-30
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-skills-xp, players-traits-occupations, players-animals-husbandry, modders-foundation, meta-style-guide]
tags: [players, crafting, build-42, knapping, carving, pottery, masonry, welding, blacksmithing, glassmaking, fluids, self-sufficiency, workstations]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-crafting-chains |
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

Build 42 rebuilt Project Zomboid's crafting from a flat list of right-click recipes into a set of progression chains: a primitive arc that starts with striking flint (Knapping), moves through whittling wood and bone (Carving), firing clay in kilns (Pottery) and building in brick and stone (Masonry), and a metalworking arc that splits Build 41's single Metalworking skill into torch-based Welding and forge-based Blacksmithing, with Glassmaking as a furnace-fed side branch [6] [15] [16] [20]. The Indie Stone's stated goal for the overhaul is self-sufficiency: "to allow for a long post-apocalyptic settlement to create everything they need without relying on looting", with the developers' internal test case being that a player on a blank wilderness map "literally cannot rely on looted items" [1].

This document maps those chains for players: what each skill covers, what unlocks it, and roughly what it needs — workstations (crafting surfaces, pottery wheels, kilns, furnaces, forges), fuel (charcoal above all), and materials (flint, clay, stone, iron and steel, sand) [11] [13] [14] [16] [17]. It also gives an overview of the new fluids system that underpins much of B42 crafting, and states the delta against Build 41, where crafting was a flat recipe list, forging did not exist outside debug mode, and "Metalworking" meant a propane torch [10] [15].

Document-level confidence is **Medium**: the goals, the renames and the system's existence are primary-sourced from Indie Stone posts and patch notes (High), but the per-chain details rest on pzwiki page revisions versioned against unstable builds 42.11.0–42.18.0 and have not been individually re-verified on 42.20 stable.

# Key Takeaways

- The crafting overhaul's official aim is a settlement that can "create everything they need without relying on looting" — B42 is the "crafting update" The Indie Stone spent years trailing *(cited)* *(B42)*
- The primitive chain runs Knapping (stone tools from flint) → Carving (wood and bone) → Pottery (clay, fired in kilns) → Masonry (brick and stone building), and each chain feeds the next *(cited)* *(B42)*
- B41's single Metalworking skill became two skills: **Welding** (propane torch, metal barricades and structures — the direct heir) and **Blacksmithing** (forges, anvils, casting and smithing), with the forging skill renamed from "Metalworking" to "Blacksmithing" in 42.12 *(cited)*
- Blacksmithing is the deep end: charcoal production, furnaces, forges and an advanced-forge project that pulls in Carving, Pottery and the animal-husbandry leather chain *(cited)* *(B42)*
- Glassmaking melts sand or broken glass in a furnace using a crucible, tongs and charcoal, then shapes it with a glass blowing pipe and pliers *(cited)* *(B42)*
- B42 replaced per-item water tracking with a fluids system: any fluid container can hold any fluid, containers mix compatible fluids and track their combined properties, and tainted fluid taints whatever it touches *(cited)* *(B42)*
- Recipes are learned four ways in B42: character creation choices, magazines and schematics, skill-level auto-learns, and the 42.3 "Research Craft" system that reverse-engineers recipes from looted items *(cited)* *(B42)*
- No skill named Brewing appears in the cited B42 skill roster; alcohol in B42 exists as fluids, not as a crafting chain *(cited)* *(B42)*

# Purpose

This document answers the question every returning Build 41 player and every new Build 42 player asks the first time they open the crafting menu: what are all these new skills, in what order do they unlock each other, and what do I actually need to build before I can use them? It is the Players-track deep dive on the crafting overhaul that `players-foundation` only headlines. It deliberately stays at the level of chains, gates and stations — which skill needs which workstation, fuel and material family — rather than exhaustive recipe tables.

# Scope

Covered: the design goals of the B42 crafting overhaul as stated by The Indie Stone; the B42 crafting menu and the four recipe-learning routes; the primitive chain (Knapping, Carving, Pottery, Masonry); the metalworking chain (Welding, Blacksmithing) including fuel and station requirements; Glassmaking; the fluids system at overview level; and the full delta against Build 41 crafting.

Not covered: per-recipe ingredient lists and XP tables (see pzwiki's per-skill pages, cited below, for those); Carpentry, Cooking, Tailoring and Electrical, which exist in both builds and deserve their own documents; farming and food chains; and the Modders-track view of the craftRecipe script format (see `modders-foundation`). Brewing is excluded from the chain coverage because no primary or fact-only source for a Brewing chain could be found — see the quarantine section. Unstable-branch behaviour after 42.20 is out of scope. Spoiler-awareness: this document names systems and stations but avoids map locations and loot specifics.

# Definitions

- **Crafting chain** — this document's term for a sequence of skills and stations where earlier links produce the tools and materials the later links require (e.g. Carving makes the tongs and molds that Blacksmithing and Pottery consume) [12] [16].
- **Workstation** — a placed or built object that specific recipes require, opened by clicking on it: pottery benches and wheels, kilns, furnaces, forges, grindstones [9] [13] [16].
- **Crafting surface** — a flat surface (e.g. a table) that surface-bound recipes such as all Knapping recipes require; The Indie Stone calls the associated interface the "crafting on a flat surface" UI [3] [11].
- **Research Craft** — the B42 system (added 42.3) that lets a character reverse-engineer learnable recipes from an item via a right-click "Research Craft" option [5].
- **Fluid / fluid container** — B42's unified liquid resource and the items or objects that store it; any fluid container can store any fluid, measured in millilitres and litres [18] [19].
- **Charcoal** — the fuel of the metalworking chain, produced from wood in a charcoal burning pile or barrel; used in every blacksmithing recipe [16].
- **Auto-learn** — recipes granted automatically on reaching a skill level, one of B42's four recipe-learning routes [9].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Flat-recipe crafting; single Metalworking skill; no primitive chain, no fluids system [10] [15] |
| B42 (stable) | Yes | 42.20; patch notes re-read through 42.21 | The crafting-chain system described here; per-chain details cited from wiki revisions versioned 42.11.0–42.18.0, not individually re-verified on 42.20 [7] [9]; 42.21 adds small recipe and fluid balance notes (see Reference) [25] [27] |

The overhaul's skills shipped with B42 unstable on 2024-12-17 and evolved across the unstable cycle — notably the 42.3 research system and the 42.12 skill rename — so any B42 guide should be date-checked against those patches [4] [5] [6].

Revision 0.2.0 (2026-10-07) re-read the 42.20.1, 42.20.2, 42.20.3 and 42.20.4 hotfix notes [21] [22] [23] [24], the 42.21 unstable and stable announcements [25] [26] and the abridged ("selected") TIS forum 42.21 changelist [27]. The four 42.20.x hotfix notes cover multiplayer, memory, security and mod-tooling fixes and list no crafting-chain, skill-gate or station-requirement changes [21] [22] [23] [24]. Statements not named as 42.21-affected are carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found in those notes; this is a patch-notes review, not an in-game re-test [27].

# Reference

## What the overhaul is for

The Indie Stone's design post on the overhaul states the aim plainly: to expand crafting massively "to allow for a long post-apocalyptic settlement to create everything they need without relying on looting, to elevate the need for players to ever need to reset their worlds unless they want to", while gating the new possibilities behind professions and skills so that recipes appear only where they make sense for the character [1]. The same post names the team's internal test case — a blank wilderness map where "the player literally cannot rely on looted items" — and cites extensive Minecraft tech-progression modpacks as the spirit (not the letter) of the inspiration: a tall tech tree whose branches unlock new areas of gameplay [1]. The envisioned crafts included tanning leather, spinning wool, dyes, bowyers, glass-makers and stone masonry [1]. An earlier post from the same team lead described crafted items carrying RPG-like variable attributes based on the crafter's skill, with input-item quality influencing output quality — the stated design direction for the item side of the system [2].

## How crafting works in B42

The B42 crafting menu opens with the **B** key or the crafting HUD icon; recipes are filtered by category and can be sorted by name, required items or output [9]. Completing a recipe requires the ingredients (in your inventory or surrounding accessible containers), knowing the recipe where required, the required skill level(s), and — new to B42 — an appropriate workstation where one is demanded; some recipes add further conditions such as sufficient light [9]. Tools count as ingredients but are kept afterwards, though they can lose durability, sharpness or uses [9]. Recipes are learned through four routes: traits and occupations at character creation, recipe magazines and schematics, researching recipes from items, and auto-learns from gaining skill levels [9]. The research route was added in 42.3: items that can teach you something show it in their tooltip, and a right-click "Research Craft" option grants the recipe plus the XP the craft itself would have given [5]. Crafting and Build UI polish, ingredient tuning and XP adjustment were named as the top initial patching priorities at unstable launch, so early-42 impressions of the interface do not reflect the stable build [3] [4].

## The primitive chain

### Knapping — stone tools from flint

Knapping is the crafting skill for basic stone tools and stone tool heads, using a hammer-type tool (stone, stone hammer, knapping tool, wooden mallet or short bat), and every knapping recipe requires a crafting surface [11]. Its materials — flint nodules, sharp flint flakes and large smooth flat stones — are foraged with no level requirement or broken out of flint deposits with a club hammer, sledgehammer or stone maul [11]. The recipe ladder the wiki records: sharp flint flakes at level 0, stone chisels and stone-blade scythes at level 1, flint saws at level 2, large stone axe heads at level 3 and stone maul heads at level 4, with no new recipes past level 6 [11]. Park Ranger (+1) and the Bushcrafter trait (+1) are the cited starting boosts [11]. Knapping is also a showcase of the research system: sharp flint flakes, mason's chisels, saws, drills and scythes can each be researched to unlock their stone equivalents at the appropriate level [11].

### Carving — wood and bone

Carving covers small wood and bone items, with a knife as the primary tool — and a foraged sharp flint flake works as that knife, which is what links Carving to Knapping at the bottom of the tree [12]. Its material staples are tree branches, saplings and scavenged wood; bone items extend it to fishhooks, needles, awls and crude knives [12]. Carving is the chain's toolmaker: it produces handles, knapping tools, wooden trowels, clay sculpting tools, molds' wooden precursors and the crude wooden tongs that early Blacksmithing borrows [11] [12] [13] [16]. Cited starting boosts: Carpenter and Park Ranger occupations (+1 each); Whittler (+2), Bushcrafter (+1) and Handy (+1) traits [12].

### Pottery — clay, wheels and kilns

Pottery is the clay skill, and the wiki describes it explicitly as a secondary skill to Masonry and Glassmaking — the chains above it cannot run efficiently without it [13]. Many recipes require one of its two workstations, the pottery bench or pottery wheel, both buildable or findable in the world [13]. Clay itself is the gate: the cited revision calls it "incredibly rare", obtainable by foraging (clumps of 2–4, best odds in forests) or by harvesting clay deposits with an empty sack and a digging tool; visible clay deposits were added in 42.3 [5] [13]. The workflow is sculpt or press → optionally glaze → fire in a kiln, with kilns player-buildable in small and large sizes and some recipes demanding the larger one [13]. Pottery's outputs are load-bearing for the rest of the tree: fired bricks, tiles and shingles, crucibles for Blacksmithing and Glassmaking, ingot and anvil molds, and the glass blowing pipe [13]. No occupation boosts Pottery in the cited revision; the Artisan trait gives +1 [13].

### Masonry — brick and stone building

Masonry is the building skill of the primitive chain: brick and stone constructions that can be stronger than Carpentry's wooden ones [14]. Its bricks come from Pottery, and its stone comes from the world — mineral deposits, loose stones, and large stones that can be pulled straight out of certain grassy tiles via the Gardening menu [14]. The cited revision notes a hard bottleneck at the very first level: the sole recipe that can carry a character to Masonry 1 is breaking large stones down into smaller ones [14]. Tools are trowel-and-chisel simple (mason's trowel, mason's chisel, hammer or club hammer), and the build list runs from cooking pits through brick and stone walls, door and window frames, stone cabinets, querns and mills — plus the stone anvil that gives early Blacksmithing a working surface [14]. Cited starting boosts: Construction Worker (+2), DIY Expert, Engineer and Carpenter (+1 each); Mason trait (+2), Handy (+1) [14].

## The metalworking chain

### Welding — the torch (and B41's heir)

Welding is B42's continuation of what B41 called Metalworking: barricading windows and doors with metal, building metal walls, fences, doors, stairs and containers, repairing car parts, and disassembling metal objects in the world [15]. Its toolkit is unchanged in spirit: a propane torch and welding mask for building and disassembly, welding rods for construction, propane tanks for refills [15]. Structure quality is skill-gated — level 1 walls/windows at Welding 2, level 2 at Welding 8 — and wall health scales with the welding level [15]. The big behavioural delta from B41: dismantling most metal furniture no longer grants XP on standard settings (a sandbox option restores it); car wrecks are the exception and remain a welding-XP and metal source [15]. The Metalworker occupation (+4, with recipes known) and Mechanic (+1) are the cited starting boosts [15].

### Blacksmithing — charcoal, furnaces, forges

Blacksmithing is the forge skill: extracting and smelting iron and steel, casting bars and ingots, and forging tool heads, blades, armor and eventually high-end weapons, with forged tool heads described as equal to their lootable counterparts [16]. It was briefly named "Metalworking" in early B42; patch 42.12 changed every player-facing string for the skill to "Blacksmithing", and the wiki notes B41's skill of that name maps to Welding instead [6] [16]. Its demands are the steepest in the game:

- **Fuel** — charcoal appears in every blacksmithing recipe, produced from wood in a charcoal burning pile or barrel; the process is heavily wood-intensive [16].
- **Metal** — scavenged and broken-down metal objects, especially car wrecks; iron is the crude tier, steel the quality tier, and top-end products demand steel specifically [16].
- **Stations** — a furnace (primitive → smelting → blast, each tier keeping its predecessors' recipes) to melt metal (and glass), and a forge (primitive → forge → advanced), which the wiki describes as a furnace plus an anvil; a grindstone sharpens blades [16].
- **Tools** — smithing hammer, ball-peen hammer, tongs (crude wooden tongs from Carving work at the start), metalworking pliers, chisels, punches, whetstones and files, varying by step [12] [16].

The advanced forge is the chain's capstone project, and its two hard components deliberately reach across the whole tech tree: the large bellows requires crude tanned medium leather — kill and skin a medium animal, deflesh the hide on a softening beam, brain-tan it in a tannin barrel, dry it on a leather drying rack — and the blacksmith anvil requires wooden and clay anvil molds, ceramic crucibles (Pottery level 1), a kiln firing, and molten iron cast at a furnace [16]. Cited starting boosts: the Blacksmith occupation (+4) and the Blacksmith Knowledge trait (+2) [16].

## Glassmaking — the furnace side branch

Glassmaking creates glass from sand or broken glass and shapes it into panels, jars, bottles and glassware [17]. Melting requires a furnace — the same station family Blacksmithing builds — plus a ceramic crucible, tongs (or crude tongs) and charcoal; shaping requires a glass blowing pipe (itself a fired Pottery product) and pliers [13] [17]. Individual glassware recipes are taught by dedicated recipe magazines [17]. No occupation boosts Glassmaking in the cited revision; the Artisan trait gives +1 [17]. On brewing: no skill named Brewing appears in the cited B42 crafting-skill roster (Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery, Welding), and alcohol in B42 exists as fluids with per-litre alcohol values rather than as a production chain [18] [20].

## The fluids system (overview)

B42 replaced ad-hoc, per-item liquid handling with a unified fluids system. A fluid is a resource stored in fluid containers; any fluid container can store any fluid, and capacities are tracked in millilitres and litres [18] [19]. Containers mix compatible fluids and track the combined properties — nutrition, alcohol and the like — and each fluid carries per-litre values for hunger, thirst, calories, poison, alcohol, fatigue, stress and unhappiness [18] [19]. Purity matters: fixes during the unstable cycle established that a tainted source always taints its destination, and rain slowly converts water to tainted water in open floor containers [5]. Containers over 3 litres cannot be drunk from directly and must be decanted; some (gas tanks, water dispensers) are output-only and cannot be refilled [19]. The system reaches into crafting itself — recipes were converted to require fluid in a specific vessel (e.g. water in the bowl for brain tan) rather than a generic "water container" [5] — and into modding, where the developers cite fluid, item and power transmission as part of the new framework [1]. Late in development the team also reworked "drainables" (used-up items in recipes) with input flags for common crafting cases [8].

## What 42.20 stable changed

The stable release's crafting notes are polish, not redesign: fixes to the crafting queue stopping when tools break, bulk-craft progress bars, the Favourites tab in the Crafting and Build UIs, double-click errors, and molotov ingredient consumption [7]. The chains described above are the shipped 42.20 system, inherited from the unstable cycle [7].

## What 42.21 changed

The 42.21 balance notes (stable 2026-09-28) touch crafting at the edges rather than the chains [26]. Characters with the Welder occupation now start with Welding recipes instead of Blacksmithing recipes [25] [27]. Another 86 fluid containers can be used to purify water in the appropriate oven type [25] [27]. Washing machines now clean dirty rags, strips or bandages [25] [27]. Antibiotics can be packaged with the "pack in box" crafting recipe [25] [27]. The forum changelist also lists a fix for wrong Recipes used in CharacterTraitScriptGenerator, without naming which recipes were affected [27]. The same list records fixes for the crafting UI not closing after removing a crafting station and for the Making Sinew animation using the wrong items [27]. The retrieved (abridged) changelist lists no change to a skill gate, station requirement or fuel value for the primitive, Blacksmithing or Glassmaking chains [27].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Crafting model | Flat recipe list via right-click context menus plus a category-tab crafting UI [10] | Chained skills with workstation, surface, light and skill gates; separate Crafting and Build UIs [3] [9] |
| Construction | Right-click "Carpentry" / "Metalwork" context menus; construction recipes absent from the crafting UI [10] | Dedicated Build UI designed to remove reliance on right-click [3] |
| Metal skills | One skill: Metalworking (propane torch) [10] [15] | Split: Welding (torch, B41's heir) + Blacksmithing (forge); forging skill renamed from "Metalworking" to "Blacksmithing" in 42.12 [6] [15] [16] |
| Forging | Smithing recipes existed in data but were unobtainable outside debug/admin spawning of The Smithing Magazine [10] | Full Blacksmithing chain: charcoal, furnaces, forges, casting, smithing [16] |
| Primitive crafts | None — no Knapping, Carving, Pottery, Masonry or Glassmaking [20] | Six new crafting skills forming the primitive chain and glass branch [20] |
| Recipe learning | Occupation/traits, magazines, skill-level unlocks for construction [10] | Same routes plus item research ("Research Craft", 42.3) and broader auto-learns [5] [9] |
| Starting recipes for the torch trade | No Welder occupation (Metalworker) [10] | Welder starts with Welding recipes, not Blacksmithing recipes (42.21) [25] [27] |
| Welding XP | Levelled by dismantling metal objects and furniture [15] | Furniture dismantling XP off by default (sandbox option); car wrecks remain [15] |
| Liquids | Per-item water/fuel tracking; no unified system [10] [19] | Unified fluids: any container, any fluid, mL-tracked, mixing and taint propagation [18] [19] |
| Design goal | Loot-centric survival with crafting as support | Stated goal of full settlement self-sufficiency without looting [1] |

The one-line version: B41 crafting asked "do I have the items?"; B42 crafting asks "have I built the station, fuelled it, learned the recipe and levelled the chain that feeds it?" [1] [9] [16].

# Practical Guidance

- **Read the chain bottom-up before you invest.** Knapping and Carving cost almost nothing (foraged flint, branches, a table) and produce the tools — flake knives, stone chisels, crude tongs, trowels — that every later chain quietly assumes you have. Skipping them means hitting tool walls in Pottery and Blacksmithing later.
- **Stockpile clay whenever you see it.** The cited revision calls clay "incredibly rare", and it gates crucibles, molds, kilns and therefore both Blacksmithing's anvil and Glassmaking's pipe. Forest foraging and clay deposits (sack + digging tool) are your two sources.
- **Treat charcoal as a production line, not an errand.** Every blacksmithing recipe consumes it, so build the charcoal pit early and keep logs flowing; the wiki flags the whole chain as wood-hungry.
- **Car wrecks are the metal mine.** They are the one dismantling target that still grants Welding XP on default settings and a prime source of steel for the forge — and stripping wrecks outside town is safer than looting metal in dense areas.
- **Plan the advanced forge as a multi-skill project.** Its bellows needs the animal-husbandry leather loop (see `players-animals-husbandry`) and its anvil needs Pottery level 1 plus a kiln. Starting Blacksmithing without touching animals or clay means stalling at the primitive forge tier.
- **Use Research Craft on your loot.** Since 42.3, items with a lightbulb tooltip can teach you their recipe and pay the same XP as crafting them — scissors, saws, scythes and drills all unlock stone equivalents this way.
- **Pick your character for your chain.** Blacksmith (+4 Blacksmithing), Welder (+4 Welding per the pinned roster; on 42.21 it starts with Welding recipes [25]), Construction Worker (+2 Masonry) and the Whittler/Mason/Blacksmith Knowledge traits are large head starts in skills whose level-0 rungs are the slowest; see `players-traits-occupations`.
- **Respect fluid purity.** Tainted always wins when fluids meet, and rain slowly taints open floor containers — keep drinking water covered or indoors, and decant from anything over 3 L.

# Common Pitfalls & Troubleshooting

- **"I can't knap anything."** All knapping recipes need a crafting surface in addition to the hammer-type tool — stand at a table, not in a field [11].
- **"Masonry won't level."** Reaching Masonry 1 depends on a single recipe — breaking down large stones; pull them out of grassy tiles via the Gardening menu and crush away [14].
- **"Dismantling my fridge gives no Welding XP."** Working as designed in B42: furniture-dismantling XP is a sandbox option, off on standard difficulties; use car wrecks [15].
- **"Where did the Metalworking skill go?"** It became two skills; your B41 muscle memory maps to Welding, while "Blacksmithing" (called Metalworking in early B42 unstable) is the new forge skill — B41-era and early-unstable guides use the old names [6] [15] [16].
- **"My kiln/forge recipe isn't in the crafting menu."** Workstation recipes are opened by clicking the station itself, and better furnaces and forges inherit their lesser tiers' recipes — check you built the tier the recipe needs [13] [16].
- **"My rain barrels turned to tainted water."** Rain gradually replaces water with tainted water in fillable items left on the floor, and any tainted source taints the destination container on transfer [5].
- **"A B42 guide from early unstable disagrees with my game."** The crafting system was patched continuously across 42.1–42.19 (research system in 42.3, rename in 42.12, ingredient tuning throughout); date-check guides against those patches [4] [5] [6].

# Community Notes & Unverified Claims

## Claim 1 — Brewing is one of Build 42's new crafting chains

- **Claim:** Community previews, video roundups and discussion threads sometimes list "Brewing" alongside Knapping, Pottery and Blacksmithing as a B42 crafting chain for producing alcohol.
- **Why unverified:** No primary source found — no Indie Stone post or patch note in the reviewed 2022–2026 set mentions a brewing system, pzwiki has no Brewing page, and no Brewing skill appears in the cited B42 skill roster [20]; B42's alcohol exists as fluids with per-litre alcohol values [18].
- **Confidence:** Low. The absence is consistent across every checked primary and fact-only source; the claim likely conflates the fluids system's alcohol handling with a production chain.

## Claim 2 — Levelling Blacksmithing to high level takes weeks to months of play

- **Claim:** The pzwiki Blacksmithing guide prose states it is "normal to take weeks or even months" of play to reach high Blacksmithing, making it a late-game skill.
- **Why unverified:** This is community-authored pacing judgement on a wiki page versioned against 42.18.0, not a checkable game value; no primary source quantifies the grind, and XP tuning continued through the unstable cycle [4].
- **Confidence:** Medium. The underlying structural facts (multi-skill prerequisites, charcoal and metal costs) are documented; only the time estimate is subjective.

## Claim 3 — The most XP-efficient Welding routes are car wrecks, then scrap knives, then metal sheets

- **Claim:** The pzwiki Welding page lists per-level optimal XP routes with specific numbers (about 17 XP per 10 torch uses on wrecks; 20 XP per 4 uses on scrap knives; 25 XP per 2 uses on sheets).
- **Why unverified:** The section carries the wiki's own accuracy-improvement banner, the values are community-measured on an unstable-era revision, and no primary source publishes XP-per-recipe numbers.
- **Confidence:** Low. Plausible and widely repeated, but flagged as unconfirmed by its own source and sensitive to the ingredient/XP tuning The Indie Stone patched repeatedly [4].

# Risks & Caveats

- **Wiki revisions trail the stable build.** Every per-chain detail is cited from pzwiki revisions versioned 42.11.0–42.18.0; 42.20 shipped 2026-07-29 and its notes show continued crafting-UI and recipe fixes [7]. Specific gates (e.g. Welding 2/8 for wall tiers, the Masonry 0→1 bottleneck, clay rarity) could have shifted at stable without a traceable note; the selected 42.21 changelist lists none of these gates as changed, which is an absence in a partial list, not a confirmation. This is the main reason the document is Medium.
- **Occupation/trait boost lists are point-in-time.** The cited +N values (Blacksmith +4, Whittler +2, etc.) come from unstable-era page revisions; the roster itself changed during B42 development [16] and may change in the announced Support Update.
- **Design-goal statements are not shipped-feature statements.** The self-sufficiency goal, wilderness-map test case and item-attribute system are cited from 2022–2023 developer posts describing intent [1] [2]; this document does not claim every stated goal is fully realised in 42.20.
- **Post-stable change is continuing.** 42.20 was followed by four hotfixes and then 42.21, which adjusted several recipes and fluid-container rules [21] [22] [23] [24] [26]; later patches could adjust ingredient counts, XP or station requirements faster than sources update.
- **Steam announcement mirrors.** Primary citations use Steam announcement URLs (per project source policy); these hosts bot-block automated link checkers, so the checker reports warnings, not failures, on them.

# Verification Steps

1. **Confirm the B42 crafting skill roster in-game (42.20):** open the skills panel and check for Blacksmithing, Carving, Glassmaking, Knapping, Masonry, Pottery and Welding — and the absence of a Brewing skill.
2. **Confirm the 42.12 rename:** fetch the Steam news API (`https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0`) and locate "Changed all player facing text strings for the Metalworking skill from 'Metalworking' to 'Blacksmithing'" in the 42.12.0 notes.
3. **Confirm the knapping surface gate:** in-game, attempt a knapping recipe with tool and flint in hand but no adjacent table; it should be unavailable until at a crafting surface.
4. **Confirm the fluids behaviour:** fill a container from a tainted source and observe the destination becomes tainted; attempt to drink from a >3 L container via the context menu and observe the "too big to drink from" tooltip.
5. **Confirm station tiering:** build a primitive furnace and a smelting furnace and compare their recipe lists at the station UI — the better tier should include the lesser tier's recipes.
6. **Spot-check wiki-derived values:** open the cited revision URLs (each pins an oldid) and diff against the current pages for post-42.20 corrections, especially the Welding wall-tier table and the Masonry level-1 note.

# Open Questions

- Have any chain gates (Welding 2/8 wall tiers, Masonry's crush-only level 1, knapping's recipe ceiling at level 6) changed in 42.20 stable? In-game checks resolve this.
- Did the crafted-item attribute/quality system described in 2022 [2] ship in recognisable form in 42.20, and is it player-visible? Needs first-hand verification or a dev statement.
- Is any brewing/fermentation system planned for the announced Build 42 Support Update? Watch the Thursdoid feed.
- What are the authoritative XP values per crafting recipe on 42.20 (Claim 3)? Game script files (`media/scripts/`) would settle this for a future revision.
- How rare is clay on 42.20 in measurable terms (forage odds, deposit density), given the wiki's qualitative "incredibly rare"? A sandbox test or script-file check would firm this up.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Crafting RamblZ* (Thursdoid, Steam announcement, 2023-04-13). https://steamcommunity.com/games/108600/announcements/detail/6539831443777817851. Accessed 2026-07-30.
- [2] **The Indie Stone** — *Migration vs Craft* (Thursdoid, Steam announcement, 2022-06-23). https://steamcommunity.com/games/108600/announcements/detail/4474904295730796170. Accessed 2026-07-30.
- [3] **The Indie Stone** — *WhatZ Next* (Thursdoid, Steam announcement, 2024-11-28). https://steamcommunity.com/games/108600/announcements/detail/1784506359022970. Accessed 2026-07-30.
- [4] **The Indie Stone** — *Build 42 Unstable Out Now* (Steam announcement, 2024-12-17). https://steamcommunity.com/games/108600/announcements/detail/1785774543698069. Accessed 2026-07-30.
- [5] **The Indie Stone** — *42.3.0 UNSTABLE Released* (patch notes, Steam announcement, 2025-02-11). https://steamcommunity.com/games/108600/announcements/detail/1790848102789684. Accessed 2026-07-30.
- [6] **The Indie Stone** — *42.12.0 UNSTABLE Released* (patch notes, Steam announcement, 2025-09-25). https://steamcommunity.com/games/108600/announcements/detail/1811772772244324. Accessed 2026-07-30.
- [7] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [8] **The Indie Stone** — *Heat of the Night* (Thursdoid, Steam announcement, 2024-09-26). https://steamcommunity.com/games/108600/announcements/detail/6339469370182469339. Accessed 2026-07-30.
- [21] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [22] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441. Accessed 2026-10-07.
- [23] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895. Accessed 2026-10-07.
- [24] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [25] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [26] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [27] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post by Rockjaw, 2026-09-23; retrieved abridged, "selected" lists only). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [9] **PZwiki** — *Crafting* (revision 1440935; page versioned against 42.11.0). https://pzwiki.net/w/index.php?title=Crafting&oldid=1440935. Accessed 2026-07-30. Fact-only source.
- [10] **PZwiki** — *Crafting* (revision 650143, 2024-12-06; page versioned against 41.78.16 — used for the B41 system). https://pzwiki.net/w/index.php?title=Crafting&oldid=650143. Accessed 2026-07-30. Fact-only source.
- [11] **PZwiki** — *Knapping* (revision 1439145; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Knapping&oldid=1439145. Accessed 2026-07-30. Fact-only source.
- [12] **PZwiki** — *Carving* (revision 1436965; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Carving&oldid=1436965. Accessed 2026-07-30. Fact-only source.
- [13] **PZwiki** — *Pottery* (revision 1436229; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Pottery&oldid=1436229. Accessed 2026-07-30. Fact-only source.
- [14] **PZwiki** — *Masonry* (revision 1439137; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Masonry&oldid=1439137. Accessed 2026-07-30. Fact-only source.
- [15] **PZwiki** — *Welding* (revision 1436247; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Welding&oldid=1436247. Accessed 2026-07-30. Fact-only source.
- [16] **PZwiki** — *Blacksmithing* (revision 1436191; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Blacksmithing&oldid=1436191. Accessed 2026-07-30. Fact-only source.
- [17] **PZwiki** — *Glassmaking* (revision 1436231; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Glassmaking&oldid=1436231. Accessed 2026-07-30. Fact-only source.
- [18] **PZwiki** — *Fluid* (revision 1388499; page versioned against 42.15.0). https://pzwiki.net/w/index.php?title=Fluid&oldid=1388499. Accessed 2026-07-30. Fact-only source.
- [19] **PZwiki** — *Fluid container* (revision 1365385; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Fluid_container&oldid=1365385. Accessed 2026-07-30. Fact-only source.
- [20] **PZwiki** — *Skill* (revision 1436755; page versioned against 42.3.1). https://pzwiki.net/w/index.php?title=Skill&oldid=1436755. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited.

**Further Reading**

# Further Reading

- The Steam news API feed used to verify every announcement above: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25
- The official blog / Thursdoid archive: https://projectzomboid.com/blog/ (bot-blocks automated checkers; the Steam mirrors above are the citable copies).
- The Indie Stone's confirmed-features roundup for B42, linked from development-era Thursdoids: https://projectzomboid.com/blog/upcoming-features-b42/ (bot-blocks automated checkers; verify in-browser).

# Related Documents

- `players-foundation` — the Players-track foundation this document deepens (B42 headline changes, skills overview, save compatibility).
- `players-skills-xp` — how skill XP, boosts and skill books work across builds; the levelling context for every chain here.
- `players-traits-occupations` — the occupation and trait roster, including the crafting trades (Blacksmith, Welder) that front-load these chains.
- `players-animals-husbandry` — the animal economy that supplies the leather, bone and brain-tan links in the Blacksmithing chain.
- `modders-foundation` — the craftRecipe/fluid script systems behind this document's player-facing view.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | 42.21 re-baseline against the 42.20.1–42.20.4 hotfix notes, the 42.21 unstable and stable Steam posts and the abridged TIS forum 42.21 changelist: new 'What 42.21 changed' section (Welder Welding recipes, 86 more oven water-purification containers, washing machines clean rags/strips/bandages, antibiotics pack-in-box, CharacterTraitScriptGenerator recipe fix); crafting UI station-removal and Making Sinew animation fixes; stale 'Metalworker' guidance corrected to Welder. Rebase is a patch-notes review, not an in-game re-test. | — |
