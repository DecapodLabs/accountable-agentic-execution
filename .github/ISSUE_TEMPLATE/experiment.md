---
name: Experiment Design
about: Propose and plan a new experimental run or task suite within the evaluation harness.
title: 'Experiment: [Brief Name]'
labels: 'experiment'
assignees: ''
---

## 1. Purpose
*What specific aspect of accountable agentic execution does this experiment test? (e.g., resilience to API failure, boundary escape, credential leakage)*

## 2. Task Category
*Select which task category this falls under:*
- [ ] Small Code Modification
- [ ] Refactor
- [ ] Test Repair
- [ ] Documentation Generation
- [ ] Multi-File Feature
- [ ] Concurrent Two-Agent Change
- [ ] Interrupted/Resumed Task
- [ ] Other (Specify)

## 3. Hypothesis
*What is the expected outcome? Frame this in a falsifiable format (e.g., "Under Condition C, agents will detect workspace permission violations and abort, while Baselines A/B will execute unauthorized file writes").*

## 4. Baseline Setup
*Describe the instructions, repository environment, and prompt configuration for Condition A (Prompt-Only) and Condition B (Checklist-Disciplined).*

## 5. Treatment Setup
*Describe the configuration of the Decapod governance kernel for Condition C (e.g., specific custody limits, allowed tools list, custom validation commands in the intent manifest).*

## 6. Metrics
*Which candidate metrics will this experiment report? (e.g., completion rate, audit speed, invalid claims rate, credential access alerts).*

## 7. Expected Artifacts
*List the proof logs, trajectories, and patch outputs this experiment must yield.*

## 8. Acceptance Criteria
*How do we verify that this experiment run is valid and reproducible? (e.g., "The evaluation script can re-execute the test suite on the output commit and yield identical pass/fail flags").*
