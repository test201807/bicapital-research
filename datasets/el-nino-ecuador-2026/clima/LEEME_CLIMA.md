# LEEME — datos/clima (estudio El Niño 2026, Ecuador)

- **Fecha de recopilación:** 25-oct-2026.
- **Formato:** todos los CSV están en UTF-8, separados por comas, y cada fila tiene `fuente_url` y `nota`.
- **Reglas:** no se inventó ni se interpoló ninguna cifra. Las celdas vacías corresponden a datos no encontrados o no aplicables. Todo valor de prensa, de fuente secundaria o de un gráfico lleva la marca `aproximado` en `nota`.
- **Cálculos derivados:** los pocos que hay (porcentajes, normales de lluvia, picos de cada evento) se señalan como tales en `nota`.

## Archivos

### 1. `oni_mensual.csv` — 921 filas × 17 columnas, 1950-01 a 2026-09
Una fila por mes. Para el ONI, el mes es el mes **central** de la temporada de 3 meses (DJF → enero).

| Columnas | Contenido | Cobertura | Fuente |
|---|---|---|---|
| `temporada_oni_3m`, `oni_v5_sst_total_c`, `oni_v5_anom_c` | ONI v5 (ERSSTv5, climatologías móviles de 30 años) | 1950 DJF a 2026 JAS | https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt |
| `oni_v6_anom_c` | ONI v6 (ERSSTv6), 1 decimal | 1950 a 2026 JAS | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/oni/v6/ (tabla HTML) |
| `roni_anom_c`, `categoria_roni_mes` | **RONI, el índice oficial de CPC desde 2026** (NWS PIS 26-05), 1 decimal; la categoría es la del mes suelto | 1950 a 2026 JAS | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/ (tabla HTML) |
| `nino12_ersst5_sst_c`, `nino12_ersst5_anom_c`, `nino34_ersst5_anom_c` | Niño 1+2 y Niño 3.4 mensuales en ERSSTv5, base 1991-2020 | 1950-01 a **2026-06** (el archivo no estaba actualizado más allá) | https://www.cpc.ncep.noaa.gov/data/indices/ersst5.nino.mth.91-20.ascii |
| `nino12_oisst_*`, `nino3_oisst_anom_c`, `nino34_oisst_anom_c` | OISST v2 mensual, base 1991-2020 | **1982-01** a 2026-09 | https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices |

**Advertencias:**
- Los últimos valores de RONI y ONI pueden revisarse hasta 2 meses después.
- No se pudo resolver `origin.cpc.ncep.noaa.gov`. Se usó el archivo ascii equivalente.
- Los semanales de Niño 1+2 (wksst9120.for) no se guardaron como CSV. Están resumidos en `estado_enso_actual.md`.

### 2. `estado_enso_actual.md`
Contiene:
- la verificación de la premisa;
- CPC (8-oct-2026): tablas de RONI y de probabilidades por intensidad;
- IRI (19-oct-2026);
- CN-ERFEN 007, 08, 010 y 011-2026 (28-ago, 4-sep, 1-oct y 22-oct-2026);
- ENFEN N°18-2026 (16-oct-2026);
- impactos hasta la fecha.

### 3. `eventos_nino_ecuador.csv` — 22 filas × 31 columnas
- **Eventos:** 1972-73, 1982-83, 1997-98, 2015-16, 2017 costero, 2023-24 y 2026-27 (en curso).
- **Estructura:** cada evento tiene una fila de "índices NOAA" (fechas de inicio, pico y fin, pico de ONI v5 y RONI, pico de Niño1+2, todo derivado de `oni_mensual.csv`) y una fila por cada fuente de impactos.
- **Métricas:** daños en millones de USD (total, directos e indirectos, con año de precios), % del PIB, muertes, heridos, desaparecidos, afectados, damnificados, familias, viviendas afectadas y destruidas, ha perdidas y afectadas, km de vías, puentes y sectores principales.
- **Fuentes:**
  - CEPAL 1983 E/CEPAL/G.1274 (final) y G.1240 (preliminar), vía copias de Internet Archive.
  - CAF 2000 "Las lecciones de El Niño: Ecuador".
  - MSP/OPS "Crónicas" (cap. Ecuador).
  - ONU Ecuador.
  - SGR/SNGR (2016, 2017).
  - IFRC DREF MDREC026 (2024).
  - ECOSOC 2016.
  - Martínez et al. 2017 (Redalyc).
  - ERFEN 2026.
  - Prensa (aproximado).

### 4. `impactos_sectoriales_historicos.csv` — 61 filas × 13 columnas
Daños por sector y subsector en millones de USD (total, directo e indirecto) y % del total del evento. El % está **calculado**, porque las fuentes no lo imprimen.

