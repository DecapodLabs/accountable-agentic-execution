# Reproducible Research Artifact

This directory contains the code, data contracts, scripts, and staged execution harness for the empirical research program in *"Intent, Custody, Trajectory, and Proof: Toward Accountable Execution in Agentic Software Engineering"*. Study A remains the primary one-shot walk-away comparison. Prospective Studies B–D cover handoff, concurrent fleets, and tool switching; Study E is observational dogfooding evidence. Checked-in controlled run records and summaries are explicitly `synthetic_fixture` records, not executions by an LLM or human reviewers.

---

## Artifact Philosophy

A key contribution of this paper is the **reproducible artifact**. Rather than simply publishing aggregate statistics or static charts, this artifact is designed to let any researcher audit, replay, and verify our findings. 

To achieve this, the artifact strictly adheres to the following principles:

1. **Completeness of Run Data**: Every run record must identify its data kind and preserve the schema needed for the planned experiment:
   * **Kind and study**: controlled records declare `synthetic_fixture`, `pilot`, or `empirical` and one study identifier; aggregation fails closed when kinds or studies are mixed.
   * **Initial State**: The base repository and exact commit hash before the run.
   * **Prompt**: The exact natural language instruction given to the agent, paired to one canonical intent.
   * **Pre-inference context**: The selected authority sources, rationale, hashes, exclusions, relevance audit, and resolution latency for governed runs.
   * **Convergence**: Model requests, tokens, tool calls, searches, pre-edit reads, failure cycles, rewrites, and time to acceptable completion.
   * **Trajectory**: Governance and intervention records; real tool trajectories are not present in synthetic fixtures.
   * **Validation Logs**: Synthetic outcome fields in fixtures; real validation logs must be collected and provenance-linked for pilot or empirical runs.
   * **Proof Artifact**: A planned evidence field, not a claim that a proof certificate was generated.
2. **Separation of Raw Data from Analyzed Results**:
   * Raw run logs (`.jsonl` files) can be quite large and are not committed directly to the git history. They should be stored locally (or downloaded using download scripts) to keep the repository lightweight.
   * Statistical summaries, parsed CSVs, and visualization scripts are checked into git under `artifact/results/`.
   * `observational` Study E records remain outside controlled summaries. Repository-derived facts, author testimony, and causal claims are separate evidence classes.
3. **Reproducibility Over Novelty**: The goal of this artifact is to enable a reader to run a single script and verify that the results match the tables in the paper, using standard, lightweight Python tools.

---

## Directory Organization

* **`tasks/`**: Canonical paired task packages. The current draft contains one example package; 34 additional packages must be authored before protocol freeze.
* **`schemas/`**: Versioned task, run-record, and protocol data contracts.
* **`baselines/`**: Legacy synthetic fixtures only; real CN records use the versioned run contract.
* **`decapod-runs/`**: Legacy synthetic fixtures only; real DN records use the versioned run contract.
* **`scripts/`**: Automation scripts to run evaluations, collect metrics, and generate tables/figures.
* **`results/`**: Parsed statistical results, generated tables, and plotting files.
* **`fixtures/fleet/`**: Conspicuously synthetic Study B–D schema fixtures.
* **`observational/`**: Git-derived Study E snapshots with explicit non-causal boundaries.

For the delegation design and staged execution rules, see [docs/delegation-protocol.md](../docs/delegation-protocol.md), [docs/fleet-coherence-protocol.md](../docs/fleet-coherence-protocol.md), [docs/human-intervention-protocol.md](../docs/human-intervention-protocol.md), and [docs/statistical-analysis-plan.md](../docs/statistical-analysis-plan.md). For commands, see [artifact/scripts/README.md](scripts/README.md).

No fleet pilot or empirical run is authorized by these files. `capture_coordination.py` requires explicit real-run confirmation and frozen manifests; it does not launch or authorize a model. The inspected Decapod implementation basis and claim boundaries are recorded in [docs/implementation-claim-matrix.md](../docs/implementation-claim-matrix.md).
