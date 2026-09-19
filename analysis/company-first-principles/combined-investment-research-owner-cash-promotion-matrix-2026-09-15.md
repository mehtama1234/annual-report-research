# Combined investment research owner-cash promotion matrix

Research date: `2026-09-16`

This matrix generalizes the retail owner-cash promotion rule across the three
pilots. It distinguishes a gate that is genuinely not applicable from one that
is merely missing, so different business models cannot silently inherit the
same cash denominator.

The executable field surfaces supporting this matrix are the [Wheaton Q-03
return schema](capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md),
[retail CA-06 owner-cash schema](capital-flow-retail-owner-cash-input-schema-2026-09-16.md),
and [Apollo–Athene Q-07 common-owner schema](capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.md).
The schemas preserve observed, partial, and missing inputs; this matrix is the
promotion decision layer, not a substitute for any missing source document.

## Cross-pilot gate status

| Pilot / denominator | Period alignment | Operating cash and working capital | Reinvestment / financing | Owner claims and legal entity | Service or contract attribution | Promotion decision | Next promotion test |
| --- | --- | --- | --- | --- | --- | --- |
| Wheaton–Antamina PMPA | `qualified` — H1 stream proxy is not a full-year delivery forecast | `partial` — delivered metal credits, settlement, and cash receipt are not joined | `partial` — company debt, tax, and interest are visible but not Antamina allocated | `partial` — corporate residual and lender waterfall remain open | `partial` — contract formula is visible; BHP-only payable/settlement quantity remains open | Hold at stream-level proxy; do not promote to asset-level owner cash | Join BHP-only metal-credit quantity to settlement and Wheaton receipt/receivable |
| TJX | `qualified` — FY2026 and H1 FY2027 screens have different seasonality | `partial` — inventory, temporary support, vendor/interchange effects, and service costs remain; ordinary repairs are expensed as incurred | `partial` — capitalized maintenance versus growth within renovations, leases, taxes, and dilution remain | `partial` — lease and diluted-share cash claims remain | `partial` — attached-service cash conversion is not separately disclosed | Hold at reported/illustrative screen | Obtain capitalized-maintenance allocation and service-cost allocation plus comparable working-capital bridge |
| Target | `partial` — H1 2026 annualization is not promoted | `partial` — tariff/vendor/payable, supplier finance, inventory, balance-change, and gift-card timing remain | `partial` — H1 maintenance/growth capex split remains open | `partial` — leases, taxes, dilution, and support settlement remain | `partial` — Roundel/card/other service costs and collection cash remain | Hold at reported/illustrative screen | Join next annual filing to H1 support/capex categories, gift-card redemption/tender effects, and attached-service cost/collection allocation |
| Walmart | `partial` — H1 FY2027 is not a normalized annual denominator | `partial` — supplier finance, tariff support, inventory, and payable timing remain | `partial` — category capex is visible but maintenance share and lease/tax/SBC burden remain | `partial` — common-owner cash still needs full claim bridge | `partial` — advertising, membership, fulfillment, and data costs are not allocated | Hold at reported/illustrative screen | Use annual capex categories and next filing to separate maintenance from growth and quantify ecosystem cash conversion |
| Apollo–Athene | `qualified` — Q2/H1 earnings and cash periods are aligned but entity scopes differ; Q2 AMAPS 1 exposure is `$2.544B` versus `$2.550B` at year-end | `partial` — policyholder, VIE, statutory, fee-entity, and issuer financing pools are not one owner pool; Apollo Debt Solutions leaves a `$1.450B` financing-use residual after visible lines | `partial` — debt, preferred claims, repurchases, compensation, and regulatory capital remain | `partial` — Athene-to-AGM receipt and elimination are unresolved | `partial` — fee, spread, investment, borrower, AMAPS collateral, and Broadcom fee-timing routes are not all collected common cash | Hold at segment/statutory proxy; do not promote to AGM common cash | Obtain dated Athene-to-AGM receipt, AMAPS collateral/trustee remittance, Apollo Debt Solutions note-level payment allocation, Broadcom fee collection/draw evidence, and eliminate the flows against statutory and HoldCo cash pools |

The retail [consolidated cash frontier](combined-investment-research-pilot-02-retail-consolidated-cash-frontier-2026-09-15.md)
joins the maintenance-capital and support-removal dimensions without selecting
a point estimate. It improves sensitivity coverage but does not change any
promotion decision.

For Apollo–Athene, the newly identified `$799M` fund-distribution line is a
company-level route, not an Athene receipt. The promotion test must reconcile it
to the broader `$2.040B` consolidated investing line and keep both separate from
Athene's `$110M` H1 distribution-to-parent observation before any amount can
enter a common-owner cash bridge.

## Promotion rule

A denominator can enter a promoted owner-cash valuation only when every
applicable gate is `proven` or an explicitly bounded, source-backed sensitivity
is carried into the valuation range. A sensitivity can expose uncertainty; it
cannot be relabeled as observed cash.

The following distinctions are mandatory:

- A streaming contract's operator-borne costs are not the same as zero costs;
  delivery, settlement, tax, financing, and corporate residual still require
  proof.
- An insurer's consolidated cash is not unrestricted HoldCo cash; policyholder,
  VIE, statutory, restricted, preferred, and NCI claims must remain visible.
- A retailer's OCF less property spending is not owner cash while support,
  working capital, maintenance capex, leases, tax, dilution, or attached
  services remain unresolved. Ordinary repairs already expensed in operating
  expenses should not be subtracted again; the unresolved question is the
  maintenance content of capitalized renovations and improvements.

## Current conclusion

All three pilots have usable denominators for expectation testing, but none has
earned promotion to a fully normalized common-owner cash conclusion. This is a
control against false comparability, not a claim that the businesses lack
economic cash generation.

Structured matrix: [owner-cash promotion CSV](data/combined-investment-research-owner-cash-promotion-matrix-2026-09-15.csv).
Related index: [owner-cash and denominator index](combined-investment-research-owner-cash-denominator-index.md).
