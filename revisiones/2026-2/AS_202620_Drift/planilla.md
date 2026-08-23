# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Drift |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Integrantes y su usuario de GitHub | Jerry Daniel Buelvas Mejia (`JerryDBM`) · Mauricio Andres Fernandez Espinosa (`maufern4ndez`) · Luis Mario Perez Diaz (`lmpdiaz12`) · Joshua David Reyes Leones (`JoshuaR01` y `JoshXX`, mismo correo) |
| URL del sistema desplegado | sin desplegar todavía |
| Última revisión | 2026-08-23 (Evidencia S2) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `b7ec296c` · 2026-08-09T22:59:42-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `23fb8c29` · 2026-08-16T22:39:37-05:00 | 6/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas ni enlaces a escenarios | S1 | sí | Ver feedback S1/S2 |
| Ficha del problema sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Documentación arc42 y C4 fuera de las rutas del contrato | S2 | cerrado el 2026-08-22 (tras el cierre; reubicada en `arc42/`) | Ver feedback S1/S2 |
| Jerry y Joshua sin commits en S1 | S1 | cerrado (ambos aparecen en S2) | Ver feedback S1/S2 |
| Desbalance de contribución en el periodo | S2 | sí | Ver feedback S1/S2 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_Drift`, público. |
| Estructura mínima | No cumple | En el cierre S2: arc42 en `docs/arc42_*.md` y C4 en `docs/c4_contexto.md` (fuera de ruta); sin `docs/adr/`. Reorganizado el 08-22, tras el cierre. |
| Convención de nombres de ADR | Cumple (vacuo) | Sin ADR. |
| ADR aceptados sin reescribir | Cumple (vacuo) | Sin ADR. |
| `docs/ia.md` al día | Cumple | Commit `8df39f3` en el periodo S2. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas en 4 personas (20/7/6/4). |
| Pipeline en verde | No verificado | Sin pipeline todavía (no exigido en S2). |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Mauricio Andres Fernandez Espinosa | `maufern4ndez` | 7 (S1) / 20 (S2) | — | — | — |
| Luis Mario Perez Diaz | `lmpdiaz12` | 4 (S1) / 4 (S2) | — | — | — |
| Jerry Daniel Buelvas Mejia | `JerryDBM` | 0 (S1) / 6 (S2) | — | — | sin commits en S1 |
| Joshua David Reyes Leones | `JoshuaR01` + `JoshXX` (mismo correo) | 0 (S1) / 7 (S2) | — | — | sin commits en S1; dos identidades consolidadas |

## Preguntas abiertas para la sustentación

- Confirmar que `JoshuaR01`/`JoshXX` corresponden a Joshua David Reyes Leones (mismo correo `correo omitido`).
- ¿Por qué el árbol de utilidad no muestra la priorización por impacto y riesgo si la sección 1 sí la tiene?
- ¿Qué herramienta usarán para medir los p95 declarados en los escenarios?
