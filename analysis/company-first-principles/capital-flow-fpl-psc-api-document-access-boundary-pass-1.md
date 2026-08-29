# Capital Flow FPL PSC API Document Access Boundary Pass 1

## Purpose

This pass tests whether the Florida PSC public app exposes a deeper document-detail or attachment route for FPL `20260010-EI` discovery materials.

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-fpl-psc-api-document-access-boundary-pass-1.csv`

The upstream discovery/audit route pass is:

`/cluster/capital-flow-fpl-2026-discovery-audit-receipt-proof-route-pass-1.md`

## Question

`Can the PSC public API move us beyond docket notices into actual FPL discovery answers, POD productions, workpapers, or attachment files?`

## Short Answer

`No public API upgrade found. The PSC app exposes useful endpoints for docket filing inventory and document-number lookup. Those endpoints return document descriptions, document IDs, file metadata, and public PDF links. For the sampled FPL discovery/audit route, they do not expose hidden attachments, served answer packages, POD production files, billing determinant workpapers, category receipt ledgers, source-of-funds schedules, legal-entity waterfalls, collateral/funding certificates, or return models.`

## Access Table

| Gate | Current Evidence | Status | Boundary |
|---|---:|---|---|
| App endpoint discovery | PSC app bundle exposes `PSCDocketFilingsDetails` and `DocketDetailsByDocumentNumber`. | `api-route-visible` | Endpoint existence is not cash proof. |
| Docket inventory endpoint | `PSCDocketFilingsDetails` returned `138` records for `20260010-EI`. | `docket-api-visible` | Inventory is not discovery substance. |
| Document detail endpoint | `DocketDetailsByDocumentNumber` returned document id, description, metadata, and PDF link for DN `03417-2026`. | `document-detail-visible` | No extra workpaper files appeared. |
| Response notice lookup | FPL response notice document numbers route back to public notice PDFs. | `response-metadata-only` | Notices are not answers or schedules. |
| Request notice lookup | Staff/Panama City request document numbers route to certificates/notices. | `request-metadata-only` | Certificates are not interrogatory/POD text. |
| Confidential inventory scan | Sampled inventory PDFs DN `04110-2026` and DN `04480-2026` did not surface target FPL billing/receipt entries. | `no-target-confidential-index-found` | Does not rule out later or separate confidentiality filings. |
| Audit workpaper access | DN `03417-2026` says no confidential workpapers were associated with the audit. | `audit-workpaper-boundary-visible` | Audit route does not provide category cash proof. |
| Public access verdict | Public API stops at docket/document metadata plus visible PDFs for this test. | `hold-public-api-stops-at-notice-layer` | Full named cash proof remains missing. |

## Stop Rule

Do not keep re-querying the same PSC public docket/document endpoints as if they will reveal the served discovery contents. The next upgrade requires a new source class:

1. actual served FPL discovery answers
2. actual POD production attachments
3. docket-specific confidentiality requests, orders, or indexes
4. hearing exhibits
5. staff recommendation workpapers
6. public records request output
7. party-file material from Panama City or another intervenor

## Decision

`fpl-psc-api-document-access-boundary-hold-public-api-stops-at-notice-layer`

The public API is useful for inventory, route control, and document metadata. It does not currently unlock FPL named cash proof.

## Safe Claim

`Florida PSC public endpoints can enumerate the current FPL 20260010-EI docket and retrieve document-number metadata, but the tested route stops at public certificates, notices, audit summary material, and PDF links. The public API layer sampled here does not expose FPL Distribution Inspection-specific billing determinants, billed or collected customer cash, category receipt allocation, source-of-funds allocation, legal-entity funding waterfall, collateral/funding certificate, earned ROE, IRR, NPV, payback, or full named cash return.`
