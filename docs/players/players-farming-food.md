---
id: players-farming-food
title: "Farming, Foraging and Food: Feeding a Survivor Long-Term"
version: 1.0.0
status: approved
confidence: Medium
category: Players
topic: "Farming & food"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-animals-husbandry, players-crafting-chains, players-skills-xp, meta-style-guide]
tags: [players, farming, agriculture, foraging, cooking, fishing, food-preservation, canning, drying-racks, nutrition, growing-seasons, build-42]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-farming-food |
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

Every Project Zomboid run eventually collides with the same wall: looted food runs out, the electricity dies, and whatever was in the fridge follows it. This document covers the systems that carry a survivor past that wall — crop farming (the skill B41 calls Farming and B42 renames Agriculture), foraging with Search Mode, fishing, trapping at overview level, cooking, food preservation (canning, drying racks, refrigeration against the power shutoff), and the nutrition model that sits underneath all of it. It is a Players-track tier-2 document that goes deeper than the survival-loop overview in `players-foundation` and hands off animal husbandry, hunting and butchering depth to `players-animals-husbandry`.

The headline build story: Build 42 turned crop farming from a small side activity into a calendar-driven system — "advanced crop farming" with a much larger crop roster and realistic growing seasons, where planting in the wrong month curses a crop and winter punishes everything not cold-hardy [21]. B42 also shipped a fishing overhaul with a new tension minigame [21] [19], drying racks as a new food-preservation route [21] [5], per-macronutrient tooltips and rebalanced calorie burn [6] [7], and a foraging system whose zones are now generated automatically and whose XP flows only from finds [21] [7].

Document confidence is **Medium**: the change spine rests on official Steam patch notes (High), but the dense numeric layer — water thresholds, disease math, the crop table, foraging radii — comes from pzwiki revisions versioned against 42.18.0, before the 42.20 stable release, and has not been re-verified in-game on 42.20, 42.21 or 41.78.16.

# Key Takeaways

- Crop farming is called **Farming on B41 and Agriculture on B42**; the internal Skill ID stays `Farming`, so B41 muscle memory (and mod references) still point at the same skill *(cited)* *(both)*
- On B42, **only harvesting crops you planted yourself grants Agriculture XP** — plowing, sowing, watering, weeding and fertilizing give none *(cited)* *(B42)*
- B42's **growing-seasons calendar is unforgiving**: planting outside a crop's season, hitting its bad months, or reaching winter (December–February) curses the crop, and a cursed crop can never be uncursed *(cited)* *(B42)*
- B42 added a large batch of new crops — garlic, corn, rye, barley, peas, flax, hops, sugar beets, industrial hemp, sunflowers, tobacco and hot peppers, plus a herb roster — on top of B41's small vegetable set *(cited)* *(B42)*
- Foraging's Search Mode is shared by both builds (it replaced the old system in 41.60), but B42 generates foraging zones automatically and grants XP only when an item is found, not when it is picked up *(cited)*
- **Fertilizer is a one-per-growth-phase tool**: the first application speeds growth and adds health, repeat applications damage the crop, and a third curses it — compost never harms *(cited)* *(B42)*
- Food preservation has three cited pillars: **canning** (Cooking 8 or the American Homesteading magazine), **drying racks** (herbs one in-game day, leather seven) *(B42)*, and **refrigeration**, which dies with the electricity shutoff on a sandbox-configured random day *(cited)*
- Nutrition tracks calories, proteins, lipids and carbohydrates, activity burns calories at rebalanced per-action rates, and the whole layer can be toggled with a sandbox checkbox *(cited)*
- The B41 crop roster of roughly seven vegetables circulates widely but could not be re-verified against a pre-B42 source during writing *(community, unverified)*

# Purpose

This document answers the question a mid-game player eventually asks: "the canned food is running out and the power just died — how do I eat forever?" It is the Players-track reference for growing, finding, catching, cooking and preserving food across both supported builds, and for how much of that changed between Build 41.78 and Build 42.20. It exists so that a player does not have to reconstruct B42's season calendar, curse rules and disease math from scattered patch notes and unstable-era guides.

# Scope

Covered: the crop-farming skill on both builds (rename, XP model, skill effects, leveling resources); the full B42 farm cycle — seeds, siting, plowing, sowing, seasons, watering, fertilizing, health, curses, diseases, harvest; the B42 crop roster and its per-build differences; foraging (Search Mode, radius math, zones, focus categories, modifiers, B42 changes); fishing at mechanic level; trapping and hunting at overview only; cooking (skill effects and evolved recipes); food preservation (canning, drying racks, refrigeration and the power shutoff, composting as a disposal chain); and the nutrition system at overview.

Not covered: animal husbandry, butchering, tracking and hunting depth (see `players-animals-husbandry`); the crafting tech tree that produces farm tools, pottery and preservation stations (see `players-crafting-chains`); per-skill XP mathematics and skill-book multipliers in general (see `players-skills-xp`); per-item nutrition tables; and unstable-branch behaviour after 42.20.

# Definitions

