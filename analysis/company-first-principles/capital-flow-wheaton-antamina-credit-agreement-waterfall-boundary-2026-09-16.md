# Wheaton–Antamina credit-agreement waterfall boundary

Research date: `2026-09-16`

## 2026-09-18 executed-borrowing upgrade

Wheaton's filed Q2 2026 financial statements now provide a source-visible
borrowing event that is distinct from the March credit agreement. The filing
states that the Company drew the new `$1.500B` non-revolving Term Loan on
April 1, 2026 and used it, together with a Revolving Credit Facility draw, to
partially fund the BHP Antamina PMPA. The debt note reports `$1.500B` of gross
Term Loan debt outstanding at June 30, 2026. This proves that the facility was
funded and gives the drawn principal amount; it does not expose the executed
Drawdown Notice, designated payee, agent funding record, or BHP seller-account
transfer.

This is recorded separately as `Q03-CAB-006` in the structured ledger. The
credit-agreement rows remain contractual mechanics; the Q2 financial-statement
row is an executed-borrowing observation. Neither row is promoted to a complete
closing funds-flow allocation or Antamina-specific debt-service waterfall.

The SEC-hosted March 26, 2026 Non-Revolving Term Facility Credit Agreement
provides a stronger Q-03 legal-debt boundary than a filing summary alone. The
agreement names Wheaton Precious Metals Corp. and Wheaton Precious Metals
International Ltd. as borrowers, Bank of Montreal as administrative agent, and
the participating lender syndicate. It establishes a `1.500B USD` non-revolving
term facility whose maturity is two years from the closing date.

## What the agreement proves

- Interest on a Term Benchmark Loan is the Adjusted Term SOFR Rate plus the
  Applicable Rate.
- The Applicable Rate is determined by the leverage-ratio range in Schedule H;
  the agreement also includes sustainability adjustments.
- Accrued interest is payable on the applicable interest-payment dates, and
  outstanding principal, accrued interest, and fees are due in full at the
  maturity date.
- Wheaton must maintain a capitalization ratio no greater than `0.60:1`.
- The agreement creates a lender and administrative-agent route for the debt
  obligation and its repayment notices.
- Section 11.1(d) requires the borrowers to apply all Credit Facility proceeds
  to partially finance the Antamina Mine Silver Stream Acquisition. This is a
  contractual use-of-proceeds link, not a bank-transfer or seller-receipt
  record.
- Section 2.1 makes the facility available through a single drawdown on the
  Closing Date, Section 2.3 reduces the facility to the amount of that actual
  draw, and the form of Drawdown Notice allows the borrowers to irrevocably
  direct the Administrative Agent to pay proceeds to a designated payee. This
  narrows the decisive missing source to the executed Drawdown Notice, its
  designated-payee/payment instruction, the agent funding record, and the
  seller-account confirmation; it does not show that any of those records were
  obtained.

The [BHP upfront-settlement bridge](capital-flow-wheaton-antamina-bhp-upfront-settlement-bridge-2026-09-16.md)
adds a contemporaneous amount-and-date observation for the named `$4.300B`
payment and BHP's reported receipt. It does not replace the missing drawdown
notice, payment instruction, or lender waterfall required to allocate the
facility to the seller account or to an Antamina-specific return.

## What it does not prove

The agreement is a credit-document boundary, not an executed funds-flow
ledger. It does not identify which draw dollars entered the BHP-PMPA seller's
account, how cash on hand and revolver proceeds were combined with the term
loan, how principal was repaid, or how tax and interest were allocated to the
Antamina stream. It therefore cannot by itself produce an Antamina-specific
debt-service waterfall, IRR, NPV, or common-owner cash result.

The single-draw mechanics improve request precision but do not change that
boundary: contractual authority to direct proceeds to a designated payee is
not evidence of the executed payee, amount drawn, agent funding, or BHP receipt.
The Q2 filing now proves the amount actually drawn (`$1.500B`), so the missing
amount is no longer the primary uncertainty; the decisive gap is the payment
instruction and agent-to-seller funds-flow join.

## Public-source search boundary

The checked SEC/IR perimeter includes the credit-agreement exhibit, Wheaton's
Q1 and Q2 2026 reports, the April closing announcement, and the Q2 financial
statements. Those sources establish that the `$4.300B` PMPA payment was funded
with cash on hand, a revolving-facility draw, and the `$1.500B` term loan. The
targeted search did not locate an executed drawdown notice, borrowing notice,
payment instruction, seller-account confirmation, lender remittance, or
asset-specific repayment ledger. The newly isolated single-draw/designated-
payee object remains absent from the checked public perimeter. This is
`searched-negative` for the checked public perimeter, not a claim that private
treasury records do not exist.

## Q-03 consequence

Q-03 advances from a term-loan summary to direct agreement-level debt
mechanics, borrower identity, lender route, contractual Antamina use of
proceeds, maturity, pricing basis, and a capitalization covenant. The result
remains `evidence-insufficient` for a
financed after-tax Antamina return. The next decisive records are the executed
single-draw Drawdown Notice and any designated-payee/payment instruction, the
agent/seller closing funds flow, borrower-level repayment ledger, tax
allocation, and asset-specific delivery/receipt schedule.

## Source

- [SEC-hosted Non-Revolving Term Facility Credit Agreement](https://www.sec.gov/Archives/edgar/data/1323404/000106299326001700/exhibit99-2.htm), preserved locally as [non-revolving-term-facility-credit-agreement.htm](../../raw/primary-sources/capital-flow/wheaton/2026-03/non-revolving-term-facility-credit-agreement.htm)
- [Wheaton Q2 2026 financial statements](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex993.htm), preserved locally as [wpm-20260630-ex99-3-financial-statements.htm](../../raw/primary-sources/capital-flow/debt-refinancing/wheaton/q2-2026/wpm-20260630-ex99-3-financial-statements.htm)
- [Wheaton Q2 2026 financing cash-flow upgrade](capital-flow-wheaton-antamina-financing-cash-flow-upgrade-2026-09-15.md)
- [Wheaton financing terms boundary](capital-flow-wheaton-antamina-financing-terms-boundary-upgrade-2026-09-15.md)

Structured result: [credit-agreement boundary CSV](data/capital-flow-wheaton-antamina-credit-agreement-waterfall-boundary-2026-09-16.csv).
