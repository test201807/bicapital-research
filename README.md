# BICAPITAL Research

Independent quantitative research by Héctor Sandoval ([ORCID 0009-0008-4411-9851](https://orcid.org/0009-0008-4411-9851)), Ecuador.
Trading and investing claims tested with real data and real costs: open methods, dated results, mistakes included.

Articles are published on [BICAPITAL Research (Substack)](https://hectorsandoval.substack.com) in English and Spanish.
This repository keeps the article sources, the figures and the data behind each chart, so anyone can check them.

| Date | Article | Files |
|---|---|---|
| 2026-10-25 | More than 130 million trading combinations declared: here is what I found | [`articles/2026-10-B01`](articles/2026-10-B01) |
| 2026-10-28 | My real portfolio: the thesis, the rules and how far it can fall | [`articles/2026-10-I33`](articles/2026-10-I33) |
| 2026-10-30 | My backtest was perfect and my evaluation account was losing: one line of code was looking into the future | [`articles/2026-11-B02`](articles/2026-11-B02) |
| 2026-11-01 | Decision diary no. 1 (October 2026): I lost to Bitcoin, and here is what I decided | [`articles/2026-10-I34`](articles/2026-10-I34) |
| 2026-11-05 | El Niño 2026-27 in Ecuador: what the data say before the rains (data report) | [`articles/2026-11-E01`](articles/2026-11-E01) · data: [`datasets/el-nino-ecuador-2026`](datasets/el-nino-ecuador-2026) |
| 2026-11-06 | Why your TradingView backtest lies: the indicator that "worked" and returned +20% in almost 8 years | [`articles/2026-11-B17`](articles/2026-11-B17) |
| 2026-11-07 | My 17-parameter system did not beat buying and holding Bitcoin | [`articles/2026-11-I05`](articles/2026-11-I05) |
| 2026-11-08 | Prop-firm challenges: out of every 100 who try without an edge, 93 lose the fee | [`articles/2026-11-B11`](articles/2026-11-B11) |
| 2026-11-09 | The altcoin season myth: altcoins amplify the falls, not the rises | [`articles/2026-11-I11`](articles/2026-11-I11) |
| 2026-11-10 | "The day's high or low is set in the first hour 7 times out of 10": it is geometry | [`articles/2026-11-B18`](articles/2026-11-B18) |
| 2026-11-11 | The factory stops being a building: a distributed production network for Ecuador (white paper, public edition) | [`articles/2026-11-E02`](articles/2026-11-E02) · PDF: [`whitepapers/produccion-distribuida-ecuador`](whitepapers/produccion-distribuida-ecuador) |
| 2026-11-12 | Survivorship bias in crypto: more than half the coins of 2022-24 no longer trade | [`articles/2026-11-I12`](articles/2026-11-I12) |
| 2026-11-13 | Chart patterns: 28 figures against chance, on eight chart types | [`articles/2026-11-B07`](articles/2026-11-B07) |
| 2026-11-14 | My own strategy performed the same as entering at random | [`articles/2026-11-B12`](articles/2026-11-B12) |
| 2026-11-15 | Binance funding: from 30% a year to 2% | [`articles/2026-11-M06`](articles/2026-11-M06) |
| 2026-11-16 | Renko and Heikin Ashi: the trends the chart draws by itself | [`articles/2026-11-B19`](articles/2026-11-B19) |
| 2026-11-17 | "It's on a streak": switching strategies on and off by how they are doing does not work | [`articles/2026-11-M15`](articles/2026-11-M15) |
| 2026-11-18 | Holding index CFDs overnight: the swap turns +6.7% into −4.8% | [`articles/2026-12-B13`](articles/2026-12-B13) |
| 2026-11-19 | Support and resistance: last month's and last year's highs do not stop price | [`articles/2026-12-M16`](articles/2026-12-M16) |
| 2026-11-20 | Nine method errors I found in my own research | [`articles/2026-12-I20`](articles/2026-12-I20) |

TradingView (open source): [`tradingview/TV01-lookahead-leak-demo`](tradingview/TV01-lookahead-leak-demo), a Pine Script
that shows how `request.security` with `lookahead_on` leaks the future (same rule: 100.0% hit rate with the leak, 52.0%
without it, on BTCUSDT 1h with a daily higher timeframe). Published on TradingView as "Look-ahead leak demo: request.security".
[`tradingview/TV02-heikin-ashi-streaks`](tradingview/TV02-heikin-ashi-streaks): how often a Heikin Ashi colour repeats vs how
often the next real price move follows it (BTCUSDT daily: 76.4% vs 48.5%). Published on TradingView with an educational idea.

Datasets: [`datasets/el-nino-ecuador-2026`](datasets/el-nino-ecuador-2026), 17 sourced tables on El Niño in Ecuador
(ocean, rainfall, damage, crops, dengue, prices), with the code that redraws every chart.

White papers: [`whitepapers/produccion-distribuida-ecuador`](whitepapers/produccion-distribuida-ecuador), a distributed
production network for Ecuador (central hub + automated last-mile cells + orchestration software), public edition, in Spanish.

Software: [causality-probe](https://github.com/test201807/causality-probe), a tool to detect look-ahead bias in backtests.

*Educational and research content. Not investment advice. Backtest and simulation results are hypothetical and past.*

---

# BICAPITAL Research (español)

Investigación cuantitativa independiente. Los artículos se publican en Substack en inglés y en español; aquí están sus
fuentes, las figuras y los datos de cada gráfico. *Contenido educativo; no es asesoría de inversión.*
