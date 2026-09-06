---
name: security-analysis
description: Review a feature for auth, secrets, validation, and exposure risks.
---

# Goal

Independent security verdict before release HITL.

# Process

1. Review authentication and authorization paths.
2. Check input validation and injection risk.
3. Check secrets handling and logging of sensitive data.
4. Check new API exposure.
5. Set `release_allowed` false if any high or critical finding is open.

# Output

`security.json` with findings and `release_allowed`.

# Never

- Do not modify application code.
- Do not store credentials in artifacts.
