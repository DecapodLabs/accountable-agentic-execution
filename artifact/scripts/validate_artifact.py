#!/usr/bin/env python3
"""Validate task/run contracts and enforce synthetic/real separation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def require(record: dict, keys: list[str], label: str) -> None:
    missing = [key for key in keys if key not in record]
    if missing:
        raise SystemExit(f"{label}: missing required fields {missing}")


def validate_tasks(root: Path) -> int:
    count = 0
    for path in sorted(root.glob("task-*/task.json")):
        record = json.loads(path.read_text())
        require(record, ["schema_version", "task_id", "canonical_intent", "motivation", "constraints", "priorities", "open_questions", "stop_conditions", "acceptance_rubric", "prompt_variants", "clarification_oracle", "starting_repository", "context_available", "complexity_profile", "interruption_concurrency", "exclusion_rules", "evaluation"], str(path))
        if set(record["prompt_variants"]) != {"natural_delegation", "procedural"}:
            raise SystemExit(f"{path}: prompt variants must be natural_delegation and procedural")
        count += 1
    return count


def validate_runs(root: Path) -> tuple[int, set[str]]:
    count = 0
    kinds: set[str] = set()
    for path in sorted(root.rglob("*.json")):
        if path.name in {"summary.json", "task.json", "manifest.json"} or "tasks" in path.parts or "schemas" in path.parts:
            continue
        record = json.loads(path.read_text())
        if "kind" not in record:
            raise SystemExit(f"{path}: run record has no kind; refusing ambiguous aggregation")
        require(record, ["schema_version", "kind", "run_id", "task_id", "substrate", "instruction_style", "prompt", "provenance", "outcome"], str(path))
        if record["kind"] in {"pilot", "empirical"}:
            require(record, ["repetition_index", "canonical_intent_id", "walk_away", "context_alignment", "convergence", "execution"], str(path))
            if record["schema_version"] != "run-record.v3":
                raise SystemExit(f"{path}: real records must use run-record.v3")
            if record["walk_away"].get("coaching_allowed") is not False or record["execution"].get("evaluator_blind") is not True:
                raise SystemExit(f"{path}: real run is not walk-away or evaluator-blind")
            if not record["provenance"].get("protocol_tag"):
                raise SystemExit(f"{path}: real run has no immutable protocol tag")
        kinds.add(record["kind"])
        count += 1
    if len(kinds) > 1:
        raise SystemExit(f"mixed run kinds in one artifact tree: {sorted(kinds)}")
    return count, kinds


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-root", type=Path, default=Path("artifact"))
    args = parser.parse_args()
    tasks = validate_tasks(args.artifact_root / "tasks")
    runs, kinds = validate_runs(args.artifact_root)
    print(f"validated {tasks} task package(s), {runs} run record(s), kind={next(iter(kinds), 'none')}")


if __name__ == "__main__":
    main()
