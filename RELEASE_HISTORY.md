# Release History

Each release freezes a cluster: all gates green → human approval → per-doc
v1.0.0 → annotated git tag. Every tag records the game build(s) and the
Umbrella commit the release was validated against.

| Tag | Date | Scope | Game builds validated | Umbrella commit | Notes |
|-----|------|-------|----------------------|-----------------|-------|
| kb-release-2026.07.30 | 2026-07-30 | Foundation cluster: 6 tier-1 docs (all four tracks + lore + meta style guide) | 41.78.16 (legacy41), 42.20.0 (stable) | Release tag `42.20.0` (PZ-Umbrella/Umbrella) | All gates green; 107/107 links live independently verified; approved via standing mandate. |
| kb-release-2026.10.08 | 2026-10-08 | 42.21 re-baseline and full-corpus freeze: all 41 documents (Players, Admins, Modders, Creator, Lore, Meta) at `approved` | 42.21 (stable), 41.78.21 (legacy41) | Release tag `42.21.0` at commit `13d01f9ee58fa48773553920db56d06f0005e7f8` (PZ-Umbrella/Umbrella) | All gates green (validate, genre audit, license hygiene, API-existence 349 refs, server-settings, links 0 dead, freshness current); approved by the project owner on 2026-10-08, including re-approval of the six foundations. Not re-tested in game. |
