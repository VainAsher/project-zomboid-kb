---
id: meta-release-versioning-policy
title: "Release and Versioning Policy: Document Versions, kb-release Tags and Game-Build Pins"
version: 0.1.0
status: in-review
confidence: High
category: Meta
topic: "Release & versioning policy"
build: both
document_type: policy
created: 2026-10-07
updated: 2026-10-07
review_due: 2027-01-05
sources_verified: 2026-10-07
supersedes: null
related: [meta-style-guide, meta-source-registry-companion, modders-lua-api-surface, admins-server-ini-reference, players-foundation]
tags: [meta, governance, release, versioning, freshness, qa-gates, pins]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | meta-release-versioning-policy |
| Version | 0.1.0 |
| Status | in-review |
| Confidence | High |
| Category (track) | Meta |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-07 |
| Review due | 2027-01-05 |
| Game versions verified | 41.78.16, 42.20 |

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
manages, and the Umbrella repository [2], whose release tags are what the
API pins refer to. Confidence is High for the mechanics described. It would
fall if the scripts were changed without a revision of this document; the
live state on 2026-10-07 already shows unreconciled drift (see Reference
and Open Questions).

# Key Takeaways

- A document version is semver, validated mechanically for shape only;
  `0.1.0` / `in-review` is the entry state and `1.0.0` is the freeze, cut
  by the orchestrator at a cluster release. *(repo rule and observed
  practice; see Reference)*
- A fact change cuts a new version with a revision-history row, never a
  silent edit (`CLAUDE.md` rule 6). Nothing in the gates checks that a
  revision row exists; this is a human/orchestrator discipline. *(repo
  rule)*
- Exactly one release tag exists today, `kb-release-2026.07.30`, an
  annotated tag whose message names the game builds and the Umbrella
  release tag. No release has been cut since; 27 documents sit unfrozen at
  `in-review`. *(repo state at commit `0ad3a16`)*
- `sources/pins.json` pins Umbrella B42 `42.20.0` @ `58204fc` and B41
  `41.78.16` @ `fa2e7e1`; the B41 game baseline is the legacy41
  maintenance line (user decision 2026-07-31), but the B41 API pin cannot
  move because no newer B41 stub tag exists. *(repo file)*
- `python scripts/check_freshness.py` exits 0 (current), 1 (fetch error) or
  2 (drift). On 2026-10-07 it exits 2: Steam news shows B42 stable 42.21 and
  legacy41 41.78.21, while pins say 42.20.0 and 41.78.19. *(run on
  2026-10-07)*
- Green gates prove structure, citation hygiene, name existence and
  link liveness. They do not prove a statement is true, current, or
  correctly interpreted. *(see the gate table)*
- Open policy gaps are real: no LICENSE file for the KB's prose, no
  automated re-queue, freshness and API gates not wired into CI,
  markdownlint not installed locally. *(see Open Questions)*

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
| B41 (legacy41) | Yes | 41.78.16 | Baseline is the maintenance line; Umbrella pin stays at 41.78.16 |
| B42 (stable) | Yes | 42.20 | Newer 42.21 stable is announced but not yet pinned or reconciled |

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
| `game_versions_verified` | Builds the facts were verified against | The human or orchestrator reading freshness output; not read by `check_freshness.py` |
| `sources_verified` | Date the cited sources were last checked | Humans; plus `ROADMAP.md` Stage 3 plan |
| `review_due` | Date the document should be re-reviewed | `ROADMAP.md` Stage 3 plans re-queue through it; no script does so yet |

The template's example `review_due` is about three months after creation
(`2026-07-30` to `2026-10-30`), and this document follows the same
three-month interval. The interval is a template habit, not a validated
rule.

## Release tags and what they pin

