## What this changes

<!-- One line. -->

## Which applies

- [ ] A tripwire fired — name it, and state the reading that crossed the threshold
- [ ] A defect is being fixed — name it
- [ ] Neither

If neither, this belongs in an issue rather than a pull request. Every change names the tripwire that fired or the defect it fixes; that rule is in CONTRIBUTING.md and is not paperwork.

## Checks

- [ ] `python3 check.py` passes locally
- [ ] Quoted or edited text came from the markdown, not the PDF
- [ ] `CHANGELOG.md` updated with the **reasoning**, not just the change
- [ ] If a source was added, it is in `REFERENCES.md` with a quality class, and in `check.py`'s source list

## If this changes an estimate

State the old value, the new value, and what moved it. An estimate change without a stated cause will be declined regardless of whether the new number is better.

<!--
Standing rules that will send a PR back:
- Estimate tables keep their row structure across versions
- No process commentary in the body, in either direction
- The word ceiling binds; raising it needs a reason recorded in check.py
-->
