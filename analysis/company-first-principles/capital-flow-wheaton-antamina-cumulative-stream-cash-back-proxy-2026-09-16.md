# Wheaton–Antamina cumulative stream cash-back proxy

Research date: `2026-09-16`

## Source route

The [Wheaton Q2 2026 MD&A](../../raw/primary-sources/capital-flow/debt-refinancing/wheaton/q2-2026/wpm-20260630-ex99-2-mda.htm)
reports the Antamina row in a combined `Glencore/BHP` perimeter. The Q2 table
reports cumulative received-and-sold silver, cash flow generated to date,
upfront consideration paid to date, and PBND.

## Observed cumulative baseline

| Metric | Q2 2026 reported value | Evidence grade | Limitation |
| --- | ---: | --- | --- |
| Attributable silver interest | `67.50%` | `combined-stream-denominator-visible` | Combines Glencore `33.75%` and BHP `33.75%` |
| Upfront consideration paid to June 30 | `$5.200B` | `combined-stream-use-visible` | Not BHP-PMPA-only in the cumulative table |
| Silver ounces received and sold to date | `56.718M` | `combined-stream-receipt-proxy-visible` | Not a BHP-only metal-credit ledger or invoice |
| Cash flow generated to date | `$1.171862B` | `combined-stream-cash-back-proxy-visible` | Stream-row cash-flow proxy; not a collected BHP settlement account |
| Q2 PBND | `1.412M` ounces | `combined-stream-timing-visible` | Does not identify BHP versus Glencore timing |

## Interpretation

This creates a useful cumulative bridge:

```text
combined Glencore/BHP Antamina stream
  -> $5.200B cumulative upfront consideration
  -> 56.718M ounces received and sold
  -> $1.171862B cumulative cash flow generated to date
  -> 1.412M ounces Q2 PBND
```

The bridge is stronger than a production-only observation because it includes
received-and-sold ounces and a cash-flow proxy. It remains a combined-stream
denominator and cannot be used to infer BHP's metal-credit quantity, invoice,
quotation-period settlement price, or receipt cash.

The structured companion is the [cumulative received/sold cash-flow bridge](data/capital-flow-wheaton-antamina-cumulative-received-sold-cashflow-pass-1.csv).

## Proof grade

`combined-stream-cumulative-cash-back-proxy-confirmed`.

The combined cash-flow proxy divided by the cumulative upfront consideration is
`22.5358%` (`$1.171862B / $5.200B`). This is an undiscounted combined-stream
screen, not a return, payback, IRR, NPV, or BHP-only cash result. The next Q-01
upgrade remains a BHP-only metal-credit quantity joined to settlement and
Wheaton receipt evidence.
