---
id: players-beginner-guide-b42
title: "Starting Project Zomboid on Build 42.21: A First-Week Survival Guide"
version: 1.0.0
status: approved
confidence: Medium
category: Players
topic: "Guides"
build: B42
document_type: tutorial
created: 2026-07-31
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, players-skills-xp, players-traits-occupations, players-medical-moodles, players-map-locations, meta-style-guide]
tags: [players, beginner, tutorial, first-week, apocalypse-preset, character-creation, spawn-towns, moodles, skill-books, build-42]
game_versions_verified: ["42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | players-beginner-guide-b42 |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Players |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 42.20, 42.21 |

# Executive Summary

This document is the onboarding path for a player installing Project Zomboid for the first time on Build 42 stable (42.21 since 2026-09-28 [19]; 42.20 before that). Where `players-foundation` maps the whole game and the deeper Players-track documents cover single systems exhaustively, this document does one narrower job: it puts the actual sequence of decisions a brand-new survivor faces — the tutorial, which game mode to start, which occupation and town to pick, and what to prioritise in the first in-game hours and days — into the order a new player meets them, and says what matters and what can wait.

The headline finding is that Build 42 gives a new player more up-front choice than earlier builds did. The Indie Stone rebuilt the game-mode menu during the unstable cycle into four playstyles with one explicit purpose each: Apocalypse as the "Lore Canon" reference experience, Outbreak for faster, less grind-heavy progression, Extinction for veterans only, and Rising as the mode the developers describe in the game files themselves as designed for newer players [2] [3] [5]. Layered under all of them is Custom Sandbox, where every numeric setting from that menu can be hand-tuned [5] [6]. This document treats that mode choice, plus occupation, trait and town selection, as the real "first decision" of a run, ahead of anything that happens in-world.

Document-level confidence is **Medium**. The game-mode overhaul and its intent are primary-sourced to an Indie Stone Thursdoid and its accompanying patch notes (High), and the current game-mode roster is corroborated by a pzwiki revision fetched the day after 42.20 shipped. But several of the beginner-mechanics facts this document leans on — the Survival Guide's early-priority advice, barricade behaviour, and the zombification percentages — are cited from wiki pages stamped against 41.78.19–42.13.1 and not independently re-verified against 42.20, which is the same caveat the sibling Players-track documents carry. Since the original draft, the 42.20 hotfixes and the 42.21 update changed a few first-week details (utility-failure food storage, water purification, farming paths); those are folded in and cited to the official notes.

# Key Takeaways

- **Play the in-game tutorial first.** It is a short, self-contained scenario with no settings to choose, built specifically to teach movement, looting, combat and the moodle rack before a real run begins *(cited)*
- **Apocalypse is the default, "canon" mode** — tuned for realism (accurate loot rates, no zombie respawning) rather than for being gentle. Rising is the mode the game itself is documented as aiming at newer players; Extinction is explicitly flagged as unsuitable for a first run *(cited)*
- **The four canon spawn towns are Muldraugh, West Point, Riverside and Rosewood.** Of those, community assessment rates Riverside the easiest and West Point the hardest; Rosewood's B42 zombie redistribution means its old "safe starter town" reputation no longer holds *(cited, wiki-sourced difficulty ratings)*
- **A handful of occupations cost zero creation points while still granting solid starting skills** — Doctor, Farmer, Firefighter, Lumberjack, Nurse and Rancher among them — making them efficient beginner picks without needing a deep trait study first *(cited)*
- **Water and electricity fail on their own random schedule, within the first month on most presets**, and neither is announced by name in advance in the same way — treating a run as if utilities are permanent is a first-week planning mistake *(cited)*
- **A zombie bite is a death sentence; a scratch or laceration is not.** The zombification odds most beginners need to know are stark: scratch 7%, laceration 25%, bite 100% on default settings, and no first-aid skill or item changes those odds *(cited)*
- **Firearms are a beginner trap, not a beginner tool.** They are loud enough to redirect every nearby zombie toward the shooter and are wildly inaccurate below a trained Aiming level, which is why melee is the documented default early-game weapon category *(cited)*
- **Skill books are cheap insurance against wasted XP** — reading the right volume before grinding a skill multiplies the XP earned in that level band, and is worth doing before any serious levelling push *(cited)*

# Purpose

This document exists to answer the question a completely new player asks in the first five minutes: "I have Project Zomboid 42.21 open, what do I actually do, and in what order?" It is deliberately sequencing-first rather than mechanics-first — every deeper system it touches (skills and XP, traits and occupations, moodles and health, the map) has its own Players-track document, and this one exists to tell a beginner which of those systems to care about *this week*, and to point at the deeper document when more detail is warranted.

# Scope

Covered: the in-game tutorial; the Build 42 game-mode menu (Apocalypse, Outbreak, Extinction, Rising, Custom Sandbox) and what each actually changes; beginner-level occupation and trait guidance (which occupations are cheap and solid, deferring full rosters and point tables); beginner-level spawn-town choice among the four canon towns (deferring full town profiles); the first-day and first-week priority order — securing a starting building, water, food, and a weapon; reading moodles at a "what to watch for" level; the beginner value of skill books; and the single biggest causes of new-player death.

Not covered, and covered instead by sibling documents: the full skill and XP mathematics (`players-skills-xp`), the complete occupation and trait rosters and point economy (`players-traits-occupations`), full moodle and injury mechanics (`players-medical-moodles`), and full town profiles and the wider map (`players-map-locations`). This document is written for Build 42.20 and 42.21 only; it does not cover Build 41.78 play, and it does not cover multiplayer server administration (Admins track) or modding.

# Definitions

- **Game mode (playstyle)** — the top-level scenario chosen before spawn location and character creation, which pre-fills the entire Custom Sandbox settings sheet with a themed set of defaults [5] [6].
- **Custom Sandbox** — the fully manual settings mode, and the underlying settings sheet every other game mode is a preset for [6].
- **Canon starting town** — one of the four towns (Muldraugh, West Point, Riverside, Rosewood) that support occupation-specific spawn points; see `players-map-locations` for full profiles [4].
- **Zero-point occupation** — community shorthand (used here descriptively) for an occupation whose point cost is 0, meaning it neither spends nor grants creation points while still providing starting skill levels; see `players-traits-occupations` for the full cost table.
- **Zombification** — infection with the Knox Infection following a zombie-inflicted wound; distinct from ordinary bacterial wound infection. See `players-medical-moodles` for the full mechanic.
- **Skill book volume** — a readable item that multiplies XP gain for one skill across a specific two-level band; see `players-skills-xp` for the full multiplier table.

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|-------------------|-------|
| B41 (legacy41) | No | — | Out of scope by design — see B41 vs B42 Delta below |
| B42 (stable) | Yes | 42.20, 42.21 (patch notes) | Facts target the 42.20 stable release [1]; current stable is 42.21 since 2026-09-28 [19] |

Re-baseline 2026-10-07: this document was re-checked against the official 42.20.1, 42.20.3, 42.20.4, 42.21 unstable and 42.21 stable posts and the abridged TIS forum 42.21 changelist [15] [16] [17] [18] [19] [20]. Statements those notes do not touch (game modes, tutorial, occupation costs, town ratings, wiki-sourced mechanics) are carried forward from 42.20 and the cited pzwiki revisions with no contradicting change found; they were not re-tested in-game. This document only makes claims about Build 42.20 and 42.21. Where a cited pzwiki page's own version banner predates 42.20 (several do — see Risks & Caveats), that is flagged inline and the fact is treated as "documented pre-42.20, not independently re-verified," matching the convention used across this KB's Players-track documents.

# Reference

## Step zero: the tutorial

Project Zomboid ships a short, fenced-off tutorial scenario with no settings to configure, aimed at teaching a completely new player the interface before a real run starts: camera and zoom, the health panel, the skills panel, movement, looting, moodles, equipping items and world interaction, plus melee attacking [5]. The tutorial also demonstrates one specific danger deliberately: it teaches the player to shout to draw zombies, and the scenario is built so that using the mechanic without understanding it leads to being overrun and the tutorial ending in death, inside a fenced map with a deliberately limited food supply so that outcome is not avoidable indefinitely [5]. A pzwiki-hosted beginner's guide independently recommends completing the tutorial before starting any real game mode [7].

## Choosing a game mode

Build 42's mode-select screen (checked in the 42.20 sources; 42.21 notes mention no change) offers five options: Apocalypse, Outbreak, Extinction, Rising, and Custom Sandbox, each pre-loading a themed settings sheet that can still be opened and hand-tuned before the run starts [5] [6]. The Indie Stone rebuilt this menu partway through the Build 42 unstable cycle, in the same release that reworked Apocalypse into the "Lore Canon" mode and introduced the other three as fresh replacements for the older mode line-up, stating plainly that "it has come time to refresh the Game Modes" for a build that had added enough new systems (animals, crafting, muscle strain) to need new defaults [2] [3].

| Mode | Stated intent | What changes for the player |
|------|----------------|------------------------------|
| **Apocalypse** | "The canon Zomboid experience. Take your time, be careful, and watch your back." — in-game description [5] | Tuned toward realism rather than convenience: loot tables, animal growth, crop seasons and vehicle condition are aimed at an authentic 1993-Kentucky feel, including more firearms in the world; zombies do not respawn and no longer generate "population loot" bonuses; weapon jamming is on; fences take more damage from concentrated attacks; and muscle strain and clothing discomfort are deliberately reduced from their raw values [2] [5] |
| **Outbreak** | "An accelerated experience for those who enjoy less grindy life. Just as lethal." — in-game description [5] | Non-combat skill progression, refrigerator effectiveness, animal and crop timelines and loot density are all tuned for a shorter, less grind-heavy playthrough — danger level is explicitly stated as unchanged from Apocalypse [2] [5] |
| **Extinction** | "A brutal and unforgiving world, where everything wants you dead NOW. Not recommended for newer players." — in-game description [5] | The first official mode to include sprinting zombies, paired with scarcer supplies; The Indie Stone's own framing singles this mode out as unsuitable for a first playthrough [2] [5] |
| **Rising** | "A cozier, less stressful environment for those who dream of building the perfect survivor's homestead." — in-game description [5] | The pzwiki mode description states this preset is designed for newer players and for players who prefer building, farming and exploration over combat, with more abundant building materials and a gentler zombie presence than the other three modes [2] [5] |
| **Custom Sandbox** | "Choose your own zombie apocalypse." — in-game description [5] | Every value behind every mode above — zombie count, distribution, utility-shutoff windows, loot multipliers and more — is exposed for direct editing [5] [6] |

One concrete, beginner-relevant number sits inside these presets: on Apocalypse's default settings, both the water and electricity supply shut off at a random point within the first 30 days of the run, a window shared with the Survival-era legacy preset this menu replaced [5] [6]. Nothing in the game announces the exact day in advance under either utility [7].

## Character creation: occupation and traits at a beginner level

Character creation still runs on the shared points system covered in `players-foundation` and detailed fully in `players-traits-occupations`: an occupation, a set of positive traits (which cost points) and negative traits (which grant points), with the build only permitted once the total is zero or higher [10]. For a first character, the fastest useful shortcut is the occupation list's zero-point rows: on the pinned Build 42 occupation roster, Doctor (First Aid 6), Farmer (Agriculture 4, Animal Care 1, Strength 1), Firefighter (Axe 1, Fitness 1, Running 1, Strength 1), Lumberjack (Axe 2, Maintenance 1, Strength 1), Nurse (First Aid 3, Fitness 1, Lightfooted 1) and Rancher (Animal Care 4, Butchering 3, Fitness 1) all cost exactly 0 points while still granting several free skill levels [10]. Because any skill started above level 0 earns a permanent XP-rate boost (mechanic detailed in `players-skills-xp`), a zero-cost occupation with a decent starting skill is strictly better value for a first run than starting from Custom Occupation's +8 free points and buying the same levels back piecemeal [10].

Beyond the occupation, this document deliberately does not walk through the trait list — `players-traits-occupations` carries the full B42 cost table, the point-economy history, and which traits changed price across the unstable cycle. The one beginner-relevant judgement call is budget discipline: it is easy to spend points on traits that sound protective and end up with an expensive, fragile build; a new player is better served by a small number of cheap, low-drama negative traits than by chasing the cheapest-looking combination on a wiki table without reading what each one actually does in play.

## Choosing a spawn town

On Build 42, occupation-specific spawn points exist only in four canon towns: Muldraugh, West Point, Riverside and Rosewood [4]. Anywhere else on the map — including the westward Build 42 additions — is reachable only through Custom Sandbox's town-selection option, and only with a generic, non-occupational spawn point [4]. The Spawn Point Selection preview videos were refreshed in 42.21 to match the map overhaul [18] [20]. `players-map-locations` carries full profiles of all of them; the beginner-relevant summary is the wiki's relative difficulty assessment for the four canon towns: Riverside is rated easy-to-medium and is the community's standing first-timer recommendation, with roughly two-thirds of its zombie population concentrated in its riverfront business district and a wealthy gated community, leaving quieter suburbs to learn the game in [11]. West Point, by contrast, is rated the hardest of the four, with heavy zombie presence in both its suburbs and its downtown — offset by the best firearm availability of the canon towns, which matters little to a beginner who should not be relying on guns yet [13]. Rosewood is the smallest canon town and was once the other commonly recommended beginner spawn, but the pinned Build 42 revision of its wiki page records that its zombies were redistributed to concentrate around its Main Street points of interest, and the page's own editors now rate it medium rather than the easy beginner-safe town it was on Build 41 [12].

## Securing a starting base

The Survival Guide hosted on pzwiki — a community-maintained but wiki-fact-classed beginner walkthrough — frames the first move after spawning as staying inside the starting building rather than immediately exploring outward, because it is very likely to be search-clear and is the safest structure available in the whole run [7]. Its documented immediate priorities are: cover every window that lacks curtains, using a sheet if necessary, so the character cannot be seen from outside; move quietly and avoid running or shouting, since noise and light both attract zombies; and loot the starting building itself for a weapon (kitchen knives, rolling pins, or anything sturdier found in a garage or closet) and a bag, since a school bag, duffel bag or even a plastic grocery bag meaningfully increases how much can be carried out of that first building [7].

Once a longer-term base is chosen, the game's actual reinforcement mechanic is the barricade: wooden planks, metal sheets or metal bars can be attached to a door or window, up to four per side, each one destroyed individually by an attacking zombie before the opening itself takes damage [8]. Barricades only slow zombies down; they do not stop a determined attack indefinitely, and because they make noise when struck, they double as an early-warning system that something is trying to get in [8]. Two or three planks per side still allow the player to see through the window, while three or four block the view entirely — a real trade-off between visibility and stealth that a new player should make deliberately rather than by default [8].

## Water, food and the first-week clock

Both utilities fail on an unannounced schedule: on Apocalypse's default settings, water and electricity both go down within the first 30 days, and unlike an in-fiction weather report, no specific warning names the exact day it happens [5] [6]. The Survival Guide's practical framing is to spend the early days consuming perishable food from refrigerators before it spoils, since once power fails, cooling stops and fresh food starts to rot — with any windfall of fresh food best moved into a working freezer immediately to buy extra time [7]. One 42.21 detail refines that: fridges and freezers now warm gradually on the day the power goes out rather than abruptly, and food carried in a bag inside a fridge or freezer is now refrigerated correctly [18] [20]. Non-perishable canned and dry goods are the fallback once the fridge empties, and the same source recommends treating carpentry materials for a rain-collection barrel, or a nearby natural water source, as the actual long-term water plan rather than depending on taps indefinitely [7]. Two 42.21 changes widen your options: 86 more fluid containers can now be used to purify water in the appropriate oven type, and washing machines now clean dirty rags, strips and bandages [18] [20]. Building a renewable food source — farming, fishing or trapping — by roughly the end of the first month is the same guide's recommended threshold for a survivable long game, well before stored food realistically runs out [7]. If you farm, note that since 42.21 player pathfinding avoids walking over crop plants where possible, though the notes state that stepping on crops never damaged them and the change is cosmetic; furrows trampled by zombies are now removed entirely [20].

## Arming yourself: melee first, firearms later

For a first character, the documented default approach is melee. A baseball bat, hammer or comparable blunt weapon found early in a residential building is treated as adequate starting equipment, while firearms are flagged as a trap rather than an upgrade: a single gunshot is loud enough to draw zombies from several blocks away, and without training in the Aiming skill — which most starting occupations do not grant — accuracy is poor enough that shots are likely to be wasted while still alerting every nearby zombie [7]. This is a direct extension of the muscle-strain and combat-pacing changes covered in `players-medical-moodles`; the beginner-level takeaway is simply to leave guns holstered until a specific reason (a trained Aiming occupation, or a defensible chokepoint) justifies the noise.

## Reading moodles: what a beginner actually needs to watch

The full moodle roster, its every effect and Build 42's added entries are `players-medical-moodles`'s job. At beginner level, the practical habit documented across both that sibling document and the Survival Guide is the same: moodles are the game's only warning system, appearing as icons in the top-right of the screen, and ignoring them is how avoidable deaths happen [7]. Two are worth specific early attention. Tiredness degrades combat and narrows awareness the longer it is ignored, and can only be fixed by sleep or caffeine — not by pushing through it [7]. Encumbrance (Heavy Load) slows movement and, at its worst, drains health directly, and the single most useful emergency response to being over-encumbered while spotted is to drop a secondary bag on the spot and retrieve it later once the area is clear [7].

## Skill books: cheap, high-value early reading

Skill books are single-use readables that multiply the XP a skill earns while the character's level sits inside that specific book's two-level band, and the multiplier scales up through five volumes per skill, covering levels 1–2 through 9–10 [14]. For a beginner the practical rule is simple and does not require memorising every multiplier: find and fully read the Volume I book for whatever skill is about to be levelled, before grinding it, because reading below or above the correct band either refuses the read or wastes it entirely [14]. `players-skills-xp` carries the full multiplier table and the per-build book coverage; this document's point is sequencing — check the bookshelf before the workbench.

## The single biggest causes of new-player death

Two mechanical facts do most of the explanatory work for "how did I die." First, the zombification odds attached to a zombie-inflicted wound are stark and asymmetric: on default settings, a scratch carries a 7% chance of the fatal Knox Infection, a laceration 25%, and a bite 100% — and no first-aid skill, item or trait changes those odds once a wound has happened [9]. That makes the practical question after any zombie contact not "how do I treat this" but "what kind of wound was it," since a bite is fundamentally a different situation from a scratch. Second, the same causes of death that predate any patch remain true on 42.20: starvation and dehydration from ignoring the Hungry and Thirsty moodles, exhaustion-driven combat failure from ignoring Tired, and horde mismanagement — getting spotted, panicking, and running into a second group of zombies while fleeing the first — are all documented failure modes in the community guide cited throughout this section, and none of them require a single mistake so much as an ignored warning repeated over hours [7] [9].

# B41 vs B42 Delta

Not applicable — single-build document. This guide is deliberately scoped to Build 42 (42.20 and 42.21) only: Build 41.78 is now the `legacy41` maintenance line (its latest primary-attested hotfix is 41.78.21, 2026-08-26 [17]) rather than the build a brand-new player installing the game today will land on, and `players-foundation` already documents how to reach `legacy41` for a player who specifically wants Build 41. Writing a beginner's first-week sequence that tried to serve both builds at once would blur exactly the kind of build-specific detail (the game-mode menu, the occupation roster, the muscle-strain caution around firearms and melee) that this document exists to get right for the build a newcomer is actually running.

# Practical Guidance

- **Play the tutorial before your first real run**, even if you think you already know the interface — it is short, and it is the one place the game safely shows you what a mistake looks like.
- **Pick your game mode deliberately, not by habit.** Apocalypse is the reference experience most guides (including this one) assume, but it is not designed to be gentle. If your goal on a first run is to learn the systems without constant combat pressure, Rising is the mode the game itself documents as built for that.
- **Do not start on Extinction.** The Indie Stone's own in-game description tells you not to, and there is no reason to argue with the people who tuned it.
- **Take a zero-point occupation with a skill you intend to use.** Doctor, Farmer, Firefighter, Lumberjack, Nurse or Rancher hand you real starting levels for nothing, which is strictly better than spending your first run's points learning what traits do.
- **Spawn in Riverside if you have no preference.** It is the community's standing easy recommendation among the four canon towns. Save West Point for a run where you specifically want early pressure, and do not assume Rosewood is still the soft option it was on Build 41.
- **Stay inside your starting building at first.** Cover the windows, find a bag and a blunt weapon, and only then think about what is outside.
- **Treat the utility shutoff as a countdown from day one**, not an emergency to react to later — start planning a rain barrel or a water-adjacent base well before the taps actually run dry. Since 42.21 your fridge buys you a little more grace on the day the power fails, because it warms gradually [20].
- **Stay on the Stable branch for your first save.** The developers recommend a manual backup before testing a new update on Unstable with an existing save [18].
- **Leave the gun in the bag.** Melee is quieter, ammo-free, and does not require a skill most starting occupations do not give you.
- **Read the Volume I book before you grind anything.** It is free efficiency that costs you nothing but the in-game time to read it.
- **After any zombie wound, the first question is "what kind," not "how bad."** A scratch and a bite are not the same emergency, and no amount of first aid changes which one you have.

# Common Pitfalls & Troubleshooting

- **"I ran outside immediately and got swarmed."** The documented first move is the opposite: secure the building you're already in before exploring it further or leaving it [7].
- **"I fired my gun once and now there are twenty zombies at my door."** Working as documented — firearms are loud enough to redirect a wide area's zombie population toward the sound, which is exactly why melee is the recommended default [7].
- **"I picked Rosewood because a guide said it was the easy town."** That guide was probably written for Build 41. The pinned Build 42 wiki revision for Rosewood documents a zombie redistribution that the page's own editors now rate as harder than its old reputation [12].
- **"My water/power just stopped and I had no warning."** Also working as documented: the utility shutoff window is randomised within roughly the first month and is not announced by an exact date in advance [5] [7].
- **"I got scratched and panicked like it was a bite."** A scratch carries a 7% zombification chance on default settings, nowhere near the 100% of an actual bite — treat the two very differently [9].
- **"I started Extinction as my first game and died in ten minutes."** The mode's own description tells new players not to start there; if this happened, the mode did exactly what it says on the tin [5].
- **"The zombies I saw a minute ago are gone after I walked away and came back."** That was a chunk re-entry bug in singleplayer and multiplayer, fixed in 42.21; the developers say a few instances remain [19] [20].
- **"The game slows down or crashes after hours of play."** 42.20.1 and 42.20.3 fixed memory leaks that did this; if out-of-memory errors persist on a new save, the developers ask for a bug report with logs and a debug profiler video [15] [16].
- **"A huge tree is hiding my house or blocking my view while driving."** 42.21 changed XXL tree cutaway so they hide overhung houses and furniture less and cut away better for drivers; the developers call it work in progress [19] [20].
- **"I ignored the Tired moodle and lost a fight I should have won."** Fatigue degrades combat and narrows your effective vision the longer it is ignored, and only sleep or caffeine actually clears it — pushing through it is the mistake, not bad luck [7].

# Community Notes & Unverified Claims

## Claim 1 — Rising is simply an "easy mode" with the numbers turned down

- **Claim:** Community discussion frequently shorthands Rising as the easy-mode option, implying its zombie population and danger level are a straightforward across-the-board reduction from Apocalypse.
- **Why unverified:** The primary Thursdoid describes Rising as cozier, more building-focused and lower-combat, and the in-game description on the mode itself is documented as targeting newer players [2] [5], but this document did not extract Rising's full Custom Sandbox variable sheet, so the exact scale of the zombie-count and difficulty reduction relative to Apocalypse is not independently confirmed here.
- **Confidence:** Medium. The directional claim (Rising is gentler and aimed at newcomers) is primary-sourced; the specific magnitude a player should expect is not.

## Claim 2 — New players should avoid firearms entirely for the whole early game

- **Claim:** A common blanket rule repeated in community guides and forum advice is that a new player should not touch a firearm at all until deep into a run.
- **Why unverified:** The documented reasons to be cautious — noise radius and poor accuracy without Aiming training — are real and cited [7], but nothing in the cited sources states an absolute prohibition; an occupation that starts with Aiming levels (Police Officer, Veteran) changes the calculus, and the "never" framing is a community simplification of a more conditional caution.
- **Confidence:** Medium. The underlying caution is well supported; the absolute version of the rule is not stated by any source used here.

## Claim 3 — Rosewood is still the best town for a brand-new player

- **Claim:** Older community guides and some current discussion still name Rosewood as the safest canon town to learn the game in, a reputation carried over from Build 41.
- **Why unverified:** The pinned Build 42 wiki revision for Rosewood explicitly documents a zombie-distribution change concentrating population around its Main Street area and states the town is now rated medium rather than easy [12]; the persistence of the older claim appears to be B41-era habit rather than a currently supported assessment.
- **Confidence:** Medium. The contradicting fact is wiki-sourced and dated after the change it describes, but "best beginner town" is ultimately a judgement call this document cannot fully settle without further first-hand 42.20 testing.

# Risks & Caveats

- **Several cited pzwiki pages predate 42.20.** The Survival Guide and Barricade pages are both stamped against version 41.78.19, and the Custom Sandbox page carries the same stamp; none have been independently re-verified against 42.20 stable, though nothing in their content contradicts anything confirmed elsewhere in this KB for 42.20 [6] [7] [8].
- **The Game modes wiki page mixes fresh and stale content.** Its edit history shows a revision made the day after 42.20 shipped, and its playstyle descriptions (Apocalypse, Outbreak, Extinction, Rising) read as current, but its page-version banner still names Build 42.15.0 and its listed Challenge names do not match the two challenges named in the 42.20 stable release notes elsewhere in this KB — a sign that not every section of that page was updated at the same time [1] [5]. This document only draws on the playstyle section, cross-checked against the primary Thursdoid, not the challenge list.
- **The exact Rising, Outbreak and Extinction Custom Sandbox variable sheets were not fully extracted for this document** — only Apocalypse's was read in full detail; the comparative statements above rest on the modes' documented intent and stated highlights, not a line-by-line settings diff.
- **Zombification odds are wiki-sourced, not patch-note-sourced**, a caveat this document inherits directly from `players-medical-moodles`: no Indie Stone announcement stating 7%/25%/100% was located during this document's research, only the pzwiki Knox Infection page [9].
- **Patch recency.** Hotfixes 42.20.1 to 42.20.4 and the 42.21 update have landed since the original draft [15] [16] [17] [19]; none of their notes mention the utility-shutoff window, occupation costs or game-mode values cited here, but those were not re-tested in-game and later patches could move them.
- **Abridged forum changelist.** The TIS forum 42.21 list [20] was captured in abridged form; an absent item is not necessarily absent from the full list.
- **Steam announcement mirrors.** Primary citations use Steam announcement URLs, which bot-block automated link checkers by design; they were retrieved and verified through the Steam news API for app 108600.

# Verification Steps

1. **Confirm the mode menu:** on 42.20 or 42.21, open a new game and record the exact five options offered, comparing them against the Apocalypse/Outbreak/Extinction/Rising/Custom Sandbox list above.
2. **Confirm the tutorial's scope:** play the tutorial once and check it covers zoom, health, skills, movement, looting, moodles, equipping, world interaction and attacking, as listed [5].
3. **Confirm the zero-point occupations:** at character creation, check that Doctor, Farmer, Firefighter, Lumberjack, Nurse and Rancher each show a Points cost of 0.
4. **Confirm the canon-town spawn list:** verify that only Muldraugh, West Point, Riverside and Rosewood offer occupation-specific spawn points outside Custom Sandbox.
5. **Confirm the utility-shutoff window:** on an Apocalypse-preset game, open Custom Sandbox before starting and check the Water Shutoff and Electricity Shutoff values against the "0–30 days" figure cited here.
6. **Confirm barricade limits:** in-game, attempt to add more than four planks to one side of a window and confirm the game refuses the fifth.
7. **Confirm the zombification odds:** cross-check against `players-medical-moodles`'s own verification steps, which propose a large-sample in-game test.
8. **Confirm the 42.21 changes you rely on:** after a power cut, watch a fridge warm over the day, and check that a bagged food item inside it stays cold [18] [20].
9. **Re-verify the wiki sources:** open each cited pzwiki revision URL (each pins an `oldid`) and diff against the live page for post-42.20 corrections.

# Open Questions

- What is Rising's (and Outbreak's and Extinction's) full Custom Sandbox variable sheet on 42.20, and how does it compare numerically to Apocalypse's? This document only extracted Apocalypse's in full.
- Are the older "Outdated playstyles" presets (Survivor, Builder, Survival, Initial Infection, One Week Later, Six Months Later) still selectable as Saved Presets inside Custom Sandbox on 42.20, and does the wiki's claim that they were removed "as of Build 41" reflect an actual game-version cutoff or a page-authoring inconsistency?
- Does the tutorial scenario differ in any way on 42.20 relative to the version described by the cited wiki revision?
- Is there a primary Indie Stone source for the 7%/25%/100% zombification odds, or are they wiki-only? (Inherited open question from `players-medical-moodles`.)
- Has The Indie Stone published any beginner-specific guidance (a "new player" blog post or Thursdoid) that would upgrade this document's game-mode and town recommendations from wiki-corroborated to fully primary-sourced?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; retrieved via the Steam news API, ISteamNews app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [2] **The Indie Stone** — *SOME NEW THINGS* (Thursdoid, Steam announcement, 2026-03-09; the Game Mode Refresh announcing Apocalypse's Lore Canon rebalance and the new Outbreak, Extinction and Rising modes). https://steamcommunity.com/games/108600/announcements/detail/1826362059930346. Accessed 2026-07-31.
- [3] **The Indie Stone** — *Build 42.15.0 Unstable Released* (Steam announcement, 2026-03-09; the patch notes accompanying the Game Mode Refresh). https://steamcommunity.com/games/108600/announcements/detail/1826362059930323. Accessed 2026-07-31.
- [4] **The Indie Stone** — *Location, Location* (Thursdoid, Steam announcement, 2026-04-17, covering 42.17 Unstable; states the four canon starting towns and the Sandbox-only status of other towns). https://steamcommunity.com/games/108600/announcements/detail/1830163047261202. Accessed 2026-07-31.

