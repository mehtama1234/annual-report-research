# Capital Flow Customer Receipts Billing Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-001`.

It asks:

`Can current local evidence prove customer receipts or billing support for FPL, Sterling, Energy Transfer, MasTec, and Plains, or does each row still hold at proxy level?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-customer-receipts-billing-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full customer-receipt upgrade yet. The local evidence gives strong proxies: FPL has aggregate clause revenue and true-up mechanics, Sterling and MasTec have backlog/revenue/contract-timing evidence, Energy Transfer has company DCF/EBITDA and named capacity additions, and Plains has tariff route/rate evidence. None of the five rows currently proves named category, project, route, or backlog-cohort customer cash receipts.`

## Row Outcomes

| Row | Case | Current Local Evidence | Customer Receipt / Billing Result | Next Source Needed |
|---|---|---|---|---|
| `CFCRBSR-001` | FPL Distribution Inspection | Aggregate SPPCRC revenue, final recovery components, true-up line, rate-factor authority | Hold with regulated-recovery proxy | Billing determinants, category allocation workpapers, customer bill/collection support for Distribution Inspection |
| `CFCRBSR-002` | Sterling backlog | RPO/backlog growth, contract-liability timing, OCF less capex, L/C/surety wrapper | Hold with backlog-to-company-cash proxy | Named owner funding, signed contract schedules, retainage/receivable collection, project billing and margin |
| `CFCRBSR-003` | Energy Transfer projects | Company EBITDA/DCF, growth capex, refinancing, Nederland/Lone Star/y-grade capacity evidence | Hold with company/project proxy | Shipper/customer contracts, tariff/fee billing records, utilization, project revenue, project EBITDA/DCF |
| `CFCRBSR-004` | MasTec backlog | Backlog, revenue, EBITDA, OCF, DSO, contract liabilities, liquidity/debt context | Hold with backlog-to-revenue/cash proxy | Owner budgets, customer contracts, retainage/receivable aging, backlog-cohort billing and collection |
| `CFCRBSR-005` | Plains tariff route | Texas RRC tariff route/rate, negotiated-rate mechanic, Cactus III capacity/acquisition/control context | Hold with tariff-route/rate proxy | Committed shipper contracts, open-season results, tariff billing records, route throughput, realized route revenue |

## Decision

`customer-receipts-billing-source-route-hold`

`CFRMSWO-001` is executed against the current local source set. It does not upgrade any affected row to receipt-proof status, but it narrows the next source route for each row.

## Safe Claim

`The customer receipts and billing support pass confirms that FPL, Sterling, Energy Transfer, MasTec, and Plains have recovery, backlog, company-cash, capacity, or tariff proxies, but current local evidence does not prove named customer cash receipts, route billing, project collection, or backlog-cohort cash realization for any of the five rows.`

## Next Work

1. Search/fetch FPL SPPCRC billing determinants and category allocation workpapers.
2. Search/fetch Sterling and MasTec owner funding, retainage, receivable aging, and project billing support.
3. Search/fetch Energy Transfer and Plains shipper contracts, tariff billing, route throughput, and realized route revenue.
4. If no receipt/billing sources are available, move to `CFRMSWO-002` source-to-use allocation.
