# Benchmark Task Suite

This directory contains the definitions and target codebases for the 35 benchmark tasks used in the evaluation.

## Task Format

Each task is defined in a structured subdirectory containing:
* `task.json`: A manifest detailing:
  * `id`: Unique identifier (e.g., `task-01-code-mod`).
  * `category`: One of the 7 task categories.
  * `description`: The prompt description provided to the agent.
  * `base_commit`: The commit hash of the target repository state.
  * `validation_commands`: Shell commands that must succeed for the task to be considered complete (e.g., `pytest tests/test_parser.py`).
* `gold/`: The reference solution diff, used only for human auditing comparisons and checking correctness.
* `eval_suite/`: An independent set of unit and integration tests run by the evaluation harness to verify the agent's work. Crucially, these tests are *not* accessible to the agent during execution, acting as an external correctness check.

## Directory Structure (Planned)

```text
tasks/
├── task-01-code-mod/
│   ├── task.json
│   ├── gold.diff
│   └── eval_suite/
├── task-02-refactor/
│   └── ...
└── README.md (this file)
```
