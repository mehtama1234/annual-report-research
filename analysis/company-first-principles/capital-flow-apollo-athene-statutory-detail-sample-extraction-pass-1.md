# Capital Flow Apollo Athene Statutory Detail Sample Extraction Pass 1

## Purpose

This pass tests whether the located Athene statutory Schedule D/BA detail pages can produce named CUSIP/issuer rows.

It asks:

`Can the Athene Annuity and Life Company statutory statement move from summary statutory bridge to named holding-level evidence?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-statutory-detail-sample-extraction-pass-1.csv`

The upstream compact extraction is:

`/cluster/capital-flow-apollo-athene-statutory-compact-extraction-pass-1.md`

## Short Answer

`Yes, at sample level. Targeted reads from Schedule BA Part 1, Schedule BA Part 2, Schedule D issuer-credit obligations, and Schedule D asset-backed securities produce named CUSIP/issuer rows with statutory fields. This is a real upgrade from summary-only statutory evidence. It is still not full Apollo/Athene cash proof because the full Schedule D/BA population, holding-level income normalization, liability-cost spread, borrower matching, and asset-level return model are not yet complete.`

## Detail Sample Rows

| Row | Schedule | Page | Named Holding / Issuer | Current Evidence | Proof Use | Boundary |
|---|---|---:|---|---|---|---|
| 1 | Schedule BA Part 1 | `5813` | `00264#-AA-5` / AP Aristotle Holdings LLC Aristotle Junior `0.000%` perpetual | Actual cost `16.122455M`, fair value/book value `10.783834M`, unrealized decrease `5.338621M`. | Named Schedule BA holding with valuation fields. | Not cash receipt or borrower-use proof. |
| 2 | Schedule BA Part 1 | `5813` | `G2973#-AB-4` / AP Chia Issuer LLC AP Chia PERP NC10 JR Notes | Actual cost `118,042`, fair value `112,655`, book value `111,779`, amortization/accretion `9,118`. | Named Schedule BA debt-style holding. | Not complete income/return proof. |
| 3 | Schedule BA Part 1 | `5813` | `G2971@-AA-0` / AP Pistachio LP Pistachio Jr Secured Perp Nts | Actual cost `3.944526M`, fair value `4.425152M`, book value `4.291472M`; transferred from Schedule D. | Named Schedule BA holding and transfer clue. | Not source/use or repayment proof. |
| 4 | Schedule BA Part 1 | `5813` | `90117P-AQ-8` / 1211 Avenue of the Americas Tr AOTA 2015-1211 E | Actual cost `85.081101M`, fair value/book value `77.949983M`, NAIC `3.C`, investment income `3.463856M`. | Named real-estate/structured-credit style Schedule BA income row. | Does not prove underlying property cash waterfall. |
| 5 | Schedule BA Part 1 | `5813` | `04410R-AQ-9` / Ashford Hospitality Trust 2018 AHT1 2018-ASHF F | Actual cost `46.997050M`, fair value/book value `46.962386M`, NAIC `3.B`, investment income `4.052450M`. | Named hospitality-related Schedule BA income row. | Not borrower-level hotel cash proof. |
| 6 | Schedule BA Part 1 | `5813` | `61764B-AU-7` / Morgan Stanley Capital I Trust MSC 2014-150E G | Actual cost `34.234162M`, fair value/book value `22.425000M`, OTTI `11.809162M`, investment income `595,159`. | Named impaired Schedule BA row. | Needs underlying collateral and loss attribution. |
| 7 | Schedule BA Part 1 | `5813` | AP Grange Holdings LLC AP Grange Tranche B | Actual cost `429.756073M`, fair value/book value `411.998739M`, NAIC `2.B`, investment income `31.661927M`. | Large named affiliated Schedule BA holding. | Not ultimate borrower cash proof. |
| 8 | Schedule BA Part 2 | `5826` | Ace Credit Fund LP ACE J59738 `5.420%` | Actual cost at acquisition `50.955599M`. | Named Schedule BA acquisition/addition row. | Not year-end income or return proof by itself. |
| 9 | Schedule BA Part 2 | `5826` | Ace Credit Fund LP ACE J59738 `5.460%` | Actual cost at acquisition `37.389504M`. | Second named Schedule BA acquisition row. | Not cash return proof. |
| 10 | Schedule D Part 1 Section 1 | `5836` | `912810-QH-4` / U.S. Treasury Bond | Actual cost `143.226702M`, par `147.210000M`, fair value `144.950562M`, book value `143.285105M`, NAIC `1.A`, interest income `836,189`, interest received `1.848438M`, maturity `2040-05-15`. | Named Schedule D issuer-credit row with income and received-interest fields. | Government bond row, not private-credit borrower destination. |
| 11 | Schedule D Part 1 Section 1 | `5836` | `912810-QE-1` / U.S. Treasury Bond | Actual cost `61.157561M`, par `61.191000M`, fair value `61.941881M`, book value `61.160841M`, NAIC `1.A`, interest income `1.068972M`, maturity `2040-02-15`. | Named Schedule D row with rating/designation and income. | Not private-credit cash loop. |
| 12 | Schedule D Part 1 Section 2 | `5912` | `38375B-3G-5` / GNMA GNR 2013-H14 SI | Actual cost `161,848`, fair value `136,264`, book value `157,636`, NAIC `1.A`, interest received `55,826`, maturity `2063-05-20`. | Named ABS Schedule D row with received-interest field. | Not originator-level borrower proof. |
| 13 | Schedule D Part 1 Section 2 | `5912` | `38375B-AE-2` / GNMA GNR 2010-H02 DI | Actual cost `77,116`, fair value `125,297`, book value `85,909`, NAIC `1.A`, interest income `2,787`, interest received `53,237`, maturity `2060-02-20`. | Named ABS row with income/received-interest fields. | Not security-level prepayment/collateral cash proof. |
| 14 | Schedule D Part 1 Section 2 | `5912` | `38375B-KM-3` / GNMA GNR 2011-H06 FI | Actual cost `163,101`, fair value `105,078`, book value `149,850`, NAIC `1.A`, OTTI `6,706`, interest income `5,627`, interest received `76,488`, maturity `2061-02-20`. | Named ABS row with impairment and income/receipt fields. | Needs full collateral/prepayment explanation. |

