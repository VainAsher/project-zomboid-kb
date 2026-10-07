---
id: modders-item-scripts-distributions
title: "Item Scripts, Recipes and Loot Distributions: Defining Content Through Script Files"
version: 0.2.0
status: in-review
confidence: Medium
category: Modders
topic: "Item scripts & distributions"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-05
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-lua-api-surface, modders-events-callbacks, modders-modinfo-modid-conventions, modders-first-mod-tutorial-b42, modders-porting-b41-to-b42, players-crafting-chains, admins-workshop-mod-wiring, meta-style-guide]
tags: [modding, scripts, zedscripts, item-script, craftrecipe, recipe, evolvedrecipe, fixing, item-tags, distributions, proceduraldistributions, loot, b42]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-item-scripts-distributions |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-05 |
| Game versions verified | 41.78.16 (Umbrella stubs), 42.20 (Umbrella 42.20.0 stubs); ScriptsDocs pages are stamped 42.21.0 |

# Executive Summary

Most content mods in Project Zomboid are defined twice: once in plain-text
script files under `media/scripts/` (items, recipes, fixing and evolved
recipes), and once in Lua tables that decide where those items spawn as loot.
This document covers both layers: the block syntax shared by all script files,
the item block and its `ItemType` classes, the Build 42 `craftRecipe` format
with its `inputs` and `outputs` children against the Build 41 `Recipe`
block, item tags, the `evolvedrecipe` and `fixing` blocks, and the three
distribution files that drive world loot [7] [8] [9] [18].

The headline change for porters: B42 replaced the single-line B41 recipe
description with a structured `craftRecipe` block whose ingredients live in a
child `inputs` block and whose results live in `outputs` [9] [10]. B42 also
turned item tags from a fixed enum into a registry that mods can extend [3]
[22], and renamed the item-class parameter from `Type` to `ItemType` [8].
Distribution tables kept their file names and overall shape, but the B42 pass
added and removed room and container entries [4].

Script syntax is not covered by Umbrella, which is Lua-only. The API-existence
gate therefore only validates the Lua symbols named in code spans here
(distribution events, `ItemTag` registration); the script grammar is sourced
from the generated ScriptsDocs reference [7] and the game's own patch notes.
Confidence is Medium: the script reference is primary but generated against
game version 42.21.0, one release newer than the 42.20.0 stubs this document
was checked against, and no in-game test was run [7] [2].

# Key Takeaways

- Script files are plain-text data, not code: a `module` block wrapping
  blocks such as `item`, `craftRecipe`, `evolvedrecipe` and `fixing`. *(cited)* *(both)*
- The `item` block's behaviour is selected by `ItemType`; the old `Type`
  parameter is marked deprecated, replaced by `ItemType` as of 42.13.0. *(cited)* *(B42)*
- B42 recipes are `craftRecipe` blocks with required `inputs` and usually
  `outputs` children; the B41 `Recipe` block is listed on the wiki as the
  Build 41 format and is not documented in ScriptsDocs. *(cited)* *(both)*
- B42 item tags are namespaced (`base:egg`) and a mod can register its own
  through Lua at load time. *(cited)* *(B42)*
- Loot lives in Lua: `ProceduralDistributions.list` holds weighted item
  lists, and room/container tables reference them by name. *(cited)* *(both)*
- Three distribution events exist on both builds: `Events.OnPreDistributionMerge`,
  `Events.OnDistributionMerge` and `Events.OnPostDistributionMerge`. *(cited)* *(both)*
- The two builds' Umbrella stubs describe the Pre event differently; which
  event is safest for edits is not settled by a primary source. *(cited)* *(both)*
- ScriptsDocs is stamped 42.21.0, newer than the 42.20.0 stubs; treat any
  parameter detail as 42.21-era until re-checked. *(cited)* *(B42)*

# Purpose

This document answers: "I want to add an item, a way to make it, and a way to
find it in the world: which files, which block syntax, and what changed
between Build 41 and Build 42?" It goes deeper than `modders-foundation`,
which only introduces script files, module blocks and the `craftRecipe`
headline, and it is the modding-side companion to `players-crafting-chains`,
which holds the player-facing facts about the crafting overhaul.

# Scope

Covered: script file layout, module and imports blocks, the item block and
common parameters, `craftRecipe` with `inputs`/`outputs`/`itemMapper`, the
B41 `Recipe` block at the level the sources support, `evolvedrecipe`,
`fixing`, item tags, translation keys for scripts, and the Lua distribution
tables and events that place items in the world.

