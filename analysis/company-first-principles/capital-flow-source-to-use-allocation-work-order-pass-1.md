# Capital Flow Source-To-Use Allocation Work Order Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-002`.

It asks:

`Can current local evidence tie specific financing or cash sources to specific capex, acquisition, debt repayment, payout, project, or restructuring uses?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-source-to-use-allocation-work-order-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full source-to-use allocation upgrade across the affected set. PBF and Liberty have the strongest transaction-level source/use mechanics with boundaries. Matador and Devon have useful aggregate source/use reconciliations but not source-priority proof. FPL and Energy Transfer remain holds because current local evidence does not allocate debt, equity, cash, revolver, note, or retained-cash sources to the named category or named projects.`

## Row Outcomes

| Row | Case | Current Local Evidence | Source-To-Use Result | Remaining Gap |
|---|---|---|---|---|
| `CFSTUA-001` | FPL Distribution Inspection | Recovery components, FPL-wide cash/capex/debt context, capital-structure support | Hold | No debt/equity/cash source allocation to Distribution Inspection projects |
| `CFSTUA-002` | Energy Transfer projects | EBITDA, DCF, growth capex, revolver availability, senior notes, refinancing, named capacity additions | Hold | No allocation from retained cash, revolver, notes, or debt stack to Nederland/Lone Star/y-grade projects |
| `CFSTUA-003` | Matador borrowing base | Operating cash plus net financing reconciles to aggregate investing use and cash/restricted-cash increase | Aggregate source/use pass with boundary | No borrowing notice, lender allocation, note-proceeds allocation, BLM funds-flow, or asset-level cash tie |
| `CFSTUA-004` | Devon treasury allocation | H1 2026 visible sources equal visible uses across OCF, merger cash, cash drawdown, capex, acquisitions, debt repayment, dividends, buybacks | Aggregate treasury envelope pass with boundary | No daily source priority, use-by-source allocation, Permian lease funds-flow, payout source, or stress-tested coverage |
| `CFSTUA-005` | PBF refinancing | 2034 note proceeds, cash bridge, 2028 note redemption, revolver borrowings/repayments, OCF context | Transaction source/use mechanics pass with boundary | No redemption settlement, accrued interest, fee/tax allocation, ABL availability, or refinery-level cash use/return |
| `CFSTUA-006` | Liberty Broadband holdco | Charter loan, margin-loan proceeds, restricted cash, debenture retirement, margin-loan repayment, collateral context | Holdco transaction source/use mechanics pass with boundary | No restricted-cash split, contractual LTV certificate, Charter loan full economics, merger funds-flow, tax, or shareholder realization |

## Decision

`source-to-use-allocation-work-order-mixed-boundary`

`CFRMSWO-002` is executed against the current local source set. The result is not a full graph upgrade. It separates transaction-level mechanics from true allocation proof:

- PBF and Liberty have the strongest specific source/use mechanics.
- Matador and Devon have aggregate reconciliations.
- FPL and Energy Transfer remain allocation holds.

## Safe Claim

`The source-to-use allocation pass shows that the current evidence can sometimes reconcile sources and uses at transaction or aggregate treasury level, but it does not prove named source-to-use allocation across the affected set. FPL and Energy Transfer remain holds; Matador and Devon remain aggregate-envelope cases; PBF and Liberty pass transaction-mechanics visibility with unresolved economic and final funds-flow boundaries.`

## Next Work

1. For FPL, find debt/equity/cash funding support tied to Distribution Inspection.
2. For Energy Transfer, find project capital schedules and retained-cash/revolver/note allocation to named projects.
3. For Matador and Devon, find borrowing notices, treasury ledgers, closing statements, and source-priority support.
4. For PBF and Liberty, find settlement statements, fee/tax schedules, restricted-cash split, and final funds-flow documents.
5. Move next to `CFRMSWO-003` project or asset cash contribution.
