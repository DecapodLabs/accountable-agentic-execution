# Research Claims and Falsifiability Ledger

This ledger bounds the empirical claims made by the paper and identifies observations that would weaken them.

## 1. Core thesis

Intent is the human or team’s desired outcome, motivation, constraints, priorities, unresolved questions, and standard of completion. A prompt is an initial and often incomplete expression of that intent. Plans, todos, specifications, context capsules, proof hooks, and acceptance rubrics are governed representations, projections, or resolutions of intent; they are not its source of authority.

Decapod is hypothesized to increase effective agent autonomy at a fixed level of human instruction, or reduce human instruction and intervention burden at a fixed level of outcome quality. The underlying language model is unchanged. The governed system may behave more capably because it can recover relevant context, preserve intent, coordinate execution, and verify its work.

## 2. Research questions and hypotheses

* **RQ1 — Instruction burden:** At equivalent outcome quality, does Decapod reduce initial procedural instruction?
* **RQ2 — Ongoing intervention:** Does Decapod reduce corrective follow-ups, unnecessary decisions, supervision time, and hands-on recovery work?
* **RQ3 — Natural delegation:** Under outcome-oriented prompts, does Decapod improve task success, intent fidelity, context discovery, and proof completeness?
* **RQ4 — Interaction:** Does Decapod reduce the performance penalty associated with less procedural prompting?
* **RQ5 — Governance reliability:** Does Decapod reduce invalid completion claims, improve interruption recovery, and reduce uncoordinated workspace failures?
* **RQ6 — Cost and overhead:** What latency, token, tool-call, workspace, validation, proof, and reviewer overhead does governance introduce?

Primary hypothesis: a Decapod-governed agent receiving a natural delegation prompt will be non-inferior in outcome quality to a conventional agent receiving a procedural prompt, while requiring materially less human instruction and intervention. The non-inferiority margin, power analysis, and analysis population must be frozen before confirmatory execution; until then this is a pilot/exploratory hypothesis, not a demonstrated result.

The delegation frontier is analyzed as the relationship between human effort and outcome quality. The study reports underlying dimensions rather than inventing an opaque composite score.

## 3. Primary design

The primary experiment is a 2×2 factorial design with a matched canonical intent and hidden evaluator for each task:

| Execution substrate | Natural delegation | Procedural/micromanaged |
| --- | --- | --- |
| Conventional workflow | primary cell | primary cell |
| Decapod-governed workflow | primary cell | primary cell |

Natural prompts state the outcome, motivation, meaningful constraints and priorities, and completion standard. Procedural prompts are semantically matched and add anticipated steps, likely files, commands, validation actions, sequencing, and defensive instructions. Neither style may change the canonical intent or hidden rubric. The prior checklist condition is retained only as a labeled secondary ablation when useful.

## 4. Non-claims and boundaries

Decapod does not change intrinsic LLM capability or parameters. It is not a complete operating-system sandbox, does not guarantee credential isolation, does not intercept every model or shell action, and does not establish universal semantic correctness. Its trajectory is a governance record, not a universal tamper-proof execution ledger. Proof artifacts establish what configured gates observed, not total correctness. Isolated workspaces reduce direct collisions but can still produce later merge conflicts. Governance may impose material cost and may fail to improve outcomes.

## 5. Falsifiable predictions

The study predicts that Decapod may reduce invalid completion claims and improve recovery and evidence completeness, especially under natural delegation. It must also measure the possibility that procedural prompts remain necessary, that context resolution merely relocates human effort into setup, that clarification burden increases, or that governance overhead outweighs benefits.

The thesis is weakened if natural delegation with Decapod does not improve on natural delegation without it; if procedural prompting remains necessary for acceptable quality; if a checklist or smaller intervention performs equivalently; if clarification/context costs rise without improving fidelity; or if governance overhead dominates autonomy and reliability gains.

Current synthetic fixtures are harness demonstrations, not empirical evidence. Pilot observations are labeled and excluded from confirmatory estimates. Confirmatory claims require a frozen protocol, raw provenance, independent evaluation, and reproducible analysis.
