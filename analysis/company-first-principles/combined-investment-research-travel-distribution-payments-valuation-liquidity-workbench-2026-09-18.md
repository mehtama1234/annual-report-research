# Travel distribution and payments valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench moves Booking Holdings from travel-marketplace evidence into a
company-specific valuation, settlement, retention, and owner-cash test. It
keeps Booking's agency and merchant models separate from hotel ownership,
local delivery, and alternative-accommodation supply ownership.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Booking Holdings | Retained travel contribution after payment, marketing, support, fraud, refunds, taxes, technology, acquisitions, debt, SBC, and dilution | Search/discovery, software, payment and trust systems, customer support, loyalty, marketing, acquisitions, and working-capital settlement | Travel downturn, supplier/consumer dislocation, merchant refunds or chargebacks, regulatory/tax change, take-rate pressure, debt, or higher customer-acquisition cost | Gross bookings and merchant mix rise while retained contribution, direct-repeat economics, settlement cash, or diluted per-share residual deteriorate |

## Current evidence anchors

- FY2025 revenue was about `$26.917B` and operating cash flow was `$9.409B`;
  PP&E purchases were about `$322M` and SBC about `$613M`.
- FY2025 common-owner screen after PP&E and SBC was about `$8.474B`; the
  company repurchased about `$6.440B` of stock and paid about `$1.248B` of
  dividends while carrying roughly `$18.736B` of long-term debt.
- Q1 2026 gross bookings were `$53.758B`, merchant gross bookings `$38.736B`,
  and merchant mix `72%`; Q2 gross bookings were `$50.957B`, merchant gross
  bookings `$36.996B`, and merchant mix `73%`.
- Booking.com had about `4.7M` properties at June 2026; alternative lodging was
  about `37%` of Booking.com room nights. Room nights, flights, cars, mobile,
  direct behavior, and loyalty remain operating inputs rather than owner cash.

## QoE and financial-shenanigans prompts

1. Reconcile merchant gross bookings from traveler collection through supplier
   remittance, payment cost, refunds, fraud, chargebacks, support, and retained
   contribution.
2. Separate agency and merchant take rates, working capital, supplier funds,
   deferred revenue, and travel-completion obligations.
3. Test whether direct/app/loyalty growth lowers paid acquisition cost after
   discounts and rewards, rather than merely increasing booking volume.
4. Split accommodation, flights, cars, alternative lodging, payments, and
   Connected Trip attachment by contribution and service burden.
5. Normalize software, trust, AI/customer-support, acquisition, SBC, debt, and
   diluted shares before treating adjusted EBITDA less capex as owner cash.
6. Treat gross bookings, room nights, merchant mix, and buybacks as diagnostic
   until retained contribution and common residual are joined.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test converts active supply, available
inventory, search conversion, booking frequency, average booking value, and
retained take rate into contribution after payment and service cost. The Lyn
Alden-style stress test asks whether discretionary travel, exchange rates,
airfare, geopolitical shocks, supplier health, regulation, and debt leave the
platform with enough liquidity to defend demand and supply. The marketplace
can be asset-light while still carrying substantial settlement and trust risk.

## Promotion boundary

`travel-distribution-qualified; retained-contribution-and-settlement-cash-open; no-ranking`

Promotion requires same-entity, same-period joins from gross bookings, retained
revenue, agency/merchant mix, payment and supplier settlement, refunds,
chargebacks, marketing, support, fraud, taxes, software, acquisitions, SBC,
debt, and diluted common residual. Gross bookings, room nights, direct share,
merchant mix, adjusted EBITDA less capex, and repurchases remain diagnostic.

## Sources

- [Booking company page](../deep-company-pages/booking-holdings-inc.md)
- [Booking company packet](../../extracted/services/transportation-services/booking-holdings/company-packet.md)
- [Booking source ledger](../../extracted/services/transportation-services/booking-holdings/source-ledger.md)
