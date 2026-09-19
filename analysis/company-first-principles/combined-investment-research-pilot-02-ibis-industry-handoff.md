# Pilot 02 IBIS industry-to-filing handoff

Date: `2026-09-15`

This bridge makes the IBIS layer explicit in the affordability pilot. IBIS is
used to frame industry structure and adjacent forces; the annual-report
research remains the authority for company-period facts, cash, and valuation.

## Force-to-test map

| IBIS force from crosswalk | Industry implication | Filing-level test in this pilot | Boundary |
| --- | --- | --- | --- |
| `the-hollow-middle` | Consumers may split between premium identity spending and lower-cost value systems | Compare TJX off-price discovery, Target planned value, and Walmart low-price scale using traffic, mix, margin, inventory, and cash | IBIS framing does not prove household prevalence or which retailer wins |
| `the-margin-vise` | Input, labor, promotional, and affordability pressure can compress retail spread | Test gross margin, markdowns, vendor income, tariffs, inventory, payables, fulfillment, and capex in the company filings | Industry force does not identify the company-specific cause of a margin change |
| `the-channel-shift` | Customer access and purchase pathways move across stores, digital, membership, and services | Test comparable sales, traffic, e-commerce, membership, advertising, card economics, and attached-service cash allocation | Reported digital or service growth is not incremental owner cash |

## Handoff chain

```text
IBIS force framing
  -> retail industry/control-point hypothesis
  -> TJX / Target / Walmart candidate cohort
  -> primary filing metrics and burden map
  -> owner-cash denominator
  -> valuation and thesis breaker
```

The structured mapping is in the [IBIS handoff CSV](data/combined-investment-research-pilot-02-ibis-industry-handoff.csv).
It is intentionally not an additional company-fact ledger: it records why a
source-layer hypothesis enters the filing queue and what evidence must test it.

## Current grade

`industry-handoff-confirmed`: the IBIS crosswalk now has a named retail route
into the pilot's filing tests. The handoff does not upgrade the social or
industry evidence into causal demand proof.

## Source

- [IBIS industries crosswalk](../../notes/ibis-industries-crosswalk.md)
- [Pilot 02 affordability/value evidence ledger](data/combined-investment-research-pilot-02-affordability-value.csv)
