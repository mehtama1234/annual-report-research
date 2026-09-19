# Apollo–Athene annual parent-source route validation — 2026-09-15

## Result

Apollo's FY2025 Form 10-K corroborates the parent-source route described in
the Q2 2026 Form 10-Q: the annual filing says Athene's capital may be used in
part to make dividend payments to AGM. The same filing explains that insurance
subsidiaries face restrictions and limitations on dividends and other
distributions to their parent, including ordinary/extraordinary dividend and
regulatory-capital constraints.

This is stronger than inferring a route from consolidated cash alone. It is
still a source-route and legal-availability result, not a dated cash receipt.
The annual filing does not provide the receiving bank account, a dollar
amount tied to a specific AHL-to-AGM transfer, intercompany elimination, or a
common-owner residual.

## Proof boundary

```text
Athene operating and investment capital
  -> possible dividend payment to AGM       source route: confirmed
  -> ordinary/extraordinary and solvency tests legal access: constrained
  -> AGM unrestricted cash                   dated receipt: not joined
  -> Apollo common-owner residual            unresolved
```

The FY2025 annual language therefore supports the existing `partial` Q-07
grade and narrows the next request. It does not justify treating Athene's
reported cash, dividends paid, or consolidated Apollo cash as freely available
to Apollo common owners.

## Next upgrade

Join an AHL dividend declaration/payment record to an AGM bank, intercompany,
or parent cash-flow ledger, then subtract preferred, NCI, debt, tax, regulated
capital, and dilution claims before calculating common-owner cash.

## Primary source

[Apollo FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1858681/000185868126000012/apo-20251231.htm), sections discussing Athene capital deployment and restrictions on dividends and other distributions.
