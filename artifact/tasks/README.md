# Benchmark Task Suite

This directory contains the definitions and target codebases for the target 35-task cohort. The repository currently contains one example package to validate the contract; the cohort is not frozen and no confirmatory execution is authorized.

## Task Format

Each task is defined in a structured subdirectory containing:
* `task.json`: A manifest detailing:
  * `id`: Unique identifier (e.g., `task-01-code-mod`).
  * `category`: One of the 7 task categories.
  * `canonical_intent`: The human/team desired outcome, motivation, constraints, priorities, unresolved questions, stop conditions, and completion standard shared by both cells.
  * `prompt_variants`: Semantically matched `natural_delegation` and `procedural` prompts.
  * `base_commit`: The commit hash of the target repository state.
  * `context_available`: The project authority and repository context visible to each substrate; treatment context must be provenance-linked and the hidden rubric excluded.
  * `complexity_profile`: Required interacting reasoning and empirical-eligibility status.
  * `study_eligibility`: Studies for which the package has frozen checkpoints, task graphs, and evaluators.
  * `handoff_checkpoint` / `task_graph`: Study B/D transfer rules or Study C dependency/integration contract when applicable.
  * `validation_commands`: Shell commands that must succeed for the task to be considered complete (e.g., `pytest tests/test_parser.py`).
* `gold/`: The reference solution diff, used only for human auditing comparisons and checking correctness.
  * `eval_suite/`: An independent evaluator withheld from the agent workspace during execution.
  * `oracle.json`: Prewritten responses for clarification questions.

## Directory Structure

```text
tasks/
├── task-01-code-mod/
│   ├── task.json
│   ├── oracle.json
│   ├── prompts/
│   └── eval_suite/       # harness-controlled, withheld from the agent
├── task-02-refactor/
│   └── ...
└── README.md (this file)
```

The current example is a deterministic schema/harness fixture and is not empirical-eligible. Future Study B packages require a frozen observable checkpoint and conventional/Decapod payload definitions. Study C packages require a task graph, overlap classes, and post-integration validation. Study D additionally freezes workbench pairs. Hidden evaluators and rubrics remain unavailable to executing agents.
