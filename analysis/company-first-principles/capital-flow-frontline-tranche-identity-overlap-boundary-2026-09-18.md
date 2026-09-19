# Frontline Tranche Identity and Overlap Boundary

## Purpose

This artifact separates the current public Frontline observations by legal
borrower name, maturity, pricing, PIK terms, and instrument label. It is a
facility-reconstruction control, not a facility-size estimate.

The central rule is:

> Do not add holder fair values into a promoted facility total unless the
> borrower legal entity, tranche, facility, and period are reconciled.

## Current identity buckets

| Identity bucket | Public borrower name(s) | Maturity | Pricing / PIK marker | Instruments observed | Current interpretation |
|---|---|---|---|---|---|
| A | `Frontline Road Safety LLC` | `03/04/2032` or `03/2032` | SOFR/SF + `4.75%` to `5.00%`; selected `2.00%` to `2.30%` PIK | First-lien term, delayed-draw, revolver | Strong same-period cluster, but holder rows may represent different tranches or participations. |
| B | `Frontline Road Safety Operations, LLC` | `03/2032` or `03/04/2032` | SOFR/S + `4.75%` to `5.00%`; selected `2.00%` PIK | First-lien term, delayed draw, revolver | Likely related borrower family, but legal-entity equivalence is not proven by name similarity. |
| C | `Frontline Road Safety Operations, LLC` | `03/2031` | SOFR + `4.75%`; `2.00%` PIK in the CCLFX schedule | Revolver | A distinct maturity bucket; must not be merged into the 2032 facility without an amendment or credit agreement. |
| D | `Frontline Road Safety Holdings II LLC` | `03/04/2032` | SOFR + `5.00%`; `8.64%` effective yield | Mixed first-lien investment/commitment row and delayed-draw commitment | OHA reports `$1.200M` fair value on `$5.000M` reported par, but footnote (6) says the position or a portion may be unfunded; it separately reports `$3.750M` commitment capacity. |

## Evidence by holder

| Holder | Q2 observation | Identity signal | What remains unresolved | Primary source |
|---|---|---|---|---|
| KKR Enhanced US Direct Lending Fund-L | `03/04/2032`; base term, delayed draws, May 2025 add-on, and revolver; SOFR + `2.50%` to `4.75%`, selected PIK | Explicit tranche labels and add-on chronology | Whether these rows are the same facility Ares arranged and how much was drawn by the borrower | [SEC Q2 filing](https://www.sec.gov/Archives/edgar/data/2012839/000162828026056657/ebdc-20260630.htm) |
| Cliffwater Corporate Lending Fund | `03/2031` and `03/2032` rows; revolver, term, delayed draw; SOFR + `4.75%` | Shows at least two maturity buckets within one holder schedule | Whether 2031 and 2032 instruments are amended, parallel, or separate facilities | [SEC Q2 N-PORT](https://www.sec.gov/Archives/edgar/data/1735964/000173596426000022/ea0302317-01_nport.htm) |
| Ares Strategic Income Fund | `03/2032`; SOFR + `5.00%`, `2.00%` PIK; term loan and undrawn revolver | Direct Ares-managed current exposure | Whether Q1-to-Q2 change was draw, assignment, trade, PIK, or valuation movement | [SEC Q2 supplement](https://www.sec.gov/Archives/edgar/data/1918712/000162828026054928/asifq2-202610qsupplement.htm) |
| Ares Capital Corporation | `03/2032`; approximately `$23.9M` fair value across three funded rows | Direct Ares-managed BDC exposure; includes June 2026 acquisition-date row | Exact tranche and relation to ASIF / arranger facility | [SEC Q2 filing](https://www.sec.gov/Archives/edgar/data/1287750/000162828026050307/arcc-20260630.htm) |
| Sixth Street Lending Partners | `03/2032`; `$40.625M` par / `$38.594M` fair value; separate `$121.875M` delayed-draw commitment | Instrument and commitment are separately disclosed | Whether delayed-draw capacity is shared with other holders' commitment rows | [SEC Q2 filing](https://www.sec.gov/Archives/edgar/data/1925309/000119312526335004/ck0001925309-20260630.htm) |
| KKR FS Income Trust | `03/2032`; five first-lien rows; `$4.559M` commitment capacity | Same legal borrower name as KKR Enhanced but separate vehicle | Whether any rows overlap with K-FITS or KKR Enhanced positions | [SEC Q2 filing](https://www.sec.gov/Archives/edgar/data/1930679/000162828026056131/kfit-20260630.htm) |

## Controlled arithmetic

The controlled lower bound remains:

`FS KKR Capital Corp. $132.800M + KKR FS Income Trust Select $47.936M + Goldman Sachs BDC $17.939M = $198.675M fair value`

The broader current-period figure is a visibility measure only:

`$622.8244M reported fair value + $130.796M reported commitments`

It is not promoted as total facility size because the identity buckets above
are not reconciled. In particular:

- a shared borrower name does not prove a shared tranche;
- a shared maturity does not prove a shared facility;
- fair value does not prove funded principal or borrower cash received; and
- a commitment row does not prove a draw or a cash outflow.

## Promotion gate

The breadth figure can be promoted only if at least one of the following is
obtained:

1. the credit agreement and amendments naming obligors, tranches, commitments,
   and lenders;
2. an agent or lender allocation schedule that maps the public positions to a
   facility; or
3. a settlement / trade / draw record that reconciles holder changes to
   borrower-level cash movement.

Until then, the correct claim is:

`Frontline has broad public holder visibility across related legal borrower names and 2031/2032 first-lien instruments; the full facility and overlap map remain unproven.`

## Decision

`frontline-holder-breadth-expanded; tranche-and-facility-identity-open`

The related public facility-size and bank-replacement search is now bounded in
[the 2026-09-18 search-boundary artifact](capital-flow-frontline-facility-size-search-boundary-2026-09-18.md).
