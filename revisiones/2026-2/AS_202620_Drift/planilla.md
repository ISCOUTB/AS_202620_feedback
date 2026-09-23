# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Drift |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Integrantes y su usuario de GitHub | Jerry Daniel Buelvas Mejia (`JerryDBM`) · Mauricio Andres Fernandez Espinosa (`maufern4ndez`) · Luis Mario Perez Diaz (`lmpdiaz12`) · Joshua David Reyes Leones (`JoshuaR01` y `JoshXX`, mismo correo) |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-09-23 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 8 | S8 | `9334a03` (2026-09-20T20:19:47-05:00) | 1/12 | 1.3 (prelim.) | si |
| 7 | S7 | `9334a03` (2026-09-20T20:19:47-05:00) | 5/10 | 3.0 | si |
| 6 | S6 | `5f7fa4c` (2026-09-13T22:07:49-05:00) | 5/8 | 3.5 (prelim.) | si |
| 5 | CORTE1 | `74337a3` (2026-09-08T02:53:31Z) | 7/12 | 3.3 | si |
| 4 | S4 | `4254f4a` (2026-08-30T19:13:01-05:00) | 7/10 | 3.8 | si |
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
| Prueba automatizada del recorrido completo | S4 | si | |
| Tabla de trazabilidad en docs/aspectos.md | S4 | si | |
| ADR con trazabilidad y marcado de reemplazo | S4 | si | |
| README con requisitos previos y comando de arranque | S4 | si | |
| Evidencia de run de CI en verde | S4 | si | |
| Verificar/crear etiqueta corte-1 | S5 | sí (el propio equipo la reconoce pendiente en `docs/correciones.md`) | Se calificó el último commit ≤ cierre (`d110d6d0`); se les pidió crear la etiqueta antes del próximo corte, ya tienen el procedimiento escrito. |
| Registrar ADR del reto con alternativas y decisión | S5 | sí (autoadmitido pendiente) | El propio equipo lo marca "Pendiente, corresponde al reto que será asignado" en `docs/correciones.md`. |
| Medir línea base con procedimiento | S5 | sí (autoadmitido parcial) | Método de verificación definido en `docs/escenarios.md`; falta ejecutar la medición y registrar el resultado. |
| Completar aspectos.md con 8 columnas | S5 | cerrado | `docs/aspectos.md` ya tiene las 8 columnas del contrato con las 5 filas E1-E5. |
| Añadir rechazos con motivo en ia.md | S5 | cerrado | Registro 11 de `docs/ia.md` descarta una alternativa con motivo técnico explícito. |
| Evidenciar run de CI en verde | S5 | cerrado | Run verde confirmado sobre el commit calificado, antes del cierre. |
| ADR con marca de reemplazo y trazabilidad | S5 | cerrado | ADR-0001 marca "Superada parcialmente por ADR-0002" con enlace; corrige el hallazgo preliminar. |
| Nombres de ADR enuncian el tema, no la decisión | S5 | sí | 0001 y 0002 comparten el título "Selección de Arquitectura Base"; deberían titularse por la decisión (p. ej. "Adoptar Next.js/FastAPI..."). |
| Tres commits llegaron después del cierre (2026-09-07T05:22Z–06:26Z) | S5 | — (no se calificaron) | Se les avisó que solo cuenta lo anterior al cierre; esos commits corrigen duplicación de pruebas y documentan en ia.md. |
| dbb98d3 elimina duplicación en tests de búsqueda | S5 | no (resuelto tarde) | — |
| 75881e4 elimina duplicación en test de búsqueda (corte 1) | S5 | no (resuelto tarde) | — |
| e77a240 actualiza README con validación | S5 | no (resuelto tarde) | — |
| c12dda8 documenta proceso de corte vertical en ia.md | S5 | no (resuelto tarde) | — |
| 74337a3 actualiza README con instrucciones de prueba vertical | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz | S5 | si | |
| secciones arc42 7/8/11 | S5 | si | |
| trazabilidad E3-E5 | S5 | si | |
| commit en ADR-0001 | S5 | si | |
| verificación de pipeline | S5 | si | |
| README con comando único | S5 | si | |
| Mapa de contextos con relaciones tipificadas | S6 | si | |
| Tabla módulo-datos con dueño único | S6 | si | |
| Lista de violaciones con plan de corrección | S6 | si | |
| Sección 8 de arc42 | S6 | si | |
| C4 nivel 3 y ADR si aplica | S6 | si | |
| Trazabilidad completa en aspectos.md | S6 | si | |
| Registro de rechazos en ia.md | S6 | si | |
| Instrucciones de arranque y prueba en README | S6 | si | |
| Evidencia de ejecución de CI | S6 | si | |
| Correcciones a correcciones.md y enlaces subidas después del cierre (commits 1cab45e, df8f512, 11577b9, 6e275a6, 6d0a1b8, 2026-09-10T22:15:10Z a 22:21:13Z) no estaban en el estado calificado. | S5 | no (resuelto tarde) | — |
| correcciones.md en la raíz (a HEAD sigue en docs/correciones.md). | S5 | si | |
| Enlaces rotos en docs/aspectos.md y docs/correciones.md. | S5 | si | |
| Celdas pendientes en la tabla de trazabilidad (E3-E5). | S5 | si | |
| Nomenclatura de ADR no conforme. | S5 | si | |
| Falta SonarCloud en el pipeline. | S5 | si | |
| Contrato OpenAPI/AsyncAPI versionado (S7) | S7 | si | |
| Prueba de contrato ejecutada por el pipeline (S7) | S7 | si | |
| Evidencia de que la prueba de contrato falla ante un cambio incompatible (S7) | S7 | si | |
| ADR de estrategia de integración síncrona o asíncrona (S7) | S7 | si | |
| Evidencia pública de SonarCloud con Quality Gate, pendiente desde S6 | S7 | si | |
| C4 nivel 2 con protocolo y formato en cada flecha | S7 | si | |
| Trazabilidad de ADR-0001 y ADR-0003 (commit y enlaces pendientes) | S7 | si | |
| Prueba de sustitución del adaptador para E2, declarada pendiente en docs/aspectos.md | S7 | si | |
| 2026-09-15T11:04-11:27 -05:00: b2bf164, 56f979b, 66dccb3, 7483132, 579ff78 y 430b9a0 reescriben y renombran el documento S6 y ajustan los enlaces del README después del cierre 2026-09-14T05:00Z. | S6 | no (resuelto tarde) | — |
| 2026-09-15T10:40:25-05:00: 418196c elimina matrices de cumplimiento y secciones de conclusión del paquete S6 tras el cierre. | S6 | no (resuelto tarde) | — |
| Evidencia pública de SonarCloud (run exitoso del scanner y URL del análisis con Quality Gate) para el hash revisado. | S6 | si | |
| Lista de no conformidades de propiedad con entidad, dueño esperado y ubicación observada, más su plan de corrección. | S6 | si | |
| Tipificación de las relaciones del mapa de contextos con el vocabulario de la semana. | S6 | si | |
| Trazabilidad de ADR-0003 (commit de implementación y enlace correcto al ADR de referencia) y de ADR-0001. | S6 | si | |
| Prueba específica de sustitución del adaptador externo para el escenario E2, hoy citada con una prueba que no la cubre. | S6 | si | |
| Ninguno: commits_tardios_post_cierre está vacío y el último commit (9334a03) es anterior al cierre; los ajustes de contrato y su evidencia se registraron el 2026-09-20. | S7 | no (resuelto tarde) | — |
| Aportar la línea de ci.yml que ejecuta la prueba de contrato y la URL del run. | S7 | si | |
| Aportar el registro del cambio incompatible que hizo fallar la prueba, o un run en rojo. | S7 | si | |
| Aportar la URL pública de SonarCloud con Quality Gate y el run que invocó el scanner. | S7 | si | |
| Completar la evidencia de correspondencia contrato-código (main.py frente a openapi.yaml). | S7 | si | |
| Aportar el contenido de arc42 sección 6, C4 de contenedores y docs/aspectos.md. | S7 | si | |
| Despliegue accesible desde fuera con URL y health check. | S8 | si | |
| Infraestructura como codigo versionada y README de recreacion del entorno. | S8 | si | |
| Pipeline en verde sobre master y analisis SonarCloud auditable. | S8 | si | |
| Logs estructurados y metrica consultable ligada al escenario E1. | S8 | si | |
| Estimacion de costo mensual con supuestos; limite de costo y 'sin tarjeta' en arc42 seccion 2. | S8 | si | |
| arc42 seccion 7 y un ADR por decision de plataforma con alternativa descartada. | S8 | si | |
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
| Pipeline en verde | No verificado | `.github/workflows/ci.yml` con runs verdes confirmados vía API, incluido el commit calificado de S5 (`d110d6d0`, antes del cierre). |

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
