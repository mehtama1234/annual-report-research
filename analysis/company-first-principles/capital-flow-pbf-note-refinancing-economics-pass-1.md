# Capital Flow PBF Note Refinancing Economics Pass 1

## Purpose

This page executes PBF row `CFDRBUQ-014` from the debt/refinancing bridge upgrade queue:

`Can PBF's 2028-to-2034 note refinancing be upgraded from named source/use evidence to measured debt-service economics?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-pbf-note-refinancing-economics-pass-1.csv`

The upstream queue is:

`/cluster/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.md`

The upstream PBF bridge is:

`/cluster/capital-flow-pbf-refining-liquidity-use-return-bridge-pass-1.md`

## Current Answer

`PBF can be upgraded to note-refinancing mechanics visible with first-order annual coupon relief, but not to refinancing value creation. In Q2 2026 PBF issued 500.0M USD of 2034 7.25% senior unsecured notes, received 492.1M USD of net proceeds, and used those proceeds plus available cash to redeem all 801.6M USD of its 2028 6.00% senior notes at par plus accrued interest. The new notes carry a higher coupon by 1.25 percentage points, but the refinanced note principal is 301.6M USD smaller. Simple annual coupon dollars fall from about 48.096M USD on the redeemed notes to 36.250M USD on the new notes, or 11.846M USD of annual coupon relief before fees, accrued interest, tax, amortization, liquidity opportunity cost, and broader debt-stack effects.`

## Reconciliation

| Step | Amount | Meaning |
|---|---:|---|
| 2034 senior notes issued | `500.000M USD` | Gross new-note principal. |
| Net proceeds | `492.100M USD` | Cash proceeds after initial purchasers' discount and offering expenses. |
| 2028 senior notes redeemed | `801.600M USD` | Old-note principal retired. |
| Minimum available cash needed before accrued interest | `309.500M USD` | Old principal less net proceeds. |
| Gross senior-note principal reduction | `301.600M USD` | Old principal less new principal. |
| Old annual coupon dollars | `48.096M USD` | `801.600M USD * 6.00%`. |
| New annual coupon dollars | `36.250M USD` | `500.000M USD * 7.25%`. |
| Simple annual coupon delta | `11.846M USD` | Coupon-dollar relief from lower principal despite higher coupon. |
| Deferred financing costs and other, net | `7.900M USD` | Visible financing-cost cash outflow. |
| Loss on extinguishment | `2.200M USD` | Accounting loss tied to redemption. |

## What Improved

| Area | Prior Bridge | This Pass |
|---|---|---|
| Source/use | The PBF bridge showed notes proceeds plus available cash redeemed old notes. | The pass measures the gross-to-net proceeds gap, cash bridge, principal reduction, coupon-rate change, and simple annual coupon delta. |
| Debt-service | Cash interest and coupons were visible as facts. | Simple annual coupon economics are calculated: `48.096M USD` old note coupon dollars versus `36.250M USD` new note coupon dollars. |
| Cost boundary | Refinancing cost was an open gap. | The pass captures `7.900M USD` of deferred financing costs and `2.200M USD` loss on extinguishment while keeping full economic cost open. |
| Liquidity boundary | PBF had revolver movement and zero quarter-end revolver debt. | The pass separates note economics from ABL availability, collateral, and facility-exit proof. |

## Decision

`note-refinancing-mechanics-visible-benefit-not-proven`

This is an upgrade from:

`refining-liquidity-cash-bridge-visible-company-level`

It does not reach:

`refinancing-value-creation-proven`

The queue pass test required maturity extension and debt-service economics after fees and redemption cost. The visible filing evidence supports mechanics, simple coupon math, deferred financing costs, and extinguishment loss. It does not yet support a full after-fee, after-tax, pro forma debt-service or NPV conclusion.

## Remaining Gap

| Gap | Why It Matters | Next Source |
|---|---|---|
| Redemption settlement detail | Needed to isolate accrued interest, settlement timing, and any cash premium detail. | 2028 redemption notice and settlement statement. |
| Pro forma interest schedule | Needed to compare run-rate interest after note issuance, redemption, capitalized interest, and other debt-stack movement. | Interest expense rollforward and company pro forma debt-service schedule. |
| Fee amortization and tax treatment | Needed to convert gross-to-net proceeds and extinguishment loss into after-tax economics. | Debt issuance cost rollforward and tax footnote. |
| Liquidity opportunity cost | Needed because at least `309.500M USD` of available cash was used before accrued interest. | Treasury cash rollforward and liquidity policy. |
| ABL availability and collateral | Needed to test whether zero revolver debt means real liquidity improvement or just quarter-end balance management. | ABL agreement, availability table, and borrowing-base certificate. |
| Refinery-level recurring cash | Needed to decide whether PBF's operating cash can sustain the debt-service profile. | Insurance-normalized cash flow and refinery-level cash contribution tables. |

## Safe Claim

`PBF's Q2 2026 filing supports a bounded note-refinancing economics claim: PBF issued 500.0M USD of 2034 7.25% senior notes, received 492.1M USD of net proceeds, used those proceeds plus available cash to redeem 801.6M USD of 2028 6.00% senior notes at par plus accrued interest, reduced the refinanced senior-note principal layer by 301.6M USD, and created about 11.846M USD of simple annual coupon relief before fees, accrued interest, tax, amortization, liquidity opportunity cost, and broader debt-stack effects. This does not prove refinancing value creation, ABL exit, refinery-level return, or recurring cash-return quality.`

## Next Work

1. Pull the 2034 indenture, offering memorandum, and any 8-K exhibit terms.
2. Find the 2028 redemption notice or settlement detail.
3. Build a pro forma interest schedule with capitalized interest treatment.
4. Add ABL availability and borrowing-base evidence.
5. Normalize PBF first-half cash flow for insurance and outage effects before making recurring-return claims.
