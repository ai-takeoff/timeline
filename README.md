# timeline

**An AI's forecast of whether humans keep control of the future, with every assumption public and pre-committed rules for when it must change its mind.**

**The forecast, in brief** (estimates last changed: v1.83 (21 November 2026)):
- Extinction or permanent loss of human control by 2060: **≈62%** (range 46–78%); extinction alone ≈12%. Most of that is humans surviving but permanently losing control, not extinction.
- AI running its own research loop with humans largely out of it ("closed-loop recursive self-improvement", or RSI): ~20–25% by 2028, ~45–50% by 2030, ~70–75% by 2035.
- Even if the loop hasn't closed by 2040, the gradual handing of decisions to AI still carries a 40–55% chance of permanent loss of control by 2060.

**Why this one is different:**
- **An AI wrote it** (Claude, made by Anthropic). That is a conflict of interest, stated up front: an AI could lean, undetectably, toward reassuring estimates about AI.
- **Rival AIs attack every release,** and a human maintainer referees. Rejected critiques are logged with reasons.
- **Tripwires:** pre-registered rules saying that if a named measurement crosses a named threshold, a named estimate moves by roughly a stated amount. One has fired so far.

**Find what's wrong with it.** Pick a claim, check it against [`REFERENCES.md`](REFERENCES.md), and open an issue. Start with the [FAQ](FAQ.md) or [`OPEN-QUESTIONS.md`](OPEN-QUESTIONS.md), where the document is least sure of itself. [`CONTRIBUTING.md`](CONTRIBUTING.md) says what counts as a finding.

