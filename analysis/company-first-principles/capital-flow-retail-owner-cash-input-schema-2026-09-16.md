# Retail cohort owner-cash input schema

Research date: `2026-09-17`

This schema turns CA-06 for TJX, Target, and Walmart into an executable
denominator checklist. It keeps reported operating cash less property spending
separate from normalized owner cash and requires each adjustment to be matched
by company, period, accounting treatment, and source path.

The schema does not estimate missing maintenance capital, service costs, cash
taxes, lease payments, or recurring support. `observed` means the field is
reported for the relevant company-period; `partial` means a bounded proxy or
category exists; `missing` means the promotion input is not disclosed or not
assembled. A final owner-cash number cannot be promoted while required fields
remain missing or period-mismatched.

## Required input families

| Family | Required control |
| --- | --- |
| Reported denominator | Net sales, operating cash flow, property spending, inventory, and accounts payable must share a defined period. |
| Temporary and noncash effects | Support, refunds, unusual receipts, supplier finance, and stock compensation must be identified without double counting. |
| Reinvestment and claims | Maintenance capital, growth capital, leases, cash taxes, debt claims, and service costs must be separated or explicitly ranged. |
| Per-share residual | Diluted shares and the final residual must use the same period and claim perimeter. |

The structured [retail owner-cash input schema](data/capital-flow-retail-owner-cash-input-schema-2026-09-16.csv)
is the machine-readable source of truth for the field list and current status.
The [retail capex classification boundary](combined-investment-research-pilot-02-retail-capex-classification.md),
[common-period cash matrix](combined-investment-research-pilot-02-retail-common-period-cash-matrix.md),
and [attached-service boundary](combined-investment-research-pilot-02-retail-attached-services-cash-frontier-2026-09-15.md)
provide the current evidence routes.

## Promotion rule

The first defensible screen remains reported operating cash flow less total
property spending. Promotion to normalized owner cash requires a source-backed
period join for working capital, temporary support, maintenance/growth capital,
leases, taxes, attached services, senior claims, and dilution. Where a filing
does not disclose the field, the model must retain a range or an unresolved
label rather than silently assigning zero.

Status: `retail-owner-cash-inputs-structured; normalized owner cash unresolved`.

## Live SEC-source recheck — 2026-09-17

The latest official filing search rechecked the current TJX FY2026 annual
source, Target Q2 2026 10-Q, and Walmart Q2 FY2027 10-Q. It confirms the
source-bounded cash inputs already in the bridge—TJX FY2026 operating cash of
`$6.874B` and property additions of `$1.957B`, Target H1 operating cash of
`$4.519B` and property spending of `$2.404B`, and Walmart H1 operating cash of
`$19.710B` and property spending of `$14.181B`—alongside the relevant inventory,
payable, supplier-finance, and share-compensation disclosures.

The recheck did not disclose the missing promotion objects: a
maintenance-versus-growth capex split, matched interim cash taxes and lease
payments, service-level cost and collection allocation, or a final diluted
common-owner residual. The three rows therefore remain bounded diagnostic
screens, not normalized owner cash. This is a current source boundary, not a
claim that the costs or payments do not exist.

The supplier-finance field is a qualified partial rather than an empty field:
Target's FY2025 and Walmart's FY2026 filings disclose confirmed-invoice-paid
roll-forwards, but those annual flows do not identify the current H1 cash
allocation or permit a balance-only deduction from operating cash.

### Target current-period recheck — August 1, 2026

Target's latest Q2 2026 10-Q improves the current H1 perimeter: it reports
`$4.519B` OCF, `$2.404B` property spending, `$945M` inventory cash use, `$612M`
accounts-payable support, `$3.2B` supplier-finance-eligible obligations, and
`$994M` of IEEPA tariff refunds. It also reports `$3.733B` of operating-lease
liabilities and `$835M` of tax provision, but no matched H1 cash-paid lease or
cash-tax line. The current-period maintenance split, service-level cash, and
normalized owner-cash residual therefore remain missing; these observations
are a dated perimeter upgrade, not a promotion.
