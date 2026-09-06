# Demo — Session 07

### Say

The orchestrator is a traffic cop, not a superhero developer.

### Demo

`agents/orchestrator.md` vs `agents/developer.md`.

### Ask

If the orchestrator uses the strongest model, should it get deploy permission?

### Expected

No. Model ≠ privilege.

### Explain

Least privilege.

---

### Say

QA and security after code: parallel, then join, then human.

### Demo

```powershell
cd sessions/session-07-multi-agent
py -3 run_multi.py
```

### Ask

Did developer write qa.json?

### Expected

No. Separate files, separate agents.

### Explain

Writer ≠ judge.

---

### Say

Session 08 runs the same story as one labeled enterprise demo with the full diagram.
