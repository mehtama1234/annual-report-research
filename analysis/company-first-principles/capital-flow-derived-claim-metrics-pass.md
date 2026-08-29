# Capital Flow Derived Claim Metrics Pass

## Purpose

This pass goes from extracted evidence back into claims.

The source extraction files give raw numbers. This page asks what those numbers imply after simple, auditable calculations.

The derived table is:

`analysis/company-first-principles/data/capital-flow-derived-claim-metrics.csv`

## Why This Matters

The research should not only say:

`we found a number`

It should also say:

`this number changes the claim in this specific way`

This pass uses formulas that can be checked by hand. It does not introduce new unsupported facts.

## Derived Metrics

| Platform | Derived Metric | Result | Claim It Supports | Boundary |
|---|---|---:|---|---|
| Apollo / Athene | Selected FY2025 credit-strategy AUM lanes | `675.7B USD` | Apollo has very large disclosed credit-lane scale across direct origination, asset-backed finance, opportunistic credit, and multi-credit. | Not all of this is private credit, and it does not identify borrower-level bank displacement. |
| Apollo / Athene | Direct origination share of selected credit lanes | `44.71%` | Direct origination is the largest selected Apollo credit lane. | The denominator is only the named lanes extracted here. |
| Apollo / Athene | Asset-backed finance share of selected credit lanes | `41.84%` | ABF is almost as large as direct origination in this selected Apollo credit set. | Collateral mix and credit quality still need schedule/rating detail. |
| Apollo / Athene | Athene Accounts fee-generating AUM / Athene Accounts AUM | `98.55%` | Almost all extracted Athene-related account AUM was fee-generating for Apollo. | This is monetizable managed capital, not a fee-rate calculation. |
| Apollo / Athene | Athene Accounts AUM / Apollo total AUM | `41.81%` | Athene-related accounts were a major part of Apollo's FY2025 platform scale. | This does not mean all Athene-related AUM is private credit. |
| Apollo / Athene | Floating-rate liabilities / floating-rate investments | `92.80%` | Athene's floating-rate liabilities offset most of its floating-rate investments. | Rate-offset evidence is not credit-loss evidence. |
| Brookfield Wealth Solutions | Implied private-credit exposure | `55.208B USD` | Brookfield's 33% private-credit allocation implies about 55.2B USD of private-credit exposure on invested insurance assets. | This is derived from disclosed allocation percentage and invested assets; statutory schedules are still needed. |
| Brookfield Wealth Solutions | Implied public-credit exposure | `81.976B USD` | Public credit remains larger than private credit in Brookfield's disclosed insurance portfolio mix. | It does not separate public-credit instrument types. |
| Brookfield Wealth Solutions | Private credit plus private funds | `63.573B USD` | A broad private-asset proxy equals about 63.6B USD. | This is not the same as a statutory Schedule BA extraction. |
| Brookfield Wealth Solutions | FY2025 total investments / total assets | `73.06%` | The annual filing shows most of the balance sheet is invested assets. | This is annual balance-sheet mix, not private-credit allocation. |
| Brookfield Wealth Solutions | FY2025 policyholder balances / total assets | `59.16%` | Policyholder balances are a major liability source behind the platform. | It does not tie a specific liability dollar to a specific loan. |
| Brookfield Wealth Solutions | FY2025 unfunded commitments / total investments | `10.71%` | The 20-F adds a visible forward-deployment queue. | Commitments are not funded assets yet. |
| KKR / Global Atlantic | Global Atlantic credit AUM / Global Atlantic AUM | `74.55%` | KKR's insurance platform is heavily credit-oriented. | This does not separate public and private credit. |
| KKR / Global Atlantic | Global Atlantic AUM / KKR total AUM | `27.64%` | Global Atlantic is a large part of KKR's total platform scale. | It is platform context, not private-credit destination proof. |
| KKR / Global Atlantic | Mortgage and other loan receivables / insurance investments | `25.77%` | Loans are a large insurance investment category at Global Atlantic. | The bucket includes mortgage, consumer, and other loans, not only corporate private credit. |
| KKR / Global Atlantic | Mortgage loans 90 days or more past due or in foreclosure / total mortgage loans | `0.66%` | The 10-Q adds a concrete credit-quality denominator to the Global Atlantic analysis. | This is not a full default forecast and does not include consumer-loan risk. |
| KKR / Global Atlantic | FHLB pledged assets / insurance investments | `4.86%` | Global Atlantic still interacts with bank-adjacent funding channels. | This is the opposite of a bank-free claim. |
| KKR | LTM capital invested / LTM new capital raised | `78.20%` | KKR is deploying capital at high scale relative to capital formation. | It does not show same-dollar matching or strategy destination. |
| Blackstone Credit & Insurance | Credit & Insurance AUM / total Blackstone AUM | `34.86%` | Credit & Insurance is about one-third of Blackstone AUM. | This is not owned insurance liability evidence. |
| Blackstone Credit & Insurance | Direct-lending inflows / segment quarterly inflows | `42.90%` | Direct lending was a major Q2 2026 inflow bucket. | It is a one-quarter flow mix, not a balance-sheet allocation. |
| Blackstone Credit & Insurance | Insurance SMA inflows / infrastructure and ABF inflows | `75.76%` | Insurance SMAs drove most of the cited infrastructure and asset-based credit inflow bucket. | It proves insurer-client capital importance, not Blackstone insurance liability ownership. |
| Blackstone Credit & Insurance | LTM capital deployed / LTM inflows | `45.73%` | LTM deployment was meaningful but materially below LTM inflows. | This does not mean the remaining inflows are idle or permanent. |
| Ares | Credit Group AUM / total AUM | `65.62%` | Ares is mainly a credit platform by AUM. | This does not mean all credit AUM is direct lending or private credit. |
| Ares | U.S. plus European direct lending AUM | `285.725B USD` | Direct lending is a very large Ares credit lane. | It does not identify individual borrower use of proceeds. |
| Ares | U.S. plus European direct lending / Credit Group AUM | `64.86%` | Direct lending is roughly two-thirds of Ares Credit Group AUM. | This is a strategy mix ratio, not a bank-displacement ratio. |
| Ares | Credit new commitments / total new commitments | `65.03%` | Credit drove about two-thirds of Q2 2026 new commitments. | Commitments are not the same as funded deployment. |
| Ares | Credit FPAUM deployment / total FPAUM deployment | `70.16%` | Credit drove most Q2 2026 fee-paying deployment/increase in leverage. | This is a FPAUM rollforward metric, not a direct borrower-originations table. |

