# Demo — Session 03

### Say

Four specialists. One manager: the YAML. The architect does not run the factory.

### Demo

`workflow/sequential.yaml`

### Ask

If I delete the YAML and keep the four agent files, do they still run in order?

### Expected

Not by themselves.

### Explain

A collection of `.md` files is not a workflow engine.

---

### Say

We will use a tiny teaching script. This is not Cursor.

### Demo

```powershell
cd sessions/session-03-sequential
py -3 run_sequential.py
py -3 run_sequential.py
py -3 run_sequential.py skip-to-developer
```

### Ask

Did skip-to-developer work?

### Expected

No. Error: architecture not complete.

### Explain

That is dependency. Retry = run the script again on the current failed stage, not a full reset, unless you delete state.

---

### Say

Next session: API, DB, and UI analysis do not wait on each other.
