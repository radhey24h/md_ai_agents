# Walkthrough — Session 01

This session is one worker with no pipeline. You are hiring a Customer Analyst: a job card, a playbook, one standing rule, and a fact sheet. Nothing here starts the next agent.

Open `agents/customer-analyst.md`. That file names **who** does the work. It is not an autonomous system and it is not a running process. An `.md` file only becomes useful when a runtime (you, or an IDE) loads it.

Then open `skills/customer-analysis/SKILL.md` and `rules/no-invent.md` side by side. The skill is *how* this kind of analysis is done — a reusable playbook. The rule is a few lines of *what must always be true*. You *could* paste the skill into the agent file, but then the agent becomes a wiki and nobody else can reuse the playbook. Skill = how. Agent = this worker.

Now walk a real request: “Add SMS opt-out.” Read `docs/notification-facts.md` and `../../examples/customer-notification/business-rules.md`. SMS is not in those files, so it is **UNKNOWN**, not a fact. Inventing SMS is the failure this session exists to prevent. Label what you know as FACT, EVIDENCE, INFERENCE, or UNKNOWN.

Optional: write a few lines into `artifacts/analysis-notes.md` using those labels. A filled example is in [README — Expected output](README.md#expected-output).

If a planner joined tomorrow, they could not trust a Slack screenshot of this chat. Today we only separated the four files. Session 02 freezes the result as a file they can actually read.
