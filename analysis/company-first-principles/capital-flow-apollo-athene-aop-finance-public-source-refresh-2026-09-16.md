# Apollo–Athene AOP Finance Partners public-source refresh

Research date: `2026-09-16`

## Question

Can public sources connect the Athene AOP Finance Partners statutory disposal
candidates to an Apollo/Athene-controlled investment vehicle, identify the
economic destination, and support a cash-return or return calculation?

## Result

`evidence-insufficient` for exact CUSIP settlement, borrower or collateral
cash, liability-adjusted return, or Apollo common-owner cash, with a meaningful
legal-entity and economic-benefit upgrade.

Athene's 2021 Form 10-K identifies AOP Finance Partners, LP (AOP) as one of
Athene's consolidated primary variable-interest entities. The same disclosure
reports `$747M` of AOP investment-fund assets at December 31, 2021 and says
Athene was the only limited partner or holder of profit-participating notes in
the listed investment funds, receiving the economic benefits and losses other
than management fees and carried interest paid to an Apollo affiliate or other
related general partner. Athene's subsidiary exhibit also lists AOP Finance
Partners, LP as a Delaware subsidiary.

The current statutory disposal parser identifies two AOP instruments:

- `00196#-AA-8`, AOP Finance Partners LP AOP 6.132% due 03/31/41: two
  disposal rows, approximately `$451.859M` of consideration and `$31.093M`
  of interest/dividend fields.
- `00196#-AB-6`, AOP Finance Partners LP AOP 7.132% due 03/31/41: two
  disposal rows, approximately `$233.026M` of consideration and `$20.698M`
  of interest/dividend fields.

Together these are approximately `$684.884M` of consideration and `$51.791M`
of interest/dividend fields. The rows are disposal-only in the current parser;
there is no year-end holding match. Their `Paydown` classification makes them
cash-like candidates, not proof that cash was received by Athene. The statutory
fields do not establish whether each row represents a full paydown, a partial
redemption, a sale, a transfer, or a corrected identifier.

## Decision

Promote AOP from a generic named issuer to an Apollo/Athene-controlled
investment-vehicle route with a documented economic-benefit perimeter. Do not
promote the statutory consideration to borrower repayment, Athene receipt,
liability-adjusted spread, realized IRR/NPV, or Apollo common-owner cash.

Keep AOP separate from newer AOP II origination vehicles. The 2024–2026 SEC
filings for Apollo Origination II provide useful platform and collateral-
administrator context, but they are not substitutes for AOP's 2025 statutory
lot, borrower, or settlement records.

## Next documents

Request AOP's applicable offering memorandum, loan or investment schedule,
administrator/trustee reports, paydown or redemption notices, Athene trade
confirmations, custodian settlement ledger, and any borrower-level repayment
or collateral report. Then reconcile principal, accrued interest, fees, funding
cost, insurance-liability cost, taxes, and the residual available to Athene and
Apollo common owners.

## Safe claim

`Public SEC sources establish that AOP Finance Partners was an Athene-
consolidated investment vehicle in 2021 and that Athene received its economic
benefits and losses subject to related-party management and carry economics.
The 2025 AOP statutory disposal rows are named cash-like candidates, not
proven settlements, borrower receipts, liability-adjusted returns, or common-
owner cash.`

## Sources

- [Athene 2021 Form 10-K: AOP VIE and economic-benefit disclosure](https://www.sec.gov/Archives/edgar/data/1527469/000152746922000018/R14.htm)
- [Athene 2021 Exhibit 21.1 subsidiary list](https://www.sec.gov/Archives/edgar/data/1527469/000152746922000018/q42021exhibit211.htm)
- [AOP Finance Partners SEC filer record](https://www.sec.gov/Archives/edgar/data/1852976/000119312524169125/0001193125-24-169125-index.htm)
- [Apollo Origination II loan and security agreement](https://www.sec.gov/Archives/edgar/data/2052152/000119312525065612/d880406dex105.htm)

