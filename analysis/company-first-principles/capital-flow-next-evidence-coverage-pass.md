# Capital Flow Next Evidence Coverage Pass

## Purpose

This page answers the practical question:

`How do we gather real numbers from annual reports, quarterly reports, and outside data sources, while also letting the actual analysis generate new claims?`

The matrix file is:

`analysis/company-first-principles/data/capital-flow-next-evidence-coverage-matrix.csv`

## The Two-Way Loop

| Direction | What We Do | Output |
|---|---|---|
| Claim to evidence | Start with a claim we want to test, then list the exact numbers and source documents that would prove or disprove it. | A source checklist and acceptance rule. |
| Evidence to claim | Start with extracted numbers, then rewrite the claim so it only says what those numbers prove. | A safer, narrower, more defensible claim. |

This is the operating rule:

`claim -> metric needed -> source -> extraction -> decision -> rewritten claim`

Then reverse it:

`source number -> pattern -> safe claim -> missing proof -> next source`

## Source Hierarchy

| Evidence Strength | Source Type | Use |
|---|---|---|
| Highest | SEC 10-K, 10-Q, 8-K, proxy, debt commitment exhibit, final credit agreement | Borrower financing, use of proceeds, lender roles, segment metrics, risk factors. |
| High | Company quarterly supplement, earnings release, investor deck, shareholder letter | AUM, inflows, deployment, insurance assets, asset allocation, earnings bridge. |
| High but harder to access | NAIC/statutory filings, state insurance exam reports, Bermuda insurer financial statements | Insurance investment schedules, capital and surplus, ratings mix, affiliated assets, statutory quality. |
| Useful independent check | Rating-agency reports, regulator publications, Federal Reserve, FDIC, EIA, FERC, ISO data | Credit quality, capital adequacy, bank denominators, power/grid denominators. |
| Context only | News, law-firm deal notes, sponsor releases | Deal framing and lender identity when primary documents are not yet available. |

## Current Evidence To Claim

| Evidence We Actually Have | Claim It Supports | Claim Boundary |
|---|---|---|
| Apollo/Athene has `17.095B USD` Athene-attributable Q2 2026 inflows, `314.090B USD` net invested assets, `20.396B USD` gross alternative investments, and `877M USD` spread related earnings. | Apollo/Athene has a large retirement-liability and invested-asset engine. | This does not yet show which new liability dollars went into which private-credit borrowers. |
| KKR/Global Atlantic has `220B USD` Global Atlantic AUM and `164B USD` Global Atlantic credit AUM. | KKR has a large insurance-linked credit capital base. | This does not yet separate public credit, private credit, structured credit, and borrower destination. |
| Brookfield Wealth Solutions has `190.715B USD` total insurance assets, `167.297B USD` invested insurance assets, and an investment portfolio allocation of `33%` private credit, `49%` public credit, and `5%` private funds. | Brookfield gives direct evidence that insurance assets are allocated to private credit at scale. | This still needs credit quality, ratings, and borrower/asset-pool details. |
| Blackstone Credit & Insurance has `469.3B USD` AUM, `143.0B USD` LTM inflows, `13.3B USD` direct-lending inflows, `9.9B USD` infrastructure and asset-based credit inflows, and `7.5B USD` insurance SMA inflows. | Blackstone shows third-party insurer money flowing into managed credit strategies. | This is not owned-liability evidence and the local PDF download is blocked by Cloudflare. |
| Ares has `671.319B USD` total AUM, `440.544B USD` Credit Group AUM, and `285.725B USD` of U.S. plus European direct lending AUM. Its U.S. direct lending release shows `8.2B USD` across `69` Q2 transactions and `52.3B USD` across `347` LTM transactions, with selected borrowers in industrial equipment, infrastructure services, automotive service, wealth management, precision manufacturing, insurance brokerage, aerospace MRO, and building maintenance. Follow-through evidence adds Atwell, Precinmac, AeriTek, and Valcourt operating context. Atwell now has a separate bank-replacement pursuit log: `200M USD` 2024 Bank of America-led senior facility, 2026 Ares senior secured acquisition facility role, 2026 Antares first-lien joint-lead-arranger clue, and two KKR-related SEC schedules showing combined disclosed funded-principal-plus-unfunded-commitment Atwell exposure of `8.090M USD`. | Ares gives direct evidence of borrower-facing private-credit origination scale and destination breadth. Atwell adds a concrete prior-bank-to-private-credit test case with reported holder-level debt slices across more than one filing vehicle. | This is not owned-insurance-liability evidence and does not prove bank displacement until a payoff, termination, amendment, rating report, or credit agreement shows what happened to the 2024 bank facility. |
| Auctane/Stamps.com closing 8-K confirms a prior bank-led credit agreement was terminated at close. | Auctane is a primary-source-backed borrower-level bank-facility takeout case. | It does not prove banks had no post-close roles. |
| Medallia acquisition 8-K states approximately `1.8B USD` of debt financing and approximately `5B USD` equity commitment. | Medallia is primary-source-backed for acquisition debt financing amount. | Final lender identity and bank displacement need the credit agreement or debt commitment details. |

