# Publication and Artifact Roadmap

This document outlines the roadmap for publishing this research and distributing its corresponding artifact. It focuses on maintaining empirical rigor, complying with venue requirements, and achieving high standards of reproducibility.

---

## 1. Phased Publication Plan

We adopt a phased approach to distributing our findings, ensuring that early reviews refine our empirical work before final submission to peer-reviewed venues.

### Phase 1: Technical Report and Public Artifact Release
* **Goal**: Publish the initial complete draft of the paper as a formal Technical Report alongside the open-source release of the evaluation artifact.
* **Channels**: Decapod Labs documentation/website, GitHub Pages, or a similar public repository.
* **Target Date**: Q3 2026.
* **Prerequisites**: Completion of the 525 planned execution runs (not simulator output), independent verification of raw data and analysis, a reproducible artifact run, and validation of all proof files.

### Phase 2: arXiv Submission
* **Policy Check**: We adhere strictly to arXiv's policies for the CS category, which subject survey and position papers to prior-review requirements. Because this paper presents an empirical systems artifact and quantitative evaluation (not just a position or survey), it qualifies for standard arXiv distribution.
* **Timing**: We will upload the paper to arXiv *only* after:
  1. The full empirical evaluation is complete and analyzed.
  2. The artifact repository contains fully runnable scripts that reproduce all tables and figures.
  3. The text has been peer-reviewed internally by at least two external systems/SE researchers.

### Phase 3: Peer-Reviewed Conference Submission
We will target major software engineering or systems research venues. The choice of venue depends on the depth of the systems contribution versus the software engineering process contribution.

* **Target Option A: International Conference on Software Engineering (ICSE)**
  * *Rationale*: ICSE’s research track is well-suited for studies of developer workflows, code generation tool validation, and LLM-based software engineering frameworks.
  * *Focus*: Emphasize the software engineering metrics: reduced false completion claims, lower developer audit time, and improved concurrent correctness.
* **Target Option B: Symposium on Operating Systems Principles (SOSP) / Operating Systems Design and Implementation (OSDI)**
  * *Rationale*: If our systems implementation of custody limits and concurrency isolation (the Decapod kernel itself) represents a significant distributed systems advancement.
  * *Focus*: Emphasize kernel primitives, performance overhead, security bounds of workspace isolation, and state consensus.
* **Target Option C: ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (FSE)**
  * *Rationale*: Similar to ICSE, focusing on the foundations of how agentic workflows are governed and validated.

---

## 2. Artifact Badging Guidelines

To maximize academic impact, the artifact must be designed to meet the criteria for ACM Artifact Badging:

1. **Artifacts Evaluated – Functional**:
   * The artifact must include a clear, step-by-step setup guide.
   * All scripts must execute without errors on standard Linux environments.
   * A mini-benchmark run must be provided to let reviewers quickly verify functionality in under 10 minutes.
2. **Artifacts Evaluated – Reusable**:
   * The source code for the Decapod kernel must be clearly documented.
   * The evaluation harness must support adding new LLM backends or new benchmark tasks.
   * All code must be licensed under an OSI-approved license (e.g., MIT or Apache 2.0).
3. **Artifacts Available**:
   * The final version of the code and all raw run logs (`.jsonl` files) must be hosted on a permanent, citable repository (e.g., Zenodo or Figshare) with a unique DOI.
