# Retail H1 owner-cash denominator handoff

Research date: `2026-09-17`

## Purpose

This handoff consolidates the current retail evidence into one company-period
denominator surface. It is the next CA-06/Q-04–Q-06 execution object: a
reconciliation control for cash already reported, cash-like claims that remain
period-mismatched, and burdens that cannot yet be allocated. It does not create
a normalized retail ranking.

The rule is:

`reported OCF -> property spending -> working-capital and supplier-finance timing -> support and unusual items -> maintenance/growth allocation -> leases/taxes -> service cash and cost -> debt/NCI/dilution -> common-owner residual`

Lease cash, taxes, supplier-finance movements, and working-capital changes that
are already inside operating cash flow cannot be subtracted again merely
because an annual or period-end balance is separately disclosed.

## Current same-period surface

| Company / period | OCF | Property spending | Cash after property | Current burden/control | Safe conclusion |
|---|---:|---:|---:|---|---|
| TJX / H1 FY2027 | `$3.345B` | `$1.159B` | `$2.186B` | `$0.750B` support candidate, `$85M` SBC sensitivity, and `$222M` disclosed new-store growth floor; H1 capex by segment is visible, but no H1 maintenance split, supplier-finance settlement, service-cost allocation, or matched lease/tax cash | Reported cash-after-property screen only; ordinary repairs are expensed and must not be deducted again, while capitalized renovations/distribution/IT remain mixed |
| Target / H1 2026 | `$4.519B` | `$2.404B` | `$2.115B` | `$1.364B` support candidate, `$154M` SBC sensitivity, `$3.2B` supplier-finance obligation at period-end; annual FY2025 lease/tax cash is context only | H1 denominator remains exposed to tariff/vendor support, supplier-finance timing, maintenance/growth capex, leases, taxes, service costs, and dilution |
| Walmart / H1 FY2027 | `$19.710B` | `$14.181B` | `$5.529B` | `$4.548B` support candidate, `$2.303B` debt-principal sensitivity, `$6.4B` supplier-finance obligation; `$1.087B` new-store category is a narrow growth floor, not a maintenance split | Company-defined FCF is not common-owner cash; the `$13.094B` residual after the narrow new-store floor is mixed spending, not maintenance |

## What the latest filing evidence adds

### Working capital and supplier finance

Target and Walmart disclose period-end supplier-finance obligations, but the
balances are not a matched-period cash adjustment. Walmart's FY2026 annual
filing provides a stronger annual settlement-flow control—`$40.342B` invoices
confirmed and `$40.062B` confirmed invoices paid—while Target's FY2025 filing
reports `$11.426B` invoices confirmed and `$12.066B` confirmed invoices paid.
Those annual flows cannot be assigned to H1 without payment dates and cash-flow
classification. The H1 obligation changes (`+$0.2B` Target and `+$0.4B`
Walmart versus January) remain period-end diagnostics, not owner-cash
deductions.

### Reinvestment

Walmart's H1 categories are `$7.659B` supply chain/customer-facing/
technology/other, `$3.623B` remodels, `$1.087B` new stores/clubs, and `$1.812B`
international. Only the new-store category can serve as a narrow labeled
growth floor; the remainder contains mixed productivity, replacement,
fulfillment, automation, and growth spending. TJX and Target disclose category
direction but not a period-matched maintenance dollar split.

### Leases, taxes, and attached services

Annual lease and tax cash is useful burden context—TJX `$2.214B` lease cash and
`$1.471B` taxes; Target `$529M` and `$1.091B`; Walmart `$2.315B` and `$5.364B`—
but it is not an incremental H1 deduction. The attached-service surfaces
(advertising, membership, marketplace, card, fulfillment, and related income)
still lack comparable legal-entity collection and allocated labor,
technology, working-capital, capex, tax, and senior-claim schedules.

## Promotion gates

| Gate | TJX | Target | Walmart |
|---|---|---|---|
| Same-period OCF/property | observed | observed | observed |
| Working-capital settlement | partial | partial | partial |
| Supplier-finance cash allocation | missing | missing | missing for H1 allocation |
| Maintenance/growth capital | missing | missing | partial; narrow new-store floor only |
| Lease/tax period match | missing | missing | missing |
| Attached-service cash and cost | missing | missing | missing |
| Diluted/common-owner claims | partial | partial | partial, including NCI/debt claims |
| Promotion status | hold | hold | hold |

No company reaches normalized owner cash. The correct result is a range or
reported denominator with missing fields carried explicitly—not a cross-company
multiple based on cash after property.

## Next joinable source by company

- **TJX:** next quarterly or annual filing with supplier-finance, lease/tax,
  service, and capitalized renovation/project detail; do not use the FY2027
  forward category guide as H1 maintenance cash.
- **Target:** matched H1 or next annual payment-date schedules for supplier
  finance, lease, tax, service collection/cost, and maintenance/growth capital.
- **Walmart:** H1 supplier-finance payment allocation, project-level capex or
  maintenance schedule, ecosystem cost/collection allocation, and full
  common-owner claim bridge.

## Decision

Q-04 through Q-06 remain `partial`. The new evidence does improve the
denominator control: annual supplier-finance paid-invoice roll-forwards,
current H1 capex categories, narrow growth floors, and annual lease/tax burden
context are now joined without double counting. The decisive H1 allocation
objects remain undisclosed, so the retail lane stays qualified and unranked.

## Sources

- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)
- [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm)
- [Walmart FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm)
- [TJX FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
- [Retail supplier-finance roll-forward](combined-investment-research-pilot-02-retail-supplier-finance-roll-forward-2026-09-16.md)
- [Retail capex classification boundary](combined-investment-research-pilot-02-retail-capex-classification.md)
- [Retail annual lease/tax cash control](combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md)

Structured companion: [H1 denominator table](data/combined-investment-research-retail-h1-owner-cash-denominator-handoff-2026-09-17.csv).
