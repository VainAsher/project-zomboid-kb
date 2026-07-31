---
id: kebab-case-unique-id
title: "Human-Readable Title"
version: 0.1.0
status: draft            # draft | in-review | approved | frozen | superseded
confidence: Medium       # High | Medium | Low  (see confidence rubric below)
category: Players        # Modders | Players | Admins | Creator | Lore | Meta
topic: "Skills & XP"
build: both              # B41 | B42 | both | historic  — REQUIRED version tag
document_type: reference # reference | mechanic | api | server-setting | tutorial | overview
created: 2026-07-30
updated: 2026-07-30
review_due: 2026-10-30
sources_verified: 2026-07-30
supersedes: null
related: []              # list of related document ids
tags: []
game_versions_verified: ["41.78.16", "42.20"]  # exact versions checked first-hand or via patch notes
---

<!--
  GENRE = reference. The cardinal rule of this knowledge base:
  NEVER let a judgement or hearsay wear the costume of a fact.
    • "Reference" and "B41 vs B42 Delta" are the EVIDENCE layer — every claim
      there is cited to a primary source (official blog/patch notes, Steam
      announcements, game script files, Umbrella/ZomboidDoc API indices, dev
      Discord/forum posts) with a working link.
    • "Community Notes & Unverified Claims" is the QUARANTINE layer — clearly
      labelled community claims that cannot (yet) be traced to a primary,
      each carrying its own confidence rating and why it is unverified.
  Keep the section order below; the QA validator enforces it.

  LICENSE RULE (hard): pzwiki.net is CC BY-NC-SA 3.0. It may be used as a FACT
  source (cite URL + revision), but its prose and tables must NEVER be copied
  or lightly paraphrased. Write 100% original prose. The license-hygiene gate
  (scripts/check_license_hygiene.py) flags n-gram overlap mechanically.

  BUILD RULE (hard): `build:` is required. B41 = the legacy41 branch
  (41.78.x maintenance line; record the exact version you verified against).
  B42 = Build 42 stable (42.20+) only. both = document covers both builds and
  MUST carry a substantive "B41 vs B42 Delta" section. historic = older
  builds / lore. Any B42-only value quoted in a `both` document must be
  tagged inline, e.g. "(B42)".

  Confidence rubric (document-level `confidence:` field):
    High   — claims rest on primary sources (official patch notes, game files,
             pinned API stubs) and/or first-hand in-game verification.
    Medium — a mix of primary fact and corroborated secondary sources; some
             values not re-verified against the current patch.
    Low    — largely community-sourced, unstable-era, or conflicting sources.
-->

# Document Control

| Field | Value |
|-------|-------|
| Document ID | kebab-case-unique-id |
| Version | 0.1.0 |
| Status | draft |
| Confidence | Medium |
| Category (track) | Players |
| Build | both |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-07-30 |
| Updated | 2026-07-30 |
| Review due | 2026-10-30 |
| Game versions verified | *e.g. 41.78.16, 42.20* |

# Executive Summary

Two or three short paragraphs: what this document covers, how the mechanic /
API / setting behaves in the current builds, and the headline B41→B42 change
if any. State the document-level confidence and why.

# Key Takeaways

- Bullet the 4–8 most important, decision-useful points.
- Mark each as *(cited)* or *(community, unverified)* so the reader can tell
  primary-sourced fact from quarantined hearsay at a glance.
- Tag build-specific points inline: *(B41)*, *(B42)*, *(both)*.

# Purpose

Why this document exists and what question it answers for the reader
(a player, a mod developer, a server admin, or a content creator).

# Scope

What is and is not covered — which entities, which builds (B41.78 legacy /
B42.20 stable), and any deliberate exclusions (e.g. unstable-branch behaviour).

# Definitions

Document-specific terms. Prefer the shared `GLOSSARY.md`; define here only
narrowed or document-specific usages.

# Build Applicability

State exactly which game versions the facts in this document were verified
against, and what happens on the other build. Example [1]:

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Yes | 41.78.16 | Behaviour X differs — see Delta |
| B42 (stable) | Yes | 42.20 | Current as of 2026-07-30 |

# Reference

**Evidence layer — cite everything.** The factual core: how the mechanic
works, what the API element does, what the setting controls, exact values and
ranges. Every sentence that asserts a fact carries a `[n]` citation to a
primary source [1]. Use tables for enumerable values. Do not editorialise
here — record what is documented, with the build tag on any value that is not
`both` [2].

# B41 vs B42 Delta

**Evidence layer — cite everything.** What changed between Build 41.78 and
Build 42.20 for this document's subject: renames, rebalances, refactors,
removals, additions [2]. If the document is single-build and no delta exists,
state "Not applicable — single-build document." and why. A `build: both`
document must fill this section substantively (the validator enforces it).

# Practical Guidance

The track-voiced "so what": tips for players, code patterns for modders,
copy-pasteable commands for admins, production notes for creators. Guidance
may synthesise the cited facts above but must not introduce new uncited facts.

# Common Pitfalls & Troubleshooting

Known failure modes, gotchas and misconceptions, each traced back to the
cited behaviour above (or explicitly quarantined below if community-sourced).

# Community Notes & Unverified Claims

**Quarantine layer — label it.** Claims circulating in the community that are
useful but not yet traceable to a primary source. Repeat the block below for
each claim; the genre auditor (`scripts/audit_genre.py`) enforces the three
bullets. If there are none, write "None."

## Claim 1 — <one-line statement of the community claim>

- **Claim:** <what the community says, attributed to where it circulates>.
- **Why unverified:** <no primary source found / unstable-era value / conflicts with [n]>.
- **Confidence:** <High | Medium | Low>. <one sentence why>.

# Risks & Caveats

Risks in the document itself: source recency vs the current hotfix wave,
values established during the unstable cycle, single-sourced numbers, and
anything a hotfix could invalidate. Honest about what could be wrong.

# Verification Steps

Concrete steps a reader (or a re-verification worker) can take to confirm the
key facts first-hand: which game files to open, which in-game test to run,
which debug/admin command to issue, which API stub to grep.

# Open Questions

What remains unverified or contested, and what would resolve it. Feeds the
research backlog and the freshness re-queue.

# References

Cite every factual claim. Number contiguously from [1]; every number must
resolve here and be cited in the text. Split by class:

**Primary Sources** — official blog/Thursdoids, Steam announcements/patch notes, game script files, Umbrella/ZomboidDoc API indices, dev posts.

- [1] **The Indie Stone** — *Post or patch-note title*. URL. Accessed 2026-07-30.

**Fact-Only Sources (no prose reuse)** — pzwiki (CC BY-NC-SA 3.0): cite URL + revision id; facts only, never prose.

- [2] **PZwiki** — *Page title* (revision NNNNN). URL. Accessed 2026-07-30. Fact-only source.

**Secondary & Corroborating** — hosting-company KBs, Steam guides, tooling repos.

**Community & Creator** — named forum/Discord/Reddit threads, videos (dated).

**Further Reading**

# Further Reading

Non-cited but useful background.

# Related Documents

Links to related knowledge-base documents (by id).

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-07-30 | KB Pipeline (virtual agent) | Initial draft. | — |
