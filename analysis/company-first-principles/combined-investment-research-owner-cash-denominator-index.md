# Combined investment research owner-cash and denominator index

Research date: `2026-09-15`

This index is the review entry point for the denominator layer. It keeps
reported operating cash, mechanical sensitivities, company-level burdens, and
common-owner claims separate across the three pilots.

The cross-pilot [owner-cash promotion matrix](combined-investment-research-owner-cash-promotion-matrix-2026-09-15.md)
is the controlling gate summary for deciding whether any denominator may enter
a promoted valuation.

The companion [capital-obligation and claim matrix](combined-investment-research-capital-obligation-claim-matrix-2026-09-15.md)
records debt, capex, lease, supplier-finance, dilution, and capital-return
claims with explicit non-additivity rules.

The [cash-denominator reconciliation](combined-investment-research-cash-denominator-reconciliation-2026-09-15.md)
is the CA-06 control: it identifies the correct current denominator for each
business model and the exact blocker to promoting it to common-owner cash.

## Pilot 01 — Wheaton–Antamina

- [Integrated Wheaton–Antamina pilot](combined-investment-research-pilot-01-wheaton-antamina.md)
- [Antamina scenario workbench](combined-investment-research-pilot-01-antamina-scenario-workbench.md)
- [Company-level financed-return frontier](capital-flow-wheaton-antamina-financed-return-frontier-2026-09-15.md)
- [After-tax financed allocation frontier](capital-flow-wheaton-antamina-after-tax-financed-allocation-frontier-2026-09-15.md)
- [Reserve-capped upfront-recovery frontier](capital-flow-wheaton-antamina-reserve-capped-upfront-recovery-frontier-2026-09-15.md)

The denominators are `$4.300B` upfront consideration, stream-level H1 OCF
proxy, company finance and tax burdens, and reserve-constrained payable-ounce
screens. None is promoted to asset-level common-owner cash without BHP-only
settlement, tax, debt, and delivery evidence.

## Pilot 02 — Retail cohort

- [Common-period retail cash matrix](combined-investment-research-pilot-02-retail-common-period-cash-matrix.md)
- [Normalized-cash screen](combined-investment-research-pilot-02-retail-normalized-cash-screen.md)
- [Margin and working-capital normalization](combined-investment-research-pilot-02-retail-margin-working-capital-normalization.md)
- [Target inventory/payable balance-change screen](combined-investment-research-pilot-02-target-inventory-payable-balance-screen-2026-09-15.md)
- [Cross-cohort inventory/payable balance and cash-flow screen](combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.md)
- [Retail capex classification](combined-investment-research-pilot-02-retail-capex-classification.md)
- [Retail consolidated cash frontier](combined-investment-research-pilot-02-retail-consolidated-cash-frontier-2026-09-15.md)
- [Retail post-financing residual screen](combined-investment-research-pilot-02-retail-post-financing-residual-screen-2026-09-15.md)
- [Attached-services cash frontier](combined-investment-research-pilot-02-retail-attached-services-cash-frontier-2026-09-15.md)

The cohort tables retain OCF, property spending, inventory, payables,
supplier-finance obligations, temporary support, leases, dilution, attached
services, and maintenance/growth capex as separate fields. Reported cash after
property is a screen, not normalized owner cash.

## Pilot 03 — Apollo–Athene

- [Apollo common-owner bridge](combined-investment-research-pilot-03-apollo-common-owner-bridge.md)
- [Apollo SOTP workbench](data/combined-investment-research-pilot-03-apollo-sotp-workbench.csv)
- [Q2 upstream source-to-destination bridge](capital-flow-apollo-athene-q2-upstream-source-destination-bridge-2026-09-15.md)
- [Q2 parent-receipt attribution frontier](capital-flow-apollo-athene-q2-parent-receipt-attribution-frontier-2026-09-15.md)
- [Athene statutory cash-return upgrade](capital-flow-apollo-athene-statutory-cash-return-upgrade-2026-09-15.md)

The Apollo lane keeps segment earnings, statutory entity cash, subsidiary
distributions, intercompany notes, consolidated unrestricted cash, preferred
and RSU claims, and common-owner residuals separate. A subsidiary distribution
is not treated as AGM cash until the receiving-account and elimination bridge
is proven.

## Promotion rule

Only a denominator joined to the correct legal entity, period, burden set, and
cash route can enter a normalized owner-cash valuation. Mechanical frontiers
are useful for expectation testing but remain excluded from the promoted
owner-cash tables until their missing proof fields are closed.

Structured source routes are checked by the [pilot verifier](../../scripts/verify-combined-investment-pilots.py), while requirement-level status remains in the [completion audit](combined-investment-research-completion-audit.md).
