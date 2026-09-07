# Agent Markdown Learning

Hands-on curriculum for **Agent Markdown architecture**. Start tiny. End with a full enterprise-style workflow. One business example the whole way: **Customer Notification Preferences**.

This folder is a **course and workshop kit**. It is not a production agent platform.

> **Markdown is the job card.**  
> **The IDE is the runtime.**  
> **MCP is the toolbox.**  
> **Workflow + HITL is the manager.**  
> **An `.md` file is not an agent by itself.**

```text
                         ┌──────────────┐
                         │    MODEL     │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │    AGENT     │
                         │    WHO       │
                         └──────┬───────┘
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
              SKILLS          RULES           DOCS
               HOW            MUST             FACTS
                 │              │              │
                 └──────────────┼──────────────┘
                                ▼
                         ┌──────────────┐
                         │   ARTIFACT   │
                         │   HANDOFF    │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │   WORKFLOW   │
                         │    ORDER     │
                         └──────┬───────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
                 SEQUENTIAL              PARALLEL
                    │                       │
                    └───────────┬───────────┘
                                ▼
                              HITL
                                │
                                ▼
                              MCP
                                │
                                ▼
                              TOOLS
```

```text
Foundation → Artifacts → Sequential → Parallel → HITL → MCP → Multi-Agent → Enterprise Workflow
```

Start at [sessions/session-01-foundation](sessions/session-01-foundation/README.md). Session map: [learning-path.md](learning-path.md).

---

## What is this project?

Eight sessions. Each one adds **one** idea. Teach them live (`demo.md`) or study the session `README.md`.

| Session | Topic | New idea | Execution |
|---------|--------|----------|-----------|
| 01 | [Foundation](sessions/session-01-foundation/README.md) | Agent, Skill, Rule, Doc | Single |
| 02 | [Artifact & Handoff](sessions/session-02-artifacts-handoff/README.md) | Durable communication, not chat | Sequential (two workers) |
| 03 | [Sequential](sessions/session-03-sequential/README.md) | Workflow owns order | Sequential |
| 04 | [Parallel](sessions/session-04-parallel/README.md) | Independent work, then join | Parallel + join |
| 05 | [HITL](sessions/session-05-hitl/README.md) | Human approve / reject; model does not self-approve | Sequential + HITL |
| 06 | [MCP](sessions/session-06-mcp/README.md) | Tools as capabilities, not as the job card | Agent + tools |
| 07 | [Multi-Agent](sessions/session-07-multi-agent/README.md) | Orchestrator + specialists + least privilege | Sequential + parallel |
| 08 | [Complete Enterprise](sessions/session-08-complete-enterprise/README.md) | Same feature, full path | Complete |

Markdown does not execute agents. A runtime (IDE or script) does.

- **Native to an IDE:** loading `AGENTS.md` / `CLAUDE.md`, optional subagent folders, optional skill auto-discovery, optional glob rules.
- **This curriculum’s demos:** small Python scripts and JSON artifacts that **show** sequence, join, HITL stop, and MCP. They are teaching runtimes, not Cursor or Copilot.

---

## Who is this for?

Developers, technical leads, architects, AI engineers, solution architects, engineering managers, and anyone learning agentic architecture. Each session README has interview-ready lines.

---

## Prerequisites

- Comfort reading Markdown and a little YAML/JSON
- Ability to open files in any editor
- Python 3.10+ **only** if you want to run the later demo scripts (`py -3` on Windows)
- No vendor certification and no deep ML background

---

## How to use it

1. Skim [Glossary](#glossary) once.
2. Follow [learning-path.md](learning-path.md).
3. For a live walkthrough, open each session’s `demo.md`: the problem, what to do, the one takeaway.
4. Keep [eShop-customer-notification](eShop-customer-notification/README.md) open. The same shop grows from Session 1 to Session 8.

Do not start at Session 8. Session 1 is intentionally small.

---

## Glossary

Markdown configures. A runtime executes. Do not claim Markdown “runs the pipeline” by itself.

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

---

## Execution decisions

| Situation | Execution |
|-----------|-----------|
| Requirements → Architecture | Sequential |
| Architecture → Development | Sequential |
| API + DB + UI discovery | Parallel |
| QA + Security analysis | Parallel |
| Release after QA (and security join) | Sequential |
| Human approval | Gate |
| Independent inventory tasks | Parallel |
| Dependent tasks | Sequential |

```text
Dependency exists → Sequential
No dependency → Parallel
Risk/decision exists → HITL
External capability required → MCP
Persistent communication → Artifact
```

---

## Least privilege

| Role | Allowed | Not allowed |
|------|---------|-------------|
| Architect | Read, analyze, design | Change app code, deploy |
| Developer | Change application code after design HITL | Approve own work, production deploy |
| QA | Run tests, write verdict | Modify production code |
| Security | Analyze, set `release_allowed` | Approve release as a human |
| Release | Deploy after HITL | Invent business rules |
| Orchestrator | Sequence, read state | Do specialist design/code |

More capable **models** do not get more **permissions**.

---

## Native vs demonstration

| Concern | Native IDE (typical) | This curriculum |
|---------|----------------------|-----------------|
| Job cards / skills / rules as files | Yes, if you put them where the product looks | Yes, as teaching files in each session |
| Subagent picker | `.cursor/agents`, `.github/agents`, `.claude/agents` | Not required for learning |
| Guaranteed HITL stop | Not reliable across products | Session 5+ **scripts** stop until approve/reject |
| MCP | Product loads a configured server | Session 6 tiny teaching server |

Do not tell learners that a folder of `.md` files is a workflow engine.

---

## Evidence

```text
FACT:      GET/PUT /api/customers/{id}/preferences and POST /api/orders/{id}/ship exist.
EVIDENCE:  eShop-customer-notification/app/shop/api/http.py
INFERENCE: Preferences are customer-owned; shipping is the send path.
UNKNOWN:   Whether SMS is a supported channel (not in http.py, db.py, or the HTML pages).
```

If it is not proven, it is UNKNOWN. Agents must not invent business behavior.