- **Agriculture** — the B42 name of the crop-farming skill; Skill ID `Farming`, renamed from B41's Farming [16].
- **Growing season** — a crop's calendar profile on B42: a planting window, best and poor months, bad months, and a growth duration [16].
- **Cursed crop** — a B42 crop permanently penalised (halved recovery, doubled losses, reduced yield, doubled disease chance) for being planted or grown at the wrong time or over-fertilized; there is no cure [16].
- **Search Mode** — the foraging interface (default hotkey END) that blurs the screen outside a skill-scaled search radius; introduced when 41.60 replaced the previous foraging system [17].
- **Evolved recipe** — a cooking construction (soup, stew, salad, sandwich and similar) that accepts variable ingredients, each contributing recipe-specific hunger and nutrition [18].
- **Drying rack** — a B42 station that dries plants, herbs and leather over in-game days; part of B42's new food-preservation layer [21] [5].
- **Power shutoff** — the sandbox-scheduled random day on which grid electricity stops, disabling refrigerators and lights [20].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Skill named Farming; foraging Search Mode present since 41.60 [17]; B41-only values tagged *(B41)* |
| B42 (stable) | Yes | 42.20, re-checked against 42.21 patch notes | Skill named Agriculture; seasons, curses, drying racks and the fishing overhaul are B42 systems [16] [21]; B42-only values tagged *(B42)* |

The mechanical core of this document (seasons, curses, disease math, foraging radii, cooking scaling) is cited from pzwiki revisions versioned against 42.18.0 and from unstable-cycle patch notes; 42.20 stable shipped fixes in these systems but no documented redesign of them [15]. The 42.21 stable release (2026-09-28) was reviewed for this document by reading the official Steam announcements for 42.20.1 through 42.21 and the 42.21 forum changelist [24] [25] [26]; only the farming, refrigeration and water-purification items noted in the Reference section changed any statement here, and every other statement is carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found in those notes. That was a patch-note review, not an in-game re-test. Nothing below has been re-verified first-hand on 42.20 or 42.21, and B41-side numeric detail is deliberately thin because pre-B42 wiki revisions could not be re-fetched during writing (see Risks & Caveats).

# Reference

## One skill, two names

Crop farming is governed by a single skill that B41 presents as Farming and B42 presents as Agriculture; the wiki records the rename as a Build 42 change and notes the technical Skill ID remains `Farming` [16]. The sibling document `players-skills-xp` establishes the wider rename pattern (Farming→Agriculture, Metalworking→Welding, Sprinting→Running, all with unchanged IDs); this document goes deeper on what the skill actually does. On the B42-era page the skill sits in a dedicated Farming skill group alongside Animal Care and Butchering *(B42)* [16].

The skill's read-out value is information: at level 3 a hover tooltip reports a crop's growth phase, water level (colour-coded) and any disease with its severity; at level 4 the info window gains a water-level bar; at level 6 the window states the time to the next growth phase in months, weeks, days or hours [16]. Beyond information, the wiki lists five per-level effects, flagged on the page itself as needing B42 verification: each Agriculture level reduces the chance a crop planted in a poor month becomes cursed by 5 percentage points (from a 50% base), raises the bonus-yield chance under best-month or fertilized conditions by 5 points (50–95%), adds 1 initial health to planted crops, deepens disease-level reduction by 1, and adds 1 to yield *(B42)* [16].

Levelling is unusually narrow: on the B42-era revision, the only XP-earning action is harvesting a crop the character planted — plowing, sowing, weeding, watering and fertilizing all give nothing *(B42)* [16]. Harvest XP equals the crop's health at harvest divided by two, plus 25 for a well-kept crop or minus 15 for a neglected one, capped at 100 per crop [16]. Starting boosts come from the Farmer occupation (+4) and Gardener trait (+1); five Agriculture skill books cover level bands 1–2 through 9–10, and a shelf of magazines (American Homesteading, Cropping for Cash, The Farmers Guide and others) teaches recipes and growing seasons to characters who did not start as farmers [16]. Individual seed packets can also be read to learn that crop's season [16]. During the unstable cycle The Indie Stone added a backstop: on reaching skill level 10 a character auto-learns every growing-season recipe not already known *(B42)* [6].

## Starting a farm: seeds, siting, labor

Seeds arrive by five routes on the B42-era page: looted seed packets (five seeds each, most common in barns, gardening shops and farm sheds); extracting seeds from vegetables with tweezers or a knife (destroying the vegetable, whatever its freshness short of rotten); harvesting a crop in its blooming phase, which returns seeds equal to half the vegetables harvested; planting items that carry the seed item tag directly, if fresh or stale (fresh only for herbs); and foraging, which sometimes bundles seeds with wild finds [16]. A few crops never bloom their seeds out and must be extracted, some only after drying — flax additionally requires rippling first [16].

Siting rules: furrows can only be dug on grass or dirt tiles free of bushes, trees and stones; crops must be outdoors for sunlight and at ground level, though sandbox options allow indoor/greenhouse planting and planting on upper floors; dirt can be hauled in sacks with a shovel and placed as dirt flooring to farm anywhere [16]. Zombies walking over crops destroy them and vehicles damage them, while the player's own footsteps are safe; scything grass wipes out any crops caught in the swing [16]. Plowing (any tool with the dig-plow tag, such as a trowel or shovel — no hand-injury risk), sowing and harvesting each apply minor muscle strain on B42 *(B42)* [16].

Build 42.21 *(B42)* adds cosmetic farm-footprint behaviour: player pathfinding now steers around farming plants where possible, and the developers state that characters do not damage crops by stepping on them [24] [26]. The same build removes furrows that zombies trampled entirely from the game and world, and fixes an error that occurred when zombies walked over un-sown furrows [26]. Players on 42.20 or earlier should not assume either behaviour.

## The B42 calendar: seasons, winter and cursed crops

Every B42 crop carries a calendar profile [16]:

| Calendar element | Effect |
|------------------|--------|
| Planting season | Safe months to sow — no curse risk [16] |
| Poor months | Sowing risks a curse at 50% minus 5% per Agriculture level [16] |
| Best months | Sowing adds a bonus-yield chance [16] |
| Bad months | On the first day of the crop's first bad month, every crop of that kind in the world is cursed; sowing during them curses too [16] |
| Winter (Dec–Feb) | On the first day of winter all non-cold-hardy crops globally become cursed [16] |

