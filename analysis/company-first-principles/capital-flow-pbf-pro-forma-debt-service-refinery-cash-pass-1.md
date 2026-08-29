# Capital Flow PBF Pro Forma Debt-Service And Refinery-Cash Pass 1

## Purpose

This pass executes `CFE2EGUQ-008`:

`Can PBF's note refinancing mechanics be tied to pro forma debt-service evidence and same-period refinery cash quality?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-pbf-pro-forma-debt-service-refinery-cash-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md`

## Short Answer

Partly.

PBF now has pro forma debt-service and refinery-cash proxy evidence. It does not have refinancing value-creation proof or refinery-level return proof.

The strongest current money-movement answer is:

`PBF issued 500.0M USD of 2034 7.25% senior notes, received 492.1M USD of net proceeds, and used those proceeds plus available cash to redeem 801.6M USD of 2028 6.00% senior notes. The targeted note layer shrank by 301.6M USD, simple annual coupon dollars fell by about 11.846M USD, and the company paid 90.9M USD of first-half cash interest while generating 1.2651B USD of reported OCF and 1.1538B USD of OCF after operating-section insurance proceeds. This supports a bounded debt-service/refinery-cash proxy, not a claim that the refinancing created economic value or improved refinery-level returns.`

## Money Movement Answer

| Link | Current Answer | Status |
|---|---|---|
| Source of money | `500.0M USD` of 2034 7.25% senior notes and `492.1M USD` of net proceeds. | refinancing source visible |
| Additional source | At least `309.5M USD` of available cash or other liquidity was needed before accrued interest. | cash bridge visible |
| Use of money | Full redemption of `801.6M USD` of 2028 6.00% senior notes. | refinancing use visible |
| Debt-service mechanics | Gross note principal fell by `301.6M USD`; coupon rate increased by `1.25` percentage points; simple annual coupon burden fell by about `11.846M USD`. | first-order pro forma visible |
| Refinancing costs | `7.9M USD` deferred financing costs and other net; `2.2M USD` loss on extinguishment. | cost markers visible |
| Liquidity movement | H1 `2026` revolver borrowings of `1.100B USD`, repayments of `1.200B USD`, and zero quarter-end revolver balance. | liquidity activity visible |
| Company cash | H1 `2026` reported OCF of `1.2651B USD`; operating insurance-adjusted OCF proxy of `1.1538B USD`. | company cash proxy visible |
| Capital/maintenance burden | H1 `2026` PP&E spending plus deferred turnaround spending of `718.9M USD`. | use/cash burden visible |
| Debt-service coverage proxy | Insurance-adjusted OCF covered cash interest by about `12.7x`. | reported-period coverage proxy visible |
| Refinery output/margin context | H1 throughput of `156.7M` barrels, gross refining margin of `2.9263B USD`, and `16.67 USD` per barrel gross refining margin excluding special items. | operating context visible |
| Missing proof | Refinancing NPV, after-tax economics, accrued-interest settlement, fee amortization, ABL availability, recurring outage-normalized refinery cash, refinery-level contribution, and refinery-level return. | hold |

## Evidence Stack

| Gate | Evidence | Result |
|---|---|---|
| Named source | `500.0M USD` 2034 7.25% senior notes. | Refinancing source visible. |
| Net cash source | `492.1M USD` net proceeds. | Usable proceeds visible, but not enough alone. |
| Named use | `801.6M USD` 2028 6.00% senior notes redeemed. | Refinancing use visible. |
| Cash bridge | Minimum `309.5M USD` available-cash bridge before accrued interest. | Shows company cash/liquidity was part of the movement. |
| Simple pro forma | About `11.846M USD` annual coupon relief. | Supports first-order debt-service math, not value creation. |
| Cost markers | `7.9M USD` deferred financing costs and `2.2M USD` extinguishment loss. | Full NPV still missing. |
| Liquidity movement | `1.100B USD` revolver borrowings, `1.200B USD` repayments, zero quarter-end revolver balance. | Shows liquidity churn, not ABL exit proof. |
| Cash quality | `1.1538B USD` operating insurance-adjusted OCF proxy. | Strong company cash proxy after one adjustment. |
| Capital burden | `476.5M USD` PP&E plus `242.4M USD` deferred turnaround spending. | Capital/maintenance use visible. |
| Debt-service proxy | About `12.7x` insurance-adjusted OCF/cash interest. | Strong reported-period coverage proxy. |
| Operating context | `156.7M` barrels throughput and `2.9263B USD` gross refining margin excluding special items. | Refinery activity visible, not refinery-level return. |

## Decision

`CFE2EGUQ-008` should move from `partial-local` to:

`executed-local-boundary-pass-1`

Pass result:

`PBF reaches pro forma debt-service and refinery-cash proxy status with named refinancing source/use, gross and net proceeds, available-cash bridge, principal reduction, simple annual coupon relief, visible refinancing costs, revolver movement, insurance-normalized company cash, capital/turnaround burden, cash-interest coverage, throughput, and refining-margin context.`

Hold result:

`Full upgrade remains unproven because the local evidence does not prove refinancing NPV, after-tax economics, accrued-interest settlement, fee amortization, ABL legal availability, borrowing-base cushion, recurring outage-normalized refinery cash, refinery-level contribution, or refinery-level return.`

## Safe Claim

`PBF has explicit refinancing source/use mechanics and a bounded company-level debt-service/refinery-cash proxy. It should not be described as refinancing value creation, ABL exit proof, or refinery-level return proof until redemption settlement, pro forma interest, fee amortization, tax, liquidity opportunity cost, ABL availability, outage normalization, and refinery-level cash contribution are visible.`

