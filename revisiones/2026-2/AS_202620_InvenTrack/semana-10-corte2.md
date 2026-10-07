# Semana 10 · Segundo corte · InvenTrack

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_InvenTrack |
| Estado revisado | `35a9c63dd603bab989a18ed17ca56063c5616585` en `origin/main` (2026-10-04T22:14:10-05:00) |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.213435+00:00 |
| Punta revisada para S10 | `35a9c63dd603bab989a18ed17ca56063c5616585` (2026-10-04T22:14:10-05:00) |
| S9 congelado, solo como línea base | `35a9c63dd603bab989a18ed17ca56063c5616585` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** No se localizó una asignación oficial del reto S10. ESC-04 es un escenario de calidad previo y el documento del reto disponible es de corte 1; no se asume que equivalga a la asignación del segundo corte. Fuente o búsqueda: [docs/arc42/arc42-template-EN.md:747-756](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/arc42/arc42-template-EN.md#L747-L756); [docs/evidencia-ia-corte-s9.md:7-18](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L7-L18); búsqueda en README, ADR y docs/retos. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `ac951e3fc2acf849f2cc89ffb622d392b268672a`: el delta hasta esta punta modifica 65 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | main 35a9c63dd603bab989a18ed17ca56063c5616585 (2026-10-04T22:14:10-05:00); punta anterior al cierre futuro. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://inventrack.iscoutb.dev/health: HTTP 200, 7.043 s; /metrics: HTTP 200, 7.454 s. Consulta iniciada 2026-10-06T21:17:34Z. URL en [README.md:34-39](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/README.md#L34-L39). Son sondas read-only; no se ejecutó el flujo de inventario. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | No se localizó una asignación oficial del reto S10. ESC-04 es un escenario de calidad previo y el documento del reto disponible es de corte 1; no se asume que equivalga a la asignación del segundo corte. [docs/arc42/arc42-template-EN.md:747-756](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/arc42/arc42-template-EN.md#L747-L756); [docs/evidencia-ia-corte-s9.md:7-18](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L7-L18); búsqueda en README, ADR y docs/retos |
| Línea base medida y reproducible | No verificado | [docs/evidencia-ia-corte-s9.md:78-94](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L78-L94) no es línea base del reto confirmado; /health no modela consultas de stock bajo carga. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0007-exponer-p95-de-latencia-en-metricas.md:15-38](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0007-exponer-p95-de-latencia-en-metricas.md#L15-L38) acredita decisión de p95/costo, pero falta asignación para juzgar adecuación S10. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [app/main.py:99-102](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L99-L102) y [app/main.py:143-162](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L143-L162) implementan cálculo y métrica; no se los da por respuesta al reto sin conocerlo. |
| Resultado contrastado con el umbral | No verificado | No hay contraste verificable de línea base/respuesta del reto S10 identificado; la medición S9 de [docs/evidencia-ia-corte-s9.md:78-94](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L78-L94) tiene alcance local. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Health y /metrics accesibles; logs JSON en [app/main.py:36-90](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L36-L90). Falta run actual confirmado, Quality Gate bloqueante y vínculo de métrica al reto asignado; no se confunde estado visible con resultado de carga. |
| Secretos protegidos | No verificado | La auditoría del equipo declara ausencia de credenciales en [docs/evidencia-ia-corte-s6.md:176-180](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s6.md#L176-L180). Las referencias de secretos de CI son variables en [.github/workflows/test.yml:37-41](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L37-L41). El barrido independiente ampliado fue cancelado por la herramienta y el único reintento no lo completó; no se convierte esa limitación en evidencia de exposición ni en un árbol limpio verificado. |
| C4, arc42, ADR y contratos correspondientes al MVP | Cumple | [docs/c4/containers.md:68-74](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/c4/containers.md#L68-L74) distingue API real, frontend futuro y memoria; [docs/c4/containers.md:122-128](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/c4/containers.md#L122-L128) declara límites. [docs/aspectos.md:19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/aspectos.md#L19) enlaza cambio, prueba y medición; ADR-0007 y vista de despliegue están versionados. Coherencia documental de la base acreditada, sin convertirla en logro S10. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:7-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L7-L15) consolida decisiones, pero no aporta confirmación/reemplazo basado en el experimento S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de sesión docente en el despliegue y ejecución de pipeline en vivo. |

Recuento descriptivo: 3 Cumple, 0 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Reto asignado no confirmado; no se puntúa ESC-04 como si fuera esa asignación. |
| Decisión e implementación | No verificado | Pendiente | Código, ADR y alternativas presentes para S9; adecuación al reto S10 pendiente. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Sondas y métrica verificadas por lectura; run actual, secreto y gate requieren completar evidencia. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Base documentada y enlazada; confirmación/reemplazo por experimento S10 pendiente. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | La fija el docente en sesión. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_InvenTrack; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Árbol Git contiene seis rutas mínimas; tabla de aspectos [docs/aspectos.md:15-19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/aspectos.md#L15-L19) y documentos enlazados existentes. |
| Estado calificado identificable | Cumple | main, 35a9c63dd603bab989a18ed17ca56063c5616585, fecha y corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Listado docs/adr: 0001–0009, todos NNNN-titulo-en-kebab-case; [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:1-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L1-L15). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md:7-15](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md#L7-L15) reconoce ediciones aceptadas de 0002/0004/0005 y declara consolidación futura; no marca cada decisión anterior reemplazada con enlaces. Historial del periodo incluye restauración [193e2628](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/193e2628757f3e8987ae5a01a90b8e8cce45d7a0). La corrección de política se reconoce, pero no borra las reescrituras. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:23-25](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L23-L25) contiene usos hasta S9, aceptado y rechazos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [sonar-project.properties:1-7](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/sonar-project.properties#L1-L7) y [.github/workflows/test.yml:23-45](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L23-L45) acreditan configuración/scanner. Una consulta de runs del commit (limitada a pull_request por el conector) no devolvió registros; no acredita ausencia de push ni éxito. No se verificó el Quality Gate público para este hash; además el YAML no incluye espera/bloqueo explícito de Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | La auditoría del equipo declara ausencia de credenciales en [docs/evidencia-ia-corte-s6.md:176-180](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s6.md#L176-L180). Las referencias de secretos de CI son variables en [.github/workflows/test.yml:37-41](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L37-L41). El barrido independiente ampliado fue cancelado por la herramienta y el único reintento no lo completó; no se convierte esa limitación en evidencia de exposición ni en un árbol limpio verificado. |
| Contribución de todos los integrantes | No verificado | El historial contiene varias firmas; las atribuciones por semejanza no se usan. La planilla previa reconoce correspondencias pendientes. Se debe validar cuenta–integrante y distribución, sin publicar correos. |

## Estado global del proyecto (overall)

Punta observada de `origin/main`: `35a9c63dd603bab989a18ed17ca56063c5616585` (2026-10-04T22:14:10-05:00). Hay 0 commits posteriores al estado congelado S9. La punta coincide con el cierre S9. El backend y las sondas del dominio institucional responden; el proyecto conserva almacenamiento en memoria. El cálculo p95 es verificable estáticamente y la medición debe pasar de /health al flujo de negocio bajo la carga de ESC-04.

- Medir catálogo/stock con la carga y condiciones de ESC-04; la sonda /health no es un sustituto.
- Completar el registro inmutable/reemplazo de ADR anteriores y aportar run/scanner/Quality Gate público del hash revisado.
- Terminar la verificación independiente de secretos e identidad de contribuciones; la limitación de herramienta no demuestra exposición.
- Identificar escenario S10, línea base del despliegue y resultado reproducible.

### Hallazgos anteriores cerrados o delimitados

- Se cierra «sin porción S9»: app/main.py y tests/test_metrics.py cambian dentro del periodo.
- ASP-03 ya enlaza ocho eslabones y existe mutación documentada que falla.
- Hay auditoría de límites con universo de dependencias nuevo vacío explícito; se corrige la lectura anterior que penalizaba no añadir paquetes.
- ADR-0008 formaliza no incorporar generación; ADR-0009 reconoce el problema de inmutabilidad, aunque su resolución es parcial.
- Sondas del despliegue institucional responden; la falta de URL/health no sigue abierta como ausencia de artefacto.

## Preparación de la sustentación

1. Fallo: si se reinicia o replica el proceso, ¿qué ocurre con stock, locks y el historial p95 y cómo detectarán inconsistencias?
2. Costo: ¿qué volumen o necesidad de persistencia obligaría a abandonar el presupuesto cero y qué alternativa compararon?
3. Medición: si las consultas reales de stock incumplen 400 ms aunque /health sea rápido, ¿qué cambio harían y con qué experimento lo validarían?

## Próximos pasos

Las sondas públicas de salud y métricas responden. Confirmen el escenario operativo asignado, midan una línea base del flujo de negocio y comparen la respuesta con el umbral en el despliegue. Aporten evidencia actual del pipeline y Quality Gate y preparen la defensa del almacenamiento en memoria y de su costo de evolución.
