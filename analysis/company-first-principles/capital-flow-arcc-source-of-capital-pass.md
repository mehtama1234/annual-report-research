# Capital Flow ARCC Source-Of-Capital Pass

## Purpose

This is the first execution pass from the ultimate-source document queue.

Target: Ares Capital Corporation.

Question: when ARCC shows up as a holder of operating-company loans, what can we say about the capital stack behind that holder?

Extraction table:

`analysis/company-first-principles/data/capital-flow-arcc-source-of-capital-extractions.csv`

Primary source:

`raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-2026-q2-10q.html`

## Simple Answer

ARCC borrower rows are not just “Ares arranged a deal.”

They are public-BDC balance-sheet holdings. As of June 30 2026, ARCC reported:

- `29.349B USD` of investments at fair value
- `30.498B USD` of total assets
- `15.773B USD` of debt carrying value
- `13.891B USD` of stockholders' equity
- `15.924B USD` of senior securities principal outstanding
- `186%` asset coverage

So when ARCC appears beside Valcourt, Sunvair, AeriTek, or MAI, the visible holder channel is a public BDC funded by a mix of public equity and debt instruments, not a direct claim on Ares corporate balance-sheet money.

## Balance-Sheet Snapshot

| Metric | Q2 2026 Value | Source Location |
|---|---:|---|
| Total investments at fair value | `29349M USD` | Consolidated balance sheets page 3 |
| Total assets | `30498M USD` | Consolidated balance sheets page 3 |
| Debt carrying value | `15773M USD` | Consolidated balance sheets page 3 |
| Total liabilities | `16607M USD` | Consolidated balance sheets page 3 |
| Total stockholders' equity | `13891M USD` | Consolidated balance sheets page 3 |
| Net asset value per share | `19.35 USD` | Consolidated balance sheets page 3 |

Derived ratios:

| Ratio | Value | Read |
|---|---:|---|
| Debt carrying value / total assets | `51.72%` | More than half of ARCC's asset base is debt-funded on a carrying-value basis. |
| Stockholders' equity / total assets | `45.55%` | Equity is a large funding layer but not the only one. |
| Debt carrying value / stockholders' equity | `1.1355x` | ARCC is materially levered, as expected for a BDC. |

## Debt Stack

| Funding Instrument / Class | Principal Outstanding | What It Means |
|---|---:|---|
| Revolving Credit Facility | `1566M USD` | Bank/facility liquidity used at ARCC level. |
| Revolving Funding Facility | `1086M USD` | Secured/funding-facility financing layer. |
| SMBC Funding Facility | `728M USD` | Named bank funding facility at ARCC level. |
| BNP Funding Facility | `674M USD` | Named bank funding facility at ARCC level. |
| Secured credit and funding facilities subtotal | `4054M USD` | Computed from the four facility rows above. |
| CLO notes and secured loans | `1720M USD` | Structured/securitized funding layer. |
| Unsecured notes | `10150M USD` | Largest disclosed debt-funding class. |
| Total principal amount outstanding | `15924M USD` | Reconciles to ARCC's disclosed senior securities principal. |
| Total carrying value of debt | `15773M USD` | Reconciles to balance sheet debt. |

Liquidity:

- ARCC reported `3860M USD` available for borrowing under the Revolving Credit Facility, subject to borrowing-base restrictions.
- ARCC maintained a `1000M USD` commercial paper program.
- ARCC reported `0M USD` commercial paper outstanding at June 30 2026.

## Adviser / Platform Link

ARCC says it is externally managed by Ares Capital Management LLC, a subsidiary of Ares Management Corporation.

ARCC also says Ares Operations LLC, another Ares Management subsidiary, provides administrative services.

This matters because the borrower rows connect to an Ares-managed public BDC. It does not mean Ares corporate balance sheet or Ares insurance capital funded every ARCC loan.

## Borrower Cases This Upgrades

| Borrower | ARCC Visible Holder Evidence | Upgrade From This Pass |
|---|---|---|
| Valcourt | `117.6M USD` Q2 2026 ARCC fair value | Public-BDC holder backed by ARCC funding stack. |
| Sunvair | `68.1M USD` Q2 2026 ARCC fair value | Public-BDC holder backed by ARCC funding stack. |
| AeriTek | `59.6M USD` Q2 2026 ARCC fair value | Public-BDC holder backed by ARCC funding stack. |
| MAI Capital | `8.0M USD` Q2 2026 ARCC fair value | Public-BDC holder backed by ARCC funding stack. |

## Claim Upgrade

Before this pass:

ARCC reported borrower-level exposure to several operating companies.

After this pass:

ARCC reported borrower-level exposure, and ARCC itself was funded by a large public-BDC capital stack: stockholders' equity, unsecured notes, secured/funding facilities, CLO notes/secured loans, and unused revolving availability.

## What This Still Does Not Prove

This pass does not prove:

- which ARCC debt or equity funding source funded any specific borrower loan
- who owned ARCC's unsecured notes
- who owned ARCC common stock
- whether any insurance liabilities funded ARCC borrower exposure
- total facility size at Valcourt, Sunvair, AeriTek, or MAI
- bank replacement at the borrower level

## Next ARCC Work

The next deeper ARCC questions are:

- What is the shareholder and noteholder base?
- Which banks provide the revolving and funding facilities?
- Are any ARCC financing subsidiaries tied to specific collateral pools?
- Does any statutory insurer filing show ARCC shares, notes, or affiliated credit exposure?
- Can we map ARCC borrower holdings to facility-level lender groups through credit agreements or rating reports?

## Current Bottom Line

For ARCC-linked borrower rows, the source-of-funds answer is now stronger:

The immediate holder is a public BDC with `13.891B USD` of stockholders' equity and `15.773B USD` of debt carrying value. That public-BDC funding stack is the visible source channel. The ultimate capital owners behind the shares and notes remain a separate evidence problem.
