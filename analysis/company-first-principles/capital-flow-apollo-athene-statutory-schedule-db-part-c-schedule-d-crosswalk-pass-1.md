# Apollo/Athene Schedule DB Part C to Schedule D crosswalk pass 1

Research date: `2026-09-18`

## Crosswalk result

The `735` Schedule DB Part C cash-component rows were matched by exact CUSIP
string against the corrected Schedule D full-range population:

- `728` Part C rows matched Schedule D;
- the crosswalk contains `743` rows because some Part C components reuse the
  same Schedule D CUSIP under multiple derivative/replication identifiers;
- `586` unique cash-instrument CUSIPs matched; and
- `7` Part C rows remain unmatched because their source identifiers are
  private/asterisked or malformed in the PDF text layer.

The structured crosswalk is in the [Schedule DB–Schedule D crosswalk CSV](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-schedule-d-crosswalk-pass-1.csv).

## Named matches

| Part C cash instrument | Schedule D result | Schedule D book value | Schedule D interest income | Schedule D interest received |
|---|---|---:|---:|---:|
| `592918-AE-6` / MF1 2025-B2 B | exact CUSIP; `04687#AB4` | `$57.647M` | `$135.731K` | `$2.526M` |
| `592918-AG-1` / MF1 2025-B2 C | exact CUSIP; `04687#AB4` | `$39.961M` | `$98.751K` | `$1.831M` |
| `592918-AC-0` / MF1 2025-B2 AS | exact CUSIP; `04687#AH1` | `$90.000M` | `$201.406K` | `$3.763M` |
| `02300A-AA-8` / AMAPS 1 Tranche A | exact CUSIP; two Part C parent routes | `$1.9175B` | `$48.871M` | blank in corrected Schedule D row |
| `02300A-AC-4` / AMAPS 1 Tranche B | exact CUSIP; `04687#AG3` | `$367.000M` | `$10.883M` | blank in corrected Schedule D row |
| `049400-AA-2` / Atlas secured advance funding | exact CUSIP; two Part C parent routes | `$1.4125B` | `$255.100K` | `$19.017M` |
| `91835W-AA-7` / Varde Partners | exact CUSIP; three Part C parent routes | `$422.174M` | `$916.672K` | `$16.119M` |

These are identity and statutory holding/income joins. They do not prove that
Schedule DB derivative cash settled, that Schedule D interest was remitted by a
borrower, or that any amount reached Apollo common owners.

## Boundary

The crosswalk is exact at the CUSIP-string level, but repeated CUSIPs under
multiple Part C derivative identifiers require lot-level and component-level
allocation. The Schedule D row is a year-end holding row; it does not itself
prove the derivative contract's counterparty, collateral, termination cash,
policyholder hedge purpose, liability cost, or parent receipt.

## Decision

`named-schedule-db-to-schedule-d-identity-and-income-join-visible; lot-settlement-and-liability-allocation-open`

The next promotion-quality object is a matched-lot ledger that reconciles the
Part C component values, Schedule D book/fair values, derivative termination
flows, counterparties/custody, and product/liability hedge assignment.
