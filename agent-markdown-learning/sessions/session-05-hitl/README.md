# Session 05 — A person must sign

## In this session

**Office analog:** After the write-up, a named manager clicks Approve. The intern (or the model) cannot mark their own exam.

**We are doing:** After requirements, the run **stops**. You approve or reject. Only then may architecture run.

**We are not doing:** The model writing `approved: true` on itself.

**How to check:** Second `run` prints STOP and there is no `design.json` yet. After `approve --by "alex"`, `approvals/requirements.json` has that name and design appears. After `reject`, you are back on requirements.

## Why

Someone has to accept “email-only is the product.” A checkbox the model ticks is not a decision.

## How it works

```text
requirements.json → STOP → human APPROVE → architect
                              REJECT  → rewrite requirements
```

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. HITL is a stopped runner plus a signed file, not a sentence in a prompt.
2. The model must not approve its own output.
3. Reject is rework, not skip to release.

## Next

[Session 06](../session-06-mcp/README.md) — tools (hands), still not self-approve.
