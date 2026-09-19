# Wheaton–Antamina Q-03 receivable-classification boundary

Research date: `2026-09-17`

## Why this update matters

The Q2 financial statements provide a useful negative control for the Q-03
receipt search. Wheaton reports total accounts receivable of `$26.056M` at
June 30, 2026, consisting of `$17.867M` of provisional concentrate-sale trade
receivables, `$7.200M` of cobalt-sale trade receivables, and `$0.989M` of other
receivables. The filing separately says that precious-metal credits are sold
through bullion banks and that revenue is recognized when control transfers.

The statement does not identify an Antamina, BHP, or metal-credit receivable in
that accounts-receivable table. That narrows the public classification
evidence, but it does not prove that no BHP-related amount existed: a credit
could have been sold, settled, netted, included in another line, or disclosed
only in a transaction-level ledger unavailable in the filing.

## Observed Q2 classification surface

| Field | June 30, 2026 | December 31, 2025 | Interpretation |
|---|---:|---:|---|
| Total accounts receivable | `$26.056M` | `$46.723M` | Company-wide balance, not an Antamina cash receipt |
| Provisional concentrate-sale trade receivables | `$17.867M` | `$41.545M` | Concentrate route, not identified as BHP metal credits |
| Cobalt-sale trade receivables | `$7.200M` | `$3.472M` | Separate cobalt route |
| Other accounts receivable | `$0.989M` | `$1.706M` | Unallocated public category |

## What this proves

- The public Q2 accounts-receivable table is not a BHP-specific receipt ledger.
- Wheaton's accounting policy confirms a metal-credit sale can be recognized
  when the credit is sold through a bullion bank, so physical delivery is not
  the required evidence object.
- The company-wide receivable decline cannot be assigned to BHP settlement,
  and the `$0.989M` “other” category cannot be promoted to an Antamina claim.

## Remaining promotion object

The decisive source remains a BHP-to-Wheaton credit issuance, sale or
receivable record with credit date, payable ounces, price, settlement, and bank
collection. If the credit was sold before period end, the matching sales and
cash record must identify the BHP route; if it remained outstanding, the
receivable note or counterparty ledger must identify it.

## Decision

Q-03 remains `searched-negative` for a publicly identified BHP-specific
receivable or bank receipt and `full-return-inputs-incomplete`. This is a
classification-boundary upgrade, not a cash-receipt upgrade. No Antamina
receipt, owner cash, or return ranking is promoted.

## Sources

- [Wheaton Q2 2026 financial statements](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm)
- [Wheaton Q2 2026 results exhibit](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex991.htm)

Structured companion: [Q-03 receivable classification table](data/capital-flow-wheaton-antamina-q03-receivable-classification-boundary-2026-09-17.csv).
