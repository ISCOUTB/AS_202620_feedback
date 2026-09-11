# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | CampusMarket |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Integrantes y su usuario de GitHub | Nilver Garcia Pimentel · Camilo Jose Martinez Berrio · Joshua Jose Tenorio Alvarez — cuentas consolidadas: `nilver-garcia`/`Nnigarp` (mismo id de cuenta, es una sola persona), `camilixo92`, `Carulla-sd` |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-11 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `81ef5f1` · 2026-08-08T20:17:21-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `4f72799` · 2026-08-16T22:01:41-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `4dd857a` · 2026-08-23T23:54:16-05:00 | 9/9 | no se publica | sí |
| 4 | S4 | `f3f4367` (2026-08-30T22:55:30-05:00) | 9/10 | 4.6 | si |
| 5 | CORTE1 | `8044215` (2026-09-06T16:05:15-05:00) | 10/12 | 4.3 | si |
| 6 | S6 | `8044215` (2026-09-06T16:05:15-05:00) | 1/8 | 1.5 (prelim.) | si |
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
| Historial con una sola identidad de commits (23/23) | S1 | no (S3: 3 personas; confirmado en S5 que `nilver-garcia`/`Nnigarp` son la misma cuenta) | Consolidar la identidad duplicada en git |
| Estructura fuera de convención: archivos sueltos en `docs/` | S1 | no (S3 resuelto, confirmado en `corte-1`) | `docs/arc42/`, `docs/adr/` y `docs/c4/` ya existen |
| `docs/aspectos.md` sin tabla ni enlaces | S1 | no (S3 resuelto; en S5 llegó a 6 filas con ASP-06 completo) | Tabla de 8 columnas con enlaces funcionales |
| `docs/ia.md` sin registro de lo rechazado | S1 | no (resuelto en S3/S4, confirmado en S5) | Mantener una entrada por semana con rechazo o corrección y motivo técnico |
| ADR 0001 ausente aunque arc42 y aspectos.md lo enlazaban | S3 | no (resuelto en PR #5) | ADR completo y enlazado desde EC-03 y ASP-03 |
| README sin comando único de arranque | S3 | no (resuelto) | `python -m uvicorn backend.app.main:app --reload` documentado |
| Sin prueba automatizada ni pipeline | S3 | no (resuelto) | `backend/tests/test_health.py` + workflow con runs en verde |
| Esqueleto Flutter por defecto, sin módulos del ADR | S3 | no (resuelto en S4: módulos `usuarios/publicaciones/catalogo/administracion`) | Backend y frontend con los 4 módulos |
| Integrar SonarCloud al pipeline | S4 | no (resuelto en S5: `.sonarcloud.properties` con proyecto oficial `ISCOUTB_AS_202620_PROYECTO_CAMPUSMARKET`; Quality Gate no verificado de forma independiente) | Confirmar en vivo el Quality Gate en la sustentación |
| Verificar arranque con un solo comando mediante ejecución | S4 | no (resuelto: evidencia en `docs/evidencias/arranque-un-comando-2026-09-04.md`) | — |
| Enlazar ADR-0001 con commit que lo implementa | S4 | no (resuelto: PR #5, commit `4dd857a`) | — |
| Definir medición de línea base | S4 | no (resuelto en S5 junto con el reto) | — |
| Diagnóstico de la restricción asignada (R-07) | S5 | no (resuelto: ADR-0002 y `docs/evidencias/linea-base-bloqueo-sqlite-2026-09-05.md`) | — |
| ADR del reto con alternativas y decisión | S5 | no (resuelto: ADR-0002) | — |
| Implementación del cambio sobre el corte vertical | S5 | no (resuelto: PR #28, commit `ff68cf2`) | — |
| Pruebas y medición contra umbral | S5 | no (resuelto: `test_bloqueo_sqlite_degrada_controladamente_y_se_recupera`, `medir_bloqueo_sqlite.py`) | — |
| Trazabilidad del reto en docs/aspectos.md | S5 | no (resuelto: fila ASP-06) | — |
| Registro de IA del corte en docs/ia.md | S5 | no (resuelto: sección "Evidencia S5") | — |
| PDF de dos páginas en Moodle | S5 | sin verificar | No disponible en el kit; confirmar en Moodle antes de cerrar la nota |
| ASP-01 y ASP-02 sin materializar en el corte vertical | S5 | sí (declarado explícitamente por el equipo, no oculto) | Materializar en cortes siguientes o mantener la declaración explícita si se posponen |
| Verificar entrega del PDF en Moodle | S5 | si | |
| Confirmar sustentación del corte | S5 | si | |
| Mapa de contextos con relaciones tipificadas | S6 | si | |
| Tabla módulo a datos con dueño único | S6 | si | |
| Lista de violaciones de propiedad de datos con plan de corrección | S6 | si | |
| Sección 8 de arc42 con lenguaje ubicuo y mapa de contextos | S6 | si | |
| C4 nivel 3 y ADR si los límites cambian | S6 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público (clon sin auth) |
| Estructura mínima | Cumple | Las seis rutas presentes en `corte-1`, en minúsculas |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md`, `0002-manejo-bloqueo-sqlite.md` |
| ADR aceptados sin reescribir | Cumple | Un único commit para 0001 (`dbdd9c4`); 0002 es un archivo nuevo |
| `docs/ia.md` al día | Cumple | Sección "Evidencia S5" con rechazos y motivo técnico |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 3 personas consolidadas: Nilver Garcia (124), Camilo Martinez (26), Joshua Tenorio (19) |
| Pipeline en verde | Cumple | Run del commit de la etiqueta (`80442158`) en success: https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/34059972075 |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits (HEAD) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Nilver Garcia Pimentel | `nilver-garcia` / `Nnigarp` (misma cuenta, id 115980006) | 124+10+2 | — | — | Mayor volumen; ADR-0002 y reto S5 |
| Camilo Jose Martinez Berrio | `camilixo92` | 26 | — | — | Autor principal S1–S2; merges de PR #2, #3, #5 |
| Joshua Jose Tenorio Alvarez | `Carulla-sd` | 19 | — | — | Módulos de frontend |

## Preguntas abiertas para la sustentación

- ¿Pueden mostrar en vivo el Quality Gate de SonarCloud para confirmar la afirmación de `correcciones.md`?
- ¿Cuándo materializarán ASP-01 y ASP-02 en el corte vertical?
