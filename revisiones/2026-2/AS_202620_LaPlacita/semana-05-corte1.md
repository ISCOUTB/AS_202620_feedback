# Semana 05 · Primer corte · LaPlacita

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03 (sobre `812d227`, previa a la respuesta al reto), hecha antes del cierre `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Estado revisado | etiqueta `corte-1` → `50b92f8558f2f57d01aeee14dfe202c9e076e74f` · 2026-09-06T17:45:05-05:00 (= 22:45:05Z, anterior al cierre) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log`; `git checkout corte-1`; `git show`/`git diff` sobre commits del reto; `git grep` de secretos; `curl` a `actions/runs?per_page=8` (1 llamada) |
| Restricción asignada | **RES-05 — Aislamiento estricto por establecimiento** (`tiendaId` obligatorio; 0 accesos cruzados entre tiendas), declarada por el propio equipo en `docs/adr/0004-aislamiento-por-establecimiento.md` |

## Resumen

Este es, de los cinco equipos de este lote, el que sí construyó una respuesta completa y verificable al reto de Corte 1: diagnóstico con línea base medida, ADR con alternativas y costo de reversión, cambio de código real en los cinco módulos de dominio, prueba nueva y script de medición reproducible, todo con la etiqueta `corte-1` puesta antes del cierre y el pipeline en verde en ese commit.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` → `corte-1` → `50b92f8` (2026-09-06T22:45:05Z), anterior al cierre | Cumple | — |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay ruta en el repo | No verificado | Adjunto de Moodle no accesible desde el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/adr/0004-...md` liga RF-02→A-02→ESC-02; `docs/aspectos.md` fila A-02; código en `src/modules/{catalogo,pedidos,pagos,entrega,notificaciones}/index.js` con `tiendaId` obligatorio | Cumple | Localización completa y consistente entre documentos y código. |
| Línea base medida y verificable antes del cambio | ADR-0004 §Contexto: sobre `812d227`, **2/2 accesos cruzados logrados**; verificado directamente: `git show 812d227:src/modules/pedidos/index.js` muestra `obtenerPedido(pedidoId)` y `cambiarEstado(pedidoId, nuevoEstado)` **sin parámetro `tiendaId`** | Cumple | Línea base con cifra y verificable en el propio historial de git, no solo afirmada. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/0004-aislamiento-por-establecimiento.md`: 3 alternativas (A/B/C) con ventajas/desventajas y motivo de descarte, decisión B, consecuencias positivas/negativas, **criterio de revisión** ("si una tienda concentra >40% del tráfico") y **costo de reversión** explícito | Cumple | Nivel sobresaliente: declara qué dato haría revisar la decisión y su costo de reversión, tal como pide el ancla de la rúbrica. |
| Cambio implementado y ejecutable de extremo a extremo | Confirmado en código: `pedidosPorTienda`, `obtenerProducto(productoId, tiendaId)`, `validarPin(pedidoId, tiendaId, pin)`; `node src/corte-vertical.js` sigue el flujo catálogo→pedidos→pagos→entrega→notificaciones | Cumple | Cambio real en los 5 módulos de dominio, no solo documentación. |
| Límites declarados conservados tras el cambio | ADR-0004 y `docs/c4/contenedores.md` declaran que no se añaden ni retiran contenedores; el cambio es interno al monolito | Cumple | Los límites del C4 (backend único, módulos internos) se mantienen. |
| Prueba que cubre el cambio, en verde en el pipeline | Run sobre `50b92f8` (la etiqueta), éxito, 2026-09-06T22:45:12Z; `tests/aislamiento.test.js` (4 pruebas) corre dentro de `npm test` en CI | Cumple | El commit del cambio (`95ec841`) falló CI por configuración de SonarCloud, pero los dos commits siguientes lo arreglaron y la etiqueta `corte-1` en sí está en verde. |
| Resultado contrastado con el umbral del escenario y reproducible | `scripts/medir-aislamiento.js`: 100 ciclos × 3 accesos cruzados = 300 intentos, **0 logrados**, `exit 0`; script real y ejecutable, con procedimiento documentado en el propio archivo | Cumple | Medición reproducible con herramienta (`node scripts/medir-aislamiento.js`), carga (300 intentos) y procedimiento explícitos. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` fila A-02: RF-02→ESC-02→C4→ADR-0001/ADR-0004→código→`tests/aislamiento.test.js`→evidencia (0/300, línea base 2/2) | Cumple | Cadena completa y verificada celda a celda; ninguna lleva a un hueco. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md`, entrada 06/09/2026 ("Big Pickle / Ollama"): describe extensamente qué se implementó y aceptó para el reto; la columna "Validación" queda como "Pendiente de revisión del equipo" en vez de confirmar el resultado final | Cumple (con reserva) | Es la entrada más débil del conjunto: no registra explícitamente algo rechazado o corregido de esta semana (sí lo hace en semanas anteriores, p. ej. 23/08). Se sugiere al equipo cerrar esta entrada con el resultado real de la verificación. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_LaPlacita` sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r --name-only corte-1` devuelve README.md, docs/adr/, docs/arc42/, docs/aspectos.md, docs/c4/, docs/ia.md | Cumple | arc42 en archivo único `arc42-template-EN.md` (desviación de forma, no ausencia). |
| Estado calificado identificable | Etiqueta `corte-1` → `50b92f8`, anterior al cierre | Cumple | — |
| Nombres de ADR según la convención | `0001-adopcion-monolito-modular.md`, `0002-ratificacion-monolito-modular.md`, `0003-despliegue-railway-docker-sonarcloud.md`, `0004-aislamiento-por-establecimiento.md` | Cumple | — |
| ADR aceptados no reescritos | ADR-0001 tenía estado "propuesto" hasta el commit `95ec841`, que lo cambia a "aceptado (ratificado por ADR-0002)" y completa los campos que decían "Pendiente"; no se reescribe un ADR ya aceptado, se cierra uno que seguía propuesto | Cumple | El estado del archivo, no solo el de ADR-0002, decía "propuesto"; completar sus campos pendientes no es una reescritura post-aceptación. |
| `docs/ia.md` al día para la semana | Entrada del 06/09/2026 referida explícitamente al Reto Corte 1 (RES-05) | Cumple | Ver reserva anotada en la matriz de la ficha (columna Validación incompleta). |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de secretos sin coincidencias (exit 1); sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne corte-1`: Jorge Castillo 58, Samuel Jiménez 22, Miguel Isaza (2 identidades) 23, Mateo Buendía (2 identidades) 10 | Cumple | Los 4 integrantes tienen commits en el historial. |

