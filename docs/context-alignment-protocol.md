# Pre-Inference Context Alignment Protocol

This protocol tests whether Decapod supplies better selected and more authoritative context, rather than merely more text.

## Treatment context manifest

Each Decapod-governed run records a manifest before the first implementation action. Every item has:

- authority source path and authority type;
- selection rationale and task relevance;
- content hash, byte/token size, and selected/excluded status;
- the project decision, constraint, standard, or proof expectation it resolves.

The manifest also records selected constitutional nodes, project specifications, capability overlays, negative requirements, prior decisions, unresolved questions and escalation rules, excluded context, total context size, and context-resolution latency.

## Control boundary

The conventional run records an explicit empty Decapod-context manifest and the ordinary repository context visible to the runtime. It must not receive the treatment's capsule, hidden rubric, evaluator logic, or governance state. Both cells receive the same canonical task prompt, repository commit, tools, timeout, model, and evaluator.

## Independent audit

An auditor who does not execute the task classifies every supplied item as `necessary`, `useful`, `irrelevant`, `redundant`, `contradictory`, or `harmful`, with a reason and source reference. The audit is separate from the agent's completion claim and is included in the provenance chain.

The study must report harmful or irrelevant context, not discard it as an instrumentation nuisance. Context quantity alone is not a mechanism outcome.

For Studies B–D, record the context manifest available immediately before and after transfer or concurrent task claim. The audit distinguishes newly resolved context from reused project memory and records stale, contradictory, redundant, or lost items. This extension does not change Study A's primary context-alignment estimand.
