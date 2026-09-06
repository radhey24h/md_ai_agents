---
name: requirements-analysis
description: Turn a feature request into a testable requirements artifact with explicit unknowns.
---

# Goal

Produce requirements that architecture and QA can consume without reading a chat transcript.

# Process

1. Restate the request in business language.
2. Read `docs/business-rules.md` and `docs/glossary.md`.
3. List functional requirements as numbered items.
4. Attach the business rules that apply. If a rule is missing, mark UNKNOWN.
5. Write acceptance criteria in Given/When/Then or checkable bullets.
6. List risks, out-of-scope items, and open questions.

# Output

JSON artifact with `status`, `functionalRequirements`, `businessRules`, `acceptanceCriteria`, `unknowns`, `risks`.

# Never

- Do not design tables, routes, or class names here.
- Do not invent customer-facing behavior.
- Do not mark the stage complete while a critical UNKNOWN remains unlisted.
