# Accountable Agentic Execution

> **Research paper and executable evaluation program investigating individual-agent alignment and heterogeneous fleet coherence through Intent, Custody, Trajectory, and Proof.**
>
> **Status**: Pre-results technical report. The model, terminology, paper, and reproducibility harness are public. The empirical benchmark has not yet been executed. Checked-in run records and aggregate values are synthetic harness fixtures, not observations; no treatment effect or performance claim should be inferred from them.

---

[![LaTeX Compilation](https://github.com/DecapodLabs/accountable-agentic-execution/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/DecapodLabs/accountable-agentic-execution/actions/workflows/deploy-pages.yml)
[![Artifact Project Page](https://img.shields.io/badge/Project-Dashboard-blueviolet)](https://decapodlabs.github.io/accountable-agentic-execution/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## 1. Executive Summary

As Large Language Model (LLM) coding agents transition from passive completion assistants to autonomous, tool-using executors, their operations resemble concurrent processes running over a mutable repository space. Many workflows still rely heavily on conversational transcripts and code diffs as durable records; that baseline does not by itself preserve authority, ownership, cross-session continuity, or machine-checkable completion evidence.

This repository hosts the LaTeX source and reproducible evaluation harness for our paper: **"Intent, Custody, Trajectory, and Proof: Toward Accountable Execution in Agentic Software Engineering."**

We formalize four core primitives to achieve accountable agentic execution:

* **Intent**: The human or team’s desired outcome, motivation, constraints, priorities, unresolved questions, and standard of completion, progressively represented across governed artifacts.
* **Custody**: Governed task ownership and isolated git-worktree or configured container boundaries within which the agent operates.
* **Trajectory**: Event-backed records of selected task, broker, proof, memory, and governance activity that can be rendered as a flight-recorder timeline.
* **Proof**: Programmatically checkable validation, proof-run, workunit, and provenance evidence for a governed workspace state.

This artifact is designed to evaluate these primitives using **Decapod**, a daemonless, local-first governance kernel that coordinates intent, task custody, validation, proof events, and publication around existing coding agents. The primary empirical question remains whether one complex natural outcome-oriented request can support “type the outcome and walk away”: Decapod resolves authoritative project context before implementation inference, while the underlying model remains unchanged.

The expanded research program also tests **fleet coherence**: whether independently launched agents can use durable project authority, task ownership, selected trajectory, and shared proof to hand work across sessions/workbenches and execute concurrently with less reconstruction, duplication, and integration waste. Fleet coherence is an emergent property of the four primitives, not a fifth primitive or a claim of global consensus. The human speaks naturally to the available agent; the agent handles Decapod's stable governance protocol.

The central fleet-coherence question is: **Can multiple independently launched agents concurrently solve similar but distinct problems in the same codebase while preserving shared authority, distinct task custody, isolated mutation, dependency awareness, and integrated proof?** Worktrees alone answer only the direct-mutation part of that question; the prospective fleet study also measures duplicate inference, semantic overlap, dependency violations, merge and integration repair, and proof after combination.

Decapod is offered as a candidate **agent-governance interoperability profile**: a standard agent-callable component that coding-agent harnesses could pre-bundle or discover. The goal is a narrow machine contract for authority, task custody, selected trajectory, and proof so users and agents can move fluidly among Claude, Codex, Antigravity, Grok, and other conforming harnesses without making one vendor conversation the project's durable state. This is a standards direction inspired by MCP and A2A and by the layered, independently implementable interfaces of HTTP and IP—not a claim that Decapod is already an adopted standard, native MCP/A2A implementation, HTTP service, or vendor-bundled component. The current implementation is a daemonless local CLI plus a Decapod-specific structured process RPC. See the [interoperability profile and implementation roadmap](docs/agent-governance-interoperability.md).

The constitution is the authority root for that contract. Decapod currently embeds a structured baseline constitution in the binary and supports a binding project-local override; task-scoped context resolution selects provenance-bearing projections before inference. An organization-level overlay is planned but not implemented at the inspected revision. This design is the author's response to repository-instruction poisoning: authority, scope, selection, and proof expectations should be explicit rather than treating any large instruction file as automatically trustworthy. The author reports reaching this approach through an independent internal evaluation several months before the February 2026 ETH Zurich preprint; public git history currently establishes constitution/override work around the preprint's publication, so the earlier chronology remains labeled author testimony rather than a priority claim.

The implementation mapping is pinned to Decapod [`e7df80d`](https://github.com/DecapodLabs/decapod/commit/e7df80d8234a80c490f6fe2119a6cff32135a386) (`v0.66.1`). It verifies real task claims, trust-gated handoff, workspaces, context capsules, repository memory, governance events, proofs, and publication gates. It also records narrower boundaries: shared ownership exists, handoff does not transfer hidden conversation state, worktrees do not guarantee clean integration, and the public cloud backend is unavailable.

Study A is the primary walk-away CN-versus-DN comparison. Prospective Studies B–D cover handoff continuity, concurrent fleets, and tool switching. Study E is a separately labeled longitudinal case study: at the inspected commit, a checked-in git-derived snapshot records 2,127 commits and 326 tags between February and July 2026, but those facts do not establish a causal effect or low review burden. No controlled fleet results exist. The project does not claim complete OS-level sandboxing, credential isolation, universal action interception, conflict-free merging, or signed completion certificates.

Public adoption is ecological context, not performance evidence. A July 13, 2026 API snapshot reported 222 GitHub stars, 21 forks, and 6,983 crates.io downloads—approximately 7,000 downloads, but not more than 7,000 in that query. These counts do not establish correct use, interoperability, or a treatment effect.

---

## 2. Directory Layout

The workspace is organized to keep paper drafts, empirical records, and system documentation strictly partitioned:

```text
├── paper/                 # LaTeX paper sources and bibtex citations
│   ├── sections/          # Draft files for sections 01-09
│   ├── figures/           # Plot files and diagram vectors
│   └── tables/            # Evaluator-generated LaTeX table inputs
├── artifact/              # Reproducible experiment package
│   ├── tasks/             # Task-package contract + one non-empirical fixture; target suite is 35
│   ├── baselines/         # Execution traces for prompt & checklist baselines
│   ├── decapod-runs/      # Execution traces under Decapod governance
│   ├── scripts/           # Execution and metrics collation scripts
│   ├── fixtures/          # Synthetic schema fixtures, never empirical evidence
│   ├── observational/     # Separately bounded longitudinal repository facts
│   └── results/           # Processed synthetic summary data and future generators
├── docs/                  # Design registers, publications logs, and taxonomy
│   ├── research-claim.md  # Main claims and falsifiable predictions
│   ├── experiment-plan.md # Metric definitions and experimental layout
│   ├── fleet-coherence-protocol.md # Prospective handoff/concurrency/tool-switch studies
│   ├── agent-governance-interoperability.md # Candidate thin-waist profile and implementation roadmap
│   ├── implementation-claim-matrix.md # Decapod code/test support and boundaries
│   └── terminology.md     # Project taxonomy and definitions
└── pages/                 # Web landing page and metrics dashboard
```

---

## 3. Getting Started

> [!IMPORTANT]
> To compile the LaTeX draft or execute the verification scripts, you must install the required system dependencies:
> ```bash
> sudo apt-get update && sudo apt-get install -y build-essential latexmk texlive-latex-extra git python3
> ```

### Building the Paper
To build the LaTeX source document to a compiled PDF locally:
```bash
make paper
```
To check directory layout integrity and list system dependencies:
```bash
make check
```
To clean build files:
```bash
make clean
```

### Running the Artifact
Please refer to the [reproducibility guide](artifact/README.md) inside the `artifact/` directory for instructions on executing baseline agents, running the Decapod governance kernel, and regenerating the statistical plots shown in the paper.
