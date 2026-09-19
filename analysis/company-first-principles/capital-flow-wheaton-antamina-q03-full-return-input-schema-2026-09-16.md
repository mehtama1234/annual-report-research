# Wheaton–Antamina Q-03 full-return input schema

Research date: `2026-09-17`

This schema converts the Q-03 open return question into model-ready fields. It
does not create a return estimate. It specifies the exact observations needed
to move from the current company-level financing and stream-cash proxies to an
Antamina-specific after-tax financed IRR/NPV.

The structured companion is
[the Q-03 input CSV](data/capital-flow-wheaton-antamina-q03-full-return-input-schema-2026-09-16.csv).

## Promotion rule

No field may be promoted into the asset-level return model merely because a
company-level proxy exists. Each row requires a source, legal entity, period,
unit, denominator, and reconciliation status. The return model is promotion-
ready only when delivery, receipt, tax, financing, repayment, and reserve-life
fields join to the same BHP PMPA perimeter.

| Input family | Required model field | Current state | Model use | Exact upgrade document |
| --- | --- | --- | --- | --- |
| Contract | BHP PMPA entitlement and step-down | Observed: 33.75% until 100M ounces, then 22.5% | Defines payable stream | Executed PMPA and amendment schedule |
| Contract | Payable factor | Observed: 90.0% | Converts recovered to payable ounces | PMPA settlement schedule |
| Delivery | BHP-only recovered ounces by period | Missing | Delivery volume | BHP-PMPA delivery ledger or Wheaton mine-by-mine schedule |
| Delivery | Payability, assays, smelter weights, PBND | Partial: formula/context only | Delivered payable ounces | Settlement statement, assay/weight certificate, PBND rollforward |
| Price | Quotation-period realized price | Missing | Gross stream receipt | Wheaton invoice and quotation-period settlement support |
| Cash receipt | Invoice, settlement date, amount, currency, receivable/cash account | Missing | Receipt timing and cash flow | Wheaton settlement ledger, custodian or bank confirmation |
| Cash cost | 20.0% ongoing payment formula and delivery-level cash paid | Formula observed; cash paid missing | Net stream cash cost | Delivery payment schedule and remittance support |
| Funding | Cash, term-loan, and revolver dollars allocated to PMPA | Partial funding control: planned `$1.9B` cash, `$1.5B` term loan, and `$0.9B` revolver reconcile to the `$4.3B` payment; actual H1 corporate flow includes `$2.700B` drawn and `$728M` repaid, but seller-account and asset allocation remain missing | Initial financing sources | Closing funds-flow statement and borrowing notices |
| Financing | Term-loan rate, fees, dates, and interest paid | Partial: contractual basis and H1 `$29.886M` interest paid are observed; facility-specific and PMPA allocation remain missing | Debt-service cash flow | Facility rate notices, lender schedule, interest statement |
| Financing | Principal repayment, maturity bullet, and waterfall | Principal scale observed; allocation missing | Financing outflows and terminal claim | Lender repayment schedule and waterfall |
| Tax | Antamina-specific current/deferred tax allocation | Partial: company effective-tax-rate context supports a labeled sensitivity, but asset-level allocation is missing | After-tax cash flow | Tax allocation schedule or explicit asset-level disclosure |
| Reinvestment | Reserve-backed production and delivery curve | Partial: proxy and ceiling only | Forecast cash-flow duration | BHP reserve/production schedule or independent reserve report |
| Return | Initial outflow, periodic net cash, terminal value, discount rate | Partial: illustrative IRR/NPV workbench exists, but its delivery, tax, and financing inputs are not source-linked to the asset | IRR/NPV/payback | Integrated PMPA return model with source-linked inputs |

## Current boundary

The local evidence supports a strong named source/use/cash-return proxy and a
labeled company-tax sensitivity: the
`$4.300B` PMPA payment, company-level funding context, H1 2026 Antamina
revenue/cost/profit/OCF, and bounded financing and reserve sensitivities. It
 does not support filling the missing rows with consolidated company values or
calling the illustrative workbench an asset-level return.
Until the BHP-only delivery and receipt rows join the tax and financing rows,
the correct status is `full-return-inputs-incomplete`.

## Next execution order

1. Acquire the executed single-draw Drawdown Notice, designated-payee/payment instruction, agent funding record, and seller-account confirmation.
2. Acquire the BHP-only delivery and settlement ledger, including legal counterparty and period-level allocation.
3. Join quotation-period price, invoice, receivable, and cash receipt fields through a custodian or bank confirmation.
4. Allocate term-loan/revolver interest and principal by documented source, then obtain Antamina tax treatment and reserve-backed delivery schedule.
5. Run the source-linked IRR/NPV model and compare it with the required return.
