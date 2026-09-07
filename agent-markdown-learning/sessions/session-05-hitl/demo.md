# Walkthrough — Session 05

Accepting requirements is a high-risk step. A named person signs. The model does not.

```powershell
cd sessions/session-05-hitl
py -3 run_hitl.py start
py -3 run_hitl.py run
py -3 run_hitl.py run
```

The first `run` writes `requirements.json` and stops at a HITL gate. The second `run` must **stop** again. The architect has not run. A sentence in a prompt (“please get approval”) is not a gate. A stopped runner is.

Approve path — a human records the decision, then work continues:

```powershell
py -3 run_hitl.py approve --by "alex" --comment "email-only is enough"
py -3 run_hitl.py run
```

You should see `approvals/requirements.json` with `status: approved`, then a design artifact.

Reject path — start again so you can show the other branch:

```powershell
py -3 run_hitl.py start
py -3 run_hitl.py run
py -3 run_hitl.py reject --by "alex" --comment "need explicit opt-out wording"
py -3 run_hitl.py run
```

Current stage returns to **requirements**. Reject is rework, not “skip to release.”

The same pattern belongs on security exceptions and production. Session 06 adds tools (MCP). Approve stays human-only even when it is a tool name.
