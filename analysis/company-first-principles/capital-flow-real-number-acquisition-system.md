# Capital Flow Real-Number Acquisition System

## Purpose

The capital-flow work needs a repeatable evidence pipeline, not one-off notes.

The pipeline should answer two questions at the same time:

| Direction | Question | Practical Output |
|---|---|---|
| Claim to evidence | What exact source number would prove or weaken this claim? | Source manifest row and extraction target. |
| Evidence to claim | What claim does this source number actually justify? | Verification-log row and revised claim language. |

## The Four-Layer Data Stack

| Layer | Source Type | What It Proves | Example |
|---|---|---|---|
| Company filings | 10-K, 10-Q, 8-K exhibits | Audited or filed financial facts, risks, segment definitions, capital structure | Apollo 10-K, Ares 10-Q |
| Investor materials | Earnings releases, supplements, decks, transcripts | Timely operating metrics and management explanation | AUM, FPAUM, fundraising, deployment, originations |
| Market and regulator datasets | Fed, FDIC, FERC, EIA, CMS, ISO queues, NRC | Outside denominator or disproof check | Bank loan growth, power load, rate base, Medicare rate pressure |
| Cross-company ledger | Normalized CSV rows | Comparison across companies and claims | Claim ID, company, metric, value, period, source URL |

The key rule: a claim is not strong until it has both company evidence and an outside denominator or disproof source where relevant.

The end-to-end thesis and mechanism are maintained in:

`analysis/company-first-principles/capital-flow-to-real-economy-end-to-end-thesis.md`

That page defines the full chain the acquisition system is trying to prove:

`original money source -> routing platform -> funding vehicle -> borrower or company -> asset, project, backlog, fleet, facility, or collateral pool -> use of proceeds -> operating output -> cash, return, durability, and risk -> safe claim`

The structured question-and-answer matrix is:

`analysis/company-first-principles/capital-flow-meta-question-answer-matrix.md`

`analysis/company-first-principles/data/capital-flow-meta-question-answer-matrix.csv`

The first bank-role follow-through pass is:

`analysis/company-first-principles/capital-flow-bank-role-after-private-credit-pass-1.md`

`analysis/company-first-principles/data/capital-flow-bank-role-after-private-credit-pass-1.csv`

The first source-to-vehicle bridge pass is:

`analysis/company-first-principles/capital-flow-capital-source-to-vehicle-bridge-pass-1.md`

`analysis/company-first-principles/data/capital-flow-capital-source-to-vehicle-bridge-pass-1.csv`

The first use-of-proceeds classification pass is:

`analysis/company-first-principles/capital-flow-use-of-proceeds-classification-pass-1.md`

`analysis/company-first-principles/data/capital-flow-use-of-proceeds-classification-pass-1.csv`

For the private-credit claim, the first denominator pass uses Federal Reserve H.8 bank-credit series from FRED. That keeps the analysis honest: Apollo and Ares prove nonbank credit scale, while bank data tests whether the scale is material relative to commercial-bank lending.

For borrower-level testing, BDC filings are the next practical layer. They show portfolio-company exposure, funding activity, loan seniority, yield, and non-accruals.

For funded-destination testing, BDC industry disclosures and schedules are the next layer after the borrower panel. They identify whether private-credit dollars are landing in software, healthcare, professional services, insurance, commercial services, logistics, defense, or other borrower lanes.

## New Files

