# Session 04 — Parallel Agents

## Objective

Run **independent** analysis together. **Join** before anyone depends on the full picture. Do not parallelize Architecture + Developer.

## What you will learn

Fan-out, join, good vs bad parallel candidates.

## Prerequisites

Session 03.

## How it works

```text
          FEATURE
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
   API      DB       UI     (no dependencies)
    │        │        │
    └────────┼────────┘
             ▼
           JOIN (all)
             ▼
       consolidator
```

Synchronization: `join: all` in `workflow/parallel.yaml`.

**Good parallel:** API inventory, DB inventory, UI inventory, dependency inventory, security *inventory* (not release).

**Bad parallel:** Architecture + Developer when Developer requires approved architecture.

## Folder structure

```text
workflow/parallel.yaml
run_parallel.py
agents/  skills/  rules/  docs/  artifacts/
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

Branches have no input edges to each other. Join waits for all three.

## Expected output

```text
artifacts/api-analysis.json
artifacts/db-analysis.json
artifacts/ui-analysis.json
artifacts/consolidated-analysis.json
```

Each branch JSON cites a real eShop file (`http.py`, `db.py`, settings + warehouse HTML). SMS stays unknown. `py -3 run_parallel.py illegal` prints that architecture and developer cannot share a parallel group.

## What to observe

Consolidator does not start with only one branch.

## Common mistakes

Starting Developer in the same fan-out as Architect.

## Interview takeaway

1. “I parallelize only independent tasks and introduce a join before downstream agents consume their combined output.”
2. “API, database, and UI discovery are typical fan-out work; architecture then development is not.”
3. “A join policy of `all` means incomplete branches cannot silently proceed.”

## Next session

[Session 05 — HITL](../session-05-hitl/README.md)
