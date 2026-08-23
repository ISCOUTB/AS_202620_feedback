# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | AudioShare |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Integrantes y su usuario de GitHub | Santiago Adolfo Camacho Hernandez (commits como «Santiago Adolfo Camacho Hernández») · Vincent Cardona Castro (presumiblemente `cardonavincent26-design`, sin confirmar) · Elian Daniel Perea Vanegas («Elian Daniel Perea Vanegas») · Yeiver Andres Verjel Perez («Yeiver Andrés Vergel Pérez») |
| URL del sistema desplegado | sin desplegar todavía |
| Última revisión | 2026-08-23 (Evidencia S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `1c9ebb0a` · 2026-08-09T20:31:49-05:00 | 2/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d0760fdf` · 2026-08-16T23:31:32-05:00 | 4/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Nombre del repositorio con «PROYECTO_» de más (`AS_202620_PROYECTO_AudioShare`) | S1 (cierre 2026-08-10) | cerrado el 2026-08-18 (`31bcc18`), después del cierre S2 | Ver feedback S1/S2 (convención de nombre) |
| `docs/aspectos.md` sin la tabla de 8 columnas del curso | S1 | sí | Ver feedback S1/S2 |
| `docs/arc42/` sin montar en S1; en S2 en AsciiDoc y con sección 10 y árbol fuera de `docs/arc42/` | S1 (ausencia), S2 (formato/ubicación) | sí | Ver feedback S1/S2 |
| `docs/ia.md` sin entradas de «qué se rechazó y por qué» | S2 | sí | Ver feedback S1/S2 |
| Vincent Cardona Castro sin commits en el historial S1 | S1 | cerrado (aparece en S2) | Ver feedback S1/S2 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | No cumple | En el cierre S2 el nombre era `AS_202620_PROYECTO_AudioShare`; renombrado el 2026-08-18, tras el cierre. Público sí. |
| Estructura mínima | No cumple | Falta `docs/adr/` (sin `.gitkeep`); el resto de rutas existe. |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR todavía. |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR. |
| `docs/ia.md` al día | Cumple | Actualizado dentro del periodo S2 (`40dd80b`); pendiente la columna de rechazos. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias en `git grep`, `.env` ni historial. |
| Contribución de todos los integrantes | Cumple | Los 4 integrantes firman commits en S2 (15/14/13/12). |
| Pipeline en verde | No verificado | Sin pipeline todavía (no exigido en S2). |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Yeiver Andres Verjel Perez | firma como «Yeiver Andrés Vergel Pérez» | 6 (S1) / 14 (S2) | — | — | — |
| Santiago Adolfo Camacho Hernandez | firma como «Santiago Adolfo Camacho Hernández» | 3 (S1) / 12 (S2) | — | — | — |
| Elian Daniel Perea Vanegas | firma como «Elian Daniel Perea Vanegas» | 2 (S1) / 13 (S2) | — | — | — |
| Vincent Cardona Castro | presumiblemente `cardonavincent26-design` (sin confirmar) | 0 (S1) / 15 (S2) | — | — | sin commits en S1 |

## Preguntas abiertas para la sustentación

- Confirmar la cuenta de GitHub de Vincent Cardona Castro (¿`cardonavincent26-design`?) contra la matrícula.
- ¿Por qué el C4 de contexto omite la red Wi-Fi y el moderador que declara la sección 3?
- ¿Cómo medirán los escenarios (herramienta, carga, umbral)? Ninguno lo declara todavía.
