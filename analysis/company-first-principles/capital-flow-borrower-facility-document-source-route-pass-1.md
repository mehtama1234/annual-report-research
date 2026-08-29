# Capital Flow Borrower Facility Document Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-005`.

It asks:

`Can current local evidence tie private-credit, insurance-credit, or borrowing-base exposure to borrower facility size, use of proceeds, lender share, borrower repayment route, and bank residual role?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-borrower-facility-document-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full borrower facility and lender-schedule upgrade yet. Ares/Frontline and Matador are partials: Ares has borrower-destination, arranger-role, holder-dollar, commitment, and instrument-marker evidence; Matador has agreement-grade reserve-based facility evidence and bank-lender group visibility. KKR/Global Atlantic and Blackstone remain holds because the current local evidence does not tie channel assets or borrower candidates to statutory vehicles, facility schedules, lender allocations, use of proceeds, borrower cash flow, or repayments.`

## Row Outcomes

| Row | Case | Current Facility/Borrower Evidence | Facility Result | Remaining Gap |
|---|---|---|---|---|
| `CFBFDSR-001` | KKR / Global Atlantic channel | `220B USD` Global Atlantic AUM, `164B USD` credit AUM, `62B USD` Ivy/sponsored reinsurance vehicle AUM, `189.204380B USD` insurance investments, `48.754106B USD` mortgage and other loan receivables net, asset-income, allowance, LTV, and FHLB pledged-asset context | Hold with insurance asset-class proxy | No statutory legal-entity schedule, borrower/facility schedule, private-placement loan record, use of proceeds, borrower cash receipt, repayment performance, or liability-cost spread |
| `CFBFDSR-002` | Ares borrower exposure | Frontline Road Safety operating-borrower context, Bain sponsor transaction, Ares arranger/bookrunner role, latest Q2 `2026` visible holder fair value of `198.675M USD`, `54.300M USD` visible commitment context, first-lien senior secured loan markers, and March `2032` maturity cluster | Partial borrower facility marker and holder-dollar proxy | No total facility size, Ares funded allocation, full lender group, use-of-proceeds funds-flow, borrower financials, debt-service coverage, payoff letter, or bank residual-role proof |
| `CFBFDSR-003` | Blackstone credit channel | Credit & Insurance AUM, inflows, deployment, BXSL public vehicle denominator, industry destinations, and borrower candidates including Auctane/Stamps.com, Guidehouse, and Medallia | Hold with borrower-candidate facility context | No Blackstone vehicle-to-borrower allocation, lender schedule, funded tranche share, use of proceeds, borrower cash flow, interest/principal receipts, repayment evidence, or bank-role resolution |
| `CFBFDSR-004` | Matador borrowing base | Reserve-based Credit Agreement, June `2026` borrowing-base reaffirmation, `3.25B USD` borrowing base, `2.75B USD` elected commitments, PNC administrative agent, broad bank lender group, collateral mechanics, draws/repayments, OCF, capex, acquisitions, and production/revenue output | Partial bank-facility and lender-group proxy | No lender commitment allocation, borrowing notices, borrowing-base certificate, reserve/collateral valuation, acquisition funds-flow, cash-interest schedule, or asset-area repayment route |

## Decision

`borrower-facility-document-source-route-hold-with-partials`

`CFRMSWO-005` is executed against the current local source set. It produces two partial facility/lender rows and two holds:

- Ares/Frontline: partial borrower facility marker and holder-dollar proxy.
- Matador: partial bank-facility and lender-group proxy.
- KKR/Global Atlantic: hold below statutory vehicle-to-borrower facility proof.
- Blackstone: hold below vehicle-to-borrower facility proof.

## Safe Claim

`The borrower facility document source-route pass confirms that current local evidence can identify some borrower/facility markers, holder-dollar exposure, bank-facility mechanics, and lender-group context, but it does not yet prove full borrower facility size, lender allocation, use of proceeds, borrower cash generation, repayment route, or bank replacement across the four affected rows.`

## Next Work

1. For Ares/Frontline, pull the Frontline credit agreement or amendment, lender schedule, use-of-proceeds funds-flow, borrower financials, payoff letter, UCC termination/amendment, and bank-role evidence.
2. For Matador, extract the full credit-agreement lender commitment schedule, borrowing notices, borrowing-base certificate, reserve report, cash-interest schedule, and BLM acquisition funds-flow.
3. For KKR/Global Atlantic, pull statutory legal-entity schedules, Schedule D/BA holdings, private-placement or loan schedules, FHLB collateral files, borrower records, and liability-cost schedules.
4. For Blackstone, join BXSL/BCRED/N-PORT/SMA holdings to borrower candidates and pull credit agreements, debt commitment letters, lender schedules, payoff letters, and borrower cash-flow evidence.
5. Move next to `CFRMSWO-006` statutory investment schedules and asset-income detail.
