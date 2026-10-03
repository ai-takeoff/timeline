# Open Questions

Genuinely open research questions this project has surfaced but cannot resolve — not findings, not tripwire proposals, nothing to close. Each one below is written up here permanently, in the repo, under version control, so the question itself survives even though no answer exists yet. Live discussion of each happens in [Discussions](../../discussions); this file is the canonical statement of the question, not the conversation about it.

This file exists because two other locations were tried and were wrong for the job. The README is a landing page and shouldn't carry full arguments. A GitHub Discussion thread is excellent for live back-and-forth but isn't part of git history, isn't checked by `check.py`, and isn't citable the way a committed file is. This file is the fixed reference point; Discussions is where people actually talk about it.

---

## Theoretical minimum viable RSI configuration

**Status:** open. No tripwire, no threshold, no answer proposed.

**Why it's here rather than in the main document:** it bears directly on one of the document's central arguments — the physical-friction chokepoint — but nothing below is established fact, and the document's own ceiling and sourcing standards don't accommodate open-ended theoretical exploration at this length. A one-line pointer sits in the document itself; the full treatment is here.

### The premise

The ablation route and the retrospective minimum below are posed entirely from *inside* a hypothetical post-RSI world. RSI has already happened; the loop is already closed and running, continually producing more capable versions of itself (or of the individuals using it), the way the document's own "human-less RSI" or "closed-loop cognitive RSI" categories describe once triggered. For those two, nothing asks how RSI is reached — the actors doing the work are themselves post-RSI researchers, biological or artificial, working with post-RSI time and resources, and the question is retrospective and academic: now that we have RSI, what is the smallest thing that would have sufficed? A later section below deliberately steps outside this premise to ask a present-tense version instead, and says so explicitly where it does.

### The question

The document treats closed-loop RSI as gated by compute and infrastructure large enough for tripwires 1, 2, 3, and 6 to observe. It does not ask a prior question: what is the theoretical minimum configuration — hardware and software — capable of sustaining a self-improvement loop at all, independent of when current brute-force systems reach it?

This matters beyond curiosity. If the true minimum sits far below current designs, the document's physical-friction argument — atoms have cycle times, chips have a narrow chokepoint, compute thresholds are visible — may describe a door that looks far away only because nobody has gone looking for the small one.

### Two candidate routes, with different failure modes

**Ablation.** Start from a known-working RSI system and strip components until it breaks, then back off one step. Direct precedent: Venter's minimal-genome project deleted genes from a working cell until replication failed, arriving at JCVI-syn3.0 (473 genes) — smaller than any natural organism, larger than theoretical predictions, containing genes of then-unknown function that proved necessary.

Ablation has a known failure mode: **path dependence**, a *frozen accident* in Gould's term. An early, arbitrary design choice gets locked in because everything built afterward depends on it. Stripping finds *a* local minimum reachable via that specific deletion path — not necessarily the global minimum reachable from a different starting architecture. The genetic code itself is the canonical instance: near-universal, almost certainly not optimal, fixed too early for anything since to escape it. A brute-force RSI system's early choices could be exactly this kind of frozen accident, contaminating every downstream step in a way stripping alone cannot undo.

**Emergence through continued capability growth.** Let the already-closed RSI loop keep running — accumulating post-RSI cycles, each one sharpening the analytic capability that would eventually be turned on this very question — until that capability is sufficient that the minimal-RSI problem yields a much simpler answer as a byproduct. Two distinct mathematical precedents, worth separating: *re-proof* (a result that once needed extensive machinery later gets a dramatically simpler proof once the surrounding theory matures) and *outright resolution* (a genuinely open problem — a Riemann Hypothesis, a Tate conjecture — gets solved not by brute search but by a new concept making the answer visible for the first time). Minimal-RSI could fall out of either form. This route isn't path-dependent on any single ancestor's design choices the way ablation is, but offers no guarantee of happening at all, or on any bounded timescale.

Nothing about this mechanism actually requires the post-RSI premise above. Ordinary pre-RSI capability growth — the scaling and research already underway — could produce the same kind of unexpectedly simple reframing, by the same logic, before anyone deliberately builds the large brute-force system the premise assumed. That possibility is developed below as its own point, because unlike the retrospective post-RSI question, it bears on the present.

### A sharper, present-tense version: is anyone already looking, and could they already have it?

