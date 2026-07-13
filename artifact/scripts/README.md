# Evaluation and Replication Scripts

This directory contains the automation scripts to execute the benchmarks, perform validation checks, parse raw run trajectories, and compile empirical results.

## Script Descriptions

* `run_benchmark.py`: Reproducible `synthetic_fixture` generator for the legacy three-condition schema. It never emits pilot or empirical records.
* `run_agent.py`: Explicitly authorized walk-away pilot/empirical capture wrapper for a supplied agent command and independent blind evaluator. It requires a task package, model metadata, immutable protocol tag, event log, frozen-oracle intervention log, pre-inference context manifest, evaluator result, and explicit real-run confirmation.
* `parse_results.py`: Fail-closed parser/aggregator. It refuses mixed data kinds and refuses to treat synthetic fixtures as pilot or empirical evidence.
* `validate_artifact.py`: Standard-library validation for task packages, run records, provenance, and data-kind separation.

The current repository is in harness validation. Run `run_agent.py` only for an approved small pilot after credentials, task scope, and protocol state are available. It does not invoke a model by itself and does not authorize a paid benchmark.
