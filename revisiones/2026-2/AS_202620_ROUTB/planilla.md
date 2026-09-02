# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ROUTB |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ROUTB` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-02 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `68b0b05` · 2026-08-09T14:48:08-05:00 | 5/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `14e6688` · 2026-08-16T12:44:08-05:00 | 2/9 | no aplica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `1ed002b` · 2026-08-23T20:31:54-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `83b8c5e` (2026-08-30T19:33:15-05:00) | 10/10 | 5.0 | si |
| 5 | CORTE1 | `83b8c5e` (2026-08-30T19:33:15-05:00) | 0/12 | no aplica | si |
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
| `docs/ia.md` sin contenido real | S1 (08-09) | no (S3 resuelto) | Ya registra semana 3 con aceptado/rechazado/justificación |
| `docs/aspectos.md` sin 8 columnas ni enlaces | S1 (08-09) | no (S3 resuelto) | Ya tiene la tabla y enlaza el ADR |
| Tensiones de calidad del problema sin declarar | S1 (08-09) | revisar en corte 1 | Enfrentar dos atributos de calidad en la ficha del problema |
| Escenarios sin las seis partes y con medidas sin condición de carga | S2 (08-16) | no (S3 resuelto) | Tabla 10.2 con seis partes y cifras |
| C4 de contexto sin leyenda ni flechas etiquetadas | S2 (08-16) | sí (verificar en S3) | Etiquetar relaciones y añadir leyenda |
| ADR sin enlace desde el escenario motivador (10.2) | S3 | sí | Enlazar la decisión desde el escenario de calidad que la motiva |
| README sin comando único de arranque (multi-paso) | S3 | sí | Documentar un solo comando con requisitos previos |
| Sin workflow ni evidencia de prueba en verde | S3 | sí | Añadir `.github/workflows/` con `pytest` y aportar el run |
| Completar arc42 secciones 7, 8 y 11 | S4 | si | |
| Completar filas 1 y 3 de docs/aspectos.md | S4 | si | |
| Integrar SonarCloud al pipeline | S4 | si | |
| Enlazar ADR 0001 con commit de implementación | S4 | si | |
| Registrar medición de línea base | S4 | si | |
| Crear etiqueta corte-1 | S5 | si | |
| Diagnóstico y línea base del reto | S5 | si | |
| ADR del reto | S5 | si | |
| Implementación y pruebas | S5 | si | |
| Medición contra umbral | S5 | si | |
| Completar celdas vacías de docs/aspectos.md | S5 | si | |
| Configurar SonarCloud | S5 | si | |
| Registrar uso de IA de la semana 5 | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público y con el nombre de la convención |
| Estructura mínima | Cumple | Las seis rutas presentes en `1ed002b` |
| Convención de nombres de ADR | Cumple | `0001-usar-monolito-modular.md` con título que enuncia la decisión |
| ADR aceptados sin reescribir | Cumple | 2 commits de construcción en S3, sin reescrituras posteriores |
| `docs/ia.md` al día | Cumple | Semana 3 registrada con aceptado/rechazado/justificación |
| Sin credenciales en el repositorio ni en el historial | Cumple | git grep y `.env` sin coincidencias |
| Contribución de todos los integrantes | Cumple | 4 personas para 4 integrantes (MKeinerrr consolidado) |
| Pipeline en verde | No cumple | Sin `.github/workflows/`; se espera desde el segundo corte |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Keiner Enrique Mendivil Diaz | MKeinerrr | 22 (20+2, dos identidades) | | | Consolidado; autor de la entrega S3 |
| Diego Jose Baron Ruiz | diegobrr999-commits | 6 | | | C4 en S2 |
| Julian David Manjarrez Guzman | juliandmanjarrez-tech | 3 | | | C4 en S2 |
| Junior Jose Orozco Atencio | junior14700 | 2 | | | Restricciones en S2 |

## Preguntas abiertas para la sustentación

- ¿Los 4 integrantes tenían acceso al repositorio desde la semana 1? (sin API no se listan colaboradores)
- ¿Quién ejecutó `pytest` en verde y pueden aportar la evidencia del run?
- ¿El C4 de contexto quedó con leyenda y flechas etiquetadas (pendiente de S2)?
