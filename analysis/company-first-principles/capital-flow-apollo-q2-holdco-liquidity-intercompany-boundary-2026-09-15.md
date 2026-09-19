# Apollo Q2 HoldCo liquidity and intercompany boundary

Research date: `2026-09-15`; balance-sheet summary refreshed `2026-09-16`

Apollo's Q2 2026 Form 10-Q makes the parent-cash route more explicit while
preserving the entity boundary. Apollo states that AGM is a holding company
whose primary cash-flow source is distributions and other intercompany
transfers from operating subsidiaries, specifically AAM and AHL. It reports
`$25.4B` of consolidated unrestricted cash and cash equivalents at June 30,
2026, but that figure is not a parent-only cash balance and cannot be assigned
to the Athene flow without an entity-level reconciliation.

The same filing reports the current-period intercompany perimeter for the
obligor group after eliminating intercompany transactions within that group:

- due from non-guarantor subsidiaries: `$1.175B`;
- due to non-guarantor subsidiaries: `$1.617B`;
- six-month intercompany revenue: `$785M`;
- six-month intercompany expense: `$300M`;
- six-month intercompany interest income: `$17M`.

## Parent-level liquidity context

The Apollo/Athene Q2 2026 earnings-release supplement separately presents an
Apollo HoldCo and Asset Management summary balance sheet. At June 30, 2026 it
shows:

| Summary line | Amount | Safe use in this research |
| --- | ---: | --- |
| Cash and cash equivalents | `$3.412B` | Parent-level balance-sheet context; not assumed unrestricted or Athene-funded |
| Investments, net | `$3.467B` | Asset-value context; not substituted for cash |
| Accrued performance fees receivable | `$1.511B` | Receivable context; collection timing and availability remain open |
| Net clawback payable | `$(95M)` | A claim reducing the displayed parent summary value |
| Debt | `$(5.762B)` | Parent summary debt claim |
| Net balance sheet value | `$2.533B` | Reported summary value, not common-owner free cash |
| Shares outstanding | `624M` | Denominator context only |

## Cash-denominator scope cross-check

The public Q2 materials show two nearby but non-identical cash figures:

| Source surface | Reported cash | Safe interpretation |
| --- | ---: | --- |
| HoldCo & Asset Management summary balance sheet | `$3.412B` | Summary-balance-sheet denominator used for the parent-liquidity screen |
| GAAP Asset Management segment table | `$3.415B` | Segment cash-and-cash-equivalents line before the summary presentation's scope and classification differences |
| Mechanical difference | `$3M` | Unreconciled presentation difference; not assigned to Athene, AGM, or common owners |

The `$3M` difference is immaterial to the broad liquidity screen but material
to evidence discipline: the two figures must not be silently averaged or
treated as interchangeable parent cash. The summary figure remains the
authoritative input for the HoldCo summary table; the segment figure remains a
separate segment-pool observation. A future supplement or reconciliation note
would be required to explain the exact bridge.

This creates a cleaner parent-level denominator context than consolidated
cash, but it still does not create a normalized liquidity measure. The table
does not establish legal-entity ownership of each balance, restricted versus
unrestricted cash, monetizability of investments or receivables, debt
maturities, preferred or other senior claims, taxes, or whether Athene's
`$110M` H1 distribution is included in the parent cash balance. The reported
`$2.533B` net balance sheet value therefore must not be used as common-owner
cash or added to the consolidated cash-flow bridge.

## Proof-grade consequence

This confirms the documented AGM liquidity route and provides a current-period
intercompany/elimination boundary. It does not identify whether Athene's
reported `$110M` H1 distributions to parent are included in any of these
balances, whether AGM received them in an unrestricted parent account, or what
amount remained after parent debt, tax, preferred claims, common dividends, and
repurchases.

Status:

`AGM liquidity route, intercompany perimeter, and parent-summary balance-sheet context confirmed; Athene-specific receipt and common-owner residual unresolved`

## Primary source

[Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm), especially “Liquidity and Capital Resources,” “Dividends and Distributions,” and the summarized obligor-group information; and the [Apollo/Athene Q2 2026 earnings-release supplement](https://ir.athene.com/sec-filings/all-sec-filings/content/0001527469-26-000047/agmearningsrelease2q2026.htm), Apollo HoldCo & Asset Management summary balance sheet.

Structured result: [HoldCo boundary CSV](data/capital-flow-apollo-q2-holdco-liquidity-intercompany-boundary-2026-09-15.csv).
