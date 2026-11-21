# Security

## What this repository contains

Only Markdown instructions for AI agents. By design:

- No scripts or executables inside `skills/`.
- No network calls, webhooks or telemetry.
- No instructions to read secrets, credentials or files outside the task.
- No instructions to change the agent's own permissions or settings.

Every change is checked in CI by `.github/scripts/lint_skills.py` (frontmatter, size limits, hidden Unicode, encoded blobs, executable files).

## Reporting a problem

If you find instructions that could make an agent behave unsafely, open a [private security advisory](../../security/advisories/new) on this repository. Please do not open a public issue for security reports.

We aim to reply within 7 days.
