# One-Shot Walk-Away Delegation Protocol

This prospective protocol tests the central delegation hypothesis: can a human provide one sufficiently complex outcome-oriented software request, walk away, and receive an independently acceptable result because Decapod aligns the agent with the human's intent before implementation inference? It is not a preregistration and is not empirical evidence until a frozen tag exists.

## Mechanism and primary comparison

The human expresses the desired outcome in one natural delegation prompt. Before implementation inference, Decapod resolves the applicable constitution, repository state, capabilities, constraints, prior decisions, standards, unresolved questions, escalation rules, and proof expectations. The agent then executes in the governed custody and validation corridor. The underlying model is unchanged; Decapod is hypothesized to make the agent system operationally more knowledgeable and contextually aligned by supplying better selected, authoritative context at decision time.

The primary comparison uses the identical natural prompt, model, runtime, repository commit, tools, timeout, hidden rubric, evaluator, and clean-context reset:

| Cell | Substrate | Prompt | Human after start |
| --- | --- | --- | --- |
| CN | Conventional agent | Natural delegation | Walk away; no coaching |
| DN | Decapod-governed agent | The identical natural delegation | Walk away; no coaching |

The conventional run receives ordinary repository/tool access without Decapod-mediated constitution resolution, orientation, task claim, context capsule, custody workflow, or proof corridor. The governed run receives those configured mechanisms. Treatment context must not include hidden acceptance criteria unavailable to control.

Clarifications follow a frozen oracle. Prefer tasks resolvable from the prompt and repository. If clarification is necessary, record the request and the prewritten response; do not provide ad hoc corrective direction.

## Primary outcome

The primary outcome is independent fidelity of the final repository state to the complete human/team intent under zero or tightly bounded post-prompt intervention. The hidden rubric scores functional correctness, explicit requirements, implicit project invariants, architecture and conventions, applicable standards, regression avoidance, scope discipline, validation, evidence, and readiness for human acceptance.

## Convergence and alignment measures

Capture model inference requests, input/output tokens, tool calls, repository searches, files opened before the first implementation edit, time to first relevant implementation action, failed attempts, redundant calls, compiler/test/lint/validation failure cycles, substantial rewrites, clarification requests, unresolved questions, elapsed time to acceptable completion, premature completion claims, and cost where available. “Inference hits” is informal language only; analysis uses these defined quantities.

For the pre-inference mechanism, record each supplied context item, authority source, rationale, hash, size, selected/excluded status, context-resolution latency, and total context size. An independent audit labels each item necessary, useful, irrelevant, redundant, contradictory, or harmful. More context is not assumed to be better.

## Hypotheses

- **H1 — Outcome fidelity:** DN more often satisfies the hidden intent rubric than CN.
- **H2 — Convergence efficiency:** DN requires fewer model requests, failed cycles, redundant operations, and substantial rewrites before acceptable completion.
- **H3 — Contextual alignment:** DN identifies and applies more relevant architecture, conventions, and standards without those details being enumerated in the prompt.
- **H4 — Human absence tolerance:** DN more often completes without clarification or corrective intervention.
- **H5 — Evidence quality:** DN produces more complete validation, provenance, and review evidence.
- **H6 — Cost boundary:** Any gain is evaluated against context-resolution, workspace, validation, token, latency, and operational overhead.

## Secondary ablation

Natural-versus-procedural prompting remains a secondary 2x2 ablation:

| Substrate | Natural | Procedural |
| --- | --- | --- |
| Conventional | CN | CP |
| Decapod-governed | DN | DP |

The procedural prompt is semantically matched but additionally names anticipated files, steps, commands, tests, sequencing, and defensive instructions. It must not change canonical intent or the hidden rubric. A former checklist-only condition is optional and clearly labeled secondary.

## Failure conditions and task complexity

The thesis is weakened if DN does not improve fidelity, does not reduce failed or redundant cycles, increases cost without improving results, supplies irrelevant or harmful context, still requires regular human correction, is matched by CN at equal or lower effort, benefits only from leaked acceptance information, improves proof without task quality, or shifts supervision into extensive upfront configuration.

Tasks must require interacting reasoning: architecture discovery, multi-layer changes, compatibility, security/persistence/API/concurrency or operational standards, validation, and scope discipline. Trivial fixture tasks are harness tests, not empirical-eligible tasks.

## Stages

1. Harness validation uses deterministic tests and synthetic fixtures only.
2. A small labeled pilot tests instrumentation, evaluator blindness, oracle behavior, resets, and provenance; it is excluded from confirmatory estimates.
3. Protocol freeze records tasks, paired prompts, rubrics, context manifests, outcomes, exclusions, analysis, and the exact model/runtime in a tagged commit.
4. Confirmatory execution runs the frozen primary cohort and any separately activated secondary ablation.
5. Independent audit/reproduction checks the provenance chain and selected outcomes.

No synthetic, pilot, or unmeasured value may be presented as confirmatory evidence.

This remains Study A and the paper's primary controlled experiment. Cross-workbench handoff, concurrent fleets, tool switching, and longitudinal dogfooding are separately bounded in `docs/fleet-coherence-protocol.md`; their records and outcomes cannot silently enter this study's estimates.
