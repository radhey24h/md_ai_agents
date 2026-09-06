# Agent Markdown workspace

This folder holds **two independent projects** about the same architecture. They are not copies of each other.

> Markdown is the job card. The IDE is the runtime. MCP is the toolbox. Workflow + HITL is the manager. An `.md` file is not an agent by itself.

| Project | What it is | Start here |
|---------|------------|------------|
| **Learning curriculum** | Eight sessions. Small first. Enterprise last. | [agent-markdown-learning/README.md](agent-markdown-learning/README.md) |
| **Enterprise sample** | One shared knowledge plane for Cursor, Copilot, and Claude, with a real HITL runner. | [enterprise-agent-platform/README.md](enterprise-agent-platform/README.md) |

```text
md_ai_agents/
├── README.md                          ← this file
├── .gitignore
├── agent-markdown-learning/           ← course + workshop kit
└── enterprise-agent-platform/         ← runnable shared-tree sample
```

Use **learning** to understand the pieces. Use **enterprise** to run the same idea as one repo.

---

## 1. Agent Markdown Learning

Hands-on curriculum. Not a production platform.

One business example throughout: **Customer Notification Preferences**.

| Session | Topic | Link |
|---------|--------|------|
| 01 | Agent / Skill / Rule / Doc | [session-01-foundation](agent-markdown-learning/sessions/session-01-foundation/README.md) |
| 02 | Artifact and handoff | [session-02-artifacts-handoff](agent-markdown-learning/sessions/session-02-artifacts-handoff/README.md) |
| 03 | Sequential pipeline | [session-03-sequential](agent-markdown-learning/sessions/session-03-sequential/README.md) |
| 04 | Parallel + join | [session-04-parallel](agent-markdown-learning/sessions/session-04-parallel/README.md) |
| 05 | Human-in-the-loop | [session-05-hitl](agent-markdown-learning/sessions/session-05-hitl/README.md) |
| 06 | MCP / tools | [session-06-mcp](agent-markdown-learning/sessions/session-06-mcp/README.md) |
| 07 | Multi-agent workflow | [session-07-multi-agent](agent-markdown-learning/sessions/session-07-multi-agent/README.md) |
| 08 | Complete enterprise demo | [session-08-complete-enterprise](agent-markdown-learning/sessions/session-08-complete-enterprise/README.md) |

**Also useful**

- [Learning path](agent-markdown-learning/learning-path.md) — what each session adds
- [Glossary](agent-markdown-learning/glossary.md)
- [Architecture overview](agent-markdown-learning/architecture-overview.md) — sequential vs parallel vs HITL vs MCP
- [Sessions index](agent-markdown-learning/sessions/README.md)
- [Customer notification example](agent-markdown-learning/examples/customer-notification/README.md)

Open `agent-markdown-learning/` and start at Session 01. Do not start at Session 08.

---

## 2. Enterprise Agent Platform

Runnable sample: **one** `agents/`, `rules/`, `skills/`, and `docs/` tree. Cursor, Copilot, and Claude all follow that tree. HITL is enforced by Python CLI + MCP, not by a prompt.

```text
requirements → HITL → architect → HITL → developer → QA → security → HITL → DONE
```

**Also useful**

- [README](enterprise-agent-platform/README.md) — how to run + speakable knowledge session
- [AGENTS.md](enterprise-agent-platform/AGENTS.md) — constitution every IDE loads
- [Workflow YAML](enterprise-agent-platform/workflow/feature-development.yaml)
- [How the pipeline runs](enterprise-agent-platform/docs/flow.md)
- [Docs index](enterprise-agent-platform/docs/README.md)
- [Model policy](enterprise-agent-platform/workflow/model-policy.md)
- Agents: [orchestrator](enterprise-agent-platform/agents/orchestrator.md), [requirements](enterprise-agent-platform/agents/requirements.md), [architect](enterprise-agent-platform/agents/architect.md), [developer](enterprise-agent-platform/agents/developer.md), [QA](enterprise-agent-platform/agents/qa-reviewer.md), [security](enterprise-agent-platform/agents/security-reviewer.md)

```powershell
cd enterprise-agent-platform
py -3 scripts/workflow_runner.py start --feature customer-notification
py -3 scripts/workflow_runner.py run
py -3 scripts/workflow_runner.py approve --by "jane" --comment "ok"
py -3 scripts/workflow_runner.py status
```

Open `enterprise-agent-platform/` as the workspace when you run this sample.

---

## How they relate

| | Learning | Enterprise |
|--|----------|------------|
| Purpose | Teach one concept at a time | Show a complete shared-tree repo |
| Complexity | Grows session by session | Full pipeline from day one |
| Runtime | Small teaching scripts in later sessions | `workflow_runner.py` + MCP server |
| Knowledge plane | Per-session files | One `agents/` `rules/` `skills/` `docs/` |
| Audience | Workshop, interview prep | Architecture review, live demo |

Do not merge the two folders. Do not copy the enterprise tree into the curriculum.

---

## Shared mental model

| Piece | Question |
|-------|----------|
| Agent | Who performs the work? |
| Skill | How is this type of work performed? |
| Rule | What must always be true? |
| Doc | What facts do we know? |
| Artifact | What does the worker hand to the next worker? |
| Workflow | What happens next? |
| HITL | Where must a human decide? |
| MCP | What external capability can the agent call? |
| Model | What provides reasoning? |
