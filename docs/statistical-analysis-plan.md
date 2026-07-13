# Statistical Analysis Plan

This prospective plan is not frozen until a protocol tag records the final task cohort, prompts, evaluators, exclusions, model/runtime, and analysis rules.

## Estimand and primary comparison

The primary estimand is the paired within-task difference in independently scored intent fidelity between Decapod-governed natural delegation (DN) and conventional natural delegation (CN), under identical prompt and execution inputs except for the Decapod context/corridor. The primary outcome is final-state fidelity, not prompt length. The key human-absence outcome is acceptable completion without clarification or corrective coaching.

## Mechanism and secondary outcomes

Convergence outcomes are model requests, tokens, tool calls, repository searches, pre-edit files opened, time to first relevant action, failed attempts, redundant operations, validation failure cycles, reversals/re-writes, clarification requests, unresolved questions, time to acceptable completion, premature completion claims, and cost. Context alignment outcomes include item-level relevance labels and context size/latency. Secondary outcomes include proof/validation completeness, invalid completion claims, recovery, regressions, scope expansion, and governance overhead. Human effort is reported as dimensions and a delegation-frontier plot, not an unexplained composite.

## Design and estimation

Runs are paired or blocked by task and repeated runs are clustered by task. Report cell distributions, paired differences, effect sizes, and confidence intervals. For the secondary 2x2, estimate substrate, prompt-style, and interaction effects with task-level clustering. Randomize run order within task blocks and reset repository/model context between runs.

Failed, timed-out, crashed, clarification-blocked, and incomplete runs remain in operational-reliability denominators. Exclusions require reason, timestamp, protocol tag, and reviewer; never silently convert missing outcomes to success or drop them. Sensitivity analyses cover exclusions, task difficulty, alternate fidelity scoring, and runtime nondeterminism.

## Non-inferiority and multiplicity

No non-inferiority claim is permitted until a domain-justified margin and power analysis are frozen before confirmatory execution. Otherwise describe the study as exploratory/pilot and report estimates with uncertainty. Declare the primary outcome family before collection and state multiplicity treatment for secondary outcomes.

## Prospective fleet-study analyses

Studies B–D are separate outcome families and do not enter Study A's primary estimate. Each requires its own frozen task/checkpoint blocks, sample-size justification, retry policy, and multiplicity treatment.

- **Study B:** pair by task, checkpoint, repetition, source/destination workbench, and (where possible) model. Estimate differences in reorientation calls/time, duplicate exploration, preserved constraints, final fidelity, proof continuity, and human briefing. Stratify rather than pool same-model and heterogeneous-model transfers.
- **Study C:** treat the task graph/repetition as the cluster. Report duplicate starts, claim conflicts, direct collisions, textual merge conflicts, semantic integration failures, repair effort, integrated fidelity, publication success, and wall-clock/resource cost. Do not combine direct-collision and integration-failure outcomes.
- **Study D:** use Study B estimands with workbench pair as a declared factor. Version drift and provider failures remain in denominators or the frozen infrastructure-failure stratum.
- **Study E:** descriptive observational statistics only. No controlled effect estimate, hypothesis test, or pooling with Studies A–D is permitted.

Study-specific aggregation requires one `study_id`, one run kind, and one evidence class. Sensitivity analyses must include alternate duplicate-operation adjudication, stale-context exclusions, failed handoffs, integration-gate availability, and total governance/configuration cost.