- Source manifest: `analysis/company-first-principles/data/capital-flow-source-acquisition-manifest.csv`
- Download log: `analysis/company-first-principles/data/capital-flow-source-download-log.csv`
- Fetch script: `scripts/fetch-capital-flow-sources.py`
- Bank-credit denominator refresh script: `scripts/refresh-bank-credit-denominators.py`
- ARCC schedule extraction script: `scripts/extract-arcc-schedule.py`
- OBDC schedule extraction script: `scripts/extract-obdc-schedule.py`
- Cross-BDC industry comparison builder: `scripts/build-cross-bdc-industry-comparison.py`
- BXSL industry percentage extraction script: `scripts/extract-bxsl-industry-percentages.py`
- Verified metric log: `analysis/company-first-principles/data/capital-flow-primary-source-verification-log.csv`
- Local extraction table: `analysis/company-first-principles/data/capital-flow-local-source-extractions.csv`
- Bank denominator table: `analysis/company-first-principles/data/capital-flow-bank-denominator-extractions.csv`
- Bank comparison table: `analysis/company-first-principles/data/capital-flow-private-credit-bank-denominator-comparison.csv`
- BDC borrower evidence table: `analysis/company-first-principles/data/capital-flow-bdc-borrower-evidence.csv`
- BDC industry lane evidence table: `analysis/company-first-principles/data/capital-flow-bdc-industry-lane-evidence.csv`
- Borrower matching workbench: `analysis/company-first-principles/data/capital-flow-borrower-matching-workbench.csv`
- Borrower source-of-funds evidence: `analysis/company-first-principles/data/capital-flow-borrower-source-of-funds-evidence.csv`
- Borrower transaction fact extractions: `analysis/company-first-principles/data/capital-flow-borrower-transaction-fact-extractions.csv`
- Borrower claim-strength matrix: `analysis/company-first-principles/data/capital-flow-borrower-claim-strength-matrix.csv`
- Borrower transaction raw sources: `raw/primary-sources/capital-flow/borrower-transactions/`
- ARCC schedule parser rows: `analysis/company-first-principles/data/capital-flow-arcc-schedule-parser-rows.csv`
- ARCC schedule industry summary: `analysis/company-first-principles/data/capital-flow-arcc-schedule-industry-summary.csv`
- ARCC official industry subtotals: `analysis/company-first-principles/data/capital-flow-arcc-official-industry-subtotals.csv`
- OBDC official industry subtotals: `analysis/company-first-principles/data/capital-flow-obdc-official-industry-subtotals.csv`
- OBDC industry summary: `analysis/company-first-principles/data/capital-flow-obdc-industry-summary.csv`
- BXSL official industry percentages: `analysis/company-first-principles/data/capital-flow-bxsl-official-industry-percentages.csv`
- Cross-BDC industry lane comparison: `analysis/company-first-principles/data/capital-flow-cross-bdc-industry-lane-comparison.csv`
- Real-number extraction roadmap: `analysis/company-first-principles/capital-flow-real-number-extraction-roadmap.md`
- Real-number extraction queue: `analysis/company-first-principles/data/capital-flow-real-number-extraction-queue.csv`

## Acquisition Workflow

1. Start with a claim ID from `capital-flow-claims-evidence-backlog.md`.
2. Identify companies, source documents, and proof/disproof metrics.
3. Add source rows to `capital-flow-source-acquisition-manifest.csv`.
4. Run:

```bash
python3 scripts/fetch-capital-flow-sources.py
```

5. Extract exact numbers from the downloaded files.
6. Add extracted numbers to `capital-flow-primary-source-verification-log.csv`.
7. Add borrower-lane rows when the filing gives industry percentages, portfolio-company names, or schedule tags.
8. Only then decide whether the thesis should be promoted, narrowed, or rejected.

The more detailed local extraction table should be used when a number has been found inside a downloaded file. It captures page numbers, spreadsheet cells, and the claim effect of each metric.

The industry-lane evidence table should be used when the source identifies where capital is going by borrower category. Treat explicit percentages as high-confidence rows. Treat raw schedule mentions as medium-confidence until a structured parser extracts cost, fair value, lien, rate, and industry fields.

The borrower matching workbench should be used when the claim moves from "private credit funds this lane" to "private credit displaced banks for this borrower." That upgrade requires borrower, sponsor, use of proceeds, prior financing source, current lender group, and bank facility role.

Parser-derived schedule extracts should be kept separate from verified extraction logs until they reconcile to reported totals. The ARCC official industry subtotal table reconciles to total investment fair value, while the ARCC row-level parser remains `parser-derived-needs-reconciliation`. The OBDC official industry subtotal table now also reconciles exactly to reported total investment fair value, including miscellaneous commitment adjustments.

For a no-write preview:

```bash
python3 scripts/fetch-capital-flow-sources.py --dry-run
```

For one source:

```bash
python3 scripts/fetch-capital-flow-sources.py --source-id=ares-2026q2-earnings-presentation
```

## What Annual And Quarterly Reports Add

Annual reports and 10-Ks are best for:

- Segment definitions
- Long-run AUM and revenue bridges
- Risk factors
- Capital structure
- Insurance or retirement-services mechanics
- Credit and liquidity risk

