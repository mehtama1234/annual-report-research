# Capital Flow KKR Global Atlantic Accordia Schedule D Coordinate Owned-Bond Reconciliation Pass 1

## Purpose

This pass uses source-page coordinate columns to reconcile Accordia Schedule D owned bonds after the held-row geometry diagnostic.

It asks:

`Can broad CUSIP starts, including statutory private-marker CUSIPs, and x/y column reads reconcile owned issuer-credit and ABS book value to the Accordia statutory Schedule D bond base?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-coordinate-owned-bond-reconciliation-diagnostic-pass-1.csv`

## Short Answer

`Yes, for owned-bond book value at source-page coordinate level. The coordinate pass extracts 1165 owned bond rows: 1007 issuer-credit rows and 158 ABS rows. It finds 79 statutory private-marker CUSIP rows that the raw parser did not cleanly promote. Coordinate book value sums to 7318321094 USD versus the 7318322163 USD statutory bond target, a variance of -1069 USD and 99.999985% coverage.`

## Diagnostic Metrics

| Metric | Value |
|---|---:|
| Coordinate owned bond rows | 1165 |
| Coordinate issuer-credit rows | 1007 |
| Coordinate ABS rows | 158 |
| Standard CUSIP-like rows | 1086 |
| Statutory private-marker CUSIP rows | 79 |
| Matched raw parser rows | 1086 |
| Not in raw parser private-marker/geometry rows | 79 |
| Coordinate book value sum | 7318321094 |
| Coordinate issuer-credit book value | 6484939301 |
| Coordinate ABS book value | 833381793 |
| Coordinate private-marker book value | 908555462 |
| Statutory bond target | 7318322163 |
| Coordinate variance | -1069 |
| Coordinate coverage pct | 99.999985 |

## Private-Marker Rows That Explain The Parser Gap

| ID | Page | CUSIP | Marker Type | Book Value | Parser Status |
|---|---:|---|---|---:|---|
| CFKKRGACEDCOB-1006 | 240 | 90231*-AA-0 | statutory-private-marker-cusip | 202125000 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0081 | 219 | 78486#-AA-3 | statutory-private-marker-cusip | 61250000 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1080 | 243 | 09543#-AA-9 | statutory-private-marker-cusip | 54903258 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1095 | 244 | 09545*-AA-1 | statutory-private-marker-cusip | 54609338 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1158 | 246 | 45675#-AA-3 | statutory-private-marker-cusip | 53763837 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1085 | 243 | 09544*-AA-2 | statutory-private-marker-cusip | 40010505 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0068 | 219 | 00151@-AB-1 | statutory-private-marker-cusip | 34134276 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1154 | 245 | 26363*-AA-4 | statutory-private-marker-cusip | 31683331 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0069 | 219 | 12789@-AA-8 | statutory-private-marker-cusip | 29186321 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0067 | 219 | 00151@-AA-3 | statutory-private-marker-cusip | 27000000 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1007 | 240 | L9632@-AA-0 | statutory-private-marker-cusip | 21019811 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1155 | 245 | 45033@-AA-2 | statutory-private-marker-cusip | 18322566 | not-in-raw-parser-private-marker-or-geometry-row |

## Rows Not Promoted By The Raw Parser

| ID | Page | CUSIP | Marker Type | Book Value | Parser Status |
|---|---:|---|---|---:|---|
| CFKKRGACEDCOB-0067 | 219 | 00151@-AA-3 | statutory-private-marker-cusip | 27000000 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0068 | 219 | 00151@-AB-1 | statutory-private-marker-cusip | 34134276 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0069 | 219 | 12789@-AA-8 | statutory-private-marker-cusip | 29186321 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0070 | 219 | 12789@-AB-6 | statutory-private-marker-cusip | 2792287 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0071 | 219 | 12789@-AC-4 | statutory-private-marker-cusip | 3027207 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0072 | 219 | 12789@-AD-2 | statutory-private-marker-cusip | 3208321 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0073 | 219 | 12789@-AE-0 | statutory-private-marker-cusip | 3429583 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0081 | 219 | 78486#-AA-3 | statutory-private-marker-cusip | 61250000 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0197 | 222 | 04923#-AD-4 | statutory-private-marker-cusip | 6050522 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0863 | 237 | 85238@-AA-1 | statutory-private-marker-cusip | 5610639 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-0973 | 239 | 92939U-A@-5 | statutory-private-marker-cusip | 16200000 | not-in-raw-parser-private-marker-or-geometry-row |
| CFKKRGACEDCOB-1006 | 240 | 90231*-AA-0 | statutory-private-marker-cusip | 202125000 | not-in-raw-parser-private-marker-or-geometry-row |

## Proof Effect

This pass materially improves the KKR/Global Atlantic statutory prototype. The prior token parser showed a `-908.556531M USD` book-value variance because it missed or swallowed statutory private-marker rows and subtotal-adjacent geometry. The coordinate pass reads the same source pages by x/y column bands and nearly reconciles owned Schedule D bonds to the statutory target.

The safe use is:

`Accordia owned Schedule D bond book value is near-reconciled at coordinate-column level, including statutory private-marker CUSIP rows.`

## Boundary

This is still not full named-cash proof. It proves source-page owned-bond column reconciliation to near tolerance. It does not prove issuer-level income, disposal proceeds, borrower receipt/use, liability-cost spread, funds-withheld waterfall, FHLB economics, collateral certificates, or return.

## Next Action

Promote the coordinate-owned-bond table as the owned-bond baseline, then join it to income/proceeds fields and liability context. The next named-cash milestone is `accordia-coordinate-owned-bond-income-proceeds-join`.

## Decision

`kkr-global-atlantic-accordia-coordinate-owned-bond-near-reconciled-income-proceeds-join-next`
