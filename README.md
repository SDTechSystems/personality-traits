<p align="center">
  <img src=".github/assets/banner.png" alt="SD Tech Systems" width="640">
</p>

# personality-traits

Build the AI assistant you want to work with. Pick personality traits (lean, careful, thrifty, a skeptical senior, an explainer...), set how strong each one is, and your agent changes how it codes, decides and reports to match. It learns your style over time, like an employee training with a new boss.

```bash
npx skills add sdtechsystems/personality-traits
```

Or install only what you want:

```bash
npx skills add sdtechsystems/personality-traits --skill trait-composer --skill trait-lean --skill trait-thrifty
```

Works best with Claude Code; any agent that reads `SKILL.md` files can use it.

## Getting started

On first use, the agent offers a one-minute interview (what you use it for, how comfortable you are with code, how much autonomy you want) and suggests a setup. Or set it yourself, in a message or in your project's `CLAUDE.md` / `AGENTS.md`:

```
Traits: lean:2, cautious:3
```

```
Pack: production + explainer:1
```

Each task starts with one line so you always know who you are working with:

```
Working as: lean·2, cautious·3
```

## Traits

| Trait | What to expect | Impact on work and code |
|---|---|---|
| `lean` | The shortest path that fully works | Small diffs, no extras |
| `diligent` | Finishes completely | Tests, docs and cleanup in every change |
| `cautious` | Small, reversible steps | Backups, flags and dry runs before risky steps |
| `attentive` | Catches details, remembers what you said | Follows conventions; flags inconsistencies |
| `proactive` | Thinks one step ahead | Asks for everything up front; proposes automation |
| `consultative` | Checks in before real decisions | Questions with options; you keep control |
| `thrifty` | Saves AI usage, money and dependencies | Plans a budget; says what it saved |
| `explainer` | Tells you what was built and how to use it | Short briefs after big or non-obvious changes |
| `skeptic` | A senior QA and security reviewer | Questions the plan; then does the job well |
| `security-minded` | Security and privacy first | Safe defaults; checks secrets, inputs, data |

Every trait has three levels: `:1` light, `:2` normal (default), `:3` strong.

## Packs

| Pack | Traits | For |
|---|---|---|
| `startup` | lean:2 + proactive:2 + thrifty:2 | Prototypes and solo builders: fast and cheap |
| `production` | cautious:3 + diligent:2 + skeptic:2 + security-minded:2 | Live systems and client work: safe and complete |
| `non-coder-boss` | explainer:2 + consultative:1 + diligent:2 | People who direct the work but don't code |
| `autopilot` | proactive:3 + cautious:2 + attentive:2 | Long tasks while you're away |

## Same request, different traits

> **You:** add a dark mode toggle

| Trait | Response |
|---|---|
| lean | One toggle using the existing CSS variables. 1 file, 14 lines. |
| diligent | Toggle, remembered choice, system default, 3 tests, contrast checked, README updated. |
| cautious | Added behind a feature flag, off by default. Light theme verified unchanged. |
| attentive | Used your brand tokens. Noticed the dark logo will vanish on the dark background. |
| proactive | Done. Next: a white logo variant and a screenshot test for both themes. |
| consultative | Two decisions first: remember the choice? Follow the system setting? I'd say yes to both. |
| thrifty | CSS variables only, nothing added to the bundle. A smaller model would have been enough. |
| explainer | Done. Where the toggle is, what it remembers, and how to try it. |
| skeptic | Three components use hard-coded colors and would look broken; converting them too. |
| security-minded | Nothing security-relevant here; stored the preference locally, no personal data. |

## Conflicts

When traits disagree, this order sets the floor: **security-minded > cautious > skeptic > diligent > attentive > thrifty > proactive > explainer > lean > consultative**. So `lean + diligent` gives you the smallest solution with its test, and `thrifty + security-minded` the cheapest option that stays secure.

## It adapts

When a task clearly needs a different trait (touching production, handling personal data), the agent proposes it before starting. Early on it asks; once it knows you, it applies it for that task and tells you.

## Limits every trait keeps

No trait, level or pack will:

1. Skip confirmation for irreversible or outward-facing actions (delete, push, deploy, send, pay), unless you pre-authorized that exact action.
2. Disable tests, validations or security checks to go faster.
3. Grant itself permissions or edit its own configuration.
4. Report "done" without checking.

## Pairs well with

[common-sense](https://github.com/sdtechsystems/common-sense): the baseline judgment every trait builds on (time, devices, intent, your technical level, cost).

## Security

Markdown only: no scripts, no network calls, no access to secrets. See [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE)

---

Developed by **SD Tech Systems** · Part of SD Tech
