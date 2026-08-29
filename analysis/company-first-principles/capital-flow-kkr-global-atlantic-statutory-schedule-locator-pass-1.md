# Capital Flow KKR Global Atlantic Statutory Schedule Locator Pass 1

## Purpose

This pass converts the `10` locally acquired Global Atlantic statutory PDFs into targeted extraction maps.

It asks:

`Where inside the Global Atlantic legal-entity filings are the schedules needed to test assets, liabilities, investment income, cash flow, named holdings, proceeds, funds-withheld/reinsurance economics, and Bermuda investment context?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-schedule-locator-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-schedule-locator-diagnostic-pass-1.csv`

The upstream source acquisition pass is:

`/cluster/capital-flow-kkr-global-atlantic-statutory-source-acquisition-pass-1.md`

## Short Answer

`The Global Atlantic statutory source set is now extraction-ready. The locator probes 10 local PDFs, covering 38 targeted pages out of 1226 available PDF pages, and creates 38 locator rows, including 9 Schedule D rows, 0 Schedule BA rows, and 8 cash/income rows. This locates the proof zones but does not yet parse holdings, income, proceeds, liability spread, or named cash return.`

## Main Result

| Metric | Value |
|---|---:|
| PDFs scanned | 10 |
| PDF pages available | 1226 |
| Targeted pages probed | 38 |
| Locator rows | 38 |
| Annual locator rows | 26 |
| Quarterly locator rows | 4 |
| Bermuda locator rows | 8 |
| Schedule D locator rows | 9 |
| Schedule BA locator rows | 0 |
| Cash/income locator rows | 8 |
| Full named cash proof upgrades | 0 |

## Key Located Targets

| ID | Legal Entity | Period | Target | Pages | Status |
|---|---|---|---|---|---|
| CFKKRGASL-005 | Accordia Life and Annuity Company | Q4 2025 | assets page | 3 | page-located |
| CFKKRGASL-006 | Accordia Life and Annuity Company | Q4 2025 | liabilities surplus and other funds | 4 | page-located |
| CFKKRGASL-007 | Accordia Life and Annuity Company | Q4 2025 | summary of operations | 5 | page-located |
| CFKKRGASL-008 | Accordia Life and Annuity Company | Q4 2025 | cash flow | 6 | page-located |
| CFKKRGASL-009 | Accordia Life and Annuity Company | Q4 2025 | exhibit of net investment income | 15 | page-located |
| CFKKRGASL-010 | Accordia Life and Annuity Company | Q4 2025 | Schedule D Part 1A quality and maturity | 130;135 | range-located |
| CFKKRGASL-013 | Accordia Life and Annuity Company | Q4 2025 | Schedule D long-term bonds owned | 220-245 | range-located |
| CFKKRGASL-014 | Accordia Life and Annuity Company | Q4 2025 | Schedule D acquired during year | 250-255 | range-located |
| CFKKRGASL-015 | Accordia Life and Annuity Company | Q4 2025 | Schedule D disposed during year | 260-265 | range-located |
| CFKKRGASL-019 | Commonwealth Annuity and Life Insurance Company | Q4 2025 | Schedule S funds withheld and reinsurance | 120 | page-located |
| CFKKRGASL-020 | Commonwealth Annuity and Life Insurance Company | Q4 2025 | Schedule D Part 1A quality and maturity | 160 | page-located |
| CFKKRGASL-023 | First Allmerica Financial Life Insurance Company | Q4 2025 | exhibit of net investment income | 18 | page-located |
| CFKKRGASL-024 | First Allmerica Financial Life Insurance Company | Q4 2025 | Schedule D Part 1A quality and maturity | 150 | page-located |
| CFKKRGASL-027 | Forethought Life Insurance Company | Q4 2025 | exhibit of net investment income | 18 | page-located |
| CFKKRGASL-029 | Forethought Life Insurance Company | Q4 2025 | Schedule D Part 1A quality and maturity | 140 | page-located |
| CFKKRGASL-031 | Global Atlantic Re Limited | FY 2025 | Bermuda balance sheet | 2-5 | range-located |
| CFKKRGASL-032 | Global Atlantic Re Limited | FY 2025 | Bermuda income statement | 6-7 | range-located |
| CFKKRGASL-034 | Global Atlantic Re Limited | FY 2025 | Bermuda investment note | 10-15 | range-located |
| CFKKRGASL-035 | Global Atlantic Assurance Limited | FY 2025 | Bermuda balance sheet | 2-5 | range-located |
| CFKKRGASL-036 | Global Atlantic Assurance Limited | FY 2025 | Bermuda income statement | 6-7 | range-located |
| CFKKRGASL-038 | Global Atlantic Assurance Limited | FY 2025 | Bermuda investment note | 10-15;20 | range-located |

## Proof Effect

This pass moves KKR/Global Atlantic from local source acquisition to targeted extraction readiness. It shows where to extract the legal-entity balance sheet, liabilities, summary operations, cash flow, net investment income, Schedule D, Schedule BA, Schedule S/funds-withheld, Schedule E, and Bermuda investment-note zones.

## Boundary

This pass is still a locator, not a parser.

It does not prove named Schedule D/BA holdings, NAIC designations, borrower allocation, cash receipts, liability-cost spread, funds-withheld economics, FHLB liability economics, debt waterfalls, collateral certificates, or asset-level return.

## Next Action

Run `global-atlantic-statutory-compact-extraction` against the located pages, starting with the four Q4 `2025` U.S. annual statements and then the Q2 `2026` quarterlies and FY `2025` Bermuda financials.

## Decision

`kkr-global-atlantic-statutory-schedule-locator-ready-compact-extraction-next`

## Safe Claim

`The locally acquired Global Atlantic statutory filing set is schedule-located and ready for targeted extraction. The current locator identifies the pages and ranges needed for legal-entity assets, liabilities, cash flow, net investment income, Schedule D/BA, funds-withheld/reinsurance, Schedule E, and Bermuda investment context. It does not yet prove issuer-level holdings, investment income by holding, liability-cost spread, borrower destination, realized cash return, or asset-level return.`
