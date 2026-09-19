# Apollo/Athene AP Grange call-to-statutory bridge pass 1

Research date: `2026-09-18`

## Question

Does Athene's public Q2 2026 AP Grange call disclosure close the cash and
return route for the named 2025 Schedule BA AP Grange row?

## Public filing observation

Athene's Q2 2026 Form 10-Q lists investment-grade ABS debt issued by AP Grange
at `$5.080B` at December 31, 2025 and states that, during Q2 2026, AP Grange
called the ABS debt outstanding and Athene recognized a `$673M` gain. The filing
also states that concentration amounts may represent only a portion of the
total investments associated with a related party.

The local primary filing is
[Athene Q2 2026 Form 10-Q](../../raw/primary-sources/capital-flow/apollo/q2-2026/athene-q2-2026-10q.html).

The filing's structured XBRL concentration record independently reports the
`$673M` investment-related gain and the `$5.662B` March 31, 2026 / `$5.080B`
December 31, 2025 concentration values in the AP Grange row: [Athene XBRL
R48](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000028/R48.htm).

A separate exact-name public AP Grange operating agreement also appears in
search results, but it describes an Intel/co-investor project with units,
capital calls, and operating-account mechanics. No issuer, CUSIP, tranche, or
Athene crosswalk joins that agreement to the AP Grange ABS debt. It is held as
a same-name artifact, not merged into this route. See the [June 2024 AP Grange
operating agreement](https://www.sec.gov/Archives/edgar/data/50863/000005086324000103/a06032024form8-kex102.htm).

## 2025 statutory rows

The current Athene Schedule BA coordinate population shows a much narrower
instrument-level route:

| Schedule | Identifier | Source row | Value | Interpretation |
| --- | --- | --- | ---: | --- |
| Part 1 | `G2964#-AB-5` | AP Grange Holdings LLC, Tranche B | `$411.998739M` book value; `$31.661927M` investment income | Named year-end affiliated BA holding. |
| Part 2 | `G2964#-AB-5` | AP Dolphin / AP Grange Tranche B New | `$396.661750M` acquisition cost; `$33.407636M` additional investment | Addition/transfer row, not year-end cash or income by itself. |
| Part 3 | `G2964#-AB-5` | AP Grange Holdings LLC, Tranche B | `$313,313` consideration; `$313,313` book on disposal; nature blank | Statutory disposal/transfer/repayment event; settlement type unresolved. |

The Part 3 row also carries `$24,078` in its extracted investment-income
column. That is an event-row field and is not added to the Part 1 income row.

## Bridge result

The public `$673M` gain cannot currently be joined to the `$313,313` Part 3
consideration or the `$411.999M` Part 1 Tranche B book value. The most
defensible interpretation is:

`AP Grange issuer-level call and Athene gain visible -> exact affected notes,
legal-entity allocation, settlement proceeds, and gain attribution unresolved`

The filing's `$5.080B` concentration is an issuer/concentration perimeter,
not proof that Athene's one `G2964#-AB-5` Tranche B row represented the entire
called position. The statutory Part 3 blank nature field prevents calling the
`$313,313` event a cash call, sale, or repayment.

## Q2 2026 statutory Schedule D settlement candidate

The official [Athene statutory-filings page](https://ir.athene.com/financial-information/statutory-filings)
provides the second-quarter 2026 AAIA statutory statement. Its Schedule D
Part 4, PDF page `2490`, contains a current-quarter row for the exact
`G2964#-AA-7` instrument:

| Field | Filed value | Interpretation |
| --- | ---: | --- |
| Disposal date | `04/10/2026` | Current-quarter disposition, inside the AP Grange call window. |
| Purchaser | `Various` | Counterparty is not identified as a trustee, paying agent, or bank. |
| Consideration | `$4,052,553,175` | Statutory disposition consideration candidate. |
| Par value | `$3,687,230,219` | Position amount associated with the row. |
| Actual cost | `$3,690,374,758` | Statutory cost field. |
| Book/adjusted carrying value at disposal | `$3,691,539,180` | Legal-entity disposal carrying-value control. |
| Total gain/loss on disposal | `$(4,308,961)` | Row-level realized loss, not the issuer-level `$673M` GAAP gain. |
| Bond interest received during year | `$414,342,613` | Year-to-date statutory received-interest field; not an incremental Q2 receipt. |

This is a material upgrade: the exact Athene statutory instrument now has a
dated Q2 disposal row and a consideration amount. It narrows the event bridge
from `issuer call -> unidentified statutory lot` to
`issuer call -> G2964#-AA-7 dated 04/10/2026 disposal -> $4.053B statutory
consideration`. It still does not prove that the disposal was a redemption,
identify the paying agent or ultimate purchaser behind `Various`, show bank
settlement, allocate the `$673M` GAAP gain, or connect proceeds to Apollo
common-owner cash. The row is therefore a **statutory settlement candidate**,
not settled cash.

The direct statement is the [Q2 2026 AAIA statutory PDF](https://d1io3yog0oux5.cloudfront.net/_f301a7da18a01c1717e3734d3a0fe50c/athene/db/2370/22562/pdf/2Q+2026+AAIA+Statement.pdf).

A targeted scan of the statement's Schedule D Part 3 and Part 4 page range
(PDF pages `2457–2598`) found `G2964#-AA-7` only on page `2490`. It found no
`G2964#-AB-5` row and no second AP Grange row in that current-quarter
acquisition/disposition perimeter. This is a useful negative control: the
2025 Schedule BA Tranche B event is not silently being treated as a second Q2
2026 call-settlement row. It does not prove that no other AP Grange-related
position existed under a different identifier or in another legal entity.

### Reconciliation diagnostics — not a completed cash bridge

The new row is directionally close to, but does not reconcile, the other
public amounts:

| Comparison | Mechanical difference | Safe interpretation |
| --- | ---: | --- |
| `$5.080B` December 31 concentration less `$4.053B` row consideration | `$1.027B` | The issuer concentration and exact AAIA disposal row have different perimeter/measurement bases or include other positions; do not force a tie. |
| `$5.662B` March 31 concentration less `$4.053B` row consideration | `$1.609B` | The March concentration is not a payment instruction or exact affected-lot total. |
| Apollo's approximately `$5.0B` credit-strategy redemption flow less `$4.053B` row consideration | `$947M` | Fund-flow and statutory consideration are different scopes; this is not an unexplained missing receipt. |
| `$4.053B` consideration less `$3.692B` disposal book value | `$361M` | A statutory consideration-versus-carrying-value diagnostic; it is not the `$673M` GAAP gain allocation. |

These differences are retained as explicit perimeter controls. They are not
used to infer other called tranches, fees, taxes, or owner cash.

Apollo's Q2 2026 Form 10-Q adds a separate cross-entity anchor: its
credit-strategy net flows included approximately `$5.0B` of redemptions related
to the prepayment of AP Grange. This makes the event visible in Apollo's
fund-flow perimeter, but the rounded AUM/net-flow amount is not a bank receipt
and does not identify Athene's tranche allocation. See the [prepayment
cross-entity bridge](capital-flow-apollo-athene-ap-grange-prepayment-cross-entity-bridge-pass-2-2026-09-18.md).

## What this upgrades

- It provides a current-period public issuer-level call and realized-gain
  observation for a named Apollo/Athene route.
- It creates a specific reconciliation target: AP Grange call schedule,
  affected tranche/CUSIP population, settlement proceeds, and gain allocation.
- It shows why public gain recognition can be directionally relevant without
  being substituted for the legal-entity cash ledger.

## What remains open

- AP Grange call notice, payment date, paying agent, and settlement account;
- the full Athene AP Grange position by tranche/CUSIP before the call;
- allocation of the `$673M` gain across Athene entities and instruments;
- reconciliation of the issuer-level `$5.080B` concentration to statutory
  holdings and the `$313,313` Part 3 event;
- fees, taxes, liability cost, and net spread;
- cash remittance to Athene and any upstream Apollo distribution.
- exact relationship between Apollo's approximately `$5.0B` fund-flow figure
  and Athene's `$673M` gain / `$5.662B` concentration.

## Decision

`ap-grange-public-call-and-gain-visible; instrument-level-settlement-and-return-hold`

The next source should be the AP Grange call notice, trustee/remittance record,
or Athene investment accounting/custody workpaper, not another broad issuer
search.

The machine-readable companion is the [AP Grange call/statutory bridge ledger](data/capital-flow-apollo-athene-ap-grange-call-statutory-bridge-pass-1-2026-09-18.csv). It preserves the issuer-level call and gain separately from the statutory holding, addition, and unclassified event rows; none is treated as settled cash or asset-level return.
