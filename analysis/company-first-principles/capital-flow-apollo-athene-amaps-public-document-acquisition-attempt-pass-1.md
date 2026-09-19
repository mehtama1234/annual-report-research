# Capital Flow Apollo Athene AMAPS Public Document Acquisition Attempt Pass 1

## Purpose

This pass executes the first public acquisition attempt against the AMAPS controlled-document request packet.

The question is:

`Can any AMAPS 1 documents needed for cash-all-the-way-through proof be found publicly, or are the routes access-controlled, analog-only, or not found?`

The acquisition-attempt table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-amaps-public-document-acquisition-attempt-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-amaps-public-document-acquisition-attempt-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-amaps-public-document-acquisition-attempt.py`

## Main Result

All `9` AMAPS document families were tested.

| Status | Rows | Meaning |
|---|---:|---|
| located / access-controlled | `1` | AMAPS 1 appears to have a DealX document route, but content was not accessible |
| public proxy or analog found | `3` | public Apollo, KBRA, Fitch, S&P, and AMAPS 4/5 sources improve wrapper/collateral/waterfall context, but not AMAPS 1 proof |
| public consolidated exposure found | `1` | Apollo/Athene public filing confirms AMAPS 1 concentration, but not subsidiary reconciliation |
| AMAPS 1 not found publicly | `4` | no public tranche/trade, trustee/remittance, allocation/custodian, or return-model source was found |

No row upgraded to AMAPS 1 collateral-tape proof.

No row upgraded to Athene receipt proof.

No row upgraded to return-model proof.

All `9` document families remain controlled-document-needed.

## 2026-09-18 exact-route recheck

A narrow public-source recheck searched the exact CUSIP `02300A-AA-8`, the
named statutory counterparty `Apollo Capital Markets Partner`, and the AMAPS 1
consideration amount across SEC, Apollo, and Athene domains. It returned no
relevant public result. This is a searched-negative for the public perimeter,
not evidence that controlled or private settlement records do not exist. It
does not change the proof grade or replace the requested trade, custodian,
trustee, and allocation documents.

## Attempt Outcomes

| Request | Document Family | Attempt Status | Proof Effect |
|---|---|---|---|
| `CFAAAMAPSDR-001` | AMAPS 1 offering memorandum | `located-access-controlled` | DealX appears to index `AMAPS 1 - ABS`, but no offering memorandum content was accessible. |
| `CFAAAMAPSDR-002` | tranche supplement and note purchase agreement | `not-found-public` | CUSIP `02300A-AA-8` remains visible only in local Athene statutory rows, not public tranche or purchase documents. |
| `CFAAAMAPSDR-003` | full rating rationale reports | `amaps-1-not-found-public-amaps-4-5-analog-and-premium-routes-visible` | AMAPS 4/5 rating actions and premium report routes are visible; no AMAPS 1-specific public rating rationale was found. |
| `CFAAAMAPSDR-004` | collateral tape or portfolio schedule | `public-collateral-category-proxy-found-tape-not-found` | Public Apollo and AMAPS 4/5 sources describe collateral categories and diversification; no AMAPS 1 collateral tape was found. |
| `CFAAAMAPSDR-005` | trustee remittance and noteholder reports | `not-found-public` | U.S. Bank Trust Investor Reporting public search did not show AMAPS/AMAPS 1; no remittance reports were located. |
| `CFAAAMAPSDR-006` | payment waterfall and LTV test support | `public-analog-waterfall-proxy-found-amaps-1-waterfall-not-found` | AMAPS 4/5 public releases describe LTV and waterfall-style mechanics; no AMAPS 1 waterfall was found. |
| `CFAAAMAPSDR-007` | Athene allocation, trade, and custodian support | `not-found-public` | No public Athene AMAPS 1 trade, custodian, allocation, or cash-ledger evidence was found. |
| `CFAAAMAPSDR-008` | statutory subsidiary reconciliation | `public-consolidated-exposure-found-subsidiary-reconciliation-not-found` | Apollo/Athene public filing confirms `2.550B USD` AMAPS 1 concentration, but no subsidiary reconciliation was found. |
| `CFAAAMAPSDR-009` | liability-cost and return model support | `not-found-public` | No AMAPS 1-specific Athene liability-cost, spread, IRR, NPV, ROIC, or payback model was found. |

## What The Search Improved

The public search improved the AMAPS route in four ways:

1. The AMAPS 1 document route is not purely hypothetical. DealX appears to index `AMAPS 1 - ABS`, although access/content was not obtained.
2. AMAPS 4 and AMAPS 5 rating-agency sources describe the AMAPS format: multi-asset investment strategy, corporate credit, asset-backed finance, private and broadly syndicated lending, LTV tests, asset coverage, redemption gates, income proceeds, debt payment sequence, and sequential repayment mechanics.
3. Apollo's public AMAPS materials support wrapper identity, collateral-category direction, tranche/CUSIP framing, and Apollo/Athene alignment.
4. Apollo/Athene SEC disclosure confirms AMAPS 1 as a material public concentration, which gives a reconciliation target against local Athene statutory Schedule D rows.

## What Still Blocks Full Proof

The hard documents remain missing:

1. actual AMAPS 1 offering memorandum
2. actual tranche supplement and purchase/support documents for CUSIP `02300A-AA-8`
3. AMAPS 1 full rating rationale or private-letter-rating support
4. AMAPS 1 collateral tape or portfolio schedule
5. trustee remittance and noteholder reports
6. AMAPS 1 priority-of-payments, waterfall, LTV, and trigger calculations
7. Athene allocation, trade, custodian, and cash-ledger support
8. subsidiary reconciliation from local Athene row to public AMAPS 1 concentration
9. liability-cost and return model support

## What This Tells Us In Simple Terms

AMAPS did not turn into full public proof.

The route got sharper:

`Athene statutory CUSIP row -> AMAPS 1 note -> Apollo AMAPS wrapper -> DealX/rating-agency controlled routes -> missing AMAPS 1 collateral/remittance/return documents`

The public evidence is enough to know what to ask for next. It is not enough to prove who all the underlying borrowers are, how collateral cash moved through the waterfall, what Athene actually received, or what Athene earned after liability cost.

## What This Proves

This pass proves:

1. all `9` AMAPS controlled-document families were tested through public routes
2. DealX appears to index an AMAPS 1 ABS route
3. AMAPS 4/5 rating-agency public releases and premium routes can guide AMAPS 1 document requests
4. Apollo/Athene public filing gives a `2.550B USD` AMAPS 1 concentration reconciliation target
5. trustee reports, Athene allocation support, and return model support were not found publicly
6. the next step is access/request execution, not more broad AMAPS description

The exact-route recheck reinforces that stop rule: do not repeat broad public
searches unless a new filing or transaction-specific source appears.

## What It Does Not Prove

This pass does not prove:

1. the AMAPS 1 offering memorandum was obtained
2. the AMAPS 1 tranche supplement was obtained
3. AMAPS 1 collateral tape was obtained
4. trustee reports were obtained
5. Athene received AMAPS cash through a verified remittance or custodian record
6. AMAPS 1's pooled collateral generated enough cash for a specific distribution
7. Athene's statutory row reconciles to the full public AMAPS 1 concentration across subsidiaries
8. Athene earned a liability-adjusted spread or return
9. IRR, NPV, ROIC, cash-on-cash return, or platform profit

## Safe Claim

`The first AMAPS public document acquisition attempt tested all nine controlled-document families. Public search located an access-controlled DealX route for AMAPS 1 ABS, confirmed Apollo/Athene's public 2.550B USD AMAPS 1 concentration, and found AMAPS 4/5 rating-agency analog and premium routes that clarify collateral and waterfall-style mechanics. It did not find AMAPS 1 offering contents, tranche purchase support, collateral tape, trustee remittance, Athene allocation/trade support, subsidiary reconciliation, liability-cost support, or return-model proof. AMAPS remains a strong Apollo/Athene wrapper-and-alignment case, not full named cash proof.`

