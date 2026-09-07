# Semana 5 · Primer corte · Recobra

> Revisión definitiva post-cierre — 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03 (que no vio nada de este trabajo: se hizo después). Cierre: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado calificado | etiqueta `corte-1` → `f7c1a6c7c4371f1e9df38ca268895544cca43c17` (2026-09-07T09:59:41-05:00 = **14:59:41Z, posterior al cierre**) |
| Último commit ≤ cierre (referencia) | `6ee5b66adb06705d59b302a4d56e535b0fb086d0` (2026-09-05T20:26:56-05:00 = 2026-09-06T01:26:56Z) |
| HEAD para el overall | igual al estado calificado; no hay commits posteriores a la etiqueta |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log -1 corte-1`; `git log 2268b33..corte-1`; `git diff --stat 6ee5b66 f7c1a6c`; lectura de `docs/adr/0003-reto-corte1-stack-obligatorio.md`, `docs/medicion-corte1.md`, `docs/aspectos.md`, `docs/ia.md`, `test/publicaciones-degradacion.e2e-spec.ts`; `git log --follow` sobre ADR-0001; `git shortlog -sne HEAD`; `git grep` (secretos) + `git show 905f546:node_modules/debug/.coveralls.yml`; extracción de texto de `docs/entrega-corte1-moodle.pdf` (2 páginas) con `pypdf`; una consulta a `GET /repos/.../actions/runs` |
| Revisor | agente de revisión, solo lectura; no se ejecutó código del equipo |
| Alcance externo no disponible | Ninguno: la restricción quedó localizada por el propio equipo — **"stack obligatorio del curso: backend NestJS o FastAPI; frontend Flutter o NextJS"** (`docs/adr/0003-reto-corte1-stack-obligatorio.md`) |

## Nota sobre la etiqueta

`corte-1` apunta a un commit del **7 de septiembre a las 09:59:41 hora Colombia (14:59:41 UTC)**, casi 10 horas después del cierre (`05:00:00Z`). El equipo siguió moviendo la etiqueta hacia adelante mientras seguía trabajando (`25525ae` → `6ee5b66` → `f7c1a6c`), y el último movimiento cruzó el cierre. Por la regla del protocolo para etiquetas posteriores al cierre, se revisa igual el contenido de la etiqueta para la matriz de la ficha, pero la fila 1 de esa matriz y la fila de versionado de la matriz transversal quedan en **No cumple**. El commit `6ee5b66`, anterior al cierre, ya contenía casi todo el trabajo sustantivo del reto (ADR-0003, migración a NestJS/Flutter, medición reproducible); lo único añadido después del cierre (`f7c1a6c`) fue enlazar el ADR a sus commits, actualizar 2 líneas de `docs/aspectos.md` y añadir la prueba de degradación — ver detalle en **overall**.

## Matriz de la ficha (evaluada sobre `corte-1` = `f7c1a6c`)

| Criterio de evaluación | Estado | Observaciones |
|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | No cumple | `f7c1a6c` es posterior al cierre (14:59:41Z vs. cierre 05:00:00Z el mismo día). |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Cumple | `docs/entrega-corte1-moodle.pdf` está en el propio repositorio: 2 páginas, con diagnóstico, alternativas/decisión, línea base/resultado/contraste con umbral y enlaces de trazabilidad. Nota: la página 2 cita la latencia previa como "8-15 ms", una cifra que `docs/medicion-corte1.md` corrige explícitamente a `p95 = 0.54–1.00 ms` — el PDF no se regeneró tras esa corrección. |
| Impacto de la restricción localizado en requisitos, C4 y código | Cumple | ADR-0003 §"Diagnóstico del impacto" localiza el impacto por capa (requisitos/escenarios S4a-S5, C4 contenedor API, código del adaptador HTTP y composition root), con síntoma, causa raíz y supuesto explícito sobre cuál es la restricción asignada. |
| Línea base medida y verificable antes del cambio | Cumple | `docs/medicion-corte1.md`: p95=0.54-1.00 ms con procedimiento (`measure-post.js`, N=50, 3 corridas) sobre el commit de línea base `905f546`; el propio documento corrige una estimación anterior sin medir ("~8-15 ms"), lo cual es evidencia de rigor, no de error oculto. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Cumple | `docs/adr/0003-reto-corte1-stack-obligatorio.md`: 3 alternativas con ventajas/desventajas, decisión, consecuencias positivas/negativas, criterio de reconsideración explícito y costo de reversión declarado ("medio", con pasos concretos) — nivel sobresaliente de la rúbrica. |
| Cambio implementado y ejecutable de extremo a extremo | Cumple | Commit de integración `3a82ca6`; README documenta arranque (`npm install && npm run start`, cliente `flutter run`) y pruebas (`npm test`, `npm run test:e2e`, `flutter test`). |
| Límites declarados conservados tras el cambio | Cumple | El ADR declara que el dominio y los casos de uso no cambian, solo el adaptador HTTP; `docs/c4/README.md` refleja el contenedor API como NestJS y el cliente Flutter, coherente con el código. |
| Prueba que cubre el cambio, en verde en el pipeline | Cumple | `test/publicaciones-degradacion.e2e-spec.ts` cubre la degradación controlada del puerto de persistencia. El run de CI sobre `6ee5b66` (anterior al cierre) terminó en `success` el 2026-09-06T01:27:50Z; el run sobre la propia etiqueta `f7c1a6c` (posterior al cierre) también fue `success`. |
| Resultado contrastado con el umbral del escenario y reproducible | Cumple | Tabla antes/después en `docs/medicion-corte1.md` contra el umbral de S5 (no reescribir el dominio, no romper pruebas) y un objetivo local de 100 ms; procedimiento de reproducción documentado paso a paso. |
| Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable | Cumple | Filas A1 y A2 de `docs/aspectos.md` recorridas celda a celda sin huecos; A3 declara explícitamente "pendiente de implementación en corte posterior" (trazabilidad honesta, no oculta). |
| Salida de IA aceptada/corregida/rechazada con motivo técnico | Cumple | `docs/ia.md`, entrada del 2026-09-05: **"Rechazado: reescribir el dominio en Python/FastAPI y pasar el cliente a NextJS (mayor riesgo de aprendizaje sin beneficio para S5)"**, y una segunda entrada rechazando "desactivar Sonar o excluir `mobile/` del análisis para pasar en verde sin corregir las causas". Ambas con motivo técnico y fecha dentro del corte. |
| Sustentación del reto | No verificado | Lo resuelve el docente en la sesión. |

**Recuento: 10 de 12** (1 No cumple — versionado —, 1 No verificado — sustentación —).

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Observaciones |
|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon sin autenticación de `ISCOUTB/AS_202620_Recobra` responde el 2026-09-07. |
| b. Estructura mínima presente | Cumple (con desviación) | `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md` presentes; persiste `docs/arc42.md` como archivo suelto además de `docs/arc42/04-estrategia-solucion.md` — desviación de estructura, no ausencia. |
| c. Estado calificado identificable | No cumple | La etiqueta existe pero es posterior al cierre; ver nota arriba. |
| d. Nombres de ADR según la convención | Cumple | `0001-estilo-arquitectonico.md`, `0002-arquitectura-y-stack.md`, `0003-reto-corte1-stack-obligatorio.md`, los tres en kebab-case con la decisión en el título. |
| e. ADR aceptados no reescritos | Cumple | ADR-0001 quedó marcado explícitamente "Reemplazada por ADR-0002 - 2026-09-05" en vez de editarse o borrarse (`git log --follow` muestra el archivo intacto desde `cb5c579`, con una nota de estado añadida, no una reescritura de su contenido decisorio). |
| f. `docs/ia.md` al día para la semana | Cumple | Entradas del 2026-09-05 específicas del reto, con aceptado/corregido/rechazado y motivo. |
| g. Sin credenciales en el repositorio ni en el historial | **No cumple** | `node_modules/` ya no está en HEAD, pero el token de Coveralls que contenía (`repo_token: SIAeZjKYlHK74rbcFvNHMUzjRiMpflxve`) sigue siendo recuperable en el historial público, en el commit `905f546` (`git show 905f546:node_modules/debug/.coveralls.yml`). El propio equipo lo reconoce en `docs/checklist-entrega-manual.md:27-29` ("Si ese token era real de alguna cuenta, rótenlo en Coveralls") pero no confirma haberlo rotado ni haber limpiado el historial. Por CONTRATO §9, un repo público con una credencial en el historial es un incidente, no un descuido de forma, y sigue siéndolo mientras el token no se rote. |
| h. Contribución de todos los integrantes | Cumple (con reserva) | `git shortlog -sne HEAD`: Cconde31 (26, incluye la identidad `Steamlinker` ya consolidada por `.mailmap`), vylrir/Verónica Ubarne (9), MiguelJacome (7), Fernando Isacc Conde Herrera (1). Los cuatro integrantes tienen commits, pero la contribución de Fernando sigue siendo mínima (un solo commit en todo el semestre). |

## Estado global del proyecto (overall)

HEAD coincide con `corte-1`. El grueso del reto (migración a NestJS/Flutter, ADR-0003, medición reproducible) ya estaba en `6ee5b66`, **antes** del cierre; después del cierre el equipo solo añadió la prueba de degradación controlada, enlazó el ADR a sus commits y ajustó dos líneas de `docs/aspectos.md`. Es una diferencia relevante para la sustentación: la sustancia del reto se entregó a tiempo, pero la etiqueta que formalmente delimita "lo entregado" se movió después del cierre, lo cual no puede darse por válido según la ficha. Persisten dos pendientes de higiene: el token de Coveralls sigue en el historial sin rotar, y `docs/arc42.md` (archivo suelto) convive con `docs/arc42/04-estrategia-solucion.md`.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia |
|---|---:|---:|---|
| Diagnóstico del reto | sobresaliente | 1,00 | Distingue síntoma (stack fuera del espacio permitido) de causa raíz (decisión de ADR-0001 tomada antes de que existiera la restricción), declara el supuesto sobre cuál es la restricción asignada, y prioriza el riesgo (backend antes que cliente). |
| Alternativas y decisión | sobresaliente | 1,00 | ADR-0003 con 3 alternativas, fuerzas, decisión, consecuencias, criterio de reconsideración cuantificable y costo de reversión explícito. |
| Aplicación sobre el corte vertical | sobresaliente | 1,00 | Cambio de extremo a extremo, arranque reproducible, límites C4 conservados, y degradación controlada explícita ante un fallo del adaptador de persistencia (prueba dedicada). |
| Pruebas, medición y trazabilidad | sobresaliente | 1,00 | Cadena `docs/aspectos.md` sin huecos en A1/A2, medición reproducible con script propio, autocorrección de una cifra no medida, y entrada de IA con dos rechazos justificados técnicamente. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **4,00 / 4,00** | Propuesta; no sustituye la nota total sobre 5,00 ni compensa el criterio 1 (versionado), que la ficha evalúa aparte. |

**Advertencia para el docente:** el subtotal técnico refleja la calidad del trabajo, no la puntualidad de la entrega. La etiqueta `corte-1` es posterior al cierre por casi 10 horas; corresponde al docente decidir si eso amerita una penalización por entrega tardía, independiente de esta rúbrica de contenido.

## No verificado

- Sustentación (la fija el docente en sesión).
- Rotación efectiva del token de Coveralls expuesto en el historial (el equipo lo reconoce pero no confirma haberlo hecho).

## Hallazgos

- La etiqueta `corte-1` se movió después del cierre; el trabajo sustantivo del reto ya estaba completo antes, pero formalmente la entrega llegó tarde.
- Token de Coveralls sigue siendo recuperable en el historial público (`905f546:node_modules/debug/.coveralls.yml`); el equipo lo documentó pero no confirmó la rotación.
- Trabajo del reto (ADR-0003, migración de stack, medición, prueba de degradación, PDF) es de calidad sobresaliente y honesto en sus propias limitaciones (ASP-A3 declarado pendiente, cifra de latencia corregida).
- Fernando Isacc Conde Herrera sigue con un solo commit en todo el semestre.
- Sin `correcciones.md`: no hay objeciones del equipo a la revisión preliminar que adjudicar en este lote.

## Preguntas para la sustentación

- ¿Por qué la etiqueta se movió después del cierre pese a que el trabajo sustantivo ya estaba en `6ee5b66`, antes del cierre?
- ¿Rotaron el token de Coveralls? Muestren la cuenta y el token nuevo, o confirmen que el proyecto de Coveralls fue dado de baja.
- ¿Cómo va a contribuir Fernando de forma sustantiva en los próximos cortes?
