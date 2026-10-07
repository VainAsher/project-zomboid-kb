---
id: players-medical-moodles
title: "Health, Injuries and Moodles: The Body Simulation"
version: 0.2.0
status: in-review
confidence: Medium
category: Players
topic: "Medical & moodles"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-skills-xp, admins-sandboxvars-reference, meta-style-guide]
tags: [players, moodles, health, injuries, first-aid, zombification, knox-infection, muscle-strain, medical, build-42]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-medical-moodles |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 |

# Executive Summary

Project Zomboid does not model a health bar so much as a body. Your character has seventeen separately-tracked body sections, each of which can carry its own wound, its own bleed, its own fracture and its own infection, and a single overall health figure that those wounds jointly cap [12] [13]. Sitting on top of that body is the moodle rack in the top-right corner of the screen — the game's only warning system, and the closest thing it has to a HUD [10]. This document is the deep dive that `players-foundation` deliberately stopped short of: the complete moodle roster with what each one actually does to you, every injury type with its cause and treatment, the two completely different things the game calls "infection", the zombification odds attached to each kind of zombie wound, what the First Aid skill does and does not buy you, and the muscle-strain system Build 42 added to combat.

The headline B41→B42 change for this subject is muscle strain. The Indie Stone flagged "combat building up muscle strain" as one of a small set of deliberate changes to the *flow* of the game, alongside rebalanced zombie spawns and a heavier emphasis on sneaking [2]. It is not a moodle; it is accumulated fatigue damage written into the individual limbs that swing the weapon, and it went through a long balance arc across the unstable cycle — melee strain cut to 60% of its launch value within three days of Unstable going public, over-encumbrance strain halved a month later, and the whole system given its own sandbox multiplier alongside the Apocalypse preset's reduced-impact tuning [3] [4] [5]. B42 also grew the moodle roster (Restricted movement became obtainable; Noxious smell and Discomfort are new) and added sandbox switches over injury severity, fractures and wound-infection damage that B41 never exposed [10] [11] [16].

Document-level confidence is **Medium**, and the reason is specific rather than vague: the mechanical spine of this document — per-moodle effects, injury heal times, First Aid multipliers, the muscle-strain formulas — is sourced from pzwiki page revisions stamped against 42.13.2, 42.15.3, 42.18.0 and 42.13.1, none of which have been re-verified against 42.20 stable. The zombification transmission odds (7% / 25% / 100%) are the load-bearing numbers in this document and are corroborated across two independently-versioned wiki revisions covering both builds [12] [13] [14], but they are still wiki-sourced, not patch-note-sourced. Everything about muscle strain's *existence and balance history* is primary-sourced to Steam announcements; the *formula detail* is not.

# Key Takeaways

- The body is split into **17 tracked sections**; wounds cap your maximum health rather than just subtracting from it, so an unhealed upper-torso fracture holds you near 60% health indefinitely *(cited)* *(both)*
- **Zombie wound → zombification odds: scratch 7%, laceration 25%, bite 100%** on default settings, identical across both builds; non-zombie wounds never transmit it *(cited)* *(both)*
- **First Aid does not make scratches or lacerations heal faster.** It speeds up medical actions, makes bandages last longer, makes splints more effective, roughly quintuples fracture healing at level 10, and improves your read on wound severity *(cited)* *(both)*
- The game contains **two unrelated "infections"**: bacterial wound infection (a pain penalty, treatable with antibiotics, 100% survivable) and the Knox Infection (untreatable, unavoidably fatal, invisible in the UI) *(cited)* *(both)*
- **Neck wounds bypass the usual health cap** and can kill within minutes if left unbandaged — the one injury location that is categorically more dangerous than the others *(cited)* *(both)*
- **Muscle strain is Build 42's signature combat cost**: it accumulates into the specific limbs doing the work, grows with every zombie a swing connects with, and is reduced by weapon skill and Strength *(cited)* *(B42)*
- B42's moodle roster gains **Noxious smell** and **Discomfort** and makes **Restricted movement** obtainable; nine further moodle icons ship in the files but are not active *(cited)* *(B42)*
- Sandbox lets you switch the whole zombification system off or make it universal — `ZombieLore.Transmission`, `ZombieLore.Mortality` and `ZombieLore.Reanimate` are the three keys that define it *(cited)* *(both)*
- The muscle-strain formula detail circulating in the community appears to be code-derived and includes an alleged double-applied time multiplier; treat it as unverified *(community, unverified)*

# Purpose

`players-foundation` told you that moodles exist and that ignoring them kills you. That is true and useless. This document answers the next questions: which moodle is actually costing me combat performance right now, what does this wound in my health panel do if I leave it, how likely is that scratch to be the end of the run, is it worth spending points on First Aid, and why does my character's arm hurt after a fight in Build 42 when it never did in Build 41. It is written for a player at the health panel deciding what to do in the next sixty seconds, and for a returning B41 player who needs to know what changed under them.

# Scope

Covered: the health panel and the 17-section body model; the overall body-status ladder; the complete moodle roster with per-moodle effects, plus the removed/future moodles; every injury type with cause, symptom profile, treatment and documented heal time; wound infection, the common cold and food illness; the Knox Infection end-to-end (transmission odds, symptom timeline, trait modifiers, why it cannot be treated); the First Aid skill's numeric effects and levelling routes; Build 42's muscle-strain system and its balance history; and the sandbox keys that govern all of the above.

Not covered: exhaustive medical item statistics (bandage-by-bandage, plant-by-plant — the item tables here are indicative, not complete), nutrition and weight as systems in their own right, sleep, exercise and fitness training, combat mechanics beyond the strain they generate, the lore of the Knox Event (see the Lore track), and multiplayer-specific medical UI. Modded medical overhauls are out of scope entirely.

# Definitions

- **Moodle** — an icon in the top-right rack reporting one physical or emotional state, with a hover tooltip and, for most, several severity stages [10].
- **Health panel** — the body diagram opened with `H` or the heart icon at the upper-left; where injuries are inspected and treated [12] [15].
- **Knox Infection** — the fatal zombie-borne disease, also called zombie infection; distinct from wound infection, food poisoning and the common cold [14].
- **Wound infection** — the bacterial infection of an untreated or dirty-bandaged wound; a pain penalty, not a death sentence [12] [14].
- **Muscle strain** — Build 42's accumulated exertion damage, applied to the specific body parts performing an action rather than to overall health [12].
- **Incubation period** — the window between contracting the Knox Infection and diagnosis becoming certain; 24 hours on default settings [15].
- **Damage cap** — the ceiling that open or unhealed injuries impose on how far health can recover; neck wounds ignore it [12].
- **Bandage power** — a per-bandage-item value governing how long a dressing stays effective before turning dirty [15].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Moodle and Health facts drawn from wiki revisions stamped 41.78.16 [11] [13]; no muscle strain, smaller moodle roster |
| B42 (stable) | Yes | 42.20, re-checked against 42.21 patch notes | Muscle strain, expanded moodles, new medical sandbox keys; values *(B42)*-tagged inline |

The 42.21 stable release (2026-09-28) was reviewed for this document by reading the official Steam announcements for 42.20.1 through 42.21 and the 42.21 forum changelist [24] [25] [26]. Only three medical items there affect this document (the antibiotics packaging recipe, reduced grave-digging strain in multiplayer and the multiplayer pill-taking animation fix, all recorded below); every other statement is carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found in those notes. That was a patch-note review, not an in-game re-test.

