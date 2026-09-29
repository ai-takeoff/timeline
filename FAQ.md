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
