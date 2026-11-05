# El Niño 2026-27 in Ecuador: an open dataset

Seventeen tables that bring together the public data on El Niño in Ecuador: the ocean, rainfall, damage, crops, health,
prices, employment and exports. Every row carries its source URL and a note. The tables are used in the data report
[`articles/2026-11-E01`](../../articles/2026-11-E01), and `make_figures.py` recomputes every chart in it.

- **Data cut-off:** 25 October 2026. NOAA's October 2026 values were added on 5 November 2026: in `clima/oni_mensual.csv`,
  rows 2026-09 (ONI and RONI for Aug-Oct) and 2026-10 (OISST monthly).
- **Compiled by:** Héctor Sandoval, BICAPITAL Research (ORCID 0009-0008-4411-9851), with AI-assisted collection. Every
  figure was read from the cited source. Nothing was invented or interpolated: empty cells mean "not found". Values read
  from press reports, secondary sources or charts are marked `aproximado` in the `nota` column.
- **Language:** column names and notes are in Spanish. All CSV files are UTF-8, comma-separated.

## Tables

| File | Rows | What it contains | Main sources |
|---|---:|---|---|
| `clima/oni_mensual.csv` | 922 | Monthly ONI v5, ONI v6, RONI (NOAA's official index since 2026), Niño 1+2, Niño 3 and Niño 3.4 (ERSST v5 and OISST v2), 1950-2026 | NOAA CPC |
| `clima/eventos_nino_ecuador.csv` | 22 | El Niño events 1972-73 to 2026-27: index peaks, damage, deaths, people affected, hectares, roads | NOAA, ECLAC, CAF, PAHO, SNGR, IFRC, ERFEN |
| `clima/impactos_sectoriales_historicos.csv` | 61 | Damage by sector, 1982-83 and 1997-98 | ECLAC 1983, CAF 2000, PAHO/MSP |
| `clima/lluvias_costa.csv` | 215 | Monthly rainfall at coastal stations in El Niño seasons, with a computed 1971-2000 normal | NOAA NCEI GHCN-Monthly v4, ERFEN |
| `economia/ipc_mensual.csv` | 441 | Consumer prices: overall and food, 1990-2026 | INEC, CEPALSTAT, IMF |
| `economia/canasta_basica.csv` | 141 | Basic and vital food basket, family income, minimum wage, 2015-2026 | INEC |
| `economia/precios_productos.csv` | 3,673 | Wholesale, producer and international prices (rice, bananas, potatoes, eggs, cocoa, shrimp, coffee, oil and more) | MAG SIPA, INEC, World Bank, IMF, press |
| `economia/pib_sectorial.csv` | 10,114 | Real growth and value added by industry, quarterly and annual | Central Bank of Ecuador, CEPALSTAT, World Bank |
| `economia/pib_anual.csv` | 209 | GDP growth, GDP per capita, inflation and farm share of GDP, 1980-2025, tagged by El Niño episode | World Bank, Central Bank of Ecuador |
| `economia/empleo.csv` | 1,592 | Unemployment, adequate employment, underemployment and informality | INEC ENEMDU |
| `economia/exportaciones.csv` | 525 | Exports of shrimp, bananas, cocoa, flowers and oil | Central Bank of Ecuador, UN Comtrade |
| `salud/dengue_anual.csv` | 75 | Annual dengue cases, severe cases, deaths and serotypes, 1980-2026 (every published vintage kept) | PAHO via OpenDengue, MSP |
| `salud/dengue_semanal_o_mensual.csv` | 10,032 | Weekly dengue: national 2014-2026 and by province from MSP bulletins | PAHO, OpenDengue, MSP bulletins |
| `salud/otras_vectoriales.csv` | 226 | Malaria, cholera, leptospirosis, chikungunya, zika and others | PAHO/MSP, MSP bulletins |
| `salud/mortalidad_general.csv` | 375 | Total deaths and main causes; deaths attributed to El Niño events | INEC, UN, WHO, PAHO, ECLAC |
| `salud/covid_ecuador.csv` | 52 | COVID cases and deaths, all-cause and excess deaths, 2020-2023 | Our World in Data |
| `salud/plagas_agricolas.csv` | 51 | Crop pests and diseases (Fusarium R4T, black sigatoka, frosty pod rot, white spot) and farm damage assessments | Agrocalidad, MAG, FAO, IDB, ECLAC |

The Spanish notes in each folder (`LEEME_*.md`, `estado_enso_actual.md`, `contexto_2025_2026.md`,
`evidencia_nino_salud.md`) explain coverage, known gaps and methodological warnings.

## Known limits

- **Rainfall normals are computed** from the same GHCN station and include El Niño years; they are not INAMHI's official normals.
- **Data sources change over time.** The OISST series starts in 1982. CPC's official index changed to RONI in 2026; compare
  events with the same index.
- **Figures get revised.** Dengue totals are revised by the Ministry of Health, so all published versions are kept.
- **Series breaks.** INEC changed its CPI base and food basket in July 2026, so earlier months are not comparable.
- **Missing data:**
  - a quantitative rainfall forecast for December 2026 to April 2027;
  - dollar damage assessments for 2015-16, 2017 and 2023-24;
  - product prices in 1997-98;
  - employment from June to September 2026.

## License and citation

The compilation, notes and code are released under CC BY 4.0 (code: MIT). The underlying data remain subject to the terms of
each original source (NOAA data are public domain; World Bank, OWID and OpenDengue data are CC BY 4.0; Ecuadorian
government data are public). Please cite the original sources and:

> Sandoval, H. (2026). *El Niño 2026-27 in Ecuador: an open dataset* (version 2026-11-05). BICAPITAL Research.
> https://github.com/test201807/bicapital-research/tree/master/datasets/el-nino-ecuador-2026

*Data report for educational and informational purposes. Not an official forecast and not investment advice. For alerts
and safety decisions, follow Ecuador's Risk Management Secretariat, INAMHI and INOCAR.*

---

## En español

Diecisiete tablas con los datos públicos sobre El Niño en Ecuador: océano, lluvia, daños, cultivos, salud, precios, empleo
y exportaciones. Cada fila lleva la URL de su fuente y una nota. Las usa el informe
[`articles/2026-11-E01`](../../articles/2026-11-E01), y `make_figures.py` recalcula todas sus gráficas.

- **Corte de datos:** 25 de octubre de 2026. El 5 de noviembre se añadieron los valores de la NOAA de octubre.
- **Reglas de la compilación:** ninguna cifra se inventó ni se interpoló; una celda vacía significa «no encontrado». Lo
  leído en prensa, en fuentes secundarias o en gráficos lleva `aproximado` en la columna `nota`.
- **Licencia:** CC BY 4.0 para la compilación y MIT para el código. Los datos originales mantienen los términos de cada
  fuente.

*Informe de datos con fines educativos. No es un pronóstico oficial ni asesoría de inversión.*
