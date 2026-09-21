# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ShareU |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Ultima revision | 2026-09-21 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | S1 | `(sin commits)` () | sin actividad | no aplica | si |
| 2 | S2 | `(sin commits)` () | sin actividad | no aplica | si |
| 3 | S3 | `master` `0bae184` · excepción docente | 7/9 | 4.1 | sí |
| 4 | S4 | `master` `0bae184` · excepción docente | 7/10 | 3.8 | sí |
| 5 | CORTE1 | `19ce719` (2026-09-07T22:41:14-05:00) | 5/12 | 2.7 | si |
| 6 | S6 | `c389364` (2026-09-13T23:21:08-05:00) | 7/8 | 4.5 (prelim.) | si |
| 7 | S7 | `29184bc` (2026-09-20T23:34:09-05:00) | 5/10 | 3.0 | si |
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
| Falta matriz de capas, hexagonal y monolito modular contra el árbol de utilidad | S3 · revisión excepcional | Sí | Construir la comparación explícita con los escenarios y sus trade-offs. |
| El escenario de usabilidad no enlaza directamente el ADR 0001 | S3 · revisión excepcional | Sí | Añadir el enlace desde el escenario hacia el ADR que motiva. |
| No hay C4 de contexto: ambos archivos `.mmd` son diagramas de contenedores | S4 · revisión excepcional | Sí | Crear el C4 nivel 1 y conservar el nivel 2 de contenedores. |
| Trazabilidad en ruta desviada y sin las ocho columnas | S4 · revisión excepcional | Sí | Mover o exponer `docs/aspectos.md` y completar ID, C4 y el resto de la cadena. |
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
| Responder al reto de restricción asignada | S5 | si | No hay diagnóstico ni ADR nuevo en el árbol del corte 1; sigue pendiente. |
| Crear ADR del reto con alternativas y decisión | S5 | si | Solo existe el ADR 0001 de agosto; falta el ADR del reto. |
| Implementar el cambio y probarlo | S5 | si | Ningún commit entre S4 y la etiqueta toca app/; sin cambio de código. |
| Medir contra umbral | S5 | si | No hay archivo de medición ni procedimiento en el árbol. |
| Subir PDF de dos páginas | S5 | si | No verificable desde el repositorio; depende de Moodle. |
| Crear etiqueta corte-1 | S5 | si | Existe, pero apunta a un commit posterior al cierre (a5d08c1, +7h): corregir para el próximo corte. |
| Evidenciar pipeline en verde | S5 | si | 0 runs de CI en la vida del repositorio (actions/runs total_count=0). |
| Completar docs/ia.md y docs/aspectos.md | S5 | si | Ambos siguen fechados en S3-S4; sin entradas del reto de este corte. |
| Correcciones.md debe llamarse exactamente correcciones.md. | S5 | si | |
| Pipeline de CI debe pasar en el hash calificado. | S5 | si | |
| Trazabilidad de aspectos debe ser navegable. | S5 | si | |
| PDFs fuera de docs/adr. | S5 | si | |
| Evidencia de SonarCloud pendiente. | S5 | si | |
| Contrato de API en OpenAPI o AsyncAPI versionado en el repositorio | S7 | si | |
| Routes y esquemas de datos dentro del contrato | S7 | si | |
| Prueba de contrato presente y ejecutada por el workflow | S7 | si | |
| Evidencia de que la prueba falla ante un cambio incompatible | S7 | si | |
| ADR de estrategia de integración (síncrona o asíncrona) con alternativa descartada | S7 | si | |
| Etiquetado de protocolo y formato en cada flecha del C4 nivel 2 | S7 | si | |
| Columnas ID y C4 en la tabla de aspectos | S7 | si | |
| Paso del scanner de SonarCloud en CI y URL pública del Quality Gate | S7 | si | |
| Puntos de la revisión del corte 1 aún sin resolver, según correcciones.md (reto/restricción asignada y etiqueta) | S7 | si | |
| 0bae184 (2026-09-14T15:26:52-05:00, posterior al cierre 2026-09-14T05:00:00Z): elimina docs/adr/ShareU_Trazabilidad.pdf; es exactamente el diff respecto del estado calificado c389364. | S6 | no (resuelto tarde) | — |
| C4 nivel 3 del reajuste de límites de Calificaciones (ADR 0003 sigue en estado Propuesto). | S6 | si | |
| Columnas ID y C4 en docs/aspectos/aspectos.md para completar las ocho del contrato. | S6 | si | |
| Paso del scanner de SonarCloud en el workflow y URL pública del análisis con su Quality Gate. | S6 | si | |
| Puntos 1 y 2 de correcciones.md: ADR/diagnóstico de la restricción del corte 1 y definición del mecanismo de cierre, aún sin resolver en el repositorio. | S6 | si | |
| Implementación del plan de corrección V1 (tabla y servicio propios de calificaciones). | S6 | si | |
| La triplicación del árbol (AS_202620_ShareU-master/, shareu_base/) señalada en la revisión de semana 5 ya no aparece en el árbol de 29184bc, según se documenta en correcciones.md. | S7 | no (resuelto tarde) | — |
| Los commits 0bae184 (2026-09-14, borrado de docs/adr/ShareU_Trazabilidad.pdf) y f189703 (2026-09-20, Update requirements.in) corrigen entregas anteriores sobre trazabilidad y versiones de dependencias. | S7 | no (resuelto tarde) | — |
| Prueba de contrato en el pipeline y evidencia de que falla ante un cambio incompatible (criterios 5 a 7 de la ficha). | S7 | si | |
| Correspondencia contrato-código sin evidencia citable de los routers. | S7 | si | |
| C4 nivel 2 con protocolo y formato en cada flecha. | S7 | si | |
| Tabla de aspectos con las ocho columnas del contrato (faltan ID y C4). | S7 | si | |
| SonarCloud auditable: paso del scanner en el workflow y URL pública del análisis con Quality Gate para el hash revisado. | S7 | si | |
| Carpeta docs/adr/ con un PDF ajeno a la convención de nombres. | S7 | si | |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Público y con el nombre de la convención |
| Estructura mínima | Cumple | Faltan `docs/arc42/` (plantilla en `docs/`) y `docs/c4/` en `0833272` |
| Convención de nombres de ADR | Cumple | `0001-estilo-arquitectonico.md` |
| ADR aceptados sin reescribir | Cumple | Creación y ajuste el mismo día, antes del cierre |
| `docs/ia.md` al día | No cumple | Entradas de S3 sin columna de rechazados |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 y `log -S` sin coincidencias |
| Etiqueta corte-1 (corte 1) | No cumple | Existe pero apunta a un commit posterior al cierre (`a5d08c1`, +7h); fallback admisible `1728495` |
| Contribución de todos los integrantes | Cumple | Corte 1 (post-cierre, 2026-09-07): los 4 integrantes tienen commits propios (Dayana 6, luiscorredor 2, Nicolas-HH 1, steven 1) |
| Pipeline en verde | No cumple | Sin `.github/workflows`; prueba sin evidencia de ejecución |

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