## Decision

`amaps-public-document-route-located-full-proof-access-controlled`

The next move is to pursue access-controlled routes first:

1. DealX AMAPS 1 ABS documents
2. KBRA/Fitch/S&P/Moody's AMAPS 1 full rating or private-letter-rating support
3. Apollo/Athene AMAPS 1 offering and tranche records
4. trustee or collateral administrator remittance reports
5. Athene allocation, custodian, statutory subsidiary, and liability-cost support

## Source Links

- DealX AMAPS ABS list: `https://dealx.com/reportstream/deallist/33`
- Apollo AMAPS product article: `https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps`
- Apollo/Athene SEC investment disclosure: `https://www.sec.gov/Archives/edgar/data/1527469/000152746926000013/R12.htm`
- KBRA AMAPS 4 public rating release: `https://www.kbra.com/publications/QHVDGMYg`
- KBRA AMAPS 5 public rating release: `https://www.kbra.com/publications/KDBMTzJQ`
- KBRA Funds publications/premium report route: `https://www.kbra.com/sectors/funds/publications?pageNumber=3`
- S&P AMAPS 5 presale route: `https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101689861`
- Fitch AMAPS 5 presale route: `https://www.fitchratings.com/research/structured-finance/amaps-5-llc-presale-report-11-06-2026`
- U.S. Bank Trust Investor Reporting public deal search: `https://trustinvestorreporting.usbank.com/TIR/public/deals/`
