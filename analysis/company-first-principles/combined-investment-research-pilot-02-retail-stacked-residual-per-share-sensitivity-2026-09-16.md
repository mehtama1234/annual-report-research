# Retail stacked-residual per diluted share sensitivity

Research date: `2026-09-16`

This artifact translates the existing common-period retail stacked-residual
screen into per-diluted-share terms. It is a sensitivity for valuation review,
not normalized owner cash. The numerator starts with reported operating cash
flow less property spending, then subtracts the source-bounded support
candidate, available stock-compensation sensitivity, and disclosed debt
principal repayment from the common-period normalization surface.

| Company / period | Diluted shares | Reported cash after property | Stacked residual | Stacked residual per diluted share | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| TJX / H1 FY2027 | `1,118M` | `$2.186B` | `$1.351B` | `$1.208` | Stress sensitivity |
| Target / H1 2026 | `456.2M` | `$2.115B` | `($0.473B)` | `($1.037)` | Stress sensitivity |
| Walmart / H1 FY2027 | `7,989M` | `$5.529B` | `($1.322B)` | `($0.165)` | Stress sensitivity |

The calculation is:

```text
stacked residual per diluted share
  = stacked residual in millions / diluted weighted-average shares in millions
```

The resulting per-share figures are not directly comparable investment
conclusions. The periods are different, the support candidates can overlap
with working-capital signals, and maintenance capital, leases, taxes,
seasonality, attached-service costs, and future dilution are not fully
allocated. A negative sensitivity is not a claim that the company reported
negative owner cash; it shows how the residual changes when selected burdens
are layered onto the reported cash-after-property screen.

This is the appropriate bridge into price-implied analysis: the market-price
comparison may use the reported and stacked screens as explicitly labeled
frontiers, but it must not substitute either for a normalized annual owner-cash
denominator. Promotion requires a period-matched allocation of the unresolved
burdens and a stable diluted-share basis.

Source artifact: [retail common-period normalization surface](combined-investment-research-pilot-02-retail-common-period-normalization-surface-2026-09-15.md).

Structured rows: [per-share sensitivity CSV](data/combined-investment-research-pilot-02-retail-stacked-residual-per-share-sensitivity-2026-09-16.csv).