A cursed crop halves its health gains from sun and good watering, doubles its losses from cold, darkness, thirst, bad months and winter, doubles its disease chance, loses bonus yield and — through the health loss — ordinary yield; nothing uncurses a crop [16]. Over-fertilizing (three or more fertilizer applications) is the one player-inflicted curse route [16]. Two hardiness flags mitigate the calendar: cold-hardy crops ignore winter cursing and sub-10 °C health penalties, and bad-month-hardy crops shrug off their bad months once they have reached the growth phase matching their hardiness level [16].

Growth runs through seven phases — seedling (1–2), young (3–4), almost ready (5), ready to harvest (6) and blooming (7) — with harvest possible at 6 or 7 but seeds returned only from blooming; an unharvested blooming crop rots when its next phase would have arrived [16]. Some crops regrow from phase 2 after harvest for repeat pickings [16]. Average growth times in the B42-era crop table run from 30 days (radish) through 60–108 for most vegetables and herbs to 240 days for garlic, hemp, hops and wild garlic; each phase's timing also wobbles randomly by as much as half a day [16]. The developers treat the calendar as a live gameplay concern — the "Spring is Here" post closes by telling players to check growing seasons before sowing spring crops *(B42)* [11] — and season knowledge got dedicated magazines during unstable, including a Herbal Remedy Growing magazine after wild-herb seasons were split out of Wilderness Survival [4].

## Water, health, fertilizer

A newly sown B42 crop starts at water 0 and must be raised into its comfort band; watering pours 10 units per action from any water container, and rain contributes at intensity-scaled rates [16]. The page's water bands: 0–29 parched, 30–59 dry, 60–69 thirsty, 70–89 fine, 90–100 well watered — but what matters is each crop's own minimum (30 for hardy field crops like barley and corn up to 80 for cabbage, basil and strawberries): at or above minimum a crop gains 0.4 health per 3 hours; 1–10% below, growth is delayed an hour per missing point; 10–30% below, growth halts and 0.2 health drains per 3 hours; beyond 30% below, the drain is 0.5; at water 0 the crop dies [16]. Any deficit also raises disease risk [16].

Crop health runs 0–100, starting around 50 with a moon-phase modifier (descending moon 37–44, ascending 47–53, full 57–64), updating every 3 hours: sunny weather adds 1, overcast 0.25, and temperatures below 10 °C subtract 0.25 unless the crop is cold hardy [16]. Every 10 health above 50 at harvest adds one vegetable to the yield [16].

Fertilizer and compost are first-application tools: the first use in a growth phase cuts 40 hours from that phase (20 if weeded-over), adds 10 health, and — in phases 1–3, on an uncursed, weed-free crop — can trigger bonus yield [16]. A second fertilizer application in the same phase instead removes 25 health, and a third curses the crop; compost repeated is merely wasted, never harmful [16]. Neither helps in winter or at phases 6–7 [16]. Compost comes from a composter (buildable at Carpentry 3 or scavenged from backyards) fed stale or rotten food, breaking down over two in-game weeks by default — the interval is a sandbox option ("Compost Time") [16] [20]. Weeds that erode onto crop tiles halve fertilizer's time cut, double water loss and disease chance, halve health gain, double health loss and deny fertilizer bonus yield; plowing clears them [16].

## Diseases

B42 crops face four diseases — mildew, pest flies, slugs and aphids — rolled at each new growth phase against a 2% base chance, halved by bonus yield, doubled by weeds or a curse, and modified by the Plant Resilience sandbox setting; disease also spreads from diseased crops one tile away with the same per-crop odds [16]. Pest flies, slugs and aphids cannot infect during winter or at or below 10 °C [16]. Untreated disease grows every 2 hours (0.5 for mildew/flies/slugs on a well-watered crop, 1 when underwatered, 1 for aphids regardless); at level 10–29 growth is delayed, at 30–59 stopped, and at 60+ the crop dies on its next phase [16]. Aphids and slugs also strip one vegetable of yield per 10 disease points, while pest flies drain an extra water point per 10 [16].

Cures for mildew, pest flies and aphids are craftable sprays — each needs an empty gardening spray can plus milk (mildew), tobacco in several forms or rubbing alcohol (flies/aphids), unlocked by the Farmer occupation, Gardener trait, the Kentucky Farmer magazines, or Agriculture 6 — while a slug cure exists only as looted slug repellent [16]. Insect repellent also treats flies, and aphids can be starved by deliberately underwatering: 2 disease points fall per 2 hours below minimum water, the same decay all three pest diseases show in winter [16]. Some crops are outright immune to specific pests and, from growth phase 3, even shield adjacent non-immune crops [16]. One naming footnote for returning players: B41's disease roster called the aphids slot "Devil's Water Fungi"; B42 renamed it [16].

## The crop roster per build

The B42-era crop table lists over fifty plantable crops split between vegetables and herbs, from 30-day radishes to 240-day garlic, each with its own minimum water, seasons and hardiness flags [16]. The Build 42 overview page states the expansion directly: advanced crop farming arrived with a fresh crop roster and realistic growing seasons; among the newcomers it lists garlic, corn, rye, barley, peas, flax, hops, sugar beets, industrial hemp, sunflowers, tobacco and hot peppers, together with a wide spread of herbs such as rosemary *(B42)* [21]. The exact pre-B42 roster is quarantined below (Claim 1) because no pre-B42 revision could be re-verified during writing.

## Foraging: Search Mode on both builds

