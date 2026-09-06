# Demo — Session 08

### Say

Same feature as Session 01. Now it has a manager, specialists, joins, and humans.

### Demo

`../../examples/customer-notification/README.md` then `workflow/enterprise.yaml`.

### Ask

Did we invent SMS between Session 1 and Session 8?

### Expected

No. UNKNOWN remains.

### Explain

Docs and rules survived the journey.

---

### Say

Live run. Name the human out loud at each gate.

### Demo

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

### Ask

Could the developer command have run before design HITL?

### Expected

The runner refuses.

### Explain

That is the whole course.

---

### Say

Close: production needs roles, skills, rules, artifacts, state, tools, guardrails, humans — not a pile of prompts.
