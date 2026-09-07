# Session 06 — do this

This session is **how an agent would call tools**, not a new product. C-1002’s skip still lives in `notifications.py`.

1. Open `agents/tool-user.md` and `tools/README.md`. Job card vs tool list.

2. From this folder:

   ```powershell
   py -3 scripts/mcp_client_demo.py
   ```

   You should see tool names, a snippet of the fact file, and **hitl_approve refused** for the model.

**Check:** You can say: “The `.md` file is not the mailer. MCP is how a worker *calls* something.”
