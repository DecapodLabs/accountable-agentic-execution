# Research Claims and Falsifiability Ledger

This document establishes the precise academic claims, non-claims, and empirical testability of our research. It acts as an intellectual honesty guard, forcing us to bound our assertions and outline exactly what observations would disprove or weaken our thesis.

---

## 1. Core Thesis

Agentic software engineering is increasingly a distributed execution problem. When autonomous models edit files, invoke compilers, run tests, and execute tools, the traditional record of work (the chat transcript, system prompt, and final code diff) is insufficient for safety, recovery, and verification. Accountable execution requires four explicit, repo-native systems primitives: **Intent**, **Custody**, **Trajectory**, and **Proof**.

---

## 2. Main Claim

Implementing explicit, repo-native mechanisms for **Intent**, **Custody**, **Trajectory**, and **Proof** as first-class primitives in agentic coding workflows:
1. **Reduces the rate of invalid completion claims** (where an agent falsely asserts it has completed a task when the requirements are not met or verification fails).
2. **Improves recoverability** (the ability of a human or subsequent agent to resume work from an interrupted, aborted, or partially failed agent run).
3. **Prevents authority leakage and cross-task state corruption** in environments where multiple agents operate concurrently.

---

## 3. Secondary Claims

* **Auditability**: Traces generated under custody constraints with explicit trajectory logs require significantly less human review effort to verify for correctness than raw LLM execution transcripts.
* **Deterministic Verification**: Embedding validation gates directly in the agent's workspace custody context ensures that completion claims can be checked programmatically before code is proposed for merge.
* **Intent Drift Mitigation**: A durable intent statement (e.g., a formal checklist or spec tracked outside the context window) reduces the likelihood of an agent drifting off-task during long-running tool loops.

---

## 4. Non-Claims

To remain rigorous, we explicitly state what this paper does **NOT** claim:
* **We do not claim that Decapod makes the underlying LLM "smarter" or inherently better at writing code.** The generation capability of the model remains bounded by its parameters and pretraining. Rather, we claim Decapod prevents execution failure modes and makes the work safe and reviewable.
* **We do not claim that our framework eliminates all bugs or malicious actions.** A model under custody limits can still generate buggy code, provided that code passes the defined validation gates.
* **We do not claim that Decapod is a general-purpose agent framework.** It is a *governance kernel* (a control plane) that wraps existing agents. It does not replace or redefine the agent loop itself.
* **We do not claim that a machine-generated proof can represent all dimensions of human intent.** Soft requirements (e.g., code readability, elegance, future maintainability) are still difficult to verify programmatically and require human review.

---

## 5. Falsifiable Predictions

Our evaluation is designed around the following concrete, falsifiable predictions:

1. **Prediction 1 (Completion Claims)**: In a benchmark of 50 multi-step coding tasks, the Treatment group (Decapod-governed) will exhibit at least a 50% reduction in "false-positive completion claims" compared to Baseline A (prompt-only) and Baseline B (checklist-only).
2. **Prediction 2 (Interruption Recovery)**: When an agent's execution is abruptly killed mid-task and resumed, the Treatment group (using the checkpointed Trajectory and Intent primitives) will successfully complete the task in at least 30% more cases than Baseline A, which must restart from the initial prompt and current workspace state.
3. **Prediction 3 (Concurrent Safety)**: Under a test of two agents making edits to overlapping sections of a repository, Treatment group runs (using isolated workspace custody and branch lockouts) will result in zero uncoordinated merge conflicts, whereas baselines running on the same branch will show frequent overwrites or corrupt states.
4. **Prediction 4 (Audit Speed)**: An independent human reviewer can correctly accept/reject a task modification 40% faster when presented with a Decapod Trajectory and Proof artifact than when reviewing a raw chat transcript.

---

## 6. What Would Weaken or Disprove This Thesis?

Our thesis would be weakened or disproven if any of the following are observed during evaluation:

* **Observation A**: If Baseline B (simply writing a todo list in markdown and appending it to the prompt) achieves the same level of task completion and prevents invalid completion claims just as well as the complete Decapod Treatment. This would suggest that complex governance kernels are unnecessary overhead, and prompting disciplines are sufficient.
* **Observation B**: If the runtime overhead of creating isolated custody workspaces (e.g., git worktrees, docker containers) and recording trajectories increases execution latency and tool calls so severely that it outweighs the safety benefits.
* **Observation C**: If agents frequently bypass custody controls or fail to parse their bounds in a way that causes *more* failures, proving that the governance kernel introduces a fatal mismatch with modern model reasoning.
* **Observation D**: If human reviewers find the generated proof files and trajectories confusing, leading to *no* reduction in audit/review time compared to reading raw transcripts.
