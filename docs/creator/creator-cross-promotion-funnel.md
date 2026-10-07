---
id: creator-cross-promotion-funnel
title: "From Video to Server to Mod: A Cross-Promotion Funnel for a Project Zomboid Creator"
version: 1.0.0
status: approved
confidence: Medium
category: Creator
topic: "Cross-promotion funnel"
build: B42
document_type: reference
created: 2026-10-07
updated: 2026-10-08
review_due: 2027-01-07
sources_verified: 2026-10-07
supersedes: null
related: [creator-foundation, creator-format-catalogue, creator-channel-competitor-map, creator-content-calendar, admins-ubuntu-runbook, admins-modded-server-runbook, admins-workshop-mod-wiring, modders-first-mod-tutorial-b42, modders-modinfo-modid-conventions, players-beginner-guide-b42, meta-style-guide]
tags: [creator, cross-promotion, funnel, youtube, twitch, discord, steam-workshop, server-listing, compliance, monetisation, terms]
game_versions_verified: ["42.21"]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | creator-cross-promotion-funnel |
| Version | 1.0.0 |
| Status | approved |
| Confidence | Medium |
| Category (track) | Creator |
| Build | B42 |
| Owner | PZ Knowledge-Base Pipeline |
| Created | 2026-10-07 |
| Updated | 2026-10-08 |
| Review due | 2027-01-07 |
| Game versions verified | 42.21 (change list re-read 2026-10-07; server-setting names are from a 42.20-era pzwiki snapshot) |

# Executive Summary

A Project Zomboid creator has three durable assets they can point viewers
toward: a community server, a Steam Workshop mod, and a Discord. This document
records what the platforms and The Indie Stone (TIS) have actually published
about each, then builds a funnel design from those facts. The parent overview
(creator-foundation) sketches the funnel in one paragraph; this document goes
deeper on the mechanics and the compliance boundary.

The compliance picture is more constrained than the "monetise your videos"
headline suggests. TIS's Terms say gameplay and "Let's Play" videos may be
monetised [1], yet the same Terms limit use of the game's art, music and video
footage as *assets* to non-commercial, promotion-related work with a required
credit line [1], allow server owners to charge for server access but not for
server-exclusive items, mods or gameplay [1], and the Modding Policy forbids
selling mod access or building donor-only mod content [2]. Those rules decide
which funnel stages may carry money.

Document confidence is **Medium**. TIS's primary pages were opened directly and
are high-quality sources, but both are dated 2022 [1][2], the TIS Terms leave
the footage-versus-asset boundary open to interpretation, and the platform help
pages change without notice. Every growth or conversion belief is quarantined;
no statistics are asserted.

# Key Takeaways

- TIS's Terms state that gameplay and "Let's Play" videos can be monetised, with
  the creator responsible for them *(cited)* *(both builds)* [1].
- Using Project Zomboid art, music, video footage or other assets creatively is
  licensed only if the result promotes the game or TIS, is non-commercial
  unless TIS agreed otherwise, and carries TIS's prescribed credit text
  *(cited)* [1].
- Server owners may charge for server access, but TIS does not encourage or
  allow charging for items, mods or gameplay made exclusively for that server
  *(cited)* [1].
- Mods cannot be sold or gated behind donations, though voluntary donations and
  commissioned (unsold) mods are permitted *(cited)* [2].
- The server browser listing, welcome message and Workshop item list are all
  `server.ini` settings, so the "joined from a video" flow is a configuration
  exercise, not a coding one *(cited)* [8].
- Discord invites default to seven days and never-expiring invites need a
  Community Server, so a link pasted in a video description can silently die
  *(cited)* [7].
- YouTube ad-revenue eligibility is a published threshold set, and
  "reused" or "inauthentic" content is a stated policy risk *(cited)* [5][6].
- Every conversion or growth number about funnels circulating in creator
  circles is unverified and quarantined *(community, unverified)*.

# Purpose

This document answers one question for a content creator: how can a video
channel, a community server and a mod be wired into one audience path without
breaking platform rules or TIS's terms? It separates what is documented from
what is designed, so the reader can see which funnel stages are constrained by
policy and which are open creative choices.

# Scope

