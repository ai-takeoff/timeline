# References

Every externally checkable claim in `ai-timelines-and-outcomes.md`, with its source and a source-quality class. The document itself carries no links, to keep it readable and under its word ceiling; this file is where verification starts.

**Source classes:**

- **P** — primary. The paper, dataset, filing or official statement itself.
- **S** — secondary. Reporting or analysis about a primary source.
- **I** — inference. The document's own reasoning from P or S material, not a claim anyone else has made.
- **U** — unverified. Reported but not independently confirmed; flagged as such in the document.
- **P\*** — primary, fetched and quoted directly, but a specific figure within it later failed a second party's independent search-based re-verification. Worth re-checking rather than either dismissing or fully trusting.

If a claim in the document cannot be traced from this file, that is a defect worth an issue.

## Link durability

Link rot is a real threat to a document built on checkability, and silent *editing* of a live source is a worse one, because a 404 is visible and an edit is not. Sources are therefore handled by stability class:

- **Permanent identifiers preferred.** arXiv IDs and DOIs are versioned and never rewritten in place. Where one exists it is the citation; the URL is convenience. These are not link-checked.
- **Unstable sources must carry an archive snapshot** alongside the live URL — Substack and other newsletter hosts, social posts, startup sites, and news reporting. A Wayback or archive.today capture is the citation of record; the live link is secondary. In this file that currently means the AI Futures post, the Truth Social post, market reporting, and RentAHuman.
- **Institutional sources** (METR, Epoch, lab disclosures) sit between: archive them when a claim depends on a specific figure rather than the existence of the page.

`linkcheck.py` runs monthly via GitHub Actions and opens an issue on failure. It is deliberately **not** part of `check.py`: link health and structural integrity are different failure modes, and a dead external link should not block a commit that fixes a typo.

It reports **404 and 410 as dead**, and treats **403 and 429 as inconclusive** rather than failures, since those are overwhelmingly anti-bot responses rather than missing resources. Inconclusive results need a human look, not an alarm.

When a link does die: replace it with an archive snapshot if one exists, re-source the claim, or mark the row unverifiable here. **Do not silently drop the claim from the document** — a claim that can no longer be checked is itself information, and hiding that is the failure this file exists to prevent.

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
| Model revision simulating training runs raised AC→ASI median 1.22→1.72 yr and 3.86→4.56 yr, slowing fast takeoffs only | AI Futures Project, same post (fetched directly and quoted from at the time; a later reviewer's search could confirm the revision and direction but not these exact figures — worth an independent re-check) | P* |
| AI Futures forecasts are conditional on maximum technically feasible speed | AI Futures Project, same | P |
| Halstead's alignment-bottleneck argument | AI Futures Project, same | P |
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
| 162× fewer agent calls vs SimpleTES; **1.7× vs its own fixed-exploration ablation**; 1.79–2.43× on GPU kernels; >50× on math optimization | Same paper. The 1.7× figure is the one that isolates the recursive contribution | P |
| Domains are algorithm engineering, GPU kernels, math optimization — not AI research | Same | P |
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
| RentAHuman.ai: REST API and MCP server, stablecoin payouts, self-reported registration figures | https://rentahuman.ai/ and contemporaneous coverage | P/S |
| Security researchers characterise such marketplaces as a CAPTCHA-solving analogue with physical-world reach | arXiv preprint; **link to be added** | P |

---

## Known gaps

Several rows above are marked with links or primary sources still to be pinned. These are real gaps, not placeholders for things that don't exist — each claim traces to material that was read, but the citation was not recorded at the time it entered the document.

**This is itself a finding about the process.** A document built around checkability accumulated twenty externally verifiable claims and zero links before anyone noticed. Contributions that pin an unpinned source, or that show a cited source does not say what the document claims, are among the most useful available.

| Kokotajlo: material bottlenecks "nothing comes remotely close"; "apply that speedup multiplier" | 80,000 Hours podcast, "Daniel Kokotajlo on what a hyperspeed robot economy might look like," Jan 2026 | P |
| AI Futures model: compute growth "will slow over time... speed of building new fabs," "big impact in ~2035+" | aifuturesmodel.com, AI Futures Model documentation | P |
| Co-authored piece: AI R&D automation implies proximity to robots that "reliably construct and operate power plants, fabs, mines" | AI 2040: Plan A, LessWrong comment thread, 2026 | P |

## Claims that are inference, not citation

The following are the document's own reasoning and should not be attributed to any source:

- That the retraining clock bounds hard takeoff specifically rather than closed-loop RSI generally (though AI Futures' model revision independently supports it)
- That alignment dominates the disempowerment column while the two levers are comparable on extinction
- That pathway B produces comparable disempowerment risk without RSI
- That rented human labour bears on pathways A and B but not on physical RSI
- The three- and four-way friction taxonomies for physical bootstrap
- All probability estimates in every table
