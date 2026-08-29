# Capital Flow End-To-End Graph Pass 1

## Purpose

This is the spine artifact for the big-picture research goal.

It asks:

`Can we express the current evidence as source-backed capital-flow rows from capital source to router, wrapper, recipient, use, output, cash outcome, proof level, and missing proof?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-end-to-end-graph-pass-1.csv`

The front-door synthesis is:

`/cluster/capital-flow-research-sprint-answer-synthesis-pass-1.md`

The 519-company money movement map is:

`/cluster/capital-flow-519-company-money-movement-map-pass-1.md`

The debt/refinancing allocation pass is:

`/cluster/capital-flow-debt-refinancing-source-use-cash-allocation-pass-1.md`

The graph upgrade queue is:

`/cluster/capital-flow-end-to-end-graph-upgrade-queue-pass-1.md`

## Meaty End-To-End Goal

`Build a source-backed capital-flow graph that traces money from capital pools to real-economy uses and then to cash outcomes, without skipping proof gates.`

The row shape is:

`capital source -> router -> vehicle/instrument -> recipient -> use of funds -> asset/project/borrower -> output metric -> cash metric -> proof level -> missing proof -> safe claim`

## Current Answer

`The first graph pass has 16 seeded flows. It shows that the evidence system can now describe actual money routes across insurance/private credit, regulated recovery, infrastructure/backlog, tariffed pipelines, debt/refinancing, streaming/PMPA funding, fleet capital, and LNG export infrastructure. The strongest current flows reach source/use/cash-proxy visibility, and Wheaton Antamina reaches named source/use/cash-return proxy visibility. No row is asset-level-return-proven.`

## Proof Levels

| Proof Level | Meaning |
|---|---|
| `source-route-visible-hold` | Source/router/channel is visible, but use and cash allocation are still open. |
| `source-use-destination-visible` | Destination or borrower exposure is visible, but use-of-proceeds and cash return are open. |
| `source-use-commercial-route-visible` | Commercial route/rate is visible, but realized cash is open. |
| `source-use-output-visible` | Source/use/output chain is visible, but cash outcome remains open. |
| `source-use-output-cash-proxy-visible` | Source/use/output and company or category cash proxy are visible. |
| `named-source-use-company-cash-context-visible` | Named source/use is visible with same-period company cash context. |
| `treasury-source-use-cash-coverage-proxy-visible` | Statement-level treasury sources and uses reconcile to cash coverage proxies. |
| `aggregate-source-use-output-cash-proxy-visible` | Aggregate source/use/output/cash bridge is visible, but source-specific allocation is open. |
| `holdco-source-use-restructuring-visible` | Holding-company source/use mechanics are visible, but operating or shareholder return is open. |
| `named-source-use-cash-return-proxy-visible` | Named source/use and asset-level cash-return proxy are visible, but full return proof is open. |

## Seeded Graph

