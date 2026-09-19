# Wheaton–Antamina after-tax financed allocation frontier — 2026-09-15

This screen advances Q-03 by making the unresolved tax and financing
allocation visible. It is not an Antamina-specific after-tax IRR: Wheaton's
Q2 filing reports company-level finance costs and income-tax expense, but does
not assign either burden to the BHP PMPA.

## Source-anchored inputs

| Input | H1 2026 reported | Mechanical annualized screen | Boundary |
| --- | ---: | ---: | --- |
| Antamina stream operating-cash-flow proxy | `$222.223M` | `$444.446M` | Stream-level proxy; annualization is not a forecast |
| Finance costs | `$32.502M` | `$65.004M` | Wheaton corporate burden; not PMPA-assigned debt service |
| Income-tax expense | `$210.876M` | `$421.752M` | Wheaton corporate burden; not PMPA-assigned tax |
| PMPA upfront payment | — | `$4.300B` | Named BHP Antamina purchase price |

## Allocation frontier

The same explicit allocation rate is applied to the annualized corporate
finance-cost and tax-expense screens. This is a sensitivity device, not an
assertion that the corporate burdens should be allocated pro rata to the PMPA.

| Allocation case | Finance allocated | Tax allocated | After-tax financed cash | Cash / upfront payment | Simple payback |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0% / 0% | 0% | 0% | `$444.446M` | `10.336%` | `9.67 years` |
| 25% / 25% | 25% | 25% | `$322.757M` | `7.506%` | `13.32 years` |
| 50% / 50% | 50% | 50% | `$201.068M` | `4.676%` | `21.39 years` |
| 75% / 75% | 75% | 75% | `$79.379M` | `1.846%` | `54.17 years` |
| 100% / 100% | 100% | 100% | `-$42.310M` | `-0.984%` | not meaningful |

```text
after-tax financed cash
  = annualized stream OCF proxy
  - (annualized finance cost × allocation rate)
  - (annualized tax expense × allocation rate)

cash / upfront payment
  = after-tax financed cash ÷ $4,300M
```

## Interpretation boundary

The frontier shows why the return conclusion cannot be promoted from a
company-level burden screen to an asset-level after-tax return. Even modest
allocation assumptions materially change the apparent payback, while the
actual allocation could depend on debt source, legal entity, tax basis,
delivery timing, foreign tax, and the lender waterfall. The negative final row
is not a forecast; it is the arithmetic consequence of assigning all reported
corporate tax and finance expense to the stream proxy.

This screen still excludes BHP-only delivered ounces, settlement receipts,
principal repayment, reserve-backed delivery timing, and a terminal or
life-of-mine value. It therefore does not establish PMPA IRR, NPV, debt-service
coverage, or common-owner cash.

## Proof-grade result

| Gate | Result |
| --- | --- |
| Corporate finance and tax inputs | Proven for the reported H1 period |
| Source-bounded after-tax allocation frontier | Proven as sensitivity arithmetic |
| Antamina-specific tax and interest allocation | Not proven |
| Asset-level financed IRR / NPV | Not proven |
| Required next proof | PMPA funds-flow allocation, tax basis, principal waterfall, and BHP-only settlement cash |

Sources: [Wheaton company-burden boundary](capital-flow-wheaton-antamina-company-burden-boundary-upgrade-2026-09-15.md), [financing cash-flow upgrade](capital-flow-wheaton-antamina-financing-cash-flow-upgrade-2026-09-15.md), and [Antamina scenario workbench](combined-investment-research-pilot-01-antamina-scenario-workbench.md).
