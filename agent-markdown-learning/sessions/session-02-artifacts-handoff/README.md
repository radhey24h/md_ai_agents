# Session 02 — Artifact & Handoff

## Objective

Show why the next worker must read a **file**, not the previous chat.

## What You Will Learn

- Artifact vs conversation
- Handoff
- Why state belongs on disk

## Prerequisites

Session 01.

## Concepts

See [concept.md](concept.md). Chat = conversation. Artifact = durable handoff.

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
agents/analyst.md
agents/planner.md
skills/write-analysis/SKILL.md
rules/no-invent.md
docs/notification-facts.md
artifacts/analysis.json
```

## Step-by-Step Demo

### Step 1

Show `agents/analyst.md` output path: `artifacts/analysis.json`.

### Step 2

Open the JSON. Point at `unknowns` and `evidence`.

### Step 3

Show `agents/planner.md`: it lists **only** that JSON as input. Hide the chat.

Full script: [demo.md](demo.md).

## What Happens Internally

Analyst finishes → writes JSON → planner starts with an empty chat but a full artifact.

## Expected Output

See [expected-output.md](expected-output.md) and `artifacts/analysis.json`.

## What to Observe

Planner must not ask “what did we decide in chat?”

## Common Mistakes

Passing a 4,000-word transcript. Two agents expecting different filenames.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 03 — Sequential](../session-03-sequential/README.md)
