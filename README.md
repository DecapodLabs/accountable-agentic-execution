# Accountable Agentic Execution

> **Research paper and reproducible evaluation artifact investigating LLM-based software engineering agents as distributed execution processes governed by Intent, Custody, Trajectory, and Proof.**

---

[![LaTeX Compilation](https://github.com/DecapodLabs/accountable-agentic-execution/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/DecapodLabs/accountable-agentic-execution/actions/workflows/deploy-pages.yml)
[![Artifact Project Page](https://img.shields.io/badge/Project-Dashboard-blueviolet)](https://decapodlabs.github.io/accountable-agentic-execution/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## 1. Executive Summary

As Large Language Model (LLM) coding agents transition from passive completion assistants to autonomous, tool-using executors, their operations resemble concurrent processes running over a mutable repository space. The standard record of agentic work—typically consisting only of conversational chat transcripts and code diffs—fails to provide the verification, safety, and recoverability guarantees required for production environments. 

This repository hosts the LaTeX source and reproducible evaluation harness for our paper: **"Intent, Custody, and Proof: Toward Accountable Execution in Agentic Software Engineering."**

We formalize four core primitives to achieve accountable agentic execution:

* **Intent**: A durable, structured manifest that defines the task objective and success criteria outside the model's transient context window.
* **Custody**: The isolated workspace boundaries (branches, file scopes, permitted commands) within which the agent is allowed to execute.
* **Trajectory**: An append-only, kernel-logged audit ledger of every observation, action, and validation state during the run.
* **Proof**: Programmatically checkable, cryptographically signed evidence that the workspace state has passed all validation criteria.

This artifact is designed to evaluate these primitives using **Decapod**, a local-first governance kernel that enforces custody limits and compiles proof files around existing coding agents.

---

## 2. Directory Layout

The workspace is organized to keep paper drafts, empirical records, and system documentation strictly partitioned:

```text
├── paper/                 # LaTeX paper sources and bibtex citations
│   ├── sections/          # Draft files for sections 01-09
│   ├── figures/           # Plot files and diagram vectors
│   └── tables/            # Evaluator-generated LaTeX table inputs
├── artifact/              # Reproducible experiment package
│   ├── tasks/             # Suite of 35 benchmark tasks
│   ├── baselines/         # Execution traces for prompt & checklist baselines
│   ├── decapod-runs/      # Execution traces under Decapod governance
│   ├── scripts/           # Execution and metrics collation scripts
│   └── results/           # Processed summary data and chart generators
├── docs/                  # Design registers, publications logs, and taxonomy
│   ├── research-claim.md  # Main claims and falsifiable predictions
│   ├── experiment-plan.md # Metric definitions and experimental layout
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
