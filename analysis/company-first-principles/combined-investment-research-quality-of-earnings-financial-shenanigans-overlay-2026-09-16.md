# Quality-of-earnings and financial-shenanigans overlay

Research date: 2026-09-17

## Purpose

This overlay adds a formal quality-of-earnings and financial-shenanigans review
to the three integrated pilots. It is a diagnostic layer, not a mechanical
fraud score. The overlay asks whether reported growth, earnings, cash flow, and
valuation inputs are supported by period-matched cash, operating assets,
disclosed obligations, and legal-entity receipts.

The structured [QoE and financial-shenanigans register](data/combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.csv)
is the field-level source of truth. It deliberately distinguishes:

- observed: the filing or ledger directly reports the relevant fact;
- partial: a bounded proxy or one side of the reconciliation exists;
- searched-negative: the named public source was searched and the requested
  field was not disclosed; and
- not-assembled: the diagnostic requires a multi-period or cross-company
  calculation that has not yet been built.

No not-assembled or partial row may be converted into a fraud conclusion. The
correct output is a falsifiable risk flag and the exact source needed to
upgrade or clear it.

## Diagnostic coverage

The overlay covers the main classic warning families:

1. cash conversion and accrual quality;
2. receivable, inventory, payable, and supplier-finance timing;
3. capitalization of costs and maintenance-versus-growth capex;
4. recurring one-time support, refunds, settlements, and restructuring;
5. stock compensation, dilution, and per-share denominator quality;
6. revenue timing, contract liabilities, gift cards, memberships, and attached
   services;
7. related-party fees, intercompany balances, and parent-receipt attribution;
8. insurance, policyholder, restricted-cash, and legal-entity perimeter risk;
9. acquisition accounting, transaction consideration, and seller/buyer cash
   mismatches; and
10. a future composite accrual screen, kept not-assembled until comparable
    multi-period inputs are available.

This is intentionally broader than a single Beneish-style score. A composite
score can compress information and create false precision when the denominator,
period, entity, or accounting taxonomy is not comparable across a streaming
company, a retailer, and an insurer/asset manager.

## Pilot conclusions

### Retail: TJX, Target, and Walmart

The existing retail work already exposes the highest-value earnings-quality
tests: operating cash flow versus property spending, inventory/payables,
supplier finance, tariff/refund support, stock compensation, gift-card and
membership timing, attached-service cost allocation, and annual versus H1
lease/tax period matching. The overlay classifies these as diagnostic or
partial rather than alleging manipulation. The decisive open test is whether
reported cash survives normalized reinvestment, working-capital reversal,
service costs, taxes, leases, and dilution.

### Wheaton-Antamina

The main quality risk is not an unsupported accusation about revenue. It is
whether aggregate Antamina production, sold ounces, stream revenue, and cash
proxies can be incorrectly presented as BHP-PMPA-specific settled cash. The
overlay therefore flags combined-versus-BHP-only quantities, revenue-recognition
objects, financing allocation, and the missing invoice/receipt trail. Until
those joins exist, the aggregate operating figures remain useful but not a
settlement-level return denominator.

### Apollo-Athene

The main risks are adjusted earnings versus collected fees, legal-entity cash
versus consolidated cash, related-party asset transfers, policyholder and
restricted cash, acquisition consideration versus executed settlement, and
Athene-to-AGM/common-owner attribution. The overlay uses the existing fee
rollforward, intercompany-note, statutory cash, ARI, parent-receipt, and claim
denominator artifacts. It does not treat a balance movement, distribution, or
contractual payment schedule as a parent receipt.

## Promotion rule

A pilot may clear a QoE warning only when the relevant fact is joined by the
same company or legal entity, reporting period, denominator, accounting
treatment, and cash or claim perimeter. A warning is promoted to a thesis
breaker when a repeated filing pattern changes the preferred denominator,
reverses cash conversion, or invalidates the stated owner-cash or valuation
assumption. A warning is not promoted merely because a ratio is unusual.

The new [retail component screen](combined-investment-research-quality-of-earnings-retail-component-screen-2026-09-16.md)
assembles six same-company annual transitions from the controlled vectors. It
calculates only the available transition components and labels the missing
receivables, gross-profit, total-assets, and cash-flow-tax/acquisition fields.
It remains below a Beneish-style composite gate and does not impute Target
receivables or convert a ratio movement into a manipulation claim.

The overlay therefore strengthens the larger chain:

    reported growth or earnings
      -> accrual and working-capital tests
      -> capitalization and recurring-support tests
      -> legal-entity and claim-perimeter tests
      -> collected cash and diluted-owner denominator
      -> valuation and filing-based thesis breaker

## Current boundary