## Claims That Get Stronger

| Claim | Why Stronger |
|---|---|
| Insurance-linked credit channels are real. | Apollo/Athene, KKR/Global Atlantic, Brookfield, and Blackstone each show a measurable insurance-linked or insurer-client credit channel. |
| KKR now has balance-sheet depth, not only AUM. | The SEC 10-Q adds insurance investments, policy liabilities, loan receivables, net investment income, credit allowances, mortgage-loan performance, and FHLB pledged collateral. |
| Brookfield is the clearest allocation case so far. | Its disclosed `33%` private-credit allocation can be converted into an implied `55.208B USD` private-credit exposure; the FY2025 20-F adds annual balance-sheet scale with `157.181B USD` of assets, `114.833B USD` of investments, and `92.992B USD` of policyholder account balances. |
| Blackstone is structurally different from Apollo/KKR/Brookfield. | The derived insurance-SMA shares show insurer-client capital inside managed strategies, not owned-liability capital. |
| Apollo/Athene is a credit-and-spread system. | Athene-related accounts are large and almost entirely fee-generating, while Apollo's selected credit lanes are very large. |
| Ares strengthens the direct-lending destination claim. | Its Credit Group is `65.62%` of total AUM, U.S. plus European direct lending totals `285.725B USD`, and official direct-lending origination disclosure identifies `8.2B USD` of Q2 commitments across `69` transactions. |

## Claims That Stay Unproven

| Claim | Why Still Unproven |
|---|---|
| Private credit is broadly replacing banks. | The derived metrics show nonbank capacity and insurer funding channels, but not category-matched bank share loss. |
| Insurance liabilities directly fund named private-credit loans. | We still need asset-pool or statutory schedules connecting liabilities to holdings. |
| Every Ares direct-lending transaction displaced a bank loan. | Ares' direct-lending release identifies commitments and borrowers but not prior facility repayment, full lender group, or post-close bank roles. |
| The credit risk is safe. | We need independent rating-agency reports, statutory filings, impairments, non-accruals, and capital adequacy. |
| The capital is productive real-economy investment. | We need borrower use-of-proceeds tags and operating outcomes. |

## Simple Version

The numbers are now saying:

`This is not just fundraising. These platforms are building large credit-routing systems fed by retirement liabilities, insurance balance sheets, and insurer-client accounts.`

But the numbers are also saying:

`Do not overclaim bank displacement yet. The current evidence proves capacity, flows, allocation, and structure. Bank displacement still requires borrower documents and bank denominator comparisons.`

## Next Best Question

The next high-value question is:

`Which of these derived ratios can be repeated over multiple quarters or years?`

That turns one-period evidence into a trend:

| Ratio | Next Trend Test |
|---|---|
| Brookfield implied private-credit exposure | Recalculate every quarter from invested insurance assets and allocation percent. |
| Brookfield annual investment and liability ratios | Recalculate from each 20-F and reconcile to quarterly supplement invested insurance assets. |
| KKR Global Atlantic credit AUM / Global Atlantic AUM | Track whether Global Atlantic is becoming more or less credit-heavy. |
| Blackstone insurance SMA inflows / Credit & Insurance inflows | Track whether insurer-client capital is becoming a larger share of inflows. |
| Apollo Athene Accounts AUM / Apollo total AUM | Track whether Athene remains a major share of Apollo scale. |
| Apollo floating-rate offset ratio | Track rate-risk management through rate cycles. |
