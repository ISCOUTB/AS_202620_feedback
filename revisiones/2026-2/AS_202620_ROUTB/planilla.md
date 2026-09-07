# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ROUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Integrantes y su usuario de GitHub | Diego Jose Baron Ruiz (`diegobrr999-commits`) · Julian David Manjarrez Guzman (`juliandmanjarrez-tech`) · Keiner Enrique Mendivil Diaz (`MKeinerrr`, dos correos) · Junior Jose Orozco Atencio (`junior14700`) |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-07 (revisión definitiva post-cierre) |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `68b0b05` · 2026-08-09T14:48:08-05:00 | 5/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `14e6688` · 2026-08-16T12:44:08-05:00 | 2/9 | no aplica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `1ed002b` · 2026-08-23T20:31:54-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `83b8c5e` (2026-08-30T19:33:15-05:00) | 10/10 | 5.0 | si |
| 5 | Primer corte · reto de línea base | `corte-1` → `493efdb` (2026-09-07T01:11:13Z) | 10/12 | subtotal técnico 3,20/4,00; sustentación pendiente | revisión definitiva post-cierre 2026-09-07 |
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
| `docs/ia.md` sin contenido real | S1 (08-09) | no (S3 resuelto; en S5 hay entrada específica del reto) | Ya registra por semana con aceptado/rechazado/justificación |
| `docs/aspectos.md` sin 8 columnas ni enlaces | S1 (08-09) | no (S3 resuelto; en S5 la fila 1 llega hasta la evidencia del reto) | Ya tiene la tabla y enlaza el ADR |
| Tensiones de calidad del problema sin declarar | S1 (08-09) | sin verificar en esta pasada | Revisar en el próximo corte |
| Escenarios sin las seis partes y con medidas sin condición de carga | S2 (08-16) | no (S3 resuelto) | Tabla con seis partes y cifras |
| C4 de contexto sin leyenda ni flechas etiquetadas | S2 (08-16) | sin verificar en esta pasada | Revisar en el próximo corte |
| ADR sin enlace desde el escenario motivador (10.2) | S3 | no (en S5, `docs/aspectos.md` enlaza los ADR desde cada fila) | — |
| README sin comando único de arranque (multi-paso) | S3 | no (resuelto: `uvicorn app.main:app --reload` y `flutter run`) | — |
| Sin workflow ni evidencia de prueba en verde | S3 | no (resuelto: `.github/workflows/ci.yml`, runs verdes) | — |
| Completar arc42 secciones 7, 8 y 11 | S4 | sin verificar en esta pasada | Revisar en el próximo corte |
| Completar filas 1 y 3 de docs/aspectos.md | S4 | no (resuelto en S5) | — |
| Integrar SonarCloud al pipeline | S4 | parcial: **integrado pero consistentemente en rojo** desde el 05/09 | Corregir los hallazgos de SonarCloud; no basta con tener el workflow, tiene que pasar |
| Enlazar ADR 0001 con commit de implementación | S4 | sin verificar en esta pasada | — |
| Registrar medición de línea base | S4 | no (resuelto en S5) | — |
| Crear etiqueta corte-1 | S5 | no (creada, antes del cierre) | — |
| Diagnóstico y línea base del reto | S5 | no (resuelto, aunque sin confirmar que responda a la restricción asignada) | Confirmar en la sustentación cuál fue la restricción individual asignada |
| ADR del reto | S5 | no (resuelto, nivel competente) | Añadir criterio de reconsideración y costo de reversión |
| Implementación y pruebas | S5 | no (resuelto) | — |
| Medición contra umbral | S5 | no (resuelto) | — |
| Completar celdas vacías de docs/aspectos.md | S5 | no (resuelto) | — |
| Configurar SonarCloud | S5 | sí, sigue en rojo | Resolver los hallazgos de SonarCloud antes del próximo corte |
| Registrar uso de IA de la semana 5 | S5 | no (resuelto) | — |

## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público y con el nombre de la convención |
| Estructura mínima | Cumple | Las seis rutas presentes en `corte-1` |
| Convención de nombres de ADR | Cumple | 0001, 0002, 0003 con título de la decisión en kebab-case |
| ADR aceptados sin reescribir | Cumple | Sin reescrituras detectadas |
| `docs/ia.md` al día | Cumple | Entrada de S5 fechada 05/09 |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep sin secretos reales; sin `.env` |
| Contribución de todos los integrantes | Cumple | 4 personas para 4 integrantes (MKeinerrr consolidado); muy concentrada en MKeinerrr |
| Pipeline en verde | Cumple en pruebas / **No cumple en análisis estático** | `Backend CI`/`CI ROUTB` en verde, incluido el commit de la etiqueta; `SonarCloud` en `failure` en todas las ejecuciones vistas |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Keiner Enrique Mendivil Diaz | `MKeinerrr` | 31+2 (dos correos, consolidado) | | | Autor de casi todo el reto S5 |
| Diego Jose Baron Ruiz | `diegobrr999-commits` | 6 | | | C4 en S2 |
| Julian David Manjarrez Guzman | `juliandmanjarrez-tech` | 3 | | | C4 en S2 |
| Junior Jose Orozco Atencio | `junior14700` | 2 | | | Restricciones en S2 |

## Preguntas abiertas para la sustentación

- ¿Cuál fue exactamente la restricción individual asignada al equipo?
- ¿Por qué SonarCloud nunca pasó en verde y qué plan tienen para resolverlo?
- ¿Cómo van a repartir mejor la contribución? Casi todo el reto S5 lo hizo una sola persona.
