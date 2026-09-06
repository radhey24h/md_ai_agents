# Session 05 — Human-in-the-Loop

## Objective

The workflow **stops**. A human **approves** or **rejects**. The model never approves its own work.

## What You Will Learn

HITL gates, approve vs reject, why architecture / security / release need humans.

## Prerequisites

Session 03 (sequence) recommended.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
workflow/hitl.yaml
run_hitl.py
agents/  skills/  rules/  docs/  artifacts/  approvals/
```

## Step-by-Step Demo

### Step 1

Run until the gate. Show that the next agent does not start.

### Step 2

`approve` → architect runs.

### Step 3

Reset or second demo: `reject` → back to requirements.

Details: [demo.md](demo.md).

## What Happens Internally

`run` on a HITL stage prints STOP. Only `approve`/`reject` changes stage.

## Expected Output

See [expected-output.md](expected-output.md).

## What to Observe

A prompt that says “please get approval” is not HITL. A stopped runner is.

## Common Mistakes

Letting the requirements agent set `approval.status = approved`.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

[Session 06 — MCP](../session-06-mcp/README.md)
