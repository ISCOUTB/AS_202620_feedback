# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Calificación automática |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S1 `4f6f568` + S2 `d4302f4`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `4f6f568` · 2026-08-09T13:16:43-05:00 | 7/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d4302f4` · 2026-08-16T23:17:26-05:00 | 7/9 | no aplica | sí |
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
| `docs/adr` versionado como blob vacío, no como directorio | S1 (08-09) | Sí, en S2 | Reemplazar por directorio real con `.gitkeep` (en la S3 ya recibe `0001.md`) |
| Ficha del problema fuera del repositorio (se cita un «Informe Inicial» de Moodle) | S1 (08-09) | Sí, en S2 | Subir la ficha al repositorio para que la entrega sea defendible |
| Solo 1 cuenta contribuyendo al historial | S1 (08-09) | Sí, en S2 | Los 4 integrantes deben contribuir con su cuenta para que la contribución individual sea verificable |
| `docs/aspectos.md` sin enlaces desde las filas a los escenarios del arc42 | S2 (16-ago) | Sí | Enlazar cada escenario desde la fila de su aspecto en la tabla de trazabilidad |
| Restricciones sin categorías organizativas ni legales | S2 (16-ago) | Sí | Completar la clasificación con los tres tipos del curso |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `lsremote.txt:17`; público y con el nombre de la convención |
| Estructura mínima | Cumple | Presente en `d4302f4`; `docs/adr` es blob vacío (desviación de montaje) |
| Convención de nombres de ADR | Cumple | Sin ADR al cierre de S2; el primero (`docs/adr/0001.md`, 22-ago) no sigue `NNNN-titulo-en-kebab-case.md` — revisar en S3 |
| ADR aceptados sin reescribir | Cumple | Sin ADR al cierre de S2 |
| `docs/ia.md` al día | Cumple | Entradas 1 y 2 con aceptado/rechazado/justificación |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `git log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 1 de 4 personas hasta el cierre de S2 |
| Pipeline en verde | No aplica todavía | Sin `.github/workflows`; se espera desde el segundo corte |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Sebastian Canas Plata | scp1109 | 16 (hasta cierre S2) | | | Todo S1 y S2 |
| Josue David Ortega De Arco | josueacademico17-source | 6 (todos después del cierre S2, 22-ago) | | | Aparece en semana 3 |
| Maria Del Mar Restrepo Licona | sin cuenta observada | 0 | | | No aparece en el historial |
| Susana Marcela Rosales Castellar | sin cuenta observada | 0 | | | No aparece en el historial |

## Preguntas abiertas para la sustentación

- ¿Dónde está la ficha del problema (el «Informe Inicial» citado)? No está en el repositorio.
- ¿Con qué cuentas contribuirán María Restrepo y Susana Rosales?
