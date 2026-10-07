---
id: modders-modoptions-pzapi
title: "PZAPI.ModOptions and the B42 Mod Settings API: Building an Options Screen"
version: 0.1.0
status: in-review
confidence: Medium
category: Modders
topic: "ModOptions & PZAPI"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-05
sources_verified: 2026-10-07
supersedes: null
related: [modders-foundation, modders-lua-api-surface, modders-events-callbacks, modders-mp-networking-porting, modders-modinfo-modid-conventions, modders-first-mod-tutorial-b42, modders-porting-b41-to-b42, admins-workshop-mod-wiring, meta-style-guide]
tags: [modding, lua, pzapi, modoptions, options, keybind, ui, b42]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | modders-modoptions-pzapi |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Modders |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-05 |
| Game versions verified | 41.78.16 (Umbrella index), 42.20.0 (Umbrella stubs) |

# Executive Summary

Build 42 ships a native mod-settings API: `PZAPI.ModOptions`. A mod calls `create` once to obtain an options section, then adds typed controls to it (tick box, multiple tick box, combo box, slider, text entry, colour picker, key bind, button) plus three layout helpers (title, description, separator). The stubs pinned at Umbrella 42.20.0 describe the whole surface, including the exact `add*` signatures and the `load` / `save` pair that persists values to a `ModOptions.ini` file [1].

Build 41 has no such API. The B41 Umbrella pin (41.78.16) contains no `PZAPI` or ModOptions library file, so everything here marked *(B42)* simply does not exist on `legacy41` [3]. The B41 world used a community framework mod named "Mod Options", which the wiki describes as a separate implementation; code does not port unchanged [11] [10].

Confidence is Medium. The signatures are stub-sourced (strong), but the file location, several bug reports and the call-order semantics of `onChange` versus `onChangeApply` rest on a pzwiki page last updated for 42.12.1, and nothing was run in-game. This document was verified against 42.20.0 stubs only: Build 42.21 went stable on 2026-09-28 and 41.78.21 shipped on 2026-08-26 [5] [6].

# Key Takeaways

- `PZAPI.ModOptions` is a *(B42)*-only API; the B41 pin has no such library file. *(cited)* *(B42)* [1] [3]
- Entry point is `create(modOptionsID, name)`; the returned options object exposes eleven `add*` methods. *(cited)* *(B42)* [1]
- Reads go through `getValue()` on an option object, fetched either from a cached local or via `getOption(id)`; the MultipleTickBox takes an index. *(cited)* *(B42)* [1] [10]
- Values persist through `PZAPI.ModOptions:load()` and `PZAPI.ModOptions:save()` into an ini file under the user cache folder. *(cited)* *(B42)* [1] [10]
- Key binds are stored as key codes; detecting presses is done by comparing the pressed key against the option value inside an `Events.OnKeyPressed` handler. *(cited)* *(both)* [10]
- Mod options are for client-side preferences only; gameplay-affecting settings belong in sandbox options. *(cited)* [10] [11]
- Two persistence/robustness fixes landed during the B42 unstable cycle (saving, empty text entries). *(cited)* *(B42)* [7] [8]
- The button `arg4` bug, the ini filename case and B41 framework details are quarantined below. *(community, unverified)*

# Purpose

This document answers one question for a modder: how do I give my mod a settings screen, read the values safely, and know what changes between Build 41 and Build 42? It goes deeper on the one-line `PZAPI.ModOptions` mention in the foundation document and assumes its vocabulary.

# Scope

Covered: the `PZAPI.ModOptions` library as defined in the Umbrella 42.20.0 stubs, every option type and its `add*` signature, value access, persistence, change callbacks, key-bind handling, the `PZAPI.UI` namespace as it appears in the same stubs, and a verified minimal example. Also covered: the B41 situation, limited to what is primary-sourceable.

Not covered: the Lua client option screens of the base game, translation-file layout, sandbox options (server-controlled settings), and unstable branches after 42.20.0. Networking and multiplayer sync belong to the MP porting document.

# Definitions

