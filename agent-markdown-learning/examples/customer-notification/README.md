# Customer Notification Preferences

One feature for every session. Session 1 analyzes it. Session 8 runs a full teaching workflow around it.

## What the product wants

A customer can control whether they receive notifications, starting with **email**. Preference belongs to the **customer**. The system must not send mail when they have opted out.

## Files

| File | Use |
|------|-----|
| [requirements.md](requirements.md) | What we think we are building |
| [business-rules.md](business-rules.md) | Facts agents must not invent |
| [sample-data/](sample-data/) | Tiny “evidence” (not a real service) |

## How sessions use this

1. Analyst reads the docs.  
2. Later sessions turn findings into JSON artifacts.  
3. HITL sessions approve requirements/design/release.  
4. Parallel sessions split API / DB / UI discovery.

Keep UNKNOWN labeled. Do not add SMS just because it sounds complete.
