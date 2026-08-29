# Capital Flow Apollo Athene Statutory Source Acquisition Pass 1

## Purpose

This pass executes the second ranked row from the big-money platform source acquisition queue:

`Apollo / Athene legal-entity asset-income case.`

It asks:

`Can the Apollo/Athene insurance-liability channel move from channel-level spread evidence to legal-entity statutory source acquisition?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-source-acquisition-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-big-money-platform-source-acquisition-queue-pass-1.md`

## Short Answer

`Partial upgrade. Apollo/Athene does not yet reach statutory asset-income proof, but the source route is now stronger than before because an official Athene statutory filing page is public and one large year-end 2025 Athene Annuity and Life Company statutory statement has been downloaded locally. The acquired PDF is about 212 MB and 9,612 pages, so the next step is a targeted Schedule D/BA and investment-income extraction strategy, not a blind full-file text scan.`

## Acquired Source

| Source | Local Path | Status | What It Adds | Boundary |
|---|---|---|---|---|
| Fourth Quarter `2025` Statutory Financial Statement for Athene Annuity and Life Company | `raw/primary-sources/capital-flow/apollo/athene/statutory/2025/athene-annuity-and-life-company-2025-statutory-statement.pdf` | `downloaded-local` | Gives a real legal-entity statutory filing to attack for Schedule D/BA, admitted assets, liabilities, investment schedules, income, gains/losses, and capital/surplus. | Not yet parsed into holdings, NAIC designations, investment income, realized gains/losses, impairment, liability cost, borrower allocation, or spread bridge. |

## Public Routes Checked

| Route | Result | Proof Effect | Boundary |
|---|---|---|---|
| Athene statutory filings page | Current public route lists `2026`, `2025`, and prior statutory filing links, including Athene Life Re Ltd., Athene Annuity and Life Company, Athene Annuity & Life Assurance Company of New York, ALIRT exhibits, and separate-account statements. | Confirms official recurring statutory filing source route. | Route visibility is not extraction. |
| Athene Annuity and Life Company year-end `2025` PDF | HEAD check returned reachable PDF with about `221,368,204` bytes; file was downloaded locally as a `212M` PDF. | Converts the Athene statutory path from route-visible to local-source-acquired for one core legal entity. | It is too large for naive whole-file extraction. |
| Athene Life Re Ltd. year-end `2025` CloudFront route | Browser/search route exists, but direct HEAD attempt returned `403` in this environment. | Identifies a second important legal-entity route. | Not locally acquired in this pass. |
| Bermuda Monetary Authority Athene Bermuda `2025` financial statement | Public search route exposes audited Athene Bermuda group financial statements. | Useful secondary route for Bermuda statutory/financial context. | Not the same as U.S. Schedule D/BA extraction. |
| Athene SEC 10-K route | SEC route remains available for consolidated disclosures and statutory discussion. | Supports bridge to Apollo/Athene consolidated reporting. | SEC 10-K is not legal-entity statutory holdings detail. |
| Current local Apollo/Athene evidence | Existing extraction already shows Q2 `2026` inflows, invested assets, alternative investments, direct-origination AUM, ABF AUM, Athene Accounts AUM, and spread-related earnings. | Confirms why this is a high-value source acquisition target. | Still not statutory asset-income proof. |

## What This Changes

Before this pass, Apollo/Athene statutory proof was mainly a route and request:

`pull Athene statutory filings`

After this pass, one core legal-entity statement is local:

`Athene Annuity and Life Company 2025 statutory statement -> local 212M PDF -> 9,612-page extraction target`

That is a real improvement, but it is not enough to answer the cash question. The cash question requires extracting and joining:

1. legal-entity admitted asset base
2. Schedule D bond/loan holdings
3. Schedule BA alternative/other invested assets
4. NAIC designations and ratings
5. statutory investment income
6. realized gains/losses
7. impairments or credit losses
8. liabilities, credited interest, surrender or reserve cost
9. spread by legal entity or asset class
10. borrower or asset destination where schedules expose names

## Extraction Boundary

The acquired PDF is not practical for blind full-file text extraction inside the interactive pass. A lightweight `pypdf` check confirmed `9,612` pages before the scan was stopped. The next extraction should use a targeted approach:

1. build a PDF outline/table-of-contents locator if available
2. find page ranges for Schedule D, Schedule BA, investment income, liabilities, and capital/surplus
3. extract only those ranges into text or CSV
4. normalize holdings by issuer/CUSIP, book value, fair value, affiliate status, and NAIC designation
5. summarize asset-income and liability-cost bridge separately from holdings

## Decision

`apollo-athene-statutory-source-acquisition-partial-local-source-acquired-extraction-pending`

Apollo/Athene improves from statutory-route-visible to one core statutory source acquired locally. It remains below statutory cash-return proof until Schedule D/BA, investment income, liability-cost, credit-quality, and spread data are extracted.

## Safe Claim

`Apollo/Athene now has a local statutory source for one core Athene legal entity: the year-end 2025 Athene Annuity and Life Company statutory statement. This supports the next extraction step toward legal-entity holdings and statutory asset-income proof. It does not yet prove Schedule D/BA holdings, NAIC designations, investment income by asset class, realized gains/losses, impairments, liability-cost spread, borrower destination, or asset-level cash return.`

## Next Work

1. Build a targeted parser or page-range locator for the `9,612` page Athene statutory statement.
2. Extract Schedule D and Schedule BA headings/page ranges first.
3. Extract legal-entity balance sheet, summary investment schedule, net investment income exhibit, realized gains/losses, capital/surplus, and liability/reserve pages.
4. Only after extraction, attempt borrower/issuer matching to private-credit or ABF destinations.
