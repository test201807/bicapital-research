# Datos de salud y plagas para el estudio El Niño en Ecuador

Carpeta: `datos/salud/`. Corte: 2026-10-25.

Todos los CSV están en UTF-8, separados por comas, y cada fila lleva `fuente_url` y `nota`. No se inventó ni se interpoló ningún número. Las celdas vacías significan "no encontrado". Las lecturas secundarias (prensa, gráficos, resúmenes) llevan `aproximado` en `nota`.

## Archivos

| Archivo | Contenido | Cobertura | Fuentes |
|---|---|---|---|
| `dengue_anual.csv` | Formato largo: una fila por año y fuente. Columnas: casos totales, DSSA, DCSA, dengue grave, muertes, incidencia, serotipos, evento ENSO. | Casos 1980-2026 (2026 hasta la SE41). Gravedad y muertes 2017-2026. Serotipos 1988-2026 con huecos. | PAHO/PLISA vía OpenDengue V1.3; gacetas vectoriales del MSP 2017-2026 (cierres de año y tabla histórica de 2026); OPS/MSP *Crónicas El Niño 1997-98*; Real-Cotto 2017 (serotipos); Sánchez 2025 (secundaria) |
| `dengue_semanal_o_mensual.csv` | ~10.000 filas. (a) Serie semanal nacional PAHO 2014-2024. (b) Tablas provinciales de cada gaceta MSP: casos de la SE, acumulado anterior y acumulado. (c) Acumulado nacional semanal 2025-2026 tomado del texto de las gacetas. (d) Serie semanal por provincia 2013 (MOH vía OpenDengue). (e) PAHO subnacional 2017-2020, incompleto. (f) Semestres 1996-98. | Gacetas por provincia: 2017 (32 semanas), 2018 (44), 2019 (46), 2020 (46), 2021 (46), 2022 (45), 2023 (36), 2024 (48), 2025 (SE5-20) y 2026 (8 semanas con desglose DCSA/DG/DSSA). Nacional 2025 completo (SE1-53) y 2026 SE1-41. | ~510 PDF de https://www.salud.gob.ec/gacetas-vectoriales/ (descargados y leídos automáticamente); OpenDengue |
| `otras_vectoriales.csv` | Malaria (total, vivax, falciparum), cólera (nacional y por provincia en 1998), leptospirosis (1998 mensual y 2023-25), chikungunya (por provincia 2014-2017), zika, leishmaniasis, Chagas, fiebre amarilla, Mayaro, bartonelosis. | 1982-84, 1991-92, 1993, 1996-98 y 2014-2026 | OPS/MSP 2000; gacetas MSP (SE09-2020, SE52-2017, SE53-2025, SE41-2026); prensa (Vistazo, Primicias) para leptospirosis reciente |
| `covid_ecuador.csv` | Por mes: casos y muertes COVID confirmados, muertes de todas las causas, esperadas y exceso. Incluye filas TOTAL por año. | 2020-01 a 2023-12 | OWID `cases_deaths/full_data.csv` (fuente WHO); OWID `excess_mortality.csv` (World Mortality Dataset, Registro Civil) |
| `mortalidad_general.csv` | Defunciones totales por año, principales causas y muertes atribuidas a eventos El Niño. Construido por un subagente. | Totales 1979-2024 (2025 aún no publicado por INEC). Causas en 1979-86 y 1997-2024. 8 filas de eventos El Niño. | INEC (serie 1.1.1 y microdatos), UN Demographic Yearbook, WHO, OPS, CEPAL |
| `plagas_agricolas.csv` | 51 filas: Fusarium R4T, sigatoka negra, moniliasis, roya, sogata/hoja blanca, caracol manzana, mosca de la fruta, langosta (Perú), mancha blanca y Taura en camarón, y evaluaciones de daño agrícola de El Niño 1982-83, 1997-98, 2015-16 y 2023-24. Construido por un subagente. | 1982-2026 | Agrocalidad/CAN, MAG, FAO, BID (Vos et al.), CEPAL, CAF, prensa |
| `evidencia_nino_salud.md` | Revisión de evidencia con citas: retrasos y magnitud de El Niño, lluvia y temperatura sobre dengue, malaria, leptospirosis y cólera en Ecuador y Perú. | — | Ver citas dentro del archivo |

## Advertencias

1. **Hay varias versiones (vintages) de cada año.** El MSP revisa sus cifras. Ejemplos:
   - 2021: 20.592 al cierre, 10.639 en la tabla de 2026 (probable error de esa tabla).
   - 2024: 61.329, 61.352, 61.400 o 61.810, según la publicación.

   Por eso `dengue_anual.csv` guarda todas las versiones y `fuente_tipo` dice de dónde sale cada una. Para una serie larga y homogénea, recomiendo la de **PAHO vía OpenDengue (1980-2024)** y, para 2025-2026, el MSP.
2. **La cifra de 1988 (420.025) es probablemente una estimación de la epidemia de Guayaquil**, no casos notificados.
3. **Las tablas provinciales de las gacetas se leyeron automáticamente de los PDF** con pdfplumber y posiciones de columnas.
   - Descarté 4 gacetas cuyo total rompía la secuencia acumulada (había tomado otra tabla).
   - Cuando la suma de provincias no coincide con el total nacional, `nota` lo indica: suele faltar una provincia porque las etiquetas del mapa se superponen.
   - `casos_periodo` en las gacetas son los casos que esa gaceta atribuye a la SE e incluyen notificación tardía.
4. **Faltan provincias en la segunda mitad de 2025 y en la mayor parte de 2026.** Esas gacetas solo publican tasas por provincia, no casos. Para esos periodos hay únicamente el total nacional.
5. **COVID:** los picos de muertes confirmadas en 2020-09 (4.736) y 2021-07 (9.312) son cargas retroactivas, no muertes del mes. El exceso agrupa semanas por la fecha de fin, así que el reparto mensual es aproximado.

## Huecos (no encontrados o no accesibles)

- **Dengue grave y muertes antes de 2017.** El portal PLISA (www3.paho.org) devolvía 502 y el nuevo portal Arbo de OPS (Tableau) no deja descargar datos sin sesión. Tampoco hay muertes anuales de dengue 1988-2016 ni casos por provincia de 2014-2016. La gaceta solo trae chikungunya por provincia para esos años.
- **Serie anual de malaria 1985-2014.** Solo tengo puntos sueltos (1982-84, 1993, 1996-98). Faltaría el World Malaria Report de OMS.
- **Serie anual de leptospirosis 1999-2022.** Las gacetas zoonóticas del MSP no estaban en las URL probadas. 2023-25 sale solo de prensa.
- **Cólera y diarrea en 1982-83.** No hay cifras de salud del Niño 1982-83, salvo malaria.
- **Exceso de mortalidad antes de 2020** y desglose de mortalidad por provincia.
- **Literatura.** El cupo de búsquedas web de la sesión se agotó. Quedaron pendientes los informes de OPS sobre 2023-24, los informes peruanos del INS/CDC sobre 2017 y 2023, y los textos completos de Gagnon 2001 y 2002.

## Cómo se construyó

- Los scripts de descarga y lectura están en el scratchpad de la sesión, no en esta carpeta.
- Herramientas: OpenDengue V1.3 (`Temporal`, `Spatial` y `National` extracts); los PDF del MSP leídos con pdftotext y pdfplumber; OWID desde GitHub.
- `mortalidad_general.csv` y `plagas_agricolas.csv` los construyeron subagentes con la misma regla de no inventar cifras. Revisé que todas sus filas tengan URL y verifiqué la URL del boletín de Fusarium R4T (CAN/Agrocalidad).
