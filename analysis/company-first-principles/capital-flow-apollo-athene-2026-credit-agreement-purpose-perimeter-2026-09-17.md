# Apollo–Athene 2026 credit agreement: purpose and entity perimeter

Research date: `2026-09-17`

This pass tests whether Athene's June 26, 2026 public credit agreement can
close any part of Q-07's financing-to-common-owner bridge. It does not treat a
facility, commitment, or permitted use as a borrowing, receipt, distribution,
or common-owner residual.

## What the agreement establishes

| Field | Observed evidence | Safe interpretation |
| --- | --- | --- |
| Borrower perimeter | Athene Holding Ltd., Athene Annuity Re Ltd., Athene Life Re Ltd., and Athene USA Corporation are the named borrowers. | This is an AHL/Athene borrowing perimeter; it is not an AGM receiving-account record. |
| Aggregate commitment | The agreement states aggregate commitments of `$1.750B` as of the agreement date. | Facility capacity is not a drawn balance or cash receipt. |
| Facility balance at quarter end | Athene's Q2 2026 Form 10-Q states that no amounts were outstanding under the current or previous credit facilities as of June 30, 2026. | This closes the external revolving-facility draw hypothesis at the quarter-end date; it does not address the separate AHL-to-AGM intercompany note or other private funding. |
| Contractual purpose | Borrowers may use borrowings for working capital and other lawful corporate purposes. | Purpose language is broad and does not identify asset purchases, dividends, AGM transfers, or a specific use of proceeds. |
| Affiliate/intercompany perimeter | The agreement permits specified transactions among borrowers, their subsidiaries, AHL, HoldCo entities, and affiliates, subject to stated conditions; it separately permits debt among AHL, HoldCo entities, and subsidiaries when not prohibited. | Legal permission is not evidence that a transaction occurred or that it was cash-funded. |
| Financial covenant | The agreement sets a minimum consolidated net worth of `$22.059963B` and a maximum consolidated debt-to-capitalization ratio of `40%`. | These are lender constraints on the consolidated AHL group, not a common-owner cash denominator. |
| Public observability | The agreement requires consolidated financial statements and certain statutory statements to be delivered to the administrative agent, with public delivery possible when filed with the SEC. | It creates a future document route but does not expose loan notices, bank wires, or a controlled cash ledger. |

## Q-07 effect

This upgrades the financing layer from a generic intercompany-note observation
to a dated, primary-filed facility-purpose and borrower-perimeter control. The
following remain open:

- whether any borrowing occurred;
- draw date, amount, and receiving account;
- whether proceeds reached AGM or another HoldCo entity;
- use-of-proceeds allocation;
- intercompany elimination;
- debt service and liability cost; and
- the residual available to Apollo common owners.

The facility therefore remains `financing-perimeter-visible; external draw
closed at June 30; receipt-unproven`.

## Note-balance date control

The apparent `$279M`/`$280M` discrepancy is not a same-date conflict. The
March 31, 2026 filing reports a `$280M` AHL note receivable from AGM; the June
30, 2026 Form 10-Q reports `$279M` and comparative December 31, 2025 balance
of `$227M`. The longitudinal series should therefore retain `$280M` at March
31 and `$279M` at June 30. The one-million-dollar sequential change is a
reported period-end balance movement, not evidence of a repayment or cash
receipt. The filings still do not provide dated draw notices, principal versus
interest components, bank settlement, or use of proceeds.

This date control also keeps the external-facility statement separate: the
June 30 Form 10-Q says no amounts were outstanding under the current or
previous external credit facilities, while separately disclosing the AHL
receivable from AGM and an AHL note payable with no outstanding balance. Those
are different instruments and directions.

## Primary source

- [Athene Q2 2026 Form 10-Q, Exhibit 10.1 — June 26, 2026 Credit Agreement](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/q22026exhibit101.htm)
- [Athene Q2 2026 Form 10-Q — Note 8, Debt](https://www.sec.gov/Archives/edgar/data/1527469/000152746926000056/ahl-20260630.htm)

Structured rows: [credit-agreement purpose-perimeter CSV](data/capital-flow-apollo-athene-2026-credit-agreement-purpose-perimeter-2026-09-17.csv).
