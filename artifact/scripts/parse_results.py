#!/usr/bin/env python3
"""Fail-closed aggregation for synthetic, pilot, or empirical run records."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ALLOWED_KINDS = {"synthetic_fixture", "pilot", "empirical"}


def bootstrap_ci(data: list[float], replicates: int = 1000) -> tuple[float, float]:
    if not data:
        return 0.0, 0.0
    random.seed(42)
    means = [sum(random.choice(data) for _ in data) / len(data) for _ in range(replicates)]
    means.sort()
    return means[int(replicates * 0.025)], means[int(replicates * 0.975)]


def load_records(root: Path) -> list[dict[str, object]]:
    records = []
    for folder in (root / "baselines", root / "decapod-runs", root / "runs"):
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.json")):
            record = json.loads(path.read_text())
            record["_path"] = str(path)
            records.append(record)
    return records


def validate_kind(records: list[dict[str, object]], requested_kind: str) -> None:
    if not records:
        raise SystemExit("No run records found; refusing to generate an empty aggregate.")
    kinds = {record.get("kind") for record in records}
    if kinds - ALLOWED_KINDS:
        raise SystemExit(f"Unknown run kind(s): {sorted(kinds - ALLOWED_KINDS)}")
    if kinds != {requested_kind}:
        raise SystemExit(f"fail-closed: requested kind={requested_kind}, found kinds={sorted(kinds)}")
    for record in records:
        if record.get("schema_version") not in {"run-record.v2", "run-record.v3"}:
            raise SystemExit(f"Unsupported schema in {record['_path']}")
        if requested_kind in {"pilot", "empirical"}:
            provenance = record.get("provenance", {})
            if provenance.get("task_commit") in {None, "", "synthetic-fixture-no-repository"}:
                raise SystemExit(f"Missing real task provenance in {record['_path']}")
            model = provenance.get("model", {})
            if model.get("identifier") in {None, "", "none"}:
                raise SystemExit(f"Missing model provenance in {record['_path']}")


def legacy_metrics(records: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    """Aggregate only the retained legacy three-condition synthetic fixture."""
    results: dict[str, dict[str, object]] = {}
    for condition in ("A", "B", "C"):
        selected = [r for r in records if r.get("synthetic_parameters", {}).get("condition") == condition]
        if not selected:
            continue
        outcome = [r["outcome"] for r in selected]
        successes = [float(o["task_success"]) for o in outcome]
        failures = [o for o in outcome if not o["task_success"]]
        invalid = [float(o["invalid_completion_claim"]) for o in failures]
        accuracy = [float(o["validation_accuracy"]) for o in outcome]
        recovery = [float(o["interruption_recovery_success"]) for o in outcome]
        review = [float(o["human_review_time_seconds"]) for o in outcome]
        results[condition] = {
            "kind": "synthetic_fixture",
            "runs_count": len(selected),
            "task_completion_rate": {"mean": round(sum(successes) / len(successes) * 100, 1), "ci": [round(x * 100, 1) for x in bootstrap_ci(successes)]},
            "invalid_success_claims": {"mean": round(sum(invalid) / len(invalid) * 100, 1) if invalid else 0.0, "ci": [round(x * 100, 1) for x in bootstrap_ci(invalid)]},
            "validation_accuracy": {"mean": round(sum(accuracy) / len(accuracy) * 100, 1), "ci": [round(x * 100, 1) for x in bootstrap_ci(accuracy)]},
            "interruption_recovery": {"mean": round(sum(recovery) / len(recovery) * 100, 1), "ci": [round(x * 100, 1) for x in bootstrap_ci(recovery)]},
            "concurrent_conflicts_sum": sum(int(o["concurrent_conflicts"]) for o in outcome),
            "human_review_time": {"mean": round(sum(review) / len(review), 1), "ci": [round(x, 1) for x in bootstrap_ci(review)]},
        }
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, default=Path("artifact"))
    parser.add_argument("--output-root", type=Path, default=Path("artifact/results"))
    parser.add_argument("--kind", choices=sorted(ALLOWED_KINDS), default="synthetic_fixture")
    args = parser.parse_args()
    records = load_records(args.input_root)
    validate_kind(records, args.kind)
    if args.kind == "synthetic_fixture":
        results = legacy_metrics(records)
    else:
        raise SystemExit("Real aggregation is intentionally not implemented by the legacy metric path; use the frozen statistical analysis plan.")
    args.output_root.mkdir(parents=True, exist_ok=True)
    (args.output_root / "summary.json").write_text(json.dumps({"kind": args.kind, "results": results}, indent=2) + "\n")
    with (args.output_root / "summary.csv").open("w") as output:
        output.write("kind,condition,runs,completion_mean,invalid_claims_mean,validation_accuracy_mean,recovery_mean,conflicts_sum,review_time_mean\n")
        for condition, result in results.items():
            output.write(f"{args.kind},{condition},{result['runs_count']},{result['task_completion_rate']['mean']},{result['invalid_success_claims']['mean']},{result['validation_accuracy']['mean']},{result['interruption_recovery']['mean']},{result['concurrent_conflicts_sum']},{result['human_review_time']['mean']}\n")
    print(f"Aggregated {len(records)} {args.kind} records into {args.output_root / 'summary.json'}.")


if __name__ == "__main__":
    main()
