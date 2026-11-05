"""Figures for the data report "El Niño 2026-27 in Ecuador" (Spanish and English).

Reads the CSV tables in this folder and recomputes every figure shown in the article; prints the numbers.
Usage:  python make_figures.py   ->  ./figures/E01_*.png (es) and *_en.png (en)
Requires pandas and matplotlib. License: MIT (see repository LICENSE).
"""
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

DATOS = pathlib.Path(__file__).resolve().parent
OUT = DATOS / "figures"
OUT.mkdir(exist_ok=True)
SUP, TXT, TXT2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
AZUL, NARANJA, GRIS = "#2a78d6", "#eb6834", "#8a8984"
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



def base(t, sub):
    fig, ax = plt.subplots(figsize=(12, 6.2))
    fig.subplots_adjust(top=0.78, bottom=0.22, left=0.08, right=0.97)
    titulo(fig, t, sub)
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    ax.spines[["top", "right"]].set_visible(False)
    return fig, ax



def cierre(fig, ax, archivo, fuente, nota, handles=None, labels=None, loc="upper right"):
    if handles:
        leg = fig.legend(handles, labels, loc="upper left", bbox_to_anchor=(0.075, 0.855), ncol=len(labels), frameon=False)
        for tt in leg.get_texts():
            tt.set_color(TXT)
    if nota:
        fig.text(0.015, 0.075, nota, fontsize=10.5, color=TXT2, ha="left")
    pie(fig, fuente)
    fig.savefig(OUT / archivo, dpi=160)
    plt.close(fig)



def grupos(archivo, t, sub, cats, series, valores, colores, fmt, eje, fuente, nota, ymin, ymax, linea=None,
           loc="upper right"):
    fig, ax = base(t, sub)
    k = len(series)
    w = 0.8 / k
    xs = list(range(len(cats)))
    hs = []
    for j, (vals, col) in enumerate(zip(valores, colores)):
        pos = [x - 0.4 + w * (j + 0.5) for x in xs]
        hs.append(ax.bar([p for p, v in zip(pos, vals) if v is not None], [v for v in vals if v is not None],
                         width=w * 0.92, color=col, zorder=2))
        for p, v in zip(pos, vals):
            if v is not None:
                off = (ymax - ymin) * 0.015
                ax.text(p, v + off if v >= 0 else v - off, fmt(v), ha="center", va="bottom" if v >= 0 else "top",
                        fontsize=11.5, color=TXT, weight="bold")
    if linea is not None:
        ax.axhline(linea, color=TXT2, linewidth=1.2, linestyle="--", zorder=1)
    ax.set_xticks(xs, cats)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: num(v, 2 if ymax - ymin < 1 else (1 if ymax < 2 else 0))))
    ax.set_ylim(ymin, ymax)
    ax.set_ylabel(eje)
    cierre(fig, ax, archivo, fuente, nota, hs if k > 1 else None, series if k > 1 else None, loc)




GRIS_OSC = "#3f3e3b"


def cargar():
    d = {}
    o = pd.read_csv(DATOS / "clima" / "oni_mensual.csv")
    d["oni"] = o
    d["lluvia"] = pd.read_csv(DATOS / "clima" / "lluvias_costa.csv")
    d["danos"] = pd.read_csv(DATOS / "clima" / "impactos_sectoriales_historicos.csv")
    d["pib"] = pd.read_csv(DATOS / "economia" / "pib_sectorial.csv", low_memory=False)
    d["ipc"] = pd.read_csv(DATOS / "economia" / "ipc_mensual.csv")
    d["dsem"] = pd.read_csv(DATOS / "salud" / "dengue_semanal_o_mensual.csv", low_memory=False)
    return d


# --- cálculos -------------------------------------------------------------------------------------------------

EVENTOS = [(1982, "1982-83"), (1997, "1997-98"), (2015, "2015-16"), (2023, "2023-24"), (2026, "2026-27")]


