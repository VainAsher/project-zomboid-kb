---
id: modders-foundation
title: "Modding Project Zomboid: Ecosystem, Toolchain and Where the API Truth Lives"
version: 1.1.0
status: approved
confidence: Medium
category: Modders
topic: "Modding foundations"
build: both
document_type: overview
created: 2026-07-30
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [players-foundation, admins-foundation, creator-foundation, lore-foundation, meta-style-guide]
tags: [modding, lua, kahlua, umbrella, zomboiddoc, javadocs, mod-info, workshop, b42]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-foundation |
| Version | 1.1.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20.0, 42.21.0 (42.21 by review of patch notes and API stubs, not in-game) |

# Executive Summary

This is the foundation document for the Modders track. It maps what "modding
Project Zomboid" means across the two live builds — Build 41.78 (kept on the
`legacy41` Steam beta branch) and Build 42, stable since 29 July 2026 as
42.20.0 [1] [4] and currently at 42.21 (stable since 28 September 2026) [34] —
and tells a new modder where the load-bearing pieces
are: the Kahlua-based Lua 5.1 scripting environment [15], the mod folder
anatomy and `mod.info` manifest (including the Build 42 versioned-folder
layout) [17] [18], and the small set of community-maintained artifacts that
function as the de-facto API reference: the Umbrella type stubs, ZomboidDoc,
the unofficial JavaDocs and the LuaDocs [8] [10] [11] [12].

The headline for anyone arriving from Build 41: The Indie Stone stated
plainly at the start of the B42 cycle that Build 41 saves and mods are not
compatible with Build 42 [3]. The mod structure, the recipe script format and
the options API all changed [17] [21] [19], and the modding API itself was
restricted by a security patch in 42.14 whose lost functionality was only
restored in 42.20 [1]. Meanwhile the official modding guide and the next
generation of official tools (WorldZed, TileZed updates, AnimZed) are announced but, as of 2026-10-07, not announced as shipped in any
official post reviewed through the 42.21 stable release [2] [28] [34].

Document confidence is Medium: the release facts and repository facts come
from primary sources (re-checked on 2026-10-07 against the 42.20.1 to 42.21
posts and the 42.21.0 stubs), but much of the structural detail rests on
pzwiki fact citations whose page versions trail the current release by
several patches, and nothing here has been re-verified in-game.

# Key Takeaways

- Build 42.21 is the current stable build (released 28 September 2026,
  following 42.20.0 on 29 July 2026); Build 41 remains available on the
  `legacy41` beta branch. *(cited)* *(both)*
- B41 mods and saves do not work on B42 — The Indie Stone said so explicitly
  when B42 entered unstable. Porting is required, not optional. *(cited)*
- PZ Lua is Kahlua, a Java implementation based on Lua 5.1 with differences,
  with the game's Java classes exposed to scripts. It is not stock Lua and
  not 5.3+/LuaJIT. *(cited)* *(both)*
- A B42 mod needs a `common/` folder plus one or more version folders
  (`42/`, `42.1/`, …) each carrying its own `mod.info`; B41 used a flat
  `media/` + root `mod.info` layout. One Workshop upload can serve both
  builds because the two layouts do not collide. *(cited)*
- There is no complete official API documentation. The working truth lives in
  community artifacts: Umbrella EmmyLua stubs (release-tagged per game
  version, 41.78.16 through 42.21.0), the unofficial B42 JavaDocs (42.21.0),
  LuaDocs, and ZomboidDoc for compiling your own annotated library. *(cited)*
- B42 added a native options API, `PZAPI.ModOptions`, replacing the B41-era
  community "Mod Options" framework mod. *(cited)* *(B42)*
- B42 recipes use the new `craftRecipe` script block; B41's `Recipe` block is
  the legacy format. New B42-only script types include `entity` and
  `fluid`. *(cited)*
- The official modding guide, WorldZed/TileZed releases and AnimZed are
  announced for after the stable hotfix wave; no reviewed official post up to
  42.21 stable announces them as released. *(cited)*
- Since 42.20.0: use `%%` for a literal `%` in mod translation strings, mods
  may write `.json` files, and `loadstring`/`loadstream` were removed in
  42.20.4 and re-enabled in 42.21. *(cited)* *(B42)*

# Purpose

This document exists so that a developer who wants to mod Project Zomboid —
or an agent writing deeper Modders-track documents — starts from a correct
map: which build to target, what the scripting environment actually is,
where a mod's files go, which reference sources are authoritative at which
tier, and which official promises are still unshipped. Every later Modders
document assumes this foundation and goes deeper on one part of it.

# Scope

