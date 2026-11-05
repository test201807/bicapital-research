# Estado ENSO actual (corte 25-oct-2026)

## Verificacion de la premisa (leer primero)

**Premisa:** "hay un El Niño en curso y le faltan unos 2 meses para llegar a su pico".

- **"El Niño en curso": CONFIRMADO.** NOAA CPC mantiene el estado "El Niño Advisory" (discusión del 8-oct-2026). El CN-ERFEN declaró oficialmente El Niño en Ecuador el **28-ago-2026** (Informe ERFEN 007-2026), y la SNGR emitió la alerta roja nacional. La prensa la fecha el 28 o el 29-ago-2026: Vistazo habla de una resolución del 28-ago y KCH, del 29-ago. Es un evento **canónico muy fuerte** (Pacífico central, Niño 3.4) y además un **El Niño costero extraordinario** (Niño 1+2, frente a Ecuador y Perú). Las dos cosas ocurren a la vez.
- **"Pico en ~2 meses": APROXIMADAMENTE CIERTO, pero probablemente un poco antes.**
  - En el **océano** (índice central de Niño 3.4), el pico previsto es la temporada **OND 2026** (centrada en noviembre). Es decir, a **~0-1 mes** de hoy, con una meseta hasta NDJ (centrada en diciembre).
    - CPC (RONI, mediana): OND 2.74; NDJ 2.65; DJF 2.36.
    - IRI (plume): ~+3.5 °C tanto en OND como en NDJ.
  - En **Niño 1+2** (la costa ecuatoriana), ENFEN (Perú) prevé magnitud **extraordinaria hasta enero de 2027**.
  - Los **impactos en lluvias en Ecuador** se dan normalmente **después** del pico oceánico, en la estación lluviosa de la costa (enero-abril).
    - En 1997-98 el ONI tocó máximo en NDJ 1997, pero en Guayaquil las lluvias máximas fueron en marzo (911 mm) y abril (1 138 mm) de 1998 (ver `lluvias_costa.csv`).
    - Para el estudio, el máximo **de impactos** debería esperarse **ene-abr 2027**, es decir a ~3-6 meses.
- **Cambio de índice oficial:** desde 2026, CPC usa el **RONI** (Relative ONI, ERSSTv6) como índice oficial (NWS Public Information Statement 26-05). No usa el ONI clásico.
  - Las magnitudes difieren. Para JAS 2026: **RONI = 1.7**, ONI v6 = 2.2 y ONI v5 = 2.16.
  - Comparar con eventos pasados exige usar el mismo índice. `oni_mensual.csv` trae los tres.

## 1. NOAA CPC — ENSO Diagnostic Discussion (emitida 8-oct-2026; próxima 12-nov-2026)
Fuente: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml

- **Estado:** El Niño Advisory.
- **Sinopsis (cita):** "El Niño continues to strengthen, with a strong-to-very strong El Niño likely through January-March 2027".
- **Observado:**
  - Anomalías del mes pasado: Niño-3.4 +2.1 °C, Niño-3 +3.0 °C, Niño-1+2 +3.9 °C.
  - Anomalías de TSM de más de +4.0 °C en partes del Pacífico ecuatorial oriental.
  - Subsuperficie de más de +10 °C en profundidad en el Pacífico oriental.
  - SOI tradicional y ecuatorial "significativamente negativos".
- **Probabilidad de un evento "histórico"** (RONI de 3 meses ≥ +2.5 °C, superior a cualquier El Niño desde 1950): 54% para SON, 83% para OND y 70% para NDJ.

**Pronóstico oficial de RONI** (emitido oct-2026). Fuente: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/outlook/