Foraging's current shape is shared by the builds: 41.60 replaced the old click-to-scavenge system with Search Mode, and the B42-era page states the system itself has not structurally changed even as its data went through heavy backend rework [17]. The skill (ID `PlantScavenging`) governs what can be found, how far away it registers, item rarity, which Search Focus categories are unlocked, and the poison risk of berries and mushrooms — the page gives the poison roll as the item's base chance plus five times (10 minus foraging level) [17]. XP comes from finding items; on B42, The Indie Stone explicitly removed XP from the pickup action so only finds pay, added a distance bonus for widely spaced finds *(B42)* [7], and then hotfixed an over-generous XP rate shortly after [8].

Mechanically: toggling Investigate Area opens the overlay (terrain type, sun position) and Search Mode (default END) blurs everything outside a target radius of 3–10 tiles, extendable to 15 with bonuses; each foraging level adds 0.7 tiles [17]. When the character comes within radius of an item their level can find, an eye icon appears, lingering reveals the item and grants the XP, and a double-click collects it [17]. The radius is squeezed by darkness (up to −95%; above −50% no new items can be spotted and the floor drops from 3 tiles to 1.5 — a light source negates darkness entirely), by rain, snow and fog (up to −75%, an umbrella cutting the rain share by 90%), by face-covering clothing (−2.5% for glasses up to −75% for full head coverage, capped at −95% total), by moodles (hunger helps find food, up to +50%; panic, sickness and pain families reach −75 to −95%), and by movement (aiming +33%, sneaking +10%, running or sprinting −100%) [17]. During unstable, rain and snow bonuses were changed to scale with precipitation intensity instead of a flat percentage *(B42)* [4], and a fix stopped the darkness penalty from flickering when foraging by flashlight [12].

What appears depends on level, category, month and zone. Categories unlock progressively — berries, mushrooms, firewood, stones, junk, trash, medical supplies and junk food from level 0, wild vegetables and forest rarities at 2, ammunition and wild fruit starting at 4, dead animals from level 5 upward, traps and hiking bags at 8, and top-end finds like dead rabbits at 10 [17]. Search Focus, unlocked per category between levels 0 and 7, biases drops toward a chosen category at the expense of the rest [17]; on B42 the focus and sprite-affinity systems were reworked to play a much larger role in what actually spawns *(B42)* [3]. Zones weight the tables: firewood dominates deep forest, berries and mushrooms the forests, crops and produce the farmland, stones the roads, and trash the towns and trailer parks; "Nothing Here" zones yield nothing [17]. Seasonality is sharp — most organic categories vanish in winter, some berries exist only in fall and winter, and firewood spikes +50% in fall [17]. The sandbox "Nature's Abundance" setting scales zone density from −75% to +100% [17]. On B42 the zones themselves are generated automatically together with map biomes [21]; a 42.13.1 hotfix fixed zones failing to generate [8], mod items became foragable in 42.18 *(B42)* [12], and 42.20 closed an exploit that manipulated forage-spawned items [15].

Occupations and traits mostly stretch the spotting distance for themed categories — a Park Ranger reads the deep woods (+2 base radius and big bonuses across wild categories), a Fishing Guide spots bait, a DIY Expert or Mechanic spots trash and junk at +33% — while Short Sighted (−2 tiles, removable with glasses), Agoraphobic and Unlucky shrink it [17]. The Bushcrafter and Herbalist traits or the herbalist magazine unlock poison identification for berries and mushrooms and the poultice-crafting chain from medicinal plants (plantain for wounds, comfrey for fractures, wild garlic against infection, black sage for pain, common mallow for colds, ginseng for endurance, lemongrass against food poisoning) [17].

## Fishing

B42 shipped a fishing overhaul: a new minigame by Aiteron, procedurally determined fish groups with their own locations, sizes and behaviors, and fishing zones that react to noise and can be baited with chum *(B42)* [21]. On the current page, fishing requires a rod and bait; the cast targets water (ripples are the best odds), and a tension meter drives the catch — reel to bring the fish in, give slack when it fights, and keep tension from snapping or degrading the line [19]. Rods do not lose durability from fishing, but lines break: relining consumes a nail or paperclip plus twine or fishing line [19]. Makeshift rods are craftable, and fishing nets catch bait fish [19]. Fish come in three size classes per species with a random size roll; a fish's hunger reduction is its weight times ten, and weight derives from length divided by a per-species modifier [19]. Live bait skews the size distribution to 50/30/20 (small/medium/big) against 60/25/15 for tackle [19]. XP scales with the weight of the catch, and higher skill pulls bigger, fattier fish [19]. The page's own tips: dusk (18:00–21:00) and dawn (04:00–07:00) buff catches, as does standing seven-plus tiles into the water ("deep water"), and line tension telegraphs what is hooked — trash barely pulls [19]. The Fishing Guide occupation starts at +3 [19].

## Trapping and hunting, at overview

Trapping is a survivalist skill adjacent to foraging: box, cage, crate, mouse, snare and stick traps can themselves be foraged at level 8, and forage-caught worms, crickets, grasshoppers and cockroaches double as stick-trap and fishing bait (since 41.77, caterpillars, millipedes and slugs no longer function as bait for stick traps) [17]. Build 42 was originally framed as the "Hunting update", planned around roaming wildlife and an expanded trapping system [21]. The trait economy around it moved during the B42 cycle: the Hunter trait and occupation swapped their +1 Trapping for +1 Tracking, and the Hiker trait (+1 Trapping, +1 Foraging) got a cost cut *(B42)* [13] [14]. Everything deeper — wild-animal behavior, tracking, butchering yields, hunting workflow — lives in `players-animals-husbandry` and is deliberately not duplicated here.

