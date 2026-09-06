# Demo — Session 01

### Say

We hired one intern: Customer Analyst. We will not give them a manager yet. We will give a job card, a playbook, one rule, and facts.

### Demo

Open `agents/customer-analyst.md`.

### Ask

Is this an autonomous system?

### Expected

No. It is a job description.

### Explain

An `.md` file is not an agent by itself. A runtime has to load it.

---

### Say

Now the playbook. This is *how* to analyze, not *who*.

### Demo

Open `skills/customer-analysis/SKILL.md`. Contrast with `rules/no-invent.md` (three lines).

### Ask

Could we paste the skill into the agent file?

### Expected

Yes, but then you cannot reuse the playbook and the agent becomes a wiki.

### Explain

Skill = reusable how. Agent = this worker.

---

### Say

Facts live in docs. Walk the request: “Add SMS opt-out.”

### Demo

`docs/notification-facts.md` and `../../examples/customer-notification/business-rules.md`.

### Ask

Is SMS a FACT?

### Expected

UNKNOWN. Not in the rules or sample data.

### Explain

FACT / EVIDENCE / INFERENCE / UNKNOWN. Inventing SMS is the failure mode this session exists to prevent.

---

### Say

Optional: write a few lines into `artifacts/analysis-notes.md` using those labels.

### Demo

Show [expected-output.md](expected-output.md).

### Ask

If a planner joined tomorrow, could they trust a Slack screenshot of this chat?

### Expected

No. That is Session 02.

### Explain

Today we only separated the four files. Next we freeze the result as a file.
