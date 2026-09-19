# Pilot 02 retail cohort inventory/payable balance screen — 2026-09-17

This screen extends the Target balance-change work to the full retail cohort.
It compares the latest reported balance-sheet dates with each company's fiscal
year-end opening balances. The result is a mechanical working-capital signal,
not a cash-flow attribution: inventory composition, seasonality, markdowns,
freight, accruals, supplier finance, and acquisition or currency effects can
make the balance changes differ from the cash-flow statement.

## Cross-cohort balance changes

| Company / period | Inventory opening | Inventory ending | Inventory change | Accounts payable opening | Accounts payable ending | Accounts payable change | Mechanical net signal |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| TJX / H1 FY2027 | `$7.297B` | `$7.862B` | `+$565M` | `$4.575B` | `$5.024B` | `+$449M` | `-$116M` |
| Target / H1 2026 | `$12.304B` | `$13.249B` | `+$945M` | `$12.622B` | `$13.306B` | `+$684M` | `-$261M` |
| Walmart / H1 FY2027 | `$58.851B` | `$61.600B` | `+$2.749B` | `$63.061B` | `$64.318B` | `+$1.257B` | `-$1.492B` |

The mechanical signal is calculated as:

```text
accounts-payable increase − inventory increase
```

It is negative for each retailer in this comparison, meaning the reported
payable balance increase did not fully offset the inventory balance increase.
That observation is narrower than saying the cohort consumed that exact amount
of cash: the cash-flow statements contain other working-capital lines and
period timing, and Walmart's reported six-month cash-flow inventory/AP rows are
`-$2.660B` and `+$1.648B`, respectively.

## Cash-flow cross-check

| Company / period | Cash-flow inventory effect | Cash-flow accounts-payable effect | Cash-flow mechanical signal | Boundary |
| --- | ---: | ---: | ---: | --- |
| TJX / H1 FY2027 | `-$603M` | `+$470M` | `-$133M` | Timing and other presentation effects remain. |
| Target / H1 2026 | `-$945M` | `+$612M` | `-$333M` | Balance-sheet changes and cash-flow rows align directionally but are not a complete working-capital bridge. |
| Walmart / H1 FY2027 | `-$2.660B` | `+$1.648B` | `-$1.012B` | The filing includes broader timing and reconciliation effects. |

The cross-check confirms that the balance screen is directionally consistent
with reported cash-flow working-capital pressure, while also demonstrating why
the balance changes cannot be inserted into owner cash as a standalone
adjustment.

## Supplier-finance overlay

The balance screen must be read beside the separate supplier-finance disclosure:
Target reports a `$3.2B` eligible obligation included in accounts payable, and
Walmart reports `$6.4B` outstanding under supplier-finance programs. Those are
period-end obligations, not one-period cash adjustments. The H1 cash-flow AP
rows above remain the usable period screen; the full supplier-finance balance
must not be subtracted from operating cash a second time. TJX has no comparable
separately quantified supplier-finance balance in this controlled screen.

The next Q-04 upgrade is a dated supplier-finance roll-forward with settlement
timing that can be reconciled to accounts payable and cash disbursements.

## Interpretation boundary

This screen improves the denominator evidence by placing comparable opening
and ending balances beside the OCF and cash-after-property frontiers. It does
not normalize inventory turns, vendor terms, markdowns, shrink, freight,
supplier-finance settlement, taxes, leases, maintenance capital, or seasonality.
The signal must not be subtracted from OCF a second time where the same period
cash-flow statement already captures the working-capital movement.

Status: `cross-cohort balance-change screen; recurring owner cash unresolved`.

## Same-period QoE double-count control — 2026-09-17

The balance-sheet and cash-flow views are now explicitly treated as two
diagnostic surfaces, not additive adjustments:

| Company / period | Balance signal | Cash-flow signal | Difference to investigate |
| --- | ---: | ---: | --- |
| TJX H1 FY2027 | `-$116M` | `-$133M` | Presentation, timing, and other working-capital lines |
| Target H1 2026 | `-$261M` | `-$333M` | Timing and broader working-capital reconciliation |
| Walmart H1 FY2027 | `-$1.492B` | `-$1.012B` | Broader cash-flow reconciliation and timing |

The cash-flow signal is the recognized period movement already embedded in
operating cash flow; the balance signal is a period-end diagnostic. Neither
the full supplier-finance balance nor its mechanical change may be subtracted
again without a settlement-date bridge. This is a QoE control against
manufacturing a recurring-cash adjustment from a balance-sheet movement.

Structured result: [cross-cohort balance-screen CSV](data/combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.csv).

Primary sources: [TJX Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm), [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm), and [Walmart Q2 FY2027 Form 10-Q](https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000154/wmt-20260731.htm).
