# Merchant power and generation valuation/liquidity workbench

Research date: `2026-09-17`

## Purpose

This workbench moves Constellation, Exelon, NRG, and Vistra into separate
valuation, reinvestment, liquidity, and thesis-breaker objects. It keeps clean
nuclear generation, regulated wires, customer-backed power, and merchant fleet
optimization distinct from the existing NextEra/AEP/Duke rate-base and
customer-recovery lane.

## Decision matrix

| Company/model | Correct valuation object | Reinvestment denominator | Liquidity stress | Filing-based thesis breaker |
| --- | --- | --- | --- | --- |
| Constellation | Scarce clean-reliable generation cash after fleet availability, nuclear contracts, PPAs, restarts, integration, and debt | Nuclear maintenance, relicensing, restart/upgrade, gas/renewables, customer-specific power campuses, environmental obligations, and dilution | Nuclear outage, Calpine integration, PPA economics, regulatory friction, load/customer concentration, and debt | Clean-power demand grows while availability, contract margin, restart/integration cash, or per-share residual deteriorates |
| Exelon | Regulated transmission/distribution cash after rate-base investment, storm costs, customer affordability, and recovery | Wires, substations, storm hardening, reliability, transmission, working capital, and debt | Disallowed recovery, affordability politics, storms, execution, financing, and rate pressure | Rate base grows while recovery, reliability, customer affordability, or diluted residual weakens |
| NRG | Customer-backed generation and retail cash after capacity projects, demand response, retail claims, LS Power integration, and debt | Generation, retail systems, demand response, smart-home services, Bring Your Own Power projects, acquisitions, and dilution | Hyperscaler project failure, retail churn, affordability, market rules, acquisition integration, and financing | Customer-backed load grows while project funding, retail cash, capacity margin, or per-share residual deteriorates |
| Vistra | Merchant dispatchable fleet cash after hedging, availability, PPAs, retail obligations, acquisitions, and debt | Fleet maintenance, nuclear, storage, generation acquisitions, hedging collateral, environmental obligations, and dilution | Power-price normalization, hedge mismatch, availability, Cogentrix integration, PPAs, and collateral/liquidity | Availability and contracts rise while hedge, fleet, acquisition, debt, or diluted residual economics weaken |

## Current evidence anchors

- Constellation describes a `55 GW` fleet; Q2 2026 adjusted operating earnings
  were `$2.55` per share, guidance was `$11.50-$12.50`, and it added `920 MW`
  of long-term clean-power PPAs. A CyrusOne agreement included `380 MW` with
  an exclusive path for another `380 MW`.
- Exelon serves nearly `11 million` customers through six regulated utilities;
  its 2026 capital plan was `$41.7B`, with expected rate-base growth of `7.9%`
  and close to `90%` of rate base under established recovery mechanisms through
  2026-2027.
- NRG serves roughly `8 million` customers and has about `25 GW` of generation;
  Q2 2026 adjusted EBITDA was `$1.217B` and FCFbG `$1.025B`. Its Texas project
  was `1.2 GW` and tied to a cloud/AI hyperscaler; LS Power added `13 GW`.
- Vistra Q2 2026 ongoing-operations adjusted EBITDA was `$1.767B`, with at
  least `97%` commercial availability during extreme heat. Its pending
  Cogentrix acquisition was `5,500 MW`, and 2026-2028 generation hedge coverage
  was approximately `100%`, `84%`, and `58%`.

## QoE and financial-shenanigans prompts

1. Separate regulated recovery, merchant price, hedged price, PPA cash,
   retail collections, capacity payments, and customer-backed project funding.
2. Carry nuclear/generation maintenance, wires capex, storm costs, turnarounds,
   environmental obligations, hedge collateral, and debt before owner cash.
3. Keep approved capacity, signed load, PPAs, and customer commitments separate
   from funded construction, collected receipts, and common-owner residual.
4. Test acquisitions through purchase price, integration costs, fleet return,
   availability, debt, and dilution.
5. Do not apply a regulated rate-base multiple to merchant generation or a
   merchant power multiple to Exelon's regulated wires model.

## Damodaran/Lyn Alden application

The Damodaran-style expectation test asks what availability, realized price,
hedge/PPA economics, rate-base growth, project return, reinvestment, and cost
of capital the valuation requires. The Lyn Alden-style stress test asks whether
rates, fuel, load growth, affordability, weather, refinancing, market rules,
and collateral demands preserve cash through a power-market reversal.

## Promotion boundary

`merchant-power-and-generation-qualified; availability-recovery-and-project-cash-open; no-ranking`

Promotion requires same-period generation or regulated collection, maintenance
and project cash, hedge/PPA settlement, customer-backed funding, acquisition
return, debt, and diluted common-owner residual. MW, availability, adjusted
EBITDA, FCFbG, capacity, signed load, and PPAs remain diagnostic inputs.

## Sources

- [Constellation company analysis](utilities/diversified-utilities/constellation-energy-corporation/company-analysis.md)
- [Exelon company analysis](utilities/electric-utilities/exelon-corporation/company-analysis.md)
- [NRG company analysis](utilities/other-utilities/nrg-energy-inc/company-analysis.md)
- [Vistra company analysis](utilities/other-utilities/vistra-energy-corp/company-analysis.md)