Not covered: vehicle, model, sound and `entity`/`fluid` script blocks (own
documents), full per-parameter tables (use ScriptsDocs, linked below), Lua
APIs beyond the named distribution/tag symbols (`modders-lua-api-surface`),
event semantics in general (`modders-events-callbacks`), and mod folder
layout (`modders-foundation`, `modders-modinfo-modid-conventions`). The
B41-format `Recipe` block syntax is not reproduced because no primary source
documenting it was reachable (see Open Questions).

# Definitions

- **Script file** — a `.txt` file under `media/scripts/` in a mod or the
  game; a custom block format, not a programming language [27].
- **Module** — the namespace block wrapping script entries; `Base` is the
  game's own, and full IDs take the form `module.id` [13].
- **Full type** — `module.id`, for example `Base.Nails` [8] [13].
- **Soft override** — redefining an existing block merges or replaces it
  depending on block type instead of failing; ScriptsDocs marks each block
  as supporting it or not [7] [27].
- **ItemType** — the item-block parameter selecting the item class
  (`base:food`, `base:weapon`, ...) and thus which parameters apply [8].
- **Item tag** — a namespaced string label on an item, queried from Lua,
  Java and recipes [8] [15].
- **Procedural distribution** — a named loot list (rolls plus weighted
  items) referenced by room and container tables [16] [18].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes, partially | Umbrella 41.78.16 stubs [19] [21] [24]; wiki block list [27] | `Recipe` block and Lua distribution tables; ScriptsDocs does not cover B41 [7] |
| B42 (stable) | Yes | Umbrella 42.20.0 stubs [18] [20] [22] [23]; ScriptsDocs stamped 42.21.0 [7] | Latest stable is now 42.21 (see below) |

Game 42.21 stable was released on 2026-09-28 [2] [6] and 41.78.21 legacy
hotfixes on 2026-08-26 [5] [6]. This document is verified against the 42.20.0
Umbrella stubs only. The ScriptsDocs site it relies on is itself generated from
42.21.0 data (its page title reads "PZ API Documentation 42.21.0") [7], so
script parameter details here are 42.21-era and have not been diffed against
42.20.0 game files. The B41 side rests on the 41.78.16 stub pin; the legacy
line has since moved to 41.78.21 [5].

# Reference

## Script file anatomy

Scripts are text files ending in `.txt` under `media/scripts/`, with no
mandated folder organisation; the wiki advises a subfolder named after the
mod to reduce clashes [27]. Entries are blocks delimited by braces, parameters
are `Key = Value,` pairs whose trailing comma is mandatory even on the last
line, and comments use `/* ... */` only [27]. The root of every script file
may only contain `module` blocks [13] (sandbox option scripts are the
documented exception) [27].

A `module` block is a namespace and carries a mandatory ID; `Base` is the
game's namespace. The module page lists as permitted children, among others,
`item`, `craftRecipe`, `evolvedrecipe`, `fixing`, `fluid`, `entity`, `model`,
`sound`, `vehicle` and `imports` [13]. The `Recipe` block is not in that
list [13], and ScriptsDocs has no page for it, while the wiki still lists it
as the Build 41 recipe block [27].

An `imports` block inside a module gives direct access to other modules'
entries without a prefix; ScriptsDocs notes that `Base` is already parsed and
suggests referencing IDs with their module instead [13]. The wiki adds that
unqualified references search the current module, then imports, then `Base`,
then all others, and that this is inconsistent between block types [27].
Writing a block whose ID already exists is a soft override for item and
`craftRecipe` blocks, while whole-file replacement happens when a mod uses
the same relative path as an existing script file [27].

## The item block

An `item` block lives in a module, takes a mandatory ID without spaces, and
may have child blocks including `component FluidContainer` and
`component Durability` [8]. Its `ItemType` is required and must be one of
`base:alarmclock`, `base:alarmclockclothing`, `base:animal`, `base:clothing`,
`base:container`, `base:drainable`, `base:food`, `base:key`, `base:literature`,
`base:map`, `base:moveable`, `base:normal`, `base:radio`, `base:weapon` or
`base:weaponpart`; parameters specific to one class (for example
`Calories` for food or `ClipSize` for weapons) are only loaded for that
class [8]. The older `Type` parameter is flagged deprecated since 42.13.0,
replaced by `ItemType` [8].

Representative general parameters documented for the block [8]:

