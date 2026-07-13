# Research Taxonomy and Terminology

This document defines the key concepts and terms used in our paper and evaluation suite. Defining these terms precisely prevents semantic drift and ensures clarity.

---

## 1. Core Primitives

### Accountable Agentic Execution
The execution of software-engineering tasks by autonomous agents in a manner that is auditable, bounded, recoverable, and verifiable. It shifts the operational model of agents from unsupervised text generation to bounded systems processes whose actions are tracked and whose outputs are checked against formal assertions.

### Intent
The human or team’s desired outcome, why it matters, constraints and priorities, unresolved questions, stop conditions, and standard of completion. A prompt is an initial and often incomplete expression of intent. Decapod preserves and progressively resolves intent through governed plans, todos, project specifications, context capsules, proof hooks, and acceptance rubrics; those artifacts are projections of intent, not its source of authority.

### Custody
The scoped ownership and authority context assigned to an agent for a specific task. Custody defines the boundaries of the agent's environment, specifying:
* The isolated workspace (e.g., a specific git worktree or container).
* The permitted git branches.
* The files it is allowed to read or write.
* The tools (compilers, test runners, network APIs) and credentials it is authorized to access.
Custody reduces cross-task corruption by assigning ownership and keeping repository mutations in the governed workspace. It is not, by itself, a complete operating-system sandbox or credential-isolation guarantee.

### Trajectory
An event-backed record of governance activity during an agent task. In Decapod, todo, broker, proof, and related event journals can be rendered as a flight-recorder timeline or transcript. The record is useful for reconstruction and review, but this paper does not claim that it captures every model token, shell byte, file diff, or tamper-proof execution event.

### Proof
Reviewable, machine-checkable evidence about the configured validation and proof gates for a declared *intent*. A proof can include test logs, compiler outputs, proof events, workunit results, validation reports, and provenance references. It is evidence for a completion decision, not a guarantee of semantic correctness; this paper does not claim that Decapod currently signs one universal certificate.

---

## 2. Systems and Architectural Concepts

### Validation
The execution of programmatic tests, compilers, linter checks, and security scanners within the custody context to evaluate whether the agent's changes satisfy the rules of the project. Validation acts as a filter that must be passed before a completion claim is accepted.

### Governance Kernel
A daemonless, local-first, repo-native control plane that agents invoke to resolve context, manage intent and task ownership, establish workspaces, run validations, record governance events, and gate promotion. The kernel does not generate code and does not necessarily intercept every action of an external agent runtime.

### Operationally More Knowledgeable
A system-level property under test: the unchanged underlying model has more relevant, correctly scoped, and authoritative project information available when it decides what to do. This does not mean Decapod trains the model, changes its parameters, or increases intrinsic model intelligence.

### Transcript-Only Workflow
An analytical baseline in which the durable record is primarily the prompt, chat transcript, and final diff. Many real workbenches add memory, sandboxing, checkpoints, CI, or coordination, so the term must not be used as a universal description of current agent systems.

### Proof-Backed Completion
A state transition in which task completion or promotion is permitted only after the configured validation, proof, workunit, and workspace gates are satisfied. Verbal assertions alone are insufficient; the exact gates and evidence are part of the project configuration.

### Local-First Governance
A design philosophy for agent control planes where all configuration, workspaces, trajectories, validations, and proofs are stored directly within the target repository filesystem and executed locally. This avoids dependency on third-party cloud orchestration APIs and allows standard developers to audit and replay agent runs using local tools.

### Fleet Coherence
The bounded emergent property by which independently launched agent processes can resolve common authority, obtain explicit task/workspace custody, reconstruct selected governance state, transfer work, and inspect shared proof through durable project state. Fleet coherence is produced by Intent, Custody, Trajectory, and Proof; it is not a fifth primitive. It does not imply global consensus, complete action capture, lossless conversation transfer, or conflict-free integration.

### Cross-Runtime Context Discontinuity
Loss of usable task state when execution moves between sessions, workbenches, models, or providers that do not share a conversation. This is distinct from finite-context drift inside one session.

### Project-Owned Memory
Governed decisions, constraints, observations, unresolved state, and provenance whose authority and lifecycle belong to the project rather than a vendor chat account. Project-owned memory may still be stale, irrelevant, contradictory, or harmful and therefore requires selection and audit.

### Governed Handoff
An approved transfer of task ownership accompanied by durable summary/event and available task, context, dependency, workspace, and proof references. The current implementation does not transfer hidden model reasoning or guarantee merge success.

### Operator Decoupling
Separation between the human's natural-language expression of software intent and the workbench-specific governance operations needed to execute it. The agent invokes the stable Decapod CLI/RPC contract at governance boundaries; this does not claim that vendor-specific commands cease to exist.

### Proof Portability
The ability of a later agent or reviewer to inspect and revalidate configured evidence bound to a governed state. Portability does not make stale local proof sufficient for a changed or integrated state.

### Cost-of-Fragmentation Terms
**Context rehydration waste** is repeated project discovery; **duplicated inference waste** is multiple agents reasoning over the same work; **collision waste** is repair after overlapping mutation or assumptions; **handoff waste** is reconstruction of missing state; **verification waste** is repeated checking because evidence is unavailable or untrusted; **integration waste** is repair after separately valid work fails in combination; **dialect waste** is human translation into provider procedures; **context-bloat waste** is inference spent on irrelevant governance material; and **abandonment waste** is interrupted work that cannot be resumed economically.
