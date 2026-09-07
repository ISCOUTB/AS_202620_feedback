# Semana 5 · Primer corte · ROUTB

> Revisión definitiva post-cierre — 2026-09-07. Reemplaza la revisión manual preliminar del 2026-09-03 (que no vio nada de este trabajo: se hizo después). Cierre: `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Estado calificado | etiqueta `corte-1` → `493efdb4cc54548bd9722406d13677b8d60402f0` (2026-09-06T20:11:13-05:00 = 2026-09-07T01:11:13Z) — anterior al cierre |
| HEAD para el overall | `6f6e40c7adef3abffd1208edc92629e90df6eb36` (2026-09-07T13:23:46-05:00 = 18:23:46Z, **posterior al cierre**) |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log -1 corte-1`; `git log 83b8c5e..corte-1`; lectura de `docs/adr/0003-control-atomico-de-cupos.md`, `docs/aspectos.md`, `docs/ia.md`, `docs/arc42/10_requisitos_de_calidad.md`, `backend/tests/test_cupos.py`, `README.md`; `git shortlog -sne HEAD`; `git grep` (secretos); `GET /repos/.../actions/runs` (una consulta, filtrando por el commit de la etiqueta y por el workflow de SonarCloud); búsqueda de `correcciones.md` en todo el historial (no existe) |
| Revisor | agente de revisión, solo lectura; no se ejecutó código del equipo |
| Alcance externo no disponible | No se localizó un documento que declare una restricción individual asignada por el curso a este equipo; `docs/ia.md` describe el reto como "concurrencia y disponibilidad de cupos", que parece autoidentificado por el equipo a partir del dominio, no una restricción externa impuesta como en otros equipos del lote. Se anota como incertidumbre, no como ausencia. |

## Matriz de la ficha (evaluada sobre `corte-1` = `493efdb`)

| Criterio de evaluación | Estado | Observaciones |
|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Cumple | `493efdb` del 2026-09-07T01:11:13Z, anterior al cierre (05:00:00Z). |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No verificado | No está en el kit ni en el repositorio. |
| Impacto de la restricción localizado en requisitos, C4 y código | Cumple (con reserva) | `docs/aspectos.md` fila 1 liga el aspecto de "gestión de disponibilidad de cupos" a C4, ADR-0001/0003 y al módulo `trips`. La reserva es que no se identificó una restricción individual asignada externamente: el reto parece autoidentificado a partir de un riesgo de concurrencia del propio dominio. |
| Línea base medida y verificable antes del cambio | Cumple | `docs/arc42/10_requisitos_de_calidad.md`: "20 intentos al endpoint de reserva, los 20 terminaron con `404 Not Found`" — línea base real y verificable (el endpoint no existía), aunque no es una cifra de degradación cuantificada sino un estado binario. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Cumple (nivel competente) | `docs/adr/0003-control-atomico-de-cupos.md`: 2 alternativas descartadas con motivo, decisión y consecuencias positivas/negativas. No declara fuerzas como sección aparte ni un criterio de reconsideración o costo de reversión — no alcanza el nivel sobresaliente que sí muestran otros equipos del lote. |
| Cambio implementado y ejecutable de extremo a extremo | Cumple | Módulo `trips` con `POST /trips/`, `GET /trips/{id}`, `POST /trips/{id}/reservations`; README documenta arranque de backend (`uvicorn app.main:app --reload`) y frontend (`flutter run`), sin cambios respecto a S4. |
| Límites declarados conservados tras el cambio | Cumple | `docs/ia.md` (S5) declara explícitamente que se rechazó modificar los diagramas C4 existentes porque el cambio se mantuvo dentro de los límites del contenedor API Backend, la base de datos y el módulo `trips`. |
| Prueba que cubre el cambio, en verde en el pipeline | Cumple | `backend/tests/test_cupos.py::test_reservas_concurrentes_no_sobrevenden_cupos` cubre 20 intentos concurrentes sobre 4 cupos. El run de CI de pruebas sobre el propio commit de la etiqueta (`493efdb4`) terminó en `success` el 2026-09-07T01:11:16Z, antes del cierre. |
| Resultado contrastado con el umbral del escenario y reproducible | Cumple | Tabla en `docs/arc42/10_requisitos_de_calidad.md`: antes (0/20 solicitudes procesadas, `404`) vs. después (20/20 procesadas, 4 reservas exitosas, 0 cupos restantes, p95 = 0,2281 s) contra el umbral declarado (< 3,99 s); procedimiento fijo y reproducible (misma carga, mismos cupos iniciales). |
| Cadena aspecto→requisito→C4→ADR→código→pruebas→evidencia navegable | Cumple | Fila 1 de `docs/aspectos.md` recorrida celda a celda sin huecos. |
| Salida de IA aceptada/corregida/rechazada con motivo técnico | Cumple (débil) | `docs/ia.md` (05/09/2026): "Se rechazó modificar los diagramas existentes del C4, alterar el workflow original del backend CI o incluir detalles técnicos internos..." — hay un rechazo con motivo, pero es más una decisión de alcance que un rechazo técnico de una propuesta de IA concreta; menos sólido que en otros equipos del lote. |
| Sustentación del reto | No verificado | Lo resuelve el docente en la sesión. |

