# Capital Flow Capital-Intensive Project/Cash Extraction Pass 1

## Purpose

This pass starts executing the project/cash queue for the capital-intensive buildout lane.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-project-cash-extraction-pass-1.csv`

The goal is to move beyond:

`This company is high-signal.`

And into:

`Which source-backed number shows capital becoming a project, asset, backlog, fleet, material volume, network, regulated system, or cash-producing throughput?`

## What This Pass Adds

This pass adds `15` extracted rows across the same `15` buildout companies:

| Evidence Type | Companies | Why It Matters |
|---|---|---|
| growth/maintenance capex | Energy Transfer | The cleanest current split between growth spend and maintenance spend. |
| project schedule / milestone | Cheniere | LNG train completions, cargoes, capacity, DCF, and capital deployment line up directionally. |
| fleet capex and cash conversion | United Rentals | Gross rental capex, free cash flow, fleet productivity, leverage, and liquidity are all visible. |
| backlog and project mix | Sterling, Jacobs, AECOM, KBR | Capital plans become work only if backlog is funded, executable, and cash-converting. |
| materials throughput | Nucor, Steel Dynamics, Knife River, Reliance | Capex and demand show up as tons, reserves, processing, public-funded backlog, inventory, and cash flow. |
| electrical/instrumentation equipment | Eaton, Teledyne | AI, electrification, aerospace, defense, sensing, and resilience demand require physical equipment and funded backlog. |
| telecom network capex | Verizon | Digital demand still requires capital-heavy networks and a large debt stack. |
| regulated replacement capital | ONE Gas | Gas distribution capital is about system integrity, rate recovery, customer extensions, and allowed economics. |

## Status Buckets Used

| Bucket | Meaning |
|---|---|
| `capex-visible` | A capex or capacity-investment amount is visible, but the growth/maintenance split or cash conversion is incomplete. |
| `growth-maintenance-split` | Growth and maintenance capex are separated at least at first-pass level. |
| `project-scheduled` | A named project, capacity addition, train, expansion, or in-service milestone is visible. |
| `contracted-or-regulated` | Backlog, contract, public funding, tariff, rate, or recovery language is visible, but full cash conversion is not yet proven. |
| `cash-converting` | Cash flow, free cash flow, DSO, fleet metrics, working capital, or debt/liquidity evidence is visible alongside the operating claim. |

## Extraction Summary

| ID | Company | Status Bucket | Strongest Metric | Safe Claim | Missing Proof |
|---|---|---|---|---|---|
| CIPE-001 | Energy Transfer | `growth-maintenance-split` | Q2 2026 growth capex `1.10B USD`; maintenance capex `307M USD`; 2026 growth capex guide `5.6B-5.9B USD`; Nederland/Lone Star/y-grade capacity metrics | Midstream capital is being redirected toward named bottleneck-clearing assets and contracted capacity. | Project costs, financing stack, contract terms, debt maturities, return expectations. |
| CIPE-002 | Cheniere | `project-scheduled` | Sabine Pass `30 mtpa`; Corpus Christi `15 mtpa`; `670` FY2025 cargoes; Stage 3 train completions; FY2025 DCF `5.3B USD` | LNG capital is becoming train capacity, export throughput, and cash-flow capacity. | SPA table, project debt, train-level capex, utilization, regulatory approval detail. |
| CIPE-003 | United Rentals | `cash-converting` | FY2025 free cash flow `2.181B USD` after gross rental capex `4.189B USD`; Q2 YTD gross rental capex `2.931B USD`; leverage `1.8x` | Rental fleet is a real capital-absorption and access model, not just a construction demand proxy. | OEC, utilization, fleet age, gross-to-net capex bridge, debt maturities. |
| CIPE-004 | Sterling Infrastructure | `contracted-or-regulated` | Q2 backlog `4.33B USD`; combined backlog `5.62B USD`; mission-critical `92%` of E-Infrastructure backlog | Data-center, semiconductor, and manufacturing capital is reaching field execution. | Funded backlog, customer/project list, margins, working capital, acquisition split. |
| CIPE-005 | Nucor | `capex-visible` | FY2025 capex `3.42B USD`; 2026 capex expectation `2.50B USD`; outside steel mill sales `19.848M tons` | Domestic steel capacity is absorbing large capital while producing high physical throughput. | Growth/maintenance split, utilization, project list, returns. |
| CIPE-006 | Steel Dynamics | `cash-converting` | FY2025 operating cash flow `1.450B USD`; record shipments `13.7M tons`; fabrication backlog nearly `45%` above prior year | Domestic buildout is visible through shipments, fabrication backlog, recycling, processing, and aluminum expansion. | Capex table, aluminum project schedule, utilization, backlog contract quality. |
| CIPE-007 | Knife River | `contracted-or-regulated` | `1.3B` tons reserves; FY2025 backlog `1.0B USD`; `89%` publicly funded; H1 growth initiatives `244.5M USD` | Public infrastructure funding is becoming aggregates, contracting backlog, reserves, acquisitions, and greenfields. | DOT/customer mapping, project timing, reserve additions, debt maturities. |
| CIPE-008 | Reliance Steel & Aluminum | `cash-converting` | FY2025 tons sold `6.4M`; capex `328.9M USD`; operating cash flow `831.4M USD`; Q2 tons sold +`10.8%` YoY | The service-center layer converts project demand into local metal processing, inventory, and delivery speed. | Inventory, receivables, revolver use, capex-by-location, customer/project mix. |
| CIPE-009 | Jacobs | `contracted-or-regulated` | Backlog rose to `28.9B USD`; RPO about `22.2B USD`; liquidity `1.17B USD` cash plus `1.50B USD` revolver | Advanced-facilities, data-center, semiconductor, power, water, and transport spend becomes engineering backlog. | Funded backlog, contract assets/liabilities, cash flow, capex, debt. |
| CIPE-010 | AECOM | `cash-converting` | FY2025 FCF `685M USD`; Q2 backlog `26.204B USD`; Q2 FCF negative `27M USD` due to timing/claims | Infrastructure design and program-management demand is real, but backlog must be checked against cash conversion. | DSO, funded status, contract assets, claims, debt, customer funding source. |
| CIPE-011 | KBR | `contracted-or-regulated` | FY2025 backlog `16.864B USD`; award options `6.347B USD`; Q2 backlog `17.805B USD`; contract-type split | Program-complexity demand is visible, but contract type and portfolio separation govern margin quality. | Funded/unfunded split, working capital, debt, cash flow, STS project economics. |
| CIPE-012 | Eaton | `capex-visible` | FY2025 sales `27.448B USD`; `13B USD` acquisitions; `1.5B USD` North American capacity investment | Electrification and AI-related demand require physical power equipment, capacity, and M&A. | Exact orders, backlog, acquisition funding, debt, project locations, schedule. |
| CIPE-013 | Teledyne | `cash-converting` | Q2 funded backlog about `5.0B USD`; Q2 FCF `284.7M USD`; leverage `1.1x` | Buildout demand includes sensing, imaging, surveillance, marine, environmental, defense, and mission systems. | Segment orders/backlog, capex, acquisition funding, customer duration. |
| CIPE-014 | Verizon | `cash-converting` | FY2025 operating cash flow `37.1B USD`; FCF `20.1B USD`; capex `17.0B USD`; net unsecured debt `110.1B USD` | Digital demand still depends on physical network capex and balance-sheet capacity. | Capex category, fiber/spectrum split, Frontier funding, debt ladder, return metrics. |
| CIPE-015 | ONE Gas | `contracted-or-regulated` | FY2025 capex/asset removal `759.5M USD`; new rates and normalization mechanisms; line extensions/customer growth | Regulated gas networks absorb recurring replacement, integrity, extension, and recoverable capital. | Rate cases, rate base, allowed ROE, rider recovery, debt/equity funding. |

## What The Evidence Says Now

The capital-intensive lane now has three layers:

1. `First-pass ledger`: identifies the `15` companies and their buildout role.
2. `Project/cash queue`: defines what source tables must be pulled next.
3. `Project/cash extraction pass 1`: classifies the currently visible evidence by proof type.

The most advanced rows right now are:

- Energy Transfer, because growth and maintenance capex are separated and tied to named capacity additions.
- United Rentals, because fleet capex, free cash flow, productivity, leverage, and liquidity sit in the same packet.
- Cheniere, because LNG capacity, cargoes, train completions, DCF, and capital deployment are visible together.
- AECOM, because the packet shows both backlog strength and a cash-conversion warning, which is exactly the kind of two-sided evidence this project needs.

## What Claims We Can Derive

Safe claim:

`Capital-intensive buildout is not one story. Some capital is entering physical assets directly, some is entering service backlog, some is entering materials throughput, some is entering rental fleet, and some is entering regulated replacement systems.`

Sharper claim:

`The strongest near-term evidence is where project/capacity metrics and cash/funding metrics appear together: Energy Transfer, Cheniere, United Rentals, Teledyne, Verizon, Steel Dynamics, Reliance, and AECOM.`

Boundary:

`A row can be cash-converting without being project-and-cash-grade. It still needs source-table extraction, exact definitions, project schedules, debt/funding detail, and outside denominators.`

## Next Pass

The next pass should start with four rows:

1. Energy Transfer: project table, capex table, contracted-volume terms, debt/funding stack.
2. Cheniere: train-level capex, SPA maturity table, project debt, DCF allocation.
3. United Rentals: OEC, gross/net rental capex, fleet utilization, debt maturity.
4. Sterling: signed versus combined backlog, funded status, customer/project mix, working-capital conversion.

These four give the best spread across the lane:

- midstream project capex
- LNG expansion
- rental fleet access
- specialty construction backlog

Together they test the central question:

`When money is committed to build the physical economy, who actually absorbs it, and what evidence proves that absorption is turning into capacity and cash?`
