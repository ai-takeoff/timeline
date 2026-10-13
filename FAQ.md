# FAQ

Questions a reader could reasonably get wrong on first encounter, with answers you can check against the main document. Unlike the questions in [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md), these have answers. If you think an answer here is wrong, open a Finding issue and quote the passage you are challenging.

---

## A new AI system claims "recursive self-improvement." Doesn't that fire tripwire 17?

Check which side of one line the result is on.

Tripwire 17 fires on scaffolding gains reported on **model design, training-method search, or evaluation design** — decisions that shape how a frontier model itself gets built, trained, or measured. It does not fire on **algorithm engineering and kernels** — general coding, optimization, and research-tooling work, however impressive the results or however good the evidence that it generalizes — because those tasks give fast, cheap, checkable feedback (the code runs faster or it doesn't, the answer verifies or it doesn't), which is exactly what lets a scaffold improve itself without retraining anything. Improving how a frontier model is designed and trained has no such shortcut: every candidate change still has to be tested by a real training run that takes weeks and costs millions, so success in the cheap-feedback domain doesn't tell you the trick works in the expensive one.

The test to apply to any new claim: does the result improve *how a frontier model gets designed, trained, or evaluated*, or does it improve *the tool doing the improving* — search policy, memory management, harness code — on general engineering tasks? Only the first can fire the tripwire.

### Four real results, checked against that line

| Result | What it actually improved | Side of the line |
|---|---|---|
| Dream-RSI (arXiv 2609.14858) | The exploration policy of a frozen agent, on algorithm design, math optimization, and GPU kernels | Non-firing. This is the tripwire's own named example of the non-firing side |
| ScienceBuddy, PhAI Labs (arXiv 2609.17523) | An agent harness (inner loop, model fixed), then the model itself via reinforcement learning on trajectories produced under that harness, on genomics, biology, and literature-retrieval tasks | Non-firing. A different domain entirely, and a small task model rather than a frontier one |
| DSec, DeepSeek (arXiv 2609.22978) | Sandbox infrastructure for training agents at scale, including agents building the training environments used to train later agents | Non-firing. Training infrastructure, not a training-method, model-design, or evaluation-design result |
| AIDE², Weco AI (arXiv 2609.26457) | An AI research agent's own harness (search policy, memory management), evaluated on machine-learning-engineering benchmarks, with gains that carried over to four held-out benchmarks | Non-firing. ML engineering by a research-tooling agent, not model design. Weco itself places the result at Level 1 on its own 0–3 scale |

Each is real progress on the non-firing side. None of the four reports a result on the firing side.

### What would fire it

A report of Dream-RSI-style scaffolding gains — frozen weights, better search — measured on model design, training-method search, or evaluation design, rather than on algorithm engineering and kernels. That is the tripwire's observable, as worded in the main document.

A stronger and separate event is a system-originated training or architectural change actually adopted into a production run. That is tripwire 4, not tripwire 17, and it carries a much larger update.

Even when tripwire 17 does fire, the main document is explicit about how much it means: cheap search makes *proposing* candidate training methods faster, but not *evaluating* them, and evaluation — a real training run — is the expensive step that still bottlenecks the loop. That is why tripwire 17 carries a modest magnitude (closed-loop 2030 +8 points, hard takeoff +2) rather than a large one.

### Why this is stated as a test rather than a list

Harness self-improvement is an active research area with many groups working on it, so more results like these are coming. A list of examples goes stale with the next headline; a test lets you apply the same check yourself without waiting for this document to catch up.

### If you think a result belongs on the firing side

Open a Finding issue, quote the specific passage in the paper showing the technique applied to model design, training-method search, or evaluation design, and say what was measured. That is the evidence that would change this answer.

---

## Hasn't AI already taken over, without any "singularity"?

That is a serious view, and the main document's numbers already give it a lot of weight. It is also easy to miss, because the document's dated predictions are about recursive self-improvement (RSI), and RSI is not where most of this risk lives.

### The view, at full strength

Yuval Noah Harari's Tanner Lecture at Oxford (21 May 2026, "AI has hacked the code of human civilization") argues that AI does not need to rebel, self-improve, or build robots to take control. Human dominance rests on large-scale cooperation, and that cooperation runs through bureaucracies — banks, courts, states, churches — whose operating code is language. AI is a "native bureaucrat": it can hold every law, every transaction, every precedent at once. As AI systems take over loan decisions, admissions, hiring, sentencing and targeting, control shifts from inside, with no single moment anyone would call a takeover. He adds a second channel: as AI masters language it moves from capturing attention (social media) to forming intimate relationships, and so into the trust that all of those institutions depend on. His present-tense evidence is social media ranking algorithms, narrow optimizers that changed politics worldwide without being agents in any strong sense.

Connor Leahy makes a related point about oversight: there may be human CEOs for a long time, but if they "just rubber stamp what the AI CEOs tell them to do," that is not oversight.

### Where the document already agrees

