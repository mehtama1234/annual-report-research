# Capital Flow Debt Refinancing Bridge Upgrade Queue Pass 1

## Purpose

This page converts the completed five-company debt/refinancing bridge lane into an executable source and extraction queue.

The question is:

`What exact documents and fields are needed to move each debt/refinancing bridge from company- or facility-level mechanism evidence toward asset-level return, cash-realization, or disproof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.csv`

The upstream frontier is:

`/cluster/capital-flow-debt-refinancing-use-return-frontier-pass-1.md`

## Current Answer

`The five debt/refinancing bridges are ready for targeted upgrade work, but none should be promoted to asset-level return yet. The next evidence should be specific: Wheaton needs Antamina delivery/cash receipt and debt-service evidence; Matador needs source-to-specific-use, reserve/collateral, asset cash, and debt-service evidence; Liberty Broadband needs margin-loan LTV, Charter loan terms, debenture settlement economics, and final merger funds-flow; PBF needs ABL availability, note economics, insurance-normalized cash flow, and refinery-level output/cash evidence; Devon needs treasury funds-flow, realized Coterra synergy, Permian lease development/cash, and debt/payout sustainability evidence.`

The first Matador queue row has now been executed:

`/cluster/capital-flow-matador-source-specific-use-allocation-pass-1.md`

Result:

`aggregate-timing-source-use-reconciliation-visible`

The pass reconciles Matador's first-half source/use envelope but holds source-specific allocation open.

The first Devon queue row has also been executed:

`/cluster/capital-flow-devon-treasury-funds-flow-pass-1.md`

Result:

`treasury-funds-flow-reconciliation-visible-statement-level`

The pass reconciles Devon's first-half cash source/use envelope while keeping non-cash merger stock consideration, assumed debt, and exchange offers outside the cash-flow total.

The Wheaton Antamina PMPA economics row has also been executed:

`/cluster/capital-flow-wheaton-antamina-pmpa-economics-pass-1.md`

Result:

`pmpa-economics-proxy-visible-return-model-incomplete`

The pass upgrades Wheaton from company-level source/use/output terms to stream-level PMPA economics proxy evidence. It ties the `4.300B USD` Antamina PMPA cash outflow and `67.50%` payable-production / `20.00%` delivery-payment terms to H1 `2026` Antamina revenue of `277.563M USD`, cost of sales excluding depletion of `55.340M USD`, depletion of `51.322M USD`, profit of `170.901M USD`, operating cash flow of `222.223M USD`, and assets of `4.708329B USD`, while keeping full PMPA return proof open.

The Wheaton Antamina tax/depletion/interest allocation row has also been executed:

`/cluster/capital-flow-wheaton-antamina-net-cash-return-pass-1.md`

Result:

`net-cash-return-proxy-visible-tax-interest-allocation-incomplete`

The pass upgrades Wheaton from gross PMPA economics to a bounded pre-tax, pre-interest net cash-return proxy. It shows H1 `2026` Antamina operating cash flow of `222.223M USD`, depletion of `51.322M USD`, profit after depletion of `170.901M USD`, assets of `4.708329B USD`, company-level finance costs of `32.502M USD`, company-level income tax expense of `210.876M USD`, and a mechanical annualized OCF/upfront-payment proxy of `10.336%`, while keeping Antamina-specific tax, interest, debt-service, lender allocation, IRR, NPV, and full PMPA return proof open.

The first PBF note-economics row has also been executed:

`/cluster/capital-flow-pbf-note-refinancing-economics-pass-1.md`

Result:

`note-refinancing-mechanics-visible-benefit-not-proven`

The pass measures PBF's 2028-to-2034 note refinancing mechanics, including `500.0M USD` of new 2034 notes, `492.1M USD` of net proceeds, `801.6M USD` of redeemed 2028 notes, `301.6M USD` of gross senior-note principal reduction, and about `11.846M USD` of simple annual coupon relief, while keeping total refinancing value creation open.

The PBF insurance-normalized cash-flow row has also been executed:

`/cluster/capital-flow-pbf-insurance-normalized-cash-flow-pass-1.md`

Result:

`insurance-normalized-company-cash-proxy-visible-recurring-refinery-return-unproven`

The pass measures PBF's reported first-half operating cash flow of `1.2651B USD`, separates `111.3M USD` of operating insurance proceeds and `245.2M USD` of investing insurance proceeds, and calculates a conservative `1.1538B USD` company-level operating-cash proxy after removing operating insurance proceeds. It supports debt-service and capital-use comparison while keeping recurring refinery-level return open.

