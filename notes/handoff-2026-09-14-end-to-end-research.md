# End-to-end research handoff — 2026-09-14

Repository: `annual-report-research`

## Packet Inputs Used

- the current company packets and source ledgers for the healthcare, AI
  physical-capacity, financial-intermediation, recreation, and restaurant
  additions described below;
- the linked deep company dossiers, cohort comparisons, first-principles
  essays, scenario register, and cross-framework verifier; and
- the prior September 13 forensic cross-sector handoff and current repository
  navigation surfaces.

## Active objective

Build a source-grounded, cross-sector investment research archive from annual
reports, SEC filings, company IR materials, and earnings calls. Each priority
company should be read through macro/liquidity/durability, narrative-to-
numbers/reinvestment/valuation, and forensic earnings-quality lenses. The
output must explain real operating economics, cash conversion, capital burden,
incentives, valuation expectations, and filing-based thesis breakers.

The plain-language rule remains active: explain technical finance in everyday
words, define terms when they first matter, avoid analogies and clichés, and
show the causal chain from the filed fact to the investment conclusion.

### 2026-09-15 continuation update

The live reader now contains `443` catalog entries: `236` company studies,
`67` first-principles explanations, and `140` comparisons. The homepage now
shows four evidence-backed findings, including Cigna's payer-scale-versus-
claims-risk conclusion, and seven conceptual starting points, including the
healthcare payment and shareholder-cash essay.

The healthcare handoff now connects the first-principles healthcare page, the
Cigna and UnitedHealth dossiers, the payer comparison card, the cohort writing
map, and the healthcare lane audit. Cigna's dossier links directly to the
UnitedHealth dossier so the paired comparison can be checked from either
company page. The reader glossary now defines medical-cost trend, reserve
development, and required capital.

The consumer lane now includes a substantive TJX dossier and an off-price
comparison. TJX is the first roster-workbench company promoted into the deep
reader: its FY2026 and Q1 FY2027 source chain is used to test value discovery,
inventory turns, markdowns, shrink, leases, store capital, vendor funding,
buybacks, and per-share cash. A standalone call transcript remains absent.

The healthcare lane now also includes a substantive Astrana Health dossier and
a provider-network-versus-product-flow comparison. Astrana's annual and
quarterly packet includes a Q2 2026 transcript, but the local archive still
lacks a Q2 2026 10-Q; claims, reserves, subsidiary capital, and retained margin
remain explicit next-filing tests.

The local server now preserves query strings when redirecting legacy
`/site/viewer.html?file=...` links to the reader. The browser suite tests this
legacy route as well as the current article route. The browser-review link
audit now declares all legacy targets as required artifacts and passes with
zero missing coverage. The full insight-system verifier also passes.

The presentation layer now surfaces three additional conclusions from the
existing evidence base. The retail finding compares TJX, Target, and Walmart
on buying flexibility, vendor-funded margin, attached services, inventory, and
physical reinvestment. The healthcare reader cohort compares payer, hospital,
tools, and device economics through UnitedHealth, HCA, Thermo Fisher, Abbott,
and Intuitive Surgical. The occasion-demand cohort adds Signet's milestone and
ritual spending to the travel, home, and foodservice comparison. These are
reader links to existing source-backed analyses, not new claims beyond those
pages.

Williams-Sonoma is now promoted from packet evidence into a full reader dossier.
The page tests whether its design-led home and hosting relationship survives
inventory funding, tariffs, freight, fulfillment, attached services, buybacks,
and diluted-share claims. The new dossier is linked into the occasion-demand
cohort beside RH and Wayfair and preserves the missing-transcript boundary.

DoubleVerify is now promoted into a trust-and-verification dossier. It keeps
the standalone advertising-proof economics separate from the August 2026
Nielsen merger agreement and tests activation, measurement, supply-side
revenue, retention, platform dependence, adjusted earnings, cash, buybacks,
and independence. The trust-as-paid-product cohort now surfaces DoubleVerify
beside S&P Global, CME, Ecolab, and Veralto.

AptarGroup is now promoted into a packaging-interface dossier. It separates
qualified dosing, dispensing, closure, and drug-delivery economics from
commodity packaging throughput, and tests Pharma mix, core growth, customer
qualification, raw materials, plant utilization, capex, quality, and owner
cash. The packaging comparison and cohort map now link this interface case.

General Mills is now promoted into a staples-demand dossier. It tests whether
frequent household use becomes durable owner cash after value investment,
retailer power, trade spending, input costs, inventory timing, brand support,
pet and foodservice mix, and transformation charges. The affordability and
value-reinvestment comparison and consumer reader theme now surface the case.

The Campbell's Company is now promoted into a complementary pantry dossier.
It separates Meals & Beverages from Snacks and tests at-home cooking demand,
Rao's growth, retailer ordering, price and volume, tariffs, trade spending,
input costs, productivity, cash conversion, and the cost of repairing the
portfolio. The same affordability comparison now links both staple-food cases.

Colgate-Palmolive is now promoted into a habitual-use consumer dossier. It
tests whether oral care, personal care, home care, and Hill's pet nutrition
produce cleaner cash through repeat use, efficacy, category leadership, and
science-supported brands after advertising, innovation, retailer power,
private-label pressure, and portfolio impairments. The consumer reader and
cohort map now surface this contrast with the broader food-staples cases.

The AI reader now also has a single burden-carrier cohort spanning Quanta,
Digital Realty, Equinix, GE Vernova, KLA, and NVIDIA. It makes field labor,
data-center property, power equipment, process control, and architecture
comparable at the level of control point, capital required, backlog or demand
visibility, and cash after the burden.

### Previous presentation and coverage audit — 2026-09-14 checkpoint

The reader's current catalog contains 427 research pages: 222 company studies,
67 first-principles explanations, and 138 comparisons. All 222 company studies
and all 67 explanations currently expose the five core questions in the reader:
what the business does, how activity becomes cash, what can break the reported
earnings, what the current valuation requires, and what the next filing should
prove or disprove. Comparison pages are intentionally labeled by their actual
coverage; older comparisons do not get presented as if they contain the full
company-level treatment.

The local reader server prebuilds and then caches the 427-entry catalog for five
minutes. A repeated homepage load is therefore fast during normal browsing,
while `/api/catalog?refresh=1` or a server restart picks up newly added
research. The direct reader URL is `http://localhost:8765/`.
The library also avoids rendering all long opening excerpts when the result
set is broad; excerpts return when a search narrows the list, keeping the full
catalog readable without an oversized initial page.

A separate valuation-register audit found 224 source-linked scenario rows, with
the denominator and implied values checked by the verifier. Two deep company
pages remain outside a common row. They are not all the same: Annaly has a
specialized book-value/EAD screen and Affirm now has a specialized two-engine
credit/network screen. Neither should be forced into a common owner-cash
denominator. RH,
Wayfair, Starbucks, Option Care, DoorDash, Domino's, Planet Fitness, Booking,
Huron, Hyatt, Korn Ferry, and Uber now have cautious initial screens based on their
filing chains. See the
[valuation coverage audit](valuation-coverage-audit-2026-09-14.md).
This is a control on presentation and traceability, not a claim that every
company has the same evidence depth or that a scenario is a price target.

The new [payment and marketplace burden comparison](../analysis/cross-sector/payment-conversion-and-marketplace-burden-forensic-comparison-2026-09-15.md)
connects the latest Affirm, Uber, DoorDash, Booking, and Wayfair screens. It
keeps customer conversion, retained revenue, credit, labor, supplier,
inventory, fulfillment, acquisition, and dilution burdens separate.

