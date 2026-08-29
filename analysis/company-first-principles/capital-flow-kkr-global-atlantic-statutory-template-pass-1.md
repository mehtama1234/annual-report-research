# Capital Flow KKR Global Atlantic Statutory Template Pass 1

## Purpose

This pass reuses the Apollo/Athene statutory proof architecture for KKR/Global Atlantic.

The question is:

`How do we move KKR/Global Atlantic from insurance balance-sheet and asset-income proxy evidence to legal-entity statutory holdings, Schedule D/BA assets, investment income, borrower allocation, liability cost, and cash-return proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-statutory-template-pass-1.csv`

## Short Answer

KKR/Global Atlantic is now ready for a statutory source-acquisition pass.

The reason is simple:

1. Local KKR evidence already shows a large insurance investment balance sheet.
2. Global Atlantic has an official public financial-statements page with U.S. statutory annual and quarterly statements by legal entity.
3. The Apollo/Athene parser stack gives us a reusable method for Schedule D/BA, income, proceeds, issuer mapping, and named proof chases.

The current proof level remains:

`public-company asset-income and credit-quality proxy; statutory vehicle-to-borrower allocation not yet proven`

## Current Evidence

The local KKR/Global Atlantic evidence already shows:

| Evidence | Value |
|---|---:|
| Global Atlantic AUM | `220B USD` |
| Global Atlantic credit AUM | `164B USD` |
| Ivy and sponsored reinsurance vehicle AUM | `62B USD` |
| insurance investments | `189.204380B USD` |
| insurance policy liabilities | `205.499130B USD` |
| AFS fixed maturities | `88.056662B USD` |
| mortgage and other loan receivables, net | `48.754106B USD` |
| six-month insurance net investment income | `4.028186B USD` |
| six-month fixed-maturity investment income | `3.351757B USD` |
| six-month mortgage/other-loan investment income | `1.541995B USD` |
| mortgage and other loan allowance | `671.094M USD` |
| past-due/foreclosure mortgage loans | `296.4M USD` |
| FHLB pledged assets | `9.2B USD` |

That is materially stronger than AUM-only evidence.

But it still does not identify:

1. statutory legal-entity holdings
2. Schedule D or Schedule BA named assets
3. NAIC designation distribution
4. realized gain/loss and impairment schedules
5. asset-by-asset income
6. borrower/facility allocation
7. FHLB liability economics
8. liability-cost spread
9. final return

## Public Statutory Route

The Global Atlantic financial statements page is the key route:

`https://www.globalatlantic.com/investor-relations/financial-statements`

The page lists U.S. statutory annual and quarterly statements for:

1. Accordia Life and Annuity Company
2. Commonwealth Annuity and Life Insurance Company
3. First Allmerica Financial Life Insurance Company
4. Forethought Life Insurance Company

It also lists Bermuda reinsurer reports for:

1. Global Atlantic Re Limited
2. Global Atlantic Assurance Limited

This matters because Apollo/Athene taught us that the statutory source route is where named CUSIP and asset-income proof can start.

## Apollo/Athene Template To Reuse

The reusable proof architecture is:

1. source acquisition
2. schedule locator
3. compact extraction
4. Schedule D full-range parser
5. reconciliation diagnostic
6. income/cash bridge
7. disposal/proceeds parser
8. same-CUSIP cash-back match
9. proof packet
10. raw-text inspection
11. column review
12. issuer/borrower map
13. named source-acquisition packet
14. controlled-document request packet
15. public document acquisition attempt
16. prototype synthesis

KKR/Global Atlantic should not start from scratch. It should reuse this stack.

## KKR/GA Statutory Template

