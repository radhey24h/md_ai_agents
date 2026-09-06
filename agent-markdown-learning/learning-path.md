# Learning path

Eight sessions. Each is independently readable. Each assumes only what the previous session taught.

| Session | Topic | Main concept | Execution |
|---------|--------|----------------|-----------|
| 01 | Foundation | Agent / Skill / Rule / Doc | Single |
| 02 | Artifact & Handoff | Agent communication | Sequential (two workers) |
| 03 | Sequential | Pipeline | Sequential |
| 04 | Parallel | Independent work | Parallel + join |
| 05 | HITL | Human approval | Sequential + HITL |
| 06 | MCP | Tool invocation | Agent + tools |
| 07 | Multi-Agent | Orchestration | Sequential + parallel |
| 08 | Complete Enterprise | Everything | Complete |

Business thread: **Customer Notification Preferences** ([examples/customer-notification](examples/customer-notification/README.md)).

---

## Session 01 — Foundation

- **Objective:** Separate *who*, *how*, *must*, and *facts*.
- **Already knows:** Nothing required about agents.
- **New:** Agent, Skill, Rule, Doc. Evidence labels.
- **Demonstrated:** One Customer Analyst reads a skill, a rule, and a doc.
- **Artifact:** Informal analysis notes (not yet a contract).
- **Afterward:** Learner can explain why a 500-line “rule” is a skill.
- **Next:** Make the output a file another worker can trust.

## Session 02 — Artifact & Handoff

- **Objective:** Stop depending on chat memory.
- **Already knows:** Agent / Skill / Rule / Doc.
- **New:** Artifact, handoff, durable state.
- **Demonstrated:** Analyst writes `analysis.json`. Planner reads only that file.
- **Artifact:** `analysis.json` with requirements, unknowns, evidence.
- **Afterward:** Chat vs artifact is clear.
- **Next:** More than two stages, with enforced order.

## Session 03 — Sequential

- **Objective:** Workflow owns order; agents own work.
- **Already knows:** Artifacts.
- **New:** Pipeline, dependencies, failure, retry.
- **Demonstrated:** Requirements → Architect → Developer → QA. Developer cannot run first.
- **Artifact:** One JSON per stage.
- **Afterward:** “The architect agent should not decide the whole factory.”
- **Next:** Work that does *not* need to wait.

## Session 04 — Parallel

- **Objective:** Fan-out independent analysis; join before anyone depends on the set.
- **Already knows:** Sequential pipelines.
- **New:** Parallel branches, join, what must stay sequential.
- **Demonstrated:** API / DB / UI analysis in parallel, then consolidator.
- **Artifact:** Three analysis files + `consolidated-analysis.json`.
- **Afterward:** Architecture and Developer in parallel is illegal if Developer needs the design.
- **Next:** Humans at the dangerous steps.

## Session 05 — HITL

- **Objective:** The run **stops** until a named human approves or rejects.
- **Already knows:** Sequential handoff.
- **New:** HITL gates; model must not self-approve.
- **Demonstrated:** Approve continues. Reject returns to rework.
- **Artifact:** `approvals/*.json` plus stage files.
- **Afterward:** HITL is a file and a stop, not a prompt (“please get approval”).
- **Next:** Tools, without mixing them into the job card.

## Session 06 — MCP

- **Objective:** MCP is capability access, not the agent definition.
- **Already knows:** Workflow and HITL conceptually.
- **New:** MCP tools vs Markdown vs workflow.
- **Demonstrated:** Tiny teaching server: status, read doc, read artifact. Approve is human-only.
- **Artifact:** Tool call results (text/JSON).
- **Afterward:** “Markdown says what. Workflow says when. MCP says what it can call.”
- **Next:** Put the pieces under an orchestrator.

## Session 07 — Multi-Agent

- **Objective:** Orchestrator + specialists + least privilege + writer ≠ judge.
- **Already knows:** Seq, parallel, HITL, MCP ideas.
- **New:** Combining them; QA/security independence.
- **Demonstrated:** Discovery parallel, design sequential with HITL, QA ‖ security, join, release HITL.
- **Artifact:** Bundle of stage JSON files.
- **Afterward:** Permissions follow role, not model strength.
- **Next:** One end-to-end story with the same feature.

## Session 08 — Complete Enterprise Demo

- **Objective:** Capstone. Same customer-notification feature, full path.
- **Already knows:** Sessions 1–7.
- **New:** How it *fits* (no new primitive).
- **Demonstrated:** Request → orchestrator → parallel discovery → requirements HITL → architecture HITL → implementation → QA ‖ security → join → release HITL.
- **Artifact:** Full run folder under the session `artifacts/`.
- **Afterward:** Production-grade agent systems need roles, skills, rules, artifacts, state, tools, guardrails, and humans — not a pile of prompts.
- **Next:** Apply the same split in a real repo (without copying a vendor mesh).
