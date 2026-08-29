# Capital Flow Debt-Service Waterfall Source Route Pass 1

## Purpose

This page executes repeated missing-source work-order row `CFRMSWO-004`.

It asks:

`Can current local evidence tie asset, project, route, or transaction cash to debt service, lender allocation, creditor payback, restricted accounts, or a repayment waterfall?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-debt-service-waterfall-source-route-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-repeated-missing-source-work-order-pass-1.md`

## Short Answer

`No full debt-service waterfall or lender-allocation upgrade yet. PBF, Liberty Broadband, and Matador have the strongest partial debt/payback mechanics. Wheaton, Cheniere, and Energy Transfer show financing or entity-debt context but not asset/project payback allocation. Plains remains a tariff-route case with no current route debt-service proof.`

## Row Outcomes

| Row | Case | Current Debt/Payback Evidence | Waterfall Result | Remaining Gap |
|---|---|---|---|---|
| `CFDSWSR-001` | Wheaton Antamina | `4.300B USD` Antamina PMPA payment, `1.500B USD` term loan, `472.000M USD` revolver debt, `2.700B USD` bank debt drawn, `728.000M USD` repaid, and Antamina OCF/profit proxy | Hold with financing-context proxy | No Antamina-specific debt-service schedule, lender allocation, borrowing notice, repayment waterfall, interest allocation, or PMPA payback model |
| `CFDSWSR-002` | Cheniere LNG | SPL/CQP/CCH/parent debt buckets, `29.0B USD` debt plus interest payments, LNG revenue/EBITDA/DCF, cargo output, contracted production, and train milestones | Hold with entity-debt denominator proxy | No train/entity restricted-account schedule, debt draw, DSCR, distribution waterfall, SPA cash attribution, or project return |
| `CFDSWSR-003` | Energy Transfer projects | Q2 `2026` adjusted EBITDA, DCF, growth capex, unused credit-facility availability, long-term debt, senior-note refinancing, leverage, and named capacity additions | Hold with company debt/refinancing-capacity proxy | No Nederland, Lone Star, y-grade, or export-project debt-service allocation, shipper cash, project EBITDA, or repayment waterfall |
| `CFDSWSR-004` | Matador borrowing base | `3.25B USD` borrowing base, `2.75B USD` elected commitments, `939.0M USD` borrowings, `53.8M USD` L/Cs, first-half draws/repayments, senior-note proceeds/purchases, covenant thresholds, and interest expense | Partial borrowing-base debt-movement proxy | No borrowing notices, lender schedule, reserve/collateral support, cash-interest schedule, source-specific use, or asset-area payback |
| `CFDSWSR-005` | PBF refinancing | `500.0M USD` 2034 notes, `492.1M USD` net proceeds, `801.6M USD` 2028 notes redeemed, `301.6M USD` principal reduction, about `11.846M USD` simple annual coupon relief, `90.9M USD` H1 cash interest, and company OCF/refinery-cash proxies | Partial note-refinancing debt-service proxy | No full redemption settlement, pro forma debt-service schedule, fee/tax amortization, ABL borrowing-base support, normalized refinery cash, or refinery-level return |
| `CFDSWSR-006` | Liberty Broadband holdco | `966M USD` debenture retirement funded with Margin Loan Facility proceeds and restricted cash, `1.771B USD` repayments, `1.239B USD` borrowings, `523M USD` total-debt decrease, `359M USD` Charter loan, collateral shares/value, and LTV trigger context | Partial holdco debt-repayment/collateral proxy | No restricted-cash/facility split, contractual LTV certificate, collateral schedule, Charter loan economics, merger close funds-flow, tax, or shareholder realization |
| `CFDSWSR-007` | Plains tariff route | Published Texas RRC tariff route/rate, negotiated-rate mechanic, Cactus III capacity/acquisition/control context | Hold with tariff-route/no-debt-service proxy | No shipper billing volume, realized route revenue, route EBITDA/cash, asset-level debt-service, lender allocation, or asset return |

## Decision

`debt-service-waterfall-source-route-hold-with-partials`

`CFRMSWO-004` is executed against the current local source set. It produces three partial debt/payback mechanics rows and four holds:

- PBF: partial note-refinancing debt-service proxy.
- Liberty Broadband: partial holdco repayment and collateral mechanics proxy.
- Matador: partial borrowing-base debt-movement proxy.
- Wheaton, Cheniere, Energy Transfer, and Plains: hold below asset/project/route debt-service waterfall proof.

## Safe Claim

`The debt-service waterfall source-route pass confirms that current local evidence can show several financing, refinancing, borrowing-base, and collateral mechanics, but it does not prove that named asset, project, train, route, or acquisition cash was allocated through a debt-service waterfall to specific lenders or capital providers.`

## Next Work

1. For PBF, pull redemption settlement, pro forma interest, fee amortization, tax, ABL availability, borrowing-base, and refinery-level cash schedules.
2. For Liberty, pull the Margin Loan Facility agreement, LTV certificate, restricted-cash rollforward, collateral schedule, Charter Loan Facility terms, and merger close funds-flow.
3. For Matador, pull borrowing notices, lender schedules, reserve reports, borrowing-base certificates, cash-interest schedule, and acquisition funds-flow.
4. For Wheaton and Cheniere, pull term-loan/revolver agreements, indentures, restricted-account schedules, DSCR or distribution waterfalls, and project/entity debt-service support.
5. For Energy Transfer and Plains, pull project debt allocation, shipper/customer billing, route/project EBITDA, and asset-level repayment support.
6. Move next to `CFRMSWO-005` borrower facility documents and lender schedules.
