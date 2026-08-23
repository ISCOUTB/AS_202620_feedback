# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ShareU |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S1 `8886d4e` + S2 `aa0659c`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `8886d4e` · 2026-08-09T22:03:52-05:00 | 4/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `aa0659c` · 2026-08-16T22:47:16-05:00 | 2/9 | no aplica | sí |
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
| Estructura sin montar: `docs/arc42/` (la plantilla está suelta en `docs/`), `docs/adr/` y `docs/c4/` inexistentes | S1 (08-09) | Sí, en S2 | Muevan la plantilla a `docs/arc42/` y creen `docs/adr/` y `docs/c4/` |
| `docs/aspectos.md` sin la tabla de 8 columnas ni ID | S1 (08-09) | Sí, en S2 | Armen la tabla del curso y enlacen cada escenario desde su fila |
| Luis Carlos Corredor Altamiranda sin aparición en el historial | S1 (08-09) | Sí, en S2 | El integrante debe contribuir con su cuenta para que la contribución individual sea verificable |
| `docs/ia.md` sin registro de usos ni de lo rechazado (anuncia una tabla que no tiene entradas) | S1 (08-09) | Sí, en S2 | Registren cada uso con qué se aceptó y qué se rechazó y por qué |
| Problema del proyecto cambiado entre semanas (EncuentraUTB → ShareU) | S2 (16-ago) | Sí | Revisar que toda la documentación hable del mismo problema para el corte 1 |
| Tensiones de calidad sin declarar | S1 (08-09) | Sí, en S2 | Enfrenten dos atributos de calidad en la ficha del problema |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `lsremote.txt:16`; público y con el nombre de la convención |
| Estructura mínima | No cumple | `docs/arc42/` ausente (plantilla en `docs/`), `docs/adr/` y `docs/c4/` inexistentes en `aa0659c` |
| Convención de nombres de ADR | Cumple | Sin ADR (no existe `docs/adr/`) |
| ADR aceptados sin reescribir | Cumple | Sin ADR |
| `docs/ia.md` al día | No cumple | Sin registro de usos ni rechazos |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `git log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 3 de 4 personas en el historial (falta Luis Carlos Corredor) |
| Pipeline en verde | No aplica todavía | Sin `.github/workflows`; se espera desde el segundo corte |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Dayana Narvaez Vasquez | daynarvaez | 12 | | | Toda la S1 y parte de la S2 |
| Nicolas Ivan Hernandez Hernandez | Nicolas-HH | 8 | | | Desde 10-ago |
| Steven David Contreras Orozco | steven | 1 | | | Solo 10-ago (README) |
| Luis Carlos Corredor Altamiranda | sin cuenta observada | 0 | | | No aparece en el historial |

## Preguntas abiertas para la sustentación

- ¿Por qué cambió el problema del proyecto entre la semana 1 (EncuentraUTB) y la semana 2 (ShareU)?
- ¿Luis Carlos Corredor Altamiranda tiene acceso al repositorio y con qué cuenta contribuirá?
