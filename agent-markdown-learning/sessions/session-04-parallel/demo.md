# Demo — Session 04

### Say

Three people can open the repo at once. None needs the others’ JSON first.

### Demo

`workflow/parallel.yaml` and the three agent files.

### Ask

Does UI analysis need `api-analysis.json`?

### Expected

Not in this teaching example.

### Explain

No dependency → parallel.

---

### Say

The consolidator must wait.

### Demo

```powershell
cd sessions/session-04-parallel
py -3 run_parallel.py
```

Show four JSON files.

### Ask

Could we start the consolidator after only API analysis?

### Expected

No. Join is `all`.

### Explain

Downstream would be incomplete.

---

### Say

Illegal pairing.

### Demo

`py -3 run_parallel.py illegal`

### Expected

Error: Developer depends on Architecture.

### Explain

Dependency exists → sequential (and later HITL).
