# Apollo–Athene Eliant legal-entity bridge refresh

Research date: `2026-09-18`

## Result

`eliant-instrument-and-apollo-entity-perimeter-confirmed; borrower-and-cash-loop-open`

The Athene statutory packet contains two exact same-CUSIP Eliant routes:

| CUSIP | Athene statutory identity | Cash-like consideration candidate |
|---|---|---:|
| `28655*-AA-7` | Eliant Invest Holding LP, Class B, 5.683%, 12/15/2041 | `$358,251,536` |
| `28655*-AB-5` | Eliant Invest Holding LP, Class C, 6.133%, 12/15/2041 | `$189,464,130` |

The row-level packet records the first route's year-end book value at
`$23,238,692`, the `Various` consideration candidate at `$356,444,966`, and a
separate redemption-row candidate. The second route is a distinct CUSIP and is
not merged into the first route.

## Legal-entity evidence

Apollo's SEC subsidiary exhibit lists, in the same Apollo entity perimeter:

- Eliant Invest GP LP;
- Eliant Invest Holding LP;
- Eliant Invest Management LP;
- Apollo Eliant GP Advisors LLC; and
- Apollo Eliant Management GP LLC.

Athene's Q3 2025 statutory Schedule Y organizational chart separately lists
Eliant Invest GP LP and Eliant Invest Holding LP within the insurer's reported
holding-company-group organizational population. A current LEI record also
identifies Eliant Invest Holding LP as an active Delaware limited partnership,
with LEI `549300GBHFWXPLBUNT21` and Delaware registration identifier
`5871670`.

Together these sources strengthen the legal-entity and Apollo-related-wrapper
join behind the statutory CUSIPs. They do not establish that Apollo owns the
Athene asset, that Eliant is the underlying borrower, or that a statutory
consideration field was remitted as cash to Athene or Apollo.

## What remains open

1. Eliant offering, note-purchase, or private-placement documents.
2. Underlying borrower and collateral schedule.
3. Explanation of the `Various` event and the separate redemption event.
4. Trade confirmation, custodian statement, or settlement ledger for Athene.
5. Borrower receipt, use-of-proceeds, repayment, or trustee remittance evidence.
6. Athene liability-cost allocation and asset-level return model.

## Safe claim

`Athene's named Eliant statutory rows can now be routed to a corroborated
Apollo-related legal-entity perimeter: Apollo filings list Eliant GP,
Holding, Management, and Apollo Eliant management entities, while Athene's
organizational schedule independently lists Eliant Invest GP and Holding LP.
The statutory rows support cash-like consideration candidates of $358.252M and
$189.464M for separate Eliant tranches, but the underlying borrower, event
type, settlement, remittance, liability spread, and final return remain open.`

## Sources

- [Apollo SEC subsidiary exhibit](https://www.sec.gov/Archives/edgar/data/1411494/000141149422000014/exhibit211q42021.htm).
- [Athene Q3 2025 statutory statement](https://d1io3yog0oux5y.cloudfront.net/_dba1be0c285a911400c2777dd374e041/athene/db/2370/22514/pdf/AANY_3Q_2025_Statement_-_FINAL.pdf), Schedule Y.
- [Eliant Invest Holding LP LEI record](https://lei.bloomberg.com/leis/view/549300GBHFWXPLBUNT21).