| Temporada | P5 | P25 | **Mediana** | P75 | P95 |
|---|---|---|---|---|---|
| SON 2026 | 2.18 | 2.35 | **2.47** | 2.59 | 2.76 |
| OND 2026 | 2.25 | 2.54 | **2.74** | 2.94 | 3.23 |
| NDJ 2026-27 | 2.00 | 2.39 | **2.65** | 2.92 | 3.31 |
| DJF 2026-27 | 1.58 | 2.04 | **2.36** | 2.68 | 3.14 |
| JFM 2027 | 1.13 | 1.59 | **1.90** | 2.22 | 2.67 |
| FMA 2027 | 0.66 | 1.05 | **1.33** | 1.60 | 2.00 |
| MAM 2027 | 0.23 | 0.58 | **0.83** | 1.08 | 1.43 |
| AMJ 2027 | -0.22 | 0.14 | **0.40** | 0.66 | 1.02 |
| MJJ 2027 | -0.68 | -0.26 | **0.03** | 0.32 | 0.74 |

**Probabilidades por categoría de intensidad, % de El Niño** (CPC, oct-2026). Fuente: https://cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/strengths/

| Temporada | Débil 0.5-1.0 | Moderado 1.0-1.5 | Fuerte 1.5-2.0 | Muy fuerte ≥2.0 |
|---|---|---|---|---|
| SON | 0 | 0 | 0 | 100 |
| OND | 0 | 0 | 0 | 100 |
| NDJ | 0 | 0 | 4 | 96 |
| DJF | 0 | 3 | 16 | 81 |
| JFM | 2 | 15 | 37 | 46 |
| FMA | 16 | 44 | 32 | 6 |
| MAM | 48 | 32 | 5 | 0 |
| AMJ | 38 | 7 | 0 | 0 (54 neutral) |
| MJJ | 15 | 2 | 0 | 0 (70 neutral) |

Una lectura (mía, no de CPC): la mediana más alta está en **OND 2026**. El Niño se debilitaría rápido desde FMA 2027, y lo más probable es que se pase a neutral entre AMJ y MJJ de 2027.

**Datos semanales CPC (OISST, base 1991-2020).** Fuente: https://www.cpc.ncep.noaa.gov/data/indices/wksst9120.for

| Semana centrada | Niño1+2 anomalía °C | Niño3 | Niño3.4 | Niño4 |
|---|---|---|---|---|
| 02-sep-2026 | 4.4 | 3.5 | 2.8 | 1.0 |
| 16-sep-2026 | 4.7 | 3.8 | 3.0 | 1.0 |
| 23-sep-2026 | 4.9 | 4.0 | 3.1 | 1.1 |
| 30-sep-2026 | 5.3 | 4.0 | 3.2 | 1.2 |
| 07-oct-2026 | 5.2 | 4.1 | 3.3 | 1.3 |
| 14-oct-2026 | 5.2 | 4.2 | 3.3 | 1.1 |

Como referencia, el máximo mensual de Niño 1+2 en 1997-98 fue +4.47 °C (ERSSTv5, nov-1997) o +3.73 °C (OISST). En sep-2026 el valor mensual OISST ya es **+4.69 °C**.

## 2. IRI / CCSR — ENSO Quick Look y Technical Update (publicado 19-oct-2026)
Fuente: https://iri.columbia.edu/our-expertise/climate/forecasts/enso/current/

- **Niño 3.4 tradicional (OISST):** JAS 2026 +2.46 °C; septiembre +2.84 °C; semana del 14-oct +3.3 °C.
- **Niño 1+2:** más de +5.0 °C durante tres semanas seguidas. IRI lo describe como "the emergence of exceptionally strong coastal El Niño conditions along the South American coast".
- **Plume (27 modelos, 16 dinámicos y 11 estadísticos):**
  - El promedio multimodelo llega a **~+3.5 °C en OND y NDJ 2026**.
  - Todos los modelos prevén "muy fuerte" (≥ +2.0 °C) de OND 2026 a DJF 2026-27.
  - Unos 10 modelos prevén ≥ +3.5 °C.
