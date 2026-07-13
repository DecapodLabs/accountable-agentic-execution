# Reproducible Research Artifact

This directory contains the code, data, and scripts for the planned evaluation in *"Intent, Custody, Trajectory, and Proof: Toward Accountable Execution in Agentic Software Engineering"*. The checked-in run records and summaries are synthetic harness fixtures, not executions by an LLM or human reviewers.

---

## Artifact Philosophy

A key contribution of this paper is the **reproducible artifact**. Rather than simply publishing aggregate statistics or static charts, this artifact is designed to let any researcher audit, replay, and verify our findings. 

To achieve this, the artifact strictly adheres to the following principles:

1. **Completeness of Run Data**: Every generated fixture preserves the schema needed for the planned experiment:
   * **Initial State**: The base repository and exact commit hash before the run.
   * **Prompt**: The exact natural language instruction given to the agent.
   * **Trajectory**: A placeholder outcome record; real tool trajectories are not present in these fixtures.
   * **Validation Logs**: Synthetic outcome fields; real validation logs must be collected during the benchmark.
   * **Proof Artifact**: A planned evidence field, not a claim that a proof certificate was generated.
2. **Separation of Raw Data from Analyzed Results**:
   * Raw run logs (`.jsonl` files) can be quite large and are not committed directly to the git history. They should be stored locally (or downloaded using download scripts) to keep the repository lightweight.
   * Statistical summaries, parsed CSVs, and visualization scripts are checked into git under `artifact/results/`.
3. **Reproducibility Over Novelty**: The goal of this artifact is to enable a reader to run a single script and verify that the results match the tables in the paper, using standard, lightweight Python tools.

---

## Directory Organization

* **`tasks/`**: The benchmark task suite. Contains the coding task specifications, test suites, and target codebases.
* **`baselines/`**: Executions under Condition A (prompt-only) and Condition B (checklist-only).
* **`decapod-runs/`**: Executions under Condition C (Decapod-governed).
* **`scripts/`**: Automation scripts to run evaluations, collect metrics, and generate tables/figures.
* **`results/`**: Parsed statistical results, generated tables, and plotting files.

For details on how to run a reproduction test, see the scripts documentation in [artifact/scripts/README.md](file:///home/arx/src/papers/accountable-agentic-execution/artifact/scripts/README.md).
