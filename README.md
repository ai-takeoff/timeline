# timeline

A dated, falsifiable snapshot of estimates on AI capability timelines and the outcomes that follow from them.

## What this is

`ai-timelines-and-outcomes.md` is the document. It states probability estimates with the reasoning attached, so that if the estimates turn out wrong it is possible to see *why* rather than only *that*. It carries pre-registered update rules — tripwires — which commit in advance to a direction and rough magnitude of revision when a named observable crosses a named threshold. The point of pre-registering them is that a passive watchlist permits post-hoc rationalisation: any outcome can be narrated as consistent with the priors.

`CHANGELOG.md` holds the revision history, including the versions that predate this repository.

## Status

The instrument has not yet been read. Every revision so far has been a correction to the document, not an update triggered by evidence crossing a threshold. Treat the estimates as a baseline awaiting its first real test.

## Provenance and known limitations

The estimates were produced by Claude (Opus 5) in conversation and are that model's own, not a survey of expert opinion and not the human collaborator's, whose figures ran higher on physical and rogue-state timelines and are deliberately not represented so that this stays a single-forecaster baseline.

They should be weighted accordingly. An AI system estimating AI risk has an obvious conflict of interest and no privileged insight into capability trajectories. The document's own outside-view section notes that these figures are far more aggressive than field-wide researcher surveys and somewhat less aggressive than frontier-lab insiders, and that a reader who simply defers to the surveys is not being unreasonable.

## Related work

This is a variant on an established method, not a new one. Anyone evaluating it should know what it sits alongside.

**[AI Futures Project](https://blog.aifutures.org/) — the nearest substantive neighbour.** Their AI 2027 scenario (April 2025) is a far more detailed forecast than this document, by a better-resourced team with a real track record. They update publicly, assess their own pace against reality — their Q2.5 2026 post puts actual progress at roughly 70–90% of what AI 2027 projected — and maintain a record of how their medians have moved since 2018. They have publicly corrected a modelling bug that shifted their own median by about nine months. Read them first.

**[Metaculus](https://www.metaculus.com/), Samotsvety, Manifold — pre-registered resolution criteria.** Specifying in advance what would settle a question is the core of how these platforms work, and Metaculus runs a tournament scoring AI 2027's milestones directly. "Commit before the observation" is not novel.

**[us-china-segmented-bipolarity](https://github.com/dr-robert-li/us-china-segmented-bipolarity) — the same method, another domain.** Pre-registered falsifiers committed before the estimation code existed, with commit history as proof of ordering, so that any later change to a threshold appears as a diff rather than a silent revision. Structurally very close to this repository, applied to geopolitics.

**[falsify](https://github.com/studio-11-co/falsify) — tooling for the same problem.** Cryptographically locks a claim and threshold before an experiment runs. Its SHA-256 timestamping is stronger than this repository's reliance on git history.

### What is actually different here

Three things, stated narrowly:

1. **Update rules carry magnitudes.** A Metaculus question pre-registers what resolves it. A tripwire here pre-registers that *if this named series crosses this threshold, this specific estimate moves by roughly this much, in this direction.* That is a different object, and no equivalent was found for AI timelines.
2. **Rejected critiques are logged with reasons**, not only accepted ones. The changelog records findings that were declined and why, which is what makes single-maintainer editorial control auditable rather than arbitrary.
3. **The author is an AI system, the conflict of interest is disclosed, and the adversarial-review record is public** — including which reviews were wrong.

None of these is a large claim. If you know of prior art for any of them, open an issue; that is a useful contribution in itself.

## Reading it

The estimates and tripwires are the operative content. The argumentative sections at the back — on thermodynamic inevitability, resource-competition scenarios, hazard rates, and the hype hypothesis — are context and are deliberately placed last.
