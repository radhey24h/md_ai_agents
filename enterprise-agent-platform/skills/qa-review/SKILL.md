---
name: qa-review
description: Validate an implemented feature against requirements, design, and tests.
---

# Goal

Give an evidence-based QA verdict.

# Process

1. Load requirements, design, implementation artifacts.
2. Check each acceptance criterion: PASS, FAIL, or NOT_TESTED.
3. Check API/contract alignment.
4. Note regression risk.
5. Return PASS, PASS_WITH_RISKS, or FAIL.

# Output

`qa.json` with criterion results and defects.

# Never

- Do not modify application code.
- Do not pass with empty evidence.
