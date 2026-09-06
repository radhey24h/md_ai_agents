# Architecture — Session 03

```text
WORKFLOW sequential.yaml
    → requirements agent → requirements.json
    → architect          → design.json
    → developer          → implementation.json
    → qa                 → qa.json
```

Least privilege (conceptual): only developer “implements.” QA is read-only.
