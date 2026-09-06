# Session 04 — Parallel Agents

## Objective

Run **independent** analysis together. **Join** before anyone depends on the full picture. Do not parallelize Architecture + Developer.

## What You Will Learn

Fan-out, join, good vs bad parallel candidates.

## Prerequisites

Session 03.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
workflow/parallel.yaml
run_parallel.py
agents/  skills/  rules/  docs/  artifacts/
```

## Step-by-Step Demo

### Step 1

Show the three independent analysts.

### Step 2

`py -3 run_parallel.py` writes three files then `consolidated-analysis.json`.

### Step 3

Show `run_parallel.py illegal` — architecture+developer blocked.

Details: [demo.md](demo.md).

## What Happens Internally

Branches have no input edges to each other. Join waits for all three.

## Expected Output

See [expected-output.md](expected-output.md).

## What to Observe

Consolidator does not start with only one branch.

## Common Mistakes

Starting Developer in the same fan-out as Architect.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 05 — HITL](../session-05-hitl/README.md)