| Flow | Capital Source | Router | Recipient / Asset | Proof Level | Missing Proof |
|---|---|---|---|---|---|
| `CFE2EG-001` | Retirement/Athene inflows | Apollo/Athene | Insurance credit and alternative-investment portfolio | `source-use-cash-proxy-visible` | Asset-level statutory income and borrower cash return |
| `CFE2EG-002` | Insurance liabilities and credit vehicles | KKR / Global Atlantic | Private-credit borrower/holder channels | `source-route-visible-hold` | Borrower facility/use/cash evidence |
| `CFE2EG-003` | BDC/private-credit vehicle capital | Ares | Named borrower exposure | `source-use-destination-visible` | Facility size, use of proceeds, and borrower cash generation |
| `CFE2EG-004` | Private-credit vehicle funding stacks | Blackstone | Credit vehicle investments | `source-route-visible-hold` | Borrower use and cash return |
| `CFE2EG-005` | Regulated recovery and utility capital structure | NextEra/FPL | Distribution Inspection / SPPCRC category | `source-use-output-cash-proxy-visible` | Category customer receipts and funding allocation |
| `CFE2EG-006` | DCF, EBITDA, debt, revolver, growth capex | Energy Transfer | Midstream/export expansion | `source-use-output-cash-proxy-visible` | Project contracts and project EBITDA |
| `CFE2EG-007` | Backlog/RPO, contract liabilities, OCF, credit wrapper | Sterling | Infrastructure project backlog | `source-use-output-cash-proxy-visible` | Funded backlog, margin, and collection |
| `CFE2EG-008` | Customer awards, backlog, working capital, credit | MasTec | Infrastructure project backlog | `source-use-output-cash-proxy-visible` | Owner funding, retainage, and project cash collection |
| `CFE2EG-009` | Tariff-supported shipper payments | Plains | Karnes to Cactus III/Hobson route | `source-use-commercial-route-visible` | Committed volumes and realized revenue |
| `CFE2EG-010` | Bank debt, term loan, revolver, OCF | Wheaton | Antamina PMPA production rights | `named-source-use-cash-return-proxy-visible` | Delivery cash receipts, tax, interest, lender waterfall, IRR/NPV |
| `CFE2EG-011` | 2034 notes, cash, revolver, OCF | PBF | Refining balance sheet and refinery capital context | `named-source-use-company-cash-context-visible` | ABL availability, pro forma debt service, refinery-level cash |
| `CFE2EG-012` | OCF, debt stack, merger cash, liquidity | Devon | E&P capex, acquisition, payouts, debt repayment | `treasury-source-use-cash-coverage-proxy-visible` | Daily source priority, synergy, commodity-stress FCF, asset contribution |
| `CFE2EG-013` | OCF, Credit Agreement, notes, borrowing base | Matador | Development capex, acquisitions, reserve-backed assets | `aggregate-source-use-output-cash-proxy-visible` | Borrowing notices, lender schedule, reserve support, asset cash |
| `CFE2EG-014` | Margin loan, restricted cash, Charter loan, debt proceeds | Liberty Broadband | Holdco debenture retirement and collateral structure | `holdco-source-use-restructuring-visible` | LTV, funds-flow, tax, merger close, shareholder realization |
| `CFE2EG-015` | Fleet cash flow, ABL, AR securitization, liquidity | United Rentals | Rental fleet and Yak/Matting platform | `source-use-output-cash-proxy-visible` | Growth/replacement capex, category margin, utilization, ROIC |
| `CFE2EG-016` | Equity-funded growth capital, project debt, LNG commercialization | Cheniere | LNG trains and export infrastructure | `source-use-output-visible` | Train-level cash receipts, EBITDA, return |

## What This Lets Us Answer

The graph can now answer the user's real question in one controlled format:

`who is investing, where the money starts, who routes it, what wrapper carries it, what it enters, what output is visible, what cash proxy is visible, and what proof is still missing.`

It also prevents the most dangerous shortcut:

`cash proxy evidence is not asset-level cash-return proof.`

## Decision

`capital-flow-end-to-end-graph-seeded`

The evidence system now has a first graph-shaped spine with `16` flows. Future extraction passes should either add new rows to this graph or upgrade existing rows to stronger proof levels.

## Safe Claim

`The current capital-flow evidence graph has 16 seeded flows across private credit, insurance, regulated recovery, infrastructure, debt/refinancing, streaming, fleet capital, and LNG. It can show source, router, wrapper, use, output, cash proxy, proof level, and missing proof for selected cases. It does not prove asset-level cash return across the full 519-company universe.`

## Next Work

1. Upgrade `CFE2EG-010` Wheaton Antamina toward full cash-return proof only after delivery, cash receipt, tax, interest, and debt-service allocation are joined.
2. Upgrade `CFE2EG-005` FPL by pursuing category customer receipts, billing determinants, and source-of-funds allocation.
3. Upgrade `CFE2EG-003` Ares by reconstructing facility size, use of proceeds, borrower cash generation, and residual bank role.
4. Upgrade `CFE2EG-006` and `CFE2EG-007` by adding project contracts, customer payments, project EBITDA, backlog margin, and collection evidence.
5. Add queued 519-company rows only when they have enough source evidence to populate the same graph schema without weakening the proof standard.
