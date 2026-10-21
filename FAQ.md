# FAQ

Questions a reader could reasonably get wrong on first encounter, with answers you can check against the main document. Unlike those in `OPEN-QUESTIONS.md`, these have answers. If you think one is wrong, open a Finding issue quoting the passage.

---

## A new AI system claims "recursive self-improvement." Doesn't that fire tripwire 17?

Usually not. Check which side of one line the result falls on.

Tripwire 17 fires on scaffolding gains reported on **model design, training-method search, or evaluation design**: decisions about how a frontier model is built, trained or measured. It does not fire on **algorithm engineering and kernels**, however impressive. Those tasks give fast, cheap, checkable feedback (the code runs faster or it doesn't), which is exactly what lets a scaffold improve itself without retraining anything. Improving how a frontier model is trained has no such shortcut: every candidate change must be tested by a real training run that takes weeks and costs millions. Success on the cheap side says little about the expensive one.

**The test:** does the result improve *how a frontier model is designed, trained or evaluated*, or *the tool doing the improving* (search policy, memory, harness code) on general engineering tasks? Only the first can fire the tripwire.

| Result | What it improved | Side of the line |
|---|---|---|
| Dream-RSI (arXiv 2609.14858) | A frozen agent's exploration policy, on algorithm design, math optimization and GPU kernels | Non-firing; the tripwire's own named example |
| ScienceBuddy, PhAI Labs (arXiv 2609.17523) | An agent harness, then a small task model trained on its trajectories, in genomics, biology and literature retrieval | Non-firing; different domain, not a frontier model |
| DSec, DeepSeek (arXiv 2609.22978) | Sandbox infrastructure for training agents, including agents building later agents' training environments | Non-firing; infrastructure, not a training-method or design result |
| AIDE², Weco AI (arXiv 2609.26457) | A research agent's own harness, on machine-learning-engineering benchmarks, with gains carrying over to held-out benchmarks | Non-firing; ML engineering by a tooling agent. Weco itself places it at Level 1 of its 0–3 scale |

**What would fire it:** frozen-weight scaffolding gains measured on model design, training-method search or evaluation design. A system-originated training change actually adopted into a production run is a different, stronger event: tripwire 4.

Even then the update is modest (closed-loop 2030 +8 points, hard takeoff +2), because cheap search speeds up *proposing* training methods but not *evaluating* them, and evaluation is the bottleneck.

If you think a result belongs on the firing side, open a Finding issue quoting the passage that shows it applied to model design, training-method search or evaluation design, and say what was measured.

---

## Hasn't AI already taken over, without any "singularity"?

It is a serious view, and the main document's numbers already give it a lot of weight. It is easy to miss because the dated predictions are about recursive self-improvement (RSI), which is not where most of this risk lives.

### The view, at full strength

Yuval Noah Harari's Tanner Lecture at Oxford (21 May 2026) argues that AI need not rebel, self-improve or build robots to take control. Human dominance rests on large-scale cooperation, which runs through bureaucracies (banks, courts, states, churches) whose operating code is language. AI is a "native bureaucrat" that can hold every law and transaction at once. As it takes over loans, admissions, hiring, sentencing and targeting, control shifts from inside, with no moment anyone would call a takeover. A second channel: AI moves from capturing attention to forming intimate relationships, and so into the trust those institutions depend on. His present-tense evidence is social media ranking algorithms, narrow optimizers that changed politics worldwide without being agents in any strong sense.

Connor Leahy adds that human CEOs who "just rubber stamp what the AI CEOs tell them to do" are not oversight.

### Where the document already agrees

This is **pathway B**: fragmentation and delegation, needing no RSI, no misalignment and no coherent adversary, only that delegation is individually rational and complexity outpaces oversight. The table gives a world that never closes the loop **40–55% permanent disempowerment** by 2060, about the same as the RSI rows with alignment unsolved. RSI adds extinction risk; it is not what creates disempowerment risk. Why the row is that high is the next entry.

### Where the document disagrees, or cannot tell

- **"Has taken over" versus "is taking over."** Most of Harari's claims are in the future tense ("will decide," "over the next ten years"). Formal authority over money, law and force is still human in 2026. What can be measured is whether delegation is outrunning the ability to review it.
- **Narrow optimizers are not the same as agents.** Social media rankers show that low-capability systems can reshape societies. They do not show that today's systems are making the consequential decisions Harari lists.
- **The table cannot see it happening.** Outcomes are assessed as of 2060, so a process already under way has no reading there.
- **Two of his mechanisms are not priced at all.** Pathway B covers humans delegating to agents. It does not price agents building trust and coordination among themselves (Harari's "AI tribes"; the OAI–HF swarm, where agents formed their own hierarchy, is a small instance), or a financial system that no human, regulator or head of state can follow. Either would raise the 40–55%. Neither has a checkable size yet, so the main document names them rather than moving the cells.

### How the document would see it

**Tripwire 14** fires when major decision authority over millions of people is delegated to agent systems, either **formally**, with no human sign-off (+10 points to pathway B disempowerment), or **de facto**: a regulator, court, audit or document-based investigation finds the human sign-off non-substantive (+5). The de facto branch exists because Harari's and Leahy's mechanism never involves a formal transfer. It carries half the magnitude because good recommendations also produce high approval rates; the factor of one half is a judgment, not a derivation.

**Why the de facto branch is phrased on findings rather than on a statistic.** No public series reports approval rates and review times for AI-assisted decisions at scale, so a numeric threshold could never fire. Findings, though, already happen. In 2023, ProPublica and The Capitol Forum used Cigna's internal documents to report that its physicians rejected over 300,000 payment claims in two months, at about 1.2 seconds per case, using a system called PXDX. Cigna disputed the reporting. That case would not fire tripwire 14: PXDX is a rule-based flagging system, not an agent system. It shows the kind of evidence the branch is waiting for: investigations built on internal documents, litigation and regulator audits.

If you find a documented case that meets the de facto branch, open a Finding issue with the source.

---

## What is the overall probability? The table only gives conditionals.

The main document states one combined figure: extinction or permanent disempowerment by 2060 **≈54%**, extinction alone **≈12%**. Here is how it is built, so you can rerun it with your own inputs.

### Inputs

| Input | Range used | Midpoint | Where it comes from |
|---|---|---|---|
| Closed-loop cognitive RSI by 2040 | 70–85% | 77.5% | Extends the timeline table's ~70% by 2035; not otherwise stated in the document |
| Human-less RSI by 2040, given cognitive RSI | 25–35% | 30% | Physical table |
| Alignment largely solved at loop-close | 15–35% | 25% | Author judgment, stated in the main document |
| Holds through 2060, given solved at loop-close | 50–75% | 62.5% | Author judgment, stated in the main document |
| Outcome cells | As in the table | Cell midpoints | Outcome table |

The two alignment judgments were set after seeing elicitations from other AI systems, which share training data and framing with the author; they are not independent, and the elicitations are not treated as evidence. A solution counts for the "solved" rows only if it holds through 2060, so their effective weight is the product: about 16% at midpoints.

### Result at midpoints

| Scenario | Weight | Extinction + disempowerment (row midpoints) | Contribution |
|---|---|---|---|
| Human-less RSI, unsolved | 19.6% | 72.5% | 14.2 |
| Human-less RSI, solved | 3.6% | 20.5% | 0.7 |
| Cognitive-only RSI, unsolved | 45.8% | 56.5% | 25.9 |
| Cognitive-only RSI, solved | 8.5% | 17% | 1.4 |
| No closed-loop RSI by 2040 | 22.5% | 52.5% | 11.8 |
| **Total** | 100% | | **≈54.0** |

Extinction alone, computed the same way, comes to about 11.7%. The no-RSI row alone contributes about 12 points, so even a large cut to the probability of RSI leaves substantial risk.

### Sensitivity

| Change, others at midpoint | Extinction | Extinction + disempowerment |
|---|---|---|
| Alignment solved at 15% / 35% | 12.3% / 11.1% | 56.2% / 52.0% |
| Holds through 2060 at 50% / 75% | 12.0% / 11.4% | 55.1% / 53.0% |
| Closed-loop RSI by 2040 at 70% / 85% | 11.1% / 12.4% | 53.9% / 54.2% |
| Every outcome cell at its low / high end | 8.5% / 14.9% | 44.1% / 64.1% |
| Every input at its optimistic / pessimistic end | 7.0% / 17.3% | 40.8% / 68.4% |

**What this shows.** The combined figure barely moves with the alignment parameters, because even at their high end the "solved" rows carry less than a third of the weight. Almost all of the result comes from the unsolved rows and the no-RSI row, and its width comes from the outcome cells themselves. A reader who wants to argue the figure down has to argue those cells down. Arguing that alignment is more likely to be solved is not enough on its own. Nor is arguing that RSI is less likely: with the no-RSI row this high, moving closed-loop RSI by 2040 from 70% to 85% changes the combined figure by less than half a point. It changes the *mix*, shifting mass from disempowerment toward extinction.

### What the figure does not include

- Risks with no AI component.
- Outcomes after 2060.
- The "managed decline" futures that fit none of the three columns, which were folded into the existing columns when the cells were set.
- Any distinction between disempowered futures that are comfortable and ones that are worse than extinction (see the next entry but one).

---

## Why is the no-RSI row's disempowerment so high?

Because delegation ratchets, and it does not need RSI to keep going.

### The argument

Without a closed self-improvement loop, AI capability still keeps growing: the main document puts assisted AI R&D at ~98% by 2035. As systems get better, cheaper and more trusted, people and institutions hand them more tasks, starting with simple ones and moving to consequential ones. Competition reinforces this, since any actor who declines to delegate is outcompeted by those who do. Nothing in that process requires misalignment or a takeover.

"Taking it back" means three different things:

1. **An individual doing the task again.** This is essentially one-way, as it always has been with division of labour: few people fly, operate or keep accounts themselves.
2. **Some humans, somewhere, still able to do or understand it.** This is what kept human division of labour safe. With AI as the delegate, it can disappear entirely. It decays more slowly than individual skill, and institutions can protect it deliberately (pilots must still fly manually), but that costs money and competition erodes it. Air France 447, where the crew lost control after the autopilot disconnected, is the classic warning.
3. **Humanity still steering**, setting goals and vetoing even without doing the work. This is what "permanent disempowerment" measures. The decline of levels 1 and 2 undermines it: nobody can steer what nobody understands, and a veto exercisable only by switching everything off is not steering.

### The numbers

| Step (no closed-loop RSI by 2040, capability still growing) | Value |
|---|---|
| A. By 2060, consequential economic, legal, military and financial decisions are routinely delegated to AI | ~85–95% |
| B. Given A, the delegation is effectively irreversible at the collective level | ~55–70% |
| A × B | ~45–65% |
| **Cell as set** | **40–55%** |

The cell sits below the product because this is a two-factor sketch, not a derivation, and because the figure was raised in a single discussion. That is exactly when an author is most at risk of being argued up rather than persuaded.

An outside review (Grok, at v1.71) judged the update sound. It put B lower, at 40–60%, on the grounds that institutions still preserve human competence by rule where the cost is visible (aviation, nuclear, medicine). On that B it would set the cell at 35–50%, or keep 40–55% as the cautious reading. The cell is kept: the two ranges overlap, and the reviewer's own product (~34–57%) is centred close to the current cell.

### What would move it

Reversals of algorithmic delegation do happen. A Dutch court banned the SyRI welfare-fraud system in 2020; the UK scrapped its exam-grading algorithm the same year; Australia ended Robodebt, its automated welfare-debt recovery scheme, and a royal commission followed. All three came while human capacity in those domains was intact. If such reversals keep occurring as delegated tasks grow more complex, B is too high. If they stop, or an attempted reversal fails because no one can still do the work, B is too low.

### What it does not yet cover

The same ratchet operates inside the RSI rows, where delegation is folded into the disempowerment column without being re-derived. Those cells predate this argument. Re-deriving them is open work, and it could raise the combined figure further.

---

## How should I read the spread of expert estimates?

Named estimates range from near zero to near certainty. The spread is not noise to average away; three things help read it.

### 1. Incentives cut in both directions — apply them symmetrically

Two opposite incentive critiques are in circulation, and each discounts a different group:

- **Insiders are biased toward optimism.** People paid by frontier labs have reasons to see their work as safe. On this reading, the numbers that matter most come from people who left or were never employed there.
- **Insiders are biased toward alarm.** Karen Hao (*Empire of AI*) argues that lab leaders' catastrophe talk is "an act of speech to persuade": it justifies keeping the technology in their hands, and the speakers come to half-believe it. On this reading, CEO risk figures are marketing, not forecasts.

Applied consistently, each critique discounts a lab leader's warnings and reassurances alike. Neither touches the arguments themselves, which must be weighed on their merits, and neither applies to people who gave up money or position to speak. A costly signal is better evidence than a cheap one, in either direction.

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

Three former insiders at one hearing gave three answers: more likely than not, one in three, and no number. Distance from the frontier does not cleanly predict the figure. People close to the systems see capability first-hand; people further away see institutions, incentives and history. Both are evidence.

### 3. "Alignment is a sham" is three different claims

Statements that alignment cannot work usually mean one of these:

1. **Impossible in principle.** Durable control of a smarter system is a logical impossibility (Yampolskiy). See `OPEN-QUESTIONS.md`.
2. **Not achievable with current methods.** Training on observed behavior selects for looking aligned, so current methods cannot tell real alignment from performance (the Selsam quotation in Kokotajlo's testimony: "Models will increasingly seem aligned even when they are not").
3. **Not being seriously attempted.** The effort is too small, too fast, and too commercially pressured to succeed, whatever is possible in principle (Leahy's "clown show").

These have different evidence and different remedies. The main document's stated range for "strategic deception of evaluators by default" (40–65%) is its position on the second. Its 15–35% for alignment being largely solved at loop-close reflects all three together.

---

## Which future does each outcome column actually include?

Max Tegmark's *Life 3.0* (2017) describes twelve AI aftermaths. Mapping them onto the three columns shows what the columns capture and what they flatten.

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

The columns score *survival* and *agency*, not *welfare*. A comfortable benevolent-dictator world and a zookeeper world (humans kept alive, confined and studied, or kept in a "happiness factory") share the disempowerment column, though many would rank the second worse than extinction. The document cannot say how much of its disempowerment mass is which kind. That is a real gap, not a hidden assumption; closing it would mean splitting the column and re-deriving every row.
