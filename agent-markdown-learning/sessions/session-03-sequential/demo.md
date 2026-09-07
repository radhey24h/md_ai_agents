# Session 03 walkthrough

## The problem

You now have four job cards: requirements, architect, developer, QA. If you only *tell* the model “please do them in order,” a busy Friday it will skip ahead and start coding. Then QA reviews a design that never existed.

Agents do the work. Something else must own **order**. The code they would change later is eShop (`eShop-customer-notification/app/shop/`). In this folder the manager is YAML plus a tiny teaching script (not Cursor).

## What to do

1. Open `workflow/sequential.yaml`.  
   It lists: requirements → architecture → implementation → qa. Delete this file in your head and keep only the four `.md` agents. They will **not** line up by themselves. Markdown is not a workflow engine.

2. Run the teaching script from this folder:

   ```powershell
   cd sessions/session-03-sequential
   py -3 run_sequential.py
   py -3 run_sequential.py
   py -3 run_sequential.py skip-to-developer
   ```

   The first two runs write `requirements.json`, then `design.json`. The third command **must fail**. Developer is not allowed yet. That error is the lesson: dependency is a lock, not a hint.

3. Run `py -3 run_sequential.py` until the script says completed.  
   You should have four JSON files plus `state.json`. The “current stage” lives on disk. Retry means run *this* stage again, not wipe the factory, unless you delete state.

## The point

**The architect must not run the factory.** Workflow owns sequence. Developer cannot start before architecture output exists.

## Next

Some work has *no* dependency. Session 04 is three inventories at once, then a join — and why architecture + developer still cannot run in parallel.
