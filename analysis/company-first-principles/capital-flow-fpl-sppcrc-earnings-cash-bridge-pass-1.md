# Capital Flow FPL SPPCRC Earnings/Cash Bridge Pass 1

## Purpose

This page tests the next hard FPL question:

`After final factor-order, final true-up, and physical-output evidence, can we prove realized earnings or cash conversion for the same storm-protection recovery chain?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-sppcrc-earnings-cash-bridge-pass-1.csv`

## Short Answer

Not fully.

The Q2 2026 NextEra source package gives strong FPL-wide earnings, cash-flow, capex, regulatory-capital-employed, regulatory ROE, receivable, regulatory-asset, debt, and rate-stabilization evidence. It does not isolate SPPCRC category-level earnings, customer receipts, financing source, or project IRR.

This is still a useful upgrade. The FPL chain now has:

- SPPCRC category recovery rows
- factor/WACC/true-up rows
- final true-up rows
- final factor-order and tariff-authorization rows
- AP-1/AP-2 physical-output and variance rows
- FPL-wide earnings/cash/asset/financing context

The missing link is attribution.

## Source Package

| Source | Local Path | Status |
|---|---|---|
| NextEra Q2 2026 earnings release | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/q2-2026/nextera-2026-q2-earnings-release.pdf` | fetched and extracted |
| NextEra Q2 2026 prepared remarks | `raw/primary-sources/capital-flow/power-grid-pilot/nextera/q2-2026/nextera-2026-q2-prepared-remarks.pdf` | fetched and extracted |

## Extracted Evidence

| Family | Period | Metric | Value |
|---|---|---|---:|
| income statement | Q2 2026 | FPL operating revenues | `4896M USD` |
| income statement | Q2 2026 | FPL operating income | `1822M USD` |
| income statement | Q2 2026 | FPL net income attributable to NextEra Energy | `1412M USD` |
| cost recovery expense | Q2 2026 | FPL depreciation and amortization | `1029M USD` |
| financing cost | Q2 2026 | FPL interest expense | `349M USD` |
| construction return | Q2 2026 | FPL allowance for equity funds used during construction | `58M USD` |
| income statement | H1 2026 | FPL operating revenues | `9167M USD` |
| income statement | H1 2026 | FPL net income | `2874M USD` |
| cash flow | H1 2026 | FPL net cash provided by operating activities | `5388M USD` |
| capex | H1 2026 | capital expenditures of FPL | `5780M USD` |
| cash-flow adjustment | H1 2026 | cost recovery clauses and franchise fees | `-7M USD` |
| cash-flow adjustment | H1 2026 | recoverable storm-related costs | `-19M USD` |
| asset base | June 30 2026 | FPL property, plant and equipment, net | `85930M USD` |
| receivables | June 30 2026 | FPL customer receivables, net | `2016M USD` |
| regulatory assets | June 30 2026 | FPL regulatory assets, current plus noncurrent | `7478M USD` |
| financing | June 30 2026 | FPL long-term debt | `30188M USD` |
| regulatory return | Q2 2026 | FPL regulatory capital employed growth | `9.3%` |
| capex | Q2 2026 | FPL capital expenditures | `2800M USD` |
| capex | FY 2026 expectation | FPL capital investments expected range midpoint | `12500M USD` |
| regulatory return | 12 months ending June 2026 | FPL reported ROE for regulatory purposes | `11.7%` |
| timing mechanism | Q2 2026 | rate stabilization mechanism reversal | `110M USD` |
| timing mechanism | Q2 2026 | rate stabilization mechanism after-tax balance | `1300M USD` |
| demand context | Q2 2026 | FPL average customer growth | `90000 customers` |
| billing determinant context | Q2 2026 | FPL weather-normalized retail sales growth | `0.6%` |

## What This Answers

The strongest answer is:

`FPL-wide earnings and cash conversion are visible, and management says regulatory capital employed growth was a significant driver of FPL EPS growth. But the public Q2 2026 earnings package does not allocate that earnings/cash conversion to SPPCRC categories such as Distribution Inspection, Transmission Inspection, feeder hardening, or vegetation management.`

So the FPL lane improves from:

`approved recovery and physical output`

to:

`approved recovery, physical output, and utility-wide earnings/cash context`

It does not improve to:

`SPPCRC category-level realized return`

## What The Bridge Proves

It proves that the broader FPL utility platform had:

- utility-wide operating revenue and net income
- utility-wide operating cash flow
- large capital expenditures and expected capital investments
- regulatory capital employed growth
- reported regulatory ROE
- customer receivables and regulatory assets
- long-term debt and AFUDC-equity markers
- rate-stabilization timing mechanics

That is enough to make the next model precise.

## What It Still Does Not Prove

It does not prove:

- SPPCRC customer receipts by rate class
- SPPCRC category earnings
- SPPCRC category depreciation, tax, AFUDC, or carrying charge realized by period
- financing source for Distribution Inspection, Transmission Inspection, feeder hardening, or vegetation management
- project-level IRR
- whether a specific customer surcharge dollar funded a specific asset

## Workbench Upgrade

| Gate | Status After This Pass | Reason |
|---|---|---|
| CFPGW-007 realized earnings/cash | partial | FPL-wide earnings, operating cash flow, capex, regulatory ROE, receivables, regulatory assets, debt, AFUDC, and rate-stabilization evidence are visible, but SPPCRC category-level attribution is not. |
| CFPGW-008 full pass decision | partial | The bridge now has recovery, order, output, and FPL-wide cash/earnings context, but not source/use/output/cash alignment in one category row. |

## Next Proof

The next search should not be broad. It should target one category and one attribution method:

| Target | Needed Evidence |
|---|---|
| Distribution Inspection | Clause schedule or workpaper that ties actual project count, actual cost, depreciation, tax, return, and revenue requirement into one line. |
| Transmission Inspection | Same as above, but this category has both final recovery and AP-1 actual cost/project-count evidence. |
| Customer receipts | Bill determinant or clause collection schedule by rate class, ideally matching the factor order and final true-up. |
| Financing source | FPL debt/equity issuance, utility construction funding, or regulatory workpaper tying capex funding to plant additions. |
| Earnings attribution | Depreciation, return, tax, AFUDC, and true-up schedule for selected SPPCRC category. |

## Decision

`fpl-wide-cash-earnings-context-visible - FPL has company-level earnings, cash-flow, capital, regulatory ROE, receivable, regulatory-asset, debt, AFUDC, and rate-stabilization evidence, but the SPPCRC category-level earnings/cash attribution remains open.`
