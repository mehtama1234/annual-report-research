# Combined investment research thesis-breaker register

Research date: `2026-09-16`

This register converts each pilot's prose falsifiers into observable tests. A
breaker is not a prediction that the thesis fails; it is the specific filing,
metric, or legal document that would weaken the claim if the observed result
crosses the stated boundary.

## How to use it

1. Read the thesis claim only with its current evidence grade.
2. Collect the named next document when it becomes available.
3. Measure the observable breaker against the stated denominator.
4. Update the conclusion and valuation if the trigger is reached.

The register deliberately avoids invented numeric thresholds where the current
source packet has not established one. In those cases, the trigger is defined
as a reconciliation failure, a directionally adverse filing result, or a
source-backed return below the required return.

The structured version is [the thesis-breaker CSV](data/combined-investment-research-thesis-breaker-register.csv).

## Current coverage

| Pilot | Breakers | Core question |
| --- | ---: | --- |
| Wheaton–Antamina | 3 | Do BHP-only deliveries become cash and an after-tax financed return? |
| Retail cohort | 3 | Does value demand and attached-service growth survive margin, supplier-finance, working-capital, lease, and reinvestment burdens? |
| Apollo–Athene | 3 | Do fee and related-party asset routes survive credit, capital, and access constraints? |

Current state for all nine rows is `active-qualified`: the tests are defined,
but no pilot has earned a full-proof conclusion.

## Latest Q-10 observation

The retail affordability-to-cash breaker has now been run against the current
18-row FY2020–FY2026 bridge. The pooled regime split is confounded by company
scale and company actions. The within-company diagnostic finds `6` same-
direction and `6` opposite-direction transitions; the lagged diagnostic finds
`7` same-direction and `8` opposite-direction usable transitions. These are
useful falsifier observations against a simple universal macro-to-cash rule,
but they do not activate TB-RET-01 or TB-RET-02 because the sample remains
small and fiscal overlap, mix, capex, inventory, vendor terms, support,
seasonality, and store actions are not fully controlled.

Supporting records: [within-company diagnostic](combined-investment-research-through-cycle-retail-within-company-diagnostic-2026-09-16.md),
[lagged diagnostic](combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.md),
and [causal-test protocol](combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.md).

TB-RET-02 now also carries the period-matching control from the [interim
lease-and-tax search boundary](combined-investment-research-pilot-02-retail-interim-lease-tax-search-boundary-2026-09-16.md):
the checked TJX, Target, and Walmart H1/Q2 HTML does not provide dedicated
cash-paid lease or cash-tax lines. The result keeps annual burden observations
diagnostic and prevents them from being used as matched-period H1 owner cash.
It does not activate the breaker or prove that interim payments did not occur.

The Concord Q-08 route has also been refined: the July 2026 KBRA page is a
dated timely-interest proxy, while the underlying transaction surveillance
tables remain login-gated. The proxy is therefore retained as servicing
observability and cannot activate an Apollo return breaker or prove Athene cash.
