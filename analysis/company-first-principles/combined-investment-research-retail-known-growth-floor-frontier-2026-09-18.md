# Retail known-growth-floor frontier

Research date: `2026-09-18`

## Purpose

This control turns the latest TJX, Target, and Walmart interim disclosures into
a comparable capex frontier without pretending that the unallocated property
remainder is maintenance or growth. It is a denominator diagnostic for CA-06
and Q-05, not a normalized owner-cash calculation.

## Same-period evidence

| Company / period | OCF | Property cash/additions | Reported OCF less all property | Disclosed same-period growth floor | Unallocated property remainder |
| --- | ---: | ---: | ---: | ---: | ---: |
| TJX H1 FY2027 | `$3.345B` | `$1.159B` | `$2.186B` | `$222M` new-store spending | `$937M` |
| Target H1 2026 | `$4.519B` | `$2.404B` | `$2.115B` | Not quantified in H1 filing | `$2.404B` |
| Walmart H1 FY2027 | `$19.710B` | `$14.181B` | `$5.529B` | `$1.087B` new stores, expansions, and relocations | `$13.094B` |

The remainder is calculated as property cash/additions less the disclosed
growth floor. For Target, no H1 dollar growth floor is disclosed, so the full
property line remains unallocated. Walmart's categories outside new stores,
expansions, and relocations remain mixed across supply chain, customer-facing
initiatives, technology, other, remodels, and international. TJX's explicit
new-store amount does not classify the remaining segment additions.

Target's official Q2 operating update adds a unit-count control: it opened `17`
new stores in Q2 and `24` year-to-date against a plan for more than `30` in
2026. This confirms that some portion of the `$2.404B` H1 property line is
growth-related, but Target does not disclose the dollars assigned to those
stores in the Q2 materials. The count therefore remains an expectation and
classification control, not a dollar maintenance/growth allocation or an
owner-cash deduction.
The Q2 call also describes the same `$2.4B` H1 deployment as incremental
investment in new stores, full-store remodels, supply chain, and technology,
but does not split those categories into maintenance versus growth dollars.

## Sensitivity boundary

Adding a disclosed growth floor back to the reported OCF-less-property figure
would create an optimistic “after unallocated remainder only” sensitivity of
`$2.408B` for TJX and `$6.616B` for Walmart. Those values are not owner cash:
they assume, only for the sensitivity, that every unallocated dollar is not a
required replacement or operating investment. Target cannot receive the same
numeric treatment from the current source set.

The safe interpretation is therefore:

```text
reported OCF - all reported property cash
  <= possible residual after property
  <= reported OCF - disclosed maintenance only
```

The upper bound is not observable until the mixed remainder is allocated. The
known growth floor improves the direction of the bound but does not identify
maintenance cash, project return, lease/tax burden, supplier-finance
settlement, attached-service cost, debt, or diluted common residual.

## Promotion result

`Q-05-evidence-insufficient; CA-06-partial; no-ranking`

This frontier is a stronger, reproducible classification control. Promotion
still requires a same-company, same-period project or asset schedule that
identifies replacement, remodel, technology, supply-chain, and expansion
spending and links the categories to cash return. No company is promoted from
this frontier.

The machine-readable companion is the [known-growth-floor frontier ledger](data/combined-investment-research-retail-known-growth-floor-frontier-2026-09-18.csv). Its optimistic sensitivity is calculated as `cash after property + disclosed growth floor`; it is only a bounded classification screen and is not additive to the other burden or support sensitivities.

## Sources

- [TJX Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm)
- [Target Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm)
- [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm)
- [Target Q2 2026 operating update](https://corporate.target.com/news-features/article/2026/08/q2-2026-earnings)
- [Target Q2 2026 earnings-call transcript](https://corporate.target.com/getmedia/d01cb805-63cb-4150-bae4-8d717f0d9ed3/Q2-2026-Target-Corp-Earnings-Call.pdf)