Version-stamp warning, stated plainly because it governs everything below: the pzwiki pages this document draws its mechanics from are versioned against **42.13.2** (Moodle) [10], **42.15.3** (Health) [12], **42.18.0** (First Aid) [15] and **42.13.1** (Knox Infection) [14] — all unstable-era, none re-verified against 42.20 stable. Where a number below is not also confirmed by a Steam announcement, assume it was established during the B42 unstable cycle and may have shifted. The B41-side figures come from revisions the wiki itself stamps 41.78.16 [11] [13], which is the frozen legacy build, so those are more stable by nature.

# Reference

## The health model: seventeen body parts, one health figure

Health is the character statistic representing overall physical integrity, shown both as a bar in the health panel and as the Injured moodle on screen; reaching zero is immediate and permanent death [12]. The panel opens from the heart icon at the upper-left of the screen or with the `H` key, and the icon animates when damage is taken so that the player notices without watching it [12]. Treatment is initiated by right-clicking either the body diagram or the injury text in that window, and always consumes materials — even improvised ones like ripped sheets or bourbon [15].

The body is divided into **17 tracked sections**: left and right foot, shin, thigh, hand, forearm and upper arm (twelve), plus groin, lower torso, upper torso, neck and head (five) [12]. Each section carries its own injuries independently. Overall health is then reported qualitatively rather than numerically [12]:

| Status | Health range |
|--------|--------------|
| OK | No damage |
| Slight damage | 90–100% |
| Very Minor damage | 80–90% |
| Minor damage | 70–80% |
| Moderate damage | 60–70% |
| Severe damage | 50–60% |
| Very Severe damage | 40–50% |
| Critical damage | 20–40% |
| Highly Critical damage | 10–20% |
| Terminal damage | 0–10% |
| Deceased | 0% |

The single most important structural fact about healing is that **injuries cap health rather than merely subtracting from it**. Recovery proceeds by default provided nothing is actively preventing it — an unbandaged bleeding wound will prevent it — but the number and severity of outstanding injuries set a ceiling that health sinks back toward; the wiki's worked example is an upper-torso fracture holding maximum health around 60% until it mends [12]. Recovery rate is modified by moodles: being well fed accelerates it, while hunger, thirst and a cold slow it, and extreme states such as full fever or starvation invert it into net health loss [12]. Sleep substantially boosts the recovery rate [12].

Location matters less than players assume, with one enormous exception. Comparable wounds on an arm and on the torso cost roughly the same health, differing mainly in the physical penalties the limb wound imposes [12]. **Neck wounds are the exception**: they ignore the usual damage cap and drain health rapidly while unbandaged, to the point that an unattended neck scratch can be lethal within minutes [12]. Build 42 reinforced this in the UI — from 42.1, a bleeding neck injury pins the Bleeding moodle straight to maximum, where previously the moodle level tracked only the *count* of bleeding parts irrespective of severity *(B42)* [4].

## The moodle roster and what each one costs you

Moodles report emotional and physical state as icons in the top-right corner, each with a hover tooltip [10]. Most run through multiple severity stages, and the penalties below generally scale with the stage. The roster in the current wiki revision *(B42, 42.13.2)* is [10]:

| Moodle | What it reports | Documented effect |
|--------|-----------------|-------------------|
| Hungry | Hunger state; red for hungry, green for well fed | Well fed raises healing rate; hunger cuts carry capacity, healing rate and body-heat generation. Hunger and nutrition are separate systems — calorie burn does not move this moodle |
| Thirsty | Time since last drink | Weakness, reduced carry capacity, slightly raised heat generation, and eventual death if ignored |
| Panic | Fear response, usually from visible zombies | Penalises many combat abilities while granting occasional benefits; managed with beta blockers or alcohol; resistance builds with survival time |
| Bored | Inactivity, usually indoors | No direct mechanical penalty; functions purely as an early warning for Unhappy. Clears outdoors or while panicking |
| Stressed | Accumulated stress, chiefly infection fear and the Smoker trait | Degrades combat ability; chronic stress feeds Unhappy. Managed with cigarettes or reading |
| Unhappy | Accumulated unhappiness | Minor slowdown to item interactions; treated with medicine, recreation or quality food |
| Drunk | Alcohol intoxication | Drowsiness, delayed vehicle response, Search Mode penalties; fades over time |
| Heavy load | Encumbrance | Heavily reduces movement and attack speed, raises endurance drain, and at the extreme inflicts direct damage of as much as a quarter of total health |
| Endurance | Exertion from running, swinging and carrying | Rapidly falling combat ability, slower movement, sprint/run limits, faster tiredness gain. Recovered by idling, sitting or resting on furniture |
| Tired | Sleep debt | Rapid combat penalties, narrowed vision cone and reduced awareness, linearly slower endurance recovery. Fixed by sleep or caffeine |
| Hyperthermia | Above-normal body temperature | Raises dehydration and fatigue rates. Causes include heat, exertion, insulating clothing and zombie infection |
| Hypothermia | Below-normal body temperature | Sharply reduced movement and attack speed; can approach lethality |
| Windchill | Perceived-temperature penalty outdoors in cold weather | Lowers effective outside temperature and raises hypothermia risk while outdoors |
| Wet | Accumulated moisture from rain or sweat | Slight movement penalty plus cold risk; countered by shelter, insulation, towels or the outdoorsman trait |
| Injured | Health below given thresholds | Escalating carry-capacity penalty. Note it tracks *health level*, not the presence of a wound — light wounds may not trigger it |
| Pain | Usually wound-driven; also exercise fatigue | Progressive combat degradation and, at high levels, prevents sleep. Fades as wounds heal; suppressed by painkillers or alcohol |
| Bleeding | Number of actively bleeding wounds | The warning to bandage; treated with bandages |
| Restricted movement | Inability to sprint | Triggered by bare feet, leg injuries, overloading, heavy clothing or speed-penalising moodles *(B42 — see Delta)* |
| Has a cold | Illness from prolonged wet or cold exposure | Periodic sneezing and coughing that draws nearby zombies. Cured by staying indoors, fed, hydrated and rested |
| Sick | Poisoning, spoiled or dangerous food, corpse proximity — or the Knox Infection | Reduced carry capacity, raised body temperature, diminished healing. Non-fatal sickness passes; lemongrass helps. Zombie infection here is always fatal on default settings |
| Noxious smell | Two distinct sources: corpse sickness and toxic fumes | Corpse proximity slowly induces Sick; indoor generator fumes damage up to 5% of health. Gas masks or full suits mitigate *(B42)* |
| Discomfort | Wearing too many discomfort-bearing garments | Increases unhappiness *(B42)* |
| Dead | Death at zero health without zombie infection | Terminal; the only moodle that persists on screen |
| Zombie | Death at zero health while zombie-infected | Terminal; the alternative to Dead |

Five further moodles exist in the game but cannot be obtained in normal play [10]. **Angry** was an NPC-interaction moodle whose escalating stages blocked interaction attitudes up to open hostility; it is disabled with NPCs absent, can be forced via debug mode, and currently has no effect on anything. **Hungover** flagged being outdoors during or after intoxication and is no longer obtainable. **Fear**, **Morale** and **Sanity** are unimplemented values visible only in debug — Fear is nudged by some radio and television broadcasts but changing any of the three does nothing; sanity sound assets still ship in the game files [10].

