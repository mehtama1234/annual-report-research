# Apollo/Athene Schedule DB Part C named-lot control — pass 1

This control ledger narrows the exact-CUSIP crosswalk to named MF1, AMAPS, Atlas, Varde, and Ares instruments. It is an exposure and identity control, not a settlement, liability-allocation, repayment, or Apollo-owner-cash bridge.

- Included `52` named CUSIP controls from the Part C ↔ Schedule D crosswalk.
- Families: AMAPS `2`, ARES `20`, ATLAS `3`, MF1 `23`, VARDE `4`.
- Statuses: `matched-identity-component-exposure-control` `51`, `matched-identity-with-ambiguous-part-c-candidate` `1`.
- Part C values are summed only when a row exposes one unambiguous numeric candidate. Pipe-separated alternatives remain in the raw columns and are excluded from the numeric aggregate.
- A difference between a Part C component and a Schedule D holding is not treated as an error or a cash-flow match; it is a perimeter/control signal because Part C presents replication components while Schedule D presents statutory holdings.

## What this advances

The ledger gives the next reviewer a reproducible page/CUSIP queue: named derivative component, Schedule D row, statutory book/fair value, interest income, and interest received. It identifies where a custody or transaction-level document could connect a derivative component to a legal-entity cash or liability bridge.

## What remains unproven

- derivative cash settlement and counterparty remittance;
- whether Schedule D interest received was collected into Athene cash for the matched lot;
- policyholder-liability or product-level hedge-cost allocation;
- borrower/project repayment or asset-level return; and
- cash available to Apollo common owners.

The machine-readable ledger is [here](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-control-pass-1.csv).
