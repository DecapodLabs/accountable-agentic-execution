# Evaluation and Replication Scripts

This directory contains the automation scripts to execute the benchmarks, perform validation checks, parse raw run trajectories, and compile empirical results.

## Script Descriptions

* `run_benchmark.py`: Core execution harness. It sets up target repositories, launches the selected agent under the designated condition (A, B, or C), injects interruption events, and captures logs.
* `evaluate.py`: Verification script that runs the external test suites (`tasks/task-id/eval_suite`) on the output workspace and writes outcome reports.
* `parse_results.py`: Aggregates the raw JSON outcomes, metrics, and tokens into comparative CSVs and summarizes statistical significance tests.
* `plot_results.py`: Renders tables and plots (e.g., bar charts for task completion vs. false success claims, and cumulative audit times).
* `audit_study.py`: A helper script for running the human-auditor evaluation study. It displays trajectories and measures the time required for a human to approve or reject a change.
