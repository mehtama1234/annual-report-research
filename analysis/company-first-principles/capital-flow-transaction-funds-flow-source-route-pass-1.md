# Capital Flow Transaction Funds-Flow Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-011`.

It asks:

`Can current local evidence reconcile acquisition, refinancing, merger, redemption, settlement, tax, fee, assumed-debt, and final cash-use mechanics for the affected transaction rows?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-transaction-funds-flow-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full transaction closing funds-flow upgrade yet. All five affected rows have partial transaction mechanics: Matador has aggregate source/use and BLM acquisition-use context; Devon has statement-level treasury source/use reconciliation and Coterra merger cash separation; PBF has note-refinancing proceeds, redemption, fees, and coupon math; Liberty Broadband has debenture-put retirement, funding-source language, debt rollforward, and collateral context; Plains has Cactus III acquisition/control and assumed-debt accounting context. None has the final closing package needed to prove full proceeds, fee, tax, settlement, debt-treatment, and final economic outcome.`

## Row Outcomes

| Row | Case | Current Transaction Evidence | Funds-Flow Result | Remaining Gap |
|---|---|---|---|---|
| `CFTFSR-001` | Matador borrowing base | H1 `2026` operating cash of `1.407674B USD`; net financing of `661.672M USD`; visible sources of `2.069346B USD` matching net investing use plus cash/restricted-cash increase; `745.343M USD` development capex; `1.228834B USD` oil-and-gas property acquisitions; named `1.160B USD` BLM Acquisition | Partial aggregate acquisition funds-use proxy | No BLM closing statement, borrowing notices, note-proceeds allocation, lender allocation, purchase-price settlement, title/reserve support, fee/tax allocation, or asset cash contribution |
| `CFTFSR-002` | Devon treasury allocation | H1 `2026` visible sources and uses both equal `6.451B USD`; sources include `5.329B USD` OCF and `581M USD` Coterra merger cash; uses include `2.157B USD` capex, `2.919B USD` property/equipment acquisitions, `500M USD` debt repayment, `266M USD` buybacks, and `521M USD` dividends; non-cash merger stock consideration and assumed debt kept separate | Partial statement-level treasury and merger funds-flow proxy | No daily cash ledger, closing funds-flow, BLM lease payment support, debt repayment notices, make-whole economics, source priority, synergy realization, or asset-level return |
| `CFTFSR-003` | PBF refinancing | `500.0M USD` of 2034 notes; `492.1M USD` net proceeds; redemption of `801.6M USD` 2028 notes at par plus accrued interest; at least `309.5M USD` available-cash bridge before accrued interest; `301.6M USD` principal reduction; `7.9M USD` deferred financing costs and other net; `2.2M USD` extinguishment loss; `11.846M USD` simple annual coupon relief | Partial note-refinancing settlement mechanics proxy | No redemption settlement detail, accrued-interest split, pro forma interest schedule, fee amortization, tax treatment, liquidity opportunity cost, ABL availability, or refinery-level return |
| `CFTFSR-004` | Liberty Broadband holdco | April `6`, `2026` put and retirement of all outstanding `3.125%` exchangeable senior debentures due `2053`; `966M USD` paid including accrued interest using Margin Loan Facility proceeds and restricted cash; debenture carrying value moved from `956M USD` to zero; total debt fell by `523M USD`; instrument rollforward reconciles debenture retirement against `74M USD` margin-loan increase and `359M USD` new Charter loan | Partial debenture-retirement funds-flow proxy | No accrued-interest split, fair-value rollforward, exact restricted-cash/margin-loan source split, contractual LTV certificate, Charter loan full economics, tax outcome, final merger funds-flow, or shareholder realization |
| `CFTFSR-005` | Plains tariff route | Cactus III acquisition/control context: `55%` and `45%` stake acquisitions with assumed debt, about `2.016B USD` purchase-accounting consideration, `2.737B USD` property and equipment acquired, Cactus III capacity above `600000 bpd`, and Plains operator-of-record status | Partial acquisition/control accounting proxy | No closing statement, final funds-flow, debt assumption schedule, fee/tax allocation, purchase-price allocation detail, route revenue, committed-volume economics, Cactus III cash contribution, or asset return |

## Decision

`transaction-funds-flow-source-route-hold-with-partials`

`CFRMSWO-011` is executed against the current local source set. It produces five partial transaction-mechanics rows and no full closing funds-flow proof:

- Matador: partial aggregate acquisition funds-use proxy.
- Devon: partial statement-level treasury and merger funds-flow proxy.
- PBF: partial note-refinancing settlement mechanics proxy.
- Liberty Broadband: partial debenture-retirement funds-flow proxy.
- Plains: partial acquisition/control accounting proxy.

## Safe Claim

`The transaction funds-flow source-route pass confirms that all five affected rows have some acquisition, refinancing, merger, redemption, settlement, or accounting mechanics visible, but the current local evidence does not prove final closing funds-flow, exact source priority, fee and tax treatment, settlement allocation, debt-close treatment, asset-level cash contribution, or final economic outcome across the affected rows.`

## Next Work

1. For Matador, pull BLM closing/payment records, borrowing notices, lender allocation, note-proceeds allocation, title/reserve support, and acquisition funds-flow.
2. For Devon, pull treasury cash ledgers, Coterra closing funds-flow, debt repayment notices, make-whole calculations, BLM lease records, and realized synergy support.
3. For PBF, pull redemption notices, settlement statements, accrued-interest split, pro forma interest, fee amortization, tax treatment, ABL availability, and refinery-level cash support.
4. For Liberty Broadband, pull debenture settlement statements, put notices, restricted-cash rollforward, margin-loan/LTV certificates, Charter loan agreement terms, tax treatment, and final merger closing documents.
5. For Plains, pull closing statements, purchase-price allocation detail, assumed-debt support, fee/tax allocation, committed-volume agreements, route revenue, and Cactus III contribution support.
6. Move next to `CFRMSWO-012` IRR, NPV, ROIC, reserve-life, or return-model support.
