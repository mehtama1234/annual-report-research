# Hotel property-owner valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Apple Hospitality REIT from RevPAR and hotel-demand
evidence into a property-level margin, replacement-capital, refinancing,
disposition, and distributable-cash test. It is separate from hotel brands,
loyalty platforms, and senior-housing property models. RevPAR, Adjusted
EBITDAre, FFO/AFFO, distributions, and asset sales are not normalized common-
owner cash by themselves.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Apple Hospitality REIT | Property cash after occupancy, ADR, labor, management fees, insurance, taxes, utilities, maintenance/renovation capital, debt, refinancing, REIT obligations, and dilution | Room/common-area replacement, technology, safety, energy, renovation, property repositioning, acquisitions, and financing | RevPAR decline, business/government travel weakness, labor/insurance inflation, renovation deferral, rates/maturities, property-value decline, or disposition dependence | RevPAR rises while property margin, replacement capital, fixed-charge coverage, per-share value, or sustainable distribution deteriorates |

## Current evidence anchors

- Apple owned `217` hotels and `29,583` rooms at December 31, 2025, and `216`
  hotels and `29,459` rooms at June 30, 2026 after a disposition.
- FY2025 comparable occupancy was `74.1%`, ADR `$159.09`, and RevPAR `$117.95`;
  occupancy and RevPAR both declined year over year.
- Q2 FY2026 occupancy was `80.1%`, ADR `$169.90`, RevPAR `$136.17`, and
  Adjusted EBITDAre `$144.5M`; the recovery still requires property-margin and
  normalized-capital confirmation.
- Hotels use third-party managers and Marriott/Hilton flags. Apple owns the
  physical property and residual capital burden, not the full guest or loyalty
  relationship.

## QoE and financial-shenanigans prompts

1. Decompose RevPAR into occupancy, ADR, market, weekday/weekend, business/
   leisure, government, group, event, and calendar effects.
2. Reconcile RevPAR to property-level EBITDA after labor, management fees,
   utilities, insurance, taxes, repairs, brand fees, and service quality.
3. Establish a normalized replacement and renovation-capital allowance rather
   than capitalizing a low current-year spend.
4. Track dispositions by sale price, book value, debt reduction, yield, and cash
   removed from the operating portfolio.
5. Reconcile Adjusted EBITDAre, FFO/AFFO, and distributions to interest, debt
   maturities, preferred/operating-partnership claims, capex, and dilution.
6. Test brand fees and standards against owner RevPAR, renovation requirements,
   operator coverage, and property return.
7. Charge debt, refinancing, insurance, taxes, distributions, and diluted
   shares before promoting residual property cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what stabilized occupancy, ADR,
RevPAR, property margin, replacement capex, capitalization rate, debt cost, and
per-share value the equity price requires. The Lyn Alden-style stress test asks
whether employment, business travel, rates, insurance, wages, supplies, and
property replacement costs can be absorbed through a weak demand cycle.

## Promotion boundary

`hotel-property-owner-qualified; revpar-to-distributable-cash-open; no-ranking`

Promotion requires same-period joins from occupancy and ADR to property cash,
maintenance/renovation capital, debt and fixed-charge coverage, dispositions,
property value, REIT obligations, and diluted common residual. RevPAR, Adjusted
EBITDAre, FFO/AFFO, distributions, and asset sales remain diagnostic inputs.

## Sources

- [Apple Hospitality deep company page](../deep-company-pages/apple-hospitality-reit-inc.md)
- [Apple Hospitality company packet](../../extracted/real-estate/reit-hotel-motel/apple-hospitality-reit-inc/company-packet.md)
- [Apple Hospitality source ledger](../../extracted/real-estate/reit-hotel-motel/apple-hospitality-reit-inc/source-ledger.md)