Covered: the meaning and legal frame of PZ modding; the Kahlua/Lua 5.1
environment at overview level; mod folder layout and `mod.info` basics for
B41 and B42, including B42 version-folder resolution and Mod ID hygiene; the
API-knowledge landscape (Umbrella, ZomboidDoc, JavaDocs, LuaDocs, game
files); the headline B41→B42 modding deltas; announced-but-unshipped
official tooling; and Steam Workshop publishing basics.

Not covered (deeper documents own these): Lua API details and events, script
block parameter references, per-field `mod.info` parameter tables, mapping
and 3D-asset pipelines, multiplayer/networking mod porting specifics, and
server-side mod deployment (Admins track). Unstable-branch behaviour after
42.21 stable is out of scope.

# Definitions

- **Kahlua** — the Java implementation of Lua that Project Zomboid embeds;
  based on Lua 5.1 with differences, running Lua scripts inside the Java
  game process [14] [15].
- **Mod ID** — the `id` value in `mod.info`; identifies a mod to the game
  and must not collide with another loaded copy [17] [18].
- **Workshop ID** — the numeric identifier Steam assigns to an uploaded
  Workshop item; distinct from the Mod ID, and one Workshop item may contain
  several mods [17] [24].
- **Version folder** — a B42 mod subfolder named after a game version
  (`42/`, `42.1/`), holding build-specific files and its own `mod.info` [17].
- **`common/` folder** — the B42 mod subfolder for shared assets, loaded
  before the matched version folder; mandatory for a B42 mod to be
  detected [17].
- **Umbrella** — community-maintained EmmyLua type stubs for the PZ Lua API,
  used for IDE intellisense and type checking [8].
- **ZomboidDoc (pz-zdoc)** — a compiler that generates an annotated Lua
  library from an installed copy of the game [10].
- **Spiffo's Workshop** — Project Zomboid's Steam Workshop hub, the official
  channel for sharing mods [26].
- **legacy41** — the Steam beta branch that keeps Build 41 playable after
  42.20.0 became the default stable build [4].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 (via sources dated to the B41 era; not re-run in-game) | Flat mod layout, `Recipe` scripts, community Mod Options framework [17] [21] [20] |
| B42 (stable) | Yes | 42.20.0, released 2026-07-29 [1] [27]; re-baselined to 42.21 (stable 2026-09-28) [34] | Versioned mod layout, `craftRecipe`, native `PZAPI.ModOptions` [17] [21] [19] |

Facts in this document were first verified against sources retrieved on
2026-07-30, the day after 42.20.0 shipped. Several pzwiki pages cited here
carry page-version stamps between 42.8.1 and 42.20.0; where a fact was last
wiki-verified before 42.20.0 this is noted in Risks & Caveats [17] [18] [19].

**What was re-checked for 42.21 (2026-10-07).** The official Steam posts for
42.20.1, 42.20.2, 42.20.3, 42.20.4 with 41.78.21, 42.21 unstable and 42.21
stable, and the 42.21 forum change list, were read for anything touching mod
structure, scripts, the Lua environment, tooling or the announced official
modding deliverables [30] [31] [32] [33] [34] [35]; the Umbrella 42.21.0
release and the Steam news feed were consulted for the tooling and
announcement status [9] [36] [28]; and the unofficial JavaDocs and LuaDocs
version stamps were re-read [11] [12]. Every other statement is carried
forward from the 2026-07-30 revision with no contradicting change found; it
was not re-tested in a game.

# Reference

## What modding Project Zomboid is

Project Zomboid ships with modding as a first-class feature: the game has a
built-in mod manager and an API surface intended for user content, and the
official distribution channel for mods is Spiffo's Workshop, PZ's home on
the Steam Workshop [14] [26]. Modding activity spans several fields: text
"script" files that define items, recipes and vehicles; Lua code against the
game API; Java-level modification; 3D modelling, texturing, animation;
mapping; and translations [14].

Modding is governed by the game's Terms & Conditions and the published
Modding Policy: modders may accept donations, but selling mods or gating mod
content behind payment is not allowed, and commissioned work is permitted
only so long as access to the resulting mod is not sold individually [6]
[14].

## The Lua environment: Kahlua, a modified Lua 5.1

PZ mods are programmed against Kahlua, a Lua interpreter written in Java;
it runs mod scripts inside the game's own Java process and exposes selected
Java classes and methods to Lua code [14] [15]. The language baseline is
Lua 5.1 [13], with differences from the reference implementation — pzwiki
warns that code behaving one way in an external Lua 5.1 interpreter may not
carry over exactly, and that features beyond 5.1 are unavailable [16].
Practical consequence: the authoritative description of what a modder can
call is not the Lua manual but the set of exposed Java classes plus the
game's own Lua files — which is why the API-truth artifacts in the next
subsection matter so much [15] [22].

