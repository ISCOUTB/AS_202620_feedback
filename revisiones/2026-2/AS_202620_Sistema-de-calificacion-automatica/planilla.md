# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Calificación automática |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-10 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4f6f568` · 2026-08-09T13:16:43-05:00 | 7/9 | no aplica | sí |
| 2 | S2 | `d4302f4` (2026-08-16T23:17:26-05:00) | 3/9 | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dd422fb` · 2026-08-23T23:52:23-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `cede35e` (2026-08-30T23:51:34-05:00) | 6/10 | 3.4 | si |
| 5 | CORTE1 | `201acac` (2026-09-06T23:34:17-05:00) | 7/12 | no aplica | si |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | | | no aplica | |
| 7 | Evidencia S7 · Contrato de API y prueba de contrato | | | no aplica | |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | | | no aplica | |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | | | no aplica | |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/adr` versionado como blob vacío, no como directorio | S1 (08-09) | no (S3 resuelto) | Directorio con 0001, 0002 y 0003 |
| Ficha del problema fuera del repositorio («Informe Inicial» de Moodle) | S1 (08-09) | no (resuelto en `dd422fb`) | `docs/Ficha-problema.md` subida el 23-ago 23:52 |
| Solo 1 cuenta contribuyendo al historial | S1 (08-09) | no (S3 resuelto) | 4 cuentas en el historial |
| `docs/aspectos.md` sin enlaces desde las filas a los escenarios | S2 (16-ago) | no (S3 resuelto) | Tabla ADD con enlaces a EC y ADR |
| Restricciones sin categorías organizativas ni legales | S2 (16-ago) | no (S3 resuelto) | Categorías completas en arc42 §2 |
| Esqueleto ejecutable prometido en ADR-0001 y no entregado al cierre | S3 | parcial: entró 2 h después del cierre (`e976c92` 01:58) — no cuenta para S3 | Para S4: el esqueleto debe traer run en verde del pipeline; respetar los cierres |
| Matriz comparativa de estilos contra el árbol de utilidad ausente | S3 | no (resuelto) | §4.1 con filas por EC-01…EC-07 |
| ADR sin hipervínculo desde el escenario motivador EC-04 | S3 | no (resuelto) | EC-04 y EC-05 con enlaces al ADR |
| 2 commits posteriores al cierre (`88294cc` 01:00, `e976c92` 01:58) | S3 (cierre) | registrado | Entregar dentro del cierre de la actividad; lo tardío no califica |
| C4 nivel 2 incompleto en docs/c4/doc-c4.md | S4 | si | Corregido: el equipo demostró (correcciones_feedback.md, hallazgo 2) que el Nivel 2 ya estaba completo en cede35e; aceptado. |
| Fila A-01 de aspectos.md con C2 pendiente | S4 | si | Resuelto para el corte 1: la fila A-01 ahora enlaza C4 Nivel 2 real, ADR 0002+0006, código y pruebas sin huecos. |
| Verificación de CI sin runs | S4 | si | Corregido: 21+ runs en verde confirmados por curl a actions/runs, incluido uno sobre el commit calificado; aceptado (hallazgo 1 de correcciones_feedback.md). |
| Secciones 7 y 8 del arc42 pendientes (declarado) | S4 | si | Fuera del alcance de esta revisión de corte 1 (evidencia S4, no recalificable); queda anotado. |
| Confirmar etiqueta corte-1 | S5 | si | Confirmada: corte-1 -> 201acac, 2026-09-07T04:34:17Z, antes del cierre. |
| Contrastar diagnóstico con la restricción asignada | S5 | si | La restricción de Moodle no llegó al equipo; se trabajó sobre R-06 (deuda declarada) con diagnóstico medido y aceptado. |
| Medir línea base y resultado contra umbral | S5 | si | Resuelto: 100% de pérdida silenciosa medida antes del cambio, 0% después, dentro del umbral de 10s. |
| Evidenciar pipeline en verde | S5 | si | Resuelto: run success sobre 201acacb a las 2026-09-07T04:43:04Z, antes del cierre. |
| Completar trazabilidad de A-04 | S5 | si | No se revisó A-04 en este corte; el reto tocó A-01. Sigue abierto para A-04. |
| Verificar contenido de docs/ia.md | S5 | si | Verificado: entrada 7 (2026-09-06) con 4 rechazos y motivo técnico, referida a este corte. |
| ADR y estructura docs/adr creados después del cierre (commits 9a80cf0 a 201acac, 2026-08-30 en adelante). | S2 | no (resuelto tarde) | — |
| Pipeline CI agregado tras el cierre (.github/workflows/ci.yml solo en HEAD). | S2 | no (resuelto tarde) | — |
| README actualizado con arranque y prueba tras el cierre (commit 02c39d8 2026-08-30T14:05:57-05:00). | S2 | no (resuelto tarde) | — |
| docs/aspectos.md actualizado con A-04 y retiro de tensión T-2 tras el cierre (commit 9469642 2026-08-30T14:11:19-05:00). | S2 | no (resuelto tarde) | — |
| Código y evidencia del aspecto A-01 agregados después del cierre (59e182e y db99e99, 2026-08-30). | S2 | no (resuelto tarde) | — |
| Escenarios de calidad con medida numérica en arc42 sección 10. | S2 | si | |
| Árbol de utilidad priorizado por impacto y riesgo. | S2 | si | |
| Tabla de aspectos navegable hasta código, ADR, pruebas y evidencia. | S2 | si | |
| Clasificación de restricciones en técnicas, organizativas y legales. | S2 | si | |
| 8b0d00b (2026-09-07T14:29:28-05:00) renombra correcciones_feedback.md a correcciones.md: corrige la fila 2 de la ficha S5 después del cierre. | S5 | no (resuelto tarde) | — |
| docs/ia.md sigue ausente en HEAD. | S5 | si | |
| Correcciones trazables en correcciones.md no se pudieron contrastar: no se verificó su contenido ni respuesta a hallazgos S1-S4. | S5 | si | |
| No hay runs_ci citados para respaldar el pipeline en HEAD. | S5 | si | |
| Renombrado de correcciones_feedback.md a correcciones.md en 8b0d00b (2026-09-07T14:29:28-05:00), posterior al cierre | S5 | no (resuelto tarde) | — |
| Verificar contenido de correcciones.md a HEAD | S5 | si | |
| Confirmar run de CI para el hash calificado | S5 | si | |
| PDF en Moodle | S5 | si | |
| Sustentación | S5 | si | |
| Confirmar organización ISCOUTB | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público y con el nombre de la convención |
| Estructura mínima | Cumple | Las seis rutas presentes en `b65626e` |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md`, `0002-procesar-calificacion-de-forma-asincrona.md` |
| ADR aceptados sin reescribir | Cumple | 0001 marcado como reemplazado por 0002, sin reescrituras de contenido |
| `docs/ia.md` al día | No cumple | Actualizado en S3 (`aa14dca`) con aceptado/rechazado/justificación |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 4 cuentas para 4 integrantes |
| Pipeline en verde | No verificado | Sin código ni prueba al cierre; el esqueleto tardío trae prueba, pendiente de run en verde para S4 |
| Etiqueta corte-1 (corte 1) | Cumple | `201acac`, 2026-09-07T04:34:17Z, antes del cierre |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits (a corte-1, `201acac`) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Canas Plata | scp1109 | 35 | — | — | Todo S1-S2, ADR 0003, ficha del problema en S3, reto del corte 1 (commit único) |
| Josue David Ortega De Arco | josueacademico17-source | 16 | — | — | Desde la semana 3 |
| Susana Marcela Rosales Castellar | SusanaRosales | 7 | — | — | Desde S3 |
| Maria Del Mar Restrepo Licona | Mariadelmar-restrepo | 3 | — | — | Desde S3 |

Corrección aceptada (hallazgo 8 de `correcciones_feedback.md`): la tabla anterior daba 27/9/1/3; `git shortlog -sn` sobre `cede35e` y `corte-1` confirma 34-35/16/7/3.

## Preguntas abiertas para la sustentación

- ¿Por qué el esqueleto y el README del stack entraron 1 y 2 horas después del cierre de S3?
- ¿Cuándo entregarán el run en verde del pipeline sobre el esqueleto ya existente?
