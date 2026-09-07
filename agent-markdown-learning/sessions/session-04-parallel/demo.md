# Walkthrough — Session 04

Three people can open the same repo at once. None of them needs the others’ JSON first.

Open `workflow/parallel.yaml` and the three analyzer agents (`api-analyzer`, `db-analyzer`, `ui-analyzer`). In this teaching example, UI analysis does **not** wait for `api-analysis.json`. No dependency → parallel.

The consolidator is different: it must wait for all three branches. Run:

```powershell
cd sessions/session-04-parallel
py -3 run_parallel.py
```

You should see four files: three branch analyses plus `consolidated-analysis.json`. Starting the consolidator after only the API file would leave downstream incomplete. Join policy here is `all`.

Then show the illegal pairing:

```powershell
py -3 run_parallel.py illegal
```

That must error: Developer depends on Architecture. Dependency exists → sequential (and later, a human gate).
