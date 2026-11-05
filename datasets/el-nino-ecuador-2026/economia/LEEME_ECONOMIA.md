# Datos económicos – Estudio El Niño Ecuador 2026

Recopilado el 2026-10-25. Todos los CSV están en UTF-8, separados por comas, y cada fila tiene `fuente_url` y `nota`. No hay cifras inventadas ni interpoladas. Las celdas vacías son datos que no se encontraron.

Algunos valores están **calculados** a partir de niveles publicados (variaciones del índice, crecimiento a partir de VAB). Esas filas lo dicen en `nota` ("calculado del indice" o "calculado de niveles"). Las lecturas de gráficos o de fuentes secundarias llevan `aproximado` en `nota`.

## Aviso sobre la premisa
Según NOAA y ERFEN (ver `contexto_2025_2026.md`), **a fines de 2025 no había El Niño**. Hubo **La Niña de oct-2025 a mar-2026**. NOAA declaró condiciones El Niño el **11-jun-2026** y el ERFEN de Ecuador lo declaró presente el **28-ago-2026**. NOAA lo describía el 8-oct-2026 como un evento fuerte a muy fuerte, con pico esperado entre nov-2026 y mar-2027. Por tanto, "el último año" en los datos es en su mayor parte pre-Niño o La Niña. El efecto El Niño solo aparece desde jul–oct 2026.

## Archivos

| Archivo | Contenido | Cobertura | Fuente principal |
|---|---|---|---|
| `ipc_mensual.csv` | IPC general: índice y variaciones mensual, anual y acumulada. División Alimentos y bebidas no alcohólicas: índice y variaciones mensual y anual. Índice INEC base 2014 cuando se pudo leer. | General: 1990-01 a 2026-09. Alimentos: índice 1997-01 a 2026-07; variación mensual hasta 2026-09. | CEPALSTAT API (indicadores 365 y 1684, Ecuador, serie INEC empalmada) y boletines técnicos INEC jun, jul, ago y sep-2026. Contraste con FMI IMF.STA CPI. |
| `canasta_basica.csv` | Costo de la CFB y CFV, ingreso familiar, cobertura % y SBU. | 2015-01 a 2026-09, 141 meses sin huecos en las canastas. | Informes Ejecutivos de Canastas Analíticas de INEC (PDF mensuales) y tabulados CFBC/CFVB de sep-2026. |
| `precios_productos.csv` | Formato largo. (a) Precios mayoristas nacionales MAG SIPA (Azuay, Guayas, Pichincha) de arroz, banano, plátano, papa, tomate, cebolla, limón, huevos, pollo, leche y azúcar. (b) Precios de sustentación de banano, maíz, arroz y leche. (c) Prensa e INEC (variaciones por producto en sep-2026). (d) Precios internacionales mensuales de banano, cacao, camarón, café, Brent, WTI, arroz, maíz, azúcar y harina de pescado. | Nacional: sep-2024 a ago-2026, más algunos datos 2023 y 1997-98. Internacional: 1996-99, 2014-17 y 2022-01 a 2026-09. | MAG SIPA, INEC, prensa, World Bank Pink Sheet (actualizado 2-oct-2026) y FMI PCPS. |
| `pib_sectorial.csv` | Crecimiento real interanual por industria (20 a 36 ramas) y VAB a USD de 2018. | Trimestral BCE base 2018: 2001-T1 a 2026-T2. Trimestral BCE base 2007: 2001-T1 a 2023-T1 (separa camarón). Anual BCE 1980-2025, CEPAL base 1975 y WDI 1980-2025. | BCE (boletines 136 y 123 de Cuentas Nacionales), CEPALSTAT y WDI. |
| `pib_anual.csv` | Crecimiento del PIB real, PIB per cápita, inflación promedio anual y peso del agro en el PIB, con etiqueta de episodio El Niño. | 1980 a 2025. | API del Banco Mundial (WDI) y PIB BCE base 2018 copiado de `pib_sectorial.csv`. |
| `empleo.csv` | ENEMDU: desempleo, empleo adecuado, subempleo, otro empleo no pleno e informalidad; nacional, urbano y rural. | Trimestral dic-2007 a dic-2019. Mensual sep-2020 a may-2026 (serie nueva de INEC). | Tabulados ENEMDU de INEC, may-2026. |
| `exportaciones.csv` | Valor FOB y volumen de camarón, banano y plátano, cacao y elaborados, flores, crudo y derivados. | BCE mensual ene-2024 a ago-2026, anual 2024-2025 y acumulado ene-ago 2026. UN Comtrade anual 2015-2025 por código HS. | BCE y UN Comtrade. |
| `contexto_2025_2026.md` | Narrativa con fechas y enlaces: ENSO, lluvias e inundaciones 2026, electricidad (Mazar), precios, decretos, FMI, macro, y lecciones de 1997-98 y 2015-16. | Mediados de 2025 a oct-2026. | NOAA, SNGR, MAG, INEC, BCE, FMI y prensa. |