Moodles are not purely informational plumbing, either: the 42.0.2 hotfix added sandbox multipliers for moodle effects on hit chance and halved the moodle hit-chance penalties outright, and confirmed that moodles are among the modifiers feeding melee/ranged accuracy alongside weather, lighting and headgear *(B42)* [17]. From 42.4.0, being at maximum Unhappy or Drunk doubles the time timed actions take *(B42)* [18].

## Injury types

Every entry below is a distinct injury state visible in the health panel, with its own causes and its own treatment path [12]:

| Injury | Symptoms | Principal causes | Treatment |
|--------|----------|------------------|-----------|
| Scratched | Minor health loss, bleeding, minor pain | Zombie scratch, smashing a window, botched vault while running, handling broken glass, vehicle collision, tripping | Bandage. **If inflicted by a zombie: 7% zombification chance** |
| Lacerated | Moderate health loss, bleeding, moderate pain | Same causes as scratches — a more severe form | Bandage, treatment identical to scratches. **If inflicted by a zombie: 25% zombification chance** |
| Bitten | Moderate health loss, bleeding, moderate pain | Zombie attack; zombies are far likelier to land bites from behind | Bandage stops the immediate loss, but **100% zombification** unless sandbox says otherwise. Long heal time if bites are made survivable |
| Bleeding | Health loss scaling with the number of bleeding wounds | Accompanies scratches, lacerations, bites, deep wounds, lodged bullets and lodged glass | Bandage the affected part. Untreated, it caps recovery or eventually kills |
| Deep Wound | Health loss, bleeding, moderate pain | Bare-handed window smashing, climbing through broken glass, walking on glass unshod, falling one level, extracting a bullet or shard, ~40–50 mph collisions, axe hits | Stitch with a suture needle or needle and thread (the suture needle hurts less). Alternatively bandage it for roughly a month |
| Lodged Bullet | Severe health loss, bleeding, moderate pain | Gunshot | Remove with tweezers, then treat as a deep wound: disinfect, stitch, bandage |
| Lodged Glass Shard | Severe health loss, bleeding, moderate pain | Breaking a window empty-handed, climbing through broken glass, picking up glass bare-handed, walking on glass unshod | Remove with tweezers or bare hands, then treat as a deep wound |
| Burn | Severe health loss, severe pain | Standing too close to fire | Bandage and keep the dressing clean; heal time is long. Extinguish the fire first — water or an extinguisher — or death follows quickly |
| Fracture | Severe health loss; leg fractures slow you, arm fractures wreck combat, torso fractures drain endurance, head fractures raise fatigue; severe pain | Falls from above ground level (worse when overloaded), 60 mph+ collisions, blunt-weapon impacts | Splint (ripped sheet plus a straight wooden item), then bandage. Head and torso fractures cannot be splinted. Comfrey poultices stack with splints |
| Exercise Fatigue | Pain; overworked arms swing slower and hit softer, overworked legs cost speed and add clumsiness | Overexercising | Wait it out; high regularity delays onset |
| Wound infection | A slow trickle of health damage while the wound sits unbandaged, minor pain | Any wound, open or bandaged, may become infected | Disinfect, dress with a sterilized bandage or rag, take antibiotics, or apply a wild garlic poultice. **Always survivable** |

Documented heal times, in hours unless noted, and how the Fast Healer and Slow Healer traits move them [12]:

| Injury | Base | Slow Healer | Fast Healer |
|--------|------|-------------|-------------|
| Scratch | 7–15 | 15–25 | 4–10 |
| Window scratch | 12–20 | 20–30 | 5–10 |
| Weapon scratch | 5–10 | 10–20 | 1–5 |
| Laceration | 10–20 | 20–30 | 5–10 |
| Bite | 50–80 | 80–150 | 30–50 |
| Deep wound (with or without glass) | 15–20 | 20–32 | 11–15 |
| Lodged bullet | 17–23 | 22–28 | 12–18 |
| Fracture (**days**) | up to 60 | up to 140 | up to 40 |
| Burn | 50–100 | 50–100 | 50–100 |

Two footnotes to that table matter in play. Scratches slow movement more than lacerations do per unit, but lacerations are more severe overall, so in practice a laceration is the bigger mobility loss most of the time [12]. Burns appear unaffected by either healing trait [12].

Several conditions are not "injuries" in the panel but behave like them [12]. Carrying a Very Heavy or Extremely Heavy Load produces a **back injury**: slower movement and health draining down to 75% and stopping there until the load is reduced. It is not listed separately in the panel and the only treatment is dropping weight; sitting down (on the ground or in a vehicle) stops the health drain [12]. **Fall damage** scales with height, encumbrance and traits such as underweight — a second-storey jump can produce severe damage, infected deep wounds and fractures, while higher falls can simply kill [12]. **Lower-limb injuries** from crawler attacks, crashes, falls or glass cause limping, blocking running and sprinting; bandaging improves limp speed slightly, but treating the leg forces the character to stop moving [12]. **Arm injuries** severely cut damage dealt with both melee weapons and firearms, which is the mechanism by which a bad fight leaves you unable to win the next one [12].

## The two infections, plus colds and food illness

The game uses one word for two unrelated systems, and conflating them is the most common medical misunderstanding in Project Zomboid [12] [14].

**Wound infection** is bacterial. A wound displaying *Infected* in the panel has been neglected — left unbandaged too long, or left under a dirty dressing. Its entire cost is pain: the wiki is explicit that it does not penalise health, healing rate or physical ability further, and that it roughly doubles the pain accrual of an untreated infected wound [12] [15]. Clean bandaging lowers infection chance; disinfecting first and applying a sterilized bandage or rag lowers it further and can clear an existing infection; dirty bandages actively raise it [12] [15]. Antibiotics reduce wound-infection strength [15]. Non-zombie infected wounds are 100% survivable [12]. B42 exposes a `WoundInfectionFactor` sandbox multiplier over the damage this system does — raised from 0.5 (and from 0.0 in some presets) to 1.0 across the board in 42.17, and set to 2.0 for the Extinction preset in 42.20 stable *(B42)* [1] [6] [16].

**The Knox Infection** is the zombie disease and is invisible: nothing in the UI ever tells you that you have it [12] [14]. It is contracted only from zombie attacks that break the skin — scratches, lacerations and bites — and no non-zombie injury can ever transmit it [14]. It is untreatable. Disinfection does not remove it, first aid does not affect the odds of catching it, and there is no cure or treatment of any kind [14] [15]. Its progression can only be *slowed*, by staying well fed, hydrated and free of a cold, never halted or reversed [14].

Beyond those two, the **common cold** is contracted from prolonged wet or cold exposure and produces sneezing and coughing that attracts zombies; it is cured by staying indoors, fed, hydrated and rested, and cannot be treated with antibiotics [10] [12]. **Food illness** comes from spoiled or dangerous food and tainted water, initially slowing healing and, if it reaches fever, draining health toward death [12]. Its documented duration in in-game ticks is 200–280 normally, 120–230 with Weak Stomach and 80–150 with Iron Gut [12]. Lemongrass soothes food poisoning [15]. **Corpse sickness** from decaying bodies drives the Sick moodle through the Noxious smell channel, and B42 exposes it as `DecayingCorpseHealthImpact` with an optional `ZombieHealthImpact` extension to living zombies nearby *(B42)* [10] [16].

## Zombification: the numbers

The chance of contracting the Knox Infection from a zombie-inflicted wound, on default settings [14]:

