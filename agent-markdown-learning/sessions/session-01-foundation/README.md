# Session 01 — Agent / Skill / Rule / Doc

## Objective

Teach the four pieces that people mix up: **who**, **how**, **must**, and **facts**. One tiny agent. No workflow, MCP, HITL, or parallelism.

## What You Will Learn

- What an Agent Markdown file is (and is not)
- Why a Skill is not a Rule
- Why Docs are not instructions
- FACT / EVIDENCE / INFERENCE / UNKNOWN

## Prerequisites

None. Read the root [glossary.md](../../glossary.md) if terms are new.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
session-01-foundation/
  agents/customer-analyst.md
  skills/customer-analysis/SKILL.md
  rules/no-invent.md
  docs/notification-facts.md
  artifacts/   (empty until you write notes)
```

## Step-by-Step Demo

Follow [demo.md](demo.md). Short version:

### Step 1

Open `agents/customer-analyst.md`. That is **who**.

### Step 2

Open `skills/customer-analysis/SKILL.md`. That is **how**.

### Step 3

Open `rules/no-invent.md` and `docs/notification-facts.md`. **Must** vs **facts**. Walk a user request through all four.

## What Happens Internally

The runtime (you, or an IDE) loads the agent file. A careful worker then follows the skill, obeys the rule, and reads the doc. Nothing here starts the next agent.

## Expected Output

See [expected-output.md](expected-output.md). Informal analysis with labeled unknowns — not JSON yet.

## What to Observe

SMS is not in the docs. The analyst must say UNKNOWN, not invent it.

## Common Mistakes

- Putting the whole playbook in the agent file
- Calling a long procedure a “rule”
- Treating Confluence-style docs as executable workflow

## Questions to Ask During the Demo

See [demo.md](demo.md) **Ask** lines.

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 02 — Artifact & Handoff](../session-02-artifacts-handoff/README.md)
