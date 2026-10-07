---
id: modders-first-mod-tutorial-b42
title: "Your First Build 42 Mod: A Verified Step-by-Step Tutorial"
version: 1.0.0
status: approved
confidence: Medium
category: Modders
topic: "First mod tutorial"
build: B42
document_type: tutorial
created: 2026-10-07
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-lua-api-surface, modders-events-callbacks, modders-modoptions-pzapi, modders-item-scripts-distributions, modders-mp-networking-porting, modders-modinfo-modid-conventions, modders-porting-b41-to-b42, players-crafting-chains, admins-workshop-mod-wiring, meta-style-guide]
tags: [tutorial, first-mod, b42, lua, mod-info, events, halo-text, item-script, workshop, debug]
game_versions_verified: ["42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-first-mod-tutorial-b42 |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Modders |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 42.20 and 42.21 (API names checked against the Umbrella 42.21.0 stubs; 42.20.0 stubs kept as comparison; code never run in a live game) |

# Executive Summary

This tutorial walks a newcomer through the smallest useful Build 42 mod: a
folder skeleton with the mandatory `common/` folder and a `42/` version
folder, a `mod.info` manifest, one client-side Lua file that reacts to a game
event and shows floating "halo" text above the player, and an optional
scripted item handed to a brand-new character. It then covers local testing,
the log file to read when something fails, Debug mode, and packaging for the
Steam Workshop.

Every API name used in the code is confirmed to exist in the Umbrella 42.21.0
stubs [1] [2] [3] [4], and every path or key claim is cited to a stub, a
documentation site generated from game data, or a pinned pzwiki revision
used as a fact source only. The code itself has not been executed in a live
game by the author of this document; the Verification Steps section is
the test plan. For that reason document confidence is Medium.

Version note: this revision re-baselines the tutorial from 42.20 to 42.21,
which reached stable on 2026-09-28 [7]. The API names were re-checked against
the 42.21.0 stubs and the 42.20.1 to 42.21 patch notes were read for anything
that touches the steps [21] [22] [23] [24]; no step needed to change. Nothing
was run in a live game, so the 42.21 check is a stub-and-notes review, not a
play test.

# Key Takeaways

- A B42 mod is detected only if it has a `common/` folder or at least one
  version folder; the safe layout carries both, with `mod.info` and `media/`
  inside the version folder. *(cited)* *(B42)*
- Client Lua lives under `media/lua/client/`; use a subfolder named after your
  mod to avoid file-path clashes with vanilla and other mods. *(cited)* *(both)*
- `Events.OnGameStart` is documented as firing once loading finishes and the
  player enters the game, which makes it a good first hook. *(cited)*
- `HaloTextHelper.addGoodText(player, text)` shows green halo text and exists
  in the B42 stubs; the B41 stubs list no `addGoodText`. *(cited)* *(B42)*
- An item script needs `ItemType`, and its display name comes from an
  `ItemName` translation entry, not from the deprecated `DisplayName`
  parameter. *(cited)* *(B42)*
- Read `console.txt` in the `Zomboid` cache folder when a mod misbehaves; add
  `-debug` to the launch options to start in Debug mode. *(cited)*
- Do not keep two loaded copies of one Mod ID; they overwrite each other.
  *(cited)*
- The exact in-game menu clicks to enable a mod are not primary-sourced here
  and are quarantined as a claim. *(community, unverified)*

# Purpose

To give a first-time modder one linear, minimal path from an empty folder to a
published Build 42 Workshop item, with each step tied to a citable fact and
each API symbol checked against the pinned stubs. It deliberately goes deeper
on workflow than the overview in `modders-foundation` and defers API breadth
to `modders-lua-api-surface` and `modders-events-callbacks`.

# Scope

Covered: folder and `mod.info` set-up, one client Lua file, one optional item
script, local testing, the log file, Debug mode, and Workshop packaging, all
for Build 42.21 (stable), with wiki-sourced layout facts carried forward from
the 42.20 revision. Not covered: recipes (see
`modders-item-scripts-distributions` and `players-crafting-chains`), mod
options (see `modders-modoptions-pzapi`), multiplayer networking (see
`modders-mp-networking-porting`), Mod ID rules in depth (see
`modders-modinfo-modid-conventions`), server-side Workshop wiring (see
`admins-workshop-mod-wiring`), and porting B41 mods (see
`modders-porting-b41-to-b42`). Unstable-branch behaviour is out of scope.

# Definitions

- **Halo text** — the short floating text shown above a character; here
  produced through the `HaloTextHelper` class [2].
- **Version folder** — a mod subfolder such as `42/` that holds that game
  version's `media/` and `mod.info` [14].
- **Full type** — an item's module name and ID joined by a dot, for example
  `MyFirstMod.Token` [16] [8].
- **Cache folder** — the `Zomboid` directory in the user's profile, holding
  `console.txt`, `mods/` and `Workshop/` [14] [17].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | No | Not verified | This is a B42 tutorial; see Delta for what differs. Legacy 41.78.21 was released 2026-08-26 [13] |
| B42 (stable) | Yes | API names against Umbrella 42.21.0 (commit `13d01f9`) [1]; scripts and mod.info against a ScriptsDocs site labelled 42.21.0 [8] [9] | 42.20.0 went stable 2026-07-29 [12]; 42.21 stable followed on 2026-09-28 [7]. Previously verified against the 42.20.0 stubs (commit `58204fc`) [25] |

**What was re-checked for 42.21.** The five symbols in the table under
"Events and API used in this tutorial" were re-opened in the 42.21.0 stubs and
their signatures and descriptions match the 42.20.0 text [1] [2] [3] [4] [25].
The 42.20.1, 42.20.2, 42.20.4, 42.21 unstable, 42.21 stable and forum patch
notes were read for changes to mod folders, mod.info, scripts, item naming,
events or halo text [21] [22] [13] [23] [7] [24]; the changes that bear on this
tutorial are listed in Reference. Statements that cite the pzwiki pages, the
documentation-site pages and the ScriptsDocs site are carried forward from the
42.20 revision with no contradicting change found in those notes; they were
not re-tested in a game.

# Reference

**Evidence layer.** Facts below are cited; the walkthrough built from them is
in Practical Guidance.

## Folder layout

The B42 mod layout puts a `common/` folder and one or more version folders
(`42/`, `42.1/`) inside the mod folder; each version folder holds its own
`media/` and `mod.info` [14]. The `common/` folder is documented as mandatory
even when empty, and at least one version or `common/` folder is needed for
the game to recognise the mod [14]. The game loads `common/` first, then the
version folder closest to the running game version, which overrides matching
`common/` files [14].

Two cache sub-folders matter: `mods/` for manually placed mods and
`Workshop/` for items being prepared for upload, with
`Workshop/<Item>/Contents/mods/<Mod>/` as the uploaded part, plus
`workshop.txt` and a 256x256 `preview.png` beside `Contents/` [14]. Two copies
of one Mod ID in different recognised locations clash and overwrite each
other [14].

## mod.info

`mod.info` is the manifest file; its `id` is the unique identifier used to
activate the mod and is not the Workshop ID [9]. The `name` parameter is the
title shown in the in-game mod manager, `description` and `author` are
free text, and `versionMin` sets the lowest compatible game version in at
least `build.major` form, for example `42.0` [9]. The file name must be lowercase
for Linux and macOS [20].

## Lua placement and loading

Lua files go in `client`, `server` or `shared` folders under `media/lua`; the
`client` folder is not loaded on a multiplayer server, and organisation inside
is free [15]. A Lua file with the same relative path as a vanilla file
overwrites it, so a subfolder named after the mod avoids clashes [15]. Lua is
loaded in the order shared-vanilla, shared-mod, client-vanilla, client-mod [15].

## Events and API used in this tutorial

| Symbol | What the stubs say | Build |
|--------|--------------------|-------|
| `Events.OnGameStart` | Client event triggered upon finishing loading and entering the game; callback takes no arguments [1] | B42 stubs |
| `Events.OnNewGame` | Client event triggered when a local player character is first created; callback receives the player and the spawn square [1] | B42 stubs |
| `getSpecificPlayer(0)` | Global returning the player for a split-screen index; the stub notes it is preferred over `getPlayer()` for split-screen support [3] | B42 stubs |
| `HaloTextHelper.addGoodText(player, text)` | Static helper taking an `IsoPlayer` and a string [2] | B42 stubs |
| `ItemContainer:AddItem(type)` | Takes an item type string and returns the created `InventoryItem` [4] | B42 stubs |

## Item scripts

Script files sit under `media/scripts/` [16]. Entries live in a `module`
block; the vanilla module is `Base`, and a custom module name is allowed
[16] [10]. The documentation site recommends a mod-specific module over
inserting into `Base` [10]. An `item` block requires an ID and an `ItemType`
whose allowed values include `base:normal` [8]. The item's display name is
provided through an `ItemName` translation entry keyed by the full type, and
`DisplayName` is marked deprecated as of 42.13.0 [8] [11]. The `Weight` parameter
defaults to 1.0, and the page warns an item needs a translation entry
for weight to work in game [8].

## Changes since 42.20.0 that touch this tutorial

Mods gained the ability to write `.json` files in 42.20.1 [21]. Translation
files needed a fix for the percent sign: mod translations should write `%%` to
show a literal `%` [21], a temporary workaround accepts both forms, and the
developers said it will be removed in a future unstable update [22]. 42.21
updated the localization system to allow more translatable strings [23] [24],
and its notes say a `RuntimeException` is now raised when missing translations
or missing recipes are detected, in place of a `System.err.println` message
[24]. The notes do not say in which situations the exception fires. The
42.21.0 `events.lua` stub declares ten events that the 42.20.0 stub does not
(`AcceptedMedicalCheck`, `OnFillInventoryContextMenuNoItems`, `OnForagePool`,
`OnForageRequestZone`, `OnForageSpot`, `OnJoypadDebugRenderUIOptionSet`,
`OnPreFillInventoryContextMenuNoItems`, `OptionControllerButtonStyleChanged`,
`OptionGamepadBindingPresetChanged`, `RequestMedicalCheck`) and drops none; the
tutorial uses none of them [1] [25]. The `loadstring` and `loadstream` methods
removed in 42.20.4 were re-enabled in 42.21; the tutorial uses neither [13] [7].

## Logs and Debug mode

The main game log is `console.txt` in the `Zomboid` folder, which defaults to
`%USERPROFILE%\Zomboid` on Windows; logs can reveal which mod causes an error
[17]. Debug mode is entered by adding `-debug` to the launch options, with JVM
arguments first and ended by `--` when present [18]. Lua can be reloaded
manually in Debug mode from the main menu [15]. The startup-parameters
page is stamped for 42.17.0, older than the current stable [18].

## Packaging and upload

The in-game uploader is reached from Workshop, then "Create and update
items", and lists the valid mods in the `Workshop/` folder [19]. It asks for
title, description, tags and visibility, creates or reuses a Workshop ID, and
appends the Workshop ID and Mod ID to the description [19]. It overwrites the
whole description on each upload [19]. Files removed from a new version are
not removed on subscribers' machines [19].

# B41 vs B42 Delta

A short delta, since this is a B42-only document; the differences that change
the workflow are below.

- **Layout.** B41 used `media/` and `mod.info` directly in the mod folder;
  B42 adds `common/` and version folders, and both layouts can coexist in one
  mod folder [14].
- **Halo helper.** The 42.21.0 stub declares `HaloTextHelper.addGoodText` and
  `HaloTextHelper.addBadText` *(B42)* [2]; the 41.78.16 stub lists only
  `HaloTextHelper.addText` and `HaloTextHelper.addTextWithArrow` *(B41)* [5].
- **Item naming.** `DisplayName` is deprecated from 42.13.0 in favour of an
  `ItemName` translation entry *(B42)* [8].
- **Script syntax.** The `ItemType = base:normal` form comes from a B42
  documentation site [8]; the B41 item format is outside this document.
- **Events.** `OnGameStart`, `OnNewGame` and `OnCreatePlayer` appear in both
  stub sets, as checked by the repository's index builder against the 42.21.0 stubs [1]
  and the 41.78.16 stubs [6].
- **Wider B41 to B42 differences** are covered in `modders-porting-b41-to-b42`.

# Practical Guidance

This is the walkthrough. Each step restates cited facts from Reference;
anything that cannot be sourced is in Community Notes.

## Step 1 - Create the folder skeleton

Develop in the cache folder, using the layout from [14]:

```text
Zomboid/Workshop/MyFirstModWorkshop/
  Contents/mods/MyFirstMod/
    common/
    42/
      mod.info
      media/
        lua/client/MyFirstMod/Hello.lua
        scripts/MyFirstMod_items.txt
  preview.png        (256x256)
  workshop.txt
```

Keep only one copy of the Mod ID on the machine (unsubscribe from your own
published copy) [14].

## Step 2 - Write mod.info

```text
name = My First Mod
id = MyFirstMod
author = Your Name
description = Shows a halo text message when a game starts.
versionMin = 42.0
```

Keep the file name lowercase [20] [9].

## Step 3 - Write the Lua file

Create `42/media/lua/client/MyFirstMod/Hello.lua`:

```lua
local function sayHello()
    local player = getSpecificPlayer(0)
    if player then
        HaloTextHelper.addGoodText(player, "My First Mod is running")
    end
end

Events.OnGameStart.Add(sayHello)
```

This uses `Events.OnGameStart` [1], `getSpecificPlayer(0)` [3] and
`HaloTextHelper.addGoodText` [2]. The `if player` guard is a defensive habit,
not a documented requirement.

## Step 4 (optional) - Add one item and give it to new characters

Create `42/media/scripts/MyFirstMod_items.txt`:

```text
module MyFirstMod
{
    item Token
    {
        ItemType = base:normal,
        Weight = 0.1,
    }
}
```

The module-and-item structure and `base:normal` come from [10] and [8]. Give
the item to a fresh character by adding to the same Lua file:

```lua
local function giveToken(player, square)
    player:getInventory():AddItem("MyFirstMod.Token")
end

Events.OnNewGame.Add(giveToken)
```

This uses `Events.OnNewGame` [1] and `ItemContainer:AddItem(type)` [4]. For a
readable name, add an `ItemName` entry whose key is `MyFirstMod.Token` [8] [11].
The file location of that entry is not primary-sourced here (Claim 2).

## Step 5 - Test locally

1. Launch the game and open the in-game mod manager; enable `My First Mod`
   (see Claim 1 for the menu route). The manager lists mods by their
   `name` [9].
2. Start a new game. You should see the halo text on entering the world, and
   the token in your inventory if you did Step 4.
3. If nothing appears, open `console.txt` in the `Zomboid` folder and look
   for errors that name your file [17].
4. Optionally start with `-debug` in the Steam launch options [18]. In Debug
   mode the main menu can reload Lua without restarting [15].

## Step 6 - Package and publish

Ensure `preview.png` is 256x256 and `Contents/mods/MyFirstMod/` is complete
[14]. In the main menu choose Workshop, then "Create and update items", select
the mod, fill in title, description, tags and visibility, and upload [19].
Keep a private copy of your description text, because the next upload
overwrites it [19].

# Common Pitfalls & Troubleshooting

- **Mod not listed.** Missing `common/` and version folders, or `mod.info`
  placed at the mod root instead of in `42/` [14].
- **Edits not visible.** Two loaded copies of the same Mod ID overwrite each
  other; remove the duplicate [14].
- **Nothing happens at start.** The Lua file is outside `media/lua/client`, or
  has a typo; read `console.txt` for the error [15] [17].
- **Item has no proper name or odd weight.** Missing `ItemName` entry [8]. On 42.21 missing translations may also surface as an exception rather than a log line [24].
- **Percent sign in a translation string.** Write `%%` for a literal `%` [21] [22].
- **Case errors on Linux and macOS.** Folder and file names are
  case-sensitive, so `common` is not `Common` [14] [20].
- **Ghost files after an update.** The Workshop does not delete removed files
  on subscriber machines; ship them emptied [19].
- **Halo helper missing when testing on B41.** The B41 stubs do not list
  `addGoodText` [5].

# Community Notes & Unverified Claims

## Claim 1 — Mods are enabled from a "Mods" button on the main menu by ticking the mod and accepting

- **Claim:** Community tutorials describe a Mods entry on the main menu where
  each mod is switched on (and sometimes ordered) before starting or loading a
  save.
- **Why unverified:** No primary source describing the exact menu route was
  found for 42.20; the cited docs confirm only that a mod manager exists and
  lists mods by name [9].
- **Confidence:** Medium. Widely repeated and consistent with [9], but the
  exact clicks are unsourced.

## Claim 2 — The ItemName translation file sits under media/lua/shared/Translate/EN/

- **Claim:** Community mods place a JSON `ItemName` translation file in a
  `Translate/EN` folder under `media/lua/shared` in B42.
- **Why unverified:** The documentation site names the file type and key
  format [11] but gives no folder path, and the folder convention changed in
  the 42.x cycle (wiki mentions a move to JSON) without a primary path
  statement.
- **Confidence:** Low. Path and file naming are unconfirmed on 42.20 and 42.21 (the 42.21 localization-system update is not documented in enough detail to settle it [23]).

# Risks & Caveats

- The tutorial code was not run in a live game during authoring; treat it as
  checked-against-stubs, not play-tested.
- ScriptsDocs is community-maintained and labelled 42.21.0, which now matches
  the stub pin [8] [9]; it was not re-fetched during this revision.
- The 42.21 re-baseline is a review of stubs and patch notes. The tutorial was
  not run on 42.21 or 42.20, and its multiplayer behaviour is not covered (see
  `modders-mp-networking-porting`).
- The Umbrella `42.20.0` tag was later moved upstream, so pin by commit, not
  by tag name [6].
- The startup-parameters, mod-structure and uploading wiki pages are stamped
  older than 42.20.0 [18] [14] [19].
- Whether `Workshop/` items load locally without copying to `mods/` is not
  stated in the cited sources; see Verification Steps.

# Verification Steps

1. Pin Umbrella to commit `13d01f9ee58fa48773553920db56d06f0005e7f8` (release 42.21.0) and grep `library/events.lua` for
   `Events.OnGameStart` and `Events.OnNewGame` [1].
2. Open the HaloTextHelper stub file in the same commit and confirm `addGoodText` [2].
3. Build the folder from Step 1 and start the game; confirm the mod appears
   under its `name` [9].
4. Start a new game and confirm the halo text and, for Step 4, the item.
5. Place the mod in `Zomboid/mods/` instead of `Workshop/` to see whether the
   behaviour differs; record the result.
6. Deliberately break the Lua and confirm the error shows in `console.txt`
   [17].
7. Re-run `python scripts/check_api_exists.py` on this file after any edit.

# Open Questions

- Which of `Workshop/` or `mods/` is loaded for local testing on a stock
  install? [14]
- Exact path of the B42 `ItemName` JSON file (Claim 2).
- Resolved for the keys used here: the 42.21 stable post and forum notes list no change to item script keys, `mod.info` or folder layout [7] [24]; still untested in game.
- Where do `ItemName` entries live after the 42.21 localization-system update, and when does the missing-translation exception fire? [23] [24]
- Does `OnGameStart` also fire when a save is loaded, not only on new games?
  The stub says "upon finishing loading and entering the game" [1], which
  suggests yes, but it was not tested.

# References

**Primary Sources** — pinned Umbrella stubs, official announcements, ScriptsDocs.

- [1] **PZ-Umbrella** — *library/events.lua* at commit 13d01f9ee58fa48773553920db56d06f0005e7f8 (release 42.21.0). https://github.com/PZ-Umbrella/Umbrella/blob/13d01f9ee58fa48773553920db56d06f0005e7f8/library/events.lua Accessed 2026-10-07.
- [2] **PZ-Umbrella** — *HaloTextHelper.lua* at 42.21.0 commit 13d01f9. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/characters/HaloTextHelper.lua Accessed 2026-10-07.
- [3] **PZ-Umbrella** — *library/java/__global.lua* at 42.21.0 commit 13d01f9 (`getSpecificPlayer`, `getPlayer`). https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/__global.lua Accessed 2026-10-07.
- [4] **PZ-Umbrella** — *ItemContainer.lua* at 42.21.0 commit 13d01f9. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/13d01f9ee58fa48773553920db56d06f0005e7f8/library/java/zombie/inventory/ItemContainer.lua Accessed 2026-10-07.
- [5] **PZ-Umbrella** — *Candle HaloTextHelper.lua* at the 41.78.16 commit fa2e7e1. https://raw.githubusercontent.com/PZ-Umbrella/Umbrella/fa2e7e19799740b57902f1cb4e989225c295c05e/library/Candle/zombie.characters/HaloTextHelper.lua Accessed 2026-10-07.
- [6] **PZ-Umbrella** — *Umbrella releases* (tags 41.78.16 to 42.21.0); pins recorded in this repository's `sources/pins.json`. https://github.com/PZ-Umbrella/Umbrella/releases Accessed 2026-10-07.
- [7] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28; located through the Steam news API). https://steamcommunity.com/ogg/108600/announcements/detail/1844751498231307 Accessed 2026-10-07 (host bot-blocks checkers).
- [8] **PZ-Wiki-Modding** — *ScriptsDocs: item* (documentation site labelled 42.21.0). https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/item.html Accessed 2026-10-07.
- [9] **PZ-Wiki-Modding** — *ScriptsDocs: ROOT-ModInfo*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root_files/modinfo.html Accessed 2026-10-07.
- [10] **PZ-Wiki-Modding** — *ScriptsDocs: module*. https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/module.html Accessed 2026-10-07.
- [11] **PZ-Wiki-Modding** — *ScriptsDocs: Translation Files*. https://pz-wiki-modding.github.io/PZ-API-Docs/translations/translation_files.html Accessed 2026-10-07.
- [12] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/ogg/108600/announcements/detail/1839676055882259 Accessed 2026-10-07 (host bot-blocks checkers).
- [13] **The Indie Stone** — *42.20.4 STABLE and 42.19.2 UNSTABLE and 41.78.21 LEGACY Hotfixes Released* (Steam announcement). https://steamcommunity.com/ogg/108600/announcements/detail/1842212951296601 Accessed 2026-10-07 (host bot-blocks checkers).

