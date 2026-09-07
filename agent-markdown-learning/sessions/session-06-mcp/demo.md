# Session 06 walkthrough

## The problem

People say “the agent called the database” as if Markdown grew hands. It did not.

- The **agent file** is still the job card (who / what / must not).
- **Workflow** still decides *when* the next step is allowed.
- **MCP** is a standard plug: “here are tools you may call.”
- The **tool** is the actual thing (read a file, ask workflow status, run a scanner).

If you unplug MCP, the model can still *think* about pasted docs. It cannot *call* `workflow_status`. Thinking and capability are different.

## What to do

1. Open `agents/tool-user.md` and `tools/README.md`.  
   Same specialist idea as Session 01. The new piece is a list of tools, not a second job description.

2. Run the teaching client (this is **not** the enterprise platform next door):

   ```powershell
   cd sessions/session-06-mcp
   py -3 scripts/mcp_client_demo.py
   ```

   You should see: server starts, tools listed (`workflow_status`, `read_artifact`, `read_project_doc`, `run_next_agent`, `hitl_approve`), a snippet of the project doc, and **`hitl_approve` refused** when the caller is the model.

3. Notice what is missing from the Markdown: passwords, API keys, “just approve this.” Secrets stay with the tool, not in `SKILL.md`.

## The point

**Markdown says what to do. Workflow says when. MCP says what it can call.** `hitl_approve` is a human recording a decision, not a self-score.

## Next

Session 07 puts a traffic cop (orchestrator) in front of specialists. Strongest model still does not get deploy rights.
