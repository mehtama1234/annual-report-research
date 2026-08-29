# Capital Flow Devon Treasury Funds-Flow Pass 1

## Purpose

This page executes the Devon treasury funds-flow row from the debt/refinancing bridge upgrade queue:

`Can Devon's Q2 2026 merger-period allocation bridge be upgraded from qualitative allocation language to statement-level source/use reconciliation?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-devon-treasury-funds-flow-pass-1.csv`

The queue row is:

`/cluster/capital-flow-debt-refinancing-bridge-upgrade-queue-pass-1.md`

The upstream Devon bridge is:

`/cluster/capital-flow-devon-merger-period-allocation-bridge-pass-1.md`

## Current Answer

`Devon can be upgraded to treasury funds-flow reconciliation visible at statement level. For the first half of 2026, visible sources total 6.451B USD: 5.329B USD of operating cash flow, 581M USD of cash acquired in the Coterra merger, 90M USD of divestiture proceeds, 22M USD of investment distributions, a 425M USD cash/restricted-cash drawdown, and 4M USD of FX benefit. Visible uses also total 6.451B USD: 2.157B USD of capex, 2.919B USD of property/equipment acquisitions, 12M USD of investment contributions, 500M USD of long-term debt repayments, 266M USD of buybacks, 521M USD of dividends, 5M USD of finance-lease repayments, and 71M USD of tax-withholding/other equity cash use. This proves statement-level treasury reconciliation, not daily dollar sequencing, asset-level return, acquisition return, realized synergy, or financing causality.`

## First-Half Reconciliation

| Source | Amount |
|---|---:|
| Operating cash flow | `5.329B USD` |
| Cash acquired in Coterra merger | `581M USD` |
| Divestiture proceeds | `90M USD` |
| Investment distributions | `22M USD` |
| Cash/restricted-cash drawdown | `425M USD` |
| FX benefit | `4M USD` |
| Total visible source envelope | `6.451B USD` |

| Use | Amount |
|---|---:|
| Capex | `2.157B USD` |
| Acquisitions of property/equipment | `2.919B USD` |
| Contributions to investments and other | `12M USD` |
| Long-term debt repayments | `500M USD` |
| Common stock repurchases | `266M USD` |
| Dividends | `521M USD` |
| Finance lease repayments | `5M USD` |
| Tax withholding/other equity cash use | `71M USD` |
| Total visible use envelope | `6.451B USD` |

## What Improved

| Area | Prior Bridge | This Pass |
|---|---|---|
| Cash source | OCF and cash balances were visible. | Sources now reconcile exactly to uses at first-half statement level. |
| Capital allocation | Capex, acquisitions, debt repayment, dividends, and buybacks were visible as separate facts. | These uses are now placed into one source/use envelope. |
| Merger treatment | Coterra stock consideration, assumed debt, and post-close contribution were visible. | Cash acquired in the merger is separated from non-cash stock consideration and assumed debt. |
| Boundary | Devon was company-level allocation, not return proof. | Devon is now treasury funds-flow reconciliation visible, still not source-specific or return proven. |

## Decision

`treasury-funds-flow-reconciliation-visible-statement-level`

This is an upgrade from:

`merger-period-allocation-cash-return-bridge-visible-company-level`

It does not reach:

`dollar-level-source-use-allocation-visible`

The queue pass test required Devon's uses to be reconciled to sources at company level without double counting. That passes at statement level. It does not pass at daily cash-ledger, transaction-closing, asset-level, or return level.

## Non-Cash Items Kept Separate

The Coterra merger was large, but not all of it belongs in the treasury cash-flow envelope:

- `24.946B USD` of Devon common stock issued in the merger is non-cash consideration.
- `24.946B USD` of net assets acquired is purchase-accounting value, not cash use.
- `12.304B USD` of liabilities assumed is balance-sheet mechanics, not cash funding.
- `3.500B USD` face value of Coterra debt assumed and `2.950B USD` of New Devon Notes issued in exchange offers are capital-stack integration evidence, not cash proceeds.

## Remaining Gap

| Gap | Why It Matters | Next Source |
|---|---|---|
| Daily cash ledger | Needed to prove source priority and sequencing. | Treasury cash ledger and funds-flow schedule. |
| BLM lease closing statement | Needed to prove exact cash source for the `2.6B USD` Permian lease acquisition. | BLM closing/payment records and internal funds-flow. |
| Debt repayment notices | Needed to map `500M USD` of debt repayment to specific cash source and economics. | Term-loan repayment notice, senior-note redemption notice, and make-whole calculation. |
| Asset contribution | Needed to convert capex/acquisition spend into operating return. | Asset-level production, reserves, revenue, LOE, EBITDA, and OCF contribution. |
| Realized synergy | Needed to move Coterra from merger contribution/target to cash-return evidence. | Post-Q2 integration reporting and realized synergy schedule. |

## Safe Claim

`Devon's first-half 2026 filing supports statement-level treasury funds-flow reconciliation: 6.451B USD of visible sources matches 6.451B USD of visible uses. Sources include OCF, merger cash, divestitures, investment distributions, cash-balance drawdown, and FX. Uses include capex, property/equipment acquisitions, investment contributions, debt repayment, buybacks, dividends, finance leases, and tax-withholding/other equity cash use. This is not dollar-level source/use allocation, asset-level return, acquisition return, realized synergy, or financing causality.`

## Next Work

1. Pull BLM lease-sale payment and closing records.
2. Find debt repayment notices and make-whole/term-loan repayment economics.
3. Search for a Devon treasury allocation or cash waterfall table.
4. Build a Coterra realized synergy and asset contribution pass after later filings.
5. Join Permian lease and capex uses to wells, reserves, production, and cash contribution.
