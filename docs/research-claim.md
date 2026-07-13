# Research Claims and Falsifiability Ledger

## Central claim under test

Intent is the human or team's desired outcome, motivation, constraints, priorities, unresolved questions, stop conditions, and standard of completion. A prompt is an initial and potentially incomplete expression of that intent. Plans, todos, specifications, context capsules, proof hooks, and acceptance rubrics are governed representations or resolutions of intent, not its source of authority.

The primary claim is that, under the same complex natural delegation prompt and no ongoing human coaching, Decapod's pre-inference context resolution and governed execution corridor may improve independent fidelity and convergence efficiency. The underlying model is unchanged. Decapod is hypothesized to make the agent system operationally more knowledgeable and contextually aligned by resolving authoritative project context before implementation inference.

The key interaction is human absence: the intended interaction is “type the outcome, start the agent, and walk away.” The primary comparison is conventional agent + natural delegation versus Decapod-governed agent + the identical natural delegation.

## Hypotheses

- **H1:** Decapod-governed runs more often satisfy a hidden intent-fidelity rubric.
- **H2:** They require fewer model requests, failed execution cycles, redundant tool operations, and substantial rewrites before acceptable completion.
- **H3:** They apply more relevant repository constraints, conventions, and applicable standards without those details being named in the prompt.
- **H4:** They more often complete without clarification or corrective human intervention.
- **H5:** They produce more complete validation, provenance, and review evidence.
- **H6:** Gains, if any, are reported against context-resolution, workspace, validation, token, latency, and operational overhead.

## Primary measurements

The primary outcome is independently evaluated fidelity of the final repository state to the human/team intent. The hidden rubric covers functional correctness, explicit requirements, project invariants, architecture, conventions, standards, regressions, scope, validation, evidence, and acceptance readiness.

Convergence measurements include model requests, tokens, tool calls, repository searches, pre-edit files opened, time to first relevant action, failed attempts, redundant calls, validation failure cycles, reversals or substantial rewrites, clarification requests, unresolved questions, time to acceptable completion, premature completion claims, and cost where available. Context alignment records selected authority nodes, specifications, capabilities, constraints, standards, prior decisions, excluded context, context size/latency, and item-level independent relevance labels.

## Secondary design

The prior 2x2 substrate × prompt-style design is retained as a secondary ablation: conventional/Decapod-governed crossed with natural/procedural prompts. Natural and procedural prompts are matched projections of one canonical intent. A checklist-only condition is secondary only.

## Failure conditions

The thesis is unsupported or weakened if Decapod does not improve fidelity, fails to reduce failed or redundant execution cycles, increases cost without better results, supplies irrelevant or harmful context, still needs regular correction, is matched by conventional execution at equal or lower effort, benefits from hidden rubric leakage, improves proof while task quality does not improve, or merely relocates supervision into setup/configuration.

## Boundaries

Decapod does not change LLM parameters or intrinsic capability. It is not a complete operating-system sandbox, does not guarantee credential isolation, does not intercept every model or shell action, and does not establish universal semantic correctness. Its trajectory is a governance record, not a universal tamper-proof execution ledger. Proof establishes what configured gates observed, not total correctness. Isolated workspaces reduce direct collisions but can still produce later merge conflicts. Synthetic fixtures and pilot observations are not confirmatory evidence.
