# Statistical Analysis Plan

This is a prospective analysis plan for the delegation study. It is not frozen until the repository records a protocol tag/commit and the final task cohort, evaluator logic, exclusions, and margins are fixed.

## Experimental unit and pairing

The experimental unit is one task-by-cell run from a clean starting commit and isolated model context. Runs are paired or blocked by task; repeated runs are clustered by task and model/configuration. Run ordering is randomized within task and execution capacity.

## Primary outcomes

1. Hidden-evaluator outcome quality and intent fidelity.
2. Human procedural instruction burden.
3. Ongoing human intervention burden.

Secondary outcomes include invalid completion claims, recovery, proof completeness, context discovery, regressions, scope expansion, review accuracy/time, and governance overhead.

## Estimation

Report cell-level distributions, paired differences, effect sizes, and confidence intervals. Model the substrate, instruction style, and their interaction with task-level clustering. Do not treat repeated runs as independent observations without accounting for task clustering.

## Missingness and exclusions

Failed, timed-out, crashed, and incomplete runs remain in the denominator for operational reliability outcomes. Exclusions require a recorded reason, timestamp, protocol version, and reviewer. Missing outcome data are not converted to success or silently dropped.

## Non-inferiority

The non-inferiority margin is not yet set. Confirmatory non-inferiority claims are prohibited until the margin is justified from domain requirements, pilot variance, and a power analysis. Until then, label the study exploratory/pilot and report uncertainty without a non-inferiority conclusion.

## Multiplicity and sensitivity

Declare one primary outcome family before execution, state multiplicity treatment for secondary outcomes, and run sensitivity analyses for exclusions, task difficulty, model configuration, and alternative intent-fidelity scoring.
