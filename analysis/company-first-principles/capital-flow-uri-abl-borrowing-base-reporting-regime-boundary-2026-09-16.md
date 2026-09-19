# URI ABL borrowing-base reporting-regime boundary

## Purpose

This pass tests whether the public United Rentals ABL record exposes a more
precise route to the missing Borrowing Base Certificate. It does not treat a
reporting obligation as a populated certificate. The structured [boundary table](data/capital-flow-uri-abl-borrowing-base-reporting-regime-boundary-2026-09-16.csv)
records the reporting cadence, trigger thresholds, closing-condition evidence,
and the latest public disclosure of covenant status.

## What is now source-visible

The July 2025 ABL agreement requires quarterly Borrowing Base Certificates as
of each fiscal quarter-end, with delivery by the 25th day of the following
month. It also requires a monthly certificate when daily Combined Availability
falls below 65% of the Maximum Revolver Amount, subject to an exception tied to
at least 25% Combined Availability, at least 75% Suppressed Availability, and
two specified credit ratings. The closing condition also proves that a May 31,
2025 certificate was delivered to the agent and lenders, and that closing
Combined Availability had to be at least `$1.000B`.

URI's June 30, 2026 10-Q says specified ABL availability exceeded the required
threshold and the fixed-charge covenant was therefore inapplicable. The same
filing reports `$2.802B` ABL borrowing capacity net of letters of credit and
`$1.666B` outstanding debt, but those are public availability snapshots rather
than the underlying collateral calculation.

This strengthens the legal-control route:

`facility agreement -> certificate cadence/trigger -> lender-held certificate -> collateral and availability calculation`

The public record still does not disclose the live certificate, eligible fleet
NBV, NOLV appraisal, reserves, L/C schedule, Combined Borrowing Base, or
Suppressed Availability. The reporting regime therefore narrows the acquisition
target but does not produce certificate-grade legal availability.

## Decision

`reporting-regime-and-thresholds-visible; populated-certificate-unproven`

The `$2.802B` capacity and `$1.666B` debt snapshot must not be presented as
unencumbered collateral value, lifecycle return, or proof that fleet cash paid
down the facility. The next decisive document remains a quarter-end certificate
or lender collateral report with component values.

## Source routes

- [URI July 2025 credit-agreement filing](https://www.sec.gov/Archives/edgar/data/1067701/000110465925067406/tm2520569d1_ex10-1.htm)
- [URI Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1067701/000106770126000026/uri-20260630.htm)
- [URI Q2 2026 earnings release](https://www.sec.gov/Archives/edgar/data/1067701/000106770126000028/uri-6302026xex991.htm)
