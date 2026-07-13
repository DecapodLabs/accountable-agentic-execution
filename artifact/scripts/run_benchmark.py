#!/usr/bin/env python3
"""Generate explicitly labelled legacy synthetic fixtures.

This script is a schema/harness fixture generator, not an agent runner. It must
never be used to create pilot or empirical records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
from pathlib import Path

TASKS_COUNT = 35
RUNS_PER_TASK = 5
CONDITIONS = ["A", "B", "C"]
PROTOCOL_ID = "legacy-three-condition-fixture-v1"

COND_CONFIGS = {
    "A": {"comp": 0.40, "invalid": 0.38, "val_acc": 0.55, "recovery": 0.15, "conflicts": 1.4, "review": 125.0},
    "B": {"comp": 0.48, "invalid": 0.24, "val_acc": 0.68, "recovery": 0.22, "conflicts": 1.2, "review": 98.0},
    "C": {"comp": 0.85, "invalid": 0.00, "val_acc": 0.98, "recovery": 0.72, "conflicts": 0.0, "review": 42.0},
}


def simulate_run(task_id: int, condition: str, seed: int) -> dict[str, object]:
    task_hash = int.from_bytes(hashlib.sha256(str(task_id).encode()).digest()[:8], "big")
    random.seed(seed + task_hash)
    config = COND_CONFIGS[condition]
    success = random.random() < config["comp"]
    invalid_claim = (not success) and random.random() < config["invalid"]
    validation_accuracy = random.random() < config["val_acc"]
    recovery_success = random.random() < config["recovery"]
    conflicts = 0
    if config["conflicts"] > 0:
        threshold = 2.71828 ** (-config["conflicts"])
        k, probability = 0, 1.0
        while probability > threshold:
            k += 1
            probability *= random.random()
        conflicts = k - 1
    return {
        "schema_version": "run-record.v2",
        "kind": "synthetic_fixture",
        "run_id": f"fixture-task-{task_id:02d}-{condition}-{seed}",
        "task_id": f"task-{task_id:02d}",
        "protocol_id": PROTOCOL_ID,
        "substrate": "legacy_fixture",
        "instruction_style": "legacy_fixture",
        "prompt": {
            "text": "Legacy three-condition synthetic fixture; no model prompt was executed.",
            "characters": 0,
            "approx_tokens": 0,
            "procedural_steps": 0,
            "named_paths": 0,
            "named_commands": 0,
            "named_tests": 0,
            "implementation_prescriptions": 0,
        },
        "provenance": {
            "protocol_id": PROTOCOL_ID,
            "task_commit": "synthetic-fixture-no-repository",
            "model": {"provider": "none", "identifier": "none", "version": "none", "decoding": {}},
            "runtime": {"agent_version": "fixture-generator", "decapod_version": "none"},
            "timestamps": {"started_at": None, "ended_at": None, "elapsed_seconds": None},
            "environment": {"host": "fixture", "container": False},
            "configuration": {"tool_permissions": "not_applicable", "workspace": "not_applicable"},
        },
        "outcome": {
            "task_success": success,
            "intent_fidelity": None,
            "invalid_completion_claim": invalid_claim,
            "proof_completeness": None,
            "validation_accuracy": validation_accuracy,
            "interruption_recovery_success": recovery_success,
            "concurrent_conflicts": conflicts,
            "human_review_time_seconds": round(max(10.0, random.normalvariate(config["review"], config["review"] * 0.25)), 2),
        },
        "synthetic_parameters": {"condition": condition, "seed": seed, "generator": "run_benchmark.py"},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["synthetic_fixture"], default="synthetic_fixture")
    parser.add_argument("--output-root", type=Path, default=Path("artifact"))
    args = parser.parse_args()
    if args.mode != "synthetic_fixture":
        raise SystemExit("fail-closed: run_benchmark.py only generates synthetic_fixture records")

    baseline_dir = args.output_root / "baselines"
    decapod_dir = args.output_root / "decapod-runs"
    baseline_dir.mkdir(parents=True, exist_ok=True)
    decapod_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for task_idx in range(1, TASKS_COUNT + 1):
        for condition in CONDITIONS:
            for seed_idx in range(1, RUNS_PER_TASK + 1):
                seed = 42 + seed_idx * 17
                record = simulate_run(task_idx, condition, seed)
                folder = decapod_dir if condition == "C" else baseline_dir
                path = folder / f"run_task-{task_idx:02d}_cond_{condition}_seed_{seed}.json"
                path.write_text(json.dumps(record, indent=2) + "\n")
                count += 1
    print(f"Wrote {count} synthetic_fixture records; no agent or model was executed.")


if __name__ == "__main__":
    main()
