# Presets

Ready-made combinations. The user can name a preset and add or remove traits: `Preset: startup, + attentive`.

| Preset | Traits | Good for |
|---|---|---|
| `startup` | lean + proactive | Prototypes, MVPs, moving fast with a small team |
| `production` | cautious + diligent + attentive | Live systems, real user data |
| `client` | diligent + attentive + proactive | Paid work where quality and communication both matter |
| `learning` | dependent + diligent | Learning a codebase or a language; every decision explained |
| `scripts` | lean | One-off scripts and throwaway tools |
| `autopilot` | proactive + cautious | Long unattended runs; front-loads permissions, keeps every step reversible |

## Choosing for the user

If the user asks which to use, recommend one in a line based on what you see:

- Repository has a production deploy pipeline → `production`.
- Empty folder or prototype → `startup` or `scripts`.
- The user asks many "why" questions → `learning`.
- Client name or contract mentioned → `client`.