## Estado global del proyecto (overall · HEAD)

- **HEAD** = etiqueta `corte-1` = `50b92f8558f2f57d01aeee14dfe202c9e076e74f`; no hay commits posteriores al cierre.
- CI en verde en el commit etiquetado.
- SonarCloud: `sonar-project.properties` y el paso en `ci.yml` existen, pero el análisis en vivo depende de un `SONAR_TOKEN` real que el propio equipo señala como pendiente de activar (correciones.md).
- C4 de contenedores marca Redis/PostgreSQL/Portal como "planeado (Corte 2)", coherente con lo que el código implementa hoy (memoria, monolito Next.js).

## Nivel de rúbrica sugerido (propuesta al docente, NO nota aplicada)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Sobresaliente | 1,00 | Distingue síntoma/causa/riesgo, con línea base medida y verificable en el propio historial de git (no solo afirmada), y prioriza el riesgo arquitectónico sobre el "uso correcto" como criterio de descarte de alternativas. |
| Alternativas y decisión | Sobresaliente | 1,00 | ADR-0004 declara explícitamente qué dato revisaría la decisión (40% de tráfico concentrado) y el costo de reversión (bajo en memoria, alto si ya hay servicios separados). |
| Aplicación sobre el corte vertical | Competente | 0,80 | Funciona de extremo a extremo, arranca reproducible (`npm install && npm run dev`) y conserva los límites del C4; no se observó degradación controlada explícita ante condición adversa más allá de los `throws` de aislamiento. |
| Pruebas, medición y trazabilidad | Sobresaliente | 1,00 | Cadena navegable, contraste con umbral, medición reproducible con herramienta/carga/procedimiento documentados; la única reserva es la entrada de IA sin cierre explícito de validación. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico** | | **3,80 / 4,00** | Propuesta al docente; la nota final se fija en Moodle. |

