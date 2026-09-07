---
name: architecture-design
description: Design APIs, data, events, and boundaries for one approved feature.
---

# Goal

Turn approved requirements into an implementation-ready design.

# Process

1. Confirm requirements HITL is approved.
2. Read `docs/architecture.md` and `docs/api-contracts.md`.
3. Define API endpoints or UI surfaces.
4. Define data ownership and schema changes.
5. Define events, failure handling, and security controls.
6. Map each acceptance criterion to a design element.
7. Call out breaking changes for HITL.

# Output

JSON artifact with `apiDesign`, `dataChanges`, `serviceBoundaries`, `events`, `failureHandling`, `security`, `scalability`, `acceptanceMap`.

# Never

- Do not write application code.
- Do not ignore an existing contract in `docs/api-contracts.md`.
