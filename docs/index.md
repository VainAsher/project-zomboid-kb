# Project Zomboid Knowledge Base (B41 & B42)

!!! warning "Unofficial fan reference — not affiliated with The Indie Stone"
    This is an unofficial, community-produced research reference. It is not affiliated with, endorsed by, or sponsored by The Indie Stone. Project Zomboid and all related content are trademarks and copyrights of The Indie Stone. Every document carries a build tag (B41 / B42 / both); the game moves fast — verify against the current patch notes and in-game behaviour before relying on any value.

Evidence-based, source-cited Project Zomboid reference for modders, players, server admins and creators — every document version-tagged for Build 41 (legacy41) and Build 42.

**12 documents** across **11 topics** — every factual claim carries a citation to a primary or authoritative source, unverified community claims are labelled and quarantined, and build tags, links, citations and structure are checked automatically in CI.

*Confidence: 1 High · 11 Medium · 0 Low.*  *Build: B42 2 · both 9 · historic 1.*

## Class 1 — Track foundations (Modders / Players / Admins / Creator)

- [Running a Project Zomboid Dedicated Server: Architecture, Branches and Hosting Choices](admins/admins-foundation.md) — *Server foundations* (both)
- [The Project Zomboid Content Landscape: Formats, Channels and the B42-Stable Window](creator/creator-foundation.md) — *Creator foundations* (B42)
- [The Knox Event and the History of Project Zomboid's Builds](lore/lore-foundation.md) — *Lore & history* (historic)
- [How This Knowledge Base Is Written: Genre, Build Tags and License Rules](meta/meta-style-guide.md) — *KB governance* (both)
- [Modding Project Zomboid: Ecosystem, Toolchain and Where the API Truth Lives](modders/modders-foundation.md) — *Modding foundations* (both)
- [Surviving Knox Country: The Core Game Across Build 41 and Build 42](players/players-foundation.md) — *Player foundations* (both)

## Class 2 — Core reference (mechanics, entities, API, settings)

- [SandboxVars Reference: Gameplay Rules per Server](admins/admins-sandboxvars-reference.md) — *Server configuration* (both)
- [server.ini Reference: The Settings That Matter, by Area](admins/admins-server-ini-reference.md) — *Server configuration* (both)
- [Animals and Husbandry in Build 42](players/players-animals-husbandry.md) — *Animals & husbandry* (B42)
- [The B42 Crafting Overhaul: From Knapping to Blacksmithing](players/players-crafting-chains.md) — *Crafting* (both)
- [Skills and XP: Levelling, Multipliers and the B42 Skill Roster](players/players-skills-xp.md) — *Skills & XP* (both)
- [Traits and Occupations: Points, Rosters and the B42 Rework](players/players-traits-occupations.md) — *Traits & occupations* (both)

## Knowledge graph

??? note "Cross-reference graph (click to expand)"

    ```mermaid
    graph LR
      subgraph Tier1["Tier 1"]
        admins_foundation["admins-foundation"]
        creator_foundation["creator-foundation"]
        lore_foundation["lore-foundation"]
        meta_style_guide["meta-style-guide"]
        modders_foundation["modders-foundation"]
        players_foundation["players-foundation"]
      end
      subgraph Tier2["Tier 2"]
        admins_sandboxvars_reference["admins-sandboxvars-reference"]
        admins_server_ini_reference["admins-server-ini-reference"]
        players_animals_husbandry["players-animals-husbandry"]
        players_crafting_chains["players-crafting-chains"]
        players_skills_xp["players-skills-xp"]
        players_traits_occupations["players-traits-occupations"]
      end
      meta_style_guide -->|governs| modders_foundation
      meta_style_guide -->|governs| players_foundation
      meta_style_guide -->|governs| creator_foundation
      meta_style_guide -->|governs| lore_foundation
      meta_style_guide -->|governs| admins_foundation
      players_foundation -->|complements| modders_foundation
      players_foundation -->|complements| creator_foundation
      players_foundation -->|complements| lore_foundation
      players_foundation -->|complements| admins_foundation
      players_foundation -->|conforms_to| meta_style_guide
      lore_foundation -->|informs| players_foundation
      lore_foundation -->|informs| modders_foundation
      lore_foundation -->|informs| creator_foundation
      lore_foundation -->|informs| admins_foundation
      lore_foundation -->|conforms_to| meta_style_guide
      modders_foundation -->|relates_to| players_foundation
      modders_foundation -->|relates_to| creator_foundation
      modders_foundation -->|relates_to| lore_foundation
      modders_foundation -->|relates_to| meta_style_guide
      modders_foundation -->|relates_to| admins_foundation
      creator_foundation -->|complements| modders_foundation
      creator_foundation -->|complements| players_foundation
      creator_foundation -->|complements| lore_foundation
      creator_foundation -->|complements| admins_foundation
      creator_foundation -->|conforms_to| meta_style_guide
      admins_foundation -->|related| players_foundation
      admins_foundation -->|related| modders_foundation
      admins_foundation -->|related| creator_foundation
      admins_foundation -->|related| lore_foundation
      admins_foundation -->|conforms_to| meta_style_guide
      players_skills_xp -->|deepens| players_foundation
      players_skills_xp -->|relates_to| players_traits_occupations
      players_skills_xp -->|relates_to| players_crafting_chains
      players_skills_xp -->|relates_to| players_animals_husbandry
      players_skills_xp -->|conforms_to| meta_style_guide
      players_traits_occupations -->|deepens| players_foundation
      players_traits_occupations -->|related| players_skills_xp
      players_traits_occupations -->|related| players_crafting_chains
      players_traits_occupations -->|related| players_animals_husbandry
      players_traits_occupations -->|conforms_to| meta_style_guide
      players_crafting_chains -->|deepens| players_foundation
      players_crafting_chains -->|relates_to| players_skills_xp
      players_crafting_chains -->|relates_to| players_traits_occupations
      players_crafting_chains -->|complements| players_animals_husbandry
      players_crafting_chains -->|informs| modders_foundation
      players_crafting_chains -->|conforms_to| meta_style_guide
      admins_sandboxvars_reference -->|deepens| admins_foundation
      admins_sandboxvars_reference -->|complements| admins_server_ini_reference
      admins_server_ini_reference -->|deepens| admins_foundation
      admins_server_ini_reference -->|complements| admins_sandboxvars_reference
      admins_server_ini_reference -->|complements| modders_foundation
      admins_server_ini_reference -->|complements| meta_style_guide
      players_animals_husbandry -->|deepens| players_foundation
      players_animals_husbandry -->|relates_to| players_skills_xp
      players_animals_husbandry -->|relates_to| players_crafting_chains
      players_animals_husbandry -->|relates_to| players_traits_occupations
      players_animals_husbandry -->|conforms_to| meta_style_guide
      admins_sandboxvars_reference -->|informs| players_foundation
      admins_sandboxvars_reference -->|conforms_to| meta_style_guide
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a document matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

