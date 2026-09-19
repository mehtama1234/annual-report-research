# Wheaton–Antamina BHP annual delivery-curve proxy

Research date: `2026-09-16` (official BHP FY2026 operational-review refresh)

The BHP FY2026 operational review supplies the first annual and quarterly
counterparty-side series that can inform a delivery curve. Under the table
heading `Antamina, Peru — BHP interest 33.75%`, BHP reports payable silver
production of `1.313M`, `1.632M`, `1.438M`, `1.462M`, and `1.056M` troy ounces
for the quarters ended June 2025, September 2025, December 2025, March 2026,
and June 2026, respectively. FY2026 production totals `5.588M` ounces.

BHP reports payable silver sales of `0.953M`, `1.705M`, `1.553M`, `1.201M`,
and `0.947M` ounces for those same quarters, with FY2026 sales of `5.406M`
ounces. The June 2026 quarter covers April–June 2026 and therefore contains
the first post-April-1 quarter after the BHP-PMPA effective date.

The official BHP FY2026 operational review, published July 16, 2026, confirms
the same FY2026 Antamina BHP-interest production and sales table and gives
FY2027 Antamina copper guidance of `120–140 kt`. The review does not provide a
forward Antamina silver schedule. Copper guidance is therefore retained only
as operating context and is not converted into a silver-delivery forecast.

## Denominator discipline

The table is explicitly labeled `BHP interest 33.75%`. The safe use is a
counterparty-side BHP-interest payable-metal series and a production-versus-
sales timing screen. It should not automatically be multiplied by `33.75%`
again: doing so could double-count the BHP ownership share if the reported
series already represents BHP's attributable payable metal. Conversely, the
table alone does not prove that BHP's reporting convention exactly matches the
PMPA's fixed `90.0%` payable factor or Wheaton's metal-credit ledger.

The following screens are therefore kept separate:

| Screen | Value | Interpretation |
| --- | ---: | --- |
| FY2026 BHP-interest payable silver produced | `5.588M oz` | Operating denominator, not stream settlement |
| FY2026 BHP-interest payable silver sold | `5.406M oz` | Sales/timing denominator, not Wheaton receipt |
| June 2026 post-effective-date production | `1.056M oz` | First quarter counterparty production signal |
| June 2026 post-effective-date sales | `0.947M oz` | First quarter counterparty sales signal |
| FY2026 sold/produced screen | `96.7%` | `5.406 / 5.588`, a timing/settlement screen only |

## Proof-grade result

`annual-counterparty-delivery-curve-proxy-confirmed`: BHP's official annual
operational review now provides an annual and quarterly BHP-interest series
that can anchor a modeled delivery curve. It does not prove the BHP-only
metal-credit quantity, invoice, settlement date, realized price, or cash
receipt. The reserve-backed life-of-mine curve and the contract's `90.0%`
payability reconciliation remain open.

## Primary sources

- [BHP Operational Review for the year ended 30 June 2026](https://www.bhp.com/news/media-centre/releases/2026/07/bhp-operational-review-for-the-year-ended-30-june-2026)
- [BHP FY2026 Operational Review PDF](https://www.bhp.com/-/media/documents/media/reports-and-presentations/2026/260716_bhpoperationalreviewfortheyearended30june2026.pdf)
- [BHP FY2026 Form 20-F / annual report](https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm)
