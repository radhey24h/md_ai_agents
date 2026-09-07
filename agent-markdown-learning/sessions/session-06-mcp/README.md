# Session 06 — Job card vs tools

## In this session

**Office analog:** The job description is not the email server. Hands (tools) are plugged in separately. The model still cannot stamp “approved” on itself.

**We are doing:** A tiny teaching MCP client: list tools, read a fact file, refuse `hitl_approve` for the model.

**We are not doing:** Replacing eShop. This server is a classroom plug, not Cursor.

**How to check:**

```powershell
py -3 scripts/mcp_client_demo.py
```

It lists tools, reads a fact file, and **refuses** `hitl_approve` for the model.

## Why

People say “the agent emailed C-1002.” The `.md` file did not grow SMTP. A **tool** would send mail. MCP is a standard way to expose tools.

## How it works

Markdown = what to do. Workflow = when. MCP = what it can call.

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. MCP separates reasoning from capabilities.
2. Do not put secrets in agent Markdown.
3. `hitl_approve` is a human recording a decision.

## Next

[Session 07](../session-07-multi-agent/README.md) — traffic cop + specialists on the same shop.
