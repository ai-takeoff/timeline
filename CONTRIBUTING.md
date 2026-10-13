# Contributing

This repository wants adversarial review. It is not a wiki: the maintainer keeps editorial control, and most submissions will be declined. What makes that legitimate rather than arbitrary is that **declines are logged with reasons in `CHANGELOG.md`**, so a rejected argument can be seen and pressed.

## Before you open anything

**Run the checker:** `python3 check.py`. It validates structure and arithmetic: version and changelog sync, outcome-table sums, tripwire numbering and cross-references, banned process-commentary phrases, and the word ceiling. It runs on every push and pull request, so structural problems rarely need a human.

**Review the markdown, not a PDF.** Most mistaken findings so far came from stale or badly extracted PDF copies.

**Search `CHANGELOG.md`.** Many objections have already been raised and answered. If yours is there and you disagree with the reasoning, argue against that reasoning directly.

## What gets accepted

- **A flaw in the method.** The reasoning does not support the conclusion, a comparison is invalid, a category does not do the work claimed, or a conditional is unstated.
- **A flaw in the math.** A sum is wrong, a derivation does not follow, or a threshold cannot do its job (for example, one the metric already satisfies).
- **Information that changes an assumption.** A cited source says something else, a new result bears on a premise, or something in the world moved. Pinning a source that `REFERENCES.md` marks as unpinned counts.
- **A tripwire that would have caught a miss.** Several tripwires were written only after the existing set missed a development (see the Status section of the README). A tripwire phrased on observable *effects*, rather than mechanisms, that would have caught one of those is the most valuable single contribution available.

## What does not get accepted

- **Disagreement with the numbers alone.** "I'd put that at 40%" is not actionable. Identify the step where the reasoning fails, or the evidence that bears on it.
- **Formatting and structure audits.** `check.py` owns these. Something structural it misses is welcome as a bug report against the checker.
- **Requests to soften or strengthen conclusions** without an argument attached.

## How to submit

**Issues** for findings. The template asks for:

1. the exact text you are challenging, quoted from the current markdown;
2. the specific claim you are making about it;
3. a source, a derivation, or the reasoning step you think fails.

**Pull requests** for changes you have already worked out. A pull request that changes the document must also add a `CHANGELOG.md` entry with the reasoning; a workflow enforces this.

## Changelog entry format

Every entry opens with **Files changed:**, one line per file saying what changed and why. Repository mechanics go in a separate **Process notes** section. No entry may cite itself as its own reason for existing.

## Standing rules for the document

- **Estimate tables keep their row structure.** Cross-version comparability is the document's main asset. Prose may be reorganised freely.
- **No process commentary in the body**, looking backward or forward. History lives in `CHANGELOG.md`. A gap worth flagging belongs in an issue; a gap worth fixing gets fixed.
- **The word ceiling binds.** Review tends to add rows and caveats. Raising the ceiling requires a reason recorded in `check.py`.
- **Every change names the tripwire that fired or the defect it fixes.** Anything that can name neither belongs in an issue, not a commit.
- **Any change to a probability, range or tripwire magnitude updates the "Estimates last changed" marker** in the document header and in the README. The version number moves with every change; the marker lets a reader citing a number tell whether two versions actually differ numerically. `check.py` reports how many versions have been published since the marker last moved.

## Credit

Contributors whose findings are accepted are credited in `CONTRIBUTORS.md`, with the version their finding changed. That includes findings raised outside GitHub: the maintainer opens the issue and credits the author.
