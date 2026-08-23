# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Clubs UTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Integrantes y su usuario de GitHub | Hollman Jose De Orta Gonzalez (`deortahollman-star`) · Josh Robinson Ortega Castellon (`Josh4OP`, correo `correo omitido`) · Diego Andres Ramos De Avila (`Zavod Dev`, atribución sin confirmar) · Luis Daniel Salas Reyes (`Luis-Salas-Reyes`) |
| URL del sistema desplegado | sin desplegar todavía |
| Última revisión | 2026-08-23 (Evidencia S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `c92595ed` · 2026-08-09T13:25:24-05:00 | 2/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `69cfe68f` · 2026-08-16T18:33:10-05:00 | 7/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` sin la tabla de 8 columnas del curso | S1 | sí (rompe el criterio 9 de S2) | Ver feedback S1/S2 |
| Ficha del problema sin tensiones de calidad | S1 (no existía; en S2 se creó sin tensiones) | sí | Ver feedback S1/S2 |
| Hollman Jose De Orta Gonzalez sin commits en S1 | S1 | cerrado (aparece en S2) | Ver feedback S1/S2 |
| Estructura incompleta | S1 (sin README ni carpetas); en S2 falta `docs/c4/` literal (está `docs/C4/`) | sí | Ver feedback S1/S2 |
| `docs/ia.md` sin usos reales ni rechazos, sin commits en S2 | S2 | sí | Ver feedback S1/S2 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_Clubs_UTB`, público. |
| Estructura mínima | No cumple | C4 en `docs/C4/` (mayúscula) en lugar de `docs/c4/`; el resto de rutas existe. |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR; `docs/adr/` solo con `.temp`. |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR. |
| `docs/ia.md` al día | No cumple | Sin commits en el periodo S2; sin registro de usos ni rechazos. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | Cumple | Los 4 integrantes firman commits en S2 (21/5/4/3). |
| Pipeline en verde | No verificado | Sin pipeline todavía (no exigido en S2). |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Diego Andres Ramos De Avila | `Zavod Dev` (atribución sin confirmar) | 1 (S1) / 21 (S2) | — | — | firma con correo `correo omitido` |
| Josh Robinson Ortega Castellon | `Josh4OP` | 1 (S1) / 5 (S2) | — | — | correo `correo omitido` |
| Luis Daniel Salas Reyes | `Luis-Salas-Reyes` | 1 (S1) / 4 (S2) | — | — | correo `correo omitido` |
| Hollman Jose De Orta Gonzalez | `deortahollman-star` | 0 (S1) / 3 (S2) | — | — | sin commits en S1 |

## Preguntas abiertas para la sustentación

- Confirmar que `Zavod Dev` es Diego Andres Ramos De Avila.
- ¿Existen restricciones legales aplicables o hay que declarar que no aplican?
- ¿Por qué `docs/aspectos.md` no usa la tabla de 8 columnas si las secciones 01 y 02 enlazan hacia ella?
- De los 6 escenarios (U1–U3, C1–C3), ¿cuáles se conservarán si el rango pedido es 3–5?
