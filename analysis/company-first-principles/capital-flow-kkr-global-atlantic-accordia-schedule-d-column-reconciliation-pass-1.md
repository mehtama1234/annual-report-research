# Capital Flow KKR Global Atlantic Accordia Schedule D Column Reconciliation Pass 1

## Purpose

This pass tests whether the raw Accordia Schedule D owned-bond rows can be promoted from numeric-token evidence to statutory-column evidence.

It asks:

`Can we safely assign actual cost, par, fair value, and book/adjusted carrying value for the owned Schedule D bond/ABS universe, and does the candidate book value reconcile to the Accordia statutory bond base?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-column-reconciliation-diagnostic-pass-1.csv`

## Short Answer

`Partial hold. The first-four-token candidate map covers 1065 owned Schedule D rows and marks 21 rows for column review. Candidate book/adjusted carrying value sums to 6409765632 USD versus the 7318322163 USD statutory bond target, a variance of -908556531 USD and 87.585180% coverage. This is not clean enough for final book-value proof, but it is a quantified reconciliation frontier.`

## Reconciliation Metrics

| Metric | Value |
|---|---:|
| Owned reconciliation rows | 1086 |
| Candidate mapped rows | 1065 |
| Held rows | 21 |
| Candidate actual cost sum | 6470295613 |
| Candidate fair value sum | 5350633976 |
| Candidate book value sum | 6409765632 |
| Statutory bond target | 7318322163 |
| Candidate book variance | -908556531 |
| Candidate book coverage pct | 87.585180 |

## Candidate Examples

| ID | CUSIP | Issuer | Candidate Book Value | Status |
|---|---|---|---:|---|
| CFKKRGACEDCR-0001 | 912810-RC-4 | UNITED STATES TREASURY | 401,704 | candidate-first-four-column-map |
| CFKKRGACEDCR-0002 | 912810-TB-4 | UNITED STATES TREASURY | 1,909,447 | candidate-first-four-column-map |
| CFKKRGACEDCR-0003 | 912810-TG-3 | UNITED STATES TREASURY | 99,452 | candidate-first-four-column-map |
| CFKKRGACEDCR-0004 | 912810-TJ-7 | UNITED STATES TREASURY | 1,762,326 | candidate-first-four-column-map |
| CFKKRGACEDCR-0005 | 912810-TW-8 | UNITED STATES TREASURY | 409,028 | candidate-first-four-column-map |
| CFKKRGACEDCR-0006 | 912828-YB-0 | UNITED STATES TREASURY | 894,965 | candidate-first-four-column-map |
| CFKKRGACEDCR-0007 | 91282C-FF-3 | UNITED STATES TREASURY | 52,109 | candidate-first-four-column-map |
| CFKKRGACEDCR-0008 | 91282C-GM-7 | UNITED STATES TREASURY | 151,300 | candidate-first-four-column-map |
| CFKKRGACEDCR-0010 | 268317-AK-0 | ELECTRICITE DE FRANCE SA | 3,248,956 | candidate-first-four-column-map |
| CFKKRGACEDCR-0012 | 13063A-7D-0 | CALIFORNIA ST | 1,932,934 | candidate-first-four-column-map |

## Proof Effect

This pass does not finish the cash proof, but it narrows the exact blocker. The named-security universe exists. The first-four-token column map works for many normal rows, but final promotion requires resolving short-token and long-token rows and likely page-column geometry for dense statutory rows.

## Boundary

Do not use this pass as final book-value, proceeds, income, gain/loss, or return proof. The current evidence is a candidate reconciliation map with an unresolved variance against the statutory bond target.

## Next Action

Build `accordia-schedule-d-held-row-column-geometry` for the held rows and high-dollar variance drivers, then rerun reconciliation against the `7.318322163B USD` statutory bond base.

## Decision

`kkr-global-atlantic-accordia-schedule-d-column-reconciliation-candidate-map-visible-held-row-geometry-next`
