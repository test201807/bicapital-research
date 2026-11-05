# Heikin Ashi streaks: chart colour vs real price

Pine Script v6 indicator, published open source on TradingView by `hectorldu` on 2026-11-05.

- Script: https://www.tradingview.com/script/eN7WgKVI-Heikin-Ashi-streaks-chart-colour-vs-real-price/
- Educational idea: https://www.tradingview.com/chart/BTCUSDT/5Tk2Jw7E-Heikin-Ashi-trends-also-appear-on-random-prices/

It computes Heikin Ashi candles from the chart's ordinary OHLC and counts three rates over the loaded history:

| Row | What it counts |
|---|---|
| Heikin Ashi colour → next HA colour | A Heikin Ashi candle followed by another of the same colour |
| Ordinary candle → next candle | The same on ordinary candles (control) |
| Heikin Ashi colour → next real price move | After a green (red) HA candle, the next bar closes higher (lower) than the previous close |

Result when published:

| Chart | HA → next HA | Ordinary → next | HA → next real move | Bar pairs |
|---|---:|---:|---:|---:|
| BINANCE:BTCUSDT, 1D | 76.4% | 46.6% | 48.5% | 3,366 |
| OANDA:EURUSD, 1h | 75.3% | 49.6% | 48.8% | about 11,300 |

The colour persists because each Heikin Ashi candle averages the previous one; the price does not inherit that
persistence. In the underlying study (76 series, 43 chart configurations, 30 random walks per chart), Heikin Ashi
"continues" 77.9% of the time on real markets and 78.8% on random prices with the same volatility. Article:
[`articles/2026-11-B19`](../../articles/2026-11-B19).

The script does not repaint: it only uses closed values of the current and previous bars.

License: Mozilla Public License 2.0 (as published on TradingView). Educational tool, not investment advice.