`RELEASE_HISTORY.md` states the release procedure: all gates green, human
approval, per-document `1.0.0`, then an annotated git tag, and every tag
records the game builds and Umbrella commit it was validated against. The
single row so far is `kb-release-2026.07.30` (foundation cluster, six
documents), which records game builds 41.78.16 (legacy41) and 42.20.0
(stable) and the Umbrella release tag `42.20.0`. The annotated tag message
itself reads "Foundation cluster v1.0.0 - game builds 41.78.16 + 42.20.0,
Umbrella release tag 42.20.0" (`git tag -n9`). The tag points at commit
`49b9ada`, the freeze commit.

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
| Umbrella B42 | release tag `42.20.0`, commit `58204fc47895ba249592519cedecc7cfbaaebd60` | Upstream repository [2] |
| Umbrella B41 | release tag `41.78.16`, commit `fa2e7e19799740b57902f1cb4e989225c295c05e` | No newer B41 stub tag exists, per the file's note |
| Game B42 stable | `42.20.0` | Compared by the freshness script |
| Game B41 legacy | `latest_primary_attested` 41.78.19 (security-only hotfix, 2026-04-08); `latest_wiki_attested` 41.78.20 | Only the primary-attested value is compared |

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
  confirmation; `PROJECT_STATUS.md` lists confirming it as a follow-up.

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
(2026-08-26), UNSTABLE 42.21 (2026-09-23) against pins B42 42.20.0 and B41
41.78.19, reported both drifts, and exited 2. `PROJECT_STATUS.md` records the
same unreconciled drift and the need for a re-baseline decision.

## The re-queue rule

