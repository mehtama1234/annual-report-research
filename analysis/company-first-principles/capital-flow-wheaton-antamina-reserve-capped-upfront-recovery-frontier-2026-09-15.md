# Wheaton–Antamina reserve-capped upfront-recovery frontier — 2026-09-15

This screen joins the disclosed BHP-interest Proven and Probable reserve
quantity to the PMPA payment formula and the `$4.300B` upfront consideration.
It is a bounded recovery screen, not an annual delivery curve, IRR, NPV, or
claim that current reserves are the complete mine life.

## Source-anchored calculation

The transaction materials disclose `65.7M` contained BHP-interest silver
ounces, a fixed `90%` payable factor, and a `20%` ongoing payment on delivered
ounces. The current P&P quantity therefore implies a mechanical `59.13M`
payable-ounce ceiling. That is below the `100M`-ounce initial stream threshold,
so this screen does not apply the post-threshold `22.5%` share.

```text
payable reserve ceiling = 65.7M contained oz × 90% = 59.13M payable oz
reserve-capped cash before corporate burden
  = payable reserve ceiling × silver price × (1 − 20% stream payment)
cash after burden haircut
  = reserve-capped cash before corporate burden × (1 − burden haircut)
```

## Frontier

| Silver price | Cash before burden | Cash after 20% burden haircut | After-burden / `$4.300B` upfront |
| ---: | ---: | ---: | ---: |
| `$35/oz` | `$1.656B` | `$1.325B` | `30.80%` |
| `$60/oz` | `$2.838B` | `$2.271B` | `52.81%` |
| `$90/oz` | `$4.257B` | `$3.406B` | `79.21%` |

At a `$90/oz` price and zero additional burden haircut, the reserve-capped
gross cash is `$4.257B`, or `99.01%` of the upfront payment. That is an
expectation-burden result, not a transaction-loss conclusion: it excludes
mine-life extensions, reserve conversion, price changes, delivery timing,
taxes, financing, operating costs beyond the stream payment, terminal value,
and the possibility that the reported reserve basis is not the complete
economic tail.

## Forward-profile versus reserve-ceiling cross-check — 2026-09-17

Wheaton's September 2026 Investor Day profile states approximately `6.0M`
ounces per year for the first five years and `5.4M` per year for the first ten
years. If those figures are treated as the same BHP-interest, stream-relevant
quantity basis, the first-ten-year cumulative profile is `57.0M` ounces:

```text
5 × 6.0M + 5 × 5.4M = 57.0M ounces
59.13M reserve-capped payable-ounce ceiling − 57.0M = 2.13M ounces
```

This is a useful consistency screen: the management profile would consume
approximately `96.4%` of the mechanical reserve-capped payable ceiling in ten
years, before any definition, recovery, assay, or reserve-conversion issue.
It is not a delivery forecast. The presentation calls the figures a forward
profile, while the reserve input and the PMPA payable convention are not
identical source objects. A future model must therefore carry both a
profile-as-stated case and a 90%-payability case rather than silently merging
them.

## Proof-grade result

| Gate | Result |
| --- | --- |
| Reserve quantity and payable conversion | Proven source-anchored input |
| Reserve-capped recovery arithmetic | Proven mechanical frontier |
| Annual reserve-backed delivery curve | Not proven |
| Asset-level after-tax financed return | Not proven |
| BHP-only settlement cash | Not proven |

The safe use is to expose the burden placed on price, reserve conversion, and
mine-life extension assumptions before a Damodaran valuation conclusion is
written. The frontier must not be presented as a forecast or as a replacement
for the missing settlement and debt waterfall.

Sources: [Antamina reserve-constrained delivery ceiling](capital-flow-wheaton-antamina-reserve-constrained-delivery-ceiling-2026-09-15.md), [Wheaton transaction terms](https://www.sec.gov/Archives/edgar/data/1323404/000127956926000131/ex991.htm), and [BHP FY2026 Form 20-F](https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm).

Structured result: [reserve-capped frontier CSV](data/capital-flow-wheaton-antamina-reserve-capped-upfront-recovery-frontier-2026-09-15.csv).
