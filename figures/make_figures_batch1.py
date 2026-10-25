"""Figures for articles B01 and I33 (Spanish and English).

Usage: python figures/make_figures_batch1.py   ->  figures/*.png (es) and *_en.png (en)
Requires matplotlib.
"""
import csv
import datetime as dt
import math
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "figures"
OUT.mkdir(exist_ok=True)

SUP, TXT, TXT2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
AZUL, NARANJA, GRIS = "#2a78d6", "#eb6834", "#8a8984"   # categorical 1-2 validados; gris = referencia neutra
MARCA = "BICAPITAL Research"
LANG = "es"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13, "axes.edgecolor": GRID,
                     "axes.labelcolor": TXT2, "xtick.color": TXT2, "ytick.color": TXT2,
                     "figure.facecolor": SUP, "axes.facecolor": SUP, "savefig.facecolor": SUP})

MESES = {"es": ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
         "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]}


def num(x, dec=1):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".") if LANG == "es" else s


def pct(x, dec=1):
    return f"{num(x, dec)} %" if LANG == "es" else f"{num(x, dec)}%"


def nombre(base):
    return f"{base}.png" if LANG == "es" else f"{base}_en.png"


def pie(fig, fuente):
    fig.text(0.015, 0.02, f"{'Fuente' if LANG == 'es' else 'Source'}: {fuente}", fontsize=10, color=TXT2, ha="left")
    fig.text(0.985, 0.02, MARCA, fontsize=10, color=TXT2, ha="right", weight="bold")


def titulo(fig, t, sub=None):
    fig.text(0.015, 0.94, t, fontsize=19, color=TXT, weight="bold", ha="left")
    if sub:
        fig.text(0.015, 0.885, sub, fontsize=12.5, color=TXT2, ha="left")


def tiles(archivo, t, sub, items, fuente, flechas=True):
    """Fila de cifras grandes (la forma correcta para unos pocos titulares)."""
    fig = plt.figure(figsize=(12, 5.2))
    titulo(fig, t, sub)
    n = len(items)
    for i, (valor, etiqueta, color) in enumerate(items):
        x = 0.03 + i * (0.94 / n)
        ax = fig.add_axes([x, 0.16, 0.94 / n - 0.02, 0.62])
        ax.set_axis_off()
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, facecolor="#f3f2ef",
                                   edgecolor="none", zorder=0))
        ax.text(0.5, 0.60, valor, ha="center", va="center", fontsize=34, weight="bold", color=color)
        ax.text(0.5, 0.24, etiqueta, ha="center", va="center", fontsize=12, color=TXT2, wrap=True)
        if flechas and i < n - 1:
            fig.text(x + 0.94 / n - 0.012, 0.47, "→", fontsize=22, color=GRIS, ha="center", va="center")
    pie(fig, fuente)
    fig.savefig(OUT / archivo, dpi=160)
    plt.close(fig)


def barras(archivo, t, sub, etiquetas, valores, colores, unidad, eje, fuente, nota=None):
    fig, ax = plt.subplots(figsize=(12, 6.2))
    fig.subplots_adjust(top=0.78, bottom=0.17, left=0.08, right=0.97)
    titulo(fig, t, sub)
    x = range(len(valores))
    ax.bar(x, valores, color=colores, width=0.55, zorder=2)
    ax.axhline(0, color=TXT2, linewidth=1, zorder=3)
    for i, v in enumerate(valores):
        ax.text(i, v + (0.012 if v >= 0 else -0.012), f"{'+' if v > 0 else '−' if v < 0 else ''}{num(abs(v), 3)} {unidad}",
                ha="center", va="bottom" if v >= 0 else "top", fontsize=13, color=TXT, weight="bold")
    ax.set_xticks(list(x), etiquetas)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: num(v, 2)))
    ax.set_ylabel(eje)
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    lo, hi = min(valores + [0]), max(valores + [0])
    ax.set_ylim(lo - 0.08 * (hi - lo) - 0.03, hi + 0.15 * (hi - lo) + 0.03)
    if nota:
        fig.text(0.015, 0.075, nota, fontsize=10.5, color=TXT2, ha="left")
    pie(fig, fuente)
    fig.savefig(OUT / archivo, dpi=160)
    plt.close(fig)