Alongside Lua, the game consumes "script" text files (zedscripts) under
`media/scripts/` — a custom block-based data format (not a programming
language) that defines items, recipes, vehicles, sounds and more. Script
entries live inside a `module` block (the vanilla module is `Base`, so full
item IDs look like `Base.ItemName`), and definitions with an existing ID can
soft-override the original [21].

## Mod anatomy and mod.info

Local mods live in two cache-folder locations with different jobs:
`Zomboid/mods/` for manually installed mods, and `Zomboid/Workshop/` for
mods under development and destined for upload. Two loaded copies of the
same Mod ID clash and overwrite each other, which is a classic source of
"my changes don't appear" confusion during development [17].

A Workshop upload has the shape
`Workshop/<YourItem>/Contents/mods/<YourMod>/` plus `workshop.txt` (upload
metadata) and `preview.png` (the Workshop thumbnail, 256×256 as enforced by
the game). Only `Contents/` is uploaded, so sibling folders can hold a git
repository, raw assets or IDE files without polluting the released mod [17].

**Build 41 layout (B41):** the mod folder directly contains `media/` plus a
root `mod.info` and `poster.png` [17].

**Build 42 layout (B42):** the mod folder contains a mandatory `common/`
folder (shared assets — even if empty the mod is not detected without at
least one `common/` or version folder) plus one or more version folders
named after game versions (`42/`, `42.1/`), each holding its own `media/`
and its own `mod.info`. The game loads `common/` first, then the version
folder closest to the running game version, whose files override matching
`common/` files. Version-folder names resolve at build.major precision — a
folder named `42.1.5` is treated as `42.1` [17]. Because the B42 layout sits
one level deeper than the B41 layout, both can coexist in a single mod
folder, letting one Workshop item serve both builds [17].

`mod.info` is the manifest that makes the game recognise a mod: a plain
text file whose practically required parameters are `id` and `name`, with
further parameters including `author`, `description`, `poster`, `icon` and
`require` (dependencies by Mod ID). The filename must be lowercase for
Linux/macOS compatibility, and on B42 it is best kept in each version folder
rather than only in `common/`, since requirements tend to change with the
game version [18]. ID hygiene conventions worth adopting from the same
sources: keep the Mod ID unique (clashes overwrite), never develop from the
downloaded-Workshop copy of your own mod, and prefix script entry names
(`MyMod_MyItemID`) when defining entries inside the vanilla `Base`
module [17] [18] [21].

## Where the API truth lives

There is no complete, current official API documentation; the official
JavaDoc hosted at projectzomboid.com/modding/ stops at Build 41.77 [22].
The Indie Stone said with the 42.20 release that additional Modding API
documentation is planned [1]. In the meantime the working reference stack
is community-built:

| Artifact | What it is | Build coverage | Where |
|----------|------------|----------------|-------|
| Umbrella | EmmyLua type stubs for the PZ Lua API; drives intellisense and type checking in EmmyLua (recommended) or LuaLS language servers [8] | Releases tagged per game version from 41.78.16 through 42.21.0 (42.21.0 stubs published 2026-09-28, 42.20.0 on 2026-07-29) [9] | github.com/asledgehammer/Umbrella (now the PZ-Umbrella org) [8] |
| ZomboidDoc (pz-zdoc) | GPL-3.0 Lua library compiler that generates an annotated, EmmyLua-ready library from an installed game, aimed at IntelliJ IDEA [10] | Built in the B41 era; repository last pushed May 2023, so treat B42 output with caution [10] | github.com/cocolabs/pz-zdoc [10] |
| Unofficial JavaDocs (B42) | JavaDoc-style reference of the game's Java classes, maintained by Albion; its site stamp read 42.20.0 on 2026-07-30 and 42.21.0 on 2026-10-07 [11] [23] | B42 (a separate community project covers B41.78) [22] | albion.codeberg.page/PZ-JavaDocs [11] |
| LuaDocs | Doxygen-generated documentation of the game-side Lua: events, callbacks, hooks, classes and file locations; self-described as WIP and inference-reliant [12] [25] | 42.13.0 on 2026-07-30; its site stamp read 42.20.3 on 2026-10-07 [12] | demiurgequantified.github.io/ProjectZomboidLuaDocs [12] |
| Game files | The installed game's `media/scripts/` and `media/lua/` trees are the ultimate ground truth for both builds; decompiling the Java fills the remaining gaps [21] [22] | Per installed build | Local install |

