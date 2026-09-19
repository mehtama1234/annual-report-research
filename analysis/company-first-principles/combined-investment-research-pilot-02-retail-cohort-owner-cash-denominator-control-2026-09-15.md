# Retail cohort owner-cash denominator control — 2026-09-15

This matrix connects the TJX, Target, and Walmart denominator work into one
review route. The periods are each the latest H1/current filing window in the
pilot, but the figures are not a comparable owner-cash ranking. The purpose is
to show which burden layers are visible, which are sensitivity candidates, and
which remain unallocated.

## Cross-company control surface

| Company / period | Cash after property | Temporary-support candidate | SBC sensitivity | Debt principal repayment | Support + SBC + debt residual | Current grade |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| TJX / H1 FY2027 | `$2.186B` | `$0.750B` | `$0.085B` | `$0.000B` | `$1.351B` | `source-bounded residual` |
| Target / H1 2026 | `$2.115B` | `$1.364B` | `$0.154B` | `$1.070B` | `($0.473B)` | `source-bounded residual` |
| Walmart / H1 FY2027 | `$5.529B` | `$4.548B` | `NA` | `$2.303B` | `($1.322B)` | `source-bounded residual; SBC unavailable` |

The calculation is:

```text
cash after property
  − support-removal candidate
  − disclosed SBC sensitivity where available
  − disclosed H1 debt-principal repayment
  = stacked burden screen
```

The negative lower corners do not mean the companies reported negative owner
cash. They show that cash after property cannot be promoted to common-owner
cash while temporary support, maintenance capital, working capital, leases,
taxes, attached-service costs, debt, and dilution remain unresolved.

## Denominator discipline

- TJX has the cleanest current reported bridge, but its H1 support candidate,
  inventory timing, leases, maintenance capital, and annual seasonality remain
  open.
- Target's stacked screen is affected by tariff refunds, vendor/payable
  support, supplier finance, share-based compensation, and the `$1.070B` debt
  repayment.
- Walmart has the largest absolute cash-after-property figure, but it also has
  the largest disclosed capital program and a material tariff-refund/support
  candidate; current H1 SBC is not separately populated in the controlled
  screen.

The safe cohort conclusion is therefore `reported cash bridges are
constructed; normalized common-owner cash is not ranked`. The next upgrade is
not a fourth multiple or a simple average. It is a period-matched allocation
of maintenance capital, working capital, leases, taxes, service costs, and
dilution for each company.

Structured claims: [retail cohort denominator CSV](data/combined-investment-research-pilot-02-retail-cohort-owner-cash-denominator-control-2026-09-15.csv).

Source routes: [TJX H1 cash screen](combined-investment-research-pilot-02-tjx-h1-cash-screen-upgrade-2026-09-15.md), [Target H1 denominator control](combined-investment-research-pilot-02-target-h1-owner-cash-denominator-control-2026-09-15.md), and [Walmart H1 denominator control](combined-investment-research-pilot-02-walmart-h1-owner-cash-denominator-control-2026-09-15.md).