## Recuento

10 de 12 criterios Cumple (todo salvo PDF y sustentación, ambos No verificado).

## No verificado

- PDF de dos páginas en Moodle.
- Sustentación del equipo.

## Hallazgos

- Respuesta completa y verificable al reto RES-05: línea base medida, ADR sobresaliente, cambio de código real en 5 módulos, prueba y medición reproducibles.
- La entrada de `docs/ia.md` del Corte 1 no cierra con el resultado final de validación (queda "Pendiente de revisión del equipo"); cerrarla con el resultado real de las pruebas.
- SonarCloud configurado pero no activado en vivo (falta `SONAR_TOKEN`).
- El commit que implementó el reto (`95ec841`) rompió el CI por un problema de configuración de SonarCloud, corregido en dos commits inmediatos; la etiqueta final sí quedó en verde.
- arc42 en archivo único en vez de secciones 1-12 separadas.

## Correcciones del equipo

El equipo mantiene `correciones.md` (nombre con una errata, sin la segunda "c") en la raíz del repositorio, actualizado semana a semana, incluyendo una sección específica de Corte 1 que enumera lo que consideran resuelto frente a los hallazgos previos. Se verificó cada punto de esa sección contra el estado real del repositorio en `corte-1`, no contra el testimonio del equipo.

| Corrección | Adjudicación | Justificación |
|---|---|---|
| "Etiqueta `corte-1` con CI en verde" — pendiente al momento de escribir el documento, a crear antes del cierre | Aceptada | Verificado: la etiqueta existe (`50b92f8`), es anterior al cierre y el run de CI sobre ese commit es exitoso. |
| "Restricción RES-05 declarada y diagnosticada con línea base 2/2" | Aceptada | Verificado directamente en `git show 812d227:src/modules/pedidos/index.js`: las funciones no recibían `tiendaId`, consistente con la cifra de línea base declarada. |
| "ADR-0004 con alternativas A/B/C, decisión B y trazabilidad" | Aceptada | Verificado: el archivo existe, tiene alternativas, fuerzas, decisión, consecuencias, gobernanza y trazabilidad. |
| "Implementación con `tiendaId` obligatorio en los 5 módulos y prueba nueva en CI" | Aceptada | Verificado en `src/modules/{catalogo,pedidos,pagos,entrega,notificaciones}/index.js` y en `tests/aislamiento.test.js`, incluido en el run verde de la etiqueta. |
| "Medición reproducible: línea base 2/2 → post-cambio 0/300" | Aceptada | Verificado: `scripts/medir-aislamiento.js` existe, es ejecutable, documenta herramienta/carga/procedimiento y su lógica corresponde a lo declarado. |
| "ADR-0001 marcado 'aceptado (ratificado por ADR-0002)' con trazabilidad de commits reales" | Aceptada | Verificado en el diff del commit `95ec841`: el estado cambia de "propuesto" a "aceptado", y los campos de implementación/pruebas dejan de decir "Pendiente". No es una reescritura de un ADR ya aceptado, porque su propio campo "Estado" seguía en "propuesto" hasta ese commit. |
| "`docs/ia.md` con entrada del Corte 1" | Aceptada parcialmente | La entrada existe y es sustanciosa, pero su columna "Validación" no cierra con un resultado final (queda "pendiente de revisión"), a diferencia de otras entradas del mismo archivo que sí registran un rechazo con motivo técnico. Se recomienda al equipo completarla, aunque no invalida el cumplimiento del criterio 11. |
| "PDF pendiente del equipo, se sube a Moodle sin commitear" | Aceptada (no es un hallazgo, es correcto) | Consistente con la ficha: el PDF no se versiona en el repositorio. |

## Preguntas para la sustentación

1. ¿Por qué el commit que implementó RES-05 rompió el CI por SonarCloud, y qué le faltó a la configuración inicial?
2. ¿Qué pasaría si una tienda concentrara más del 40% del tráfico, como menciona el ADR-0004 como criterio de revisión? ¿Ya tienen un plan concreto para ese escenario?
3. ¿Cuál fue el resultado final de las pruebas y la medición que dejaron pendiente de "revisión del equipo" en la entrada de `docs/ia.md` del 06/09?
