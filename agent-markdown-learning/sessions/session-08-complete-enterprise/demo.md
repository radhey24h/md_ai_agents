# Walkthrough — Session 08

Same feature as Session 01 — Customer Notification Preferences — now with a manager, specialists, joins, and humans. Open `../../examples/customer-notification/README.md`, then `workflow/enterprise.yaml`. SMS must still be UNKNOWN. Docs and rules survived the whole journey; nobody invented a channel along the way.

Live run. Name the human at each gate. From this folder:

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

Discovery fans out, then HITL. Requirements and design each stop for a person. Implementation cannot run before design HITL — the runner refuses. QA and security join, then release HITL. `status` should end at `completed`.

That is the course in one run: roles, skills, rules, artifacts, workflow state, tools as a layer, guardrails, and humans — not a pile of prompts.
