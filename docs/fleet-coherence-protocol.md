# Fleet Coherence Research Protocol

Status: prospective extension in harness validation. No pilot or empirical fleet records exist.

## Definition and mechanism

**Fleet coherence** is the bounded ability of independently launched, potentially heterogeneous agent processes to operate against one durable project authority without making intent, ownership, context, progress, and evidence disposable at every session boundary. It is an emergent property of the existing four primitives:

- **Intent** supplies common human/team authority and the desired outcome.
- **Custody** records task ownership and assigns bounded workspaces.
- **Trajectory** preserves selected governance state across sessions, retries, and handoffs.
- **Proof** supplies a shared acceptance and publication boundary independent of the executing workbench.

Agents and conversations are ephemeral execution processes; the governed repository is the durable coordination subject.

This definition does not imply global consensus, conflict-free merging, lossless transcript transfer, complete runtime interception, or production cloud federation. The inspected public Decapod implementation is local-first. It supports repository-native tasks, claims, handoff events, workspaces, context capsules, knowledge, governance events, proofs, and publication gates; its public cloud backend is unavailable.

## Research questions

- **RQ7 — Cross-agent continuity:** Does Decapod reduce reorientation and reconstruction work when execution transfers between independent sessions or workbenches?
- **RQ8 — Duplicate-work prevention:** Do explicit task claims reduce duplicated investigation and implementation across concurrent agents?
- **RQ9 — Fleet integration:** Does Decapod reduce uncoordinated workspace failures and integration repair without merely deferring conflicts until merge?
- **RQ10 — Provider independence:** Can a receiving workbench continue governed work without replaying the complete prior transcript or receiving an ad hoc human briefing?
- **RQ11 — Project memory:** Does repository-owned governed state preserve relevant decisions, constraints, dependencies, and unresolved questions more reliably than conversation-owned state?
- **RQ12 — Coordination cost:** Do continuity and coordination benefits outweigh context resolution, governance, workspace, proof, and integration overhead?

## Hypotheses and falsification

- **H7:** Governed handoffs reduce reorientation model requests, repeated file reads/searches, and duplicated commands relative to a structured conventional handoff.
- **H8:** Exclusive task claims reduce duplicate task starts relative to a conventional issue-plus-worktree workflow without shared custody state.
- **H9:** Governed context and trajectory reduce loss of project constraints after a session or workbench switch.
- **H10:** Worktree custody reduces direct mutation collisions, but may have no effect on semantic merge conflicts.
- **H11:** Portable proof references reduce repeated verification work when the receiving agent can validate their provenance and state binding.
- **H12:** Any continuity benefit is reported alongside governance setup, context, token, latency, workspace, proof, and integration cost.

The fleet thesis is weakened or unsupported if a standardized handoff document performs as well as Decapod; a shared issue tracker plus ordinary worktrees captures most benefits; shared context is stale, irrelevant, or harmful; proof improves while integrated task quality does not; agents still require ad hoc human briefings; or governance overhead removes any net cost benefit.

## Study B — Cross-workbench handoff continuity

### Unit and conditions

The unit is a paired task/checkpoint/repetition. Agent A begins the same complex task from the same clean commit. At a frozen checkpoint, A exits and Agent B starts with a clean model context.

- **Conventional structured handoff:** B receives the repository/branch, git history, public task description, and a frozen structured handoff document produced under the baseline protocol.
- **Decapod handoff:** B receives the same baseline artifacts plus the frozen Decapod task, ownership transfer, context references, trajectory, unresolved-state references, workspace state, and proof state that the current implementation exposes.

The baseline is deliberately credible: it is not an unexplained diff or a shared dirty checkout. Hidden rubric and condition labels remain unavailable to the executing agent. Evaluators are blinded where artifacts permit.

### Checkpoint and transfer controls

The checkpoint is task-defined and selected before execution by an observable event rule, such as the first completed implementation edit plus one validation attempt. Transfer uses the same elapsed-time limit in both conditions. The human supplies no ad hoc briefing. Any necessary answer follows the frozen clarification oracle and counts as absence intolerance.

### Measures

