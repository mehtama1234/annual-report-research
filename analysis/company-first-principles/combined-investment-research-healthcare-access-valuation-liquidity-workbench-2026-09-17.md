# Healthcare access and care-delivery valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench translates the Q2 2026 healthcare-access refresh into
company-specific valuation objects, reinvestment burdens, liquidity stresses,
and thesis breakers. It does not create a healthcare ranking. Payers,
treatment sites, alternate-site infusion, home care, and pharmacy/provider
orchestration have different cash denominators.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment and denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| UnitedHealth | Normalized premium/service margin after medical-cost trend, reserve development, claims funding, Optum mix, capital, tax, and dilution | Claims paid, IBNR, days claims payable, provider/pharmacy cost, risk adjustment, care investment, debt, and legal-entity access | Medical-cost acceleration, reserve deterioration, provider-rate pressure, cyber/trust shock, capital requirements, or restricted subsidiary cash | Favorable development repeats as reported margin while claims payable, IBNR, MCR, or cash conversion worsen |
| Cigna | Cigna Healthcare and Evernorth segment cash after medical cost, pharmacy economics, risk adjustment, working capital, capital, and dilution | Net medical costs payable, pharmacy inventory/receivables, rebates and client settlement, debt, tax, and legal-entity allocation | MCR deterioration, PBM spread/rebate pressure, client attrition, claims funding, refinancing, or regulatory remediation | Adjusted income grows while net medical costs payable rises faster than enrollment/revenue or cash does not follow |
| DaVita | Treatment-level cash after reimbursement per treatment, labor, supplies, center cost, maintenance capital, NCI, debt, and tax | Treatment volume, payer mix, staffing, center maintenance/development, NCI distributions, leases, debt, and risk-contract claims | Payer-rate compression, labor shortage, center disruption, NCI/funding demand, refinancing, or value-based loss | Treatments and disclosed FCF rise while reimbursement, labor, maintenance capital, NCI, or debt-service coverage deteriorate |
| Option Care | Therapy/cohort contribution after drug cost, nursing, authorization, collection, working capital, capex, and diluted repurchases | Receivables, inventory, drug procurement, nurse capacity, authorization, PP&E, buybacks, debt, and tax | Payer denial or delay, drug-cost inflation, nurse scarcity, inventory funding, revolver use, or concentration | Revenue and repurchases rise while receivables consume cash, therapy margin falls, or nurse capacity limits delivery |
| Addus | Branch and service-line cash after caregiver wages, state/payer rate, utilization, compliance, acquisition, and technology burden | Billable hours, wage pass-through, branch density, receivables, acquisition capital, compliance, capex, and debt | Wage/rate mismatch, Medicaid or state budget pressure, caregiver shortage, receivable delay, or acquisition leverage | Service revenue grows while gross margin, payer rates, staffing, receivables, or branch returns deteriorate |
| BrightSpring | Continuing-operations pharmacy/provider cash after labor, pharmacy gross profit, acquisitions, interest, SBC, divestiture, and NCI | PP&E, acquisitions, interest, SBC replacement, labor, pharmacy working capital, debt, NCI, and sponsor/legal-entity claims | Reimbursement pressure, labor cost, acquisition funding, refinancing, pharmacy margin compression, or sponsor restrictions | Adjusted EBITDA grows while adjustments, acquisitions, interest, SBC, or divestiture perimeter consume common cash |
| Enhabit | Final public Home Health/Hospice cash baseline only; post-close value requires private sponsor-period evidence | Payer mix, clinical labor, settlement effects, capex, debt, leases, sponsor claims, and legal-entity access | Reimbursement/quality changes, labor shortages, cap-rate pressure, refinancing, or private reporting opacity | Post-close claims cannot be reconciled to public filings; the public-company series must not be extended by assumption |

## Current evidence anchors

- UnitedHealth Q2 revenue was `$112.0B`, operating cash was `$11.1B`, MCR was
  `86.7%`, favorable prior-period medical reserve development was `$860M`, and
  claims payable was `47.0` days with `$26.5B` of IBNR medical costs payable.
  Its Q2 Form 10-Q also provides a six-month medical-cost-payable roll-forward:
  `$148.847B` reported medical costs, `$149.320B` of medical payments, and
  `$38.930B` ending medical costs payable, including `$1.250B` favorable
  prior-year development and a `$66M` held-for-sale perimeter adjustment. This
  is a payer-liability/payment diagnostic, not a complete legal-entity claims
  collection or common-owner cash bridge.
