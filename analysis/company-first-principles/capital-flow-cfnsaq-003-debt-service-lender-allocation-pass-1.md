# Capital Flow CFNSAQ-003 Debt-Service/Lender Allocation Pass 1

## Purpose

This page executes the third row of the next-source acquisition queue.

It asks:

`Can current local sources tie source cash, debt service, lender allocation, funds-flow, or payback mechanics to named capital providers and named uses?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cfnsaq-003-debt-service-lender-allocation-pass-1.csv`

The queue input is:

`/cluster/capital-flow-next-source-acquisition-queue-pass-1.md`

## Short Answer

`CFNSAQ-003 is executed against the current local source set. It finds four partial routing/payback rows: Matador, PBF, Liberty Broadband, and Devon. Wheaton, Cheniere, Energy Transfer, and Plains remain holds because their evidence still does not connect named project, asset, route, train, or PMPA cash to lender-level debt service, restricted-account waterfalls, or exact source-to-use allocation.`

## Execution Result

| Row | Target Case | Current Evidence | Result | What Still Blocks Proof |
|---|---|---|---|---|
| `CFNSAQ003-001` | Wheaton Antamina | `4.300B USD` Antamina PMPA payment; `1.500B USD` term loan; `472.000M USD` revolver debt; `2.700B USD` bank debt drawn; `728M USD` bank debt repaid; H1 `2026` Antamina stream revenue of `277.563M USD` | `hold-no-antamina-debt-service-waterfall` | Antamina-specific borrowing notice, lender allocation, repayment waterfall, interest allocation, restricted account schedule, PMPA closing funds-flow |
| `CFNSAQ003-002` | Cheniere LNG | SPL/CQP/CCH/parent debt buckets; about `29.0B USD` debt plus interest payments; FY `2025` revenue of `19.98B USD`; Q2 `2026` DCF of `1.17B USD`; cargo and contracted-demand evidence | `hold-no-train-or-entity-waterfall` | Train/entity restricted-account schedule, debt draw, DSCR, distribution waterfall, SPA cash attribution, project-level debt-service coverage |
| `CFNSAQ003-003` | Energy Transfer projects | Q2 `2026` EBITDA/DCF, growth capex, `3.76B USD` unused credit-facility availability, `68.393B USD` long-term debt, senior-note refinancing, named capacity additions | `hold-no-named-project-debt-service-allocation` | Named-project debt-service allocation, shipper cash, project EBITDA, repayment waterfall |
| `CFNSAQ003-004` | Matador borrowing base | `3.250B USD` borrowing base; `2.750B USD` elected commitments; `939.000M USD` borrowings; `53.800M USD` letters of credit; aggregate H1 source/use evidence | `partial-borrowing-base-debt-movement-proxy` | Borrowing notices, lender schedule, reserve/collateral support, cash-interest schedule, source-specific use, BLM closing statement |
| `CFNSAQ003-005` | PBF refinancing | `500.0M USD` 2034 notes; `492.1M USD` net proceeds; `801.6M USD` 2028 notes redeemed; `894.100M USD` cash; `1.749100B USD` long-term debt | `partial-note-refinancing-debt-service-proxy` | Full redemption settlement, accrued-interest split, pro forma debt-service schedule, fee/tax amortization, ABL support, refinery cash allocation |
| `CFNSAQ003-006` | Liberty Broadband holdco | `966M USD` debenture retirement; `1.150B USD` term loan facility; `864M USD` margin loan outstanding; `359M USD` Charter loan outstanding; `5.507B USD` Charter investment collateral asset | `partial-holdco-debt-repayment-collateral-proxy` | Restricted-cash/facility split, LTV certificate, collateral schedule, Charter loan economics, merger funds-flow, tax allocation |
| `CFNSAQ003-007` | Devon treasury allocation | H1 `2026` visible sources and uses both equal `6.451B USD`, including `5.329B USD` OCF and `581M USD` Coterra merger cash | `partial-statement-level-treasury-merger-funds-flow-proxy` | Daily cash ledger, closing funds-flow, use-by-source priority, lease payment support, debt repayment notices, make-whole economics, asset-level return |
| `CFNSAQ003-008` | Plains tariff route | Published tariff route/rate, negotiated-rate mechanic, Cactus III capacity and acquisition/control context, including `55%` and `45%` stake acquisitions | `hold-no-route-debt-service` | Route billing volume, realized revenue, route EBITDA/cash, asset-level debt-service, lender allocation, closing statement, route return |

## What This Answers

This pass is the payback-routing test. It shows where financing mechanics are visible enough to explain a capital path, but still not enough to prove capital-provider payback from the named asset:

- Matador shows borrowing-base size, elected commitments, borrowings, letters of credit, and aggregate source/use mechanics.
- PBF shows note proceeds and redemption mechanics.
- Liberty shows holdco debt retirement, margin-loan/collateral context, and Charter loan balances.
- Devon shows a statement-level treasury envelope.
- Wheaton has a named Antamina cash use and strong stream economics, but not a PMPA-level lender waterfall.
- Cheniere has entity debt and LNG cash proxies, but not train/entity waterfall proof.
- Energy Transfer has company cash, capex, debt, and refinancing capacity, but not named-project allocation.
- Plains has tariff/acquisition context, but not route revenue or debt-service allocation.

## Decision

`cfnsaq-003-executed-current-local-mixed-partial-hold`

The queue row is executed against current local evidence. It improves the money-route answer for four cases, but it does not close full lender/payback proof for any case.

## Safe Claim

`The current local source set shows partial debt-service, lender, source/use, or funds-flow mechanics for Matador, PBF, Liberty Broadband, and Devon. Wheaton, Cheniere, Energy Transfer, and Plains remain holds below named waterfall or lender-allocation proof. No CFNSAQ-003 row proves full capital-provider payback from a named asset or project.`

## Next Work

1. Move to `CFNSAQ-004` for statutory legal-entity schedules, borrower facility files, and collateral availability.
2. Preserve all debt-service and lender-allocation holds unless borrowing notices, lender schedules, restricted-account waterfalls, settlement statements, or contractual collateral/LTV certificates are acquired.