| Parameter | Documented role |
|-----------|-----------------|
| `Weight` | Encumbrance, float, default 1.0 |
| `DisplayCategory` | Key suffix for the inventory category label (`IGUI_ItemCat_<value>`) |
| `Tags` | Semicolon-separated list of item tags |
| `EvolvedRecipe` | Which evolved recipes the item may be an ingredient in, as `name:quantity` pairs |
| `ConditionMax` | Durability pool, integer, default 10 |
| `DisplayName` | Deprecated since 42.13.0 in favour of a translation entry |

The item's visible name comes from a translation entry keyed by the item's
full type in the `ItemName` translation file, and ScriptsDocs warns that
without a translation entry the weight will not work in game [8].

## craftRecipe (B42)

A `craftRecipe` block sits in a module, has a mandatory ID that may contain
spaces, and requires an `inputs` child; `outputs`, `itemMapper` and
`overlayMapper` children are optional [9]. Defined inside an `entity` it
becomes the build recipe of that buildable instead of an item recipe [9].
`craftRecipe` supports soft overrides [9]. Documented parameters include [9]:

| Parameter | Documented role |
|-----------|-----------------|
| `tags` | Required list; must include at least one crafting-bench tag such as `AnySurfaceCraft` or `InHandCraft` |
| `time` | Crafting time, integer, default 50, unit not specified |
| `timedAction` | Timed action script for animation, sounds and calorie cost |
| `category` | Menu category, default `Miscellaneous`; label via an `IGUI_CraftingCategories_` key |
| `SkillRequired` | `Skill:level` pairs separated by semicolons |
| `xpAward` | `Skill:xp` pairs |
| `NeedToBeLearn` | Whether the recipe must be learned first |
| `AutoLearnAll` / `AutoLearnAny` | Skill thresholds that grant the recipe automatically |
| `MetaRecipe` | Links recipes so that knowing one grants the other, one direction only |
| `OnCreate`, `OnTest`, `OnFailed`, `OnUpdate`, `OnAddToMenu` | Lua callbacks named as global functions |
| `AllowBatchCraft` | Batch slider, default true |
| `CanWalk` | Whether the player may walk while crafting, default false |
| `Tooltip` | Key in the `Tooltip` translation file |

The recipe name is translated by an entry in the `Recipes` translation
file keyed by the recipe ID alone, without the module [9]. `OnCreate`
functions receive the craft data and the character, and `OnTest` receives
an item and the character and returns a boolean [9]. Custom crafting-bench
tags are created by adding a `component CraftBench` to an `entity` script [9].

The `inputs` block has no ID and no parameters of its own; it may be a child
of `craftRecipe` or of `component CraftRecipe` [10]. The documented example
lines show the grammar: an input line starts with `item`, a count, then
either a bracketed list of full types or a `tags [...]` selector, optionally
followed by `mode:keep` or `mode:destroy`, a `flags [...]` list and a
`mappers [...]` reference, and a fluid line of the form `fluid 1.0 [Petrol]`
also appears [9]. The `outputs` block has no ID or parameters; each line is
`item <quantity> <full type>` or `item <quantity> mapper:<mapperID>` [10]. An
`itemMapper` child block declares a table from input item to output item
with an optional `default` [9] [14].

The recipe page's own examples place the recipe in the `Base` module and
show crafts that keep a tool via `mode:keep` while consuming logs, and a
lantern refill using a mapper [9]. Recipe lists in the crafting UI are
filtered by the bench tags and learning state; the player-facing view of that
system is in `players-crafting-chains`.

## The B41 Recipe block

The wiki's block list describes `Recipe` as the block used to define recipes
in Build 41 [27]. The Build 41.78.16 Umbrella stub for the Java `Recipe`
class exposes the data model behind it: a name, category, result, sources,
required skills, time to make, a tooltip, flags such as hidden, learn
requirement and "can be done from floor", and Lua hooks for create, test,
can-perform and give-XP [24]. The B42.20.0 stubs still ship a `Recipe` class
[25]; whether 42.20 still parses `Recipe` blocks in scripts is not established
by any source cited here (see Open Questions).

## evolvedrecipe and fixing