## Claim To Evidence

| Stronger Claim | Exact Evidence Required | Decision Rule |
|---|---|---|
| Insurance liabilities are funding private credit. | Same-period liability inflows, invested assets, private-credit allocation, and credit-quality metrics for the insurer. | Promote only when both the liability side and asset-allocation side are visible. |
| Private credit is replacing bank credit. | Borrower documents showing prior bank facility, use of proceeds, new lender group, repayment or termination language, and post-close bank roles. | Make broad claims only after multiple borrower cases or category-matched bank denominator evidence. |
| The credit risk is moving outside banks. | Non-accruals, ratings migration, below-investment-grade exposure, Level 3 or hard-to-value exposure, liquidity terms, and insurer capital adequacy. | Separate risk-location claims from growth claims. Scale alone is not risk proof. |
| Capital is funding productive real-economy assets. | Use-of-proceeds tags, capex/project data, borrower operating metrics, infrastructure MW, backlog, revenue, or installed asset growth. | Do not treat every loan as real-economy investment; distinguish acquisition finance, refinancing, dividend recap, capex, rescue capital, and working capital. |

## Next Evidence Targets

| Priority | Target | Why |
|---|---|---|
| 1 | Apollo/Athene asset allocation and credit quality from Apollo 10-K/10-Q, Athene IR, NAIC/statutory filings, and rating-agency reports. | Apollo has the clearest liability engine, but still needs the asset-quality bridge. |
| 2 | KKR/Global Atlantic insurance balance-sheet detail from KKR 10-Q, Global Atlantic IR, Global Atlantic Re financial statements, and NAIC/statutory filings. | KKR has a large Global Atlantic credit AUM number, but it needs composition and risk detail. |
| 3 | Brookfield Wealth Solutions/AEL credit quality and statutory allocation. | Brookfield has the clearest private-credit allocation percentage, so the next question is quality and borrower destination. |
| 4 | Blackstone insurer-client SMA details. | Blackstone is structurally different: insurer client capital, not owned liabilities. |
| 5 | Borrower documents for Auctane, Medallia, and Guidehouse. | These decide whether the bank-displacement claim is real at the transaction level. |
| 6 | FDIC and category-matched bank denominators. | This decides whether borrower-level takeout is isolated or part of a broader lane shift. |
| 7 | Ares selected direct-lending transaction follow-through. | The Ares release names borrower cases; Atwell is now the top borrower follow-through because it has both prior-bank evidence and later Ares/Antares private-credit evidence. |

## Simple Version

The research should not start by asking:

`Is private credit good or bad?`

It should ask:

`Whose money is this, where did it go, what document proves it, and what would change our mind?`

The current numbers say insurance-linked credit funding is real. The next numbers must show asset quality, borrower destination, and whether specific bank loans were displaced or merely refinanced inside a larger still-growing credit system.

## Source Entry Points

- Athene IR: `https://ir.athene.com/`
- Apollo FY2025 10-K: `https://ir.apollo.com/sec-filings/content/0001858681-26-000013/apo-20251231.htm`
- Global Atlantic IR: `https://www.globalatlantic.com/investor-relations`
- Global Atlantic Re 2025 financial statements: `https://cdn.bma.bm/documents/2026-07-16-21-57-04-Global-Atlantic-Re-Limited-2025-Financial-Statement-Class-3A.pdf`
- Brookfield Wealth Solutions annual reports: `https://bnt.brookfield.com/reports-filings/annual-reports`
- AEL SEC filing: `https://www.sec.gov/Archives/edgar/data/1039828/000103982825000010/angpa-20241231.htm`
- Iowa AEL examination report: `https://iid.iowa.gov/media/817/download`
- NAIC InsData: `https://content.naic.org/industry/insdata`
- NAIC financial statement filing information: `https://content.naic.org/prod_serv_financial_home.htm`
- FDIC Quarterly Banking Profile: `https://www.fdic.gov/analysis/quarterly-banking-profile`
