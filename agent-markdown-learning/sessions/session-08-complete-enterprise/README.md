# Session 08 — Complete Enterprise Demo

## Objective

Capstone. **Customer Notification Preferences** through the full teaching path. No new primitive — show how Sessions 01–07 fit.

## What You Will Learn

The whole picture: foundation → artifacts → seq/parallel → HITL → MCP (as a layer) → multi-agent → this run.

## Prerequisites

Sessions 01–07.

## Concepts

See [concept.md](concept.md).

## Architecture

See [architecture.md](architecture.md).

## Folder Structure

```text
agents/     orchestrator, discovery (api/db/ui), consolidator,
            requirements, architect, developer, qa, security, release
skills/ rules/ docs/ workflow/
artifacts/ approvals/
run_enterprise.py
```

This is **not** a copy of `enterprise-agent-platform/`. It is a classroom path with the same *ideas*.

## Step-by-Step Demo

### Step 1

Show `../../examples/customer-notification/business-rules.md`.

### Step 2

Walk [architecture.md](architecture.md) diagrams (parallel discovery, then gated delivery).

### Step 3

Run `run_enterprise.py` with the HITL pauses documented in [demo.md](demo.md).

## What Happens Internally

Same as Sessions 03–05: files + state. MCP is referenced, not re-implemented here.

## Expected Output

See [expected-output.md](expected-output.md).

## What to Observe

SMS stays UNKNOWN. Release waits for join of QA and security plus HITL.

## Common Mistakes

Calling this “production Cursor.” It is a demo runtime.

## Questions to Ask During the Demo

See [demo.md](demo.md).

## Interview Takeaway

See [interview-takeaway.md](interview-takeaway.md).

## Next Session

Apply the split in a real repository. Keep knowledge in one `agents/` `skills/` `rules/` `docs/` tree; use workflow + HITL for control; use MCP for tools.
