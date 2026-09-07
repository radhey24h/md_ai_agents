# Walkthrough — Session 02

Yesterday’s analyst was useful only if today’s planner can start without sitting in the same chat. Open `agents/analyst.md`, then `artifacts/analysis.json`. The JSON is the handoff. The planner should not need Slack jokes, screenshots, or “what we decided verbally.”

Open `agents/planner.md` and look at the inputs. The planner is allowed to read that file and nothing else as source of truth. It must not invent extra channels. If `unknowns` is empty but SMS was discussed in conversation, that is a bug in the **analyst** — the planner will never see the chat. Completion criteria belong on the writer of the artifact.

Two agents and one filename is still a convention. Session 03 adds a workflow that *refuses* to skip a stage.
