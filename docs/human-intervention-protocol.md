# Human Intervention Protocol

Human assistance is an outcome of the experiment, not an unlogged repair mechanism.

The primary run models “type the outcome and walk away.” Corrective coaching and follow-up instructions are prohibited after the agent starts in both CN and DN. Clarification is permitted only through the task's frozen oracle; if the oracle cannot resolve the question, record the run as clarification-blocked or a protocol deviation rather than improvising help.

Every intervention record must include:

- run identifier and timestamp;
- trigger: agent question, failure, timeout, policy gate, or human observation;
- response source: prewritten oracle/decision table, approved escalation, or protocol deviation;
- response text or a redacted reference;
- duration and whether the intervention changed task scope;
- adjudication: necessary, avoidable, correctly escalated, or protocol deviation.

Clarification responses come from the task's prewritten oracle. The operator must not improvise materially different help across cells. The intervention log records `coaching_allowed=false`, oracle usage, human presence after start, and every response source.

Human review is a secondary study requiring a separate reviewer protocol, blinded assignment where possible, correctness checks, consent/ethics review, and a frozen analysis plan.

For Studies B and D, the receiving agent gets only the frozen conventional or Decapod handoff payload. An ad hoc human explanation is prohibited and recorded as a failed human-absence outcome or protocol deviation. For Study C, humans may perform only predeclared integration/publish actions; manual task reassignment, conflict resolution, or dependency advice is an intervention. The protocol records exact briefing content, duration, and whether it exposed information unavailable to the comparison condition.
