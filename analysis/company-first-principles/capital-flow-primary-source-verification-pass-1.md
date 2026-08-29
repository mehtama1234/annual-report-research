# Capital Flow Primary-Source Verification Pass 1

## What This Pass Does

This pass tests the capital-flow thesis in both directions.

| Direction | Question | Output |
|---|---|---|
| Analysis to evidence | We already claimed Apollo and Ares show private-credit and insurance-linked capital flow. What exact numbers would prove that? | A source checklist and verified metrics. |
| Evidence to analysis | Once we read the source numbers, what claims do they actually support? | Narrower, testable claims with limits and next evidence needs. |

The first pass covers Apollo and Ares because they are the cleanest starting points for the private-credit and insurance-liability channel.

## Workspace Source Status

The local source ledgers for Apollo and Ares point to older raw paths that are not present in this workspace:

- `extracted/financial/asset-management/apollo-global-management-inc/source-ledger.md`
- `extracted/financial/asset-management/ares-management-corporation/source-ledger.md`

Because those raw filings were not available locally, this pass uses live primary issuer and SEC sources. The extracted company-analysis notes remain useful as claim generators, but they are not enough for final evidence status.

## Claim-First Test

### Apollo

Starting claim from analysis:

`Apollo is a private-credit origination and retirement-spread engine, not just an alternative asset manager.`

Testable claim:

`Insurance and retirement liabilities are being converted into private-credit origination power.`

Ledger claim:

`CF-004`

Required proof metrics:

- Originations
- Inflows
- AUM
- Fee-generating AUM
- Spread-related earnings
- Retirement-services or Athene-linked asset and liability data
- Credit quality and spread commentary

Disproof or weakening metrics:

- Lower originations
- Lower inflows
- Spread compression
- Credit losses
- Surrender pressure
- Regulatory restriction

### Ares

Starting claim from analysis:

`Ares is a fee-paying-AUM and private-credit origination machine, not a classic realization-dependent alternatives firm.`

Testable claim:

`Private credit is replacing part of bank lending and Ares is one of the recurring-fee routers of that shift.`

Ledger claim:

`CF-005`

Required proof metrics:

- AUM
- Fee-paying AUM
- Available capital / dry powder
- Gross fundraising
- Net inflows
- Deployment
- Direct-lending and credit-segment detail
- Non-accruals or credit-loss commentary

Disproof or weakening metrics:

- Fundraising slowdown
- Weak deployment
- Falling available capital
- Rising non-accruals
- Spread compression
- Fee-paying AUM stagnation

## Primary-Source-Backed Numbers

| Company | Period | Metric | Value | Source | Claim Use |
|---|---:|---|---:|---|---|
| Apollo | Q2 2026 | AUM | about `1.05T USD` | Apollo Q2 2026 results press release | Supports platform scale for CF-004. |
| Apollo | FY2025 | Originations | more than `300B USD` | Apollo FY2025 SEC 8-K exhibit / earnings release | Supports credit-manufacturing scale for CF-004. |
| Apollo | FY2025 | Inflows | more than `225B USD` | Apollo FY2025 SEC 8-K exhibit / earnings release | Supports capital-gathering demand for CF-004. |
| Apollo | FY2025 | AUM | about `938B USD` | Apollo FY2025 SEC 8-K exhibit / earnings release | Shows scale before crossing the Q2 2026 trillion-dollar mark. |
| Ares | Q2 2026 | AUM | `671.3B USD` | Ares Q2 2026 earnings presentation | Supports platform scale for CF-005. |
| Ares | Q2 2026 | Fee-paying AUM | `409.9B USD` | Ares Q2 2026 earnings presentation | Supports recurring-fee private-credit/alternatives economics. |
| Ares | Q2 2026 | Available capital | `170.0B USD` | Ares Q2 2026 earnings presentation | Supports future deployment capacity. |
| Ares | Q2 2026 | Gross fundraising | `36.4B USD` | Ares Q2 2026 earnings presentation | Supports current investor demand. |
| Ares | Q2 2026 | Net inflows | `34.4B USD` | Ares Q2 2026 earnings presentation | Supports current capital formation. |
| Ares | Q2 2026 | Capital deployment | `35.9B USD` | Ares Q2 2026 earnings presentation | Shows capital moving into assets, not only sitting in dry powder. |
| Ares | Q2 2026 | Fee-related earnings | `491.1M USD` | Ares Q2 2026 earnings presentation | Supports recurring earnings from fee-paying assets. |
| Ares | Q2 2026 | Realized income | `521.5M USD` | Ares Q2 2026 earnings presentation | Supports near-term earnings conversion. |

## Local Extraction Pass

The first downloaded source pack has now been converted into a local extraction table:

`analysis/company-first-principles/data/capital-flow-local-source-extractions.csv`

Current local extraction count:

| Company | Rows | Claim IDs |
|---|---:|---|
| Apollo | 15 | CF-004 |
| Ares | 13 | CF-005 |
| Total | 28 | CF-004, CF-005 |

The table is more audit-ready than the first verification log because each metric points to:

