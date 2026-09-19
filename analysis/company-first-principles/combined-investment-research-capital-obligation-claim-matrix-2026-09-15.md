# Combined investment research capital-obligation and claim matrix

Research date: `2026-09-15`

This matrix controls the reinvestment, financing, liability, acquisition, and
dilution layer across the three pilots. It is an attribution map, not a sum of
all balances: several rows are alternative views of the same economic burden.

## Source-backed burden map

| Pilot | Obligation or claim | Period / balance | What is proven | Non-additivity or allocation rule | Remaining upgrade |
| --- | --- | ---: | --- | --- | --- |
| Wheaton–Antamina | Bank debt drawn | H1 2026: `$2.700B` | Corporate financing inflow is reported | Do not call the entire draw PMPA funding without a funds-flow join | Lender-level PMPA allocation |
| Wheaton–Antamina | Bank debt repaid | H1 2026: `$728M` | Corporate repayment is reported | Do not subtract again from an OCF proxy that already reflects reported financing separation | Principal waterfall and asset allocation |
| Wheaton–Antamina | Interest paid and debt-issue costs | H1 2026: `$29.886M` and `$5.118M` | Actual financing cash outflows are reported | Do not replace actual cash with annualized rate sensitivity or allocate it fully to Antamina | Antamina-specific interest, tax, and debt service |
| Retail cohort | Operating lease cash | Company periods | Lease cash is included in operating cash flow | Do not subtract lease cash again from cash-after-property; use lease liabilities in invested-capital/return analysis | Lease-adjusted return and renewal burden |
| Retail cohort | Maintenance versus growth property spending | H1 periods | Total property spending and category directions are reported | Maintenance-share sensitivities are not company estimates and must not be combined with full property spending twice | Quantified maintenance schedule |
| Retail cohort | Supplier finance / payable support | H1 periods | Target `$3.2B` and Walmart `$6.4B` obligations, plus payable movements, are visible | Payable support and supplier-finance balances are not automatically additive cash benefits | Settlement and recurring-normalization bridge |
| Apollo–Athene | Preferred conversion claim | Q2 2026: `14.588M` underlying shares | Apollo adjusted denominator includes the claim | Do not add preferred underlying shares to cash claims without preferred priority and conversion economics | Preferred cash priority and conversion timing |
| Apollo–Athene | RSU claims | Q2 2026: `17.073M` vested and `15.922M` unvested dividend-equivalent shares | Adjusted share denominator includes both classes | Do not treat adjusted share count as cash expense and also subtract full SBC without settlement analysis | Vesting, settlement, and future dilution |
| Apollo–Athene | Equity-based compensation | H1 2026: `$478M` | Reported compensation claim is visible | Do not subtract SBC as cash and again treat all adjusted-share claims as separate cash outflows | Cash settlement and per-share economics |
| Apollo–Athene | Common dividends and repurchases | H1 2026: `$654M` and `$729M` | Parent capital-return uses are reported | Uses of capital are not evidence of upstream receipt or distributable residual | Parent cash source and residual waterfall |
| Apollo–Athene | Preferred dividends | H1 2026: `$49M` parent-level; Athene also reports preferred claims | Senior/common-claim distinction is visible | Do not treat common dividends as residual cash before preferred, NCI, regulated, and VIE claims | Full parent-to-common waterfall |

## Promotion consequence

The matrix allows the valuation workbenches to show debt, capex, leases,
supplier finance, dilution, and capital returns without double counting. It does
not close the key attribution gaps: PMPA funds flow, retailer maintenance
capital, Athene-to-AGM receipt, regulated cash availability, borrower cash, and
common-owner residual.

Status: `capital-obligation and claim map source-backed; full owner-cash
allocation unresolved`.

Structured matrix: [capital-obligation CSV](data/combined-investment-research-capital-obligation-claim-matrix-2026-09-15.csv).
Related control: [owner-cash promotion matrix](combined-investment-research-owner-cash-promotion-matrix-2026-09-15.md).