The overlay is connected and evidence-routed. The new [retail transition panel](combined-investment-research-quality-of-earnings-retail-transition-panel-2026-09-16.md)
assembles six adjacent-period same-company transitions with raw ratio changes
and follow-up flags. It deliberately stops before a composite multi-period
accrual score. Retail attached-service allocation,
BHP-only settlement cash, and Apollo/Athene parent-to-common-owner cash remain
the decisive unresolved QoE boundaries. The current output is therefore a
qualified diagnostic panel and risk register, not a fraud finding and not a
claim that any company has misstated its accounts.

## QoE-to-thesis-breaker handoff

The diagnostic layer now has an explicit handoff to the investment claims it
can weaken. This is a routing control, not an activation of any breaker:

| QoE diagnostic family | Thesis-breaker route | What would activate the breaker | Current state |
| --- | --- | --- | --- |
| Combined-versus-BHP-only ounces, settlement object, and stream cash conversion | `TB-WPM-01`, `TB-WPM-02`, `TB-WPM-03` | A BHP-only delivery shortfall, failure to separate the BHP PMPA from Glencore, or an after-tax financed return below the required return | First delivery and combined economics are visible; BHP-only quantity, receipt, tax, debt service, and return remain open |
| Retail working capital, supplier finance, temporary support, and attached-service conversion | `TB-RET-01`, `TB-RET-02` | Demand weakens despite the value thesis, or margin/attached-service growth fails after inventory, vendor terms, leases, taxes, and collection are normalized | Diagnostic transition flags exist; the comparable normalized cash bridge is incomplete |
| Retail capitalization, maintenance-versus-growth spending, dilution, and claim burden | `TB-RET-02`, `TB-RET-03` | Reinvestment or senior claims consume apparent cash, or incremental capital fails the stated productivity/return test | Category and burden screens exist; the maintenance split and incremental return remain open |
| Apollo fee accrual/collection, legal-entity cash, policyholder claims, and parent attribution | `TB-APO-01`, `TB-APO-02` | Fee cash is not collected, regulated cash cannot upstream, or credit/spread losses overwhelm the related-party income | Fee roll-forward, statutory cash, and claim boundaries exist; recipient cash and common-owner residual remain open |
| ARI transaction consideration, borrower cash, and acquisition accounting | `TB-APO-03` | The named asset transfer lacks borrower repayment, produces weak credit performance, or the settlement/wire perimeter fails | Seller/buyer balance and transaction terms are visible; executed settlement, borrower receipt, and loan-level return remain open |

The handoff rule is deliberately asymmetric: a diagnostic can create a
follow-up or thesis-breaker test, but a favorable ratio cannot clear the
breaker without the same-entity, same-period, cash-or-claim reconciliation.
All nine thesis-breaker rows therefore remain `active-qualified`, and the
cross-pilot Beneish-style composite remains `not-assembled`.

## Cross-pilot composite gate audit — 2026-09-17

The composite gate was re-audited against the current artifacts. The minimum
comparable field set is now explicit:

| Required field | Retail cohort | Wheaton–Antamina | Apollo–Athene | Composite decision |
| --- | --- | --- | --- | --- |
| Same legal entity and period | Partial across fiscal calendars | Partial: combined stream versus BHP tranche | Partial: statutory, Athene, and AGM perimeters | Hold |
| Revenue/earnings denominator | Partial: Target and Walmart taxonomy gaps remain | Partial: stream proxy is asset/company-specific | Partial: adjusted segment and statutory income differ | Hold |
| Total assets and accrual inputs | Missing comparable total-assets/gross-profit joins | Not analogous to retail accrual taxonomy | Schedule D and statutory fields are not comparable | Hold |
| Operating cash and claims | Partial owner-cash bridge | Corporate/stream cash allocation missing | Policyholder, regulated, and parent claims missing | Hold |
| Cash-flow and accounting-policy reconciliation | Partial | Partial settlement/accounting boundary | Partial legal-entity/remittance boundary | Hold |

The result is not merely “no score yet”: the current fields fail the
comparability gate for reasons that would make a pooled composite misleading.
The system may continue to use Sloan-, Schilit-, and Beneish-style diagnostics
as named, denominator-specific prompts, but it must not publish a cross-pilot
score until the missing fields and perimeters are joined. This preserves the
financial-shenanigans approach while preventing a false precision upgrade.

## Primary routes

- [Retail owner-cash input schema](capital-flow-retail-owner-cash-input-schema-2026-09-16.md)
- [Retail capex classification boundary](combined-investment-research-pilot-02-retail-capex-classification.md)
- [Retail annual lease-and-tax cash control](combined-investment-research-pilot-02-retail-annual-lease-tax-cash-control-2026-09-16.md)
- [Wheaton-Antamina production/receipt bridge](capital-flow-wheaton-antamina-production-receipt-bridge-pass-1.md)
- [Apollo-Athene related-party return bridge](combined-investment-research-pilot-03-apollo-related-party-return-bridge.md)
- [Expansion-lane QoE overlay](combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md)
- [Completion audit](combined-investment-research-completion-audit.md)
