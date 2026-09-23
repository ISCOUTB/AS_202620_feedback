# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | DinamikUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_DinamikUTB` |
| Integrantes y su usuario de GitHub | Luis Daniel Padilla Leottau (`Daniel-dev02`) · Gillianis Del Carmen Perez Revolledo (`gillianisperez-prog`) · Esteban Ramirez Rios (`Eramirezr`) · Juan Jose Vargas Perez (`JuanchisV`, firma también como «Juan José Vargas Pérez» con el mismo correo) |
| URL del sistema desplegado | sin desplegar todavía |
| Ultima revision | 2026-09-23 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 8 | S8 | `65202f2` (2026-09-21T22:51:09-05:00) | 1/12 | 1.3 (prelim.) | si |
| 7 | S7 | `5e6fa73` (2026-09-20T23:57:27-05:00) | 7/10 | 3.8 | si |
| 6 | S6 | `265e652` (2026-09-13T23:29:49-05:00) | 0/8 | 1.0 | si |
| 5 | CORTE1 | `72bfc7e` (2026-09-07T22:28:37-05:00) | 8/12 | 3.7 | sí (actualizada) |
| 4 | S4 | `8558156` (2026-08-30T23:52:24-05:00) | 7/10 | 3.8 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `769f970` · 2026-08-09T21:24:49-05:00 | 7/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `58734e1c` · 2026-08-16T23:33:53-05:00 | 9/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `fe52ab594` · 2026-08-23T23:20:33-05:00 | 5/9 | no se publica | sí (actualizada tras el cierre) |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Ficha del problema entregada en PDF, no en Markdown | S1 | sí | Ver feedback S1/S2 |
| Solo una tensión de calidad declarada (se pedían dos) | S1 | sí | Ver feedback S1/S2 |
| Trabajo del periodo concentrado en un integrante | S2 | sí (en S3, JuanchisV firma 21 de 46 commits) | Ver feedback S1/S2 y S3 |
| Esteban sin commits en el periodo (S1; reaparece en S3) | S1 | cerrado en S3 (2 commits: `2c78be9`, `fe52ab5`) | Ver feedback S3 |
| Matriz de estilos sin referencia a los escenarios del árbol de utilidad | S3 | sí | Ver feedback S3 |
| `docs/aspectos.md` con la columna ADR en «Pendiente» aun existiendo el ADR 0001 (la tabla de 8 columnas y los enlaces a escenarios ya llegaron) | S3 | sí (parcialmente cerrado: tabla y enlaces a escenarios OK; columna ADR sigue pendiente) | Ver feedback S3 |
| 4258407 Update start.bat (2026-08-31T00:07:55-05:00) | S4 | no (resuelto tarde) | — |
| d87a771 Merge pull request #8 (2026-08-31T00:11:21-05:00) | S4 | no (resuelto tarde) | — |
| 1308052 Update start.bat (2026-08-31T00:12:04-05:00) | S4 | no (resuelto tarde) | — |
| 3c16fba Update start.bat (2026-08-31T00:13:28-05:00) | S4 | no (resuelto tarde) | — |
| Enlazar ADR-0002 en sección 9 | S4 | si | |
| Añadir trazabilidad commit/PR y pruebas en ADR | S4 | si | |
| Evidencia de run de CI en verde | S4 | si | |
| Verificar fila de aspectos.md | S4 | si | |
| Verificar contenido de docs/ia.md | S4 | si | |
| Correcciones S1–S4 trazables y contrastadas | S5 | cerrado | `correcciones.md` relaciona cada hallazgo con rutas verificadas en el hash calificado. |
| Pipeline de CI en el estado calificado | S5 | cerrado | El run asociado a `72bfc7e` terminó en verde. |
| Trazabilidad consolidada de aspectos | S5 | sí | A-02 a A-08 tienen eslabones o columnas pendientes en `docs/aspectos.md`. |
| ADR 0001 reescrito después de su aceptación | S5 | sí | Documentar cambios posteriores como ADR nuevo, sin editar una decisión aceptada. |
| PDF exigido por el aula y sustentación | S5 | No verificado | Se comprueban en Moodle y en la sesión docente, no en el repositorio. |
| Confirmar mapa de contextos y tabla módulo-datos en 08-cross-cutting-concepts.md | S6 | si | |
| Verificar violaciones de propiedad de datos y plan de corrección | S6 | si | |
| Comparar C4 nivel 3 con el hash de S5 y posible ADR de reajuste | S6 | si | |
| Revisar docs/aspectos.md | S6 | si | |
| Evidenciar ejecución del pipeline con runs_ci | S6 | si | |
| Contrato OpenAPI/AsyncAPI/proto versionado con rutas y esquemas | S7 | si | |
| Prueba de contrato integrada al pipeline | S7 | si | |
| Demostración de que la prueba de contrato falla ante cambio incompatible | S7 | si | |
| ADR de estrategia de integración (síncrono vs asíncrono) | S7 | si | |
| Etiquetado de protocolo y formato en el C4 nivel 2 | S7 | si | |
| Contenido verificable de docs/aspectos.md y docs/ia.md | S7 | si | |
| Evidencia pública del análisis estático con Quality Gate | S7 | si | |
| YAML de ci.yml corregido en 31350f1 el mismo día del cierre, tras el experimento del contrato. | S7 | no (resuelto tarde) | — |
| Bloqueo de permisos de SonarCloud documentado como hallazgo en 1ffe3e2 y 5e6fa73 en vez de resolverse. | S7 | no (resuelto tarde) | — |
| Commit 8a5ae13 'Update ci.yml' posterior al cierre (2026-09-21T00:01:43-05:00). | S7 | no (resuelto tarde) | — |
| SonarCloud: run que invoque el scanner y URL pública del análisis con Quality Gate. | S7 | si | |
| Contenido de arc42 sección 6 y del C4 nivel 2 con protocolo y formato por flecha. | S7 | si | |
| Historial git del contrato y confirmación de la versión de la API. | S7 | si | |
| Contenido de docs/aspectos.md con sus ocho columnas navegables. | S7 | si | |
| Publicar URL del sistema accesible desde fuera de la red universitaria, con hora de comprobación. | S8 | si | |
| Health check consultable y su código de respuesta. | S8 | si | |
| Infraestructura como código versionada (Dockerfile/compose o IaC del proveedor). | S8 | si | |
| Logs estructurados y métrica consultable ligada a un escenario de calidad. | S8 | si | |
| Estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita. | S8 | si | |
| arc42 §7 con una caja por pieza y §2 con límite de costo y restricción de tarjeta. | S8 | si | |
| Un ADR por decisión de plataforma con alternativa descartada. | S8 | si | |
| Pendiente desde S6: URL pública del análisis en SonarCloud con estado del Quality Gate. | S8 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `AS_202620_DinamikUTB`, público. |
| Estructura mínima | Cumple | Las seis rutas presentes; arc42 con 12 secciones. |
| Convención de nombres de ADR | Cumple | `0001-seleccion-monolito-modular.md` conforme. |
| ADR aceptados sin reescribir | No cumple | ADR 0001 tuvo una actualización posterior a su aceptación el 1 de septiembre; debe preservarse y sucederse con un ADR nuevo. |
| `docs/ia.md` al día | Cumple | Entradas del 23/08 con rechazos («Rechazado parcialmente») y motivo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | Cumple | 4 de 4 en S3 (Juan 21, Gillianis 11, Luis 12, Esteban 2); desbalance anotado. |
| Pipeline en verde | No cumple | El workflow de CI y el run asociado a `72bfc7e` verifican backend y frontend en verde. |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Juan Jose Vargas Perez | `JuanchisV` (+ firma «Juan José Vargas Pérez») | 21 (S3) | — | — | Autor del ADR y del esqueleto |
| Gillianis Del Carmen Perez Revolledo | `gillianisperez-prog` | 11 (S3) | — | — | Enlaces de escenarios en aspectos.md |
| Luis Daniel Padilla Leottau | `Daniel-dev02` (+ firma «LUIS DANIEL») | 12 (S3) | — | — | README y merges de ramas |
| Esteban Ramirez Rios | `Eramirezr` | 2 (S3) | — | — | Estructura del proyecto e ia.md; reapareció tras S1/S2 sin commits |

## Preguntas abiertas para la sustentación

- ¿Por qué la ficha del problema declara una sola tensión de calidad cuando se pedían dos?
- ¿Cómo se repartirá el trabajo de las próximas entregas para equilibrar la contribución del historial?
- ¿Por qué la columna ADR de `docs/aspectos.md` sigue en «Pendiente» si el ADR 0001 existe desde el 23 de agosto (y la nota dice que los elementos «todavía no existen»)?
- ¿Qué tácticas concretas aplicarán a Q-01, Q-02 y Q-03 para la semana 4?
