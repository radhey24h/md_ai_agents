# Session 08 walkthrough

## The problem

Session 01 was one analyst and a question about SMS. If you jump straight to “enterprise multi-agent,” nobody remembers why the files exist.

This folder is the **same product** — customer notification preferences — with everything from Sessions 01–07: discovery in parallel, humans on requirements/design/release, developer only after design, QA and security independent. It is a classroom runner, not production Cursor.

The test that you understood the course: **SMS is still UNKNOWN.** Nobody invented a channel to look complete.

## What to do

1. Open `../../eShop-customer-notification/README.md` (Maya vs Omar, email only) and `workflow/enterprise.yaml`.  
   Confirm `notifications.py` skips opt-out and `http.py` has no SMS route. Warehouse ships Omar without email.

2. Run the path. Say the human’s name at each approve so it does not feel like the script approved itself:

   ```powershell
   cd sessions/session-08-complete-enterprise
   py -3 run_enterprise.py start
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate discovery --by "alex"
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate requirements --by "alex"
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate design --by "alex"
   py -3 run_enterprise.py run
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate release --by "alex"
   py -3 run_enterprise.py status
   ```

   What the machine is doing: API/DB/UI together → join → human → requirements → human → architecture → human → code → QA and security together → join → human → release. Developer **cannot** sneak in before design HITL.

3. Open `artifacts/requirements.json`. `unknowns` should still include SMS. `status` should be `completed` only after the last approve.

## The point

**A production-shaped system is not a pile of prompts.** It is roles, skills, rules, artifacts, workflow state, tool access, and human gates — and it still must not invent the product.
