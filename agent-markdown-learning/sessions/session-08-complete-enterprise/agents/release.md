---
name: release
description: Record release after QA+security join and human HITL. Does not deploy without the gate.
---
Read `qa.json`, `security.json`, and `approvals/release.json`. Write `artifacts/release.json`.
Do not invent production steps. Do not self-approve.