| Zombie wound | Zombification chance |
|--------------|---------------------|
| Scratch | 7% |
| Laceration | 25% |
| Bite | 100% |

These are the load-bearing figures of this document and they are corroborated across separate wiki pages and separate build-era revisions: the Knox Infection page states them as a set [14], while the Health page states 7% for zombie scratches ("in build 41 and later") and 25% for zombie lacerations in both its 41.78.16-stamped and its 42.15.3-stamped revisions [12] [13]. That agreement across builds is the basis for treating the odds as unchanged from B41 to B42. No Indie Stone patch note stating these percentages was located, so they remain wiki-sourced.

Two traits shift the *speed* of the disease, not the odds of catching it: **Resilient** reduces the zombification rate by 25% and **Prone to Illness** raises it by 25% [14]. The documented symptom timeline on default settings [14]:

| Time since infection | Stage |
|----------------------|-------|
| Immediately | Rapid body-temperature increase |
| 1–4 hours | Anxiety |
| 5–12 hours | Queasy moodle (stage 1); health starts slipping |
| 13–24 hours | Nauseous (stage 2); the drain steepens |
| 25–48 hours | Sick (stage 3); health falls away hard |
| 49–71 hours | Fever (stage 4); the damage is no longer survivable |
| 72 hours | Death, then reanimation |

Because nothing announces the infection, diagnosis is inferential: stress and queasiness with rising body temperature, appearing for no other reason within hours of a zombie encounter, is effectively confirmation [14]. The First Aid page frames the practical rule as monitoring a zombie-inflicted scratch or laceration for at least the 24-hour incubation period before concluding you are clear [15]. Infected characters reanimate within a minute or two of death regardless of what actually killed them [14].

Sandbox governs all of this through three keys, all in the Zombies tab [14] [16]:

| Key | Default | Options |
|-----|---------|---------|
| `ZombieLore.Transmission` | Blood and Saliva (1) | Blood and Saliva — scratches, lacerations and bites all transmit; Saliva Only (2) — bites only; Everyone's Infected (3) — every death reanimates regardless of cause; None (4) — never transmits, not even from a bite |
| `ZombieLore.Mortality` | 2–3 Days (5) | Instant, 0–30 Seconds, 0–1 Minutes, 0–12 Hours, 2–3 Days, 1–2 Weeks, Never. "Never" means survival is possible, not that infection cannot be caught |
| `ZombieLore.Reanimate` | 0–1 Minutes (3) | Instant, 0–30 Seconds, 0–1 Minutes, 0–12 Hours, 2–3 Days, 1–2 Weeks. Uninfected corpses never rise unless Transmission is Everyone's Infected |

The enum codes and defaults above come from the 42.20-stamped sandbox listing [16]; the option semantics come from the Knox Infection page, versioned 42.13.1 [14]. B42 additionally exposes `InjurySeverity` (Low/Normal/High, governing injury impact and healing time) and `BoneFracture` (on/off) — neither of which exists in the B41 sandbox schema *(B42)* [16]. See `admins-sandboxvars-reference` for the full key surface.

## The First Aid skill

First Aid is a survivalist skill whose in-game tooltip promises increased information about injuries and improved treatment quality [15]. Its technical skill ID is `Doctor` [15]. XP is earned by performing medical actions, on yourself or on other players [15].

What it actually modifies, per skill level [15]. Reading the pattern rather than memorising the cells: dressing longevity gains 15 percentage points per level, fracture mending gains 50 points per level from a halved baseline, and the mobility-while-fractured modifier climbs 0.05 per level:

| Skill level | Dressing longevity | Fracture mending rate | Mobility modifier while fractured |
|-------------|--------------------|-----------------------|-----------------------------------|
| 0 | ×1.00 | ×0.5 | 0.25 |
| 1 | ×1.15 | ×1.0 | 0.30 |
| 2 | ×1.30 | ×1.5 | 0.35 |
| 3 | ×1.45 | ×2.0 | 0.40 |
| 4 | ×1.60 | ×2.5 | 0.45 |
| 5 | ×1.75 | ×3.0 | 0.50 |
| 6 | ×1.90 | ×3.5 | 0.55 |
| 7 | ×2.05 | ×4.0 | 0.60 |
| 8 | ×2.20 | ×4.5 | 0.65 |
| 9 | ×2.35 | ×5.0 | 0.70 |
| 10 | ×2.50 | ×5.5 | 0.75 |

Alongside those, higher levels perform medical actions faster, make poultices last longer, make splints more effective, and improve the character's assessment of wound and infection severity [15]. Two negatives are stated as explicitly as the positives: First Aid **does not** make scratches or lacerations heal faster, and it has **no influence** on whether a zombie-inflicted wound leads to zombification [15]. Well fed adds a separate +30% to injury healing rate, independent of skill [15].

Starting levels and XP rates [15]:

| Route | Effect |
|-------|--------|
| Doctor (occupation) | +6 |
| Nurse (occupation) | +3 |
| Park Ranger (occupation) | +1 |
| First Aider (trait) | +1 |
| Former Scout (trait) | +1 |
| Fast Learner (trait) | XP rate 130% |
| Slow Learner (trait) | XP rate 70% |

Skill books run in the usual two-level bands — *A Scouts Injury Guide* (1–2), *Bandaging and Suturing* (3–4), *Emergency Paramedics Manual* (5–6), *Gray's Anatomy of the Human Body* (7–8), *Surgical Techniques of the Operating Room* (9–10) [15]. Two VHS tapes award XP toward the skill — *Combat Wound Management* at +87.5 and *RMFA* at +75 — with entertainment gains capped to the first three levels plus overflow [15]. See `players-skills-xp` for how the band multipliers and XP curve work generally.

The documented treatment order is: identify wound type and location; bandage scratches and lacerations promptly, because untreated wounds do not heal at all and dirty bandages do not slow healing (only *unbandaged* time does, which is why swapping a dirty dressing mid-heal is not urgent for healing purposes); for deep wounds remove any foreign object first — mandatory for bullets — using tweezers or a suture needle holder, then stitch, then bandage, which halves recovery time; for fractures splint where possible, bandage, and apply comfrey to cut fracture recovery by 50%; for burns, extinguish first, then treat as for lacerations while expecting a much longer heal [15].

Indicative item values [15]:

| Category | Item | Key value |
|----------|------|-----------|
| Bandage | Adhesive bandage | Bandage power 1.5 |
| Bandage | Bandage / Sterilized bandage | Bandage power 4.0 |
| Bandage | Denim strips, leather strips, rag | Bandage power 2.0 |
| Bandage | Any dirty variant | Bandage power 0.5 |
| Disinfectant | Bottle of disinfectant | Disinfect power 3 |
| Disinfectant | Bourbon | Disinfect power 2 |
| Disinfectant | Alcohol wipes / alcohol-doused cotton balls | Disinfect power 4 |
| Suture | Suture needle | Single use, low pain |
| Suture | Needle and thread | Reusable thread, higher pain |
| Suture | Forceps | Not consumed; speeds the procedure and reduces pain while merely held |

All bandages heal at the same rate; the differences are purely in how quickly they turn dirty and how they interact with infection [15]. Of the seven medicinal plants, plantain, comfrey and wild garlic must be ground into poultices with a mortar and pestle — plantain for wounds, comfrey for fractures, wild garlic against infection — while black sage (mild pain relief), common mallow (cold and flu), ginseng (endurance) and lemongrass (food poisoning) are eaten raw [15]. The poultice recipes are auto-learnt at First Aid 5 or Foraging 5, or from the *Wilderness Survival* magazine [15].

