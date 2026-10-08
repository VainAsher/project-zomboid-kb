# Content License and Notices

Copyright (c) 2026 VainAsher. **All rights reserved** for the content
described below.

This file states the terms for the knowledge-base *content*. The repository's
*software* is separately licensed under the MIT License (see `LICENSE`). This
notice is a statement of the project owner's chosen terms, not legal advice.

## What is covered (all rights reserved)

| Path | What it is |
|------|------------|
| `docs/` | The knowledge-base documents (original prose, structure and selection) |
| `templates/` | The document template |
| `prompts/` | The worker operating contract |
| `exports/` | Generated knowledge graph, matrix, coverage report and RAG chunks (derived from `docs/`) |
| `*.md` at the repository root | README, status, index, glossary, source registry, changelog and similar |

No license to copy, adapt, redistribute, republish, train on or otherwise
reuse this content is granted, except as GitHub's Terms of Service allow for
viewing and forking a public repository on GitHub itself. To ask for
permission, contact the copyright holder.

Facts are not claimed. Only the original expression, selection and
arrangement in this content is covered; the underlying game facts remain
free for anyone to state and to verify against the cited primary sources.

## What is not covered (third-party material)

- **Project Zomboid.** The game, its name, art, text, audio and fiction are
  the trademarks and copyrights of The Indie Stone. This is an unofficial fan
  project, not affiliated with, endorsed by or sponsored by The Indie Stone.
  Quotations of game or Indie Stone text are minimal, attributed and cited.
  Nothing here relicenses any of it.
- **pzwiki.net (CC BY-NC-SA 3.0).** Used as a fact source only. The
  knowledge base copies none of its prose or tables, and an overlap gate
  checks this (`scripts/check_license_hygiene.py`). The local snapshots in
  `sources/pzwiki/*.txt` are git-ignored, are not distributed with this
  repository and remain under the wiki's license.
- **`sources/schemas/api-index-B41.json` and `api-index-B42.json`
  (and `archive/`).** Lists of class, member, event and global names that
  `scripts/extract_api_index.py` extracts from the PZ-Umbrella stub library.
  The upstream repository carries no license file at the pinned commits, so
  these name lists are provided for verification only and are not licensed
  by this repository.
- **`sources/schemas/server-settings.json`.** A list of server setting key
  names, extracted by `scripts/extract_server_schema.py` from this project's
  own Admin reference documents. Setting names are facts about the game, not
  expression, so this file is offered for verification use and is not
  claimed as protected content.
- **`sources/pins.json`.** Factual records of release tags, commit ids and
  game build numbers.
- **Cited third-party sites and tools.** Mentioned by name and linked,
  never rehosted. Their licenses and terms are their own.

## Citing and linking

Linking to the published site or to a document, and citing a document by
title, id and version, is welcome and needs no permission.