def nino12_alineado(o):
    """Anomalía Niño 1+2 (OISST) de enero del año de inicio a junio del siguiente."""
    o = o.dropna(subset=["nino12_oisst_anom_c"])
    out = {}
    for y0, et in EVENTOS:
        s = o[((o.anio == y0)) | ((o.anio == y0 + 1) & (o.mes <= 6))].copy()
        s["k"] = (s.anio - y0) * 12 + s.mes - 1
        out[et] = s[["k", "nino12_oisst_anom_c"]].values.tolist()
    return out


def lluvia_gye(ll):
    g = ll[(ll.estacion.str.startswith("Guayaquil (Aero")) & (ll.temporada_nino == "1997-98")]
    return g.mes.tolist(), g.precip_mm.tolist(), g.normal_mm.tolist()


def danos_9798(dn):
    t = dn[(dn.evento == "1997-98") & (dn.fuente_corta.str.startswith("CAF")) & (dn.nivel.isin(["sector", "subtotal"]))]
    total = 2881.6
    agri = t[t.sector == "Agricultura"].danos_total_musd.item()
    trans = t[t.sector == "Transportes (subtotal)"].danos_total_musd.item()
    emerg = t[t.sector == "Prevencion y emergencia"].danos_total_musd.item()
    viv = t[t.sector == "Vivienda"].danos_total_musd.item()
    ind = t[t.sector.isin(["Industria", "Comercio", "Turismo"])].danos_total_musd.sum()
    resto = total - agri - trans - emerg - viv - ind
    vals = [agri, trans, emerg, ind, viv, resto]
    return [round(100 * v / total, 1) for v in vals], vals


def cultivos(pib):
    a = pib[(pib.frecuencia == "anual") & (pib.variable == "crecimiento_real_interanual_pct")
            & (pib.base == "BCE base 2018 (encadenado, retropolado)")]
    sec = ["Cultivo de banano, café y cacao", "Otros cultivos agrícolas", "Pesca y acuicultura", "TOTAL PIB"]
    anios = ["1983", "1998", "2016", "2024"]
    return [[round(a[(a.sector == s) & (a.periodo.astype(str) == y)].valor.item(), 1) for y in anios] for s in sec]


def dengue_seco(ds):
    """Casos semanales medios en las semanas 31-41 (estación seca de la costa)."""
    n = ds[ds.nivel == "nacional"]
    p = n[(n.periodo_tipo == "semana_epi") & n.anio.between(2014, 2024)].copy()
    p["se"] = p.semana_epi.astype(int)
    res = {int(a): g[(g.se > 30) & (g.se <= 41)].casos_periodo.sum() / 11 for a, g in p.groupby("anio")}
    acc = n[(n.periodo_tipo == "acumulado semanal (texto gaceta)")].copy()
    acc["se"] = acc.semana_epi.astype(int)
    for a in (2025, 2026):
        g = acc[acc.anio == a].set_index("se").casos_acum_hasta_periodo
        res[a] = (g[41] - g[30]) / 11
    return {k: round(v) for k, v in sorted(res.items())}


def alimentos(ipc):
    i = ipc.set_index("fecha")
    out = {}
    for et, a, b in [("2015-16", "2015-07", "2016-06"), ("2023-24", "2023-07", "2024-06")]:
        s = i.loc[a:b]
        out[et] = (s.alimentos_var_anual_pct.max(), s.inflacion_anual_pct.max())
    return out


# --- textos ---------------------------------------------------------------------------------------------------

