# Security rules

- Authentication required for preference changes.
- Authorization: a user may change only their own notification preferences.
- Validate channel and locale inputs. Reject unknown values.
- Do not expose internal user ids in error messages.
- Secrets live in a secret manager or environment, never in agent Markdown.
