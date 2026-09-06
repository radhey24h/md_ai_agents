# Glossary

| Term | Meaning in this curriculum |
|------|----------------------------|
| **Model** | The reasoning engine. Not the agent. |
| **Agent** | Who does the work: role, inputs, outputs, what it must never do. |
| **Skill** | How a *type* of work is done (playbook). Reusable across agents. |
| **Rule** | Short standing constraint. Not a 500-line procedure. |
| **Doc** | Facts about this system. Not instructions. |
| **Artifact** | Durable file the next worker reads. Not the chat transcript. |
| **Handoff** | Passing an artifact (and often a status) to the next stage. |
| **State** | Where the run is now (`currentStage`, gates). Not conversation memory. |
| **Workflow** | What runs next, in what order, under what condition. |
| **Sequential** | B waits for A because B needs A’s output or a gate. |
| **Parallel** | Independent work at the same time; then a **join**. |
| **Join** | Wait for branches; then one downstream consumer. |
| **HITL** | Human-in-the-loop. The run stops until approve or reject. |
| **MCP** | Model Context Protocol. Standard way to expose tools/resources. |
| **Tool** | A callable capability (status, read file, scanner). |
| **Orchestrator** | Sequences specialists. Does not do their specialist work. |
| **Least privilege** | An agent gets only the access its job needs. |
| **FACT** | Proven from code, tests, docs, or approved runtime evidence. |
| **EVIDENCE** | Where the fact was observed. |
| **INFERENCE** | Reasonable but not proven. Label it. |
| **UNKNOWN** | Not proven. Do not invent. Escalate. |
| **Native (IDE)** | What Cursor / Copilot / Claude load by convention. |
| **Demo runtime** | Teaching scripts in this repo that illustrate order, HITL, MCP. |

Markdown configures. A runtime executes. Do not claim Markdown “runs the pipeline” by itself.
