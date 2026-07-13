# Empirical Evaluation Plan

This document outlines the experimental design, conditions, metrics, and methodology to evaluate the effectiveness of governed agent execution using Intent, Custody, Trajectory, and Proof primitives. The experiments compare governed agent execution against standard un-governed agent runs.

---

## 1. Experimental Conditions

The evaluation uses a single underlying LLM (e.g., GPT-4o, Gemini 1.5 Pro, or Claude 3.5 Sonnet) configured with the same temperature and system instructions across three distinct operational environments:

### Condition A: Baseline (Prompt-Only)
* **Description**: The agent is given a target repository, access to command-line tools (e.g., shell, file edit), and a prompt describing the task.
* **Control**: No structured guidelines are enforced. The agent is free to run any commands, edit any files, and must declare completion verbally in the chat transcript.
* **Custody**: Single shared workspace, direct main branch edits.
* **Verification**: Verbal assertion in chat (e.g., "I have finished the task and verified it works").

### Condition B: Structured Baseline (Checklist-Disciplined)
* **Description**: The agent is provided with the same tools and prompt as Baseline A, but is prompted to create and update a markdown checklist (`todo.md`) in the repository.
* **Control**: The agent is instructed to write down its checklist before starting, check off items as it progresses, and write a summary of changes upon completion.
* **Custody**: Single shared workspace, direct main branch edits.
* **Verification**: Self-reported checklist validation.

### Condition C: Treatment (Decapod-Governed)
* **Description**: The agent is executed within the Decapod governance kernel.
* **Custody**: Work is isolated in a dedicated workspace (e.g., `git worktree`) bound to a task-scoped branch. Repository and runtime policy boundaries are applied where configured; this is not a claim of arbitrary command or credential filtering.
* **Intent**: Durable task intent is represented through Decapod plans, todo records, project specs, and proof hooks rather than a universal `.decapod/intent.json` file.
* **Trajectory**: Decapod records governance events across todo, broker, proof, and related journals; the flight recorder renders these records, but the current kernel is not claimed to capture every tool input, output, or file diff.
* **Validation & Proof**: The agent must run the configured validation and proof hooks. Successful results are recorded in proof events and can be required by workunit and publication gates; the current kernel is not claimed to freeze every workspace byte or generate one universal signed certificate.

---

## 2. Evaluation Metrics

We evaluate the runs across these key metrics:

| Metric | Dimension | Definition | Measurement Method |
| :--- | :--- | :--- | :--- |
| **Task Completion Rate** | Utility | Percentage of tasks where the final repository state meets the objective. | Evaluated by an independent test suite run by the orchestrator (not accessible to the agent). |
| **Invalid Completion Claims** | Reliability | Rate at which the agent asserts "finished" but the code fails the validation criteria. | Binary flag: `1` if agent claims success but tests fail; `0` otherwise. |
| **Validation Pass/Fail Accuracy** | Rigor | Alignment between the agent's reported validation outcome and external evaluation. | Difference between agent-reported test passing and external-run test passing. |
| **Recoverability Rate** | Resilience | Rate of successful task completion after a forced mid-run interruption. | Terminate process at 50% average step limit. Resume using condition rules. Record success. |
| **Concurrent Edit Conflicts** | Safety | Number of task conflicts or corrupted files when two agents run concurrently. | Run two agents simultaneously on overlapping files. Count merge conflicts / build failures. |
| **Review Effort (Auditing Time)** | Human Cost | Time taken by a human developer to audit and approve or reject the work. | User study tracking seconds spent reviewing logs before correctly making a merge decision. |
| **Trace Usefulness** | Auditability | Qualitative/Quantitative metric scoring if a reviewer can locate a bug from the log. | Reviewer rating (1-5) and accuracy in identifying introduced runtime errors. |
| **Evidence Reproducibility** | Reproducibility | Verification that the claims made in the proof match a re-run of the validation suite. | Automated replay of the trajectory against the captured repository snapshot. |

---

## 3. Representative Task Categories

We evaluate the three conditions against a suite of 35 benchmark tasks (5 tasks per category):

1. **Small Code Modification**: Changing a single logic path (e.g., fixing a date parser boundary condition) in a single file.
2. **Refactor**: Restructuring a codebase (e.g., extracting an interface) across 3-5 files without changing behavior.
3. **Test Repair**: Fixing an existing broken test suite in a legacy project where codebase context is large.
4. **Documentation Generation**: Reading source code and generating correct API documentation that matches the implementation.
5. **Multi-File Feature**: Adding a new endpoint and corresponding database models, validation schemas, and unit tests.
6. **Concurrent Two-Agent Change**: Two separate agents attempting to resolve two separate but related issues in the same codebase concurrently.
7. **Interrupted/Resumed Task**: A task designed to trigger mid-run failure (e.g., api timeout, rate limits, or direct signal kill) and verify if the agent can resume cleanly.

---

## 4. Execution Protocol

To gather data, we will run the following automated pipeline:

1. **Scaffold Repositories**: Initialize 5 target base repositories (e.g., small Python, Go, and TypeScript codebases with test suites).
2. **Inject Tasks**: Programmatically inject the benchmark tasks into the repositories.
3. **Execute Runs**:
   - Run each task 5 times per condition (totaling 35 tasks * 3 conditions * 5 runs = 525 executions) to account for LLM non-determinism.
   - For interruption tasks, send `SIGINT` to the running process at a random step between step 3 and 10.
4. **Extract Metrics**: Run the available parsing and aggregation scripts under `artifact/scripts/` to measure completion rates, invalid claims, and validation results; add and test any missing evaluator before claiming reproducibility.
5. **Synthesize Results**: Generate comparative tables and export data to `artifact/results/` for plotting.
