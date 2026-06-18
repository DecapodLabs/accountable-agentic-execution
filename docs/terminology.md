# Research Taxonomy and Terminology

This document defines the key concepts and terms used in our paper and evaluation suite. Defining these terms precisely prevents semantic drift and ensures clarity.

---

## 1. Core Primitives

### Accountable Agentic Execution
The execution of software-engineering tasks by autonomous agents in a manner that is auditable, bounded, recoverable, and verifiable. It shifts the operational model of agents from unsupervised text generation to bounded systems processes whose actions are tracked and whose outputs are checked against formal assertions.

### Intent
The durable, human-declared objective and set of constraints driving an agentic task. Unlike transient model prompts, *intent* is represented as a structured manifest (e.g., JSON/YAML) that remains persistent across model calls, surviving context window overflows, api timeouts, or agent restarts. It specifies what must be achieved and what validation criteria must pass.

### Custody
The scoped ownership and authority context assigned to an agent for a specific task. Custody defines the boundaries of the agent's environment, specifying:
* The isolated workspace (e.g., a specific git worktree or container).
* The permitted git branches.
* The files it is allowed to read or write.
* The tools (compilers, test runners, network APIs) and credentials it is authorized to access.
Custody ensures that an agent cannot access unauthorized data or corrupt concurrent tasks running in adjacent workspaces.

### Trajectory
The immutable, ordered ledger of all events occurring during an agent's execution. A trajectory records:
* Every user interaction and task checkpoint.
* Every tool call (command run, API requested) along with exact inputs and outputs.
* Every file modification (patch/diff).
* Every validation check result.
The trajectory is captured by the governance kernel, not self-reported by the agent, ensuring its reliability as an audit trail.

### Proof
Reviewable, machine-checkable evidence demonstrating that the repository state satisfies the declared *intent*. A proof typically consists of successful test suite logs, lint reports, static analysis results, and compiler outputs, cryptographically bound to a snapshot of the workspace (commit hash or tree hash). It represents a concrete justification of completion, rather than a conversational claim.

---

## 2. Systems and Architectural Concepts

### Validation
The execution of programmatic tests, compilers, linter checks, and security scanners within the custody context to evaluate whether the agent's changes satisfy the rules of the project. Validation acts as a filter that must be passed before a completion claim is accepted.

### Governance Kernel
A local-first, repo-native control plane that intercepts agent execution to enforce custody, manage intent manifests, record trajectories, run validations, and compile proofs. The kernel does not generate code; it governs the processes that do.

### Transcript-Only Workflow
The standard industry practice where the only record of an agent's work is the text chat transcript containing the prompt, the model's chat responses, and the final git diff. This workflow lacks explicit custody, structured intent manifests, immutable tool logs, and independent proof generation.

### Proof-Backed Completion
A state transition protocol where an agent's task is only marked as "complete" (and eligible for merging) once the governance kernel generates a valid *proof* artifact showing all validation gates have passed. Verbal assertions of completion by the agent are ignored.

### Local-First Governance
A design philosophy for agent control planes where all configuration, workspaces, trajectories, validations, and proofs are stored directly within the target repository filesystem and executed locally. This avoids dependency on third-party cloud orchestration APIs and allows standard developers to audit and replay agent runs using local tools.
