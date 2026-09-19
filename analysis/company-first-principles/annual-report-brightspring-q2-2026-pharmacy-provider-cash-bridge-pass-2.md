# BrightSpring Q2 2026 pharmacy-provider cash bridge pass 2

## Purpose

This pass moves BrightSpring from a broad pharmacy/provider route to a
company-specific valuation and liquidity object. It separates pharmacy product
volume from provider-service delivery, and continuing operations from the
Community Living divestiture.

The correct object is `continuing-operations pharmacy/provider cash after drug
cost, service labor, working capital, acquisitions, debt, SBC replacement, and
common claims`. Adjusted EBITDA, divestiture proceeds, and consolidated OCF are
diagnostic inputs rather than normalized owner cash.

## Filing and period

- Company: BrightSpring Health Services, Inc. (`BTSG`)
- Filing: Q2 2026 Form 10-Q, period ended June 30, 2026
- Primary source: [BrightSpring Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1865782/000119312526327014/btsg-20260630.htm)
- Results exhibit: [BrightSpring Q2 2026 results](https://www.sec.gov/Archives/edgar/data/1865782/000119312526326654/btsg-ex99_1.htm)
- Companion data: `data/annual-report-brightspring-q2-2026-pharmacy-provider-cash-bridge-pass-2.csv`

## Segment and payer bridge

| Object | H1 2026 evidence | Interpretation and boundary |
| --- | ---: | --- |
| Total revenue | `$7.4869B` | Scale of continuing operations; not owner cash. |
| Pharmacy Solutions revenue | `$6.5785B` | Product-heavy pharmacy route. |
| Provider Services revenue | `$908.3M` | Service/labor-backed provider route. |
| Pharmacy cost of drugs | `$5.5897B` | Direct product burden; pharmacy revenue cannot be valued at service margins. |
| Pharmacy other direct costs | `$389.9M` | Additional pharmacy burden before segment SG&A. |
| Provider cost of services | `$532.3M` | Direct provider-service burden. |
| Segment EBITDA | `$490.0M` | `Pharmacy $349.1M` plus `Provider $140.8M`; not common cash. |
| Adjusted EBITDA | `$395.3M` | Non-GAAP diagnostic; adjustments include SBC, transactions, restructuring, and divestiture-related items. |
| Payor mix | Top 10 states `52%` of H1 revenue; federal/state/local, commercial, private, and other payors | Geographic and payer concentration matter; rates and budgets can change. |
| Accounts receivable | `$1.139B` at June 30 vs `$989.7M` at December 31 | Collection funding burden; no service-line cash collection schedule is disclosed here. |
| Inventory | `$575.0M` at June 30 vs `$815.2M` at December 31 | Working-capital release may support cash; it is not recurring margin. |

## Cash and capital structure bridge

| Cash object | H1 2026 evidence | Boundary |
| --- | ---: | --- |
| Operating cash flow | `$166.859M` | Includes continuing/discontinued cash-flow perimeter as reported and does not equal common residual. |
| PP&E cash use | `$50.576M` | Required and growth capital are not separately allocated. |
| Acquisitions | `$42.203M` | Acquisition cash and acquired return remain separate. |
| Community Living sale proceeds | `$810.908M` | One-time divestiture funding, not recurring care-delivery cash. |
| Long-term debt repayment | `$320.491M` | Financing allocation; relevant to residual liquidity and leverage. |
| Debt issuance costs | `$3.378M` | Financing burden. |
| Common-share repurchases | `$120.000M` | Residual claim/funding use, not proof of surplus cash. |
| Interest expense, net | `$75.5M` | Senior funding burden before common residual. |
| Share-based compensation | `$23.169M` reported H1 cash-flow adjustment | Non-cash in the period but a potential replacement/dilution burden. |
| Ending cash | `$550.381M` | Company-level cash; total liquidity including revolver/LC availability was `$1.026B`. |
| First Lien Tranche B-6 | `$2.2149B` at `5.62%`, maturing February 21, 2031 | Refinancing after using `$300M` of divestiture proceeds to repay B-5; not an operating asset return. |

The mechanical pre-owner screen is:

`$166.859M OCF - $50.576M PP&E - $42.203M acquisitions = $74.080M`

This is only a diagnostic. It excludes no debt principal, repurchases, or
other senior/common claims, and it must not add the `$810.908M` divestiture
proceeds as if they were recurring operating cash. It also should not subtract
SBC a second time from OCF without defining whether the test is cash-paid
replacement, dilution, or both.

## Correct operating path

`complex patient need -> pharmacy product or provider service -> payer,
authorization, fulfillment, clinical labor, and collection -> drug/service
cost -> working capital -> required PP&E and acquisitions -> interest/debt,
SBC replacement, repurchases, and other claims -> common residual`

BrightSpring says the Community Living transaction closed March 30, 2026 and
that current results are presented as continuing operations. The cash-flow
statement nevertheless includes the divestiture proceeds, so the model must
keep the operating perimeter and the financing/liquidity event separate.

## QoE and thesis-breaker controls

1. Keep Pharmacy Solutions and Provider Services separate; pharmacy revenue is
   largely product revenue with a drug-cost denominator, while provider revenue
   carries service labor and direct-service costs.
2. Reconcile AR, inventory, rebate receivables, and payer mix to collected cash;
   inventory release and receivable growth can move OCF without changing
   normalized service economics.
3. Do not capitalize the `$810.908M` Community Living sale proceeds or the
   related gain into recurring care-delivery cash.
4. Treat the `$395.3M` adjusted EBITDA bridge as a prompt to reconcile SBC,
   acquisition/integration, restructuring, and divestiture items—not as a
   substitute for net income or OCF.
5. Keep the `$320.491M` debt repayment, `$75.5M` interest burden, `$120M`
   repurchase, and `$23.169M` SBC visible in the residual claim map.
6. Test whether pharmacy gross profit and provider-service margin survive payer
   rate changes, labor costs, specialty-drug mix, reimbursement delays, and
   refinancing before assigning a continuing-operations terminal value.

## Promotion status

`brightspring-pharmacy-provider-cash-qualified; divestiture-and-common-residual-open`

BrightSpring is qualified for a current-period pharmacy/provider and liquidity
diagnostic. It remains unranked. Promotion requires service-line collection,
drug-margin, labor, acquisition-cohort, debt-service, SBC replacement, and
diluted common-owner evidence after excluding the divestiture event.

