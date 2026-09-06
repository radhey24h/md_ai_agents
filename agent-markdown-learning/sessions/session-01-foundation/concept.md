# Concept — Session 01

| Piece | Question | In this folder |
|-------|----------|----------------|
| Agent | Who performs the work? | `agents/customer-analyst.md` |
| Skill | How should this type of work be done? | `skills/customer-analysis/SKILL.md` |
| Rule | What must always be true? | `rules/no-invent.md` |
| Doc | What facts are known? | `docs/notification-facts.md` |

The model reasons. The agent file says who it is. Markdown does not “run” the analysis by sitting in a folder.

```text
User request
     ↓
Customer Analyst
     ↓
Skill
     ↓
Rules
     ↓
Docs
     ↓
Analysis (notes)
```
