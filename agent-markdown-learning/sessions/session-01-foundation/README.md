# Session 01 — Agent / Skill / Rule / Doc

## Objective

Teach the four pieces that people mix up: **who**, **how**, **must**, and **facts**. One tiny agent. No workflow, MCP, HITL, or parallelism.

## What you will learn

- What an Agent Markdown file is (and is not)
- Why a Skill is not a Rule
- Why Docs are not instructions
- FACT / EVIDENCE / INFERENCE / UNKNOWN

## Prerequisites

None. Terms: [root glossary](../../README.md#glossary).

## How it works

Single worker. No pipeline. The model reasons. The agent file says who it is. Markdown does not “run” the analysis by sitting in a folder.

| Piece | Question | In this folder |
|-------|----------|----------------|
| Agent | Who performs the work? | `agents/customer-analyst.md` |
| Skill | How should this type of work be done? | `skills/customer-analysis/SKILL.md` |
| Rule | What must always be true? | `rules/no-invent.md` |
| Doc | What facts are known? | `docs/notification-facts.md` |

```text
MODEL  →  AGENT (Customer Analyst)
              ├── SKILL  customer-analysis
              ├── RULE   do not invent
              └── DOC    notification facts
                        ↓
                   analysis notes
```

Permissions: read docs and the eShop app only. No next agent. No tools.

## Folder structure

```text
agents/customer-analyst.md
skills/customer-analysis/SKILL.md
rules/no-invent.md
docs/notification-facts.md
artifacts/   (notes after you write them)
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

The runtime (you, or an IDE) loads the agent file. A careful worker follows the skill, obeys the rule, and reads the doc. Nothing here starts the next agent.

## Expected output

Conceptual (you may type this by hand). Not a workflow contract yet.

```text
FACT: Email opt-in/out is implemented per customer. Ship skips opted-out buyers.
EVIDENCE: app/shop/services/notifications.py skipped_opt_out; app/shop/db.py email_enabled.
INFERENCE: Preference sits on the customer, not on the warehouse job.
UNKNOWN: SMS / push / locales — not in the app.

Do not add SMS. Do not invent routes that are not in app/shop/api/http.py.
```

A filled example lives at `artifacts/sample-analysis-notes.md`.

## What to observe

SMS is not in the app. The analyst must say UNKNOWN, not invent it.

## Common mistakes

- Putting the whole playbook in the agent file
- Calling a long procedure a “rule”
- Treating Confluence-style docs as executable workflow

## Interview takeaway

1. “An agent file names **who** does the work; it is not a running process by itself.”
2. “A **skill** is a reusable how-to; a **rule** is a short standing constraint.”
3. “**Docs** hold system facts. I do not hide the only copy of a business rule inside an IDE-specific agent file.”
4. “If I cannot prove a behavior, I label it UNKNOWN instead of inventing it.”

## Next session

[Session 02 — Artifact & Handoff](../session-02-artifacts-handoff/README.md)