TX = {
    "es": {
        "n12": ("Frente a Ecuador, el mar ya está más caliente que en 1997-98",
                "Anomalía de la temperatura del mar en la región Niño 1+2, mes a mes desde enero del año de inicio",
                "°C sobre lo normal", "NOAA CPC, OISST v2 (base 1991-2020)",
                "Octubre de 2026: +5,25 °C, el mayor valor mensual desde que empieza la serie (1982)."),
        "lluvia": ("En 1997-98 el mar tocó techo a fines de 1997; la lluvia, en abril",
                   "Guayaquil (aeropuerto), lluvia mensual de septiembre de 1997 a junio de 1998",
                   ["1997-98", "Normal 1971-2000 (calculada)"], "mm al mes", "NOAA NCEI, GHCN-Monthly v4",
                   "La normal se calculó con la misma estación e incluye años de El Niño; no es la oficial del INAMHI."),
        "danos": ("1997-98: el campo y las carreteras se llevaron casi el 70 % del daño",
                  "Daños de El Niño 1997-98 en Ecuador por sector, % del total (2.881,6 millones de USD, 14,6 % del PIB)",
                  ["Agricultura", "Transporte", "Prevención y\nemergencia", "Industria, comercio\ny turismo", "Vivienda",
                   "Resto"], "% del daño total", "CAF (2000), que resume la evaluación de CEPAL de 1998",
                  "Incluye daños directos e indirectos, a precios corrientes de 1997-98."),
        "cult": ("Banano, café y cacao: lo primero que cae en un El Niño extremo",
                 "Crecimiento real del año del impacto, % frente al año anterior",
                 ["1983", "1998", "2016", "2024"], ["Banano, café y cacao", "Otros cultivos", "Pesca y acuicultura",
                                                    "PIB total"], "% real", "BCE, cuentas nacionales base 2018 (series retropoladas)",
                 "2016 incluye el terremoto de abril; 2024, la crisis eléctrica. Pocos casos: describe, no prueba causa."),
        "dengue": ("El dengue de 2026 no bajó en la estación seca",
                   "Casos semanales medios de dengue entre las semanas 31 y 41 (agosto a mediados de octubre)",
                   "casos por semana", "OPS vía OpenDengue (2014-2024) y gacetas del MSP (2025-2026)",
                   "Azul: años en que empezaba un El Niño. 2025-2026 salen de acumulados de gaceta (incluyen notificación tardía)."),
    },
    "en": {
        "n12": ("Off Ecuador, the sea is already warmer than in 1997-98",
                "Sea temperature anomaly in the Niño 1+2 region, month by month from January of the onset year",
                "°C above normal", "NOAA CPC, OISST v2 (1991-2020 base)",
                "October 2026: +5.25 °C, the highest monthly value since the series began (1982)."),
        "lluvia": ("In 1997-98 the sea peaked in late 1997; the rain, in April",
                   "Guayaquil (airport), monthly rainfall from September 1997 to June 1998",
                   ["1997-98", "1971-2000 normal (computed)"], "mm per month", "NOAA NCEI, GHCN-Monthly v4",
                   "The normal was computed from the same station and includes El Niño years; it is not INAMHI's official one."),
        "danos": ("1997-98: farming and roads took almost 70% of the damage",
                  "El Niño 1997-98 damage in Ecuador by sector, % of total (USD 2,881.6 million, 14.6% of GDP)",
                  ["Agriculture", "Transport", "Prevention and\nemergency", "Industry, trade\nand tourism", "Housing",
                   "Other"], "% of total damage", "CAF (2000), summarising ECLAC's 1998 assessment",
                  "Direct and indirect damage, at current 1997-98 prices."),
        "cult": ("Bananas, coffee and cocoa: the first to fall in an extreme El Niño",
                 "Real growth in the impact year, % vs the previous year",
                 ["1983", "1998", "2016", "2024"], ["Bananas, coffee and cocoa", "Other crops", "Fishing and aquaculture",
                                                    "Total GDP"], "% real", "Central Bank of Ecuador, national accounts base 2018 (back-cast series)",
                 "2016 includes the April earthquake; 2024, the power crisis. Few cases: it describes, it does not prove cause."),
        "dengue": ("Dengue in 2026 did not fall in the dry season",
                   "Average weekly dengue cases in epidemiological weeks 31 to 41 (August to mid-October)",
                   "cases per week", "PAHO via OpenDengue (2014-2024) and Ministry of Health bulletins (2025-2026)",
                   "Blue: years in which an El Niño was starting. 2025-2026 come from cumulative bulletin totals (include late reports)."),
    },
}


# --- figuras --------------------------------------------------------------------------------------------------

