# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Drift |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Drift` |
| Integrantes y su usuario de GitHub | Jerry Daniel Buelvas Mejia (`JerryDBM`) · Mauricio Andres Fernandez Espinosa (`maufern4ndez`) · Luis Mario Perez Diaz (`lmpdiaz12`) · Joshua David Reyes Leones (`JoshuaR01` y `JoshXX`, mismo correo) |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-09-11 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 6 | S6 | `6d0a1b8` (2026-09-10T22:21:13-05:00) | 0/8 | 1.0 (prelim.) | si |
| 5 | CORTE1 | `d110d6d` (2026-09-06T23:34:21-05:00) | 4/12 | no aplica | si |
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
