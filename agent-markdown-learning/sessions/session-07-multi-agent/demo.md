# Session 07 — do this

Many hats. The person who codes does not also say “QA passed.”

1. Open `agents/orchestrator.md` vs `agents/developer.md`. Traffic cop vs coder.

2. From this folder:

   ```powershell
   py -3 run_multi.py
   ```

   Stops after discovery/requirements. No `qa.json` from the developer.

3. Then (you are pretending a human already signed):

   ```powershell
   py -3 run_multi.py --approve-demo
   ```

   Now you should see design, implementation, qa, security, join.

**Check:** Stop happened. QA is a separate file. Developer did not write it.
