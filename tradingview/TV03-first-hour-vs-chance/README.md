# First-hour high/low: real market vs random direction

Pine Script v6 indicator, published open source on TradingView by `hectorldu` on 2026-11-05.

- Script: https://www.tradingview.com/script/04yB4RRn-First-hour-high-low-real-market-vs-random-direction/
- Educational idea: https://www.tradingview.com/chart/SPY/YSa9ABgj-High-or-low-in-the-first-hour-true-and-random-gives-the-same/

It counts two popular statistics over the completed sessions loaded on the chart, and the same two statistics on random
paths built from the same bars (each bar keeps its exact moves from the previous close, but its direction is flipped at
random):

| Row | What it counts |
|---|---|
| Session high or low inside the first window | Sessions whose high or low was set in the first N minutes |
| First window ends in its upper half → session low already in | Among sessions whose first window closed above the middle of its range, those whose low was already set |

Result when published:

| Chart | Sessions | High or low in first hour (real / random) | Low already in (real / random) |
|---|---:|---:|---:|
| AMEX:SPY, 15 min | 402 | 73.1% / 72.2% | 59.0% / 58.2% |
| AMEX:SPY, 5 min | 129 | 73.6% / 72.7% | 60.9% / 57.6% |

In the underlying study (S&P 500, 885 days, minute data), the figures were 70.5% real vs 68.5% at random and 60.4% vs 59.1%;
16 pre-registered versions of "trade in the direction of the first hour" all failed with real costs. Article:
[`articles/2026-11-B18`](../../articles/2026-11-B18).

Default session 09:30-16:00 New York; works best on 1- to 15-minute charts. License: Mozilla Public License 2.0.
Educational tool, not investment advice.
