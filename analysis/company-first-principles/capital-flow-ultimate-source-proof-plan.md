# Capital Flow Ultimate Source Proof Plan

## Purpose

The current evidence proves borrower-level credit exposure and visible holder channels.

This plan defines what we need next to prove the deeper question:

Where did the capital behind those credit vehicles actually come from?

Machine-readable queue:

`analysis/company-first-principles/data/capital-flow-ultimate-source-document-queue.csv`

## Current State

We now have three evidence layers:

| Layer | Current Status | What It Proves |
|---|---|---|
| Borrower exposure | Built | Specific operating-company borrowers appear in SEC schedules and transaction sources. |
| Holder/source map | Built | Specific reporting vehicles or platforms hold/arrange borrower exposure. |
| Vehicle taxonomy | Built | The visible holders can be classified as public BDCs, private/non-traded credit vehicles, direct-lending programs, funds, bank facilities, or arranger-only sources. |

The missing fourth layer is ultimate capital source.

## Queue Summary

| Queue Area | Rows | Why It Matters |
|---|---:|---|
| Public BDCs | `5` | Public BDCs are the cleanest visible holder channel, but we still need balance-sheet funding detail. |
| Non-traded BDC / private credit funds | `3` | These may reveal retail/wealth/private-capital distribution channels, but that must be documented. |
| Direct lending program / private credit vehicle | `1` | SDLP is the largest visible funded channel and needs ownership/member-capital proof. |
| Private credit fund | `1` | New Mountain's MAI exposure needs fund/adviser/source detail. |
| Registered credit fund | `1` | CION Ares shows a small Sunvair route and can test registered-fund participation. |
| Middle-market lending fund | `1` | Phillip Street gives historical Relation route evidence that needs vehicle context. |
| Arranger / asset manager | `1` | Ares arranger-only evidence needs credit agreements or rating reports to become facility evidence. |
| Bank displacement test | `1` | Atwell needs payoff, amendment, coexistence, or UCC evidence. |

Total queue rows: `14`.

Current queue status: `8` first-pass extractions complete, `6` rows still queued.

## Priority Order

| Priority | Target | Document To Pull | Upgrade Sought |
|---:|---|---|---|
| 1 | Ares Capital Corporation | Latest 10-K and 10-Q capital structure/funding notes | First pass complete: ARCC holder rows are now tied to public-BDC balance-sheet funding. |
| 2 | Senior Direct Lending Program LLC | Formation, ownership, member-capital, and related-party notes | First pass complete: SDLP holder rows are now tied to ARCC/Varagon joint-venture funding layers. |
| 3 | Ares Strategic Income Fund | Prospectus, registration statement, annual report | First pass complete: ASIF holder rows are now tied to a non-traded BDC/private-credit vehicle with debt, net-asset, share-class, and distribution-channel disclosures. |
| 4 | FS KKR Capital Corp. | Latest 10-K and 10-Q funding notes | First pass complete: FSK holder rows are now tied to a public-BDC balance sheet with debt facilities, unsecured notes, CLO notes, preferred stock, and common equity. |
| 5 | KKR FS Income Trust Select | Prospectus, registration statement, annual report | First pass complete: K-FITS holder rows are now tied to a non-traded BDC/private-credit vehicle with Class S shares, private-offering mechanics, placement-agent distribution, shareholder equity, and revolving credit facilities. |
| 6 | Goldman Sachs BDC Inc. | Latest 10-K and 10-Q funding notes | First pass complete: GSBD holder rows are now tied to a Goldman-managed public-BDC balance sheet with public common equity, a revolving credit facility, unsecured notes, and asset-coverage disclosure. |
| 7 | Goldman Sachs Private Credit Corp. | Prospectus, registration statement, annual report | First pass complete: GSPCC commitment rows are now tied to a non-listed Goldman private-credit BDC with Class I/S/D shares, private-offering mechanics, revolver funding, unsecured notes, and asset-coverage disclosure. |
| 8 | Blue Owl Capital Corporation | Latest 10-K and 10-Q funding notes | First pass complete: OBDC holder rows are now tied to a Blue Owl-advised public-BDC balance sheet with public common equity, a revolving credit facility, SPV asset facilities, CLOs, unsecured notes, and asset-coverage disclosure. |
| 9 | New Mountain Private Credit Fund | Annual report, registration statement, adviser/funding disclosures | Explain MAI private-credit-fund exposure. |
| 10 | CION Ares Diversified Credit Fund | Annual report, prospectus, adviser agreement | Explain Sunvair registered-fund exposure. |
| 11 | Kayne Anderson BDC Inc. | Latest 10-K and 10-Q funding notes | Explain AeriTek Kayne exposure. |
| 12 | Phillip Street Middle Market Lending Fund LLC | Latest annual report and adviser/funding disclosures | Explain historical Relation middle-market route. |
| 13 | Ares Management Corporation transaction cases | Credit agreements, lender allocation schedules, rating reports | Convert arranger role into facility size and lender allocation. |
| 14 | Atwell facilities | Payoff, amendment, UCC, or credit-agreement evidence | Confirm or reject the bank-replacement hypothesis. |

## Extraction Fields

For every vehicle document, extract:

- vehicle type
- adviser and sub-adviser
- debt outstanding
- secured funding facilities
- notes payable
- SPVs or financing subsidiaries
- shareholder or member capital
- subscription/investor channel
- affiliated or related-party transactions
- co-investment arrangements
- any insurance-account or insurer-affiliate links

For every borrower facility document, extract:

- borrower legal name
- sponsor
- administrative agent
- arranger/bookrunner
- lender list
- facility size
- tranche names
- pricing
- maturity
- use of proceeds
- prior debt repayment or refinancing language
- bank role after closing

## Claim Ladder

| Evidence Found | Claim We Can Make |
|---|---|
| Borrower schedule row only | A filing vehicle held borrower debt or commitment exposure. |
| Vehicle taxonomy document | The holder belongs to a specific capital channel. |
| Vehicle funding notes | The channel was funded by named liabilities, notes, facilities, equity, subscriptions, or member capital. |
| Insurer statutory/rating source | Insurance liabilities or insurer accounts supplied capital to the credit channel. |
| Credit agreement / rating report | The borrower facility size, lender group, and use of proceeds can be stated. |
| Payoff / termination / amendment evidence | Bank displacement, coexistence, or no-displacement can be tested borrower by borrower. |

## Simple Bottom Line

We have enough to say private credit is funding real operating companies through identifiable credit vehicles.

We do not yet have enough to say exactly whose money funds each loan.

The next move is to pull vehicle-level documents, not more broad market commentary. Those documents are what turn “Ares-managed holder row” or “Goldman private-credit commitment” into a defensible source-of-capital claim.
