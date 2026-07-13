# Decapod Repository-Use Inventory

Snapshot date: July 13, 2026.

This inventory records repositories identified by their maintainers as using Decapod and verified, through an authenticated GitHub API query, to contain `.decapod/config.toml` on the default branch. It is ecological deployment evidence only. Presence of a configuration marker does not establish active use, correct use, version compatibility, agent-host activation, outcome improvement, fleet coherence, or adoption by an independent organization.

The snapshot contains 13 repositories across three owner namespaces: 11 public and 2 private. The private repository names are included at the owner's direction; their contents are not part of this research artifact.

The author reports running `decapod init` once when establishing each repository, before the first agent interaction or other engineering operation. Thereafter the human interacts naturally with agents, and the generated `AGENTS.md` contract requires the agents to continue using Decapod at governance boundaries. Marker presence is consistent with that operating practice but cannot independently establish initialization order, agent compliance, or outcome effects.

## `alexhraber` — six repositories

- [`alexhraber/pi-cluster`](https://github.com/alexhraber/pi-cluster) — public
- [`alexhraber/builddeck`](https://github.com/alexhraber/builddeck) — public
- [`alexhraber/agentic-sdlc-intake-attack`](https://github.com/alexhraber/agentic-sdlc-intake-attack) — public
- [`alexhraber/go-scaling`](https://github.com/alexhraber/go-scaling) — public
- [`alexhraber/nixos`](https://github.com/alexhraber/nixos) — public
- [`alexhraber/cycle`](https://github.com/alexhraber/cycle) — private

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
- Maintainer ownership creates correlated adoption; this is not evidence of 13 independent adopters.
- A future reproducible public inventory should record default-branch commit, Decapod version, first/last observed marker, and an explicit maintainer attestation without collecting repository secrets.