Covered: TIS's published Terms and Modding Policy as they bear on creators;
Steam Subscriber Agreement points relevant to Workshop publishing; YouTube
Partner Program thresholds and monetisation policy summaries; Discord invite
mechanics; the `server.ini` settings that expose a server to the in-game
browser and to a Discord; the in-game Workshop uploader as documented by
pzwiki; the KB's own disclaimer obligations.

Not covered: Twitch Affiliate and Partner requirements (the Twitch help page
could not be opened for this draft, see Open Questions), tax, sponsorship
disclosure law, YouTube Shorts strategy, and server hosting or mod coding
detail (see admins-modded-server-runbook, admins-ubuntu-runbook,
admins-workshop-mod-wiring and modders-first-mod-tutorial-b42). Audience-size
data lives in creator-foundation and creator-channel-competitor-map. This is
not legal advice.

# Definitions

- **Funnel stage** — one step on the path from a stranger watching a video to a
  returning community member: discovery (video), capture (Discord), play
  (server), and retention (mod or Workshop collection).
- **Asset use** — in TIS's Terms, creative use of art, music, video footage or
  other game assets [1]; treated here as distinct from the gameplay-video
  allowance in the same document [1].
- **Server listing** — the combination of `Public`, `PublicName` and
  `PublicDescription` settings that decide whether and how a server appears in
  the in-game browser [8].
- **Workshop ID** — the numeric identifier the in-game uploader assigns to a
  Workshop item [9]; also the value a server lists in `WorkshopItems` [8].

# Build Applicability

| Build | Applies | Verified against | Notes |
|-------|---------|------------------|-------|
| B41 (legacy41) | Context only | — | Policy and platform facts are not build-scoped [1][2]; server setting names were not checked against 41.78 |
| B42 (stable) | Yes | 42.21 (change list); server-setting names from a 42.20-era snapshot | Server-setting facts come from the pzwiki Server settings snapshot rev 1443167 [8], taken in the 42.20 era; the TIS site header showed stable build 42.21 on 2026-10-07 [1] |

B42 stable is now **42.21**, as shown in the header of TIS's own pages on the
access date [1]. This revision re-read the TIS forum 42.21 patch notes [10]
(abridged) for changes touching the cited server settings and Discord hooks.
It lists a fix for an infinite connection loop when the Discord API is
unavailable, a fix for connection failures when the `UsernameDisguises` option
is enabled, and a server-browser change showing the last wipe rather than the
last restart [10]. It does not list a change to `Public`, `PublicName`,
`PublicDescription`, `ServerWelcomeMessage`, `WorkshopItems` or the Discord
setting names, but the list is abridged, so that absence is not proof of no
change [10]. The setting names themselves were not checked against an
installed 42.21 file. Platform facts (YouTube, Discord, Steam,
TIS terms) are not tied to a game build; they are tied to their access date,
2026-10-07.

# Reference

## TIS terms that bear on creators

