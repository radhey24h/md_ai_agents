# Session 05 — do this

Before anyone designs APIs, a person must accept the write-up.

1. Show the **stop**:

   ```powershell
   py -3 run_hitl.py start
   py -3 run_hitl.py run
   py -3 run_hitl.py run
   ```

   First `run` writes requirements. Second `run` STOPS. No design yet.

2. **Approve** (you are alex, a human):

   ```powershell
   py -3 run_hitl.py approve --by "alex" --comment "email-only shop is enough"
   py -3 run_hitl.py run
   ```

   Open `approvals/requirements.json` — your name is there. Then `design.json` appears.

3. Optional: start again and **reject** (`reject` → back to requirements, not to release).

**Check:** The machine waited for you. Your name is in the approval file. That is HITL.
