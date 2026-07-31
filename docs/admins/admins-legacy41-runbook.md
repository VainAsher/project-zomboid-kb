---
id: admins-legacy41-runbook
title: "Keeping a Build 41 Server Alive: The legacy41 Runbook"
version: 0.1.0
status: in-review
confidence: Medium
category: Admins
topic: "Server runbooks"
build: B41
document_type: tutorial
created: 2026-07-31
updated: 2026-07-31
review_due: 2026-10-31
sources_verified: 2026-07-31
supersedes: null
related: [admins-foundation, admins-backups-migration, admins-server-ini-reference, lore-foundation, meta-style-guide]
tags: [legacy41, build-41, steamcmd, beta-branch, maintenance-line, hotfix, workshop-mods, dedicated-server, runbook]
game_versions_verified: ["41.78.16", "41.78.19"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | admins-legacy41-runbook |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Admins |
| Build | B41 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-31 |
| Updated | 2026-07-31 |
| Review due | 2026-10-31 |
| Game versions verified | 41.78.16, 41.78.19 |

# Executive Summary

Since 2026-07-29, Build 42.20 is Project Zomboid's stable public build, and a community that wants to keep playing Build 41 does so on a named Steam beta branch: `legacy41` [1] [2] [3]. The Indie Stone published the branch ahead of the switch precisely so that server owners could move themselves *and their players* before launch day, because Build 41 savegames cannot be carried into Build 42 [1] [2]. This document is the operating runbook for that choice: how to install or switch a dedicated server onto `legacy41`, how to keep every client on the matching branch (and what happens to the player who forgets), what "staying on 41" actually means now that B41 is a maintenance line rather than a frozen artifact, how the B41-era configuration surface differs from the B42 documentation most guides now assume, and what the branch decision does to your mod ecosystem.

The core operational surprise this runbook exists to deliver: **legacy41 is not frozen**. Build 41 received a wave of security hotfixes in March and April 2026 — 41.78.17, 41.78.18 and the 41.78.19 security-vulnerability update — driven by a Workshop malware incident and an internal security audit [4] [5] [6], and the wiki's Build 41 version history additionally records a 41.78.20 released the same day Build 42 went stable [8]. A legacy41 server therefore still needs a working, branch-pinned update procedure, and its operator still needs to watch the official announcement feed. At the same time, The Indie Stone has committed to no end-of-support date in either direction — the honest position on lifespan is that nobody outside the studio knows, and this document quarantines the community's speculation rather than repeating it.

Document-level confidence is **Medium**: the branch mechanics, hotfix timeline and mod-structure facts rest on official announcements and revision-pinned wiki pages, but the B41-era configuration documentation is thinner than B42's (the pinned B41 settings revision self-describes as incomplete), 41.78.20 is currently wiki-attested only, and several operationally important behaviours (exact client version-mismatch handling, Workshop-update breakage) rest on community experience and are quarantined below.

# Key Takeaways

- Build 41 lives on the `legacy41` Steam beta branch: clients opt in via Steam Properties → "Game Versions & Betas" → `legacy41`; dedicated servers pin it in SteamCMD with `app_update 380870 -beta legacy41 validate` *(cited)*
- B41 saves cannot migrate to B42, and a separate `42.19` beta branch exists solely for finishing unstable-era 42.19 saves — neither branch is a conversion path *(cited)*
- Server and players must move branch **together**, before the switch; the 42.20 release notes document the client's switch-back path for anyone who updated by accident *(cited)*
- legacy41 is a maintenance line, not a museum piece: 41.78.17 (2026-03-19), 41.78.18 (2026-03-20) and the 41.78.19 security patch (2026-04-08) all shipped in 2026 *(cited)*; a 41.78.20 (2026-07-29) is wiki-attested, with no matching official announcement found *(cited, fact-only source)*
- Keep your update script running and branch-pinned — skipping updates on a "frozen" build means skipping security patches *(cited synthesis)*
- The B41 `.ini` surface differs from current B42 documentation: B41-only key families exist, the loot-respawn keys live in the `.ini` on B41 rather than SandboxVars, and the `AntiCheat*`/`Backups*` families have no B41-era documentation — see `admins-server-ini-reference` *(cited)*
- One Workshop item can carry B41 and B42 content side by side (flat `media/` folder for B41; `common/` plus version folders for B42), and Workshop items carry author-set "Build 41"/"Build 42" filter tags — but nothing forces an author to keep the B41 side alive *(cited)*
- There is no committed end-of-support date for legacy41, in either direction; all lifespan predictions circulating in the community are speculation *(community, unverified)*

# Purpose

This document answers the question a community leader asks the week Build 42 goes stable: *we are staying on Build 41 — what exactly do I have to do, once and then forever?* It is written as an ops runbook for the admin who operates the server, briefs the players, and curates the mod list. The parent overview (`admins-foundation`) maps the whole server landscape across both builds; this document goes deeper on exactly one path through it — the legacy41 path — and carries the copy-pasteable procedures for staying on it safely.

# Scope

Covered: what the `legacy41` branch is and how it relates to the `42.19` bridge branch; installing a fresh B41 server or switching an existing one onto the branch (Steam UI and SteamCMD, Windows and Linux); keeping clients on the matching branch, including the documented recovery path for a client that updated to B42; the 2026 B41 maintenance-hotfix record and what it obliges an operator to keep doing; the B41-era `server.ini` surface at summary level (the key-by-key detail belongs to `admins-server-ini-reference`); mod-ecosystem implications of staying on B41 (mod structure, Workshop build tags, the 2026 Workshop security incident); and an honest assessment of the branch's lifespan evidence.

Not covered: backup, restore and world-migration procedure (owned by `admins-backups-migration` — a legacy41 server should be running that document's runbook unchanged); the full `.ini` and SandboxVars key references (sibling reference documents); B42 server operations; and hosting-panel-specific branch switches (vendor UIs wrap the same SteamCMD mechanics documented here).

# Definitions

- **`legacy41`** — the Steam beta branch, for both the game client and the dedicated-server tool, that keeps Build 41.78 installed after Build 42 became the default stable build [1] [2] [7].
- **`42.19`** — a parallel beta branch preserving unstable 42.19, published because 42.19 saves are incompatible with 42.20; it is a bridge for finishing unstable-era worlds, not a B41 concern beyond not confusing the two [1] [2].
- **Maintenance line** — this knowledge base's term for B41 as it now exists: a branch that receives security/maintenance hotfixes (41.78.17 through at least 41.78.19) but no content development [4] [5].
- **Branch pinning** — encoding the beta flag into every install/update command so routine updates can never silently hop the server onto the default (B42) branch [7].
- **Build matching** — the operational duty that server and all clients run the same build; the announcements instruct owners to move "(and your players)" together [1] [2].
- **`outdatedunstable`** — an official branch that lags one content update behind `unstable`; part of the studio's 2026 security-driven branch policy and useful context for how The Indie Stone manages legacy versions [4] [6].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 baseline; 41.78.19 primary-attested | This document's subject. The KB's B41 baseline follows the legacy41 maintenance line; 41.78.17–.19 are announcement-attested security/maintenance patches [4] [5], 41.78.20 wiki-attested only [8] |
| B42 (stable) | Context only | 42.20 | Cited only where the branch split itself is the fact (release date, incompatibility, switch instructions) [1] [2] [3] |

This is a single-build (B41) document. Facts that describe the B42 side of the boundary — the stable release date, save incompatibility, the client switch-back instructions — are cited to the primary announcements rather than asserted about B42 behaviour generally.

# Reference

## The branch, and why it exists

Build 42.20.0 reached the stable public branch on 2026-07-29, ending Build 41.78's run as the default version [3]. Both pre-release announcements state the boundary condition without hedging: "Build 41 savegames clearly will not be compatible with Build 42" [1] [2]. For players and server communities wanting to continue on Build 41, The Indie Stone published the `legacy41` beta channel ahead of the release, with explicit instructions to move over *before* launch day: right-click Project Zomboid in the Steam library, open Properties, and select `legacy41` under "Game Versions & Betas" [1] [2]. The 42.20 release notes repeat the same three steps under the heading of switching back to Build 41, which is the documented recovery path for anyone who reached 42.20 first [3].

A second beta branch, `42.19`, was published at the same time for a different population: players finishing saves from unstable 42.19, which are likewise incompatible with 42.20 [1] [2]. A B41 community has no reason to touch it — but its existence matters operationally, because two similarly-purposed "old version" branches now sit in the same Steam menu and picking the wrong one installs the wrong game.

## Installing or switching the server

The dedicated server is the same free SteamCMD product on both builds — App ID 380870, anonymous login — with the branch selected per install [7]. The wiki's Dedicated server page (pinned revision, versioned 42.20.0) documents legacy-build servers along two paths [7]:

- **Steam UI**: if you run the server tool from the Steam library, pick the branch from the tool's own Game Versions and Betas properties menu, exactly as for the client [7].
- **SteamCMD**: add the beta flag to the update command — `app_update 380870 -beta legacy41 validate` [7].

On Linux, the wiki's pattern keeps the branch pinned inside the reusable SteamCMD script (`update_zomboid.txt`), so every routine update re-asserts the branch [7]:

```text
// update_zomboid.txt
@ShutdownOnFailedCommand 1
@NoPromptForPassword 1
force_install_dir /opt/pzserver/
login anonymous
// the branch pin below is the load-bearing line:
app_update 380870 -beta legacy41 validate
// done — exit steamcmd
quit
```

Two consequences follow from the mechanics. First, switching an existing B41 server that was installed from the (then-default) stable branch is the same command — SteamCMD validates the install against the `legacy41` depot and downloads whatever differs. Second, the world data is not part of the switch: saves, configuration and the account database live in the `Zomboid` data folder, not the install directory, and the branch flag touches only the server binaries [7]. (Protecting that data folder is `admins-backups-migration`'s runbook.)

## Keeping clients on the matching branch

The announcements treat build matching as the server owner's job: the channel exists "for you (and your players) to move over to before the event" [1] [2]. The client-side procedure is the three Steam Properties steps above [1] [2] [3]; there is no server-side switch you can perform on your players' behalf.

What the primary record documents about a mismatched client is indirect but sufficient: a client on 42.20 is running a build whose saves and content are incompatible with B41's [1] [2], and the server-side `DoLuaChecksum` setting (default true) ejects clients whose Lua files fail the checksum comparison against the server's [9]. The exact refusal behaviour a 42.20 client sees when it targets a legacy41 server — at what stage the connection fails and with what message — is not described in any primary source this document could find, and is quarantined below (Claim 2). Operationally the distinction barely matters: a client on the wrong branch cannot play, and the fix is the same three Steam steps followed by a restart of the client [2] [3].

The day-one failure mode is predictable from the instructions themselves: any player whose Steam installation sat on the default branch received Build 42 when it became the stable public version, because `legacy41` is opt-in [1] [2] [3]. The 42.20 release notes' "switch back" section exists precisely for that player [3].

## The maintenance-hotfix reality: B41 in 2026

Build 41.78.16 shipped in December 2022 and stood as the stable version for over three years [8]. The 2026 record then breaks the "frozen build" mental model:

| Version | Date | Attestation | What it was |
|---------|------|-------------|-------------|
| 41.78.17 | 2026-03-19 | Wiki version history [8]; consistent with the announcement's patch wave [4] | Security patch wave (see below) |
| 41.78.18 | 2026-03-20 | Announcement (named as the then-current default public version) [4]; wiki [8] | Security patch wave, plus rare-crash hotfixes [4] |
| 41.78.19 | 2026-04-08 | Announcement [5] | "Security Vulnerability Update" [5] |
| 41.78.20 | 2026-07-29 | Wiki version history only [8] | No official announcement or patch notes found; contents unknown |

The context behind that wave is documented in two announcements. In March 2026, following a responsibly disclosed vulnerability and the studio's own internal security audit, The Indie Stone patched the stable (then-B41) and unstable branches and temporarily removed unpatched legacy version branches from circulation entirely, stating that older legacy versions "will remain unavailable" because the team's priority "needs to be Build 42 stable, and future content updates" [4]. In April 2026, fourteen Steam Workshop mods by a single banned author were found to contain obfuscated code creating malicious files outside the game directory; the exploit itself only affected Build 42 branches, but the same day's hotfix pair shipped 41.78.19 to Build 41 to close a *separate* vulnerability found during the internal audit [5] [6].

Three operational conclusions, each anchored in that record. First, legacy41 still updates: a server on the branch received at least one security-critical binary update in 2026, so an operator who disabled updates "because B41 is done" was running a known-vulnerable server after 2026-04-08 [5]. Second, the studio patches B41 for security, not content — every 2026 B41 change in the primary record is security- or crash-driven [4] [5]. Third, the studio has demonstrated it will remove legacy branches it cannot secure [4] — which is the single most concrete data point available about legacy41's long-term future, and it cuts both ways (they patched B41 rather than pulling it; they also proved willing to pull what they could not patch).

The 41.78.20 row deserves its own honesty note: the wiki's Build 41 version-history table lists it with a 2026-07-29 release date — the same day 42.20 went stable — but this document found no Steam announcement, blog post or patch note naming it, after scanning the official announcement feed for the period [8]. Treat "current legacy41 = 41.78.20" as fact-only-sourced until a primary confirms it; the KB's pinned B41 baseline follows the maintenance line accordingly.

## The B41 configuration surface: what your B42-era guides get wrong

A legacy41 server is configured through the same four name-keyed files as a B42 server (`<name>.ini`, `<name>_SandboxVars.lua`, spawnpoints, spawnregions) [7] — but the *contents* of the `.ini` differ, and almost all current documentation (including the wiki's own Server settings page) is versioned against 42.20 [9]. The key-by-key comparison is `admins-server-ini-reference`'s territory; what a legacy41 operator needs to internalize is the shape of the difference, from that document's two pinned revisions [9] [10]:

- **Keys that exist only in the B41-era documentation** — among them the Steam port pair (`SteamPort1`/`SteamPort2`), the VOIP codec quartet (`VoiceComplexity`, `VoicePeriod`, `VoiceSampleRate`, `VoiceBuffering`), the zombie network-update tuning family, and `AutoCreateUserInWhiteList` [10]. A B42-era guide will never mention them.
- **Keys that live in different files per build** — the loot-respawn trio (`HoursForLootRespawn`, `MaxItemsForLootRespawn`, `ConstructionPreventsLootRespawn`) and `MinutesPerPage` are `.ini` keys in the B41-era revision but SandboxVars settings in the B42-era revision [9] [10]. Following a current guide, you would edit a file your B41 server does not read for that setting.
- **Key families with no B41-era documentation** — the `AntiCheat*` family, the four `Backups*` keys, chat moderation, the login queue and the expanded Discord bridge appear only in the B42-era revision [9] [10]. Whether any of them function undocumented on 41.78 is an open question (`admins-server-ini-reference`, Claim 1); do not build B41 operations on them.
- **Same-name keys with different documented defaults** — including `MaxPlayers` (16 at B41 vs 32 at B42) and `PingLimit` (250 vs 0) [9] [10]; a "recommended settings" paste from a B42 source silently changes your server's behaviour relative to B41 defaults.
- **Renamed keys** — the B41-era `DisableSafehouseWhenPlayerConnected` corresponds to B42's `DisableSafehouseWhenOwnerConnected`, and the B41 Discord bridge uses `DiscordChannel`/`DiscordChannelID` rather than the B42 channel triple [9] [10].

The unifying pitfall: an unrecognized key in the `.ini` fails silently, so B42-era configuration pasted into a legacy41 server produces no error — just a server that does not do what the guide promised [10].

## Mods on a frozen-in-time build

The B41 mod ecosystem's mechanics are documented and stable; its *social* dynamics are not. The documented part, from the pinned Mod structure page [11]:

- B41 mods use the flat structure — the mod's files sit in a `media/` folder directly under the mod folder, beside `mod.info` [11].
- B42 introduced versioning: a mandatory `common/` folder plus per-game-version folders (`42/`, `42.1/`, …) [11].
- The two structures can coexist in one mod folder: because the B42 layout nests one level deeper, the B41 `media/` folder and the B42 `common/` + version folders are isolated from each other, and the page states a mod can mix both [11]. The B41 loader does not recognize the `common/` folder as its own content source [11].

Two consequences for a legacy41 server. First, a Workshop item that was updated for B42 does not *necessarily* break for B41 — if the author kept the flat `media/` layout beside the new folders, both builds are served by the same item [11]. Second, nothing in the structure obliges an author to keep the B41 side: the moment an update removes or stops maintaining the flat layout, the item's B41 content is gone or stale, and your server inherits that on its next mod update. That failure mode is community-reported rather than primary-documented and is quarantined below (Claim 3).

Discovery-side, the Steam Workshop for Project Zomboid carries author-set build filter tags — "Build 40", "Build 41" and "Build 42" all exist as selectable tags on the Workshop browse page — so B41-compatible mods remain findable as a category [12]. Tags are author-maintained metadata, not a compatibility guarantee: treat them as a search filter, and verify against the mod's own structure and changelog.

Finally, the April 2026 Workshop incident is required reading for any admin curating a mod list: fourteen mods containing heavily obfuscated malicious code were distributed through the Workshop before being banned, installed on hundreds to thousands of machines [6]. That exploit affected Build 42 branches only — "Build 41 was not vulnerable to this specific issue" — but B41 received its own security patch the same day for a separately identified vulnerability [5] [6]. The lesson for a legacy41 operator is not "B41 is safe"; it is that the mod supply chain is an attack surface on every build, and a frozen server with an unfrozen mod list is not actually frozen.

## Lifespan: what the record supports, and what it does not

What can be said with citations: The Indie Stone created legacy41 deliberately and publicised it in three consecutive launch-window communications [1] [2] [3]; it shipped security patches to B41 as recently as April 2026 [5]; its stated 2026 roadmap is entirely B42-shaped — hotfixes, a patch aimed at late-game feedback, mapping/animation tool releases, and a "Build 42 Support Update" through the rest of 2026 [1]; its stated priority when security work forced triage was "Build 42 stable, and future content updates" [4]; and it has already removed older legacy version branches it could not afford to keep patched, while explicitly declining to commit to their return [4].

What cannot be said: any end-of-support date, any commitment to keep legacy41 available for a defined period, or any statement that it will be retired. No primary source this document could locate makes any such commitment in either direction. Community predictions on both sides circulate widely and are quarantined below (Claim 1). The planning posture that follows from the evidence is in Practical Guidance.

# B41 vs B42 Delta

Not applicable — single-build document. This runbook covers the B41 (legacy41) branch only; the cross-build comparison it would otherwise carry lives in the sibling documents. `admins-foundation` maps the branch split, save incompatibility and operational differences at overview level; `admins-server-ini-reference` carries the key-by-key B41-era vs B42-era configuration delta; `admins-backups-migration` documents why no save crosses the B41→B42 boundary. B42-side facts cited here (release date, incompatibility statements, client switch instructions) appear in the Reference section with their primary citations [1] [2] [3].

# Practical Guidance

## Day 0 — commit to the branch, in writing

1. **Pin the server.** Reinstall/validate with the beta flag — inside SteamCMD, set `force_install_dir <path>`, then `login anonymous`, and then run the load-bearing line: `app_update 380870 -beta legacy41 validate`. On Linux, bake the flag into `update_zomboid.txt` as shown in Reference so it is impossible to update without it.
2. **Brief the players, with the exact clicks.** Publish the three-step client instruction (Steam library → right-click Project Zomboid → Properties → "Game Versions & Betas" → `legacy41`) in your Discord/MOTD *before* they need it, plus one line for the player who already updated: same menu, same selection, then let Steam download and restart the client. Both procedures are official [2] [3].
3. **Write the branch into your ops docs.** Server name, branch, update command, and the rule "no update without the `-beta legacy41` flag". The single worst legacy41 failure is a routine update that silently lands 42.20 on a B41 world.

## Steady state — the recurring duties

- **Keep updating.** Schedule the branch-pinned SteamCMD update regularly and after every official security announcement. The 2026 record shows B41 receives security patches with no advance notice [4] [5]; an unpatched "frozen" server is the worst of both worlds.
- **Watch the announcement feed.** The Steam news feed for app 108600 is where every 2026 B41 hotfix was announced [4] [5] [6]; check it (or mirror it via the ISteamNews API, Further Reading) as part of your weekly routine.
- **Use B41-era documentation for configuration.** Before applying any settings guide, check its build vintage against `admins-server-ini-reference`'s per-key build tags; remember the loot-respawn keys are `.ini`-side on B41, and ignore `AntiCheat*`/`Backups*` advice written for B42.
- **Run the standard backup runbook.** Nothing about legacy41 changes `admins-backups-migration`'s procedures; if anything, a branch with an uncommitted future raises the value of cold, off-machine backups of the whole `Zomboid` tree.

## Mod-list curation on legacy41

- **Prefer mods whose items still ship the B41 flat structure** (a `media/` folder at the mod root) and whose Workshop pages carry the "Build 41" tag [11] [12]; verify structure over tags when they disagree.
- **Stage every mod update.** Test Workshop updates on a copy of the server before they reach production — an author's B42-focused update is the ecosystem event most likely to break your server without any action on your part (Claim 3).
- **Treat the mod list as your active attack surface.** After the April 2026 incident [6], audit additions: prefer established authors, read recent changelogs and comments, and be suspicious of freshly uploaded packs of popular content.
- **Record Workshop ID + Mod ID pairs** for everything you run, so you can rebuild the `WorkshopItems=`/`Mods=` lists from documentation rather than memory (the pairing mechanics are in `admins-foundation` and `admins-server-ini-reference`).

## Planning posture on lifespan

Plan as if legacy41 continues but is not guaranteed: keep full cold backups (world + config + database) that would let you re-host or hand off the community; keep your players' branch instructions permanently posted, because every new player joins from the B42 default; and revisit the decision at each official roadmap post. Do not build multi-year commitments on an uncommitted branch, and do not panic-migrate off a branch that is demonstrably still receiving security care [4] [5].

# Common Pitfalls & Troubleshooting

- **Routine update hopped the server to 42.20.** The update command lacked `-beta legacy41`; SteamCMD's default branch is now Build 42 [3] [7]. Re-run with the flag and validate. The world data is untouched by the binary swap — but do not boot a 42.20 server against a B41 world; restore discipline per `admins-backups-migration`.
- **Player "can't join since the update".** Their client auto-updated to 42.20 because `legacy41` is opt-in [2] [3]. Fix is client-side only: Properties → Game Versions & Betas → `legacy41`, wait for the download, restart [3].
- **Player picked `42.19` instead of `legacy41`.** Wrong branch — that channel preserves unstable 42.19 saves, not Build 41 [1] [2]. Same menu, correct selection.
- **Config edits do nothing.** Check the build vintage of the guide you followed: B42-only keys fail silently in a B41 `.ini`, and on B41 the loot-respawn settings are `.ini` keys, not SandboxVars entries [9] [10].
- **Mods stopped working after a Workshop update.** Likely an author restructuring for B42; check whether the item still contains a B41 flat `media/` layout [11], and see Claim 3 before assuming foul play. Roll back by pinning a known-good local copy on a test box while you contact the author.
- **Assumed no updates were needed because "B41 is done".** 41.78.19 was a security-vulnerability update [5]; treat update discipline on legacy41 exactly as seriously as on stable.
- **Trusting Workshop build tags as compatibility proof.** Tags are author-set filter metadata [12]; the mod's actual folder structure and changelog are the evidence.

# Community Notes & Unverified Claims

## Claim 1 — legacy41 will be retired soon / will be supported for years

- **Claim:** Community discussion (Steam forums, Reddit, admin Discords) confidently predicts legacy41's future in both directions: that The Indie Stone will pull the branch once B42 stabilises, or conversely that it will remain patched "like B40's branch" for years.
- **Why unverified:** No primary source commits to any end-of-support date or continuation guarantee. The closest primary evidence points both ways: B41 received security patches as late as 2026-04-08 [5], while the studio removed *older* legacy version branches it could not keep patched and declined to commit to restoring them, citing B42 as the priority [4].
- **Confidence:** Low. Every specific prediction is speculation; the only defensible statement is that the branch's future is uncommitted.

## Claim 2 — A 42.20 client that targets a legacy41 server is refused at connect with a version-mismatch error

- **Claim:** Community reports describe a mismatched client failing at the connection stage with a version/mismatch message (rather than, say, crashing mid-join), which is why admins routinely diagnose "can't join since the update" as a branch problem sight unseen.
- **Why unverified:** The primary record establishes that builds must match (owners move "(and your players)" together [1] [2]) and documents the file-checksum kick for mismatched Lua [9], but no primary source describes the exact client-side failure mode and message text for a cross-build connection attempt.
- **Confidence:** Medium. The behaviour is universally reported and the mechanism is consistent with the documented build-matching design, but the specific refusal semantics are unverified against a primary source or first-hand test.

## Claim 3 — B42-focused Workshop updates routinely break mods on legacy41 servers

- **Claim:** Admin communities report that since Build 42's unstable cycle, Workshop items updated for B42 sometimes stop working on B41 — attributed to authors removing or abandoning the flat B41 `media/` layout when restructuring, with clients and servers auto-receiving the updated item.
- **Why unverified:** The structural half is primary-adjacent — the pinned Mod structure page documents that the B41 flat layout and the B42 versioned layout coexist in one item and are isolated, which means removal of the flat layout would remove the item's B41 content [11] — but no primary source documents the reported breakage pattern, its frequency, or the update-propagation behaviour on a live legacy41 server.
- **Confidence:** Medium. Mechanically plausible and consistent with the cited structure rules, widely reported, but resting on community accounts; the staging advice in Practical Guidance is cheap insurance either way.

# Risks & Caveats

- **41.78.20 is single-sourced.** Its existence and 2026-07-29 date rest on the wiki's Build 41 version history alone [8]; no announcement, patch note, or contents description was found. If a primary surfaces (or the wiki entry proves wrong), this document's version table changes.
- **The B41 configuration picture inherits an incomplete page.** The B41-era settings revision self-describes as needing improvement [10]; "B41-only" and "B42-only" statements here are documentation facts, not verified game-code facts (see `admins-server-ini-reference`, Claim 1).
- **The hotfix timeline is announcement-shaped.** 41.78.17's exact date rests on the wiki table [8] plus the announcement's description of the patch wave [4]; only .18 (as "Default Public Version") and .19 are named directly in announcements [4] [5].
- **Post-42.20 drift.** The wiki pages cited were captured in the 42.20 launch window; the Dedicated server and Mod structure pages will continue evolving B42-ward, and their B41 content may thin over time. Pinned revision IDs in References protect this document's citations, not the live pages.
- **Steam announcement URLs bot-block.** All primary citations were content-verified through the ISteamNews API mirror per project source policy; the steamcommunity.com URLs 403 automated checkers (allowlisted WARN in the link gate).
- **Lifespan honesty.** Nothing in this document should be read as an assurance the branch persists; the studio's only relevant commitments are quoted in Reference, and they concern B42.

# Verification Steps

1. **Confirm the branch primaries:** query `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0` and read "BUILD 42 STABLE PLANS" (2026-07-24), "B42 CHECKLIST" (2026-07-28) and "Build 42.20.0 Stable Released" (2026-07-29) for the legacy41/42.19 instructions and incompatibility statements, and "Stable(41.78.19) + UNSTABLE(42.16.3) Hotfixes Released" plus "Patching a Zero Day Exploit" (both 2026-04-08) and "[Updated 2026-03-20] Important Security Updates" for the maintenance-line record.
2. **Confirm the branch exists and installs:** in SteamCMD, log in anonymously and run `app_update 380870 -beta legacy41 validate` against a scratch directory; verify the installed server reports a 41.78.x version at startup, and record which exact version the branch currently serves (this also resolves the 41.78.20 question first-hand).
3. **Confirm the client path:** on a test Steam account, select `legacy41` under Properties → Game Versions & Betas, verify the client downloads and reports Build 41.78.x on the main menu, then switch back to the default branch and confirm it returns to 42.20.
4. **Test the mismatch behaviour (resolves Claim 2):** point a 42.20 client at the scratch legacy41 server and record where the connection fails and with what message.
5. **Verify the B41 config surface:** on the scratch legacy41 server, generate a fresh `servertest.ini` and check it against `admins-server-ini-reference`'s B41 rows — presence of the B41-only keys, absence (or undocumented presence) of `AntiCheat*`/`Backups*`, and the loot-respawn keys in the `.ini`.
6. **Verify the mixed mod structure:** subscribe the scratch server and a test client to a Workshop mod whose item contains both a flat `media/` folder and `common/` + `42/` folders, and confirm the B41 server loads the flat side [11].
7. **Verify the Workshop tags:** open `https://steamcommunity.com/workshop/browse/?appid=108600` in a browser and confirm "Build 41" and "Build 42" appear as selectable filter tags [12].

# Open Questions

- What does 41.78.20 actually contain, and why did it ship without an announcement on B42's launch day [8]? A patch note, dev post, or first-hand server-version check (Verification step 2) would resolve it.
- Will The Indie Stone state any support policy for legacy41 — even a soft one — as the B42 hotfix wave settles and the "Build 42 Support Update" work proceeds [1] [4]? (Claim 1 hangs on this.)
- What is the exact cross-build connection-refusal behaviour (Claim 2)? Verification step 4 resolves it empirically.
- How much of the B41 Workshop catalogue still ships a functional flat `media/` layout post-42-stable, and at what rate is it decaying (Claim 3)? A structured sample of top "Build 41"-tagged items would quantify it.
- Does the legacy41 branch serve identical binaries to the pre-switch default branch, or has it diverged (e.g., 41.78.20)? Comparing depot manifests via SteamCMD across time would answer it.

# References

**Primary Sources**

- [1] **The Indie Stone** — *BUILD 42 STABLE PLANS* (Steam announcement, 2026-07-24; retrieved via the ISteamNews API mirror, app 108600). https://steamcommunity.com/games/108600/announcements/detail/1839041357029453. Accessed 2026-07-31.
- [2] **The Indie Stone** — *B42 CHECKLIST* (Steam announcement, 2026-07-28; retrieved via the ISteamNews API mirror). https://steamcommunity.com/games/108600/announcements/detail/1839041357038237. Accessed 2026-07-31.
- [3] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29; includes the "switch back to Build 41" client instructions; retrieved via the ISteamNews API mirror). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259. Accessed 2026-07-31.
- [4] **The Indie Stone** — *[Updated 2026-03-20] Important Security Updates* (Steam announcement, 2026-03-18, updated 2026-03-20; names 41.78.18 as the then-current default public version and documents the legacy-branch removals and `outdatedunstable` policy; retrieved via the ISteamNews API mirror). https://steamcommunity.com/games/108600/announcements/detail/1827626365750608. Accessed 2026-07-31.
- [5] **The Indie Stone** — *Stable(41.78.19) + UNSTABLE(42.16.3) Hotfixes Released* (Steam announcement, 2026-04-08; retrieved via the ISteamNews API mirror). https://steamcommunity.com/games/108600/announcements/detail/1829528821304362. Accessed 2026-07-31.
- [6] **The Indie Stone** — *Patching a Zero Day Exploit* (Steam announcement, 2026-04-08; the Workshop malware incident, affected-mod list, and the B42-only scope statement; retrieved via the ISteamNews API mirror). https://steamcommunity.com/games/108600/announcements/detail/1829528821304702. Accessed 2026-07-31.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [7] **PZwiki** — *Dedicated server* (revision 1443349; page versioned against 42.20.0; "Running Legacy Builds" section). https://pzwiki.net/w/index.php?title=Dedicated_server&oldid=1443349. Accessed 2026-07-31. Fact-only source.
- [8] **PZwiki** — *Build 41* (revision 1443631; version-history table listing 41.78.17 through 41.78.20 with dates). https://pzwiki.net/w/index.php?title=Build_41&oldid=1443631. Accessed 2026-07-31. Fact-only source.
- [9] **PZwiki** — *Server settings* (revision 1443167; page versioned against 42.20.0). https://pzwiki.net/w/index.php?title=Server_settings&oldid=1443167. Accessed 2026-07-31. Fact-only source.
- [10] **PZwiki** — *Server settings* (revision 157571; page versioned against 41.78.16, last edited 2023-10-22) — also preserved at https://web.archive.org/web/20231028101749/https://pzwiki.net/wiki/Server_settings. https://pzwiki.net/w/index.php?title=Server_settings&oldid=157571. Accessed 2026-07-31. Fact-only source.
- [11] **PZwiki** — *Mod structure* (revision 1443271; B41 flat layout, B42 `common/` + versioning folders, and the "Mixing build 41 and 42" coexistence rules). https://pzwiki.net/w/index.php?title=Mod_structure&oldid=1443271. Accessed 2026-07-31. Fact-only source.

**Secondary & Corroborating**

- [12] **Steam Workshop (Spiffo's Workshop)** — Project Zomboid Workshop browse page, app 108600 (author-set "Build 40" / "Build 41" / "Build 42" filter tags observed in the tag list). https://steamcommunity.com/workshop/browse/?appid=108600. Accessed 2026-07-31.

**Community & Creator**

- None cited. Claim attributions above name where the claims circulate; no community URL met the citation bar.

**Further Reading**

# Further Reading

- The ISteamNews mirror used to content-verify every primary announcement: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=100&maxlength=0
- Valve's SteamCMD documentation (beta-branch selection mechanics): https://developer.valvesoftware.com/wiki/SteamCMD
- The official blog / Thursdoid feed (bot-blocks automated checkers; read in-browser): https://projectzomboid.com/blog/
- gorcon/rcon-cli — RCON tooling that works identically on legacy41 and 42.20 servers: https://github.com/gorcon/rcon-cli

# Related Documents

- `admins-foundation` — the parent overview: the branch picture, install paths, ports, memory and tooling this runbook assumes.
- `admins-backups-migration` — the backup/restore/migration runbook a legacy41 server should run unchanged; owns the save-incompatibility and branch-strategy detail from the data side.
- `admins-server-ini-reference` — the key-by-key `.ini` reference whose pinned B41-era revision underwrites this document's configuration-surface section.
- `lore-foundation` — what the Build 41 world your community is preserving actually is.
- `meta-style-guide` — the style rules this document conforms to.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-31 | KB Pipeline (virtual agent) | Initial draft. | — |