The JavaDocs matter because they document exactly the Java classes and
methods exposed to Lua — if a name does not appear there, it is not in the
Java surface [22]. A further community alternative, a B42 JavaDoc with
source viewer (geromet.github.io/PZJavaDocs, at 42.15 when wiki-checked),
exists as a fallback [22].

## Modding-relevant changes in 42.20.1 to 42.21

Mods gained the ability to write `.json` files in 42.20.1 [30]. Translation
strings that contain a percent sign must use `%%` to show a literal `%`
(42.20.1), a temporary workaround accepts both forms, and the developers said
it will be removed in a future unstable update, with error logs pointing at
strings needing the fix (42.20.2) [30] [31]. 42.21 updated the localization
system to enable more translatable strings [33] [35]. For multiplayer, 42.20.1
improved Lua checksum validation as part of anti-cheat, and 42.21 expanded the
anti-cheat system [30] [33].

The 42.20.4 hotfix (shipped for stable, unstable and legacy) fixed security
vulnerabilities and, as part of that, removed the `loadstring` and
`loadstream` methods; authors who used them to run server-sent code were told
to create explicit methods and call them through commands, and to report
unsolvable cases in the official Discord's mod-portal channel [32]. 42.21
re-enabled both after further investigation of the security issue, with an
apology to modders and server admins [33] [34]. The 42.21.0 Umbrella index
declares neither as a global, so type stubs alone cannot tell you whether
they are callable [36].

## Steam Workshop publishing basics

Uploading happens from the main menu: Workshop → "Create and update items"
lists every valid mod in your `Workshop/` cache folder. The uploader sets
title, description, tags and visibility, creates or reuses a Workshop ID,
and appends the Workshop ID and Mod ID to the page description. Two known
behaviours to plan around: the uploader overwrites the whole Workshop
description each upload, and files deleted from a new version are not
removed on subscribers' machines (the wiki's workaround is to ship them
empty) [24]. Alternative pipelines exist — SteamCMD with a build config for
controlled uploads, plus community tools for preview images and partial
page updates [24].

## Announced but not shipped (as of 2026-10-07)

In the pre-stable "NEXT STEPS" post, The Indie Stone committed to releasing,
once stable hotfixing settles: their latest mapping tools (WorldZed,
TileZed, etc.), the in-house animation editor and integration tool AnimZed,
and an extensive modding guide [2]. The Steam announcement "BUILD 42 STABLE
PLANS" (2026-07-24) repeats the tools and the modding guide, and both it and
the earlier Steam "NEXT STEPS" announcement (2026-07-09) say the team will
also work, through the rest of 2026, on a Build 42 Support Update covering
optimization, additional modding support and player-requested polish [28]
[29]. None of the official posts from 42.20.1 through 42.21 stable (a
review of the posts, not of the whole internet) announces the release of the
tools or the modding guide, and the 42.21 posts describe 42.21 as the first
incremental update after Build 42 without calling it the Support Update [30]
[31] [32] [33] [34]. The currently available official
mapping tools remain, per the last wiki check on 2026-07-30, the B41-era
TileZed and WorldEd distributed free on the forums, with an outdated copy on
Steam under "Project Zomboid Modding Tools" [25]; that wiki page was not
re-fetched on 2026-10-07. Treat any workflow built on WorldZed or AnimZed as
future work, not present capability [2] [28].

# B41 vs B42 Delta

- **Compatibility break.** The Indie Stone's Build 42 unstable announcement
  (17 December 2024) states that Build 41 saves and mods are NOT compatible
  with Build 42 [3]. B41 remains playable — and B41 mods usable — via the
  `legacy41` beta branch [4]. Build 42 entered unstable 2024-12-17,
  reached stable as 42.20.0 on 2026-07-29 [27] [1], and stable moved to 42.21
  on 2026-09-28 [34].
- **Mod structure.** B41: flat layout, `media/` and `mod.info` at the mod
  root. B42: mandatory `common/` folder plus per-game-version folders each
  with their own `mod.info`; `common/` loads first and the closest version
  folder overrides it. The B41 `media/` folder is ignored by B42 and
  vice-versa, which is what makes dual-build Workshop items possible [17].
- **Recipes and scripts.** The B41 `Recipe` script block is legacy; B42
  recipes use the new `craftRecipe` block (with child blocks such as
  `inputs`). B42 also introduces script types with no B41 equivalent,
  including `entity` (buildables) and `fluid` (the fluid registry), while
  `Multistagebuild` is a B41-only block [21].
- **Mod options.** On B41, per-user mod settings required the community
  "Mod Options" framework mod; since B42 the game ships a native
  `PZAPI.ModOptions` Lua API (text entries, tickboxes, comboboxes, color
  pickers, keybinds, sliders, buttons), with a different implementation from
  the B41 framework — options code does not port unchanged [19] [20].