- Cigna's Q2 Cigna Healthcare MCR was `84.5%`; net medical costs payable rose
  from `$4.49B` a year earlier and `$4.78B` at March 31 to `$5.09B` at June 30,
  while Q2 revenue was `$71.668B` and adjusted income from operations was
  `$2.054B`.
  Its Q2 Form 10-Q adds a six-month Cigna Healthcare unpaid-claims bridge:
  `$15.825B` incurred, `$14.834B` paid, `$143M` ending recoverables, and
  `$5.228B` ending unpaid claims, including `$268M` favorable prior-year
  development. The broader filing also reports `$1.5B` of H1 receivables sold,
  `$0.9B` uncollected, and `$0.3B` collected but not remitted; these are
  financing and collection controls, not automatic owner cash.
- DaVita reported Q2 revenue of `$3.554B`, operating cash of `$490M`, disclosed
  FCF of `$256M`, and `7.2266M` U.S. dialysis treatments. The FCF definition
  carries NCI and capital-allocation boundaries that prevent automatic promotion
  to common-owner cash.
  Its Q2 Form 10-Q adds H1 U.S. treatments of `14.256M`, average patient-service
  revenue of `$416.71` per treatment, `$811M` OCF, `$197M` maintenance capital,
  `$75M` development capital, `$150M` NCI distributions, and `$396M` disclosed
  FCF. It also shows `$1.561B` of NCI subject to put provisions and `$500M` of
  incremental Term Loan B-2 funding; the care-site-to-common-owner waterfall
  remains open.
- Option Care reported Q2 operating cash of `$184M`; H1 operating cash was
  `$171.485M`, receivables used `$37.941M`, inventory supplied `$71.544M`, and
  repurchases were `$170.545M`. The repurchase amount therefore cannot be read
  as surplus cash without a therapy-margin and working-capital bridge.
  Its Q2 Form 10-Q adds H1 commercial payer revenue of `$2.381B`, government
  payer revenue of `$364M`, patient revenue of `$47M`, H1 gross profit of
  `$529M`, and Q2 gross margin of `18.5%`. It also identifies an estimated
  `$55M` 2026 CID therapy-mix headwind, `$154.9M` earned but unbilled
  receivables, a `$20.123M` PP&E cash use, `$30.377M` interest paid, and
  `$846M` net revolver availability. Therapy-level collection and payer margin
  remain unproven.
- Addus reported Q2 net service revenue of `$377.417M`, operating cash of
  `$40.0M`, H1 revenue of `$741.028M`, and H1 gross margin of `32.0%`; personal
  care represented `$577.089M` of H1 revenue. The Q2 filing adds personal-care
  gross margin of `28.3%`, H1 state/local/other-government and MCO payer mix of
  `50.0%` and `47.3%`, Illinois concentration of `32.1%` of total revenue,
  `$92.376M` H1 OCF, `$145.123M` ending AR, `$12.182M` acquisition cash, and
  `$3.050M` PP&E/technology cash. Labor and payer-rate evidence are the central
  return variables; the filing says cash was also affected by AR and payroll/AP
  timing.
- BrightSpring reported H1 revenue of `$7.4869B`, including `$6.5785B` Pharmacy
  Solutions and `$908.3M` Provider Services; segment EBITDA was `$490.0M`.
  H1 operating cash was `$166.859M`, PP&E `$50.576M`, acquisitions `$42.203M`,
  net interest expense `$75.5M`, SBC `$23.169M`, AR `$1.139B`, and inventory
  `$575.0M`. The Community Living divestiture produced `$810.908M` of cash and
  requires a continuing-operations perimeter test; it is not recurring care
  cash.
- Enhabit's final public Q1 baseline was `$35.2M` OCF, `$(2.6M)` investing cash,
  `$(26.6M)` financing cash, and a `$17.7M` non-recurring settlement gain. The
  May 15 private transition blocks an assumed public Q2 continuation.

## QoE and financial-shenanigans prompts

The relevant prompts are falsifiable reconciliation requests, not fraud
findings:

