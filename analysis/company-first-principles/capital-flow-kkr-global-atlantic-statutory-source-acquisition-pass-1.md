# Capital Flow KKR Global Atlantic Statutory Source Acquisition Pass 1

## Purpose

This pass executes the KKR/Global Atlantic statutory source route identified in the statutory template.

The goal is to acquire the filings needed to test the insurance-capital money chain:

`KKR / Global Atlantic -> insurance legal entity -> statutory assets and liabilities -> Schedule D/BA holdings -> investment income/proceeds -> named issuer cash-back hold/pass`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-source-acquisition-diagnostic-pass-1.csv`

## Source Route

Global Atlantic's official financial-statement page lists U.S. statutory annual and quarterly statements for Accordia Life and Annuity Company, Commonwealth Annuity and Life Insurance Company, First Allmerica Financial Life Insurance Company, and Forethought Life Insurance Company. It also lists Bermuda reinsurer financial information for Global Atlantic Re Limited and Global Atlantic Assurance Limited.

Source index:

`https://www.globalatlantic.com/investor-relations/financial-statements`

## Main Result

| Metric | Value |
|---|---:|
| Source acquisition rows | 10 |
| U.S. statutory legal entities targeted | 4 |
| Q4 2025 U.S. annual statements targeted | 4 |
| Q2 2026 U.S. quarterlies targeted | 4 |
| FY 2025 Bermuda reports targeted | 2 |
| Downloaded local files | 10 |
| Download holds | 0 |
| Largest file size bytes | 8644493 |
| Full named cash proof upgrades | 0 |

## Acquisition Rows

| ID | Legal Entity | Period | Status | Bytes |
|---|---|---|---|---:|
| CFKKRGASA-001 | Accordia Life and Annuity Company | Q2 2026 | downloaded-local-extraction-pending | 1047094 |
| CFKKRGASA-002 | Commonwealth Annuity and Life Insurance Company | Q2 2026 | downloaded-local-extraction-pending | 1037821 |
| CFKKRGASA-003 | First Allmerica Financial Life Insurance Company | Q2 2026 | downloaded-local-extraction-pending | 1002674 |
| CFKKRGASA-004 | Forethought Life Insurance Company | Q2 2026 | downloaded-local-extraction-pending | 1045900 |
| CFKKRGASA-005 | Accordia Life and Annuity Company | Q4 2025 | downloaded-local-extraction-pending | 8644493 |
| CFKKRGASA-006 | Commonwealth Annuity and Life Insurance Company | Q4 2025 | downloaded-local-extraction-pending | 2657944 |
| CFKKRGASA-007 | First Allmerica Financial Life Insurance Company | Q4 2025 | downloaded-local-extraction-pending | 2452264 |
| CFKKRGASA-008 | Forethought Life Insurance Company | Q4 2025 | downloaded-local-extraction-pending | 2295673 |
| CFKKRGASA-009 | Global Atlantic Re Limited | FY 2025 | downloaded-local-extraction-pending | 387259 |
| CFKKRGASA-010 | Global Atlantic Assurance Limited | FY 2025 | downloaded-local-extraction-pending | 359187 |

## Proof Effect

This pass moves KKR/Global Atlantic from statutory-template planning to source-file acquisition. The filings are the document family needed to chase named holdings, legal-entity investment income, sale/maturity/proceeds fields, liability source context, FHLB/funds-withheld economics, and Schedule D/BA borrower allocation.

## Boundary

This pass does not yet parse the Global Atlantic statutory statements.

It does not prove named Schedule D/BA holdings, NAIC designations, borrower allocation, cash receipts, liability-cost spread, FHLB liability economics, debt waterfalls, collateral certificates, or asset-level return.

## Next Action

Run `global-atlantic-statutory-schedule-locator` across the acquired files, then adapt the Apollo/Athene Schedule D/BA parser and legal-entity income bridge.

## Decision

`kkr-global-atlantic-statutory-source-acquisition-local-files-acquired-schedule-locator-next`
