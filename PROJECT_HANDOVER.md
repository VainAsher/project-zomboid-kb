# Project Handover — read this first in a fresh session

You are the **orchestrator** of an evidence-based Project Zomboid knowledge
base built on the kb-factory chassis. Quality comes from the process and its
deterministic gates, not from model cleverness.

## Where things stand

Read `PROJECT_STATUS.md` for the current stage. As of bootstrap the repo is
at the **hard human-approval gate**: no documents may be generated until the
user approves the taxonomy in `MASTER_INDEX.md` (bottom section), the source
registry, and the first cluster.

## How the factory runs (post-approval)

1. Pick the approved cluster; define each document's id/title/category/topic/
   build/document_type/path/scope + sibling ids.
2. Spawn one worker per document, handing `prompts/worker_contract.md`
   **verbatim** plus the scope. Workers write only their own file and return
   the contract's JSON.
3. You own all shared files (`MASTER_INDEX.md`, `GLOSSARY.md`,
   `SOURCE_REGISTRY.md`), git, and releases. Merge the JSON returns
   mechanically.
4. **Independently re-run** `python scripts/check_links.py` — 0 dead links on
   your own run, not the worker's word.
5. All gates green (see `CLAUDE.md`) → human gate → freeze cluster at v1.0.0
   per doc → `git tag kb-release-YYYY.MM.DD` recording game build + pinned
   Umbrella commit.
6. Offer the user a standing "auto-approve on green QA" mandate; pause only on
   gate failures or unverifiable core claims.

## Non-negotiables

- Build tags on everything; `both` docs need a substantive delta section.
- pzwiki = facts only, never prose (CC BY-NC-SA 3.0 vs commercial context).
- Never fabricate URLs; hosting-company numbers are corroborate-only.
- Publishing to a public GitHub repo only on explicit per-repo authorization.
