# Wheaton–Antamina Financing Cash-Flow Upgrade

Research date: `2026-09-15`

This upgrade executes the financing-flow portion of queue item `Q-03` using
Wheaton's Q2 2026 condensed interim consolidated cash-flow statement. It
reconciles the actual period movement in bank debt with the reported interest
and debt-issue cash flows. It does not allocate those flows to Antamina.

Primary local source:

`raw/primary-sources/capital-flow/debt-refinancing/wheaton/q2-2026/wpm-20260630-r5.htm`

The structured extraction is:

`data/capital-flow-wheaton-antamina-financing-cash-flow-upgrade-2026-09-15.csv`

The ledger now carries a separate contractual-use row from the March 2026
credit agreement. That row is intentionally not merged with the cash-flow
rows: a legal requirement that facility proceeds partially finance Antamina is
stronger than a financing-purpose summary, but weaker than an executed
drawdown, seller-account transfer, or repayment ledger.

## Actual financing-flow reconciliation

For the six months ended June 30, 2026, Wheaton reports `$2.700B` of bank
debt drawn, `$728M` of bank debt repaid, and `$5.118M` of debt-issue costs.
The net debt movement is therefore `$1.972B`, matching the term-loan plus
revolving-facility balance used in the company-level burden screen:

```text
2,700M drawn - 728M repaid = 1,972M net debt movement
```

The same cash-flow statement reports `$29.886M` of interest paid in H1 2026,
compared with `$178,000` in the prior-year period. This is actual cash paid,
not the annualized rate sensitivity. Because the new term loan was entered on
April 1, 2026 and the facility balance changed during the period, H1 interest
paid cannot be divided by `$1.972B` and presented as a full-year borrowing
rate.

Wheaton reports `$1.796853B` of cash generated from financing activities in
H1 2026. That amount is a financing-flow total, not cash available for the
Antamina PMPA: it includes debt draw, repayment, debt-issue costs, dividends,
lease payments, and other financing items according to the statement's
classification.

## Relation to the Antamina purchase

The Q2 notes state that the `$4.300B` BHP Antamina PMPA was paid on April 1,
2026. They also show that the term loan was entered into on that date and that
the revolving facility was available for acquisitions, investments, or
general corporate purposes. This establishes a tight timing and capacity
relationship, but not a lender-level funds-flow allocation. The filing does
not say which dollar of the `$2.700B` drawn was applied to the PMPA, what cash
on hand funded the remainder, or whether any revolver balance funded another
investment.

The transaction announcement gives an explicit planned funding composition:
approximately `$1.9B` of cash on hand, `$1.5B` of term-loan proceeds, and
approximately `$0.9B` of revolver proceeds. The arithmetic reconciles to the
`$4.3B` PMPA payment:

```text
1.9B cash on hand + 1.5B term loan + 0.9B revolver = 4.3B PMPA payment
```

The two announced debt components separately reconcile to an approximately
`$2.4B` planned debt-funding envelope (`$1.5B + approximately $0.9B`). That is
not interchangeable with the `$2.7B` H1 actual corporate bank-debt draw: the
public record does not identify whether the difference reflects timing, other
corporate borrowing, gross-versus-net presentation, or another facility-level
movement. The announced envelope, actual financing statement, and executed
PMPA funds flow therefore remain separate objects.

The Q2 results release provides a same-period post-close funding-envelope
cross-check: Wheaton reports `$4.5B` of net upfront cash payments for mineral
stream interests, including `$4.3B` for BHP Antamina; approximately `$100M` of
cash on hand at June 30; and approximately `$2.0B` outstanding under the term
loan and revolving facility. This confirms the scale and timing of the
company-level source/use envelope, but it does not replace a closing funds-flow
statement. The release does not allocate the `$4.5B` across seller accounts,
identify which portion of the `$2.700B` H1 bank debt draw funded BHP, or show a
facility-specific repayment waterfall.

This is a funding-composition screen, not a bank-transfer ledger. Q2 reports
`$1.972B` of gross bank debt outstanding (`$1.500B` term loan plus `$472M`
revolver), but the public cash-flow statement does not identify which facility
repayments produced the difference from the approximately `$2.4B` of planned
debt funding. No facility-specific repayment or seller-account allocation is
inferred.

## Proof-grade result

| Gate | Result | Boundary |
| --- | --- | --- |
| Actual debt draw and repayment | Proven | Corporate financing flow; not Antamina-assigned debt |
| Net debt movement | Proven | `$1.972B` reconciles the reported draw less repayment; allocation remains open |
| Actual interest paid | Proven for H1 cash flow | Short-period cash paid, not a normalized full-year interest rate |
| Debt-issue costs | Proven | Financing cash outflow is visible; amortization and asset allocation remain open |
| Financing cash-flow total | Proven | Includes multiple financing items and is not Antamina free cash |
| PMPA funding allocation | Not proven | Cash-on-hand versus term-loan versus revolver source is not fully allocated |
| Financed IRR/NPV | Not proven | Requires payment dates, tax, principal waterfall, delivery curve, and asset-specific debt allocation |

## Updated safe claim

`Wheaton's Q2 2026 filing proves the actual corporate financing movement around
the Antamina closing: $2.700B of bank debt was drawn, $728M was repaid,
$5.118M of debt-issue costs were paid, and $29.886M of interest was paid in
the first half. The resulting $1.972B net debt movement supports a corporate
financing burden screen. The filing does not prove that the debt was allocated
to Antamina, nor does it provide an Antamina-specific debt-service waterfall,
tax allocation, IRR, or NPV.`

## Next gate

The remaining Q-03 requirement is an asset-specific funds-flow and repayment
waterfall: identify the lender-funded portion of the `$4.300B` payment, actual
principal amortization/repayment, tax burden, delivery timing, and BHP-only
settlement cash.

Source refresh: [Wheaton Q2 2026 results and financial disclosures](https://www.wheatonpm.com/news/news-details/2026/Wheaton-Precious-Metals-Announces-Second-Quarter-2026-Results-and-Record-Year-to-Date-Production-Revenue-Earnings-and-Cash-Flow/default.aspx).

## Live official-source recheck — 2026-09-17

A fresh search of the SEC-hosted Q2 2026 results release, Q2 MD&A, and
transaction exhibits returned the same Q-03 boundary. The official packet
continues to state that the April 1 `$4.300B` BHP Antamina payment was funded
with cash on hand, a new `$1.500B` term loan, and a revolver draw; it also
reports the H1 corporate financing movements and confirms that the term-loan
proceeds were used to partially fund the PMPA. The packet does not disclose an
executed closing funds-flow, seller-account confirmation, facility-specific
draw-dollar allocation, Antamina-specific repayment, or asset-level tax and
interest schedule.

This is a current searched-negative result for the checked public perimeter,
not evidence that the missing documents do not exist. The promotion gate
therefore remains `full-return-inputs-incomplete`: the next useful source is a
closing statement, borrowing notice, lender repayment schedule, tax allocation,
or asset-level settlement record—not another company-level OCF proxy.
