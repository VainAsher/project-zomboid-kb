# Source Registry — Project Zomboid Knowledge Base

Ranked source-authority list. Workers reach for sources in **tier order**;
lower tiers corroborate, never sole-source. Every reference in a document is
classed as: Primary / Fact-Only (pzwiki) / Secondary & Corroborating /
Community & Creator / Further Reading.

## Priority order (summary)

1. Official Indie Stone primaries (blog, Steam announcements, forums, Discord)
2. Code truth (Umbrella stubs, ZomboidDoc-generated indices, game script files)
3. pzwiki.net — **facts only, never prose** (CC BY-NC-SA 3.0)
4. Open-source server/admin tooling repos (MIT etc.)
5. Hosting-company KBs and community guides — corroborate-only
6. YouTube/creator sources — creator-track evidence only, never game-fact sourcing

## Tier 1 — Authoritative primaries

| # | Source | Type | License/attribution | Cadence | Ingestion |
|---|--------|------|---------------------|---------|-----------|
| 1 | projectzomboid.com/blog | Official blog / Thursdoids / patch notes | © The Indie Stone; facts citable, prose not reusable | Irregular (monthly-ish, event-driven) | Rate-limited polling scraper (site has bot detection) or the Steam mirror (#2). Authoritative version/patch source. |
| 2 | steamcommunity.com/app/108600/announcements | Mirror of official posts | © TIS / Valve ToS | Event-driven | Steam news API (`ISteamNews`, app 108600) |
| 3 | theindiestone.com/forums | Dev posts, modding subforum, official mod releases | © TIS / posters | Continuous | Scraper/RSS |
| 4 | The Indie Stone Discord (official) | Modding instructions, MP mod-porting guide, dev Q&A | Ephemeral; quote with attribution + date | Continuous | Read-only archive bot on designated channels (#modding, #announcements); treat as primary-but-ephemeral |

## Tier 2 — Modding API / code truth

| # | Source | Type | License | Cadence | Ingestion |
|---|--------|------|---------|---------|-----------|
| 5 | github.com/asledgehammer/Umbrella | EmmyLua/LuaCATS type stubs (Candle = Java-exposed, PZLuaStubs, PZEventStubs) | Check repo LICENSE before redistribution; citing/validation fine | Active | `git pull`; **pin a commit per KB release**. Machine-checkable ground truth for the API-existence gate. |
| 6 | github.com/cocolabs/pz-zdoc (+ smorimoto fork) | Generates annotated Lua library from an installed game | Check repo LICENSE | On demand | Run against a B41 install and a B42 install → per-build API index |
| 7 | Unofficial JavaDocs (B41, B42) + LuaDocs (Doxygen) | Class/function reference | Community-generated | Per build | Scrape into normalized API index; cross-check against Umbrella |
| 8 | Game script files (installed B41.78 + B42.20 copies) | Item/recipe/sandbox definitions | © TIS — quote minimally, cite path + build | Per patch | Local install; cite `media/scripts/...` path + game version |
| 9 | Steam Workshop (Spiffo's Workshop) | Mod pages, mod.info, changelogs, compat tags | Mod authors' IP — link and cite, never rehost | Continuous | Workshop web API + changelog scraping; key by Workshop ID **and** Mod ID |

## Tier 3 — Fact-only wiki

| # | Source | Type | License | Cadence | Ingestion |
|---|--------|------|---------|---------|-----------|
| 10 | pzwiki.net | Community wiki (MediaWiki) | **CC BY-NC-SA 3.0** (dev art/lore excepted). NonCommercial clause = hard constraint: FACTS ONLY, never prose/tables | Continuous; updating to B42.20 | MediaWiki Action API (`action=query`, `Special:Export`) into `sources/pzwiki/` with revision-id provenance. Cited as "Fact-only source". |

## Tier 4 — Server admin & tooling (mostly open-source)

| # | Source | Type | License | Notes |
|---|--------|------|---------|-------|
| 11 | pzwiki "Dedicated server" + official server docs | server.ini / SandboxVars reference | As #10 / © TIS | Basis for the server-setting gate schema |
| 12 | github.com/Bobagi/Project-Zomboid-Ubuntu-Server | Ubuntu SteamCMD setup (App ID 380870) | Open-source | Canonical for the Linux self-host track |
| 13 | github.com/beyenilmez/pz-admin | RCON desktop admin app | MIT | Preferred over hosting-company panels |
| 14 | zomboid-rcon (PyPI / jmwhitworth) | Python RCON library | MIT | Also used to script setting validation |
| 15 | gorcon/rcon-cli, Tiiffi/mcrcon | Generic RCON CLIs | Open-source | For scripts and docs |
| 16 | Hosting-company KBs (BisectHosting, Shockbyte, XGamingServer, …) | Setup guides, RAM numbers | Marketing-adjacent | **Corroborate-only; never sole-source a hard number** |

## Tier 5 — Community guides / YouTube (secondary)

| # | Source | Use |
|---|--------|-----|
| 17 | Steam community guides | Structure references; many are unstable-era — always check the date vs 42.20 |
| 18 | YouTube channels (ambiguousamphibian, Pr1vateLime, Retanaru, Mattsi, NurseVO, …) | Creator-track evidence and content-gap analysis only; never game-fact sourcing. Subscriber/view numbers are third-party estimates — label as estimates. |

## Known bot-block hosts (checker WARNs, does not FAIL)

`projectzomboid.com`, `theindiestone.com`, `store.steampowered.com`,
`steamcommunity.com`, `discord.com` / `discord.gg`. Prefer the Steam news API
mirror for blog posts and Internet Archive snapshots for ephemeral content.

## Reliably-dead-for-bots (do not cite; use an equivalent)

Discord message deep-links (`discord.com/channels/...`) — archive the quoted
text into the local Discord store and cite that archive entry instead.
