# United Rentals fleet-lifecycle valuation/liquidity workbench

Research date: `2026-09-18`

## Purpose

This workbench tests United Rentals as a fleet-capacity allocator. The chain is `fleet purchase -> rental utilization/rate -> customer collection -> resale recovery -> debt/ABL/AR funding -> replacement and growth capital -> common residual`.

## H1 2026 filed cash and lifecycle bridge

| Field | Amount | Treatment |
| --- | ---: | --- |
| Operating cash flow | `$3.305B` | Reported operating cash |
| Rental-equipment purchases | `($2.720B)` | Gross fleet investment |
| Non-rental equipment/intangibles | `($165M)` | Corporate/non-fleet reinvestment |
| Equipment sale proceeds | `$706M` | Recovery, not recurring revenue |
| Acquisitions | `($400M)` | Separate growth use |
| Contingent consideration | `($18M)` | Acquisition claim |
| Repurchases including settlement taxes | `($816M)` | Post-OCF capital claim |
| Dividends | `($248M)` | Distribution |

Derived screens are `$585M` of OCF less gross rental-equipment purchases, `$1.265B` after adding rental-equipment sale proceeds, and `$420M` after subtracting rental and non-rental equipment/intangible purchases. None is normalized owner cash. Resale proceeds depend on age, utilization, used-equipment pricing, and replacement policy; gross capex cannot be classified as all growth or all maintenance.

Rental-equipment net book value was `$17.350B` against approximately `$23.8B` original equipment cost. H1 operating cash absorbed `$272M` of receivables and `$54M` of inventory while receiving `$623M` from accounts payable and `$114M` from accrued liabilities. The cash bridge requires both lifecycle and working-capital persistence tests.

## Financing and legal-availability boundary

Q2 public disclosures report `$2.802B` of ABL borrowing capacity net of letters of credit and `$85M` of AR-securitization capacity, or `$2.887B` in facility-level availability. This reconciles to `$2.999B` of total liquidity less `$112M` of cash. The public ABL agreement identifies certificate fields, collateral, and covenant mechanics, but no current populated borrowing-base certificate, eligible-equipment schedule, NOLV, reserves, L/C schedule, or live Combined Availability calculation was found.

The facility figure is a public proxy, not legal availability. ABL capacity cannot be assigned to a particular fleet cohort or purchase without a draw/use ledger. The `$330M` used-equipment sale proceeds and 52.9% quarterly OEC recovery rate are recovery observations, not proof of lifecycle return after maintenance, debt, tax, overhead, and replacement needs.

## Valuation expectation screen — September 18, 2026

The market snapshot reports approximately `$63.108B` equity value at `$1,013.91` per share. Using the H1 OCF-less-gross-rental-capex screen of `$374M`, annualized to `$748M`, gives approximately `84.4x` market capitalization to the mechanical annualized screen. This is a price-implied expectation diagnostic, not a DCF, normalized FCF multiple, or ranking.

## Damodaran/Lyn Alden application

Use replacement, growth, and stress cases. The replacement case maintains fleet capacity with conservative utilization and resale; the growth case adds fleet only with incremental demand, funding, and return evidence; the stress case lowers utilization and used-equipment recovery while increasing rates, reserves, collection delays, and replacement capital. Fleet growth, adjusted EBITDA, reported FCF, facility capacity, and resale proceeds remain diagnostic.

## Promotion boundary

`fleet-lifecycle-qualified; facility-availability-visible; certificate-hold; owner-cash-open; no-ranking`

Promotion requires a populated borrowing-base or equivalent collateral report, utilization and rate/mix data, replacement-versus-growth capex, fleet-cohort funding, resale recovery, debt/lease claims, and diluted common residual.

## Sources

- [URI fleet lifecycle bridge](combined-investment-research-industrial-uptime-uri-fleet-lifecycle-bridge-pass-1-2026-09-17.md)
- [URI public ABL proxy bridge](capital-flow-uri-abl-public-disclosure-proxy-bridge-pass-1.md)
- [URI borrowing-base proof chase](capital-flow-uri-borrowing-base-collateral-availability-proof-chase-pass-1.md)
- [United Rentals Q2 2026 Form 10-Q](../../raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html)