def fig_nino12(tx, serie):
    t, sub, eje, fuente, nota = tx["n12"]
    fig, ax = base(t, sub)
    estilo = {"1982-83": (GRIS_OSC, 2.0, "-"), "1997-98": (AZUL, 2.4, "-"), "2015-16": (GRIS, 1.6, "--"),
              "2023-24": (GRIS, 1.6, ":"), "2026-27": (NARANJA, 3.2, "-")}
    for et, pts in serie.items():
        col, lw, ls = estilo[et]
        k = [p[0] for p in pts]
        v = [p[1] for p in pts]
        ax.plot(k, v, color=col, linewidth=lw, linestyle=ls, zorder=3 if et == "2026-27" else 2)
        ax.text(k[-1] + 0.25, v[-1], et, color=TXT, fontsize=11.5, weight="bold" if et in ("2026-27", "1997-98") else None,
                va="center")
    meses = MESES[LANG]
    ticks = list(range(0, 18, 2))
    ax.set_xticks(ticks, [meses[k % 12] + ("\n" + ("año 0" if LANG == "es" else "year 0") if k == 0 else
                                           ("\n" + ("año 1" if LANG == "es" else "year 1") if k == 12 else "")) for k in ticks])
    ax.axhline(0, color=TXT2, linewidth=1)
    ax.set_xlim(-0.3, 19.5)
    ax.set_ylim(-2, 6)
    ax.set_ylabel(eje)
    cierre(fig, ax, nombre("E01_nino12"), fuente, nota)


def render(lang, d, calc):
    global LANG
    LANG = lang
    tx = TX[lang]
    fig_nino12(tx, calc["n12"])
    t, s, series, eje, fuente, nota = tx["lluvia"]
    meses, mm, normal = calc["lluvia"]
    cats = [MESES[lang][m - 1] for m in meses]
    grupos(nombre("E01_lluvia_gye"), t, s, cats, series, [mm, normal], [AZUL, GRIS],
              lambda v: num(v, 0), eje, fuente, nota, 0, 1300, loc="upper left")
    t, s, cats, eje, fuente, nota = tx["danos"]
    grupos(nombre("E01_danos_9798"), t, s, cats, ["x"], [calc["danos"][0]], [AZUL],
              lambda v: pct(v, 1), eje, fuente, nota, 0, 50)
    t, s, cats, series, eje, fuente, nota = tx["cult"]
    grupos(nombre("E01_cultivos"), t, s, cats, series, calc["cult"], [NARANJA, AZUL, GRIS_OSC, GRIS],
              lambda v: num(v + 0.0 if round(v, 1) != 0 else 0.0, 1), eje, fuente, nota, -45, 15, linea=0)
    t, s, eje, fuente, nota = tx["dengue"]
    ds = calc["dengue"]
    anios = list(ds)
    fig, ax = base(t, s)
    cols = [NARANJA if a == 2026 else (AZUL if a in (2015, 2023) else GRIS) for a in anios]
    ax.bar(range(len(anios)), [ds[a] for a in anios], color=cols, width=0.72, zorder=2)
    for x, a in enumerate(anios):
        ax.text(x, ds[a] + 18, num(ds[a], 0), ha="center", va="bottom", fontsize=11, color=TXT, weight="bold")
    ax.set_xticks(range(len(anios)), [str(a) for a in anios])
    ax.set_ylim(0, 1600)
    ax.set_ylabel(eje)
    cierre(fig, ax, nombre("E01_dengue_seco"), fuente, nota)


if __name__ == "__main__":
    d = cargar()
    calc = {"n12": nino12_alineado(d["oni"]), "lluvia": lluvia_gye(d["lluvia"]), "danos": danos_9798(d["danos"]),
            "cult": cultivos(d["pib"]), "dengue": dengue_seco(d["dsem"])}
    print("Niño1+2 máximos:", {k: max(p[1] for p in v) for k, v in calc["n12"].items()})
    m, mm, nn = calc["lluvia"]
    print("Lluvia GYE 1997-98:", dict(zip(m, mm)), "total", round(sum(mm), 1), "normal", round(sum(nn), 1),
          "x", round(sum(mm) / sum(nn), 2))
    print("Daños 97-98 %:", calc["danos"][0], "MUSD:", calc["danos"][1])
    print("Cultivos:", calc["cult"])
    print("Dengue SE31-41:", calc["dengue"])
    print("Alimentos (máx anual alimentos, máx anual general):", alimentos(d["ipc"]))
    for lang in ("es", "en"):
        render(lang, d, calc)
    print(sorted(p.name for p in OUT.glob("E01_*.png")))