- **Modding API churn within B42.** A security patch in 42.14 removed
  modding API functionality; 42.20 restored it, and TIS asked mod authors to
  report residual compatibility breakage in the official Discord's
  mod-portal channel [1]. Within the 42.20 line, 42.20.4 removed and 42.21
  re-enabled `loadstring` and `loadstream` [32] [34]. Multiplayer returned in unstable 42.13
  (December 2025) with an official forum migration guide for updating
  existing mods to the new networking [14] [7].
- **Documentation surfaces.** The official JavaDoc covers only B41.77; B42
  API truth currently lives in the community stack (Umbrella 42.21.0 stubs,
  unofficial B42 JavaDocs stamped 42.21.0, LuaDocs stamped 42.20.3 on
  2026-10-07) [22] [9] [11] [12].

# Practical Guidance

- **Pick your build deliberately.** New mods should target B42 (42.21
  stable); maintain a B41 variant only if your audience sits on `legacy41`.
  The dual-layout trick — B41 files at the mod root, `common/` + `42/` for
  B42 — lets one Workshop item serve both [17] [4].
- **Set up type-checked Lua from day one.** Install EmmyLua (or LuaLS) in
  your editor and point it at the Umbrella release matching your target game
  version; pin that release by commit hash (the upstream 42.20.0 tag was moved
  after publication) and bump it when the game updates [8] [9] [36].
- **Develop in `Zomboid/Workshop/`, not `Zomboid/mods/`,** so the in-game
  uploader can see your mod, and keep exactly one loaded copy of your Mod ID
  on the machine — unsubscribe from your own published mod while
  developing [17] [24].
- **Answer API questions in tier order:** Umbrella stub → unofficial B42
  JavaDocs → game `media/lua/` and `media/scripts/` files → decompiled Java.
  If a symbol is absent from the JavaDocs, it is not exposed Java [22] [8].
- **Put gameplay-affecting settings in sandbox options, not ModOptions.**
  The wiki's guidance on the B42 API is blunt: mod options are for
  client-side/UI preferences; anything that changes shared game state
  belongs in sandbox options or you will be forced to rework it for
  multiplayer [19].
- **Version your `mod.info` per version folder** and keep heavyweight shared
  assets (models, textures, animations) in `common/` to avoid duplicating
  them across version folders [17] [18].
- **Before publishing:** correct 256×256 `preview.png`, lowercase
  `mod.info`, unique Mod ID, and keep an off-Steam copy of your Workshop
  description because the uploader will overwrite it [17] [18] [24].

# Common Pitfalls & Troubleshooting

- **"My B42 mod doesn't show up in the mod list."** Most commonly a missing
  `common/` folder (mandatory even when empty — at least one `common/` or
  version folder must exist), a `mod.info` left only at the B41 position, or
  wrong folder casing on Linux/macOS [17] [18].
- **"My changes don't appear in-game."** Duplicate copies of the same Mod ID
  (local dev copy + subscribed Workshop copy, or `mods/` + `Workshop/`
  copies) overwrite each other unpredictably [17].
- **"My recipe worked on B41 but not B42."** B41 `Recipe` blocks are not the
  B42 format; recipes must be rewritten as `craftRecipe` [21].
- **"My mod options code from B41 errors on B42."** The B41 Mod Options
  framework and B42's native `PZAPI.ModOptions` are different
  implementations; the API calls do not transfer [19] [20].
- **"It worked on 42.13 but broke later."** Intra-B42 churn is real: the
  42.14 security patch removed API functionality that only returned in
  42.20, and TIS warned that 42.20 changes may affect some mods [1].
- **"A `%` in my translation shows wrong."** Mod translations should write
  `%%` for a literal `%`; the tolerant workaround is temporary [30] [31].
- **"My code calls `loadstring` and fails on some 42.20 builds."** The methods
  were absent on 42.20.4 and are back in 42.21 [32] [34].
- **"A Lua idiom from stock 5.1 misbehaves."** Kahlua is based on Lua 5.1
  with differences; verify against the game, not an external
  interpreter [15] [16].
- **"Subscribers report ghost files after my update."** The Workshop does
  not delete files removed from a new upload; ship emptied files
  instead [24].

# Community Notes & Unverified Claims

## Claim 1 — Kahlua executes Lua noticeably slower than native Lua/LuaJIT, so per-tick mod code must be kept lean

- **Claim:** A long-standing modding-community belief (modding Discord,
  Reddit performance threads) holds that the Java-hosted Kahlua interpreter
  is substantially slower than reference Lua or LuaJIT, making per-tick event
  handlers the main mod performance hazard.
