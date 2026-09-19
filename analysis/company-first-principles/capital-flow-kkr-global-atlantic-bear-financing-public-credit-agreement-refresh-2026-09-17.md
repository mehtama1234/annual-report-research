# Capital Flow KKR Global Atlantic Bear Financing Public Credit-Agreement Refresh

Research date: `2026-09-17`

## Purpose

This refresh upgrades the [Bear Financing source-acquisition packet](capital-flow-kkr-global-atlantic-accordia-bear-financing-source-acquisition-packet-pass-1.md)
using the official Accordia annual statement published by Global Atlantic. It
tests whether the private-marker issuer can be connected to a dated legal
credit agreement and an affiliated legal-entity perimeter.

## Primary-source result

The FY2024 Accordia annual statement states that:

- on January 5, 2024, Accordia entered into a credit agreement with 2023 Bear
  Financing L.P.;
- Accordia committed to issue a `$245,000,000` senior loan to Bear Financing;
- Accordia and Bear Financing are both indirect subsidiaries of KKR, which the
  filing identifies as Accordia's ultimate controlling person.

The same filing's Schedule D page 166 identifies the matching private-marker
CUSIP `90231*-AA-0` as `2023 BEAR FINANCING L.P.` and reports:

| Field | FY2024 source observation |
|---|---:|
| Book / par value | `$202.125M` |
| Fair value | `$202.7718M` |
| Stated rate | `8.500%` |
| Effective rate | `8.612%` |
| Interest due/accrued | `$6.585906M` |
| Interest received during year | `$11.604153M` |
| Acquired date | `01/05/2024` |
| Maturity date | `01/05/2039` |

The later Q4 2025 coordinate row already in the local corpus carries the same
CUSIP and issuer with `$202.125M` book value and `$17.419245M` interest
received. The two observations strengthen continuity across reporting periods,
but they are not a principal-repayment or bank-settlement record.

## What this upgrades

The route now moves from:

`source-visible private-marker issuer and statutory income`

to:

`Accordia legal entity -> dated $245M senior-loan credit agreement -> KKR-affiliated Bear Financing borrower -> matching Schedule D CUSIP -> period-specific interest fields`

This is materially stronger legal-entity and instrument evidence. It also
clarifies the relationship: this is an affiliated intercompany or controlled
investment route, not merely a third-party bond label.

## What it does not prove

The annual statement does not, in the checked excerpts, establish:

- the draw date and bank account;
- whether the `$245M` commitment was fully funded;
- borrower use of proceeds;
- principal amortization or repayment;
- cash interest settlement separate from accrual;
- collateral, guarantees, or covenant package;
- Accordia liability-cost or funds-held allocation; or
- KKR parent or common-owner residual cash.

The `$245M` credit-agreement commitment must not be added to the `$202.125M`
book value or to the interest fields. They are different objects and periods.

## QoE and financial-integrity controls

This refresh closes a legal-instrument identity gap but not a cash gap. The
period comparison should test interest-received growth, book-value continuity,
fair-value movement, commitment-versus-funded amount, and any related-party
eliminations. Those are reconciliation prompts, not evidence of manipulation.

## Next promotion documents

1. Credit agreement and amendments, including funding conditions and use of
   proceeds.
2. Accordia loan subledger and bank/custody draw confirmation.
3. Bear Financing borrower financials and repayment schedule.
4. Interest payment notices or account statements separating cash from accrual.
5. KKR/Global Atlantic related-party elimination and liability-cost schedules.

## Safe claim

`The official FY2024 Accordia annual statement now connects CUSIP 90231*-AA-0 and 2023 Bear Financing L.P. to a January 5, 2024 $245M senior-loan credit agreement and identifies both entities as indirect KKR subsidiaries. The matching Schedule D row reports $202.125M of book value, an 8.500% stated rate, and $11.604153M of FY2024 interest received; the later FY2025 row reports $17.419245M. This upgrades legal-entity and instrument continuity, but does not prove draw, borrower use, settlement, liability-adjusted spread, repayment, or owner cash.`

## Decision

`bear-financing-dated-credit-agreement-and-affiliate-perimeter-visible; draw-settlement-use-and-return-open`

## Primary source

[Global Atlantic / Accordia FY2024 annual statement](https://www.globalatlantic.com/sites/globalatlantic/files/PDFs/Financial_Statements/FY2024/Accordia_4Q24_Annual_Statement.PDF)