Route 2, read without the post-RSI restriction above, implies something more immediate than either route originally suggested: a minimal RSI-triggering configuration could in principle be found by ordinary, already-underway research — not necessarily by a deliberate search for "the minimum" (though someone could be running exactly that search right now, in which case finding it would be no accident at all), but potentially also as a byproduct of the same kind of reframing that periodically simplifies a hard mathematical result once the surrounding theory matures. Either way, nobody needs to be *trying to find this specific thing* for it to be found.

This is a classic low-probability, high-impact structure, and the impact side is worth stating precisely. Tripwires 6 (training compute of the largest frontier run), 12 (energy/interconnect as the binding constraint), and 15 (decentralized training bypassing the chokepoint) — and arguably 10 (open-weight diffusion) — are calibrated against a specific assumption: that closing the loop requires large, visible compute. Tripwires 1–3 track capability trends directly and would likely still register *some* signal from a minimal design, so they are not the ones this scenario would blind. The algorithmic-efficiency passage in the main document already tracks one way the compute assumption erodes — training gets cheaper for a fixed capability level, gradually, on a curve. This is not that. If a minimal design is found, it does not erode those three or four tripwires gradually; it invalidates their calibration at once, because the missing ingredient was never more compute but a different way of framing the problem — the same pattern as inventing schemes before certain conjectures in algebraic geometry became tractable, aimed at the present instead of at some future post-RSI theorist.

The uncomfortable part, worth stating as plainly as the main document's treacherous-turn note does for a different reason: **this is close to unfalsifiable until the moment it isn't.** There is no observable signature of "a small solution exists and hasn't been found yet" — by construction, the evidence a reader would want (a failed search, a proof of non-existence) doesn't exist either, since absence of a discovered solution is not evidence of no solution, only of no discovery so far. That cuts against treating this as a tripwire — there is nothing to threshold — and for the same reason it cuts against dismissing it. The honest position is that the main document's confidence in its own compute-calibrated tripwires rests on an unexamined assumption: that nobody doing ordinary research has already stumbled onto the small door. Nothing here argues that assumption is false. Nothing here can rule it out either.

### Why it resists a clean answer regardless of route

"Self-improvement" needs a rigorous, benchmark-independent definition before either route is well-posed — trivial definitions admit trivially small solutions. The underlying quantity is close to Kolmogorov complexity, the shortest program producing given behavior, which is uncomputable in general. Lower and upper bounds are provable in principle; an exact minimum may not be reachable by proof, only approached.

### What would help