- **Options section** — the object returned by `PZAPI.ModOptions:create`; one per `modOptionsID`, rendered as a named section in the game options [1] [10].
- **Option object** — the table returned by an `add*` call; its `type` field is a string tag such as `tickbox` or `slider` [1].
- **modOptionsID** — the unique string identifying a section [1].
- **Layout element** — a title, description or separator; these are entries in the section's data list but have no value [1].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | No native API | Umbrella 41.78.16 pin (library tree contains no PZAPI/ModOptions file) [3] | Community "Mod Options" framework only [11] |
| B42 (stable) | Yes | Umbrella 42.20.0 stubs [1]; game 42.20.0 released 2026-07-29 [4] | Not re-run in-game |

Build 42.21 went stable on 2026-09-28 [5] and the legacy line reached 41.78.21 on 2026-08-26 [6]. This document is verified against the 42.20.0 stubs only; no 42.21 stub release was checked, and the 42.21 stable announcement text contains no mention of mod options [5]. Re-verify before relying on any signature for 42.21.

# Reference

## Namespace and entry points

The stub declares a global `PZAPI` table whose `ModOptions` field is typed as the `PZAPI.ModOptions` module [1]. The module defines four fields and four functions: `Data` (list of all options sections), `Dict` (sections keyed by ID), `OtherOptions`, and `Options` (the options class), plus `create`, `getOptions`, `load` and `save` [1].

| Function | Signature (from stub) | Purpose |
|----------|-----------------------|---------|
| `PZAPI.ModOptions:create` | `create(modOptionsID, name)`; `name` optional, defaults to the ID | Creates a section and returns it [1] |
| `PZAPI.ModOptions:getOptions` | `getOptions(modOptionsID)` | Returns an existing section or nil [1] |
| `PZAPI.ModOptions:load` | `load()` | Loads all mod options from ModOptions.ini [1] |
| `PZAPI.ModOptions:save` | `save()` | Saves all mod options to ModOptions.ini [1] |

The wiki adds that because `getOptions` can reach any section, an addon mod may append controls to another mod's section [10].

## The options-section object

A section carries `data` (array of every element including layout elements), `dict` (options keyed by ID), `modOptionsID` and `name` [1]. It also exposes `getOption(id)`, which returns the option or nil, and `apply()`, documented in the stub as a placeholder function [1]. The wiki describes assigning your own function to `apply` as the hook for reacting to changed settings [10].

## Option types and add* signatures

All signatures below are quoted from the 42.20.0 stub [1]. Parameters prefixed with an underscore are optional tooltips in the stub.

| Type tag | Method | Signature | Value accessors |
|----------|--------|-----------|-----------------|
| `tickbox` | `addTickBox` | `(id, name, value, _tooltip)`, `value` boolean | `getValue()`, `setValue(value)` [1] |
| `multipletickbox` | `addMultipleTickBox` | `(id, name, _tooltip)`; entries added with `addTickBox(name, value)` | `getValue(index)`, `setValue(index, value)`, `setEnabled(optionName, value)` [1] |
| `combobox` | `addComboBox` | `(id, name, _tooltip)`; entries added with `addItem(name, selected)` | `getValue()` returns an integer index, `setValue(index)` [1] |
| `slider` | `addSlider` | `id` and `name`, then `min`, `max`, `step`, the starting `value`, and an optional tooltip | `getValue()`, `setValue(value)` [1] |
| `textentry` | `addTextEntry` | `(id, name, value, _tooltip)`, `value` string | `getValue()`, `setValue(value)` [1] |
| `colorpicker` | `addColorPicker` | `id` and `name`, then four colour components `r`, `g`, `b`, `a` (each 0 to 1), and an optional tooltip | `getValue()` and `setValue()` use an RGBA table [1] |
| `keybind` | `addKeyBind` | `(id, name, key, _tooltip)`, `key` an integer key code | `getValue()`, `setValue(value)`; also fields `key`, `defaultkey` [1] |
| `button` | `addButton` | `id`, `name`, `tooltip`, then the click function `onclickfunc`, a `target`, and up to four extra arguments `arg1` to `arg4` | no value; fields `onclick`, `target`, `args` [1] |
| `title` | `addTitle` | `(name)` | none [1] |
| `description` | `addDescription` | `(text)`; the stub says the text is processed by `getText` | none [1] |
| `separator` | `addSeparator` | `()` | none [1] |

Every value-bearing option also inherits `id`, `name`, `tooltip`, `element` and `setEnabled(bool)` from a shared base type, except the multiple tick box which overrides `setEnabled` with a two-argument form [1].

