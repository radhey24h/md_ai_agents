# Demo — Session 02

### Say

Yesterday’s intern was smart. Today a planner joins. They were not in the chat.

### Demo

`agents/analyst.md` then `artifacts/analysis.json`.

### Ask

Can the planner reconstruct the intern’s jokes in Slack?

### Expected

They should not need to.

### Explain

The JSON is the handoff.

---

### Say

Planner is forbidden from inventing extra channels.

### Demo

`agents/planner.md` inputs section.

### Ask

What if `unknowns` is empty but SMS was discussed verbally?

### Expected

That is a bug in the analyst. The planner only sees the file.

### Explain

That is why completion criteria belong on the writer.

---

### Say

Connect to Session 03: two files are a convention. Four stages need a workflow that *refuses* to skip.
