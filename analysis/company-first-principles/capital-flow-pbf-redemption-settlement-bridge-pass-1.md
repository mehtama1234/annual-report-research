# Capital Flow PBF Redemption Settlement Bridge Pass 1

## Purpose

This pass executes the closest next pull from the top-three named cash source acquisition packet:

`PBF redemption settlement and accrued-interest support.`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-pbf-redemption-settlement-bridge-pass-1.csv`

The upstream packet is:

`/cluster/capital-flow-top-three-named-cash-source-acquisition-packet-pass-1.md`

## Question

`Can PBF's 2028 note redemption move from completed-redemption-visible status to settlement-ledger proof?`

## Short Answer

`Not yet. PBF is the closest current source/use case and has now cleared an important gate: completed redemption is visible, not merely planned. The Q2 2026 10-Q says PBF issued 500.0M USD of 2034 7.25% senior notes, received 492.1M USD of net proceeds after initial purchasers' discount and offering expenses, and redeemed all 801.6M USD of 2028 6.00% senior notes on June 25, 2026 using the new-note proceeds and available cash. The local economics pass also measures the minimum 309.5M USD cash bridge before accrued interest, 301.6M USD principal reduction, 11.846M USD simple annual coupon relief, 7.9M USD deferred financing costs and other net, and 2.2M USD loss on extinguishment. It still does not expose the trustee settlement statement, exact accrued-interest cash, final cash-on-hand split, fee amortization, tax treatment, ABL availability effect, or refinancing NPV.`

## Settlement Bridge

| Gate | Current Evidence | Status | Boundary |
|---|---:|---|---|
| New source instrument | `500.0M USD` aggregate principal of 2034 `7.25%` senior notes. | `source-instrument-visible` | Offering memorandum, buyer allocation, and final gross settlement are not extracted. |
| Net proceeds | `492.1M USD` net proceeds after initial purchasers' discount and offering expenses. | `gross-to-net-visible` | Fee components and amortization schedule are not separated. |
| Target debt retired | All `801.6M USD` of 2028 `6.00%` senior notes redeemed. | `old-debt-retirement-visible` | Trustee settlement and accrued-interest cash are not disclosed. |
| Redemption date | June `25`, `2026`. | `settlement-date-visible` | Exact payment timestamp, trustee transfer record, and holder distribution are not visible. |
| Cash bridge | Minimum `309.5M USD` available cash needed before accrued interest. | `cash-bridge-derived` | Exact cash-on-hand contribution and source priority are not disclosed. |
| Coupon mechanics | Old annual coupon `48.096M USD`; new annual coupon `36.250M USD`; simple annual coupon delta `11.846M USD`. | `coupon-proxy-visible` | Not after fees, tax, accrued interest, amortization, ABL effects, or liquidity opportunity cost. |
| Cost markers | `7.9M USD` deferred financing costs and other net; `2.2M USD` loss on extinguishment. | `cost-markers-visible` | No detailed fee schedule, tax treatment, or NPV. |
| Company cash support | H1 `2026` reported OCF `1.2651B USD`; insurance-adjusted OCF proxy `1.1538B USD`; cash interest `90.9M USD`. | `company-cash-support-visible` | Not refinery-level recurring return or refinancing value creation. |

## What This Upgrades

PBF moves from:

`planned-or-conditional-redemption-visible`

to:

`completed-redemption-source-use-visible`

This is a real upgrade because the old notes were actually redeemed by June `30`, `2026`, and the filing identifies both the new-note proceeds and available cash as funding sources.

## What Still Blocks Full Proof

Full settlement-ledger proof still requires:

1. trustee redemption statement or settlement notice
2. exact accrued-interest cash through June `24`, `2026`
3. exact cash-on-hand contribution
4. detailed financing-fee schedule and amortization
5. tax effect of extinguishment loss and fees
6. post-redemption liquidity and ABL availability
7. refinancing NPV after all costs
8. recurring refinery-level cash contribution

## Decision

`pbf-completed-redemption-source-use-visible-settlement-ledger-hold`

PBF is now the closest near-term named cash upgrade candidate. It has named source/use and completed debt retirement. It remains below settlement-ledger and economic-return proof.

## Safe Claim

`PBF's Q2 2026 filing supports completed redemption source/use evidence: 500.0M USD of 2034 7.25% notes generated 492.1M USD of net proceeds, and those proceeds plus available cash redeemed all 801.6M USD of 2028 6.00% notes on June 25, 2026. Local calculations show a minimum 309.5M USD cash bridge before accrued interest, 301.6M USD principal reduction, and about 11.846M USD of simple annual coupon relief. This is not full settlement-ledger proof or refinancing value creation because accrued interest, cash-on-hand split, detailed fees, tax, liquidity effect, ABL availability, refinancing NPV, and refinery-level return remain missing.`

## Next Source Package

1. Trustee redemption settlement statement for the 2028 notes.
2. Accrued-interest calculation from last coupon date through June `24`, `2026`.
3. Treasury cash bridge showing new-note proceeds, available cash, and final payment.
4. Debt issuance cost and fee amortization schedule for the 2034 notes.
5. Extinguishment-loss tax treatment and after-tax refinancing economics.
6. ABL availability and borrowing-base support before and after redemption.
7. Refinery-level cash contribution and outage-normalized margin support.
