---
id: meta-style-guide
title: "How This Knowledge Base Is Written: Genre, Build Tags and License Rules"
version: 1.0.0
status: approved
confidence: High
category: Meta
topic: "KB governance"
build: both
document_type: reference
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: [modders-foundation, players-foundation, admins-foundation, creator-foundation, lore-foundation]
tags: [meta, governance, style-guide, licensing, build-tags, qa-gates]
game_versions_verified: ["41.78.16", "42.20"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | meta-style-guide |
| Version | 1.0.0 |
| Status | approved |
| Confidence | High |
| Category (track) | Meta |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | 41.78.16, 42.20 |

# Executive Summary

This knowledge base is a *reference* work: an evidence-based, source-cited
Project Zomboid encyclopedia written for four audience tracks (Modders,
Players, Admins, Creator) plus Lore and Meta. This document explains, in one
place, the rules every document in the repository follows: the three-layer
genre discipline (evidence, guidance, quarantine), the load-bearing build-tag
system that keeps Build 41 and Build 42 facts from contaminating each other,
the per-track voice, the ranked source order, the licensing stance, and the
deterministic QA gates a document must pass before it can be merged.

The build-tag system exists because the two supported builds genuinely
diverge: The Indie Stone stated ahead of the Build 42 stable launch that
"Build 41 savegames clearly will not be compatible with Build 42" [1], and
Build 42.20 shipped as the stable branch on 2026-07-29 with Build 41 retained
as an opt-in `legacy41` beta [2]. A knowledge base that blurred which build a
number belongs to would mislead every one of its readers.

Most factual claims in this document are about this repository itself and are
verifiable by opening the named repo files. The external claims — license
terms, content ownership, build compatibility — are cited to the Creative
Commons deed [3], The Indie Stone's own terms [4], PZwiki's copyright policy
[5], and official release announcements [1] [2]. Confidence is High: the
document rests on primary sources and directly inspectable repository files.

# Key Takeaways

- Genre is **reference**, enforced in three layers: the evidence layer must
  cite every factual sentence, the guidance layer may only synthesise cited
  facts, and uncited community claims live exclusively in a labelled
  quarantine section. *(cited, and mechanically enforced by repo scripts)*
- Every document carries a `build:` tag — `B41`, `B42`, `both`, or
  `historic` — and a `both` document must fill its "B41 vs B42 Delta"
  section substantively; single-build values are tagged inline *(B41)* /
  *(B42)*. *(repo rule; motivated by cited build divergence [1] [2])*
- pzwiki.net is licensed CC BY-NC-SA 3.0, whose NonCommercial clause bars
  commercial use [3] [5]; this commercially-adjacent project therefore uses
  pzwiki as a **fact-only** source — cite URL plus revision id, never reuse
  its prose or table layouts. *(cited)*
- Project Zomboid content and materials are trademarks and copyrights of The
  Indie Stone [4] [5]; the KB is an unofficial fan project and says so
  site-wide. *(cited)*
- Sources are reached for in a fixed priority order — official primaries,
  then code truth, then pzwiki facts, then tooling repos, then
  corroborate-only community material — summarised here and specified in
  `SOURCE_REGISTRY.md`. *(repo rule)*
- Five deterministic QA gates (structure/citations, genre audit, license
  hygiene, markdownlint, link check) must all be green before a document
  merges. *(repo rule, inspectable in `scripts/`)*

# Purpose

New readers need to know how much to trust what they read here, and new
contributors (human or agent) need the house rules in one compact document
rather than scattered across `CLAUDE.md`, `templates/document_template.md`
and `prompts/worker_contract.md`. This document is that single explanation:
what the genre is, why the build tag exists, which sources outrank which,
what the licensing constraints are, and what a document must survive to be
merged. It summarises the governing files; where they conflict with this
summary, the governing files win.

# Scope

Covered: the reference genre and its three layers; the build-tag system and
the enforced delta section; the four track voices; the source-priority order
and reference classes; the licensing stance (pzwiki, The Indie Stone IP, the
KB's own prose); and the QA gates. Covered for both builds in the sense that
these rules govern documents about B41 41.78.16 and B42 42.20 alike.

Not covered: the full ranked source table (see `SOURCE_REGISTRY.md`), the
19-section template itself (see `templates/document_template.md`), the worker
process mechanics (see `prompts/worker_contract.md`), and the release/freeze
workflow (see `CLAUDE.md` and `ROADMAP.md`). This is the style guide, not a
reprint of the rulebook.

# Definitions

- **Evidence layer** — the "Reference", "B41 vs B42 Delta" and "Build
  Applicability" sections, where every factual sentence carries a `[n]`
  citation to a primary source.
- **Guidance layer** — "Practical Guidance" and "Common Pitfalls &
  Troubleshooting": synthesis of the cited facts, forbidden from introducing
  new uncited facts.
- **Quarantine layer** — "Community Notes & Unverified Claims": the only
  section where an uncited community claim may appear, always as a labelled
  claim block with its own confidence rating.
- **Build tag** — the required `build:` front-matter field: `B41` (legacy
  41.78.16 only), `B42` (42.20+ stable only), `both`, or `historic`.
- **Fact-only source** — a source whose facts may be cited but whose prose
  and table layouts must never be copied or lightly paraphrased; in this KB,
  pzwiki.net.
- **Claim block** — the fixed three-bullet shape (Claim / Why unverified /
  Confidence) that every quarantined community claim must use.

# Build Applicability

This is a governance document: its rules apply to every document in the
repository regardless of build tag. It is tagged `both` because the rules it
describes exist precisely to manage the two live builds — B41 41.78.16 on
the `legacy41` beta branch and B42 42.20 on stable [2] — and because its
motivating examples cite both.

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Governance rules apply; B41 remains available as an opt-in Steam beta [2] |
| B42 (stable) | Yes | 42.20 | Stable branch since 2026-07-29 [2] |

# Reference

## The genre: reference, in three layers

The cardinal rule of this knowledge base is: **never let a judgement or
hearsay wear the costume of a fact.** The rule is made mechanical by
splitting every document into three layers. The evidence layer ("Reference",
"B41 vs B42 Delta", "Build Applicability") asserts facts, and every sentence
that does so carries a numbered citation to a primary source — an official
blog post or Thursdoid, a Steam announcement or patch note, a game script
file, a pinned API index, or a named and dated dev post. The guidance layer
("Practical Guidance", "Common Pitfalls & Troubleshooting") turns those
cited facts into advice and may not smuggle in new uncited facts. The
quarantine layer ("Community Notes & Unverified Claims") is the only place an
uncited community claim may live, and each one must appear as a labelled
claim block stating what the claim is, why it is unverified, and how
confident the KB is in it. `scripts/validate.py` enforces the structure and
citation resolution; `scripts/audit_genre.py` enforces the layer discipline.

Each document also carries a confidence rating (High / Medium / Low) applied
mechanically by the weakest evidence it rests on, with a hard floor: numbers
sole-sourced from hosting-company knowledge bases cannot rate above Medium,
and a document verified only against a superseded patch cannot rate High.

## The build-tag system

Every document declares `build: B41 | B42 | both | historic`. The tag is
load-bearing because the builds materially diverge: The Indie Stone's
pre-launch checklist stated flatly that Build 41 savegames will not be
compatible with Build 42 [1], and the 42.20 stable release notes document
behaviour changes between the builds down to details like default-option
migration [2]. A `both` document must therefore fill its "B41 vs B42 Delta"
section with real, cited content — the validator rejects an empty or
hand-waved delta. Inside a `both` document, any value that holds on only one
build is tagged inline as *(B41)* or *(B42)*, and a number established during
the B42-unstable cycle that has not been re-verified on 42.20 must say so
explicitly. `historic` marks older-build or lore material kept for the
record.

## The four track voices

All tracks obey the same evidence rules; what changes is the register of the
guidance layer:

| Track | Voice | Guidance reads like |
|-------|-------|---------------------|
| Modders | Peer engineer | Code patterns, API caveats, "here is why that event never fires" |
| Players | Friendly survival guide | Plain-language advice, decision-useful numbers, no jargon walls |
| Admins | Ops runbook | Copy-pasteable commands, exact setting names, rollback steps |
| Creator | Candid strategist | Production and channel notes, honest about what the data does and does not show |

The Lore track records narrative and world-building material (tagged
`historic` where it describes superseded builds), and the Meta track — this
document's track — documents the KB itself.

## Sources: priority order and reference classes

Workers reach for sources in the ranked order specified in
`SOURCE_REGISTRY.md`, summarised: (1) official Indie Stone primaries — blog,
Steam announcements, forums, Discord; (2) code truth — Umbrella/ZomboidDoc
API stubs and game script files; (3) pzwiki.net, facts only; (4) open-source
server and admin tooling repos; (5) hosting-company KBs and community
guides, corroborate-only; (6) creator/YouTube sources, admissible only as
creator-track evidence, never for game facts. Every reference in a document
is classed as Primary, Fact-Only (pzwiki), Secondary & Corroborating,
Community & Creator, or Further Reading, numbered contiguously from `[1]`,
with every marker resolving and every entry cited. URLs are never fabricated:
a worker may only cite a URL it actually opened, or one on the known
bot-block allowlist corroborated through a mirror such as the Steam news API.

## The licensing stance

Three distinct bodies of rights shape this project.

**pzwiki.net.** PZwiki states that all of its content — except
developer-owned images, art and lore — is licensed under Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported [5]. That license permits
sharing and adaptation only with attribution, forbids use "primarily
intended for commercial advantage or monetary compensation", and requires
adaptations to be distributed under the same license [3]. This project is
commercially adjacent (it supports a monetized YouTube channel), so it
cannot safely create derivative works of pzwiki text. The KB therefore
treats pzwiki as a fact-only source: a pzwiki page may be cited for a fact,
with URL and revision id recorded for provenance (this document cites
PZwiki:Copyrights at revision 1156861 [5]), but every sentence in this KB is
written as original prose, and `scripts/check_license_hygiene.py`
mechanically flags n-gram overlap against the ingested pzwiki corpus in
`sources/pzwiki/`.

**The Indie Stone's IP.** Project Zomboid content and materials are
trademarks and copyrights of The Indie Stone [5], whose published terms
govern use of the game and its materials [4]. This knowledge base is an
unofficial fan project — not affiliated with, endorsed by, or sponsored by
The Indie Stone — and carries that disclaimer site-wide. Game-file excerpts
are quoted minimally, cited by path and game version, and never rehosted.

**The KB's own prose.** Because every document is 100% original expression
citing facts to their sources, the prose of this KB is the project's own
work and is not a derivative of pzwiki or of official text. The repository
does not yet carry an explicit outbound LICENSE file for that prose; see
Open Questions.

## The QA gates

A document must pass five deterministic gates before it can merge, run from
the repo root:

1. `python scripts/validate.py <file>` — front matter fields valid, all 19
   template sections present in order, citations contiguous and resolving,
   and the build gate (a `both` document has a substantive delta section).
2. `python scripts/audit_genre.py --strict <file>` — the evidence sections
   actually cite, and every quarantined claim carries its three labelled
   bullets.
3. `python scripts/check_license_hygiene.py <file>` — no pzwiki prose
   overlap.
4. `npx --no-install markdownlint-cli2 --fix <file>` — zero markdown style
   errors against the repo's `.markdownlint.jsonc`.
5. `python scripts/check_links.py <file>` — zero dead links; known
   bot-blocking hosts produce warnings, not failures.

Cluster-level gates (`build_graph.py`, `build_rag.py`, `build_site.py`) and
the human approval gate are the orchestrator's job; no cluster merges to
`main` without human approval unless a standing auto-approve-on-green
mandate has been granted. A fact change always cuts a new document version
with a revision note — never a silent edit.

# B41 vs B42 Delta

For this governance document the "delta" is the policy itself: how the KB
handles the divergence between the two builds.

The motivating facts are cited, not assumed. The Indie Stone's launch-week
checklist told players that "Build 41 savegames clearly will not be
compatible with Build 42", and directed players and server owners who wanted
to stay on Build 41 to opt in to the `legacy41` Steam beta channel before
the release [1]. The same post noted that even saves from the 42.19 unstable
build would not survive the jump to 42.20 because of added map content [1].
The 42.20 stable release notes repeat the `legacy41` opt-out instructions,
warn that a launch-week security change "may affect some mods", and record
build-migration behaviour such as Build 42 now correctly applying default
options when migrating from Build 41 [2]. In short: saves, mods and even
option defaults are build-scoped in the game itself.

The KB mirrors that reality with three rules. First, the front-matter
`build:` tag scopes every document to the build(s) its facts were verified
on. Second, every `both` document must carry a substantive, cited "B41 vs
B42 Delta" section — renames, rebalances, removals, additions — or
explicitly cite that nothing changed; `scripts/validate.py` rejects a `both`
document with an empty delta. Third, inside a `both` document every
single-build value is tagged inline *(B41)* / *(B42)*, so a reader on the
`legacy41` branch [2] never mistakes a 42.20 number for one that applies to
41.78.16.

# Practical Guidance

For a contributor (human or worker agent) writing a document:

- Write the file skeleton first — full front matter and all 19 headings —
  then research and fill it. An interrupted session should still leave a
  recoverable file.
- Decide the `build:` tag before writing the Reference section; it dictates
  whether you owe a substantive delta section and inline build tags.
- Cite as you write. If a sentence in an evidence section has no `[n]`, the
  sentence is either cut or moved to quarantine as a claim block. Do not
  plan to "add citations later".
- Use pzwiki for facts freely, but record the revision id and write your own
  sentence from scratch — do not start from the wiki's wording and edit it,
  because the n-gram gate catches light paraphrase.
- Prefer the Steam news API mirror of an official post over the bot-blocked
  blog URL, and Internet Archive snapshots for anything ephemeral.
- Run all five gates from the repo root and fix until green before handing
  the document back; a red gate is not a reviewer's problem to discover.

# Common Pitfalls & Troubleshooting

- **Uncited fact in a guidance section.** Guidance may only synthesise facts
  already cited above; a new number appearing first in "Practical Guidance"
  is a genre violation even if true.
- **Light paraphrase of pzwiki.** Rewriting a wiki sentence word-by-word
  still trips `check_license_hygiene.py` and, more importantly, still
  creates a derivative of NonCommercial-licensed text [3]. Extract the fact;
  write a new sentence.
- **`both` with a hollow delta.** A `both` document whose delta section says
  only "minor changes" fails validation; either document the delta with
  citations or retag the document to a single build.
- **Missing inline build tags.** A 42.20-only value quoted untagged in a
  `both` document silently misinforms `legacy41` readers — the exact failure
  the build system exists to prevent [1].
- **Guessed URLs.** A citation to a URL nobody opened is fabrication, even
  when the fact is right. Unopenable bot-blocked URLs are citable only when
  allowlisted and corroborated.
- **Sole-sourced hosting-KB numbers.** Hosting-company knowledge bases are
  marketing-adjacent; a hard number sourced only there caps the document at
  Medium confidence and must say so.
- **Claim blocks in the wrong shape.** The genre auditor expects `## Claim N`
  headings with the three bold bullets; `###` sub-headings or free prose in
  the quarantine section are flagged.

# Community Notes & Unverified Claims

None.

# Risks & Caveats

- The license summaries here are working rules for this project, not legal
  advice. The Creative Commons deed itself notes it is a human-readable
  summary of, and not a substitute for, the underlying legal code [3].
- PZwiki's licensing statement [5] is cited at a specific revision; the wiki
  could change its policy, so the revision id is the provenance anchor and
  the page should be re-checked at review time.
- The Indie Stone's terms page [4] sits on a bot-blocking host and was cited
  as an allowlisted URL corroborated by PZwiki's own link to it [5], not
  fetched directly; a human re-check of its current wording is cheap and
  worthwhile.
- Internal process claims (gate behaviour, template shape) are accurate as
  of the repo files on 2026-07-30; scripts evolve, and this document should
  be revised — with a version bump — when they do.

# Verification Steps

- Open https://creativecommons.org/licenses/by-nc-sa/3.0/ and confirm the
  BY, NC and SA terms summarised here [3].
- Query the PZwiki API for the copyright policy and confirm the licensing
  statement and revision id:
  `https://pzwiki.net/w/api.php?action=parse&page=PZwiki:Copyrights&prop=wikitext|revid&format=json` [5].
- Confirm the build-divergence facts against the Steam announcements [1] [2]
  (mirrored by the Steam news API, `ISteamNews`, app id 108600).
- Open `scripts/validate.py`, `scripts/audit_genre.py` and
  `scripts/check_license_hygiene.py` and confirm they enforce the structure,
  genre and license rules as described.
- Run the five gate commands from the repo root against any document and
  observe the enforcement first-hand.

# Open Questions

- **Outbound license for the KB's own prose.** The repository asserts
  original authorship but ships no LICENSE file declaring terms for reuse of
  its own text. A human decision is needed (e.g. CC BY 4.0, CC BY-SA, or all
  rights reserved), noting that ShareAlike obligations would only be
  triggered if pzwiki-derivative text existed — which the pipeline is
  designed to prevent.
- **Planned deterministic gates.** The API-existence gate (Modder docs vs
  pinned Umbrella/ZomboidDoc indices) and the server-setting gate (Admin
  docs vs per-build server.ini / SandboxVars schemas) are specified in
  `ROADMAP.md` but not yet live; this document should gain a section on them
  when they land.
- **Discord provenance.** The archive-and-cite workflow for ephemeral
  Discord primaries is specified in `SOURCE_REGISTRY.md` but the local
  archive store is not yet populated.

# References

**Primary Sources**

- [1] **The Indie Stone** — *B42 CHECKLIST* (Steam announcement, 2026-07-28). https://steamcommunity.com/games/108600/announcements/detail/1839041357038237 Accessed 2026-07-30 via the Steam news API (ISteamNews, app 108600); host is bot-block allowlisted.
- [2] **The Indie Stone** — *Build 42.20.0 Stable Released* (Steam announcement, 2026-07-29). https://steamcommunity.com/games/108600/announcements/detail/1839676055882259 Accessed 2026-07-30 via the Steam news API (ISteamNews, app 108600); host is bot-block allowlisted.
- [3] **Creative Commons** — *Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) deed*. https://creativecommons.org/licenses/by-nc-sa/3.0/ Accessed 2026-07-30.
- [4] **The Indie Stone** — *Project Zomboid — Terms & Conditions*. https://projectzomboid.com/blog/support/terms-conditions/ Accessed 2026-07-30. Bot-block allowlisted host; URL corroborated by the link in [5].

**Fact-Only Sources (no prose reuse)**

- [5] **PZwiki** — *PZwiki:Copyrights* (revision 1156861). https://pzwiki.net/wiki/PZwiki:Copyrights Accessed 2026-07-30 via the MediaWiki API. Fact-only source.

# Further Reading

- `SOURCE_REGISTRY.md` — the full ranked source-authority table this
  document summarises.
- `templates/document_template.md` — the 19-section template with its
  embedded genre, license and build rules.
- `prompts/worker_contract.md` — the operating contract handed to every
  writer.
- `CLAUDE.md` — the repository's operating rules, including the
  freeze/version/release policy.
- `ROADMAP.md` — planned deterministic gates and pipeline stages.

# Related Documents

- modders-foundation — the Modders track foundation (peer-engineer voice).
- players-foundation — the Players track foundation (survival-guide voice).
- admins-foundation — the Admins track foundation (ops-runbook voice).
- creator-foundation — the Creator track foundation (candid-strategist voice).
- lore-foundation — the Lore track foundation.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-07-30 | Orchestrator (KB Pipeline) | Approved and frozen — foundation cluster release kb-release-2026.07.30. | Standing mandate (2026-07-30) |