## Cooking and evolved recipes

The Cooking skill (a crafting skill on both builds) stretches ingredients and nutrition: per the B42-era table, ingredient consumption in evolved recipes falls from 100% at level 0 to 70% at level 10 while nutrition contributed per ingredient climbs to about 117% (with such extreme diminishing returns that level 10 is fractionally below level 9), and at level 7 small amounts of rotten food become safe to include (5%, then 10% at higher level) [18]. Cooking also runs the poison-detection duel: any evolved recipe holding at least three ingredients is a valid poisoning target, and spotting the poison requires a cooking level three above the poisoner's, scaling up their level [18]. XP flows from cooking on heat sources, from cooking craft recipes, and from adding ingredients to evolved recipes; Burger Flipper starts +2 and Chef +4 [18].

Evolved recipes inherit age only from their base ingredient — a stale bread makes a stale sandwich — while non-rotten added ingredients contribute regardless of staleness, which is why stale-first cooking is the efficient pattern [18]. Each ingredient's hunger contribution is recipe-specific (a potato gives a soup 15 hunger but beef jerky gives a sandwich only 5), partial ingredients return to inventory, and higher cooking levels subtract less from the ingredient while contributing more to the dish [18]. Spices add boredom and unhappiness relief on top of the recipe's own bonuses [18]. During unstable, product-splitting was automated so that soup poured into bowls carries its nutrition, cooked state and any poison through correctly [7].

## Food preservation

**Canning.** The B42-era cooking page carries a preserved-food recipe: a jar and lid, vinegar, salt, water and six units of a vegetable (bell peppers, broccoli, cabbage, carrots, eggplant, leeks, potatoes, radishes, tomatoes — or fish roe) make a jar of preserved food, unlocked by the American Homesteading magazine or Cooking 8 [18]. Jars found in the world were aligned with player-made ones during unstable so both take equally long to go stale or rotten *(B42)* [7].

**Drying.** Build 42's feature list names food preservation with drying racks as a new system [21]. Patch notes flesh it out: plant drying racks buildable from sticks and rags (no twine needed) [2], variable batch sizes per rack [6], herb drying set to one in-game day and leather to seven [5], dried corn, peas and soybeans carrying real hunger and nutrition values [6], racks made functional in multiplayer in 42.13.2 [9], sped back up in 42.18 [12], and still collecting fixes in 42.19 and 42.20 stable [14] [15]. No salting or smoking preservation chain for food surfaced in any primary source reviewed for this document — cigarettes are the only "smoking" in the patch notes.

**Refrigeration and the shutoff clock.** The sandbox defines the race: water and electricity each stop on a random day inside a configured window (instant, 0–30 days, 0–2/2–6/6–12 months, up to five years, or never), and the electricity shutoff explicitly stops refrigerators and lights working [20]. Two further sandbox dials govern the aftermath — Food Spoilage speed, and Refrigeration Effectiveness stated in days (20/50/100/200/500 across its steps) [20]. Freezers and fridges also slow animal-corpse decay [6], eggs stored in a fridge go too cold to stay fertilized [1], and unstable-cycle fixes tightened the details: non-standard fridges failing to chill properly (42.18) [12] and frozen-versus-freezing display states (42.19) [14]. Build 42.21 *(B42)* changed two further details: fridges and freezers now warm gradually on the day the power goes out, and refrigeration is applied correctly to food items carried in a bag inside a fridge or freezer [25] [26]. Build 42.21 also fixes the Seasoning label not appearing on the food tooltip for food without Spices [26]. Build 42.21 also lets 86 more fluid containers purify water in the appropriate oven type and lets washing machines clean dirty rags, strips and bandages [25] [26].

## Nutrition, at overview

Food carries calories, proteins, lipids and carbohydrates — B42's fluid tooltips list all four for the container's current contents *(B42)* [7] — and activity burns calories at per-action metabolic rates that were rebalanced during unstable to cost less for common tasks and rest, and more for intensive ones *(B42)* [6]. Even sitting in a vehicle has a defined burn rate (a 42.18 fix corrected it) [12]. Fishing illustrates the survival meaning: the wiki calls fish high-satiety, high-calorie food capable of fattening a survivor up [19]. The whole layer is optional — a sandbox checkbox controls whether food's nutritional value affects the character's condition [20]. The Nutritionist trait exposes nutrition values on unpackaged food and was repriced from −4 to −2 points during the B42 cycle *(B42)* [10] [23]. Deeper weight mechanics (weight bands, weight-linked traits) belong to the traits/occupations documents rather than here.

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 / 42.21 *(B42)* |
|------|---------------------|---------------------|
| Skill identity | Farming | Agriculture; Skill ID still `Farming`; sits in a new Farming skill group [16] |
| Farming model | Pre-seasons crop farming (roster quarantined — Claim 1) | "Advanced crop farming": growing seasons, poor/best/bad months, winter cursing, moon-phase starting health, hardiness flags [16] [21] |
| Crop roster | Small vegetable set (Claim 1) | Adds garlic, corn, rye, barley, peas, flax, hops, sugar beets, hemp, sunflowers, tobacco, hot peppers and a herb roster [21] |
| Disease naming | "Devil's Water Fungi" among crop threats | Renamed to aphids; four-disease system with craftable cures [16] |
| Farm labor | No muscle-strain system | Plowing, sowing and harvesting apply minor muscle strain [16] |
| Season knowledge | Not applicable | Learned from magazines and seed packets; all seasons auto-learned at Agriculture 10 [4] [6] [16] |
| Foraging system | Search Mode since 41.60 [17] | Same Search Mode; zones/biomes generated automatically [21]; XP only on finds plus a spacing bonus [7]; Search Focus and sprite affinity reworked to matter more [3]; rain/snow modifiers scale with intensity [4]; mod items foragable [12] |
| Fishing | Pre-overhaul fishing | New minigame (tension/reel/slack), procedural fish groups, noise-reactive zones, chum [19] [21] |
| Trapping/hunting | Trapping present; stick-trap bait list trimmed in 41.77 [17] | Framed by the "Hunting update" plan; Hunter trait/occupation moved from +1 Trapping to +1 Tracking; Hiker cheaper [13] [14] [21] |
| Preservation | Canning-era toolset; no drying racks | Drying racks added (herbs 1 day, leather 7 days; buildable from sticks and rags) [2] [5] [21] |
| Nutrition display | Nutrition system present, coarser display | Calories/proteins/lipids/carbohydrates on fluid tooltips; per-action calorie burn rebalanced [6] [7] |
| Trait pricing | B41-era costs | Nutritionist −4 → −2 during B42 cycle [10] |
| Refrigeration at shutoff *(42.21)* | Not covered by the 42.21 notes | Fridges/freezers warm gradually on the day power goes out; bagged food refrigerates correctly [25] [26] |
| Farm plots *(42.21)* | Not covered by the 42.21 notes | Pathfinding avoids plants (cosmetic); zombie-trampled furrows removed from the game [24] [26] |

