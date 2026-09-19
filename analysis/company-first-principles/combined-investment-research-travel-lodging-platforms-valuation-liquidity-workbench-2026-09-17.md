# Travel and lodging platforms valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench routes Airbnb, Booking, Marriott, Hilton, and Sunstone as
separate travel-control models. Airbnb and Booking are marketplaces and
payment interfaces; Marriott and Hilton are brand/loyalty/fee systems; Sunstone
owns concentrated physical hotels. Host Hotels remains a separate property-
owner comparison.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Airbnb | Trust marketplace cash after host payouts, payment, support, safety, marketing, regulation, product, SBC, and dilution | Trust/identity, customer support, payments, insurance, product, local compliance, services/experiences, SBC, and debt | Travel demand, regulation, host supply, safety, refunds, payment, rates, and trust | GBV/nights grow while take rate, host economics, safety/support cost, regulation, or diluted cash deteriorates |
| Booking | Travel-distribution and merchant-payment cash after supplier remittance, marketing, fraud, refunds, technology, and dilution | Search/discovery, payments, customer support, merchant working capital, loyalty, technology, acquisitions, and SBC | Travel cycle, FX, supplier concentration, merchant refunds/chargebacks, regulation, and customer acquisition | Gross bookings and Connected Trip grow while take rate, payment risk, supplier cash, marketing, or diluted residual weakens |
| Marriott | Brand, franchise, management, loyalty, and co-brand fee cash after loyalty claims, owner support, technology, guarantees, and dilution | Reservation/loyalty systems, Bonvoy points, owner distribution, technology, contract acquisition, debt, SBC, and diluted shares | Hotel-owner health, loyalty redemption, travel/geopolitics, guarantees, brand dilution, and rates | Rooms/pipeline grow while owner returns, loyalty liability, contract costs, guarantees, or per-share cash deteriorate |
| Hilton | Brand/fee cash after loyalty, contract acquisition, consolidated-hotel capex, owner support, debt, and dilution | Hilton Honors, reservation/technology, contract acquisition, brand standards, owner support, acquisitions, and SBC | Owner financing, renovations, loyalty claims, travel demand, franchise retention, guarantees, and refinancing | Rooms/pipeline and fees grow while owner retention, loyalty cost, contract investment, debt, or diluted cash weakens |
| Sunstone | Concentrated hotel-property cash after labor, renovation, insurance, interest, asset recycling, debt, and common claims | Hotel renewal/repositioning, property capex, labor, insurance, taxes, redevelopment, acquisitions, and dilution | RevPAR/occupancy, event/weather, property concentration, refinancing, renovation, and asset-sale timing | RevPAR/FFO rises while property cash after renewal, interest, claims, or asset value deteriorates |

## Current evidence anchors

- Marriott 2025 had `9,805` properties, `1,779,936` rooms, about `$5.383B`
  adjusted EBITDA, `$3.212B` OCF, `$604M` capital/technology spend, and a
  `$7.992B` guest-loyalty liability; full-year RevPAR grew `2.0%`.
- Hilton had `9,158` properties and `1,351,351` rooms at 2025 year-end, a
  roughly `520,500`-room pipeline, and 2025 OCF of `$2.129B` after property/
  software capex and contract-acquisition costs.
- Airbnb and Booking are marketplace cases where GBV/gross bookings are not
  retained revenue; host/supplier payouts, payments, refunds, support, fraud,
  and regulation remain senior claims.
- Sunstone owned `14` hotels and `6,999` rooms at 2025 year-end; Q2 2026 RevPAR
  was `$263.61`, up `9.3%`, with adjusted EBITDAre `$76.7M`.

## QoE and financial-shenanigans prompts

1. Separate GBV/gross bookings, take rate, merchant remittance, host/supplier
   payouts, refunds, payment costs, and collected platform cash.
2. Treat hotel pipelines, room counts, RevPAR, loyalty points, and franchise
   fees as different objects; pipeline rooms are not current cash.
3. Charge loyalty redemption, contract acquisition, owner support, guarantees,
   renovation, labor, insurance, interest, and property capex before residual.
4. Test asset-light brand economics against owner health; owners fund the
   buildings but brand companies retain loyalty, reputation, and support claims.
5. Keep Sunstone and Host property cash separate from Marriott/Hilton fee cash.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what nights, GBV, take rate, room
growth, RevPAR, fee rate, loyalty economics, renewal, property capex, and cost
of capital the valuation requires. The Lyn Alden-style stress test asks whether
income, rates, travel behavior, regulation, labor, insurance, FX, owner
financing, and refinancing preserve liquidity.

## Promotion boundary

`travel-lodging-qualified; marketplace-brand-property-and-loyalty-cash-open; no-ranking`

Promotion requires same-period booking/fee or property collection, host/supplier
settlement, loyalty and contract claims, maintenance/renovation capital,
owner/property return, debt, SBC, and diluted common residual. GBV, bookings,
rooms, pipeline, RevPAR, FFO, adjusted EBITDA, and buybacks remain diagnostic.

## Sources

- [Airbnb deep-company memo](../deep-company-pages/airbnb-inc.md)
- [Booking deep-company memo](../deep-company-pages/booking-holdings-inc.md)
- [Marriott deep-company memo](../deep-company-pages/marriott-international-inc.md)
- [Hilton deep-company memo](../deep-company-pages/hilton-worldwide-holdings-inc.md)
- [Sunstone deep-company memo](../deep-company-pages/sunstone-hotel-investors-inc.md)
