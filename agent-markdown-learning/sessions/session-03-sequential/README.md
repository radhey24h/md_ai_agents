# Session 03 — Sequential Agents

## Objective

**Agents perform work. The workflow controls order.** Developer cannot run before Architecture.

## What you will learn

Sequence, dependencies, state, handoff, failure, retry.

## Prerequisites

Session 02.

## How it works

```text
WORKFLOW sequential.yaml
    → requirements agent → requirements.json
    → architect          → design.json
    → developer          → implementation.json
    → qa                 → qa.json
```

| Idea | Meaning |
|------|---------|
| Sequence | Fixed order |
| Dependency | Developer needs `design.json` |
| State | `artifacts/state.json` current stage |
| Handoff | Each stage writes a JSON file |
| Failure | `status: FAIL` stops the pipeline |
| Retry | Re-run the **same** stage; do not restart from requirements unless the workflow says so |

Markdown files do not enforce this. `run_sequential.py` does (teaching runtime). Least privilege (conceptual): only developer implements; QA is read-only.

## Folder structure

```text
workflow/sequential.yaml
run_sequential.py          teaching runtime (not an IDE)
agents/  skills/  rules/  docs/  artifacts/
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

Script reads `state.json`. Only the current stage may write. Skip-ahead exits with an error.

## Expected output

After four successful `run_sequential.py` calls:

```text
artifacts/state.json              current: completed
artifacts/requirements.json
artifacts/design.json             requires requirements.json
artifacts/implementation.json     requires design.json
artifacts/qa.json
```

Skip-ahead: `ERROR: cannot run developer; current stage is requirements`.

## What to observe

Order is in YAML, not in a prompt (“then please call QA”).

## Common mistakes

Letting the architect agent also decide to start coding.

## Interview takeaway

1. “I use workflow orchestration to control the sequence of specialized agents rather than allowing agents to decide the overall execution order.”
2. “Developer must not start until architecture output exists; that is a dependency, not a suggestion.”
3. “On failure I retry the failed stage when it is retryable, instead of blindly restarting the whole pipeline.”
4. “Agents perform work; the workflow owns order, state, and handoff.”

## Next session

[Session 04 — Parallel](../session-04-parallel/README.md)
