# Research Master Map

Date baseline: 2026-08-09

Repo root: `/home/manishmehta/ui-projects/annual-report-research`

This file is the top-level map for the current archive. It is meant to answer four practical questions:

1. What is already being tracked?
2. How is the `2025 annual report` plus trailing-quarters workflow organized?
3. Which research tracks are already real rather than aspirational?
4. Where should new companies and new themes plug in next?

## Archive model

The repo is organized in four layers:

- `raw/`: source capture from `annualreports`, `company-ir`, `sec`, and `earnings-calls`
- `extracted/`: company packets and sector/theme synthesis files
- `analysis/`: sector briefs, theme memos, and cross-sector reads
- `indexes/`: coverage trackers, company universes, theme trackers, and interface maps

The operating collection standard is:

- `2025` annual report
- annual filing for that same reporting year
- latest three reported quarters in scope as of `2026-08-09`

In `coverage-tracker.csv`, a company counts as a fully packetized base case when all of these are present:

- annual report collected
- annual filing collected
- latest quarter collected
- prior quarter collected
- third quarter back collected

## Core indexes

- [Pilot Companies](/indexes/pilot-companies.md)
- [Coverage Tracker](/indexes/coverage-tracker.csv)
- [Theme Tracker](/indexes/theme-tracker.csv)
- [Force Map](/indexes/force-map.csv)
- [Sectors](/indexes/sectors.csv)
- [Companies](/indexes/companies.csv)

Specialized interface maps already exist for higher-density areas:

- [Technology Interface Research Index](/indexes/technology-interface-research-index-2026-08-09.md)
- [Financial Interface Research Index](/indexes/financial-interface-research-index-2026-08-09.md)
- [Consumer Interface Research Index](/indexes/consumer-interface-research-index-2026-08-09.md)

## Active research tracks

The archive is already running multiple parallel tracks.

### 1. Sector coverage track

This is the base layer: collect and packetize companies by `sector -> industry -> company`.

Current sector coverage from `coverage-tracker.csv`:

| Sector | Companies tracked | Fully packetized base cases |
|---|---:|---:|
| Basic Materials | 11 | 7 |
| Consumer Goods | 10 | 9 |
| Financial | 17 | 13 |
| Healthcare | 10 | 8 |
| Industrial Goods | 22 | 13 |
| Real Estate | 6 | 5 |
| Retail | 3 | 3 |
| Services | 25 | 10 |
| Technology | 18 | 13 |
| Utilities | 14 | 7 |

Important taxonomy note:

- `AnnualReports.com` sector labels are useful but not clean.
- Several retail-like businesses currently sit under `Services` or `Consumer Goods` in the source taxonomy.
- The archive should preserve the source taxonomy while also using cross-sector theme files and interface maps to recover the actual business-model structure.

### 2. Company packet track

Each company packet is the working unit of analysis. A good packet should let us answer:

- what changed in the `2025` annual report
- what happened across the latest three reported quarters
- what management is emphasizing now
- what recurring economics, margin structure, capital intensity, or demand pattern actually matter

The packet workflow is:

1. save source artifacts under `raw/...`
2. build or update the company folder under `extracted/<sector>/<industry>/<company>/`
3. roll the company into sector, industry, interface, and theme summaries
4. log residual collection gaps in `coverage-tracker.csv` and source ledgers

### 3. Sector and industry interpretation track

The repo already contains sector briefs in `analysis/sectors/`. These are not just collection logs; they are early reads on what each sector is becoming in the `2025` annuals and late-`2025` / `2026` quarterlies.

Current sector-brief coverage:

- Basic Materials
- Consumer Goods
- Financial
- Healthcare
- Industrial Goods
- Real Estate
- Services
- Technology
- Utilities

This means the archive is already beyond raw collection and is in the interpretation phase for most major sectors.

### 4. Cross-sector theme track

