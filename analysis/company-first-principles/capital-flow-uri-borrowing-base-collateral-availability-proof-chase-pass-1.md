# Capital Flow URI Borrowing-Base Collateral Availability Proof Chase Pass 1

## Purpose

This pass executes the second ranked named-cash proof target:

`United Rentals borrowing-base certificate and collateral availability support.`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.csv`

The upstream source locator is:

`/cluster/capital-flow-named-cash-proof-source-locator-pass-1.md`

## Question

`Can URI move from fleet/facility proxy to legal borrowing-base and collateral-availability proof?`

## Short Answer

`No full upgrade yet. URI has unusually strong public proxy evidence: July 2025 ABL reset availability, a real May 31 2025 certificate-delivery condition, a 1.000B USD minimum closing Combined Availability condition, Q2 2026 liquidity and facility balances, AR securitization collateral-pool coverage, fleet asset-base proxies, and covenant-threshold evidence. But the public record still does not expose populated borrowing-base certificate values, eligible collateral schedules, NOLV appraisal values, reserves, L/C schedules, or Combined Borrowing Base/Combined Availability calculations.`

## Sources Checked

The local check covered:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-1.htm`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-ex99-earnings-release.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-06-18-ex10-1-receivables-purchase-amendment.html`

The public check surfaced the July `2025` SEC 8-K announcing the ABL reset. That filing adds a useful availability datapoint: approximately `2.428B USD` available for additional ABL borrowings, net of letters of credit and subject to borrowing-base limitations. It still does not provide the actual certificate.

## Official 2026 SEC refresh

The July 2026 second-quarter results provide a stronger period-matched
operating and liquidity bridge. URI reports `2.999B USD` of total liquidity at
June 30, 2026, `3.305B USD` of year-to-date operating cash flow, `2.720B USD`
of gross rental-equipment purchases, and `330M USD` of used-equipment sale
proceeds. The filing also reports a `52.9%` OEC recovery rate on fleet sold in
the quarter. These observations connect fleet activity to cash generation and
liquidity, but total liquidity still combines cash, ABL availability, and AR
securitization availability.

The public credit-agreement exhibit exposes a form of Borrowing Base
Certificate and the ABL agreement defines the secured borrower, collateral,
and availability framework. That improves the certificate field map, but no
populated current certificate, eligible-collateral schedule, NOLV appraisal,
reserve schedule, L/C schedule, Combined Borrowing Base, or Combined
Availability calculation was located in the checked public filings.

### Q2 2026 facility-level availability disclosure

The Q2 2026 10-Q improves the availability bridge beyond the earlier
total-liquidity subtraction. At June 30, 2026, URI reports `$2.802B` of ABL
borrowing capacity net of letters of credit and `$85M` of accounts-receivable
securitization capacity. Together these equal `$2.887B`, reconciling to the
previously derived `$2.999B` total liquidity less `$112M` of cash.

This is filed facility-level availability, not a populated certificate: the
10-Q still does not disclose eligible equipment by category, NOLV, reserves,
U.S./Canadian borrowing-base components, or a live Combined Borrowing Base and
Combined Availability calculation. The corrected classification is therefore
`facility-availability-visible`, while the certificate-grade gate remains open.

The QoE implication is explicit: the `330M USD` used-equipment proceeds and
`52.9%` OEC recovery rate are cash and recovery observations, not proof that
the fleet earned a lifecycle return after maintenance capital, debt service,
tax, overhead, and replacement needs.

## What We Can Prove Now

| Gate | Result | Evidence |
|---|---|---|
| ABL reset availability | Pass with boundary | July `2025` 8-K reports approximately `2.049B USD` drawn and `2.428B USD` available, net of letters of credit and subject to borrowing-base limitations. |
| Certificate existence | Pass with boundary | The ABL agreement says a Borrowing Base Certificate prepared as of May `31`, `2025` was delivered to Agent and Lenders as a closing condition. |
| Minimum closing availability | Pass with boundary | The agreement required post-transaction Combined Availability of at least `1.000B USD`. |
| Certificate field map | Pass with boundary | The agreement identifies the required field families for a certificate-grade proof test. |
| Q2 `2026` facility availability | Pass with boundary | The 10-Q discloses `$2.802B` of ABL borrowing capacity net of letters of credit and `$85M` of AR securitization capacity, totaling `$2.887B`; this reconciles to total liquidity less cash. |
| ABL draw intensity | Pass with boundary | Q2 `2026` ABL balance was `1.666B USD` against stated facility size of `4.500B USD`. |
| AR collateral pool | Pass with boundary | AR securitization collateral pool net of reserves/deductions was `1.779B USD` against `1.414B USD` borrowings, or `125.8%` coverage. |
| Fleet asset base | Pass with boundary | Rental equipment NBV was `17.350B USD`; OEC was `23.8B USD`. |
| Covenant threshold | Pass with boundary | URI disclosed covenant compliance and that specified availability exceeded the springing covenant threshold. |
| Populated borrowing-base certificate | Hold | No public/current local source exposes live certificate values or component calculations. |

## Why This Matters

URI is the cleanest asset-backed operating case in the current proof system. It shows the economic machine:

`fleet asset base -> rental capex -> rental revenue and OCF -> receivables/fleet collateral -> ABL and AR funding availability`

But named cash proof requires legal availability, not just a large fleet and unused facility capacity.

The missing document is specific:

`Borrowing Base Certificate or equivalent collateral availability report.`

That document should show eligible inventory, eligible rental-equipment NBV, eligible rental-equipment NOLV, reserves, outstandings, L/C usage, Combined Borrowing Base, Combined Availability, and Suppressed Availability.

## Upgrade Test

URI can move to collateral-availability proof only if a source joins:

1. period-tested facility balance
2. eligible collateral by category
3. appraisal/NOLV or valuation support
4. reserves and ineligible collateral deductions
5. L/C usage and outstandings
6. Combined Borrowing Base
7. Combined Availability
8. covenant or availability threshold reconciliation

The July `2025` availability disclosure and Q2 `2026` facility-level split are
useful, but they do not satisfy the certificate-grade test.

## Decision

`uri-borrowing-base-collateral-availability-proof-chase-hold-with-facility-availability-and-stronger-2026-operating-cash-proxy`

The URI collateral chase is executed against local SEC sources and targeted public search. URI improves to strong public availability/collateral proxy status, but it remains below certificate-grade legal availability proof.

## Safe Claim

`United Rentals has strong public evidence for an asset-backed fleet funding model: July 2025 ABL availability of approximately 2.428B USD, a filed agreement requiring a May 31 2025 borrowing-base certificate and at least 1.000B USD of closing Combined Availability, Q2 2026 filed facility availability of 2.802B USD under the ABL plus 85M USD under the AR facility, ABL draw intensity of 37.0%, AR collateral-pool coverage of 125.8%, rental equipment NBV of 17.350B USD, and OEC of 23.8B USD. Current public evidence still does not provide populated borrowing-base certificate values, eligible collateral, NOLV, reserves, U.S./Canadian component schedules, or live Combined Borrowing Base and Combined Availability calculations.`

## Live SEC-source recheck — 2026-09-17

The latest SEC search also rechecked the June 18, 2026 Amendment No. 18 to
United Rentals' receivables purchase agreement. The filing confirms the
current AR-facility parties and amendment route, but it does not attach a
period-tested purchaser availability schedule, receivables report, populated
borrowing-base certificate, or live Combined Availability calculation. It
therefore strengthens the legal facility route without changing Q-13's
`evidence-insufficient` certificate-grade status.

This is a searched-negative result for the checked public perimeter, not a
claim that lenders lack the underlying reports. The next decisive source
remains a current certificate, collateral availability report, NOLV/appraisal,
reserve schedule, or lender/purchaser report that can join legal availability
to fleet purchase funding and lifecycle return.

Source: [June 18, 2026 Amendment No. 18](https://www.sec.gov/Archives/edgar/data/1067701/000110465926075708/tm2618215d1_8k.htm).

## Live SEC filing-index and Q2 2026 10-Q recheck — 2026-09-18

The current SEC index for URI's June 30, 2026 Form 10-Q lists `53` filing
documents and does not include a populated borrowing-base certificate or
collateral-availability report. The 10-Q itself reports the relevant public
proxy fields—`$2.802B` ABL borrowing capacity net of letters of credit, `$85M`
of receivables-securitization capacity, `$1.666B` of ABL debt, and a `$1.779B`
receivables collateral pool—but its borrowing-base discussion remains a
definition and covenant/availability boundary. It does not disclose the
eligible-equipment schedule, NOLV, reserves, U.S./Canadian components, or live
Combined Borrowing Base/Combined Availability calculation.

This recheck therefore confirms `searched-negative` for the certificate-grade
object within the current SEC filing perimeter and leaves Q-13 at
`evidence-insufficient`; it does not upgrade facility availability into legal
collateral proof or lifecycle return.

The same Q2 2026 10-Q adds a period-matched cash-burden and source/use control:
URI reports `$3.305B` of H1 operating cash flow, `$2.885B` of payments for
rental and non-rental equipment and intangible assets, `$706M` of equipment
sale proceeds, `$400M` of acquisitions, `$91M` of net debt payments, `$816M`
of share purchases, `$248M` of dividends, and `$158M` of net cash taxes paid.
These figures sharpen the operating-to-capital and senior-claim bridge, but
they remain consolidated company cash flows. They do not allocate cash to a
particular ABL draw, fleet cohort, borrowing-base collateral pool, or
lifecycle return, and they do not replace the missing certificate/NOLV/reserve
schedule.

Sources: [June 30, 2026 Form 10-Q filing index](https://www.sec.gov/Archives/edgar/data/1067701/000106770126000026/0001067701-26-000026-index.htm) and [URI Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1067701/000106770126000026/uri-20260630.htm).

## Targeted lender and rating-route recheck — 2026-09-18

A targeted public search was run for a current URI borrowing-base certificate,
NOLV or reserve schedule, lender collateral-coverage report, rating-agency
availability analysis, or lender presentation with populated collateral
values. The search surfaced the official Q2 2026 investor presentation
([preserved local artifact](../../raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/investor-presentations/2026-q2-investor-presentation.pdf)) and
the already-preserved ABL agreement, but no new certificate-grade document or
period-tested collateral component schedule. The Q2 presentation repeats
management's liquidity and fleet framework; it does not disclose eligible
equipment, NOLV, reserves, L/C deductions, or live Combined Availability.

This is a searched-negative for the targeted public route, not evidence that
the underlying lender reports do not exist. Q-13 remains
`evidence-insufficient`; the next decisive source remains a lender/collateral
report, populated certificate, appraisal/NOLV schedule, or later filing that
exposes the component calculation. Do not repeat the same broad route without
one of those new source objects.

## Next Source Package

1. Rating-agency report with ABL collateral coverage, advance-rate, or liquidity detail.
2. Future 8-K exhibit containing a certificate form, collateral report, or amended borrowing-base schedule.
3. Lender presentation or syndication package with availability and collateral values.
4. Later 10-Q/10-K liquidity note that splits ABL availability from AR securitization availability.
5. Receivables monthly report or purchaser availability schedule for the AR facility.

The [structured Q-13 next-source package](data/capital-flow-uri-q13-next-source-package-2026-09-18.csv)
now preserves these five requests with their minimum fields, promotion joins,
and current public-status boundaries. A later public document should be
accepted as an upgrade only if it satisfies one of these requests; another
headline liquidity figure does not close certificate-grade legal availability.
