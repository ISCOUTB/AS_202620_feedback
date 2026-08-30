# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | CampusMarket |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Integrantes y su usuario de GitHub | Nilver Garcia Pimentel · Camilo Jose Martinez Berrio · Joshua Jose Tenorio Alvarez — historial con tres identidades: `camilixo92`, `nilver-garcia` y `Nnigarp` (misma cuenta de GitHub, consolidar) y `Carulla-sd` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-08-28 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `81ef5f1` · 2026-08-08T20:17:21-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `4f72799` · 2026-08-16T22:01:41-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `4dd857a` · 2026-08-23T23:54:16-05:00 | 9/9 | no se publica | sí |
| 4 | S4 | `0197341` (2026-08-29T01:13:49-05:00) | 8/10 | 4.2 | si |
| 5 | Primer corte · reto de línea base | `corte-1` | | | |
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
| Historial con una sola identidad de commits (23/23) | S1 | no (S3: 3 personas; `nilver-garcia` y `Nnigarp` son la misma cuenta, consolidar) | Consolidar la identidad duplicada en git |
| Estructura fuera de convención: archivos sueltos en `docs/` | S1 | no (S3 resuelto) | `docs/arc42/`, `docs/adr/` y `docs/c4/` ya existen |
| `docs/aspectos.md` sin tabla ni enlaces | S1 | no (S3 resuelto) | Tabla de 8 columnas con enlaces funcionales |
| `docs/ia.md` sin registro de lo rechazado | S1 | sí (sin entradas de S3 tampoco) | Incluir la columna de rechazos con motivo y las entradas del 17-23 ago |
| ADR 0001 ausente aunque arc42 y aspectos.md lo enlazaban | S3 | no (resuelto en PR #5) | ADR completo y enlazado desde EC-03 y ASP-03 |
| README sin comando único de arranque | S3 | no (resuelto) | `python -m uvicorn backend.app.main:app --reload` documentado |
| Sin prueba automatizada ni pipeline | S3 | no (resuelto) | `backend/tests/test_health.py` + workflow con 4 runs en verde |
| Esqueleto Flutter por defecto, sin módulos del ADR | S3 | parcial | Backend con los 4 módulos; el frontend sigue siendo la plantilla Flutter por defecto |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público (clon sin auth) |
| Estructura mínima | Cumple | Las seis rutas presentes en `4dd857a` |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md` |
| ADR aceptados sin reescribir | Cumple | Un único commit (`dbdd9c4`) |
| `docs/ia.md` al día | No cumple | Último commit 2026-08-16; sin entradas S3 ni columna de rechazos |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 3 personas para 3 integrantes (`nilver-garcia`+`Nnigarp` = misma cuenta); correspondencia por confirmar |
| Pipeline en verde | Cumple | 4 runs «Pruebas del backend» success; el último (32691690794) anterior al cierre |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Nilver Garcia Pimentel | `nilver-garcia` / `Nnigarp` (misma cuenta, consolidar) | 33 | — | — | Todo el esqueleto S3: backend, prueba, workflow, README |
| Camilo Jose Martinez Berrio | ¿`camilixo92`? (confirmar) | 26 | — | — | Autor principal S1–S2; merges de PR #2, #3 y #5 |
| Joshua Jose Tenorio Alvarez | ¿`Carulla-sd`? (confirmar) | 1 | — | — | Esqueleto Flutter inicial |

## Preguntas abiertas para la sustentación

- ¿Cuál cuenta corresponde a cada integrante (`camilixo92`, `nilver-garcia`/`Nnigarp`, `Carulla-sd`)?
- ¿Cuándo modularizarán el frontend con la misma frontera de módulos del backend?
