---
id: players-vehicles
title: "Vehicles: Finding, Fixing and Driving Across Both Builds"
version: 1.0.0
status: approved
confidence: Medium
category: Players
topic: "Vehicles"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-skills-xp, players-map-locations, meta-style-guide]
tags: [players, vehicles, mechanics, hotwiring, towing, fuel, car-keys, engine-quality, build-42]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-vehicles |
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

Cars are Project Zomboid's answer to a map measured in kilometres: they haul loot, carry co-op groups, flatten the occasional zombie, and double as lockable mobile storage. The vehicle system predates both current builds — it arrived with Build 39 in 2018, complete with physics, a dashboard UI, part-by-part damage and hotwiring — and its core loop has carried into Build 41.78 and Build 42.20 largely intact [2]. This document goes below the `players-foundation` overview: how to get a dead car moving (keys, hotwiring, fuel), how the Mechanics skill loop works (magazines, tools, per-part condition, the engine-quality trap), what the three vehicle classes mean in practice, how towing behaves, and how refuelling interacts with the world's electricity shutoff.

Build 42 does not reinvent vehicles the way it reinvents crafting, but it touches them repeatedly: town-specific liveries such as local sheriff and police cars, an improved key system, built-in cigarette lighters, and animal-hauling trailers that serve the new husbandry systems [1] [5] [8]. The 42.20 stable release then rebalanced vehicle speed and towing — trailers can now break loose if you corner too hard or too fast — and fixed a cluster of Mechanics-menu and engine-power bugs [1] [3].

