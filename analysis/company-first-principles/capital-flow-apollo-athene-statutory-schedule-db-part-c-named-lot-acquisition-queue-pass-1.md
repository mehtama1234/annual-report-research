# Apollo/Athene named-lot acquisition queue — pass 1

This queue converts the named Part C ↔ Schedule D control into a targeted evidence request order. It is a source-acquisition worklist, not evidence that the requested records exist or that cash was received.

- `52` named CUSIP routes retained; tiers: A `8`, B `30`, C `14`.
- Ranking prioritizes Schedule D statutory book value, then received interest, while placing source-column ambiguity in Tier A for resolution.
- The minimum decisive object is deliberately specific: page-level column support, custody, trustee/paying-agent remittance, transaction settlement, or lot-level income allocation.
- A targeted local-corpus check found no new decisive custody, trustee, or settlement record for the front AMAPS, Atlas, MF1, or Varde routes. The AMAPS route already has a dedicated [controlled-document request packet](capital-flow-apollo-athene-amaps-controlled-document-request-packet-pass-1.md); use that packet rather than repeating broad public searches.

## Promotion rule

Do not promote a queue row to Athene cash, liability-adjusted return, borrower repayment, or Apollo common-owner cash unless the requested object joins the exact legal entity, period, CUSIP/lot, counterparty or payer, amount, and cash/claim disposition.

The machine-readable queue is [here](data/capital-flow-apollo-athene-statutory-schedule-db-part-c-named-lot-acquisition-queue-pass-1.csv).
