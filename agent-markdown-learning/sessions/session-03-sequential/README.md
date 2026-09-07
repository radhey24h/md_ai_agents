# Session 03 — Don’t code before design

## In this session

**Office analog:** Requirements, then architecture, then code, then QA. The intern cannot “just start coding.”

**We are doing:** A teaching script that **blocks** skip-ahead. It writes JSON stand-ins (it does not edit the shop yet).

**We are not doing:** Parallel work. Human approval. Changing eShop in this session.

**How to check:** From this folder:

```powershell
py -3 run_sequential.py skip-to-developer
```

That **errors** while you are still on requirements. After four normal `run`s you have four JSON files and `state.json` says completed.

## Why

If you only *ask* the model to go in order, Friday it starts coding before anyone designed. QA then tests a design that never existed.

## How it works

```text
YAML order: requirements → architecture → implementation → qa
Enforcer:   run_sequential.py  (teaching runtime, not Cursor)
```

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. Workflow owns sequence; agents do not pick the factory order.
2. Developer must not start until architecture output exists.
3. Retry the failed stage; do not blindly restart everything.

## Next

[Session 04](../session-04-parallel/README.md) — API, database, and screens can be read at the same time.