The control-point synthesis now contains a dedicated architecture-versus-
complete-system-delivery section for Broadcom, Cisco, and Dell. It separates
design-layer cash, installed-network recurring cash, and financing-supported
system-delivery cash, with exact FY2025/FY2026 evidence and filing-based
falsifiers for customer concentration, Splunk/VMware integration, backlog,
financing receivables, debt, and dilution.

The company/cohort map and reader now also expose the dedicated security-control
comparison for CrowdStrike, Palo Alto Networks, Zscaler, and F5. That cohort
keeps trust, access policy, platform consolidation, cloud processing, systems
and services, acquisitions, SBC, and diluted owner cash separate.

The industrial-capacity lane now exposes the embedded-distribution cohort for
Fastenal, Grainger, Ferguson, Core & Main, and WESCO. Its comparison keeps
procurement density and replenishment control separate from inventory, branch
and service labor, receivables, acquisition cash, and customer timing.

The security cohort's valuation alignment is now explicit: CrowdStrike, Palo
Alto Networks, and Zscaler company pages carry the same dated scenario-register
inputs as the cohort and valuation audit, while F5 retains its existing screen.
The pages distinguish recorded equity value from live price data and keep
renewal, cloud-processing, acquisition, trust, SBC, and dilution tests open.

At the 2026-09-14 checkpoint, the source reconciliation covered 222 of 222 company studies. It found
532 linked local sources available in the checkout and five additional links
that resolve through the archive manifest. ASML and GE Vernova remain the two
explicit external-only company pages; they are not described as locally
reproducible. These are dossier-level link counts, not packet-depth scores:
many company pages with fewer direct local links still point to official
external filings and to packets whose ledgers contain the fuller source chain.

The reader therefore leads with the worked company studies and first-principles
essays, then uses the coverage filter and source trail to show where a
comparison is complete, qualified, or still partial. All 427 catalog entries
now have at least one honest coverage label; the high-level four-lane overview
is identified as an overview of business economics and open edges, rather than
being presented as a detailed cash or valuation study. The intended reading
path is now editorial: start with the plain-language argument, inspect the
causal chain and burden split, and only then open the filing evidence and
valuation screen.

## What changed in this continuation

### RH and Wayfair evidence boundary

The RH and Wayfair source ledgers now state directly that their packets and
ledgers are present in the current checkout, while the raw filing and IR
artifacts referenced by legacy absolute paths are not. Their column headings
now call those entries `Recorded legacy path`, and each ledger links to the
reproducibility note with official SEC recovery routes. This preserves source
identity without implying that the raw files can be opened locally.

### Nine formerly unregistered valuation cases

The restored RH and Wayfair filing chains now support cautious initial
owner-cash screens. RH's FY2025 OCF less PP&E was about `$252M`, or roughly
`$209M` after stock compensation; Wayfair's was `$464M`, or roughly `$129M`
after stock compensation. The screens charge housing, inventory, logistics,
leases, returns, and required growth capital rather than valuing adjusted
EBITDA alone.

DoorDash now has a separate marketplace screen: FY2025 OCF less PP&E before
the `$4.151B` Deliveroo acquisition was about `$2.174B`, or about `$1.123B`
after `$1.051B` of stock compensation. Its dated market value therefore
requires successful acquisition integration and continued growth after
provider, insurance, regulation, software, membership, advertising, and
dilution costs.

The same treatment now covers Starbucks and Option Care. Starbucks' FY2025
OCF less PP&E was about `$2.442B`, or `$2.124B` after stock compensation, while
its `$2.771B` dividend exceeded that adjusted residual. Option Care's FY2025
OCF less PP&E was about `$1.068B`, or `$999M` after stock compensation, while
its `$882M` repurchase program consumed almost all of that adjusted residual.
Domino's and Planet Fitness now add the franchise-platform cases. Domino's
FY2025 SBC-adjusted residual was about `$627M`, while dividends and buybacks
were about `$595M`; Planet Fitness' comparable residual was about `$241M`,
while repurchases were about `$500M` against approximately `$2.482B` of debt.
The screens therefore keep franchisee health, parent support, leverage, and
capital returns visible rather than treating either business as a pure royalty
stream.
Booking and Huron now complete the travel-distribution and professional-
services screens. Booking's FY2025 cash after PP&E and SBC was about `$8.474B`,
but `$7.688B` of dividends and buybacks absorbed most of it while debt reached
about `$18.736B`. Huron's FY2025 cash after PP&E, acquisitions, and SBC was
only about `$25M`, and first-half 2026 operating cash was negative despite
adjusted EBITDA. Their valuation screens therefore carry very different
burdens: Booking needs durable retained contribution per booking; Huron needs
working-capital normalization and acquisition-independent cash.
These are not interchangeable screens: Starbucks is a repair-phase
company-operated network with leases and debt; Option Care is a specialty-care
workflow exposed to drug mix, payer timing, inventory, clinical labor, quality,
and acquisition requirements. The register now contains 216 validated rows,
and the [valuation coverage audit](valuation-coverage-audit-2026-09-14.md)
tracked the remaining ten exceptions at that earlier checkpoint.

### Professional-services cohort refresh

The [institutional adaptation comparison](../analysis/cross-sector/institutional-adaptation-and-capability-outsourcing-comparison-2026-08-11.md)
now adds a current Korn Ferry forensic checkpoint beside Huron. It separates
remaining fees from cash, distinguishes Executive Search, Interim, RPO, and
consulting mix, and compares Korn Ferry's FY2025 `$209.5M` SBC-adjusted
residual with Huron's first-half 2026 negative operating cash despite positive
adjusted EBITDA. The cohort now makes delivery labor, utilization, collections,
acquisition integration, and dilution visible as separate tests.

The same cohort now has a valuation-expectation table for CACI, Leidos, KBR,
AECOM, Gartner, and Korn Ferry. It separates funded-backlog conversion,
receivables, project estimates, pass-through revenue, contract value,
retention, compensation, acquisitions, debt, and diluted cash instead of
treating institutional demand as automatically high-quality earnings.

The software-control comparison now adds registered expectation screens for
Adobe, ServiceNow, Snowflake, and Cloudflare. It keeps subscription renewal,
consumption volatility, cloud/GPU cost, network cost, stock compensation,
deferred commissions, and dilution separate instead of treating recurring
revenue as one common cash denominator.

### Public-asset-manager valuation refresh

The financial-intermediation synthesis now compares the registered valuation
screens for BlackRock, T. Rowe Price, Invesco, and Franklin. It keeps AUM,
flows, fee rates, acquisitions, compensation, product concentration, and
per-share cash separate, then states what each current market value requires.
BlackRock requires newer platform layers to earn back acquisition spending; T.
Rowe Price requires flow repair; Invesco requires durable ETF and QQQ economics;
Franklin requires product migration and Western Asset repair. The comparison is
an expectation test, not a price-target ranking.

### Reader navigation — 2026-09-14 checkpoint

The local reader now exposes direct cohort cards for all four qualified lanes:
healthcare and aging, recreation and occasion demand, AI physical capacity, and
financial intermediation/property. The recreation card routes to the latest
available cohort comparison and links RH, Wayfair, Darden, CAVA, Marriott, and
Booking, so the lane is not represented only by its status summary.

The landing page then put three evidence-backed findings immediately below the
opening statement, before the theme directory. This lets a reader encounter a
concrete conclusion first and then choose the sector or company path behind it.
The finding cards retain the company dossier link, the period, the supporting
fact, and the unresolved question so the presentation does not turn a finding
into an unsupported headline.

That reader pass also replaced early navigation shorthand with plain
language: valuation sections now explain that different businesses need
different cash measures, research-status cards use “working conclusion,” and
the broader page directory is called a company coverage index. The technical
terms remain defined inside the articles rather than being removed from the
underlying analysis.

