# Empirical Results

This directory contains the synthesized evaluation data, statistical analyses, and figures generated from the experiments. Unlike the raw run logs, the files in this directory are checked into git to ensure the paper can be compiled with the correct data directly.

## Files

* `summary.csv`: Aggregated performance metrics (completion rates, invalid completion claims, audit speed) comparing Baseline A, Baseline B, and the Treatment.
* `concurrency_conflicts.csv`: Log of conflicts, corrupted states, and compilation errors observed during concurrent execution experiments.
* `audit_study_times.csv`: Detailed anonymized logs from the user-study measuring the duration of manual code reviews.
* `figures/`: Renders of plots in PDF and PNG format (e.g., `completion_vs_claims.pdf` and `audit_time_dist.pdf`) used directly in the LaTeX paper.
* `tables/`: Auto-generated LaTeX table inputs (e.g., `performance_comparison.tex`) imported by `paper/sections/06-evaluation.tex`.
