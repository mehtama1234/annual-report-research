# Apollo–Athene AP Aristotle public-search refresh

Research date: `2026-09-16`

## Question

Does the public filing perimeter contain the current AP Aristotle instrument,
its 2025 paydown/settlement record, or a borrower-facing document that can
close the Athene CUSIP cash loop?

## Result

`searched-negative` for the exact Athene route. The checked SEC public search
did not surface CUSIP `00264#-AB-3`, the Athene 2025 paydown settlement, a
current note purchase agreement, a borrower repayment notice, or an Athene
custodian/receipt ledger.

The search did find two older SEC filings containing an AP Aristotle Holdings
LLC name. The [Barings BDC March 31, 2022 filing](https://www.sec.gov/Archives/edgar/data/1379785/000137978522000023/a2022033110qbbdc.htm)
describes an older subordinated term loan with `19.8%` cash, acquired in
December 2021 and due June 2025. The [Barings BDC 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1379785/000137978522000008/a202110-k.htm)
provides similar historical borrower-name context. These are analog sources,
not the Athene 2025 instrument, and their economics are not merged into the
Athene route.

The structured search record is in the [public-search table](data/capital-flow-apollo-athene-aristotle-public-search-refresh-2026-09-16.csv).

## Decision

The public route is now explicitly bounded rather than treated as an
unsearched possibility. AP Aristotle remains a qualified statutory
same-CUSIP/paydown candidate with `776.032348M` of selected cash-like
consideration candidates, but no current public source upgrades it to borrower
receipt, settlement cash, liability-adjusted return, or Apollo common-owner
cash.

## Next source request

Prioritize the exact CUSIP through Athene investment accounting, Apollo/ATLAS
transaction files, the custodian, trustee, broker/dealer, and borrower records:
note purchase or offering documents, paydown notice, trade confirmation,
settlement statement, and receipt ledger.

## Safe claim

`Public SEC search found historical AP Aristotle borrower-name analogs but no
current Athene 2025 instrument or settlement evidence. The analogs improve
historical context only and do not alter the qualified cash-loop boundary.`
