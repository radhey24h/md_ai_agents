# Session 04 — Look at API, DB, and UI together

## In this session

**Office analog:** Three people can inventory HTTP, SQLite, and the two HTML pages at the same time. The coder still cannot start until architecture exists.

**We are doing:** Fan-out three inventories, then **join**. Show that architect + developer in parallel is illegal.

**We are not doing:** Letting developer start in parallel with architect.

**How to check:**

```powershell
py -3 run_parallel.py
py -3 run_parallel.py illegal
```

First command: three analyses + `consolidated-analysis.json` citing real eShop files. Second: **error**.

## Why

Reading `http.py`, `db.py`, and the HTML pages does **not** require waiting on each other. Coding **does** require an approved design.

## How it works

```text
API inventory  ─┐
DB inventory   ─┼─► JOIN ─► consolidator
UI inventory   ─┘
```

## Walkthrough

[demo.md](demo.md)

## Interview takeaway

1. Parallelize only independent work; join before anyone consumes the set.
2. API / DB / UI discovery is typical fan-out; architecture then development is not.
3. `join: all` means incomplete branches cannot sneak through.

## Next

[Session 05](../session-05-hitl/README.md) — a person must sign before design starts.
