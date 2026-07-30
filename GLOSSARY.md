# Glossary — Project Zomboid Knowledge Base

Shared terms. Orchestrator-owned; workers propose entries via their return
JSON, never edit this file. `source_key` points at `SOURCE_REGISTRY.md` tiers.

| Term | Definition | Source |
|------|------------|--------|
| B41 / legacy41 | Build 41 (final: 41.78.16), kept available as the `legacy41` Steam beta branch after B42 went stable. B41 saves and mods are not compatible with B42. | Tier 1 |
| B42 | Build 42, first on the unstable branch 2024-12-17 (single-player), multiplayer from unstable 42.13 (2025-12-11), stable as 42.20 on 2026-07-29. | Tier 1 |
| Thursdoid | The Indie Stone's dev-blog post series; cadence is irregular (roughly monthly, event-driven), not weekly. | Tier 1 |
| IWBUMS / unstable | The opt-in Steam beta branch where builds are tested before stable. | Tier 1 |
| Umbrella | asledgehammer's EmmyLua/LuaCATS type-stub repo for the PZ Lua API; this KB's machine-checkable API ground truth. | Tier 2 |
| ZomboidDoc / pz-zdoc | Tool that compiles an annotated Lua library from an installed game's exposed classes; used to generate per-build API indices. | Tier 2 |
| Kahlua | The Java implementation of (modified) Lua 5.1 that Project Zomboid runs mods on. | Tier 2 |
| Mod ID / Workshop ID | A mod's internal identifier (mod.info) vs its Steam Workshop item number; servers need both wired (`Mods=` / `WorkshopItems=`). | Tier 2 |
| SandboxVars | The per-save/server gameplay-settings Lua file; edited only while the server is stopped. | Tier 4 |
| RCON | Remote console protocol used to administer a dedicated server. | Tier 4 |
| Moodle | Project Zomboid's on-screen status icons for character states (hunger, panic, etc.). | Tier 3 |
| Knox Event | The in-game outbreak; lore is The Indie Stone's copyrighted fiction — document, don't republish. | Tier 1 |
