# Demo — Session 05

### Say

High-risk step: accepting requirements. A person signs. Not the model.

### Demo

```powershell
cd sessions/session-05-hitl
py -3 run_hitl.py start
py -3 run_hitl.py run
py -3 run_hitl.py run
```

Second `run` should STOP.

### Ask

Did the architect already run?

### Expected

No.

### Explain

That is a real gate.

---

### Say

Approve path.

### Demo

```powershell
py -3 run_hitl.py approve --by "alex" --comment "email-only is enough"
py -3 run_hitl.py run
```

### Expected

`approvals/requirements.json` status approved. Architect artifact appears.

---

### Say

Reject path (start a new run or reset).

### Demo

```powershell
py -3 run_hitl.py start
py -3 run_hitl.py run
py -3 run_hitl.py reject --by "alex" --comment "need explicit opt-out wording"
py -3 run_hitl.py run
```

### Expected

Back to requirements stage.

### Explain

Reject is not “skip to release.”

---

### Say

HITL also belongs on security exceptions and production. Next: tools (MCP), still with human-only approve.
