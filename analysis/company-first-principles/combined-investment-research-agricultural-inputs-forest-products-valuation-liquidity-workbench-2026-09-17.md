# Agricultural inputs and forest products valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves CF Industries and West Fraser from basic-materials
observations into company-specific valuation, reinvestment, liquidity, and
thesis-breaker objects. It keeps nitrogen-to-food economics separate from
wood-products-to-housing economics; neither is treated as a generic materials
multiple or as mechanical operating cash less capex.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| CF Industries | Through-cycle nitrogen cash after natural-gas input, ammonia-plant uptime, logistics, maintenance, Blue Point investment, debt, and capital returns | Plant maintenance, outage recovery, turnaround, gas contracts, logistics, low-carbon ammonia, environmental obligations, debt, and diluted shares | Nitrogen-price normalization, gas-cost inflation, Yazoo outage, farmer affordability, global supply, tariffs, and Blue Point offtake | Cash generation/repurchases continue while production uptime, realized nitrogen economics, Blue Point commitments, debt, or per-share residual deteriorate |
| West Fraser | Through-cycle wood-products cash after mill cost, housing/repair demand, tariffs, curtailments, modernization, restructuring, and debt | Mill maintenance and modernization, Henderson ramp, closures/curtailments, timber/log supply, environmental claims, working capital, and diluted shares | Housing starts, lumber/panel prices, tariffs/duties, freight, mill utilization, restructuring cash, and liquidity | Housing or repair demand recovers while mill utilization, modernization return, impairment burden, debt, or diluted residual weakens |

## Current evidence anchors

- CF FY2025 net earnings were `$1.46B`, adjusted EBITDA `$2.89B`, and free
  cash flow `$1.79B`; it repurchased `16.6M` shares for `$1.34B`. Gross ammonia
  production was about `10.1M` tons, with 2026 expectations reset to about
  `9.5M` tons because of Yazoo.
- CF's Blue Point permits allowed construction to begin in August 2026; the
  project remains an investment and offtake/return question, not current owner
  cash.
- West Fraser FY2025 sales were `$5.462B`, earnings were `$(937)M`, and
  adjusted EBITDA was `$56M`; restructuring and impairment charges were `$712M`.
  About `54%` of lumber capacity was in the U.S. South, and Q2 2026 adjusted
  EBITDA improved to `$59M` as Henderson output more than doubled versus Q1.

## QoE and financial-shenanigans prompts

1. Separate realized nitrogen or lumber price, volume, mix, freight, duties,
   energy, and plant/mill uptime before treating reported margin as durable.
2. Keep outage, insurance, litigation, restructuring, impairment, and tax
   deposits separate from recurring cash; exceptional proceeds are not a
   commodity-cycle denominator.
3. Model maintenance, turnarounds, modernization, environmental obligations,
   and low-carbon projects as capital claims before repurchases or dividends.
4. Test CF's farmer affordability and Blue Point offtake rather than assuming
   biological nitrogen demand guarantees price or cash flow.
5. Test West Fraser's Henderson and portfolio high-grading economics against
   housing starts, regional capacity, tariffs, and mill utilization.
6. Carry debt, share count, SBC, and impairment/restructuring cash into the
   common-owner residual rather than using adjusted EBITDA or reported FCF.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what through-cycle price, volume,
utilization, replacement capital, project return, reinvestment rate, and cost
of capital the valuation requires. The Lyn Alden-style stress test asks whether
food and housing affordability, energy, rates, tariffs, global supply, farmer or
builder liquidity, and debt service preserve the companies' cash through a
commodity reversal.

## Promotion boundary

`agricultural-inputs-and-forest-products-qualified; commodity-cycle-and-replacement-normalization-open; no-ranking`

Promotion requires same-period realized-price/netback or lumber-price/mix,
plant/mill uptime, maintenance and modernization cash, project/offtake return,
working-capital settlement, debt, and diluted common-owner residual. Production,
adjusted EBITDA, OCF, free cash flow, repurchases, and dividends remain
diagnostic inputs.

## Sources

- [CF Industries company analysis](basic-materials/agricultural-chemicals/cf-industries-holdings-inc/company-analysis.md)
- [West Fraser company analysis](basic-materials/lumber-wood-production/west-fraser-timber-co-ltd/company-analysis.md)
- [Basic materials Q2 cash-quality refresh](combined-investment-research-basic-materials-q2-2026-cash-quality-refresh-2026-09-17.md)