## What This Proves

The statutory PDF can produce named holding rows. That matters because it moves Apollo/Athene one step closer to the actual proof chain:

`insurance liabilities -> Athene legal entity -> named statutory holdings -> income / received interest -> credit quality`

The sample shows Schedule BA and Schedule D rows include the fields we need:

1. CUSIP or internal identifier
2. issuer / holding name
3. NAIC designation
4. actual cost
5. par value where applicable
6. fair value
7. book / adjusted carrying value
8. unrealized valuation change
9. OTTI or impairment field where applicable
10. investment income or interest received
11. acquisition date and maturity where applicable

## What It Still Does Not Prove

This remains a sample extraction only.

It does not prove:

1. the full Schedule D/BA population
2. total income by holding across every relevant page
3. private-credit borrower matching
4. asset-backed originator or collateral cash flow
5. liability-cost spread
6. Apollo-managed account allocation to individual holdings
7. full asset-level return

## Decision

`apollo-athene-statutory-detail-sample-extraction-named-holdings-visible-full-parse-pending`

Apollo/Athene now has named statutory holding samples from Schedule BA and Schedule D. The next step is a broader targeted parser for the page ranges already identified.

## Safe Claim

`Athene Annuity and Life Company's 2025 statutory statement can produce named Schedule BA and Schedule D holding rows with CUSIP/identifier, description, NAIC designation, cost, fair value, book value, income, received-interest, impairment, acquisition, and maturity fields. This supports holding-level extraction readiness. It does not yet prove full portfolio composition, borrower destination, liability-cost spread, or asset-level cash return.`

## Next Work

1. Build a parser for Schedule D issuer-credit obligations pages `5836-5911`.
2. Build a parser for Schedule D asset-backed securities pages `5912-6027`.
3. Build a parser for Schedule BA pages `5813-5835`, keeping Parts 1, 2, and 3 separate; Part 3 continues through pages `5834-5835` and Schedule D begins at `5836`.
4. Normalize fields into issuer/CUSIP, asset class, NAIC designation, cost, fair value, book value, income, received interest, OTTI, acquisition date, and maturity.
