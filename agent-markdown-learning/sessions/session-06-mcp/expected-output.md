# Expected output — Session 06

`py -3 scripts/mcp_client_demo.py` prints:

- initialize ok
- tools: workflow_status, read_artifact, read_project_doc, run_next_agent, hitl_approve
- read_project_doc returns the session doc text
- hitl_approve is labeled human-only (demo refuses model self-approve)

This is a **scripted client**, so you do not need to paste JSON-RPC by hand.
