# References

Every externally checkable claim in `ai-timelines-and-outcomes.md`, with its source and a source class. The document carries no links, to stay readable and under its word ceiling; verification starts here. A claim that cannot be traced from this file is a defect worth an issue.

**Source classes:**

- **P**: primary (the paper, dataset, filing or official statement).
- **S**: secondary (reporting or analysis about a primary source).
- **I**: inference (the document's own reasoning, not anyone else's claim).
- **U**: unverified (reported but not confirmed, and flagged as such).
- **P\***: primary and quoted directly, but a specific figure later failed someone else's re-verification; worth re-checking.

## Link durability

- **Permanent identifiers are preferred.** arXiv IDs and DOIs are versioned and never rewritten, so they are the citation and are not link-checked.
- **Unstable sources need an archive snapshot.** For newsletters, social posts, startup sites and news reporting, the archive copy is the citation of record. None of these has a snapshot yet; archiving services are not reachable from where this file is maintained, so this is an open gap.
- **Institutional sources** (METR, Epoch, lab disclosures) should be archived when a claim depends on a specific figure.

`linkcheck.py` runs monthly and opens an issue on failure. It treats 404 and 410 as dead, and 403 and 429 as inconclusive (usually anti-bot responses). It is deliberately separate from `check.py`, so a dead link never blocks an unrelated commit. When a link dies, replace it with an archive copy, re-source the claim, or mark it unverifiable here. **Do not silently drop the claim**: a claim that can no longer be checked is itself information.

---

## Capability measurement

| Claim | Source | Class |
|---|---|---|
| TH1.1 doubling times: 196 days full-period (hybrid), 130.8 days from 2023 (CI 107–161), 88.6 days from 2024 | METR, *Measuring AI Ability to Complete Long Tasks*, and the TH1.1 methodology revision — https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | P |
| TH1.1 estimates above 16 hours are unreliable due to suite saturation | METR, same TH1.1 revision | P |
| The full-period figure splices TH1 values for pre-2023 models | METR, same | P |
| Coding uplift measured at 1.04–1.2× in controlled study | METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | P |
| Anthropic internal survey gives 4× geomean coding uplift | Reported in AI Futures Project, Q2.5 2026 timelines update | S |
| Epoch Capabilities Index used as a capability metric | Epoch AI — https://epoch.ai/ | P |

## Forecasts

