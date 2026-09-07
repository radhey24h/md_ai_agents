# Walkthrough — Session 03

Four specialists, one manager: the YAML. The architect designs; it does not run the factory.

Open `workflow/sequential.yaml`. If you deleted that file and kept only the four agent Markdown files, they would **not** run in order by themselves. A folder of `.md` files is not a workflow engine.

The teaching runtime is a small Python script, not Cursor. From this folder:

```powershell
cd sessions/session-03-sequential
py -3 run_sequential.py
py -3 run_sequential.py
py -3 run_sequential.py skip-to-developer
```

The first two runs write requirements, then architecture. `skip-to-developer` must fail: current stage is still before implementation. That is a **dependency**, not a suggestion. Retry means run the current stage again, not wipe the whole pipeline, unless you delete `artifacts/state.json`.

After four successful `run` calls you should have `requirements.json`, `design.json`, `implementation.json`, and `qa.json`. Session 04 is work that does *not* have to wait: API, DB, and UI analysis can start together.
