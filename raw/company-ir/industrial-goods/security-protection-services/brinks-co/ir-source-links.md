# The Brink's Company IR Source Notes

Date checked: 2026-08-10
Investor relations domain attempted: `https://investors.brinks.com/`

## Access result during this pass

- Direct automated fetch attempts to the Brink's investor-relations site were unstable during this pass.
- `curl` returned repeated `HTTP/2` stream errors on the overview and financial routes.
- Follow-up scripted fetch attempts did not produce a reliable saved HTML source set in the repo during this pass.

## Practical implication

- This packet uses AnnualReports for taxonomy and archive confirmation.
- The authoritative annual and quarter evidence chain is SEC-first:
  - `2025` 10-K
  - `Q1 2026` 10-Q and earnings release
  - `Q2 2026` 10-Q and earnings release