## Change callbacks

The tick box, multiple tick box, combo box, colour picker, slider and text entry each declare optional `onChange` and `onChangeApply` function fields in the stub [1]. Their declared argument lists are: tick box `(option, selected)`; multiple tick box `(option, index, selected)`; combo box `(option, selected)` with an integer index; colour picker `(option, color)`; slider `(option, value)`; text entry `(option, text)` [1]. The stub does not state when each callback fires relative to the other [1]; see Open Questions.

The button's click handler is the `onclickfunc` parameter, stored as `onclick`; the wiki documents it as called with the target first and the button object second, followed by the extra arguments [10].

## Key-bind handling

The key bind option stores an integer key code and its element is a subtype of the base game's key-text widget flagged `isModBind` [1]. The wiki's documented pattern is to cache or look up the option and compare the key number passed to an `Events.OnKeyPressed` handler against the option's `getValue()` result; the sibling events `Events.OnKeyStartPressed` and `Events.OnKeyKeepPressed` are listed alongside [10]. The wiki also recommends passing an already-translated string through `getText` as the key bind's `name`, citing a bug in how mod key binds are identified as of 42.13.3 [10].

## Persistence

The stub states that `load` and `save` read and write a file called ModOptions.ini [1]. The wiki places it in the user cache folder under `Lua/` [10]. The 42.3.0 unstable notes list "Fixed modOptions not saving" [8], and the 42.13.0 notes list fixes for an empty text entry blocking the menu and for mod options passing nil for an empty text field (an empty value is replaced by a single space) [7].

## The PZAPI.UI namespace

The same stub tree defines `PZAPI.UI` and `PZAPI.UI.Extensions`; in the extracted index the former lists only underscore-prefixed internal helpers, and the latter lists `Mouse` and `Scroll` [1] [2]. The Umbrella tree holds widget files under `PZAPI/ui` (atoms, molecules and organisms directories) [2]. This document does not treat `PZAPI.UI` as a mod-settings facility; its use for custom windows is out of scope.

## Minimal verified example

Every API name in this example appears in the 42.20.0 stub or the pinned event list [1]. It follows the wiki's documented access patterns [10]. It has not been run in-game.

```lua
-- media/lua/client/MyMod_Options.lua  (B42 only)
local options = PZAPI.ModOptions:create("MyModOptions", "My Mod")

options:addTitle("Overlay")
options:addDescription("Client-side display preferences only.")

local showOverlay = options:addTickBox("showOverlay", "Show overlay", true, "Toggles the overlay")
local scale = options:addSlider("overlayScale", "Overlay scale", 0.5, 2, 0.1, 1)

local mode = options:addComboBox("overlayMode", "Mode")
mode:addItem("Compact", true)
mode:addItem("Detailed")

options:addSeparator()
local toggleKey = options:addKeyBind("toggleKey", "Toggle overlay", Keyboard.KEY_H)

local cached = {}
options.apply = function(self)
    cached.show = showOverlay:getValue()
    cached.scale = scale:getValue()
    cached.mode = mode:getValue()
end

Events.OnMainMenuEnter.Add(function() options:apply() end)

Events.OnKeyPressed.Add(function(key)
    if key == toggleKey:getValue() then
        cached.show = not cached.show
    end
end)
```

# B41 vs B42 Delta

- **Native API.** *(B42)* `PZAPI.ModOptions` with `create`, `getOptions`, `load` and `save` is defined in the 42.20.0 stubs [1]. The B41 pin 41.78.16 contains no PZAPI or ModOptions library path, and the extracted B41 index has no `PZAPI` class [3].
- **Predecessor.** On B41 the wiki says the options facility was an unofficial framework mod called "Mod Options", and that Build 42 now has the feature natively but with a different implementation [11] [10].
- **Porting consequence.** Option-definition code written against the B41 framework must be rewritten for the native API; there is no documented compatibility shim [10] [11].
- **Layout of the call.** *(B42)* Options are added with method-call syntax on the object returned by `create`, and values are read with `getValue()` on the returned option objects [1].
- **Events.** `Events.OnKeyPressed`, `Events.OnKeyStartPressed`, `Events.OnKeyKeepPressed` and `Events.OnMainMenuEnter` exist in both index files, so the key-handling half of a key-bind implementation is portable even though the option-definition half is not [1] [3].
- **Fixes within B42.** Saving was fixed in 42.3.0 unstable [8] and empty text-entry handling in 42.13.0 unstable [7]; both fixes predate 42.20.0 [4].
- **Security patch.** The 42.20.4 hotfix removed the `loadstring` and `loadstream` methods; mods that used those should be updated [6].

