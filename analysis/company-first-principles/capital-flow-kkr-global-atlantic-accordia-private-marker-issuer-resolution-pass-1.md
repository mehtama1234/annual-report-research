# Capital Flow KKR Global Atlantic Accordia Private-Marker Issuer Resolution Pass 1

Research date: `2026-09-17`

## Purpose

This pass resolves the highest-interest unresolved Accordia private-marker
row selected in the [Apollo-vs-KKR named-asset selection](capital-flow-apollo-kkr-statutory-named-asset-selection-pass-1.md).

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-kkr-global-atlantic-accordia-private-marker-issuer-resolution-pass-1.csv`

The question is:

`Can the private-marker CUSIP 90231*-AA-0 be assigned a source-visible issuer name without confusing statutory row text with full legal-instrument or borrower-cash proof?`

## Resolution

Yes, at the source-row level.

The Accordia Schedule D coordinate row on source page `240` identifies:

| Field | Source-visible value |
|---|---:|
| Private-marker CUSIP | `90231*-AA-0` |
| Issuer text in raw Schedule D row | `2023 BEAR FINANCING L.P.` |
| Schedule | Part 1, Section 1 issuer-credit obligations owned |
| Book-adjusted carrying value | `$202.125M` |
| Actual cost / par value | `$202.125M` / `$202.125M` |
| Fair value | `$202.145213M` |
| Stated / effective rate | `8.500%` / `6.999%` |
| Interest due/accrued | `$6.585906M` |
| Interest received during year | `$17.419245M` |
| Acquired / maturity date | `01/05/2024` / `01/05/2039` |

The raw parser's source text places the row immediately after the affiliated
corporate-bond subtotal and before the corresponding subtotal close. The
coordinate pass includes it in the near-reconciled owned-bond base of
`$7.318321094B` versus the statutory target of `$7.318322163B`, a `$1,069`
variance.

## What this upgrades

The row can now move from:

`private-marker CUSIP with no issuer name in the selected match table`

to:

`Accordia legal entity -> source-visible 2023 Bear Financing L.P. row -> $202.125M owned bond -> $17.419245M interest received`

This is useful because it gives the comparison lane a named private-credit or
corporate-finance issuer target alongside the standard-CUSIP Intel, Orange,
Wells Fargo, and Commonwealth Edison rows.

## What remains unproved

The source-row issuer text is not yet a complete legal-entity identity packet.
The following still require separate support:

- private-placement or offering documents confirming the issuer, instrument,
  and security terms;
- borrower or sponsor identity and use of proceeds;
- exact lot continuity and any acquisition/disposal coordinates;
- custodian, broker, or bank evidence for interest settlement;
- reinsurance, funds-held, or liability-cost allocation;
- credit-loss, tax, fee, and realized-return treatment; and
- any KKR, Global Atlantic, or common-owner residual allocation.

The `$17.419245M` field is statutory interest received during the year. It is
not by itself borrower cash, a trustee remittance, or platform profit.

## Next source request

Request the 2023 Bear Financing L.P. private-placement or rating package,
Accordia's investment subledger and custodian statement for CUSIP
`90231*-AA-0`, and the related ALM or liability-cost allocation. Search the
Accordia acquired and disposed Schedule D sections for the same private-marker
family before attempting a return calculation.

## Safe claim

`Accordia's highest-interest private-marker row is now source-visible as 2023 Bear Financing L.P. CUSIP 90231*-AA-0. The coordinate Schedule D row carries $202.125M of book value and $17.419245M of interest received, within a near-reconciled $7.318321094B owned-bond base. This upgrades issuer targeting and legal-entity cash-back proxy analysis, but it does not prove the private instrument's full legal identity, borrower use, settlement, liability-cost-adjusted return, or KKR/common-owner cash.`

## Decision

`accordia-private-marker-issuer-source-row-resolved; instrument-settlement-and-return-open`
