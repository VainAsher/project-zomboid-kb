---
id: meta-source-registry-companion
title: "Source Registry Companion: How Each Source Is Reached, What Is Ingested and What Is Blocked"
version: 0.2.0
status: in-review
confidence: Medium
category: Meta
topic: "Source registry companion"
build: both
document_type: reference
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [meta-style-guide, meta-release-versioning-policy, modders-lua-api-surface, modders-modinfo-modid-conventions, admins-server-ini-reference, creator-channel-competitor-map]
tags: [meta, sources, ingestion, bot-block, umbrella, scriptsdocs, pzwiki, licensing]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | meta-source-registry-companion |
| Version | 0.2.0 |
| Status | in-review |
| Confidence | Medium |
| Category (track) | Meta |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 (pins and index counts re-read 2026-10-07) |

# Executive Summary

`SOURCE_REGISTRY.md` ranks the sources this knowledge base may use. It does
not say how a worker actually gets a byte out of each one on a given day, what
the repository already holds locally, or what silently fails. This companion
records that operational layer, written from the repository's state on
2026-10-07 and from what workers hit while building the first nine waves of
documents.

The headline findings: Steam announcements are best read through the public
news API rather than the bot-blocked announcement pages [1]; the Umbrella
type stubs are pinned per build and reduced to two committed symbol indices
(1,498 classes for B41, 4,124 for B42 at 42.21.0), with the previous 42.20.0
B42 index archived beside them [2]; the upstream Umbrella 42.20.0 tag was
later moved to a different commit, so pins are recorded by commit [2]; the
community-run ScriptsDocs site was stamped 42.21.0 when opened on 2026-10-07,
which now matches the Umbrella pin [3] [4]; the pzwiki license-gate corpus is
67 snapshot pages whose prose is gitignored and whose provenance manifest is
committed [5]; the Indie Stone forum's 42.21 patch-notes thread was readable
through a browser page-text extraction [12], while the migration-guide PDFs
need a signed-in download and are deliberately not stored in the repository
[6]; and the link-checker allowlist now also holds `support.discord.com`,
`pzwiki.net` and `developer.valvesoftware.com`.

Confidence is Medium. Repository facts are directly inspectable, but the
live-access behaviour (which sites challenge which clients, and when) is
intermittent and was observed on a single day.

# Key Takeaways

- Read TIS announcements through the Steam news API for app 108600, not the
  announcement pages, which 403 automated clients. *(cited)* [1]
- Umbrella is pinned by release tag and commit per build; B41 is 41.78.16
  and B42 is 42.21.0 (commit `13d01f9`), with 42.20.0 kept as `B42_previous`,
  and no newer B41 stub tag exists. The upstream 42.20.0 tag was later moved
  to commit `98f50ae`, so pin by commit, not tag. *(cited, repo file)* [2]
- Two committed API indices back the API-existence gate: B41 has 1,498
  classes, 240 events and 664 globals; B42 (42.21.0) has 4,124 classes, 244
  events and 930 globals. The archived 42.20.0 index has 4,266 classes, 234
  events and 947 globals. *(repo file counts)*
- ScriptsDocs is community-maintained; its pages were stamped 42.21.0 when
  opened on 2026-10-07, equal to the Umbrella pin since the re-baseline. Treat
  a ScriptsDocs fact as corroboration, not as a pin. *(cited, opened
  2026-10-07)* [3] [4]
- The pzwiki license corpus is 67 manifest entries; the `.txt` prose is
  gitignored and never published, the manifest is committed. *(repo files)* [5]
- The 42.13 migration-guide PDFs came from a signed-in browser download on
  2026-10-07 and are not in the repo because they are TIS copyright. *(cited)* [6]
  The 42.21 patch-notes thread (topic 101693) needed no sign-in: its text was
  read through a browser page-text extraction. *(cited)* [12]
