# Combined Investment Research: Next-Cycle Candidate Expansion

Research date: `2026-09-16`

This is the public-evidence-only handoff after the three integrated pilots.
It does not rank companies by expected return and it does not close the
CA-06 denominator gap. It selects the next research lanes by the quality of
their possible evidence chain: named payer, control point, burden carrier,
cash denominator, valuation object, and filing-based falsifier.

The candidate order is inherited from the repository's [theme selection work
order](annual-report-theme-selection-work-order-pass-1.md), narrowed to the
next three lanes that most directly extend the existing methods. The source
work order is a discovery and sequencing input, not company-quality proof.

## Recommended next cycle

| Priority | Lane | Initial candidates | Why this is next | Required proof before promotion |
| ---: | --- | --- | --- | --- |
| 1 | Power-grid customer cash | FPL, AEP, Duke | Extends the control-point method from consumer affordability to regulated infrastructure and offers a direct payer/recovery question | Named load or recovery category, approved cost, billing determinant, billed or collected revenue, in-service project, and recoverable return |
| 2 | Insurance statutory named-asset income | Apollo/Athene AP Aristotle; KKR/Global Atlantic Accordia | Extends the Apollo pilot's legal-entity and statutory method while narrowing from platform activity to an identifiable asset and income route | Named CUSIP or issuer row, legal-entity holding, income, proceeds/disposal, liability-cost context, and bounded spread/return math |
| 3 | Asset-backed collateral and borrowing base | United Rentals; Target/Zebra/Pool distributor comparison | Tests whether liquidity is supported by eligible collateral that actually collects or turns into cash, directly strengthening the working-capital and QoE lanes | Eligible collateral, borrowing capacity, advance rate, aging/collection or remittance, debt service, and cash-flow reconciliation |

The private-credit borrower-facility lane remains the next reserve option after
these three: Ares/Frontline or another document-rich borrower should enter only
when a credit agreement, lender role, use of proceeds, borrower cash source,
collateral, and repayment path can be assembled together.

## First lane already underway: power-grid customer cash

This is not a speculative queue item. The repository already has a [power-grid
answer synthesis](capital-flow-power-grid-pilot-answer-synthesis-pass-2.md), a
[customer-cash work order](annual-report-power-grid-customer-cash-proof-work-order-pass-1.md),
and a [proof-status dashboard](capital-flow-power-grid-pilot-proof-status-dashboard-pass-1.md).
The lane is currently `hold-with-strong-route-visible`: FPL has category-level
recovery, factor, true-up, output, component, and capital-structure evidence;
NextEra has named-customer contracted-output evidence; and Plains has tariff
and acquisition-capital-stack evidence. None has yet reached full project-
return proof.

The first active test is:

`FPL Distribution Inspection category recovery -> rate-class billing determinant -> billed or collected customer dollars -> category allocation -> earned return`

The parallel AEP customer-obligation route now has an eight-gate [proof chase](capital-flow-aep-large-load-customer-obligation-proof-chase-pass-1.md) and [CSV register](data/capital-flow-aep-large-load-customer-obligation-proof-chase-pass-1.csv). It is `hold-with-security-and-tariff-visible`: AEP's tariff and approximately `$2B` of mixed security are real evidence, but executed customer agreements, project allocation, billing determinants, and receipts remain unproved.

The Duke comparison now has an eight-gate [ESA and Anderson project-recovery chase](capital-flow-duke-esa-project-recovery-proof-chase-pass-1.md) and [CSV register](data/capital-flow-duke-esa-project-recovery-proof-chase-pass-1.csv). It is `hold-with-approval-and-monitoring-visible`: secured ESAs, customer-protection language, Order `2026-244`, project cost, ownership, and monitoring are visible, but final participation terms, CWIP/rate-base treatment, in-service billing, and receipts remain unproved.

The contractor comparison now has an eight-gate [project-cash proof chase](capital-flow-industrial-contractor-project-cash-proof-chase-pass-1.md) and [CSV register](data/capital-flow-industrial-contractor-project-cash-proof-chase-pass-1.csv). Sterling and MasTec remain `hold-backlog-and-aggregate-cash-visible`: backlog, aggregate OCF, capex, and acquisition data are diagnostic, while funded scope, project billing, collection, cost-to-complete, and common-owner residual remain open.

The turbine/equipment comparison now has an eight-gate [supplier-cash proof chase](capital-flow-aep-duke-turbine-supplier-cash-proof-chase-pass-1.md) and [CSV register](data/capital-flow-aep-duke-turbine-supplier-cash-proof-chase-pass-1.csv). AEP/Duke remain `hold-capacity-visible`: secured turbine capacity and regulatory pathways are visible, while vendor identity, order terms, deposits, delivery, supplier collections, and project residual cash remain open.

