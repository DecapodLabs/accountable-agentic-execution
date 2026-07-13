# Empirical Evaluation Plan

The repository is in the harness-validation phase of a staged empirical program. No current synthetic value is an observation about an agent.

## 1. Primary factorial design

The experimental unit is one isolated agent run on one task, paired by task across conditions. The primary design is 2×2:

| Execution substrate | Instruction style |
| --- | --- |
| Conventional agent workflow | Natural delegation prompt |
| Conventional agent workflow | Procedural/micromanaged prompt |
| Decapod-governed workflow | Natural delegation prompt |
| Decapod-governed workflow | Procedural/micromanaged prompt |

The substrate, model, decoding settings, starting commit, task package, and hidden evaluator are held constant within a task block. Natural and procedural prompts are semantically matched projections of one canonical intent. Checklist-only remains an optional secondary ablation and is never substituted for the primary factorial comparison.

Natural delegation states the desired outcome, why it matters, meaningful constraints and priorities, and the standard of completion. It does not prescribe implementation details unless those details are themselves part of intent. The procedural variant adds anticipated steps, likely paths, commands, tests, sequencing, and defensive instructions.

## 2. Research questions and outcomes

RQ1 asks whether Decapod reduces initial procedural instruction at equivalent outcome quality. RQ2 asks whether it reduces follow-ups, corrective interventions, supervision time, unnecessary decisions, and recovery work. RQ3 asks whether it improves success, intent fidelity, relevant context discovery, and proof completeness under natural delegation. RQ4 tests the substrate × instruction-style interaction. RQ5 tests invalid completion claims, interruption recovery, and uncoordinated workspace failures. RQ6 reports governance cost.

Record, at minimum:

* prompt characters/tokens, explicit steps, named paths, commands, tests, and implementation prescriptions;
* follow-up turns, intervention count and duration, supervision time, clarification requests, and oracle classification of each clarification;
* hidden-evaluator success, intent fidelity, regressions, unintended scope expansion, discovered repository guidance, validation/proof completeness, and invalid completion claims;
* interruption recovery, reviewer accuracy/time when a separately approved reviewer protocol exists;
* model tokens, tool calls, elapsed time, workspace/proof/validation cost, and protocol deviations.

Report these dimensions directly as a delegation frontier rather than combining them into an unexplained score.

## 3. Reproducible task packages

Each task package contains canonical intent, motivation, priorities, constraints, open questions, escalation policy, hidden acceptance rubric, independent evaluator, matched prompts, a prewritten clarification oracle, starting repository commit, available project context, interruption/concurrency configuration, and exclusion criteria. Rubrics and evaluators are not exposed to the agent. Every run starts from a clean repository and isolated model context; all interventions and oracle responses are logged.

## 4. Staged execution

1. **Harness validation:** deterministic schema, evaluator, aggregation, and synthetic-fixture tests only.
2. **Pilot:** a small authorized set of real runs used to test difficulty, instrumentation, interventions, and evaluator correctness. Pilot records are excluded from confirmatory estimates.
3. **Protocol freeze:** tag a commit containing tasks, prompts, hypotheses, metrics, exclusions, evaluator logic, and statistical analysis plan.
4. **Confirmatory execution:** run the frozen protocol and deposit immutable raw evidence.
5. **Independent audit/reproduction:** a second reviewer checks provenance, analysis, and selected outcomes.

The current repository implements the task/run contracts, synthetic fixture path, fail-closed aggregation, independent task evaluator, and an explicitly authorized real-run capture wrapper. It does not fabricate pilot or empirical records and does not initiate paid model execution.

## 5. Statistical and protocol controls

Before collection, freeze the task-level experimental unit, task-block pairing, randomization and run ordering, model/context reset, repeated-run treatment, task clustering, primary/secondary outcomes, confidence intervals, effect sizes, multiplicity treatment, sensitivity analyses, governance-overhead reporting, and handling of failed, missing, timed-out, or excluded runs. A non-inferiority claim requires a justified margin and power analysis; otherwise report exploratory estimates. Human review is secondary until reviewer consent, blinding where possible, correctness checks, and ethics documentation exist.

## 6. Provenance boundary

Every real record identifies data kind (`pilot` or `empirical`), task and prompt variant, exact prompt, model/provider/version/settings, seed or request ID, agent/runtime and Decapod versions, target commit, environment, permissions, timestamps, usage, interventions, workspace/proof/validation configuration, raw outcome, independent evaluation, exclusions, crashes, deviations, and links to generated tables and figures. `synthetic_fixture` records cannot be aggregated into pilot or empirical results.
