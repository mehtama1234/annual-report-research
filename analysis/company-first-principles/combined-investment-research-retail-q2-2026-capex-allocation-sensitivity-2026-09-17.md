# Retail Q2 2026 capex allocation sensitivity

## Purpose

This pass tests CA-06/Q-05 using the latest interim capital-allocation
disclosures. It distinguishes a disclosed growth category from the remainder
of property spending; it does not relabel the remainder as maintenance.

## Current evidence

Walmart's six-month property spending of `$14.181B` is categorized as:

| Category | H1 FY2027 spend |
|---|---:|
| Supply chain, customer-facing initiatives, technology, and other | `$7.659B` |
| Store and club remodels | `$3.623B` |
| New stores, expansions, and relocations | `$1.087B` |
| Walmart International | `$1.812B` |

The `$1.087B` new-store/expansion/relocation category is a disclosed growth
floor. The other `$13.094B` is a mixed remainder, not a maintenance estimate.
Walmart also reports H1 OCF of `$19.710B` and management-defined FCF of
`$5.529B`; the latter still excludes debt service, contractual obligations, and
acquisitions.

Target's latest filing reports `$2.404B` of H1 property expenditures and `$4.519B`
of OCF, but the interim statement does not split the property line between
maintenance, remodel, technology, supply chain, and growth. TJX reports
`$1.159B` of H1 property additions and `$3.345B` of OCF, but its interim filing
also does not provide a maintenance/growth dollar split. Segment sales and
profit, store counts, inventory, and lease liabilities are useful operating
context, not capex classification.

## Bounded sensitivity

For Walmart only, treating the `$1.087B` disclosed category as growth creates
a known-growth floor. It does not justify treating the remaining `$13.094B` as
maintenance or growth. For Target and TJX, the safe range remains bounded by
reported OCF-less-property and a separate scenario that applies a stated
assumption to an unallocated property pool. No scenario is promoted to
normalized owner cash.

## QoE and valuation implication

The capex classification is a valuation input, not an earnings-quality finding.
The financial-shenanigans risk is overclaiming a low maintenance burden by
calling all unclassified property growth or by using management FCF as residual
cash. Damodaran-style reinvestment must use a transparent maintenance/growth
range; the Lyn Alden-style liquidity test must also consider debt, supplier
terms, inventory timing, leases, and customer affordability.

## Promotion status

Q-05 remains `evidence-insufficient` for a fully normalized common-owner cash
denominator. The required next object is a same-company, same-period project or
asset schedule that identifies replacement, remodel, technology, supply-chain,
and expansion spending and links each category to operating benefit and cash
return.

Sources: [Walmart Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm), [Target Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm), and [TJX Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/109198/000010919826000048/tjx-20260801.htm).

Decision marker: `retail-q2-2026-capex-allocation-sensitivity-qualified`
