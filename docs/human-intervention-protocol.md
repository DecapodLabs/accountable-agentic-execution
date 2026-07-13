# Human Intervention Protocol

Human assistance is an outcome of the experiment, not an unlogged repair mechanism.

Every intervention record must include:

- run identifier and timestamp;
- trigger: agent question, failure, timeout, policy gate, or human observation;
- response source: prewritten oracle/decision table, approved escalation, or protocol deviation;
- response text or a redacted reference;
- duration and whether the intervention changed task scope;
- adjudication: necessary, avoidable, correctly escalated, or protocol deviation.

Clarification responses come from the task's prewritten oracle. The operator must not improvise materially different help across cells. Unresolved questions that the oracle cannot answer are recorded as exclusions or protocol deviations rather than silently resolved.

Human review is a secondary study requiring a separate reviewer protocol, blinded assignment where possible, correctness checks, consent/ethics review, and a frozen analysis plan.
