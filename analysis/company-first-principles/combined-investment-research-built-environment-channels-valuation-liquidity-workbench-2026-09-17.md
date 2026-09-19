# Built-environment channel valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves Core & Main, Watsco, Builders FirstSource, and Ferguson
from company-level first-principles observations into company-specific
valuation, reinvestment, liquidity, and thesis-breaker objects. It keeps civic
waterworks, HVAC replacement, homebuilder production, and contractor repair
channels separate rather than treating all distribution revenue as one margin
pool.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Core & Main | Waterworks and fire-protection channel cash after inventory, branch density, private label, acquisitions, municipal timing, and debt | Branch inventory, freight, treatment/waterworks expertise, greenfields, acquisitions, private-label support, working capital, SBC, and debt | Municipal appropriations, project timing, supplier terms, tariffs, freight, acquisition integration, and water-infrastructure funding | Sales/EBITDA growth continues while inventory, municipal collection, acquisition return, margin, or diluted per-share cash deteriorates |
| Watsco | HVAC replacement-channel cash after inventory transition, contractor support, refrigerant conversion, branch density, and working capital | Equipment/parts inventory, branches, digital tools, contractor training, A2L transition, acquisitions, SBC, and debt | Weather, housing/RMI softness, A2L inventory conversion, manufacturer terms, contractor credit, tariffs, and margin compression | Replacement demand persists while A2L conversion, inventory turns, contractor economics, or diluted cash weaken |
| Builders FirstSource | Builder-workflow cash after commodity exposure, prefabrication, installation, digital tools, housing starts, and acquisition integration | Components, manufacturing capacity, delivery fleet, installation labor, prefabrication, digital systems, acquisitions, and debt | Mortgage rates, starts, lumber/commodity deflation, labor, builder concentration, land-cycle weakness, and acquisition leverage | Value-added mix and prefabrication rise while starts, margin, working capital, or per-share residual deteriorate |
| Ferguson | Contractor-channel cash after repair/maintenance mix, branch density, acquisitions, inventory, and non-residential project exposure | Branch inventory, delivery, technical support, waterworks/PVF/mechanical categories, acquisitions, working capital, and debt | Residential weakness, project deferral, supplier pricing, tariffs, acquisition integration, and contractor credit | Repair/non-residential resilience fails while inventory, acquisition returns, margin, or diluted owner cash weaken |

## Current evidence anchors

- Core & Main FY2025 net sales were `$7.647B`, adjusted EBITDA `$931M`, and
  operating cash flow `$650M`; Q1 2026 guidance was reaffirmed at `$7.8B-$7.9B`
  of sales and `$950M-$980M` of adjusted EBITDA.
- Watsco Q2 2026 revenue was `$2.105B`, up `2%`, while gross profit fell `4%`
  to `$579M`; A2L refrigerant conversion and pricing actions materially affect
  inventory, mix, and channel economics.
- Builders FirstSource operated about `585` locations in `43` states in 2025;
  FY2025 sales were `$15.8B` and adjusted EBITDA `$1.6B`, while Q2 2026 sales
  fell `8.8%` and adjusted EBITDA fell `34.9%`.
- Ferguson's FY2025 10-K described `1,746` branches serving a roughly `$340B`
  North American construction market, with approximately two-thirds of sales
  tied to repair, maintenance, and improvement; Q2 2026 sales rose `4.6%` to
  `$8.751B` and non-residential revenue rose `8%`.

## QoE and financial-shenanigans prompts

1. Reconcile inventory turns, supplier terms, freight, rebates, and contractor
   or builder credit before treating distribution OCF as durable owner cash.
2. Separate commodity price, volume, mix, acquisitions, private-label or
   value-added services, and branch expansion; revenue growth alone does not
   establish channel quality.
3. Keep replacement, repair, maintenance, and new-construction demand separate
   from the capital required to support each channel.
4. Test acquisition cohorts through purchase price, integration costs,
   working-capital absorption, margin realization, and diluted shares.
5. For Watsco, model the A2L conversion as a physical inventory and contractor
   workflow event, not only as a regulatory narrative.
6. For Builders FirstSource, test whether prefabrication and installation
   actually reduce job-site labor and protect returns through a housing cycle.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what branch density, replacement or
repair demand, value-added mix, acquisition return, reinvestment rate, margin,
and cost of capital the price requires for each company. The Lyn Alden-style
stress test asks whether rates, housing starts, municipal budgets, weather,
commodity prices, supplier credit, tariffs, and contractor liquidity impair the
channel before reported revenue declines.

## Promotion boundary

`built-environment-channels-qualified; channel-cohort-and-working-capital-normalization-open; no-ranking`

Promotion requires same-period collection, inventory and supplier settlement,
maintenance/growth capital, acquisition-cohort return, debt, SBC, and diluted
common-owner cash. Sales, branch counts, adjusted EBITDA, backlog, repair mix,
or reported OCF remain diagnostic inputs.

## Sources

- [Core & Main company analysis](industrial-goods/building-materials-wholesale/core-main-inc/company-analysis.md)
- [Watsco company analysis](industrial-goods/electronics-wholesale/watsco-inc/company-analysis.md)
- [Builders FirstSource company analysis](industrial-goods/general-building-materials/builders-firstsource-inc/company-analysis.md)
- [Ferguson company analysis](industrial-goods/plumbing-hvac-distribution/ferguson-enterprises-inc/company-analysis.md)
