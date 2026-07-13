# Lab Example

This is a deliberately small, fake Python project contained inside the research repository. It is a demonstration fixture for tracing a governed task; it is not an empirical agent run and makes no security-isolation claim.

The project is initialized with Decapod in this directory. The trace under `traces/` records a bounded prompt, task state, validation command, and result references. The prompt is a fixture, not a model transcript.

The demonstration changes `app.py` and `test_app.py`, then runs a direct Python assertion check. It shows that a task contract, bounded change, and validation result can be kept together in one contained project; it does not prove credential isolation, universal command capture, or an empirical treatment effect. See [`traces/01-bounded-change.jsonl`](traces/01-bounded-change.jsonl).
