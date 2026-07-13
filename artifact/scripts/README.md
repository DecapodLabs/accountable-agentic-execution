# Evaluation and Replication Scripts

This directory contains the automation scripts to execute the benchmarks, perform validation checks, parse raw run trajectories, and compile empirical results.

## Script Descriptions

* `run_benchmark.py`: Synthetic fixture generator for the planned conditions (A, B, or C). It is not an agent runner and does not produce empirical evidence.
* `parse_results.py`: Available parser for raw JSON outcomes. Any final empirical evaluator, plotting pipeline, or reviewer-study harness must be added, tested, and documented before publication claims are made.