The energy lane also closed a reconciliation gap in this handoff. The Exelon-
AEP comparison and both company dossiers now point to the registered utility
screens: Exelon uses approximately `$44.3B` of current equity value against
`$1.8B / $2.6B / $3.4B` risk-adjusted common-earnings cases, while AEP uses
approximately `$67.9B` against `$1.8B / $3.0B / $4.5B` cases. These are
rate-base and recovery screens, not ordinary post-capex owner-cash screens;
the open tests remain earned returns, load conversion, customer funding,
financing cost, and dilution.

### Raw-evidence governance refresh

The legacy-root evidence audit was refreshed after the archive expanded. It now
records `633` Markdown files containing the retired root, of which `628` are
raw-provenance references and `5` are explicit historical or non-raw notes.
The raw-evidence governance verifier and the full insight-system verifier both
pass against those current counts.

### Healthcare integration

[Healthcare, aging, and owner cash](../analysis/cross-sector/healthcare-aging-to-owner-cash-forensic-synthesis-2026-09-14.md)
now connects hospitals, chronic treatment, home care, diagnostics, procedure
tools, distribution, payers, and healthcare property. It separates repeated
need from economic capture and identifies where labor, reimbursement,
inventory, property, quality, and required capital land.

### AI and physical-capacity integration

[AI physical capacity to owner cash](../analysis/cross-sector/ai-physical-capacity-to-owner-cash-forensic-synthesis-2026-09-14.md)
now connects architecture, semiconductor process control, validation,
networking, security, power, cooling, data-center real estate, and field
deployment. It explicitly separates orders, RPO, backlog, ARR, delivery,
collection, utilization, replacement capital, guarantees, and common-owner
cash.

### Financial-intermediation integration

[Financial intermediation to common-owner cash](../analysis/cross-sector/financial-intermediation-to-owner-cash-forensic-synthesis-2026-09-14.md)
now separates banks, payments, exchanges, custody, asset managers, private
capital, brokers, insurers, hotel brands, property owners, and levered mortgage
vehicles. It keeps client assets, deposits, float, collateral, required capital,
and common-owner cash distinct.

Bank of America now supplies a three-year money-center-bank denominator: 2023
through 2025 revenue, net income, deposits, loans, CET1, tangible-common-equity
returns, charge-offs, allowance coverage, and provision expense are shown
together. The dossier treats the 2025 improvement as conditional on deposit
pricing, credit normalization, risk-weighted assets, and the capital required
to support further balance-sheet growth.

The financial-intermediation synthesis now extends that denominator comparison
across JPMorgan, Bank of America, and Citi. It keeps each bank's reported
revenue, earnings, credit-cost measure, return measure, and CET1 ratio together,
then separates scale, recovery from a low base, deposit repricing, capital
requirements, transformation cost, and market-sensitive income before drawing a
common-owner conclusion.

### Recreation and participation integration

The recreation cohort now includes deep dossiers for:

- [Booking Holdings](../analysis/deep-company-pages/booking-holdings-inc.md)
- [Hyatt](../analysis/deep-company-pages/hyatt-hotels-corporation.md)
- [Planet Fitness](../analysis/deep-company-pages/planet-fitness-inc.md)
- [Domino's](../analysis/deep-company-pages/dominos-pizza-inc.md)

[Recreation, lifestyle, and occasion demand](../analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md)
now covers travel distribution, branded lodging, marketplace travel,
affordable participation, direct restaurant operation, home identity, gifting,
ritual spending, and foodservice support.

The home-demand lane now also has a first-principles essay,
[Home demand: curation, logistics, and owner cash](../analysis/first-principles/home-demand-curation-logistics-and-owner-cash.md),
which separates RH, Williams-Sonoma, and Wayfair by customer problem, control
point, burden, lifecycle, and owner-cash denominator.

The restaurant lane now includes a deep [Starbucks dossier](../analysis/deep-company-pages/starbucks-corporation.md)
and a comparison update. Starbucks adds the mature routine-and-loyalty model,
including stored value, Rewards liabilities, mobile ordering, labor repair, and
company-operated versus licensed-store economics. It strengthens the restaurant
evidence; the later Darden dossier closes the separate mature full-service
operator role.

The healthcare lane now includes a deep [DaVita dossier](../analysis/deep-company-pages/davita-inc.md),
which converts mandatory chronic treatment into a treatment-volume,
reimbursement, labor, facility, home-dialysis, risk-based medical-cost, and
maintenance-capital test.

It now also includes a deep [Addus dossier](../analysis/deep-company-pages/addus-homecare-corporation.md),
which separates aging-in-place demand from caregiver availability, delivered
hours, state and managed-care reimbursement, service quality, acquisitions, and
working-capital cash conversion.

The healthcare lane now includes [Option Care](../analysis/deep-company-pages/option-care-health-inc.md)
as the specialty-therapy and alternate-site workflow case. Its dossier
separates drug pass-through from retained service contribution and tests
authorization, nursing, pharmacy, inventory, receivables, quality, acquisitions,
and liquidity.

The healthcare lane now includes a deep [AdaptHealth dossier](../analysis/deep-company-pages/adapthealth-corp.md),
which separates home-equipment placement from recurring resupply and tests
referral access, payer authorization, capitated contracts, supplier pricing,
inventory, free cash flow, impairment, and replacement capital.

The healthcare lane now includes a deep [Brookdale dossier](../analysis/deep-company-pages/brookdale-senior-living-inc.md),
which turns aging demand into an occupancy, resident-fee, care-intensity,
community-labor, property-maintenance, lease, debt, and affordability test.

The healthcare property lane now includes a deep [Welltower dossier](../analysis/deep-company-pages/welltower-inc.md),
which separates senior-housing operating NOI from normalized FFO and tests
operator health, resident affordability, maintenance capital, acquisitions,
debt, dilution, and property-value risk.

The Darden and Welltower dossiers now include explicit September 14, 2026
market-expectation screens. Darden is tested against normalized adjusted EPS
after direct operating capital; Welltower is tested against normalized FFO and
the separate NAV/property-cash burden. Neither screen is presented as a price
target.

The financial-intermediation synthesis now contains a carrier comparison across
Chubb, Markel, MetLife, and Prudential. It separates P&C underwriting and
specialty float from life/retirement spread earnings and requires each model to
be tested after claims, reserves, reinsurance, asset-liability risk, and
required capital.

The recreation and restaurant lanes now include a deep [Darden dossier](../analysis/deep-company-pages/darden-restaurants-inc.md),
which supplies the mature full-service direct-operator case. It separates
traffic, price, menu mix, food, labor, occupancy, maintenance, new-unit,
acquisition, lease, debt, and buyback economics from consolidated adjusted EPS.

The hotel cohort is also now explicitly portable: the [Marriott versus Host
comparison](../analysis/cross-sector/hotel-relationship-control-versus-property-owner-cash-forensic-comparison-2026-09-13.md)
shows that Marriott's fee-platform residual and Host's property-owner residual
cannot share a denominator. Marriott's next claims are loyalty, technology,
guarantees, debt, and diluted shares; Host's are normalized renewal capital,
hotel labor and insurance, interest, refinancing, distributions, and REIT/OP
attribution. The comparison now includes a burden-adjusted table and a reader
workflow for moving from RevPAR to common-owner cash.

The procedure-medtech comparison now includes [HCA](../analysis/deep-company-pages/hca-healthcare-inc.md)
alongside [Intuitive Surgical](../analysis/deep-company-pages/intuitive-surgical-inc.md)
and [Stryker](../analysis/deep-company-pages/stryker-corporation.md). It makes
the pull-through distinction explicit: Intuitive must convert systems into
procedures, instruments, and service; Stryker must earn back acquisition and
integration capital; HCA must convert staffed procedures into collected
reimbursement after labor, maintenance capex, interest, and noncontrolling
interests.

The restaurant franchise comparison now has a common franchisee-health matrix
for RBI, YUM, and Wingstop. It separates system sales and digital activity from
the operator's after-labor, food, rent, remodel, financing, and tax return, and
ties parent distributions and debt to the support burden that may sit outside
the consolidated income statement.

The backlog synthesis now has a direct WESCO/Vertiv/Comfort Systems burden
comparison. It distinguishes distributor cash absorbed by receivables and
inventory, equipment cash before acquisition and capacity returns, and
contractor cash supported by customer billings. It also adds the related
management-incentive test for backlog, adjusted EBITDA, SBC, buybacks,
acquisitions, debt, and diluted owner cash.

The Chubb carrier dossier now includes the explicit September 2026 valuation
screen already represented in the scenario register. The denominator is
risk-adjusted common earnings after underwriting, reserve, catastrophe,
investment, life, and required-capital tests; insurance operating cash flow is
not treated as distributable owner cash.

The financial-intermediation synthesis now includes a common carrier
capital-release scorecard for Chubb, Markel, MetLife, and Prudential. It makes
the differences in underwriting, float, life/retirement spread, reserve,
reinsurance, subsidiary-capital, and holding-company-liquidity burdens
explicit before comparing capital returns. The new expectation table carries
Chubb at approximately `$130.5B`, Markel at `$22.3B`, MetLife at `$61.7B`, and
Prudential at `$42.7B` of equity value against their registered risk-adjusted
earnings cases; none is presented as industrial free cash flow or a price
target.

The healthcare-distribution peer synthesis now includes three-year residual
paths and a per-share capital-allocation scorecard for McKesson, Cencora, and
Cardinal. It prevents the latest-year residual from being read without
payable timing, acquisition cadence, legal cash, debt, SBC, and dilution.

The healthcare-aging synthesis now includes a common six-layer bridge using
HCA, Addus, Intuitive Surgical, McKesson, UnitedHealth, and Welltower. Each
company is kept on its proper denominator while the analysis tracks the same
sequence: activity, collected payment, labor or product burden, working
capital, maintenance/growth capital, required claims, and diluted owner cash.

It now adds a senior-housing cohort bridge for Brookdale, Welltower, and
Ventas. Brookdale is kept as the direct community operator; Welltower and
Ventas are kept as property and operating platforms. The comparison records
occupancy/RevPAR or NOI, normalized FFO, operator and labor claims, recurring
property capital, investment volume, debt, equity issuance, and per-share
falsifiers without treating demographic demand as common-owner cash.

Brookdale now also has a filed FY2023–FY2025 cash bridge: operating cash flow,
capital expenditures, asset acquisitions, and the residual after those listed
uses. The FY2025 operating-cash improvement is explicitly kept separate from
the continuing-operations loss and from adjusted EBITDA, while the remaining
work is maintenance-versus-development capital, lease-adjusted community cash,
and acquisition returns.

The Brookdale dossier now also includes a September 14, 2026 reverse-valuation
screen. Its market value is compared with FY2025 cash after capex before
acquisitions, showing why the recovery must become self-funded cash rather than
remaining an occupancy and adjusted-EBITDA narrative.

That Brookdale screen is now also in the deep-dossier scenario register, which
the verifier reports at `190` rows. The memo and register use the same bear,
base, and bull cash assumptions and implied values.

Wingstop's dossier now has an explicit sources and reproducibility section
linking the official FY2025 10-K, annual report, source ledger, company packet,
and the Q1/Q2 2026 filing and IR boundary. This closes a traceability gap in a
priority restaurant comparison without changing the underlying conclusion that
franchisee cash health remains unresolved.

The AI physical-capacity synthesis now includes a common capacity-to-cash bridge
across architecture, process control, validation, network/security,
power/thermal equipment, powered real estate, and field deployment. It keeps
the denominators separate while recording the capital, commitment, customer-
concentration, acquisition, SBC, and dilution claims that sit between demand
and common-owner cash.

It now also includes a commitment-perimeter screen for NVIDIA, Vertiv, Equinix,
and Quanta. The screen puts receivables, inventory, AI-cloud guarantees,
backlog, acquisitions, total versus recurring property capex, debt, RPO,
retainage, labor, and contract claims beside reported operating cash. The
falsifier is an expanding gap between demand visibility and collected cash
after the capital and obligations required to fulfill the work.

The financial-intermediation synthesis now includes a cross-model
liability-and-capital bridge for banks, cards, exchanges, custody, asset
managers, brokers, carriers, property, and mortgage vehicles. It keeps client
assets, deposits, collateral, float, policyholder liabilities, property, and
common-owner cash separate before the remaining within-model return work.

The recreation synthesis now includes a common unit and relationship cash bridge
for CAVA, Darden, RBI/YUM/Wingstop, Marriott, and Host. It makes the direct
operator, franchise platform, hotel fee platform, and property-owner
denominators explicit, including food, labor, franchisee health, loyalty,
renewal capex, debt, support, and dilution claims.

The recreation comparison now adds an expectation screen across Marriott,
Booking, Darden, Domino's, CAVA, Planet Fitness, RH, and Wayfair. It keeps
hotel-fee cash, travel contribution, direct-store cash, franchise residuals,
and home-platform residuals separate, and states the evidence each base case
requires. The ranges are explicitly scenario inputs rather than a ranking or
price target.

The archive-level “Who keeps the cash?” synthesis now refreshes its valuation
discipline table with current examples from the newer work: NVIDIA, State
Street, Exelon, Brookdale, and CAVA. This makes the cross-sector rule
inspectable: architecture cash, custody fees, regulated common earnings,
operator cash, and growth-restaurant cash each require different claims and
different future proof.

The financial-intermediation synthesis now adds a bank valuation-expectation
screen for M&T, Regions, WaFd, Truist, U.S. Bancorp, and PNC. It uses
risk-adjusted common earnings rather than industrial free cash flow and keeps
deposit pricing, credit, liquidity, CET1 retention, merger cleanup, technology,
and dilution inside the expectation test.

The backlog-conversion synthesis now adds the same expectation test for WESCO,
Vertiv, Comfort Systems, Quanta, EMCOR, MasTec, and Sterling. It shows why
backlog cannot be valued apart from receivables, inventory, labor, project
estimates, acquisitions, contract liabilities, debt, and dilution; WESCO's
near-zero normalized cash case and Vertiv's high-growth burden make the
contrast explicit.

The restaurant comparison now adds a direct-operator burden bridge for CAVA,
Chipotle, Darden, and McDonald's: operating cash flow is shown after listed
property and equipment spending and acquisition cash, with the fiscal-period
mismatch and remaining lease, maintenance, franchisee-health, SBC, and support
claims stated directly. Starbucks remains a repair case rather than being
forced into the same residual table because its current evidence is dominated
by labor, service, and store-reset investment.

The CECO Environmental dossier was upgraded as a plain-language teaching case
for project-industrial earnings quality. It now separates orders, backlog,
revenue/profit, and owner cash; explains why those measures can diverge; and
walks a new reader through receivables, inventory, contract assets, PP&E,
adjusted-FCF exclusions, acquisition returns, and dilution before accepting the
data-center, reshoring, and Thermon growth narrative.

The Wheaton dossier now exposes the deeper Antamina proof stack that had
previously remained in company-first-principles work files. It connects the
$4.300B named PMPA payment to H1 2026 stream revenue, cash cost, depletion,
profit, operating cash flow, contract entitlement, production evidence, and
post-transaction debt. It also preserves the boundary: delivered-ounce cash
receipts, Antamina-specific tax and interest, lender waterfall, reserve-backed
delivery curve, IRR, and NPV remain unproven.

The Applied Industrial Technologies dossier now makes the industrial-
distribution incentive test explicit. It separates management FCF from the
post-acquisition residual, tests buybacks against SBC and diluted ownership,
and links the company to the industrial procurement first-principles essay and
the broader distribution comparison. The conclusion remains conditional on
acquisition-cohort cash returns, inventory and receivable discipline, and
whether technical service gross profit pays for its added labor and capital.

The Westlake dossier now adds an explicit lifecycle and incentive test for the
chemical/materials cohort. It requires the $600M PEM improvement plan to show
durable unit-cost, utilization, fixed-cost, or capital benefits after shutdown,
environmental, stranded-overhead, and customer-service costs. It also links
Westlake's HIP/PEM split to the chemical-spread comparison and the commodity
owner-cash first-principles essay.

The Celanese dossier now makes the leveraged specialty-materials recovery test
explicit. It separates adjusted EPS/EBITDA and management FCF from cumulative
cash after restructuring, working capital, interest, dividends, debt repayment,
and portfolio renewal. It treats refinancing as a liquidity improvement rather
than automatic value creation and links Celanese to the chemical lifecycle
cohort.

The Veralto dossier now adds a full-cost test to its recurring measurement and
water-quality thesis. It explains why low PP&E is an advantage but not zero
reinvestment, and compares Veralto's measurement proof, Ecolab's site service,
and CECO's engineered systems by the cash required to maintain each control
point. The current conclusion is cleaner reported conversion, but not proven
superior long-term return until organic growth, acquisitions, R&D, and support
cost are charged together.

The Kinross dossier now adds the focused gold-miner lifecycle test. It treats
buybacks and dividends as claims that must be covered after sustaining capital,
reclamation, taxes, debt service, and reserve replacement, and it separates the
Great Bear, Curlew, Phase X, Redbird, and Lobo-Marte projects as investments
requiring their own returns. Kinross is now explicitly linked to the diversified
mining cohort and the commodity-renewal first-principles essay.

The NRG dossier now makes the customer-backed-generation test explicit. It
separates customer announcements from funded and energized load, FCF before
growth from post-LS Power common cash, and retail scale from weather-normalized
margin. BYOP is now framed as a contract and financing question requiring
credit support, take-or-pay terms, construction contributions, interconnection,
cancellation, and collection evidence.

The Alliant dossier now provides the regulated counterpoint in the power cohort.
It treats rate-base growth, contracted load, approved capital, earnings, and
dividend continuity as separate outcomes, then tests them through regulatory
lag, customer contributions, affordability, debt/equity funding, disallowance,
and cancellation risk. Alliant's cleaner revenue visibility is now explicitly
set against NRG's retail/merchant customer-and-generation model.

The power-demand synthesis now contains an initial eight-company filing bridge
across NextEra, ONEOK, Vertiv, Equinix, MasTec, Sterling, Comfort Systems, and
EMCOR. It keeps the periods and residual definitions explicit: NextEra's
capital deficit, ONEOK's post-capex residual, Vertiv's acquisition-adjusted
screen, Equinix's recurring-capex versus total-capex split, and the contractors'
backlog, contract-asset, acquisition, and collected-cash tests are not collapsed
into one free-cash-flow ranking. The next step is within-model normalization and
current valuation, financing, dilution, and maintenance-capital testing.

The RH and Wayfair recreation evidence chain was also repaired further. Eleven
SEC annual, continuity-quarter, and latest-quarter filings or wrappers are now
stored under the documented local `raw/sec/...` paths with SHA-256 records in
`notes/rh-wayfair-restored-artifacts-2026-09-14.tsv`. The source ledgers point
to those local files. Earnings exhibits, IR PDFs, and call transcripts remain
explicitly qualified rather than being represented as locally verified.

The Vistra dossier now completes the merchant-fleet counterpoint. It makes the
adjusted-FCF and hedge tests explicit: hedge percentages must be reconciled to
settlement cash, collateral, output, and fleet cost, while capital returns must
be covered after nuclear fuel, service agreements, acquisitions, debt, and
retirement obligations. Vistra is now directly positioned against Alliant, NRG,
and Constellation by burden and control point.

The Motorola Solutions dossier now includes the Q2 2026 quality checkpoint:
record sales, operating cash flow, software/services growth, and backlog are
balanced against the $60M IEEPA tariff-refund benefit and the Q1 Silvus earnout.
The dossier now explicitly separates policy recovery and acquisition accounting
from recurring margin, and links the company to the mission-critical workflow
and software/process-control first-principles cohorts.

The EOG Resources dossier now adds the upstream depletion and capital-return
test. Its 70% return policy is evaluated through cash per diluted share,
production and reserves per share, stock compensation, impairments, and the
capital required to replace depleted acreage. EOG is explicitly positioned
against integrated energy, royalty/streaming, and contracted-infrastructure
models rather than treated as generic energy exposure.

The Rio Tinto dossier now adds the diversified-miner portfolio-allocation test.
It treats Arcadium, copper/lithium growth, Pilbara renewal, partner funding,
rehabilitation, debt, and dividends as competing claims on cash, and requires
project returns to be tested against final capital, ramp, output, and cash.
Rio is explicitly positioned against Kinross, Newmont, Wheaton, and
Franco-Nevada by physical control and burden.

The Newmont dossier now adds the large gold-major portfolio-renewal test. It
separates debt reduction and divestiture proceeds from operating improvement,
charges the $6.8B asset-retirement obligation to the mine lifecycle, and tests
buybacks and projects against cash per diluted share after sustaining capital,
reclamation, taxes, debt service, and renewal funding.

The Freeport-McMoRan dossier now adds the focused copper scarcity test. It
charges Grasberg restart capital, sustaining and growth spending, environmental
obligations, debt, minority interests, and operating-rights risk to the
shareholder denominator, and tests whether byproduct credits make copper cost
metrics look stronger than a conservative full-cycle return. Freeport is now
explicitly positioned against Rio, Newmont, Kinross, and Wheaton.

The Mosaic dossier now adds the agricultural-input conversion test. It treats
inventory, sulfur/ammonia/energy costs, curtailments, Brazil working capital,
sustaining and environmental capital, and restart costs as part of the cash
denominator. Mosaic is explicitly compared with CF Industries, Nutrien, and
FMC by product, input, distribution, and capital burden.

The S&P Global dossier now includes the Q2 2026 quality checkpoint: revenue,
adjusted EPS, and margin improved, but the analysis requires separation of
ratings issuance, recurring subscriptions, index fees, acquisitions,
restructuring, technology investment, NCI, SBC, and debt. S&P is now linked to
the standards/ratings/clearing comparison and software-process-control
first-principles cohort.

The Gallagher dossier now makes the broker-roll-up return test explicit. It
requires AssuredPartners and future acquisition cohorts to prove client and
producer retention, organic growth after anniversary, compensation-adjusted
margin, earnout cash, working capital, debt reduction, and cash return on
purchase price. Gallagher is explicitly positioned against Aon, Marsh, Chubb,
and Markel by relationship control and balance-sheet burden.

## Current research standard

Every deep dossier should answer, in order:

1. What does the customer actually buy?
2. What relationship or bottleneck does the company control?
3. Which party performs the labor or funds the physical system?
4. What is the correct operating denominator?
5. How does the preferred management metric reconcile to GAAP and cash?
6. What working-capital, liability, acquisition, SBC, debt, or dilution claim
   sits ahead of common owners?
7. What does the macro and liquidity environment do to durability?
8. What reinvestment must earn a return for growth to create value?
9. What valuation expectation is already embedded in the price, where a
   defensible market snapshot exists?
10. What exact future filing would confirm or break the thesis?

The cohort page must then identify at least three concrete companies and state
which economics repeat and which remain company-specific.

## Evidence status

The archive currently has:

- `238` company pages covered by the cross-framework verifier;
- `221` scenario-register rows with source links and implied values checked;
- company packets and source ledgers for the new Booking, Hyatt, Planet
  Fitness, and Domino's dossiers;
- cohort comparisons for healthcare, AI physical capacity, financial
  intermediation, recreation, restaurants, industrial infrastructure,
  materials, utilities, and technology control points; and
- first-principles essays that explain the major recurring business mechanics.

The counts prove structural coverage, not that every page is equally deep or
that every company has a current-quarter valuation row. The valuation coverage
audit records the 14 exceptions and their next tests. Where a clean market
snapshot or comparable cash bridge is absent, the dossier must say so rather
than invent precision.

## Qualified conclusions currently supported

- Durable demand and durable owner cash are separate questions. Healthcare,
  travel, AI infrastructure, and financial intermediation all show this.
- The cleanest economics often occur where the company controls a repeated,
  qualified, or trusted workflow while another party funds more of the labor or
  physical asset burden.
- Burden transfer is not burden elimination. Franchisees, hotel owners,
  hospitals, caregivers, cloud operators, suppliers, and policyholders can
  carry costs that eventually return to the platform through weaker retention,
  support needs, guarantees, or regulation.
- Revenue, gross bookings, AUM, backlog, RPO, members, room count, treatments,
  and orders are activity measures. They become investment evidence only after
  the cash, liability, reinvestment, and diluted-share bridges are shown.
- Adjusted EBITDA, adjusted EPS, FRE, ANI, FFO, and distributable earnings are
  useful views, not universal owner-cash measures. Each must be reconciled to
  the burdens it excludes.
- A high-quality business can still be a poor investment when its current price
  requires years of peak margin, growth, or low-cost liquidity.

The current lane-by-lane completion assessment is in [Lane completion audit](lane-completion-audit-2026-09-14.md).
It labels healthcare, recreation, AI physical capacity, and financial
intermediation/property as qualified rather than implying that every company
page has equal depth.

The RH and Wayfair evidence chains have a separate [reproducibility gap note](reproducibility-gap-rh-wayfair-2026-09-14.md): their packets preserve source identity and facts, but the cited raw artifacts are not currently recoverable through the local checkout or offload manifest.
The gap note now also preserves direct official SEC and IR fallback routes, so
the claims are externally recoverable even though local checksums and raw-file
resolution remain incomplete.

The reader presentation was tightened after a reproducibility and readability
pass. None of the 221 deep company pages contains an inherited sibling-
worktree path; their absolute links resolve to the current checkout. Inherited
paths remain in 1,191 extracted packet/profile/ledger files, where the RH and
Wayfair note keeps the distinction between a recorded source identity and a
locally recoverable artifact visible. Article pages now show an at-a-glance
block for article type, reading time, reporting period, evidence location, and
the questions addressed. The language is intentionally written for a reader,
not for the internal audit process. The mobile header now keeps the navigation
usable as a horizontal row instead of allowing later links to clip. The
reader browser check was updated to assert the new language and passed on
desktop and 390px mobile layouts, including article, comparison, source-boundary,
filter, search-restore, and empty-state checks.
The reader data layer also now labels dates by what they actually mean: a
research date, an "as of" date, or a reporting period. This prevents a research
date in the opening evidence note from being presented as an absent reporting
period. Pages with no explicit date now say "Not stated" rather than repeating
the phrase "Date not stated" as both a label and a value; no date is inferred.
The library filter was also rewritten as "Pages addressing all five questions"
and result metadata now says simply "of 5 questions." It describes what the
filter checks without implying that a page is complete or that the analysis is
final.

## Remaining high-value work

The project is not complete. The next work should remain substantive:

1. Audit the weakest priority company pages against the current dossier
   standard and upgrade the most important qualified pages, not every page
   mechanically.
   The UnitedHealth page now includes an explicit Q2 2026 repair checkpoint,
   while preserving the distinction between reported improvement and proved
   claims, reserve, Optum-cash, and regulated-capital durability.
2. Add current market-expectation and denominator-specific valuation rows for
   the newest dossiers when reliable evidence is available; retain explicit
   exclusions when it is not.
   Arista now displays its existing scenario-register valuation screen directly
   in the company memo, including the cash denominator, market snapshot, and
   assumptions required for the bull case.
   Chipotle now does the same for the direct-operator restaurant case, with
   explicit traffic, margin, unit-payback, lease, and buyback assumptions.
   Intuitive Surgical now exposes its existing scenario-register screen and
   states the expectation burden created by its procedure, instrument,
   platform-transition, inventory, and SBC assumptions.
   CAVA now exposes its growth-stage restaurant screen, making the gap between
   current cash after PP&E and the owner cash required by the market visible.
   Stryker now exposes the mature medtech peer screen, making acquisition
   return, amortization, debt, dilution, and organic procedure assumptions
   visible beside Intuitive Surgical.
   KLA now exposes the process-control screen, separating installed-base
   service durability from product-cycle, export-control, R&D, SBC, and
   customer-capex assumptions.
   The restaurant cohort now has a cross-model valuation table covering CAVA,
   Chipotle, Darden, RBI, YUM, and Wingstop, while preserving the different
   direct-operator and franchise-platform denominators.
   The healthcare synthesis now adds a layer-specific valuation screen for
   Intuitive, Stryker, McKesson, Cencora, and Cardinal, while explicitly
   excluding payer and property models from the same ranking.
   The AI physical-capacity synthesis now adds representative valuation screens
   for architecture, process control, network/security, power, powered real
   estate, and field deployment, with each denominator kept distinct.
   The financial-intermediation synthesis now adds representative valuation
   expectations for banks, cards, exchanges, brokers, carriers, hotel brands,
   and alternative-capital platforms without treating their cash measures as
   interchangeable.
   Annaly now adds the missing mortgage-REIT expectation screen: current price
   versus book value, annualized EAD, and separate bear/base/bull book-value and
   EAD cases, with repo, hedge, leverage, and dilution conditions stated.
   Host Hotels now adds the property-owner counterpart: normalized cash after
   recurring capex and planned investment, with RevPAR, labor, insurance,
   refinancing, renovation, and asset-sale conditions attached to each case.
   Its screen is also registered in the deep-dossier scenario file, which now
   contains 191 validated rows.
   HCA now adds the provider counterpart to the register, reducing
   consolidated operating cash for PP&E, acquisitions, and noncontrolling-
   interest distributions before applying the common-owner valuation cases.
   Addus now adds the labor-intensive home-care counterpart with a qualified
   three-quarter cash window and explicit fill-rate, reimbursement, wage,
   acquisition, and dilution conditions. The register now contains 193
   validated rows. DaVita now adds the chronic-treatment counterpart with a
   qualified Q4 2025–Q2 2026 cash window, keeping risk-based medical spend and
   treatment-capital requirements outside revenue and owner cash. The register
   now contains 194 validated rows. AdaptHealth now adds the equipment-and-
   resupply counterpart, explicitly contrasting FY2025 free cash flow with
   negative 2026 free cash flow during capitated rollout and portfolio reset.
   The register now contains 195 validated rows.
   Gallagher’s broker-rollup screen is now also registered, preserving its
   negative acquisition-year residual and separating normalized post-
   AssuredPartners cash from organic fee economics. The register now contains
   196 validated rows. Markel’s carrier screen is now also registered as an
   insurance-capital case rather than an owner-cash multiple, with underwriting,
   reserves, catastrophe, reinsurance, subsidiary surplus, and operating-
   company claims kept ahead of common value. The register now contains 197
   validated rows. Prudential’s liability-backed insurance screen is now
   registered separately, preserving policyholder guarantees, reserve and
   assumption risk, investment spread, PGIM flows, subsidiary capital, parent
   liquidity, and dilution. The register now contains 198 validated rows.
   American Express’s closed-loop card screen is now registered separately from
   deposit-funded banks, preserving rewards, receivables funding, charge-offs,
   reserves, marketing, regulatory capital, and buyback claims. The register
   now contains 199 validated rows. State Street’s institutional-servicing
   screen is now registered separately from asset managers and banks, keeping
   AUC/A and AUM as scale measures rather than owner cash. The register now
   contains 200 validated rows. The existing Ares alternative-capital screen
   was rechecked and its distinction between company-only cash after listed
   uses and FRE remains explicit, along with compensation, performance,
   insurance, credit, partner, debt, liquidity, and dilution claims.
   M&T Bank’s regional-bank screen is now registered separately, keeping
   relationship deposits and net interest margin distinct from deposit
   repricing, commercial and real-estate credit losses, securities marks, CET1,
   stress capital, and dilution. The register now contains 201 validated rows.
   Apple’s qualified integrated-device and Services screen is now registered
   separately from pure software or semiconductor cases. The Q1-Q3 FY2026
   evidence window is kept distinct from a full-year measure, with device mix,
   Services take rate, R&D, tariffs, China, regulation, buybacks, cash, debt,
   and diluted shares kept visible. The register now contains 202 validated
   rows.
   Welltower’s healthcare-property screen is now registered separately from
   direct care and healthcare distribution. Annualized Q2 FY2026 normalized FFO
   remains an operating denominator rather than owner cash; recurring property
   capital, operator support, acquisitions, debt, cap rates, preferred claims,
   and dilution remain explicit. The register now contains 203 validated rows.
   AGNC’s mortgage-REIT screen is now registered separately from Annaly, using
   tangible book value converted through approximately 1.162B shares and
   0.80x/1.00x/1.10x book-value cases. Repo funding, hedge duration, mortgage
   spreads, prepayments, leverage, dividend coverage, and dilution remain
   explicit. The register now contains 204 validated rows.
   Regions Financial’s Southeast regional-bank screen is now registered
   separately from M&T, keeping low-cost deposits, treasury and wealth fees,
   deposit repricing, Southeast credit, securities duration, reserve coverage,
   CET1, liquidity, payout, and dilution visible. The register now contains 205
   validated rows.
   Brookfield’s alternative-capital screen is now registered separately from
   Ares and the other fee platforms, keeping recurring distributable earnings
   before realizations distinct from insurance spread, operating-asset cash,
   partner/NCI claims, taxes, debt, liquidity, parent costs, and reinvestment.
   The register now contains 206 validated rows.
   Invesco’s public-asset-manager screen is now registered separately from
   alternative-capital platforms and custody banks, keeping fee-paying AUM and
   product-level flows distinct from headline AUM. QQQ concentration, fee
   compression, active outflows, compensation, distribution, technology, China,
   private-market marks, impairment, buybacks, and dilution remain explicit.
   The register now contains 207 validated rows.
   Franklin Resources’ transition screen is now registered separately from
   Invesco’s ETF and QQQ case, keeping recent inflows distinct from fee-paying
   breadth, legacy active outflows, Western Asset repair, alternatives costs,
   impairment, technology, capital returns, and dilution. The register now
   contains 208 validated rows.
   Carlyle’s component-valued alternative-manager screen is now registered
   separately, giving FRE a higher durability test while keeping realized carry,
   marks, credit, partner and employee claims, taxes, debt, liquidity, and
   dilution outside recurring fee value until supported. The register now
   contains 209 validated rows.
   Loews’ permanent-capital conglomerate screen is now registered separately,
   keeping consolidated earnings distinct from CNA reserves and capital,
   Boardwalk maintenance and debt, hotel and packaging reinvestment, parent
   liquidity, cash remittance, taxes, minority claims, holding-company discount,
   and repurchases. The register now contains 210 validated rows.
   WaFd’s thrift-to-business-bank transition screen is now registered separately,
   keeping transaction deposits, treasury attachment, NIM, new-loan profitability,
   legacy mortgage and CRE losses, transition costs, liquidity, CET1, buybacks,
   and dilution visible. The register now contains 211 validated rows.
   Upstart’s qualified AI-led lending screen is now registered separately from
   merchant-linked credit, keeping loan originations distinct from partner
   funding, product contribution, cohort losses, model and compliance cost,
   working capital, retained exposure, GAAP-to-cash conversion, and dilution.
   The register now contains 212 validated rows.
   A content audit also made the cash bridges explicit in the Prudential and
   Ventas dossiers. Prudential now names the path from adjusted income through
   policyholder claims, reserve changes, subsidiary capital, parent remittances,
   and common distributions. Ventas now names the path from rent and SHOP cash
   through renewal capital, debt, acquisitions, equity issuance, dilution, and
   the common-owner residual. These are bridge clarifications, not new valuation
   assumptions.
   A forensic-label audit then standardized the existing accounting-risk
   sections in PepsiCo, Korn Ferry, Powell Industries, Airbnb, and GE Vernova.
   Each page now names its forensic earnings-quality or financial-engineering
   section directly; the underlying tests and conclusions were already present.
   The thin-source-trail audit then added direct packet, ledger, company-profile,
   and primary-filing routes to the US Foods and Ventas dossiers. Their reader
   source summaries now expose three locally available links each rather than
   requiring the reader to infer the evidence route from one packet link.
   A second source-route pass added packet, profile, and ledger links to
   Cloudflare, Fortis, Intel, MetLife, ServiceNow, and Snowflake. The live
   reconciliation now covers 584 available local links across the 222 company
   studies; the remaining external-only pages are ASML and GE Vernova.
   The next visible cohort pass added local profile or packet/ledger routes for
   AEP, American Express, Aon, BlackRock, CAVA, Comfort Systems, EMCOR, Exelon,
   Host Hotels, McKesson, Quanta, and Stryker. The remaining below-three-link
   pages are now concentrated in less visible or route-depth cases rather than
   the principal reader cohort.
   A live reader-visible audit confirms that every company directly surfaced by
   the themes, findings, cohort cards, or research-state cards has at least
   three local evidence links except ASML and GE Vernova, which remain marked
   external-only.
   The framework index header now explains the depth boundary: it is the broad
   packet-backed map, while the main reader is the 222-dossier editorial layer.
   This prevents a roster page from being mistaken for a completed deep
   investigation.
   The recreation comparison then added a reader-facing franchisee evidence
   table for RBI, YUM, Wingstop, and Domino's. It separates disclosed parent
   cash and system activity from the still-missing operator return after
   labor, rent, debt, remodels, closures, and support. The lane remains
   qualified; this is an evidence-boundary clarification, not a proven
   franchisee-health conclusion.
   At the 2026-09-14 checkpoint, the reader landing page exposed six
   first-principles entry points before the company catalog, including the control-point/burden question,
   owner-cash bridge, installed-base economics, marketplace obligations,
   franchise systems, and balance-sheet durability. Their routes were checked
   against the live local server and the full reader browser suite passed on
   desktop, mobile, article, comparison, search, source-boundary, and framework
   index flows.
The reader's recreation status was also corrected: it now says the common
bridge is built and names the remaining undisclosed operator evidence—unit
returns, closures, remodel support, and operator debt. The reader links
directly to the lane-completion audit so “qualified” has an inspectable
explanation.
The reader now distinguishes its 222 deep company studies from the 238-page
framework index, whose additional pages are shorter roster-level packet
pages. This prevents the catalog count from implying identical depth across
every indexed company.
   The landing page now also gives software, data, and recurring workflows a
   first-class theme and status lane, connecting Adobe, ServiceNow, Snowflake,
   and Cloudflare to the recurring-revenue, cloud-cost, AI-investment, and
   dilution questions already covered by the underlying dossiers.
   The financial-intermediation synthesis now adds a within-model regional-bank
   comparison for M&T, Regions, WaFd, Truist, U.S. Bancorp, and PNC. It compares
   earnings, NIM, ROTCE, CET1, deposit cost, credit, and capital-return burden
   without presenting unlike banks as a single free-cash-flow ranking.
   The same synthesis now adds a public-asset-manager comparison for BlackRock,
   T. Rowe Price, Invesco, and Franklin, separating AUM from net flows, fee
   rates, product concentration, acquisition cash, compensation, and per-share
   owner cash.
   The same synthesis now adds an insurance-broker comparison for Aon,
   Gallagher, and Marsh McLennan, separating organic fee growth from acquired
   revenue and retaining producer retention, receivables, earnouts, goodwill,
   debt, talent cost, and dilution in the common-owner test.
   The same synthesis now adds an alternative-capital comparison for
   Blackstone, Apollo, KKR, Ares, and Carlyle. It separates recurring fee
   earnings from insurance spread, realized performance income, accrued carry,
   acquisitions, partner and employee claims, required capital, and dilution.
The conclusion remains qualified: these platforms have different earnings
denominators and should not be ranked on adjusted earnings alone.

The market-infrastructure section now also carries State Street's registered
custody-and-servicing screen: approximately `$52.9B` of equity value against
`$2.8B / $3.8B / $4.8B` normalized earnings cases, implying `$28.0B / $49.4B /
$76.8B` at `10x / 13x / 16x`. The comparison keeps AUC/A and AUM separate from
company cash and leaves fee pressure, market-versus-flow effects, technology,
cybersecurity, liquidity, and bank-capital requirements visible.

The healthcare valuation section now adds the senior-housing pair to the same
denominator-specific view: Brookdale at approximately `$2.905B` of equity value
against `$0.5B / $2.5B / $6.0B` operator cases, and Ventas at approximately
`$46.160B` against `$24.0B / $36.0B / $52.8B` property cases. Brookdale's
screen requires occupancy and cash normalization after labor, leases, and
maintenance; Ventas's requires rent, operator coverage, recurring capital,
acquisition returns, debt, and dilution. They are not interchangeable senior-
housing exposures.
   The healthcare synthesis now adds a home-care cohort comparison between
   Addus and AdaptHealth. It distinguishes paid caregiver hours and
   reimbursement from equipment placement, recurring resupply, working capital,
   capitated contracts, impairment, replacement capital, and per-share cash.
   It also adds a direct-care comparison between HCA and DaVita, separating
   hospital admissions, collections, facility renewal, policy payments, debt,
   and NCI from dialysis treatment cadence, clinic labor, home-dialysis support,
   and risk-based medical-cost exposure.
   It also adds a procedure-platform comparison between Intuitive Surgical and
   Stryker, separating installed-system utilization and instrument pull-through
   from acquisition-led breadth, inventory, amortization, cyber, debt, stock
   compensation, and post-deal cash returns.
   It also adds a product-flow distribution comparison between McKesson and
   Cencora, separating gross-profit spread from working-capital funding,
   supplier and customer terms, specialty mix, LIFO and settlement effects,
   acquisition cash, litigation, debt, and per-share cash.
   The AI physical-capacity synthesis now adds an architecture-versus-physical-
   capacity comparison between NVIDIA and Vertiv, separating architecture cash
   and customer commitments from backlog, factory, inventory, warranty, service,
   acceptance, acquisition, and working-capital burdens.
   It also adds a network-control comparison between Arista and Ciena,
   separating switching architecture, software, and customer prepayment from
   optical backlog, inventory, receivables, factoring, obsolescence, tariff
   benefits, refinancing, and dilution.
   It also adds a semiconductor-process-control comparison between KLA and
   Applied Materials, separating inspection and yield control from broader
   process coverage, service, China exposure, customer concentration, contract
   liabilities, inventory, facility capex, R&D, SBC, debt, and cycle-normalized
   cash.
   It also adds a validation-and-measurement comparison between Teradyne and
   Keysight, separating production semiconductor test from broader engineering
   and network assurance while keeping test-cycle concentration, deferred
   revenue, tax and working-capital timing, Spirent integration, R&D, SBC, debt,
   and per-share cash visible.
   The financial-intermediation synthesis now adds a market-infrastructure
   comparison between CME and State Street, separating clearing fees and
   rate-sensitive collateral income from custody and servicing fees while
   keeping restricted client balances, AUC/A, AUM, technology, cyber, liquidity,
   capital, and operational-failure claims visible.
3. Complete direct links from the main reader and operator surfaces to the
   September 14 synthesis pages.
4. Run a final lane-by-lane audit for aging/healthcare, recreation,
   connectivity/AI physical capacity, and financial/property models to label
   each as proven, qualified, or partial.
5. Normalize any inherited or offloaded source paths that prevent a reader from
   tracing an important claim to the packet, ledger, or official filing.
6. Produce a final closeout note only after the completion audit proves that
   major lanes have flagship names, exact facts, causal interpretation,
   burden split, watchlist, falsifier, and reproducible source route.

## Verification commands

Run from the repository root:

```text
python3 scripts/verify-deep-dossier-scenario-register.py
python3 scripts/verify-cross-framework-company-pages.py
git diff --check
bash scripts/verify-insight-system.sh
```

Last observed result on this handoff: all four checks passed, including
`insight-system-ok`.

## Important navigation

- [Combined end-to-end forensic research system](../analysis/cross-sector/combined-end-to-end-forensic-research-system-2026-09-13.md)
- [Company findings to cohort explanations](../analysis/cross-sector/company-and-cohort-writing-map-2026-09-14.md)
- [Healthcare, aging, and owner cash](../analysis/cross-sector/healthcare-aging-to-owner-cash-forensic-synthesis-2026-09-14.md)
- [AI physical capacity to owner cash](../analysis/cross-sector/ai-physical-capacity-to-owner-cash-forensic-synthesis-2026-09-14.md)
- [Financial intermediation to common-owner cash](../analysis/cross-sector/financial-intermediation-to-owner-cash-forensic-synthesis-2026-09-14.md)
- [Standards, ratings, and clearing infrastructure](../analysis/cross-sector/standards-ratings-versus-clearing-infrastructure-forensic-comparison-2026-09-13.md)
- [Company findings to cohort explanations](../analysis/cross-sector/company-and-cohort-writing-map-2026-09-14.md)
- [Recreation, lifestyle, and occasion demand](../analysis/cross-sector/recreation-lifestyle-occasion-demand-comparison-2026-08-11.md)
- [Home demand: curation, logistics, and owner cash](../analysis/first-principles/home-demand-curation-logistics-and-owner-cash.md)
- [Lane completion audit](lane-completion-audit-2026-09-14.md)
- [RH and Wayfair reproducibility gap](reproducibility-gap-rh-wayfair-2026-09-14.md)
- [Deep-dossier scenario register](../analysis/valuation/deep-dossier-scenario-inputs-2026-09-13.csv)

## Skeptical Reader Test

A skeptical reader should be able to identify the exact company and filing
window behind each current conclusion, understand why the operating metric is
not automatically owner cash, see which party carries the burden, and find the
next filing test that could weaken the conclusion. If a page does not meet that
test, it remains qualified work and should not be described as fully proven.