On drift the script prints its own instruction: re-queue documents whose
`game_versions_verified` predates the new build. The roadmap adds a second
trigger, stale `sources_verified` re-queuing through `review_due`, and plans
tags after each hotfix wave (`ROADMAP.md`, Stage 3). Today re-queuing is a
manual orchestrator action: no script lists the affected documents, no
script reads `review_due`, and `check_freshness.py` does not inspect
`docs/`. The mapping from a patch to the entities it touches ("changelog to
entity map" in the roadmap) does not exist yet.

## The QA gates: what each proves and does not prove

The canonical list is in `CLAUDE.md`. The table adds the limits, taken from
each script's own docstring or code.

| Gate | Command | Proves | Does not prove |
|------|---------|--------|----------------|
| Structure and citations | `python scripts/validate.py` | Required front matter, valid enums and ISO dates, 19 sections in order, a substantive delta for `both`, references contiguous, every marker resolving, every reference cited | That a cited source says what the sentence claims; that version and status agree; that a revision row exists |
| Genre audit | `python scripts/audit_genre.py --strict` | Reference and delta contain at least one `[n]` marker (or an explicit "Not applicable"); every quarantined claim has Claim, Why unverified and Confidence with High, Medium or Low | That every individual sentence is cited, only that the section cites at all; that a claim is correctly rated |
| License hygiene | `python scripts/check_license_hygiene.py` | No shared word n-gram at or above the threshold (default 8) with the ingested pzwiki snapshots | Originality of table layout (the script says it is a human-review item); overlap with pages that are not in the corpus; overlap with any non-pzwiki source |
| Markdown lint | `npx --no-install markdownlint-cli2 "docs/**/*.md" "*.md"` | Style conformance to `.markdownlint.jsonc` | Anything about content; currently not runnable locally (not installed) |
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

Wiring to CI (`.github/workflows/qa.yml`): the offline job runs validate,
genre audit, license hygiene, server settings, graph, RAG and site, then
fails if committed exports are stale; markdownlint runs in a separate job
using `npx --yes`; the link check runs only on the weekly schedule or manual
dispatch. The workflow does not call `check_api_exists.py` or
`check_freshness.py`.

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
| Game-build pin used by freshness | `41.78.19`, the latest primary-attested value *(B41)* | `42.20.0` *(B42)* |
| Umbrella API pin | Release tag `41.78.16`, commit `fa2e7e1`; cannot advance for lack of a newer stub tag *(B41)* | Release tag `42.20.0`, commit `58204fc` *(B42)* |
| Baseline concept | Maintenance line, not a frozen build (decision 2026-07-31) *(B41)* | The latest stable build; no equivalent decision recorded *(B42)* |
| Observed drift on 2026-10-07 | 41.78.21 announced, two patch levels ahead of the primary-attested pin *(B41)* | 42.21 stable announced, one minor ahead of the pin *(B42)* |

The asymmetry is deliberate: on B41 the KB follows a line whose later builds
are security or maintenance releases, so documents keep their 41.78.16-era
verification until revised, whereas on B42 a minor release such as 42.21 can
change gameplay and APIs and is expected to trigger real re-verification.
That reading of B42 is an inference from the version number, not a verified
fact about 42.21's contents, which this document did not open.

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
  independently, and also run `check_api_exists.py` and
  `check_freshness.py` by hand, since CI does not. If freshness exits 2,
  decide explicitly whether to re-baseline before tagging, because the tag
  will claim validation against the pinned builds.
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
- **Counting markdownlint as passed.** It runs in CI but cannot run locally
  here; a local run reports it as unavailable, not green.
- **Citing wiki-attested builds as official.** 41.78.20 is wiki-attested
  only; the freshness comparison deliberately ignores it.

# Community Notes & Unverified Claims

None.

# Risks & Caveats

- The mechanics described are accurate for repo commit `0ad3a16` on
  2026-10-07; any script change makes this document stale and should come
  with a version bump here.
- Version-increment semantics are inferred from the revision history of
  existing documents, not from a written rule, so a maintainer could
  reasonably choose differently.
- The Steam drift figures come from a live feed read on 2026-10-07 and will
  change; the feed titles were parsed by the script, and this document did
  not open the 42.21 or 41.78.21 announcements themselves.
- The 42.20 announcement [1] is on a bot-blocking host and is cited as an
  allowlisted URL.
- The count of unfrozen documents (27) is the number of Wave A to E documents
  merged `in-review` plus the other non-foundation documents on disk at
  commit `0ad3a16`; recount before quoting it.

# Verification Steps

- Run `git tag -n9` and `git log --oneline` from the repo root and compare
  with `RELEASE_HISTORY.md`.
- Open `sources/pins.json` and compare the Umbrella commit ids with the
  upstream release tags [2].
- Run `python scripts/check_freshness.py` and note the exit code
  (`echo $?`); 2 means drift.
- Run `python scripts/check_api_exists.py` with no arguments and read the
  closing summary line.
- Open `.github/workflows/qa.yml` and confirm which gates it runs.
- Run `python scripts/validate.py docs/meta/meta-release-versioning-policy.md`
  and confirm it accepts the version and status values described.
- Run `npx --no-install markdownlint-cli2 "docs/**/*.md"` and confirm
  whether the tool is installed on your machine.

# Open Questions

- **Outbound license for the KB's own prose.** `PROJECT_STATUS.md` lists the
  missing repository LICENSE file as an open item needing a human decision.
  Until it exists, the reuse terms of every document, and of the exports and
  site built from them, are undeclared.
- **No automated re-queue.** The roadmap plans changelog-to-entity mapping
  and `review_due` re-queueing; neither exists. Stale documents are found by
  a human reading freshness output.
- **Freshness and API gates outside CI.** Neither `check_freshness.py` nor
  `check_api_exists.py` is in `qa.yml`, so a regression in either would not
  fail a push.
- **Re-baseline of 42.21 and 41.78.21.** Documented as unreconciled in
  `PROJECT_STATUS.md`; the decision of what 42.21 means for the freeze
  schedule is open.
- **Unfrozen backlog.** Nothing has been frozen since `kb-release-2026.07.30`
  although the standing mandate permits it; whether to freeze before or
  after the re-baseline is undecided.
- **Revision-row enforcement.** No gate verifies that a version bump has a
  matching Revision History row or `CHANGELOG.md` entry.
- **Local markdownlint.** The tool is not installed here, so one of the five
  contract gates cannot be run by workers.
- **Tag content.** Whether tags should carry Umbrella commit ids directly,
  rather than the release tag name, is unsettled.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259 Accessed 2026-07-30 via the Steam news API (ISteamNews, app 108600); host is bot-block allowlisted.
- [2] **PZ-Umbrella** — *Umbrella* (Project Zomboid type stubs; release tags per game version). https://github.com/PZ-Umbrella/Umbrella Repository URL as recorded in `sources/pins.json`.

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
