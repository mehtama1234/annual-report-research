# Capital Flow Power/Grid Customer Contract Receipt Workbench Pass 1

## Purpose

This pass executes the next action from:

`/cluster/capital-flow-power-grid-data-center-customer-cash-map-pass-1.md`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-power-grid-customer-contract-receipt-workbench-pass-1.csv`

The question is:

`Which exact contract, billing, receipt, project, or supplier documents would move the power/grid/data-center theme from evidence bridge to named cash proof?`

## Short Answer

The power/grid/data-center lane is now a document workbench with `12` proof targets.

The strongest target remains FPL customer recovery because public regulatory filings expose the most receipt-adjacent route. AEP and Duke are the best data-center load-to-capital routes. Sterling and MasTec are the best contractor cash-conversion routes. Turbine procurement is the best supplier route. NextEra/Meta is the best named hyperscaler contract route.

The current answer is:

`We can see demand, tariffs, ESAs, capital plans, procurement, project approval, recovery factors, contractor backlog, and aggregate customer-revenue proxies. We still cannot prove named customer receipts, project-level billing, contractor cash collection, supplier cash, debt waterfalls, or asset-level returns.`

## The Workbench Logic

Each row is built around a strict promotion test:

`current evidence -> decisive missing document -> exact fields -> pass test -> hold/fail test`

This matters because the power/grid story is easy to overstate.

It is tempting to say:

`data centers need power, so utilities and contractors will make money`

The safer document-backed version is:

`large-load demand appears to be moving into utility and infrastructure money paths, but each path needs customer contracts, billing determinants, collected receipts, project approvals, contractor collections, supplier orders, or return models before it becomes named cash proof.`

## Ranked Workbench

| Priority | Target | Current Evidence | Decisive Document Needed | Pass Test | Current Status |
|---:|---|---|---|---|---|
| 1 | FPL SPPCRC current docket | Docket 20260010-EI has a current public route with `138` filing records. | Full docket inventory plus workpaper map. | Identify filing/workpaper families likely to hold billing determinants or receipt schedules. | `docket_route_visible` |
| 2 | FPL Distribution Inspection receipts | `804.620369M USD` 2025 aggregate SPPCRC revenue and `1.000979763B USD` 2026 aggregate clause-revenue route are visible. | Category receipt ledger or allocation workpaper. | Reconcile Distribution Inspection recovery to billed or collected customer cash by period/rate class. | `aggregate_cash_proxy_visible` |
| 3 | FPL billing determinant math | 2027 Form 4P/Form 5P billing-base proxies are visible. | Actual billing determinant schedules. | Reconcile billing units, factors, billed dollars, actual revenue, and category allocation. | `billing_base_proxy_visible` |
| 4 | AEP Ohio data-center tariff obligation | Tariff, `25,000 kW` threshold, `10,000-100,000 USD` study fee, and reimbursement mechanics are visible. | Executed or redacted LOA/ESA/application package. | Show a large-load customer accepting payment, collateral, minimum-demand, or reimbursement obligations. | `customer_obligation_gate_visible` |
| 5 | AEP load-to-capital allocation | `69 GW` load bridge, `$78B` capital plan, and `13 GW` secured turbines are visible. | Project allocation table by load/customer class, utility, state, approval, and recovery route. | Link one load-driven project to customer obligation, capex, approval/recovery, and in-service timing. | `approved_recovery_pathway_visible` |
| 6 | Duke secured ESA cash route | `7.6 GW` secured ESAs, about `5 GW` under construction, `$103B` capital plan, and `20` turbines are visible. | ESA split by utility/project/customer class with obligation and billing terms. | Tie secured ESA rows to customer obligation, construction, billing, and recovery treatment. | `secured_load_pathway_visible` |
| 7 | Duke Anderson County | `1.365 GW` approval with co-owner allocations is visible. | Final order conditions plus construction/cost/recovery schedules. | Link approval, ownership, cost, recovery treatment, in-service timing, and earned return. | `named_project_approval_visible` |
| 8 | NextEra/Meta contracted projects | `2.5 GW`, `13` projects, `11` PPAs, `2` ESAs, and `2026-2028` online window are visible. | Project-level PPA/ESA/interconnection/regulatory package. | Link named customer, contract, output, capex/financing, price/cash, and in-service timing. | `named_customer_contract_visible` |
| 9 | Sterling project-owner cash collection | Contract-liability and RPO evidence is visible, including `646.306M USD` net contract liability and `4.233618B USD` RPO. | Project-owner funding and collection schedule. | Link backlog to owner funding, billings/collections, retainage, margin, and risk support. | `contractor_backlog_cash_proxy_visible` |
| 10 | MasTec backlog cash conversion | `21.4B USD` backlog, `4.374B USD` revenue, `384.2M USD` adjusted EBITDA, and `760.912M USD` contract liabilities are visible. | Segment backlog and working-capital collection schedules. | Tie backlog conversion to segment revenue, margin, working capital, and cash collection. | `contractor_backlog_cash_proxy_visible` |
| 11 | Turbine/equipment supplier cash route | AEP and Duke secured turbine evidence is visible. | Procurement contract or supplier disclosure. | Link utility orders to supplier backlog, deposits, delivery, revenue, or cancellation economics. | `physical_procurement_visible` |
| 12 | Outside denominator validation | Company and docket examples are visible, but broad scale is not normalized. | EIA/FERC/ISO/state crosswalk. | Compare company examples against independent grid, load, plant, rate-base, and sales denominators. | `outside_denominator_needed` |

## Best First Extraction

The best first extraction is:

`FPL SPPCRC docket inventory and billing determinant workpaper map`

The first follow-through map is:

`/cluster/capital-flow-fpl-sppcrc-docket-billing-workpaper-map-pass-1.md`

Reason:

1. FPL has the most public receipt-adjacent source route.
2. The current docket is identified.
3. The local evidence already narrowed the missing proof to billing determinants, category allocation, and receipt support.
4. A pass would upgrade the strongest customer-cash route in the whole power/grid theme.

The required output should be:

| Field | Why It Matters |
|---|---|
| Docket filing ID | Anchors every source to a public filing. |
| Filing title/sponsor | Separates testimony, petition, order, discovery, and workpaper sources. |
| Confidential status | Tells us whether the proof is public or blocked. |
| Form/schedule | Identifies factor, revenue, billing determinant, or category schedule. |
| Rate class | Needed to connect factors to customer billing. |
| Billing units | Needed to compute billed revenue. |
| Billed dollars | Converts tariff/factor authority into customer billing. |
| Collected dollars | Converts billed revenue into cash receipt proof. |
| Category allocation | Needed to isolate Distribution Inspection rather than total SPPCRC. |
| True-up bridge | Reconciles actual vs projected recovery. |

## Best Second Extraction

The best second extraction is:

`AEP Ohio large-load customer obligation packet`

Reason:

AEP is the cleaner data-center tariff route. The current evidence already shows:

- effective data-center tariff
- `25,000 kW` threshold
- `10,000-100,000 USD` study fee
- cancellation or delay reimbursement mechanics

The missing source is not another load chart. It is an executed or redacted customer obligation instrument.

## Best Third Extraction

The best third extraction is:

`Duke ESA and Anderson County project-cash packet`

Reason:

Duke has both aggregate secured data-center load and a named generation approval. That gives two paths:

1. customer-backed load path through ESAs
2. named project path through Anderson County

The upgrade requires the cash bridge between those paths: customer obligations, project costs, recovery treatment, in-service timing, and earned return.

## Why Contractor Rows Matter

Sterling and MasTec answer a different part of the theme:

`Who gets paid to build the system?`

Utilities may own the assets, but contractors and suppliers can be the operating beneficiaries. The workbench therefore keeps two contractor rows:

| Company | Best Current Evidence | Missing Proof |
|---|---|---|
| Sterling | `646.306M USD` net contract liability, `4.233618B USD` RPO, favorable contract timing proxies. | Project-owner funding, collections, retainage, margin, and risk support. |
| MasTec | `21.4B USD` backlog, `4.374B USD` Q2 revenue, `384.2M USD` adjusted EBITDA, `760.912M USD` contract liabilities. | Segment backlog, working-capital collection, funded status, and project margin. |

## Safe Claim

`The power/grid/data-center lane now has a contract and receipt workbench. It identifies the exact document families that would promote the theme: FPL billing determinants and category receipt support, AEP executed large-load obligations, Duke ESA/project recovery schedules, NextEra/Meta project contract economics, Sterling/MasTec project-owner collections, turbine supplier order cash, and outside denominators. The current evidence supports route selection and bridge claims, not named customer cash proof.`

## Decision

`power-grid-customer-contract-receipt-workbench-ready-fpl-docket-inventory`
