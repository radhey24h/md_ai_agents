# Enterprise Agent Platform

One shared knowledge plane. One workflow. Cursor, Copilot, and Claude all read the **same** `agents/`, `rules/`, and `skills/` folders.

> Markdown is the job card. The IDE is the runtime. MCP is the toolbox. The workflow plus HITL is the manager. An `.md` file is not an agent by itself.

```text
                         AGENTS.md  (every IDE)
                               |
              +----------------+----------------+
              |                |                |
           agents/          rules/          skills/
           who              always          how-to
              |                |                |
              +----------------+----------------+
                               |
                    workflow + HITL + MCP
                               |
                         artifacts/runs
```

```text
MODEL  →  AGENT  →  RULES + SKILLS + DOCS  →  MCP/TOOLS  →  ARTIFACT  →  WORKFLOW  →  HITL or NEXT AGENT
```

```text
requirements → HITL → architect → HITL → developer → QA → security → HITL → DONE
```

This file is both the **repo guide** (how the sample is laid out and how to run it) and the **speakable knowledge session** (how to walk a room through it).

| Need | Where |
|------|--------|
| Run the sample | [Quick start](#quick-start) and [Folder design](#folder-design) |
| Teach / present | [Knowledge session](#knowledge-session) |
| Pipeline detail | [`docs/flow.md`](docs/flow.md) |
| Domain docs | [`docs/README.md`](docs/README.md) |

---

## Quick start

1. Open **this folder** as the workspace.
2. The IDE loads `AGENTS.md` (Claude also loads `CLAUDE.md`; Copilot also loads `.github/copilot-instructions.md`).
3. The agent reads `agents/<role>.md` + the matching `skills/` + `rules/` + `docs/`.
4. HITL and stage order come from `workflow/feature-development.yaml` via CLI or MCP.

```powershell
py -3 scripts/workflow_runner.py start --feature customer-notification
py -3 scripts/workflow_runner.py run
py -3 scripts/workflow_runner.py approve --by "jane" --comment "ok"
py -3 scripts/workflow_runner.py status
```

MCP tools (same engine): `start_feature_run`, `run_next_agent`, `workflow_status`, `hitl_approve`, `hitl_reject`, `read_artifact`, `read_project_doc`.

Do not call `hitl_approve` unless a human approved.

---

## Folder design

```text
enterprise-agent-platform/
│
├── AGENTS.md                          ← all platforms start here
├── CLAUDE.md                          ← Claude filename only (points here)
├── .github/copilot-instructions.md    ← Copilot filename only (points here)
│
├── agents/                            ← COMMON specialists (one copy)
│   ├── orchestrator.md
│   ├── requirements.md
│   ├── architect.md
│   ├── developer.md
│   ├── qa-reviewer.md
│   └── security-reviewer.md
│
├── rules/                             ← COMMON constraints (one copy)
│   ├── global.md
│   ├── backend.md
│   ├── frontend.md
│   ├── security.md
│   └── testing.md
│
├── skills/                            ← COMMON procedures (one copy)
│   ├── requirements-analysis/SKILL.md
│   ├── architecture-design/SKILL.md
│   ├── implementation/SKILL.md
│   ├── qa-review/SKILL.md
│   └── security-analysis/SKILL.md
│
├── docs/                              ← domain facts + flow
├── workflow/                          ← stage order + HITL + schema
├── artifacts/                         ← run output (gitignored)
├── scripts/                           ← CLI + MCP (same engine)
│
├── .cursor/mcp.json                   ← MCP path for Cursor
├── .mcp.json                          ← MCP path for Claude
└── .vscode/mcp.json                   ← MCP path for VS Code / Copilot
```

| Layer | Folders | Why it is shared |
|-------|---------|------------------|
| Knowledge | `agents/`, `rules/`, `skills/`, `docs/` | Business roles and facts must not fork per IDE |
| Control | `workflow/`, `scripts/` | HITL and order are the same everywhere |
| Runtime glue | `AGENTS.md` + three tiny MCP JSON files | Each tool only differs in *where* it looks for config |

`.cursor/`, `.github/`, and `.claude/` do **not** contain agents, rules, or skills. Those copies were the mesh.

Six agent *files* remain because the pipeline has six jobs. That is not duplication. Each job card sets `model:` for that task (`fast`, `high-reasoning`, or `coding`). See `workflow/model-policy.md`.

---

## How every platform runs the same flow

Cursor, Copilot, and Claude use this layout the same way:

1. Open **this folder** as the workspace.
2. The product injects `AGENTS.md` (plus `CLAUDE.md` or `.github/copilot-instructions.md` where that product requires those filenames).
3. The agent follows the shared `agents/`, `skills/`, `rules/`, and `docs/` tree.
4. Stage order and HITL are enforced by `scripts/workflow_runner.py` and `scripts/mcp_workflow_server.py`, not by chat memory.

Details: **`docs/flow.md`**. Domain docs index: **`docs/README.md`**.

---

# Knowledge session

**Speakable script** for a live walkthrough of this folder.

**How to use this section:** lines marked **Say** are spoken. **Ask** is a question to the room. **Demo** is something you open on screen. **Note** is for you, not the audience.

**Time:** about 50 minutes. Open `enterprise-agent-platform/` as the workspace before you start.

## Session flow (speak this as the agenda)

1. Why we bother with MD agents
2. The six pieces — say them out loud
3. Walk the sample repo
4. How Cursor, Copilot, and Claude *actually load* this project
5. Nested copies vs one shared tree — is this the best way?
6. Workflow, HITL, MCP — watch it stop for a human
7. What you can automate, what you must not
8. Recap you can reuse in interviews

---

## Block 1 — Why MD agents (8 min)

**Say**

Imagine we hire a very fast intern. We do not give a job description. We do not give a playbook. We do not give a manager. Then we say: migrate the monolith.

That intern is a generic coding chat.

**Ask**

What goes wrong in the first week?

**Wait.** Collect: invents business rules, changes APIs, tests its own work, says “done” in chat, Cursor copy diverges from Copilot.

**Say**

That is why we write Agent Markdown. Not because Markdown is magic. Because we want AI work to look like engineering:

- named roles
- written procedures
- standing rules
- domain facts in Git
- a file the next worker can read
- a human gate before irreversible steps
- tools with least privilege

**Say this contrast slowly**

Without MD agents: one chat does analyze, code, test, and self-approve. “Looks done” lives in the transcript.

With MD agents: requirements write a JSON file. A human approves. Architect writes a design file. A human approves. Developer may code. QA and security are different people. A human releases.

**Ask**

Do we need this to rename a variable?

**Say**

No. Use MD agents when more than one person, one tool, or one real risk is involved.

---

## Block 2 — Six pieces. Do not mix them. (6 min)

**Demo:** draw this, or use the diagrams at the top of this file.

```text
MODEL  →  AGENT  →  RULES + SKILLS + DOCS  →  MCP/TOOLS  →  ARTIFACT  →  WORKFLOW  →  HITL or NEXT AGENT
```

**Say each line. Pause.**

**Agent** — who is responsible. Architect. Developer. QA.

**Skill** — how this *kind* of work is done. A playbook. `skills/requirements-analysis/SKILL.md`.

**Rule** — what must always be true. Short. Stable. “Do not touch another service’s database.”

**Docs** — facts about *this* system. Pricing. Current APIs. Not instructions.

**Artifact** — the handoff file. `design.json`. Not a paragraph of chat.

**Workflow plus HITL** — who runs next, and where a human must decide.

**Say**

A model is not an agent.  
Agent equals model, plus instructions, plus tools, plus context, plus state, plus guardrails, plus a loop.

**Ask**

If a procedure is five hundred lines, is that a rule?

**Say**

No. That is a skill. A global rule that long will rot and fight every other task.

---

## Block 3 — Walk the sample (7 min)

**Demo:** tree in [Folder design](#folder-design), or this shorter view on screen.

```text
enterprise-agent-platform/
├── AGENTS.md              every IDE starts here
├── CLAUDE.md              Claude’s extra filename, points to AGENTS.md
├── agents/                who  — six job cards, one copy
├── rules/                 always-true
├── skills/                how-to  — five SKILL.md packages, one copy
├── docs/                  facts + flow.md
├── workflow/              order + HITL
├── scripts/               CLI + MCP, same engine
├── .cursor/mcp.json
├── .mcp.json
├── .vscode/mcp.json
└── .github/copilot-instructions.md
```

**Say**

Six agent *files* is not duplication. The pipeline has six jobs. The writer must not be the judge.

What we killed — and you saw it on screen — was four copies of `skills/`. Same five names under `.cursor`, `.github`, `.claude`, and root. That is a mesh. Copies diverge. We do not do that.

**Demo:** open `AGENTS.md`, then `agents/developer.md`, then `skills/implementation/SKILL.md`, then `docs/business-rules.md`.

**Say**

Watch the split. `AGENTS.md` says the law of the land. The developer file says *this worker’s* job. The skill says *how* to implement. Business rules live in docs. Nobody invents marketing opt-in.

**Demo:** `workflow/feature-development.yaml`.

**Say**

This is the manager. Requirements. Human. Architecture. Human. Implementation. QA. Security. Human. Done.

Markdown does not run that by itself. The YAML plus `scripts/workflow_runner.py` plus MCP do.

---

## Block 4 — How each platform loads this project (12 min)

This is the depth question. **There is no universal `agent.md` standard.** Each product looks in different places. Our sample chooses one shared tree and *tells* every product to read it.

### 4.1 The honest loading model

**Say**

Two ways an IDE “loads” an agent:

**Auto-discovery.** The product scans a magic folder. Cursor scans `.cursor/agents/`. Copilot scans `.github/agents/*.agent.md`. Claude scans `.claude/agents/`. Skills similarly: `.cursor/skills/`, `.github/skills/`, `.claude/skills/`, and a portable `.agents/skills/`.

**Instruction-driven load.** The product always loads `AGENTS.md` — or `CLAUDE.md`, or `.github/copilot-instructions.md`. That file says: open `agents/architect.md`, follow `skills/…`, obey `rules/…`. The main agent *reads those files* as context.

**Ask**

Which one does our sample use?

**Say**

Instruction-driven. On purpose. Auto-discovery is why people nest copies under every IDE. We refused that mesh.

So: Cursor, Copilot, and Claude all boot from a short entry file. Then they follow the same folders.

### 4.2 Cursor — step by step

**Say**

You open `enterprise-agent-platform` as the folder.

Cursor always looks for **`AGENTS.md`** at the repo root. That file is injected into the agent context. It is our constitution.

Cursor also loads **`.cursor/mcp.json`**. That starts the `enterprise-workflow` MCP server — `py -3 scripts/mcp_workflow_server.py`. Now the agent can call `workflow_status`, `run_next_agent`, `hitl_approve`.

Cursor *could* auto-load:

- `.cursor/rules/*.mdc` as project rules — we do not have those. Rules live in `rules/` and `AGENTS.md` says when to open `rules/backend.md`.
- `.cursor/skills/**/SKILL.md` or `.agents/skills/` — we keep skills at root `skills/`. The agent opens them because `AGENTS.md` and the job card name the path.
- `.cursor/agents/*.md` as named subagents in the picker — we do not have those. The orchestrator (or you) says “be the architect” and the model reads `agents/architect.md`.

**Demo:** `.cursor/mcp.json` and `AGENTS.md` side by side.

**Say**

If someone asks “does Cursor natively register `agents/architect.md` as a subagent?” the answer is **no**. Native subagents want `.cursor/agents/` with YAML frontmatter. We traded the dropdown for one source of truth.

That is a real tradeoff. We will come back to it.

### 4.3 GitHub Copilot / VS Code — step by step

**Say**

Copilot loads **`AGENTS.md`**. It also loads **`.github/copilot-instructions.md`**, which in our repo is four lines: follow `AGENTS.md`, shared folders, MCP is `.vscode/mcp.json`.

VS Code Agent / Copilot *could* auto-load:

- `.github/instructions/*.instructions.md` with `applyTo` globs — we folded that into `AGENTS.md` (“when editing `*.cs`, follow `rules/backend.md`”).
- `.github/agents/*.agent.md` with **handoffs** — those can auto-submit the next agent. We removed them so HITL cannot be skipped by `send: true`. Our HITL lives in the runner, not in a Copilot handoff.
- `.github/skills/` — deleted. Skills are `skills/` at root.

MCP: **`.vscode/mcp.json`**. Same Python server as Cursor. Different filename because VS Code looks here.

**Say**

So Copilot is not running a different methodology. It is wearing a different name tag to enter the same building.

### 4.4 Claude Code — step by step

**Say**

Claude always loads **`CLAUDE.md`**. Ours is four lines: follow `AGENTS.md`, same folders, MCP is `.mcp.json`.

Claude *could* auto-load `.claude/agents/`, `.claude/skills/`, `.claude/rules/`, and **hooks** that run after edits. We do not nest those. `CLAUDE.md` points at the shared tree. Optional hook would be “run `workflow_runner.py status` on stop” — we left it off so a missing run does not fail the session.

MCP: **`.mcp.json`** at the repo root. Same server again.

**Ask**

Why three MCP JSON files?

**Say**

Because the three products refuse to share one path. The *server* is one file: `scripts/mcp_workflow_server.py`. Config is glue, not knowledge.

### 4.5 What happens when you type a request

**Say this as a story. Demo the files in order.**

User: “Implement customer notification preferences.”

1. IDE injects `AGENTS.md` (and `CLAUDE.md` or Copilot instructions).
2. Model reads: pipeline, HITL, role map.
3. Orchestrator path: read `agents/orchestrator.md`, call MCP `start_feature_run` or CLI `start`.
4. `state.json` says current stage is `requirements`.
5. Model opens `agents/requirements.md` and `skills/requirements-analysis/SKILL.md` and `docs/business-rules.md`.
6. It writes `artifacts/runs/customer-notification/requirements.json`.
7. Stage becomes HITL. `run_next_agent` **stops**.
8. A human runs `approve` or MCP `hitl_approve`.
9. Next, `agents/architect.md`. Same pattern.
10. Developer **refuses** to edit code until `approvals/design.json` is `approved`.
11. QA and security are read-only. Release HITL is last.

**Say**

If you skip the runner and only chat, you still *should* follow the files. You *can* cheat. The runner is what makes cheating visible. That is the point of artifacts plus state.

### 4.6 What is native vs what we simulate

| Capability | Native in the IDE | In this sample |
|------------|-------------------|----------------|
| Project instructions | `AGENTS.md` / `CLAUDE.md` / Copilot instructions | Yes, used |
| Subagent picker | `.cursor/agents`, `.github/agents`, `.claude/agents` | **Not used** — job cards in `agents/` |
| Auto skills packages | `.cursor/skills`, `.agents/skills`, `.github/skills` | **Not used** — `skills/` named in AGENTS.md |
| Glob rules | `.mdc` / `applyTo` | Folded into AGENTS.md |
| HITL pipeline | Not universal | Python + MCP |
| Handoffs auto-send | Copilot `handoffs.send` | Off — would skip HITL |

**Say**

Do not tell the room “Cursor loads `agents/` automatically.” Tell them “Cursor loads `AGENTS.md`, and `AGENTS.md` loads `agents/`.” Precision matters.

---

## Block 5 — Nested structure: is this the best way? (8 min)

**Ask**

Why did we ever nest `skills` under `.cursor`, `.github`, and `.claude`?

**Say**

Because each vendor documented a magic folder. The internet copy-pasted it three times. That is how you get four `skills` trees.

### 5.1 Three layouts. Name them.

**Layout A — Nested per IDE (the mesh)**

```text
.cursor/agents  skills  rules
.github/agents  skills  instructions
.claude/agents  skills  rules
```

**Pros:** native picker, native skill attach, glob rules fire without asking the model.  
**Cons:** four copies. They drift. A business rule in `.cursor` never reaches Claude.

**Layout B — Shared tree, instruction-driven (this sample)**

```text
agents/   rules/   skills/   docs/   workflow/
AGENTS.md
tiny MCP JSON per IDE
```

**Pros:** one source of truth. Git review is simple. Same methodology on every laptop.  
**Cons:** no native subagent dropdown unless you add adapters back. Root `skills/` is not in Cursor’s auto-discover list. You depend on the model obeying `AGENTS.md`.

**Layout C — Hybrid (best of both, still no mesh)**

```text
agents/  rules/  skills/  docs/     ← only copy of knowledge
.agents/skills → same skills        ← optional portable discover path
.cursor/agents/*.md                 ← 8-line frontmatter: "follow agents/architect.md"
```

**Pros:** picker works; knowledge still does not fork.  
**Cons:** a few stub files. Discipline required: stubs must never grow a second business rule.

### 5.2 What I would tell an architecture review

**Say**

For **knowledge** — agents, skills, rules, docs — Layout B is the right enterprise default. We already paid the cost of the mesh. Do not go back.

For **runtime UX** — if the team lives in Cursor and wants `/architect` in the subagent list — Layout C. Stubs only. No second `SKILL.md`.

For **skills auto-attach** across Cursor, Copilot, and Claude, the industry is converging on **`.agents/skills/`**. If we outgrow “the model opens `skills/` because AGENTS.md said so,” we *move* the one skills tree there. We do not copy it.

**Ask**

Is nested ever “very best”?

**Say**

Nested is best only for *filenames the product requires* — `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, three MCP JSON paths. Nested is worst for *knowledge*. That is the whole session in one sentence.

---

## Block 6 — Workflow, HITL, MCP (8 min)

**Demo:** speak while you run, or show the commands.

```powershell
cd enterprise-agent-platform
py -3 scripts/workflow_runner.py start --feature customer-notification
py -3 scripts/workflow_runner.py run
```

**Say**

It wrote requirements. It **stopped**. Current stage is a HITL gate. `run` again will not invent an architect. That is HITL.

```powershell
py -3 scripts/workflow_runner.py approve --by "you" --comment "requirements ok"
py -3 scripts/workflow_runner.py run
```

**Say**

Now architecture. Another gate before code. Reject sends you back. Release approve is refused if QA failed or `release_allowed` is false.

**MCP tools, say them**

`start_feature_run` — create state.  
`run_next_agent` — next specialist, then stop at HITL.  
`workflow_status` — where are we.  
`hitl_approve` / `hitl_reject` — **human only**. The model must not approve itself.  
`read_artifact` / `read_project_doc` — inspect, do not guess.

**Say**

Sequential is the sample: each stage needs the previous file. Parallel is for independent analysis — API, DB, frontend at once — then join, then HITL. Do not parallelize “code” with “design not approved.”

**Ask**

Who owns order — the architect agent or the YAML?

**Say**

In this sample, the YAML and the runner. Agents do work. The workflow owns sequence, retries, and gates. That is how you stay auditable.

---

## Block 7 — Automate work, not decisions (4 min)

**Say**

Automate: inventories, draft plans, code from an approved design, tests, SAST, PR notes.

Keep humans: service boundaries, breaking APIs, production, security exceptions, inventing a missing business rule.

**Say the evidence rule**

FACT. EVIDENCE. INFERENCE. UNKNOWN.  
If you cannot prove it from code, tests, docs, or runtime — you do not invent it. You stop.

**Say least privilege**

Architect reads. Developer writes code, not production. QA runs tests, does not rewrite the feature. Security scans. Release deploys only after HITL.

Never put secrets in `SKILL.md` or `AGENTS.md`.

---

## Block 8 — Recap they can speak (3 min)

**Say, slowly**

An Agent Markdown architecture is roles, skills, rules, docs, MCP tools, artifacts, and workflow state — so a coding runtime can run an engineering process with specialists, gates, and handoffs.

Shorter: we do not ship a pile of prompts. We ship job cards with contracts.

**Ask the room to repeat**

Knowledge is shared. Filenames are local. HITL is a file, not a vibe.

**If someone asks for the interview line, give them this**

> Markdown configures the worker. The IDE runs it. MCP is what it can call. Artifacts are how workers talk. HITL is where people stay in charge.

**Close**

Open `docs/flow.md` after this session. Run the CLI once. Then try the same feature in Cursor and in Copilot. If the artifacts match, the architecture worked.

---

## Facilitator appendix (do not speak unless asked)

### Sample commands

```powershell
py -3 scripts/workflow_runner.py start --feature customer-notification
py -3 scripts/workflow_runner.py status
py -3 scripts/workflow_runner.py run
py -3 scripts/workflow_runner.py approve --by "jane" --comment "ok"
py -3 scripts/workflow_runner.py reject --by "jane" --comment "missing opt-out"
```

### Role map in this repo

| Stage | File | Skill |
|-------|------|--------|
| Orchestrator | `agents/orchestrator.md` | — |
| Requirements | `agents/requirements.md` | `skills/requirements-analysis` |
| Architect | `agents/architect.md` | `skills/architecture-design` |
| Developer | `agents/developer.md` | `skills/implementation` |
| QA | `agents/qa-reviewer.md` | `skills/qa-review` |
| Security | `agents/security-reviewer.md` | `skills/security-analysis` |

Each job card also sets a `model:` class (`fast`, `high-reasoning`, or `coding`). See `workflow/model-policy.md`.

### Official docs (if someone wants links)

- Cursor Agent / Rules / Skills / Subagents: https://cursor.com/docs
- VS Code custom agents / AGENTS.md: https://code.visualstudio.com/docs/agent-customization/custom-agents
- Copilot custom agents and skills: https://docs.github.com/en/copilot
- Claude Code subagents and hooks: https://code.claude.com/docs
- MCP: https://modelcontextprotocol.io

### Anti-patterns (one-liners)

One mega-agent. Fifty “helpful” clones. Self-approval. Chat-only handoff. Business rules only in `.cursor`. Four copies of `skills/`. Auto `hitl_approve`. Secrets in Markdown.
