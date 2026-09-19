# Apollo–Athene segment cash-availability boundary

Research date: `2026-09-15`

Apollo's Q2 2026 Form 10-Q separates cash pools by operating segment before
any claim that cash is available to the Apollo parent. At June 30, 2026, the
filing reports:

| Segment / pool | Cash and cash equivalents | Restricted cash | Consolidated VIE cash | Safe interpretation |
| --- | ---: | ---: | ---: | --- |
| Asset Management | `$3.415B` | `$19M` | `$1.272B` | Segment and VIE cash are visible; HoldCo receipt and legal availability are not shown |
| Retirement Services | `$21.957B` | `$1.583B` | `$171M` | Athene-related cash is visible with restricted/VIE boundaries; it is not unrestricted Apollo cash |

The same filing reports consolidated operating cash flow of `$4.501B` for the
first half, but consolidated cash flow includes regulated retirement-services
and VIE activity. The segment table therefore improves the denominator map
without converting any of these balances into Apollo common-owner cash.

## Required bridge still open

```text
segment cash pool
  -> legally distributable subsidiary cash
  -> approved and executed dividend/intercompany transfer
  -> Apollo HoldCo unrestricted cash
  -> parent debt, tax, preferred, NCI, dividends, and repurchases
  -> common-owner residual
```

`segment-cash-pool-boundary-visible`: segment, restricted, and VIE cash
balances are source-backed; dated upstream receipt, legal dividend capacity,
intercompany elimination, and common-owner attribution remain unresolved.

## Primary source

[Apollo Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000040/apo-20260630.htm).