An `evolvedrecipe` block, in a module, defines a dynamic recipe whose
ingredients are added across several steps, with stats from each ingredient
summed into the product; documented parameters include `BaseItem`,
`ResultItem`, `MaxItems`, `Name`, `Cookable`, `CanAddSpicesEmpty`,
`AddIngredientIfCooked`, `AddIngredientSound` and `MinimumWater` [11]. An
item opts in as an ingredient via its own `EvolvedRecipe` parameter [8] [11].
A `fixing` block, in a module, defines how an item can be repaired, with the
documented parameters `Require`, `Fixer`, `GlobalItem` and `ConditionModifier`;
its soft-override status is listed as unknown, and most parameters have no
description [12]. The Java classes behind both blocks exist in the B41 and
B42 stubs [19] [24] [25], which is consistent with both blocks surviving the
B42 crafting overhaul. ScriptsDocs lists the `evolvedrecipe` and `fixing`
parameters but states nothing about which builds they apply to [7] [11] [12].

## Item tags

On B42, an item's `Tags` value is a semicolon-separated list of namespaced
tags such as `base:egg` and `base:hasmetal`. The Java-side field names
(for example `ItemTag.AEROSOL`) map to those script names (`base:aerosol`) [8] [15].
A mod defines its own tag by registering it from Lua with
`ItemTag.register("yourmodid:yourtagname")` *(B42)* in `registries.lua` and then using the
registered ID in item scripts [8] [22] [28]. The 42.13.0 patch notes record
that `ItemTag` was refactored from an enum into a class with registry
support [3]. The B41 Umbrella index has no `ItemTag` class [19]. Recipe
inputs can select by `tags [...]` [9].

## Registries (42.13 and later)

The Build 42.13 modding migration guide, a first post by an Indie Stone
moderator on the official forum dated 2025-12-11, states that from 42.13 a
set of identifiers must be declared from Lua before scripts can use them [28].
The declaring file must be named exactly `registries.lua`, sit in the mod's
`media` folder, and is loaded before scripts and before all other Lua [28].
The guide lists eleven registries: CharacterTrait, CharacterProfession,
ItemTag, Brochure, Flier, ItemBodyLocation, ItemType, MoodleType,
WeaponCategory, Newspaper and AmmoType [28].

Each registry is declared with a `register` call taking a namespaced ID of the
form `namespace:name`, for example the guide's `ItemTag.register("testmod:bobbypin")`
*(B42)* [28]. Two registries take more arguments: Newspaper takes a list of
entry names, and AmmoType takes an item key built from an item name and an
item type [28]. The Umbrella 42.20.0 index confirms a `register` member on all
eleven registry classes, and an `ItemKey.new` constructor, so the call shapes
exist in the 42.20.0 Lua surface *(B42)* [22] [18]. The registry classes are
absent from the 41.78.16 index, apart from unrelated same-named `ItemType` and
`MoodleType` classes *(B41)* [19].

Registered IDs are then used verbatim in scripts. The guide's example
shows a `character_trait_definition` whose `CharacterTrait` parameter holds the
registered trait ID, a `character_profession_definition` whose
`CharacterProfession` parameter and `GrantedTraits` reference registered IDs,
an item whose `Tags` value is a registered tag, and a recipe input selecting a
vanilla tag written with its namespace (`tags[base:screwdriver]`) [28]. That
last form shows recipe tag selectors are namespaced like item tags, which
resolves the unnamespaced `tags [Saw]` ambiguity in the ScriptsDocs example [9].

The guide's script-side changes are: the item `DisplayName` parameter is
removed and the name is read only from the `Module.ItemId` translation key; `Type` is
renamed `ItemType` and requires an entry in the ItemType registry; and `Tags`
require the ItemTag registry [28]. Base-game scripts, it adds, are now
generated from Java code and read as before, so they are good examples [28].

Where sources differ: ScriptsDocs calls `DisplayName` and `Type` deprecated as
of 42.13.0 with a replacement, not removed [8]; the guide says removed and
renamed [28]. ScriptsDocs lists `base:`-prefixed `ItemType` values as a fixed
allowed list [8], whereas the guide says custom ones can be registered [28];
the two are not contradictory but the allowed list on that page does not show
mod-registered values. The guide's recipe example uses the spelling
`needTobeLearn`, while the 42.13.0 patch notes say that spelling was removed in
the builder in favour of `needToBeLearn`, and ScriptsDocs documents the latter [3] [9] [28].
The guide dates from the 42.13 era; this document verified against 42.20.0
stubs and 42.21-stamped ScriptsDocs, and no registry detail was changed or
re-tested at 42.20 [28] [7].

## Loot distribution files

World loot is data in three Lua files that Umbrella stubs under
`lua/server/Items/` [18] [19]: *Distributions.lua*, *ProceduralDistributions.lua*
and *SuburbsDistributions.lua*. The B42 stubs describe the shapes with typed
annotations [18]:

