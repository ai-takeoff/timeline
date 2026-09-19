# Contributing

This repository wants adversarial review. It is not a wiki — editorial control stays with the maintainer, and most submissions will be declined. What makes that legitimate rather than arbitrary is that **declines are logged with reasons in `CHANGELOG.md`**, so a rejected argument can be seen and pressed.

## Before you open anything

**Run the checker.**

```bash
python3 check.py
```

It validates structure and arithmetic: version/changelog synchronisation, outcome-table midpoints, tripwire numbering and ordering, cross-references, empty cells, banned process-commentary phrases, and the word ceiling. It runs automatically on every push and pull request.

Across the review rounds that preceded public release, **structural complaints produced more false positives than real findings** — usually from reviewers reading a stale PDF rather than current markdown. The checker now covers that ground better than a human can. Reviewing the rendered PDF is the single most common way to waste your own time and the maintainer's.

**Read `CHANGELOG.md` first.** Many objections have already been raised and answered. If yours is there and you disagree with the reasoning, say so explicitly and argue against it — that is welcome, and more useful than raising it as though new.

## What gets accepted

**A flaw in the method.** The reasoning does not support the conclusion. A comparison is invalid. A category does not do the work it claims. A conditional is not stated.

**A flaw in the math.** A sum is wrong. A derivation does not follow. A threshold is set where it cannot do its job — as with tripwire 1, which was originally set at a value the metric already satisfied.

**Information that changes an assumption.** A cited source says something other than what the document claims. A new result bears on a premise. Something in the world moved. `REFERENCES.md` lists every externally checkable claim with its source class; unpinned sources are marked, and pinning one is a real contribution.

**A tripwire that would have caught a miss.** Three tripwires were written *after* a development the existing set failed to anticipate (now numbered 3, 16, and 17 — see `CHANGELOG.md` for what each was added in response to). Tripwires phrased on mechanisms get bypassed by mechanisms not enumerated in advance. A tripwire phrased on observable *effects* that would have caught one of those three is the most valuable single contribution available.

## What does not get accepted

**Disagreement with the numbers.** Disagreement is not a finding. If you think an estimate is wrong, identify the step where the reasoning goes wrong, or the evidence that bears on it. "I'd put that at 40%" is not actionable.

**Formatting and structure audits.** `check.py` owns this. If you find something structural it misses, that is a bug report against the checker and is welcome as such.

**Requests to soften or strengthen conclusions** without an argument attached.

## How to submit

**Issues** for findings. The template asks for three things:

1. The exact text you are challenging, quoted from current markdown (not the PDF).
2. The specific claim you are making about it.
3. A source, a derivation, or the reasoning step you think fails.

**Pull requests** for changes you have already worked out. `check.py` runs on every PR, so structural problems surface before review. A PR that changes an estimate must also update `CHANGELOG.md` with the reasoning — the log is the substance, not paperwork.

## Standing rules for the document

These apply to any accepted change, and a PR that violates them will be asked to revise:

- **Estimate tables keep their row structure across versions.** Cross-version comparability is this document's main asset. Prose may be reorganised freely; tables should not be, absent a strong reason.
- **No process commentary in the body, in either direction.** Not what an earlier version said, nor what a future one should do. History lives in `CHANGELOG.md`. A gap worth flagging belongs in an issue; a gap worth fixing gets fixed.
- **The word ceiling binds.** It guards against accretion from review, which historically pushes toward more rows and more caveats. Raising it requires a stated reason recorded in `check.py`.
- **Every change names the tripwire that fired or the defect it fixes.** Anything that can name neither belongs in an issue, not a commit.

## Credit

Contributors whose findings are accepted are credited in `CONTRIBUTORS.md`, with the version their finding changed. This applies to findings raised in comments elsewhere as well — if a real finding arrives outside GitHub, the maintainer opens the issue and credits its author.