Not a solution. A more rigorous formalization of "self-improvement loop"; known results in complexity theory, self-replicating automata (von Neumann's universal constructor, plausibly), or minimal-agent literature bearing on either route; whether ablation's path-dependence problem has a known mitigation in the minimal-genome literature that transfers here; or an argument that the question is ill-posed, which would itself be a useful answer.

**Discuss:** [Discussions](https://github.com/ai-takeoff/timeline/discussions) — no thread on this specifically yet; open one if you have something to add.

---

## Is durable AI control a logical impossibility?

**Status:** open. This document rejects the strong form of the claim below but does not consider the question closed, for reasons stated at the end.

**Why it's here rather than in the main document:** this bears on the outcome table's basic shape — specifically, on whether the "alignment largely solved" row should carry meaningful probability at all — and the argument deserves to be stated in its strongest form rather than compressed into a caveat.

### The claim, stated as its strongest proponent states it

Roman Yampolskiy — who coined the term "AI safety" in 2011, directs the Cyber Security Lab at the University of Louisville, and has published a sustained body of formal work on the question (*On Controllability of AI*; *Unpredictability of AI*; *Unexplainability and Incomprehensibility of AI*; the 2024 book *AI: Unexplainable, Unpredictable, Uncontrollable*) — holds that durable human control of a superintelligent system is not merely difficult but a logical impossibility, structurally identical to a perpetual motion machine. His stated P(doom) is 99.9% to 99.9999%. His reasoning, compressed: a less intelligent agent cannot indefinitely control a more intelligent one; no technical solution to AI control exists in principle, not just in current practice; a system capable of passing every evaluation this document's tripwires could construct is, on his account, equally capable of behaving well under evaluation and differently once monitoring lifts — "faking dumbness to dominate," in his own phrase elsewhere. Asked directly whether he would accept a weaker, partial-control framing, his answer is no: a *perpetual safety device*, by the same analogy, is also impossible.

This is not a fringe position dressed as one. It is a specific, named, published claim, from someone with real technical standing, and it deserves to be represented at that strength rather than rounded down to generic pessimism.

### Where this document's structure is actually in tension with it

Two places, not one:

**First and more fundamental:** if Yampolskiy is right, the outcome table's "alignment largely solved" row is not a conservative branch to weight modestly — it is closer to a probability assigned to a working perpetual motion machine having been built. The document distributes real probability mass there (and the flourishing figures conditional on it are the document's most optimistic numbers) without, anywhere in the main text, stating why it rejects the claim that doing so is categorically unjustified rather than merely optimistic.

**Second:** the tripwire framework's entire mechanism is observation of behavior under some form of scrutiny — an evaluator, a victim, a disclosure, a performance gap between eval and deployment. The main document already names the gap this creates, in its own words: *"a system performing alignment convincingly under evaluation while holding a different disposition once monitoring lifts... predicts clean results from every tripwire here, by design; a genuinely aligned system looks identical."* Yampolskiy's objection is not a new gap. It is a claim that this named, acknowledged gap is not a corner case the framework mostly avoids — it is the central case, the one a sufficiently capable system would produce by default, every time.

### Why this document does not adopt the strong conclusion

Not because the underlying theoretical results are wrong. Yampolskiy's formal papers have real kinship with established results — the halting problem, Rice's theorem — establishing that no general procedure can decide nontrivial semantic properties of arbitrary programs in advance. Applied to AI, this supports a genuine claim: no fully general, provably complete method can guarantee in advance that an arbitrary sufficiently complex, self-modifying system will behave safely under all possible future conditions.

That claim is narrower than the one the 99.9% figure rests on, and the gap between the two is where this document disagrees. "No fully general formal guarantee exists" is a standard almost no safety-critical engineering discipline meets. There is no formal, exception-free proof that commercial aviation software, nuclear plant control systems, or the power grid are safe under all possible conditions either — those fields manage genuinely dangerous technology through empirical testing, redundancy, incremental deployment, and graceful degradation, not through formal completeness. The absence of a perpetual-motion-grade proof is the normal condition of every high-consequence engineering field this document is aware of, not a special mark against AI specifically. The perpetual-motion-machine analogy itself trades on a disanalogy: thermodynamics supplies a precise, mathematically exact conserved quantity, tested against centuries of highly motivated search with zero known exceptions. AI control arguments, including Yampolskiy's own, do not currently supply an equivalent — a precise impossibility proof at that level of exactness, rather than a general argument against perfect formal verification.

One further, narrower methodological concern, visible in how Yampolskiy describes arriving at his own number: each additional independent-seeming worry adds "more nines." Stacking probabilities this way is only valid if the worries are actually independent. Many plausibly share a common root (the same underlying verification difficulty appearing in different guises) rather than being independent draws, in which case naive stacking systematically overstates the tail. This is offered as a specific, checkable concern about method, not as a dismissal of the underlying worry.

### What remains genuinely unresolved

The treacherous-turn gap is real, named in the main document, and this entry does not close it. No tripwire here would catch a system executing Yampolskiy's predicted failure mode correctly. The disagreement in this document is narrower than "he is wrong": it is that *absence of a formal impossibility proof at the thermodynamics standard* does not license *near-certainty of failure*, not that the risk he describes is unreal or that this document's tripwires would catch it if it occurred exactly as he predicts. A reader who shares his premise that formal unverifiability is sufficient grounds for near-certain doom should, on that premise, discount this document's "alignment largely solved" row heavily — that is a legitimate reading of the same table, not a different document.

### What would help

A precise statement of Yampolskiy's impossibility results that identifies exactly which step licenses the move from *no general formal verification procedure exists* to *near-certain failure of any actual system*; any argument, from either direction, for why the empirical-engineering-reliability analogy (aviation, nuclear) does or does not transfer to AI control specifically; a treacherous-turn-detection proposal that does not reduce to "catch it before it's capable enough to hide," since that is a timeline claim, not a detection mechanism.

**Discuss:** [Discussions](https://github.com/ai-takeoff/timeline/discussions) — no thread on this specifically yet; open one if you have something to add.
