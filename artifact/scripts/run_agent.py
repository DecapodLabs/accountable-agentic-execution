#!/usr/bin/env python3
"""Capture one explicitly authorized pilot/empirical agent run.

This wrapper executes a supplied command; it does not select a model, grant
credentials, or authorize a benchmark. The caller must provide an approved
task package, model metadata, and an independent evaluator command.
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-dir", type=Path, required=True)
    parser.add_argument("--target-dir", type=Path, required=True)
    parser.add_argument("--substrate", choices=["conventional", "decapod_governed"], required=True)
    parser.add_argument("--instruction-style", choices=["natural_delegation", "procedural"], required=True)
    parser.add_argument("--kind", choices=["pilot", "empirical"], required=True)
    parser.add_argument("--command", required=True, help="approved agent/runtime command")
    parser.add_argument("--evaluator-command", required=True, help="independent evaluator command")
    parser.add_argument("--model-provider", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-version", required=True)
    parser.add_argument("--agent-version", required=True)
    parser.add_argument("--decapod-version", required=True)
    parser.add_argument("--protocol-id", required=True)
    parser.add_argument("--confirm-real-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not args.confirm_real_run:
        raise SystemExit("fail-closed: pass --confirm-real-run only after pilot/empirical authority is approved")
    task = json.loads((args.task_dir / "task.json").read_text())
    variant_path = args.task_dir / "prompts" / ("natural_delegation.md" if args.instruction_style == "natural_delegation" else "procedural.md")
    prompt = variant_path.read_text()
    task_commit = git_value(args.target_dir, ["rev-parse", "HEAD"])
    started_at = now()
    agent_result = run(args.command, args.target_dir, args.timeout)
    evaluator_result = run(args.evaluator_command, args.target_dir, args.timeout)
    ended_at = now()
    record = {
        "schema_version": "run-record.v2", "kind": args.kind, "run_id": str(uuid.uuid4()), "task_id": task["task_id"],
        "protocol_id": args.protocol_id, "substrate": args.substrate, "instruction_style": args.instruction_style,
        "prompt": {"text": prompt, "characters": len(prompt), "approx_tokens": max(1, len(prompt) // 4), "procedural_steps": prompt.count(". "), "named_paths": sum(1 for token in ["app.py", "test_app.py"] if token in prompt), "named_commands": sum(1 for token in ["python", "pytest", "ruff", "mypy"] if token in prompt), "named_tests": prompt.lower().count("test"), "implementation_prescriptions": prompt.lower().count("add ")},
        "provenance": {"protocol_id": args.protocol_id, "task_commit": task_commit, "model": {"provider": args.model_provider, "identifier": args.model_id, "version": args.model_version, "decoding": {}}, "runtime": {"agent_version": args.agent_version, "decapod_version": args.decapod_version}, "timestamps": {"started_at": started_at, "ended_at": ended_at, "elapsed_seconds": agent_result["elapsed_seconds"]}, "environment": {"host": os.uname().nodename, "python": os.sys.version, "container": os.path.exists("/.dockerenv")}, "configuration": {"tool_permissions": "caller-supplied", "workspace": str(args.target_dir)}},
        "execution": {"agent": agent_result, "independent_evaluator": evaluator_result, "git_head_after": git_value(args.target_dir, ["rev-parse", "HEAD"]), "diff_sha256": hashlib.sha256((git_value(args.target_dir, ["diff", "--binary"]) or "").encode()).hexdigest()},
        "interventions": [], "exclusions": [], "protocol_deviations": [],
        "outcome": {"task_success": evaluator_result["exit_code"] == 0, "intent_fidelity": None, "invalid_completion_claim": None, "proof_completeness": evaluator_result["exit_code"] == 0},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(f"captured {args.kind} run {record['run_id']} to {args.output}")


if __name__ == "__main__":
    main()
