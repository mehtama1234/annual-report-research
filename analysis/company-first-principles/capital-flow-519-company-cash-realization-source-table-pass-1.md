# Capital Flow 519-Company Cash-Realization Source Table Pass 1

## Purpose

This page takes the `35` company cash-realization batch and asks the next concrete question:

`Which pilot companies already have local, source-backed cash-realization or cash-proxy evidence, and which are still only queued?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-519-company-cash-realization-source-table-pass-1.csv`

The upstream batch design is:

`/cluster/capital-flow-519-company-cash-realization-batch-pass-1.md`

The denominator control pass is:

`/cluster/capital-flow-519-company-denominator-control-pass-1.md`

The first queued-lane source/denominator upgrade is:

`/cluster/capital-flow-debt-refinancing-sec-source-denominator-pass-1.md`

## Current Answer

`The source-table pass now has 35 rows. After the debt/refinancing and Wheaton IFRS upgrades, it moves 16 pilot companies out of generic queued status and leaves 19 as explicit queued rows. Within the non-queued set, 8 are pass-with-boundary, 5 are SEC denominator-started, 1 is a source/use/cash hold, and 2 are cash-allocation holds. The strongest evidence is still bounded: the pilot shows platform cash proxies, borrower-holder destinations, regulated recovery, tariff/route economics, capex/output/cash proxies, debt/cash-flow denominators, and backlog/cash conversion, but not asset-level cash returns across the full 35-company batch.`

## Coverage

| Status | Rows | Meaning |
|---|---:|---|
| `pass-with-boundary` | `8` | Source-backed cash, recovery, tariff, output, or backlog proxy is visible, but asset-level cash return is still limited. |
| `source-visible-denominator-started` | `5` | SEC cash, debt, operating cash flow, proceeds, repayments, dividend, repurchase, or stream-acquisition denominators are visible, but use and return remain open. |
| `hold-source-use-cash-open` | `1` | Borrower-destination evidence is strong, but source/use/cash proof is not yet visible. |
| `hold-cash-allocation-open` | `2` | Platform or vehicle source stack is visible, but allocation to a named asset or borrower is open. |
| `queued-open` | `19` | The company remains in the pilot queue without local cash-realization extraction in this pass. |

## Best Current Evidence

| Company | Current Source-Visible Answer | Boundary |
|---|---|---|
| KKR | Insurance/credit platform and BDC/private-credit borrower-holder channel evidence is visible. | Not proof that KKR platform cash or insurance liabilities funded a named borrower or returned borrower cash. |
| Apollo | Athene channel has Q2 `2026` inflows, net invested assets, alternative investments, and spread-related earnings. | Not asset-level statutory cash return. |
| Ares | Named borrower-holder evidence is visible across the same-period borrower table. | Not source-of-funds or borrower cash realization. |
| Blackstone | Credit vehicle and platform source-stack evidence is visible. | Not proof that Blackstone platform capital funded a specific pilot-company use or cash return. |
| ONEOK | Same-period capex, adjusted EBITDA, segment output, and demand cues are visible. | Not named-project return. |
| MasTec | Backlog, revenue, adjusted EBITDA, operating cash flow, capex, and contract liabilities are visible. | Not project-owner funding or project cash collection. |
| Plains | Tariff route, effective date, and cents-per-barrel base rate are visible. | Not committed volume, shipper identity, or realized revenue. |
| Targa | Growth capex, completed projects, EBITDA, liquidity, and output categories are visible. | Not project-level contribution. |
| NextEra / FPL | Regulatory recovery authority, aggregate SPPCRC revenue, Distribution Inspection cost/output, and capital-structure support are visible. | Not Distribution Inspection-specific customer receipts or funding source. |
| PBF Energy | Q2 `2026` SEC cash, debt, operating cash flow, capex, and repayment denominators are visible. | Not refinancing use-of-proceeds or refinery-level cash return. |
| Devon Energy | Q2 `2026` SEC cash, debt, operating cash flow, repayment, dividend, and repurchase denominators are visible. | Not allocation of debt changes to capex, acquisitions, refinancing, or shareholder returns. |
| Matador Resources | Q2 `2026` SEC cash, debt, secured/unsecured proceeds, repayments, and operating cash flow are visible. | Not borrowing-base cushion, acquisition funding, or well-level cash conversion. |
| Liberty Broadband | Q2 `2026` SEC holding-company cash, debt, debt proceeds/repayments, and continuing-operations cash flow are visible. | Not collateral sufficiency, exchangeable-debt economics, or shareholder cash realization. |
| Wheaton Precious Metals | Q2 `2026` SEC/IFRS tables show sales, operating cash flow, cash, bank debt, term-loan debt, revolver debt, bank debt draw/repayment, and BHP Antamina PMPA funding context. | Not stream-level return, PMPA cash margin, mine delivery timing, debt-service waterfall, or lender allocation. |
| Energy Transfer | Q2 `2026` adjusted EBITDA, DCF, growth capex, output growth, expansion capacity, revolver availability, and debt are visible. | Not named-project source/use/return. |
| Sterling | RPO/backlog growth, net contract liability timing, OCF less capex, and July `2026` revolver/L/C capacity are visible. | Not project-owner funding, L/C usage, bonded backlog, or project margin. |

## What This Adds

The prior batch answered:

`What should we extract?`

This source table answers:

`What do we already have enough local evidence to say?`

It prevents three overclaims:

- platform AUM or invested assets becoming borrower cash
- backlog or capex becoming realized return
- regulatory recovery or tariff authority becoming category-level customer receipts

## Decision

`519-company-cash-realization-source-table-ready`

The first `35` company pilot now has a server-visible source table that separates source-backed cash/proxy evidence from open queue rows.

## Safe Claim

`The 35-company pilot has first-pass cash-realization source coverage: 16 companies have moved out of generic queued status. All 16 have source-visible metrics, denominators, or source-stack holds, while 19 remain queued. This supports a disciplined evidence map, not a claim that the 35-company pilot or the full 519-company universe is cash-realization proven.`

## Next Work

1. Upgrade the `queued-open` rows by lane, starting with debt/refinancing and acquisition-finance companies.
2. For source-visible rows, replace proxy status with hard cash realization only when source/use/output/cash and allocation are in the same-period evidence chain.
3. Use the denominator-control pass to add same-period numerator/denominator pairs where available, without mixing platform, vehicle, asset, and cash metrics.