| Layer | Target Source | What It Must Extract | Promotion Test |
|---|---|---|---|
| official statutory route | Global Atlantic financial statements page | legal entity, period, statement link, local path, extraction target | promote only when PDFs are downloaded and parsed |
| U.S. legal entities | Accordia, Commonwealth, First Allmerica, Forethought | assets, liabilities, capital, investment schedules, Schedule D/BA, income, gains/losses, impairments | promote if at least one entity reaches schedule-located status |
| Bermuda reinsurers | Global Atlantic Re and Global Atlantic Assurance | reinsurance assets/liabilities, funds withheld, investment portfolio, capital, notes | promote if Bermuda reports reconcile to GA reinsurance/funds-withheld economics |
| SEC 10-Q bridge | KKR Q2 2026 10-Q | insurance investments, policy liabilities, asset classes, income, allowances, LTV, FHLB pledged assets | promote only when reconciled to statutory entity schedules |
| Schedule D | fixed maturity holdings | CUSIP, issuer, NAIC designation, value, income, maturity, sale/proceeds rows | promote if named holdings parse and reconcile |
| Schedule BA / other invested assets | alternatives, real assets, affiliated investments | asset name, affiliate status, book/fair value, income, distributions, impairments | promote if named non-fixed-income assets and cash fields are visible |
| income/proceeds/credit quality | statutory income and realized schedules | income, cash/accrual, realized gains/losses, impairments, non-accruals, charge-offs | promote if tied to asset categories and selected issuer rows |
| liability and funding economics | policy liabilities, credited rates, FHLB, funds withheld | liability cost, credited interest, duration, pledged collateral, funding terms | promote if asset income can be compared with liability cost |
| borrower/facility chases | private placements, loans, structured credit | borrower, facility, use, collateral, repayment, trustee/rating reports | promote only with external borrower/facility documents |

## Immediate Download Queue

Start with:

1. Q4 2025 Accordia Life and Annuity Company
2. Q4 2025 Commonwealth Annuity and Life Insurance Company
3. Q4 2025 First Allmerica Financial Life Insurance Company
4. Q4 2025 Forethought Life Insurance Company
5. Q2 2026 versions of those same four entities
6. FY 2025 Global Atlantic Re Limited Bermuda statutory/financial statements
7. FY 2025 Global Atlantic Assurance Limited Bermuda statutory/financial statements
8. FY 2025 Global Atlantic Re Limited Financial Condition Report
9. FY 2025 Global Atlantic Assurance Limited Financial Condition Report

The first useful output should not be a final claim. It should be:

`global-atlantic-statutory-source-acquisition-pass-1`

## What This Would Answer

If the template works, we can answer:

1. Which Global Atlantic legal entity holds which assets?
2. How much fixed maturity, loan, real asset, and other investment exposure sits inside statutory entities?
3. Which named CUSIPs or issuers are visible?
4. What income and proceeds tie to those assets?
5. What NAIC designations and credit-quality markers are visible?
6. What liability or funding cost should be compared with asset income?
7. Which named issuer rows are worth chasing into borrower/facility documents?

## What It Would Not Answer Yet

Even a successful statutory parse would not automatically prove:

1. borrower receipt
2. use of proceeds
3. private-credit origination source
4. cash interest actually received by Global Atlantic
5. trustee remittance
6. FHLB funding economics by asset
7. liability-adjusted spread
8. final asset return

Those require the same controlled documents we found missing in Apollo/Athene:

1. receipts
2. settlement ledgers
3. debt waterfalls
4. collateral certificates
5. borrower financials
6. allocation/custodian records
7. return models

## Safe Claim

`KKR/Global Atlantic is ready for statutory source acquisition. Current local evidence already shows large insurance investments, policy liabilities, fixed maturities, mortgage and other loans, investment income, allowance, past-due/foreclosure, LTV, and FHLB pledged-asset proxy evidence. Global Atlantic's official financial statements page provides public statutory filing routes for four U.S. legal entities and Bermuda reinsurer reports. The Apollo/Athene statutory proof architecture can be reused to move KKR/Global Atlantic from public-company asset-income proxy toward legal-entity Schedule D/BA, income, proceeds, credit-quality, liability-cost, and named issuer proof. This template does not yet prove statutory holdings, borrower allocation, cash receipts, liability spread, or asset-level return.`

## Decision

`kkr-global-atlantic-statutory-template-ready-source-acquisition-next`

The next move is to execute Global Atlantic statutory source acquisition, beginning with the Q4 2025 U.S. statutory annual statements and then the Q2 2026 current-period statements.

## Source Links

- Global Atlantic financial statements page: `https://www.globalatlantic.com/investor-relations/financial-statements`
- KKR Q2 2026 SEC 10-Q: `https://www.sec.gov/Archives/edgar/data/1404912/000140491226000027/kkr-20260630.htm`
- Global Atlantic Re Limited 2025 BMA financial statement route: `https://cdn.bma.bm/documents/2026-07-16-21-57-04-Global-Atlantic-Re-Limited-2025-Financial-Statement-Class-3A.pdf`
