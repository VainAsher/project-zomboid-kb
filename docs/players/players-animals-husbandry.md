---
id: players-animals-husbandry
title: "Animals and Husbandry in Build 42"
version: 0.1.0
status: in-review
confidence: Medium
category: Players
topic: "Animals & husbandry"
build: B42
document_type: reference
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [players-foundation, players-skills-xp, players-crafting-chains, players-traits-occupations, meta-style-guide]
tags: [players, animals, husbandry, animal-care, butchering, tracking, breeding, genetics, hunting, build-42]
game_versions_verified: ["42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-animals-husbandry |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Players |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 42.20 |

# Executive Summary

Build 42 puts living, interactable animals into Knox Country for the first time: livestock you can pen, feed, milk, shear and breed, and wild animals you can track through the woods and hunt [1] [8]. The system was the single largest recipient of development attention on the animal side of Build 42 — The Indie Stone themselves noted that husbandry received "more than the lion's share" of the work compared to hunting [1]. This document goes one level deeper than the Players foundation overview: which species exist, how feeding, enclosures and livestock zones work, what the Animal Care, Butchering and Tracking skills do, how breeding and genetics operate at overview level, and what the animals actually give you — meat, milk, eggs, wool and leather.

For returning players the headline is simple: none of this existed in Build 41, where animal life meant trapping small game for corpses, fishing, and ambience. Build 42 adds ten species with life stages, breeds, sexes and a genome, plus three new skills (Animal Care, Butchering, Tracking) and dedicated occupations to match [8] [11] [12].

Document-level confidence is **Medium**. The design spine rests on official Indie Stone Thursdoids and the 42.20 stable release notes (High), but the most detailed numeric source — the pzwiki Animal page — is versioned against unstable 42.6.0, and several mechanics announced during development (for example fox raids on henhouses) have not been re-verified on 42.20.

# Key Takeaways

- Build 42 introduces living animals with their own AI; the cited roster covers ten species: chickens, cows, deer, mice, pigs, rabbits, raccoons, rats, sheep and turkeys *(cited)*
- Livestock exist to feed the new crafting economy: milk, eggs, wool, meat, and hides that go through a full tanning chain into leather *(cited)*
- Animals have breeds with different strengths — Angus cattle for meat, Holstein for milk, Simmental in between — and a two-allele genetics system where careless inbreeding can surface genetic illness *(cited)*
- Hungry or thirsty animals lose health until they die; undersized enclosures dramatically slow growth, cutting daily weight gain by a factor of eight *(cited)*
- Animal Care is a new Farming-family skill that improves the information you can read off an animal and the resources harvested from it; Rancher starts at +4 Animal Care and +3 Butchering *(cited)*
- Butchering on a butcher hook yields more meat plus an unprocessed hide, and 42.20 further increased meat cuts from large animals on the hook; roadkill yields significantly less meat than a clean kill *(cited)*
- Wild deer and rabbits migrate along paths and leave physical evidence — prints, droppings, broken twigs, flattened plants — readable through Search Mode with the Tracking skill *(cited)*
- Zombies are attracted by animal noise but do not attack animals under default sandbox settings, and animals cannot catch the Knox Infection *(cited)*
- Community guides state livestock zones can be drawn from the context UI without fencing, and some describe a "Tame" interaction — neither is confirmed by a primary source *(community, unverified)*

# Purpose

This document answers the Players-track questions: what animals are in Build 42, how do I keep them alive and productive, which skills and character choices matter, how does breeding work at a practical level, and how do I hunt the wild ones? The foundation document (`players-foundation`) states *that* animals arrived in Build 42; this document explains *how the system works*. It is written for players on 42.20 stable, flagging wherever a value was established during the unstable cycle and has not been re-checked.

# Scope

Covered: the animal roster and its per-species life stages; acquiring and moving livestock (zones, ropes, trailers) as far as primary sources describe it; feeding, troughs, grazing and enclosure sizing; animal health and the Animal Care skill; breeding and genetics at overview level (no exhaustive gene tables); produce — milk, eggs, wool, meat — and the Butchering skill including the tanning chain; wild animals, hunting and the Tracking skill; and dangers around animals (zombie attraction, announced predator behaviour).

Not covered: per-breed stat tables beyond illustrative examples, trapping and fishing mechanics (pre-existing systems with their own future documents), cooking with animal produce, the modding-side lua definitions of animals (Modders track), and multiplayer-specific animal behaviour. This document is spoiler-light: it names systems and species but not specific farm locations.

# Definitions

- **Husbandry** — keeping domestic animals penned, fed and bred for renewable resources; in Build 42 this spans cows, sheep, pigs and chickens as the core supported species [8].
- **Livestock zone** — a map zone within which livestock feed, drink and breed; farmsteads come with these pre-drawn, and moving animals elsewhere requires drawing one manually [2].
- **Trough** — the container animals eat and drink from; constructed or looted from farms [4].
- **Hutch / henhouse** — chicken housing; hens lay their eggs inside one when present [3] [4].
- **Butcher hook** — a workstation for butchering hanging animals, yielding more meat and an unprocessed hide compared with ground butchering [9].
- **Breed** — a sub-type of a species with its own property ranges, such as Angus (meat) or Holstein (milk) cattle [4] [8].
- **Allele** — one of the two inherited copies of each abstracted gene an animal carries; dominant and recessive alleles drive the breeding game [4] [8].
- **Virtual animal** — the off-screen representation of a wild animal group migrating along a path; it becomes a group of real animals when a player approaches [5].
- **Search Mode** — the focused foraging view (introduced in B41) reused in B42 for finding animal tracks under its "Animal Tracks" category [5] [10].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | No | — | No living animal system exists in B41; see the Delta section for what B41 had instead [8] |
| B42 (stable) | Yes | 42.20 | Release-note facts verified against the 42.20 announcement of 2026-07-29 [3]; wiki-derived values carry unstable-era revision stamps noted inline |

The most detailed fact source used here, the pzwiki Animal page, is versioned against unstable **42.6.0** and its numeric values (weights, enclosure sizes, gene ranges) have **not** been re-verified on 42.20 [8]. Thursdoid citations from 2022–2024 describe the system as designed and announced during development; where the 42.20 release notes or the wiki corroborate that a feature shipped, that is stated.

# Reference

## The roster

Build 42 populates the world with free-roaming animals driven by their own (deliberately simple, first-iteration) AI rather than the studio's full NPC behaviour work [8]. The pzwiki Animal page (revision 1385247, versioned 42.6.0) enumerates ten species with in-game pages — the four husbandry cornerstones (cows, sheep, pigs, chickens) plus deer, rabbits, raccoons, turkeys, rats and mice [8]. The system's stated purpose is to support Build 42's crafting economy, which is why the core species are husbandry animals — cows, sheep, pigs and chickens — providing renewable milk, hide and wool [8]. The same page lists announced-but-absent species under a planned heading, including snakes, black bears, additional deer types, squirrels and elk [8].

Each species runs through life stages with its own weight range per stage — for example chick → hen or cockerel, piglet → sow or boar, calf ("cowcalf") → cow or bull, lamb → ewe or ram, fawn → doe or buck, and equivalent baby stages for turkeys (poults), rabbits (kittens), raccoons (kits), rats and mice [8]. Growth stages were a design goal from the first husbandry reveal: calves become cows or bulls and grow in size along the way [4].

## Animal attributes

Every animal is defined by a set of properties [8]:

- **Species and breed.** Breeds differentiate function: Angus is a meat breed, Holstein a milk breed, with Simmental described at design time as sitting between them [4] [8].
- **Sex and age.** Sex gates functionality such as breeding and milking; age gates breeding at both ends and animals eventually die of old age [8].
- **Size.** Larger animals return more resources; the bigger the animal at butchering time, the more meat it produces [4] [8].
- **Milkability.** Milk-capable animals generate milk for a period after delivering young [8].
- **Temperament flags.** Some animals flee humans (mice, for example), and some can have a rope attached so they can be led or kept from wandering [8].
- **Hunger and diet.** Animals eat from troughs, with permitted food types per species; some graze grass when the trough is empty, at the cost of reduced growth [8].

## Feeding, enclosures and housing

Animals must eat and drink: an animal left hungry or thirsty gradually loses health until it dies [8]. Troughs are the intended feeding mechanism — built by the player or looted from farms — and grazing species can crop grass, which regrows over time at a rate controlled by a sandbox option [4] [8]. Enclosures carry a minimum size per animal and stage (for example 20 tiles for a chick, 40 for an adult hen or sow, 80 for an adult cow per the 42.6.0-era wiki figures); an animal kept in an undersized enclosure will not grow to full size and its daily weight gain is divided by eight [8].

Chickens use dedicated housing. At design time, hens were announced to lay eggs in a henhouse when one is present (on the ground otherwise), with a rooster able to fertilise them so that eggs left alone can hatch into chicks — and with a nightly chore of shutting the henhouse door against fox raids [4]. Hutches are confirmed shipped in stable: the 42.20 release notes fix chickens disappearing after being placed inside a hutch and after relogging [3]. The fox-raid mechanic itself has not been re-verified on 42.20 (see Risks).

Livestock live inside zones. Farmsteads on the map come with livestock zones already created; to move animals elsewhere a player must draw a new zone manually, which The Indie Stone acknowledged pre-release as a pain point for new players, announcing (but deferring to later in the unstable cycle) a system where each animal automatically creates its own zone to feed, drink and breed within [2]. A radial menu was added to streamline day-to-day livestock care [2].

## Moving and handling animals

Primary sources document three handling mechanisms. A rope can be attached to appropriate animals to lead them or stop them wandering — with 42.20 fixing roped animals refusing to pass open fence gates [3] [8]. Smaller animals can be picked up and carried (the 42.20 notes fix duplication on pick-up and a corruption case when grabbing an animal mid-death-animation) [3]. And a Livestock Trailer exists for bulk transport, referenced in a 42.20 fix preventing re-butchering of carcasses placed inside one [3]. Animals also track a stress stat; 42.20 fixed stress instantly maxing out near a running car engine [3].

## Health, inspection and the Animal Care skill

Animal Care is one of Build 42's new skills, grouped with Agriculture and Butchering in the Farming family [11]. Per the wiki's skill summary (revision 1436755, versioned 42.3.1), it governs how much information you can read when checking an animal, and it raises harvest output — more milk per cow, more wool per sheep [11]. Characters with appropriate skill can inspect an animal to gauge its health-related genetic attributes [8]. Health feeds back into growth: daily weight gain is multiplied by the animal's current health, so sick, hungry or thirsty animals grow slower [8].

At character creation, the Farmer occupation starts with +1 Animal Care (alongside +4 Agriculture), while Rancher is the dedicated husbandry occupation at +4 Animal Care, +3 Butchering and +1 Fitness for 0 points, per the wiki occupation table versioned 42.18.0 [12].

## Breeding and genetics (overview)

Every animal carries a genome of abstracted genes — milk quantity, life expectancy, strength, appearance and more — each holding two alleles, one inherited randomly from each parent [4] [8]. Alleles are dominant or recessive, and randomly generated base animals can carry recessive defects, so repeated inbreeding risks expressing genetic illnesses that can ruin a herd [4] [8]. The announced gameplay loop is selective breeding: pair animals to push desirable genes into offspring across generations — more milk, more eggs, or more meat — with fresh bloodlines found by ranging out to other farms (or, in multiplayer, other groups) [4]. The developers described the intended reading of genes as "more art than science": skilled characters get an informed view of health-related attributes, while traits like egg or milk output reveal themselves through observation over the animal's life [4] [8].

One concrete gene documented on the wiki is **maxWeight**: an animal's real weight is its species/stage base range multiplied by its maxWeight gene — for most breeds a multiplier somewhere between half and four-fifths of base weight — and a "skinny" genetic disorder divides base weight by three before the gene applies [8]. Specialised breeds override that default multiplier band [8]:

| Breed | Species and role | maxWeight gene band |
|-------|------------------|---------------------|
| Holstein | Cow, milk breed | 0.60 to 0.80 |
| Simmental | Cow, in-between breed | 0.50 to 0.70 |
| Angus | Cow, meat breed | 0.45 to 0.65 |
| Suffolk | Sheep | 0.55 to 0.75 |

Daily growth follows (maximum weight − minimum weight) ÷ stage duration, scaled by health, resetting to the next stage's range when the animal matures [8]. Growth pacing was designed to be realistic — around two in-game years for a cow to reach full size — but adjustable through sandbox options [4].

## Produce: milk, eggs, wool, meat and leather

- **Milk.** Cows generate milk for a period after calving; continued daily milking increases the yield, while leaving an udder full causes problems and reduces lactation [4]. Sheep were also announced as milkable [4].
- **Eggs.** Hens lay eggs, fertilised by a rooster into hatchable ones [4].
- **Wool.** Sheep grow wool retrievable with shears [4].
- **Meat.** Butchering returns meat scaled by the animal's size, with cut quality scaled by the Butchering skill [4] [9].

Butchering is a Farming-family skill whose XP comes from butchering animals, removing animal parts and filleting fish, in rough proportion to the meat harvested [9] [11]. Working on a butcher hook rather than the ground yields more meat plus the animal's unprocessed hide, and the 42.20 release notes further increased the meat cuts gained from large animals on the hook [3] [9]. Chef (+2), Rancher (+3) and Fishing Guide (+1) start with Butchering levels, and the Hunter trait adds +1 [9] [12]. A five-volume Butchering skill-book series provides the usual XP multipliers [9].

Hides feed the leather chain: an unprocessed hide is de-fleshed on a softening beam with a fleshing tool (de-furring optional, but impossible after drying), treated with brain tan — a brain extracted from a skull mixed with a bowl of water — in a tannin barrel, then dried on a leather drying rack sized to the animal (large racks for cows and adult deer, medium for adult sheep and pigs, small for rabbits, raccoons and the young of larger species) [9]. Drying takes about seven days at moderate temperatures, runs up to twice as fast in heat (capping around 39 °C), halts below roughly 4.5 °C, and pauses if the hide is rained on; dried leather cuts down in size steps, one large yielding two mediums and one medium two smalls [9].

## Wild animals, hunting and Tracking

Wild animals serve ambience and necessity: deer visibly moving through the treeline make the world feel alive, and hunting supplies materials that some advanced crafting recipes require once society's leftovers run out [5]. Deer migrate across the map along paths laid out in the world-editing tool; each group (for example a buck, several does and fawns) travels as a single "virtual animal" that spawns into real animals when a player comes close and reverts when the player leaves [5]. Groups follow daily timetables with sleeping and feeding windows [5]. Rabbits and other small wild animals run on the same migration system under a different ruleset [6]. At Build 42's unstable launch, deer paths were preordained at world creation, and The Indie Stone flagged hunting gameplay as a focus for improvement during the unstable cycle, contrasting it with the far more developed husbandry side [1] [2].

Hunting is evidence-driven. Animals leave trails — footprints with an implied direction, droppings, broken twigs and undergrowth, flattened plants marking a sleeping spot and grazed patches marking feeding — designed so a hunter can deduce a group's routine, mark likely spots on the map, and lie in wait at the right hour [5]. In play, tracks are found through Search Mode's "Animal Tracks" category: they are not highlighted like normal foraging finds, instead gaining a yellow outline when stumbled upon, and right-clicking a track reports the animal's direction, size and how fresh the trail is, with more detail at higher Tracking levels [10]. Tracking is a Survivalist-family skill; its XP comes from discovering different track types and from sneaking near wild deer and rabbits, and 42.20 fixed a bug where that sneaking XP was not awarded [3] [10] [11]. The wiki's skill summary states Tracking's wild-animal scope as deer and rabbits [11]. As with Butchering, a five-volume skill-book series exists [10].

## Dangers around animals

In the game's fiction and mechanics, animal noise attracts zombies, but zombies do not attack animals under default settings — that behaviour only changes if altered in Custom Sandbox options — and animals cannot catch the Knox Infection, which infects only humans [8]. The one announced predator threat is the fox raid on an open henhouse at night [4]; its presence in 42.20 stable is unverified. Roadkill hunting was deliberately nerfed during the unstable cycle: early Build 42 made running animals over the easiest hunt, but butchered roadkill now drops significantly less meat than an animal killed cleanly [9].

# B41 vs B42 Delta

This is a single-build (B42) document, but the delta matters because the entire subject is new. Build 42 is the build in which animals became living, interactable inhabitants of the game world [8]. The Build 42 unstable announcement of 2024-12-17 shipped them as a headline system alongside the crafting overhaul, and The Indie Stone's pre-release pillar list named "bringing animal life to the Knox Event" as one of Build 42's required features [1] [7].

What Build 41 had instead: animal presence limited to trapping (which yields dead small game — the trapping/fishing/foraging systems predate B42 and continue within it), fishing, and ambient wildlife; there were no living animals to keep, breed, milk or track [8]. Concretely, the delta for players is:

| Area | B41 (legacy41) | B42 (42.20) |
|------|----------------|-------------|
| Living animals | None — small game exists only as trapped corpses or container loot [8] | Ten-species roster with AI, life stages, breeds and genetics [8] |
| Husbandry | Not present | Zones, troughs, grazing, hutches, breeding, milking, shearing [2] [4] [8] |
| Skills | No Animal Care, Butchering or Tracking on the B41 skill roster [11] | Animal Care and Butchering (Farming family) and Tracking (Survivalist) added [11] |
| Occupations | No husbandry occupation | Rancher (+4 Animal Care, +3 Butchering); Farmer carries +1 Animal Care [12] |
| Hunting | Trapping only | Migrating deer/rabbit groups, physical track evidence, Search Mode tracking [5] [10] |
| Animal products | Trapped meat, fish | Adds milk, eggs, wool, hides and a full tanning-to-leather chain [4] [9] |

B41 saves and mods are not compatible with Build 42, so none of this back-ports [1].

# Practical Guidance

- **Pick your character for the job.** Rancher is the purpose-built start (+4 Animal Care, +3 Butchering at 0 points); Farmer trades animal depth for crops. The Hunter trait's +1 Butchering and +1 Tracking suits a hunting-focused run instead [9] [10] [12].
- **Feed and water before anything else.** Starvation and thirst are the only documented ways animals passively die outside old age — health drains until death — and every point of lost health also slows growth. Keep troughs stocked rather than relying on grazing, which stunts size [8].
- **Respect enclosure minimums.** An eight-fold growth penalty for a cramped pen means an undersized enclosure quietly wastes months of in-game feeding [8].
- **Milk on schedule.** Yield rises with consistent daily milking and falls if you leave the udder full — treat the dairy herd as a daily chore loop, not an occasional harvest [4].
- **Close the henhouse at night.** Announced predator behaviour punishes an open door; even if unverified on stable, the habit costs nothing [4].
- **Butcher on a hook.** Ground butchering forfeits the hide and meat; the hook yields both, and 42.20 made large animals on the hook even more generous [3] [9].
- **Don't hunt with your bumper.** Roadkill's meat penalty makes guns or other clean kills the efficient path [9].
- **Level Tracking by doing.** Seek out varied track types and sneak near deer and rabbits — and note the sneaking XP only works correctly from 42.20 onward [3] [10].
- **Plan breeding lines early.** Bring in outside animals rather than looping one family; recessive illness from inbreeding is an announced, deliberate failure mode [4] [8].
- **Treat unstable-era guides carefully.** Most community animal content, including the most popular video guides, predates stable and may carry stale values [13].

# Common Pitfalls & Troubleshooting

- **"Zombies will kill my herd."** Not under default rules: zombies are drawn to animal noise but do not attack animals unless the sandbox option is changed. The real risk of noise is drawing zombies onto *you* [8].
- **"My animal won't grow."** Check enclosure size, trough contents and health — all three scale growth, with a small enclosure being the harshest penalty [8].
- **"My cow gives less milk than before."** Documented behaviours: lactation is a limited post-calving window, and skipped milkings reduce output [4] [8].
- **"Chickens vanished from my hutch."** A real bug on unstable builds, fixed in 42.20 — update rather than rebuilding the coop [3].
- **"I can't lead my animal through the gate."** Roped animals refusing open fence gates was fixed in 42.20 [3].
- **"Sneaking near deer gives no Tracking XP."** Fixed in 42.20; on earlier unstable builds it silently failed [3].
- **"My animals panic at the base."** Stress spiking to maximum near running car engines was a bug fixed in 42.20; still, an idling engine next to the pen is the first thing to rule out [3].
- **"I butchered a trailer animal twice" exploits and similar duplication tricks** were closed in 42.20 (butchered carcasses in Livestock Trailers, duplication on pick-up, item spawning via attachment commands) — expect them gone on stable [3].

# Community Notes & Unverified Claims

## Claim 1 — Livestock zones can be drawn from the context UI and need no fences

- **Claim:** Community guides state a livestock zone is created by clicking "Designated Zones" then "Add Zone", that fences are optional (useful only against zombies), and that comfortable animals will not wander far outside their zone; this circulates in written B42 husbandry guides such as gamever.io's livestock guide [14].
- **Why unverified:** No primary source documents the player-facing zone UI or fence-free containment; the closest primary confirms zones exist, that farmsteads ship with them and that manual drawing was a tester pain point [2].
- **Confidence:** Medium. The mechanic's existence is primary-sourced and the UI detail is consistently repeated across independent guides, but the specific claims rest on community testing only.

## Claim 2 — Deer and rabbits are the only widespread wild roaming animals

- **Claim:** The pzwiki Tracking page states only deer and rabbits are widespread in the woods, and the wiki's skill summary scopes Tracking to those two species; the roster page nonetheless gives raccoons and turkeys their own entries [8] [10] [11].
- **Why unverified:** The wiki itself marks the statement with a verification flag, and no primary source enumerates which species roam wild versus spawn only as livestock; the page predates 42.20.
- **Confidence:** Medium. Two wiki pages agree and the deer/rabbit migration systems are the only ones shown in Thursdoids, but the wild status of raccoons and turkeys on 42.20 is unconfirmed.

## Claim 3 — Wild or feral animals can be acquired through a "Tame" interaction

- **Claim:** At least one community guide describes approaching animals and using a "Tame" interaction to recruit them [14].
- **Why unverified:** No primary source mentions taming; the handling mechanisms documented by primaries are rope attachment, picking animals up, and the Livestock Trailer [3] [8]. The claim conflicts with the documented flee-humans behaviour of some species [8].
- **Confidence:** Low. Single-sourced from a guide of uncertain rigour and unsupported by any official material; treat rope-and-carry as the verified acquisition path.

# Risks & Caveats

- **The core numeric source is ten unstable versions old.** The pzwiki Animal page is versioned against 42.6.0; every weight, enclosure size and gene range quoted here could have been rebalanced by 42.20 [8]. This is the largest single risk in the document.
- **Design-era Thursdoid facts may have shifted in shipping.** Milking behaviour, henhouse/fox raids, breed positioning and genetics details come from 2022–2023 development posts explicitly labelled work-in-progress [4] [5]; the wiki corroborates most of them as shipped, but each could differ in detail on stable.
- **Occupation naming is inconsistent across sources.** The Occupation table snapshot used here (revision 1391359) lists Farmer, Rancher and Fishing Guide, while this knowledge base's foundation document describes the same revision's roster using the names Crop Farmer, Livestock Farmer and Angler [12]. One of the two readings is wrong or the wiki page mixes naming eras; an in-game check should settle it (flagged for human review).
- **The pzwiki Husbandry and Animal Care pages were unreachable** at research time (Cloudflare bot protection blocked both the API and page fetches twice), so Animal Care detail rests on the Skill page summary and the Animal page rather than the dedicated skill page [8] [11].
- **42.20 is one day old.** Hotfix waves following stable release could adjust any animal value cited here, as The Indie Stone has signalled ongoing patching [3].

# Verification Steps

1. **Roster:** on 42.20, open a Custom Sandbox game near a farm (or use debug spawning) and confirm which of the ten species appear as livestock and which roam wild.
2. **Animal Care effects:** create a Rancher, inspect an animal's info panel at Animal Care 4 versus a fresh character at 0, and compare the visible attributes [11] [12].
3. **Zones:** stand on a farmstead and check the zone display; then attempt to create a livestock zone away from the farm and record the exact UI path (resolves Claim 1).
4. **Milking loop:** keep a post-calving cow, milk daily for a week versus skipping days, and compare yields against the announced behaviour [4].
5. **Butcher hook:** butcher two similar animals, one on the ground and one hanging, and compare meat and hide output [9].
6. **Tracking:** enter Search Mode, select Animal Tracks, and confirm the yellow-outline and right-click information behaviour plus XP on sneaking near deer [10]; cross-check the 42.20 fix [3].
7. **Wiki drift:** open the cited pzwiki revision URLs and diff against the current pages for post-42.20 corrections (the revision ids are pinned in the references).

# Open Questions

- Did the fox henhouse raid ship in 42.20, and does closing the hutch door prevent it? An overnight in-game test resolves this.
- What are Animal Care's exact per-level effects (inspection detail thresholds, harvest bonuses)? Needs the currently unreachable wiki page or first-hand testing.
- Which species roam wild on 42.20 — are raccoons and turkeys huntable or livestock-only (Claim 2)?
- Did the announced automatic per-animal zone system land during the unstable cycle, or is manual zone drawing still required on stable [2]?
- Is there any vanilla way to *buy* or trade for animals, or is acquisition purely find-rope-carry? No primary source found either way.
- Have the 42.6.0-era weight, enclosure and gene numbers been rebalanced by 42.20? A game-file check (`media/` animal definitions) would pin current values.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42 Unstable Out Now* (Steam announcement, 2024-12-17; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1785774543698069. Accessed 2026-07-30.
- [2] **The Indie Stone** — *WhatZ Next* (Thursdoid, Steam announcement, 2024-11-28). https://steamcommunity.com/games/108600/announcements/detail/1784506359022970. Accessed 2026-07-30.
- [3] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-30.
- [4] **The Indie Stone** — *Milky Milky* (Thursdoid, Steam announcement, 2022-03-31; first detailed farm-animal and genetics reveal, labelled work-in-progress). https://steamcommunity.com/games/108600/announcements/detail/4347669995461619508. Accessed 2026-07-30.
- [5] **The Indie Stone** — *The Skillful HuntZman* (Thursdoid, Steam announcement, 2023-05-11; wild-animal migration and tracking design). https://steamcommunity.com/games/108600/announcements/detail/6557848386942319011. Accessed 2026-07-30.
- [6] **The Indie Stone** — *Mizter McGregor's Garden* (Thursdoid, Steam announcement, 2023-05-25; rabbits on the migration system). https://steamcommunity.com/games/108600/announcements/detail/5151600576588209524. Accessed 2026-07-30.
- [7] **The Indie Stone** — *Eine Kleine NachtmooZik* (Thursdoid, Steam announcement, 2023-03-31; animal life named among Build 42's pillar features). https://steamcommunity.com/games/108600/announcements/detail/6839319551984212717. Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [8] **PZwiki** — *Animal* (revision 1385247; page versioned against unstable 42.6.0). https://pzwiki.net/w/index.php?title=Animal&oldid=1385247. Accessed 2026-07-30. Fact-only source.
- [9] **PZwiki** — *Butchering* (revision 1435455; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Butchering&oldid=1435455. Accessed 2026-07-30. Fact-only source.
- [10] **PZwiki** — *Tracking* (revision 1441021; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Tracking&oldid=1441021. Accessed 2026-07-30. Fact-only source.
- [11] **PZwiki** — *Skill* (revision 1436755; page versioned against 42.3.1). https://pzwiki.net/w/index.php?title=Skill&oldid=1436755. Accessed 2026-07-30. Fact-only source.
- [12] **PZwiki** — *Occupation* (revision 1391359; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Occupation&oldid=1391359. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator**

- [13] **Mattsi** — *The BEST Animal Guide for Project Zomboid build 42* (YouTube video, uploaded 2025-11-05; unstable-era, ~42.12). https://www.youtube.com/watch?v=h8JO384cEnk. Accessed 2026-07-30. Community corroboration only.
- [14] **gamever.io** — *How to Start Livestock Farming in Project Zomboid Build 42* (community guide, undated; imagery dated 2024-12-20). https://gamever.io/knowledge-base/how-to-start-livestock-farming-in-project-zomboid-build-42. Accessed 2026-07-30. Community source, quarantined claims only.

**Further Reading**

# Further Reading

- The pzwiki *Animal* page's current (non-pinned) revision for post-42.20 corrections: https://pzwiki.net/wiki/Animal
- The Steam news API feed used to source all Thursdoid citations: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25
- The Indie Stone's Build 42 feature overview linked from the stable release notes: https://projectzomboid.com/blog/features-overview-build-42-20/ (bot-blocks automated checkers; verify in-browser).

# Related Documents

- `players-foundation` — the Players-track overview this document deepens (release facts, save compatibility, headline B42 changes).
- `players-skills-xp` — the skills system in depth; Animal Care, Butchering and Tracking XP mechanics belong to its scope.
- `players-crafting-chains` — where hides, wool and tallow-adjacent products flow after harvesting.
- `players-traits-occupations` — full Rancher/Farmer/Hunter build tables.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