## Muscle strain (Build 42)

Muscle strain is Build 42's addition to the cost of fighting, and The Indie Stone introduced it as a deliberate change to the game's *flow*: alongside rebalanced zombie spawns and a renewed emphasis on sneaking past crowds, "combat building up muscle strain" was one of the changes internal testers responded to before Unstable launched, described as making the game slower, more tactical and zombies more of a threat *(B42)* [2]. A tester quote The Indie Stone published a month earlier captures the intended feel — strain arriving after roughly fifteen zombies bashed, functioning as atmosphere rather than a hard wall *(B42)* [9].

Mechanically it is not a moodle. It is fatigue damage applied to the specific body parts that performed the work, which then surfaces through Pain and the associated limb penalties [12]. The mechanics documented on the wiki *(B42, page versioned 42.15.3, not re-verified on 42.20)* are [12]:

- **All combat.** Strain scales down with the relevant weapon skill and with Strength. Each weapon-skill level cuts muscle fatigue by 7.5%, reaching 10% of the baseline at level 10. Strength starts at a 150% multiplier at level 0 and drops 10% per level to 50% at level 10. Strain scales with the number of zombies struck — hit two, take twice as much.
- **Melee weapons.** The base multiplier is 60% of weapon weight plus 120% of the weapon's endurance modifier. A two-handed weapon held in one hand adds 4/15 of its weight to that multiplier; gripping it properly with both hands cuts that surcharge in half. Fatigue lands at 250% on the right hand, forearm and upper arm, and — for two-handed use — the same again on the left side.
- **Firearms.** Recoil delay multiplies the fatigue damage, and full-auto fire halves the strain. Damage goes 100% to the right hand and 100% to the right forearm; a two-handed firearm adds 100% to the right upper arm and 10% each to the left hand and forearm.
- **Stomping.** Only 0.3 muscle fatigue, applied at 250% (0.75 total) to the right thigh, calf and foot. The multiplier and damage values passed to the strain call are irrelevant here.
- **Shoving.** Only 0.15 muscle fatigue, applied at 250% (0.375 total) across both upper arms, both forearms and both hands.
- **Other sources.** Over-encumbrance at level 2 or higher converts its health damage into muscle strain. Sheet-rope climbs load the arms at a base 0.02 strain per tick (0.007 climbing down), doubled per over-encumbrance level, with a 150% multiplier at Strength/Fitness/Nimble 0 — every 3 Nimble levels cuts it 10%, every level of the higher of Strength/Fitness cuts it 20%, bottoming at 50% with Nimble 10 and Strength or Fitness 10. Vaulting a wall runs on the same math. Certain timed actions apply strain to specific parts scaled by a relevant skill, 150% at level 0 down to 50% at level 10. Exercise adds strain matching the muscle group trained, but with roughly a 12-hour delay before it appears.

The balance history is fully primary-sourced and is worth knowing, because guides written at different points in the unstable cycle describe materially different systems. Melee weapon strain was cut to **60% of its launch value** in hotfix 42.0.1, three days after Unstable went public, with the sandbox value left untouched and the reduced figure becoming the new baseline *(B42)* [3]. In 42.1, over-encumbrance strain was **halved** (and only applies once encumbrance is heavy enough to also damage health), stone tools were tuned to produce roughly double the strain, and a bug causing health loss and strain from heavy loads *while sitting on furniture* was fixed *(B42)* [4]. 42.15 introduced the Apocalypse preset as the lore-canon mode with explicitly **reduced Muscle Strain and Discomfort impact**, and rebalanced inconsistent neck strain from sewing actions *(B42)* [5]. 42.16 reduced strain from digging furrows with a spade *(B42)* [7], and 42.21 reduced the strain from digging a single grave, listed under the multiplayer fixes *(B42)* [26]. 42.17 fixed climbing over walls not generating strain at all *(B42)* [6]. Multiplayer took two passes: 42.14.1 fixed combat strain not syncing between clients, and 42.18 fixed body damage and muscle strain from over-encumbrance accumulating **over four times faster** in multiplayer than intended *(B42)* [8] [19].

Two sandbox multipliers govern the system's weight. `MuscleStrainFactor` (default 0.7 on 42.20) scales strain, and `DiscomfortFactor` (default 0.8) scales the clothing-discomfort effect; the latter was added in 42.1 and described at the time as working like the existing Muscle Strain Factor — disable, reduce or increase *(B42)* [4] [16].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Muscle strain | Absent — the 41.78.16-stamped Health revision has no muscle-strain content at all [13] | Present as a full system with per-limb application, skill scaling and its own sandbox multiplier [2] [12] [16] |
| Active moodle roster | 21 moodles; Restricted movement is listed among the removed/unobtainable [11] | 24 moodles; Restricted movement is obtainable, and Noxious smell and Discomfort are added [10] |
| Unimplemented moodles | Restricted movement, Angry, Hungover, Fear, Sanity [11] | Angry, Hungover, Fear, Morale, Sanity [10] |
| Dormant moodle art | — | Nine further icons ship unused: Concentrating, Dizzy, Exhausted, Happy, Scared, HearingImpaired, Sedated, VisionImpaired, Wired [10] |
| Bleeding moodle | Level tracked the count of bleeding body parts, ignoring their severity [4] | A bleeding neck injury pins the moodle to maximum from 42.1 [4] |
| Discomfort | No such system | Discomfort moodle, `DiscomfortFactor` sandbox multiplier from 42.1, encumbrance-scaled discomfort in vehicles from 42.14, and a recoloured icon in 42.19 to separate it from Unhappy [4] [16] [20] |
| Endurance moodle | Static indicator | Doubles as a rest progress indicator from 42.12; the animated variant was disabled again in 42.13 pending edge-case fixes [21] [22] |
| Moodle → combat maths | Baseline penalties | Hit-chance penalties from moodles halved, and sandbox multipliers added over moodle effects on hit chance, in 42.0.2 [17] |
| Medical sandbox surface | No `InjurySeverity`, `BoneFracture`, `WoundInfectionFactor`, `MuscleStrainFactor`, `DiscomfortFactor`, `DecayingCorpseHealthImpact` or `ZombieHealthImpact` keys [16] | All present; `WoundInfectionFactor` standardised to 1.0 in 42.17 and set to 2.0 for Extinction in 42.20 [1] [6] [16] |
| Zombification odds | Scratch 7%, laceration 25%, bite 100% [13] | Unchanged: scratch 7%, laceration 25%, bite 100% [12] [14] |
| Health panel and body model | 17 sections, same status ladder [13] | 17 sections, same status ladder [12] |
| Deep wound causes | Does not list bullet/shard extraction as a cause [13] | Extracting a lodged bullet or glass shard is listed as a deep-wound cause [12] |
| Antibiotics packaging *(42.21)* | Not covered by the 42.21 notes | Antibiotics can be packaged with the "pack in box" crafting recipe [25] [26] |
| Pill-taking sync *(42.21)* | — | Fixed a remote player getting stuck in a repeated animation after taking pills (multiplayer) [26] |
| Medical UI fixes | — | Split-screen medical checks fixed in 42.20 stable; a translation error in the health panel's moodle info fixed in 42.6 [1] [23] |

