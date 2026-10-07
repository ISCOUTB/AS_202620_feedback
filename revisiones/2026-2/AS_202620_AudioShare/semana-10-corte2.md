# Segundo corte S10 · avance preliminar · AudioShare

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_AudioShare](https://github.com/ISCOUTB/AS_202620_AudioShare) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `cb65d13134b220c020d0facaa00d0a779d584245` |
| Base S8 | `e4789d887fe59b2ace65bd1d2680f79758db5b54` |
| Estado revisado | `6a03a9718776420d46ed40f7addc5667206908cd` en `origin/master` (2026-10-04T23:15:57-05:00) |
| S9 congelada | `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 |
| Punta actual / S10 preliminar | `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 |
| Comprobación | 2026-10-06T21:16:50Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `cb65d13134b220c020d0facaa00d0a779d584245`. En el delta S5→HEAD cambian 61 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 se incorporaron contratos OpenAPI/AsyncAPI, cliente Flutter, despliegue, logs y métricas; en S9 la implementación productiva no cambió, pero sí documentación y una prueba. El avance del corte se examina sobre esa evolución completa y no solo S8→S9.

## Escenario operativo asignado

No verificado. Se buscaron asignación/escenario operativo/reto S10 en README, ADR, escenarios y documentos de evidencias. EC-01 (sincronización ≤100 ms) y EC-02 (≤200 ms) son objetivos generales del producto, no prueba de asignación docente; [README.md:226–234](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L226-L234). Hace falta la consigna específica del equipo.

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master identificada en el encabezado, anterior al cierre futuro; la revisión es preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://audioshare.iscoutb.dev/health: HTTP 200, 5.847381 s, 2026-10-06T21:16:50Z; cuerpo JSON status=ok. URL declarada en [README.md:151–159](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L151-L159). Solo accesibilidad/health: flujo principal no probado. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Hay EC-01/EC-02 genéricos, pero no asignación oficial del escenario S10; [README.md:226–234](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L226-L234). |
| Línea base medida y reproducible | No verificado | No hay línea base del reto identificada; el test de constantes no la sustituye; [tests/sync-a01.test.ts:5–18](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/tests/sync-a01.test.ts#L5-L18). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | ADR-0005 es de sincronización y ADR-0004 sigue refiriéndose a Azure, mientras README declara Dokploy; no se acredita respuesta al reto asignado; [docs/adr/0005 Validación-sincronización-inicial.md:17–49](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L17-L49), [README.md:185–193](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L185-L193). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Desde S5 se añadieron Flutter, contratos, despliegue y observabilidad. En S9 no hay cambio productivo; falta identificar cuál de los cambios desde S5 responde al escenario asignado o demostrar por qué no cambiarlo. |
| Resultado contrastado con el umbral | No verificado | EC-01/EC-02 sin resultado real contrastado con umbral; falta conocer el reto S10; [README.md:203–210](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L203-L210). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | Flutter continúa en failure; hay health y logger JSON, pero la métrica solo es proxy de actividad, no mide desfase y falta vínculo con reto asignado; [src/shared/metrics.ts:1–13](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/src/shared/metrics.ts#L1-L13), [src/shared/logger.ts:1–31](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/src/shared/logger.ts#L1-L31). |
| Secretos protegidos | Cumple | No se encontraron secretos reales en el árbol de la punta. Ver alcance del barrido. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | README declara Dokploy pero arc42 §7/ADR-0004 representan Azure y la matriz sigue sin la decisión nueva; [README.md:185–193](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L185-L193), [docs/arc42/src/07_deployment_view.adoc:13–24](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/arc42/src/07_deployment_view.adoc#L13-L24), [docs/aspectos.md:38–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L38-L43). |
| Decisión anterior confirmada o reemplazada con evidencia | No cumple | ADR-0005 complementa decisiones sin confirmación experimental; no hay medición del sistema que confirme o reemplace la anterior; [docs/adr/0005 Validación-sincronización-inicial.md:61–78](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L61-L78). |
| Sustentación del reto sobre el entorno desplegado | No verificado | Se resuelve por el docente en sustentación sobre despliegue y ejecución de pipeline en vivo. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No se localizó evidencia de asignación oficial del escenario; no se sustituye por un escenario genérico. |
| Decisión e implementación | No verificado | Pendiente | No se puede juzgar la respuesta al escenario asignado hasta identificarlo. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Hay evidencia técnica parcial descrita en la matriz; falta vincularla con el escenario asignado y verificar la operación completa. |
| Evolución arquitectónica trazable | No verificado | Pendiente | La coherencia documental se informa en la matriz; falta demostrar la evolución específica exigida por el reto. |
| Sustentación del reto | Pendiente del docente | Pendiente | Sustentación sobre el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

Escala aplicable: 0,00 / 0,60 / 0,80 / 1,00 por criterio. **No se calcula total mientras haya criterios pendientes.** No se usa la fórmula semanal. Cualquier nivel es propuesta al docente; la sustentación queda a su cargo.

## Matriz transversal · punta actual

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público por HTTPS y rama remota master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Presentes README, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md; [docs/aspectos.md:36–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L36-L43). arc42 usa AsciiDoc, desviación de formato frente a Markdown. |
| Estado calificado identificable | Cumple | Hash y fecha completos en el encabezado, elegidos por git log --until sobre origin/master. |
| Nombres de ADR según la convención | No cumple | El nombre [docs/adr/0005 Validación-sincronización-inicial.md:1–7](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L1-L7) contiene espacio y acentos; no pasa NNNN-kebab-case. |
| ADR aceptados no reescritos | No cumple | ADR-0001 ya estaba aceptado en 924d133 y fue modificado en 354f1f5: se verificaron ambas versiones y el diff. El texto actual solo dice complementado, sin preservar la versión aceptada mediante reemplazo; [docs/adr/0001-usar-monolito-modular.md:1–8](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0001-usar-monolito-modular.md#L1-L8). |
| docs/ia.md al día para la semana | No cumple | Hubo cambios de S9, pero el registro específico no separa una salida rechazada con motivo técnico y mantiene Estado «semana 7»; [docs/ia.md:112–112](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L112-L112), [docs/ia.md:363–389](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L363-L389). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Scanner configurado en [sonar-project.properties:1–5](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/sonar-project.properties#L1-L5) y [.github/workflows/ci.yml:18–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/.github/workflows/ci.yml#L18-L23); la organización configurada no es isco-utb. CI success, Flutter failure en el hash. Falta análisis público y Quality Gate atribuibles a esta revisión. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el árbol: coincidencias solo con referencias a secrets de Actions. Barrido histórico completo no concluyó; no se certifica el historial. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas de autor visibles, distribuidas en el historial. No se inventa la correspondencia entre cuentas y los cuatro integrantes; falta mapa verificable para acreditar a todas las personas. Punta actual: 4 firmas y 206 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [Flutter: failure](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748991), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
- [Publicar imagen: success](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748932), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
- [CI: success](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748924), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido del snapshot completo de texto, incluidos docs y ejemplos: las coincidencias fueron referencias a secretos del almacén de Actions, no valores. No hay .env versionado. El recorrido histórico con git log -S no terminó por cancelación del entorno: la fila transversal conserva No verificado.

## Estado global del proyecto (overall)

La punta coincide con S9. Se incorporaron dos ADR y una prueba adicional, pero esta no valida la sincronización real. La aplicación responde al health check actual, lo cual no demuestra flujo de audio ni identidad entre despliegue y commit. La documentación reconoce audio simulado y mediciones pendientes. CI de backend e imagen están en verde; Flutter sigue en rojo. La plataforma declarada cambió a Dokploy sin alinear completamente la vista de despliegue y ADR.

El delta S9 contiene 9 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Sustituir la prueba de constantes por una que invoque la lógica real y falle al introducir un defecto de sincronización; registrar procedimiento y resultado.
- Completar la cadena A-01 hacia ADR-0005, código exacto, prueba y medición reproducible.
- Aportar mediciones de receptores y comparación con umbral, sin presentar un ejemplo sintético como experimento.
- Localizar la consigna oficial S10 y definir línea base, hipótesis, variables y montaje.
- Corregir Flutter CI, evidenciar SonarCloud/Quality Gate del hash y alinear Dokploy con ADR/C4/arc42.
- Hacer específica la auditoría de erosión y la verificación de dependencias; registrar rechazo técnico propio de la entrega.

## Tres preguntas de sustentación

1. ¿Qué ocurriría si un receptor recibe startAt después del instante programado y qué prueba real detectaría el desfase?
2. ¿Qué consumo y persistencia necesita Dokploy y quién asume el costo al salir del recurso académico gratuito?
3. La prueba actual produce 40 ms por construcción: ¿qué cambiarían al medir relojes, red y reproducción física reales?