- a downloaded local file
- a source ID from the acquisition manifest
- a page, section, or spreadsheet cell
- the claim effect
- the next data needed

Examples:

| Company | Metric | Value | Local Source Location |
|---|---:|---:|---|
| Apollo | AUM | `1.047T USD` | `apollo-q2-2026-earnings-release.pdf`, page 5 |
| Apollo | Fee-generating AUM | `858B USD` | `apollo-q2-2026-earnings-release.pdf`, page 5 |
| Apollo | Q2 originations | `74B USD` | `apollo-q2-2026-earnings-release.pdf`, page 5 |
| Apollo | LTM originations | `317B USD` | `apollo-q2-2026-earnings-release.pdf`, page 5 |
| Apollo | Retirement-services total gross inflows | `22.069B USD` | `apollo-q2-2026-financial-supplement.xlsx`, `RS Flows and IA!K11` |
| Apollo | Inflows attributable to Athene | `17.095B USD` | `apollo-q2-2026-financial-supplement.xlsx`, `RS Flows and IA!K16` |
| Ares | AUM | `671.3B USD` | `ares-q2-2026-earnings-presentation.pdf`, page 5 |
| Ares | FPAUM | `409.9B USD` | `ares-q2-2026-earnings-presentation.pdf`, page 5 |
| Ares | Available capital | `170.0B USD` | `ares-q2-2026-earnings-presentation.pdf`, page 5 |
| Ares | Q2 capital deployment | `35.9B USD` | `ares-q2-2026-earnings-presentation.pdf`, pages 5 and 16 |
| Ares | Credit group deployment | `23.7B USD` | `ares-q2-2026-earnings-presentation.pdf`, page 17 |
| Ares | U.S. direct-lending deployment | `12.4B USD` | `ares-q2-2026-earnings-presentation.pdf`, page 17 |

This shifts the work from "we found sources" to "we have locally auditable metrics."

## Evidence-First Claims From The Numbers

The source numbers support these narrower claims:

1. Apollo is not only gathering capital; it is manufacturing credit assets at very large scale.
2. Apollo's retirement and insurance channel matters because AUM, originations, inflows, and spread earnings need to be read together.
3. Ares is a major private-credit and alternatives capital router because it combines AUM scale, fee-paying AUM, fundraising, dry powder, and deployment.
4. Ares's Q2 2026 numbers show that capital demand and deployment were both active at the same time.
5. Ares's credit group data sharpens the private-credit claim: `440.5B USD` of credit AUM, `266.1B USD` of credit FPAUM, and `23.7B USD` of Q2 credit-group deployment make the claim more specific than broad alternatives growth.
6. The strongest shared pattern is not simply "private credit is big." The stronger claim is: `large alternative managers are becoming nonbank capital-routing infrastructure.`

## What The Numbers Do Not Yet Prove

These numbers do not yet prove how much bank lending has been displaced. They show nonbank capacity, investor demand, and deployment, but they need external credit-market comparison before the stronger displacement claim is fully supported.

Missing comparison sources:

- Federal Reserve bank credit and commercial loan data
- FDIC bank lending data
- BDC filings for borrower-level direct-lending activity
- Rating-agency private-credit default and non-accrual data
- Segment-level Ares credit AUM and deployment data
- Apollo/Athene insurance asset allocation and spread-quality detail

## How This Changes The Main Claim

Original broad claim:

`Private credit is replacing part of bank lending.`

Better current claim after pass 1:

`Apollo and Ares show that large alternative managers have enough inflow, origination, dry powder, and deployment scale to function as nonbank credit infrastructure; proving direct bank-lending displacement requires matching those flows against bank credit and borrower-level data.`

Original broad claim:

`Insurance and retirement liabilities are being converted into private-credit origination power.`

Better current claim after pass 1:

`Apollo's origination, inflow, AUM, and spread-related-earnings metrics support the idea that retirement and insurance-linked capital is a major private-credit funding channel, but the next pass needs Athene asset allocation and credit-quality detail to measure how much of the engine is liability-funded.`

## Source Links

- Apollo Q2 2026 results press release: `https://ir.apollo.com/news-events/press-releases/detail/640/apollo-reports-second-quarter-2026-results`
- Apollo financial results archive: `https://ir.apollo.com/financial-results`
- Apollo FY2025 SEC 8-K exhibit: `https://www.sec.gov/Archives/edgar/data/1858681/000185868126000007/erex9914q2025.htm`
- Ares Q2 2026 earnings presentation: `https://ir.ares.com/media/document/222f2520-e378-4363-ab8f-b7dfe8995e3c/assets/Q2-26_Earnings_Presentation_Website_Updated.pdf?disposition=inline`
- Ares financials and SEC filings archive: `https://ir.ares.com/en/financials`

## Next Pass

The next verification pass should do three things:

1. Pull Apollo's Q2 2026 earnings release, supplement, transcript, and 10-Q into local raw storage.
2. Pull Ares's Q2 2026 earnings presentation and 10-Q into local raw storage.
3. Add a primary-source verification table to the ledger schema with `primary_source_url`, `source_document_type`, `source_period`, `source_page_or_section`, and `verification_status`.