- `ProceduralDistributions.list` maps a list name to a table with `rolls`
  (integer) and `items`, an array alternating item name and weight, plus
  optional flags such as `junk`, `bags`, `isShop`, `isWorn`, `isRotten`,
  `maxMap`, `stashChance` and `onlyOne` [18] [16].
- A room's container entry is either a procedural distribution itself or a
  table with `procedural = true` and a `procList` of entries
  with `name`, `min`, `max` and `weightChance`, and optional `forceForItems`,
  `forceForRooms`, `forceForTiles` and `forceForZones` [18]. ScriptsDocs
  states `forceForZones` does nothing [17].
- Room tables may carry fields such as `isShop`, `outfit` fields, `vehicles`
  and `professionChance` [18].
- Vanilla `rolls` semantic: the roll count applies to each item entry
  individually rather than once per list [16].

The B41 stub of *ProceduralDistributions.lua* embeds vanilla data in which
items appear with bare names, such as `Baseball` followed by a weight [19]. The
B42 stub for the same file carries only the type annotations, not vanilla
entries [18], so the B42 name format cannot be confirmed from it.

Global helper functions in the same stub files exist in both builds'
indexes: `ClearAllDistributionItems`, `RemoveItemFromDistribution`,
`ReplaceItemInDistribution`, `MergeDistributionRecursive` and
`DeepPrintDistributionTable` [18] [19]. Three events cover the merge phase:
`Events.OnPreDistributionMerge`, `Events.OnDistributionMerge` and
`Events.OnPostDistributionMerge`, present in both builds' stubs [20] [21]. The B42 stub
describes the Pre event as "triggered after the distribution tables have
been merged", the same wording as the post event's near-twin, whereas the B41
stub speaks of the plain event as "fires when the tables merge" [20] [21].

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 *(B42)* |
|------|---------------------|---------------------|
| Recipe block | `Recipe` block [27] | `craftRecipe` with `inputs`/`outputs` children; documented in ScriptsDocs [9] [10] |
| Recipe knowledge | Java `Recipe` exposes learn flag and Lua hooks [24] | `NeedToBeLearn`, `AutoLearn*`, `MetaRecipe`, research parameters [9]; the see-all-recipes cheat was removed in 42.13.0 and replaced by a handcraft-panel tickbox [3] |
| Item class parameter | `Type` (wiki-era usage; deprecation noted only on B42 docs) [8] | `ItemType` with `base:` values; `Type` deprecated since 42.13.0 [8] |
| Item tags | No `ItemTag` class in the stub index [19] | Namespaced tags, `ItemTag` refactored to a registry-backed class in 42.13.0; mods can register tags [3] [22] |
| Build recipes | `Multistagebuild` block [27] | `entity` script holds a `craftRecipe` as its build recipe [9] [27] |
| Cooking recipes | `evolvedrecipe` class present [19] | Same block; `MinimumWater` and a frozen-food rule appear in the docs and notes [3] [11] |
| Distribution stubs | Stub embeds vanilla list data [19] | Stub is annotation-only [18] |
| Distribution content | Baseline | 42.13.0 "Updated loot distribution"; 42.14.0 added `agriworker`, `campworker` and `hunterstorage` rooms and removed containers unused by TIS maps; .223 references became 5.56 [3] [4] |
| Distribution events | Pre, plain and Post events present [21] | Same three events [20] |
| Doc coverage | No ScriptsDocs for B41 [7] | ScriptsDocs generated from game data, stamped 42.21.0 [7] |
| Tag/registry loading | n/a | `registries.lua` declares tags, item types, traits, professions and more before scripts load; 42.13.0 notes say mods may fill registries [3] [28] |

The 42.20.0 stable notes add two loot-adjacent entries: a fix so the same
building no longer shows different loot to different players, and a fix for an
exploit allowing arbitrary item spawning through mod data [1].

# Practical Guidance

The snippets below are illustrative templates built from the cited block
shapes, not copies of game files; check each against ScriptsDocs [7] and your
target build before shipping.

An item (B42 form; on B41 the class parameter was `Type`):

```text
module Base {
    item MyMod_Widget {
        ItemType = base:normal,
        DisplayCategory = Material,
        Weight = 0.5,
        Tags = base:hasmetal,
    }
}
```

Add `"Base.MyMod_Widget": "Widget"` to your `ItemName` translation file, keyed
by the full type, so the name and weight work [8]. Prefix your item IDs with
your mod name when using `Base` [27].

