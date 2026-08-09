# `ibis-industries` Crosswalk

Date reviewed: 2026-08-09

Related repo reviewed:

- `/home/manishmehta/ui-projects/ibis-industries`

## What it is

`ibis-industries` is a broad industry-and-forces research system. It is built from 2022 IBISWorld industry baselines refreshed with live 2024-2026 web research and organized around:

- per-industry briefs in `briefs_full.json`
- trend synthesis in `trends_full_raw.json`
- force packs such as `the-ai-rewiring`, `the-breach-economy`, `the-compute-super-cycle`, `the-health-reckoning`, and `the-hollow-middle`

It is not a duplicate of this repo's archive.

## How it differs from `annual-report-research`

`annual-report-research` is narrower and more current at the company-disclosure level:

- target annual window: `2025`
- target quarterly window: latest three reported quarters as of `2026-08-09`
- source priority: AnnualReports, official IR, SEC filings, and transcript artifacts
- output shape: company packets, company profiles, sector briefs, and theme memos tied to named public companies

`ibis-industries` is broader and more thematic:

- source priority: IBIS baseline plus live web refresh
- output shape: industry briefs and cross-cutting force narratives
- best use here: theme generation, sector gap-finding, and cultural / industrial context

## Current mapping

The strongest current crosswalks are:

- `technology-ai-platform-split`
  - closest `ibis-industries` forces:
    - `the-ai-rewiring`
    - `the-compute-super-cycle`
    - `the-breach-economy`
  - useful for:
    - AI services versus software ownership
    - cybersecurity demand
    - hardware, network, and datacenter spillover

- `financial-large-bank-scale`
  - closest `ibis-industries` forces:
    - `money-gets-unbundled`
    - `the-compliance-tax`
  - useful for:
    - scale-bank economics
    - payment rails
    - compliance as moat

- `consumer-goods-value-portfolio`
  - closest `ibis-industries` forces:
    - `the-health-reckoning`
    - `the-hollow-middle`
    - `the-margin-vise`
  - useful for:
    - affordability architecture
    - premium versus value splits
    - GLP-1 and health-pressure effects

- `healthcare-policy-and-portfolio`
  - closest `ibis-industries` forces:
    - `the-health-reckoning`
    - `the-pricing-power-collapse`
    - `the-graying-market`
    - `the-compliance-tax`
  - useful for:
    - reimbursement pressure
    - aging-demand read-through
    - provider and payer admin burden

- `industrial-automation-and-infrastructure`
  - closest `ibis-industries` forces:
    - `atoms-strike-back`
    - `the-compute-super-cycle`
    - `the-electrification`
    - `the-labor-squeeze`
  - useful for:
    - power, cooling, and electrical demand
    - infrastructure labor bottlenecks
    - reshoring and capex intensity

- `commodity-whiplash`
  - closest `ibis-industries` forces:
    - `commodity-whiplash`
    - `atoms-strike-back`
  - useful for:
    - fertilizer and agricultural-input volatility
    - copper and aluminum price-plus-restart economics
    - tariffs, duties, energy inputs, and physical-system instability

- `services-freight-brokerage-and-productivity`
  - closest `ibis-industries` forces:
    - `the-fractional-worker`
    - `the-labor-squeeze`
    - `the-channel-shift`
  - useful for:
    - route density
    - productivity pressure
    - service models under labor strain

- `cultural-value-trust-and-automation`
  - closest `ibis-industries` forces:
    - `the-hollow-middle`
    - `the-health-reckoning`
    - `the-channel-shift`
    - `the-breach-economy`
  - useful for:
    - trust-sensitive consumption
    - automation acceptance
    - premium versus value social splits

- `experience-status-and-community`
  - closest `ibis-industries` forces:
    - `the-experience-economy`
    - `the-channel-shift`
  - useful for:
    - live-event demand
    - travel and lodging demand
    - premium access, membership, and status-linked spending

- `institutional-operating-infrastructure`
  - closest `ibis-industries` forces:
    - `the-compliance-tax`
    - `the-fractional-worker`
    - `the-labor-squeeze`
  - useful for:
    - outsourced operations
    - hidden workflow systems
    - compliance-heavy service layers

- `labor-intermediation-and-fractional-work`
  - closest `ibis-industries` forces:
    - `the-fractional-worker`
    - `the-labor-squeeze`
  - useful for:
    - staffing platforms
    - contract talent and permanent placement
    - managed-services and external execution layers

- `capital-intensity-and-investment-concentration`
  - closest `ibis-industries` forces:
    - `the-compute-super-cycle`
    - `atoms-strike-back`
    - `the-electrification`
    - `the-real-estate-reckoning`
  - useful for:
    - datacenter buildout
    - power and cooling demand
    - infrastructure ownership concentration

- `regulation-trust-and-sovereignty-risk`
  - closest `ibis-industries` forces:
    - `the-compliance-tax`
    - `the-breach-economy`
    - `the-pricing-power-collapse`
  - useful for:
    - AI rules
    - privacy and security compliance
    - reimbursement and capital-rule pressure

## Practical rule for this repo

Use `ibis-industries` to answer:

1. Which sector or theme is under-covered?
2. What non-company force is likely driving several company results at once?
3. Which adjacent industry should influence the wording of a sector memo?

Do not use `ibis-industries` to answer:

1. What did a specific public company report in `2025` or `2026`?
2. Which exact quarter labels belong in a company packet?
3. Whether an earnings claim is verified without checking IR or SEC artifacts here

## Best next uses

- Pull `the-ai-rewiring__law-and-consulting.txt` and related packs when expanding the Accenture and services-layer analysis.
- Pull `the-compute-super-cycle` and `the-labor-squeeze` when broadening industrial and technology power / infrastructure themes.
- Pull `the-health-reckoning` when sharpening the consumer-goods and healthcare crossover around diet, chronic care, and payer pressure.
- Pull `money-gets-unbundled` and `the-compliance-tax` when broadening Financial beyond the current company set.
