# Agent Markdown Learning

Hands-on curriculum for **Agent Markdown architecture**. Start tiny. End with a full enterprise-style workflow. One business example the whole way: **Customer Notification Preferences**.

This folder is a **course and workshop kit**. It is not a production agent platform.

> **Markdown is the job card.**  
> **The IDE is the runtime.**  
> **MCP is the toolbox.**  
> **Workflow + HITL is the manager.**  
> **An `.md` file is not an agent by itself.**

```text
Model
  ↓
Agent
  ↓
Rules + Skills + Docs
  ↓
Tools / MCP
  ↓
Artifact
  ↓
Workflow
  ↓
HITL / Next Agent
```

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

Start at [sessions/session-01-foundation](sessions/session-01-foundation/README.md). Full map: [learning-path.md](learning-path.md).

---

## What is this project?

Eight sessions. Each one adds **one** idea. You can teach them live (every session has a `demo.md`) or study them alone.

| Session | Topic | New idea |
|---------|--------|----------|
| 01 | Foundation | Agent, Skill, Rule, Doc |
| 02 | Artifact & Handoff | Durable communication, not chat |
| 03 | Sequential | Workflow owns order |
| 04 | Parallel | Independent work, then join |
| 05 | HITL | Human approve / reject; model does not self-approve |
| 06 | MCP | Tools as capabilities, not as the job card |
| 07 | Multi-Agent | Orchestrator + specialists + least privilege |
| 08 | Complete Enterprise | Same feature, full path |

Be precise in the room:

- **Native to an IDE:** loading `AGENTS.md` / `CLAUDE.md`, optional subagent folders, optional skill auto-discovery, optional glob rules.
- **This curriculum’s demos:** small Python scripts and JSON artifacts that **show** sequence, join, HITL stop, and MCP. They are teaching runtimes, not Cursor or Copilot.

Markdown does not execute agents. A runtime (IDE or script) does.

---

## Who is this for?

Developers, technical leads, architects, AI engineers, solution architects, engineering managers, and anyone learning agentic architecture. Interview prep is built in (`interview-takeaway.md` in every session).

---

## Prerequisites

- Comfort reading Markdown and a little YAML/JSON
- Ability to open files in any editor
- Python 3.10+ **only** if you want to run the later demo scripts (`py -3` on Windows)
- No vendor certification and no deep ML background

---

## How to use it

1. Read [glossary.md](glossary.md) once.  
2. Follow [learning-path.md](learning-path.md).  
3. For a live workshop, use each session’s `demo.md` (**Say → Demo → Ask → Expected → Explain**).  
4. Keep [examples/customer-notification](examples/customer-notification/README.md) open. The same feature grows from Session 1 to Session 8.

Do not start at Session 8. Session 1 is intentionally small.

---

## Mental model (repeat this)

| Piece | Question |
|-------|----------|
| **AGENT** | Who performs the work? |
| **SKILL** | How is this type of work performed? |
| **RULE** | What must always be true? |
| **DOC** | What facts do we know? |
| **ARTIFACT** | What does the worker hand to the next worker? |
| **WORKFLOW** | What happens next? |
| **HITL** | Where must a human decide? |
| **MCP** | What external capability can the agent call? |
| **MODEL** | What provides reasoning? |

Evidence language used from Session 1: **FACT / EVIDENCE / INFERENCE / UNKNOWN**. If you cannot prove it, do not invent it.

---

## Decision shortcuts

From [architecture-overview.md](architecture-overview.md):

```text
Dependency exists → Sequential
No dependency → Parallel
Risk/decision exists → HITL
External capability required → MCP
Persistent communication → Artifact
```
