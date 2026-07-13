#!/usr/bin/env python3
"""Fail closed when a dataset mixes study, run-kind, or evidence-class boundaries."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--study-id", required=True)
    parser.add_argument("--kind", required=True)
    parser.add_argument("--evidence-class", choices=["controlled", "observational"], required=True)
    args = parser.parse_args()

    paths = sorted(args.input.glob("*.json"))
    if not paths:
        raise SystemExit("fail-closed: no records selected")
    for path in paths:
        record = json.loads(path.read_text())
        actual = (record.get("study_id"), record.get("kind"), record.get("evidence_class"))
        expected = (args.study_id, args.kind, args.evidence_class)
        if actual != expected:
            raise SystemExit(f"fail-closed: {path} has boundary {actual}, expected {expected}")
    print(f"validated {len(paths)} record(s) for {args.study_id}/{args.kind}/{args.evidence_class}")


if __name__ == "__main__":
    main()