- **Probabilidad de El Niño** (objetiva IRI): **100%** de OND 2026 a MAM 2027; 92% en AMJ; 60% en MJJ. En JJA 2027 lo más probable es neutral (51%), con El Niño en 37%.
- **IOD:** positivo desde septiembre (DMI +0.51 °C), con pico posible en noviembre.

## 3. Ecuador — CN-ERFEN (INOCAR, INAMHI, IPIAP, SNGR, ESPOL, DGAC, UPSE)

Informes en https://www.inocar.mil.ec/boletin/ERFEN/:

- **ERFEN 007-2026 (28-ago-2026, extraordinario):** https://www.inocar.mil.ec/boletin/ERFEN/erfen_20260828.pdf
  - Confirma los cuatro criterios del Protocolo y declara: "el CN-ERFEN declara oficialmente el evento El Niño en el país".
  - Aclara que la declaratoria "no implica por sí sola el inicio inmediato de lluvias intensas o generalizadas".
  - Los centros internacionales prevén intensidad muy fuerte "durante el último trimestre de 2026 e inicios de 2027, período en el que se espera su mayor desarrollo".
- **ERFEN 08-2026 (4-sep-2026):** https://www.inocar.mil.ec/boletin/ERFEN/erfen_20260904.pdf
  - Cita a la OMM: probabilidad cercana al 100% de que el evento persista hasta febrero de 2027.
  - Pronóstico INAMHI para septiembre en el Litoral: precipitación de normal a sobre lo normal.
- **ERFEN 010-2026 (Santa Cruz, 1-oct-2026):** https://www.inocar.mil.ec/boletin/ERFEN/erfen_20261001.pdf (copia en https://www.teleamazonas.com/uploads/files/2026/10/07/erfen_20261001.pdf)
  - Al 23-sep: Niño 1+2 en +4.7 °C y Niño 3.4 en +3.1 °C.
  - IEFEN = 6, "ACTIVO".
  - Estructura térmica con "destacada similitud" con 1997-98, 2015 y 2023.
  - Guayaquil tuvo "el septiembre más lluvioso de toda la serie disponible desde 1961", por encima de septiembre de 1982 y de 1997.
  - Pronóstico INAMHI para octubre en el Litoral: precipitación **sobre la normal**.
  - Advierte que en la Sierra y la Amazonía pueden darse condiciones normales a deficitarias, con riesgo para los aportes a las hidroeléctricas.
- **ERFEN 011-2026 (22-oct-2026, el más reciente):** https://www.inocar.mil.ec/boletin/ERFEN/erfen_20261022.pdf
  - **Océano:** Niño 1+2 en ~+5.2 °C. El nivel del mar está más de 40 cm sobre lo normal, y más de 50 cm en Esmeraldas.
  - **Lluvias:**
    - Milagro acumuló 195.9 mm al 20-oct, frente a una normal de octubre de 4.2 mm.
    - Guayaquil-DGAC, Milagro, Portoviejo y La Maná tuvieron "su octubre más lluvioso en las series disponibles".
    - Manta, en cambio, quedó bajo lo normal.
  - **Impactos:** la SNGR registró 335 eventos por lluvias en octubre y 6 090 personas impactadas, cifras que superan octubre de 2012-2025. Los desbordamientos subieron de 52 en septiembre a 107 en octubre.
  - **Perspectiva (cita):** "El Niño continúa fortaleciéndose y se aproxima al período previsto de su fase de madurez hacia finales de 2026".
  - **Lluvias en la temporada (cita):** "La posible coincidencia de este proceso [desplazamiento de la ZCIT al sur] con el periodo de mayor intensidad de El Niño aumentaría las condiciones favorables para lluvias frecuentes e intensas en el Litoral".
  - **Persistencia:** la reserva de calor "podría prolongar las condiciones oceánicas cálidas durante varios meses después del máximo del evento".
  - **INAMHI, 22-oct a 5-nov:** más lluvias en el norte e interior del Litoral, con episodios intensos entre el 25 y 28 de octubre y entre el 1 y 3 de noviembre.

