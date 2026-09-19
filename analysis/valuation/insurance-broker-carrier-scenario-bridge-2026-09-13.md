# Insurance broker versus carrier: valuation scenario bridge

Date baseline: 2026-09-13. This is a valuation research artifact, not an
investment recommendation. It intentionally does not force Marsh and Chubb
into the same owner-cash denominator.

## Why the denominators differ

Marsh is primarily a fee and advisory intermediary. Its FY2025 consolidated
bridge was:

`$5.292B OCF - $0.291B PP&E - $0.652B acquisitions = $4.349B residual`

That residual still requires normalization for recurring acquisitions,
receivables, producer compensation, legal costs, SBC, and debt, but it is a
reasonable starting point for a fee-platform cash scenario.

Chubb is an insurer. Its FY2025 $12.816B OCF includes premium collection,
claims timing, investment activity, and policyholder-liability movements. It
cannot be treated as distributable corporate cash. The carrier model instead
starts with normalized P&C underwriting income, after-tax recurring investment
income, normalized life income, and required capital/surplus.

## Market snapshot and scenarios

The synchronized September 11, 2026 finance snapshot recorded Chubb equity
value of approximately $130.5B at $338.25 per share. The available Marsh feed
showed $182.70 per share, but its provider equity-value field did not reconcile
cleanly with the FY2025 diluted share denominator of 494M; using price times
FY2025 diluted shares gives approximately $90.25B. That discrepancy is retained
as a data-quality note rather than silently mixing denominators.

### Marsh: fee-platform owner cash

| Case | Normalized owner cash | Equity-cash multiple | Implied equity value | What must be true |
|---|---:|---:|---:|---|
| Bear | $3.2B | 18x | $57.6B | Organic growth weakens, recurring M&A rises, receivables/legal/talent costs expand |
| Base | $4.2B | 22x | $92.4B | Organic fee growth persists, acquisition returns clear the hurdle, SBC and debt remain controlled |
| Bull | $5.2B | 26x | $135.2B | Strong organic growth, high-retention acquired platforms, margin expansion, and disciplined capital returns |

The base case is close to the derived equity value, so Marsh belongs in an
expectations audit rather than a mechanical bargain queue. The central reverse
valuation question is whether the market is paying for organic fee durability
or for another cycle of acquisition-led revenue growth.

### Chubb: underwriting and capital model

| Case | Normalized core earnings | Earnings multiple | Implied equity value | What must be true |
|---|---:|---:|---:|---|
| Bear | $7.5B | 10x | $75.0B | Combined ratio normalizes higher, reserve/catastrophe losses rise, investment yield and life spread weaken |
| Base | $9.5B | 12x | $114.0B | Underwriting remains disciplined, investment income normalizes, capital remains excess, book value compounds |
| Bull | $11.5B | 14x | $161.0B | Pricing, reserve quality, investment carry, life growth, and capital returns remain unusually strong |

Chubb's current equity value is above the base earnings screen and below the
bull screen. That does not establish overvaluation: insurers also trade on
book value, excess capital, duration, reserve confidence, and the quality of
future float. It does establish that a record 85.7% combined ratio and $6.5B
pre-tax investment income cannot simply be capitalized as permanent without a
reserve, catastrophe, credit, and surplus test.

## Forensic normalization checklist

For Marsh:

- separate organic growth from acquired revenue and currency;
- calculate acquisition-cohort cash returns after producer retention,
  compensation, integration, and amortization;
- normalize receivable collection and client-fund timing;
- treat recurring legal, cyber, restructuring, and SBC costs as economic costs;
- reconcile buybacks with diluted share count and debt.

For Chubb:

- decompose the combined ratio by accident year, catastrophe, prior-period
  development, rate, exposure, mix, and expenses;
- normalize investment income for rates, duration, credit losses, and illiquid
  marks;
- separate P&C, life, and other segment capital requirements;
- test reinsurance recoverables, reserve adequacy, and required surplus;
- compare buyback price with normalized book value and post-stress capital.

## Filing-based falsifiers

Marsh's base case weakens if organic growth remains below acquired growth,
receivables deteriorate, talent costs outrun fees, legal charges recur, or M&A
is needed merely to prevent cash contraction. Chubb's base case weakens if
reserve releases reverse, current accident-year losses rise, catastrophe/social
inflation exceeds the modeled load, investment income relies on impaired or
illiquid assets, or capital returns outrun surplus.

Primary evidence is preserved in the [Marsh memo](../deep-company-pages/marsh-mclennan-companies-inc.md),
[Chubb memo](../deep-company-pages/chubb-limited.md), [Marsh source ledger](../../extracted/financial/insurance-brokers/marsh-mclennan-companies-inc/source-ledger.md),
and [Chubb source ledger](../../extracted/financial/property-casualty-insurance/chubb-limited/source-ledger.md).
