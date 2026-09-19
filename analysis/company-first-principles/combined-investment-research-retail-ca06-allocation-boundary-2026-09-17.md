# Retail CA-06 allocation boundary — 2026-09-17

## Finding

The current retail filings support a reported OCF-to-property bridge for TJX,
Target, and Walmart, but they do not support one normalized common-owner cash
denominator. The missing fields are not interchangeable:

| Company / period | Observed | Not disclosed or not joinable in the matched period |
| --- | --- | --- |
| TJX H1 FY2027 | OCF `$3.345B`; property spending `$1.159B`; category detail; annual lease/tax context | H1 maintenance-versus-growth split, supplier-finance settlement, service cost/collection, matched lease/tax cash |
| Target H1 2026 | OCF `$4.519B`; property spending `$2.404B`; `$3.2B` supplier-finance obligation; `$994M` tariff refund | H1 maintenance-versus-growth split, supplier-finance payment allocation, cash-paid lease/tax, attached-service cost/collection |
| Walmart H1 FY2027 | OCF `$19.710B`; property spending `$14.181B`; `$1.087B` new-store category; `$6.4B` supplier-finance obligation | Full maintenance/growth allocation, H1 supplier-finance settlement, cash-paid lease/tax, ecosystem-service cost/collection |

The annual lease/tax figures and annual confirmed-invoice flows are useful
burden context but cannot be subtracted from H1 OCF without payment dates and
cash-flow classification. Supplier-finance period-end balances are obligations,
not cash-flow adjustments. Inventory/payable changes are already reflected in
OCF and must not be deducted again.

## Correct denominator rule

```text
reported OCF
  -> property/software spending
  -> working-capital and supplier-finance timing
  -> temporary support and unusual items
  -> maintenance/growth allocation
  -> lease and tax cash
  -> attached-service collection and cost
  -> debt, NCI, preferred, SBC, dilution, and other claims
  -> common-owner residual
```

The resulting screen remains company-specific and period-labeled. It is not a
retail ranking and does not convert tariff refunds, supplier-finance support,
annual burden context, or company-defined FCF into normalized owner cash.

## Promotion boundary

CA-06 can advance only with a matched payment or allocation schedule covering
maintenance/replacement capital, lease and tax cash, supplier-finance
settlement, attached-service collection and cost, and common-owner claims. The
next source object is therefore a company filing exhibit, payment-date ledger,
project/capex schedule, or management schedule that closes one of those joins;
another OCF screen is not sufficient.

Status: `CA-06-partial; retail-allocation-boundary-explicit; no-ranking`.

## Official filing recheck

## 2026-09-18 supplemental-field refresh

The latest direct SEC filing search sharpens the supplier-finance control but
does not create a matched H1 cash join. Target's Q2 2026 10-Q says its `$3.2B`
of eligible vendor obligations are included in accounts payable and do not
represent actual early payments under the supplier-finance programs. The same
filing has no H1 cash-paid operating-lease or cash-tax schedule. Walmart's Q2
2026 10-Q exposes H1 OCF of `$19.710B`, inventory use of `$2.660B`, accounts
payable support of `$1.648B`, and property-and-equipment payments of
`$14.181B`, but does not provide a matched H1 operating-lease payment field or
maintenance/growth allocation. These observations strengthen the rule that
period-end supplier-finance obligations and balance-sheet working-capital
movements cannot be deducted again from OCF without settlement evidence.

This remains a denominator-control refresh, not a promotion: lease/tax cash,
maintenance/growth allocation, service cost/collection, and common-owner
residual remain open.

The official SEC recheck confirms the boundary rather than closing it. Walmart's
H1 cash-flow statement reports `$19.710B` of OCF, `$14.181B` of property and
equipment payments, a `$2.660B` inventory use, and `$1.648B` of accounts-payable
support; its supplier-finance note reports `$6.4B` of eligible vendor
obligations. The Q2 10-Q does not provide a matched H1 operating-lease cash
payment line or a complete maintenance/growth allocation.

Target's official Q2 10-Q reports `$4.519B` of H1 OCF, `$2.404B` of property and
equipment spending, `$945M` of inventory use, `$612M` of accounts-payable
support, and `$3.2B` of supplier-finance obligations. It likewise does not
provide a matched H1 cash-paid lease/tax schedule or maintenance/growth split.
Its ROIC reconciliation reports `$3.733B` of total operating-lease liabilities,
`$172M` of trailing operating-lease interest, and `$1.402B` of trailing income
taxes, but those are invested-capital/ROIC inputs rather than H1 cash-paid
burdens and are not substituted into the owner-cash denominator.

TJX's official FY2026 10-K reports `$1.471B` of cash taxes and states that
maintenance and repairs are expensed as incurred, while its property schedule
contains mixed stores, renovations, offices, distribution, and technology
categories. That annual evidence improves the burden taxonomy but cannot be
used as a matched H1 allocation for the cohort.

Target's May 2026 strategy announcement adds more than `130` full-store
remodels, more than `30` new stores, and supply-chain/technology investment
within an approximately `$5B` 2026 investment plan. Its Q2 release says the
quarter's `$1.4B` capex was driven primarily by remodels and new stores. This
is a current growth-driver boundary for the `$2.404B` H1 property line, not a
maintenance schedule: remodels can contain both replacement and discretionary
upgrade work, and the public materials do not allocate the residual property
spend by project or cash date. See the [Target capex growth-driver boundary](combined-investment-research-target-q2-2026-capex-growth-driver-boundary-2026-09-18.md).

This is a searched-negative result for the checked public filing perimeter, not
evidence that the schedules do not exist privately. The promotion object remains
a matched payment-date, project-capex, or service-allocation schedule.

## Sources

- [Retail CA-06 source-acquisition packet](combined-investment-research-retail-ca06-source-acquisition-packet-2026-09-18.md).
- [Retail H1 owner-cash denominator handoff](combined-investment-research-retail-h1-owner-cash-denominator-handoff-2026-09-17.md)
- [TJX FY2026 owner-cash perimeter upgrade](combined-investment-research-tjx-fy2026-owner-cash-perimeter-upgrade-2026-09-17.md)
- [Target Q2 2026 cash-quality perimeter upgrade](combined-investment-research-target-q2-2026-cash-quality-perimeter-upgrade-2026-09-17.md)
- [Walmart Q2 FY2027 cash-quality perimeter upgrade](combined-investment-research-walmart-q2-fy2027-cash-quality-perimeter-upgrade-2026-09-17.md)
- [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm)
- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)
- [TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
