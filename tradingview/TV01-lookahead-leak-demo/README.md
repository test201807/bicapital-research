# Look-ahead leak demo: request.security

Pine Script v6 indicator, published open source on TradingView by `hectorldu` on 2026-11-03.

It draws the same higher-timeframe close in three ways and scores the same naive rule on each one:

| Line | Call | Behaviour |
|---|---|---|
| 1 Leaking | `request.security(..., close, lookahead = barmerge.lookahead_on)` | On history, every bar of the period sees the period's final close |
| 2 Default | `request.security(..., close)` | Honest on history, repaints in real time |
| 3 Sealed | `request.security(..., close[1], lookahead = barmerge.lookahead_on)` | Last closed period; same on history and in real time |

Rule: "if the line is above the current close, the period will finish higher than now, and the reverse", scored on
historical bars when each period ends.

Result when published (BINANCE:BTCUSDT, 1h chart, daily higher timeframe, about 15,400 scored signals per line):

| Line | Hit rate |
|---|---|
| 1 Leaking | 100.0% |
| 2 Default | 52.0% |
| 3 Sealed | 52.0% |

A 100% hit rate is not an edge: it is the future copied into the past. Numbers depend on the symbol and on how many
bars TradingView loads.

*Educational content. Not investment advice.* License: Mozilla Public License 2.0 (see the header of the script).

---

**ES.** Indicador Pine v6 publicado en abierto en TradingView. Con la misma regla, la línea con fuga (`lookahead_on`
con `close`) acierta el 100,0 % y las versiones sin fuga el 52,0 %. Contenido educativo; no es asesoría de inversión.