One-line version: the food loop's verbs are the same on both builds — plant, forage, fish, cook, preserve — but B42 wraps them in a calendar (seasons and curses), a bigger roster (crops and fish behavior), a new preservation station (drying racks), and a sharper nutrition read-out [7] [16] [21].

# Practical Guidance

- **On B42, read the calendar before the trowel.** A crop sown outside its window is cursed forever; check its season via seed packets, the farming magazines, or the Discovered Recipes panel, and treat December–February as a no-sow zone unless the crop is cold hardy. Radish (30 days) is the fastest safe experiment; garlic-class crops (240 days) are a commitment that must clear their bad months.
- **Never double-fertilize in one growth phase.** First application in a phase = faster growth and +10 health; second = −25 health; third = permanent curse. When unsure whether a phase was already fed, use compost — over-application of compost is wasted, never harmful.
- **Level Agriculture by harvesting, not busywork.** Since only self-planted harvests pay XP (health/2, bonus for good care), many small, healthy, fast crops out-level a few grand ones; skill books multiply the gains as usual (see `players-skills-xp`).
- **Forage like a stat sheet.** Walk or sneak (never run), carry a light source at night, drop the balaclava, and set a Search Focus once unlocked — with darkness beyond −50% you cannot spot anything new, and clothing plus weather penalties stack toward −95%.
- **Fish the edges of the day.** Dusk and dawn buff catches, deep-water positions (seven tiles out, e.g. a pier) buff again, and line tension tells you whether to bother reeling — near-zero pull is trash.
- **Preserve in layers before the power dies.** The shutoff day is random within the sandbox window, so run all three pillars early: can surplus vegetables (Cooking 8 or the magazine), dry herbs and batches on racks, and treat the fridge/freezer as the short-term layer it is. After shutoff, refrigerators are furniture.
- **Cook stale, add fresh.** Only the base ingredient's age carries into an evolved recipe, so build on fresh bases and burn stale ingredients as add-ins before they rot; from Cooking 7, even small rotten fractions become usable.
- **Feed the composter, not the bin.** Stale and rotten food becomes compost in about two weeks — a safe fertilizer stream that closes the farm loop.

# Common Pitfalls & Troubleshooting

- **"My whole field died overnight."** Check the date: the first day of winter, or of that crop's first bad month, curses every instance of that crop worldwide — this is calendar damage, not disease [16].
- **"Fertilizer is killing my plants."** It is the repeat-application penalty: −25 health for a second use per phase, curse on the third. Switch to compost [16].
- **"Watering and weeding aren't levelling my skill."** Working as documented — on the B42-era revision, only harvesting your own plants grants Agriculture XP [16].
- **"I can't find anything foraging at night/in this outfit."** Darkness past −50% blocks new spots entirely; face-covering clothing and weather stack penalties toward −95%. Equip a light and clear your face [17].
- **"Foraging XP feels different from my unstable-era run."** It changed during the cycle: XP was moved off pickups onto finds, a distance bonus was added, and an over-high XP rate was hotfixed [7] [8].
- **"My fishing rod broke."** Rods do not wear from fishing, but lines snap under tension — reline with a nail or paperclip plus twine or line, and slacken when the fish fights [19].
- **"Food in my fridge went bad while the lights were on" (MP/edge cases).** Unstable-era bugs on non-standard fridges failing to apply the refrigeration modifier were fixed in 42.18; if you see this on 42.20, it is report-worthy, not a mechanic [12].
- **"My jarred food rotted."** Preserved jars are not immortal — they age on the same stale/rot track whether player-made or world-spawned [7].
- **"I'm following a B41 farming guide on B42."** Its crop list, season-free planting advice and disease names are stale: the skill, roster, calendar and curse system all changed [16] [21].

# Community Notes & Unverified Claims

## Claim 1 — Build 41's plantable crop roster was seven vegetables

- **Claim:** Community guides and B41-era wiki material commonly list B41 farming as growing cabbage, carrots, broccoli, radishes, strawberries, tomatoes and potatoes, and nothing else.
- **Why unverified:** No pre-B42 pzwiki revision could be re-fetched during writing (automated access to pzwiki was Cloudflare-blocked at research time), and The Indie Stone never published an official B41 crop list; the B42 "new crops" announcement list [21] is consistent with this roster but does not confirm it.
- **Confidence:** Medium. The roster is stated uniformly across years of community material and nothing in the cited B42 additions contradicts it, but it rests entirely on community sources here.

