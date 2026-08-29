# Capital Flow Atwell SEC Holder Crosswalk

## Purpose

This pass checks whether Atwell appears in more than one public lender-side filing.

The question is:

`Can we move from a single holder-level Atwell debt slice to a cross-holder map?`

Crosswalk table:

`analysis/company-first-principles/data/capital-flow-atwell-sec-holder-crosswalk.csv`

## Sources

| Source | Filing | Local Path |
|---|---|---|
| KKR FS Income Trust Select | Q2 2026 SEC 10-Q HTML | `raw/primary-sources/capital-flow/atwell/sec/kfits-2026q2-10q.html` |
| FS KKR Capital Corp. | Q2 2026 SEC 10-Q HTML | `raw/primary-sources/capital-flow/atwell/sec/fsk-2026q2-10q.html` |

Both schedules use borrower-level rows. FSK states dollar amounts are in millions. K-FITS states dollar amounts are in thousands in the filing, and the normalized table converts its Atwell rows into USD millions for comparison.

## Cross-Holder Rows

| Reporting Entity | Funded Principal | Fair Value | Unfunded Commitment | Rate | Floor | Maturity |
|---|---:|---:|---:|---|---|---|
| KKR FS Income Trust Select | `4.002M USD` | `3.986M USD` | `0.488M USD` | SOFR + `5.0%` | `0.8%` | `04/33` |
| FS KKR Capital Corp. | `3.2M USD` | `3.2M USD` | `0.4M USD` | SOFR + `5.0%` | `0.8%` | `04/2033` |
| Combined disclosed slices | `7.202M USD` | `8.072M USD` including unfunded fair value | `0.888M USD` | SOFR + `5.0%` | `0.8%` | `04/2033` |

The combined funded-principal-plus-unfunded-commitment exposure is:

`8.090M USD`

## Claim Impact

Before this pass:

`Atwell had one SEC-filed holder-level debt slice.`

After this pass:

`Atwell appears in at least two KKR-related SEC-filed credit vehicles with matching first-lien pricing and maturity terms.`

This supports a stronger funding-route claim:

`The Atwell 2026 private-credit facility was not only a named Ares/Antares transaction; pieces of Atwell debt also appear in public BDC-style schedules, showing how the facility can be distributed into credit vehicles.`

## Boundary

This still does not prove:

- Total Atwell facility size.
- Ares' exact share.
- Antares' exact share.
- KKR's total platform-wide share beyond the two filing vehicles.
- Whether the 2024 Bank of America-led facility was repaid or replaced.

The safer bank-replacement claim remains:

`Atwell is a live bank-replacement candidate with increasingly concrete private-credit holder evidence, but not confirmed bank-displacement proof.`

## Simple Version

We found Atwell debt in two SEC-filed credit vehicles.

That means the private-credit money is visible in actual portfolio schedules, not just announcements.

But the disclosed slices add up to only `8.090M USD`, so they cannot be treated as the full deal or as proof that the `200M USD` 2024 bank facility disappeared.
