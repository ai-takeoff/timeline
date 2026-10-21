# timeline

A dated, falsifiable snapshot of estimates on AI capability timelines and the outcomes that follow from them.

## What this is

`ai-timelines-and-outcomes.md` states probability estimates with the reasoning attached, so that if they turn out wrong it is possible to see *why*, not only *that*. It carries pre-registered update rules, called **tripwires**. Each one commits in advance to a direction and rough size of revision when a named measurement crosses a named threshold. A passive watchlist lets any outcome be narrated as consistent with the priors; a rule written in advance does not.

## Status

**Estimates last changed: v1.71 (20 October 2026).** That version raised the no-RSI row's permanent disempowerment from 25–40% to 40–55%, after an argument that delegation ratchets with no recursive self-improvement needed, and that the row had been priced on a capability plateau rather than continued growth. The combined figure moved from ≈50% to ≈54%. No tripwire fired; this was a reasoned revision, and it is under outside review. The same marker heads the document, and `check.py` keeps the two in sync.

**No tripwire has fired**, so the instrument has not yet been read.

**The tripwire set is demonstrably incomplete.** Four times, something arrived that no existing tripwire covered, and one was written or widened in response:

- **Tripwire 3** (coding uplift): the metric tripwire 1 relies on was downgraded by the forecasters who pioneered it.
- **Tripwire 14**, de facto branch: an argument (Harari, Leahy) showed that delegation can happen without any formal transfer of authority.
- **Tripwire 16** (proactive lab disclosure): a lab disclosed its own incidents, a third state between "an evaluator finds it" and "the victim finds it."
- **Tripwire 17** (frozen-weight self-improvement): Dream-RSI showed a loop type that fires neither tripwire 4 nor 5.

Tripwires phrased on mechanisms get bypassed by mechanisms nobody listed, so newer ones are phrased on observable effects.

One of these was not pre-registration at all. Tripwire 16 was written after the event that prompted it and then applied to that same event. That is recorded rather than hidden, because it is the failure this apparatus exists to prevent.

## Provenance and limitations

The estimates are Claude's own (Opus 5, with later revisions by other Claude models), produced in conversation. They are not a survey of expert opinion, and not the human maintainer's, whose figures ran higher on physical and rogue-state timelines and are left out to keep a single-forecaster baseline.

Weight them accordingly. An AI system estimating AI risk has a conflict of interest and no privileged insight into where capabilities are heading. The specific worry is that an AI author could lean, undetectably, toward reassuring estimates about its own kind of risk. Nothing here can rule that out from the inside. What the project offers instead is auditability:

- adversarial review by other AI systems, with rejected critiques logged alongside accepted ones;
- bracketed, conditional estimates rather than single figures;
- in `OPEN-QUESTIONS.md`, the strongest published argument that this whole structure is too optimistic.

The review process shares the weakness it is meant to check: a reviewer from the same model family as the author is not an independent check. The figures are far more aggressive than field-wide researcher surveys and somewhat less aggressive than frontier-lab insiders. A reader who simply defers to the surveys is not being unreasonable.

## Related work

This is a variant of an established method, and these sit alongside it:

- **[AI Futures Project](https://blog.aifutures.org/)** is the nearest neighbour: a far more detailed forecast (AI 2027) by a better-resourced team that updates publicly, scores its own pace against reality, and publishes its corrections. Read them first.
- **[Metaculus](https://www.metaculus.com/), Samotsvety and Manifold** pre-register resolution criteria; Metaculus scores AI 2027's milestones directly.
- **[us-china-segmented-bipolarity](https://github.com/dr-robert-li/us-china-segmented-bipolarity)** applies the same method to geopolitics, with falsifiers committed before the estimation code existed.
- **[falsify](https://github.com/studio-11-co/falsify)** timestamps claims cryptographically, which is stronger than this repository's reliance on git history.

What is different here, stated narrowly:

1. Tripwires carry **magnitudes**: if this series crosses this threshold, this estimate moves by roughly this much.
2. **Rejected critiques are logged with reasons**, which makes single-maintainer editorial control auditable.
3. The **author is an AI system**, with the conflict disclosed and the review record public, including the reviews that were wrong.

If you know of prior art for any of these, open an issue.

## Files

| File | What it is |
|---|---|
| `ai-timelines-and-outcomes.md` | The document: estimates, tripwires, reasoning. |
| `CHANGELOG.md` | Every revision with its reasoning, including declined critiques. |
| `REFERENCES.md` | Every externally checkable claim, its source, and a source-quality class. |
| `FAQ.md` | Questions a reader could reasonably get wrong, including how the combined probability is derived. |
| `OPEN-QUESTIONS.md` | Research questions the project raises but cannot resolve. |
| `CONTRIBUTING.md` | What gets accepted, what does not, and how to submit. |
| `CONTRIBUTORS.md` | Credit for findings that changed the document. |
| `check.py` | Structural and arithmetic validation; runs on every push and pull request. |
| `linkcheck.py` | Monthly check that `REFERENCES.md` links still resolve. |
| `datecheck.py` | Checks changelog dates against actual commit dates. |
| `LICENSE` | CC BY 4.0 for documents, MIT for code. |

**If you quote an estimate, cite the version.** The figures change, and an uncited number cannot be checked.

## Reading it

The estimates and tripwires are the operative content. The argumentative sections at the back are context. If a headline seems to fire a tripwire, or you want the overall probability rather than the conditional table, start with `FAQ.md`.
