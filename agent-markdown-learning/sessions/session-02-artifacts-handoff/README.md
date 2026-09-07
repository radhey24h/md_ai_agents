# Session 02 — Hand the next person a file

## In this session

**Office analog:** Yesterday’s meeting is gone. Today’s planner was not in the room. They need a ticket, not “remember the chat.”

**We are doing:** Analyst writes `artifacts/analysis.json`. Planner is allowed to read **only that file**.

**We are not doing:** Using chat as the spec. A four-stage factory yet.

**How to check:** Open `artifacts/analysis.json`. `evidence` lists real eShop paths (`http.py`, `notifications.py`, …). Open `agents/planner.md` → Inputs list only `analysis.json`.

## Why

Without a file, the next worker guesses. Guessing is how fake features appear.

## How it works

```text
Analyst writes analysis.json  →  Planner reads only that file
```

Chat = meeting. Artifact = the ticket.

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. Hand off **artifacts**, not transcripts.
2. The artifact is the next stage’s contract.
3. If the next agent needs hidden chat, the architecture failed.

## Next

[Session 03](../session-03-sequential/README.md) — four stages; the developer cannot skip the line.
