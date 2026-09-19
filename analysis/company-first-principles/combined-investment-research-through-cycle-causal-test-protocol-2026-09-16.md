# Combined investment research through-cycle causal-test protocol

Research date: `2026-09-16`

## Purpose

The historical macro panel establishes regime consistency, not causal
attribution. This protocol defines what evidence would be needed to promote
each pilot from a plausible transmission mechanism to a through-cycle causal
conclusion. It is a test specification, not a claim that the tests have
already passed.

The current observations remain in the [historical macro-regime validation](combined-investment-research-macro-historical-regime-validation-2026-09-15.md),
the [longitudinal retail bridge](data/combined-investment-research-macro-longitudinal-retail-bridge-2026-09-15.csv),
and the three pilot ledgers.

The first bounded quantitative diagnostic is now recorded in the [retail
panel diagnostic](combined-investment-research-through-cycle-retail-panel-diagnostic-2026-09-16.md).
It compares the existing cash-after-property screen across real-wage and CPI
regimes while preserving the non-causal, pooled-panel boundary.
The follow-on [within-company diagnostic](combined-investment-research-through-cycle-retail-within-company-diagnostic-2026-09-16.md)
removes company scale from the comparison and still finds an even split between
same-direction and opposite-direction transitions.
The [lagged diagnostic](combined-investment-research-through-cycle-retail-lagged-diagnostic-2026-09-16.md)
tests whether prior real-wage conditions lead next-period cash changes; it finds
7 same-direction versus 8 opposite-direction usable transitions.

## Protocol rule

For every company period, preserve the filing period, macro observation date,
metric denominator, and company action controls. A directionally matching
result is not causal evidence when price, mix, acquisitions, supply shocks,
capital allocation, policyholder flows, hedges, or accounting changes move at
the same time. Promotion requires repeated aligned observations, a measurable
mechanism, controls for the principal confounds, and a falsifier that could
fail in a subsequent filing.

## Pilot test specifications

### Retail affordability and cash quality

Test whether real-income and inflation regimes change traffic, comparable
sales, mix, markdowns, inventory, payables, temporary support, and cash after
property spending in the predicted direction. Use comparable fiscal periods
and separate TJX, Target, and Walmart actions. Control for store openings and
closures, promotions, tariffs/refunds, vendor terms, acquisitions, shrink,
freight, and attached-service mix. A promotion-ready result requires repeated
periods where the demand signal leads the operating and cash outcomes and the
major company-specific confounds are measured. A breaker is stable demand but
declining cash quality, or deterioration after temporary support is removed.

### Wheaton–Antamina financing and delivery durability

Test whether rate, silver-price, and delivery regimes change the named stream's
payable ounces, realized settlement economics, financing burden, and owner
return in the predicted direction. The current pilot has only a post-close
operating window, so historical macro rows are stress inputs rather than
observations of the BHP tranche. Promotion requires BHP-only metal-credit
quantities, settlement and receipt dates, reserve-backed delivery periods,
Antamina-specific tax and debt allocation, and multiple observed periods. A
breaker is delivered or settled metal below the quantity, price, or timing
needed to recover the upfront payment and financing burden.

### Apollo–Athene spread and liquidity transmission

Test whether policy rates, credit losses, liability funding cost, policyholder
flows, and liquidity conditions change Athene's asset yield, cost of funds,
net investment spread, capital availability, distributions, and Apollo cash
access in the predicted direction. Control for asset mix, hedges, marks,
credit migration, reinsurance, capital requirements, preferred claims, and
legal-entity restrictions. Promotion requires period-matched spread and
liability data, asset-level or route-level realized cash, regulatory-capital
constraints, dated Athene-to-AGM receipt evidence, and repeated periods. A
breaker is spread compression, credit loss, or regulated cash restriction that
prevents the predicted upstream common-owner conversion.

## Current status

`protocol-defined; descriptive retail diagnostic added; evidence-insufficient for causal promotion`

The protocol makes the next Q-10 test reproducible and falsifiable, but it does
not turn the existing 18-row retail bridge, current-period Wheaton evidence,
or Apollo/Athene spread screen into causal proof.

## Current-regime input refresh — 2026-09-17

The live external inputs are now date-controlled through the September 16 FOMC
decision, August CPI, and July personal-income/outlays release. The protocol
will use the `3.75%–4.00%` funds target, `3.4%` headline CPI / `2.4%` core CPI,
`16.3%` energy inflation, and `3.0%` saving-rate observations as stress and
regime markers. They are exogenous input observations, not evidence that any
pilot outcome was caused by the macro regime. The next promotion still
requires repeated company-period joins and confound controls.

Structured control: [causal-test protocol CSV](data/combined-investment-research-through-cycle-causal-test-protocol-2026-09-16.csv).