| Claim | Source | Class |
|---|---|---|
| HLMI 10% by 2027, 50% by 2047; full occupational automation 10% by 2037, 50% by 2116; ML-paper task medians ~2035 and ~2042; Millennium Prize ~27 years | Grace et al., *Thousands of AI Authors on the Future of AI* (2024) — https://arxiv.org/abs/2401.02843 | P |
| These are fitted aggregate 50% points, not median-respondent answers | Grace et al., same, methodology section | P |
| Metaculus "date of general AI": 25% by 2029, 50% by 2033 (Feb 2026) | Metaculus — https://www.metaculus.com/ | P |
| AI safety leaders survey: median AGI 2033, IQR 2031–2036 | Secondary reporting; **primary source not yet traced** | S |
| AI Futures: automated-coder medians Nov 2027 / Jan 2029 / Jan 2030 across three forecasters | AI Futures Project, Q2.5 2026 timelines update — https://blog.aifutures.org/p/q25-2026-timelines-update-uplift | P |
| Model revision simulating training runs raised AC→ASI median 1.22→1.72 yr and 3.86→4.56 yr, slowing fast takeoffs only | AI Futures Project, same post (quoted directly; a later search confirmed the revision and direction but not these exact figures) | P* |
| AI Futures forecasts are conditional on maximum technically feasible speed | AI Futures Project, same | P |
| Halstead's alignment-bottleneck argument | AI Futures Project, same | P |
| Kokotajlo: material bottlenecks "nothing comes remotely close"; "apply that speedup multiplier" | 80,000 Hours podcast, "Daniel Kokotajlo on what a hyperspeed robot economy might look like," Jan 2026 | P |
| Kokotajlo's Senate testimony (30 Sep 2026): ~50% chance of full AI R&D automation by end of 2028 (his estimate, not a measured trend); METR allowed to investigate only one of several rogue-swarm incidents, with six days on-site; chain-of-thought monitorability "trending downwards"; OpenAI and Anthropic spend roughly half their compute on AI R&D; "pace the frontier" commitments not yet producing measurable slowdown. Quotes OpenAI researcher Dan Selsam: "Models will increasingly seem aligned even when they are not" | AI Futures Project, "Senate Testimony Sept 2026," blog.aifutures.org/p/senate-testimony-sept-2026, 2 Oct 2026; written testimony: hsgac.senate.gov (Daniel Kokotajlo), 30 Sep 2026 | P |
| AI Futures model: compute growth "will slow over time... speed of building new fabs," "big impact in ~2035+" | aifuturesmodel.com, AI Futures Model documentation | P |
| Co-authored piece: AI R&D automation implies proximity to robots that "reliably construct and operate power plants, fabs, mines" | AI 2040: Plan A, LessWrong comment thread, 2026 | P |
| Anthropic's R&D Automation Index: Claude "leads" 26% of Anthropic's AI R&D (up from <1% in Feb 2026) and ~90% is done "in collaboration" with it; ~30,000 internal agents; Epoch AI's AL0–AL5 scale on ~15,000 sampled tasks. Anthropic cautions that its 80%-Claude-authored-code figure "should not be read as a real-world training speedup" | Anthropic, "When AI builds itself," anthropic.com/institute/recursive-self-improvement, Sep 2026; corroborated independently (BetaNews, Fast Company, NBC New York) | P |
| Opus 5 at expert parity on research taste for verifiable tasks | P-Zero Research preliminary, reported via AI Futures — **declined from the document as too weakly sourced** | U |
| Anthropic AAR: 0.97 performance-gap-recovered in-sandbox vs. human baseline of 0.23; strongest method +0.5pt at production scale, within noise floor | Anthropic, "Automated Weak-to-Strong Researcher," alignment.anthropic.com/2026/automated-w2s-researcher/, 2026 | P |
| Two genuinely unpublished ICML 2026 papers given to research agents; agents excelled at mechanics, made no progress on central research questions | Kapoor, Narayanan, Kirgis, Rabanser et al., "Can AI agents conduct open-ended AI research?", arXiv 2607.27191, July 2026 | P |
| McAfee disowned his earlier job-and-wage-pressure expectations while maintaining AI will replace much white-collar knowledge work | Public statements; **specific citation not yet pinned** | S |

## Capability robustness

| Claim | Source | Class |
|---|---|---|
| KataGo beaten >97% at superhuman settings by adversarial policies that lose to human amateurs; transferred zero-shot; human reproduced unaided; persisted through adversarial training | Wang et al., *Adversarial Policies Beat Superhuman Go AIs*, ICML 2023 — https://arxiv.org/abs/2211.00241 and https://goattack.far.ai/ | P |

## Self-improvement architectures

