# Session 01 — Four files, not one blob

## In this session

**Office analog:** A job description, a playbook, a company policy, and a wiki page are four different things. Don’t paste them into one prompt.

**We are doing:** Open four Markdown files that describe *how to analyze the shop*. Then prove in code that C-1002 is not emailed.

**We are not doing:** Changing the shop. Running a pipeline. Building a second channel.

**How to check:** You can point at:

| File | Question it answers |
|------|---------------------|
| `agents/customer-analyst.md` | Who is doing the work? |
| `skills/customer-analysis/SKILL.md` | How do they analyze? |
| `rules/no-invent.md` | What must they never invent? |
| `docs/notification-facts.md` | What is already true? |

Your notes (or `artifacts/sample-analysis-notes.md`) cite `notifications.py` and say C-1002 ships without email.

## Why

If those four live in one chat, the model mixes “who I am” with “how I work” with “what is true.” Then it invents features that are not in the shop.

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. An agent file names **who**; it is not a running process by itself.
2. A **skill** is a playbook; a **rule** is a short standing constraint.
3. **Docs + code** are facts.
4. If you cannot prove it, label UNKNOWN.

## Next

[Session 02](../session-02-artifacts-handoff/README.md) — put the analysis in a file a planner can open tomorrow.