The next comparison tests are AEP large-load customer obligations and Duke
secured-ESA/project recovery. The lane should be promoted only if a named
category or project can be tied to customer payment or approved recovery,
period-matched cash, capital use, and a bounded return or debt-service claim.

The Duke comparison now has a named project boundary: the approximately
`1,365 MW` Anderson County combined-cycle project was reported as approved by
the South Carolina Public Service Commission, with construction anticipated in
summer 2027 and customer service targeted for early 2031. The disclosure also
identifies `95 MW` of Central Electric Power Cooperative ownership and `100 MW`
of North Carolina Electric Membership Corporation ownership. The [Anderson
approval-to-cash boundary](capital-flow-duke-anderson-county-generation-approval-recovery-boundary-2026-09-16.md)
keeps those shared ownership and forward-date fields separate from Duke net
capacity, rate-base treatment, project spending, billing, and owner cash. The
South Carolina PSC docket now adds a stronger control: full Order `2026-244`
grants the certificate subject to required federal, state, and local permits,
consultations, and certifications; the March 26 directive also requires
quarterly fuel-supply updates.
That is regulatory approval evidence, not a rate-base, cost-recovery, or
collected-cash proof object.

## Second lane already underway: insurance statutory named-asset income

The second lane is also grounded in existing work. The [insurance statutory
next-dig memo](capital-flow-insurance-statutory-named-asset-income-next-dig-pass-1.md)
sets Apollo/Athene as the prototype and KKR/Global Atlantic/Accordia as the
comparison. Apollo has legal-entity income, proceeds, and named issuer routes;
Accordia has near-reconciled owned-bond book value and row-level interest
received. These are cash-back proxies, not full borrower cash or return proof.

The KKR/Accordia comparison has now produced a bounded proceeds-column upgrade:
the [matched-disposal coordinate extraction](capital-flow-kkr-global-atlantic-accordia-matched-disposal-coordinate-extraction-pass-1.md)
captures three same-CUSIP statutory disposal rows with `1.552579M USD` of
consideration. The result remains a proceeds-column proxy, not settlement cash,
remittance, liability-adjusted return, or parent residual.

The promotion test remains strict:

`legal entity -> named asset/CUSIP -> income or proceeds -> liability cost -> remittance/waterfall -> bounded return`

The [insurance lane verifier](../../scripts/verify-insurance-statutory-expansion-lane.py)
checks the route rows and prevents the statutory rows from being promoted past
their documented boundary.

## Third lane already underway: asset-backed collateral and borrowing base

The third lane is grounded in the [United Rentals collateral proof
chase](capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md).
URI has dated ABL availability, a closing certificate-existence condition, an
ABL borrowing-base formula, AR collateral-pool coverage, fleet asset scale,
and cash-conversion proxies. It does not have a populated public certificate,
eligible-collateral schedule, NOLV appraisal, reserve schedule, or lifecycle
fleet return model.

The promotion test is:

`facility balance -> eligible collateral -> NOLV/reserves -> Combined Borrowing Base -> legal availability -> source-to-purchase use -> fleet cash/return`

The [asset-backed lane verifier](../../scripts/verify-asset-backed-expansion-lane.py)
checks the ten URI proof gates and preserves the certificate-grade hold.

All three lanes now share a field-level [QoE and financial-shenanigans
overlay](combined-investment-research-expansion-lane-qoe-overlay-2026-09-16.md).
It keeps recovery, statutory income, liquidity, collateral, and fleet-return
diagnostics separate from owner cash and does not calculate a cross-lane
manipulation score.

## Current execution checkpoint — 2026-09-17

| Queue | Current status | Current evidence | Next promotion document | Current boundary |
| --- | --- | --- | --- | --- |
| Q-11 FPL customer cash | `searched-negative; hold-with-strong-route-visible` | Category cost/activity, rate-class allocation mechanics, true-up route, and aggregate recovery formula | Non-confidential discovery response, supporting workpaper, or final true-up with a category allocation | No Distribution Inspection-specific billing determinant, collection ledger, or source-of-funds join |
| Q-12 insurance statutory named asset | `evidence-insufficient` | MF1 same-CUSIP holding/disposal row, public servicing-waterfall mechanics, and restricted report inventory | Permitted custodian/trustee or loan-periodic report joined to legal owner, receipt, liability cost, and remittance | Settlement, custody, borrower cash, liability-adjusted return, and parent residual remain unproved |
| Q-13 asset-backed collateral | `evidence-insufficient` | URI ABL capacity net of letters of credit plus AR capacity and agreement-level certificate cadence | Populated borrowing-base certificate with eligibility, NOLV, reserves, and source-to-purchase records | Legal availability is proxied, but certificate components, collateral eligibility, and lifecycle return remain undisclosed |

