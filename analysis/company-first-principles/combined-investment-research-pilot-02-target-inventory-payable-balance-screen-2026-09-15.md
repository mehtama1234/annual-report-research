# Target H1 inventory and payable balance-change screen

Research date: `2026-09-15`

This supplemental screen tightens Q-04 without pretending that balance-sheet
changes are a cash-flow statement. Target's Q2 2026 Form 10-Q reports inventory
of `$13.249B` at August 1, 2026 and `$12.304B` at January 31, 2026. It reports
accounts payable of `$13.306B` and `$12.622B` at those same dates.

## Mechanical balance movements

| Item | January 31, 2026 | August 1, 2026 | Change | Mechanical reading |
| --- | ---: | ---: | ---: | --- |
| Inventory | `$12.304B` | `$13.249B` | `+$945M` | Balance increase is a use-of-cash signal before seasonality, markdowns, shrink, freight, and accrual effects |
| Accounts payable | `$12.622B` | `$13.306B` | `+$684M` | Balance increase is a source-of-cash signal before supplier-finance and timing effects |
| Inventory plus accounts-payable movements | — | — | `-$261M` net mechanical signal | Inventory growth exceeds payable growth by `$261M`; this is not a normalized H1 working-capital cash flow |

```text
mechanical net signal = accounts-payable increase - inventory increase
                     = $684M - $945M
                     = -$261M
```

## Boundary

This screen does not replace Target's reported operating cash flow or the
cash-flow statement's changes in operating assets and liabilities. It excludes
receivables, accrued liabilities, prepaid assets, deferred revenue, taxes,
seasonality, supplier-finance presentation, markdown and shrink effects, and
the timing of goods received versus paid. It therefore cannot be promoted to
recurring owner cash or used to rank Target against TJX and Walmart.

The useful upgrade is narrower: Target's H1 cash screen now has a reproducible
inventory/payable balance-change sensitivity that makes the working-capital
burden visible while preserving the unresolved normalization boundary.

## Proof-grade result

`Target balance-change screen proven; normalized working-capital cash not
proven.`

Primary source: [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm).

Structured result: [Target inventory/payable screen CSV](data/combined-investment-research-pilot-02-target-inventory-payable-balance-screen-2026-09-15.csv).