def twr(tx):
    filas = list(csv.DictReader(open(RAIZ / "articles" / "2026-10-I33" / "portfolio_twr_percent.csv",
                                     encoding="utf-8-sig"), delimiter=";"))
    f = [dt.date.fromisoformat(r["fecha"]) for r in filas]
    c = [float(r["cartera_TWR_acum_pct"]) for r in filas]
    b = [float(r["BTC_acum_pct"]) for r in filas]
    fig, ax = plt.subplots(figsize=(12, 6.2))
    fig.subplots_adjust(top=0.78, bottom=0.15, left=0.08, right=0.86)
    titulo(fig, tx["t"], tx["sub"])
    fx, cx, bx = [], [], []
    for i, d in enumerate(f):
        if i and (d - f[i - 1]).days > 2:   # hueco sin datos: no se dibuja una recta inventada
            fx.append(f[i - 1] + (d - f[i - 1]) / 2)
            cx.append(math.nan)
            bx.append(math.nan)
            ax.axvspan(f[i - 1], d, color="#f3f2ef", zorder=0)
            ax.text(f[i - 1] + (d - f[i - 1]) / 2, -8.5, tx["hueco"], ha="center", fontsize=10, color=TXT2)
        fx.append(d)
        cx.append(c[i])
        bx.append(b[i])
    lc, = ax.plot(fx, cx, color=AZUL, linewidth=2.2, zorder=3)
    lb, = ax.plot(fx, bx, color=NARANJA, linewidth=2.2, zorder=3)
    ax.axhline(0, color=TXT2, linewidth=1)
    meses = MESES[LANG]
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda v, _: (lambda d: f"{d.day}-{meses[d.month - 1]}" if LANG == "es" else f"{meses[d.month - 1]} {d.day}")(
            mdates.num2date(v))))
    for serie, color, etiqueta in ((c, AZUL, tx["cartera"]), (b, NARANJA, "BTC")):
        ax.text(f[-1], serie[-1], f"  {etiqueta} {'+' if serie[-1] > 0 else ''}{pct(serie[-1])}",
                color=TXT, va="center", fontsize=12.5, weight="bold")
        ax.plot([f[-1]], [serie[-1]], "o", color=color, markersize=8, markeredgecolor=SUP, markeredgewidth=2, zorder=4)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pct(v, 0)))
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    leg = ax.legend([lc, lb], [tx["leyenda"], "BTC"], loc="upper left", frameon=False)
    for t in leg.get_texts():
        t.set_color(TXT)
    fig.text(0.015, 0.075, tx["nota"], fontsize=10.5, color=TXT2)
    pie(fig, tx["fuente"])
    fig.savefig(OUT / nombre("I33_rentabilidad_vs_btc"), dpi=160)
    plt.close(fig)


