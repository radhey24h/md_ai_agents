# Session 05 — Human-in-the-Loop

## Objective

The workflow **stops**. A human **approves** or **rejects**. The model never approves its own work.

## What you will learn

HITL gates, approve vs reject, why architecture / security / release need humans.

## Prerequisites

Session 03 (sequence) recommended.

## How it works

```text
requirements.json
        ↓
   Human Review
      /    \
 APPROVE   REJECT
    ↓         ↓
Architect   Requirements (rework)
```

Gate file: `approvals/requirements.json`.

Use HITL for: architecture, business-rule ambiguity, security exceptions, breaking APIs, production, release.

**The model must never approve its own work.**

## Folder structure

```text
workflow/hitl.yaml
run_hitl.py
agents/  skills/  rules/  docs/  artifacts/  approvals/
```

## Demo

Walkthrough: [demo.md](demo.md).

## What happens internally

`run` on a HITL stage prints STOP. Only `approve` / `reject` changes stage.

## Expected output

After requirements + STOP: `artifacts/requirements.json` and `state.json` current `approval-requirements`.

After approve: `approvals/requirements.json` (`status: approved`, `by: alex`) and `artifacts/design.json`.

After reject: current stage is `requirements` again. Comment stored on the rejection file.

## What to observe

A prompt that says “please get approval” is not HITL. A stopped runner is.

## Common mistakes

Letting the requirements agent set `approval.status = approved`.

## Interview takeaway

1. “HITL is used for high-risk or business-critical decisions, and the model cannot approve its own output.”
2. “A real gate stops the runner; a sentence in a prompt is not a gate.”
3. “Reject returns work to the producing agent; it does not jump to release.”
4. “Architecture, ambiguous rules, breaking APIs, security exceptions, and production need humans.”

## Next session

[Session 06 — MCP](../session-06-mcp/README.md)
