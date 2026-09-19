# Wheaton–Antamina term-maturity bullet coverage screen

Research date: `2026-09-16`

This screen makes the separate principal claim visible in the Q-03 return
workbench. Wheaton's direct credit agreement sets a `$1.500B` term-facility
principal balance with repayment at maturity, while the Q2 stream operating-
cash-flow proxy annualizes to `$444.446M`. The screen applies an explicit
allocation sensitivity to the corporate term balance; it does not claim that
any percentage is the Antamina share of debt or that annualized stream cash
will be available at maturity.

## Illustrative bullet sensitivity

| Term principal allocated to screen | Allocated maturity bullet | Bullet / annualized stream OCF proxy | One-period proxy after bullet |
| ---: | ---: | ---: | ---: |
| 0% | `$0.000M` | `0.00x` | `$444.446M` |
| 25% | `$375.000M` | `0.84x` | `$69.446M` |
| 50% | `$750.000M` | `1.69x` | `-$305.554M` |
| 75% | `$1,125.000M` | `2.53x` | `-$680.554M` |
| 100% | `$1,500.000M` | `3.37x` | `-$1,055.554M` |

```text
allocated maturity bullet
  = $1,500M × explicit allocation rate

bullet / annualized stream OCF proxy
  = allocated maturity bullet ÷ $444.446M

one-period proxy after bullet
  = $444.446M − allocated maturity bullet
```

The one-period column is a stress display, not a forecast or a debt-service
coverage ratio. Principal is due at a future maturity date, whereas the cash
proxy is an annualized H1 observation; the two are not naturally matched
without a dated delivery curve, cash accumulation, refinancing plan, asset
sale, or equity source.

## Evidence boundary

The agreement proves the facility amount, borrower and lender route, contractual
Antamina use-of-proceeds link, and maturity repayment mechanics. Wheaton's Q2
balance sheet proves the reported term balance. Public materials do not prove
the executed draw-dollar path, the seller account, Antamina-specific debt
allocation, repayment source, or lender waterfall. Accordingly this screen is
`illustrative-allocation-frontier` and does not promote Q-03 beyond
`evidence-insufficient`.

Sources: [credit-agreement boundary](capital-flow-wheaton-antamina-credit-agreement-waterfall-boundary-2026-09-16.md), [term-maturity cliff screen](capital-flow-wheaton-antamina-term-maturity-cliff-screen-2026-09-16.md), and [after-tax financed allocation frontier](capital-flow-wheaton-antamina-after-tax-financed-allocation-frontier-2026-09-15.md).

Structured result: [maturity-bullet coverage CSV](data/capital-flow-wheaton-antamina-term-maturity-bullet-coverage-screen-2026-09-16.csv).
