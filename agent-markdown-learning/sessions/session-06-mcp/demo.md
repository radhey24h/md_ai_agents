# Demo — Session 06

### Say

The analyst is still a job card. MCP does not replace `agents/`. It gives hands.

### Demo

`tools/README.md` and `agents/tool-user.md`.

### Ask

If we delete MCP, can the agent still *reason* about docs we pasted?

### Expected

Yes. It cannot *call* workflow_status.

### Explain

Reasoning vs capability.

---

### Say

Teaching server. Not the production platform next door.

### Demo

```powershell
cd sessions/session-06-mcp
py -3 scripts/mcp_client_demo.py
```

### Ask

Which tool should a model never call for its own requirements file?

### Expected

`hitl_approve`.

### Explain

Same rule as Session 05, now on a tool.

---

### Say

Next: orchestrator plus specialists, still using artifacts, seq/parallel, HITL, and tools as ideas.
