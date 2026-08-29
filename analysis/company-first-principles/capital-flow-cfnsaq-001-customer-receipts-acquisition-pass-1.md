# Capital Flow CFNSAQ-001 Customer Receipts Acquisition Pass 1

## Purpose

This page executes the first row of the next-source acquisition queue.

It asks:

`Do the current local sources prove named customer or payer cash receipts for FPL, Sterling, MasTec, Energy Transfer, or Plains?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cfnsaq-001-customer-receipts-acquisition-pass-1.csv`

The queue input is:

`/cluster/capital-flow-next-source-acquisition-queue-pass-1.md`

## Short Answer

`CFNSAQ-001 is executed against the current local source set. It does not produce full named customer-receipt proof for any of the five target cases. FPL reaches partial aggregate recovery-collection status; Sterling and MasTec remain timing and working-capital proxy cases; Energy Transfer and Plains remain below named shipper/customer billing and realized route or project revenue.`

## Execution Result

| Row | Target Case | Current Evidence | Result | What Still Blocks Proof |
|---|---|---|---|---|
| `CFNSAQ001-001` | FPL Distribution Inspection | `804.620369M USD` aggregate SPPCRC clause revenue; `65.318726M USD` aggregate true-up collected/refunded; category cost/output/recovery/component evidence | `partial-aggregate-recovery-collection-proxy` | Distribution Inspection-specific receipts, billing determinants, rate-class allocation, customer bill support, category collection schedule, source-of-funds allocation |
| `CFNSAQ001-002` | Sterling backlog | Q2 `2026` contract liabilities of `802.601M USD`; contract assets of `156.295M USD`; net contract-liability timing of `646.306M USD`; positive OCF less capex | `hold-no-retainage-or-project-collection-proof` | Retainage aging, retainage collection history, receivable aging, named owner collections, backlog-cohort cash collection, project margin, bonded backlog, actual L/C or surety usage |
| `CFNSAQ001-003` | MasTec backlog | Q2 `2026` backlog of `21.4B USD`; contract liabilities of `760.912M USD`; Q2 revenue of `4.374B USD`; adjusted EBITDA of `384.2M USD`; H1 OCF of `120.322M USD`; DSO of `72` | `hold-no-receivable-aging-or-backlog-cohort-collection-proof` | Retainage disclosure, receivable aging, project collection history, backlog-cohort billing, customer collection records, funded-award support, project margin |
| `CFNSAQ001-004` | Energy Transfer projects | Q2 `2026` company EBITDA/DCF/capex and named project/volume context | `hold-no-shipper-customer-cash` | Named-project shipper billing, customer cash, route revenue, committed-volume billing, project EBITDA, source-to-project allocation |
| `CFNSAQ001-005` | Plains tariff route | Effective `2026-07-01` tariff route and `178.98` cents per barrel base rate for Karnes County to Cactus III/Hobson | `hold-no-route-billing-or-realized-revenue` | Committed shipper volume, shipper identity, realized route revenue, billing volume, cash receipt, segment cash contribution |

## What This Answers

The first customer-receipt acquisition pass shows that the system is close in some lanes but still not at cash-receipt proof:

- FPL has the strongest receipt-adjacent evidence because aggregate SPPCRC collection mechanics are visible.
- Sterling and MasTec show project-execution and working-capital timing, but not named owner collection.
- Energy Transfer shows company-level cash generation and project context, but not named shipper cash.
- Plains shows the rate and route, but not billed barrels or cash received.

## Next Sources

| Target | Next Source |
|---|---|
| FPL | `2027` SPPCRC actual/estimated filing, billing determinants, rate-class allocation, category allocation workpapers, customer bill and collection support, financing allocation support |
| Sterling | Retainage aging, receivable aging, collection history, named owner collection schedules, bonded backlog, actual L/C and surety usage, project margin support |
| MasTec | Receivable aging, retainage disclosures, backlog-cohort billing, collection history, customer award funding, project margin, source-to-project credit allocation |
| Energy Transfer | Shipper contracts, route billing, tariff billing volumes, customer invoices or settlements, project EBITDA bridge, throughput-to-revenue support |
| Plains | Shipper contracts, committed-volume support, tariff billing records, route throughput, segment cash contribution, Cactus III route revenue support |

## Decision

`cfnsaq-001-executed-current-local-hold`

The queue row is executed against current local evidence. The next work should either fetch new primary customer/billing documents or move to `CFNSAQ-002` if no receipt-level source can be acquired immediately.

## Safe Claim

`The current local source set does not prove named customer or payer cash receipts for the five CFNSAQ-001 target cases. FPL has partial aggregate collection mechanics; the other four cases remain receipt holds with useful proxy evidence.`

## Next Work

1. Try the FPL receipt route first because it has the strongest regulatory trail and a likely `2027` follow-up source.
2. In parallel, identify whether Sterling and MasTec disclose receivable aging or retainage collection in later filings.
3. Keep Energy Transfer and Plains below receipt proof unless shipper billing or realized route/project revenue is visible.