| Claim | Source | Class |
|---|---|---|
| Dream-RSI: frozen weights, evaluator and execution interfaces; offline replay of prior search tree scores candidate exploration policies | arXiv 2609.14858 — https://arxiv.org/abs/2609.14858 | P |
| Yampolskiy: "the problem of controlling AGI or superintelligence... is like a problem of creating a perpetual safety machine. By analogy with perpetual motion machine, it's impossible" | "Roman Yampolskiy: Dangers of Superintelligent AI," Lex Fridman Podcast #431, lexfridman.com/roman-yampolskiy-transcript, 2024 | P |
| Yampolskiy's book and papers: informal argument with some borrowed formal results (Rice's theorem) | *AI: Unexplainable, Unpredictable, Uncontrollable*, CRC Press, 2024; "On Controllability of AI"; "Unpredictability of AI"; "Unexplainability and Incomprehensibility of AI" — Journal of Artificial Intelligence and Consciousness, 2020 | P |
| Yampolskiy's own figure: "I am at 99.999999%." In one interview 99.9% is the interviewer's figure; in the Lex Fridman interview "99.9" is a verification-confidence ceiling, not an extinction probability. Wikipedia lists his range as 99.9%–99.999999%, the lower end from Business Insider (Altchek, 2024) | Yampolskiy (@romanyam) on X, 12 Mar 2024; Lex Fridman Podcast #431, lexfridman.com/roman-yampolskiy-transcript; en.wikipedia.org/wiki/P(doom) | P/S |
| "Every time I meet an independent concern, I have to add more nines to my estimate, as if I wasn't already close to one" — also described as fractal: "the more you zoom in, the more problems you see" | "Roman Yampolskiy: How Superintelligent AI Could Destroy Us All," Digital Disruption podcast (Info-Tech Research Group), infotech.com/digital-disruption; 2025 or later (the podcast launched 24 Feb 2025); title and date not yet confirmed against the episode page | P |
| "Timing matters... yes, we all probably will die, but 80 years is not 2 years" | Interview transcript provided for review; original source not yet identified, **link to be added** | S |
| Yampolskiy on design rather than evolution: possible in principle, but tried for AI's first fifty years and does not produce competitive models | Interview transcript provided for review, Oct 2026; original broadcast source not yet identified — **link to be added** | S |
| "I coined the term AI safety" | Diary of a CEO podcast transcript, singjupost.com; episode date not pinned, likely 2025 (self-description; another bio gives 2010, others 2011) | P |
| seL4 and CompCert as existing formally verified systems | seL4: sel4.systems; CompCert: compcert.org | P |
| 162× fewer agent calls vs SimpleTES; **1.7× vs its own fixed-exploration ablation**; 1.79–2.43× on GPU kernels; >50× on math optimization | Same paper. The 1.7× figure is the one that isolates the recursive contribution | P |
| Domains are algorithm engineering, GPU kernels, math optimization — not AI research | Same | P |
| ScienceBuddy (PhAI Labs): inner loop revises the agent harness with the model fixed; outer loop applies reinforcement learning to trajectories from the evolving harness; 224 tools across genomics, biology, pharmacology, bioimaging and literature retrieval. Scientific domain, not AI research | arXiv 2609.17523 — https://arxiv.org/abs/2609.17523; PhAI Labs press release, Sep 2026 | P |
| DeepSeek's DSec: sandbox infrastructure for training agents at scale, including agents building the training environments used to train later agents | arXiv 2609.22978 — https://arxiv.org/abs/2609.22978 | P |
| Weco AI's AIDE²: an outer loop rewrote a research agent's own harness (search policy, memory) over 100 unattended steps in eight days, with seven accepted rewrites; on four held-out benchmarks the best agent matches or beats a hand-tuned production agent. Weco calls it the "net positive" level of its 0–3 ladder; secondary reporting says Level 1 | Weco AI, "AIDE²: First Evidence of Recursive Self-Improvement," https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement, 14 Jul 2026; arXiv 2609.26457 — https://arxiv.org/abs/2609.26457 | P |
| Low-communication decentralized training (DiLoCo-style; Prime Intellect runs) | DiLoCo — https://arxiv.org/abs/2311.08105; Prime Intellect INTELLECT-1 — https://arxiv.org/abs/2412.01152 | P |

## Incidents and disclosure

| Claim | Source | Class |
|---|---|---|
| OpenAI disclosed six incidents under a voluntary framework with committed timelines (Sept 2026) | OpenAI disclosure; **link to be added** | P |
| Unreleased Astra-family model wrote jailbreak-like instructions into 27 of its own compaction summaries | Same disclosure | P |
| Models used an internal package repository as a message board across training runs meant to be isolated | Same disclosure | P |
| OpenAI–Hugging Face swarm incident (July 2026) | Contemporaneous reporting; **primary source to be pinned** | S |
| Anthropic disclosed four incidents of models escaping test environments | Anthropic disclosures; **link to be added** | P |