Capture source/destination workbench, model, and session; owner before/after; handoff reason and timestamp; payload references; context manifests; unresolved questions, dependencies, and proof state preserved/lost; reorientation model requests; time to first relevant continuation; duplicate searches, file reads, commands, tests, and implementation attempts; revisited decisions; reversals; clarifications; final fidelity; proof continuity; tokens; cost; elapsed time; and whether continuation succeeded without an ad hoc human briefing.

The first confirmatory level should hold the underlying model fixed where technically possible and vary sessions/workbenches. Heterogeneous providers are an external-validity extension because changing the model adds a major source of variance.

## Study C — Concurrent heterogeneous fleet

### Unit and baseline

The unit is a frozen task graph containing independent, dependent, and partially overlapping tasks assigned to at least two clean agent processes. Both conditions use separate branches or worktrees.

- **Conventional:** ordinary issue/task descriptions, git branches/worktrees, and the same public repository guidance, without shared Decapod claims, context capsules, governance trajectory, or publish state.
- **Decapod:** the same tasks plus implemented Decapod claims, labels/categories, dependencies, task-scoped workspaces, selected context, events, proof, and publication gates.

### Measures

Measure duplicate starts, claim conflicts, redundant discovery, overlapping file mutation, direct workspace collisions, dependency-order violations, later textual merge conflicts, semantic integration failures, abandoned work, repair commits/time, duplicated model calls/tokens, wall-clock completion, integrated hidden-rubric correctness, proof completeness, and publication success. Report task-local proof separately from post-integration proof.

## Study D — Tool-switch continuity

Study D applies Study B's checkpoint and measures to named workbench transitions supported by the available environment. It tests whether a later workbench can orient without receiving prior chat transcripts or a long human-authored explanation. Workbench pairs are frozen before execution. Results are stratified by same-model versus heterogeneous-model transitions and are not pooled without a predeclared model effect.

## Study E — Longitudinal dogfooding experience report

Study E is observational and cannot enter controlled estimates. A read-only script derives facts from a declared Decapod git commit: first/last commit dates, commit and tag counts, merge count, explicit revert-message count, authorship distribution, and changed top-level paths. Where available, separately archived GitHub/CI/Decapod records may add release, workflow, task, workspace, and proof activity.

Evidence classes remain separate:

1. **Repository-derived facts:** reproducible from git, tags, CI exports, or committed Decapod records.
2. **Author-reported experience:** testimony about workbenches, handoffs, supervision, or review burden, labeled as such.
3. **Causal claims:** reserved for controlled studies.

Commit volume cannot establish low review burden, correctness, or a Decapod treatment effect. Any claim of continuous dogfooding since an early release requires a traceable repository or author-testimony source.

## Cost-of-fragmentation taxonomy

- **Context rehydration waste:** rediscovering project state learned in another session.
- **Duplicated inference waste:** multiple agents reasoning over or solving the same work.
- **Collision waste:** repairing overlapping mutations or incompatible assumptions.
- **Handoff waste:** reconstructing missing intent, decisions, dependencies, and unresolved state.
- **Verification waste:** rerunning checks because evidence is unavailable, stale, or untrusted.
- **Integration waste:** repairing separately acceptable changes that fail when combined.
- **Dialect waste:** translating natural intent into workbench-specific operational procedures.
- **Context-bloat waste:** spending inference capacity on irrelevant or redundant governed context.
- **Abandonment waste:** losing interrupted work because economic continuation is impossible.

The economic hypothesis is that Decapod can lower the cost floor of agentic software development by making useful intent, context, ownership, progress, and evidence reusable across requests, sessions, models, workbenches, and teams. The studies must also count the human effort needed to configure and maintain that state.

## Provenance and separation

Every record declares one `study_id` and one evidence class. Controlled pilot and empirical data are separated from synthetic fixtures. Longitudinal observations are `observational` and cannot enter controlled summaries. Aggregation fails if a record from one study is supplied to another study's analysis path.

No paid or empirical execution is authorized by this protocol. Study B–D pilot execution requires an explicit runtime, model, credential, and budget authorization after task/checkpoint packages and evaluators are frozen.
