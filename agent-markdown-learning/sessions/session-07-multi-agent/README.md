# Session 07 — Many jobs, writer is not the judge

## In this session

**Office analog:** A traffic cop sequences specialists. The person who writes the code does not also certify QA.

**We are doing:** One orchestrator. Developer must not write `qa.json`. Script stops until a human is treated as having signed.

**We are not doing:** One mega-agent that codes, tests, and ships. Extra permissions for the “smartest” model.

**How to check:**

```powershell
py -3 run_multi.py
```

Writes discovery + requirements then **STOPS**. Then:

```powershell
py -3 run_multi.py --approve-demo
```

Design, implementation, qa, security, join. Developer file must not be the author of `qa.json`.

## Why

If the same agent implements the skip-email path and also certifies it, that is marking its own homework.

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. Orchestrator sequences; it does not replace specialists.
2. Writer ≠ judge.
3. Permissions follow the role, not model size.

## Next

[Session 08](../session-08-complete-enterprise/README.md) — same shop, every gate named.