TEXTOS = {
    "es": {
        "embudo": ("De millones de pruebas a cero estrategias con ventaja real",
                   "Lo que quedó en cada filtro de la investigación (cifras verificadas)",
                   [("≈15 M", "evaluaciones medidas\n(≈118 M más, solo declaradas)"),
                    ("380", "pruebas registradas\ncon su veredicto"),
                    ("7", "en observación\n(ninguna demostrada)"),
                    ("0", "con ventaja demostrada\nen ejecución real")],
                   "registro unificado y estudio de octubre de BICAPITAL"),
        "smc": ("SMC/ICT: la señal existe, pero es más pequeña que el coste",
                "11 millones de operaciones simuladas en 145 activos",
                ["Ganancia bruta media", "Coste medio real", "Resultado neto"],
                "R por operación", "laboratorio V24 (SMC) del motor V2",
                "R = una unidad de riesgo por operación. El coste es la media ponderada (0,11 R en H1 y 0,27 R en M15)."),
        "spread": ("El espejismo del spread: el mismo trade, tres precios",
                   "Entrada a la 01:00 del servidor, verificada con ticks bid/ask (8.063 días-par)",
                   ["Backtest con velas BID", "Precio medio", "Entrada real (ASK)"],
                   "R por operación", "verificación R04 con ticks, ene-2025 a sep-2026",
                   "A esa hora el spread se abre unas 3 veces la media y luego se cierra: el backtest «gana» ese cierre."),
        "twr": {"t": "Mi cartera real frente a Bitcoin: las primeras 7 semanas",
                "sub": "Rentabilidad ponderada en el tiempo de la parte invertida (las compras no la inflan). Solo porcentajes.",
                "hueco": "sin datos", "cartera": "Cartera", "leyenda": "Cartera (40 % BTC / 60 % altcoins)",
                "nota": "Del 24-ago al 14-oct-2026. Caída máxima de la cartera −9,8 %. Siete semanas no prueban nada: "
                        "es el punto de partida del diario.",
                "fuente": "registro diario de la cartera, cálculo TWR propio"},
        "riesgo": ("El riesgo que declaro antes de saber el resultado",
                   "Prueba walk-forward de la mezcla 40/60: 58 entradas mensuales, 30 meses cada una",
                   [("2,045×", "múltiplo mediano"), ("0,660×", "percentil 10\n(el peor 10 %)"),
                    ("29,9 %", "de los caminos\nterminan con pérdida"), ("−69,7 %", "caída mediana\ndesde el máximo")],
                   "validación walk-forward de la cartera (ventanas solapadas: tensión, no predicción)"),
    },
    "en": {
        "embudo": ("From millions of tests to zero strategies with a real edge",
                   "What survived each filter of the research (verified figures)",
                   [("≈15M", "evaluations measured\n(≈118M more, declared only)"),
                    ("380", "registered tests\nwith a verdict"),
                    ("7", "under observation\n(none proven)"),
                    ("0", "with a proven edge\nin live execution")],
                   "BICAPITAL unified registry and October study"),
        "smc": ("SMC/ICT: the signal exists, but it is smaller than the cost",
                "11 million simulated trades across 145 instruments",
                ["Average gross gain", "Average real cost", "Net result"],
                "R per trade", "BICAPITAL V24 (SMC) laboratory",
                "R = one unit of risk per trade. Cost is the weighted average (0.11 R on H1, 0.27 R on M15)."),
        "spread": ("The spread mirage: same trade, three prices",
                   "Entry at 01:00 server time, verified with bid/ask ticks (8,063 pair-days)",
                   ["Backtest on BID candles", "Mid price", "Real entry (ASK)"],
                   "R per trade", "BICAPITAL R04 tick verification, Jan-2025 to Sep-2026",
                   "At that hour the spread widens about 3x and then closes: the backtest 'earns' the closing spread."),
        "twr": {"t": "My real portfolio vs Bitcoin: the first 7 weeks",
                "sub": "Time-weighted return of the invested part (new purchases do not inflate it). Percentages only.",
                "hueco": "no data", "cartera": "Portfolio", "leyenda": "Portfolio (40% BTC / 60% altcoins)",
                "nota": "Aug 24 to Oct 14, 2026. Portfolio maximum drawdown −9.8%. Seven weeks prove nothing: "
                        "this is the starting point of the diary.",
                "fuente": "daily portfolio log, own TWR calculation"},
        "riesgo": ("The risk I declare before knowing the outcome",
                   "Walk-forward test of the 40/60 mix: 58 monthly entries, 30 months each",
                   [("2.045×", "median multiple"), ("0.660×", "10th percentile\n(worst 10%)"),
                    ("29.9%", "of paths\nend with a loss"), ("−69.7%", "median drawdown\nfrom the peak")],
                   "portfolio walk-forward validation (overlapping windows: stress test, not a forecast)"),
    },
}


def render(lang):
    global LANG
    LANG = lang
    tx = TEXTOS[lang]
    t, s, items, fuente = tx["embudo"]
    colores = [TXT, TXT, TXT, NARANJA]
    tiles(nombre("B01_embudo"), t, s, [(v, e, c) for (v, e), c in zip(items, colores)], fuente)
    t, s, etq, eje, fuente, nota = tx["smc"]
    barras(nombre("B01_smc_senal_vs_coste"), t, s, etq, [0.037, -0.238, -0.201], [AZUL, GRIS, NARANJA], "R", eje,
           fuente, nota)
    t, s, etq, eje, fuente, nota = tx["spread"]
    barras(nombre("B01_spread_0100"), t, s, etq, [0.209, 0.019, -0.228], [AZUL, GRIS, NARANJA], "R", eje, fuente, nota)
    twr(tx["twr"])
    t, s, items, fuente = tx["riesgo"]
    colores = [TXT, TXT, NARANJA, NARANJA]
    tiles(nombre("I33_riesgo_declarado"), t, s, [(v, e, c) for (v, e), c in zip(items, colores)], fuente,
          flechas=False)


if __name__ == "__main__":
    for lang in ("es", "en"):
        render(lang)
    print(sorted(p.name for p in OUT.glob("*.png")))
