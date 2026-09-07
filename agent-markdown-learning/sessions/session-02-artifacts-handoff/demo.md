# Session 02 walkthrough

## The problem

The analyst did good work yesterday — in a chat window. Today a planner starts. They were on leave. They cannot scroll your Cursor thread. If the only record is conversation, the planner will guess, re-ask, or invent SMS again.

Chat is a meeting. The next worker needs a **document**, the way a ticket needs a written spec.

## What to do

1. Open `agents/analyst.md`, then `artifacts/analysis.json`.  
   The analyst’s job ends when that JSON exists. `evidence` must be **paths into eShop** (`http.py`, `notifications.py`, …). SMS stays in `unknowns` because those files do not implement it.

2. Open `agents/planner.md` and read **Inputs**.  
   It says: only `artifacts/analysis.json`. Not “remember what we said.” If SMS was discussed verbally but missing from the JSON, the **analyst** failed. The planner is not allowed to “just know.”

3. Imagine deleting the chat history and keeping only `analysis.json`.  
   The planner should still be able to draft a plan and leave SMS as an open question for a human.

## The point

**Agents talk through artifacts, not through chat memory.** If the next stage needs a hidden conversation, the architecture already failed.

## Next

Two people and one filename is still a handshake. Session 03 makes order *enforceable* so the developer cannot start before design exists.