The theme tracker currently holds `27` active themes. These are real tracks, not placeholders.

The theme set currently includes:

- `technology-ai-platform-split`
- `financial-large-bank-scale`
- `financial-premium-payments-and-membership`
- `financial-insurance-underwriting-and-investment-float`
- `financial-asset-management-flows-and-fee-rate-pressure`
- `financial-alternative-manager-fees-and-realizations`
- `financial-market-infrastructure-and-risk-transfer`
- `financial-custody-and-asset-servicing-scale`
- `financial-ratings-benchmarks-and-data-infrastructure`
- `consumer-goods-value-portfolio`
- `healthcare-policy-and-portfolio`
- `industrial-automation-and-infrastructure`
- `services-freight-brokerage-and-productivity`
- `cultural-value-trust-and-automation`
- `institutional-operating-infrastructure`
- `capital-intensity-and-investment-concentration`
- `regulation-trust-and-sovereignty-risk`
- `real-estate-reckoning`
- `experience-status-and-community`
- `labor-intermediation-and-fractional-work`
- `labor-squeeze`
- `graying-market`
- `immigration-squeeze`
- `commodity-whiplash`
- `built-environment-housing-affordability-chain`
- `recurring-consumer-interfaces-and-membership-systems`
- `loyalty-currencies-partner-monetization-and-deferred-revenue`

These themes are the main answer to the user's "more tracks" question: yes, there is already one archive, but inside it there are many active analytical tracks, and more should appear as company density rises.

### 5. Interface-model track

Some sectors are already dense enough that standard sector buckets are too coarse. That is why the repo has dedicated interface maps for:

- technology
- financials
- consumer interfaces

These interface maps are useful when the real question is not "what sector is this?" but:

- what operating interface does this company own?
- what repeated behavior does it monetize?
- what infrastructure layer does it control?
- what trust, routing, workflow, or habit surface is the real moat?

This track should expand as more packets are added in Retail, Services, and cross-sector consumer names.

## What is already clear

A few archive-level conclusions are already emerging:

- This is not just a sector archive. It is becoming a business-model and economic-structure archive.
- `AnnualReports.com` is useful for discovery and taxonomy, but official IR and SEC sources are often the real source of truth for the `2025` annual window.
- Retail, services, consumer, financial, and technology names increasingly need to be grouped by interface, recurring relationship, and monetization mechanism rather than by old top-level sector labels alone.
- The strongest cross-company reads so far are around recurring interfaces, loyalty and stored value systems, premium access, workflow infrastructure, capital intensity, and built-environment demand chains.

## Expansion rules

As more `2025` annual reports and trailing `2026` quarterlies are reviewed, new work should plug in through these rules:

1. Add the company to the correct source-taxonomy sector and industry folder.
2. Update `coverage-tracker.csv` with the real annual and quarter artifact state.
3. Add or update the company packet in `extracted/...`.
4. Roll the company into the relevant sector brief.
5. Roll the company into at least one cross-sector theme if it changes a broader pattern.
6. If the company exposes a repeated business-model structure that cuts across sectors, update an interface map or create a new one.

## Next useful build-outs

The current archive structure suggests five obvious expansion lanes:

- deepen `Retail`, which is still underrepresented as a source-taxonomy sector
- keep widening `Services`, especially where retail, dining, travel, and recurring-consumer-interface behavior blur together
- keep sharpening the consumer-interface and loyalty mechanism distinctions rather than collapsing them into one generic membership bucket
- continue adding direct operator evidence to the built-environment and housing-affordability chain
- add more interface maps when a sector starts mixing unlike business models under one broad label

## Current status

As of `2026-08-09`, this repo is already a real multi-track research system:

- organized in git
- organized by sector and industry
- organized by company packets
- organized by cross-sector themes
- increasingly organized by interface and monetization structure

That is the right shape for continuing the `2025 annual report` plus trailing-quarters buildout without losing the big picture.
