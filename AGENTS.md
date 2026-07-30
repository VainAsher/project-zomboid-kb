# AGENTS

Instructions for any coding/writing agent operating in this repository.

- **Orchestrator role:** follow `PROJECT_HANDOVER.md` and `CLAUDE.md`. You own
  shared files, git, releases, the human gate, and independent link
  re-verification.
- **Worker role:** you receive `prompts/worker_contract.md` verbatim plus one
  document scope. Write exactly one file, pass the five self-check gates,
  return the contract's JSON, and stop. Never edit shared files or run git.
- **Genre:** reference. Evidence cited to primaries; community hearsay
  quarantined and labelled. Build tags (B41/B42/both/historic) are mandatory.
- **License:** pzwiki.net is CC BY-NC-SA 3.0 — fact source only, never prose.
  This is enforced mechanically by `scripts/check_license_hygiene.py`.
- **Gates:** see `CLAUDE.md`; all must be green before a cluster freezes.