Document-level confidence is **Medium**. The spine (vehicles' introduction, the 42.20 towing rebalance and fix list) is primary-sourced to Indie Stone announcements, but the bulk of the working numbers — hotwire skill requirements, per-part tool and level tables, the engine-quality formula, noise mechanics — comes from pzwiki revisions versioned against 42.16.0 and 42.18.0, not individually re-verified on 42.20.

# Key Takeaways

- The vehicle system dates to Build 39 (2018) and its fundamentals — keys, hotwiring, per-part damage, refuelling — are the same skeleton in both current builds *(cited)* *(both)*
- Keys turn up in four places: on the ground beside the car, inside nearby buildings, in the ignition or glove box, and sometimes on the corpse of the nearest zombie you kill *(cited)* *(both)*
- No key? Hotwiring needs Electrical 1 plus Mechanics 2, or the Burglar occupation — and a failed attempt costs nothing but noise *(cited)* *(both)*
- You cannot work on a vehicle class at all until you read its Laines manual (standard / commercial / performance), unless you took the Mechanic occupation *(cited)* *(both)*
- Engine **condition** can be repaired with spare parts; engine **quality** is rolled when the vehicle spawns and can never be raised — check it before adopting a "project car" *(cited)* *(both)*
- Gas pumps only dispense while powered: before the electricity shutoff (default window 14–30 days in) they work on the grid, afterwards you need a generator — sandbox settings allow exterior generators to power pumps by default *(cited)* *(both; defaults from a B42-era snapshot)*
- Towing needs no equipment — park nose to tail, stand between, press V — but tire pressure, traits and weight all change how well it goes, and 42.20 rebalanced it so trailers detach on hard, fast turns *(cited)* *(B42 for the rebalance)*
- Bicycles, motorcycles and horse-drawn transport are **not** primary-sourced as Build 42 features; treat any claim that they are in the game as unverified *(community, unverified)*

# Purpose

This document answers the practical questions a survivor asks in roughly the order they ask them: where do I find a car, how do I start it without a key, how do I keep it fuelled once the power dies, what does the Mechanics skill actually gate, why does my repaired engine still refuse to start, and how do I drag a second vehicle home? It serves both a Build 41 player on `legacy41` and a Build 42.20 player, flagging where the builds diverge.

# Scope

Covered: acquiring a vehicle (spawn locations, keys, hotwiring, spawn-condition sandbox defaults), fuel (gauges, siphoning, pumps and the electricity shutoff), the Mechanics skill loop (magazines, tools, per-part removal/installation/repair, XP behaviour, wear), engine condition versus engine quality, vehicle classes and notable variants at overview level, engine noise and zombie attraction, towing and trailers, and Build 42's vehicle-facing changes through 42.20.

Not covered: full per-vehicle stat tables (the wiki's model-by-model numbers), exact spawn coordinates or map-specific vehicle stories (see `players-map-locations` when published), multiplayer server configuration of vehicle settings (Admins track), and vehicle modding (Modders track). Claims about B42 vehicle types that lack a primary source — bicycles, motorcycles, animal-drawn transport — are quarantined, not documented as fact.

# Definitions

- **Vehicle class** — one of three service families: standard, heavy-duty, or sports. Both whole vehicles and individual parts belong to a class, and parts from one class never fit another [5] [6].
- **Recipe magazine (Laines manual)** — one of three magazines (Standard, Commercial, Performance) that unlock working on the matching vehicle class in the Mechanics menu [5] [6].
- **Hotwiring** — starting a vehicle without its key, unlocked by Electrical 1 + Mechanics 2 or the Burglar occupation [5] [6].
- **Engine quality** — a per-vehicle reliability score (max 100) rolled at spawn; governs start-failure chance and engine power, and cannot be improved by any means [6].
- **Engine condition** — the repairable health of the engine part, restorable with spare engine parts; distinct from quality [6].
- **Mechanics menu** — the per-part vehicle panel opened by standing at the hood and pressing `E` (or via the radial menu) [5] [6].
- **Radial menu (vehicle)** — the wheel of vehicle interactions bound to `V`, both inside and outside the vehicle [5].
- **Electricity shutoff (ElecShut)** — the sandbox event that permanently ends grid power; the default window is 14–30 days after the July 9, 1993 start date in the current settings snapshot [7].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Core system inherited from Build 39 [2]; B41 not separately re-verified for per-part numbers |
| B42 (stable) | Yes | 42.20, re-checked against 42.21 patch notes | Release-note facts verified against the 42.20 announcement [1] and the 42.20.1 to 42.21 notes [8] [9] [10] [11]; wiki-sourced numbers pinned to revisions versioned 42.16.0–42.18.0 [5] [6] |

The two central pzwiki sources carry banners stating they were last updated for 42.16.0 (Vehicle) and 42.18.0 (Mechanics) against a current stable of 42.20.0 [5] [6]. Sandbox defaults are quoted from a Server settings snapshot taken after the 42.20 release [7].

The 42.21 stable release (2026-09-28) was reviewed for this document by reading the official Steam announcements for 42.20.1 through 42.21 and the 42.21 forum changelist [8] [9] [10] [11]. The vehicle-related items found are recorded in the Delta table; every other statement is carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found in those notes. That was a patch-note review, not an in-game re-test, and the towing, noise and Mechanics values were not re-checked.

# Reference

## Where vehicles spawn and what shape they arrive in

Vehicles entered the game in Build 39, which shipped nine models plus branded and emergency variants, part-level damage and replacement, real physics, a dashboard UI, headlights, horns, air conditioning, car radios and extra carrying capacity [2]. In the current builds they appear in parking lots, on driveways, along highways and bridges, and as parts of randomised roadside stories; spawn condition runs the full range from near-new to unusable wreck [5]. Job-specific vehicles carry themed loot — an ambulance can hold medical supplies, for instance [5].

Several sandbox settings shape what you find (defaults below are from the post-42.20 Server settings snapshot and have not been re-checked against B41's menu) [7]:

| Setting | Default | Player-facing effect |
|---------|---------|----------------------|
| EnableVehicles | on | Vehicles spawn at all [7] |
| CarSpawnRate | Low | How often vehicles are found [7] |
| CarGeneralCondition | Normal | Typical condition of found vehicles [7] |
| RecentlySurvivorVehicles | Low | Frequency of well-kept "survivor" vehicles maintained since the outbreak [7] |
| TrafficJam | on | Wrecked-car jams appear on main roads [7] |
| LockedCar | Sometimes | How often found vehicles are locked / need keys [7] |
| CarAlarm | Rare | How often found vehicles have live alarms [7] |
| ChanceHasGas | Normal | Odds a found vehicle has fuel in the tank [7] |
| InitialGas | Low | How full a fuelled tank is [7] |
| VehicleEasyUse | off | When on, removes lock/key friction entirely [7] |

## Keys

A car key is bound to exactly one vehicle and enables three things: starting the engine, and unlocking the doors and the trunk from outside [5]. The four documented key locations are: on the ground close to the vehicle; inside nearby structures, in boxes or drawers; in the vehicle itself, either the ignition or the glove box; and, randomly, on the body of the nearest zombie you kill [5]. When you carry the right key (or the car is hotwired), a key icon floats over your character while you are near that vehicle [5]. Leaving the key sitting in the ignition is safe — it does not drain the battery [5]. Build 42's feature list credits an improved key system among its smaller systemic upgrades *(B42)* [8].

## Hotwiring

A keyless car can still be started by hotwiring, which requires Electrical level 1 **and** Mechanics level 2, or the Burglar occupation [5] [6]. From the driver's seat, open the radial menu: a Hotwire Engine option stands in for the normal start option, and ordinary start inputs will not work without a key [5]. A failed attempt damages neither the car nor your tools, but it can make noise and attract attention, and vehicles in better condition are harder to hotwire [5]. Once hotwired, the dashboard's ignition indicator changes state and the overhead key icon appears [5]. Two caveats: in multiplayer, a hotwired car is startable by anyone; and if the doors are locked you must first smash a window or unscrew one via the Mechanics menu to get in [5].

## Fuel, pumps and the electricity shutoff

Refuelling is a right-click interaction on the vehicle; with an empty gas can in inventory, the same menu offers siphoning fuel back out [5]. You can fill a tank from any container holding gasoline or directly from a gas pump — but a pump only dispenses **while it has power** [5]. That means grid power before the electricity shutoff, whose default sandbox window is 14–30 days after the July 9, 1993 start date, or generator power afterwards [7]. The `AllowExteriorGenerator` sandbox option (default: enabled) exists precisely so generators placed on exterior tiles can power gas pumps [7]. Pump reserves are finite by default (`FuelStationGasInfinite` off), with spawn amounts governed by minimum/maximum sandbox values [7].

If the pump option refuses to appear, the gas cap is usually the problem: it may be on the far side of the car, obstructed, or out of reach — the fuel gauge carries an arrow showing which side the cap is on, so reposition accordingly [5]. The dashboard fuel warning changes state below 15% and again below 5% of tank capacity [5]. How fast you burn fuel is itself a sandbox dial (`CarGasConsumption`, default 1.0) [7].

## The Mechanics skill loop

Mechanics is a crafting-family skill whose in-game effect is fewer failed vehicle repairs [6]. The loop:

1. **Read the right magazine.** Each vehicle class is gated behind a Laines manual — Standard, Commercial (heavy-duty) or Performance (sports) [5] [6]. The Mechanic occupation (+4 Mechanics) starts knowing all three; the Vehicle Knowledge trait (+1 Mechanics) starts knowing the standard and commercial recipes but must still read the Performance manual for sports vehicles [5] [6].
2. **Open the menu.** Walk to the hood and press `E` (or use the radial menu's Vehicle Mechanics entry) [5] [6]. Clicking a part shows its details in the top-right of the panel; right-clicking offers install/uninstall when you hold the right tools [6].
3. **Have the tool for the part.** Jack plus lug wrench for tires (which must come off before brakes and suspension are reachable); wrench for large parts such as hoods, doors and trunk lids; screwdriver for small parts such as batteries, windows and radios; a tire pump maintains pressure; welding gear (torch, mask, steel sheets) repairs body parts; glue or duct tape repairs seats [6].
4. **Respect the level gates.** Batteries, lights and radios need no skill; tires sit around level 1, seats 1–2; hoods, trunk lids, brakes, suspension and side windows cluster around level 3; doors and engine work start at 4; mufflers, windshields and gas tanks need 5 or more — and brakes, suspension, gas tanks and engines demand higher levels again on heavy-duty and sports classes [6]. You *can* attempt a part below its recommended level, with a real chance of failing and damaging it [6].
5. **Know what is repairable.** Seats (glue or duct tape), and welded body parts — hood, trunk lid, doors, gas tank (which must be empty, and some parts must be uninstalled first) — can be repaired; tires, brakes, suspension, mufflers, windows, batteries and lights cannot, and are only replaced with better-condition salvage [6].

**XP behaviour.** Both success and failure grant Mechanics XP — failure always yields 0.25 XP, success scales with the part's difficulty — but each specific part on each specific vehicle only pays XP once per 24 in-game hours [6]. The practical consequence, documented on the same page, is that dedicated levelling means rotating across several sacrificial junk vehicles (wrecking yards are the classic source) rather than stripping one car repeatedly [6]. Crafty and Fast Learner raise Mechanics XP gain to 130%; Slow Learner cuts it to 70%; five skill books (Mechanics I–V) cover the usual two-level bands [6].

**Wear.** Tires, suspension and mufflers degrade with use: above 10 MPH there is a random damage chance influenced by speed, off-road driving and the vehicle's off-road efficiency, steering/pitch, and running time; tire pressure also drifts and needs a tire pump [6].

**Classes and types.** Every part carries a vehicle class (standard / heavy-duty / sports) and usually a type tier (e.g. economy, regular and performance tires or brakes). Classes can never be mixed across vehicles; type tiers can be mixed within a class, though the wiki advises against it [6].

## Engine condition vs engine quality

These two numbers are the most misunderstood part of the system. **Condition** is repairable: engines can be stripped for spare engine parts at Mechanics 4 (standard), 5 (heavy-duty) or 6 (sports), and those parts restore condition on another engine — with per-part yield improving from about 1% at the unlock level to 3–4% at Mechanics 10 [6]. Salvaging is destructive: pulling parts from an engine zeroes that engine's condition no matter what it was before, even if nothing was actually extracted, and a repair consumes *every* spare engine part in your inventory with no way to hold some back [6].

**Quality** is not repairable: it is fixed when the vehicle spawns, caps at 100, and no mechanism raises it [6]. It drives the start-failure roll — the chance an ignition attempt fails is `30 / (quality + 50)`, so a 65-quality engine fails roughly 26% of tries, while a 100-quality engine skips that roll entirely but keeps a residual 1% failure chance [6]. Engines at quality 65 or below also start harder in cold weather [6]. Emergency vehicles (ambulance, fire, police) typically roll 90–100 quality [6]. The Mechanics panel shows quality separately from condition in the top-right when you click the engine [6]. Note that 42.20 fixed a bug where engine power was set to the script maximum instead of its calculated value — pre-42.20 B42 driving impressions of engine strength are therefore suspect *(B42)* [1].

## Vehicle classes and notable variants

Vehicles split into standard, heavy-duty and sports classes, and spawn zoning tends to match the class to the neighbourhood — performance cars in wealthy districts, work vehicles around industrial lots [5]. The current wiki revision's roster spans family sedans and wagons, pickups, vans (including six-seater and radio-van variants), an ambulance, SUVs and off-roaders, luxury and race cars, plus branded and emergency variants of base models such as the Fossoil-liveried Chevalier D6 and the police Chevalier Nyala [5]. Broad class trade-offs from the same source's stat legend: greater mass helps a vehicle shove obstacles aside at the cost of slower acceleration and braking; engine power sets acceleration and towing muscle; loudness sets zombie draw; suspension stiffness sets cornering stability [5]. Heavy-duty vehicles carry the large trunks; sports cars trade cargo for speed [5].

Build 42 adds town-specific liveries — a local sheriff, local police cars — as part of its environmental-storytelling push *(B42)* [8], and B42 vehicles include built-in cigarette lighters *(B42)* [5]. Towable trailers extend cargo capacity, and the roster now includes animal-hauling variants (horse trailer, livestock trailer) that carry live animals for B42's husbandry systems, with capacity measured by animal size *(B42)* [5]; the livestock trailer's existence in 42.20 stable is confirmed incidentally by a release-note fix about butchering animals placed inside one [1]. For the future roster, the wiki's planned-vehicles list still carries fire trucks and military vehicles, sourced to 2017-era Thursdoids [5].

## Noise

Engine loudness is a per-model stat (base values 55–110 across the vanilla roster), modified by the muffler: a full-condition muffler halves effective loudness, a half-condition muffler leaves 75%, and no muffler means full volume [5]. Sound radius then scales with RPM — roughly 20% of radius idling, 40% reversing (~2,000 RPM), 100% in normal driving (~4,000 RPM), up to 175% at a theoretical 7,000 RPM, with a floor of 8 tiles [5]. Under the hood the game rolls four overlapping engine sounds every second at chances of 1, 1/10, 1/30 and 1/120, with radii of the actual volume divided by 6, 4, 2 and 1 respectively — so a running engine pings a wide area on average once every couple of minutes rather than continuously [5]. The wiki also notes engine noise is less compelling to zombies than some quieter player sounds like shouts or sneezes [5]; a sandbox multiplier (`ZombieAttractionMultiplier`, default 1.0) scales engine attraction globally [7].

## Towing and trailers

Any car — including wrecks — can be towed without special equipment: drive a second vehicle up to its front or rear, stand between the two, face either one, open the radial menu (`V`) and pick the plus sign [5]. Tow performance is shaped by the tire pressure of both vehicles; by traits, because towing leans on acceleration (Sunday Driver degrades it badly, Speed Demon helps for the same reason); and marginally by the weight-to-engine-power ratio of the pair [5]. In 42.20 The Indie Stone rebalanced vehicle speed and towing explicitly to improve the towing experience, and trailers can now detach when cornering sharpness or speed gets too high *(B42)* [1] — towing was called out among the known problem areas the stable release targeted [3] [4].

## Driving controls and the dashboard

Most interactions live on the `V` radial menu: seat switching, headlights, heater/AC, horn, lightbar (where fitted), radio options, window and door-lock control, sleeping in the seat, and the Mechanics panel [5]. The dashboard reports engine state, battery, door and trunk locks, headlights, heater, ignition, fuel, gear position, cruise control, RPM and speed [5]. Cruise control toggles with `Shift`, adjusts with `Shift`+`W` / `Shift`+`S`, and cancels with `Space` [5]. The gearshift indicator runs P/N/R and gears 1–5 — with the Sunday Driver trait locking away the upper gears (partial access to 3, none to 4–5) [5]. Two practical details: an open window equalises cabin temperature with the outside and lets both you shoot out and zombies reach in [5]; and a flat battery can be recharged by running the vehicle or with a battery charger [6].

# B41 vs B42 Delta

The vehicle system is one of the more continuous player-facing systems across the build boundary: its skeleton predates B41 entirely [2], and no primary source documents a B42 rework of the core loop (keys, hotwiring, per-part mechanics, refuelling). The documented deltas are additive and mostly arrived with B42's world and systems changes:

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Core loop | Keys / hotwire / per-part Mechanics / refuel, inherited from Build 39 [2] | Same loop; wiki sources versioned 42.16–42.18 describe it unchanged in structure [5] [6] |
| Liveries & variants | Base branded/emergency variants [2] | Town-specific liveries added (local sheriff, local police) as environmental storytelling [8] |
| Key system | B41-era key handling | Improved key system credited in the B42 feature list [8] |
| Trailers | Cargo trailers | Animal-hauling trailers (horse, livestock) serving the new husbandry systems, capacity by animal size [1] [5] |
| In-cab extras | — | Built-in cigarette lighters for cigarettes [5] |
| Towing behaviour | B41-era towing model | 42.20 rebalanced speed/towing; trailers detach on over-sharp or over-fast turns [1] [3] |
| Engine power | — | 42.20 fixed engine power wrongly pinned to the script maximum [1] |
| Mechanics QoL | — | 42.20 fixed timed-action queuing with tools in backpacks, duplicate install options and screwdriver double-listing in the Mechanics UI [1] |
| XXL trees *(42.21)* | Not covered by the 42.21 notes | XXL tree cutaway behaviour updated: better for players in vehicles, no longer hides houses and furniture the trees overhang, transparency adjusted; the notes call it work in progress [9] [10] [11] |
| MP driving, 42.21 | B41 MP | Driving at roughly 150 ms ping and above: map not loading in front of the car, passenger teleportation and juddering improved; vehicle sound, desync and animation fixes; memory leak from eating food directly from a trunk fixed; split-screen crash when sharing a moving vehicle fixed [10] [11] |
| Vehicle fixes, 42.21 supplement | — | Fixed: vehicle sound state issues, SFX issues when cars hit traffic cones in MP, car model blinking when a remote player swaps seats, walkie-talkie VOIP not working while driving, BufferUnderflow errors when driving Base.RaceCar, being unable to queue Mechanics 'Install' actions, player-built campfires colliding with vehicles, and instant removal of XXL trees through 'Remove Bush' [11] |
| Vehicle visibility in MP *(42.20.1)* | — | 42.20.1 fixed vehicles temporarily disappearing for players after another player disconnected [8] |
| Animals × vehicles | No animals in B41 | Animal stress no longer spikes to maximum near a running engine (42.20 fix) [1] |
| MP driving | B41 MP | 42.20 fixed map chunks failing to load while driving, network performance during vehicle–zombie collisions, and trunk damage from crawlers [1] [4] |

What did **not** change, per available primaries: no bicycles, motorcycles or animal-drawn vehicles appear in any Build 42 feature list or patch note reviewed for this document — see the quarantine section [1] [8].

# Practical Guidance

- **Check three things before adopting a car: quality, condition, fuel.** Click the engine in the Mechanics panel and read the quality number in the top-right before investing repairs — condition is fixable, quality never is, and a sub-65-quality engine will misfire forever and start even worse in the cold.
- **Loot the Laines manuals early.** Without the class magazine you cannot touch the class's parts at all. If you took Vehicle Knowledge, remember it covers standard and commercial only — sports cars still need the Performance manual.
- **Level Mechanics on junk, not on your daily driver.** Early attempts fail often and damage parts, failure XP is small but guaranteed, and each part pays XP only once per day per vehicle — so a wrecking yard full of sacrificial cars is the efficient (and safe) classroom.
- **Bank spare engine parts, but repair late.** Per-part repair yield roughly triples between the unlock level and Mechanics 10, and a repair consumes your entire stock of spare parts in one action — repairing at low level wastes most of the stack.
- **Plan fuel around the shutoff.** On defaults the grid can die as early as two weeks in. Top up every vehicle and gas can while pumps are free, and stage a generator (exterior placement works on default settings) at a chosen station for the long game.
- **Tow like a professional.** Pump up the tires on both vehicles, use a strong-engined tug, and after 42.20 slow down for corners — the build now punishes sharp, fast turns by dropping the trailer.
- **Treat the muffler as stealth equipment.** A pristine muffler halves your effective engine noise; driving at lower RPM shrinks the radius further. Conversely, a battered muffler on a heavy-duty van is a rolling dinner bell.
- **In multiplayer, do not hotwire your forever-car.** A hotwired vehicle starts for anyone who sits in it; find the real key for anything you keep at base, and lock the doors — locking works from any seat.

# Common Pitfalls & Troubleshooting

- **"I repaired the engine to 100% and it still won't start reliably."** Condition and quality are different numbers; the start roll uses quality, which cannot be raised — the fix is a different vehicle, not more spare parts [6].
- **"Salvaging a couple of engine parts destroyed the engine."** Working as documented: any salvage action zeroes engine condition regardless of yield [6].
- **"The gas pump gives no refuel option."** Either the pump is unpowered (post-shutoff without a generator) or the gas cap is on the wrong side, blocked, or out of reach — the fuel gauge's arrow shows the cap side; reposition the car [5] [7].
- **"I can't remove the brakes/suspension."** The tire on that corner has to come off first, which needs both a jack and a lug wrench [6].
- **"The Mechanics menu won't let me install anything."** Check, in order: the class magazine has been read, the part is class-matched to the vehicle, the part is in your main inventory / an adjacent container / on the floor (not in a worn bag), and you hold the part's tool [6]. On pre-42.20 B42, tools in a backpack also broke action queuing — fixed in 42.20 [1].
- **"My trailer fell off mid-drive."** On 42.20 that is intended behaviour when cornering too sharply or too fast, introduced with the towing rebalance [1].
- **"XP stopped coming while grinding one car."** Per-part XP has a 24-hour cooldown per vehicle; rotate parts and rotate vehicles [6].
- **"A B42-unstable guide's vehicle handling advice feels wrong on 42.20."** Two systemic changes landed at stable: the speed/towing rebalance and the engine-power calculation fix — treat pre-stable handling impressions as stale [1].

# Community Notes & Unverified Claims

## Claim 1 — Build 42 adds bicycles and/or motorcycles

- **Claim:** Recurring community discussion (subreddit threads, Steam forum wishlists, mod pages simulating bikes) asserts or assumes that two-wheeled vehicles are part of Build 42 or imminently coming to it.
- **Why unverified:** No primary source found. The Build 42 feature overview, the 42.20 stable release notes and the announcement archive reviewed for this document contain no bicycle or motorcycle vehicle feature; the only matches are motorcycle-helmet clothing items [1] [8].
- **Confidence:** Low. The absence is consistent across every primary reviewed, and existing two-wheeler experiences come from Workshop mods, not the base game.

## Claim 2 — Rideable horses or animal-drawn transport are in Build 42

- **Claim:** Community speculation, encouraged by B42's animal husbandry and by the existence of a horse trailer, holds that horses can be ridden or hitched to carts in Build 42, or will be within the B42 cycle.
- **Why unverified:** No primary source found. The announced B42 animal roster (sheep, chickens, pigs, cows, rats, rabbits, deer) does not include horses, and no announcement reviewed describes riding or animal-drawn vehicles; the horse trailer is itself a towed vehicle for hauling animals, not evidence of rideable ones [1] [5] [8].
- **Confidence:** Low. Rests on inference from a trailer asset and general roadmap hope, against a consistent silence in primaries.

## Claim 3 — Sports cars are deliberately the worst survival choice despite the class fantasy

- **Claim:** Community guides widely advise that sports vehicles are a trap outside racing fun: loudest-adjacent engines for their size, smallest trunks, highest part level requirements, and the extra Performance-manual gate.
- **Why unverified:** The constituent facts are cited above (trunk capacities, level gates, magazine gating [5] [6]), but "worst choice" is an aggregate value judgement no primary source makes.
- **Confidence:** Medium. The mechanical inputs are well-sourced; only the conclusion is community synthesis.

# Risks & Caveats

- **Version skew on the two core wiki sources.** The Vehicle page is versioned against 42.16.0 and the Mechanics page against 42.18.0, both flagged by the wiki itself as potentially stale versus 42.20.0 [5] [6]. The 42.20 rebalance explicitly touched vehicle speed and towing, so the noise/speed-adjacent numbers here are the most likely to have drifted [1].
- **Internal inconsistency in the Vehicle source.** The page's prose counts 14 vehicle models and three trailer types, while its own tables list more entries of each (including the Race Car and five trailer rows) [5]. This document therefore avoids asserting an exact roster count.
- **Trait naming instability.** The Mechanics page refers to the same trait as both "Vehicle Knowledge" and "Amateur Mechanic" in different paragraphs [6] — likely a mid-update rename artefact; this document uses the B42 roster name Vehicle Knowledge.
- **Sandbox defaults quoted from one build.** The settings table comes from a post-42.20 snapshot [7]; B41's sandbox menu was not independently re-verified and some defaults may differ there.
- **42.21 re-baseline is notes-only.** The 42.21 changes above come from patch notes [9] [10] [11]; the notes are selective, so unlisted vehicle changes may exist, and none was tested in-game.
- **Hotfix exposure.** 42.20 stable was days old when written (since then 42.20.1 to 42.20.4 and 42.21 have shipped [8] [9] [10] [11]); The Indie Stone has said hotfixes will follow the release [3], and towing behaviour — freshly rebalanced — is a plausible re-tuning target.
- **B41-side thinness.** Primary sourcing for B41-specific vehicle behaviour is limited to the Build 39-era announcements; per-part numbers cited from 42.x-era wiki revisions are assumed, not proven, to match 41.78.16.

# Verification Steps

1. **Hotwire gate (both builds):** create a character with Electrical 1 / Mechanics 2 (or Burglar), enter a keyless car's driver seat, open the radial menu and confirm Hotwire Engine appears; repeat with a fresh character and confirm it does not.
2. **Engine quality (42.20):** open the Mechanics panel on any vehicle, click the engine and confirm quality displays separately from condition in the top-right; salvage parts from a junk engine and confirm its condition drops to zero.
3. **Magazine gating (42.20):** without reading any Laines manual, attempt to uninstall a part and record the block; read the matching manual and retry.
4. **Pump power (both builds):** advance a sandbox world past the electricity shutoff, confirm pumps stop dispensing, then place and fuel a generator in range of a pump (exterior placement, default settings) and confirm refuelling returns.
5. **Trailer detach (42.20):** hitch a trailer, corner hard at speed, and confirm the trailer can detach — then repeat gently and confirm it holds.
6. **Towing traits (either build):** tow the same wreck with a Sunday Driver character and a Speed Demon character and compare achievable speed.
7. **Source spot-check:** open the pinned revision URLs in the references and diff against the live pages for post-42.20 corrections, especially on the Vehicle page's noise and stat sections.

# Open Questions

- Did the 42.20 speed/towing rebalance change any of the per-model stats or the noise/RPM radius model quoted from the 42.16-era Vehicle revision? Needs an in-game or script-file check.
- What exactly does B42's "improved key system" change from the player's perspective (key rings? key spawn logic?) — the feature list names it without detail [8].
- Are the per-part recommended levels and tools identical on 41.78.16, or have B42 revisions quietly shifted any of them? A B41-install comparison would close the delta table's biggest assumption.
- What are the B41 sandbox defaults for the vehicle settings quoted here from the B42-era snapshot?
- Does the announced Build 42 Support Update touch vehicles (the wiki's planned list still carries fire trucks and military vehicles from 2017 Thursdoids [5])?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *Build 39: Vehicles released!* (Steam announcement, 2018-05-31; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/2396358621997235099. Accessed 2026-07-31.
- [3] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-24). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453. Accessed 2026-07-31.
- [4] **The Indie Stone** — *NEXT STEPS* (Steam announcement, 2026-07-09; retrieved via Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1836506165584147. Accessed 2026-07-31.
- [8] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05; vehicles temporarily disappearing after a disconnect fixed). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [9] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28; XXL tree cutaway). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [10] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [11] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post, 2026-09-23). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [5] **PZwiki** — *Vehicle* (revision 1435869; page versioned against 42.16.0). https://pzwiki.net/w/index.php?title=Vehicle&oldid=1435869. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Mechanics* (revision 1436221; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Mechanics&oldid=1436221. Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *Server settings* (revision 1443167; snapshot taken 2026-07-30, post-42.20). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *Build 42* (revision 1443663). https://pzwiki.net/w/index.php?title=Build_42&oldid=1443663. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited.

**Further Reading**

# Further Reading

- The Steam news API mirror used to verify announcement facts: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25
- The official blog / Thursdoid feed (bot-blocks automated checkers; browse manually): https://projectzomboid.com/blog/
- `players-foundation` in this knowledge base for the wider B41→B42 context these vehicle changes sit inside.

# Related Documents

- `players-foundation` — the Players-track overview this document deepens (build landscape, save compatibility, skill roster context).
- `players-skills-xp` — the skills deep-dive; Mechanics XP behaviour documented here should be read alongside its general XP rules.
- `players-map-locations` — (planned) where to actually find vehicles, gas stations and wrecking yards in Knox Country.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed Steam announcements 42.20.1-42.21 and the 42.21 forum changelist [8] [9] [10] [11]; added XXL tree cutaway, high-ping driving, vehicle-disappearance, sound/seat-swap/VOIP/RaceCar and related vehicle fixes; version-scope statements updated. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
