# Decapod Repository-Use Inventory

Snapshot date: July 13, 2026.

This inventory records repositories identified by their maintainers as using Decapod and checked through the authenticated GitHub API. Fifteen expose `.decapod/config.toml` on the default branch; the public profile repository exposes a generated Decapod `AGENTS.md`. It is ecological deployment evidence only. Presence of a governance marker does not establish active use, correct use, version compatibility, agent-host activation, outcome improvement, fleet coherence, or adoption by an independent organization.

The snapshot contains 16 repositories across three owner namespaces: 13 public and 3 private. The private repository names are included at the owner's direction; their contents are not part of this research artifact.

The author reports running `decapod init` once when establishing each repository, before the first agent interaction or other engineering operation. Thereafter the human interacts naturally with agents, and the generated `AGENTS.md` contract requires the agents to continue using Decapod at governance boundaries. Marker presence is consistent with that operating practice but cannot independently establish initialization order, agent compliance, or outcome effects.

## `alexhraber` — nine repositories

- [`alexhraber/alexhraber`](https://github.com/alexhraber/alexhraber) — public; generated Decapod `AGENTS.md`; public researcher/engineer profile and professional credential surface, not cryptographic identity authentication
- [`alexhraber/pi-cluster`](https://github.com/alexhraber/pi-cluster) — public
- [`alexhraber/builddeck`](https://github.com/alexhraber/builddeck) — public
- [`alexhraber/agentic-sdlc-intake-attack`](https://github.com/alexhraber/agentic-sdlc-intake-attack) — public
- [`alexhraber/metaplay-fake-interview-supply-chain-incident`](https://github.com/alexhraber/metaplay-fake-interview-supply-chain-incident) — public
- [`alexhraber/go-scaling`](https://github.com/alexhraber/go-scaling) — public
- [`alexhraber/nixos`](https://github.com/alexhraber/nixos) — public
- [`alexhraber/cycle`](https://github.com/alexhraber/cycle) — private
- [`alexhraber/mentora-automa`](https://github.com/alexhraber/mentora-automa) — private

## `worldofgeese` — three repositories

- [`worldofgeese/den`](https://github.com/worldofgeese/den) — public
- [`worldofgeese/tarot-api`](https://github.com/worldofgeese/tarot-api) — public
- [`worldofgeese/mythras-chargen`](https://github.com/worldofgeese/mythras-chargen) — public

## `DecapodLabs` — four repositories

- [`DecapodLabs/decapod`](https://github.com/DecapodLabs/decapod) — public
- [`DecapodLabs/gensor`](https://github.com/DecapodLabs/gensor) — private
- [`DecapodLabs/accountable-agentic-execution`](https://github.com/DecapodLabs/accountable-agentic-execution) — public
- [`DecapodLabs/pincher`](https://github.com/DecapodLabs/pincher) — public

## Verification boundary

- Repository existence, visibility, and marker presence were queried through GitHub's repository and contents APIs.
- The snapshot does not inspect private source or expose private configuration contents.
- Maintainer ownership creates correlated adoption; this is not evidence of 16 independent adopters.
- A future reproducible public inventory should record default-branch commit, Decapod version, first/last observed marker, and an explicit maintainer attestation without collecting repository secrets.
