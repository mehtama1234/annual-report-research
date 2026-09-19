# Apollo–Athene private-credit public-search boundary

Research date: `2026-09-16`

This bounded search tests whether the two Apollo-related private-credit routes
in the Athene same-CUSIP packet expose public issuer, offering, collateral,
borrower-cash, or repayment documents.

| Route | Search perimeter | Result | Meaning |
| --- | --- | --- | --- |
| Eliant `28655*-AA-7` / `28655*-AB-5` | Exact issuer name, CUSIP fragments, Apollo/Eliant entity names, SEC filing routes, offering memorandum, note purchase, collateral, repayment, and remittance terms | `searched-negative` | Apollo entity evidence exists, but no current public borrower/collateral or receipt ledger was located |
| AP Aristotle `00264#-AB-3` | Exact issuer name, CUSIP fragments, note terms, offering memorandum, private placement, repayment, borrower, collateral, and remittance terms | `searched-negative` | Statutory disposition rows exist, but no current public borrower/collateral or receipt ledger was located |

This is a public-perimeter result, not a claim that private records do not
exist. The routes remain issuer-named cash-like candidates, below borrower
receipt, source/use, liability-cost, and asset-return promotion.

Structured control: [private-credit search boundary CSV](data/capital-flow-apollo-athene-private-credit-public-search-boundary-2026-09-16.csv).

Public Apollo entity context: [SEC subsidiary exhibit](https://www.sec.gov/Archives/edgar/data/1411494/000141149422000014/exhibit211q42021.htm).

