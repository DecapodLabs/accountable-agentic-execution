# Results and Generated Outputs

This directory contains generated outputs from the evaluation harness. The checked-in summary is explicitly `synthetic_fixture`; it is not an empirical result and must not be cited as one. Pilot and empirical aggregation remain fail-closed until the frozen statistical analysis path is implemented and real provenance is present.

## Files

* `summary.csv`: Synthetic fixture metrics retained for deterministic harness tests.
* `concurrency_conflicts.csv`: Log of conflicts, corrupted states, and compilation errors observed during concurrent execution experiments.
* `audit_study_times.csv`: Detailed anonymized logs from the user-study measuring the duration of manual code reviews.
* `figures/`: Renders of plots in PDF and PNG format (e.g., `completion_vs_claims.pdf` and `audit_time_dist.pdf`) used directly in the LaTeX paper.
* `tables/`: Auto-generated LaTeX table inputs (e.g., `performance_comparison.tex`) imported by `paper/sections/06-evaluation.tex`.
