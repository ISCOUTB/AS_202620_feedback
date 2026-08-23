# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ROUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Última revisión | 2026-08-23 (S1 `68b0b05` + S2 `14e6688`) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `68b0b05` · 2026-08-09T14:48:08-05:00 | 5/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `14e6688` · 2026-08-16T12:44:08-05:00 | 2/9 | no aplica | sí |
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
| `docs/ia.md` sin contenido real («Pendiente por documentar») | S1 (08-09) | Sí, en S2 | Registren cada uso de IA con qué se aceptó y qué se rechazó y por qué; si no han usado IA, declárenlo como entrada |
| `docs/aspectos.md` sin las 8 columnas ni ID, y sin enlaces a escenarios | S1 (08-09) | Sí, en S2 | Completen la tabla con las columnas del curso y enlacen cada escenario desde su fila |
| Tensiones de calidad del problema sin declarar | S1 (08-09) | Sí, en S2 | Enfrenten dos atributos de calidad en la ficha del problema (p. ej. tiempo de respuesta vs. costo) |
| Escenarios sin las seis partes y con medidas sin condición de carga | S2 (08-16) | Sí | Desglosen fuente, estímulo, artefacto, entorno, respuesta y medida con cifra, unidad y carga |
| C4 de contexto sin leyenda ni flechas etiquetadas (nodo del sistema duplicado) | S2 (08-16) | Sí | Etiqueten las relaciones, añadan leyenda y unifiquen el nodo ROUTB |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | `lsremote.txt:14`; público y con el nombre de la convención |
| Estructura mínima | Cumple | Las seis rutas presentes en `14e6688` |
| Convención de nombres de ADR | Cumple | Sin ADR todavía (solo `.gitkeep`) |
| ADR aceptados sin reescribir | Cumple | Sin ADR todavía |
| `docs/ia.md` al día | No cumple | Sin commits en el periodo S2; contenido de plantilla |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `git log -S` sin coincidencias |
| Contribución de todos los integrantes | Cumple | Los 4 integrantes constan en el historial (MKeinerrr con dos identidades consolidadas) |
| Pipeline en verde | No aplica todavía | Sin `.github/workflows`; se espera desde el segundo corte |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Keiner Enrique Mendivil Diaz | MKeinerrr | 21 (19 `correo omitido` + 2 `correo omitido`) | | | Dos identidades consolidadas |
| Diego Jose Baron Ruiz | diegobrr999-commits | 6 | | | Desde 13-ago |
| Julian David Manjarrez Guzman | juliandmanjarrez-tech | 3 | | | Desde 13-ago |
| Junior Jose Orozco Atencio | junior14700 | 2 | | | Desde 07-ago |

## Preguntas abiertas para la sustentación

- ¿Los 4 integrantes tenían acceso al repositorio desde la semana 1? (sin API no se listan colaboradores)
- ¿Por qué la sección 10 de arc42 quedó vacía si los escenarios se redactaron en la sección 1?