- [21] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766 Accessed 2026-10-07 (host bot-blocks checkers).
- [22] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441 Accessed 2026-10-07 (host bot-blocks checkers).
- [23] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925 Accessed 2026-10-07 (host bot-blocks checkers).
- [24] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first post, 2026-09-23; the long fix lists are abridged to "selected" in the retrieved copy). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 (host bot-blocks checkers).
- [25] **PZ-Umbrella** — *library/events.lua* at the previous pin, commit 58204fc47895ba249592519cedecc7cfbaaebd60 (release 42.20.0; the upstream tag was later moved). https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/events.lua Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): URL + revision id; facts only.

- [14] **PZwiki** — *Mod structure* (revision 1443271). https://pzwiki.net/wiki/Mod_structure Accessed 2026-10-07. Fact-only source.
- [15] **PZwiki** — *Lua (API)* (revision 1390433). https://pzwiki.net/wiki/Lua_(API) Accessed 2026-10-07. Fact-only source.
- [16] **PZwiki** — *Scripts* (revision 1442815). https://pzwiki.net/wiki/Scripts Accessed 2026-10-07. Fact-only source.
- [17] **PZwiki** — *Tech Support* (revision 1442989). https://pzwiki.net/wiki/Tech_Support Accessed 2026-10-07. Fact-only source.
- [18] **PZwiki** — *Startup parameters* (revision 1393745). https://pzwiki.net/wiki/Startup_parameters Accessed 2026-10-07. Fact-only source.
- [19] **PZwiki** — *Uploading mods* (revision 1442321). https://pzwiki.net/wiki/Uploading_mods Accessed 2026-10-07. Fact-only source.
- [20] **PZwiki** — *mod.info* (revision 1363935). https://pzwiki.net/wiki/Mod.info Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating** — none.

