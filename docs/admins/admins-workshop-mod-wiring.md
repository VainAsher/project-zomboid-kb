---
id: admins-workshop-mod-wiring
title: "Wiring Workshop Mods into a Server: IDs, Load Order and Updates"
version: 0.2.0
status: in-review
confidence: Medium
category: Admins
topic: "Server operations"
build: both
document_type: reference
created: 2026-07-31
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [admins-foundation, admins-server-ini-reference, modders-foundation, meta-style-guide]
tags: [workshop, mods, mod-id, workshop-id, load-order, server-ini, updates, b42, legacy41]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-workshop-mod-wiring |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Admins |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 |

# Executive Summary

This document is the mechanical reference for how Steam Workshop mods get
wired into a Project Zomboid dedicated server's configuration: the two ID
systems involved (Workshop ID and Mod ID), the paired `server.ini` keys that
carry them (`WorkshopItems=` and `Mods=`), the `mod.info` fields that actually
control dependency and load order (`require`, `incompatible`, `loadModAfter`,
`loadModBefore`), and what is and is not documented about how updates reach a
running server. It goes one level below `admins-foundation`'s "mod wiring
basics" subsection and the mod-list rows in `admins-server-ini-reference`,
which both point here for depth.

The load-bearing finding of this document is a gap: pzwiki's `Server settings`
page documents `WorkshopItems=` with an explicit semicolon-separated example,
but documents `Mods=` with no separator example at all [3]. Separately,
`mod.info` itself — not the `server.ini` list order — is where dependency and
load-order control is actually documented, via the `require`, `incompatible`,
`loadModAfter` and `loadModBefore` parameters generated directly from the
game's own script/Lua/Java data by the community ScriptsDocs project [2] [5].
The popular belief that the *position* of a Mod ID inside the `Mods=` line
itself governs load order, and the popular claim that Build 42 requires a
backslash before each `Mods=` entry, are both quarantined below: neither is
confirmed by a primary or fact-only source, and the pinned wiki revision
positively shows a `Mods=` example with no backslash [3] [12] [13] [14].

Document-level confidence is **Medium**: the ID-system and key-pairing facts
rest on pinned pzwiki revisions and a code-truth-generated documentation
project (High for what they document), but the two questions server admins
most want answered — does `Mods=` list order matter, and does the server
process itself keep Workshop content current without admin intervention — are
not settled by any primary source found, and are quarantined rather than
asserted.

# Key Takeaways