| Evento | Fuente | Precios | Total |
|---|---|---|---|
| 1982-83 | CEPAL G.1274, Cuadro 7 | USD de 1983 | 640.6 |
| 1982-83 | CAF 2000, Cuadro III.2.1-4 | USD de 1998 | 1 051 |
| 1997-98 | CAF 2000, Cuadro III.2.1-3 | corrientes | 2 881.6 |
| 1997-98 | MSP/OPS, Cuadro 1, citando a CEPAL | no indicado | 2 869.3 |

**Advertencia:** en 1997-98 las columnas directo/indirecto se reconstruyeron a partir de extracciones de PDF con columnas desalineadas, y se verificaron porque suman el total de cada fila. Los totales por sector se leyeron directamente.

### 5. `lluvias_costa.csv` — 215 filas × 12 columnas
Precipitación mensual en mm, de septiembre del año de inicio a junio del año siguiente, para las temporadas 1972-73, 1982-83, 1997-98, 2015-16, 2016-17, 2023-24 y 2025-26, cuando hay datos.

**Estaciones (GHCN-Monthly v4, NOAA NCEI):** https://www.ncei.noaa.gov/data/ghcnm/v4/precipitation/access/<ID>.csv

| Estación | ID | Temporadas con datos |
|---|---|---|
| Guayaquil | ECMLP084203 | 1972-73, 1982-83, 1997-98 |
| Guayaquil, serie alternativa | ECMLP084129 | 1972-73, 1982-83 |
| Portoviejo | ECM00084135 | 1972-73, 1982-83, 1997-98, 2015-16, 2016-17, 2025-26 parcial |
| Esmeraldas | ECMLP084018 | 1972-73, 1997-98 |
| Machala | ECMLP084248 | 1997-98 |
| Milagro | ECMLP084022 | 1972-73, 1982-83, 1997-98 |
| Babahoyo | ECMLP084190 | 1982-83, 1997-98 |

**Otras filas:**
- **Guayaquil 2015-16, 2016-17 y 2023-24:** suma de diarios NOAA GSOD, marcada `aproximado` porque subestima el total.
- **Milagro, octubre de 2026:** acumulado parcial del 1 al 20 de octubre, tomado del informe ERFEN 011.

**`normal_mm`:** es una media 1971-2000 **calculada** del mismo archivo GHCN. Incluye años Niño, usa solo meses sin bandera QC y no es la normal oficial de INAMHI. `pct_de_normal` también está calculado y no tiene sentido en los meses secos, de normal cercana a cero.

## Vacíos conocidos
1. **1972-73:** no hay daños en USD, % del PIB, muertes, afectados, ha ni km. Solo hay una mención cualitativa en CAF 2000.
2. **CEPAL 1998 (LC/L.1122 o LC/R.1822) original:** no se pudo descargar porque el repositorio de CEPAL bloquea el acceso automático. Se usaron CAF 2000 y MSP/OPS, que lo reproducen. Las cifras difieren:
   - total: 2 881.6 frente a 2 869.3;
   - % del PIB: 14.58% frente a 17%;
   - muertes: 286, 288 o 292.
3. **1982-83:** no hay muertes finales (solo ~50 al 15-feb-1983), ni ha totales de cultivos (solo cifras preliminares parciales), ni % del PIB publicado para Ecuador solo.
4. **2015-16, 2017 y 2023-24:** no hay una evaluación de daños en USD ni de % del PIB (ninguna evaluación CEPAL, BM o BID encontrada). Solo hay conteos SNGR/SGR de personas, viviendas, ha y km. Además:
   - los conteos cubren toda la época lluviosa, no solo el efecto de El Niño;
   - los de 2016 se mezclan con el terremoto del 16-abr-2016;
   - las cifras ECOSOC 2016 son fragmentos de búsqueda, porque el PDF dio 403.
5. **2026-27:**
   - no hay pico observado todavía;
   - no hay daños en USD;
   - no hay un pronóstico estacional cuantitativo de INAMHI para la costa de dic-2026 a abr-2027 (solo cualitativo: "sobre lo normal");
   - los impactos de la SNGR provienen de prensa.
6. **Lluvias:**
   - no hay anuarios INAMHI en línea para los años Niño;
   - no hay datos GHCN de Machala ni de Esmeraldas para 1982-83;
   - no hay ninguna estación con una serie oficial completa para 2023-24;
   - Manta solo tiene datos hasta 1981;
   - no se consultaron las tablas de la literatura (Rossel/IRD), porque el servidor IRD estaba en mantenimiento.
7. **Camarón y pesca:** no hay una línea de daños separada para el camarón en 1997-98. Según Vos et al. (BID 1999), la productividad del camarón subió más del 25%, es decir, hubo un efecto positivo.