- The link-checker allowlist now includes `support.discord.com`,
  `pzwiki.net` and `developer.valvesoftware.com`, so a challenge from those
  hosts is a WARN, not a FAIL. *(repo file)*
- Hosting-company KBs corroborate only and are never the sole source of a
  hard number. *(repo rule)* [8]

# Purpose

A worker or maintainer who has read `SOURCE_REGISTRY.md` still has to decide
which command to run, which URL form to cite, and what to do when a source
refuses an automated client. This document answers those operational
questions so the next worker does not rediscover them, and lists which
workarounds are evidenced in the repository versus merely suggested.

# Scope

Covered: per-source-class access routes as practised in this repo; the
link-checker bot-block allowlist; the Umbrella pins and the extracted and
archived indices under `sources/schemas/`; the pzwiki ingestion path and the corpus
the license gate reads; and a table of blocked or unverified sources with
workarounds that the repo itself evidences.

Not covered: the ranked authority table (see `SOURCE_REGISTRY.md`), the
license reasoning (see meta-style-guide), and release tagging (see
meta-release-versioning-policy). Discord is covered only as far as the repo
shows; no Discord archive has been built.

# Definitions

- **Pin** — a record in `sources/pins.json` fixing an external source to a
  release tag and commit for a build.
- **API index** — a JSON symbol list extracted from the pinned Umbrella
  stubs, used as ground truth by `scripts/check_api_exists.py`.
- **Allowlisted host** — a host in `BOT_BLOCK_HOSTS` in
  `scripts/check_links.py`; a non-2xx/3xx answer from it is a WARN, not a
  FAIL.
- **License corpus** — the local pzwiki plain-text snapshots that
  `scripts/check_license_hygiene.py` compares documents against.

# Build Applicability

The access routes are build-independent, but the pinned artefacts are
per-build. The repository pins one Umbrella tag per build; the B41 baseline
follows the legacy41 maintenance line, while the Umbrella B41 stub pin stays
at 41.78.16 because no newer B41 stub tag exists [2]. The 2026-10-07
re-baseline re-read `sources/pins.json`, recounted both committed indices and
the archived one, re-read `BOT_BLOCK_HOSTS`, and reviewed the 41.78.21 and
42.21 announcements and the 42.21 forum thread [10] [11] [12]; it did not
re-open ScriptsDocs, the Steam news API endpoint or the pzwiki API.

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 (Umbrella pin) | Latest primary-attested hotfix is 41.78.21 per the pins file and its announcement [2] [10]; stub pin unchanged |
| B42 (stable) | Yes | 42.21 (Umbrella 42.21.0) | Stable since 2026-09-28 [11]; ScriptsDocs observed at 42.21.0 on 2026-10-07 [3] |

# Reference

## Source classes: how each is reached in practice

| Source class | Actual access route | What is held locally | Caveat observed |
|--------------|--------------------|----------------------|-----------------|
| TIS announcements and patch notes | Steam news API, `ISteamNews/GetNewsForApp/v2`, app 108600; cite the `steamcommunity.com` announcement URL [1] | Nothing; fetched on demand | The announcement pages themselves 403 plain clients and sit on the allowlist; the API answered 200 on 2026-10-07 [1] |
| Umbrella type stubs | Git checkout at the pinned commit, then `scripts/extract_api_index.py` | Two JSON indices in `sources/schemas/` plus the archived 42.20.0 B42 index | Extraction verifies HEAD against the pin when git is available; the upstream 42.20.0 tag was moved after the first pin, so use the commit [2] |
| Server settings schema | `scripts/extract_server_schema.py` into `sources/schemas/server-settings.json` | 166 `ini` keys and 277 `sandbox` keys | Feeds the server-setting gate, a different gate from the API one |
| ScriptsDocs (PZ API Docs) | Static site at https://pz-wiki-modding.github.io/PZ-API-Docs/ ; open pages in a browser or with curl [3] | Nothing | Community-maintained; the bare host root returns a GitHub Pages "Site not found" page, only the `/PZ-API-Docs/` path works |
| pzwiki | MediaWiki Action API `action=parse` via `scripts/ingest_pzwiki.py`, provenance by revision id [5] | 67 snapshots plus a manifest | Challenge or 403 behaviour is intermittent; see the pzwiki section |
| TIS forum | Browser only; thread text readable through a browser page-text extraction (the 42.21 patch-notes thread), attachments need sign-in [6] [12] | Not stored | Host is on the bot-block allowlist; attachment PDFs are TIS copyright |
| Official Discord | Not reachable by the link checker; deep links are reliably dead for bots | No archive built | The registry specifies a local archive store; none is populated |
| Hosting-company KBs | Read in a browser when a checker 403s [8] | Nothing | Corroborate-only; never sole source for a hard number |

