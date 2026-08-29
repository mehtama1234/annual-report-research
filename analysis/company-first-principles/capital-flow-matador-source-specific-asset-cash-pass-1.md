# Capital Flow Matador Source-Specific Asset-Cash Pass 1

## Purpose

This pass executes `CFE2EGUQ-009`:

`Can Matador's reserve-based borrowing, senior-note funding, operating cash, acquisition/capex uses, and production/revenue output be upgraded into source-specific asset-cash proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-matador-source-specific-asset-cash-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md`

## Short Answer

Not fully.

Matador has aggregate source/use reconciliation, borrowing-base capacity, debt-service proxy, and company output/cash context. It does not yet have source-specific asset-cash proof.

The strongest current money-movement answer is:

`Matador generated 1.407674B USD of operating cash flow and 661.672M USD of net financing in the first half of 2026. Those sources equal 2.069346B USD, matching 2.057908B USD of net investing use plus an 11.438M USD increase in cash/restricted cash. The use side includes 745.343M USD of drilling/completion/equipping capex, 1.228834B USD of oil-and-gas property acquisitions, a named 1.160B USD BLM Acquisition, Cardinal and midstream uses, and same-period production/revenue output. The evidence still does not prove which borrowing or note proceeds funded which acquisition, wells, or assets, or what asset-level cash came back.`

## Money Movement Answer

| Link | Current Answer | Status |
|---|---|---|
| Source of money | `1.407674B USD` of operating cash flow, `541.0M USD` net Credit Agreement borrowings, `28.0M USD` net San Mateo borrowings, and `227.421M USD` net senior-note funding after issuance costs and note purchases. | aggregate source visible |
| Funding wrapper | Reserve-based Credit Agreement with `3.25B USD` borrowing base, `2.75B USD` elected commitments, `939M USD` borrowings, `53.8M USD` letters of credit, and `1.7572B USD` simple unused elected commitment after LCs. | borrowing-base capacity visible |
| Route/mechanics | Eighth Amendment shows new/increasing lenders and Collateral Coverage Minimum mechanics. | lender/collateral mechanics visible |
| Use of money | `745.343M USD` drilling/completion/equipping capex and `1.228834B USD` oil-and-gas property acquisitions. | use visible |
| Named use | BLM Acquisition cost of about `1.160B USD` for `5154` net undeveloped acres. | named acquisition visible |
| Midstream use | `37.604M USD` Cardinal acquisition, `38.697M USD` midstream capex, and `6.200M USD` midstream asset acquisition. | midstream use visible |
| Reconciliation | Operating cash plus net financing equals `2.069346B USD`, matching net investing use plus cash/restricted-cash increase. | aggregate reconciliation visible |
| Debt-service/cash proxy | H1 `2026` interest expense of `112.344M USD`, equal to about `7.981%` of OCF. | company debt-cost proxy visible |
| Output/cash context | Q2 production of `215631` BOE/d, oil production of `11.476MMbbl`, gas production of `48.9Bcf`, and Q2 revenue of `1.186392B USD`. | company output/cash context visible |
| Missing proof | Borrowing notices, lender allocations, reserve values, BLM funds-flow, acquisition cash contribution, well-level production, LOE, cash margin, cash interest, and asset-level return. | hold |

## Decision

`CFE2EGUQ-009` should move from `partial-local` to:

`executed-local-boundary-pass-1`

Pass result:

`Matador reaches aggregate source/use plus borrowing-base and output/cash-context status with operating cash, net financing, Credit Agreement movement, San Mateo movement, senior-note net source, development capex, acquisition cash, BLM acquisition evidence, reserve-based capacity, liquidity headroom, lender/collateral mechanics, debt-cost proxy, and production/revenue output.`

Hold result:

`Source-specific asset cash remains unproven because the local evidence does not tie borrowing notices, lender commitments, reserve values, note proceeds, or operating cash to specific acquisitions, wells, midstream assets, asset-area cash contribution, LOE, cash margin, cash interest, or asset-level return.`

## Safe Claim

`Matador has a clean aggregate first-half 2026 money-movement reconciliation and reserve-based funding context: operating cash plus net financing funded the aggregate investing envelope, with visible development capex, acquisition cash, a named BLM Acquisition, borrowing-base capacity, debt-cost proxy, and company output/revenue. It should not be described as source-specific asset-cash or asset-return proof until borrowing notices, lender allocation, reserve support, acquisition funds-flow, asset contribution, LOE, cash margin, and cash-interest evidence are visible.`

