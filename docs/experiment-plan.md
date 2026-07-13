# Empirical Evaluation Plan

This repository is in harness validation. The primary study tests one-shot walk-away delegation, not prompt length alone. Synthetic fixtures are harness artifacts and cannot support treatment claims.

This protocol remains a prospective draft. As Decapod develops, experiments, hypotheses, conditions, instrumentation, and sample plans may change so they continue to test implemented mechanisms rather than stale assumptions. Each pre-freeze change must be versioned and justified. After protocol freeze, a material change requires a new protocol version or an explicit deviation; confirmatory rules cannot be revised in response to observed outcomes.

## 1. Primary study

The experimental unit is an isolated run of one complex task from one clean starting commit and fresh model context. The primary paired comparison is:

| Cell | Substrate | Prompt |
| --- | --- | --- |
| CN | Conventional agent workflow | Natural delegation |
| DN | Decapod-governed workflow | Identical natural delegation |

The same model/version, decoding, runtime, repository, tools, timeout, hidden rubric, evaluator, and reset procedure are used in both cells. CN receives ordinary repository/tool access without Decapod-mediated context resolution, orientation, task claim, capsule, custody, or proof corridor. DN receives the configured Decapod context and execution corridor. No post-start coaching is allowed.

The natural prompt states outcome, motivation, meaningful constraints/priorities, and completion standard. It does not prescribe a solution. A frozen clarification oracle is used only when necessary. The optional secondary ablation crosses both substrates with natural and semantically matched procedural prompts.

## 2. Task requirements

Tasks must require several interacting forms of reasoning: architecture discovery, multi-file or multi-layer changes, compatibility, project conventions, an applicable security/persistence/API/concurrency/operational standard, validation, and scope discipline. Each package contains canonical intent, motivation, constraints, open questions, escalation policy, hidden rubric, independent evaluator, paired prompts, oracle, starting commit, available context, interruption/concurrency configuration, and exclusions. The hidden rubric is unavailable to the agent.

## 3. Outcomes

The primary outcome is independent final-state fidelity to the complete intent: functional correctness, explicit requirements, implicit invariants, architecture/conventions, applicable standards, regression avoidance, scope discipline, validation/evidence completeness, and acceptance readiness.

Convergence outcomes are model requests, input/output tokens, tool calls, repository searches, files opened before first edit, time to first relevant action, failed attempts, redundant calls, compiler/test/lint/validation failure cycles, reversals or substantial rewrites, clarification requests, unresolved questions, time to acceptable completion, premature claims, and cost. Human absence outcomes are clarification, corrective intervention, and completion without coaching. Report validation, provenance, and governance overhead separately.

## 4. Mechanism instrumentation

For each supplied context item, record authority source, authority type, selection rationale, content hash, size, selected/excluded status, and provenance. Record selected constitutional nodes, project specifications, capability overlays, constraints/negative requirements, standards, prior decisions, excluded context, total context size, and resolution latency. An independent context-relevance audit labels every item necessary, useful, irrelevant, redundant, contradictory, or harmful. More context is not presumed better.

## 5. Stages and provenance

1. Harness validation: deterministic tests and synthetic fixtures.
2. Pilot: a small labeled set across CN and DN, optionally including the secondary cells, to test capture, blindness, oracle behavior, resets, evaluator correctness, and provenance. Pilot is excluded from confirmatory analysis.
3. Protocol freeze: tag exact tasks, prompts, hidden rubrics/evaluators, context manifests, outcomes, exclusions, randomization, analysis, and model/runtime.
4. Confirmatory execution: run the frozen cohort without ad hoc retries or assistance.
5. Independent audit/reproduction: validate the chain from protocol tag through task, prompt, execution, repository state, evaluator, aggregate, and paper artifact.

Every record identifies `synthetic_fixture`, `pilot`, or `empirical`; exact prompt/runtime/model metadata; repository and Decapod commits; environment and permissions; events, interventions, oracle responses; context manifest; evaluator result; exclusions/deviations; and immutable hashes. Synthetic and pilot records fail closed in confirmatory aggregation.

## 6. Analysis

Report paired task-level contrasts, cell distributions, uncertainty intervals, effect sizes, substrate effect, and the substrate × prompt-style interaction for the secondary design. Cluster repeated runs by task and state denominators for failures, timeouts, and exclusions. Do not treat “inference hits” as a metric; use the defined request, token, tool-loop, retry, and failure-cycle measures. Do not claim non-inferiority until a margin and power analysis are frozen.

## 7. Falsification

The thesis is weakened if DN does not improve independent fidelity, does not reduce failed/redundant cycles, adds cost without better results, supplies irrelevant or harmful context, still needs regular correction, is matched by CN at equal or lower effort, benefits from hidden rubric leakage, improves proof without task quality, or relocates supervision into configuration.

## 8. Prospective fleet-coherence studies

Study A remains the primary CN-versus-DN walk-away comparison above. The following extensions use separate schemas, task packages, analyses, and headlines:

| Study | Question | Credible control | Decapod treatment |
| --- | --- | --- | --- |
| B — handoff continuity | Can a clean receiving session continue with less reconstruction? | repository, branch, git history, task description, frozen structured handoff | same artifacts plus approved task handoff, durable task/context/trajectory/proof references |
| C — concurrent fleet | Can agents solve similar yet distinct concurrent problems with less duplication and integration repair? | separate branches/worktrees and normal issue descriptions | same task graph plus claims, semantic-overlap records, labels/categories, dependencies, context, events, proof/publication paths |
| D — tool switching | Does project state survive a workbench change without transcript replay? | Study B control across a frozen workbench pair | Study B treatment across the same pair |
| E — longitudinal case study | How extensively has Decapod been exercised in its own repository? | not a treatment comparison | repository-derived facts and separately labeled author testimony |

Studies B–D hold the model fixed before adding heterogeneous models as an external-validity extension. They capture source/destination session, workbench, and model; ownership transfer; handoff payload; context manifests; preserved/lost questions, dependencies, and proof state; duplicate reads/searches/commands/attempts; claim and workspace conflicts; integration and publication outcomes; human briefing; cost; and deviations.

Study C is the central fleet-coherence test. Its task graph deliberately includes independent, dependent, and similar-but-distinct work that shares architecture, modules, tests, or publication boundaries without being duplicate tasks. It distinguishes duplicate task identity from semantic overlap, and direct mutation collisions from textual merge conflicts, semantic integration failures, and missing post-integration proof. Study E is `observational` and can never be aggregated with controlled pilot or empirical records. See `docs/fleet-coherence-protocol.md`.

## 9. Fleet research questions

- RQ7: cross-agent continuity and reorientation cost.
- RQ8: duplicate-work prevention through custody.
- RQ9: fleet integration and deferred-conflict risk.
- RQ10: workbench/provider-independent continuation.
- RQ11: project-owned versus conversation-owned memory.
- RQ12: net coordination cost including governance overhead.