**INAMHI (14-sep-2026, vía prensa):** el Litoral entró en una "etapa inicial de transición y acoplamiento atmosférico". Las lluvias de mayor intensidad y frecuencia "se desarrollarán a medida que se acerque noviembre y diciembre y se extenderán durante los primeros meses de 2027".
- Fuente secundaria (aproximado): https://www.vistazo.com/actualidad/2026-09-14-el-nino-ecuador-inamhi-anticipa-lluvias-frecuentes-costa-mayor-intensidad-EA11227232 y https://kchcomunicacion.com/?p=539771

### Pronóstico de lluvias costa dic-2026 a abr-2027: VACÍO
**No encontré un pronóstico estacional cuantitativo oficial de INAMHI** (ni en mm, ni en % de la normal, ni en probabilidades por tercil) para diciembre de 2026 a abril de 2027. Las fuentes ecuatorianas solo dan lo siguiente:
- **Cualitativo:** lluvias sobre lo normal en el Litoral, con la mayor intensidad desde noviembre-diciembre y continuación en los primeros meses de 2027 (INAMHI y ERFEN).
- **Pronósticos mensuales formales:** solo septiembre ("normal a sobre la normal") y octubre ("sobre la normal") en el Litoral.
- **Lo que hay que revisar:** el pronóstico climático de noviembre y siguientes de INAMHI (https://www.inamhi.gob.ec/ , https://servicios.inamhi.gob.ec/pronostico/) y el próximo informe ERFEN, a partir de ~5-nov-2026. La web de INAMHI no mostraba boletines estacionales el 25-oct-2026.

## 4. Perú — ENFEN, Comunicado Oficial N°18-2026 (16-oct-2026; próximo 30-oct-2026)
Fuente: https://enfen.imarpe.gob.pe/download/comunicado-oficial-enfen-n-18-2026/?wpdmdl=2165

Es útil porque Niño 1+2 es la región que comparten Ecuador y Perú.

- **Estado:** "Alerta de El Niño Costero". El titular dice: "EL NIÑO COSTERO SE EXTENDERÍA HASTA EL OTOÑO DE 2027".
- **Niño 1+2:** es más probable que el evento costero "se mantenga con una magnitud de extraordinaria hasta enero de 2027, para luego disminuir a fuerte hasta inicios del otoño de 2027".
- **Niño 3.4:** magnitud "muy fuerte" hasta febrero de 2027.
- **Lluvias en Perú:** sobre lo normal en la costa norte y central para el verano de 2027 (dic-mar).
- **Clasificación:** en la terminología ENFEN es un El Niño **costero de magnitud "extraordinaria"**, la máxima categoría del índice ICEN, y a la vez un El Niño del Pacífico central muy fuerte.

## 5. Impactos en Ecuador hasta la fecha (2026)
Ver `eventos_nino_ecuador.csv`, filas "2026-27 (actual)".

- **SNGR vía prensa (aproximado):** desde la alerta roja hay ~23 167 personas afectadas y 3 fallecidos (corte ~20-oct-2026).
- **ERFEN 010:** 13 303 personas impactadas en septiembre en el Litoral.
- **Daños económicos:** no hay estimación oficial.

## Fuentes secundarias consultadas (contexto, aproximado)
- Primicias (13-ago-2026), sobre similitud con 1997-98 y 2023-24 según ERFEN: https://www.primicias.ec/sociedad/fenomeno-elnino-2026-ecuador-pronostico-similitudes-evento-catastrofico-impacto-moderado-lluvias-calentamiento-oceanico-130104/
- Vistazo (30-ago-2026), sobre la alerta roja: https://www.vistazo.com/actualidad/2026-08-30-el-nino-declarado-oficialmente-ecuador-que-significa-proximos-meses-PI11197448
- El Universo, "El Niño es oficial en Ecuador": https://eluniverso.com/noticias/ecuador/el-nino-es-oficial-en-ecuador-que-dice-inocar-nota/