# Practical Guidance

- **Create the section at file load time** in `media/lua/client/`, not inside an event, so it exists when the options screen builds [1] [10].
- **Use a unique ID.** The section ID and each option ID are lookup keys in `dict`; collisions with another mod's section would address its data [1] [10].
- **Cache values in `apply`**, as in the example, rather than calling `getOption` every tick [1] [10].
- **Keep gameplay out of ModOptions.** Anything that changes shared state belongs in sandbox options [10] [11].
- **Guard for B41.** If one Workshop item serves both builds, put the options file in the B42 version folder, or test that `PZAPI` is non-nil before use; the B41 pin has no such table [3].
- **Prefer translated names.** Pass `getText`-resolved names to key binds per the wiki's workaround [10].
- **Validate empty text.** An empty text entry is substituted with a single space in 42.13.0 and later, so trim before testing for empty [7].

# Common Pitfalls & Troubleshooting

- **"PZAPI is nil."** You are running on B41 or on an old B42 build; the B41 pin has no PZAPI [3].
- **"My combo box returns a number."** `getValue()` on a combo box is an integer index; map it to your own list [1].
- **"Multiple tick box getValue errors."** It takes an index argument, unlike the single tick box [1].
- **"Colour values look wrong."** Colour components are 0 to 1 in the stub, not 0 to 255 [1].
- **"Settings do not persist."** Check you are on 42.3.0 or later [8], and see the ini discussion in Claim 2.
- **"Key bind not firing."** The key bind holds a key code; your `Events.OnKeyPressed` handler must compare against `getValue()` [10].
- **"Server value overridden by a client option."** Gameplay-affecting options belong in sandbox options [10].

# Community Notes & Unverified Claims

## Claim 1 — The fourth extra argument of a mod-options button is passed as the third

- **Claim:** The pzwiki ModOptions page states that on 42.10.0 the `onclickfunc` receives its arguments shifted, so `arg4` arrives where `arg3` should be, and links a bug report.
- **Why unverified:** The linked bug report was not opened and the behaviour was not tested on 42.20.0; the stub gives no hint of it [1].
- **Confidence:** Low. A single wiki sentence about a 42.10.0 observation, with no confirmation it still applies.

## Claim 2 — The ini file is named `modOptions.ini` in `<cache>/Lua/`

- **Claim:** The pzwiki page gives the file as `modOptions.ini` under the cache `Lua` folder, while the Umbrella stub text says `ModOptions.ini` [1] [10].
- **Why unverified:** The two sources differ in letter case, and the exact directory was not confirmed on a running install; Windows ignores case but Linux does not.
- **Confidence:** Low. Directory is wiki-only and case is contradicted by the stub.

## Claim 3 — The B41 "Mod Options" framework exposes a global ModOptions table with its own instance and settings-table pattern

- **Claim:** Modding-community lore describes the B41 framework mod as a global `ModOptions`-style object with settings tables mapped to UI, with a separate Workshop page and guide.
- **Why unverified:** No primary source for its API was fetched; only the wiki's one-paragraph description of its existence was available [11], and the Workshop page was not read.
- **Confidence:** Low. Recollection and secondary description only; do not code against it from this document.

# Risks & Caveats

- Stubs are community-written type annotations, not the game's own source; the file path the wiki quotes (`media/lua/client/PZAPI/ModOptions.lua`) should be opened in an install to confirm the stub [1] [10].
- The wiki page is stamped 42.12.1 and warns it may be inaccurate for 42.20.0; its example snippets were retrieved from 42.0.2 source [10].
- No 42.21 stub release was checked [5].
- The stub's `apply` is documented as a placeholder, so how the game triggers a user-supplied `apply` is wiki-sourced only [1] [10].
- The B41 absence rests on a path search of the pinned tree and the extracted index; there is no positive statement from the developers [3].

# Verification Steps

