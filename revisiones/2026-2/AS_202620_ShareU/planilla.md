# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ShareU |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-03 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `8886d4e` · 2026-08-09T22:03:52-05:00 | 4/9 | no aplica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `aa0659c` · 2026-08-16T22:47:16-05:00 | 2/9 | no aplica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `0833272` · 2026-08-23T22:46:30-05:00 | 6/9 | no se publica | sí |
| 4 | S4 | `27e1190` (2026-08-30T15:22:02-05:00) | 0/10 | 1.0 | si |
| 5 | Primer corte · reto de línea base | HEAD `7c027f0` (sin etiqueta) | 0/12 | subtotal técnico preliminar 0,00/4,00; sustentación pendiente | revisión manual preliminar 2026-09-03 |
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
| Estructura sin montar: `docs/arc42/` (la plantilla está suelta en `docs/`), `docs/adr/` y `docs/c4/` inexistentes | S1 (08-09) | Parcial: `docs/adr/` ya existe; siguen faltando `docs/arc42/` y `docs/c4/` | Muevan la plantilla a `docs/arc42/` y creen `docs/c4/` |
| `docs/aspectos.md` sin la tabla de 8 columnas ni ID | S1 (08-09) | Sí, en S3 | Armen la tabla del curso y enlacen cada escenario desde su fila |
| Luis Carlos Corredor Altamiranda sin aparición en el historial | S1 (08-09) | Sí (3 identidades para 4 integrantes en S3) | El integrante debe contribuir con su cuenta para que la contribución individual sea verificable |
| `docs/ia.md` sin registro de usos ni de lo rechazado | S1 (08-09) | Parcial: dos entradas de S3, sin columna de rechazados y «pendientes de revisión» | Completen la columna de qué se rechazó y por qué |
| Problema del proyecto cambiado entre semanas (EncuentraUTB → ShareU) | S2 (16-ago) | Sin evidencia nueva en S3 | Revisar que toda la documentación hable del mismo problema para el corte 1 |
| Tensiones de calidad sin declarar | S1 (08-09) | Sin evidencia nueva en S3 | Enfrenten dos atributos de calidad en la ficha del problema |
| README con la sección de arranque vacía y sin manifest de dependencias | S3 (cierre) | Sí | Documentar el comando único (p. ej. `uvicorn app.main:app`) y añadir `requirements.txt` |
| ADR no enlazado desde `aspectos.md` ni desde el escenario | S3 (cierre) | Sí | Enlazar el ADR desde la fila del aspecto y desde el escenario de usabilidad |
| Sin pipeline ni evidencia del verde | S3 (cierre) | Sí | Añadir workflow con la prueba y el run en verde |
| Sin árbol de utilidad formal (la matriz compara contra el escenario de aspectos) | S3 (cierre) | Sí | Documentar el árbol de utilidad con sus escenarios para el corte 1 |
| Verificar contenido de docs/arc42/arc42.md (secciones 1-6, 9, 10, 12) | S4 | si | |
| Verificar coherencia C4 nivel 1/2 y correspondencia con código | S4 | si | |
| Verificar recorrido del corte vertical en app/ | S4 | si | |
| Verificar comando de arranque en README.md | S4 | si | |
| Obtener run de CI en verde para tests/test_busqueda.py | S4 | si | |
| Verificar fila de docs/aspectos/aspectos.md | S4 | si | |
| Verificar contenido de docs/adr/0001-estilo-arquitectonico.md | S4 | si | |
| Verificar docs/ia.md | S4 | si | |
| Incorporar a los integrantes faltantes al historial | S4 | si | |
| Responder al reto de restricción asignada | S5 | si | |
| Crear ADR del reto con alternativas y decisión | S5 | si | |
| Implementar el cambio y probarlo | S5 | si | |
| Medir contra umbral | S5 | si | |
| Subir PDF de dos páginas | S5 | si | |
| Crear etiqueta corte-1 | S5 | si | |
| Evidenciar pipeline en verde | S5 | si | |
| Completar docs/ia.md y docs/aspectos.md | S5 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público y con el nombre de la convención |
| Estructura mínima | Cumple | Faltan `docs/arc42/` (plantilla en `docs/`) y `docs/c4/` en `0833272` |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | Cumple | Creación y ajuste el mismo día, antes del cierre |
| `docs/ia.md` al día | No cumple | Entradas de S3 sin columna de rechazados |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `log -S` sin coincidencias |
| Contribución de todos los integrantes | No cumple | 3 de 4 personas en el historial (falta Luis Carlos Corredor) |
| Pipeline en verde | No verificado | Sin `.github/workflows`; prueba sin evidencia de ejecución |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Dayana Narvaez Vasquez | daynarvaez | 19 | | | Toda la S3: ADR, esqueleto, README, ia.md |
| Nicolas Ivan Hernandez Hernandez | Nicolas-HH | 8 | | | S1 y S2 |
| Steven David Contreras Orozco | steven | 1 | | | Solo 10-ago (README) |
| Luis Carlos Corredor Altamiranda | sin cuenta observada | 0 | | | No aparece en el historial |

## Preguntas abiertas para la sustentación

- ¿Por qué cambió el problema del proyecto entre la semana 1 (EncuentraUTB) y la semana 2 (ShareU)?
- ¿Luis Carlos Corredor Altamiranda tiene acceso al repositorio y con qué cuenta contribuirá?
- ¿Por qué la sección «Esqueleto ejecutable — arranque» del README quedó sin el comando, y dónde está el manifest de dependencias de FastAPI?
