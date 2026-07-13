# Agent-Governance Interoperability Profile

Status: candidate research and implementation profile. Decapod is not currently an adopted Internet standard, native MCP server, A2A implementation, HTTP governance service, or vendor-pre-bundled coding-agent component.

## Goal

Decapod is offered as a standard agent-callable governance component: a narrow, versioned contract that coding-agent harnesses can bundle or discover so agents can resolve project authority, claim work, enter bounded workspaces, preserve selected trajectory, and produce shared evidence. The human should continue speaking naturally to the available agent; the agent should handle the governance protocol.

The portability goal is not a Decapod-specific command dialect for people. It is a workbench-independent machine contract that lets a person and project move among Claude, Codex, Antigravity, Grok, and other conforming harnesses without making one vendor conversation the durable project state.

This document uses HTTP and IPv4 only as architectural analogies: a narrow interface can permit independently evolving implementations and layers. It uses MCP and A2A as concrete adjacent protocols. The analogy does not imply equivalent maturity, governance, adoption, wire compatibility, or standards status.

## Implemented base at the inspected revision

The implementation audit is pinned to Decapod commit [`207e9a37e57ee970e881942de2994abea2cd737c`](https://github.com/DecapodLabs/decapod/commit/207e9a37e57ee970e881942de2994abea2cd737c), tag `v0.66.3`. The intervening commits from the prior `v0.66.1` audit change release metadata, CI, and research links rather than the mapped implementation paths.

| Surface | Implemented status | Boundary |
| --- | --- | --- |
| CLI and structured RPC | Daemonless local CLI plus a Decapod-specific request/response document over process stdin/stdout | The envelope is not JSON-RPC 2.0 and is not MCP |
| Capability discovery | `decapod capabilities` and deterministic schemas | No negotiation lifecycle or external conformance certification |
| Universal agent contract | Generated workbench entrypoint shims delegate to a common repository contract | A shim does not prove that a host follows the contract |
| Portable context | Scoped capsules and context-bundle export/import | Selection can still be irrelevant, stale, contradictory, or harmful |
| Fleet state | Todos, claims, dependencies, handoff, workspaces, events, proof, and publication gates | Local-first; no global consensus or conflict-free integration guarantee |
| Identity | Local actor/session declarations and document hashes | A claimed actor is not authenticated provider, organization, or human identity |
| Cloud | Experimental metadata and unavailable public backend | No production remote leases, synchronization, or cloud handoff |

## Candidate thin-waist contract

A conforming component should expose versioned semantics rather than require another implementation to copy Rust internals or human-facing CLI syntax:

1. capability and schema discovery;
2. project-authority and constitution resolution with source provenance;
3. task discovery, exclusive/shared custody policy, dependencies, and handoff;
4. workspace acquisition and custody status;
5. selected trajectory and project-memory queries;
6. validation, proof, workunit, provenance, and publication status;
7. deterministic error, idempotency, version-skew, and degraded-operation behavior;
8. conformance vectors proving both positive and fail-closed behavior.

Protocol adapters should layer over those semantics:

- **MCP** can let a host discover and invoke governance tools/resources through MCP's JSON-RPC lifecycle and stdio or Streamable HTTP transports.
- **A2A** can carry governed task, handoff, status, and artifact references between independent agents while leaving each agent's internal reasoning opaque.
- **HTTP** can provide an optional remote transport only after identity, authorization, repository authority, idempotency, and local-first failure behavior are defined.

Pre-bundling means a harness vendor ships or discovers a compatible local component and pins a supported profile version. It must not mean silent approval, hidden privilege escalation, or a claim that integrations exist before they ship.

## Constitutional authority chain

The constitution is central to the proposed interoperability contract. The current binary embeds a baseline constitution from `assets/constitution.json`; `decapod constitution get/search` retrieves its structured nodes. A repository can add a binding project-local `.decapod/OVERRIDE.md`, and current tests establish that two-level merge and project precedence. Task-specific context resolution is a provenance-bearing projection of that authority, not a replacement for it.

An organization-level overlay is not implemented at the inspected revision. The proposed three-level chain is:

1. embedded baseline authority;
2. organization policy overlay;
3. project-local binding override;
4. task-scoped, relevance-audited projection supplied to the agent.

Its design must define precedence, conflicts, provenance, revocation, versioning, and minimum non-overridable safety rules before the paper can claim organization-level operation.

The author coined **Intent-Driven Design** as the name of Decapod's software-engineering approach in public LinkedIn posts beginning in August 2025. By September 2025, the core approach used a project constitution to scaffold boilerplate and derived agent guidance before implementation. This design lineage predates and arose independently of the February 2026 ETH Zurich preprint on repository context files. The chronology establishes provenance of the Decapod-specific method, not empirical efficacy.

## Central fleet-coherence question

> Can multiple independently launched agents concurrently solve similar but distinct problems in the same codebase while preserving shared authority, distinct task custody, isolated mutation, dependency awareness, and integrated proof?

This is stricter than asking whether worktrees avoid direct file trampling. Similar-but-distinct tasks may share architecture, tests, modules, or publication boundaries. A credible experiment must measure duplicate starts and discovery, semantic overlap, dependency-order failures, textual and semantic merge conflicts, integration repair, proof-local versus integrated success, and total coordination overhead.

## Adoption snapshot and evidence boundary

As queried on July 13, 2026, the official GitHub API reported 222 stars and 21 forks, while the crates.io API reported 6,983 cumulative downloads for `decapod`—approximately 7,000, but not yet more than 7,000 in that query. These counts show public interest and distribution only. They do not establish correct use, fleet interoperability, research validity, or a treatment effect.

Decapod is used across 18 repositories in the `alexhraber`, `worldofgeese`, and `DecapodLabs` namespaces (15 public and three private). The `worldofgeese` maintainer discovered and adopted Decapod independently; the other namespaces are author- or organization-affiliated. The [repository-use inventory](adoption-inventory.md) records the linked repositories and methodological boundary. Because repositories within each namespace share maintainers, the footprint is not evidence of 18 independent adoptions or of improved outcomes.

## Implementation roadmap

- [#869](https://github.com/DecapodLabs/decapod/issues/869): narrow MCP/RPC/handshake documentation to implemented boundaries.
- [#870](https://github.com/DecapodLabs/decapod/issues/870): specify the versioned interoperability profile.
- [#871](https://github.com/DecapodLabs/decapod/issues/871): add conformance vectors and negotiation.
- [#872](https://github.com/DecapodLabs/decapod/issues/872): implement a native MCP adapter.
- [#873](https://github.com/DecapodLabs/decapod/issues/873): implement an A2A adapter.
- [#874](https://github.com/DecapodLabs/decapod/issues/874): add an optional authenticated HTTP transport.
- [#875](https://github.com/DecapodLabs/decapod/issues/875): package harness-native discovery and pre-bundling.
- [#876](https://github.com/DecapodLabs/decapod/issues/876): distinguish claimed actors from verified identity.
- [#877](https://github.com/DecapodLabs/decapod/issues/877): add organization-level constitution overlays.
- [#878](https://github.com/DecapodLabs/decapod/issues/878): coordinate similar-but-distinct concurrent tasks.
- [#879](https://github.com/DecapodLabs/decapod/issues/879): document constitution-design chronology and evidence.
- [#880](https://github.com/DecapodLabs/decapod/issues/880): prove that fresh agents activate governed context across representative hosts without manual human protocol commands.
- Existing [#852](https://github.com/DecapodLabs/decapod/issues/852), [#860](https://github.com/DecapodLabs/decapod/issues/860), and [#861](https://github.com/DecapodLabs/decapod/issues/861) remain the parent work for leases, fleet projections, and portable trust/provenance.
- Existing [#868](https://github.com/DecapodLabs/decapod/issues/868) tracks the observed mandatory-orientation bootstrap failure; [#715](https://github.com/DecapodLabs/decapod/issues/715) is the earlier closed materialization issue.

## Primary sources for protocol comparisons

- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) and [server specification](https://modelcontextprotocol.io/specification/2025-06-18/server/index)
- [A2A specification](https://a2a-protocol.org/dev/specification/) and [Agent Card discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)
- [HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
- [Internet Protocol, RFC 791](https://www.rfc-editor.org/rfc/rfc791.html)