A B42 recipe splitting it into parts:

```text
module Base {
    craftRecipe MyMod_SplitWidget {
        timedAction = Making,
        Time = 80,
        Tags = InHandCraft,
        category = Miscellaneous,
        inputs {
            item 1 [Base.MyMod_Widget],
        }
        outputs {
            item 2 Base.Nails,
        }
    }
}
```

Add `"MyMod_SplitWidget": "Split widget"` to the `Recipes` translation file,
keyed by the bare recipe ID [9]. Remember that `Tags` needs at least one
crafting-bench tag [9].

Adding loot, as a Lua file in `media/lua/server/`:

```lua
local function addMyLoot()
    local list = ProceduralDistributions.list.SomeVanillaList
    table.insert(list.items, "MyMod_Widget")
    table.insert(list.items, 4)
end

Events.OnPreDistributionMerge.Add(addMyLoot)
```

Replace `SomeVanillaList` with a real list name taken from the B42
procedural-distribution reference [16] [18]. The `items` array alternates name
and weight [18], so always insert the pair in order. Use the item name format
you see in the vanilla data for your target build; B41 uses bare names [19].

Working habits that follow from the sources:

- Reference item IDs with the module prefix everywhere to dodge the
  inconsistent unqualified lookup [13] [27].
- Prefer new module names for your own scripts, since redefining a block ID
  soft-overrides it, which also lets a mod change vanilla items by
  accident [8] [9] [27].
- Do your distribution edits in one function bound to one event, and use the
  helper functions to remove or replace vanilla entries rather than writing
  your own loops [18].
- Keep dual-build mods split: B41 script files at the mod root, B42 files in
  the version folder, as `modders-foundation` describes.
- Re-pull the ScriptsDocs page for any block you rely on after each game
  update, because it is generated from game data [7] [26].

# Common Pitfalls & Troubleshooting

- **"My script is ignored / parses oddly."** Missing trailing commas, or
  `//` comments, break parsing; only `/* */` comments work [27].
- **"My weight shows as zero."** Add the `ItemName` translation entry; the
  docs say weight does not work without it [8].
- **"My B41 recipe vanished on B42."** `craftRecipe` is the documented B42
  format and ScriptsDocs has no `Recipe` block, so rewrite it [9] [27].
- **"Recipe is not in the menu."** `tags` is required and needs a crafting
  bench tag; also check learn requirements and `OnAddToMenu` returns [9].
- **"My recipe name shows as the ID."** The `Recipes` translation key is the
  bare recipe ID, no module prefix [9].
- **"My custom tag does nothing."** On B42 the tag must be registered in
  `registries.lua` (exact filename, in `media`) and the namespaced ID used in
  the item script [8] [22] [28].
- **"My trait, profession or item type is rejected."** Those IDs need their
  own registry entries first, in the same file [28].
- **"Edits to distributions have no effect."** The merge events exist for
  this phase; the stub descriptions of the Pre event conflict, so test which
  event runs after the vanilla tables load in your build [20] [21].
- **"My mod's loot used a container that vanished."** 42.14.0 removed
  containers not used by TIS maps from the Distributions file [4].
- **"A mod using `loadstring` broke after 42.20.4."** Those functions were
  removed in 42.20.4 and re-enabled in 42.21 [2] [5].

# Community Notes & Unverified Claims

## Claim 1 — Distribution edits belong in Events.OnPreDistributionMerge

- **Claim:** Modding guides and community mods commonly register loot edits on
  `Events.OnPreDistributionMerge` so their changes participate in the merge.
- **Why unverified:** The Umbrella stubs only give one-line event descriptions
  that conflict between Pre and post wording [20] [21]; no primary source
  states the intended mod pattern.
- **Confidence:** Low. Widely repeated and plausible but not primary-sourced
  here; the template above uses it as an assumption.

## Claim 2 — B42 distribution item names still use bare IDs

- **Claim:** Mod authors report that loot-list entries use bare item names
  such as `Baseball` rather than full types, on B42 as on B41.
- **Why unverified:** Only the B41 stub embeds vanilla names [19]; the B42
  stub is annotation-only [18].
- **Confidence:** Low. The B41 evidence is solid but B42 is not verified.

## Claim 3 — Modded items in a custom module work in distributions

- **Claim:** Community advice says items defined in a custom module need the
  full type in distribution lists while `Base` items use bare names.
