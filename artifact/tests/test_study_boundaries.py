#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "artifact" / "scripts" / "validate_study_separation.py"
FIXTURES = ROOT / "artifact" / "fixtures" / "fleet"


class StudyBoundaryTests(unittest.TestCase):
    def test_fleet_fixtures_are_conspicuously_synthetic(self) -> None:
        for path in FIXTURES.glob("*.json"):
            record = json.loads(path.read_text())
            self.assertEqual(record["kind"], "synthetic_fixture")
            self.assertEqual(record["evidence_class"], "controlled")
            self.assertTrue(record["run_id"].startswith("synthetic-"))
            self.assertIn("coordination", record)

    def test_mixed_studies_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            for path in FIXTURES.glob("*.json"):
                (target / path.name).write_bytes(path.read_bytes())
            result = subprocess.run(
                ["python3", str(VALIDATOR), "--input", str(target), "--study-id", "handoff_continuity", "--kind", "synthetic_fixture", "--evidence-class", "controlled"],
                text=True,
                capture_output=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("fail-closed", result.stderr)

    def test_single_study_passes(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            target = Path(raw)
            source = FIXTURES / "synthetic-handoff.json"
            (target / source.name).write_bytes(source.read_bytes())
            result = subprocess.run(
                ["python3", str(VALIDATOR), "--input", str(target), "--study-id", "handoff_continuity", "--kind", "synthetic_fixture", "--evidence-class", "controlled"],
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
