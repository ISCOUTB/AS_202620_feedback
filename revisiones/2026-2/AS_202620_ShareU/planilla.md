# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | ShareU |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://shareu-backend.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `39508608eae4c1a56a5e4fc11a055bf6afb2c003` · 2026-09-28T19:56:57-05:00 | 9/10 | 4.6 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `39508608eae4c1a56a5e4fc11a055bf6afb2c003` · 2026-09-28T19:56:57-05:00 | 2/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | S1 | `(sin commits)` () | sin actividad | no aplica | si |
| 2 | S2 | `(sin commits)` () | sin actividad | no aplica | si |
| 3 | S3 | `master` `0bae184` · excepción docente | 7/9 | 4.1 | sí |
| 4 | S4 | `master` `0bae184` · excepción docente | 7/10 | 3.8 | sí |
| 5 | CORTE1 | `19ce719` (2026-09-07T22:41:14-05:00) | 5/12 | 2.7 | si |
| 6 | S6 | `c389364` (2026-09-13T23:21:08-05:00) | 7/8 | 4.5 (prelim.) | si |
| 7 | S7 | `29184bc` (2026-09-20T23:34:09-05:00) | 6/10 | 3.4 | si |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `332f67f` (2026-09-27T23:57:16-05:00) | 7/10 graduables (2 filas de despliegue pendientes) | 3.8 (provisional) | si |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Identificar el escenario oficialmente asignado y su línea base medida para S10. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Pipeline de la punta en rojo: [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458). | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Health de la URL declarada respondió 404; confirmar URL vigente y restablecer despliegue. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar ID y C4 en la tabla de trazabilidad; normalizar rutas de aspectos e IA. [docs/aspectos/aspectos.md:50–56](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/aspectos/aspectos.md#L50-L56) | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Versionar los archivos declarados ausentes o corregir documentos: Dockerfile, render.yaml, ADR 0005–0007 y prueba de contrato. [docs/evidencia/evidencia-s9.md:56–61](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L56-L61) | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Actualizar Next a una versión corregida tras revisar el aviso oficial: el registro de next 14.2.15 confirma advertencia de seguridad. [app/frontend/package.json:11–14](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/frontend/package.json#L11-L14) | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Ratificar ADR-0008/0009 y resolver marcadores documentales sin atribuir al equipo decisiones pendientes. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| El cruce búsqueda→interno de administración está corregido mediante fachada y prueba de fronteras. [app/busqueda/service.py:5–6](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/app/busqueda/service.py#L5-L6) | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se corrige el hallazgo preliminar de dependencias: no añadir paquetes no obliga a fallar; hay auditoría nueva del periodo y existencia contrastada en registros oficiales. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se excluye el hallazgo de convención sobre PDF por decisión docente; los ADR Markdown sí siguen la convención. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

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
| Publicar URL y health check y completar IaC, observabilidad, costos y ADR de plataforma. | S8 | sí | La estimación de costo, los logs y la métrica ya están; faltan URL, IaC y ADR de plataforma. |
| IaC y ADR de plataforma citados pero ausentes: README y arc42 §7 referencian `Dockerfile`, `render.yaml` y ADR 0005–0007 que no existen en el árbol. | S8 | sí | Versionar los archivos o retirar las referencias; la revisión definitiva no los encuentra en `332f67f` ni en la punta actual. |
| Pipeline de `master` en rojo en el hash calificado (`36379843854`, failure). | S8 | sí | Corregir el workflow para que el commit calificado quede en verde. |
| PDF fuera de la convención en `docs/adr/` reaparece en el estado calificado. | S8 | sí | `docs/adr/ShareU_Trazabilida.pdf`. |
| SonarCloud sin run del scanner ni Quality Gate público. | S6 | sí | Falta la evidencia auditable del §8. |
| La métrica de búsquedas de S8 tenía un cruce de frontera (`busqueda` importaba `administracion.metricas`); se corrigió en S9 con la fachada `administracion/service.py`. | S9 (prelim.) | no (resuelto en el periodo) | — |
| Sin dependencias añadidas en el periodo S9 que verificar en el registro oficial. | S9 (prelim.) | si | Añadir en el periodo las dependencias que se quieran respaldar, o dejar constancia de que no hubo. |
| Referencias a archivos inexistentes (`Dockerfile`, `render.yaml`, ADR 0005–0007, `tests/test_contrato.py`) y marcadores sin resolver en README, arc42 e `ia.md`. | S9 (prelim.) | si | Versionar los archivos o retirar las referencias; completar los marcadores. |
| CI de `master` en rojo en el hash revisado (`3950860`, run `36505758458`, failure). | S9 (prelim.) | si | Dejar el commit calificado en verde. |
| ADR-0008 y ADR-0009 en estado «Propuesto», pendientes de aprobación formal del equipo. | S9 (prelim.) | si | Aprobar los ADR y marcarlos como Aceptados. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon anónimo público de https://github.com/ISCOUTB/AS_202620_ShareU; organización y nombre conformes. |
| Estructura mínima presente | No cumple | [README.md:191–200](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md#L191-L200). Aspectos e IA existen en subcarpetas, no docs/aspectos.md y docs/ia.md. Desviación de ruta, no ausencia. |
| Estado calificado identificable | Cumple | origin/master 39508608eae4c1a56a5e4fc11a055bf6afb2c003, 2026-09-28T19:56:57-05:00; último ≤ cierre S9 y punta preliminar S10. |
| Nombres de ADR según la convención | Cumple | Los seis ADR Markdown 0001–0004, 0008 y 0009 siguen NNNN-kebab-case; [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:1–4](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L1-L4). Archivos PDF excluidos expresamente del criterio por decisión docente. |
| ADR aceptados no reescritos | Cumple | Historial de ADR leído: 0002/0003/0004/0008/0009 creados una vez; ADR-0001 solo movimientos de ruta sin edición de contenido. [docs/adr/0008-metrica-tras-interfaz-de-administracion.md:1–7](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/adr/0008-metrica-tras-interfaz-de-administracion.md#L1-L7) nuevo en 3950860. |
| docs/ia.md al día para la semana | Cumple | [docs/ia/ia.md:33](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/ia/ia.md#L33). Nueva entrada del periodo S9; ruta desviada evaluada por contenido. Aún no hay actividad adicional S10. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/tests.yml:22–32](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/.github/workflows/tests.yml#L22-L32). Consulta general Actions confirma [run 36505758458](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458) en el hash revisado, conclusión failure (2026-09-29T00:59:44Z). Sin run exitoso de scanner y Quality Gate de esta revisión acreditados. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del contrato sobre HEAD, docs y ejemplos sin credenciales identificadas; sin .env versionado; búsqueda histórica de patrones de claves privadas/tokens de alta confianza sin coincidencias. [docs/evidencia/evidencia-s9.md:75–80](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/docs/evidencia/evidencia-s9.md#L75-L80). Resultado acotado al barrido, no garantía absoluta. |
| Contribución de todos los integrantes | No verificado | 50 commits en cuatro grupos por identidad de correo; dos firmas se consolidan por coincidencia exacta, sin publicar correos. No se deduce la correspondencia completa con los cuatro integrantes solo por nombres de cuenta; validación docente pendiente, sin afirmar ausencia individual. |

## Contribución por integrante

Actualización agregada del 2026-10-06: 50 commits en cuatro grupos por identidad de correo; dos firmas se consolidan por coincidencia exacta, sin publicar correos. No se deduce la correspondencia completa con los cuatro integrantes solo por nombres de cuenta; validación docente pendiente, sin afirmar ausencia individual.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Dayana Narvaez Vasquez | daynarvaez | 19 | | | Dos identidades consolidadas (`Dayana` + `daynarvaez`) |
| Nicolas Ivan Hernandez Hernandez | Nicolas-HH | 11 | | | |
| Steven David Contreras Orozco | steven | 5 | | | |
| Luis Carlos Corredor Altamiranda | luiscorredor | 11 | | | Ya aparece en el historial (S8) |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Si se reinicia el backend y se pierden los contadores en memoria, ¿cómo distinguirán una mejora real de una métrica reiniciada?
- ¿Qué costo y cambio de plataforma requiere conservar SQLite y métricas entre reinicios o escalar a más de una réplica?
- ¿Qué cambiarían en el experimento después de comprobar que cinco documentos sintéticos se encuentran en dos interacciones, y cómo validarían que representa el uso real?
