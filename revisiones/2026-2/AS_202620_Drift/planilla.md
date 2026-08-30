# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Drift |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Integrantes y su usuario de GitHub | Jerry Daniel Buelvas Mejia (`JerryDBM`) · Mauricio Andres Fernandez Espinosa (`maufern4ndez`) · Luis Mario Perez Diaz (`lmpdiaz12`) · Joshua David Reyes Leones (`JoshuaR01` y `JoshXX`, mismo correo) |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-08-28 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 4 | S4 | `ff339e9` (2026-08-29T21:53:23-05:00) | 2/10 | 1.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `b7ec296c` · 2026-08-09T22:59:42-05:00 | 4/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `23fb8c29` · 2026-08-16T22:39:37-05:00 | 6/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `0d006bba` · 2026-08-23T18:05:58-05:00 | 5/9 | no se publica | sí |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/aspectos.md` en prosa, sin la tabla de 8 columnas ni enlaces a escenarios ni al ADR | S1 | sí | Ver feedback S1/S2 y S3 |
| Ficha del problema sin tensiones de calidad | S1 | sí | Ver feedback S1/S2 |
| Desbalance de contribución en el periodo | S2 | sí (51 vs 9 commits en S3) | Ver feedback S1/S2 y S3 |
| README con arranque contradictorio (mvn sin pom.xml / uvicorn solo backend) y sin comando único | S3 | sí | Ver feedback S3 |
| Sin pipeline: prueba existe sin evidencia de verde | S3 | sí | Ver feedback S3 |
| Matriz de estilos sin referencia a los escenarios E1–E5 | S3 | sí | Ver feedback S3 |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_Drift`, público. |
| Estructura mínima | Cumple | Las seis rutas en su lugar desde la reorganización del 08-22. |
| Convención de nombres de ADR | Cumple | `0001-arquitectura-base.md` conforme. |
| ADR aceptados sin reescribir | Cumple | Creado y renombrado el mismo día (2026-08-23), sin reescrituras posteriores. |
| `docs/ia.md` al día | Cumple | Commits 08-21/08-22; rechazo narrado en §3.1 con motivo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | Cumple | Los 4 firman en S3, con desbalance (51/19/18/9). |
| Pipeline en verde | No verificado | Sin pipeline; prueba local sin evidencia de ejecución. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Luis Mario Perez Diaz | `lmpdiaz12` | 51 (S3) | — | — | Autor del ADR y de la mayor parte del periodo |
| Mauricio Andres Fernandez Espinosa | `maufern4ndez` | 19 (S3) | — | — | — |
| Joshua David Reyes Leones | `JoshuaR01` (+ `JoshXX`, mismo correo) | 18 (S3) | — | — | dos identidades consolidadas |
| Jerry Daniel Buelvas Mejia | `JerryDBM` | 9 (S3) | — | — | — |

## Preguntas abiertas para la sustentación

- Confirmar que `JoshuaR01`/`JoshXX` corresponden a Joshua David Reyes Leones (mismo correo).
- ¿Por qué el árbol de utilidad no muestra la priorización por impacto y riesgo si la sección 1 sí la tiene?
- ¿Qué herramienta usarán para medir los p95 declarados en los escenarios?
- ¿Cuál es el comando único real de arranque (backend Python + frontend Next) y por qué el README menciona `mvn spring-boot:run` sin pom.xml?
- ¿Cómo van a equilibrar la contribución (51 vs 9 commits en S3)?
