# Pilot 02 Walmart known-growth capex boundary

Research date: `2026-09-15`

Walmart's H1 FY2027 filing separately reports `$1.087B` of capital spending for
new stores and clubs within total capital spending of `$14.181B`. The filing
does not label the remaining categories as maintenance or growth. Because a
new-store/new-club category is a direct capacity-addition category, it can be
used as a bounded inference that at least `$1.087B` of the H1 total is growth
capital, subject to the possibility that the category includes replacement or
other non-expansion work.

The resulting source-bounded screen is:

```text
H1 OCF                         $19.710B
- total capex                  $14.181B
= reported OCF less capex      $5.529B

inferred growth-capex floor    $1.087B new stores/clubs
implied maintenance ceiling    $13.094B
implied OCF less maintenance   $6.616B floor under this classification
```

The `$6.616B` figure is not reported owner cash. It is a classification-boundary
screen under the narrow assumption that all non-new-store spending is
maintenance. The upper bound remains `$19.710B` before any maintenance spend.
Neither bound adjusts for inventory and payable timing, supplier finance,
leases, taxes, stock compensation, attached-service costs, debt, or dilution.

Therefore the correct conclusion is narrower than “Walmart has `$6.616B` of
owner cash”: the filing-supported category split proves a minimum identifiable
growth bucket and narrows the capex allocation range, while the normalized
owner-cash denominator remains unresolved.

Primary source: [Walmart Q2 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm).
