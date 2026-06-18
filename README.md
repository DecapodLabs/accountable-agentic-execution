# Intent, Custody, and Proof: Toward Accountable Execution in Agentic Software Engineering

This repository contains the research paper and reproducible artifact for studying agentic software engineering through the lens of distributed accountable execution. 

## Project Overview

As LLM-based agents transition from autocomplete suggestors to active, delegated software engineers—running tools, modifying files, executing tests, and coordinating across workspaces—agentic coding ceases to be a simple text-generation task. Instead, it becomes a **distributed execution problem** involving concurrency, authority boundary crossing, partial failure, and state recovery.

The current record of agentic work—typically consisting only of a user prompt, a chat transcript, and a git diff—is insufficient for rigorous audit, safe concurrency, and verified completion. This project introduces a conceptual framework built on four systems-minded primitives:

1. **Intent**: The durable, structured objective driving a task, which must survive runtime interruption, tool failures, and context window drift.
2. **Custody**: The bounded execution and authority context assigned to an agent, defining which branches, files, tools, and credentials the agent is permitted to touch.
3. **Trajectory**: An ordered, immutable ledger of the agent's actions, tool invocations, environment feedback, validation results, and state transitions.
4. **Proof**: Machine-checkable or audit-ready evidence (e.g., test suites, compiler outputs, runtime assertions) demonstrating that the declared *intent* has been verified as complete.

We present **Decapod**, a local-first governance kernel, as a reference implementation of these primitives. Decapod acts as a control plane around existing coding agents to enforce custody boundaries, record trajectories, and generate verifiable proof files before work is merged.

---

## Repository Structure

The workspace is organized into three primary directories:

* **`paper/`**: The LaTeX sources for the working paper.
  * `main.tex`: Core document structure and compilation target.
  * `sections/`: Individual LaTeX files for sections 01–09 (Introduction through Conclusion).
  * `figures/` & `tables/`: Figures and generated statistical tables.
  * `references.bib`: Academic references including foundation papers in computation, information, learning, systems, and transformers.
* **`artifact/`**: The reproducible experiment package.
  * `tasks/`: A benchmark suite of software-engineering tasks used to evaluate execution.
  * `baselines/`: Run logs, metrics, and trajectories from baseline agents.
  * `decapod-runs/`: Governed runs execution logs using the Decapod kernel.
  * `scripts/`: Tools for executing tests, gathering metrics, and plotting results.
  * `results/`: Processed empirical data, comparisons, and figure generators.
* **`docs/`**: Research planning, taxonomy, and methodology documentation.
  * `research-claim.md`: Clear, falsifiable research claims and non-claims.
  * `experiment-plan.md`: The detailed evaluation protocol, metrics, and baselines.
  * `publication-plan.md`: Practical execution roadmap toward peer-reviewed publication.
  * `terminology.md`: Definitions of the conceptual framework.

---

## Build and Diagnostics

This repository includes a `Makefile` to automate paper compilation and workspace checks:

```bash
# Verify structure and dependencies
make check

# Build the LaTeX paper to PDF
make paper

# Print repository tree
make tree

# Clean build artifacts
make clean
```

For detailed setup instructions for running the experimental baselines and regenerating the paper's figures, please refer to [artifact/README.md](file:///home/arx/src/papers/accountable-agentic-execution/artifact/README.md).
