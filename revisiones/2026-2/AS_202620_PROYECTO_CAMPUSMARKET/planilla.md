# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | CampusMarket |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET` |
| Integrantes y su usuario de GitHub | Nilver Garcia Pimentel · Camilo Jose Martinez Berrio · Joshua Jose Tenorio Alvarez — historial con una sola identidad: `camilixo92` (correspondencias por confirmar con el docente) |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S2, commit `4f72799`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `81ef5f1` · 2026-08-08T20:17:21-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `4f72799` · 2026-08-16T22:01:41-05:00 | 7/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | | | no aplica | |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | | | no aplica | |
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
| Historial con una sola identidad de commits (23/23) | S1 | sí | 2 de 3 integrantes sin aparición; repartir contribución |
| Estructura fuera de convención: archivos sueltos en `docs/`, sin `docs/arc42/`, `docs/adr/`, `docs/c4/` | S1 | sí | Mover a la estructura mínima del contrato |
| `docs/aspectos.md` sin tabla ni enlaces a escenarios | S1 | sí (sin cambios en S2) | Actualizar con la tabla de 8 columnas y enlaces por escenario |
| `docs/ia.md` sin registro de lo rechazado | S1 | sí | Incluir la columna de rechazos con motivo |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público (ls-remote sin auth) |
| Estructura mínima | No cumple | Archivos sueltos en `docs/`; sin `docs/arc42/`, `docs/adr/`, `docs/c4/` |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR |
| `docs/ia.md` al día | No cumple | Registro de usos al día pero sin lo rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep, .env y `log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | Una sola identidad en todo el historial |
| Pipeline en verde | No verificado | Sin `.github/workflows/` (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Nilver Garcia Pimentel | sin cuenta observada | 0 | — | — | Añadido al README el 11-08 (`9a9dc3d`), después del cierre S1 |
| Camilo Jose Martinez Berrio | ¿`camilixo92`? (confirmar) | 23 | — | — | Único autor de todo el historial |
| Joshua Jose Tenorio Alvarez | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |

## Preguntas abiertas para la sustentación

- ¿Nilver Garcia Pimentel y Joshua Jose Tenorio Alvarez tienen acceso al repositorio y cómo contribuirán?
- ¿Cuándo organizarán la documentación en `docs/arc42/`, `docs/adr/` y `docs/c4/`?