## Advertencias metodológicas clave

**IPC**
- **Cambio de base en jul-2026.** INEC publica desde julio de 2026 el IPC base jul2025–jun2026=100 (CCIF 2018, 348 productos, 13 divisiones), empalmado con la base 2014.
- La columna `indice_general` usa la serie empalmada nueva. Por eso el promedio de 2014 es 86.3 y no 100.
- La columna `indice_general_inec_base2014` contiene los valores del boletín de jun-2026 (jun-25 a jun-26). Se comprobó que los índices de CEPALSTAT coinciden con los boletines INEC. Las variaciones anuales calculadas coinciden con las del FMI (±0.05 pp) en todos los meses desde 2014.
- **El FMI (IMF.STA CPI) tiene mal mayo-2026**: da -0.99 % mensual y 0.54 % anual, frente a los valores oficiales de INEC de -0.62 % y 0.92 %. Para el período sep-2025 a sep-2026 se usaron los valores del boletín INEC.

**Canastas**
- **Cambio de canasta en jul-2026.** La CFBC (98 bienes) reemplaza a la CFB de 1982 y la CFVB reemplaza a la CFV. INEC dice que no son comparables con los meses anteriores.
- Desde jul-2026 no se publican ingreso familiar ni cobertura.

**Precios internacionales**
- **Brent sep-2026**: el Pink Sheet da 116.8 USD/bbl y el FMI PCPS 102.0. El WTI coincide (96.9 frente a 97.1). Hay que verificarlo antes de usarlo.
- El camarón del Pink Sheet está vacío en meses recientes. Se usa FMI PSHRI.
- Las unidades del FMI y del Banco Mundial difieren (USD/tm frente a $/kg, centavos/lb). Revisar la columna `unidad`.

**Cuentas nacionales y exportaciones**
- Antes de 2007, la serie anual BCE base 2018 repite las tasas de la base 2007.
- El camarón no tiene serie separada después de 2023-T1.
- Las cifras de Comtrade difieren de las agrupaciones del BCE. Por ejemplo, el crudo 2024 es 7 835 en Comtrade y 8 647 MUSD en el BCE.

## Vacíos

**Precios**
- No se encontró precio doméstico de pescado ni de camarón.
- No hay precio al productor de maíz duro después de 2024.
- No hay precios por producto para 2015-16 ni 1997-98 (solo agregados del IPC).
- El boletín SIPA de sep-2026 todavía no se publica.

**IPC y canastas**
- El índice de alimentos de ago y sep-2026 no está en CEPALSTAT; solo se tiene la variación mensual publicada por INEC.
- La variación anual de alimentos de ago y sep-2026 no se publica, porque INEC publicará las variaciones anuales por división desde jul-2027.
- Ingreso familiar y cobertura de la canasta para jul a sep-2026.

**Empleo**
- No hay datos ENEMDU de jun a sep-2026.
- No hay datos nacionales de mar y sep 2008-2013, ni de mar a jun 2020.

**Cuentas nacionales**
- No hay PIB trimestral antes de 2001; los boletines .xls de los años 90 no se leyeron.
- 2026-T3 todavía no se publica.
- No se incluyen las cifras de daño de CAF/CEPAL de 1997-98 en la tabla sectorial (sí aparecen en el `.md`).

**Exportaciones**
- Antes de 2024 solo hay datos anuales (Comtrade).
- Faltan pesos de Comtrade, por ejemplo todo 2023.
- El BCE no publica volúmenes no petroleros del acumulado 2026.
- No se usaron las asociaciones gremiales (CNA, AEBE, Anecacao, Expoflores).

**Contexto**
- No se consultó directamente al BoM, INAMHI ni CIIFEN.
- No hay pérdidas MAG consolidadas por cultivo.
- No se encontró la sexta revisión del FMI.

**Proceso**
- Se agotó el límite de búsquedas web de la sesión. Para ampliar estos vacíos hace falta una nueva sesión.

## Notas de proceso
- WebFetch guardó automáticamente copias de los PDF y xlsx consultados en la carpeta `tool-results` de la sesión de Claude. Esas copias se leyeron localmente con pdftotext y con un lector xlsx de la biblioteca estándar. No se instaló software.
- Las llamadas a las API (Banco Mundial, FMI SDMX, CEPALSTAT, Comtrade) se hicieron en memoria. Las URL exactas están en `fuente_url`.
