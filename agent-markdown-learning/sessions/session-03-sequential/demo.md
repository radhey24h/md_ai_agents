# Session 03 — do this

Imagine the team will change the shop. Four jobs. The architect must not also start coding.

1. Open `workflow/sequential.yaml` — the order. Four `.md` agents alone will **not** line up.

2. From this folder:

   ```powershell
   py -3 run_sequential.py
   py -3 run_sequential.py
   py -3 run_sequential.py skip-to-developer
   ```

   First two writes: requirements, then design. Third command **must fail**. That is the lesson.

3. Keep running `py -3 run_sequential.py` until it says completed. You should see `requirements.json`, `design.json`, `implementation.json`, `qa.json`.

**Check:** Skip-ahead failed. Four artifacts exist.
