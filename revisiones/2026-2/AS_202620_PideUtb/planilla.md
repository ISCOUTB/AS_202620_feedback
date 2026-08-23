# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | PideUtb |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Integrantes y su usuario de GitHub | Daniela Sofia Arrieta Guardo · Santiago Jose Cuesta Maza · Ruddy Rodriguez Romero — cuentas observadas: `daniarriet`, `Santiago Cuesta`/`Santiago-C0` (misma persona, EQUIPOS.md:95); sin cuenta para Ruddy |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S2, commit `9b5f214`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `48cfbe3` · 2026-08-08T15:12:35-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `9b5f214` · 2026-08-16T12:47:26-05:00 | 9/9 | no se publica | sí |
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
| Estructura fuera de convención: sin `docs/arc42/`, `docs/adr/`, `docs/c4/`; ficha en PDF | S1 | sí (S2: arc42.md en raíz) | Mover a la estructura mínima del contrato; ficha en Markdown |
| `docs/ia.md` sin registro de lo rechazado | S1 | sí | Incluir la columna de rechazos con motivo en cada uso |
| Ruddy Rodriguez Romero sin aparición en el historial | S1 | sí (2 personas de 3 en S2) | Confirmar acceso y contribución del integrante |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público hoy; estuvo privado al inicio (EQUIPOS.md:49-52) |
| Estructura mínima | No cumple | `arc42.md` en raíz; sin `docs/adr/` ni `docs/c4/`; ficha en PDF |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR todavía |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR |
| `docs/ia.md` al día | No cumple | Sí registra uso en S2, pero sin lo rechazado |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep, .env y `log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 2 de 3 personas en el historial |
| Pipeline en verde | No verificado | Sin `.github/workflows/` (no exigido aún) |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Daniela Sofia Arrieta Guardo | ¿`daniarriet`? (confirmar) | 5 | — | — | Concentra la documentación S2 |
| Santiago Jose Cuesta Maza | `Santiago Cuesta` / `Santiago-C0` (misma persona) | 4 | — | — | Todo el trabajo de S1 |
| Ruddy Rodriguez Romero | sin cuenta observada | 0 | — | — | Sin aparición en el historial hasta S2 |

## Preguntas abiertas para la sustentación

- ¿Ruddy Rodriguez Romero tiene acceso al repositorio y cómo contribuirá?
- ¿Cuándo moverán la documentación a la estructura mínima (`docs/arc42/`, `docs/adr/`, `docs/c4/`) y la ficha a Markdown?
