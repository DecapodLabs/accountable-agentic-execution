# Evaluation and Replication Scripts

This directory contains the automation scripts to execute the benchmarks, perform validation checks, parse raw run trajectories, and compile empirical results.

## Script Descriptions

* `run_benchmark.py`: Reproducible `synthetic_fixture` generator for the legacy three-condition schema. It never emits pilot or empirical records.
* `run_agent.py`: Study A's explicitly authorized walk-away pilot/empirical capture wrapper for a supplied agent command and independent blind evaluator. It requires a task package, model metadata, immutable protocol tag, event log, frozen-oracle intervention log, pre-inference context manifest, evaluator result, and explicit real-run confirmation.
* `capture_coordination.py`: Study B–D record assembler for frozen prompt, provenance, execution, evaluator, context, and coordination manifests. It does not launch a model and requires explicit real-run confirmation.
* `collect_dogfooding.py`: Read-only Study E fact extractor for a declared Decapod git commit. Its output is observational, not controlled evidence.
* `validate_study_separation.py`: Fails closed unless every selected record has the requested study, run kind, and evidence class.
* `parse_results.py`: Fail-closed parser/aggregator. It refuses mixed data kinds and refuses to treat synthetic fixtures as pilot or empirical evidence.
* `validate_artifact.py`: Standard-library validation for task packages, run records, provenance, data-kind separation, and the observational boundary.

The current repository is in harness validation. Run `run_agent.py` or `capture_coordination.py` only for an approved small pilot after credentials, task scope, and protocol state are available. Neither script authorizes a paid benchmark.
