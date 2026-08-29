# Capital Flow Atwell K-FITS Holding Extraction

## Purpose

This pass adds a lender-side filing to the Atwell bank-replacement test.

The question is:

`Can we find actual reported portfolio dollars for Atwell after the 2026 Advent/Ares/Antares financing trail?`

Extraction table:

`analysis/company-first-principles/data/capital-flow-atwell-kfits-2026q2-holding-extractions.csv`

## Source

| Source | Filing | Local Path |
|---|---|---|
| KKR FS Income Trust Select | Q2 2026 SEC 10-Q HTML | `raw/primary-sources/capital-flow/atwell/sec/kfits-2026q2-10q.html` |

The schedule is useful because it reports borrower-level holdings. It does not identify the whole lender group or the full Atwell facility amount.

## Extracted Atwell Rows

The K-FITS schedule of investments includes Atwell LLC in `Senior Secured Loans--First Lien` under `Capital Goods`.

| Row | Borrower | Type | Rate | Floor | Maturity | Principal / Commitment | Amortized Cost | Fair Value |
|---|---|---|---|---|---|---:|---:|---:|
| 196 | Atwell LLC | funded first-lien loan | SOFR + `5.0%` | `0.8%` | `04/33` | `4.002M USD` | `3.983M USD` | `3.986M USD` |
| 197 | Atwell LLC | unfunded commitment | SOFR + `5.0%` | `0.8%` | `04/33` | `0.488M USD` | `0.488M USD` | `0.486M USD` |

The unfunded commitment table also lists:

`Atwell LLC -> 0.488M USD commitment amount`

The filing reports total investments at fair value of `1.553547B USD`.

So the disclosed Atwell slice is small inside K-FITS:

| Calculation | Result |
|---|---:|
| Funded fair value / total investments fair value | `0.257%` |
| Funded plus unfunded fair value / total investments fair value | `0.288%` |

## Claim Impact

Before this pass, Atwell was supported by:

`2024 bank facility -> 2026 Advent transaction -> 2026 Ares role -> 2026 Antares first-lien clue`

After this pass, Atwell also has:

`2026 SEC portfolio schedule -> KKR FS Income Trust Select disclosed Atwell first-lien position -> funded amount, unfunded commitment, rate, floor, maturity, fair value`

That upgrades the evidence from announcement-only to at least one reported holder-level balance.

## What This Proves

This proves:

- Atwell LLC appeared in a SEC-filed lender-side investment schedule as of June 30, 2026.
- The disclosed instrument was first-lien senior secured debt in Capital Goods.
- K-FITS held a `3.986M USD` funded fair-value position and a `0.486M USD` fair-value unfunded commitment.
- The listed rate was SOFR plus `5.0%`, with a `0.8%` floor and `04/33` maturity.

## What This Still Does Not Prove

This still does not prove:

- The full Atwell facility size.
- Ares' exact funded amount.
- Antares' exact funded amount.
- Whether Bank of America's 2024 facility was repaid.
- Whether bank lenders stayed in a revolver, treasury, hedge, or administrative role.

## Safer Claim

`Atwell now has borrower-level portfolio evidence: at least one SEC-filing credit vehicle reported a first-lien Atwell loan and unfunded commitment after the 2026 Advent/Ares/Antares financing trail. That supports the claim that private-credit capital reached the borrower, but it still does not prove private credit replaced the 2024 Bank of America-led facility.`

## Simple Version

We found real numbers for Atwell.

Not the full deal size, but a real lender-side slice:

`4.002M USD funded principal + 0.488M USD unfunded commitment`

That makes the Atwell case stronger. It is no longer only press releases. But it is still not enough to say the old bank facility was replaced.
