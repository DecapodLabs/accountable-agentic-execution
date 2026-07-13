#!/usr/bin/env python3
"""Capture one explicitly authorized walk-away pilot or empirical run.

The wrapper does not select a model, grant credentials, or authorize a cohort.
For real runs it fails closed unless the caller supplies the event log,
intervention log, context manifest, evaluator result, and protocol tag needed
to reconstruct the pre-inference and convergence claims.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run(command: str, cwd: Path, timeout: int) -> dict[str, object]:
    started = time.monotonic()
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True, timeout=timeout)
        return {"command": command, "argv": shlex.split(command), "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr, "elapsed_seconds": round(time.monotonic() - started, 3), "timed_out": False}
    except subprocess.TimeoutExpired as exc:
        return {"command": command, "argv": shlex.split(command), "exit_code": None, "stdout": exc.stdout or "", "stderr": exc.stderr or "", "elapsed_seconds": round(time.monotonic() - started, 3), "timed_out": True}


def git_value(cwd: Path, args: list[str]) -> str | None:
    result = subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else None


def read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"fail-closed: invalid JSON at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"fail-closed: expected JSON object at {path}")
    return value


def read_events(path: Path) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    try:
        lines = path.read_text().splitlines()
    except OSError as exc:
        raise SystemExit(f"fail-closed: cannot read event log {path}: {exc}") from exc
    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"fail-closed: invalid JSONL at {path}:{line_number}: {exc}") from exc
        if isinstance(event, dict):
            events.append(event)
    return events


def count_events(events: list[dict[str, object]], *names: str) -> int:
    return sum(1 for event in events if event.get("event") in names or event.get("type") in names)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-dir", type=Path, required=True)
    parser.add_argument("--target-dir", type=Path, required=True)
    parser.add_argument("--substrate", choices=["conventional", "decapod_governed"], required=True)
    parser.add_argument("--instruction-style", choices=["natural_delegation", "procedural"], required=True)
    parser.add_argument("--kind", choices=["pilot", "empirical"], required=True)
    parser.add_argument("--repetition-index", type=int, required=True)
    parser.add_argument("--canonical-intent-id", required=True)
    parser.add_argument("--command", required=True, help="approved agent/runtime command")
    parser.add_argument("--evaluator-command", required=True, help="independent evaluator command")
    parser.add_argument("--evaluator-result", type=Path, required=True, help="blind evaluator JSON written by evaluator-command")
    parser.add_argument("--event-log", type=Path, required=True, help="agent event JSONL")
    parser.add_argument("--intervention-log", type=Path, required=True, help="frozen-oracle/intervention JSON")
    parser.add_argument("--context-manifest", type=Path, required=True, help="pre-inference context manifest JSON")
    parser.add_argument("--model-provider", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-version", required=True)
    parser.add_argument("--decoding", default="{}")
    parser.add_argument("--request-id")
    parser.add_argument("--seed")
    parser.add_argument("--agent-version", required=True)
    parser.add_argument("--decapod-version", required=True)
    parser.add_argument("--protocol-id", required=True)
    parser.add_argument("--protocol-tag", required=True)
    parser.add_argument("--confirm-real-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.confirm_real_run:
        raise SystemExit("fail-closed: pass --confirm-real-run only after pilot/empirical authority is approved")
    task = read_json(args.task_dir / "task.json")
    for path in (args.event_log, args.intervention_log, args.context_manifest):
        if not path.exists():
            raise SystemExit(f"fail-closed: required provenance input is missing: {path}")
    variant_path = args.task_dir / "prompts" / ("natural_delegation.md" if args.instruction_style == "natural_delegation" else "procedural.md")
    prompt = variant_path.read_text()
    task_commit = git_value(args.target_dir, ["rev-parse", "HEAD"])
    started_at = now()
    agent_result = run(args.command, args.target_dir, args.timeout)
    evaluator_result = run(args.evaluator_command, args.target_dir, args.timeout)
    if not args.evaluator_result.exists():
        raise SystemExit(f"fail-closed: blind evaluator did not produce {args.evaluator_result}")
    evaluator = read_json(args.evaluator_result)
    events = read_events(args.event_log)
    interventions = read_json(args.intervention_log)
    context_manifest = read_json(args.context_manifest)
    ended_at = now()
    record = {
        "schema_version": "run-record.v4", "kind": args.kind, "study_id": "walk_away_alignment", "evidence_class": "controlled", "run_id": str(uuid.uuid4()), "task_id": task["task_id"],
        "repetition_index": args.repetition_index, "canonical_intent_id": args.canonical_intent_id,
        "substrate": args.substrate, "instruction_style": args.instruction_style,
        "walk_away": {"coaching_allowed": False, "oracle_allowed": True, "human_present_after_start": False},
        "prompt": {"text": prompt, "characters": len(prompt), "approx_tokens": max(1, len(prompt) // 4), "procedural_steps": prompt.count(". "), "named_paths": sum(1 for token in ["app.py", "test_app.py"] if token in prompt), "named_commands": sum(1 for token in ["python", "pytest", "ruff", "mypy"] if token in prompt), "named_tests": prompt.lower().count("test"), "implementation_prescriptions": prompt.lower().count("add ")},
        "provenance": {"protocol_id": args.protocol_id, "protocol_tag": args.protocol_tag, "task_commit": task_commit, "model": {"provider": args.model_provider, "identifier": args.model_id, "version": args.model_version, "decoding": json.loads(args.decoding), "request_id": args.request_id, "seed": args.seed}, "runtime": {"agent_version": args.agent_version, "decapod_version": args.decapod_version}, "timestamps": {"started_at": started_at, "ended_at": ended_at, "elapsed_seconds": agent_result["elapsed_seconds"]}, "environment": {"host": os.uname().nodename, "python": os.sys.version, "container": os.path.exists("/.dockerenv")}, "configuration": {"tool_permissions": "caller-supplied", "workspace": str(args.target_dir)}},
        "context_alignment": context_manifest,
        "convergence": {"event_count": len(events), "model_requests": count_events(events, "model_request", "inference_request"), "tool_calls": count_events(events, "tool_call"), "repository_searches": count_events(events, "repository_search", "search"), "files_opened_before_first_edit": context_manifest.get("files_opened_before_first_edit"), "failed_attempts": count_events(events, "failed_attempt", "execution_failure"), "validation_failure_cycles": count_events(events, "validation_failure", "test_failure", "lint_failure"), "redundant_tool_calls": context_manifest.get("redundant_tool_calls"), "substantial_rewrites": context_manifest.get("substantial_rewrites"), "elapsed_to_acceptable_seconds": evaluator.get("elapsed_to_acceptable_seconds")},
        "execution": {"agent": agent_result, "independent_evaluator": evaluator_result, "evaluator_result": evaluator, "evaluator_blind": True, "git_head_after": git_value(args.target_dir, ["rev-parse", "HEAD"]), "diff_sha256": hashlib.sha256((git_value(args.target_dir, ["diff", "--binary"]) or "").encode()).hexdigest()},
        "interventions": interventions,
        "exclusions": [], "protocol_deviations": [],
        "outcome": {"task_success": bool(evaluator.get("task_success", evaluator_result["exit_code"] == 0)), "intent_fidelity": evaluator.get("intent_fidelity"), "invalid_completion_claim": evaluator.get("invalid_completion_claim"), "proof_completeness": evaluator.get("proof_completeness")},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(f"captured {args.kind} run {record['run_id']} to {args.output}")


if __name__ == "__main__":
    main()
