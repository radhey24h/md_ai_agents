# Session 04 walkthrough

## The problem

To understand “customer notification preferences” you need three inventories: how the API looks, how the database looks, how the UI looks. None of those three needs the others’ file first. If you run them one after another, you waste time. If you run **architecture and developer** at the same time, the developer codes against a design that is not finished.

Parallel is not “go faster.” Parallel is “these tasks do not wait on each other.”

## What to do

1. Open `workflow/parallel.yaml` and the three agents. Then open the **real** eShop files:
   - API: `../../eShop-customer-notification/app/shop/api/http.py`
   - DB: `../../eShop-customer-notification/app/shop/db.py`
   - UI: `../../eShop-customer-notification/app/shop/web/settings.html` and `warehouse.html`

   None of those inventories needs the others’ JSON first. That is why they can run together.

2. Run:

   ```powershell
   cd sessions/session-04-parallel
   py -3 run_parallel.py
   ```

   You get three branch files, then `consolidated-analysis.json`. The consolidator is the **join**: it waits until all three exist. Starting it after only the API file would ship a half picture.

3. Run the bad pairing on purpose:

   ```powershell
   py -3 run_parallel.py illegal
   ```

   It errors: developer depends on architecture. That is the other half of the lesson.

## The point

**No dependency → parallel, then join. Dependency → sequential.** Do not put Architect and Developer in the same fan-out.

## Next

A join file is still not a business decision. Session 05 stops the machine until a **person** approves or sends work back.
