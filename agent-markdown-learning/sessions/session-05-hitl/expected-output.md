# Expected output — Session 05

After requirements + STOP:

```text
artifacts/requirements.json
artifacts/state.json     current: approval-requirements
```

After approve:

```text
approvals/requirements.json   status: approved, approved_by: alex
artifacts/design.json
```

After reject: current stage is `requirements` again. Comment stored on the rejection file.