- **Why unverified:** No primary benchmark or dev statement quantifying
  Kahlua's overhead was found; the cited sources establish only that Kahlua
  is a Java implementation based on Lua 5.1 [15].
- **Confidence:** Low. Plausible and widely repeated, but unquantified and
  unsourced to a primary.

# Risks & Caveats

- **Hotfix-wave volatility.** Four hotfixes (42.20.1 to 42.20.4) and one
  incremental update (42.21) followed 42.20.0 within about two months, and
  they changed modding-relevant behaviour (translations, file writing,
  `loadstring`); TIS itself flagged possible mod breakage from 42.20 changes
  [1] [30] [31] [32] [34].
- **Abridged change list.** The retrieved copy of the 42.21 forum notes
  abbreviates the long multiplayer and other fix lists to "selected" items,
  so a modding-relevant change could be missing from this document [35].
- **Wiki lag.** Several structural facts rest on pzwiki pages stamped before
  42.20.0 (Mod structure at 42.14.0, mod.info at 42.17.0, ModOptions at
  42.12.1, LuaDocs at 42.8.1); the layouts are stable but values could have
  moved in late patches [17] [18] [19] [25].
- **Community reference drift.** Umbrella, the unofficial JavaDocs and
  LuaDocs are volunteer-maintained and update on their own cadence — at
  verification LuaDocs trailed at 42.13.0 [12]; ZomboidDoc has had no pushes
  since May 2023 [10].
- **Repository relocation.** The Umbrella repo has moved to a PZ-Umbrella
  GitHub organisation (the asledgehammer URL redirects); pin commits/releases
  rather than trusting URL stability [8] [9]. The 42.20.0 tag was later moved
  upstream to a different commit, so tag names are not stable pins either [9].
- **Announced tooling.** Everything in the WorldZed/TileZed/AnimZed/modding
  guide list is a stated intention, with no shipped artifact to verify [2]
  [28].

# Verification Steps

1. **Build/version:** In Steam, check Project Zomboid's current build and
   confirm the `legacy41` entry under Betas [4]; cross-check the 42.20.0
   release announcement [1] [5] and the 42.21 stable announcement [34].
2. **B41→B42 incompatibility:** Read the "Build 42 Unstable" post's
   Important section for the saves/mods statement [3].
3. **Mod structure:** Create a minimal B42 mod with only a `common/` folder
   and a `42/` folder containing `mod.info` (`id` + `name`); confirm it
   appears in the in-game mod list, then delete `common/` and confirm
   detection still works with the version folder alone (the wiki says at
   least one of the two must exist) [17] [18].
4. **Kahlua:** Grep the installed game's `media/lua/` for engine calls, and
   confirm Kahlua's presence via the pzwiki Lua API description [15] and
   the game's bundled Java (decompile) [22].
5. **API truth:** Download the Umbrella release tagged 42.21.0 (commit
   `13d01f9ee58fa48773553920db56d06f0005e7f8`) [9] [36], point
   EmmyLua at its `library/` folder [8], and confirm intellisense resolves a
   known game class; spot-check the same class in the unofficial B42
   JavaDocs [11].
6. **ModOptions:** Open the installed B42 game's
   `media/lua/client/PZAPI/ModOptions.lua` and confirm the create API
   matches [19].
7. **Pending tools:** Search Spiffo's Workshop and the official site for
   WorldZed/AnimZed releases; as of 2026-10-07 no official post reviewed
   announces them as released, only the plans [2] [28] [25].

# Open Questions

- When will the official modding guide, WorldZed/TileZed and AnimZed
  actually ship (still open on 2026-10-07), and will AnimZed's release change
  the animation-modding workflow documented by the community? [2] [28]
- What exactly did the 42.14 security patch remove and the 42.20 fix
  restore, in API-surface terms? A deeper Modders document should diff the
  Umbrella stubs between 42.13/42.14/42.20 releases [1] [9].
- Will the promised "additional Modding API documentation" [1] become an
  authoritative replacement for the community JavaDocs/stubs stack, and on
  what timeline?
- Does B42.20 change any `mod.info` parameter semantics beyond what the
  42.17-stamped wiki page records? [18]
- Resolved: the Build 42 Support Update is a primary-sourced plan for the rest
  of 2026 [28] [29]; what it will contain beyond "optimization, additional
  modding support" is open.
- Which situations trigger the 42.21 `RuntimeException` for missing
  translations, and what does the localization-system update change for mod
  authors? [35]

# References

**Primary Sources** — official blog/announcements, dev-posted docs, code-truth repositories.

