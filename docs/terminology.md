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
The standard industry practice where the only record of an agent's work is the text chat transcript containing the prompt, the model's chat responses, and the final git diff. This workflow lacks explicit custody, structured intent manifests, immutable tool logs, and independent proof generation.

### Proof-Backed Completion
A state transition in which task completion or promotion is permitted only after the configured validation, proof, workunit, and workspace gates are satisfied. Verbal assertions alone are insufficient; the exact gates and evidence are part of the project configuration.

### Local-First Governance
A design philosophy for agent control planes where all configuration, workspaces, trajectories, validations, and proofs are stored directly within the target repository filesystem and executed locally. This avoids dependency on third-party cloud orchestration APIs and allows standard developers to audit and replay agent runs using local tools.