## Steam news API

The route the repo's documents use to content-verify TIS announcements is the
public endpoint `https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0`
[1]. A request with a small `count` returned HTTP 200 when tried on
2026-10-07 [1]. The citation convention is to cite the human-facing
`steamcommunity.com/games/108600/announcements/detail/<id>` URL and record
that the content was read through the API mirror, as the existing documents
do [7]. Raising `count` (the repo's documents use 25 and 100 in their
verification steps) reaches older posts [1].

## Umbrella pins and the extracted indices

`sources/pins.json` pins the Umbrella repository at release tag 42.21.0
(commit `13d01f9ee58fa48773553920db56d06f0005e7f8`) for B42 and tag 41.78.16
(commit `fa2e7e19799740b57902f1cb4e989225c295c05e`) for B41, with
`pinned_at` 2026-10-07 [2]. The original B42 pin, tag 42.20.0 (commit
`58204fc47895ba249592519cedecc7cfbaaebd60`), is kept under `B42_previous`; the
file notes that the upstream 42.20.0 tag was later moved to `98f50ae` (two
commits on, "Update lua", 2026-07-31), so the pin is by commit and the
original index is archived at
`sources/schemas/archive/api-index-B42-42.20.0.json` [2]. The same file
records that the B41 baseline follows the legacy41 maintenance line, that
41.78.21 (legacy hotfix, 2026-08-26) is the latest primary-attested B41 build
[2] [10], and that 41.78.20 is attested only by pzwiki version pages pending
primary confirmation [2]. The earlier primary-attested value, 41.78.19, was a
security-only release announced 2026-04-08 [7].

`scripts/extract_api_index.py` reads the LuaLS stub library at the pinned
commit and writes one index per build. The committed indices contain:

| Index file | Release tag | Classes | Events | Globals |
|------------|-------------|---------|--------|---------|
| `sources/schemas/api-index-B41.json` | 41.78.16 | 1,498 | 240 | 664 |
| `sources/schemas/api-index-B42.json` | 42.21.0 | 4,124 | 244 | 930 |
| `sources/schemas/archive/api-index-B42-42.20.0.json` (archived) | 42.20.0 | 4,266 | 234 | 947 |

`scripts/check_api_exists.py` consumes those files: a code-span symbol in a
Modders document must exist in the index for a build the document's tag
covers, and a line tagged *(B41)* or *(B42)* is checked against that build
only. The gate inspects only Category Modders documents.

## ScriptsDocs

ScriptsDocs is published at https://pz-wiki-modding.github.io/PZ-API-Docs/
[3]. When opened on 2026-10-07 the landing page, the ModInfo page and the
`item` script page were all titled "PZ API Documentation 42.21.0" [3] [4].
An earlier KB document recorded the same ModInfo page as titled 42.20.0 [4],
so the site moves under the KB between research dates. At that time the
Umbrella B42 pin was still 42.20.0; the pin has since moved to 42.21.0 [2], so
the two now carry the same version label. This document did not re-open
ScriptsDocs after the re-baseline.

## Link checker allowlist