- [1] **The Indie Stone** — *PROJECT ZOMBOID BUILD 42.20 RELEASED!* (29 July 2026). https://projectzomboid.com/blog/news/2026/07/project-zomboid-build-42-20-released/ — verified via the Steam news mirror [5]. Accessed 2026-07-30.
- [2] **The Indie Stone** — *NEXT STEPS* (July 2026). https://projectzomboid.com/blog/news/2026/07/next-steps-2/ — verified via the Steam news mirror [5]. Accessed 2026-07-30.
- [3] **The Indie Stone** — *Build 42 Unstable* (17 December 2024). https://projectzomboid.com/blog/news/2024/12/build-42-unstable/ — text verified via Internet Archive snapshot 20251230222720. Accessed 2026-07-30.
- [4] **The Indie Stone** — *B42 CHECKLIST* (Steam Community announcement, 28 July 2026). https://steamcommunity.com/ogg/108600/announcements/detail/674001285755702334 — verified via the Steam news mirror [5]. Accessed 2026-07-30.
- [5] **Valve** — *Steam News Web API (ISteamNews), app 108600* (mirror of official announcements). https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=15&maxlength=0 Accessed 2026-07-30.
- [6] **The Indie Stone** — *Modding Policy*. https://projectzomboid.com/blog/modding-policy/ Accessed 2026-07-30 (host bot-blocks checkers; policy terms corroborated by [14]).
- [7] **The Indie Stone Forums** — *Modding migration guide 42.13* (December 2025). https://theindiestone.com/forums/index.php?/topic/88499-modding-migration-guide-4213/ Accessed 2026-07-30 (host bot-blocks checkers; existence corroborated by [14]).
- [8] **PZ-Umbrella project (asledgehammer)** — *Umbrella: EmmyLua type stubs for Project Zomboid's modding API* (repository README). https://github.com/asledgehammer/Umbrella Accessed 2026-07-30.
- [9] **PZ-Umbrella project** — *Umbrella releases* (per-game-version release tags 41.78.16 – 42.21.0; 42.20.0 published 2026-07-29, 42.21.0 published 2026-09-28). https://github.com/PZ-Umbrella/Umbrella/releases Accessed 2026-07-30 and 2026-10-07.
- [10] **cocolabs** — *pz-zdoc (ZomboidDoc): Lua library compiler for Project Zomboid* (repository; GPL-3.0; last push 2023-05-13). https://github.com/cocolabs/pz-zdoc Accessed 2026-07-30.
- [11] **Albion** — *Unofficial PZ JavaDocs (Build 42)* (site header stated 42.20.0 on 2026-07-30 and 42.21.0 on 2026-10-07). https://albion.codeberg.page/PZ-JavaDocs/ Accessed 2026-07-30 and 2026-10-07.
- [12] **demiurgeQuantified** — *Project Zomboid LuaDocs* (site stated version 42.13.0 on 2026-07-30 and 42.20.3 on 2026-10-07; WIP, inference-based). https://demiurgequantified.github.io/ProjectZomboidLuaDocs/ Accessed 2026-07-30 and 2026-10-07.
- [13] **Lua.org** — *Lua 5.1 Reference Manual*. https://www.lua.org/manual/5.1/ Accessed 2026-07-30.
- [28] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-24; the Steam title differs from the blog title "NEXT STEPS" cited at [2], and the two were not confirmed to be the same text). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453 Accessed 2026-10-07 (host bot-blocks checkers).
- [29] **The Indie Stone** — *NEXT STEPS* (Steam announcement, 2026-07-09). https://steamcommunity.com/games/108600/announcements/detail/1836506165584147 Accessed 2026-10-07 (host bot-blocks checkers).
- [30] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766 Accessed 2026-10-07 (host bot-blocks checkers).
- [31] **The Indie Stone** — *42.20.2 STABLE Hotfix Released* (Steam announcement, 2026-08-05). https://steamcommunity.com/games/108600/announcements/detail/1840310314339441 Accessed 2026-10-07 (host bot-blocks checkers).
- [32] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601 Accessed 2026-10-07 (host bot-blocks checkers).
- [33] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925 Accessed 2026-10-07 (host bot-blocks checkers).
- [34] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07 (host bot-blocks checkers).
- [35] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first post, 2026-09-23; the long fix lists are abridged to "selected" in the retrieved copy). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 (host bot-blocks checkers).
- [36] **PZ-Umbrella project** — *Umbrella at commit 13d01f9ee58fa48773553920db56d06f0005e7f8 (release tag 42.21.0)*. https://github.com/PZ-Umbrella/Umbrella/tree/13d01f9ee58fa48773553920db56d06f0005e7f8 Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cited URL + revision id; facts only, never prose.

