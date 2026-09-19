# Apollo/Athene statutory Schedule BA full-range parser pass 1

## What this pass establishes

The Athene Annuity and Life Company 2025 statutory statement can now be parsed across the located Schedule BA detail ranges:

| population | pages | rows | safe interpretation |
|---|---:|---:|---|
| Schedule BA Part 1 | 5813–5825 | 188 | visible year-end owned-asset rows |
| Schedule BA Part 2 | 5826–5829 | 96 | current-year acquisitions/additions; not automatically year-end holdings |
| Schedule BA Part 3 | 5830–5835 | 84 | current-year disposals/transfers/repayments; not automatically recurring income |
| **Total** | **5813–5835** | **368** | repeatable named Schedule BA row population |

The raw detail output is [capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-full-range-parser-pass-1.csv). Visible subtotal/control rows are preserved separately in [capital-flow-apollo-athene-statutory-schedule-ba-control-reconciliation-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-control-reconciliation-pass-1.csv).

## First control reconciliation

The Part 1 detail total on page 5825 is source-visible as:

`7099999 - Totals ... 15,285,961,900 ... 17,724,920,754 ... 17,461,797,562 ...`

The third amount is the apparent Part 1 book/adjusted carrying-value control. The statutory verification/summary extraction records Schedule BA net admitted or statement value of `$17,387,119,006` and the earlier BA verification control records approximately `$17,461,797,563` for the book/adjusted carrying-value column. Therefore:

- the full-range parser captures the expected Part 1 control row;
- its visible book/adjusted carrying value is `$17,461,797,562`, one dollar below the verification control’s `$17,461,797,563`;
- the difference between the book/adjusted carrying-value control and the statement/net-admitted value is approximately `$74.679M`, so those columns must not be conflated;
- the one-dollar difference is a rounding/source-rendering reconciliation item, not permission to adjust individual rows.

## Boundaries

This is a population and control-row pass, not final Schedule BA accounting. The parser preserves raw row text, source blanks, schedule population, identifier, detected NAIC designation, and rough asset class. It does not yet promote row-level numeric slots to actual cost, fair value, book value, income, distributions, repayment, borrower receipt, or owner cash. Part 2 and Part 3 rows describe additions and disposals/transfers and require event matching before they can be combined with Part 1.

The current output detects 74 NAIC designations across the 368 named rows. The next safe upgrade is Part 1 income and commitment review, followed by matching Part 2/3 events without double counting. Only after that should Schedule BA income/proceeds be joined to the legal-entity income/cash bridge.

## Coordinate-column upgrade

The Part 1 coordinate parser is now available at [capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-parser-pass-1.csv), with its control output at [capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-reconciliation-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part1-coordinate-reconciliation-pass-1.csv). It identifies `436` table rows, including rows without a CUSIP, and preserves the fixed columns for actual cost, fair value, book/adjusted carrying value, valuation change, impairment, investment income, commitments, and ownership percentage.

The coordinate-level book/adjusted-carrying-value sum is `$17,461,797,566` against the page-5825 detail control of `$17,461,797,562`, a `$4` difference. `432` rows have a visible book value; four sparse rows remain blank in the source. This is an aggregate control-near-tie, not permission to impute those four cells or to claim holding-level cash return. The coordinate method is materially stronger than compact numeric-token positions because it keeps blank statutory columns in their source locations.

The same control comparison currently shows:

| Part 1 field | coordinate sum | page-5825 control | difference | status |
|---|---:|---:|---:|---|
| Actual cost | `$15,285,961,900` | `$15,285,961,900` | `$0` | tied |
| Fair value | `$17,724,920,753` | `$17,724,920,754` | `-$1` | near-tie |
| Book/adjusted carrying value | `$17,461,797,566` | `$17,461,797,562` | `+$4` | near-tie |
| Investment income | `$237,086,006` | `$237,086,005` | `+$1` | near-tie after token-center repair |
| Commitment for additional investment | `$4,368,051,290` | `$4,368,051,289` | `+$1` | near-tie after token-center repair |

The token-center repair resolves the prior column-bleed differences to one dollar each. These are now control near-ties, not evidence of cash received, cash distributable to Apollo, or borrower repayment. Page 18’s broader “Other invested assets” income category should not be used as a shortcut to force a Part 1 tie because it covers a wider statutory perimeter than the named BA Part 1 holding rows.

The [BA income-category boundary](capital-flow-apollo-athene-statutory-ba-income-category-boundary-pass-1.md) makes the difference explicit: Part 1 row income is positive `$237,086,006`, while page 18 reports Other invested assets income of `$(185,080,219)` collected and `$(132,204,517)` earned. This is an unresolved perimeter/definition break, not permission to promote either figure to BA cash.

## Part 2 coordinate population

The Part 2 coordinate pass is available at [capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-parser-pass-1.csv), with its reconciliation at [capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-reconciliation-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part2-coordinate-reconciliation-pass-1.csv). It identifies `184` acquisition/addition rows, including blank-CUSIP rows, and separates acquisition cost from additional investment made after acquisition.

The corrected Part 2 coordinate sums tie the page-5829 controls within rounding: acquisition-cost extraction is `$6,030,604,899` versus `$6,030,604,898` (`+$1`), and additional-investment extraction is `$3,822,866,876` versus `$3,822,866,876` (`$0`). Part 2 remains an event ledger and must not be added to Part 1 year-end assets until event matching is complete.

