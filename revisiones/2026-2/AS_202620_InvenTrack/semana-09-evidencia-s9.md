# Semana 9 · Generación verificada y trazable · InvenTrack

Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_InvenTrack |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.213435+00:00 |
| Cierre S9 | 2026-10-05T05:00:00Z (medianoche de Colombia) |
| Estado revisado | `35a9c63dd603bab989a18ed17ca56063c5616585` en `origin/main` (2026-10-04T22:14:10-05:00) |
| Línea base S8 | `48aeecf94e590088b21e1c4c63dee8d2feb79f11` |
| Commits del delta S8 → S9 | 14 |

## Alcance y método

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

La preliminar anterior aún no tenía porción S9. Ahora el delta añade la función p95, su prueba de 100 muestras, evidencia de mutación, ADR-0007/0008 y auditoría explícita. La falta de dependencias nuevas no se trata como fallo.

## Matriz de la ficha (10 criterios)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/ia.md:24-25](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L24-L25) identifica la extracción asistida; [app/main.py:99-102](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L99-L102) implementa p95 y [tests/test_metrics.py:3-12](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/tests/test_metrics.py#L3-L12) introduce prueba real. Commit [ab1eb204](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/ab1eb2044f7c8e5a32297029406844ff51e8ae1c) dentro del delta S8→S9. |
| Cadena completa navegable para esa porción | Cumple | [docs/aspectos.md:15-19](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/aspectos.md#L15-L19) contiene ASP-03 con ocho columnas y enlaces existentes a requisito, C4, ADR-0007, app/main.py, test_metrics.py y evidencia S9. La medición enlazada tiene la limitación separada en la fila 5. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0007-exponer-p95-de-latencia-en-metricas.md:7-46](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0007-exponer-p95-de-latencia-en-metricas.md#L7-L46) compara cálculo inline, dependencia externa y función local; justifica costo cero e historial acotado. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/evidencia-ia-corte-s9.md:31-76](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L31-L76) documenta mutación max(), resultado 0.5 frente a 0.05 y restauración; [tests/test_metrics.py:3-12](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/tests/test_metrics.py#L3-L12) realmente distingue p95 del máximo. Se acepta el procedimiento documentado, sin ejecutar la prueba. |
| Medición del escenario asociado | No cumple | [docs/evidencia-ia-corte-s9.md:78-94](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L78-L94) mide 20 GET /health con TestClient local (p95 9.066 ms); [docs/arc42/arc42-template-EN.md:747-756](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/arc42/arc42-template-EN.md#L747-L756) exige consultas simultáneas de catálogo/stock hasta 20 solicitudes/s. Una sonda estática secuencial/local y una muestra sintética prueban el cálculo, pero no el escenario de carga declarado. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:24-25](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L24-L25) registra extracción aceptada, sustitución de la prueba de 4 muestras por 100 y rechazo motivado de dependencias/modelo generativo. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/evidencia-ia-corte-s9.md:96-103](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s9.md#L96-L103) y [docs/ia.md:24](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L24) acotan la auditoría al composition root; [app/main.py:59-102](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L59-L102) confirma que la nueva función opera sobre métricas sin escribir datos de productos/inventario. No se exige inventar una violación si el contraste no la encuentra. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | Diff S8→S9 de requirements.in/requirements.txt vacío; [requirements.in:1-6](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/requirements.in#L1-L6) permanece con las mismas seis dependencias. [docs/ia.md:24](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/ia.md#L24) documenta cero incorporaciones y rechaza numpy/prometheus-client. La porción nueva usa math y colecciones estándar en [app/main.py:8-13](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/app/main.py#L8-L13). No añadir paquetes no es un incumplimiento; el universo nuevo de registro es vacío y está documentado. |
| Sin credenciales en código, ejemplos ni documentación generada | No verificado | La auditoría del equipo declara ausencia de credenciales en [docs/evidencia-ia-corte-s6.md:176-180](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/evidencia-ia-corte-s6.md#L176-L180). Las referencias de secretos de CI son variables en [.github/workflows/test.yml:37-41](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/.github/workflows/test.yml#L37-L41). El barrido independiente ampliado fue cancelado por la herramienta y el único reintento no lo completó; no se convierte esa limitación en evidencia de exposición ni en un árbol limpio verificado. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0008-no-incorporar-componente-generativo.md:7-52](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/35a9c63dd603bab989a18ed17ca56063c5616585/docs/adr/0008-no-incorporar-componente-generativo.md#L7-L52) decide no incorporarlo, con alternativas externas/locales, costo, latencia y condiciones para reabrir la decisión. |

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

## Recuento y nota sugerida

**8 de 10 criterios Cumple**,  1 No cumple y 1 No verificado. La transversal no entra en el cálculo.

**Nota propuesta pendiente de completar la comprobación bloqueada del revisor.** El recuento documental es 8/10; si las 1 comprobaciones bloqueadas resultan conformes, el intervalo resultante es 4.2–4.6. No es una nota cerrada ni se atribuye el bloqueo al equipo. La nota final la fija el docente en Moodle.

## Próximos pasos

La porción p95 ya está implementada, enlazada y acompañada de una prueba que distingue el percentil del máximo. La medición debe ejercitar consultas reales de catálogo o stock con la carga declarada: medir /health local no demuestra ese escenario. Mantengan la justificación de no añadir dependencias y completen la trazabilidad de reemplazo de ADR anteriores.