**Recuento: 10 de 12** (2 No verificado — PDF, sustentación —, 0 No cumple).

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Observaciones |
|---|---|---|
| a. Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon sin autenticación de `ISCOUTB/AS_202620_ROUTB` responde el 2026-09-07. |
| b. Estructura mínima presente | Cumple | `docs/arc42/` (12 archivos), `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md`, todo en minúsculas. |
| c. Estado calificado identificable | Cumple | `corte-1` = `493efdb`, anterior al cierre. |
| d. Nombres de ADR según la convención | Cumple | `0001-usar-monolito-modular.md`, `0002-usar-arquitectura-interna-por-capas.md`, `0003-control-atomico-de-cupos.md`. |
| e. ADR aceptados no reescritos | Cumple | Los tres ADR aparecen como archivos nuevos en commits distintos; no se detectaron reescrituras de un ADR previamente aceptado. |
| f. `docs/ia.md` al día para la semana | Cumple | Entrada "Semana 5" fechada 2026-09-05, específica del reto. |
| g. Sin credenciales en el repositorio ni en el historial | Cumple | Las coincidencias de `git grep` son nombres de campo (`password`, `hashed_password`) en esquemas y servicios de autenticación, no secretos reales; sin `.env` versionado. |
| h. Contribución de todos los integrantes | Cumple | `git shortlog -sne HEAD`: MKeinerrr (31+2, dos correos, mismo integrante), diegobrr999-commits (6), juliandmanjarrez-tech (3), junior14700 (2). Los cuatro integrantes tienen commits, aunque muy concentrados en MKeinerrr. |
| Pipeline y análisis estático (nota adicional, no es fila h) | **No cumple en la parte de análisis estático** | Las pruebas (`Backend CI` / `CI ROUTB`) están en verde, incluida la del commit de la etiqueta. Pero el workflow `SonarCloud` aparece en **`failure` en cada una de sus ejecuciones registradas** desde el 2026-09-05 hasta el 2026-09-06T19:29:31Z (última vista), sin un run en verde ni asociado al commit de la etiqueta. |

## Estado global del proyecto (overall · HEAD `6f6e40c7`, posterior al cierre)

- HEAD tiene 3 commits más que la etiqueta, todos del 07/09 después del cierre (`"Evaluación de retroalimentación de IA"` y dos más), con runs de CI en verde a las 18:2x. No se revisó su contenido en detalle porque no puede contar para esta entrega; se deja anotado que el equipo siguió trabajando el mismo día del cierre, después de la hora límite.
- El pipeline de pruebas es sólido y consistente en verde desde antes del cierre. El pipeline de SonarCloud nunca llegó a estar en verde en las ejecuciones consultadas — es un pendiente real, no solo de forma.
- No se localizó una restricción individual asignada al equipo por el curso; el reto de concurrencia de cupos parece una elección razonable del propio equipo a partir de un riesgo real del dominio (sobreventa de cupos), pero no se pudo confirmar que corresponda a la restricción que se le asignó específicamente a ROUTB.
- Sin `correcciones.md` en ningún punto del historial: no hay objeciones del equipo a la revisión preliminar que adjudicar en este lote.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia |
|---|---:|---:|---|
| Diagnóstico del reto | competente | 0,80 | Localiza el impacto en C4/ADR/código con línea base verificable (endpoints inexistentes, 404 en los 20 intentos), pero no se confirmó que responda a una restricción individual asignada, y no distingue explícitamente síntomas de causas más allá de "condición de carrera". |
| Alternativas y decisión | competente | 0,80 | ADR-0003 con 2 alternativas, decisión y consecuencias ligadas al escenario, pero sin criterio de reconsideración ni costo de reversión declarados. |
| Aplicación sobre el corte vertical | competente | 0,80 | Funciona de extremo a extremo, arranque reproducible, límites conservados; el manejo de conflictos concurrentes es correcto pero se documenta como corrección funcional, no como una degradación controlada explícitamente diseñada y probada como tal. |
| Pruebas, medición y trazabilidad | competente | 0,80 | Cadena navegable y contraste con umbral reproducible; la salida de IA rechazada es débil (una decisión de alcance, no un rechazo técnico concreto) y el análisis estático (SonarCloud) nunca llegó a estar en verde. |
| Sustentación del reto | lo fija el docente | pendiente | Requiere sesión. |
| **Subtotal técnico** | | **3,20 / 4,00** | Propuesta; no es la nota total sobre 5,00. |

## No verificado

- Restricción individual asignada al equipo (no se localizó un documento que la declare; el reto parece autoidentificado).
- PDF de dos páginas de Moodle.
- Sustentación (la fija el docente en sesión).

## Hallazgos

- El reto de concurrencia de cupos está bien resuelto técnicamente (control atómico, prueba de 20 intentos concurrentes, medición antes/después contra un umbral), pero el ADR no alcanza el nivel de rigor de otros equipos del lote (sin criterio de reconsideración ni costo de reversión).
- El pipeline de SonarCloud está consistentemente en rojo desde el 05/09 hasta la última ejecución vista; las pruebas funcionales sí están en verde, incluida la del commit de la etiqueta.
- No se pudo confirmar que el reto responda a una restricción individual asignada por el curso, a diferencia de otros equipos del lote que sí la declaran explícitamente.
- HEAD tiene actividad posterior al cierre que no se evaluó por no ser parte de la entrega.
- Sin `correcciones.md`: no hay objeciones del equipo a la revisión preliminar que adjudicar.

## Preguntas para la sustentación

- ¿Cuál fue exactamente la restricción individual que el curso les asignó, y cómo se relaciona con el control de concurrencia de cupos que implementaron?
- ¿Por qué el análisis de SonarCloud nunca llegó a estar en verde? ¿Qué hallazgos quedan sin resolver?
- ¿Qué dato los haría reconsiderar el control atómico actual (por ejemplo, frente a una base de datos distribuida) y qué costo tendría revertirlo?