- [15] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [16] **The Indie Stone** — *42.20.3 STABLE Hotfix Released* (Steam announcement, 2026-08-17). https://steamcommunity.com/games/108600/announcements/detail/1840944183785895. Accessed 2026-10-07.
- [17] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [18] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [19] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [20] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post, 2026-09-23; abridged "selected" capture retrieved 2026-10-07). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cited by URL and revision id for facts only; all prose in this document is original.

- [5] **PZwiki** — *Game modes* (revision 1443619, edited 2026-07-29; page-version banner still names 42.15.0). https://pzwiki.net/w/index.php?title=Game_modes&oldid=1443619. Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Custom Sandbox* (revision 1442995; page versioned against 41.78.19, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Custom_Sandbox&oldid=1442995. Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *Survival Guide* (revision 1393953; page versioned against 41.78.19, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Survival_Guide&oldid=1393953. Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *Barricade* (revision 1385633; page versioned against 41.78.19, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Barricade&oldid=1385633. Accessed 2026-07-31. Fact-only source.
- [9] **PZwiki** — *Knox Infection* (revision 1438437; page versioned against 42.13.1, not re-verified on 42.20). https://pzwiki.net/w/index.php?title=Knox_Infection&oldid=1438437. Accessed 2026-07-31. Fact-only source.
- [10] **PZwiki** — *Occupation* (revision 1391359; page versioned against 42.18.0). https://pzwiki.net/w/index.php?title=Occupation&oldid=1391359. Accessed 2026-07-31. Fact-only source.
- [11] **PZwiki** — *Riverside* (revision 1443703; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Riverside&oldid=1443703. Accessed 2026-07-31. Fact-only source.
- [12] **PZwiki** — *Rosewood* (revision 1442741; page versioned against 42.19.0). https://pzwiki.net/w/index.php?title=Rosewood&oldid=1442741. Accessed 2026-07-31. Fact-only source.
- [13] **PZwiki** — *West Point* (revision 1438485; page versioned against 42.13.1). https://pzwiki.net/w/index.php?title=West_Point&oldid=1438485. Accessed 2026-07-31. Fact-only source.
- [14] **PZwiki** — *Skill book* (revision 1317189; page versioned against 42.13.2). https://pzwiki.net/w/index.php?title=Skill_book&oldid=1317189. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating** — none cited.

**Community & Creator** — none cited. The community claims quarantined above are described as circulating positions, not sourced to individual posts.

**Further Reading**

# Further Reading

- The Steam news API endpoint used to retrieve and verify every primary citation above: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0
- The Indie Stone's official blog, canonical home of the Thursdoids mirrored as Steam announcements: https://projectzomboid.com/blog/ (bot-blocks automated checkers; verify in-browser).
- pzwiki's in-game "Survival Guide" companion page, useful for the exhaustive item- and location-level detail this document deliberately summarises: https://pzwiki.net/wiki/Survival_Guide

# Related Documents

- `players-foundation` — the Players-track overview this document assumes; covers the core loop, moodle system and character creation at map level.
- `players-skills-xp` — the full XP mathematics and skill-book multiplier tables this document only summarises.
- `players-traits-occupations` — the complete occupation and trait rosters and point-cost tables behind this document's zero-point occupation recommendation.
- `players-medical-moodles` — the full moodle roster, injury types and zombification mechanics behind this document's "what to watch for" summary.
- `players-map-locations` — full profiles of every canon and Build 42 town behind this document's spawn-choice recommendation.
- `meta-style-guide` — the evidence, quarantine and build-tagging rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baseline to 42.21: reviewed against the 42.20.1, 42.20.3, 42.20.4 (incl. 41.78.21), 42.21 unstable and 42.21 stable Steam posts and the abridged TIS forum 42.21 changelist (42.20.2 reviewed; modding/debug-only). Title and scope now 42.21; added fridge warming, bagged-food refrigeration, oven water purification, washing machines, farming path change, chunk re-entry fix, memory-leak fixes, XXL trees, save-backup note; legacy41 described as maintained (41.78.21). Unchanged statements carried forward, not re-tested in-game. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