## Claim 2 — B41 farming had no planting-season restrictions

- **Claim:** Community discussion holds that on B41 any crop could be sown in any month, with winter slowing growth but no curse mechanic, making B42's calendar an entirely new constraint rather than a rework.
- **Why unverified:** The B42-era Agriculture revision documents only the current system; no primary source describing B41's absence of a season calendar was found, and the pre-B42 wiki state could not be re-checked.
- **Confidence:** Medium. The Build 42 feature framing ("realistic growing seasons" as a new feature [21]) supports the direction of the claim, but the precise B41 behaviour is unverified.

## Claim 3 — Aphids can be cured for free by deliberate dehydration faster than sprays are worth crafting

- **Claim:** Community farming guides recommend never crafting aphid spray, since underwatering drains 2 aphid points per 2 hours and the crop can be re-watered afterward.
- **Why unverified:** The underlying rate is wiki-documented [16], but the "always better than sprays" efficiency judgement is community synthesis with no primary balance statement, and the interaction with the underwatering health drain has no cited net-outcome math.
- **Confidence:** Medium. The mechanic is cited; only the optimality claim is unverified.

# Risks & Caveats

- **42.21 re-baseline is notes-only.** The 42.21 review read the patch notes [24] [25] [26]; the gradual fridge warm-up has no published duration, and no value in this document was re-tested in-game on 42.21.
- **Numeric layer is 42.18-era.** The Agriculture, Foraging, Cooking and Fishing revisions cited here are all versioned against 42.18.0, two unstable releases before 42.20 stable; the Agriculture page additionally flags its per-level effects list as needing verification. 42.20's notes show fixes, not redesigns, in these systems [15], but no value below was re-verified in-game on 42.20.
- **B41-side thinness.** pzwiki could not be reached by automated fetch during writing (two attempts, both Cloudflare-blocked), so no pre-B42 revision could be pinned for B41 crop farming; B41 specifics are quarantined rather than cited. A future revision should pin a 2024-era Farming revision the way `players-foundation` pinned the B41 occupation roster.
- **Unstable-era patch-note citations.** Many B42 facts (drying times, foraging XP model, nutrition tooltips, metabolic rebalance) are cited from 42.x unstable announcements; they describe the lineage that produced 42.20 but each could have been adjusted again before stable without a traceable note.
- **Wiki-flagged uncertainty.** The Foraging page carries both-builds and outdated banners, and its recipe section is explicitly still B41-based; its numeric tables (radius factors, zone weights) may lag the B42 backend rework it acknowledges [17].
- **Sandbox defaults vs presets.** The shutoff windows, spoilage rates and refrigeration values cited are the sandbox option ranges; individual presets (Apocalypse, Six Months Later, etc.) pin different points in those ranges [20].

# Verification Steps

1. **Season/curse check (B42, 42.20):** sow any crop in a poor or bad month in a debug or sandbox game, advance time, and confirm the cursed state and its info-window presentation against the rules cited from [16].
2. **XP model check (B42):** plow, sow, water and weed with the skills panel open (no XP should register), then harvest a self-planted crop and confirm XP ≈ health/2 with the care bonus [16].
3. **Fertilizer penalty check:** apply fertilizer twice in one growth phase and watch health drop by 25 on the second application [16].
4. **Foraging radius check:** compare Search Mode's visible radius at foraging 0 versus a higher level (+0.7 tiles per level), then equip a balaclava and observe the penalty [17].
5. **Preservation clocks:** dry herbs on a rack (expect roughly one in-game day) and leather (seven) [5]; make a preserved jar at Cooking 8 and leave a world-found jar beside it to compare aging [7] [18].
6. **Shutoff behaviour:** set Electricity Shutoff to "Instant" in a custom sandbox and confirm fridges stop preserving from day one [20]; on 42.21 also watch whether contents warm gradually on the shutoff day rather than instantly [26].
7. **Sources spot-check:** open the pinned pzwiki revision URLs below (oldid links) and diff against the current pages for post-42.20 corrections; pull the cited Steam announcements via the news API (`https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0`).

# Open Questions

- What exactly was B41's crop roster and season behaviour? Resolving Claims 1–2 needs a pinned pre-B42 wiki revision or a legacy41 in-game check.
- Do the Agriculture per-level percentages (curse reduction, bonus-yield chance) hold on 42.20? The wiki flags them for verification [16].
- Did 42.20 stable adjust any drying-rack timings after the 42.18 "drying faster again" change [12]? The stable notes list rack fixes but no times [15].
- Is there any primary-sourced salting or smoking food-preservation chain in B42? None surfaced in the reviewed announcements; the question stays open rather than answered in the negative.
- How long does the 42.21 gradual fridge and freezer warm-up take on the shutoff day? The notes state the behaviour but give no duration [26].
- How do the reworked B42 foraging zone generation and sprite-affinity systems change the wiki's B41-derived zone weight table [17]? Needs data-file inspection (`forageDefinitions.lua`) on a 42.20 install.

# References

**Primary Sources**

