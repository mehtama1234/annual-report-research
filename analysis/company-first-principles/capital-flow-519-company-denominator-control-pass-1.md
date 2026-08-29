# Capital Flow 519-Company Denominator Control Pass 1

## Purpose

This page adds the denominator control layer after the first `35` company cash-realization source table.

The question is:

`Can the source-visible pilot rows be compared without mixing platform AUM, vehicle fair value, borrower fair value, capex, backlog, tariff rates, regulated recovery, and cash?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-519-company-denominator-control-pass-1.csv`

The source-table input is:

`/cluster/capital-flow-519-company-cash-realization-source-table-pass-1.md`

The first queued-lane upgrade is:

`/cluster/capital-flow-debt-refinancing-sec-source-denominator-pass-1.md`

## Current Answer

`Yes as a control layer, not yet as a cross-company ranking. The denominator table covers all 35 pilot rows. It assigns metric class, denominator family, allowed comparison, forbidden comparison, best denominator evidence, next source, and upgrade test. After the debt/refinancing and Wheaton IFRS upgrades, 16 rows have moved out of generic queued status, including 5 debt/cash-flow denominator-started rows. The remaining 19 rows are still queued and cannot be compared beyond lane coverage.`

## Why This Matters

The source table made the pilot more evidence-backed, but it also made a new problem visible.

These are not equivalent units:

- Apollo inflows and spread-related earnings
- Ares borrower fair value
- ONEOK capex and adjusted EBITDA
- Plains cents-per-barrel tariff
- FPL aggregate clause revenue
- Energy Transfer DCF
- Sterling RPO and contract liabilities

The denominator control prevents a false leaderboard. A row can be shown as source-visible without being promoted into cross-company return proof.

## Denominator Status

| Status | Rows | Meaning |
|---|---:|---|
| `company-same-period-denominator-visible` | `3` | Company-level capex/output/cash-proxy denominators are visible, but project-level return remains open. |
| `company-same-period-denominator-visible-project-open` | `1` | Company-level cash, capex, output, availability, and debt denominators are visible, but named-project allocation remains open. |
| `platform-channel-denominator-visible` | `1` | Insurance/channel denominator is visible, but asset-level allocation is open. |
| `borrower-denominator-visible-source-use-open` | `1` | Same-period borrower fair value/commitments are visible, but source/use/cash is open. |
| `vehicle-denominator-visible-allocation-open` | `1` | Vehicle balance-sheet denominator is visible, but borrower/source allocation is open. |
| `allocation-open-denominator-mismatch` | `1` | Platform, vehicle, and borrower units coexist but cannot be collapsed into one denominator. |
| `tariff-denominator-visible-volume-open` | `1` | Route and cents-per-barrel tariff are visible, but volume and billing are open. |
| `regulated-recovery-denominator-visible-category-cash-open` | `1` | Cost/recovery and aggregate clause revenue are visible, but category customer cash is open. |
| `company-backlog-denominator-visible-project-open` | `1` | Backlog/contract-liability/cash-proxy denominators are visible, but project funding is open. |
| `debt-cash-flow-denominator-started` | `5` | SEC cash, debt, operating cash flow, proceeds, repayments, dividend, repurchase, or stream-acquisition denominators are visible, but source/use and return remain open. |
| `queued-denominator-not-started` | `19` | No denominator comparison is allowed yet beyond queue and lane assignment. |

## Allowed Comparisons

| Metric Class | Allowed | Forbidden |
|---|---|---|
| Platform / insurance channel | Compare inflows, invested assets, spread earnings, and asset quality inside the same insurance or credit-channel frame. | Do not compare platform AUM or inflows to borrower fair value or project capex as if they are the same economic unit. |
| Borrower holder fair value | Compare same-period holder fair value and unfunded commitments across named borrowers. | Do not treat holder fair value as facility size, source of funds, borrower revenue, or cash return. |
| Company capex/output/cash proxy | Compare company-level capex, EBITDA, DCF, volume, output, and liquidity inside the same company/lane frame. | Do not convert company EBITDA or DCF into named-project return without project allocation evidence. |
| Tariff route/rate | Compare tariff rates, routes, effective dates, and later throughput/billing once extracted. | Do not infer realized revenue from cents-per-barrel rates without volumes and shipper evidence. |
| Regulated recovery | Compare jurisdiction, project/category cost, recovery authority, plant additions, capital structure, and aggregate clause revenue. | Do not call aggregate clause revenue a category customer receipt without billing determinant/category allocation evidence. |
| Backlog/contract liability | Compare RPO, backlog, contract liabilities, OCF less capex, revolver/L/C capacity, and project funding when visible. | Do not call backlog funded, non-cancellable, high-margin, or collected cash without project-level support. |

## Decision

`519-company-denominator-control-ready`

The `35` company pilot now has a denominator-control table. The research can show source-visible evidence without accidentally ranking incomparable units.

## Safe Claim

`The 35-company pilot now separates evidence visibility from comparability. Sixteen companies have moved out of generic queued status, but comparisons are only safe within metric class; 19 rows remain queued and should not be ranked or promoted until their primary metrics and denominators are extracted.`

## Next Work

1. Parse debt footnotes and liquidity sections for PBF, Devon, Matador, Liberty Broadband, and Wheaton.
2. Parse Wheaton's Antamina PMPA terms and expected delivery/cash-return evidence.
3. Continue queued-lane denominator upgrades with acquisition-finance companies.
