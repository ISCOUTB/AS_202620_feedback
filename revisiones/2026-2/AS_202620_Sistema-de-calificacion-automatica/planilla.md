# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Calificación automática |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-24 (S3 actualizada tras el cierre, commit `dd422fb`; 2 commits tardíos registrados) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4f6f568` · 2026-08-09T13:16:43-05:00 | 7/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d4302f4` · 2026-08-16T23:17:26-05:00 | 7/9 | no aplica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dd422fb` · 2026-08-23T23:52:23-05:00 | 6/9 | no se publica | sí |
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
| `docs/adr` versionado como blob vacío, no como directorio | S1 (08-09) | no (S3 resuelto) | Directorio con 0001, 0002 y 0003 |
| Ficha del problema fuera del repositorio («Informe Inicial» de Moodle) | S1 (08-09) | no (resuelto en `dd422fb`) | `docs/Ficha-problema.md` subida el 23-ago 23:52 |
| Solo 1 cuenta contribuyendo al historial | S1 (08-09) | no (S3 resuelto) | 4 cuentas en el historial |
| `docs/aspectos.md` sin enlaces desde las filas a los escenarios | S2 (16-ago) | no (S3 resuelto) | Tabla ADD con enlaces a EC y ADR |
| Restricciones sin categorías organizativas ni legales | S2 (16-ago) | no (S3 resuelto) | Categorías completas en arc42 §2 |
| Esqueleto ejecutable prometido en ADR-0001 y no entregado al cierre | S3 | parcial: entró 2 h después del cierre (`e976c92` 01:58) — no cuenta para S3 | Para S4: el esqueleto debe traer run en verde del pipeline; respetar los cierres |
| Matriz comparativa de estilos contra el árbol de utilidad ausente | S3 | no (resuelto) | §4.1 con filas por EC-01…EC-07 |
| ADR sin hipervínculo desde el escenario motivador EC-04 | S3 | no (resuelto) | EC-04 y EC-05 con enlaces al ADR |
| 2 commits posteriores al cierre (`88294cc` 01:00, `e976c92` 01:58) | S3 (cierre) | registrado | Entregar dentro del cierre de la actividad; lo tardío no califica |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público y con el nombre de la convención |
| Estructura mínima | Cumple | Las seis rutas presentes en `b65626e` |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md`, `0002-procesar-calificacion-de-forma-asincrona.md` |
| ADR aceptados sin reescribir | Cumple | 0001 marcado como reemplazado por 0002, sin reescrituras de contenido |
| `docs/ia.md` al día | Cumple | Actualizado en S3 (`aa14dca`) con aceptado/rechazado/justificación |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 4 cuentas para 4 integrantes |
| Pipeline en verde | No cumple | Sin código ni prueba al cierre; el esqueleto tardío trae prueba, pendiente de run en verde para S4 |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---|---:|---:|---:|---|
| Sebastian Canas Plata | scp1109 | 27 | — | — | Todo S1–S2, ADR 0003 y ficha del problema en S3; esqueleto tardío (01:58) |
| Josue David Ortega De Arco | josueacademico17-source | 9 | — | — | Desde la semana 3 |
| Maria Del Mar Restrepo Licona | Mariadelmar-restrepo | 1 | — | — | Primera aparición en S3 |
| Susana Marcela Rosales Castellar | SusanaRosales | 3 | — | — | Primera aparición en S3 |

## Preguntas abiertas para la sustentación

- ¿Por qué el esqueleto y el README del stack entraron 1 y 2 horas después del cierre de S3?
- ¿Cuándo entregarán el run en verde del pipeline sobre el esqueleto ya existente?