- **Workshop ID** (the numeric Steam Workshop item ID) and **Mod ID** (the
  `id` field in that item's `mod.info`) are different identifiers for
  different things; one Workshop item can contain several Mod IDs *(cited)*
  *(both)*
- `WorkshopItems=` takes semicolon-separated Workshop IDs with a documented
  example (`514427485;513111049`); `Mods=` takes the paired Mod IDs but the
  pinned wiki revision gives **no separator example** for that key *(cited)*
  *(both)*
- The actual documented dependency/load-order mechanism is inside `mod.info`,
  not `server.ini`: `require=` (comma-separated required Mod IDs),
  `incompatible=` (comma-separated mutually-exclusive Mod IDs),
  `loadModAfter=` and `loadModBefore=` (comma-separated Mod IDs this mod must
  load after/before) *(cited)* *(both, current wiki/ScriptsDocs revisions)*
- A mod missing one of its `require=` dependencies shows up **red** in the
  in-game mod list — this is the documented symptom, not a server log
  message *(cited)* *(both)*
- Whether the **position** of a Mod ID inside the `Mods=` line itself
  determines load/override order is **not documented** by any primary or
  fact-only source found; it is a widely circulated hosting-KB claim,
  quarantined below *(community, unverified)*
- The claim that Build 42 requires a leading backslash on each `Mods=` entry
  conflicts with the pinned wiki example and is quarantined — this document
  reaches the same conclusion as `admins-foundation`'s Claim 2 independently
  *(community, unverified)*
- A community support thread's server log excerpt (`Workshop:
  onItemQueryCompleted`) shows the dedicated server process itself queries
  Steam Workshop when `WorkshopItems=` is populated — the server does not
  merely wait for clients to fetch mods — but no primary source confirms
  whether this re-checks for author updates on every subsequent restart
  *(cited / community, unverified)*
- There is no documented mechanism to pin a `WorkshopItems=` entry to an
  older file revision; a Workshop ID always resolves to the item's current
  published version. The only documented route to a frozen mod copy is the
  separate manual-install path (`Zomboid/mods/`), which this document
  describes as a practical, but not officially named, "pinning" workaround
  *(cited synthesis)* *(both)*

# Purpose

An admin who has already read `admins-foundation`'s mod-wiring basics and
`admins-server-ini-reference`'s `Mods`/`WorkshopItems` table rows still faces
concrete mechanical questions: which ID goes in which key, what actually
decides load order when several mods touch the same content, what happens
when a required mod is missing, and whether a mod update on the Workshop
reaches a running server automatically or needs manual action. This document
answers those questions to the depth the evidence supports, and says so
plainly wherever the evidence runs out.

# Scope

Covered: the Workshop ID vs. Mod ID distinction; the `WorkshopItems=`/`Mods=`
pairing and its documented (and undocumented) syntax; the `mod.info`
dependency and load-order fields (`require`, `incompatible`, `loadModAfter`,
`loadModBefore`); the documented in-game symptom of a missing dependency;
what is and is not documented about Workshop auto-download/auto-update
interacting with a running dedicated server; and whether a mod version can be
pinned/frozen against upstream Workshop updates.

Not covered: the operational process of choosing, staging and rolling out
mods on a live community server — that is `admins-modded-server-runbook`;
Ubuntu/systemd process supervision — `admins-ubuntu-runbook`; the full
`server.ini` key-by-key reference and general (non-mod) settings —
`admins-server-ini-reference`; the B42 mod folder anatomy
(`common/`/version folders), the Kahlua Lua environment, and Workshop
publishing from the mod-author's side — all owned by `modders-foundation`,
linked to rather than repeated here. Unstable-branch behaviour after 42.20 is
out of scope.

# Definitions

- **Workshop ID** — the numeric identifier Steam assigns to a published
  Workshop item; used in `WorkshopItems=` and to fetch the item via
  SteamCMD or the in-game Workshop UI [7].
- **Mod ID** — the `id` parameter inside a mod's `mod.info`; the identifier
  the game itself loads, used in `Mods=`. One Workshop item's `Contents/`
  folder can hold more than one Mod ID [7] [5].
- **`require=`** — a `mod.info` field listing, comma-separated, the Mod IDs
  this mod needs to run [2] [5].
- **`incompatible=`** — a `mod.info` field listing, comma-separated, Mod IDs
  that cannot be enabled at the same time as this mod [2].
- **`loadModAfter=` / `loadModBefore=`** — `mod.info` fields that force this
  mod to load after/before the comma-separated Mod IDs listed [2].
- **Soft override** — the game's mechanism for merging or replacing a script
  block (e.g. an `item` or `craftRecipe`) that another loaded mod (or the
  vanilla `Base` module) already defines under the same identifier [10].
- **ScriptsDocs (PZ API Docs)** — a community-maintained documentation site
  (`pz-wiki-modding` organisation) generated from parsed script, Lua and Java
  data pulled from the installed game, rather than hand-written wiki prose;
  used here as the source for the full `mod.info` parameter list [2].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | The `WorkshopItems=`/`Mods=` pairing is a `both`-tagged row in the pinned `Server settings` revisions used throughout this knowledge base [3]. The `mod.info` fields covered here were **not** independently re-verified against a B41-era `mod.info` page revision — see Risks |
| B42 (stable) | Yes | 42.20; notes reviewed to 42.21 | 42.20 stable from 2026-07-29 [1], superseded by 42.21 stable on 2026-09-28 [19]; ScriptsDocs' `mod.info` page is titled "PZ API Documentation 42.20.0" [2], and the pzwiki `Mod.info` page's own version banner reads 42.17.0, one minor version behind [5] |

Re-baseline note (0.2.0): this revision re-checked the document against the Steam announcements 42.20.1 to 42.21 stable [16] [17] [18] [19] and the abridged TIS forum changelist for 42.21 [20] for anything touching Workshop updates, restarts, version mismatch or Lua checksums. None of those notes describes a change to how a server fetches or refreshes Workshop items or to the `WorkshopItems=`/`Mods=` keys. The pzwiki and ScriptsDocs statements remain pinned to the revisions listed in References and are carried forward from 42.20 with no contradicting change found; they were not re-tested on 42.21.

The core `WorkshopItems=`/`Mods=` mechanism predates the B42 mod-folder
restructuring and is unchanged by it; the B42-specific wrinkle is that
`mod.info` — where `require=`/`incompatible=`/`loadModAfter=`/`loadModBefore=`
live — now exists per version folder rather than once at the mod root, so a
mod's declared dependencies can in principle differ between its `42/` and
`42.1/` folders [6]. `modders-foundation` owns the full version-folder
mechanic; this document only notes the consequence for dependency fields.

# Reference

## Two identifiers, not one

A Workshop item and a mod are not the same thing to the game. The Workshop ID
is Steam's numeric identifier for the uploaded item, used to fetch it; the Mod
ID is the `id` value inside that item's `mod.info`, used by the game to
recognise and load it. A single Workshop item's `Contents/mods/` folder can
contain more than one Mod ID, and the reverse pairing mistake — Workshop IDs
and Mod IDs miscounted against each other — is the most common cause of "the
mod downloaded but never showed up in the game" [7] [5].

## The `server.ini` pairing

Two paired list keys carry the two identifiers:

| Key | Carries | Documented separator | Source |
|-----|---------|----------------------|--------|
| `WorkshopItems=` | Workshop IDs, for the server to fetch | Semicolon; documented example `WorkshopItems=514427485;513111049` | [3] |
| `Mods=` | Mod IDs, "found in `\Steam\steamapps\workshop\modID\mods\modName\info.txt`" | **Not documented** — the pinned revision gives the key's purpose but no separator example | [3] |

The pzwiki `Dedicated server` page's own four-step "Installing mods"
workflow is: collect mods into a Steam Workshop collection, run the
collection URL through the community PZ ID Grabber tool to extract paired
IDs, then paste the Workshop IDs into `WorkshopItems=` and the Mod IDs into
`Mods=` [4]. That page's own screenshot caption states that Workshop-
subscribed mods are "downloaded automatically on connecting client
machines" [4] — a documented fact about **clients**, not, on its own, proof
of what the **server process** itself does at boot (see Download and update
mechanics, below).

Every other list-type key documented on the same `Server settings` page uses
semicolons (`ChatStreams`, `ClientCommandFilter`, `ClientActionLogs`) [3];
`Mods=` fitting that same convention is a reasonable inference, not a
separately documented fact for this specific key.

## `mod.info`: where dependency and load order actually live

The `server.ini` `Mods=` line has no documented ordering semantics. The place
dependency and load order *are* documented is inside each mod's own
`mod.info`, via four fields that ScriptsDocs — generated directly from the
game's parsed script/Lua/Java data — documents with type and example for each
[2]:

```ini
require=theNeededMod,theOtherOne
incompatible=theUnwantedMod,theOtherOne
loadModAfter=someMod,anotherMod
loadModBefore=someMod,anotherMod
```

- **`require=`** — "Mods required to run this mod. Multiple mods can be
  specified separated by commas" [2]. The pzwiki `Mod.info` page's own worked
  example uses the same field and separator (`require=otherModID,
  anotherModID`) [5].
- **`incompatible=`** — mods that cannot be enabled simultaneously; enabling
  one makes the other(s) unselectable in the mod-manager UI, and vice
  versa [2].
- **`loadModAfter=`** / **`loadModBefore=`** — force this mod to load after
  or before the named Mod IDs, independent of anything in `server.ini` [2].

Neither ScriptsDocs nor the pinned `Mod.info` wiki revision states what
happens mechanically if a `require=` dependency is absent at load time (crash,
silent skip, or partial load) [2] [5]; the closest documented answer is the
symptom described next.

## The documented symptom of a missing dependency

Separately from `mod.info`'s own fields, pzwiki's `Resolving problems with
mods` page documents the user-visible sign of a missing required mod: "If the
mod is red in mods menu (or when save is running — in mod list in lower right
corner in pause menu), then the mod is missing a third-party mod that it
depends on. It is usually listed on the right side of the mod's Steam page
('Required Items')" [9]. That page is written from a client's perspective (the
in-game mod-manager UI); no primary or fact-only source found describes the
equivalent dedicated-server console/log behaviour for a `Mods=` entry whose
`require=` target is absent from the same server's `Mods=`/`WorkshopItems=`
lists.

## Manual installs vs. Workshop-managed mods

Local mods can reach a server two ways, and the two folders have different
update behaviour by construction: `Zomboid/mods/` is a manual-install path
the operator populates directly, while `Zomboid/Workshop/` is the
Steam-managed cache tied to whatever the client or server subscribes to or
lists in `WorkshopItems=` [11] [6]. Nothing in `Mods=` itself distinguishes
which folder a given Mod ID's files came from — the key only names the ID the
game should load, wherever its files currently sit [3] [11].

## Download and update mechanics: what is and is not documented

The clearest documented fact is client-side: connecting clients download
`WorkshopItems=`-listed mods automatically [4]. For the **server process
itself**, the pinned wiki pages do not spell out the mechanism in one place,
but corroborating evidence shows the server does perform its own Workshop
activity: a Steam Community support thread about a dedicated server failing
to load mods quotes the server's own launch log emitting Steamworks-style
Workshop query lines (`Workshop: onItemQueryCompleted handle=1
numResult=1`) immediately after `Mods=`/`WorkshopItems=` were populated [15] —
evidence that the server binary itself calls into the Workshop API at boot,
not merely that clients later pull the files. What is **not** documented by
any source found is whether that query/download behaviour re-checks for and
pulls a newer file on every subsequent restart, or only on first acquisition;
see Claim 3 below.

Separately, pzwiki's `SteamCMD` page confirms that SteamCMD "can be used to
... install or upload Workshop mods" and that downloading a Workshop item
"can be done anonymously" [8], but it documents this only as a general
SteamCMD capability statement — it gives no worked example of the
`workshop_download_item` console command for Project Zomboid specifically
(no app-ID/item-ID pairing, no validated command line). Hosting-community
material commonly cites a pattern such as
`steamcmd +login anonymous +workshop_download_item 108600 <id> validate +quit`
to pre-cache a mod outside of the running server, using the base game's App
ID (108600) rather than the dedicated server tool's App ID (380870) — pzwiki's
own `Workshop ID` page corroborates that Workshop content is fetched "by other
players (mods) or servers (SteamCMD)" against the game's Workshop namespace
[7] — but this document did not find a primary or fact-only source stating
the exact command syntax, so it is presented here as commonly-practiced,
uncited-command-line territory rather than a verified fact.

Whichever mechanism populates the mod files, the *config surface* itself
(`Mods=`, `WorkshopItems=`) is read at server startup like every other
`server.ini` key; `admins-foundation` and `admins-server-ini-reference`
already establish that mod-list changes are restart-required rather than
covered by the live `reloadoptions` path — this document does not re-derive
that fact, only notes that it applies equally to a Workshop file update
landing in the cache between restarts.

## Version drift and the 42.20.1 to 42.21 notes

Three official changes sit near the update-and-restart behaviour this document
describes. First, 42.20.1 lists improved Lua checksum validation for
multiplayer anti-cheat [16]; the note does not say how a mismatch between
client and server mod Lua is handled, so no mod-specific behaviour is asserted
here *(B42)*. Second, 42.21 adds a notification for players who try to connect
to a multiplayer server running a different game version [18] [20]; the
wording covers the game version, and the notes reviewed do not extend it to
Workshop mod revisions *(B42)*. Third, the 42.20.4 hotfix removed the
`loadstring` and `loadstream` Lua methods and told authors who ran
server-sent code through them to replace that with commands [17]; 42.21
re-enabled both [18] [19] *(B42)*. The 42.20.4 post is shared with the 42.19.2
unstable and 41.78.21 legacy hotfixes and does not split the Lua change by
build [17]. None of the notes reviewed alters the documented restart-required
posture of mod-list changes; the author-side detail of the Lua changes lives
in `modders-lua-api-surface` and the other Modders documents.

## Pinning a mod to a specific Workshop revision

No primary or fact-only source documents a way to lock `WorkshopItems=` to a
past file revision of a Workshop item: the Workshop ID is the item's stable
identifier, but resolving it (by any client, server, or SteamCMD call)
fetches the item's *current* published content — there is no separate
"revision ID" parameter documented anywhere in this research for
`WorkshopItems=` or `workshop_download_item` [3] [8]. The only documented
route to a frozen copy is the manual-install path already described: obtain
the mod's files at the version you want (by downloading it once, or by asking
the author for an archived copy), place them under `Zomboid/mods/<ModID>/`,
and reference the Mod ID only in `Mods=` — never adding its Workshop ID to
`WorkshopItems=` [11] [3]. Because nothing in `WorkshopItems=` names that Mod
ID, no update mechanism (server-side query or client-side subscription) has a
reason to touch that folder. This is a synthesis of documented mechanics, not
a named "mod pinning" feature described as such by any source — treat it as
a practical guidance-layer conclusion, not a reference-layer fact.

# B41 vs B42 Delta

| Area | Build 41.78 *(B41)* | Build 42.20 / 42.21 *(B42)* |
|------|---------------------|----------------------|
| `WorkshopItems=`/`Mods=` keys | Present, `both`-tagged in the pinned `Server settings` revisions [3] | Same |
| `mod.info` location | One `mod.info` at the mod root [6] | One `mod.info` per version folder (`common/`, `42/`, `42.1/`, …); dependency fields can in principle differ per version folder [6] |
| `require=`/`incompatible=`/`loadModAfter=`/`loadModBefore=` | Not independently verified against a B41-era `mod.info` page revision in this research | Documented against the current ScriptsDocs build (titled 42.20.0) and the pzwiki `Mod.info` page (versioned 42.17.0) [2] [5] |
| `loadstring`/`loadstream` (affects mods that run server-sent code) | Per-build scope of the 42.20.4 removal not separated in the combined post [17] | Removed in 42.20.4 [17]; re-enabled in 42.21 [19] |
| Mod-folder auto-detection | Flat layout; presence of `media/` + root `mod.info` is what's checked | At least one `common/` or version folder is required for detection — a fact `modders-foundation` already owns in depth [6] |

The one-line version: the `WorkshopItems=`/`Mods=` server-config pairing this
document centres on is unchanged across the branch split; what changed is
*where inside the mod's own files* `mod.info` — and therefore `require=` and
its siblings — lives, per the B42 versioned-folder restructuring that
`modders-foundation` documents in full [6].

# Practical Guidance

- **Never edit `Mods=`/`WorkshopItems=` without their partner.** Every
  Workshop ID needs its Mod ID(s) present in `Mods=`, and vice versa; a
  Workshop item containing several mods needs every one of its Mod IDs
  listed if you want them all active [3] [7].
- **Use semicolons in `Mods=` by convention, not by confirmed spec.** The
  pinned reference only demonstrates a separator for `WorkshopItems=`;
  mirroring the semicolon convention used by every other list key on the same
  page (`WorkshopItems`, `ChatStreams`, `ClientCommandFilter`) is the
  reasonable default, but verify by reading the server's boot console mod
  list every time you change this line [3].
- **Declare dependencies in `mod.info`, not by hoping `Mods=` order helps.**
  If you control a mod's `mod.info` (your own mod, or a fork), use
  `require=`, `incompatible=`, `loadModAfter=` and `loadModBefore=` — these
  are the actually-documented levers [2]. If you are wiring together
  third-party mods you cannot edit, you have no documented lever over their
  relative load order at all; treat any `Mods=`-ordering trick as
  unconfirmed folklore (Claim 2) and validate empirically per Verification
  Steps.
- **Watch the mod-manager UI (or the in-game pause-menu mod list) for red
  entries** after adding a mod bundle — that is the documented signal for a
  missing `require=` dependency, and it will point you at the Workshop page's
  "Required Items" list to find what's missing [9].
- **Do not assume an upstream Workshop update reaches your server
  automatically and safely.** The server does perform its own Workshop
  queries at boot [15], but no source found confirms this re-validates
  content on every restart, and no source at all documents whether a
  mid-session author update is picked up without a restart. Pin your update
  discipline to a restart, and consider testing a copy of the server before
  restarting production after a mod author ships a new version — this
  connects directly to `admins-modded-server-runbook`'s rollout process.
- **To freeze a mod at a known-good version, take it out of
  `WorkshopItems=` and load it from `Zomboid/mods/` instead.** This is the
  only documented way to stop a specific mod from tracking Workshop updates;
  it costs you the Workshop's own update/changelog visibility for that mod,
  so keep your own record of which version you froze and why.
- **Script and verify SteamCMD-based mod pre-caching separately from the
  server's own boot-time behaviour** if you use it — the exact
  `workshop_download_item` invocation is common practice, not a pzwiki- or
  Indie-Stone-documented command line, so test it against a scratch install
  before trusting it in an update pipeline.

# Common Pitfalls & Troubleshooting

- **Workshop ID pasted into `Mods=`, or vice versa.** The two lists take
  different ID types entirely; a Workshop ID in `Mods=` will not resolve to
  anything the game recognises as a Mod ID [3] [7].
- **One Workshop item, several Mod IDs, only one Mod ID copied.** Some
  Workshop items bundle multiple mods; check the item's page for the full
  list before assuming a single Mod ID is enough [7].
- **A bundle "installs" but a member mod never runs.** Check the in-game mod
  list (pause menu, lower-right) for a red entry — that is the documented
  missing-dependency symptom, not a separate bug per mod [9].
- **Copying a B41 mod's `mod.info` fields verbatim onto a B42 install.** The
  file may need to exist per version folder now; a `require=` line placed
  only under the mod's `common/` folder should still be found according to
  the wiki's general "works in both, best kept in versioning folders"
  guidance for `mod.info` as a whole, but this document did not separately
  verify that guidance for the dependency fields specifically [6] [5].
- **Trusting a hosting guide's backslash-prefixed `Mods=` example.** The
  pinned `Server settings` revision shows no backslash in any `Mods=`-adjacent
  text, and at least one other hosting KB's example also omits it — see
  Claim 1, shared with `admins-foundation`. Never edit an existing entry to
  add or remove a backslash "to match a guide" without testing on a copy of
  the server.
- **Assuming reordering `Mods=` fixes an override conflict.** No source
  found ties `Mods=` position to override precedence; if two mods conflict,
  the documented lever is `mod.info`'s `loadModAfter=`/`loadModBefore=` on
  the mods you can edit, not shuffling the server's list — see Claim 2.
- **Restarting only the launcher, not re-verifying the mod list.** Because
  mod changes are restart-required and the server performs its own Workshop
  queries at boot, the safest habit after any mod-related edit is reading the
  boot console's mod list before declaring the change live.

# Community Notes & Unverified Claims

## Claim 1 — Build 42 requires a leading backslash on each `Mods=` entry

- **Claim:** Several hosting guides state that Build 42 changed the `Mods=`
  format to require a leading backslash per entry
  (`Mods=\ModOne;\ModTwo`), and frame it as a leading cause of "installed but
  not loaded" mods on B42 servers [12].
- **Why unverified:** The pinned `Server settings` revision documents the
  `Mods=` key's purpose with no separator or prefix example at all [3], and
  at least one other hosting KB's own B42 example omits the backslash
  entirely [13] — the secondary sources conflict with each other, not just
  with the fact-only source. `admins-foundation` reaches the identical
  conclusion independently (its Claim 2); this document arrived at the same
  place from its own research pass rather than copying that finding forward.
- **Confidence:** Low. The claim circulates widely enough to be operationally
  relevant, but the best fact-only source available contradicts it and no
  primary source was found either way.

## Claim 2 — The order of Mod IDs inside `Mods=` controls load/override order

- **Claim:** Hosting documentation (including a dedicated "mod load order"
  guide) states that Project Zomboid loads mods in the left-to-right order
  listed in `Mods=`, that a mod loaded later can override content from a mod
  loaded earlier, and that framework/library mods should be listed first for
  this reason [14].
- **Why unverified:** No primary or fact-only source found ties `Mods=`
  list position to override precedence. The pzwiki `Scripts` page documents
  that a script definition can "soft override" an existing one of the same
  identifier, but describes the merge/override mechanism itself, not what
  determines *which* of two competing mods wins when both define the same
  identifier [10]. The actually-documented load-order lever is `mod.info`'s
  `loadModAfter=`/`loadModBefore=`, which is a different mechanism entirely
  from `server.ini` list position [2].
- **Confidence:** Low. The claim is plausible (some sequential resolution
  order must exist internally) and widely repeated, but no source — primary,
  code-truth, or fact-only — confirms that the specific, admin-controllable
  lever is the `Mods=` line's ordering rather than something the game
  resolves independently of it.

## Claim 3 — The dedicated server automatically re-checks and updates every `WorkshopItems=` entry on each restart with no admin action required

- **Claim:** Hosting guidance commonly asserts that a Project Zomboid
  dedicated server, on every restart, re-downloads and updates each Workshop
  item listed in `WorkshopItems=` to the author's latest published version
  without any separate SteamCMD step.
- **Why unverified:** A Steam Community support thread's server log excerpt
  confirms the server process itself performs Workshop query calls
  (`Workshop: onItemQueryCompleted`) when `WorkshopItems=` is populated [15],
  which is genuine evidence the mechanism exists — but that thread is a
  troubleshooting report about mods *failing* to download, not a
  confirmation that the mechanism reliably re-validates content on every
  subsequent boot once a mod is already cached. No primary source states the
  re-check behaviour either way.
- **Confidence:** Low. The server clearly talks to the Workshop API at boot;
  whether that talk includes a guaranteed refresh of already-downloaded
  content on every restart is not established by anything found in this
  research.

# Risks & Caveats

- **The core `Mods=` separator gap is load-bearing for this whole
  document.** Every piece of practical guidance about `Mods=` syntax here is
  built on the absence of documentation, not its presence — re-check the
  pinned `Server settings` revision at the next review date in case a future
  edit finally adds a separator example [3].
- **`mod.info` dependency fields were verified against the current
  documentation snapshot, not a B41-era one.** ScriptsDocs is titled
  "42.20.0" and the pzwiki `Mod.info` page's own banner reads 42.17.0 [2] [5];
  neither source in this research was checked against an archived
  B41.78-era `mod.info` page revision, so the B41 column of the Delta table
  above is honestly incomplete rather than confirmed identical.
- **The server-side Workshop-query evidence is a single community bug
  report, not a primary confirmation.** Claim 3's log excerpt is real and
  dated, but it is one user's troubleshooting thread, not an Indie Stone
  statement about the update mechanism's guarantees.
- **Wiki pages in this space edit frequently.** `Dedicated server` and `Mod
  structure` both moved to newer revisions than the ones pinned in sibling
  documents during this same research pass (within the same day); the
  citations below are pinned to the revisions read for this document
  specifically.
- **Hotfix cadence.** 42.21 has been stable since 2026-09-28 [19]; a later hotfix could change Workshop, checksum or mismatch behaviour before this document's next review.
- **Hosting-KB sources are corroborate-only by this project's own rules** and
  are used here exclusively to document claims that this document then
  quarantines — never to source a fact in the Reference section above.

# Verification Steps

1. **Confirm the `Mods=` separator empirically:** on a disposable B42 test
   server, populate `Mods=` with two known Mod IDs separated by a semicolon,
   confirm both load via the boot console, then repeat with a comma and with
   a leading backslash on each entry to see which forms the server actually
   accepts or silently ignores.
2. **Confirm `require=` failure behaviour:** create a minimal test mod whose
   `mod.info` sets `require=someMissingModID`, load it on a server that does
   not have that Mod ID in `Mods=`, and record the server console/log output
   plus the in-game mod-list colour, to compare against the client-side red
   -entry symptom documented for the standalone game [9].
3. **Probe Claim 2 directly:** define the same script identifier (e.g. an
   `item` block) in two test mods with contradictory values, list them in
   both orders in `Mods=` across two otherwise-identical server boots, and
   record which mod's value wins each time.
4. **Probe Claim 3 directly:** update a test Workshop item's content, leave
   the server's `WorkshopItems=`/`Mods=` unchanged, restart the server, and
   check the cached mod files' timestamps/content against the new upload to
   see whether the restart alone pulled the update.
5. **Confirm the manual-pin workaround:** place a mod's files under
   `Zomboid/mods/<ModID>/` without adding its Workshop ID to
   `WorkshopItems=`, restart, and confirm via the boot console that the mod
   loads and that no Workshop-side update activity touches that folder on a
   later restart after the author ships a new version.

# Open Questions

- Do the improved Lua checksum validation [16] or the 42.21 game-version
  notice [18] [20] say anything about a server and client holding different
  Workshop revisions of the same mod? The notes reviewed are silent.
- What is the actually-supported separator (and any prefix convention) for
  `Mods=`, and will pzwiki or a future Indie Stone modding-documentation
  release (flagged as planned in `modders-foundation`) finally state it
  explicitly?
- Does the dedicated server's own Workshop query at boot (Claim 3) reliably
  re-validate and refresh already-cached content, or only fetch content it
  does not yet have? Verification Step 4 answers the behaviour; no source
  found answers the intended design.
- What exactly happens when a `require=` dependency is absent from a
  dedicated server's `Mods=`/`WorkshopItems=` lists specifically — does the
  server refuse to start, start without the dependent mod, or start in a
  broken state? The documented symptom found is client/save-side only [9].
- Does `Mods=` list order affect anything at all mechanically (Claim 2), or
  is the widely-repeated "order matters" advice actually describing
  `loadModAfter=`/`loadModBefore=` behaviour misattributed to the wrong
  file?
- Is there any officially supported way to pin a Workshop item to a specific
  historical file revision (as opposed to the manual-copy workaround
  documented here), for example through a Steamworks feature not exposed by
  `workshop_download_item`'s documented anonymous-download capability [8]?

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam
  announcement, 2026-07-29; retrieved via the Steam news API, ISteamNews app
  108600). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259.
  Accessed 2026-07-31.
- [2] **PZ-Wiki-Modding** — *PZ API Documentation: ROOT-ModInfo* (ScriptsDocs;
  generated from parsed script/Lua/Java data; page titled "PZ API
  Documentation 42.20.0"). https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root_files/modinfo.html.
  Accessed 2026-07-31.

- [16] **The Indie Stone** — *42.20.1 STABLE Hotfix Released* (Steam announcement, 2026-08-05; Lua checksum validation). https://steamcommunity.com/games/108600/announcements/detail/1840310314338766. Accessed 2026-10-07.
- [17] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26; `loadstring`/`loadstream` removal). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601. Accessed 2026-10-07.
- [18] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23; `loadstring` re-enabled, game-version mismatch notice). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925. Accessed 2026-10-07.
- [19] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307. Accessed 2026-10-07.
- [20] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first post, 2026-09-23; abridged selection of the full changelist). https://theindiestone.com/forums/topic/101693-4221-patch-notes/. Accessed 2026-10-07 (host bot-block allowlisted).

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL +
revision id; facts only, never prose.

- [3] **PZwiki** — *Server settings* (revision 1443167; page versioned
  against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167.
  Accessed 2026-07-31. Fact-only source.
- [4] **PZwiki** — *Dedicated server* (revision 1443859; page versioned
  against 42.20.0). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443859.
  Accessed 2026-07-31. Fact-only source.
- [5] **PZwiki** — *Mod.info* (revision 1363935; page versioned against
  42.17.0). https://pzwiki.net/w/index.php?title=Mod.info&oldid=1363935.
  Accessed 2026-07-31. Fact-only source.
- [6] **PZwiki** — *Mod structure* (revision 1443863; page versioned against
  42.20.0). https://pzwiki.net/w/index.php?title=Mod_structure&oldid=1443863.
  Accessed 2026-07-31. Fact-only source.
- [7] **PZwiki** — *Workshop ID* (revision 1395231). https://pzwiki.net/w/index.php?title=Workshop_ID&oldid=1395231.
  Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *SteamCMD* (revision 1393761). https://pzwiki.net/w/index.php?title=SteamCMD&oldid=1393761.
  Accessed 2026-07-31. Fact-only source.
- [9] **PZwiki** — *Resolving problems with mods* (revision 1392779). https://pzwiki.net/w/index.php?title=Resolving_problems_with_mods&oldid=1392779.
  Accessed 2026-07-31. Fact-only source.
- [10] **PZwiki** — *Scripts* (revision 1442815; page versioned against
  42.17.0). https://pzwiki.net/w/index.php?title=Scripts&oldid=1442815.
  Accessed 2026-07-31. Fact-only source.
- [11] **PZwiki** — *Mods* (revision 1391047). https://pzwiki.net/w/index.php?title=Mods&oldid=1391047.
  Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [12] **Pinehosting** — *Project Zomboid Build 42 Mods: Install And Fix
  Guide* (hosting blog; source of the backslash claim). https://pinehosting.com/blog/modded-project-zomboid-server-hosting-build-42-install-steam-workshop-mods-fixes/.
  Accessed 2026-07-31.
- [13] **DoomHosting** — *How to Install Mods on a Project Zomboid Server
  (Build 42)* (hosting KB; backslash-free counter-example). https://www.doomhosting.com/help/articles/how-to-install-mods-project-zomboid-server-build-42.
  Accessed 2026-07-31.
- [14] **XGamingServer** — *Project Zomboid Mod Load Order: How to Set It
  Correctly* (hosting docs; source of the `Mods=`-order-controls-precedence
  claim). https://xgamingserver.com/docs/project-zomboid/mod-load-order.
  Accessed 2026-07-31.

**Community & Creator**

- [15] **Steam Community** — *Cant get mods downloaded to dedicated server*
  (Project Zomboid Support discussion thread; server-log evidence of
  boot-time Workshop query activity). https://steamcommunity.com/app/108600/discussions/1/4035851881534911343/.
  Accessed 2026-07-31.

**Further Reading**

# Further Reading

- Valve's Steamworks Workshop implementation documentation, linked from the
  pzwiki `SteamCMD` page as the authority for the underlying build/upload
  configuration file format: https://partner.steamgames.com/doc/features/workshop/implementation
- PZ ID Grabber, the community tool the pzwiki `Dedicated server` page's
  "Installing mods" workflow uses to extract paired Workshop ID/Mod ID lists
  from a Steam Workshop collection: https://pzidgrabber.com
- The ISteamNews mirror used to verify the primary announcement cited above:
  https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0

# Related Documents

- `admins-foundation` — the Admins-track overview; its "Mod wiring basics"
  subsection is the entry point this document deepens.
- `admins-server-ini-reference` — the key-by-key `server.ini` reference; its
  Mods and map table rows point here for the material in this document.
- `modders-foundation` — the Modders-track foundation; owns the B42 mod
  folder anatomy, the Kahlua Lua environment, and Workshop publishing from
  the mod-author's side that this document assumes as background.
- `admins-modded-server-runbook` — the operational process of selecting,
  staging and rolling out mods on a live server, once this document's
  mechanics are understood.
- `admins-ubuntu-runbook` — Linux process supervision, unrelated to mod
  wiring itself but the environment this document's server runs in.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21 (stable 2026-09-28): added a Reference section on 42.20.1-42.21 notes bearing on Workshop wiring (Lua checksum validation, loadstring/loadstream removal and re-enable, game-version mismatch notice, no documented change to Workshop fetch behaviour); updated Build Applicability, Delta, Risks and Open Questions. Sources: Steam posts 42.20.1, 42.20.4+41.78.21, 42.21 unstable and stable; TIS forum 42.21 patch notes. Unchanged statements carried forward from 42.20, not re-tested. | — |