One deliberate non-change deserves emphasis. The odds that define whether a run ends — 7%, 25%, 100% — are stated identically in the B41-stamped and B42-stamped wiki revisions [12] [13] [14]. Build 42 changed how hard it is to *avoid* being wounded (spawn rebalancing, darkness, strain, sneaking) far more than it changed what a wound means once you have one [2].

The Hungry moodle's description also differs between the two revisions: the B41 text credits being well fed with boosting strength, carry capacity and healing rate, while the B42 text credits healing rate and attributes carry-capacity and body-heat losses to hunger [10] [11]. Whether that reflects a mechanical change or a wiki rewrite is unresolved — see Open Questions.

# Practical Guidance

- **Bandage first, everything else second.** Untreated wounds do not heal at all, and bleeding both drains health and caps recovery. Because dirty bandages do not slow healing while *unbandaged* time does, the correct emergency move is to slap on whatever you have — a ripped sheet counts — and refine the treatment later.
- **Treat a neck wound as a countdown, not an injury.** The neck ignores the damage cap. If the health panel shows anything on the neck, stop what you are doing and dress it before you deal with the zombie, the door or the fire.
- **Learn the two-infection distinction and you stop panicking correctly.** "Infected" in the health panel is bacterial and survivable. The Knox Infection never appears in the panel at all. If you are asking whether you are zombie-infected, the answer is in what wounded you and how long ago, not in the UI.
- **Diagnose by exclusion inside the first 24 hours.** Anxiety, queasiness and a temperature spike with no other cause, following a zombie scratch or laceration, is effectively a positive. A scratch from a window or a fence carries no zombification risk whatsoever, so the *source* of the wound is the first thing to establish.
- **A scratch is a 93% survival chance; a laceration is 75%; a bite is over.** That framing is worth internalising because it changes behaviour: a scratched character should keep playing carefully rather than suiciding, while a bitten character on default settings should spend the remaining ~72 hours securing the base and stashing loot for the next survivor.
- **Buy First Aid for fractures, not for scratches.** Level 4 roughly triples fracture healing speed relative to level 0 and improves the mobility modifier while fractured; it does nothing for scratch and laceration heal times and nothing at all for zombification odds. If your run keeps ending in falls and car crashes, it is worth the points; if it keeps ending in bites, it is not.
- **Add comfrey to the fracture plan.** A splint, a bandage, a comfrey poultice and being well fed stack into a fracture recovery that is measured in a manageable number of days instead of dozens.
- **Carry disinfectant and a spare clean bandage, not a pharmacy.** Bandage power differences are small and all dressings heal identically; the value in the medical kit is in disinfectant, sterilized dressings, tweezers or forceps, a suture needle, and painkillers.
- **On B42, fight in shorter bursts.** Strain scales with the number of zombies hit and lands on the arms doing the swinging, so ten zombies in one uninterrupted brawl costs far more than ten spread across a morning. Stomping and shoving are cheap by comparison, and levelling your weapon skill and Strength is a direct strain reduction.
- **Two-hand a two-handed weapon.** Holding one in a single hand adds weight to the strain multiplier; holding it properly halves the increase. This is free performance.
- **Sandbox is a legitimate answer.** If permanent-death-by-scratch is not the game you want, `ZombieLore.Transmission` set to Saliva Only removes scratch and laceration risk entirely while keeping bites lethal — a far better dial than "Never", which removes the threat altogether. `MuscleStrainFactor` does the same job for B42's combat fatigue.
- **Check any B42 guide's date against the strain patches.** A guide written in the first week of Unstable describes melee strain that was cut to 60% almost immediately, and one written before 42.15 predates the Apocalypse preset's reduced-strain tuning.

# Common Pitfalls & Troubleshooting

- **"I disinfected the bite, so I'm fine."** Disinfection acts on bacterial wound infection only. It has no effect on the Knox Infection, and neither does any level of First Aid.
- **"My First Aid is 10 and this scratch is still taking forever."** Expected. First Aid never accelerated scratch or laceration healing; the skill's healing lever is fractures.
- **Changing a dirty bandage mid-crisis.** Dirty dressings raise wound-infection chance, which is a pain penalty — they do not slow healing. Bare, unbandaged time does slow healing. Prioritise accordingly.
- **"The Injured moodle isn't showing, so I'm not hurt."** Injured tracks health level, not the presence of a wound. Light injuries can sit below its threshold entirely. Read the health panel, not the moodle rack.
- **Ignoring Heavy load as a cosmetic nag.** At the extreme it can cost as much as a quarter of total health in direct damage, and on B42 it also converts that damage into muscle strain. Sitting down stops the health drain, which is a genuinely useful emergency trick.
- **Running a generator indoors.** The Noxious smell moodle's toxic-fumes variant damages up to 5% of health. It is easy to miss because the moodle icon is shared with corpse sickness, which is the far more familiar cause.
- **Treating an upper-torso fracture as background noise.** It caps health near 60%, which turns a survivable fight into a fatal one. Head and torso fractures cannot be splinted, so the only levers are First Aid level, comfrey and being well fed.
- **Jumping from a second-storey window to escape.** Documented outcomes include severe damage, infected deep wounds and fractures; higher floors can kill outright. The fall is often worse than the horde.
- **Assuming B41 muscle-strain habits.** There are none — B41 has no muscle strain. A returning player whose instinct is to clear thirty zombies in one continuous fight is playing a B41 pattern on a B42 body.
- **Reading unstable-era B42 strain numbers as current.** The system was retuned repeatedly across 42.0.1, 42.1, 42.15, 42.16, 42.17 and 42.18, including two multiplayer-only accumulation bugs. Anything not stamped 42.20 is suspect.
- **Expecting a zombie-infection warning.** There is none, by design. The only readout you get is the symptom sequence, which overlaps with food poisoning and colds — hence the incubation-period rule.

# Community Notes & Unverified Claims

## Claim 1 — First Aid makes wounds heal faster

- **Claim:** A widespread belief among players, repeated across guides and forum advice, that levelling First Aid shortens the healing time of scratches, lacerations and other open wounds, and is therefore a general survivability skill.
- **Why unverified:** Directly contradicted by [15], which names it as a popular misconception and lists the skill's actual effects (action speed, bandage and poultice longevity, splint effectiveness, fracture healing, wound assessment) without any general heal-rate term.
- **Confidence:** Low. The claim is common but the cited source refutes it explicitly, and the mechanical effect table in [15] leaves no room for a hidden general modifier.

## Claim 2 — A zombie bite is survivable

- **Claim:** Persistent community lore that a bite can be survived through rest, nutrition, disinfection, antibiotics or luck — sometimes traced to a remembered 4% survival chance.
- **Why unverified:** [14] documents the 4% figure as a genuine mechanic from patch 0.1.6a that was removed in later updates, and states that a bite is 100% lethal on default settings, with rest-and-nourishment recovery attributable to the Hypochondriac trait, ordinary food sickness or wound-infection confusion. No primary Indie Stone source stating a modern survival chance was located.
- **Confidence:** Low as a claim about current builds; the historical 4% is credible as a description of a superseded version, not of 41.78 or 42.20.

## Claim 3 — Muscle strain from sheet ropes scales exponentially with game speed because of a double-applied time multiplier

