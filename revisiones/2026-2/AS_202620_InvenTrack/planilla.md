# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo InvenTrack. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | InvenTrack |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Integrantes y su usuario de GitHub | Javier Alejandro Carta Lacharme · Esteban Javier Peluffo Marquez · Felix Andres Taborda Jimenez · Jose Gabriel Vargas Perez — cuentas abajo |
| URL del sistema desplegado | sin desplegar aún |
| Ultima revision | 2026-09-10 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 5 | CORTE1 | `2988b03` (2026-09-06T23:35:40-05:00) | 8/12 | no aplica | si |
| 4 | S4 | `d7ba824` (2026-08-30T23:39:33-05:00) | 5/10 | 3.0 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `06920209` · 2026-08-09T16:03:46-05:00 | 4/9 | 2,8 * | sí |
| 2 | S2 | `db90ff2` (2026-08-16T21:22:20-05:00) | 9/9 | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dd4ea1cb8` · 2026-08-23T23:46:24-05:00 | 9/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Javier Carta Lacharme sin commits ni cuenta atribuible | S1 | Cerrado en S3: `jxviercarta-a11y` firma 3 commits en el periodo (atribución por confirmar con el docente) | Verificar acceso al repositorio y empezar a contribuir (la contribución individual se califica en el final) |
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas del contrato | S1 | Cerrado en S3 (`8ba799f`): tabla de 8 columnas con enlace al ADR desde ASP-01 | Convertir a tabla ID·Aspecto·Requisito·C4·ADR·Código·Pruebas·Evidencia; además enlazar el ADR 0001 desde la fila del aspecto y desde ESC-01/ESC-02 |
| `docs/adr/README.md` haría fallar el filtro de nombres de ADR (placeholder) | S2 | Cerrado en S3 (`2abab34` lo eliminó) | Resuelto |
| ADR 0001 en estado «propuesto» y no alcanzable desde `aspectos.md` ni desde los escenarios que lo motivan | S3 | Parcialmente cerrado: los dos enlaces ya existen (ASP-01 y ESC-01); sigue «propuesto, pendiente de ratificación» | Ratificar (aceptar) el ADR |
| `ia.md` sin lo rechazado y su motivo en la entrada S3 | S3 | Cerrado en S3 (`8ba799f`): columna «Rechazado / motivo» llena | Resuelto |
| Prueba sin pipeline ni evidencia de ejecución | S3 | Cerrado en S3 (`3e2a54b`): workflow añadido y CI en verde sobre el hash calificado | Resuelto |
| arc42 actualizado tras el cierre (2fc55e1, b4904bd) | S4 | no (resuelto tarde) | — |
| Módulo de inventario añadido tras el cierre (666c4e4) | S4 | no (resuelto tarde) | — |
| ADR-0002 eliminado tras el cierre (64ab86f) | S4 | no (resuelto tarde) | — |
| aspectos.md y containers.md corregidos tras el cierre (4e6957e, 3de2988) | S4 | no (resuelto tarde) | — |
| Confirmar si arc42 secciones 4-6 y 12 quedaron redactadas a HEAD | S4 | si | |
| Añadir evidencia de análisis estático SonarCloud | S4 | si | |
| Completar celda de Pruebas en docs/aspectos.md | S4 | si | |
| Etiqueta `corte-1` ausente | S5 | No (creada 2026-09-06, `2988b03`) | Resuelto. |
| Respuesta al reto sin diagnóstico, ADR ni incremento identificado | S5 | Sí (más grave de lo esperado) | El equipo escribió ADR-0002, reporte de medición y trazabilidad completos sobre control de concurrencia (ASP-02), pero `git diff --stat` confirma que ningún archivo de `app/` cambió: el mecanismo de lock que describen no existe en el código y las cifras de medición no son reproducibles. Implementar realmente el mecanismo antes de sustentar. |
| Umbral de rendimiento definido sin medición ejecutada | S2 | Sí | Aportar herramienta, carga, procedimiento y resultado. |
| Módulo de inventario de HEAD sin fila propia en `docs/aspectos.md` | S5 | No (resuelto) | ASP-02 ya tiene fila completa en `docs/aspectos.md`, aunque la celda de código no refleja un cambio real (ver hallazgo crítico). |
| Registro de IA sin entrada del Corte 1 | S5 | No (resuelto) | `docs/ia.md` tiene entrada del 2026-09-06 para el Reto Corte 1 con rechazo explícito y motivo técnico. |
| Enlace del README a `docs/c4/container.md` no existe | S5 | No verificado en esta revisión | No se reinspeccionó este enlace puntual; confirmar en el próximo corte. |
| La corrección 'Update and rename feedback.md to correcciones.md' (ac951e3, 2026-09-08) es posterior al cierre. | S2 | no (resuelto tarde) | — |
| Se añadieron ADR-0001 y ADR-0002, código, CI y trazabilidad en commits posteriores al cierre (7b0aad5, bcb133d, 8d149c1). | S2 | no (resuelto tarde) | — |
| El commit cf9d7d3 define Flutter como frontend, decisión de stack posterior a la entrega s2. | S2 | no (resuelto tarde) | — |
| No hay runs_ci citables que confirmen la ejecución del pipeline a HEAD. | S2 | si | |
| Faltaba CI/ADR en s2; a HEAD ya existen, pero la evidencia de ejecución no está registrada. | S2 | si | |
| Secciones 5, 6 y glosario de arc42: se agregaron después del cierre (commits 22bd660, c870f2b y otros entre 2026-09-06 y 2026-09-08). | S4 | no (resuelto tarde) | — |
| Prueba de corte vertical: tests/productos/test_api_corte_vertical.py se agregó en HEAD pero no existe en d7ba824. | S4 | no (resuelto tarde) | — |
| Fila de aspectos con columna Pruebas completa: se resolvió en HEAD con la trazabilidad del corte 1 (commit bb4ef0c). | S4 | no (resuelto tarde) | — |
| SonarCloud: sonar-project.properties se agregó en HEAD, no en el commit calificado. | S4 | no (resuelto tarde) | — |
| En HEAD aún no se verifica ejecución de SonarCloud en un run; no hay evidencia de análisis estático en los runs disponibles. | S4 | si | |
| correcciones.md creado en ac951e3 (2026-09-08) tras el cierre, renombrando feedback.md. | S5 | no (resuelto tarde) | — |
| Frontend definido como Flutter en cf9d7d3 (2026-09-07) tras el cierre, actualizando README y containers.md. | S5 | no (resuelto tarde) | — |
| Integrar SonarCloud al pipeline de CI. | S5 | si | |
| Verificar que correcciones.md responda a todos los hallazgos S1-S4. | S5 | si | |
| Equilibrar la distribución de contribuciones. | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `ISCOUTB/AS_202620_InvenTrack`, público |
| Estructura mínima | Cumple | Seis rutas presentes; arc42 en `docs/arc42/arc42-template-EN.md` |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular-con-hexagonal-por-modulo.md`; placeholder eliminado |
| ADR aceptados sin reescribir | Cumple | Churn previo; aceptado en `45d2fa0` y sin cambios posteriores. |
| `docs/ia.md` al día | Cumple | Entrada del 2026-09-06 referida al Reto Corte 1, con rechazo y motivo técnico. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Escaneos limpios. |
| Contribución de todos los integrantes | Cumple | Cuatro personas consolidadas para cuatro integrantes en HEAD. |
| Pipeline en verde | No cumple | Run de HEAD `33811437677` en verde; no demuestra el reto. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Javier Alejandro Carta Lacharme | `jxviercarta-a11y` (atribución por confirmar) | 3 (S3) | 0 | — | Apareció en S3 (ficha, README, C4) |
| Esteban Javier Peluffo Marquez | Esteban Peluffo (correo omitido) | 3 (S3) | 0 | — | ia.md y entrega semanal |
| Felix Andres Taborda Jimenez | FlexT21 + «Felix Taborda» (mismo noreply, consolidado) | 1 (S3) | 0 | — | Correspondencia por confirmar con el docente |
| Jose Gabriel Vargas Perez | Josephva24 + «Jose Vargas» (mismo correo `[correo omitido]`, consolidado) | 6 (S3) | 0 | — | ADR, esqueleto, workflow de CI y ajustes de trazabilidad |

## Preguntas abiertas para la sustentación

- ¿`jxviercarta-a11y` corresponde efectivamente a Javier Carta Lacharme?
- ¿`FlexT21` corresponde efectivamente a Felix Taborda?
- ¿Por qué el ADR 0001 sigue «propuesto» y cuándo lo ratifican como aceptado?
