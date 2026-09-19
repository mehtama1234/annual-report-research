# TJX FY2026 owner-cash perimeter upgrade

Research date: `2026-09-17`

## Purpose

This is a company-specific annual upgrade inside the CA-06 retail cohort. It
does not close the cohort-wide normalized owner-cash requirement and does not
make TJX comparable to Target or Walmart without period and accounting joins.

## Newly joinable FY2026 observations

TJX's FY2026 annual filing reports `$6.874B` of operating cash flow and
`$1.957B` of property additions. The property schedule separates `$185M` for
new stores, `$921M` for store renovations and improvements, and `$851M` for
offices and distribution centers. TJX also reports `$1.471B` of cash income
taxes and `$2.214B` of operating cash flows paid for operating leases. The
filing states that maintenance and repairs are expensed as incurred.

The resulting first-order screen is:

`$6.874B OCF - $1.957B property additions = $4.917B reported cash-after-property`

The `$1.471B` tax and `$2.214B` lease figures are burden observations for the
same annual perimeter, not additional deductions from OCF. Subtracting them
again would double count cash already reflected in operating cash flow.

## What this improves

The annual TJX case now has a stronger legal-period denominator and a more
useful capex taxonomy. New stores are a visible growth category; renovations,
improvements, offices, distribution centers, and technology remain mixed and
cannot be labeled maintenance or growth without project-level classification.
The explicit expensing policy also prevents treating all recurring maintenance
as hidden PP&E.

## QoE and financial-shenanigans controls

1. Reconcile the `$6.874B` OCF to inventory, payables, accrued expenses, taxes,
   and other current assets; do not treat one year's working-capital support as
   a permanent margin.
2. Keep `$1.957B` property additions separate from depreciation and from
   repairs expensed as incurred.
3. Carry the `$2.214B` operating-lease cash and `$1.471B` cash-tax observations
   as senior operating burdens already embedded in OCF.
4. Test whether the `$921M` renovation/improvement category preserves the
   existing store network or expands capacity; the public filing does not
   resolve that split.
5. Keep buybacks, dividends, stock issuance, supplier terms, inventory, and
   lease obligations in the common-owner residual bridge.

## Valuation and liquidity implication

The `$4.917B` screen can support a dated Damodaran expectation test, but not a
normalized owner-cash multiple. A proper base case must carry the mixed capex
categories, recurring repairs, lease burden, tax burden, inventory funding,
and dilution. The Lyn Alden-style stress case reverses inventory/payable
support, raises occupancy and labor costs, and tests whether store and supply-
chain investment remains financeable through a liquidity tightening.

## Decision

`TJX-FY2026-annual-denominator-strengthened; maintenance-split-open; CA-06-partial`

This is a real denominator upgrade for one retail company-period. It does not
close Target/Walmart service allocation, matched interim lease/tax evidence,
supplier-finance settlement, maintenance-capital classification, or the final
cohort owner-cash residual.

## Source

[TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
