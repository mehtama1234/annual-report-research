# Capital Flow KKR Global Atlantic Accordia Schedule D Held-Row Column Geometry Pass 1

## Purpose

This pass diagnoses the exact held-row geometry problem after the first Accordia Schedule D column reconciliation.

It asks:

`Which rows block the Accordia Schedule D owned-bond reconciliation, which token patterns are likely short fragments, embedded rows, or page/section total signatures, and which high-dollar candidate rows need spot checks before book-value proof can be promoted?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-schedule-d-held-row-column-geometry-diagnostic-pass-1.csv`

## Short Answer

`The column problem is now localized. There are 21 held reconciliation rows: 3 short-token fragments and 18 long-token rows. The long rows include 3 rows with page/section-total signatures and 9 rows with possible embedded-security patterns. The held rows carry 231751265 USD of first-four candidate book value, but their extra token groups include 6622705761 USD of non-promoted candidate book-like values, including 7 values above 50M USD. That is why blindly adding later token groups would be unsafe.`

## Diagnostic Metrics

| Metric | Value |
|---|---:|
| Geometry rows | 46 |
| Held reconciliation rows | 21 |
| Short-token held rows | 3 |
| Long-token held rows | 18 |
| Subtotal-signature held rows | 3 |
| Possible embedded-security held rows | 9 |
| Held first-four candidate book value | 231751265 |
| Extra group book-like sum, not proof | 6622705761 |
| Extra group book-like values over 50M | 7 |
| Largest extra group book-like value, not proof | 5364223361 |
| High-dollar candidate rows selected | 25 |
| High-dollar selected first-four book value | 1112630206 |
| Candidate book value before geometry | 6409765632 |
| Statutory bond target | 7318322163 |
| Variance before geometry | -908556531 |
| Coverage before geometry pct | 87.585180 |

## Held Row Examples

| ID | Type | Page | CUSIP | Issuer | First-Four Book | Max Extra Book-Like Value | Geometry Class |
|---|---|---:|---|---|---:|---:|---|
| CFKKRGACEDHG-001 | held-reconciliation-row | 218 | 91282C-PN-5 | UNITED STATES TREASURY | 645310 | 6668000 | long-token-row-with-small-extra-column-noise |
| CFKKRGACEDHG-002 | held-reconciliation-row | 218 | 268317-AL-8 | ELECTRICITE DE FRANCE SA | 5314283 | 8621177 | long-token-row-with-small-extra-column-noise |
| CFKKRGACEDHG-003 | held-reconciliation-row | 218 | 57582R-N9-3 | MASSACHUSETTS COMMONWEALTH | 2905372 | 86445195 | long-token-row-with-possible-embedded-security |
| CFKKRGACEDHG-004 | held-reconciliation-row | 219 | 95308R-XA-2 | WEST HARRIS CNTY TEX REGL WTR AUTH WTR S | 3995576 | 428544580 | long-token-row-with-page-or-section-total-signature |
| CFKKRGACEDHG-005 | held-reconciliation-row | 219 | 36271M-AC-1 | GSPWC 2023 LLC Class C Asset-Backed Note | 2524178 | 61250000 | long-token-row-with-possible-embedded-security |
| CFKKRGACEDHG-006 | held-reconciliation-row | 222 | 046353-AU-2 | ASTRAZENECA PLC | 4624794 | 6050522 | long-token-row-with-small-extra-column-noise |
| CFKKRGACEDHG-007 | held-reconciliation-row | 227 | 254687-FZ-4 | WALT DISNEY CO |  | 0 | short-token-fragment-probable-income-or-continuation |
| CFKKRGACEDHG-008 | held-reconciliation-row | 231 | 53944Y-AE-3 | LLOYDS BANKING GROUP PLC |  | 0 | short-token-fragment-probable-income-or-continuation |
| CFKKRGACEDHG-009 | held-reconciliation-row | 237 | 84756N-AE-9 | SPECTRA ENERGY PARTNERS LP | 14822873 | 14379429 | long-token-row-with-possible-embedded-security |
| CFKKRGACEDHG-010 | held-reconciliation-row | 239 | 91324P-EF-5 | UNITEDHEALTH GROUP INC |  | 0 | short-token-fragment-probable-income-or-continuation |
| CFKKRGACEDHG-011 | held-reconciliation-row | 239 | 92936U-AG-4 | WP CAREY INC | 125661 | 16200000 | long-token-row-with-possible-embedded-security |
| CFKKRGACEDHG-012 | held-reconciliation-row | 240 | J41838-AQ-6 | MEIJI YASUDA LIFE INSURANCE CO | 381000 | 5364223361 | long-token-row-with-page-or-section-total-signature |

## High-Dollar Candidate Spot Checks

| ID | Type | Page | CUSIP | Issuer | First-Four Book | Max Extra Book-Like Value | Geometry Class |
|---|---|---:|---|---|---:|---:|---|
| CFKKRGACEDHG-022 | high-dollar-candidate-row | 230 | 458140-BM-1 | INTEL CORP | 66417686 | 64380157 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-023 | high-dollar-candidate-row | 237 | 87264A-AZ-8 | T-MOBILE USA INC | 65593727 | 85890000 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-024 | high-dollar-candidate-row | 219 | 91412G-HA-6 | UNIVERSITY CALIF REVS | 57637593 | 67380869 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-025 | high-dollar-candidate-row | 223 | 07274N-AQ-6 | BAYER US FINANCE II LLC | 57184894 | 60142081 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-026 | high-dollar-candidate-row | 218 | 54438C-PA-4 | LOS ANGELES CALIF CMNTY COLLEGE DIST | 56626113 | 47376763 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-027 | high-dollar-candidate-row | 227 | 26442C-BK-9 | DUKE ENERGY CAROLINAS LLC | 49918733 | 51337500 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-028 | high-dollar-candidate-row | 240 | 963320-AX-4 | WHIRLPOOL CORP | 48696573 | 12092065 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-029 | high-dollar-candidate-row | 226 | 22822V-AQ-4 | CROWN CASTLE INC | 48357679 | 0 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-030 | high-dollar-candidate-row | 230 | 437076-CD-2 | HOME DEPOT INC | 47205182 | 101679067 | candidate-mapped-high-dollar-row |
| CFKKRGACEDHG-031 | high-dollar-candidate-row | 240 | 94974B-GU-8 | WELLS FARGO & CO | 45705863 | 56541713 | candidate-mapped-high-dollar-row |

## Proof Effect

This pass improves the proof stack by identifying the real parser boundary. The short-token held rows look like fragments or continuation/income-only rows. The long-token held rows are the real issue: some later token groups may represent embedded securities, but others clearly look like page or section totals. Because the later groups mix those patterns, they cannot be promoted by formula.

The safe use is:

`Accordia Schedule D has a named-security universe and a quantified column-reconciliation frontier, but final book-value proof needs source-page column geometry for held rows and high-dollar spot checks.`

## Boundary

Do not use this pass as final statutory column proof. Do not add the extra token groups to book value. Do not claim issuer-level income, proceeds, gain/loss, liability spread, waterfall, collateral support, or return from this diagnostic.

## Next Action

Run a source-page column extraction or manual geometry pass for the held rows, starting with page/section-total signatures on pages `219`, `240`, and `246`, then rerun the full reconciliation against the `7.318322163B USD` statutory bond base.

## Decision

`kkr-global-atlantic-accordia-held-row-column-geometry-localized-next-page-column-extraction`
