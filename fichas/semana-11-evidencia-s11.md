# Evidencia S11 · Fallos parciales y decisión de extracción

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s11` |
| Semana | 11 |
| Corte | Tercer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**Tabla de modos de fallo con su mitigación**, **diseño de idempotencia o saga si aplica**, y
**ADR con la decisión de extraer o no extraer un módulo**, con sus criterios.

El recordatorio de la semana pide actualizar la sección 11 de arc42 con los modos de fallo, y
exige que el ADR de extracción registre la alternativa **no extraer** como opción evaluada, no
como ausencia de decisión.

El análisis se hace sobre la **integración principal del proyecto**: qué pasa si el otro lado no
responde, responde tarde o responde dos veces.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Identifica la integración principal** en el código y comprueba que la tabla de fallos habla
   de esa integración y no de un caso genérico.
   ```bash
   git -C "$DIR" grep -nIE '(httpx|requests\.|fetch\(|axios|HttpClient|RestTemplate|WebClient)' HEAD -- . ':!docs' | head -20
   ```
3. **Tabla de modos de fallo.** Al menos los tres casos de la semana: no responde, responde tarde
   y responde dos veces. Cada uno con su mitigación asignada, no con una intención general.
4. **Contrasta la mitigación con el código.** Si la tabla dice reintentos con espera creciente,
   circuit breaker o timeout, busca dónde está. Una mitigación declarada y no implementada se
   registra como tal, y eso no es incumplimiento de la evidencia si el equipo lo declara pendiente
   con su plan.
   ```bash
   git -C "$DIR" grep -nIE '(retry|backoff|circuit|timeout|deadline|idempoten)' HEAD -- . ':!docs' | head -30
   ```
5. **Idempotencia o saga, si aplica.** Comprueba si el sistema tiene operaciones que puedan
   repetirse. Si las tiene, exige el diseño; si no las tiene, exige que el equipo argumente por
   qué no aplica. Lo que no vale es el silencio.
6. **ADR de extracción.** Con la decisión, sus criterios y la alternativa **no extraer** evaluada
   explícitamente. Un ADR que solo dice que se mantiene el monolito porque no dio tiempo no cumple.
7. **arc42 sección 11.** Los modos de fallo identificados incorporados a riesgos y deuda técnica.
8. **Trazabilidad.** Comprueba que los aspectos afectados por la integración tienen la fila de
   `docs/aspectos.md` al día.

**Qué no hacer aquí:** no exigir que extraigan un servicio, que la decisión razonada de no hacerlo
es válida y a menudo la correcta; no exigir mensajería, que es la semana 12.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Integración principal identificada en el código | rutas donde ocurre la llamada entre componentes | | |
| Tabla de modos de fallo con no responde, responde tarde y responde dos veces | tabla citada | | |
| Mitigación asignada a cada modo de fallo | columna de mitigación de la tabla | | |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | rutas del código con reintentos, timeout o circuit breaker | | |
| Diseño de idempotencia o saga, o argumento de por qué no aplica | apartado de diseño o justificación | | |
| ADR con la decisión de extraer o no extraer, y sus criterios | `docs/adr/NNNN-*.md` | | |
| La alternativa no extraer aparece evaluada, no omitida | apartado de opciones del ADR | | |
| arc42 sección 11 con los modos de fallo | `docs/arc42/11*` | | |
| Filas de aspectos afectadas por la integración, al día | `docs/aspectos.md` | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente.

Deja anotado para el proyecto final, criterio de calidad y resiliencia: qué modos de fallo tienen
prueba y cuáles solo están descritos. El nivel competente exige que los modos de fallo **se
prueben**, no que se enumeren.
