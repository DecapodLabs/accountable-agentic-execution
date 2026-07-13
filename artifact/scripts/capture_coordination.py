#!/usr/bin/env python3
"""Assemble one authorized Study B-D record from independently captured evidence.

This command does not launch a model or grant benchmark authority. It fails closed
unless the caller confirms a real run and supplies execution, evaluator, provenance,
and coordination manifests produced by the frozen harness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import uuid
from pathlib import Path


STUDIES = {"handoff_continuity", "concurrent_fleet", "tool_switch_continuity"}


def load_object(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"fail-closed: invalid JSON at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"fail-closed: expected object at {path}")
    return value


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--study-id", choices=sorted(STUDIES), required=True)
    parser.add_argument("--kind", choices=["pilot", "empirical"], required=True)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--repetition-index", type=int, required=True)
    parser.add_argument("--substrate", choices=["conventional", "decapod_governed"], required=True)
    parser.add_argument("--protocol-tag", required=True)
    parser.add_argument("--prompt-manifest", type=Path, required=True)
    parser.add_argument("--provenance-manifest", type=Path, required=True)
    parser.add_argument("--execution-manifest", type=Path, required=True)
    parser.add_argument("--evaluator-result", type=Path, required=True)
    parser.add_argument("--coordination-manifest", type=Path, required=True)
    parser.add_argument("--context-manifest", type=Path, required=True)
    parser.add_argument("--confirm-real-run", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if not args.confirm_real_run:
        raise SystemExit("fail-closed: real coordination capture requires explicit authorization")

    inputs = {
        "prompt": args.prompt_manifest,
        "provenance": args.provenance_manifest,
        "execution": args.execution_manifest,
        "evaluator": args.evaluator_result,
        "coordination": args.coordination_manifest,
        "context_alignment": args.context_manifest,
    }
    loaded = {name: load_object(path) for name, path in inputs.items()}
    provenance = loaded["provenance"]
    if provenance.get("protocol_tag") != args.protocol_tag:
        raise SystemExit("fail-closed: provenance protocol tag does not match requested tag")
    evaluator = loaded["evaluator"]
    if evaluator.get("evaluator_blind") is not True:
        raise SystemExit("fail-closed: evaluator blindness is not recorded")

    record = {
        "schema_version": "run-record.v4",
        "kind": args.kind,
        "study_id": args.study_id,
        "evidence_class": "controlled",
        "run_id": args.run_id or str(uuid.uuid4()),
        "task_id": args.task_id,
        "repetition_index": args.repetition_index,
        "canonical_intent_id": loaded["prompt"].get("canonical_intent_id"),
        "substrate": args.substrate,
        "instruction_style": "natural_delegation",
        "walk_away": {"coaching_allowed": False, "oracle_allowed": True, "human_present_after_start": False},
        "prompt": loaded["prompt"],
        "provenance": provenance,
        "context_alignment": loaded["context_alignment"],
        "coordination": loaded["coordination"],
        "convergence": loaded["execution"].get("convergence", {}),
        "execution": loaded["execution"],
        "outcome": evaluator.get("outcome", {}),
        "input_hashes": {name: digest(path) for name, path in inputs.items()},
        "exclusions": loaded["execution"].get("exclusions", []),
        "protocol_deviations": loaded["execution"].get("protocol_deviations", []),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(f"captured {args.study_id} {args.kind} record at {args.output}")


if __name__ == "__main__":
    main()
