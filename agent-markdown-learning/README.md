# Agent Markdown Learning

Two things live in this folder. Mix them up and the course feels like nonsense.

| Layer | What it is | What you do with it |
|-------|------------|---------------------|
| **The shop** | A tiny store that emails when a mug ships | Click it. Prove C-1002 gets no email. |
| **The course** | Eight sessions on how AI workers should behave | Open Markdown, run a small Python script, see a file appear or a command fail |

You are **not** building a new shop. You are practicing **how a team of AI workers should work on this existing shop** — like job cards, tickets, a factory line, a manager’s signature.

Start at [Session 01](sessions/session-01-foundation/README.md). Map: [learning-path.md](learning-path.md). Shop: [eShop-customer-notification](eShop-customer-notification/README.md).

---

## The shop (one minute)

Two customers each ordered a mug. Warehouse clicks **Ship**.

| Customer | Order | Email setting | What happens |
|----------|--------|----------------|--------------|
| C-1001 | ORD-501 | On | Mug ships **and** they get an email |
| C-1002 | ORD-502 | Off | Mug still ships. **No email.** |

That “off” is **email opt-out**. C-1002 said “don’t email me.” The shop already does this. There is no second product.

**SMS** means phone texts. This shop does not send texts. If a chat says “add SMS opt-out,” the honest answer is “we only have email.” That is not the homework.

Prove the shop:

```powershell
cd eShop-customer-notification/app
py -3 -m unittest discover -s tests -v
py -3 -m shop
```

Then: http://127.0.0.1:8080/warehouse → ship ORD-502 (C-1002) → http://127.0.0.1:8080/api/outbox → `"status": "skipped_opt_out"`.

---

## The course (what each session is for)

Office analog: a team is about to change this shop. Each session is one team habit.

| Session | Office analog | You will know it worked when |
|---------|---------------|------------------------------|
| [01](sessions/session-01-foundation/README.md) | Don’t dump job, playbook, policy, and wiki into one prompt | You can point at four files: who / how / must / facts |
| [02](sessions/session-02-artifacts-handoff/README.md) | Hand the next person a ticket, not a Slack thread | `analysis.json` has real shop file paths; planner reads only that file |
| [03](sessions/session-03-sequential/README.md) | Don’t code before design exists | `skip-to-developer` **errors** |
| [04](sessions/session-04-parallel/README.md) | Three people can read API, DB, UI at once | Three JSON files plus a join; architect+developer together **errors** |
| [05](sessions/session-05-hitl/README.md) | A named person must sign before design | Second `run` **STOPS** until you approve |
| [06](sessions/session-06-mcp/README.md) | The job card is not the toolbox | Demo lists tools and **refuses** model self-approve |
| [07](sessions/session-07-multi-agent/README.md) | Traffic cop + specialists; coder is not QA | Run stops; developer did not write `qa.json` |
| [08](sessions/session-08-complete-enterprise/README.md) | Same shop, full company-shaped path | `status` is `completed` only after named approves |

Markdown does not run the pipeline. A runtime does (you, an IDE, or these teaching scripts).

---

## Picture of the pieces

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
                                ▼
                         ┌──────────────┐
                         │   WORKFLOW   │
                         │    ORDER     │
                         └──────┬───────┘
                    ┌───────────┴───────────┐
                    ▼                       ▼
                 SEQUENTIAL              PARALLEL
                    └───────────┬───────────┘
                                ▼
                              HITL
                                │
                                ▼
                              MCP (tools)
```

---

## Who is this for?

Developers, leads, architects, AI engineers, managers learning agentic architecture. Each session README has interview-ready lines.

## Prerequisites

- Read Markdown (and a little JSON/YAML)
- Python 3.10+ (`py -3` on Windows) for the shop tests and later demo scripts
- No ML background

## How to use it

1. Prove the shop once (commands above).
2. Do sessions 01 → 08. Each `README.md` is “what / how to check.” Each `demo.md` is the click-path.
3. Do not start at Session 08.

---

## Glossary

| Term | Meaning here |
|------|----------------|
| **Model** | The reasoning engine. Not the agent. |
| **Agent** | Who does the work (role, inputs, outputs, never-dos). |
| **Skill** | How a *type* of work is done (playbook). |
| **Rule** | Short standing constraint. |
| **Doc** | Facts. Not instructions. |
| **Artifact** | Durable file the next worker reads. Not the chat. |
| **Handoff** | Passing that file (and often a status). |
| **Workflow** | What runs next, in what order. |
| **Sequential** | B waits for A. |
| **Parallel** | Independent work, then a **join**. |
| **HITL** | Human-in-the-loop. Stop until approve or reject. |
| **MCP** | Standard plug for tools. |
| **Orchestrator** | Sequences specialists. Does not do their jobs. |
| **FACT / EVIDENCE / UNKNOWN** | Proven / where you saw it / not proven — do not invent. |

---

## Execution decisions

| Situation | Execution |
|-----------|-----------|
| Requirements → Architecture | Sequential |
| Architecture → Development | Sequential |
| API + DB + UI discovery | Parallel |
| QA + Security | Parallel |
| Release after QA | Sequential |
| Human decision | Gate (HITL) |

```text
Dependency exists → Sequential
No dependency → Parallel
Risk/decision exists → HITL
External capability required → MCP
Persistent communication → Artifact
```

## Least privilege

| Role | Allowed | Not allowed |
|------|---------|-------------|
| Architect | Read, analyze, design | Change app code, deploy |
| Developer | Change app code after design HITL | Approve own work |
| QA | Run tests, write verdict | Modify production code |
| Security | Analyze, set `release_allowed` | Act as the human approver |
| Orchestrator | Sequence, read state | Do specialist design/code |

Smarter **models** do not get extra **permissions**.

## Native vs demonstration

| Concern | Native IDE | This curriculum |
|---------|------------|-----------------|
| Job cards as files | Yes, if the product loads them | Teaching files in each session |
| Guaranteed HITL stop | Not reliable across products | Session 5+ **scripts** stop until you approve |
| MCP | Product loads a configured server | Session 6 tiny teaching server |

A folder of `.md` files is not a workflow engine.

## Evidence (shop)

```text
FACT:      Shipping emails exist. C-1002 with email off is not mailed.
EVIDENCE:  eShop-customer-notification/app/shop/services/notifications.py
UNKNOWN:   Any channel not in the app (there is no SMS).
```