This checkpoint is a move-on control: it prevents repeating searched-negative
queries while preserving the exact document that could change a proof grade.
The [structured expansion promotion action register](data/combined-investment-research-expansion-promotion-action-register-2026-09-17.csv)
is the machine-readable version of this checkpoint.

## Common admission protocol

Every candidate enters the queue with the same minimum record:

1. Force and date: what changed, where, and why the candidate is exposed.
2. Control point: what the customer or counterparty pays for and why the
   workflow is difficult to replace.
3. Burden map: labor, inventory, property, regulation, funding, credit,
   liability, acquisition, and dilution burdens.
4. Primary packet: annual report, latest relevant quarters, results release,
   call or IR materials, source ledger, and material legal or regulatory
   documents.
5. QoE screen: accrual/cash conversion, receivables, inventory/payables,
   revenue timing, capitalized costs, recurring adjustments, related parties,
   stock compensation, and perimeter changes. Sloan-style and
   Beneish-style inputs are diagnostics only; no manipulation score is
   promoted without comparable fields.
6. Owner-cash denominator: reported cash, working-capital timing, maintenance
   and growth capital, financing, taxes, leases or policyholder claims,
   acquisitions, dilution, and legal-entity access.
7. Valuation and macro: Damodaran-style implied expectations plus a
   company-specific inflation, rate, liquidity, funding, and policy stress.
8. Falsifier: one dated filing or source observation that would weaken the
   mechanism or denominator.

## Stop rules

Do not promote a candidate merely because it has a large market, high growth,
high AUM, backlog, adjusted EBITDA, reported free cash flow, or attractive
headline multiple. Hold the lane when evidence stops at management narrative,
aggregate revenue, fair value without cash, collateral without eligibility,
income without legal-entity access, or proceeds without a settlement route.

The next cycle is successful when one lane produces a stronger public cash
bridge than the current pilots—not when more company names have been added.
The same `proven`, `qualified`, `partial`, and `unresolved` proof vocabulary
continues to govern the result.

## Breadth-control checkpoint — 2026-09-18

The company-expansion pass now covers distinct lanes from the annual-report
archive through D-471, including hybrid-cloud storage, African copper buildout,
chemicals restructuring, homebuilding, grocery retail media, clinical
replenishment, laboratory diagnostics, open-web advertising, eyewear,
small-business internet infrastructure, international connectivity, lodging
redevelopment, regional fiber, specialty clinical supply, office-edge hardware,
institutional workflow, sell-side ad tech, creator imaging, regulated nicotine,
mid-tier copper-gold mining, and physical cash logistics. This breadth pass is
not a ranking and does not close CA-06.

The next scan must skip a candidate when the current repository already carries a
company-specific or broader economic-model workbench. For example, Core & Main is
already represented by the waterworks/municipal-distribution workbench; Home Depot
would repeat the Lowe's home-improvement lane; and MRC Global has no standalone
current packet after its combination into DNOW. Missing packets and exact company
name matches are not evidence of a new lane. The next meaningful action is either
one of the three public-cash expansion queues above or a packet with a genuinely
new control point and denominator.

With D-471 now recorded, the company-expansion pass is paused for this cycle.
The next execution action is a source-backed upgrade in Q-11 FPL customer cash,
Q-12 insurance statutory named-asset income, or Q-13 asset-backed collateral.
The targeted FPL filing scan did not produce a normalized billing-determinant,
category-receipt, or source-of-funds join, so FPL remains
`searched-negative; hold-with-strong-route-visible`. Additional company packets
must not be added merely to increase the roster.

## Execution routing checkpoint — 2026-09-18

The Q-11 FPL route now has a public Form 6P cost-perimeter refresh but remains
searched-negative for category billing determinants and collected receipts.
Q-12 now has Accordia coordinate-extracted disposal rows and named settlement
request packets, while Athene/Concord receipt and liability-cost documents remain
controlled. Q-13 now has a live SEC filing-index recheck confirming facility
availability proxies but no populated borrowing-base certificate. The industrial
uptime move-on cohort also has Sterling acquisition-perimeter and WESCO/Fastenal
capex-burden refreshes, with their collection and maintenance-return joins still
open.

These routes are therefore held at their current proof grades. The next public
execution order is Q-03 Wheaton–Antamina return inputs, followed by CA-06/Q-04–Q-06
retail allocation evidence. No new company packet should be added until one of
those joinable objects changes the decision-relevant proof grade or a genuinely
new source package appears.

Structured version: [next-cycle candidate expansion CSV](data/combined-investment-research-next-cycle-candidate-expansion-2026-09-16.csv).
