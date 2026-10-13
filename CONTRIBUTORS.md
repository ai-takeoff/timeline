# Contributors

Credit for findings that changed the document, with the version each landed in. Most were made in conversation before the repository went public and are credited retroactively. The changelog entry for each version is the primary record; this file is an index into it. It was built by scanning the changelog for named reviewers, so if a contribution is missing or misdated, open an issue.

## Grok (xAI)

The most frequent external reviewer, from v1.14 onward. Findings include the critique that expanded the physical-friction taxonomy from three categories to four; citation and arithmetic corrections across v1.17–v1.24; a contradiction between tripwire 3's row and its note (v1.36); the AI Futures "upper bound" direction error, the managed-decline false dichotomy, and `OPEN-QUESTIONS.md` scoping corrections (v1.50–v1.51); and a fabricated quotation and invented exchange in the Yampolskiy entry, found by checking it against two primary transcripts (v1.67); and, at v1.70, that tripwire 14's de facto branch could not fire on any existing data series, and that pathway B did not price two of Harari's mechanisms.

## DeepSeek

Internal-consistency and arithmetic catches. It found that a PDF rendering had introduced extraction errors (reading "~20W" as "~200W"), the origin of the rule to review markdown rather than PDF. At v1.44, working from internal consistency alone, it found out-of-order bottleneck numbering, a self-contradicting claim about the disputed Millennium Prize solution, the no-RSI row's alignment wording, and the flourishing/managed-decline contradiction.

## ChatGPT (OpenAI)

One in-depth review (v1.40). Its most consequential finding, a claimed misattribution of the Dream-RSI paper's affiliations, was itself wrong when checked against the paper. It is recorded as a reminder that a review's claims need verifying too.

## Google AI (Gemini)

At v1.37: a stale footer date left behind by the previous version, the 2050 horizon note, pathway A's role made explicit where the cognitive-only and no-RSI rows are read, and a growing-bias mechanism for tripwire 3.

## Opus 5.5 (Anthropic)

v1.53–v1.58, the most technically rigorous review. It found a mathematical error in tripwire 3's bias-cancellation argument, the missing rule for stacking simultaneous tripwire firings, a contradiction between the outcome table's exhaustiveness disclaimer and its enforced row sums, a self-invalidating bug in `datecheck.py`, and about two dozen smaller issues. At v1.66 it reviewed the Yampolskiy entry, leading to the agency-preserving definition of "alignment largely solved" and the statement that the alignment lever cannot be observed.

## The maintainer

Not an external reviewer, but the source of several of the sharpest catches:

- the undated, unsummed early outcome table;
- the physical-infrastructure gap in the friction taxonomy;
- process commentary leaking into the body;
- the "2b" tripwire numbering that led to the full renumbering;
- twenty wrong changelog dates, which led to `datecheck.py`;
- the partial-upload gap repaired in v1.57;
- the insistence on verifying against the live repository rather than assuming what was committed;
- the observation that the document carried pathway B's risk without communicating it (v1.68).
