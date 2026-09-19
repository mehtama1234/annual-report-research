# Pilot 02 retail cash-quality support-dependency screen

Research date: `2026-09-15`

This screen compares how much of each reported cash-after-property bridge is
removed in the conservative source-bounded case. It is a cash-quality signal,
not normalized owner cash: the adjustment bundle includes disclosed payable or
tariff support and stock-based compensation where the existing screen defines
them, but it does not solve seasonality, maintenance capital, leases, taxes,
or attached-service economics.

## Cohort screen

| Company / period | Reported cash after property | Conservative screen | Screen reduction | Reduction / reported cash |
| --- | ---: | ---: | ---: | ---: |
| TJX FY2026 | `$4.917B` | `$4.464B` | `$453M` | `9.21%` |
| Target H1 2026 | `$2.115B` | `$0.597B` | `$1.518B` | `71.77%` |
| Walmart H1 FY2027 | `$5.529B` | `$0.981B` | `$4.548B` | `82.26%` |
| TJX H1 FY2027 | `$2.186B` | `$1.631B` | `$555M` | `25.39%` |

```text
screen reduction = reported cash after property − conservative screen
support dependency = screen reduction ÷ reported cash after property
```

## Interpretation boundary

The screen says that the apparent cash quality of the Target and Walmart H1
rows is more sensitive to identified support and timing items than the TJX
FY2026 annual row. It does not say that the entire reduction is permanent
economic leakage: payable timing, tariff refunds, supplier finance, and stock
compensation have different accounting and cash consequences. Nor does it
rank the companies because the periods and adjustment bundles are not fully
comparable.

The useful conclusion is narrower: a reported OCF-less-property bridge should
not enter valuation without showing the size of its source-bounded support
dependency. The next upgrade remains a same-period roll-forward for inventory,
payables, supplier finance, capex, leases, taxes, dilution, and attached
services.

## Proof-grade result

| Gate | Result |
| --- | --- |
| Reported cash-after-property inputs | Proven from the cohort bridge |
| Conservative screen inputs | Proven as source-bounded sensitivities |
| Cross-company support-dependency comparison | Qualified because periods and bundles differ |
| Normalized owner-cash ranking | Not proven |

Sources: [retail normalized-cash screen](combined-investment-research-pilot-02-retail-normalized-cash-screen.md), [TJX H1 cash-quality upgrade](combined-investment-research-pilot-02-tjx-h1-cash-screen-upgrade-2026-09-15.md), and [retail owner-cash bridge](combined-investment-research-pilot-02-retail-owner-cash-bridge.md).
