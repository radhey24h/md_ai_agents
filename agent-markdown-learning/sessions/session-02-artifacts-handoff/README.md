# Session 02 — Artifact & Handoff

## Objective

Show why the next worker must read a **file**, not the previous chat.

## What you will learn

- Artifact vs conversation
- Handoff
- Why state belongs on disk

## Prerequisites

Session 01.

## How it works

```text
ANALYST (write) → artifacts/analysis.json → PLANNER (read only that file)
```

Chat = conversation. Artifact = durable handoff.

| | Chat | Artifact |
|--|------|----------|
| Lives | Session buffer | Git / disk |
| Next agent | Often cannot see it | Always can |
| Audit | Weak | Strong |

State here is: analysis complete; path is `artifacts/analysis.json`. Still no workflow engine. Handoff is a **convention**: the planner job card names the file.

## Folder structure

```text
agents/analyst.md
agents/planner.md
skills/write-analysis/SKILL.md
rules/no-invent.md
docs/notification-facts.md
artifacts/analysis.json
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

Analyst finishes → writes JSON → planner starts with an empty chat but a full artifact.

## Expected output

Teaching sample is already in `artifacts/analysis.json`. Evidence is **paths into eShop** (`http.py`, `notifications.py`, `db.py`, `settings.html`, `warehouse.html`, tests). `unknowns` still lists SMS / push / locales.

## What to observe

Planner must not ask “what did we decide in chat?”

## Common mistakes

Passing a 4,000-word transcript. Two agents expecting different filenames.

## Interview takeaway

1. “Agents should hand off **artifacts**, not conversation transcripts.”
2. “An artifact is durable, reviewable, and the next stage’s input contract.”
3. “If the next agent needs hidden chat context, the architecture already failed.”

## Next session

[Session 03 — Sequential](../session-03-sequential/README.md)
