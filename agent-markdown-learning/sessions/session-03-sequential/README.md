# Session 03 — Sequential Agents

## Objective

**Agents perform work. The workflow controls order.** Developer cannot run before Architecture.

## What You Will Learn

Sequence, dependencies, state, handoff, failure, retry.

## Prerequisites

Session 02.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
workflow/sequential.yaml
run_sequential.py          teaching runtime (not an IDE)
agents/  skills/  rules/  docs/  artifacts/
```

## Step-by-Step Demo

### Step 1

Show `workflow/sequential.yaml` stage list.

### Step 2

Run `py -3 run_sequential.py` (writes requirements). Run again (architecture). Show that forcing developer first fails.

### Step 3

Show four JSON files in `artifacts/`.

Details: [demo.md](demo.md).

## What Happens Internally

Script reads `state.json`. Only the current stage may write. Skip-ahead exits with an error.

## Expected Output

See [expected-output.md](expected-output.md).

## What to Observe

Order is in YAML, not in a prompt (“then please call QA”).

## Common Mistakes

Letting the architect agent also decide to start coding.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 04 — Parallel](../session-04-parallel/README.md)
