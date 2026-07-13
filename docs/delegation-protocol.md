# Delegation-Centered Empirical Protocol

This document defines the primary study that follows the current harness-validation phase. It is a prospective protocol, not a preregistration and not empirical evidence. The repository must record a frozen protocol tag before confirmatory execution.

## Research questions

- **RQ1 — Instruction burden:** At equivalent outcome quality, does Decapod reduce the initial procedural instruction required from the human?
- **RQ2 — Ongoing intervention:** Does Decapod reduce corrective follow-ups, unnecessary decisions, supervision time, and hands-on recovery work?
- **RQ3 — Natural delegation:** Under natural delegation prompts, does Decapod improve task success, intent fidelity, context discovery, and proof completeness relative to a conventional workflow?
- **RQ4 — Interaction:** Does Decapod reduce the performance penalty associated with less procedural prompting?
- **RQ5 — Governance reliability:** Does Decapod reduce invalid completion claims, improve interruption recovery, and reduce uncoordinated shared-workspace failures?
- **RQ6 — Cost and overhead:** What latency, token, tool-call, workspace, validation, proof, and reviewer overhead does governance introduce?

## Primary design

The primary experiment is a 2x2 factorial design:

| Execution substrate | Natural delegation | Procedural / micromanaged |
|---|---:|---:|
| Conventional agent workflow | cell CN | cell CP |
| Decapod-governed workflow | cell DN | cell DP |

Prompt variants are semantically matched to the same canonical intent and hidden acceptance rubric. Natural delegation states the outcome, motivation, meaningful constraints, priorities, and standard of completion. It does not enumerate implementation steps unless they are part of the intent. The procedural variant adds anticipated files, steps, commands, sequencing, and defensive instructions without changing the task requirement.

The former checklist condition is a secondary ablation only. It must not replace or obscure the factorial comparison.

## Hypotheses and failure conditions

The primary directional hypothesis is that a Decapod-governed agent receiving a natural delegation prompt will be non-inferior in outcome quality to a conventional agent receiving a procedural prompt, while requiring materially less human instruction and intervention. This remains exploratory until a defensible non-inferiority margin and power analysis are frozen; otherwise report effect estimates and uncertainty without a non-inferiority conclusion.

The delegation thesis is weakened if natural delegation with Decapod is no better than natural delegation without it, procedural prompting remains necessary for acceptable outcomes, governance merely relocates effort into setup, clarification burden increases, context resolution adds cost without improving intent fidelity, a simpler checklist is equivalent, or overhead outweighs the autonomy/reliability benefit.

## Human effort and effective autonomy

Record the underlying dimensions rather than an opaque autonomy score:

- initial prompt characters/tokens, explicit procedural steps, named paths, commands, tests, and implementation prescriptions;
- follow-up turns, corrective interventions, intervention duration, supervision time, clarification requests, and whether each clarification was necessary, avoidable, or correctly escalated;
- task outcome, intent fidelity, unintended scope, regressions, context discovered, proof completeness, invalid claims, recovery, review accuracy, and review time;
- model tokens, tool calls, elapsed time, workspace creation, validation, proof, and other governance overhead.

Analyze the **delegation frontier** as the relationship between human effort and outcome quality. Report the dimensions and uncertainty intervals separately.

## Current phase

The repository is in harness validation. The next stages are a labeled pilot, protocol freeze, confirmatory execution, and independent audit. No paid benchmark or model execution is authorized by this document.
