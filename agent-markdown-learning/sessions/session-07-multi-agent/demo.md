# Session 07 walkthrough

## The problem

One “smart” agent that writes the code, writes the tests, and signs the release. That is a conflict of interest. In a company, the person who implements is not the only person who says “ship it.”

This session is all previous ideas in one picture: orchestrator, parallel discovery, HITL, then developer, then QA and security **side by side**, then a human again.

The orchestrator is a traffic cop. It does not design APIs and it does not deploy, even if you give it the biggest model. **Model ≠ permission.**

## What to do

1. Open `agents/orchestrator.md` and `agents/developer.md`.  
   Orchestrator: sequence only. Developer: code after design is approved. QA’s job card must not let it rewrite production code.

2. Run without pretending a human signed:

   ```powershell
   cd sessions/session-07-multi-agent
   py -3 run_multi.py
   ```

   Discovery files and requirements appear, then the script **stops**. Developer must not have written `qa.json`. Writer is not the judge.

3. Only in class, simulate the human (say that out loud):

   ```powershell
   py -3 run_multi.py --approve-demo
   ```

   Then you should see design, implementation, `qa.json`, `security.json`, and a join. QA and security are two jobs, then one join, then a person — not the developer marking homework.

## The point

**An orchestrator sequences specialists; it does not replace them.** Permissions follow the role, not how “smart” the model is.

## Next

Session 08 is the same customer-notification story as Session 01, with every gate named, so you can see the whole path once.
