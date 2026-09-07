# Session 05 walkthrough

## The problem

Requirements look “good enough.” The model writes `approved: true` on its own homework and the architect starts. That is not governance. That is the intern marking their own exam.

Human-in-the-loop means the **run actually stops**. A sentence in a prompt (“please get a human”) does nothing. You need a gate: no next agent until a named person records approve or reject.

Use this for things you cannot undo cheaply: architecture, missing business rules, breaking APIs, security exceptions, production.

## What to do

1. Show that it **stops**:

   ```powershell
   cd sessions/session-05-hitl
   py -3 run_hitl.py start
   py -3 run_hitl.py run
   py -3 run_hitl.py run
   ```

   First `run` writes requirements. Second `run` prints STOP. There is no `design.json` yet. The architect did not secretly continue.

2. Show **approve** (a person named alex):

   ```powershell
   py -3 run_hitl.py approve --by "alex" --comment "email-only is enough"
   py -3 run_hitl.py run
   ```

   Open `approvals/requirements.json`. Status is approved, with a human name. Then design appears.

3. Show **reject** (start a fresh run):

   ```powershell
   py -3 run_hitl.py start
   py -3 run_hitl.py run
   py -3 run_hitl.py reject --by "alex" --comment "need explicit opt-out wording"
   py -3 run_hitl.py run
   ```

   Work goes **back to requirements**, not forward to release. Reject is “fix this,” not “ship anyway.”

## The point

**The model must never approve its own output.** HITL is a stopped runner plus a signed file.

## Next

Session 06 is tools. `hitl_approve` can be a tool name — it still must not be called by the model for its own work.
