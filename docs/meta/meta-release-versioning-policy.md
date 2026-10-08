---
id: meta-release-versioning-policy
title: "Release and Versioning Policy: Document Versions, kb-release Tags and Game-Build Pins"
version: 1.2.0
status: approved
confidence: High
category: Meta
topic: "Release & versioning policy"
build: both
document_type: policy
created: 2026-10-07
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [meta-style-guide, meta-source-registry-companion, modders-lua-api-surface, admins-server-ini-reference, players-foundation]
tags: [meta, governance, release, versioning, freshness, qa-gates, pins]
game_versions_verified: ["41.78.16", "42.20", "42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | meta-release-versioning-policy |
| Version | 1.2.0 |
| Status | approved |
| Confidence | High |
| Category (track) | Meta |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 41.78.16, 42.20, 42.21 (and the 41.78.21 legacy hotfix announcement) |

# Executive Summary

This document describes how the knowledge base versions and releases itself:
what a document version number means, which front-matter fields record
freshness, what a `kb-release-YYYY.MM.DD` tag pins, how the Build 41
baseline is defined, how the freshness script detects game-build drift, how
stale documents are re-queued, and what each automated QA gate proves and,
just as importantly, does not prove. It is the sibling of
`meta-style-guide`, which covers genre, build tags and licensing; this
document covers the lifecycle that happens after a document is written.

Nearly every claim here is about this repository and can be checked by
opening the named file or running `git log` and `git tag`. Repo facts are
cited by path and, where a change is dated, by git commit id, the same way
`meta-style-guide` does it. The external anchors are the official 42.20
stable announcement [1], which fixes the two-branch situation the policy
manages, the 42.21 stable and 41.78.21 legacy announcements [3] [4], which
the pins now follow, and the Umbrella repository [2], whose release tags are
what the API pins refer to. Confidence is High for the mechanics described.
It would fall if the scripts were changed without a revision of this
document. On 2026-10-07 the pins were moved to 42.21 and 41.78.21 and the
freshness script reports them current; on 2026-10-08 the project owner
approved the re-approval of the six foundation documents and the freeze of
the remaining 35, and the `kb-release-2026.10.08` tag was cut for that
re-baseline (see Reference).

# Key Takeaways

- A document version is semver, validated mechanically for shape only;
  `0.1.0` / `in-review` is the entry state and `1.0.0` is the freeze, cut
  by the orchestrator at a cluster release. *(repo rule and observed
  practice; see Reference)*
- A fact change cuts a new version with a revision-history row, never a
  silent edit (`CLAUDE.md` rule 6). Nothing in the gates checks that a
  revision row exists; this is a human/orchestrator discipline. *(repo
  rule)*
- Two release tags exist as of 2026-10-08: `kb-release-2026.07.30` (the six
  foundation documents) and `kb-release-2026.10.08` (the 42.21 re-baseline,
  all 41 documents at `approved`). Each is an annotated tag whose message
  names the game builds and the Umbrella release tag and commit. Before the
  second tag was cut, 35 documents sat unfrozen at `in-review`.
  *(repo state, `git tag`, `RELEASE_HISTORY.md` and the `status:` fields)*
- `sources/pins.json` pins Umbrella B42 `42.21.0` @ `13d01f9` (previous
  pin `42.20.0` @ `58204fc` kept as `B42_previous`) and B41 `41.78.16` @
  `fa2e7e1`; the B41 game baseline is the legacy41 maintenance line (user
  decision 2026-07-31), with `41.78.21` now primary-attested, but the B41 API
  pin cannot move because no newer B41 stub tag exists. *(repo file)*
- `python scripts/check_freshness.py` exits 0 (current), 1 (fetch error) or
  2 (drift). Earlier on 2026-10-07, before the re-baseline, it exited 2
  (pins 42.20.0 and 41.78.19 against announced 42.21 and 41.78.21); after the
  pins moved it exits 0 ("Pins current"). *(run on 2026-10-07)*
- Green gates prove structure, citation hygiene, name existence and
  link liveness. They do not prove a statement is true, current, or
  correctly interpreted. *(see the gate table)*
- Open policy gaps are real: re-queueing now produces a worklist and a
  tracking issue but a human still does the re-verification, the
  license-hygiene gate compares against an empty corpus in CI (the snapshots are
  gitignored), and the existence gates still pass silently on a local run if
  their schema files are missing (CI guards this). Terms for the content and
  the software are now declared in `LICENSE-CONTENT.md` and `LICENSE`.
  *(see Open Questions)*
- The upstream Umbrella `42.20.0` tag was later moved to a different commit
  (`98f50ae`, two commits on), so the KB pins by commit id, not tag name.
  *(repo file note in `sources/pins.json`)*

# Purpose

Contributors and the orchestrator need one place that answers: "When do I
bump a version? What does a release tag promise? Why did the freshness
script just fail? Can I trust a green QA run?" Without it those answers are
scattered across `CLAUDE.md`, `RELEASE_HISTORY.md`, `CHANGELOG.md`,
`sources/pins.json`, `PROJECT_STATUS.md` and the script docstrings. This
document consolidates them, states where they leave gaps, and keeps the
distinction between enforced rules and habits.

# Scope

Covered: document version and status semantics; the freshness-related front
matter; release tags and pins; the B41 baseline policy; the freshness
procedure and re-queue rule; the QA gates and their limits; the human gate
and standing mandate; open policy gaps. Both builds are in scope because the
pins and the baseline policy exist to manage them.

Not covered: genre, build-tag syntax and licensing (see `meta-style-guide`);
the ranked source list (see `SOURCE_REGISTRY.md` and
`meta-source-registry-companion`); worker mechanics (see
`prompts/worker_contract.md`); the content of any game mechanic. Also out of
scope: Stage 4 homelab publishing, which `ROADMAP.md` defers.

# Definitions

- **Document version** — the `version:` front-matter value, semver `X.Y.Z`.
- **Status** — the `status:` value, one of `draft`, `in-review`, `approved`,
  `frozen`, `superseded`.
- **Freeze** — promoting a reviewed document to `1.0.0` as part of a
  cluster release.
- **kb-release tag** — an annotated git tag `kb-release-YYYY.MM.DD` that
  records the validated game builds and Umbrella pin of a freeze.
- **Pin** — a recorded external version (a game build or an Umbrella tag
  and commit) that the KB's gates and documents are validated against.
- **Drift** — a newer official game build than the one pinned.
- **Re-queue** — marking a document for a fresh verification pass because its
  `game_versions_verified` or `review_due` is stale.
- **Baseline (B41)** — the build line B41 verification targets; here the
  legacy41 maintenance line.

# Build Applicability

The policy itself is build-agnostic, but the pins it manages are
build-specific. Both builds exist as live Steam branches: 42.20 became the
stable branch on 2026-07-29 with Build 41 retained as the opt-in `legacy41`
beta [1].

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 (Umbrella pin); 41.78.21 hotfix announcement [4] | Baseline is the maintenance line; Umbrella pin stays at 41.78.16 |
| B42 (stable) | Yes | 42.20 and 42.21 | Umbrella pin and game pin moved to 42.21 on 2026-10-07; 42.21 stable announced 2026-09-28 [3] |

# Reference

## Document version and status semantics

The template starts every worker-written document at `version: 0.1.0` with
`status: in-review` (`prompts/worker_contract.md`, section 2).
`scripts/validate.py` requires the front-matter keys, checks that `status`
is one of the five allowed values and that `version` matches semver
`X.Y.Z`; it does not relate version to status and does not read the
Revision History table. The progression below is therefore the observed
convention recorded in `CHANGELOG.md` and in the revision table of
`docs/meta/meta-style-guide.md`, not a mechanically enforced rule:

| Change | Version move | Evidence in the repo |
|--------|--------------|----------------------|
| New worker draft | `0.1.0`, `in-review` | Wave A to E documents, commits `1d703b6` through `0ad3a16` |
| Content revised while still in review | minor bump, e.g. `0.2.0` | Three Modders documents revised for the TIS 42.13 guide, `CHANGELOG.md`, commit `0ad3a16` |
| Cluster freeze | `1.0.0`, status `approved` | `meta-style-guide` revision row 1.0.0, commit `49b9ada` |
| Prose-only or hygiene rewrite, no factual change | patch bump, e.g. `1.0.1` | Five foundation documents, `CHANGELOG.md`, commit `1172a2b` |

`CLAUDE.md` rule 6 is the governing rule: a fact change cuts a new document
version with a revision note, never a silent edit. The revision note lives in
the document's own Revision History table, and the cluster-level record lives
in `CHANGELOG.md`.

## Freshness fields in front matter

Four dated fields exist and all must be ISO dates (`scripts/validate.py`):
`created`, `updated`, `review_due` and `sources_verified`. A fifth,
`game_versions_verified`, is a list of the exact builds checked first-hand or
via patch notes (`templates/document_template.md`). Their intended roles:

| Field | Meaning in this KB | Who reads it |
|-------|--------------------|--------------|
| `game_versions_verified` | Builds the facts were verified against | `scripts/requeue.py`, which compares it at major.minor precision with the newest announced builds; not read by `check_freshness.py` |
| `sources_verified` | Date the cited sources were last checked | Humans; plus `ROADMAP.md` Stage 3 plan |
| `review_due` | Date the document should be re-reviewed | `scripts/requeue.py` flags a document whose date has passed |

The template's example `review_due` is about three months after creation
(`2026-07-30` to `2026-10-30`), and this document follows the same
three-month interval. The interval is a template habit, not a validated
rule.

## Release tags and what they pin

`RELEASE_HISTORY.md` states the release procedure: all gates green, human
approval, per-document `1.0.0`, then an annotated git tag, and every tag
records the game builds and Umbrella commit it was validated against. The
first row is `kb-release-2026.07.30` (foundation cluster, six documents),
which records game builds 41.78.16 (legacy41) and 42.20.0 (stable) and the
Umbrella release tag `42.20.0`. Its annotated tag message reads "Foundation
cluster v1.0.0 - game builds 41.78.16 + 42.20.0, Umbrella release tag
42.20.0" (`git tag -n9`), and the tag points at commit `49b9ada`, the freeze
commit. The second row is `kb-release-2026.10.08` (the 42.21 re-baseline:
all 41 documents), which records game builds 42.21 (stable) and 41.78.21
(legacy41) and Umbrella `42.21.0` at commit `13d01f9`; because the upstream
`42.20.0` tag was later moved, tags that name an Umbrella release also name
its commit. The commit a tag points at can be read with `git rev-parse
<tag>^{commit}`.

Two honest details. First, `RELEASE_HISTORY.md` and the tag message name the
Umbrella release tag, while the full commit ids live in `sources/pins.json`
and were pinned the same day the corpus was armed (`pinned_at` 2026-07-30,
commit `1172a2b`). Second, `CLAUDE.md` says each tag "pins the game build(s)
and the Umbrella commit"; for the one existing tag the Umbrella commit is
therefore recoverable by joining the tag's release name to `pins.json`, not
read from the tag alone.

## Pins in sources/pins.json

| Pin | Value | Note |
|-----|-------|------|
| Umbrella B42 | release tag `42.21.0`, commit `13d01f9ee58fa48773553920db56d06f0005e7f8` | Upstream repository [2]; pinned 2026-10-07 |
| Umbrella B42 previous | release tag `42.20.0`, commit `58204fc47895ba249592519cedecc7cfbaaebd60` | Original KB pin; the upstream tag was later moved to `98f50ae`, so pin by commit; archived index at `sources/schemas/archive/api-index-B42-42.20.0.json` |
| Umbrella B41 | release tag `41.78.16`, commit `fa2e7e19799740b57902f1cb4e989225c295c05e` | No newer B41 stub tag exists, per the file's note |
| Game B42 stable | `42.21` | Compared by the freshness script; stable since 2026-09-28 [3] |
| Game B41 legacy | `latest_primary_attested` 41.78.21 (legacy hotfix, 2026-08-26) [4]; `latest_wiki_attested` 41.78.20 | Only the primary-attested value is compared |

The Umbrella pins feed the API-existence gate: `scripts/extract_api_index.py`
builds per-build symbol indices into `sources/schemas/`, which
`scripts/check_api_exists.py` consults. `SOURCE_REGISTRY.md` instructs that
the per-game-version Umbrella release tag be pinned per KB release.

## The B41 baseline policy

On 2026-07-31 the project owner decided that the B41 verification target is
the legacy41 maintenance line, not the frozen 41.78.16 build. The decision is
recorded in `sources/pins.json` (`game_builds.B41_legacy.decision`), in
`CHANGELOG.md` under Changed, and in `PROJECT_STATUS.md`, and was made in
commit `512581b`. Its operating consequences, as written in those files:

- Builds 41.78.17 to 41.78.19 were verified as security or maintenance only,
  so existing 41.78.16-era fact verification stands.
- Documents bump `game_versions_verified` at their next natural revision,
  not in a bulk edit.
- The Umbrella B41 API pin stays at release tag 41.78.16.
- 41.78.20 is attested only by pzwiki version pages and is pending primary
  confirmation; `PROJECT_STATUS.md` lists confirming it as a follow-up. The
  primary-attested value has since advanced to 41.78.21 (announced
  2026-08-26 together with the 42.20.4 and 42.19.2 hotfixes) [4].

The B41 branch is a Steam beta opt-in, per the stable-release announcement
[1]; the policy is about which maintenance versions count as the B41 target,
not about a separate document set.

## The freshness procedure

`scripts/check_freshness.py` is a Stage 3 seed. It fetches up to `--count`
(default 40) official Steam community announcements for app 108600 through
the Steam news API, splits compound titles on `&`, extracts versions labelled
STABLE, LEGACY or UNSTABLE, and compares the newest STABLE with
`game_builds.B42_stable` and the newest LEGACY with the version parsed from
`latest_primary_attested`. Exit codes, from the script's docstring:

| Exit | Meaning |
|------|---------|
| 0 | Pins current |
| 1 | Fetch error |
| 2 | Drift detected, informational for CI |

On 2026-10-07 it printed STABLE 42.21 (2026-09-28), LEGACY 41.78.21
(2026-08-26), UNSTABLE 42.21 (2026-09-23). Against the earlier pins (B42
42.20.0, B41 41.78.19) it reported both drifts and exited 2; after the pins
were updated to 42.21 and 41.78.21 the same run prints "Pins current" and
exits 0. The 42.21 sequence it detected is: unstable on 2026-09-23 [5],
stable on 2026-09-28 [3], which the stable post describes as the standard
unstable-first procedure going forward [3].

## The re-queue rule

On drift `check_freshness.py` prints its own instruction: re-queue documents
whose `game_versions_verified` predates the new build. Since 2026-10-08
`scripts/requeue.py` builds that list. It combines three signals: a
document's `game_versions_verified` lagging the newest announced build
(compared at major.minor precision, so a hotfix inside the verified minor is
not flagged; `historic` documents are skipped and B41 documents are compared
with the legacy line); a passed `review_due`; and Umbrella pin drift, which
flags every Modders document. It also reads official Steam announcements
newer than the pins and matches their lines against the entity map
(`exports/entity-map.json`, built by `scripts/build_entity_map.py` from
`sources/entity_aliases.json` plus the code-span identifiers the documents
themselves use) to show which documents each line probably affects, and it
lists the forum topics those posts link, because the forum blocks bots. A
new stable build also flags the release-bookkeeping documents named in the
alias file. The patch-note matching is a heuristic pointer with its evidence
lines printed for a human to judge, not proof of impact; extend the alias
file when a re-baseline shows a topic the map missed. `scripts/watch_umbrella.py`
supplies the Umbrella signal: it reads upstream tags with `git ls-remote` and
reports a newer tag or a pinned tag that now points at a different commit.
`requeue.py` exits 2 when its worklist is non-empty. Revising the listed
documents remains a manual, human-gated step.

## The QA gates: what each proves and does not prove

The canonical list is in `CLAUDE.md`. The table adds the limits, taken from
each script's own docstring or code.

| Gate | Command | Proves | Does not prove |
|------|---------|--------|----------------|
| Structure and citations | `python scripts/validate.py` | Required front matter, valid enums and ISO dates, 19 sections in order, a substantive delta for `both`, references contiguous, every marker resolving, every reference cited | That a cited source says what the sentence claims; that version and status agree; that a revision row exists |
| Genre audit | `python scripts/audit_genre.py --strict` | Reference and delta contain at least one `[n]` marker (or an explicit "Not applicable"); every quarantined claim has Claim, Why unverified and Confidence with High, Medium or Low | That every individual sentence is cited, only that the section cites at all; that a claim is correctly rated |
| License hygiene | `python scripts/check_license_hygiene.py` | No shared word n-gram at or above the threshold (default 8) with the ingested pzwiki snapshots | Originality of table layout (the script says it is a human-review item); overlap with pages that are not in the corpus; overlap with any non-pzwiki source |
| Markdown lint | `npx --yes markdownlint-cli2@0.23.3 "docs/**/*.md" "*.md"` | Style conformance to `.markdownlint.jsonc` | Anything about content; it is not a repo dependency, so a local run needs network access to fetch the tool (with `--no-install` and no copy installed it reports unavailable) |
| Links | `python scripts/check_links.py` | Cited URLs respond; bot-block hosts are reported as warnings | That a bot-blocked page still says what is cited; that a live page is the intended one |
| Cross-references | `python scripts/build_graph.py` | Related-document references resolve; graph export is rebuilt | That the relationship is meaningful |
| Exports | `python scripts/build_rag.py` and `python scripts/build_site.py` | Exports and site scaffolding are regenerated and match what is committed (CI diff check) | Retrieval quality, rendering of the live site |
| API existence | `python scripts/check_api_exists.py` | In Modders documents, `Events.X` and `Class:method` code spans exist in the pinned Umbrella index for the document's build(s); an inline build tag narrows the check | Correct semantics, parameters, call order or runtime behaviour; symbols not written in the checked shapes; non-Modders documents (passes trivially) |
| Server-setting existence | `python scripts/check_server_settings.py` | In Admins documents, key-table first-cell code spans exist in `sources/schemas/server-settings.json` | Value ranges, defaults, or that the key means what the document says; keys written in prose |

`check_api_exists.py` accepts a symbol if it exists in any build the
document's tag covers, so a `both` document can pass with a symbol that
exists only on one build unless the line carries an inline *(B41)* or *(B42)*
tag. The same script reported 319 symbol references clean on 2026-10-07. The
two existence gates are also silent no-ops when their schema files are absent
(the arming pattern), so a missing schema looks like a pass.

Wiring to CI: `.github/workflows/qa.yml`'s offline job first requires the
gate data files (`sources/pins.json`, `server-settings.json` and the two
`api-index-*.json` files) to exist and be non-empty, because the existence
gates pass silently without them; it then runs validate, genre audit,
license hygiene, server settings, API existence, graph, RAG and site, and
fails if committed exports are stale. The license-hygiene step emits a
notice, because in CI the pzwiki snapshots are absent and the gate passes
trivially; run it locally against the corpus before every release.
markdownlint runs in a separate job with a pinned `markdownlint-cli2`
version; the link check runs only on the weekly schedule or manual dispatch.
`.github/workflows/freshness.yml` runs `check_freshness.py`,
`watch_umbrella.py` and `requeue.py` daily and writes the report to the run
summary. It opens or updates one issue labelled `freshness` while there is
anything to re-verify and closes it when the report is empty. The run fails
only on build or Umbrella drift, so a failed scheduled run is the "re-baseline
needed" alert; a review date passing opens the issue without failing the
run, and a feed or tag read error is only a warning. `qa.yml` also rebuilds
the entity map (stale committed output fails the push) and runs
`requeue.py --offline --today 2000-01-01`, which fails if the pins have moved
ahead of the documents.

## The human gate and the standing mandate

`CLAUDE.md` rule 5: no cluster merges to `main` without human approval, or
an explicitly granted standing auto-approve-on-green-QA mandate. The mandate
was granted on 2026-07-30 (`PROJECT_STATUS.md`, "Approved scope"): the
orchestrator may approve, merge and freeze clusters on green QA and must
pause only on gate failures or unverifiable core claims. `PROJECT_HANDOVER.md`
adds that the orchestrator independently re-runs `check_links.py`, so a
worker's link result is never taken on trust, and that publishing to a public
GitHub repository needs explicit per-repo authorization.

The mandate is a standing permission about merging and freezing. The
release history shows it was used once for a freeze (the foundation
cluster); the later waves were merged as `in-review` and not frozen.

# B41 vs B42 Delta

This is a policy document, so the delta is how the policy treats the two
branches rather than a mechanic that changed.

| Aspect | B41 (legacy41) | B42 (stable) |
|--------|----------------|--------------|
| Branch status | Opt-in beta branch kept alongside stable [1] | Stable branch since 2026-07-29 [1] |
| Game-build pin used by freshness | `41.78.21`, the latest primary-attested value *(B41)* [4] | `42.21` *(B42)* [3] |
| Umbrella API pin | Release tag `41.78.16`, commit `fa2e7e1`; cannot advance for lack of a newer stub tag *(B41)* | Release tag `42.21.0`, commit `13d01f9`; previous `42.20.0` @ `58204fc` kept *(B42)* |
| Baseline concept | Maintenance line, not a frozen build (decision 2026-07-31) *(B41)* | The latest stable build; no equivalent decision recorded *(B42)* |
| Drift on 2026-10-07 | Was two patch levels ahead (41.78.21 against 41.78.19); reconciled by the re-baseline *(B41)* | Was one minor ahead (42.21 against 42.20.0); reconciled by the re-baseline *(B42)* |

The asymmetry is deliberate: on B41 the KB follows a line whose later builds
are security or maintenance releases, so documents keep their 41.78.16-era
verification until revised, whereas on B42 a minor release such as 42.21 can
change gameplay and APIs and is expected to trigger real re-verification.
That reading of B42 is an inference from the version number. The 42.21
announcements call it an incremental update with many fixes and a few
gameplay improvements [3] [5], and the repository's two B42 API indices
differ (4,124 classes, 244 events, 930 globals at 42.21.0 against 4,266,
234 and 947 at 42.20.0, from `sources/schemas/`), but the counts describe
stubs, not game behaviour.

# Practical Guidance

- **Starting a document:** write `0.1.0` / `in-review`, set
  `game_versions_verified` to the builds you actually checked, and set
  `review_due` to roughly three months after creation, following the
  template.
- **Changing a fact after review:** bump the version and add a Revision
  History row in the same change; record it in `CHANGELOG.md` through the
  orchestrator. Do not edit a frozen document in place.
- **Fixing prose only:** a patch bump with a note stating no factual change,
  as done for the foundation documents.
- **Before freezing a cluster:** run every gate, re-run the link check
  independently, and also run the license-hygiene gate locally against the
  pzwiki corpus (CI cannot), and run `check_freshness.py` once more by hand
  even though `freshness.yml` runs daily. If freshness exits 2, decide
  explicitly whether to re-baseline before tagging, because the tag will
  claim validation against the pinned builds.
- **When freshness exits 2:** treat it as a work-queue trigger, not a
  failure. List documents whose `game_versions_verified` predates the new
  build, prioritise B42 minor releases over B41 maintenance patches under
  the baseline policy, and record the decision in `PROJECT_STATUS.md`.
- **Reading a green run:** it means the structure, naming and link checks
  passed. Treat factual accuracy as a separate question answered by the
  citations and by a human spot-check.

# Common Pitfalls & Troubleshooting

- **Assuming a tag pins a commit by itself.** The tag message names the
  Umbrella release tag; the commit ids are in `sources/pins.json`. If the
  pins file changes later, the old tag no longer shows its original ids
  without checking out the tagged tree.
- **Treating exit 2 as breakage.** The script's docstring calls drift
  informational; only exit 1 means the fetch failed.
- **Believing the B41 pin is stale.** The Umbrella B41 pin sits at 41.78.16
  by necessity; the moving value is the game build, tracked separately.
- **Forgetting to bump `game_versions_verified`.** Under the baseline
  policy it moves only when a document is revised, so an old value alone
  does not mean the document is wrong, only that nobody has re-checked.
- **Reading API or server gates as accuracy checks.** Both verify names
  only, and both pass silently if their schema is missing.
- **Counting markdownlint as passed.** It runs in CI and locally through
  `npx --yes`; a run that could not fetch or find the tool is unavailable,
  not green.
- **Citing wiki-attested builds as official.** 41.78.20 is wiki-attested
  only; the freshness comparison deliberately ignores it.

# Community Notes & Unverified Claims

None.

# Risks & Caveats

- The mechanics described are accurate for repo commit `20aaa2d` plus the
  uncommitted 2026-10-07 re-baseline changes; any script change makes this document stale and should come
  with a version bump here.
- Version-increment semantics are inferred from the revision history of
  existing documents, not from a written rule, so a maintainer could
  reasonably choose differently.
- The Steam drift figures come from a live feed read on 2026-10-07 and will
  change; the feed titles were parsed by the script, and the 42.21 stable,
  42.21 unstable and 41.78.21 announcements [3] [4] [5] were read as part of
  the re-baseline.
- The 42.20, 42.21 and 41.78.21 announcements [1] [3] [4] [5] are on a
  bot-blocking host and are cited as allowlisted URLs.
- The `kb-release-2026.10.08` tag is read from `git tag` and
  `RELEASE_HISTORY.md`; it was cut after the commit that contains this
  document, so this document cannot name its own tag commit.
- The count of unfrozen documents is the number of `docs/` files whose
  `status:` is not `approved`; it was 35 of 41 on 2026-10-07 and 0 of 41
  after the 2026-10-08 freeze. Recount before quoting it. The earlier figure
  of 27 was a snapshot at commit `0ad3a16`.

# Verification Steps

- Run `git tag -n9` and `git log --oneline` from the repo root and compare
  with `RELEASE_HISTORY.md`.
- Open `sources/pins.json` and compare the Umbrella commit ids with the
  upstream release tags [2].
- Run `python scripts/check_freshness.py` and note the exit code
  (`echo $?`); 2 means drift.
- Run `python scripts/check_api_exists.py` with no arguments and read the
  closing summary line.
- Open `.github/workflows/qa.yml` and `.github/workflows/freshness.yml` and
  confirm which gates they run and when.
- Run `python scripts/validate.py docs/meta/meta-release-versioning-policy.md`
  and confirm it accepts the version and status values described.
- Run `npx --no-install markdownlint-cli2 "docs/**/*.md"` and confirm
  whether the tool is installed on your machine.

# Open Questions

- **Outbound license (decided 2026-10-08).** The project owner chose all
  rights reserved for the content (`docs/`, `templates/`, `prompts/`,
  `exports/` and root Markdown) and the MIT License for the software
  (`scripts/`, `.github/workflows/`); the terms and the third-party
  carve-outs are in `LICENSE-CONTENT.md` and `LICENSE`. This was a choice by
  the owner, not a legal review, and it does not license the Umbrella-derived
  name lists in `sources/schemas/`.
- **Re-queue is a worklist, not a repair.** `requeue.py` and `freshness.yml`
  list and track what to re-verify; a human or orchestrator still reads the
  patch notes, revises the documents and cuts the tag.
- **Entity-map coverage.** The alias file is hand-curated and the derived
  identifiers only cover names the documents already use, so a patch note
  about a topic no document mentions produces no match; it is judged on
  evidence lines, and its recall against real re-baselines has been checked
  only by replaying the 42.21 release.
- **Watchers still manual.** No watcher exists for the official blog (its
  posts are mirrored in the Steam feed already read), for a dedicated-server
  build id (needs SteamCMD or an unofficial API) or for Workshop item
  changelogs (needs a list of tracked items, which does not exist).
- **Freeze meaning.** The 2026-10-08 freeze promoted every document to
  `1.0.0` or kept its `1.1.x` version at `approved`. It records a human
  approval of the documents as they stood, not a claim that open questions
  are closed: many documents still carry Medium confidence, quarantined
  claims and carried-forward statements that were not re-tested in game.
- **Next re-baseline.** The next freshness drift (a newer stable build, a
  newer Umbrella tag) needs a repeat of the 2026-10-07 procedure; the
  worklist is automated, the revisions are not.
- **Revision-row enforcement.** No gate verifies that a version bump has a
  matching Revision History row or `CHANGELOG.md` entry.
- **Local markdownlint.** The tool is fetched on demand rather than
  installed, so a worker without network access cannot run one of the five
  contract gates.
- **Tag content.** Whether tags should carry Umbrella commit ids directly,
  rather than the release tag name, is unsettled.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259 Accessed 2026-07-30 via the Steam news API (ISteamNews, app 108600); host is bot-block allowlisted.
- [2] **PZ-Umbrella** — *Umbrella* (Project Zomboid type stubs; release tags per game version). https://github.com/PZ-Umbrella/Umbrella Repository URL as recorded in `sources/pins.json`.
- [3] **The Indie Stone** — *Build 42.21 Stable Released* (Steam announcement, 2026-09-28). https://steamcommunity.com/games/108600/announcements/detail/1844751498231307 Accessed 2026-10-07; host is bot-block allowlisted.
- [4] **The Indie Stone** — *42.20.4 STABLE & 42.19.2 UNSTABLE & 41.78.21 LEGACY Hotfixes Released* (Steam announcement, 2026-08-26). https://steamcommunity.com/games/108600/announcements/detail/1842212951296601 Accessed 2026-10-07; host is bot-block allowlisted.
- [5] **The Indie Stone** — *Re-population of the Dead: Build 42.21 Unstable Released* (Steam announcement, 2026-09-23). https://steamcommunity.com/games/108600/announcements/detail/1844751498218925 Accessed 2026-10-07; host is bot-block allowlisted.

# Further Reading

- `CLAUDE.md` — operating rules including the freeze and release rules.
- `RELEASE_HISTORY.md` and `CHANGELOG.md` — the release table and the dated change log.
- `sources/pins.json` — the pins this document describes.
- `PROJECT_STATUS.md` and `PROJECT_HANDOVER.md` — current state and orchestrator procedure.
- `ROADMAP.md` — Stage 3 freshness automation plan.
- `scripts/check_freshness.py`, `scripts/check_api_exists.py`, `scripts/check_server_settings.py` — the gates described.

# Related Documents

- meta-style-guide — genre, build tags, licensing and the five contract gates.
- meta-source-registry-companion — how the ranked source list is applied.
- modders-lua-api-surface — a Modders document governed by the API-existence gate.
- admins-server-ini-reference — the Admins document behind the server-setting schema.
- players-foundation — a frozen foundation document released under the tag described here.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined: pins now B42 42.21.0 (42.20.0 kept as previous, tag-move note) and B41 41.78.21 primary-attested; freshness now exits 0; unfrozen count 35 as of 2026-10-07; kb-release tag for the re-baseline recorded as pending; sources [3][4][5]. | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. Includes the 2026-10-08 update describing this release and the freeze. | Project owner (user instruction 2026-10-08) |
| 1.1.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Release policy updated for the 2026-10-08 CI and license changes: API-existence and gate-data guards in qa.yml, a daily freshness.yml, a pinned markdownlint, LICENSE (MIT, software) and LICENSE-CONTENT.md (all rights reserved, content). Open Questions and pitfalls revised to match. | Project owner (user instruction 2026-10-08) |
| 1.2.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Stage 3 freshness tooling described: requeue.py, watch_umbrella.py, build_entity_map.py with sources/entity_aliases.json, the extended freshness.yml (summary and tracking issue) and the qa.yml entity-map and smoke steps; re-queue rule, review_due and game_versions_verified field rows, and Open Questions revised. | Project owner (user instruction 2026-10-08) |
