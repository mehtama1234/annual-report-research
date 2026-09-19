# Combined investment research cash-denominator reconciliation

Research date: `2026-09-16`

This artifact resolves the language of CA-06. “Correct cash denominator” does
not mean one universal cash metric; it means the denominator is matched to the
business model, legal entity, period, and claim set before valuation.

## Denominator hierarchy

```text
reported operating cash
  -> less property / reinvestment screen where appropriate
  -> source-bounded support, working-capital, lease, tax, dilution, and service sensitivities
  -> legal-entity and senior-claim bridge
  -> promoted normalized common-owner cash
```

The current work reaches the third layer for the pilots. No pilot has a fully
source-backed fourth-layer denominator.

The field-level promotion surfaces are now explicit for all three lanes:
[Wheaton Q-03](capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.md),
[retail CA-06](capital-flow-retail-owner-cash-input-schema-2026-09-16.md), and
[Apollo–Athene Q-07](capital-flow-apollo-athene-q07-common-owner-input-schema-2026-09-16.md).
Together they prevent a company-level proxy from being silently substituted
for an asset-level, cohort-level, or legal-entity-specific denominator.

The annual retail control adds cash-paid lease and tax observations, but it is
not a matched-period bridge to the current H1 screens. Those observations are
used to calibrate burden visibility, not subtracted again from operating cash
flow.

## Reconciliation by pilot

| Pilot | Current source denominator | What it correctly measures | What remains outside | Promotion blocker |
| --- | --- | --- | --- | --- |
| Wheaton–Antamina | H1 Antamina stream OCF proxy `$222.223M`; PMPA payment `$4.300B`; company financing/tax screens separate; `$1.500B` term principal bullet shown in a distinct maturity-coverage screen | Stream-level operating cash, transaction burden, and terminal principal-claim sensitivity | BHP-only settled ounces, payment dates, tax, interest, Antamina debt share, repayment source, principal waterfall, and corporate residual | Asset-level delivery and debt/tax allocation |
| TJX | H1 FY2027 OCF `$3.345B` less `$1.159B` property spending; four-corner frontier `$1.436B–$3.345B`; annual control records `$2.214B` lease cash and `$1.471B` taxes | Period-specific cash and maintenance/support sensitivity; ordinary repairs are already expensed as incurred; annual cash-paid burdens are visible | Capitalized renovations/improvements may contain maintenance and growth; inventory, support recurrence, H1 lease/tax timing, services, dilution, seasonality | Annual/common-period normalized owner cash |
| Target | H1 2026 OCF `$4.519B` less `$2.404B` property spending; four-corner frontier `$751M–$4.519B`; annual control records `$529M` lease cash and `$1.091B` taxes | Reported cash-after-property and support/capex sensitivity; annual cash-paid burdens are visible | Inventory/payables, supplier finance, tariff/vendor support, maintenance split, H1 lease/tax timing, services, dilution, seasonality | H1-to-recurring owner-cash bridge |
| Walmart | H1 FY2027 OCF `$19.710B` less `$14.181B` capex; four-corner frontier `$981M–$19.710B`; annual control records `$2.315B` lease cash and `$5.364B` taxes | Reported cash-after-capex and maintenance/support sensitivity; annual cash-paid burdens are visible | Supplier finance, tariff pass-through, maintenance share, H1 lease/tax timing, services, SBC, seasonality | Maintenance and attached-service cash conversion |
| Apollo–Athene | Apollo H1 consolidated OCF `$4.501B`; Athene statutory cash and income bridges separate | Consolidated and legal-entity cash context | Policyholder/VIE/regulatory restrictions, NCI, preferred, parent receipt, intercompany elimination, common residual | AGM unrestricted cash and common-owner waterfall |

## Promotion decision

The valuation workbenches may use the current denominators as explicitly labeled
reported screens or sensitivities. They may not label them normalized common-owner
cash. The [owner-cash promotion matrix](combined-investment-research-owner-cash-promotion-matrix-2026-09-15.md)
is the controlling gate, and the [capital-obligation/claim matrix](combined-investment-research-capital-obligation-claim-matrix-2026-09-15.md)
prevents liabilities and claims from being subtracted twice.

The retail figures in this table are the four-corner frontier: the upper edge
is OCF with no modeled property or support removal, and the lower edge applies
100% assumed maintenance treatment plus removal of the identified support
candidate, before separate claims. They must not be confused with the narrower
CA-06 quantified allocation surface, which uses additional source-bounded
screens such as Target SBC removal and Walmart's known-growth capex overlay.

Status: `denominator reconciled to model scope; normalized common-owner cash
remains unproven`.

Structured result: [cash-denominator reconciliation CSV](data/combined-investment-research-cash-denominator-reconciliation-2026-09-15.csv).
