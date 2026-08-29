# Capital Flow Next Source Acquisition Queue Pass 1

## Purpose

This page converts the completed source-route execution status into the next acquisition queue.

It asks:

`Which primary source packages should be pursued first to answer who is investing where, how the money moves, what it funds, who gets paid back, and whether cash comes back from the funded asset or activity?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-next-source-acquisition-queue-pass-1.csv`

The status input is:

`/cluster/capital-flow-source-route-execution-status-pass-1.md`

## Short Answer

`The next meaty end-to-end goal is to acquire and extract the source packages that close the route from capital provider to instrument to use to operating asset to customer cash to payback or return. The first queue has 5 acquisition packages. Customer receipts and collection evidence comes first because it is the biggest blocker between visible demand, recovery, backlog, tariff, or volume evidence and actual cash-realization proof.`

## Acquisition Queue

| Queue | Rank | Source Package | Target Cases | Pass Test | Status |
|---|---:|---|---|---|---|
| `CFNSAQ-001` | `1` | Customer receipts, billing determinants, receivable aging, and collection schedules | FPL, Sterling, MasTec, Energy Transfer, Plains | Named customer or payer cash tied to a named category, project, route, or backlog cohort | `executed-current-local-hold` |
| `CFNSAQ-002` | `2` | Project/asset cash contribution and return schedules | Cheniere, Energy Transfer, Matador, PBF, MasTec, Plains | Standalone project, asset, route, train, reserve area, or backlog-cohort cash contribution is visible | `executed-current-local-hold` |
| `CFNSAQ-003` | `3` | Debt-service waterfalls, lender allocation, source-to-use ledgers, and transaction close support | Wheaton, Cheniere, Energy Transfer, Matador, PBF, Liberty Broadband, Devon, Plains | Source cash and repayment or debt-service path are tied to named capital providers and named uses | `executed-current-local-mixed-partial-hold` |
| `CFNSAQ-004` | `4` | Statutory legal-entity schedules, borrower facility files, and collateral availability | Apollo/Athene, KKR/Global Atlantic, Ares, Blackstone, Matador, United Rentals, Liberty Broadband | Legal-entity asset holding or borrower facility cash path is visible with collateral or lender allocation support | `executed-current-local-mixed-partial-hold` |
| `CFNSAQ-005` | `5` | Return model support: IRR, NPV, ROIC, reserve life, and earned return | Wheaton, FPL, United Rentals, Energy Transfer, Matador, Plains | Full return model ties invested capital to cash yield or earned return at asset, project, route, fleet, or reserve level | `executed-current-local-mixed-partial-hold` |

## Why Customer Receipts Come First

The system can already show many upstream facts: financing capacity, capex, backlog, tariff route, regulated recovery, production volume, or company cash proxy. The gap is that those facts still do not show cash paid by a customer or payer for the specific funded activity.

`CFNSAQ-001` therefore targets the evidence that can turn proxy rows into stronger cash-realization rows:

- FPL: billing determinants, rate-class allocation, customer collections, and later true-up support for Distribution Inspection.
- Sterling and MasTec: receivable aging, retainage collection, customer collection records, and project-owner funding evidence.
- Energy Transfer and Plains: shipper billing, tariff billing, route revenue, and throughput billing support.

## End-To-End Proof Standard

The queue is designed around the full money-movement question:

`capital provider -> instrument -> source of funds -> named use -> operating asset/project/route/fleet/reserve -> customer or payer cash -> debt service, equity return, or reinvestment`

A row should not be upgraded to full cash-return proof unless it joins the same-period source, use, output, cash, and payback or return evidence at row level.

## Decision

`next-source-acquisition-queue-ready`

The completed source-route status is now converted into five ranked acquisition packages. The next execution pass should start with `CFNSAQ-001`.

The `CFNSAQ-001` execution pass is:

`/cluster/capital-flow-cfnsaq-001-customer-receipts-acquisition-pass-1.md`

The `CFNSAQ-002` execution pass is:

`/cluster/capital-flow-cfnsaq-002-project-asset-cash-contribution-pass-1.md`

The `CFNSAQ-003` execution pass is:

`/cluster/capital-flow-cfnsaq-003-debt-service-lender-allocation-pass-1.md`

The `CFNSAQ-004` execution pass is:

`/cluster/capital-flow-cfnsaq-004-statutory-facility-collateral-pass-1.md`

The `CFNSAQ-005` execution pass is:

`/cluster/capital-flow-cfnsaq-005-return-model-support-pass-1.md`

The consolidated execution synthesis is:

`/cluster/capital-flow-cfnsaq-execution-synthesis-pass-1.md`

## Safe Claim

`The next-source acquisition queue ranks the primary source packages most likely to improve the capital-flow proof graph. It does not acquire those sources, prove customer receipts, prove legal-entity borrower cash paths, or prove asset-level cash returns.`

## Next Work

1. Use `/cluster/capital-flow-cfnsaq-001-customer-receipts-acquisition-pass-1.md` as the current local receipt test.
2. Use `/cluster/capital-flow-cfnsaq-002-project-asset-cash-contribution-pass-1.md` as the current local project/asset contribution test.
3. Use `/cluster/capital-flow-cfnsaq-003-debt-service-lender-allocation-pass-1.md` as the current local debt-service/lender allocation test.
4. Use `/cluster/capital-flow-cfnsaq-004-statutory-facility-collateral-pass-1.md` as the current local statutory/facility/collateral test.
5. Use `/cluster/capital-flow-cfnsaq-005-return-model-support-pass-1.md` as the current local return-model test.
6. Build a consolidated execution synthesis across `CFNSAQ-001` through `CFNSAQ-005`.