- **Claim:** The community mechanics writeup states that the time multiplier in the sheet-rope strain calculation is applied twice due to a bug, so strain grows exponentially under fast-forward or short-day settings and shrinks under debug slowdown or long days.
- **Why unverified:** Sourced only to [12], which reads as code-derived analysis rather than tested behaviour; no Indie Stone patch note acknowledging or fixing such a bug appears in the announcement history scanned for this document, and the page is versioned 42.15.3, five releases before stable.
- **Confidence:** Low. The surrounding formula detail in the same source is plausible and internally consistent, but a claimed engine bug with no primary trace and no post-42.15 re-verification cannot be rated higher.

## Claim 4 — Zombies with bloodied hands are more infectious, and broken glass can transmit the infection

- **Claim:** Two related pieces of folk wisdom — that visibly bloody zombies carry higher scratch-infection odds, and that climbing through an uncleared broken window risks zombification.
- **Why unverified:** Both are listed as myths by [14], which attributes bloodied hands to window-climbing animation state and states that only direct zombie attacks transmit the infection, though glass wounds can still develop ordinary wound infections. No primary source supports either belief.
- **Confidence:** Low. The refutation is consistent with the transmission rules documented in [12] and [14], but rests on a single unstable-era wiki page rather than a patch note.

## Claim 5 — Build 42 is meaningfully more lethal per-wound than Build 41

- **Claim:** Community consensus following B42's release holds that the build is harsher medically, citing muscle strain, darker interiors and denser hotspots.
- **Why unverified:** The constituent changes are primary-sourced [2] [5], but the per-wound outcome numbers are identical across builds [12] [13] [14] — the difficulty change is in exposure and recovery friction, not in what a scratch does. "More lethal" is therefore a synthesis, not a measurable claim, and no controlled comparison exists.
- **Confidence:** Medium. The underlying mechanical changes are confirmed; the aggregate difficulty judgement is not verifiable.

# Risks & Caveats

- **Unstable-era wiki version stamps are this document's largest risk.** Moodle is stamped 42.13.2, Health 42.15.3, First Aid 42.18.0 and Knox Infection 42.13.1 [10] [12] [14] [15]. Between 42.13 and 42.20 the game shipped seven unstable releases plus stable, several of which touched medical and strain systems [5] [6] [7] [8]. Any figure here not independently confirmed by an announcement should be treated as "last known good", not "current".
- **The transmission percentages are wiki-sourced, not patch-note-sourced.** They are corroborated across two pages and two build eras [12] [13] [14], which is why this document states them plainly, but no Indie Stone publication naming 7% and 25% was found. If one exists it should be added and this document's confidence reconsidered.
- **The muscle-strain formulas read as datamined.** The level of detail in [12] — exact multipliers, which body parts receive what fraction, the name of the internal strain call — indicates code inspection rather than in-game measurement. Code-derived values are usually accurate and usually stale; both apply here.
- **The B41 side rests on two archived revisions.** The 41.78.16-stamped Moodle and Health revisions [11] [13] were fetched by revision id and are stable, but they are single sources for the B41 roster and B41 injury behaviour, with no second B41-era source cross-checking them.
- **Roster-diff inference.** The moodle delta is derived by comparing two wiki revisions, not from a developer changelog. "B42 added Noxious smell and Discomfort" describes what the two rosters contain; the exact release in which each arrived is not established here, and Discomfort's arrival is only indirectly dated by the 42.1 sandbox-setting note [4].
- **Sandbox defaults move.** `WoundInfectionFactor` changed twice within four months of stable release [1] [6]. The defaults in this document are those in the 42.20-stamped listing [16] and are as perishable as any other balance value.
- **Bot-blocked primary hosts.** All Indie Stone citations use Steam announcement URLs, which bot-block automated link checkers by design; they were retrieved and verified through the ISteamNews API for app 108600, and the gid in each URL comes from that API response.
- **42.20 is two days old** at the time of writing. A hotfix wave is expected and could invalidate any balance number here. Update, 2026-10-07: hotfixes 42.20.1 to 42.20.4 and 42.21 followed; the notes reviewed [24] [25] [26] contain only the three medical items recorded above, but the strain, infection and moodle numbers were not re-tested in-game.

# Verification Steps

1. **Confirm the body model and status ladder:** start any game, press `H`, and count the selectable regions on the diagram (expect 17). Take light damage and confirm the qualitative status text matches the ladder in the Reference section.
2. **Confirm the moodle roster on 42.20:** enter debug mode, open the moodles panel, and enumerate the available moodles. Compare against the 24-entry table above; specifically check whether Restricted movement, Noxious smell and Discomfort are present and whether any of the nine dormant icons (Concentrating, Dizzy, Exhausted, Happy, Scared, HearingImpaired, Sedated, VisionImpaired, Wired) have become obtainable.
3. **Confirm the zombification odds:** the definitive check is the game's own scripts — inspect the infection-chance constants in the installed 42.20 build's Java/Lua source or via the pinned Umbrella stubs for the character health classes, and repeat against a 41.78.16 install. Failing that, a large-sample in-game test (fifty-plus zombie scratches on a fresh sandbox character with Mortality set to Instant) will bracket the 7% figure.
4. **Confirm First Aid's effect table:** create two characters, one at First Aid 0 and one at First Aid 10 (Doctor plus books, or debug-set), fracture the same limb on each, and compare healing durations; a ~5.5× versus 0.5× ratio corroborates the multiplier table.
5. **Confirm First Aid does not affect wound heal time:** same two characters, identical scratches, compare the hours to close. Expect no difference.
6. **Confirm muscle-strain scaling:** on 42.20, with debug on, record limb fatigue after ten swings at one zombie versus ten swings connecting with three, and repeat at weapon skill 0 and 10. Expect roughly linear scaling with zombies struck and roughly a 10× reduction at skill 10.
7. **Confirm the sandbox keys:** generate a fresh 42.20 `SandboxVars.lua` from a dedicated server and grep for `Transmission`, `Mortality`, `Reanimate`, `MuscleStrainFactor`, `DiscomfortFactor`, `WoundInfectionFactor`, `InjurySeverity` and `BoneFracture`; compare defaults against the tables above and against `admins-sandboxvars-reference`.
8. **Confirm the strain balance history:** re-query the Steam news API — `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0` — and search the returned bodies for "muscle strain" to reproduce the patch list in the Reference section.
9. **Re-verify the wiki sources:** open each cited pzwiki revision URL (each pins an `oldid`) and diff against the live page to catch post-42.20 corrections.

# Open Questions

- Do the zombification percentages (7% / 25% / 100%) hold on 42.20 stable, and is there any Indie Stone primary source that states them? This is the single highest-value open item in this document.
- Did the Hungry moodle's benefits actually change between builds — specifically, does being well fed still boost strength and carry capacity as the B41 revision states, or only healing rate as the B42 revision states? A debug-mode comparison across `legacy41` and 42.20 resolves it.
- In which release did Discomfort and Noxious smell become obtainable moodles, and in which did Restricted movement move from unobtainable to active? The revision diff narrows it; a changelog scan would pin it.
- Are the nine dormant B42 moodle icons (Concentrating, Dizzy, Exhausted, Happy, Scared, HearingImpaired, Sedated, VisionImpaired, Wired) scheduled for the announced Build 42 Support Update, or are they, like Fear and Morale, indefinitely parked?
- Is the sheet-rope time-multiplier double-application (Claim 3) real on 42.20, and if so has it been reported?
- Do the First Aid multiplier tables hold on 42.20, given the page is stamped 42.18.0 and the skill received no announcement-level changes in 42.19 or 42.20 that were located?
- What is the actual formula linking bandage power to time-to-dirty, and how does the First Aid bandage-life multiplier compose with it?
- Does `InjurySeverity` scale heal times, damage-on-injury, or both? The sandbox listing names the effect only in general terms.

