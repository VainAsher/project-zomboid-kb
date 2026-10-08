# Roadmap — Project Zomboid Knowledge Base

## Stage 0 — Bootstrap (this repo) ✅

Chassis scaffolded, reference-genre gates adapted, build-tag gate live,
license-hygiene gate live (trivially passing until the pzwiki corpus lands),
taxonomy proposed. **Hard stop at the human approval gate.**

## Stage 1 — Ingest + activate remaining deterministic gates

- Pull Umbrella + pz-zdoc; generate B41 and B42 API indices; pin commits.
- Snapshot needed pzwiki pages via MediaWiki API into `sources/pzwiki/`
  (plain text + revision-id provenance) — this arms the license-hygiene gate.
- Extract reference server.ini + SandboxVars schemas per build.
- New gates: `check_api_exists.py` (Modder docs vs pinned index per build),
  `check_server_settings.py` (Admin docs vs schema, values in range).
- Stand up (homelab, per spec): B42.20 dedicated server + legacy41 server for
  first-hand verification.

## Stage 2 — Seed the tracks (post-approval), ROI order

1. **Players + Admins** — largest, most launch-sensitive audience.
2. **Modders** — after the Umbrella commit is pinned and indices generated.
3. **Creator** — curated views + content calendar once the others have substance.

Full dual coverage: every entity documented for both B41.78 and B42.20
(`build: both` with substantive delta, or paired per-build docs where the
builds genuinely diverge, e.g. server runbooks).

## Stage 3 — Freshness automation

Done 2026-10-08: `scripts/check_freshness.py` (pinned builds vs the Steam
feed), `scripts/watch_umbrella.py` (Umbrella pins vs upstream tags, including a
moved tag), `scripts/build_entity_map.py` + `sources/entity_aliases.json`
(patch-note line -> probable documents), `scripts/requeue.py` (version, review
date, Umbrella and patch-note signals -> a worklist), and
`.github/workflows/freshness.yml` (daily run, run summary, one self-closing
`freshness` issue). Still open: a buildid watcher (needs SteamCMD or an
unofficial API), Workshop item changelog watchers (needs a tracked-item list)
and a blog watcher (the blog is already mirrored in the Steam feed).

- Watchers: Steam news API (app 108600) + blog + `steam_dedicated` buildid;
  Umbrella/pz-zdoc repos; Workshop changelogs for tracked mods.
- Changelog → entity map → re-queue affected docs; stale `sources_verified`
  re-queues via review_due.
- Cut `kb-release-YYYY.MM.DD` tags pinned to game build + Umbrella commit
  after each hotfix wave.

## Stage 4 — Homelab publishing (deferred by decision)

GitHub CI/Pages stays the QA + publishing path for now. Later: add a Gitea
remote, wire Wiki.js git storage to it, human gate = Gitea PR review.

## Benchmarks that change the plan

- **B42 Support Update / official modding guide ships** → reprioritize Modder
  track; re-pin API indices.
- **WorldZed/TileZed/AnimZed public release** → spin up a map/anim-modding
  sub-track.
- **Public server gains a stable player base** → escalate Admin
  performance/backup docs and Creator server-drama formats.
- **License-hygiene flags fire** → tighten the n-gram threshold before
  publishing anything.
