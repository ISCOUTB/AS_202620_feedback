# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo a lo largo del semestre.

## Identificación

| | |
|---|---|
| Equipo | XALD |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Xavier Yesid Garcia Diaz (xaviergarciadiaz20-commits) · Dilan Joan Gonzalez Bejarano (dilanbejarano011) · Luis Estheban Lozano Colmenares (colmenares2007-crypto) · Axel Jair Ruiz Bolano (axeljruiz717-hash) — correspondencias por los correos de los commits (nombres explícitos), por confirmar con el docente; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://xald-backend.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-06 · S9 definitiva / S10 preliminar |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `9236ff97218b632eeb9a1910f6083968e2c22909` · 2026-10-04T23:53:02-05:00 | 7/10 | 3.8 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `9236ff97218b632eeb9a1910f6083968e2c22909` · 2026-10-04T23:53:02-05:00 | 3/12 de comprobación (sin PDF) | Pendiente: rúbrica de 5 criterios, ver [S10](semana-10-corte2.md); sustentación docente | sí, avance 2026-10-06 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `bf81545` · 2026-08-08T13:39:21-05:00 | 5/9 | 3.2 (propuesta) | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `8c37887` · 2026-08-16T13:45:27-05:00 | 1/9 | 1.4 (propuesta) | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `dc38992` · 2026-08-23T22:07:19-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `0205e44` (2026-08-30T23:12:03-05:00) | 4/10 | 2.6 | si |
| 5 | CORTE1 | `9bf16cf` (2026-09-09T10:07:09-05:00) | 8/12 | 3.7 | si |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | `55993cf` (2026-09-13T22:06:22-05:00) | 8/8 | 5.0 (prelim.) | sí |
| 7 | S7 | `62a0d15` (2026-09-20T23:25:16-05:00) | 9/10 | 4.6 (propuesta) | sí (auditoría local) |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `f90f28d3` (2026-09-27T21:56:48-05:00) | 10/10 | 5.0 (propuesta; 2 filas de despliegue pendientes) | sí (definitiva) |
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
| Repetir ESC-05 con conflictos realmente simultáneos, verificar estado ganador completo y distinguir aceptación HTTP de persistencia sin pérdidas. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Precisar cuál código fue generado en S9: el handler LWW no cambia desde S8; sí cambian pruebas, medidor y documentación. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Completar en docs/ia.md qué se corrigió del periodo, o declarar honestamente que no se requirió corrección. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Cambiar enlaces de aspectos desde experimental al estado revisable y reconciliar Room/AES/TLS con el MVP real. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Resolver o priorizar H-1…H-5 de la auditoría; no presentar la auditoría como corrección ya implementada. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Integrar SonarCloud con scanner, run y Quality Gate públicos; retirar __pycache__ versionado. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Identificar la consigna operativa S10 y medir línea base en el despliegue; documentar estabilidad y recuperación tras el primer timeout. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Antes de incorporar Gemini, aportar conjunto de evaluación con resultados, costo y latencia; el ADR actual solo aplaza la integración. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Hay nueva prueba dirigida al defecto y procedimiento de mutación: [backend/tests/test_lww.py:5–8](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/tests/test_lww.py#L5-L8) y [docs/adr/0011-resolucion-conflictos-lww.md:24](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L24). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La auditoría y la verificación de dependencias S9 ya están presentes: [docs/EVIDENCIA-S9.md:1–67](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/EVIDENCIA-S9.md#L1-L67). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La decisión sobre Gemini ya está explicitada para este corte y coincide con el mock: [docs/adr/0012-aplazamiento-integracion-gemini.md:17–31](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0012-aplazamiento-integracion-gemini.md#L17-L31). | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| El pipeline sí corre sobre master y el hash actual pasa: [run](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606); no cierra SonarCloud. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| La planilla antigua decía sin URL, pero el README declara el servicio y health públicos: [README.md:8–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L8-L11). Salud actual confirmada por HTTP 200 en la segunda consulta; no se probó flujo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Ficha del problema sin usuarios, sin alcance y sin tensiones de calidad enfrentadas | S1 | sí | completar la ficha |
| Restos de edición de herramientas de IA («```[cite: 1]») en `docs/aspectos.md` | S1 | sí | limpiar el archivo |
| Restricciones sin clase legal y con decisiones presentadas como restricciones | S2 | sí | clasificar técnicas/organizativas/legales con origen |
| Escenarios de calidad de seis partes y árbol de utilidad ausentes del repositorio | S2 | sí | subirlos; sin árbol no se puede anclar la matriz comparativa |
| Nombres de ADR fuera de convención (`ADR-NNN.md`) | S2 | sí | renombrar a `NNNN-titulo-en-kebab-case.md` |
| `aspectos.md` con celdas ADR sin enlace y sin referencia al ADR-006 | S3 | sí | enlazar de verdad y añadir la fila del estilo |
| `docs/ia.md` sin entradas del periodo S3 | S3 | sí | registrar el uso de IA de esta semana con rechazados y motivo |
| Artefactos de build versionados (`.gradle/`, `build/`, `XALDAPP/.idea/`, `local.properties`) | S3 | sí | sacar del repo y completar `.gitignore` en la raíz |
| Pruebas del esqueleto sin evidencia de verde (sin CI ni run) | S3 | sí | montar pipeline o aportar el run de `gradlew test` |
| Verificar secciones 3-6, 9, 10 y glosario del arc42 | S4 | si | |
| Confirmar que Cortevertical.kt atraviesa persistencia | S4 | si | |
| Implementar o justificar Backend XALD | S4 | si | |
| Añadir SonarCloud al pipeline | S4 | si | |
| Completar ADR con opciones evaluadas y trazabilidad | S4 | si | |
| Confirmar o crear la etiqueta corte-1 sobre el commit evaluado. | S5 | no (resuelto) | el equipo creó la etiqueta el 2026-09-06, antes del cierre |
| Completar las celdas Pendiente de docs/aspectos.md. | S5 | sí | 4 de 5 filas siguen con Código/Pruebas/Evidencia en "Pendiente" en el estado etiquetado |
| Añadir trazabilidad (requisito, C4, commit, pruebas) a los ADR. | S5 | no (resuelto) | los seis ADR ya tienen sección de trazabilidad y opciones evaluadas en el estado etiquetado |
| Configurar análisis estático SonarCloud en el pipeline. | S5 | parcial | commits del 2026-09-06 corrigen hallazgos típicos de SonarCloud y docs/ia.md declara "Quality Gate Passed"; no se pudo confirmar en el dashboard |
| Entregar el PDF con diagnóstico, decisión, cambio, medición y trazabilidad. | S5 | sí | no hay PDF versionado; falta además identificar la restricción nueva asignada, con línea base y medición posterior |
| El pipeline de CI no dispara en `master` (rama por defecto), solo en `experimental`/`main`; el estado etiquetado no tiene un run propio | S5 (detectado en revisión definitiva) | sí | ajustar `on.push.branches` en `ci.yml` para incluir `master`, o cambiar la rama por defecto |
| La prueba "corte vertical" (`Entornotest.kt`) es un `assertTrue(true)` trivial, no demuestra los 5 módulos interactuando | S5 (detectado en revisión definitiva) | sí | agregar una prueba que ejercite el flujo real de datos entre módulos |
| correcciones-feedback-XALD.md renombrado a correcciones.md en 43b8e35 (2026-09-08T10:25:05-05:00), posterior al cierre. | S5 | no (resuelto tarde) | — |
| Workflow de CI ajustado a la rama master en 9bf16cf (2026-09-09T10:07:09-05:00), posterior al cierre; run success 2026-09-09T15:07:12Z. | S5 | no (resuelto tarde) | — |
| Completar CÓDIGO, PRUEBAS y EVIDENCIA en docs/aspectos.md con enlaces al estado calificado. | S5 | si | |
| Incorporar análisis estático SonarCloud. | S5 | si | |
| Verificar entrega del PDF en Moodle y sustentación. | S5 | si | |
| 43b8e35 (2026-09-08) renombra correcciones-feedback-XALD.md a correcciones.md, cerrando la fila 2 después del cierre | S5 | no (resuelto tarde) | — |
| 9bf16cf (2026-09-09) ajusta CI a la rama master, cerrando el pipeline transversal después del cierre | S5 | no (resuelto tarde) | — |
| docs/aspectos.md con celdas Pendiente en Código/Pruebas/Evidencia para A-02 a A-05 | S5 | si | |
| Enlaces de aspectos.md a rama experimental en lugar de master | S5 | si | |
| Completitud de arc42 (12 secciones) sin verificar | S5 | si | |
| PDF en Moodle y sustentación pendientes de confirmación docente | S5 | si | |
| Completar columnas CÓDIGO, PRUEBAS y EVIDENCIA en docs/aspectos.md. | S5 | si | |
| Corregir enlaces de docs/aspectos.md que apuntan a la rama experimental. | S5 | si | |
| Integrar y evidenciar SonarCloud en el pipeline. | S5 | si | |
| Contrastar cada corrección de correcciones.md con commit o run específico. | S5 | si | |
| Análisis SonarCloud público con scanner, run y Quality Gate. | S6 | sí | Pipeline sin scanner ni URL pública de análisis. |
| Completar A-04 y corregir enlaces de aspectos que apuntan a experimental. | S6 | sí | La tabla no es defendible en la rama calificada. |
| Prueba de contrato inexistente en el arbol de b00b319. | S7 | si | |
| Sin evidencia de ejecucion de CI (runs) ni analisis SonarCloud publico con Quality Gate. | S7 | si | |
| Correspondencia contrato-codigo sin verificar; el contrato declara FastAPI y el backend versionado es Node. | S7 | si | |
| Sin historial git del contrato y sin contenido aportado de docs/c4/c2.md ni docs/aspectos.md. | S7 | si | |
| Prueba de contrato inexistente y sin ejecución en el pipeline. | S7 | si | |
| Sin evidencia de fallo de la prueba ante un cambio incompatible. | S7 | si | |
| Correspondencia contrato↔código no trazada (/transacciones vs /api/v1/sync). | S7 | si | |
| SonarCloud sin configuración, run ni URL pública del análisis. | S7 | si | |
| C4 nivel 2, docs/aspectos.md y docs/ia.md sin contenido verificable en la evidencia. | S7 | si | |
| ADR-0005 en revisión y punto abierto de ADR-0007 (ReceptorSmsBancario). | S7 | si | |
| Secciones 07 y 11 de arc42 ausentes. | S7 | si | |
| c450b4f 2026-09-20T22:40:25-05:00 Update ia.md | S7 | no (resuelto tarde) | — |
| fcf0089 2026-09-20T22:52:52-05:00 Update aspectos.md | S7 | no (resuelto tarde) | — |
| b7ca7f7 2026-09-20T23:03:41-05:00 y 73de849 2026-09-20T23:18:48-05:00 Update openapi.yaml | S7 | no (resuelto tarde) | — |
| 62a0d15 2026-09-20T23:25:16-05:00 Update 06-Runtime view.md | S7 | no (resuelto tarde) | — |
| Prueba de contrato no localizada ni invocada con evidencia de run | S7 | no (resuelto en auditoría) | Redocly se ejecuta en CI y el run del hash revisado está verde. |
| SonarCloud sin las tres evidencias auditables | S7 | si | |
| docs/arc42/07-Deployment View.md vacío | S7 | si | |
| docs/c4/c2.md sin verificar protocolo y formato en cada flecha | S7 | no (resuelto en auditoría) | El C2 etiqueta protocolo o mecanismo y formato en todas las relaciones. |
| ADR-0005 con estatus inconsistente entre encabezado y trazabilidad | S7 | si | |
| Archivos __pycache__ (.pyc) versionados | S7 | si | |
| Sin URL pública, health check ni infraestructura como código de despliegue | S8 | sí | Entregar el entorno público y su configuración reproducible. |
| Sin logs estructurados ni métrica operativa consultable | S8 | sí | Ligarlos a un escenario de calidad y al entorno desplegado. |
| Sin estimación mensual de costo ni ADR de plataforma | S8 | sí | Calcular por volumen y documentar cada decisión de proveedor. |
| `docs/arc42/07-Deployment View.md` vacío | S8 | sí | Completar una caja por pieza y dónde se ejecuta. |
| Sin commits de S9: la punta coincide con el hash calificado de S8. | S9 | sí | Empujar la porción de la evidencia S9 antes del cierre. |
| El sistema declara un componente de categorización con IA (`:aigemini`) sin evaluación de costo/latencia ni ADR de decisión. | S9 | sí | Evaluar el componente generativo o decidir su no incorporación con un ADR. |
| ADR 0001–0005 editados el 2026-09-27 tras su aceptación, sin declarar reemplazo. | S9 | sí | No editar ADR aceptados; crear uno nuevo y marcar el anterior como reemplazado. |
| Sin SonarCloud auditable (configuración, línea del scanner y URL pública con Quality Gate). | S9 | sí | Integrar y publicar el análisis estático. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_XALD; [README.md:1–9](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/README.md#L1-L9). |
| Estructura mínima presente | Cumple | README y seis rutas mínimas presentes; [docs/aspectos.md:5–11](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/aspectos.md#L5-L11) enlaza arquitectura y ADR. Hay binarios __pycache__ que deben retirarse sin confundirlos con ausencia documental. |
| Estado calificado identificable | Cumple | Rama master y hash/fecha exactos del encabezado, anterior al cierre; no se usaron etiquetas ni experimental para calificar. |
| Nombres de ADR según la convención | Cumple | Doce ADR con nombres NNNN-titulo-en-kebab-case.md; [docs/adr/0011-resolucion-conflictos-lww.md:1–5](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0011-resolucion-conflictos-lww.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | Historial confirma adición de fechas a ADR 0001–0005 ya aprobados el 27-sep; por ejemplo efcc3902311cc8fec393fccf4f1cc7a95badf976 sobre [docs/adr/0001-patron-offline-first.md:1–4](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/adr/0001-patron-offline-first.md#L1-L4). Son ediciones de metadatos, no se afirma cambio de decisión; registrar adendas sin reescribir aceptados conforme al contrato. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:39–41](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/docs/ia.md#L39-L41) crece en S9 con aceptados y rechazos motivados. La falta de un apartado de corrección se recoge en la fila específica S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Android CI del hash](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/37265397606) en success; [.github/workflows/ci.yml:29–57](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/.github/workflows/ci.yml#L29-L57) ejecuta Gradle, Redocly y pytest, pero no scanner SonarCloud. No hay configuración ni Quality Gate público de la revisión: el verde de pruebas no lo sustituye. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del árbol y búsqueda histórica de patrones de alta especificidad sin credenciales reales confirmadas; [backend/app/main.py:59–65](https://github.com/ISCOUTB/AS_202620_XALD/blob/9236ff97218b632eeb9a1910f6083968e2c22909/backend/app/main.py#L59-L65). Ejemplos y valores de pruebas revisados, sin publicar valores. |
| Contribución de todos los integrantes | No verificado | 419 commits con cuatro firmas observadas (186, 98, 72 y 63); la cantidad de firmas no verifica por sí sola correspondencia con cuatro integrantes ni distribución sustantiva. |

## Contribución por integrante

Actualización agregada del 2026-10-06: 419 commits en cuatro firmas visibles: 186, 98, 72 y 63. Correspondencia individual no verificada; no se infiere desde el número de cuentas.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Dilan Joan Gonzalez Bejarano | dilanbejarano011 | 39 | — | — | autor principal; esqueleto y README (23/08) |
| Luis Estheban Lozano Colmenares | colmenares2007-crypto | 17 | — | — | — |
| Xavier Yesid Garcia Diaz | xaviergarciadiaz20-commits | 17 | — | — | ADR-006 y matriz (23/08) |
| Axel Jair Ruiz Bolano | axeljruiz717-hash | 7 | — | — | matriz comparativa (23/08) |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Qué pasa con los conflictos aceptados si Render reinicia y se borra ultima_version; qué estado y datos se recuperan?
- ¿Cuál es el costo y umbral de capacidad al agregar persistencia y eventualmente Gemini, frente al supuesto de 50 usuarios?
- Si la prueba simultánea o con relojes desfasados cambia el resultado 30/30, ¿qué política de conflicto o diseño modificarían?