- **Why unverified:** No cited source states the lookup rule for distribution
  entries; ScriptsDocs only calls module lookup inconsistent in general [13].
- **Confidence:** Low. Unverified inference from the general lookup warning.

# Risks & Caveats

- **Version skew.** ScriptsDocs is stamped 42.21.0 [7] but the Umbrella stubs
  are 42.20.0 [18]; 42.21 stable shipped 2026-09-28 [2], and parameter
  defaults could differ from 42.20.
- **Wiki lag.** The pzwiki Scripts page is stamped 42.17.0 and says it may be
  out of date [27].
- **Generated docs are incomplete.** Many ScriptsDocs parameters carry the
  type `Unknown` or "no description" [8] [12]; absence of a description is
  not evidence a parameter is useless.
- **B41 recipe syntax gap.** This document cannot give B41 `Recipe`
  grammar from a primary source.
- **No in-game test.** No snippet here has been run in a game build.
- **Stubs are not engine truth.** Umbrella describes the Lua surface only; it
  says nothing about script grammar [18].

# Verification Steps

1. Open `media/scripts/` in the installed game and read an existing `item`,
   `craftRecipe` and `evolvedrecipe` block next to ScriptsDocs [7] [8] [9].
2. Check `ItemType` is accepted: define the item snippet above on 42.20 and
   spawn it with the debug item list.
3. Test the recipe snippet; confirm the menu entry appears and the name
   resolves through the `Recipes` translation [9].
4. In the Umbrella 42.20.0 checkout open `library/events.lua` and search for
   `DistributionMerge` [20]; do the same at the 41.78.16 pin under
   `library/Events/Events.lua` [21].
5. Open the game's `media/lua/server/Items/ProceduralDistributions.lua` and
   record the item name format and a real list name [16] [18].
6. Print the merged tables after load using `DeepPrintDistributionTable`
   [18] to see which event sees vanilla data.
7. Grep ScriptsDocs for the Item page's version header to compare with your
   installed build [7].

# Open Questions

- Does 42.20 still parse the B41 `Recipe` block? The B42 stubs still ship the
  class [25], but ScriptsDocs does not list the block [13].
- Which of the three merge events runs after vanilla tables are fully
  populated, and does that differ between builds? [20] [21]
- What is the exact item-name rule in B42 distribution lists (bare or full
  type), and for custom modules?
- Is the old `Type` parameter still honoured by 42.20, or only rejected as
  the guide implies? ScriptsDocs says deprecated, the guide says renamed [8] [28]
- Did parameter defaults change between 42.20.0 and 42.21.0? [7] [2]

# References

