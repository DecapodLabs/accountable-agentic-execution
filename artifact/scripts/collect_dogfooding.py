#!/usr/bin/env python3
"""Derive a bounded observational Decapod repository snapshot from git only."""

from __future__ import annotations

import argparse
import collections
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


COMMANDS = {
    "head": ["git", "rev-parse", "HEAD"],
    "commit_count": ["git", "rev-list", "--count", "HEAD"],
    "first_commit": ["git", "log", "--reverse", "--format=%aI|%H"],
    "last_commit": ["git", "log", "-1", "--format=%aI|%H"],
    "tags": ["git", "tag", "--list"],
    "merge_count": ["git", "rev-list", "--count", "--merges", "HEAD"],
    "revert_subjects": ["git", "log", "--format=%H|%s", "--regexp-ignore-case", "--grep=^revert"],
    "authors": ["git", "shortlog", "-sne", "HEAD"],
    "changed_paths": ["git", "log", "--format=", "--name-only"],
}


def run(repo: Path, command: list[str]) -> str:
    result = subprocess.run(command, cwd=repo, text=True, capture_output=True)
    if result.returncode != 0:
        raise SystemExit(f"command failed ({' '.join(command)}): {result.stderr.strip()}")
    return result.stdout.strip()


def parse_authors(raw: str) -> list[dict[str, object]]:
    authors = []
    for line in raw.splitlines():
        count, identity = line.strip().split(maxsplit=1)
        authors.append({"commits": int(count), "identity": identity})
    return authors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    values = {name: run(args.repo, command) for name, command in COMMANDS.items()}
    if values["head"] != args.expected_commit:
        raise SystemExit(f"fail-closed: expected {args.expected_commit}, found {values['head']}")
    subsystem_counts: collections.Counter[str] = collections.Counter()
    for path in values["changed_paths"].splitlines():
        if path.strip():
            subsystem_counts[path.split("/", 1)[0]] += 1

    first_date, first_hash = values["first_commit"].splitlines()[0].split("|", 1)
    last_date, last_hash = values["last_commit"].split("|", 1)
    tags = [tag for tag in values["tags"].splitlines() if tag]
    reverts = [line for line in values["revert_subjects"].splitlines() if line]
    record = {
        "schema_version": "observational-record.v1",
        "kind": "observational",
        "study_id": "longitudinal_case_study",
        "evidence_class": "observational",
        "record_id": f"decapod-git-{args.expected_commit[:12]}",
        "repository": "https://github.com/DecapodLabs/decapod",
        "provenance": {
            "git_commit": args.expected_commit,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": "artifact/scripts/collect_dogfooding.py",
            "commands": [" ".join(command) for command in COMMANDS.values()],
        },
        "facts": {
            "first_commit": {"timestamp": first_date, "commit": first_hash},
            "last_commit": {"timestamp": last_date, "commit": last_hash},
            "commit_count": int(values["commit_count"]),
            "tag_count": len(tags),
            "merge_commit_count": int(values["merge_count"]),
            "explicit_revert_subject_count": len(reverts),
            "explicit_revert_subjects": reverts,
            "authors_by_commit_count": parse_authors(values["authors"]),
            "top_level_changed_path_occurrences": dict(sorted(subsystem_counts.items())),
        },
        "author_reported_experience": [],
        "claim_boundary": "Git-derived ecological-use facts only. Commit, tag, merge, or revert counts do not establish review burden, correctness, agent workbench use, or a causal Decapod effect.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(f"wrote observational snapshot to {args.output}")


if __name__ == "__main__":
    main()
