# Semiconductor process-control valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves KLA from a five-year cash-cycle and installed-service
boundary into an explicit valuation, reinvestment, liquidity, and thesis-
breaker object. It keeps process-control systems, installed service, R&D,
factoring, customer funding, and capital returns separate from peak-year FCF.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| KLA process control | Cycle-normalized systems plus service cash after acceptance, collections, factoring normalization, R&D/support, inventory, commitments, debt, SBC, and dilution | R&D `$1.532B`, field service/parts, inventory, PP&E, purchase commitments `$5.97B`, technical labor, and installed-base support | Semiconductor capex contraction, customer concentration, export controls, inventory build, factoring withdrawal, floating-rate debt, and FX | Revenue/service growth continues while factoring, receivables/inventory, deferred-revenue obligations, commitments, or diluted per-share cash deteriorate |

## Current evidence anchors

- FY2026 revenue was `$13.579B`, service revenue `$3.126B`, OCF `$4.143B`,
  PP&E `$375.9M`, R&D `$1.532B`, and reported FCF `$3.767B`.
- Receivables were `$2.889B` versus `$2.264B`; inventory was `$3.649B` versus
  `$3.212B`; receivables factoring was `$515.5M` versus `$230.6M`.
- Current deferred system revenue was `$932.9M`; current deferred service
  revenue was `$604.1M`; purchase commitments were approximately `$5.97B`.
- Dividends were `$1.058B` and repurchases `$2.290B`; debt was `$5.887B`,
  cash/securities approximately `$4.902B`, and revolver capacity `$1.5B`.

## QoE and financial-shenanigans prompts

1. Reconcile OCF and customer funding to the `$515.5M` of receivables
   factoring; model a no-factoring and unwind case.
2. Separate shipment, customer acceptance, deferred system/service revenue,
   receivable collection, and actual margin realization.
3. Test service revenue against installed systems, utilization, renewal,
   parts, field labor, warranty, and fab spending; the filing does not provide
   a quantitative installed-base denominator.
4. Carry R&D, technical support, inventory, purchase commitments, SBC, debt,
   and dilution into maintenance/growth analysis beyond PP&E.
5. Stress 19% customer concentration and approximately 87% international
   revenue through export, currency, credit, and geopolitical shocks.
6. Treat dividends and buybacks as capital-allocation outputs, not proof that
   the cycle-normalized residual is distributable.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what system growth, service renewal,
installed-base durability, cycle-normalized margin, R&D/support reinvestment,
factoring normalization, and cost of capital the price requires. The Lyn
Alden-style stress test combines fab-capex contraction, rates, export controls,
customer concentration, inventory build, factoring withdrawal, and floating debt
to test whether the control point survives a liquidity reversal.

## Promotion boundary

`semiconductor-process-control-qualified; installed-base-and-cycle-normalization-open; no-ranking`

Promotion requires a multi-year same-period service-per-system and cash-
conversion panel, factoring unwind, customer/geo concentration, deferred-
revenue delivery, purchase-commitment settlement, R&D/support maintenance,
SBC, debt, and diluted per-share cash. Revenue, service growth, reported FCF,
and capital returns remain diagnostic inputs.

## September 18, 2026 valuation expectation refresh

The current market snapshot reports KLA equity value of approximately `$23.318B`
at `$176.99` per share. Against FY2026 reported OCF less PP&E of `$3.767B`,
the simple market-cap screen is approximately `6.2x`. This is not a normalized
FCF multiple: FY2026 OCF margin declined to `30.5%`, the receivable-plus-
inventory-less-payable exposure screen reached `$5.914B`, receivables factoring
was `$515.5M`, and installed-base, utilization, renewal, and service-per-system
data remain undisclosed. The price input belongs in a cycle and factoring
sensitivity surface, not in a promoted owner-cash ranking.

## Sources

- [Semiconductor process-control synthesis](annual-report-semiconductor-process-control-first-principles-synthesis-pass-2-2026-09-17.md)
- [KLA five-year cash-cycle panel](combined-investment-research-kla-five-year-cash-cycle-panel-2026-09-17.md)
- [KLA cycle-normalized owner-cash pass](combined-investment-research-kla-cycle-normalized-owner-cash-pass-2-2026-09-17.md)
- [KLA installed-base denominator boundary](combined-investment-research-kla-installed-base-denominator-boundary-2026-09-17.md)