**Primary Sources** — official patch notes, ScriptsDocs generated from game data, pinned Umbrella stubs.

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (29 July 2026). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259 Accessed 2026-10-07.
- [2] **The Indie Stone** — *Build 42.21 Stable Released* (28 September 2026). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07.
- [3] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (11 December 2025). https://steamcommunity.com/games/108600/announcements/detail/1818752592122972 Accessed 2026-10-07.
- [4] **The Indie Stone** — *Build 42.14.0 Unstable Released* (16 February 2026). https://steamcommunity.com/games/108600/announcements/detail/1824644522845673 Accessed 2026-10-07.
- [5] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (26 August 2026). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601 Accessed 2026-10-07.
- [6] **Valve** — *Steam News Web API (ISteamNews), app 108600* (mirror used to date the posts above). https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0 Accessed 2026-10-07.
- [7] **PZ-Wiki-Modding** — *ScriptsDocs* index (site "PZ API Documentation 42.21.0"). https://pz-wiki-modding.github.io/PZ-API-Docs/scripts.html Accessed 2026-10-07.
- [8] **PZ-Wiki-Modding** — *ScriptsDocs: item*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html Accessed 2026-10-07.
- [9] **PZ-Wiki-Modding** — *ScriptsDocs: craftRecipe*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/craftrecipe.html Accessed 2026-10-07.
- [10] **PZ-Wiki-Modding** — *ScriptsDocs: inputs* and *outputs*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/inputs.html and https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/outputs.html Accessed 2026-10-07.
- [11] **PZ-Wiki-Modding** — *ScriptsDocs: evolvedrecipe*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/evolvedrecipe.html Accessed 2026-10-07.
- [12] **PZ-Wiki-Modding** — *ScriptsDocs: fixing*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/fixing.html Accessed 2026-10-07.
- [13] **PZ-Wiki-Modding** — *ScriptsDocs: module*, *imports* and *ROOT-Scripts*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/module.html , https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/imports.html and https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root_files/scripts.html Accessed 2026-10-07.
- [14] **PZ-Wiki-Modding** — *ScriptsDocs: itemMapper*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/itemmapper.html Accessed 2026-10-07.
- [15] **PZ-Wiki-Modding** — *PZ API Docs: Item Tags*. https://pz-wiki-modding.github.io/PZ-API-Docs/java/item_tags.html Accessed 2026-10-07.
- [16] **PZ-Wiki-Modding** — *PZ API Docs: Procedural distributions properties*. https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/procedural_distributions_properties.html Accessed 2026-10-07.
- [17] **PZ-Wiki-Modding** — *PZ API Docs: ItemPickerContainer properties*. https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/item_picker_container_properties.html Accessed 2026-10-07.
- [18] **PZ-Umbrella** — *Umbrella 42.20.0 (commit 58204fc4)*, *Distributions.lua*, *ProceduralDistributions.lua*, *SuburbsDistributions.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/lua/server/Items/Distributions.lua , https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/lua/server/Items/ProceduralDistributions.lua and https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/lua/server/Items/SuburbsDistributions.lua Accessed 2026-10-07.
- [19] **PZ-Umbrella** — *Umbrella 41.78.16 (commit fa2e7e19)*, the same three distribution stubs. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Lua/server/Items/Distributions.lua , https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Lua/server/Items/ProceduralDistributions.lua and https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Lua/server/Items/SuburbsDistributions.lua Accessed 2026-10-07.
- [20] **PZ-Umbrella** — *Umbrella 42.20.0 events.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/events.lua Accessed 2026-10-07.
- [21] **PZ-Umbrella** — *Umbrella 41.78.16 Events.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Events/Events.lua Accessed 2026-10-07.
- [22] **PZ-Umbrella** — *Umbrella 42.20.0 ItemTag.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/zombie/scripting/objects/ItemTag.lua Accessed 2026-10-07.
- [23] **PZ-Umbrella** — *Umbrella 42.20.0 CraftRecipe.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/zombie/scripting/entity/components/crafting/CraftRecipe.lua Accessed 2026-10-07.
- [24] **PZ-Umbrella** — *Umbrella 41.78.16 Recipe.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.scripting.objects/Recipe.lua Accessed 2026-10-07.
- [25] **PZ-Umbrella** — *Umbrella 42.20.0 Recipe.lua*. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/zombie/scripting/objects/Recipe.lua Accessed 2026-10-07.
- [26] **PZ-Wiki-Modding** — *pz-scripts-data* (the data repository ScriptsDocs is generated from). https://github.com/PZ-Wiki-Modding/pz-scripts-data Accessed 2026-10-07.
- [28] **The Indie Stone Forums** — *Modding Migration Guide (42.13)*, first post by moderator nasKo, 2025-12-11, with attachments "Migration Guide.pdf" and "testmod_registries.zip" (attachments need a forum sign-in; read from the user-downloaded copies). https://theindiestone.com/forums/topic/88499-modding-migration-guide-4213/ Retrieved 2026-10-07 (host bot-blocks checkers).

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [27] **PZwiki** — *Scripts* (revision 1442815, page version 42.17.0). https://pzwiki.net/wiki/Scripts Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating** — none used.

**Community & Creator** — none used; see quarantined claims.

**Further Reading**

# Further Reading

- The CraftRecipe class stub, for the Java side of the recipe model (see [23]):
  https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/java/zombie/scripting/entity/components/crafting/CraftRecipe.lua
- Room distribution reference tables:
  https://pz-wiki-modding.github.io/PZ-API-Docs/mapping/rooms_distributions.html

# Related Documents

- `modders-foundation` — parent overview: mod layout, `mod.info`, script file
  introduction.
- `modders-lua-api-surface` — the Lua API behind recipe callbacks and tags.
- `modders-events-callbacks` — event semantics for the distribution events.
- `modders-modinfo-modid-conventions` — Mod ID and naming hygiene.
- `modders-first-mod-tutorial-b42` — end-to-end B42 mod using these blocks.
- `modders-porting-b41-to-b42` — porting checklist, including recipes.
- `players-crafting-chains` — player-side facts of the crafting overhaul.
- `admins-workshop-mod-wiring` — server-side mod deployment.
- `meta-style-guide` — how documents in this knowledge base are written.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (virtual agent) | Added the 42.13+ registry system from the official migration guide; resolved the ItemType and tag-registration open questions. | — |