## Part 3 disposal/transfer continuity

The Part 3 coordinate parser is available at [capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-part3-coordinate-parser-pass-1.csv). It produces `168` source-visible disposal/transfer/repayment rows across pages 5830–5835 and a [same-CUSIP Part 1 match ledger](data/capital-flow-apollo-athene-statutory-schedule-ba-part3-part1-cusip-match-pass-1.csv). `65` rows have the same CUSIP visible in both Part 3 and the Part 1 year-end ledger. The coordinate disposal-consideration sum is `$4,417,190,618`, within `$2` of the page-450 verification control of `$4,417,190,620`.

This is a named continuity clue, not bank-receipt proof. Consideration can reflect a statutory disposal event without proving settlement account, borrower repayment, tax/fees, liability release, or Apollo distribution. The next event-level repair is to reconcile Part 3 rows to the Part 1 lot/holding and Part 2 acquisition rows without double-counting transferred assets.

The consolidated [BA event-continuity ledger](data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv) classifies the 168 Part 3 rows as:

- `61` same-CUSIP Part 1 + Part 2 + Part 3 rows;
- `4` same-CUSIP Part 1 + Part 3 rows;
- `17` same-CUSIP Part 2 + Part 3 rows;
- `2` Part 3 CUSIPs with no Part 1 or Part 2 match;
- `84` blank-CUSIP events with no continuity key.

Across the coordinate population, visible disposal consideration is `$4,417,190,618` and visible book value on disposal is `$4,394,911,942`. The extracted total gain/loss is `$(73,966,794)`, within `$3` of the page-450 control `$(73,966,791)`. These are statutory event-level controls, not realized owner returns; the settlement account, fees, taxes, liability release, and recipient remain unproven.

The continuity ledger now adds a conservative same-identifier book-value screen: `4` Part 3 rows are within `$1` of the summed Part 1 book value, `6` are within `$1M`, and `55` show a larger or multi-lot difference; `103` rows have no Part 1 amount screen because they are blank-CUSIP or lack a Part 1 match. This is useful for prioritizing lot review, but it does not prove that a Part 3 event is the same economic lot, that consideration settled through a bank account, or that proceeds reached Apollo.

The [lot-review queue](capital-flow-apollo-athene-statutory-schedule-ba-lot-review-queue-pass-1.md) preserves the ten strongest screens—four exact-within-$1 and six near-within-$1M—with Part 1, Part 2, and Part 3 page references plus consideration and gain/loss. It is an investigation queue only.

The Part 3 coordinate parser now also preserves the disposal-nature source column. The [sale review queue](capital-flow-apollo-athene-statutory-schedule-ba-sale-review-queue-pass-1.md) contains `57` rows whose source-column value is exactly `Sale`, totaling `$1,847,866,086` of coordinate-extracted consideration. This is a follow-up priority list, not settlement or owner-cash proof.

The [BA-to-Schedule-D crosswalk](capital-flow-apollo-athene-statutory-schedule-ba-sale-schedule-d-crosswalk-pass-1.md) finds only `3` same-CUSIP matches among those 57 rows. Two are Schedule D `Security Withdraw` rows marked noncash/transfer holds; one has a Schedule D cash-like candidate classification but a different consideration perimeter. This sharpens the boundary: most BA sale rows cannot be treated as Schedule D cash receipts by identifier alone.

The [settlement-search boundary](capital-flow-apollo-athene-ba-sale-settlement-search-boundary-pass-1.md) records a targeted local-corpus search for the five largest explicit-sale rows. No independent settlement, trustee, custodian, or borrower-receipt document was located in the current source set; these remain primary-document follow-up targets.

## Blank-CUSIP name-candidate bridge

The [blank-CUSIP candidate ledger](data/capital-flow-apollo-athene-statutory-schedule-ba-blank-cusip-name-candidates-pass-1.csv) tests the 50 Part 3 events without identifiers against Part 1 and Part 2 row names. It produces `19` unique high-coverage candidates, `25` ambiguous or partial candidates, and `6` events without a strong candidate. Examples include AP Aristotle, CD&R Friends & Family, Shattuck, Italian AIF, ABN AMRO, CNP Assurances, and several European bank perpetual rows.

The refreshed candidate ledger covers `84` blank-CUSIP Part 3 events and produces `33` unique high-coverage candidates, `42` ambiguous or partial candidates, and `9` events without a strong candidate. These are investigation candidates only. The coordinate text combines name, location, purchaser, and disposal fields, and several issuers have multiple Part 1 lots. No fuzzy name candidate is promoted into the continuity ledger until the underlying page row, CUSIP/identifier, lot terms, and event amount agree.

## End-to-end significance

This advances the Apollo/Athene route from a summary Schedule BA balance to a named legal-entity asset population. It still does not prove where an ultimate borrower received cash, how liabilities were funded or charged, what distributions returned to Apollo, or the asset-level return. Those remain required joins in the broader chain:

`policyholder/deposit liabilities → Athene legal entity → named Schedule BA asset → income/distribution or disposal proceeds → liability cost → Apollo/Athene owner cash → valuation and thesis breaker`.
