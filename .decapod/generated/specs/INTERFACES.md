# Interfaces


<!-- decapod:capability-overlay:public-api:start -->


## Public API Capability Overlay

### API Contract Requirements
- All public endpoints MUST define explicit request/response schemas
- Versioning strategy MUST be documented (URL path or header-based)
- All public endpoints MUST implement idempotency for mutating operations
- Rate limiting and pagination MUST be implemented for list endpoints

### Compatibility Guarantees
- Backward-compatible changes ONLY within a version
- Breaking changes require new version (v1, v2, etc.)
- Deprecation and removal policy MUST be selected for this project and proven against its consumers

### Security Requirements
- All public endpoints MUST implement authentication
- Abuse-control enforcement point MUST be a documented project decision
- Input validation MUST reject malformed requests with typed errors
<!-- decapod:capability-overlay:public-api:end -->
## Contract Principles
- Prefer explicit schemas over implicit behavior.
- Every mutating interface defines idempotency semantics.
- Every failure path maps to a typed, documented error code.

## CLI Layer
Defines command-line interface and argument parsing for all Decapod commands. CLI contracts should describe command purpose, preconditions, expected side effects, output shape, recovery path, and whether the command may mutate `.decapod/` state.

## Agent Interface
Agent-facing documentation (AGENTS.md, CLAUDE.md, etc.) and the Universal Agent Contract mandate Decapod usage patterns. Product docs under `docs/agent` and `docs/book` teach Decapod itself; generated specs under `.decapod/generated/specs/` teach the current repository to active agents.

## Generated Contract Depth
Generated interface specs should include more than endpoint names:
- Command/RPC trigger conditions and required prior Decapod calls.
- Read/write ownership for each store and generated artifact path.
- Idempotency and retry behavior for mutations.
- Typed failure classes and concrete recovery instructions.
- Compatibility expectations for existing agent workflows.
- Evidence an agent must attach before claiming an interface change complete.

## API / RPC Contracts
| Interface | Method | Request Schema | Response Schema | Errors | Idempotency |
|---|---|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## Event Consumers
| Consumer | Event | Ordering Requirement | Retry Policy | DLQ Policy |
|---|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## Outbound Dependencies
| Dependency | Purpose | SLA | Timeout | Circuit-Breaker |
|---|---|---|---|---|
| `TODO` | `TODO` | `TODO` | `TODO` | `TODO` |

## Inbound Contracts
- API / RPC entrypoints:
- CLI surfaces:
- Event/webhook consumers:
- Repository-detected surfaces: not detected yet

## Data Ownership
- Source-of-truth tables/collections:
- Cross-boundary read models:
- Consistency expectations:

## Error Taxonomy Example (not classified yet)
```ts
export enum ApiErrorCode {
  Validation = "validation_failed",
  UpstreamTimeout = "upstream_timeout",
  Conflict = "conflict"
}
```

## Failure Semantics
| Failure Class | Retry/Backoff | Client Contract | Observability |
|---|---|---|---|
| Validation | No retry | 4xx typed error | warn log + metric |
| Dependency timeout | Exponential backoff | 503 with retryable code | error log + alert |
| Conflict | Conditional retry | 409 with conflict detail | info log + metric |

## Timeout Budget
| Hop | Budget (ms) | Notes |
|---|---|---|
| Client -> Edge/API | 500 | Includes auth + routing |
| API -> Domain | 300 | Includes validation |
| Domain -> Store/Dependency | 200 | Includes retry overhead |

## Interface Versioning
- Version strategy (`v1`, date-based, semver):
- Backward-compatibility guarantees:
- Deprecation window and removal policy:

<!-- decapod:codebase-attestation:start -->
## Codebase Attestation

- Repository signal fingerprint: `d85fea05c327157b8eaa834019da77bceb474918bb9adfc1eb0873b51d54d9da`
- Significant implementation surfaces: `.github/` (2 files), `Makefile/` (1 files), `README.md/` (1 files), `artifact/` (6 files), `lab-example/` (1 files)
- Refreshed from the current codebase by `decapod specs.refresh`
<!-- decapod:codebase-attestation:end -->
