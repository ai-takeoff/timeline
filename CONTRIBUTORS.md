# Contributors

Credit for findings that changed this document, per the promise in `CONTRIBUTING.md`: contributors whose findings are accepted are credited here, with the version their finding landed in, including findings raised outside GitHub — this document's review history predates the repository's public existence, so most contributions here were made in conversation and credited retroactively rather than filed as GitHub issues. That does not make them less real; the changelog entry for each version is the primary record, and this file is an index into it, not a separate source of truth.

**This is a first pass, built by scanning the changelog for named reviewers, not a line-by-line audit of every finding in every version.** If a real contribution is missing or a version number is wrong, that is itself a legitimate finding — open an issue.

---

## Grok (xAI)

The most frequent external reviewer, across many rounds from v1.14 onward. Findings that changed the document include: the physical-friction taxonomy's original three-category framing (later expanded to four after Grok's critique of the coordination/institutional/phase-transition split), multiple citation and arithmetic corrections in the v1.17–v1.24 range, the observation that AI 2027's timeline had already drifted across the project's own outside-view section, and continued structural review through the v1.42–v1.44 stretch.

## DeepSeek

Contributed the "Impossible Date Bug" framing and several internal-consistency catches focused on arithmetic and cross-references rather than external sourcing — notably the discovery, in an early pass, that a PDF rendering of the document had introduced text-extraction errors (misreading "~20W" as "~200W"), which is the origin of this project's rule to review current markdown rather than the PDF.

## ChatGPT (OpenAI)

Reviewed the document once, in depth (v1.40). Its most consequential finding was incorrect — a claimed misattribution of the Dream-RSI paper's institutional affiliations, which turned out to be accurate when checked directly against the paper and independent fact-checks. Recorded in the changelog as an instance of a review's own claim needing verification, not just the document's.

## Google AI (Gemini)

Multiple rounds through v1.36–v1.38, focused on structural consistency: bottleneck numbering out of sequence, a self-contradicting "resolved early" claim about the Millennium Prize datum, the no-RSI row's alignment-conditioning language, and the flourishing/managed-decline definitional contradiction that led to the current wording explicitly stating the gap rather than papering over it.

## Opus 5.5 (Anthropic)

The most technically rigorous review received, v1.53–v1.57. Found a genuine mathematical error in tripwire 3's bias-cancellation argument (present since v1.29, undetected through several later edits to the same passage), the absence of any tripwire-stacking or column-propagation rule, a direct contradiction between the outcome table's exhaustiveness disclaimer and its enforced row sums, a self-invalidating bug in `datecheck.py`, and roughly two dozen smaller regressions and structural issues across every file in the repository, nearly all of which were confirmed real on direct verification before being fixed.

## The user (maintainer)

Not a contributor in the "external review" sense, but the source of several of the sharpest catches in this project's history, including: the undated, unsummed early version of the outcome table; the physical-infrastructure gap in the original three-category friction taxonomy; the process-commentary leak in early versions; the "2b" tripwire-numbering complaint that led to the full renumbering; the discovery that twenty changelog dates were wrong (leading to `datecheck.py`); the discovery of the partial-upload gap that produced v1.57's repair; and the repeated, correct insistence on verifying claims against the live repository rather than assuming committed state, which is now this project's standing practice.