`scripts/check_links.py` fetches every URL with `curl` (GET, follow
redirects, 40-second cap, two retries, user agent `Mozilla/5.0
(kb-link-checker)`) and retries once more on a connect failure. A host on
`BOT_BLOCK_HOSTS` that fails produces a WARN; any other failing host is a
FAIL and exits 1. The allowlist holds these hosts:

| Host | Why allowlisted (per the script's comments) |
|------|---------------------------------------------|
| `projectzomboid.com`, `www.projectzomboid.com` | Official blog, known bot detection |
| `theindiestone.com`, `www.theindiestone.com` | Official forums, intermittent challenges |
| `store.steampowered.com` | Regional and age gates confuse plain GETs |
| `steamcommunity.com` | Workshop and guide pages sometimes challenge |
| `discord.com`, `discord.gg` | Invite and channel links never return 200 to bots |
| `support.discord.com` | Discord help centre, 403s non-browser agents |
| `map.projectzomboid.com` | Official community map, 403s non-browser agents |
| `pzwiki.net` | Intermittent Cloudflare challenge on API and page fetches |
| `developer.valvesoftware.com` | Valve developer wiki, challenges bots |
| `legionhosting.net` | Hosting-company KB, 403s bots; corroborate-only source |

By default the checker scans `docs`, `SOURCE_REGISTRY.md`, `GLOSSARY.md` and
`MASTER_INDEX.md`. Earlier in the project `pzwiki.net` and
`developer.valvesoftware.com` were not allowlisted and a challenge from
either would have been reported as a dead link; they are allowlisted now, so
a challenge from them is a WARN that still needs a human to confirm the URL in
a browser.

## pzwiki ingestion and the license-gate corpus

`scripts/ingest_pzwiki.py` calls https://pzwiki.net/w/api.php with
`action=parse`, `prop=text|revid` and redirect-following, strips tags, and
writes one `.txt` per page with a header carrying title, revision id, fetch
date and the CC BY-NC-SA 3.0 notice [5]. Calls are sequential with a default
one-second delay, a custom user agent, and a 60-second timeout. A page that
errors is skipped and logged. Partial runs merge into the existing manifest
so earlier provenance is never dropped.

The corpus state on 2026-10-07:

| Item | Value |
|------|-------|
| Manifest entries in `sources/pzwiki/manifest.json` | 67 |
| Titles in the ingester's embedded default list | 71 |
| Default titles with no manifest key of that name | 5 (Farming, Animals, Husbandry, Animal care, Brewing) |
| Manifest key not in the default list | 1 (Animal) |
| Fetch dates | 2026-07-30 (57 pages), 2026-07-31 (10 pages) |
| `.txt` snapshot files on disk | 67 |
| Copyright page revision recorded | PZwiki:Copyrights, revision 1156861 |

The `.txt` snapshots are excluded by `.gitignore`; the manifest is not, so
provenance is committed while the licensed prose stays local. The manifest
file is saved with a UTF-8 byte-order mark, so a strict `json.load` on it
fails unless opened as `utf-8-sig`. `scripts/check_license_hygiene.py`
compares each document's word 8-grams against every corpus file, skips code
fences, URLs, quoted spans and blockquotes in the document, and treats an
n-gram dominated by numbers and unit words as data. With no corpus present
it passes trivially, so a fresh clone without the gitignored snapshots is not
protected by this gate.

## TIS forum and the 42.13 Migration Guide

The 42.13 Modding Migration Guide thread is a forum post by moderator nasKo
dated 2025-12-11 [6]. Its attached PDFs were obtained on 2026-10-07 by a
signed-in browser download, and an existing Modders document cites the
attachment without a direct file URL [6]. The PDFs are TIS copyright and are
not stored in the repository, so a later worker must repeat the signed-in
download to re-read them. Only facts from them are used, cited to the thread.

The 42.21 patch-notes thread (topic 101693) behaves differently: its first
post, by Rockjaw on 2026-09-23, was readable through a browser page-text
extraction without the signed-in download that the Migration Guide PDFs need
[12]. The captured text is facts-only working material for the re-baseline and
is not stored in the repository; documents cite the thread URL.

# B41 vs B42 Delta

The access routes do not differ by build, but the artefacts behind them do.

| Concern | B41 (legacy41) | B42 (stable) |
|---------|----------------|--------------|
| Umbrella stub pin | Tag 41.78.16 *(B41)*; no newer B41 stub tag exists [2] | Tag 42.21.0, commit `13d01f9`; previous 42.20.0 kept, upstream tag later moved *(B42)* [2] |
| Extracted API index size | 1,498 classes, 240 events, 664 globals *(B41)* | 4,124 classes, 244 events, 930 globals at 42.21.0; archived 42.20.0 index 4,266, 234, 947 *(B42)* |
| Latest primary-attested build | 41.78.21, legacy hotfix, 2026-08-26 *(B41)* [2] [10] | Stable 42.21, 2026-09-28 *(B42)* [2] [11] |
| ScriptsDocs coverage | Documents the current B42 line; no B41 edition observed [3] | Stamped 42.21.0 on 2026-10-07, equal to the Umbrella pin since the re-baseline *(B42)* [3] |
| Migration guide | Not applicable | 42.13 guide covers B42 modding changes *(B42)* [6] |

The class count roughly tripling between the B41 and B42 indices is a fact
about the stub libraries as extracted; this document does not claim it equals
the growth of the game's real API. Likewise the drop from 4,266 to 4,124
classes between the 42.20.0 and 42.21.0 B42 indices says only that the stub
libraries differ; it is not evidence that the game lost that many classes.

# Practical Guidance

- For any TIS announcement, query the Steam news API, read the post there,
  then cite the `steamcommunity.com` detail URL and note the API mirror in
  the reference line, matching existing documents [1] [7].
- Before a Modders worker trusts a ScriptsDocs page, open it and read the
  version in its title; compare against the Umbrella pin in `sources/pins.json`
  and tag the fact as newer-than-pin if they differ [2] [3].
- When re-pinning Umbrella for a release, rerun `scripts/extract_api_index.py`
  for both builds and commit the indices together with the pin change.
- If the pzwiki ingest returns 403 or a challenge, retry later with the
  project user agent rather than switching to scraping rendered pages; the
  ingester merges partial runs, so only the failed titles need repeating.
- For forum attachments, sign in with a browser, download, read, and cite the
  thread; do not copy the file into the repo [6].
- When a checker WARNs on an allowlisted host, open the URL in a browser once
  and record that you did.

# Common Pitfalls & Troubleshooting

| Symptom | Cause (from the sections above) | Workaround |
|---------|--------------------------------|------------|
| ScriptsDocs host root says "Site not found" | The project is served under the `/PZ-API-Docs/` path [3] | Use the path-qualified URL |
| ScriptsDocs fact disagrees with a KB doc dated earlier | The site is re-stamped with newer game versions [3] [4] | Re-open, compare titles, bump the doc at next revision |
| `json.load` fails on the pzwiki manifest | The file starts with a byte-order mark | Open with `encoding="utf-8-sig"` |
| License gate passes instantly with a "no corpus" note | The gitignored `.txt` snapshots are absent | Run `scripts/ingest_pzwiki.py` first |
| A pzwiki or Valve URL reports WARN in the link check | Both hosts are now allowlisted | Verify in a browser; allowlisting a further host is an orchestrator decision |
| Steam announcement URL WARNs | Allowlisted bot-block [1] | Content-verify via the news API |
| A default ingest title is missing from the manifest | Redirects store the real title, and errors skip the page | Check the manifest by the resolved title |

## Known-blocked or unverified sources and the workaround

| Source | Evidence of the block or gap | Workaround evidenced in the repo |
|--------|-----------------------------|----------------------------------|
| Steam announcement pages | Allowlisted in `check_links.py`; documents state the URLs 403 checkers [1] | ISteamNews API mirror for content, announcement URL for the citation [7] |
| projectzomboid.com blog | Allowlisted as known bot detection | Steam mirror of the post, per `SOURCE_REGISTRY.md` |
| theindiestone.com forum | Allowlisted; attachments need sign-in [6] | Signed-in browser download; cite thread, store nothing |
| Discord message links | Registry marks deep links reliably dead for bots; allowlist covers the hosts | Archive quoted text locally and cite the archive; the store is not yet populated |
| pzwiki.net API | 403 observed for a default curl request on 2026-10-07 and 200 for a request carrying a browser-style user agent minutes later | Project user agent, polite delay, merge-on-rerun in the ingester [5] |
| Valve SteamCMD wiki | An existing Admins document records a bot-verification challenge page during its research [9] | Read in a browser; cite as unfetched by automation |
| Hosting-company KBs (legionhosting.net) | Allowlisted; the host 403s bots [8] | Browser read; corroborate-only |
| Umbrella B41 beyond 41.78.16 | `pins.json` states no newer B41 stub tag exists [2] | Keep the 41.78.16 pin and say so |
| Umbrella 42.20.0 tag | `pins.json` records that the upstream tag was moved to `98f50ae` after the first pin [2] | Pin and cite by commit id; keep the archived index |
| 41.78.20 hotfix | Attested only by pzwiki version pages, pending a primary; 41.78.21 is primary-attested [2] [10] | Do not state 41.78.20 as fact; quarantine until a TIS post is found |

# Community Notes & Unverified Claims

## Claim 1 — The pzwiki challenge page appears mainly for rapid sequential requests

- **Claim:** Ingest runs that hit pzwiki quickly are said, by workers' recollection during this project, to be more likely to receive a challenge than slow runs.
- **Why unverified:** Only a single same-day 403-then-200 sequence was observed, and the cause (user agent, rate, or edge-cache state) was not isolated.
- **Confidence:** Low. One observation cannot separate user agent from request rate.

# Risks & Caveats

- Live-access behaviour (challenges, 403s, which hosts answer) was sampled on
  one day and changes without notice.
- ScriptsDocs is a community site; its version stamp moved from 42.20.0 to
  42.21.0 between two KB research dates [3] [4], so any ScriptsDocs-derived
  fact may already be stale against the pin, and it can move again.
- Counts in this document are as of the repository files on 2026-10-07 after
  the 42.21 re-baseline (the 42.21.0 index and `pins.json` were uncommitted
  working-tree changes when this revision was written); re-extracting an
  index or re-ingesting pzwiki changes them.
- The 42.21 forum thread was read via a browser page-text extraction and is
  not archived in the repository [12].
- The signed-in forum download cannot be reproduced by an unattended worker.
- The allowlist is a reviewer convenience, not proof a URL is live.

# Verification Steps

- Open `sources/pins.json` and compare the tags and commits to this document [2].
- Count classes, events and globals in each `sources/schemas/api-index-*.json`
  and in `sources/schemas/archive/api-index-B42-42.20.0.json` (top-level keys
  `classes`, `events`, `globals`).
- Count entries in `sources/pzwiki/manifest.json`, opening it as `utf-8-sig`.
- Run `curl` against the Steam news endpoint and confirm HTTP 200 [1].
- Open https://pz-wiki-modding.github.io/PZ-API-Docs/  and read the page
  title version [3].
- Read `BOT_BLOCK_HOSTS` in `scripts/check_links.py` against the table above.
- Open the forum thread in a signed-in browser and confirm the PDF
  attachments [6].

# Open Questions

- Now that `pzwiki.net` is allowlisted, does the WARN-only treatment risk
  hiding a genuinely dead wiki link? A periodic browser spot-check is the only
  safeguard.
- Should the manifest be re-saved without a byte-order mark?
- When will 41.78.20 receive a primary-source confirmation? 41.78.21 now has
  one [10].
- Is a Discord archive store worth building, given its ephemeral nature?
- Should ScriptsDocs pages be snapshotted with their version stamp per release?

# References

**Primary Sources**

- [1] **Valve / The Indie Stone** — *Steam news API, GetNewsForApp, app 108600*. https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=108600&count=25&maxlength=0 Accessed 2026-10-07 (HTTP 200).
- [2] **PZ-Umbrella** — *Umbrella repository* (pins per `sources/pins.json`: B42 42.21.0, previous 42.20.0, and B41 41.78.16). https://github.com/PZ-Umbrella/Umbrella Accessed 2026-10-07 (HTTP 200).
- [6] **The Indie Stone Forums** — *Modding Migration Guide (42.13)*, first post by nasKo, 2025-12-11, with PDF attachment (sign-in required). https://theindiestone.com/forums/topic/88499-modding-migration-guide-4213/ Accessed 2026-10-07 (host bot-blocks checkers).
- [7] **The Indie Stone** — *Stable(41.78.19) + UNSTABLE(42.16.3) Hotfixes Released* (Steam announcement, 2026-04-08; retrieved via the ISteamNews API mirror). https://steamcommunity.com/games/108600/announcements/detail/1829528821304362 Accessed 2026-10-07.
- [10] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601 Accessed 2026-10-07; host is bot-block allowlisted.
- [11] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07; host is bot-block allowlisted.
- [12] **The Indie Stone Forums** — *42.21 Patch Notes* (topic 101693, first post by Rockjaw, 2026-09-23). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07 via browser page-text extraction; host bot-blocks checkers.

**Fact-Only Sources (no prose reuse)**

- [5] **PZwiki** — *PZwiki:Copyrights* (revision 1156861), reached through the MediaWiki API. https://pzwiki.net/wiki/PZwiki:Copyrights Accessed 2026-10-07. Fact-only source.

**Secondary & Corroborating**

- [3] **PZ-Wiki-Modding** — *PZ API Documentation* (ScriptsDocs, community-maintained; titled 42.21.0 on access). https://pz-wiki-modding.github.io/PZ-API-Docs/ Accessed 2026-10-07.
- [4] **PZ-Wiki-Modding** — *ROOT-ModInfo, PZ API Documentation* (titled 42.21.0 on access). https://pz-wiki-modding.github.io/PZ-API-Docs/scripts/root_files/modinfo.html Accessed 2026-10-07.
- [8] **Legion Hosting** — *Project Zomboid mod troubleshooting* (hosting-company KB, corroborate-only). https://legionhosting.net/kb/project-zomboid/project-zomboid-mod-troubleshooting Accessed 2026-10-07 (host bot-blocks checkers).

**Community & Creator**

- [9] **Valve Developer Community** — *SteamCMD*. https://developer.valvesoftware.com/wiki/SteamCMD Accessed 2026-10-07 (automated retrieval challenged; read in browser).

**Further Reading**

# Further Reading

- `SOURCE_REGISTRY.md` — the ranked source-authority table this companion
  operationalises.
- `sources/pins.json`, `scripts/check_links.py`, `scripts/ingest_pzwiki.py`,
  `scripts/extract_api_index.py` — the files described above.
- `ROADMAP.md` — planned gates.

# Related Documents

- meta-style-guide — genre, build tags and license stance.
- meta-release-versioning-policy — how pins are tied to releases.
- modders-lua-api-surface — consumer of the Umbrella indices.
- modders-modinfo-modid-conventions — cites ScriptsDocs and the migration guide.
- admins-server-ini-reference — consumer of the server-settings schema.
- creator-channel-competitor-map — creator-track source handling.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: refreshed pins, index counts (B42 42.21.0 now 4,124 classes, 244 events, 930 globals; archived 42.20.0 index), the Umbrella tag-move finding, allowlist contents, forum 101693 readability finding; sources [10][11][12]. | — |