Quarterly reports, supplements, and earnings decks are best for:

- Current AUM and FPAUM
- Fundraising and net inflows
- Deployment
- Dry powder or available capital
- Originations
- Backlog and demand signals
- Updated management commentary

Transcripts are best for:

- Why management says the number changed
- Whether demand is broad or one-time
- Credit-quality concerns
- Bottlenecks such as power, permitting, regulation, labor, or capital cost

## Additional Data Sources By Claim Type

| Claim Type | Company Sources | Outside Sources Needed |
|---|---|---|
| Private credit replacing bank lending | Apollo, Ares, Blackstone, KKR, Carlyle filings and supplements | Federal Reserve H.8 bank credit, FDIC loan data, BDC filings, rating-agency default data |
| Insurance liabilities funding private assets | Apollo/Athene, Brookfield, KKR/Global Atlantic, Blackstone insurance disclosures | NAIC statutory filings, rating-agency reports, insurance capital/risk-based-capital data |
| AI capital becoming power/grid demand | Utilities, power producers, data-center exposed suppliers | EIA, FERC, ISO interconnection queues, PJM/ERCOT/MISO/CAISO, state rate-case filings |
| Built-environment supplier benefit | WESCO, Ferguson, Core & Main, United Rentals, Fastenal, Grainger | Construction spending, ABI, Dodge/ConstructConnect where available, data-center capex datasets |
| Healthcare site-of-care and reimbursement flows | UnitedHealth, Cigna, DaVita, Option Care, Addus, BrightSpring, Enhabit | CMS reimbursement data, Medicare Advantage rules, Medicaid rate materials, labor/wage data |
| Internet control layer | Cloudflare, Akamai, Fastly, Zscaler, DigitalOcean | Cloud spend data, traffic datasets, cybersecurity spend surveys, public-sector contract data |

## Promotion Rules

| Status | Meaning |
|---|---|
| `analysis-derived-needs-primary-source` | Number came from an analysis note and needs source re-checking. |
| `source-downloaded-not-extracted` | Source file is local and checksummed, but the metric has not been extracted. |
| `metric-found-primary-source` | The number was found in an issuer, SEC, or regulator source. |
| `metric-found-secondary-source` | The number was found in a credible outside source but not yet the original source. |
| `needs-denominator` | The company metric is real, but the broader claim still needs a market/regulator denominator. |
| `supported-narrowly` | The evidence supports a narrower version of the claim. |
| `contradicted-or-weakened` | The source evidence weakens or contradicts the claim. |

## Current Priority Queue

| Priority | Claim | First Documents |
|---|---|---|
| 1 | CF-004, CF-005 | Apollo Q2 2026 release/supplement/transcript/10-Q; Apollo FY2025 10-K and SEC exhibit; Ares Q2 2026 presentation/10-Q |
| 2 | CF-006 to CF-010 | Constellation, NextEra, Vistra, NRG, AEP, Duke, Exelon 10-Ks, 10-Qs, investor decks, and power-market datasets |
| 3 | CF-011 to CF-013 | WESCO, Ferguson, Core & Main, United Rentals, Fastenal, Grainger, Builders FirstSource, Sherwin-Williams annual/quarterly reports |
| 4 | CF-014 | Cloudflare, Akamai, Fastly, Zscaler, DigitalOcean filings, shareholder letters, and transcripts |
| 5 | CF-019 | UnitedHealth, Cigna, DaVita, Option Care, Addus, BrightSpring, Enhabit filings plus CMS and reimbursement data |

The executable queue is now in `analysis/company-first-principles/data/capital-flow-real-number-extraction-queue.csv`. It adds one row per claim question with source targets, destination tables, decision rules, current evidence anchors, and the next action.

RNQ-002 has also been refreshed against FRED. The latest available bank-credit rows did not move past `2026-08-12` for weekly series or `2026-07-01` for monthly series, and the conclusion remains: bank credit is still growing in aggregate, so displacement has to be proved borrower by borrower or category by category.

## Simple Version

We gather real numbers by building a source chain:

`claim -> source document -> downloaded file -> extracted metric -> verification log -> revised claim`

That lets us say: this claim came from analysis, this number came from a filing, and this conclusion is only as strong as the sources behind it.
