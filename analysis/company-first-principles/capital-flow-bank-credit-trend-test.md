# Capital Flow Bank Credit Trend Test

## Why This Pass Exists

The first denominator pass compared Apollo, Ares, and BDC metrics against the latest bank-credit stocks.

This pass adds time. It asks whether the relevant bank-credit pools are shrinking, stagnant, or still growing while private credit expands.

## Local Data Files

- Bank-credit trend table: `analysis/company-first-principles/data/capital-flow-bank-credit-trends.csv`
- Cross-BDC bank scale comparison: `analysis/company-first-principles/data/capital-flow-cross-bdc-bank-scale-comparison.csv`
- Raw FRED series: `raw/primary-sources/capital-flow/market-denominators/fred/`
- Refresh script: `scripts/refresh-bank-credit-denominators.py`

Refresh status: rerun on `2026-08-24`; FRED latest rows remained `2026-08-12` for weekly bank-credit series and `2026-07-01` for monthly C&I and CRE series.

## Bank-Credit Growth

| Series | Latest Value | 1-Year Change | 3-Year Change | 5-Year Change |
|---|---:|---:|---:|---:|
| C&I loans (`BUSLOANS`) | `2.899T USD` | `+8.64%` | `+5.30%` | `+18.31%` |
| Loans and leases (`TOTLL`) | `13.983T USD` | `+7.44%` | `+15.07%` | `+34.33%` |
| Bank credit (`TOTBKCR`) | `19.796T USD` | `+6.30%` | `+14.76%` | `+25.91%` |
| Commercial real estate loans (`CREACBM027NBOG`) | `3.119T USD` | `+3.24%` | `+6.64%` | `+27.04%` |

## Cross-BDC Scale Against Bank Credit

The first three-BDC panel covers ARCC, OBDC, and BXSL.

| Metric | Value | Compared With C&I Loans |
|---|---:|---:|
| Three-BDC aggregate portfolio fair value | `57.704B USD` | `1.99%` |
| Three-BDC aggregate Q2 new commitments | `3.211B USD` | `0.11%` |
| Three-BDC known funded investments | `3.146B USD` | `0.11%` |
| Three-BDC portfolio company count | `1,161` | not a dollar comparison |

## What This Proves

The bank system is not disappearing in the aggregate.

C&I loans, total loans and leases, total bank credit, and commercial real-estate loans are all higher over one-year, three-year, and five-year windows in the local FRED data.

That matters because it prevents a lazy claim like:

`Private credit is replacing banks because bank credit is shrinking.`

The data does not say that.

## What It Suggests Instead

The cleaner interpretation is:

`Private credit is growing as a parallel lending channel while bank credit remains large and, in aggregate, still growing.`

The question becomes less "Are banks gone?" and more:

`Which borrower types and transactions are moving to private credit because private lenders can offer certainty, structure, speed, leverage, or sponsor relationships that banks do not want to hold directly?`

## Claim Upgrade

Old claim:

`Private credit is replacing part of bank lending.`

Better claim after company metrics, bank denominators, BDC borrower data, and bank-credit trends:

`Private credit is not replacing the banking system in the aggregate. It is building a parallel lending channel inside specific borrower and transaction lanes, especially sponsor-backed and senior-secured floating-rate credit, while banks remain huge and often still finance parts of the private-credit ecosystem through credit facilities.`

## Next Evidence Needed

To prove actual substitution, the next dataset cannot be only aggregate bank credit.

It needs one of these:

- borrower-level refinancing evidence
- BDC portfolio industry and sponsor maps
- leveraged lending and direct-lending issuance by use of proceeds
- bank shared-national-credit or syndicated-loan exposure trends
- lender-role data showing bank-to-private-credit transfer by deal type

## Simple Version

Banks are still big and still growing.

Private credit is also big and increasingly borrower-facing.

So the right simple claim is:

`This is not banks disappearing. It is a second lending system growing beside banks, strongest where private lenders can give borrowers speed, certainty, structure, and sponsor relationships.`
