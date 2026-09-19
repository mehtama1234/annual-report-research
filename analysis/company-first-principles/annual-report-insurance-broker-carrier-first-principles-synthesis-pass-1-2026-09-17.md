# Insurance brokers versus carriers: first-principles synthesis — pass 1

Research date: `2026-09-17`

This chapter extends the research system into insurance distribution and risk
carriage. It compares Marsh McLennan and Arthur J. Gallagher as brokers with
Chubb as a carrier. It is a qualified diagnostic, not a ranking: brokers and
carriers have different revenue recognition, balance-sheet claims, capital
requirements, and owner-cash denominators.

## Force and control point

Rising risk complexity, regulation, catastrophe exposure, cyber risk, and
corporate demand for risk transfer increase the value of trusted placement,
claims expertise, data, and balance-sheet capacity. A broker controls client
access, placement workflow, advisory knowledge, and carrier negotiation. A
carrier controls underwriting capacity, pricing, claims administration, and
investment of policyholder funds.

The broker's main burden is producer talent, retention, integration, client
concentration, and acquisition financing. The carrier's burden is underwriting
losses, reserve development, catastrophe volatility, reinsurance, regulatory
capital, policyholder liabilities, and asset-liability management.

## End-to-end economic chain

```text
risk complexity and demand for protection
  -> broker relationship / carrier underwriting capacity
  -> commissions, fees, premiums, investment income, and claims service
  -> producer compensation, acquisition/integration, claims, reserves,
     reinsurance, policyholder liabilities, and capital requirements
  -> operating/statutory cash after capex and taxes
  -> debt, preferred/NCI, dividends, repurchases, SBC, and dilution
  -> broker common-owner residual or carrier common-owner residual
```

Broker revenue is not equivalent to carrier premium economics, and carrier
operating cash is not automatically distributable cash. The legal entity,
regulatory perimeter, source of funds, and claim seniority must be explicit.

## FY2025 filing-backed comparison

| Company / model | Revenue or activity surface | OCF | Visible reinvestment / claims | Mechanical observation |
| --- | ---: | ---: | --- | --- |
| Marsh McLennan / broker | — | `$5.292B` | `$291M` PP&E; `$652M` acquisitions; `$2.012B` repurchases; `$1.699B` dividends; `$394M` SBC; `$19.587B` debt | `$5.001B` OCF less PP&E before acquisitions, financing, SBC, and owner claims |
| Arthur J. Gallagher / broker | `$13.942B` revenue | `$1.930B` | `$9.904B` goodwill acquired; `$667M` dividends; `$49M` SBC; `$12.873B` debt | Acquisition intensity dominates the return hurdle; goodwill is not cash paid by itself |
| Chubb / carrier | — | `$12.816B` | `$289M` acquisitions; `$3.694B` repurchases; `$1.505B` dividends; `$15.728B` debt; `$198M` restricted cash | OCF cannot be promoted without underwriting, reserve, reinsurance, statutory capital, and policyholder claims |

These values are sourced from the FY2025 structured filing facts and are not a
cross-model cash league table. Gallagher's goodwill-acquired fact is an
accounting/acquisition indicator, not a substitute for cash paid or acquired
cohort return.

## Quality of earnings and financial-shenanigans controls

1. For brokers, separate organic commission/fee growth from acquisitions,
   contingent consideration, producer compensation, and client-fund flows.
2. Reconcile receivables, premiums/commissions payable, fiduciary cash, and
   client funds; fiduciary or restricted balances are not common-owner cash.
3. For carriers, reconcile premium growth to rate, exposure, mix, retention,
   loss ratio, reserve development, reinsurance, and actual claims payments.
4. Test investment income, realized gains, fair-value changes, and reserve
   releases; none alone proves recurring distributable earnings.
5. Keep acquisition cash, goodwill/intangible amortization, integration,
   restructuring, producer retention, and debt funding in the return hurdle.
6. Separate statutory surplus and restricted cash from holding-company
   liquidity, dividends, intercompany transfers, and common-owner residual.
7. Reconcile repurchases and dividends to post-reinvestment cash, capital
   requirements, SBC, preferred/NCI claims, and diluted shares.

## Valuation and liquidity handoff

The Damodaran-style broker valuation input is organic commission/fee growth,
retention, margin, producer reinvestment, acquisition returns, debt, and
diluted owner cash. For a carrier, the input is underwriting profit plus
investment income after expected losses, reserve development, reinsurance,
capital requirements, taxes, and liability funding costs.

The Lyn Alden-style stress path is catastrophe and claims inflation, rate and
credit-cycle changes, reinsurance pricing, client affordability, producer
retention, acquisition financing, and regulatory capital pressure. The thesis
breaker is reported growth or adjusted earnings rising while organic cash
conversion, reserve quality, acquired-cohort returns, capital availability, or
diluted owner cash deteriorates.

Current status:

`qualified-broker-versus-carrier-control-point; FY2025-diagnostic; legal-and-owner-cash-perimeters-open; no-ranking`

## Sources and verification

- [Insurance broker/carrier filing denominator verifier](../../scripts/verify-insurance-broker-carrier-filing-denominators.py)
- [Insurance broker rollup filing denominator verifier](../../scripts/verify-insurance-broker-rollup-filing-denominators.py)
- [Marsh McLennan FY2025 10-K](../../raw/sec/financial/insurance-brokers/marsh-mclennan-companies-inc/2025-10k.html)
- [Arthur J. Gallagher FY2025 10-K](../../raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2025-10k.html)
- [Chubb FY2025 filing packet](../../raw/sec/financial/property-casualty-insurance/chubb-limited/2025-10k.html)

