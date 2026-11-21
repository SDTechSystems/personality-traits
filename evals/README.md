# Evals

`evals.json` holds scenarios with the active traits and what the agent should and should not do.

## How they were run (v0.2.0, 2026-11-21)

- A Claude Sonnet 5.5 agent loaded all trait skills and answered each scenario without seeing the `expect` / `avoid` fields.
- Each answer was graded by hand against `expect` and `avoid`.

## Results

| | Pass | Partial | Fail |
|---|---|---|---|
| First run | 12 | 3 | 0 |
| After fixes | 15 | 0 | 0 |

Fixed after the first run:

- `skeptic` repeated a concern the user had already acknowledged. It now stays quiet when the user says they know the risk.
- `security-minded` built a different feature (password reset) without asking. It now proposes it and waits for a yes.
- `thrifty` suggested a smaller model for a medium-sized feature. It now does so only for small, mechanical work (checked with an extra `thrifty-small` case).
