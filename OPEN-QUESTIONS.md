# Open Questions

Research questions this project raises but cannot resolve. These are not findings or tripwire proposals, and none has a proposed answer. This file is the fixed, citable statement of each question; live discussion belongs in [Discussions](../../discussions).

---

## Theoretical minimum viable RSI configuration

**Status:** open. No tripwire, no threshold, no answer proposed.

### The question

The main document treats closed-loop RSI as gated by compute and infrastructure large enough for tripwires 1, 2, 3 and 6 to observe. It does not ask a prior question: what is the smallest configuration, in hardware and software, that could sustain a self-improvement loop at all?

If the true minimum sits far below current designs, the physical-friction argument (atoms have cycle times, the chip chokepoint is narrow, compute thresholds are visible) may describe a door that only looks far away because nobody has looked for a small one.

### Two routes, with different failure modes

**Ablation.** Start from a working RSI system and strip components until it breaks, then back off one step. The precedent is Venter's minimal-genome project, which deleted genes from a working cell until replication failed. It arrived at JCVI-syn3.0 (473 genes): smaller than any natural organism, larger than theory predicted, and including necessary genes of then-unknown function.

The known failure mode is **path dependence** (a "frozen accident," in Gould's term). An early, arbitrary design choice gets locked in because everything after it depends on it, so stripping finds *a* local minimum, not necessarily the global one. The genetic code is the canonical case: near-universal, almost certainly not optimal, fixed too early to escape.

**Reframing through capability growth.** A small design could instead fall out of capability growth as a byproduct, the way mathematics sometimes simplifies. A result that needed heavy machinery gets a short proof once the surrounding theory matures, or an open problem yields to a new concept rather than to search. This route is not path-dependent, but it offers no guarantee of happening at all, or on any timescale.

### The present-tense version: could someone already have it?

Asked after the fact, from a world where RSI already exists, this question is academic. Asked now, it is not. Ordinary research already under way could find a minimal configuration, either by deliberately searching for one or as a byproduct of a reframing, before anyone builds the large system the compute-based tripwires expect.

The impact would be concentrated. Tripwires 6 (largest training run), 12 (energy and interconnect) and 15 (decentralized training), and arguably 10 (open-weight diffusion), are calibrated on the assumption that closing the loop needs large, visible compute. Tripwires 1–3 track capability directly and would likely still register something. The main document already tracks gradual algorithmic efficiency, which makes training cheaper along a curve. This is different: a minimal design would invalidate those calibrations at once, because the missing ingredient was never more compute.

**This is close to unfalsifiable until the moment it isn't.** "A small solution exists and has not been found" has no observable signature, and the absence of a discovery is not evidence that there is nothing to discover. That argues against making it a tripwire, since there is nothing to threshold, and equally against dismissing it. The compute-calibrated tripwires rest on an unexamined assumption that nobody has already stumbled onto the small door. Nothing here shows that assumption is false, and nothing here can rule it out.

### Why it resists a clean answer

"Self-improvement" needs a rigorous, benchmark-independent definition first, since trivial definitions admit trivially small solutions. The underlying quantity is close to Kolmogorov complexity, the length of the shortest program producing a given behavior, which is uncomputable in general. Bounds can be proved; an exact minimum may only be approached.

### What would help

A rigorous formalization of "self-improvement loop"; results from complexity theory, self-replicating automata (von Neumann's universal constructor) or minimal-agent work bearing on either route; a known mitigation for path dependence in the minimal-genome literature; or an argument that the question is ill-posed, which would itself be useful.

---

## Is durable AI control a logical impossibility?

**Status:** open. The main document rejects the strong form of this claim but does not consider the question closed.

**Why it is here:** it bears on whether the "alignment largely solved" rows should carry meaningful probability at all, and deserves its strongest form rather than a caveat.

### The claim

Roman Yampolskiy directs the Cyber Security Lab at the University of Louisville and describes himself as having coined the term "AI safety" (his bios give 2010 and 2011). He has written at length on the question, mostly informal argument with some borrowed formal results: *On Controllability of AI*; *Unpredictability of AI*; *Unexplainability and Incomprehensibility of AI*; and the 2024 book *AI: Unexplainable, Unpredictable, Uncontrollable*. He holds that durable human control of a superintelligent system is not merely difficult but logically impossible.

His own stated figure is "I am at 99.999999%" (post on X, 12 March 2024). In interviews he frames the number as an impossibility claim more than a measured probability. In one, 99.9% is the interviewer's figure, and he answers through the impossibility framing rather than repeating it. In the Lex Fridman interview, "99.9" is his ceiling on formal-verification confidence, not an extinction probability. On timing he draws his own distinction: "yes, we all probably will die, but 80 years is not 2 years."

In his words, from Lex Fridman Podcast #431: controlling superintelligence "is like a problem of creating a perpetual safety machine. By analogy with perpetual motion machine, it's impossible." Systems "keep improving, learning, eventually self-modifying, interacting with the environment, interacting with malevolent actors." A cybersecurity breach gets "a new password"; this gets no second chance: "what are the chances that we'll create the most complex software ever on the first try with zero bugs and it'll continue to have zero bugs for a hundred years or more." In a separate interview, building general superintelligence means "we won't be able to control it," making the outcome "basically guaranteed" negative, because control would need "a perpetual safety device."

Four elements run through both:

1. The system keeps changing, so each version must be re-secured.
2. The horizon is indefinite.
3. Something, the system or an adversary, actively optimizes against the safeguards.
4. A single failure is not recoverable.

He also argues, in *On Controllability of AI*, that each kind of control fails in its own way. Literal obedience does not track intent. A system that decides on humanity's behalf, however well, is no longer under human control. Partial control fares no better: any achieved level of safety degrades as the system keeps changing.

### Where the main document is in tension with it

1. If he is right, the "alignment largely solved" rows assign probability to something like a working perpetual motion machine.
2. The tripwires observe behavior under scrutiny. The main document already names the gap this creates: a system performing alignment under evaluation while holding a different disposition "predicts clean results from every tripwire here, by design." His objection makes that gap the default case rather than a corner case.

### Why the main document does not adopt the strong conclusion

**Rice's theorem blocks deciding a property for *all* programs. It does not block building one specific program and proving it has that property.** Verified systems exist: seL4, a formally verified microkernel, and CompCert, a formally verified C compiler.

His objection is sharper than the general claim this answers, and seL4 does not settle it. He makes three further moves:

1. **Verifier regress.** Confirming the next system's safety needs an already-proven-safe verifier at least as capable.
2. **Residual error under volume.** Verification confidence of "99.9... but we never get to 100 percent" is not enough for a system making a billion decisions a second for a century.
3. **Design does not scale.** Asked whether building AI by design rather than by evolution could avoid the problem, he grants the path exists in principle. He rejects it on empirical grounds: it was tried for the field's first fifty years, and it does not produce competitive capability.

So the defensible position is narrower than either side's strongest framing. Impossibility in general does not entail impossibility for a specific, well-built system. But frontier models are trained, not built to a verification spec, which puts them nearer Rice's "arbitrary program" than seL4. His claim is that this gap is the reason capable systems and provable ones have not been the same systems, not an oversight the next build can fix.

Aviation and nuclear safety are a weaker analogy, because they fail on all four of his elements:

1. Their software is fixed and certified version by version.
2. Physics does not optimize against an interlock.
3. Those fields learned from *survivable* failures.
4. Testing happens in the regime of operation.

The analogy shows only that formal completeness is not the normal bar for safety-critical fields.

**The real crux is empirical: how likely is it that a capable system strategically deceives its evaluators by default, rather than as a rare failure?** His figure requires that probability to be close to certain. The main document now states its own judgment, 40–65% for frontier systems built by current methods. That is far from certain, but it is not grounded in anything a tripwire can check.

**The "more nines" method cuts both ways.** "Every time I meet an independent concern, I have to add more nines to my estimate, as if I wasn't already close to one." He also calls the effect fractal: "the more you zoom in, the more problems you see." Stacking probabilities multiplicatively is valid only if the worries are independent. If they share a root, stacking overstates the tail, and the probability collapses to the root's own, which may itself be near-certain. So the critique relocates the disagreement rather than resolving it. It also applies to his strongest quantitative argument. Per-iteration survival *p^N* goes to zero only if each iteration is an independent roll. If safety persists once achieved, long-run survival could sit far above *p^N*. Applied consistently, the tool favors neither conclusion.

### What this means for the estimates

1. **"Alignment largely solved" means the agency-preserving sense.** A value-aligned system that does not defer to human judgment meets the disempowerment definition, however good the outcome. A reader who takes "solved" to mean good outcomes, deference or not, should read the solved rows' flourishing figures as overstated.
2. **The largest lever cannot be observed.** Solving alignment moves disempowerment about 31 points, and no tripwire separates real from deceptive alignment. The main document states the parameter anyway, 15–35% at loop-close, as an author judgment no tripwire can revise.
3. **Persistence is now explicit, within a bounded window.** The "solved" rows require alignment largely solved at loop-close *and* holding through 2060 (stated at 50–75%). Solved-then-lost counts as unsolved. Indefinite persistence beyond 2060, the claim his argument targets most directly, is outside the table's horizon by design. That is a stated limit, not a rebuttal. The combined figure in `FAQ.md` moves only a few points when these two parameters are pushed toward his view, because the unsolved rows already carry most of the weight.

No specific cell has a demonstrated case for being miscalibrated.

### What remains unresolved

The treacherous-turn gap is real, and nothing here closes it: no tripwire would catch a system executing his predicted failure correctly. The disagreement is narrow. The absence of a thermodynamics-grade impossibility proof does not license near-certainty of failure. But current frontier models are not built the way verified systems are, and nobody knows how likely deception by default is. A reader who takes formal unverifiability as sufficient grounds for near-certain doom should discount the "solved" rows heavily. That is a legitimate reading of the same table.

### What would help

- Evidence on the crux, from either direction: how often capable systems deceive evaluators by default.
- A response to his claim that design-based AI does not scale to competitive capability, the point the rebuttal above most needs to survive.
- An argument that the stated 50–75% for alignment holding through 2060 is wrong, in either direction.

**Discuss:** [Discussions](https://github.com/ai-takeoff/timeline/discussions). No thread on this yet; open one if you have something to add.