- [14] **PZwiki** — *Modding* (revision 1443699, page version 42.20.0). https://pzwiki.net/wiki/Modding Accessed 2026-07-30. Fact-only source.
- [15] **PZwiki** — *Lua (API)* (revision 1390433). https://pzwiki.net/wiki/Lua_(API) Accessed 2026-07-30. Fact-only source.
- [16] **PZwiki** — *Lua (language)* (revision 1390437). https://pzwiki.net/wiki/Lua_(language) Accessed 2026-07-30. Fact-only source.
- [17] **PZwiki** — *Mod structure* (revision 1443271, page version 42.14.0). https://pzwiki.net/wiki/Mod_structure Accessed 2026-07-30. Fact-only source.
- [18] **PZwiki** — *mod.info* (revision 1363935, page version 42.17.0). https://pzwiki.net/wiki/Mod.info Accessed 2026-07-30. Fact-only source.
- [19] **PZwiki** — *ModOptions* (revision 1391013, page version 42.12.1). https://pzwiki.net/wiki/ModOptions Accessed 2026-07-30. Fact-only source.
- [20] **PZwiki** — *Mod Options* (revision 1370001). https://pzwiki.net/wiki/Mod_Options Accessed 2026-07-30. Fact-only source.
- [21] **PZwiki** — *Scripts* (revision 1442815, page version 42.17.0). https://pzwiki.net/wiki/Scripts Accessed 2026-07-30. Fact-only source.
- [22] **PZwiki** — *JavaDocs* (revision 1389757, page version 42.17.0). https://pzwiki.net/wiki/JavaDocs Accessed 2026-07-30. Fact-only source.
- [23] **PZwiki** — *Unofficial JavaDocs (Build 42)* (revision 1443597, page version 42.20.0). https://pzwiki.net/wiki/Unofficial_JavaDocs_(Build_42) Accessed 2026-07-30. Fact-only source.
- [24] **PZwiki** — *Uploading mods* (revision 1442321, page version 42.15.0). https://pzwiki.net/wiki/Uploading_mods Accessed 2026-07-30. Fact-only source.
- [25] **PZwiki** — *Mapping tools (official)* (revision 1390645) and *LuaDocs* (revision 1390445). https://pzwiki.net/wiki/Mapping_tools_(official) and https://pzwiki.net/wiki/LuaDocs Accessed 2026-07-30. Fact-only sources.
- [26] **PZwiki** — *Spiffo's Workshop* (revision 1393671, page version 42.11.0). https://pzwiki.net/wiki/Spiffo%27s_Workshop Accessed 2026-07-30. Fact-only source.
- [27] **PZwiki** — *Build 42* (revision 1443663; unstable 2024-12-17, stable 2026-07-29). https://pzwiki.net/wiki/Build_42 Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — none used for factual claims in this document.

**Community & Creator** — none.

**Further Reading** — see the Further Reading section.

# Further Reading

- Albion's PZ Modding Guides collection (community guides and documentation):
  https://github.com/demiurgeQuantified/PZModdingGuides
- The Indie Stone official Discord (Workshop category for modding help):
  https://discord.gg/theindiestone
- Alternative B42 JavaDocs with source viewer:
  https://geromet.github.io/PZJavaDocs/

# Related Documents

- players-foundation — the Players-track foundation (game-side mechanics
  this track's mods manipulate).
- admins-foundation — the Admins-track foundation (server-side mod
  deployment and Workshop IDs in server config).
- creator-foundation — the Creator-track foundation (mod showcases and
  content production).
- lore-foundation — the Lore-track foundation (setting constraints for
  lore-friendly mods).
- meta-style-guide — how documents in this knowledge base are written and
  gated.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-07-30 | Orchestrator (KB Pipeline) | Approved and frozen — foundation cluster release kb-release-2026.07.30. | Standing mandate (2026-07-30) |
| 1.0.1 | 2026-07-30 | Orchestrator (KB Pipeline) | License-hygiene prose rewrites after arming the pzwiki n-gram gate (no factual changes). | Standing mandate (2026-07-30) |
| 1.1.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined from 42.20 to 42.21 (factual update to an approved document; status stays approved pending orchestrator re-approval): current stable 42.21, Umbrella 42.21.0, JavaDocs/LuaDocs stamps, added 42.20.1-42.21 modding changes (`%%`, .json writes, localization, anti-cheat, loadstring/loadstream removed then re-enabled), refreshed Announced-but-not-shipped as of 2026-10-07, resolved the Support Update claim from Steam primary posts (former Claim 1 removed, former Claim 2 renumbered). Sources: Steam posts 42.20.1, 42.20.2, 42.20.4, 42.21 unstable and stable, NEXT STEPS, BUILD 42 STABLE PLANS, TIS forum 42.21 notes. | Project owner (user instruction 2026-10-08) |
