# Session 08 — do this

Same shop as Session 01. Now with a manager, specialists, and human gates.

1. Confirm the **real** shop still skips C-1002’s email:

   ```powershell
   cd ../../eShop-customer-notification/app
   py -3 -m unittest discover -s tests -v
   ```

2. Run the classroom pipeline (you are the human named alex):

   ```powershell
   cd ../../sessions/session-08-complete-enterprise
   py -3 run_enterprise.py start
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate discovery --by "alex"
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate requirements --by "alex"
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate design --by "alex"
   py -3 run_enterprise.py run
   py -3 run_enterprise.py run
   py -3 run_enterprise.py approve --gate release --by "alex"
   py -3 run_enterprise.py status
   ```

   Developer cannot sneak in before design approve. `status` ends `completed`.

**Check:** Shop tests still pass. Pipeline waited for your name. `status` is `completed`.