# References

**Primary Sources** — official Indie Stone Steam announcements and patch notes, retrieved and verified through the Steam news API (`ISteamNews`, app 108600).

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; Extinction-preset wound-infection rebalance, split-screen medical-check fix). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *WhatZ Next* (Thursdoid, Steam announcement, 2024-11-28; muscle strain named as a deliberate change to the game's flow). https://steamcommunity.com/games/108600/announcements/detail/1784506359022970. Accessed 2026-07-31.
- [3] **The Indie Stone** — *Hotfix 42.0.1 - Unstable Release* (Steam announcement, 2024-12-20; melee muscle strain reduced to 60% of its previous value). https://steamcommunity.com/games/108600/announcements/detail/1786573930668296. Accessed 2026-07-31.
- [4] **The Indie Stone** — *42.1 UNSTABLE Released* (Steam announcement, 2025-01-21; Discomfort Modifier sandbox setting, halved over-encumbrance strain, neck-bleeding moodle change). https://steamcommunity.com/games/108600/announcements/detail/1789039014507745. Accessed 2026-07-31.
- [5] **The Indie Stone** — *Build 42.15.0 Unstable Released* (Steam announcement, 2026-03-09; Apocalypse preset with reduced muscle-strain and discomfort impact, neck-strain rebalance). https://steamcommunity.com/games/108600/announcements/detail/1826362059930323. Accessed 2026-07-31.
- [6] **The Indie Stone** — *Build 42.17.0 Unstable Released* (Steam announcement, 2026-04-20; Wound Infection Damage Factor raised to 1.0, wall-climb strain fix). https://steamcommunity.com/games/108600/announcements/detail/1830163047266254. Accessed 2026-07-31.
- [7] **The Indie Stone** — *Build 42.16.0 Unstable Released* (Steam announcement, 2026-03-31; reduced muscle strain from digging furrows). https://steamcommunity.com/games/108600/announcements/detail/1828441623111900. Accessed 2026-07-31.
- [8] **The Indie Stone** — *Build 42.18.0 Unstable Released* (Steam announcement, 2026-05-11; multiplayer over-encumbrance damage and strain accumulation fix). https://steamcommunity.com/games/108600/announcements/detail/1832065502820909. Accessed 2026-07-31.
- [9] **The Indie Stone** — *Hallodoid* (Thursdoid, Steam announcement, 2024-11-01; published closed-beta tester impression of muscle strain in combat). https://steamcommunity.com/games/108600/announcements/detail/6146943657173915715. Accessed 2026-07-31.
- [17] **The Indie Stone** — *Unstable Branch Hotfix 42.0.2 Released!* (Steam announcement, 2024-12-23; moodle hit-chance penalties halved, sandbox multipliers for moodle effects on hit chance). https://steamcommunity.com/games/108600/announcements/detail/1786573930748612. Accessed 2026-07-31.
- [18] **The Indie Stone** — *42.4.0 UNSTABLE Released* (Steam announcement, 2025-03-04; maximum unhappiness and drunkenness double timed-action duration). https://steamcommunity.com/games/108600/announcements/detail/1792751526173735. Accessed 2026-07-31.
- [19] **The Indie Stone** — *42.14.1 BETA HOTFIX Released* (Steam announcement, 2026-02-18; combat muscle strain not synced in multiplayer). https://steamcommunity.com/games/108600/announcements/detail/1825093633182113. Accessed 2026-07-31.
- [20] **The Indie Stone** — *Build 42.19.0 Unstable Released* (Steam announcement, 2026-06-01; Discomfort moodle recoloured to differentiate it from Unhappy). https://steamcommunity.com/games/108600/announcements/detail/1833968530897275. Accessed 2026-07-31.
- [21] **The Indie Stone** — *42.12.0 UNSTABLE Released* (Steam announcement, 2025-09-25; Endurance moodle acts as a rest progress indicator). https://steamcommunity.com/games/108600/announcements/detail/1811772772244324. Accessed 2026-07-31.
- [22] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement, 2025-12-11; animated Endurance moodle indicator disabled). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972. Accessed 2026-07-31.
- [23] **The Indie Stone** — *42.6.0 UNSTABLE Released* (Steam announcement, 2025-03-24; health-panel moodle info translation fix). https://steamcommunity.com/games/108600/announcements/detail/1794830911001792. Accessed 2026-07-31.
- [24] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [25] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23; antibiotics packaging recipe). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [26] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post, 2026-09-23; reduced Muscle Strain from digging a single grave, antibiotics packaging). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cited by URL and revision id for facts only; all prose in this document is original.

- [10] **PZwiki** — *Moodle* (revision 1362797; page versioned against 42.13.2, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Moodle&oldid=1362797. Accessed 2026-07-31. Fact-only source.
- [11] **PZwiki** — *Moodle*, archived Build 41 revision (revision 478895, 2024-09-07; page versioned against 41.78.16). https://pzwiki.net/w/index.php?title=Moodle&oldid=478895. Accessed 2026-07-31. Fact-only source.
- [12] **PZwiki** — *Health* (revision 1389265; page versioned against 42.15.3, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Health&oldid=1389265. Accessed 2026-07-31. Fact-only source.
- [13] **PZwiki** — *Health*, archived Build 41 revision (revision 625901, 2024-11-12; page versioned against 41.78.16). https://pzwiki.net/w/index.php?title=Health&oldid=625901. Accessed 2026-07-31. Fact-only source.
- [14] **PZwiki** — *Knox Infection* (revision 1438437; page versioned against 42.13.1, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Knox_Infection&oldid=1438437. Accessed 2026-07-31. Fact-only source.
- [15] **PZwiki** — *First Aid* (revision 1439359; page versioned against 42.18.0, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=First_Aid&oldid=1439359. Accessed 2026-07-31. Fact-only source.
- [16] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0; source of SandboxVars key names, defaults and enum codes). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating** — none cited. No hosting-company knowledge base or community guide was used as a source for any value in this document.

**Community & Creator** — none cited. The community beliefs quarantined above are described as circulating positions, not sourced to individual posts.

**Further Reading**

# Further Reading

- The Steam news API endpoint used to retrieve and verify every primary citation above: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0
- The Indie Stone's official blog, the canonical home of the Thursdoids mirrored as Steam announcements: https://projectzomboid.com/blog/ (bot-blocks automated checkers; verify in-browser).
- pzwiki's medical item category listings, useful for exhaustive per-item statistics this document deliberately summarises: https://pzwiki.net/wiki/Medical

# Related Documents

- `players-foundation` — the Players-track overview this document deepens; it introduces moodles at roster level and stops there.
- `players-skills-xp` — how skill levels, XP curves and skill-book bands work generally; the First Aid section here assumes it.
- `players-traits-occupations` — full trait and occupation tables, including Fast Healer, Slow Healer, Resilient, Prone to Illness, First Aider and Former Scout.
- `admins-sandboxvars-reference` — the complete SandboxVars key surface, including every key referenced here with its type, range and build applicability.
- `meta-style-guide` — the evidence, quarantine and build-tagging rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: reviewed Steam announcements 42.20.1-42.21 and the 42.21 forum changelist [24] [25] [26]; added the antibiotics pack-in-box recipe, the reduced grave-digging strain and the MP pill-taking animation fix; version-scope statements updated. | — |