This is **pathway B** — fragmentation and delegation, no RSI required. It needs no misalignment, no takeoff, and no coherent adversary, only that delegation is individually rational and complexity outpaces oversight. The outcome table gives the world in which the loop never closes **25–40% permanent disempowerment** by 2060. That is roughly two-thirds of the disempowerment risk of the worst RSI row, and the main document says so directly: RSI raises the odds of disempowerment but does not create them.

### Where the document disagrees, or cannot tell

- **"Has taken over" versus "is taking over."** Most of Harari's claims are in the future tense ("will decide," "over the next ten years"). Formal authority over money, law and force is still human in 2026. What can be measured is whether delegation is outrunning the ability to review it.
- **Narrow optimizers are not the same as agents.** Social media rankers show that low-capability systems can reshape societies. They do not show that today's systems are making the consequential decisions Harari lists.
- **The table cannot see it happening.** Outcomes are assessed as of 2060, so a process already under way has no reading there.

### How the document would see it

**Tripwire 14** fires when major economic, military or administrative decision authority over millions of people is delegated to agent systems, **formally** (no human sign-off: pathway B disempowerment +10 points) or **de facto** (sign-off kept but documented as non-substantive, such as ~95%+ approval at review times too short for independent assessment: +5 points). The de facto branch exists because Harari's and Leahy's mechanism never involves a formal transfer. It carries half the magnitude because high approval rates are also what good recommendations produce.

If you find a documented case that meets the de facto branch, open a Finding issue with the source.

---

## What is the overall probability? The table only gives conditionals.

The main document states one combined figure: extinction or permanent disempowerment by 2060 **≈50%**, extinction alone **≈12%**. This is how it is built, so you can rerun it with your own inputs.

### Inputs

| Input | Range used | Midpoint | Where it comes from |
|---|---|---|---|
| Closed-loop cognitive RSI by 2040 | 70–85% | 77.5% | Extends the timeline table's ~70% by 2035; not otherwise stated in the document |
| Human-less RSI by 2040, given cognitive RSI | 25–35% | 30% | Physical table |
| Alignment largely solved at loop-close | 15–35% | 25% | Author judgment, stated in the main document |
| Holds through 2060, given solved at loop-close | 50–75% | 62.5% | Author judgment, stated in the main document |
| Outcome cells | As in the table | Cell midpoints | Outcome table |

The two alignment judgments were set after seeing probability elicitations from other AI systems. Those systems share training data and framing with the author, so the judgments are not independent of them, and the elicitations themselves are not treated as evidence. An alignment solution only counts for the "solved" rows if it holds through 2060, so the effective weight on those rows is the product: about 16% at midpoints.

### Result at midpoints

| Scenario | Weight | Extinction + disempowerment (row midpoints) | Contribution |
|---|---|---|---|
| Human-less RSI, unsolved | 19.6% | 72.5% | 14.2 |
| Human-less RSI, solved | 3.6% | 20.5% | 0.7 |
| Cognitive-only RSI, unsolved | 45.8% | 56.5% | 25.9 |
| Cognitive-only RSI, solved | 8.5% | 17% | 1.4 |
| No closed-loop RSI by 2040 | 22.5% | 37.5% | 8.4 |
| **Total** | 100% | | **≈50.7** |

Extinction alone, computed the same way, comes to about 11.7%.

### Sensitivity

| Change, others at midpoint | Extinction | Extinction + disempowerment |
|---|---|---|
| Alignment solved at 15% / 35% | 12.3% / 11.1% | 52.8% / 48.6% |
| Holds through 2060 at 50% / 75% | 12.0% / 11.4% | 51.8% / 49.7% |
| Closed-loop RSI by 2040 at 70% / 85% | 11.1% / 12.4% | 49.4% / 52.0% |
| Every outcome cell at its low / high end | 8.5% / 14.9% | 40.7% / 60.7% |
| Every input at its optimistic / pessimistic end | 7.0% / 17.3% | 36.3% / 66.2% |

**What this shows.** The combined figure barely moves with the alignment parameters, because even at their high end the "solved" rows carry less than a third of the weight. Almost all of the result comes from the unsolved rows and the no-RSI row, and its width comes from the outcome cells themselves. A reader who wants to argue the figure down has to argue those cells down. Arguing that alignment is more likely to be solved is not enough on its own.

### What the figure does not include

- Risks with no AI component.
- Outcomes after 2060.
- The "managed decline" futures that fit none of the three columns, which were folded into the existing columns when the cells were set.
- Any distinction between disempowered futures that are comfortable and ones that are worse than extinction (see the next entry but one).

---

## How should I read the spread of expert estimates?

Named estimates range from near zero to near certainty, and the spread is not noise to average away. Three things help.

### 1. Incentives cut in both directions — apply them symmetrically

Two opposite incentive critiques are in circulation, and each discounts a different group:

