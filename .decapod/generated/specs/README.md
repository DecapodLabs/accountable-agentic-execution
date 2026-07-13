# Project Specs

Canonical path: `.decapod/generated/specs/`.
These files are the project-local contract for humans and agents.

## Snapshot
- Project: accountable-agentic-execution
- Outcome: > **Research paper and reproducible evaluation artifact investigating LLM-based software engineering agents as distributed execution processes governed by Intent, Custody, Trajectory, and Proof.**
- Detected languages: Other
- Detected surfaces: not detected yet

## How to use this folder
- [INTENT.md](./INTENT.md): what success means and what is explicitly out of scope.
- [ARCHITECTURE.md](./ARCHITECTURE.md): topology, runtime model, data boundaries, and ADR trail.
- [INTERFACES.md](./INTERFACES.md): API/CLI/events/storage contracts and failure behavior.
- [VALIDATION.md](./VALIDATION.md): proof commands, quality gates, and evidence artifacts.
- [SEMANTICS.md](./SEMANTICS.md): state machines, invariants, replay rules, and idempotency.
- [OPERATIONS.md](./OPERATIONS.md): SLOs, monitoring, incident response, and rollout strategy.
- [SECURITY.md](./SECURITY.md): threat model, trust boundaries, auth/authz, and supply-chain posture.

## Canonical `.decapod/` Layout
- `.decapod/data/`: canonical control-plane state (SQLite + ledgers).
- `.decapod/generated/specs/`: **Living project specs** for humans and agents.
- `.decapod/generated/context/`: deterministic context capsules.
- `.decapod/generated/policy/context_capsule_policy.json`: repo-native JIT context policy contract.
- `.decapod/generated/artifacts/provenance/`: promotion manifests and convergence checklist.
- `.decapod/generated/artifacts/custody/`: epistemic custody artifacts (assumptions, contradictions, deferred questions).
- `.decapod/generated/artifacts/inventory/`: deterministic release inventory.
- `.decapod/generated/artifacts/diagnostics/`: opt-in diagnostics artifacts.
- `.decapod/workspaces/`: isolated todo-scoped git worktrees.

## Day-0 Onboarding Checklist
- [ ] Replace all placeholders in all 8 spec files.
- [ ] Confirm primary user outcome and acceptance criteria in [INTENT.md](./INTENT.md).
- [ ] Confirm topology and runtime model in [ARCHITECTURE.md](./ARCHITECTURE.md).
- [ ] Document all inbound/outbound contracts in [INTERFACES.md](./INTERFACES.md).
- [ ] Define validation gates and CI proof surfaces in [VALIDATION.md](./VALIDATION.md).
- [ ] Define state machines and invariants in [SEMANTICS.md](./SEMANTICS.md).
- [ ] Define SLOs, alerting, and incident process in [OPERATIONS.md](./OPERATIONS.md).
- [ ] Define threat model and auth/authz decisions in [SECURITY.md](./SECURITY.md).
- [ ] Ensure architecture diagram, docs, changelog, and tests are mapped to promotion gates.
- [ ] Run all validation/test commands and attach evidence artifacts.

<!-- decapod:codebase-attestation:start -->
## Codebase Attestation

- Repository signal fingerprint: `ecbcf9599d6fb44b41010f6f6708942017478b5559d55c780463fae3eae5e9ab`
- Significant implementation surfaces: `.github/` (2 files), `Makefile/` (1 files), `README.md/` (1 files), `artifact/` (6 files), `lab-example/` (1 files)
- Refreshed from the current codebase by `decapod specs.refresh`
<!-- decapod:codebase-attestation:end -->