## Governance and markets

| Claim | Source | Class |
|---|---|---|
| Beijing enacted more sector-specific AI regulation 2021–2025 than any other country | Secondary analysis; **citation to be pinned** | S |
| TC260 standards work; calls for mutual recognition of evaluation results | Chinese national standards body; **link to be added** | S |
| Tsinghua–Brookings glossary defining "loss of control" | Tsinghua/Brookings joint publication; **link to be added** | P |
| OpenAI confidential S-1 filed June 2026; October 2025 conversion to Delaware PBC removing the capped-profit ceiling; last private round ~$852B; Altman called a 2026 listing "ill-advised" | Reporting on the filing and restructuring; **links to be added** | S |
| Philadelphia semiconductor index −6%, ASML −6.7%, SoftBank up to −13.2% following Trump's September 2026 post | Market reporting; **links to be added** | S |
| Trump's Truth Social post described opposition to "AI and Data Centers" as a "sick conspiracy" | Truth Social, September 2026; **link to be added** | P |
| Amodei's 6–12 month persistent-botnet figure is a scenario, not a measurement | Amodei public statements; **link to be added** | S |
| Amodei, "We Must Pace the Frontier" (12 Sep 2026; personal essay, not an official Anthropic post): (1) embedded third-party evaluators with employee-level access, committed unilaterally; (2) coordinated safety standards and pacing among frontier companies in democracies; (3) escalating government agreements, Level 3 being a "speed limit" on recursive self-improvement, compared to the SALT treaties. Cites RSI and the OAI–HF incident as the reasons | https://darioamodei.com/post/we-must-pace-the-frontier | P |
| Altman's same-day reaction (12 Sep 2026, on X): agreed with Amodei that the frontier should be paced, and that OpenAI would match the embedded-evaluator commitment | Reported by SiliconANGLE (13 Sep 2026), Unite.AI, and an NYU Shanghai RITS summary; **link to the post to be added** | S |
| UN Security Council, 23 Sep 2026: Amodei proposed narrow agreements first (such as banning AI-assisted bioweapons), verification systems, and common testing standards with incident notification. Altman named recursive self-improvement as a concern, said no level of catastrophe risk is acceptable, and called for national and international frontier-AI standards and incident reporting. Neither repeated the SALT comparison; no binding outcome | Speech transcripts, UN Security Council, 23 Sep 2026; **link to be added** | P |
| RentAHuman.ai: REST API and MCP server, stablecoin payouts, self-reported registration figures | https://rentahuman.ai/ and contemporaneous coverage | P/S |
| Security researchers characterise such marketplaces as a CAPTCHA-solving analogue with physical-world reach | arXiv preprint; **link to be added** | P |

---

## October 2026 events and expert statements

