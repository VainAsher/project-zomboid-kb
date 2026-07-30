# Worker Operating Contract

**You are a worker agent. You write exactly ONE document and nothing else.**
Follow this contract literally. It is written so that quality comes from the
*process*, not from how clever you are: if you do every step, the output passes.
Do not improvise around it. When in doubt, do the smaller, more literal thing.

---

## 0. Inputs you are given

- A **document id**, **title**, **category** (Modders | Players | Admins |
  Creator | Lore | Meta), **topic**, **build** (B41 | B42 | both | historic),
  **document_type**, and an exact **file path**.
- A **scope** (what to cover) and any entities/settings/API elements to examine.
- A list of **real sibling ids** for knowledge-graph edges.

## 1. Read these first (do not skip)

1. `templates/document_template.md` — the 19 sections, in order. Copy its shape.
2. `CLAUDE.md` — the genre, build-tag and license rules.
3. `SOURCE_REGISTRY.md` — the source classes and the **source-priority order**.
4. The **parent/foundation doc** named in your scope — go *deeper*, never restate.

## 2. Write the file skeleton IMMEDIATELY (crash-safety)

Before researching in depth, write the file to its exact path with the full
front matter and all 19 `#` section headings present (even if empty). Then fill
it in. **Rationale:** if your session is interrupted, a recoverable file exists.
A worker that researches for ten minutes and dies having written nothing has
produced nothing.

Front matter, exactly these keys:
`id, title, version: 0.1.0, status: in-review, confidence, category, topic,
build, document_type, created, updated, review_due, sources_verified,
supersedes, related, tags, game_versions_verified`.

## 3. The three rules that define this knowledge base

**Rule 1 — Never let a judgement or hearsay wear the costume of a fact.**

- **EVIDENCE layer** — `Reference`, `B41 vs B42 Delta`, `Build Applicability`.
  *Every sentence that asserts a fact carries a `[n]` citation* to a primary
  source: official blog/Thursdoid, Steam announcement/patch notes, game script
  files, the pinned Umbrella/ZomboidDoc API index, or a named, dated dev post.
  If you cannot cite it, cut it — or quarantine it (Rule 3).
- **GUIDANCE layer** — `Practical Guidance`, `Common Pitfalls`. May synthesise
  the cited facts; must not introduce new uncited facts.
- **QUARANTINE layer** — `Community Notes & Unverified Claims`. The ONLY place
  an uncited community claim may appear, always in the labelled claim-block
  shape (section 4).

**Rule 2 — The build tag is load-bearing.** `build:` must be correct. A
`both` document must fill `B41 vs B42 Delta` substantively. Any value that
holds on only one build must be tagged inline: *(B41)* / *(B42)*. When a
number was established during the B42-unstable cycle and not re-verified on
42.20, say so explicitly.

**Rule 3 — pzwiki is a fact source, never a prose source.** pzwiki.net is
CC BY-NC-SA 3.0; this project is commercially adjacent. You may cite a pzwiki
page (URL + revision id, classed "Fact-only") for a fact; you must write 100%
original prose. Never copy or lightly paraphrase pzwiki sentences or table
layouts. The license-hygiene gate flags n-gram overlap mechanically and a
flag fails your document.

## 4. The Community Notes & Unverified Claims section — use this EXACT shape

For every quarantined claim, copy this block verbatim in structure (canonical
form — heading at `##`, three bold bullets). The genre auditor checks for them:

```
## Claim N — <one-line statement of the community claim>

- **Claim:** <what the community says, attributed to where it circulates>.
- **Why unverified:** <no primary source found / unstable-era value / conflicts with [n]>.
- **Confidence:** <High | Medium | Low>. <one sentence why>.
```

If there are no such claims, write exactly "None." Do **not** use `###` for
claim sub-parts (breaks markdownlint MD001). Use `##`.

## 5. Confidence rubric — apply mechanically, do not inflate

Rate the **document** and **each quarantined claim** by the weakest evidence
they rest on:

- **High** — rests on primary sources (patch notes, game files, pinned API
  stubs) and/or first-hand in-game verification; little or no inference.
- **Medium** — a mix of primary fact and corroborated secondary sources; some
  values not re-verified against the current patch.
- **Low** — largely community-sourced, unstable-era, or sources conflict.

Hard floor: **a numeric game value sourced only from a hosting-company KB or a
community guide may not be rated above Medium.** A document whose core values
were last verified on a superseded patch may not be rated High. Being honestly
"Low" is a success, not a failure.

## 6. Sources — pick from the list, never invent

- Reach for sources in the **priority order** in `SOURCE_REGISTRY.md`
  (official primaries → code truth (Umbrella/ZomboidDoc) → pzwiki facts-only →
  server tooling repos → hosting KBs / community, corroborate-only).
- **Never fabricate or guess a URL.** If you cannot open it, do not cite it.
- Classify every reference: Primary / Fact-Only (pzwiki) / Secondary &
  Corroborating / Community & Creator / Further Reading. Number them
  contiguously from `[1]`; every `[n]` in the text must resolve, and every
  reference must be cited at least once.
- These hosts bot-block automated checkers but their URLs are real — you MAY
  cite them (the checker warns, does not fail): projectzomboid.com,
  theindiestone.com, store.steampowered.com, steamcommunity.com, discord.com/
  discord.gg. Prefer the Steam news API mirror of a blog post where one exists,
  and Internet Archive snapshots for anything ephemeral.
- Never sole-source a hard number from a hosting-company KB (BisectHosting,
  Shockbyte, etc.) — corroborate against a primary or rate it Medium and say so.

## 7. Self-check GATE — run all five, fix until green, THEN return

```
python scripts/validate.py <your-file>
python scripts/audit_genre.py --strict <your-file>
python scripts/check_license_hygiene.py <your-file>
npx --no-install markdownlint-cli2 --fix <your-file>
python scripts/check_links.py <your-file>
```

Return criteria: validate = 0 issues; genre audit = clean; license hygiene =
clean; markdownlint = 0 errors; links = **0 dead** (allowlisted warnings are
fine). If any gate fails, fix and re-run. Do not return a red gate.

## 8. Return — machine-readable, so the merge is mechanical

Reply with a single fenced ```json block in this exact shape (the orchestrator
consumes it without interpretation):

```json
{
  "id": "<doc-id>",
  "index_row": {
    "title": "...", "topic": "...", "tier": 2, "build": "both",
    "confidence": "Medium", "path": "docs/.../<id>.md"
  },
  "kg_edges": [
    {"rel": "deepens", "to": "<sibling-id>"}
  ],
  "glossary": [
    {"term": "...", "definition": "...", "source_key": "<key or ->"}
  ],
  "sources": [
    {"key": "...", "source": "...", "class": "Primary", "publisher": "...", "url": "https://..."}
  ],
  "qa": {"validate": "pass", "genre": "clean", "license": "clean", "markdownlint": 0, "links_live": "42/42", "links_dead": 0},
  "confidence": "Medium",
  "flags": ["...anything a human should eyeball..."]
}
```

Then stop. Do not edit `MASTER_INDEX.md`, `GLOSSARY.md`, `SOURCE_REGISTRY.md`,
any other shared file, or run git. Those are the orchestrator's job.
