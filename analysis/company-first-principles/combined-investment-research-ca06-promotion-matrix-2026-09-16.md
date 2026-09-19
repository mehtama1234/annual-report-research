# CA-06 owner-cash promotion matrix

Research date: `2026-09-17`

## Purpose

This matrix is the end-to-end control for the sixth definition-of-done
requirement: reported performance must be reconciled to the correct owner-cash
denominator. It joins the three pilot-specific allocation surfaces into one
promotion test. It does not force a common cash formula across a streaming
company, a retail cohort, and an insurance/asset-management platform.

The structured [promotion matrix CSV](data/combined-investment-research-ca06-promotion-matrix-2026-09-16.csv)
is the source of truth.

## Current result

All three pilots have a reported or mechanically bounded base denominator, but
none is promotion-ready:

- **Wheaton–Antamina:** the stream proxy is not a BHP-only receipt ledger and
  company financing, tax, and repayment are not allocated to the stream.
- **Retail cohort:** operating cash less property spending is period-matched,
  but maintenance capital, leases, taxes, attached-service cash, supplier
  finance, support recurrence, and seasonality remain unresolved.
- **Apollo–Athene:** earnings and legal-entity cash surfaces are visible, but
  policyholder/senior claims, asset-level returns, AGM receipt, and common-owner
  residual are not joined.

The latest controls sharpen the three denominator boundaries without changing
the status: Q-03 now separates planned and actual Wheaton funding flows from
PMPA allocation; Q-02 now reconciles the forward profile to the mechanical
reserve ceiling; and retail QoE now prohibits double counting balance-sheet
supplier-finance movements against cash-flow working-capital rows.

The retail row intentionally keeps matched H1 lease and tax cash as `missing`.
The annual lease-and-tax control supplies useful burden visibility, but those
annual payments are already embedded in annual operating cash flow and cannot
be carried into the H1 denominator without period matching. They are therefore
not additional owner-cash deductions and do not change the promotion status.

The [TJX FY2026 owner-cash perimeter upgrade](combined-investment-research-tjx-fy2026-owner-cash-perimeter-upgrade-2026-09-17.md)
adds an annual, company-specific capex taxonomy and same-period tax/lease
burden observations. It produces a `$4.917B` OCF-less-property screen, but
keeps maintenance versus growth, recurring repair burden, and the final
common-owner residual unresolved. The annual observations do not fill the
missing H1 lease/tax fields for the cohort.

## Promotion rule

`allocation-sensitivity-only` is the highest status currently supported. A
pilot can move to `promotion-ready` only when the required source-backed
allocation, settlement, receipt, or waterfall is joined to the same entity and
period. The matrix therefore closes the control architecture for CA-06 while
correctly leaving the investment conclusions qualified.

Status: `CA-06-partial; three-pilot-denominator-matrix-structured`.

## Minimum promotion bundle

The next source must close a join, not merely add another observation. For a
promotion decision, the evidence bundle must identify the legal entity, period,
denominator, cash or claim object, and reconciliation path:

| Pilot | Minimum joinable bundle | Promotion result if complete |
| --- | --- | --- |
| Wheaton–Antamina | BHP-only delivered ounces and settlement/receipt; Antamina tax; facility-specific draw, repayment, and interest allocation; delivery-period cash bridge | Promote only the Antamina-specific financed owner-cash/return denominator; keep combined-stream proxies separate |
| Retail cohort | Same-period working-capital settlement; maintenance-versus-growth capital; cash-paid lease and tax where applicable; attached-service collection and allocated costs; supplier-finance and dilution treatment | Promote only the company-period normalized owner-cash denominator; do not pool TJX, Target, and Walmart into one cash number |
| Apollo–Athene | Legal-entity and regulated-claim perimeter; named-asset income/settlement; liability-cost allocation; dated AGM receipt and elimination; common-owner residual | Promote only the joined legal-entity/common-owner residual; do not convert consolidated or statutory cash into unrestricted AGM cash |

If one of these bundles is unavailable, the row remains
`allocation-sensitivity-only` and the missing object is routed to the next
evidence queue. This keeps the denominator decision tied to a reproducible
source path rather than to a larger proxy range.

## QoE and financial-shenanigans gate

The promotion bundle is also screened for quality-of-earnings and
financial-shenanigans diagnostics. These are reconciliation prompts, not a
fraud score:

| Pilot | Diagnostic that can block promotion | Required reconciliation |
| --- | --- | --- |
| Wheaton–Antamina | Recognition on metal-credit sales, combined-stream presentation, streaming-liability settlement, and corporate debt movement presented as asset funding | Join BHP-only credits, invoice/receipt, quotation-period settlement, liability rollforward, and facility-level funds flow before using stream profit or corporate interest in an asset return |
| Retail cohort | Inventory/payables timing, supplier finance, temporary support, capitalization of operating costs, attached-service revenue classification, and stock compensation/dilution | Match balance movements to cash settlement, test support recurrence, separate maintenance from growth, allocate service costs, and keep diluted claims outside owner cash until period-matched |
| Apollo–Athene | Fee-payable rollforwards, related-party transfers, statutory-versus-GAAP cash, named-asset income without settlement, and AUM or transaction activity presented as cash return | Join legal entity, CUSIP/borrower, collection or sale cash, liability cost, trustee/remittance route, parent receipt, and common-owner residual |

No row may be promoted because a diagnostic score looks favorable. A flag is
either cleared by the required reconciliation, carried into the sensitivity
range, or preserved as a thesis breaker.
