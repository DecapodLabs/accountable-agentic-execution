# Decapod Governed Runs (Treatment)

This directory stores the execution outputs for Condition C, where agent runs are actively governed by the Decapod local-first kernel.

## File Structure per Run

For each governed run, we preserve:

* `[task-id]_[run-num]_intent.json`: A copy of the initial intent manifest.
* `[task-id]_[run-num]_trajectory.jsonl`: The immutable event ledger recorded by the Decapod kernel containing all tool inputs, outputs, file changes, and environment validation steps.
* `[task-id]_[run-num]_proof.json`: The generated cryptographic proof file compiled after the validation gates successfully pass.
* `[task-id]_[run-num]_diff.patch`: The final code changes proposed by the agent.
* `[task-id]_[run-num]_outcome.json`: Run statistics and exit indicators (e.g., total steps, tool failures, interruption flags).