- [1] **The Indie Stone** — *42.2.0 UNSTABLE Released* (Steam announcement, 2025-01-27; retrieved via Steam news API, app 108600). https://steamcommunity.com/games/108600/announcements/detail/1789580505447361. Accessed 2026-07-31.
- [2] **The Indie Stone** — *42.3.0 UNSTABLE Released* (Steam announcement, 2025-02-11). https://steamcommunity.com/games/108600/announcements/detail/1790848102789684. Accessed 2026-07-31.
- [3] **The Indie Stone** — *42.6.0 UNSTABLE Released* (Steam announcement, 2025-03-24). https://steamcommunity.com/games/108600/announcements/detail/1794830911001792. Accessed 2026-07-31.
- [4] **The Indie Stone** — *42.8.1 UNSTABLE Released* (Steam announcement, 2025-05-20). https://steamcommunity.com/games/108600/announcements/detail/1799817379626544. Accessed 2026-07-31.
- [5] **The Indie Stone** — *42.11.0 UNSTABLE Released* (Steam announcement, 2025-08-04). https://steamcommunity.com/games/108600/announcements/detail/1806698490822145. Accessed 2026-07-31.
- [6] **The Indie Stone** — *42.12.0 UNSTABLE Released* (Steam announcement, 2025-09-25). https://steamcommunity.com/games/108600/announcements/detail/1811772772244324. Accessed 2026-07-31.
- [7] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972. Accessed 2026-07-31.
- [8] **The Indie Stone** — *42.13.1 BETA HOTFIX Released* (Steam announcement, 2025-12-18). https://steamcommunity.com/games/108600/announcements/detail/1819386365089349. Accessed 2026-07-31.
- [9] **The Indie Stone** — *42.13.2 UNSTABLE HOTFIX Released* (Steam announcement, 2026-01-19). https://steamcommunity.com/games/108600/announcements/detail/1821922921821035. Accessed 2026-07-31.
- [10] **The Indie Stone** — *Build 42.17.0 Unstable Released* (Steam announcement, 2026-04-20). https://steamcommunity.com/games/108600/announcements/detail/1830163047266254. Accessed 2026-07-31.
- [11] **The Indie Stone** — *SPRING IS HERE* (Thursdoid, Steam announcement, 2026-05-08). https://steamcommunity.com/games/108600/announcements/detail/1832065502816211. Accessed 2026-07-31.
- [12] **The Indie Stone** — *Build 42.18.0 Unstable Released* (Steam announcement, 2026-05-11). https://steamcommunity.com/games/108600/announcements/detail/1832065502820909. Accessed 2026-07-31.
- [13] **The Indie Stone** — *REINFORCING THE BARRICADES* (Thursdoid, Steam announcement, 2026-05-29). https://steamcommunity.com/games/108600/announcements/detail/1833968530890581. Accessed 2026-07-31.
- [14] **The Indie Stone** — *Build 42.19.0 Unstable Released* (Steam announcement, 2026-06-01). https://steamcommunity.com/games/108600/announcements/detail/1833968530897275. Accessed 2026-07-31.
- [15] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [24] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [25] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [26] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post, 2026-09-23). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [16] **PZwiki** — *Agriculture* (revision 1439053; page versioned against 42.18.0; per-level effects flagged by the page for verification). https://pzwiki.net/w/index.php?title=Agriculture&oldid=1439053. Accessed 2026-07-31. Fact-only source.
- [17] **PZwiki** — *Foraging* (revision 1442363; page versioned against 42.18.0, carries both-builds and outdated banners). https://pzwiki.net/w/index.php?title=Foraging&oldid=1442363. Accessed 2026-07-31. Fact-only source.
- [18] **PZwiki** — *Cooking* (revision 1436197; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Cooking&oldid=1436197. Accessed 2026-07-31. Fact-only source.
- [19] **PZwiki** — *Fishing* (revision 1435471; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Fishing&oldid=1435471. Accessed 2026-07-31. Fact-only source.
- [20] **PZwiki** — *Custom Sandbox* (revision 1442995). https://pzwiki.net/w/index.php?title=Custom_Sandbox&oldid=1442995. Accessed 2026-07-31. Fact-only source.
- [21] **PZwiki** — *Build 42* (revision 1443663). https://pzwiki.net/w/index.php?title=Build_42&oldid=1443663. Accessed 2026-07-31. Fact-only source.
- [22] **PZwiki** — *Build 42.20.0* (revision 1443641; release-overview framing of B42's food and farming systems). https://pzwiki.net/w/index.php?title=Build_42.20.0&oldid=1443641. Accessed 2026-07-31. Fact-only source.
- [23] **PZwiki** — *Trait* (revision 1442751; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Trait&oldid=1442751. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited (community material is quarantined above, not cited as fact).

**Further Reading**

# Further Reading

- The 42.20 stable release overview's own framing of the build — deeper crafting, animals feeding "farming, food production" and long-term self-sufficiency — is summarised on the wiki's release page [22] and in the release announcement [15].
- The Steam news API feed used to verify every announcement cited here: `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0`
- The official blog mirror of the Thursdoids: https://projectzomboid.com/blog/ (bot-blocks automated checkers; verify in-browser).

# Related Documents

- `players-foundation` — parent overview; this document deepens its survival-loop and B42-headline sections on the food axis.
- `players-animals-husbandry` — the other half of food self-sufficiency: livestock, produce, hunting, tracking and butchering depth referenced (not duplicated) here.
- `players-crafting-chains` — the tech tree that builds the farm tools, composters, racks and preservation stations this document uses.
- `players-skills-xp` — the XP mathematics, book multipliers and the rename pattern (Farming→Agriculture) this document builds on.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed Steam announcements 42.20.1-42.21 and the 42.21 forum changelist [24] [25] [26]; added pathfinding, seasoning-tooltip fix, trampled-furrow, fridge warm-up, bagged-food refrigeration, oven water purification and washing-machine items; version-scope statements updated. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
