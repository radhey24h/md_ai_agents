# Session 01 walkthrough

## The problem

Someone types: “Add SMS opt-out for customer notifications.”

A generic chat will invent Twilio. eShop already ships **email** when an order ships. Maya wants that mail. Omar opted out — warehouse still ships, **no email**. SMS is not in the product.

This session has **one** worker. Four kinds of file.

## What to do

1. Open `agents/customer-analyst.md` — the **job card** (who). It does nothing until a runtime reads it.

2. Open `skills/customer-analysis/SKILL.md` then `rules/no-invent.md` — **how** vs **must always be true**.

3. Prove email from code. Open:
   - `../../eShop-customer-notification/business-rules.md`
   - `../../eShop-customer-notification/app/shop/services/notifications.py` (skip on opt-out)
   - `../../eShop-customer-notification/app/shop/api/http.py` (routes)
   - `../../eShop-customer-notification/app/shop/web/settings.html` (email checkbox only)

   Search for `sms`. You should find no SMS implementation. UNKNOWN, not “add Twilio.”

4. Optional: copy [Expected output](README.md#expected-output). Cite **file paths**.

## The point

**Who / how / must / facts are four files.** Facts include the shop. No SMS in code → do not ship SMS.

## Next

A planner was not in this chat. Session 02 is the JSON they can trust.