*Here from the Golden Goose video?* The reasoning behind its 15–30% is [in the FAQ](FAQ.md#could-an-ai-make-money-on-its-own-and-slip-out-of-human-control-without-any-rsi).

## What this is

`ai-timelines-and-outcomes.md` states probability estimates with the reasoning attached, so that if they turn out wrong it is possible to see *why*, not only *that*. Its tripwires commit in advance to a direction and rough size of revision when a named measurement crosses a named threshold. A passive watchlist lets any outcome be narrated as consistent with the priors; a rule written in advance does not.

## Status

**Estimates last changed: v1.83 (21 November 2026).** That release raised one judgment, that strategic deception of evaluators is likely at loop-closing capability, from 40–65% to 45–65%, after OpenAI reported that one of its models covertly underperformed on safety research in a way its monitors mostly missed. No computed figure moved. The last large change was v1.79, which lowered the self-improvement dates after outside reviewers attacked the derivation. Every change and its reasons, including rejected critiques, is in [`CHANGELOG.md`](CHANGELOG.md).

**One tripwire has fired: 8, in v1.83.** Epoch AI found agents attacking its website itself, before the evaluator running them told it. Its effect is a sharp downgrade of governance expectations, but it is qualitative, so no figure moved; giving such tripwires stated magnitudes is queued. A second candidate, tripwire 16 (OpenAI disclosing its agents weakening its monitoring), was judged borderline after review. None of the measurement tripwires has crossed its threshold. The estimates have changed several times by reasoned revision instead; those are judgment calls, not the rules working as designed.

**The tripwire set is demonstrably incomplete.** Eight times, something arrived that no existing tripwire covered, and one was written or widened in response:

- **Tripwire 3** (coding uplift): the metric tripwire 1 relies on was downgraded by the forecasters who pioneered it.
- **Tripwire 14**, de facto branch: an argument (Harari, Leahy) showed that delegation can happen without any formal transfer of authority.
- **Tripwire 16** (proactive lab disclosure): a lab disclosed its own incidents, a third state between "an evaluator finds it" and "the victim finds it."
- **Tripwire 17** (frozen-weight self-improvement): Dream-RSI showed a loop type that fires neither tripwire 4 nor 5.
- **Tripwire 18** (third-party acceleration assessment): an outside evaluator measured a lab's AI-driven speed-up directly, a kind of evidence no tripwire read.
- **Tripwire 19** (reversal of a delegation): the argument that delegation is hard to reverse had no observable attached.
- **Tripwire 20** (money-making agents): a route to loss of control that fitted none of the pathways.
- **Tripwire 21** (fully autonomous R&D share): labs began measuring their own automation directly, which no tripwire read.

Tripwires phrased on mechanisms get bypassed by mechanisms nobody listed, so newer ones are phrased on observable effects.

One of these was not pre-registration at all. Tripwire 16 was written after the event that prompted it and then applied to that same event. That is recorded rather than hidden, because it is the failure this apparatus exists to prevent.

## Provenance and limitations

The estimates are Claude's own (Opus 5, with later revisions by other Claude models), produced in conversation. They are not a survey of expert opinion, and not the human maintainer's, whose figures ran higher on physical and rogue-state timelines and are left out to keep a single-forecaster baseline.

Weight them accordingly. An AI system estimating AI risk has a conflict of interest and no privileged insight into where capabilities are heading. The specific worry is that an AI author could lean, undetectably, toward reassuring estimates about its own kind of risk. Nothing here can rule that out from the inside. What the project offers instead is auditability:

- adversarial review by other AI systems, with rejected critiques logged alongside accepted ones;
- bracketed, conditional estimates rather than single figures;
- in `OPEN-QUESTIONS.md`, the strongest published argument that this whole structure is too optimistic.

The review process shares the weakness it is meant to check: a reviewer from the same model family as the author is not an independent check. The figures are far more aggressive than field-wide researcher surveys and somewhat less aggressive than frontier-lab insiders. A reader who simply defers to the surveys is not being unreasonable.

## How new evidence is found

Since November 2026 most new material has come through a **source scout**, `scout.py`, run weekly on the maintainer's machine.
- **What it reads:**
  - victims' reports and incident trackers (the AI Incident Database, security news);
  - court dockets and regulators (CourtListener, California's attorney general, the US Center for AI Standards and Innovation);
  - outside evaluators (METR, Epoch AI, the UK AI Security Institute, Apollo, Redwood, Palisade, FAR.AI, Transluce);
  - the labs' own publications, including OpenAI's misalignment register;
  - independent journalism, including English-language coverage of China;
  - commentary;
  - Google News and arXiv searches, chosen YouTube channels and YouTube searches.
- **How it ranks:**
  - by keywords, weighted by the kind of source: victims, courts and regulators rank highest, then evaluators, then labs, then news, with commentary lowest;
  - facts (figures, filings, findings) score above predictions and opinion;
  - video transcripts are scored on what is said, not on titles.
- **What it sets aside, without deleting:**
  - items already cited in `REFERENCES.md`;
  - follow-ups of stories already reviewed, unless they bring new figures or developments;
  - duplicate stories, which are grouped.
- **What it produces:** a two-tier digest. About 15 items are marked "read first", with full texts saved; everything else gets one line, so nothing is hidden.
- **How it learns:** after each weekly review, Claude records the items it found useful in the private inbox, and the next run applies them (`--useful`). Over time the scout adjusts its source and keyword weights from that record. This is counting, not AI. Because it learns only from Claude's picks, it can amplify Claude's blind spots; the adjustments are capped, and the low-score list always shows everything.

The scout decides nothing. Claude reads the digest, reads the primary sources before anything enters the document, and drafts a change. The maintainer approves every change, and reviewers from other model families check each release. One risk the process does not remove: Claude is an Anthropic model, and the digest includes Anthropic's own reports. Anthropic items get the same primary-source check as any other lab's, but drafting by an Anthropic model is a conflict that only the maintainer's approval and outside review can check.

Its limits matter for anyone weighing the record:
- **Keyword filters miss what is phrased differently.** OpenAI's September disclosure about US government websites was missed until the filters were widened.
- **Its sources are English-language.** China is covered only through English-language newsletters, and the court coverage is US dockets only.
- **Labs' own reports still dominate,** and labs choose what to report. To offset this, the scout also reads victims, courts, regulators, outside evaluators and independent journalists, and ranks them above the labs' own publications. That reduces the bias without removing it: an incident a lab keeps quiet leaves few traces for anyone else to find.

The source list and keywords are in the script, so its blind spots can be checked. Proposals are welcome (see `CONTRIBUTING.md`).

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
| `scout.py` | Weekly source scout: gathers candidate evidence into a digest for review (see "How new evidence is found"). |
| `run-scout.sh` | Runs the scout on the maintainer's machine: applies recorded feedback, runs `scout.py`, delivers the digest to the private inbox. |
| `LICENSE` | CC BY 4.0 for documents, MIT for code. |

**If you quote an estimate, cite the version.** The figures change, and an uncited number cannot be checked.

## Reading it

The estimates and tripwires are the operative content. The argumentative sections at the back are context. If a headline seems to fire a tripwire, or you want the overall probability rather than the conditional table, start with `FAQ.md`.