The first Liberty Broadband settlement-economics row has also been executed:

`/cluster/capital-flow-liberty-debenture-settlement-economics-pass-1.md`

Result:

`debenture-retirement-mechanics-visible-settlement-economics-incomplete`

The pass measures Liberty Broadband's 2053 exchangeable-debenture retirement mechanics, including `966M USD` paid to retire all outstanding 2053 debentures, funding from Margin Loan Facility proceeds and restricted cash, a `523M USD` total-debt reduction, `19.1M` Charter collateral shares with `2.7B USD` disclosed collateral-account value, and a `359M USD` LTV-triggered Charter loan, while keeping settlement value creation and shareholder realization open.

The Matador debt-service quality row has also been executed:

`/cluster/capital-flow-matador-debt-service-quality-pass-1.md`

Result:

`debt-service-quality-proxy-visible-pricing-cushion-incomplete`

The pass measures Matador's borrowing-base and note-refinancing quality at proxy level, including `3.25B USD` borrowing base, `2.75B USD` elected commitments, `939M USD` Credit Agreement borrowings, `53.8M USD` letters of credit, about `1.7572B USD` simple unused elected commitment after LCs, covenant thresholds and compliance, `112.344M USD` first-half interest expense, and a 2028-to-2034 note refinancing that lowered coupon rate but increased simple annual coupon dollars by about `10.625M USD`.

The Devon debt/payout sustainability row has also been executed:

`/cluster/capital-flow-devon-debt-payout-sustainability-pass-1.md`

Result:

`debt-payout-sustainability-proxy-visible-full-cycle-not-proven`

The pass measures Devon's same-period debt and shareholder-return coverage: `5.329B USD` first-half OCF, `2.157B USD` capex, a `3.172B USD` simple post-capex cash proxy, `521M USD` dividends, `266M USD` buybacks, `500M USD` debt repayments, `262M USD` interest based on debt outstanding, `4.0B USD` liquidity, no quarter-end revolver or commercial-paper borrowings, and `18.1%` funded-debt-to-capitalization versus a `65%` covenant limit. It supports proxy-grade same-period resilience, not full-cycle payout sustainability.

## Queue Summary

| Company | Rows | Current Bridge | Next Upgrade Test |
|---|---:|---|---|
| Wheaton Precious Metals | `4` | Company-level Antamina stream funding | Antamina-specific delivery, cash receipt, PMPA economics, and debt-service allocation. |
| Matador Resources | `4` | Borrowing-base source/use/output bridge | Source-to-specific-use, reserve/collateral, asset output/cash, and debt-service quality. |
| Liberty Broadband | `4` | Holdco collateral restructuring | LTV/collateral cushion, Charter loan terms, debenture economics, and final merger funds-flow. |
| PBF Energy | `4` | Refining liquidity bridge | ABL availability, note refinancing economics, normalized cash flow, and refinery-level output/cash. |
| Devon Energy | `4` | Merger-period allocation bridge | Treasury funds-flow, realized synergy, Permian lease return, and debt/payout sustainability. |

## Highest-Leverage Immediate Actions

| Priority | Case | Action | Why |
|---:|---|---|---|
| 1 | Wheaton Antamina | Fetch next-period delivery and cash-receipt evidence. | Best chance to upgrade from funded PMPA to stream cash bridge. |
| 5 | Matador | Reconcile draws, note proceeds, repayments, capex, and acquisitions by timing. | Best chance to move from borrowing-base bridge to source/use allocation. |
| 9 | Liberty Broadband | Extract margin-loan pledged-share and LTV support. | Best chance to test collateral sufficiency rather than only collateral existence. |
| 13 | PBF | Pull ABL availability and note-refinancing economics. | Best chance to decide whether PBF is liquidity management or refinancing improvement. |
| 17 | Devon | Build treasury funds-flow across OCF, cash balances, assumed debt, exchanged notes, stock, capex, acquisitions, debt retirement, and payouts. | Best chance to turn allocation language into dollar-level source/use evidence. |

## Decision

`debt-refinancing-bridge-upgrade-queue-ready`

The debt/refinancing lane now has an executable next-proof queue. Each row includes a proof gap, action type, target document, route/local base, fields to extract, pass test, hold/disproof test, next artifact, and safe claim.

## Safe Claim

`The five-company debt/refinancing lane has moved from generic denominator evidence to bounded mechanism bridges, and now to an upgrade queue. The queue does not prove asset-level return; it defines the exact evidence needed to prove or reject stronger claims.`