**Community & Creator** — none.

**Further Reading** — see the Further Reading section.

# Further Reading

- Unofficial B42 JavaDocs for class and method lookup:
  https://albion.codeberg.page/PZ-JavaDocs/
- Umbrella repository (type stubs for editor intellisense):
  https://github.com/PZ-Umbrella/Umbrella

# Related Documents

- modders-foundation — ecosystem, toolchain and where API truth lives.
- modders-lua-api-surface — the wider Lua API after this first mod.
- modders-events-callbacks — the event catalogue behind `OnGameStart`.
- modders-modoptions-pzapi — adding player-facing options.
- modders-item-scripts-distributions — items, recipes and loot beyond Step 4.
- modders-mp-networking-porting — multiplayer concerns for client/server code.
- modders-modinfo-modid-conventions — Mod ID and mod.info rules in depth.
- modders-porting-b41-to-b42 — moving an existing B41 mod to B42.
- players-crafting-chains — the player-facing crafting side of scripted items.
- admins-workshop-mod-wiring — using a published mod on a server.
- meta-style-guide — how documents in this knowledge base are written.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined from 42.20 to 42.21: API names re-checked against Umbrella 42.21.0 (13d01f9); added post-42.20.0 changes (`%%` in translations, .json writes, localization update, missing-translation exception, loadstring/loadstream); resolved script-key open question. Sources: Steam posts 42.20.1, 42.20.2, 42.20.4, 42.21 unstable and stable, TIS forum 42.21 notes. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