The TIS Terms page carries a last-updated date of 6 October 2022 and applies to
the game, the TIS forums and websites, including pzwiki.net [1]. Its stated
golden rule is that people may do what they want with the Services provided it
promotes Project Zomboid or TIS, is not for commercial purposes (meaning the
user's own profit unless TIS approved in advance), and is not malicious or
illegal [1]. The Terms invite anyone in doubt to ask TIS before acting [1].

| Topic | What the Terms say | Section |
|-------|--------------------|---------|
| Game assets | Art, music, video footage or other assets may be used creatively if the result relates to promoting the game or TIS, is non-commercial unless TIS agreed otherwise, and shows a prescribed credit line stating it is an unofficial fan production made under the TIS Terms | 2.2 [1] |
| Third-party content | A creator combining other IP, software or tools with the game must hold the licences and permissions needed | 2.3 [1] |
| Gameplay videos | Gameplay footage or "Let's Play" videos on YouTube or other platforms may be made and monetised, and the creator is responsible for them | 2.5 [1] |
| Mods | Mods are permitted if they comply with the Modding Policy | 2.6 [1] |
| Distribution | Creators may not distribute the game or host its download, and TIS recommends only established portals such as Steam or GOG | 3.2 [1] |
| Cheats and piracy sites | Creating, distributing or directing users to hacks or cheats (outside what the Modding Policy allows) or to unauthorised pirated-game sites is prohibited | 3.3 [1] |
| Attacks | Maliciously targeting other users, for example a DDoS against another player's server, is prohibited | 3.4 [1] |
| Charging for servers | Charging players for access to a server is allowed, and servers may run any mods that fit the Modding Policy | 4.1 [1] |
| Server-exclusive paid items | TIS does not encourage or allow server owners to charge for specific items, mods or gameplay made and distributed exclusively for their server, and says it does not approve of monetising any aspect of the game beyond server access | 4.2 [1] |

The credit line that section 2.2 requires is supplied verbatim in the Terms
page itself [1]; this KB does not reproduce it, and a creator who needs it
should copy it from the source.

## The TIS Modding Policy

The Modding Policy page is dated 4 October 2022 and says it should be read
together with the Terms, Valve's Mod Content Usage Policy and the Steam
Subscriber Agreement [2]. Its relevant provisions are:

- Modders are solely responsible for their mod, including compliance with
  hosting platforms such as the Steam Workshop, and for obtaining consents for
  third-party materials, including assets taken from another mod [2].
- A mod may not be presented as "Official" [2].
- Voluntary monetary or gift donations are allowed, but mods made exclusively
  for donors, or separate in-mod content and bonuses for donors, are not [2].
- Unless TIS has agreed otherwise, creators cannot sell access to a mod or its
  content, though commissioned mods are allowed if they are not sold [2].
- Hidden or unexpected content added in mod updates and not flagged in the
  Workshop description or evident in the mod must have visible attribution of
  where and from whom it came [2].
- Mod authors own their mods and grant TIS a broad licence to use them in
  connection with the game [2].
- Submitting work that is not your own without the owner's permission is not
  allowed, and credit for third-party material should appear in the Workshop
  description [2].
- Modpacks come in three kinds. Public packs need permission from every
  included mod's author and must list all included mods; the policy suggests a
  Workshop Collection as an alternative. Semi-private packs, posted as Unlisted
  on the Workshop, still need permission. Private packs need none provided they
  are not publicly downloadable [2].

## Steam Workshop publishing facts

The Steam Subscriber Agreement states that Workshop contributions are in
principle made available to subscribers free of charge, that Valve is not
obliged to keep distributing any contribution and may remove contributions for
any reason, and that the contributor warrants the contribution was originally
created by them or that they hold the co-creators' rights [3]. Steamworks
documentation describes ready-to-use Workshops as ones where anyone can upload
and authors can update their items at any time, and notes that users holding
only temporary licences, such as Family Sharing or free weekend access, cannot
upload [4].

For Project Zomboid specifically, the in-game uploader is reached from the main
menu Workshop entry, offers fields for title, description, tags and
visibility, assigns or reuses a Workshop ID, and lets the author write a patch
note that is uploaded with the item [9].

## Server listing and Discord hooks in `server.ini`

The following settings are documented in the pzwiki Server settings snapshot
(facts only) [8]:

| Setting | Documented effect | Source |
|---------|-------------------|--------|
| `Public` | Controls whether the in-game browser lists the server; a server running with Steam networking turned on appears in Steam's own server list regardless of this switch | [8] |
| `PublicName` | The name shown in the in-game browser and, where applicable, the Steam browser | [8] |
| `PublicDescription` | The description shown in the in-game public browser | [8] |
| `ServerWelcomeMessage` | The message players see on joining | [8] |
| `Password` | Clients must know it to join | [8] |
| `Open` | When true, clients may join without already being whitelisted | [8] |
| `WorkshopItems` | Workshop IDs the server downloads, separated by semicolons | [8] |
| `DiscordEnable` and related Discord keys | Bridge the in-game global chat to a Discord channel, authenticated with a bot token | [8] |

## Discord invite mechanics

A Discord instant invite shows a seven-day link by default unless the channel's
earlier invite settings were changed [7]. The creator can edit the duration and
the maximum number of uses, and temporary links can last as short as thirty
minutes, while an invite that does not expire is available in a Community
Server [7]. Once an invite is deleted, its code cannot be recreated, even by
Discord support [7]. Server admins can pause invites or remove individual ones
under Server Settings [7].

## YouTube monetisation facts

YouTube's Partner Program overview lists separate thresholds per feature. For
ad revenue: 1,000 subscribers and either 4,000 public long-form watch hours in
the last 365 days or 10 million public Shorts views in the last 90 days, plus
age and contract requirements [5]. For channel memberships: 500 subscribers
with either 3,000 watch hours or 3 million Shorts views, plus three public
uploads in the last 90 days [5]. The page also says features may be unavailable
in some countries and that a reviewer can find a channel ineligible even where
the numbers are met [5].

YouTube's channel monetisation policies require channels to follow the
Community Guidelines, Terms of Service and copyright rules, and describe
reviewers assessing the channel's theme, most-viewed and newest videos, titles,
thumbnails and description [6]. The page names generic or repetitive content
and reused content without significant original commentary or changes as
ineligible, and records that "repetitious content" was renamed "inauthentic
content" on 15 July 2025 [6]. It also prohibits artificially inflating
engagement and using other channels to evade demonetisation [6].

# B41 vs B42 Delta

Not applicable — single-build document. The cited TIS pages and platform
policies are not versioned per game build [1][2][5][7]; the only build-scoped
material is the server-setting names, taken from a snapshot of the 42.20 era
[8].

# Practical Guidance

Judgements built on the cited facts above; no new factual claims.

## Design the funnel around the money rules

1. **Decide which stage may earn.** YouTube ad revenue on gameplay videos is
   explicitly addressed by the Terms [1][5]. Server access fees are explicitly
   allowed [1]. Selling mods, donor-only mods, or server-exclusive paid items
   are not [1][2]. Keep revenue at the video and server-access stages, and keep
   the mod stage free.
2. **Treat donations as thank-yous.** Voluntary donations are allowed, but
   anything that gates content behind them is not [2]. A donation link on a mod
   page that unlocks nothing stays inside the policy [2].
3. **Treat non-gameplay productions carefully.** The Terms allow monetised
   gameplay and "Let's Play" videos [1], but creative use of art, music or
   footage as assets is non-commercial and needs the credit line [1]. A
   trailer, motion graphic or mod-promo reel that reuses game art sits closer
   to the second rule; if the line matters to your plan, ask TIS first as the
   Terms invite [1].

## Stage-by-stage hooks

- **Video to Discord.** Put a Discord invite in the pinned comment and
  description, created with no expiry if your Discord is a Community Server, or
  recreated on a schedule if not [7]. Keep a record of which invite code sits
  in which video, because a deleted code cannot be restored [7].
- **Discord to server.** Publish the server's name, connection route and
  password policy in a Discord channel. Decide deliberately between a public
  listing (`Public`, `PublicName`, `PublicDescription`) and a Discord-gated
  one (`Password`, whitelist via `Open` set to false) [8]. The welcome message
  can repeat the Discord link and the video that brought viewers in [8].
- **Server to mod.** A server's `WorkshopItems` list is how a creator's own mod
  reaches every player automatically [8]. Publishing the mod with the in-game
  uploader gives it a Workshop ID and a patch-note field that works as a
  changelog [9]. A Workshop Collection of the server's mod set doubles as a
  public, permission-friendly alternative to a modpack [2].
- **Mod to video.** A mod update that comes with a patch note [9] is a natural
  video hook, and the Modding Policy's attribution rule for hidden or
  unexpected content [2] means any surprise feature should be flagged in the
  description anyway.

## Compliance checklist for a funnel page or video

- State on the channel and any KB-derived page that the work is an unofficial
  fan production not affiliated with TIS, and use the credit text from the
  Terms where asset use applies [1].
- Do not host or link to game downloads outside established portals, and never
  direct viewers to cheats or pirated copies [1].
- Give written credit in the Workshop description for any third-party asset in
  your mod, and get permission before using another mod's content [2].
- Keep videos substantively original so they do not read as templated or
  reused content under YouTube's policy [6].
- Keep Discord bot tokens and RCON passwords out of screenshots; both live in
  the same settings area as the public listing keys [8].

# Common Pitfalls & Troubleshooting

- **Expiring invite in an evergreen video.** The seven-day default means a
  link created casually and pasted into a video description can die while the
  video keeps getting views [7].
- **Paid perks that create a grey area.** A paid tier offering a server-only
  item or mod collides with TIS's stated position on server-exclusive paid
  content [1] and the Modding Policy's bar on donor-only mod content [2].
- **Footage versus assets confusion.** The Terms permit monetised gameplay
  videos [1] but restrict commercial asset use [1]; treating the two as one
  rule leads to either needless caution or an unnoticed breach.
- **Unlisted modpack shortcuts.** An unlisted Workshop modpack for a "private"
  server still needs the included authors' permission [2]; a Collection avoids
  re-uploading others' work [2].
- **Assuming Workshop permanence.** Valve may remove contributions at will [3],
  so a funnel whose retention stage is one Workshop page needs a fallback.
- **Reused-content flags.** Reaction, compilation or recycled footage with
  little new commentary is called out as ineligible in YouTube's policy [6].
- **Leaking server secrets while demonstrating setup.** The Discord token,
  RCON password and server password are all plain `server.ini` values [8].

# Community Notes & Unverified Claims

## Claim 1 — Funnel conversion rates from video to Discord to server are predictable

- **Claim:** Creator forums and strategy videos quote rules of thumb for what
  share of viewers click through to a Discord and then join a server.
- **Why unverified:** No primary source or first-party analytics were found;
  no figure is asserted in this KB.
- **Confidence:** Low. Such figures depend on the channel, audience and call to
  action, and none could be traced to a measurable source.

## Claim 2 — Perks such as priority queue slots are tolerated by TIS when attached to a donation

- **Claim:** Server owners in community discussion say that donor perks which are not "pay to win" are accepted in practice.
- **Why unverified:** The Terms say TIS does not approve of monetising any aspect beyond server access [1], and no TIS statement endorsing donor perks was found.
- **Confidence:** Low. It conflicts with the plain reading of [1] and is circumstantial at best.

## Claim 3 — Placing a Discord link in the video description suppresses recommendation reach

- **Claim:** Creators repeat that outbound links in descriptions or pinned comments reduce a video's distribution.
- **Why unverified:** The YouTube policy pages opened [5][6] make no such statement and no controlled test exists.
- **Confidence:** Low. It is folk belief; the opened policies neither confirm nor deny it.

# Risks & Caveats

- **Old policy dates.** Both TIS pages carry 2022 dates [1][2]. TIS may have
  updated its position on creators and monetisation since; a human should
  re-read both pages at review time.
- **Interpretive gap.** The Terms address monetised gameplay footage in one
  clause [1] and non-commercial asset use in another [1]; the KB does not
  resolve the overlap, and this document is not legal advice.
- **Platform drift.** The YouTube thresholds and policy wording changed during
  2025 [6] and can change again; the Discord article was marked as updated two
  years before access [7].
- **Server settings from a snapshot.** The `server.ini` facts come from a
  community wiki snapshot, a fact-only source [8], not from an installed 42.21
  copy of the file; the 42.21 forum list was read in abridged form [10]. Corroborate against the game's own file before publishing
  setup instructions.
- **Steam agreement scope.** Only the Workshop-related sections of the Steam
  Subscriber Agreement were read for this draft [3].

# Verification Steps

1. Open the TIS Terms [1] and Modding Policy [2] and re-read sections 2.2, 2.5,
   4.1 and 4.2 of the Terms and sections 2.3, 2.4 and 7 of the Modding Policy.
2. Open YouTube's Partner Program overview [5] and confirm the thresholds
   quoted are current in your country.
3. In Discord, open the invite panel on a test channel and confirm the default
   duration and whether the no-expiry option appears for your server type [7].
4. On a test server, edit `Public`, `PublicName` and `PublicDescription` in
   the server's `.ini` file and confirm the listing in the in-game browser [8].
5. Use the in-game Workshop uploader on a throwaway mod and confirm the
   fields and Workshop ID behaviour described in [9].
6. Email TIS before launching any paid element of the funnel, as the Terms
   advise [1].

# Open Questions

- Does TIS publish a creator or press page beyond the Terms and Modding
  Policy that covers sponsorships, paid mod showcases or merchandise? None was
  found for this draft.
- What are Twitch's current Affiliate and Partner requirements? The Twitch help
  page could not be opened during this draft, so the Twitch stage is covered
  only structurally.
- How does TIS read the overlap between clause 2.2 and clause 2.5 of its Terms
  for trailers and promotional reels? A direct answer would settle a common
  creator question.
- Have the `Public` and Discord settings changed in 42.21? The abridged forum
  list shows a Discord-integration fix but no setting change [10]; a first-hand
  check against an installed 42.21 server file would resolve it.
- Valve's Mod Content Usage Policy, referenced by the Modding Policy [2], was
  not opened and should be read before publishing any guidance on Workshop
  monetisation.

# References

**Primary Sources**

- [1] **The Indie Stone** — *Terms! Conditions!* (last updated 6 October 2022; page header showed stable build 42.21). https://projectzomboid.com/blog/support/terms-conditions/ Accessed 2026-10-07. Bot-block allowlisted host; opened in a browser.
- [2] **The Indie Stone** — *Modding Policy* (last updated 4 October 2022). https://projectzomboid.com/blog/modding-policy/ Accessed 2026-10-07. Bot-block allowlisted host; opened in a browser.
- [3] **Valve** — *Steam Subscriber Agreement* (Workshop contribution sections). https://store.steampowered.com/subscriber_agreement/ Accessed 2026-10-07. Bot-block allowlisted host.
- [4] **Valve** — *Steamworks Documentation: Steam Workshop*. https://partner.steamgames.com/doc/features/workshop Accessed 2026-10-07.
- [5] **Google** — *YouTube Partner Program overview and eligibility* (YouTube Help). https://support.google.com/youtube/answer/72857 Accessed 2026-10-07.
- [6] **Google** — *YouTube channel monetization policies* (YouTube Help). https://support.google.com/youtube/answer/1311392 Accessed 2026-10-07.
- [7] **Discord** — *Invites 101* (Discord Support). https://support.discord.com/hc/en-us/articles/208866998-Invites-101 Accessed 2026-10-07.

- [10] **The Indie Stone** — *42.21 Patch Notes* (TIS forum topic 101693, first post 2026-09-23; abridged change list). https://theindiestone.com/forums/topic/101693-4221-patch-notes/ Accessed 2026-10-07.

**Fact-Only Sources (no prose reuse)**

- [8] **PZwiki** — *Server settings* (revision 1443167). https://pzwiki.net/wiki/Server_settings Accessed 2026-10-07 via the local ingested snapshot dated 2026-07-30. Fact-only source.
- [9] **PZwiki** — *Uploading mods* (revision 1442321). https://pzwiki.net/wiki/Uploading_mods Accessed 2026-10-07 via the local ingested snapshot dated 2026-07-30. Fact-only source.

**Secondary & Corroborating**

- None used in this document.

**Community & Creator**

- None used in this document.

**Further Reading**

- See the Further Reading section below.

# Further Reading

- creator-foundation, for the channel landscape and the one-paragraph funnel
  sketch this document expands.
- The TIS IP Rights Policy and Privacy Policy, linked from the footer of the
  TIS site; not opened for this draft.
- Valve's Mod Content Usage Policy, referenced by the TIS Modding Policy; not
  opened for this draft.

# Related Documents

- creator-foundation — the parent overview and channel landscape.
- creator-format-catalogue — video formats that feed the top of the funnel.
- creator-channel-competitor-map — who else occupies each funnel stage.
- creator-content-calendar — scheduling content around mod and server events.
- admins-modded-server-runbook — running the community server.
- admins-ubuntu-runbook — Linux hosting for that server.
- admins-workshop-mod-wiring — wiring Workshop mods into a server.
- modders-first-mod-tutorial-b42 — building the mod that closes the loop.
- modders-modinfo-modid-conventions — naming conventions for the mod.
- players-beginner-guide-b42 — the guide a new viewer lands on.
- meta-style-guide — the editorial and license rules, including disclaimers.

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-07 | KB Pipeline (virtual agent) | Initial draft. | — |
| 0.2.0 | 2026-10-07 | KB Pipeline (revision worker) | Re-baselined to 42.21: checked the TIS forum 42.21 patch notes [10] for changes touching server listing and Discord hooks; TIS Terms and Modding Policy statements unchanged (those pages were not re-fetched in this revision; the 2026-10-07 read showed 2022 update dates [1][2]). | — |
| 1.0.0 | 2026-10-08 | Orchestrator (KB Pipeline) | Approved and frozen — release kb-release-2026.10.08 (42.21 re-baseline; validated against 42.21 and 41.78.21, Umbrella 42.21.0 @ 13d01f9). Content is the reviewed 0.2.0 text. | Project owner (user instruction 2026-10-08) |
