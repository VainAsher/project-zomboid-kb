# Project Zomboid Knowledge Base (B41 & B42)

!!! warning "Unofficial fan reference — not affiliated with The Indie Stone"
    This is an unofficial, community-produced research reference. It is not affiliated with, endorsed by, or sponsored by The Indie Stone. Project Zomboid and all related content are trademarks and copyrights of The Indie Stone. Every document carries a build tag (B41 / B42 / both); the game moves fast — verify against the current patch notes and in-game behaviour before relying on any value.

Evidence-based, source-cited Project Zomboid reference for modders, players, server admins and creators — every document version-tagged for Build 41 (legacy41) and Build 42.

**33 documents** across **26 topics** — every factual claim carries a citation to a primary or authoritative source, unverified community claims are labelled and quarantined, and build tags, links, citations and structure are checked automatically in CI.

*Confidence: 1 High · 32 Medium · 0 Low.*  *Build: B41 1 · B42 4 · both 27 · historic 1.*

## Class 1 — Track foundations (Modders / Players / Admins / Creator)

- [Running a Project Zomboid Dedicated Server: Architecture, Branches and Hosting Choices](admins/admins-foundation.md) — *Server foundations* (both)
- [The Project Zomboid Content Landscape: Formats, Channels and the B42-Stable Window](creator/creator-foundation.md) — *Creator foundations* (B42)
- [The Knox Event and the History of Project Zomboid's Builds](lore/lore-foundation.md) — *Lore & history* (historic)
- [How This Knowledge Base Is Written: Genre, Build Tags and License Rules](meta/meta-style-guide.md) — *KB governance* (both)
- [Modding Project Zomboid: Ecosystem, Toolchain and Where the API Truth Lives](modders/modders-foundation.md) — *Modding foundations* (both)
- [Surviving Knox Country: The Core Game Across Build 41 and Build 42](players/players-foundation.md) — *Player foundations* (both)

## Class 2 — Core reference (mechanics, entities, API, settings)

- [Backups, Saves and Migration: Protecting a Server World](admins/admins-backups-migration.md) — *Server operations* (both)
- [Server Performance: Memory, CPU and the Levers That Are Actually Documented](admins/admins-performance-tuning.md) — *Server operations* (both)
- [RCON and Admin Commands: Operating a Live Server](admins/admins-rcon-commands.md) — *Server operations* (both)
- [SandboxVars Reference: Gameplay Rules per Server](admins/admins-sandboxvars-reference.md) — *Server configuration* (both)
- [server.ini Reference: The Settings That Matter, by Area](admins/admins-server-ini-reference.md) — *Server configuration* (both)
- [Wiring Workshop Mods into a Server: IDs, Load Order and Updates](admins/admins-workshop-mod-wiring.md) — *Server operations* (both)
- [Events and Callbacks: Hooking the Game Loop with Events.X.Add](modders/modders-events-callbacks.md) — *Events & callbacks* (both)
- [Item Scripts, Recipes and Loot Distributions: Defining Content Through Script Files](modders/modders-item-scripts-distributions.md) — *Item scripts & distributions* (both)
- [The Project Zomboid Lua API Surface: Java-Exposed Classes, Globals and the Per-Build Differences](modders/modders-lua-api-surface.md) — *Lua API surface* (both)
- [mod.info, Mod IDs and the B42 Versioned Mod Folder Layout](modders/modders-modinfo-modid-conventions.md) — *mod.info & Mod ID conventions* (both)
- [PZAPI.ModOptions and the B42 Mod Settings API: Building an Options Screen](modders/modders-modoptions-pzapi.md) — *ModOptions & PZAPI* (both)
- [Multiplayer Mod Networking: Client/Server Lua, sendClientCommand and Porting for B42 MP](modders/modders-mp-networking-porting.md) — *MP networking porting* (both)
- [Animals and Husbandry in Build 42](players/players-animals-husbandry.md) — *Animals & husbandry* (B42)
- [The B42 Crafting Overhaul: From Knapping to Blacksmithing](players/players-crafting-chains.md) — *Crafting* (both)
- [Farming, Foraging and Food: Feeding a Survivor Long-Term](players/players-farming-food.md) — *Farming & food* (both)
- [Knox Country Locations: The B41 Towns and the B42 Expansion](players/players-map-locations.md) — *Map & locations* (both)
- [Health, Injuries and Moodles: The Body Simulation](players/players-medical-moodles.md) — *Medical & moodles* (both)
- [Skills and XP: Levelling, Multipliers and the B42 Skill Roster](players/players-skills-xp.md) — *Skills & XP* (both)
- [Traits and Occupations: Points, Rosters and the B42 Rework](players/players-traits-occupations.md) — *Traits & occupations* (both)
- [Vehicles: Finding, Fixing and Driving Across Both Builds](players/players-vehicles.md) — *Vehicles* (both)

## Class 3 — Guides, tutorials & runbooks

- [Keeping a Build 41 Server Alive: The legacy41 Runbook](admins/admins-legacy41-runbook.md) — *Server runbooks* (B41)
- [Running a Modded Server: Selection, Rollout and Update Discipline](admins/admins-modded-server-runbook.md) — *Server runbooks* (both)
- [Ubuntu Dedicated Server Runbook: SteamCMD to systemd](admins/admins-ubuntu-runbook.md) — *Server runbooks* (both)
- [Your First Build 42 Mod: A Verified Step-by-Step Tutorial](modders/modders-first-mod-tutorial-b42.md) — *First mod tutorial* (B42)
- [Porting a Build 41 Mod to Build 42: A Diff-Driven Checklist](modders/modders-porting-b41-to-b42.md) — *Porting B41 mods to B42* (both)
- [The B41 Veteran's Guide to Build 42: What Your Instincts Get Wrong](players/players-b41-to-b42-transition.md) — *Guides* (both)
- [Starting Project Zomboid on Build 42.20: A First-Week Survival Guide](players/players-beginner-guide-b42.md) — *Guides* (B42)

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
        admins_backups_migration["admins-backups-migration"]
        admins_performance_tuning["admins-performance-tuning"]
        admins_rcon_commands["admins-rcon-commands"]
        admins_sandboxvars_reference["admins-sandboxvars-reference"]
        admins_server_ini_reference["admins-server-ini-reference"]
        admins_workshop_mod_wiring["admins-workshop-mod-wiring"]
        modders_events_callbacks["modders-events-callbacks"]
        modders_item_scripts_distributions["modders-item-scripts-distributions"]
        modders_lua_api_surface["modders-lua-api-surface"]
        modders_modinfo_modid_conventions["modders-modinfo-modid-conventions"]
        modders_modoptions_pzapi["modders-modoptions-pzapi"]
        modders_mp_networking_porting["modders-mp-networking-porting"]
        players_animals_husbandry["players-animals-husbandry"]
        players_crafting_chains["players-crafting-chains"]
        players_farming_food["players-farming-food"]
        players_map_locations["players-map-locations"]
        players_medical_moodles["players-medical-moodles"]
        players_skills_xp["players-skills-xp"]
        players_traits_occupations["players-traits-occupations"]
        players_vehicles["players-vehicles"]
      end
      subgraph Tier3["Tier 3"]
        admins_legacy41_runbook["admins-legacy41-runbook"]
        admins_modded_server_runbook["admins-modded-server-runbook"]
        admins_ubuntu_runbook["admins-ubuntu-runbook"]
        modders_first_mod_tutorial_b42["modders-first-mod-tutorial-b42"]
        modders_porting_b41_to_b42["modders-porting-b41-to-b42"]
        players_b41_to_b42_transition["players-b41-to-b42-transition"]
        players_beginner_guide_b42["players-beginner-guide-b42"]
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
      players_map_locations -->|deepens| players_foundation
      players_map_locations -->|relates_to| lore_foundation
      players_map_locations -->|relates_to| meta_style_guide
      players_map_locations -->|relates_to| players_vehicles
      players_vehicles -->|deepens| players_foundation
      players_vehicles -->|related| players_skills_xp
      players_vehicles -->|related| players_map_locations
      players_vehicles -->|conforms_to| meta_style_guide
      admins_rcon_commands -->|deepens| admins_foundation
      admins_rcon_commands -->|complements| admins_server_ini_reference
      admins_rcon_commands -->|complements| admins_sandboxvars_reference
      admins_rcon_commands -->|conforms_to| meta_style_guide
      admins_backups_migration -->|deepens| admins_foundation
      admins_backups_migration -->|references| admins_server_ini_reference
      admins_backups_migration -->|references| admins_sandboxvars_reference
      admins_backups_migration -->|references| lore_foundation
      admins_backups_migration -->|references| meta_style_guide
      admins_performance_tuning -->|deepens| admins_foundation
      admins_performance_tuning -->|complements| admins_server_ini_reference
      admins_performance_tuning -->|complements| admins_sandboxvars_reference
      admins_performance_tuning -->|complements| meta_style_guide
      players_medical_moodles -->|deepens| players_foundation
      players_medical_moodles -->|cross_references| players_skills_xp
      players_medical_moodles -->|cross_references| admins_sandboxvars_reference
      players_medical_moodles -->|conforms_to| meta_style_guide
      players_b41_to_b42_transition -->|deepens| players_foundation
      players_b41_to_b42_transition -->|cross_references| players_skills_xp
      players_b41_to_b42_transition -->|cross_references| players_traits_occupations
      players_b41_to_b42_transition -->|cross_references| players_crafting_chains
      players_b41_to_b42_transition -->|cross_references| players_animals_husbandry
      players_b41_to_b42_transition -->|cross_references| players_medical_moodles
      players_b41_to_b42_transition -->|cross_references| players_map_locations
      players_b41_to_b42_transition -->|cross_references| players_vehicles
      players_b41_to_b42_transition -->|conforms_to| meta_style_guide
      players_farming_food -->|deepens| players_foundation
      players_farming_food -->|complements| players_animals_husbandry
      players_farming_food -->|relates_to| players_crafting_chains
      players_farming_food -->|relates_to| players_skills_xp
      players_farming_food -->|conforms_to| meta_style_guide
      admins_legacy41_runbook -->|deepens| admins_foundation
      admins_legacy41_runbook -->|cross_references| admins_backups_migration
      admins_legacy41_runbook -->|cross_references| admins_server_ini_reference
      admins_legacy41_runbook -->|related| lore_foundation
      admins_legacy41_runbook -->|conforms_to| meta_style_guide
      admins_sandboxvars_reference -->|informs| players_foundation
      admins_sandboxvars_reference -->|conforms_to| meta_style_guide
      admins_ubuntu_runbook -->|deepens| admins_foundation
      admins_ubuntu_runbook -->|complements| admins_server_ini_reference
      admins_ubuntu_runbook -->|complements| admins_backups_migration
      admins_ubuntu_runbook -->|related| admins_workshop_mod_wiring
      admins_ubuntu_runbook -->|related| admins_modded_server_runbook
      admins_ubuntu_runbook -->|conforms_to| meta_style_guide
      admins_workshop_mod_wiring -->|deepens| admins_foundation
      admins_workshop_mod_wiring -->|deepens| admins_server_ini_reference
      admins_workshop_mod_wiring -->|deepens| modders_foundation
      admins_workshop_mod_wiring -->|related| admins_modded_server_runbook
      admins_workshop_mod_wiring -->|related| admins_ubuntu_runbook
      admins_workshop_mod_wiring -->|conforms_to| meta_style_guide
      admins_modded_server_runbook -->|deepens| admins_foundation
      admins_modded_server_runbook -->|deepens| admins_workshop_mod_wiring
      admins_modded_server_runbook -->|related| admins_ubuntu_runbook
      admins_modded_server_runbook -->|related| admins_backups_migration
      admins_modded_server_runbook -->|related| admins_performance_tuning
      admins_modded_server_runbook -->|conforms_to| meta_style_guide
      players_beginner_guide_b42 -->|deepens| players_foundation
      players_beginner_guide_b42 -->|cross_references| players_skills_xp
      players_beginner_guide_b42 -->|cross_references| players_traits_occupations
      players_beginner_guide_b42 -->|cross_references| players_medical_moodles
      players_beginner_guide_b42 -->|cross_references| players_map_locations
      players_beginner_guide_b42 -->|conforms_to| meta_style_guide
      modders_lua_api_surface -->|deepens| modders_foundation
      modders_lua_api_surface -->|related| modders_events_callbacks
      modders_lua_api_surface -->|related| modders_modoptions_pzapi
      modders_lua_api_surface -->|related| modders_item_scripts_distributions
      modders_lua_api_surface -->|related| modders_mp_networking_porting
      modders_lua_api_surface -->|related| modders_modinfo_modid_conventions
      modders_lua_api_surface -->|related| modders_first_mod_tutorial_b42
      modders_lua_api_surface -->|related| modders_porting_b41_to_b42
      modders_lua_api_surface -->|conforms_to| meta_style_guide
      modders_events_callbacks -->|deepens| modders_foundation
      modders_events_callbacks -->|related| modders_lua_api_surface
      modders_events_callbacks -->|related| modders_modoptions_pzapi
      modders_events_callbacks -->|related| modders_item_scripts_distributions
      modders_events_callbacks -->|related| modders_mp_networking_porting
      modders_events_callbacks -->|related| modders_modinfo_modid_conventions
      modders_events_callbacks -->|related| modders_first_mod_tutorial_b42
      modders_events_callbacks -->|related| modders_porting_b41_to_b42
      modders_events_callbacks -->|conforms_to| meta_style_guide
      modders_modoptions_pzapi -->|deepens| modders_foundation
      modders_modoptions_pzapi -->|related| modders_lua_api_surface
      modders_modoptions_pzapi -->|related| modders_events_callbacks
      modders_modoptions_pzapi -->|related| modders_item_scripts_distributions
      modders_modoptions_pzapi -->|related| modders_mp_networking_porting
      modders_modoptions_pzapi -->|related| modders_modinfo_modid_conventions
      modders_modoptions_pzapi -->|related| modders_first_mod_tutorial_b42
      modders_modoptions_pzapi -->|related| modders_porting_b41_to_b42
      modders_modoptions_pzapi -->|conforms_to| meta_style_guide
      modders_item_scripts_distributions -->|deepens| modders_foundation
      modders_item_scripts_distributions -->|related| modders_lua_api_surface
      modders_item_scripts_distributions -->|related| modders_events_callbacks
      modders_item_scripts_distributions -->|related| modders_modoptions_pzapi
      modders_item_scripts_distributions -->|related| modders_mp_networking_porting
      modders_item_scripts_distributions -->|related| modders_modinfo_modid_conventions
      modders_item_scripts_distributions -->|related| modders_first_mod_tutorial_b42
      modders_item_scripts_distributions -->|related| modders_porting_b41_to_b42
      modders_item_scripts_distributions -->|conforms_to| meta_style_guide
      modders_mp_networking_porting -->|deepens| modders_foundation
      modders_mp_networking_porting -->|related| modders_lua_api_surface
      modders_mp_networking_porting -->|related| modders_events_callbacks
      modders_mp_networking_porting -->|related| modders_modoptions_pzapi
      modders_mp_networking_porting -->|related| modders_item_scripts_distributions
      modders_mp_networking_porting -->|related| modders_modinfo_modid_conventions
      modders_mp_networking_porting -->|related| modders_first_mod_tutorial_b42
      modders_mp_networking_porting -->|related| modders_porting_b41_to_b42
      modders_mp_networking_porting -->|conforms_to| meta_style_guide
      modders_modinfo_modid_conventions -->|deepens| modders_foundation
      modders_modinfo_modid_conventions -->|related| modders_lua_api_surface
      modders_modinfo_modid_conventions -->|related| modders_events_callbacks
      modders_modinfo_modid_conventions -->|related| modders_modoptions_pzapi
      modders_modinfo_modid_conventions -->|related| modders_item_scripts_distributions
      modders_modinfo_modid_conventions -->|related| modders_mp_networking_porting
      modders_modinfo_modid_conventions -->|related| modders_first_mod_tutorial_b42
      modders_modinfo_modid_conventions -->|related| modders_porting_b41_to_b42
      modders_modinfo_modid_conventions -->|conforms_to| meta_style_guide
      modders_first_mod_tutorial_b42 -->|deepens| modders_foundation
      modders_first_mod_tutorial_b42 -->|related| modders_lua_api_surface
      modders_first_mod_tutorial_b42 -->|related| modders_events_callbacks
      modders_first_mod_tutorial_b42 -->|related| modders_modoptions_pzapi
      modders_first_mod_tutorial_b42 -->|related| modders_item_scripts_distributions
      modders_first_mod_tutorial_b42 -->|related| modders_mp_networking_porting
      modders_first_mod_tutorial_b42 -->|related| modders_modinfo_modid_conventions
      modders_first_mod_tutorial_b42 -->|related| modders_porting_b41_to_b42
      modders_first_mod_tutorial_b42 -->|conforms_to| meta_style_guide
      modders_porting_b41_to_b42 -->|deepens| modders_foundation
      modders_porting_b41_to_b42 -->|related| modders_lua_api_surface
      modders_porting_b41_to_b42 -->|related| modders_events_callbacks
      modders_porting_b41_to_b42 -->|related| modders_modoptions_pzapi
      modders_porting_b41_to_b42 -->|related| modders_item_scripts_distributions
      modders_porting_b41_to_b42 -->|related| modders_mp_networking_porting
      modders_porting_b41_to_b42 -->|related| modders_modinfo_modid_conventions
      modders_porting_b41_to_b42 -->|related| modders_first_mod_tutorial_b42
      modders_porting_b41_to_b42 -->|conforms_to| meta_style_guide
      modders_item_scripts_distributions -->|relates_to| players_crafting_chains
      modders_porting_b41_to_b42 -->|relates_to| players_crafting_chains
      modders_porting_b41_to_b42 -->|relates_to| admins_workshop_mod_wiring
      modders_modinfo_modid_conventions -->|relates_to| admins_workshop_mod_wiring
      modders_first_mod_tutorial_b42 -->|prerequisite_for| modders_lua_api_surface
      modders_first_mod_tutorial_b42 -->|prerequisite_for| modders_events_callbacks
      modders_lua_api_surface -->|related| players_crafting_chains
      modders_lua_api_surface -->|related| admins_workshop_mod_wiring
      modders_events_callbacks -->|related| players_crafting_chains
      modders_events_callbacks -->|related| admins_workshop_mod_wiring
      modders_modoptions_pzapi -->|related| admins_workshop_mod_wiring
      modders_item_scripts_distributions -->|related| admins_workshop_mod_wiring
      modders_mp_networking_porting -->|related| players_crafting_chains
      modders_mp_networking_porting -->|related| admins_workshop_mod_wiring
      modders_modinfo_modid_conventions -->|related| players_crafting_chains
      modders_first_mod_tutorial_b42 -->|related| players_crafting_chains
      modders_first_mod_tutorial_b42 -->|related| admins_workshop_mod_wiring
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a document matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