1. Exclude UnitedHealth's favorable reserve development from recurring margin
   until claims paid, IBNR, MCR, and the reserve roll-forward support it.
   The new roll-forward supports the payment and liability arithmetic, but the
   `$1.250B` favorable development and `$66M` held-for-sale adjustment remain
   separately bounded.
2. Do not interpret Cigna's adjusted income without matching medical-cost
   payable growth to enrollment, benefit-cost trend, risk adjustment, and cash.
   The new claims roll-forward supplies incurred-versus-paid evidence, but the
   `$268M` favorable development, pharmacy/service payable timing, and
   receivable-sale perimeter remain separate from normalized margin.
3. Do not treat DaVita's disclosed FCF as common-owner cash until NCI,
   maintenance/development capital, debt, and risk-contract claims are joined.
   The Q2 filing makes the FCF arithmetic reproducible, but the `$1.561B` NCI
   put perimeter and debt funding remain senior-claim controls rather than a
   completed common-owner residual.
4. Treat Option Care's buybacks as a residual claim, not evidence of durable
   surplus, while receivables and inventory are consuming or supplying cash.
   The Q2 filing also shows payer-category revenue, gross-profit pressure,
   unbilled receivables, and an estimated CID mix headwind; these inputs do not
   turn the `$170.545M` repurchase into operating surplus.
5. Treat Addus's `$92.376M` H1 OCF as a timing-sensitive diagnostic until the
   AR, accrued-payroll, and accrued-expense movements unwind; match the
   `$30.80` Illinois hourly reimbursement reference to caregiver wages and all
   branch costs rather than calling the spread branch profit.
6. Treat BrightSpring's adjustment and acquisition burden as a recurring
   capital-allocation question, not merely an EBITDA add-back. Keep the
   `$810.908M` Community Living proceeds, `$320.491M` debt repayment, `$120M`
   repurchase, `$75.5M` interest, and `$23.169M` SBC replacement/dilution
   questions outside normalized operating cash.

## Promotion boundary

`healthcare-access-qualified-expectation-screen; liquidity-open; no-ranking`

Promotion requires a same-entity, same-period bridge from payer or patient
activity to collected cash, required service/replacement capital, senior claims,
legal-entity availability, and diluted common residual. Revenue, MCR, treatment
volume, adjusted EBITDA, and management-defined FCF are evidence inputs—not the
final owner-cash numerator.

## Sources

- [Healthcare access Q2 2026 cash-quality refresh](combined-investment-research-healthcare-access-care-delivery-q2-2026-cash-quality-refresh-2026-09-17.md)
- [UnitedHealth Q2 2026 medical-cost-payable roll-forward pass 2](annual-report-unitedhealth-q2-2026-medical-cost-payable-rollforward-pass-2.md)
- [UnitedHealth Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/731766/000073176626000197/unh-20260630.htm)
- [Cigna Q2 2026 unpaid-claims and cash bridge pass 2](annual-report-cigna-q2-2026-unpaid-claims-cash-bridge-pass-2.md)
- [Cigna Q2 2026 earnings release](https://www.sec.gov/Archives/edgar/data/1739940/000114036126030135/ef20078875_ex99-1.htm)
- [DaVita Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/927066/000092706626000108/dva-20260630.htm)
- [DaVita Q2 2026 treatment-to-cash bridge pass 2](annual-report-davita-q2-2026-treatment-to-cash-bridge-pass-2.md)
- [Option Care Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1014739/000101473926000023/bios-20260630.htm)
- [Option Care Q2 2026 therapy-collection and margin bridge pass 2](annual-report-option-care-q2-2026-therapy-collection-margin-bridge-pass-2.md)
- [Addus Q2 2026 payer, wage, branch, and cash bridge pass 2](annual-report-addus-q2-2026-payer-wage-branch-cash-bridge-pass-2.md)
- [BrightSpring Q2 2026 pharmacy/provider cash bridge pass 2](annual-report-brightspring-q2-2026-pharmacy-provider-cash-bridge-pass-2.md)
- [Addus Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1468328/000143774926025678/adus20260630_10q.htm)
- [BrightSpring Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1865782/000119312526327014/btsg-20260630.htm)
- [Enhabit Q1 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1803737/000180373726000025/ehab-20260331.htm)