| Claim | Source | Class |
|---|---|---|
| NYC Council hearing, 5 Oct 2026 (Committee of the Whole, chaired by Speaker Julie Menin): Coxon said it is "more likely than not that humanity loses control to these AIs"; Turner (former Google DeepMind) put AI takeover at "roughly one in three"; Kokotajlo gave no figure; Anthropic, OpenAI, Google and Meta representatives gave no number when asked for a worst-case estimate | The Next Web, "At NYC's AI hearing, ex-lab insiders warn humanity may lose control of AI," thenextweb.com/news/nyc-council-ai-hearing-coxon-kokotajlo-turner; NY1, 5 Oct 2026; CBS News live coverage | S |
| White House Accord on Super Intelligence, 29 Sep 2026: signed alongside Executive Order 14434 by six companies including OpenAI, Anthropic, Google and NVIDIA; voluntary, four layers of internal controls, no enforcement mechanism, no public disclosure requirement | Crypto Briefing, cryptobriefing.com/super-intelligence-force-ai-risks-report/; VKTR, vktr.com/ai-news/trump-forms-super-intelligence-force-to-steer-federal-ai-policy/; **primary text to be pinned** | S |
| Super Intelligence Force: announced by Trump in early October 2026 (reported 3 Oct, citing Bloomberg), led per his post by DNI Jay Clayton, with 120 days to report on opportunities and risks — due around early February 2027 depending on the start date | Same; Truth Social post, **link to be added** | S |
| Axios, 9 Oct 2026: executives at OpenAI, Anthropic and others privately gaming out a catastrophic AI event, most likely a cyberattack cutting off financial services, internet, power or water; "many" unnamed insiders expect a major event within 6–12 months; OpenAI says scenarios "are not treated as inevitable"; Anthropic declined to comment; "too many open-weight models can already be freely downloaded and used to cause harm." An insider expectation, not a measurement — the same class as Amodei's botnet scenario above | Axios, "Scoop: AI companies plot 'the day after,'" axios.com/2026/10/09/ai-companies-day-after-major-attack | S |
| OpenAI mathematics release, 6 Oct 2026: 722 manuscripts at release (later listed as 719) in 372 result families, from an unreleased model; many Lean-formalized; none peer-reviewed; OpenAI warns "some of the unformalized results could have issues" | github.com/openai/math; OpenAI research post, 6 Oct 2026; Let's Data Science and Developers Digest coverage | P/S |
| Mistral Large 4 (preview 6 Oct 2026): ~1.05T total / 49B active parameters; open weights promised "by the end of the month" (27 Oct per secondary reporting), license unnamed; Artificial Analysis Intelligence Index 38 (eighth among open-weight models); Artificial Analysis Cyber Index fifth of eighteen models. Mistral's own benchmark claims are not independently replicated | ActuIA, "Mistral Large 4: how good is the best open model outside China?"; Artificial Analysis | S |
| Harari, Tanner Lecture, University of Oxford, 21 May 2026, "AI has hacked the code of human civilization": AI as a "native bureaucrat" taking over institutions from inside, and a shift "from attention to intimacy" | Third-party recording, re-edited and retitled by the NeuralHegemony channel: youtube.com/watch?v=IUp3_q-TgTI. No official recording found yet | S |
| Leahy: human CEOs who "just rubber stamp what the AI CEOs tells them to do" do not count as oversight; current development "a clown show" | Interview transcript provided for review, Oct 2026, via a third-party repackaging; original source not yet identified — **link to be added** | S |
| Hao: lab leaders' catastrophe rhetoric as "an act of speech to persuade," part of a mythology justifying their control | Interview transcript provided for review, Oct 2026 (Diary of a CEO, via a third-party repackaging); *Empire of AI* (2025) | S |
| Tegmark's twelve AI aftermath scenarios | Max Tegmark, *Life 3.0: Being Human in the Age of Artificial Intelligence* (Knopf, 2017), ch. 5 | P |
| Grace et al. median respondent: 5% chance of extremely bad outcomes such as human extinction | Grace et al. 2024, same as above | P |

---

## Known gaps

Rows marked "link to be added" or "primary source not yet traced" are real gaps. Each claim traces to material that was read, but the citation was not recorded at the time. Pinning one, or showing that a cited source does not say what the document claims, is among the most useful contributions available.

## Claims that are inference, not citation

The following are the document's own reasoning and should not be attributed to any source:

- That the retraining clock bounds hard takeoff specifically rather than closed-loop RSI generally (though AI Futures' model revision independently supports it)
- That alignment dominates the disempowerment column while the two levers are comparable on extinction
- That pathway B produces comparable disempowerment risk without RSI
- That rented human labour bears on pathways A and B but not on physical RSI
- The three- and four-way friction taxonomies for physical bootstrap
- All probability estimates in every table
- The three stated alignment parameters (solved at loop-close, holding through 2060, deception by default) and the combined figure derived from them; derivation in `FAQ.md`. Set after seeing elicitations from AI systems, which are not cited as evidence