1. Open `media/lua/client/PZAPI/ModOptions.lua` in a 42.20.x install and compare each `add*` signature with the table above [1] [10].
2. Download the Umbrella 42.20.0 release and open `library/lua/client/PZAPI/ModOptions.lua` [1].
3. Browse the B41 pin's `library` tree and confirm no `PZAPI` folder [3].
4. Run the minimal example on B42, change a value, exit, and inspect `ModOptions.ini` in the cache folder to settle Claim 2.
5. Press the mod key bind with the overlay example and log `key` to confirm the comparison pattern [10].
6. Run `python scripts/check_api_exists.py docs/modders/modders-modoptions-pzapi.md` against the pinned indexes.

# Open Questions

- What are the timing and ordering semantics of `onChange` versus `onChangeApply`? The stub gives signatures only [1].
- Does the base game call `apply` on a user-assigned section function, and when? [1] [10]
- Is the ini filename `ModOptions.ini` or `modOptions.ini`, and in which folder? (Claim 2)
- Is the button `arg4` shift still present on 42.20.0? (Claim 1)
- Did 42.21 change any ModOptions behaviour? The announcement text mentions none [5], but the forum patch notes were not read.

# References

**Primary Sources** — Umbrella stubs at pinned commits, Steam announcements.

- [1] **PZ-Umbrella** — *library/lua/client/PZAPI/ModOptions.lua at commit 58204fc (release 42.20.0)*. https://github.com/PZ-Umbrella/Umbrella/blob/58204fc47895ba249592519cedecc7cfbaaebd60/library/lua/client/PZAPI/ModOptions.lua Accessed 2026-10-07.
- [2] **PZ-Umbrella** — *library/lua/client/PZAPI/ui at commit 58204fc (release 42.20.0)*. https://github.com/PZ-Umbrella/Umbrella/tree/58204fc47895ba249592519cedecc7cfbaaebd60/library/lua/client/PZAPI/ui Accessed 2026-10-07.
- [3] **PZ-Umbrella** — *library tree at commit fa2e7e1 (release 41.78.16)*. https://github.com/PZ-Umbrella/Umbrella/tree/fa2e7e19799740b57902f1cb4e989225c295c05e/library Accessed 2026-10-07.
- [4] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/ogg/108600/announcements/detail/1839676055882259 Accessed 2026-10-07 (host bot-blocks checkers; located via the Steam news API [9]).
- [5] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/ogg/108600/announcements/detail/1844751498231307 Accessed 2026-10-07.
- [6] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/ogg/108600/announcements/detail/1842212951296601 Accessed 2026-10-07.
- [7] **The Indie Stone** — *Build 42.13.0 UNSTABLE Multiplayer Released* (Steam announcement). https://steamcommunity.com/ogg/108600/announcements/detail/1818752592122972 Accessed 2026-10-07.
- [8] **The Indie Stone** — *42.3.0 UNSTABLE Released* (Steam announcement). https://steamcommunity.com/ogg/108600/announcements/detail/1790848102789684 Accessed 2026-10-07.
- [9] **Valve** — *Steam News Web API (ISteamNews), app 108600*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=200&maxlength=0 Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): URL + revision id; facts only.

- [10] **PZwiki** — *ModOptions* (revision 1391013, page version 42.12.1). https://pzwiki.net/wiki/ModOptions Accessed 2026-10-07. Fact-only source.
- [11] **PZwiki** — *Mod Options* (revision 1370001, page version 41.78.19). https://pzwiki.net/wiki/Mod_Options Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating** — none.

**Community & Creator** — none.

**Further Reading** — see the Further Reading section.

# Further Reading

- Unofficial B42 JavaDocs: https://albion.codeberg.page/PZ-JavaDocs/
- PZ-Wiki-Modding API docs site: https://pz-wiki-modding.github.io/PZ-API-Docs/

# Related Documents

- modders-foundation — ecosystem, toolchain and where API truth lives.
- modders-lua-api-surface — the wider Lua API surface.
- modders-events-callbacks — events used for key handling.
- modders-mp-networking-porting — why gameplay settings must not live in client options.
- modders-modinfo-modid-conventions — Mod ID hygiene for unique option IDs.
- modders-first-mod-tutorial-b42 — a first B42 mod, where an options screen can be added.
- modders-porting-b41-to-b42 — porting checklist.
- admins-workshop-mod-wiring — server-side mod setup.
- meta-style-guide — how documents are written and gated.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
