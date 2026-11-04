# Nueve errores de método que encontré en mi propia investigación

Durante meses diseñé un sistema para invertir en Bitcoin y altcoins por ciclos. Tenía documentos, parámetros congelados y
resultados que parecían sólidos. Después lo audité desde cero, y encontré nueve errores de método. Ninguno era un error de
cálculo: eran errores de diseño, de los que no se ven mirando los números.

Los dejo escritos porque **el patrón importa más que las cifras.** Si investigas tus propias estrategias, es probable que
cometas alguno.

## 1. Probar solo con supervivientes

Mis pruebas de cartera usaban 24 monedas elegidas a mano. Las 24 siguen cotizando hoy. En el ciclo 2022-2024 había en
realidad 364 monedas elegibles, y el 54 % ya no existe.

**Lección:** pregunta qué podías comprar en esa fecha, no qué existe hoy.

## 2. Confundir el borde de la búsqueda con el óptimo

Optimicé el peso de Bitcoin en una rejilla de valores. El mejor quedó en el extremo. Al ampliar la rejilla, el óptimo se
movió al nuevo extremo.

**Lección:** un máximo en el borde de la rejilla no es un máximo; es el final de la búsqueda.

## 3. Leer «no había dato» como «el filtro protegió»

En una prueba, el sistema no invirtió nada en 2018-2020 y parecía que su filtro de entrada lo había protegido. En
realidad, el indicador que yo había modelado **todavía no existía** en esas fechas.

**Lección:** antes de celebrar que una regla «no entró», comprueba que tenía con qué decidir.

## 4. Vender en el techo… sabiendo cuál era el techo

La salida histórica del sistema empezaba a vender exactamente en los máximos de cada ciclo: fechas que solo se conocen
después. Lo curioso es que **saber el techo empeoraba el resultado** (rendía entre 0,775 y 0,944 veces lo que rendía sin
esa ventaja), porque la regla vendía muy poco al principio y casi todo cuando el precio ya se había desplomado.

**Lección:** busca fechas del futuro escondidas en los parámetros, no solo en el código.

## 5. Modelar la regla equivocada

En mi primera reconstrucción del filtro de entrada usé una media de 200 semanas. La regla real usaba otra combinación de
indicadores. Con la equivocada, concluí que solo se podía evaluar un ciclo; con la correcta, se podían evaluar los tres.

**Lección:** cuando reconstruyes un sistema, ve al código congelado, no a tu memoria de cómo funcionaba.

## 6. Un «comprar y mantener» que compraba en el suelo

El punto de comparación pasivo empezaba en fechas elegidas a posteriori: **cinco de las seis fechas de inicio eran
suelos identificados después**. La peor, el suelo del desplome de marzo de 2020, rinde casi un +1.000 % a un año.

Cuando repetí la comparación con 63 fechas de inicio mensuales sin elegir, la conclusión se invirtió.

**Lección:** el punto de comparación también puede hacer trampa.

## 7. Un resultado nulo sobre un diseño contaminado

Un componente de gestión de riesgo no parecía aportar nada cuando los ciclos empezaban en suelos. Con fechas de inicio
arbitrarias, aportaba en las nueve combinaciones probadas. Los datos eran los mismos; cambió desde dónde se miraba.

**Lección:** un «no funciona» obtenido con un diseño defectuoso no es un «no funciona». Hay que rehacerlo antes de
descartarlo.

## 8. Explicar antes de medir

Atribuí la caída de una estrategia a sus filtros de correlación. Cuando los quité uno a uno, esos filtros resultaron
**exactamente inertes**: el resultado no cambiaba nada. La culpa era de otra pieza.

**Lección:** una explicación plausible no es una atribución. Solo quitar las piezas una a una (la ablación) atribuye.

## 9. Una regla que «ganaba» porque evitaba otra regla mía

La misma regla de riesgo del punto 7 parecía sumar un +20 % de rentabilidad. Al desactivar la salida de emergencia del
propio sistema, su efecto pasaba a **−2,3 %**. No creaba valor: evitaba que saltara otra regla mía que, una vez disparada,
dejaba la cartera en efectivo para siempre (y saltaba en un tercio de las ventanas de tres años de la historia de
Bitcoin).

**Lección:** cuando una regla mejora mucho el resultado, mira si no está tapando un defecto de otra.

## Qué cambió después

Estos errores no eran exóticos. Tienen algo en común: **en todos, una propiedad de mi forma de probar se leyó como una
propiedad del mercado.** Desde entonces:

- pruebo con universos tal como existían en cada fecha;
- escribo las reglas y el criterio de éxito antes de mirar el resultado;
- comparo siempre con un punto de partida sin elegir;
- y separo lo documentado de lo validado. Que algo esté escrito en mis documentos no significa que esté demostrado.

*Héctor Sandoval · BICAPITAL Research*

---

*Contenido educativo y de investigación. No es asesoría de inversión ni una recomendación personalizada. Auditoría de una
investigación propia sobre datos históricos de Bitcoin y altcoins. El autor invierte capital propio en criptomonedas.*
