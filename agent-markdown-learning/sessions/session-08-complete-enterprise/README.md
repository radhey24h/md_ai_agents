# Session 08 — Same shop, full path

## In this session

**Office analog:** Discovery in parallel, then named humans on requirements / design / release, then developer, then QA and security together.

**We are doing:** Run the teaching pipeline on **the same eShop**. Confirm the real shop still skips C-1002’s email.

**We are not doing:** A new product. Pretending this script is production Cursor.

**How to check:**

1. Shop tests still pass (`skipped_opt_out` for C-1002).
2. `py -3 run_enterprise.py status` is `completed` only after named `approve`s. Developer cannot run before design HITL.

## Why

Session 01 was “understand the shop.” This session is “run a company-shaped process around that same shop.”

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. Production-shaped agent work needs roles, artifacts, workflow, tools, and humans — not a pile of prompts.
2. Parallelize discovery; serialize anything that needs an approved design.
3. Do not invent a channel the shop does not have.

## Next

Use the same split in a real repo. Keep one `agents/` `skills/` `rules/` `docs/` tree.
