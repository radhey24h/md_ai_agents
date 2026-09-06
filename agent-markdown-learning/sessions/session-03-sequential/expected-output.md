# Expected output — Session 03

After four successful `run_sequential.py` calls:

```text
artifacts/state.json              currentStage: completed
artifacts/requirements.json
artifacts/design.json             requires requirements.json
artifacts/implementation.json     requires design.json
artifacts/qa.json
```

Skip-ahead:

```text
ERROR: cannot run developer; current stage is requirements (or architecture)
```
