# Concept — Session 03

```text
Requirements → Architect → Developer → QA
```

| Idea | Meaning |
|------|---------|
| Sequence | Fixed order |
| Dependency | Developer needs `design.json` |
| State | `artifacts/state.json` current stage |
| Handoff | Each stage writes a JSON file |
| Failure | `status: FAIL` stops the pipeline |
| Retry | Re-run the **same** stage; do not restart from requirements unless the workflow says so |

Markdown files do not enforce this. `run_sequential.py` does (teaching runtime).