- **Insiders are biased toward optimism.** People paid by frontier labs have reasons to see their work as safe. On this reading, the numbers that matter most come from people who left or were never employed there.
- **Insiders are biased toward alarm.** Karen Hao (*Empire of AI*) argues that lab leaders' catastrophe talk is "an act of speech to persuade": it justifies keeping the technology in their hands, and the speakers come to half-believe it. On this reading, CEO risk figures are marketing, not forecasts.

Applied consistently, each critique discounts a lab leader's warnings and that same leader's reassurances by the same amount. Neither touches the arguments themselves, which have to be weighed on their merits. Neither applies to people who gave up money or position to say what they said. A costly signal is better evidence than a cheap one in either direction.

### 2. Vantage point changes what a person can see

| Person | Vantage point | Stated figure | Where |
|---|---|---|---|
| Jacob Coxon | Former OpenAI and Anthropic researcher; resigned from Anthropic, Sept 2026 | "More likely than not that humanity loses control," possibly ending in extinction; no timeline | NYC Council hearing, 5 Oct 2026 |
| Alex Turner | Former Google DeepMind researcher | AI takeover "roughly one in three"; no timeline | Same hearing |
| Daniel Kokotajlo | Former OpenAI researcher; AI Futures Project | ~50% chance of full AI R&D automation by end of 2028 (a timeline, not a doom figure) | US Senate testimony, 30 Sep 2026 |
| Frontier-lab representatives | Anthropic, OpenAI, Google, Meta | Declined to give a number when asked for a worst-case estimate; OpenAI's said no level of that risk is acceptable | NYC Council hearing |
| Roman Yampolskiy | Academic AI-safety researcher, never at a lab | "I am at 99.999999%" | His own post, 12 Mar 2024 |
| Tristan Harris | Societal-impact focus; says the architecture question is outside his expertise | No figure; says he thinks the companies plan to close the recursive loop "in the next 12 months" | Interview, date not pinned |
| Field-wide survey | 2,778 published AI researchers | Median 5% chance of extremely bad outcomes such as extinction; human-level AI 50% by 2047 | Grace et al. 2024; see the main document |

Three former insiders at one hearing gave three different answers: more likely than not, one in three, and no number at all. Distance from the frontier does not cleanly predict the number. People closer to the systems see capability first-hand; people further away see institutions, incentives and history. Both are evidence.

### 3. "Alignment is a sham" is three different claims

Statements that alignment cannot work usually mean one of these:

1. **Impossible in principle.** Durable control of a smarter system is a logical impossibility (Yampolskiy). See `OPEN-QUESTIONS.md`.
2. **Not achievable with current methods.** Training on observed behavior selects for looking aligned, so current methods cannot tell real alignment from performance (the Selsam quotation in Kokotajlo's testimony: "Models will increasingly seem aligned even when they are not").
3. **Not being seriously attempted.** The effort is too small, too fast, and too commercially pressured to succeed, whatever is possible in principle (Leahy's "clown show").

These have different evidence and different remedies. The main document's stated range for "strategic deception of evaluators by default" (40–65%) is its position on the second. Its 15–35% for alignment being largely solved at loop-close reflects all three together.

---

## Which future does each outcome column actually include?

Max Tegmark's *Life 3.0* (2017) describes twelve possible AI aftermaths. Mapping them onto the document's three columns shows what the columns capture and what they flatten.

| Tegmark scenario | Column | Note |
|---|---|---|
| Libertarian utopia | Flourishing or disempowerment | Depends on whether humans keep control over civilizational direction or only over their own zones |
| Benevolent dictator | **Disempowerment** | However good it feels; the document requires agency to be preserved |
| Egalitarian utopia | Flourishing | Requires that superintelligence is never built, or is restrained |
| Gatekeeper | Flourishing, if humans set and can revise the gatekeeper's goal | Otherwise disempowerment |
| Protector god | **Disempowerment** | Hidden steering is lost control even if no one notices |
| Enslaved god | Flourishing for whoever controls it | For most of humanity, power concentration: closer to disempowerment |
| Conquerors | Extinction | |
| Descendants | Extinction | Scored as extinction of humans, whatever one thinks of the successors |
| Zookeeper | Disempowerment | Possibly worse than extinction (see below) |
| 1984 | None cleanly | Human-run surveillance state; humans keep control, so not disempowerment by AI, but not flourishing either |
| Reversion | None cleanly | A deliberate retreat from technology is the "managed decline" case the main document says fits no column |
| Self-destruction | Extinction / irrecoverable collapse | |

### What the columns flatten: welfare

The columns score *survival* and *agency*. They do not score *welfare*. A comfortable benevolent-dictator world and a zookeeper world — humans kept alive, confined and studied, or kept in a "happiness factory" — land in the same disempowerment column. Many people would rank the second as worse than extinction. The document has no axis for that, so it cannot say how much of its disempowerment mass is the comfortable kind and how much the kind people fear most. It is a real gap, not a hidden assumption. Closing it would mean splitting the disempowerment column and re-deriving every row.
