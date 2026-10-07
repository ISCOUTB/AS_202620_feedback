# Evidencia S9 definitiva · Drift

Revisión actualizada tras el cierre del **2026-10-05T05:00:00Z** (domingo a medianoche COT).

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_Drift](https://github.com/ISCOUTB/AS_202620_Drift) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `74337a3c9c2a67c807e0018fe865979b29aa330c` |
| Base S8 | `74709aa4f6b9255b4792e4aafd01be2bdae8ff0e` |
| Estado revisado | `3dee7e265eec021cbbba4af4d337e13c982df316` en `origin/master` (2026-10-04T22:03:23-05:00) |
| S9 congelada | `3dee7e265eec021cbbba4af4d337e13c982df316` · 2026-10-04T22:03:23-05:00 |
| Punta actual / S10 preliminar | `3dee7e265eec021cbbba4af4d337e13c982df316` · 2026-10-04T22:03:23-05:00 |
| Comprobación | 2026-10-06T21:25:06Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Matriz S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | Se acredita la corrección real S9 de SyncPlayStationCatalog en 0ebb19e: depende de nuevo puerto GameCatalogRepository, no del adaptador concreto. [backend/app/application/usecases/sync_playstation_catalog.py:3–20](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/application/usecases/sync_playstation_catalog.py#L3-L20), [backend/app/domain/ports/game_catalog_repository.py:1–14](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/domain/ports/game_catalog_repository.py#L1-L14); auditoría asistida registrada en [docs/ia.md:532–551](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/ia.md#L532-L551) y [docs/evidencias/evidencias_semana9.md:540–610](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L540-L610). No se vuelve a acreditar Steam por mera existencia. |
| Cadena completa navegable para esa porción | No cumple | La fila E1 sigue centrada en Steam y usa rutas de código/pruebas como texto, con medición de septiembre. E2 no enlaza la corrección S9 ni una prueba específica de sustitución; [docs/aspectos.md:52–58](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/aspectos.md#L52-L58). Falta cadena completa para el cambio real del periodo. |
| ADR con la decisión argumentada por el equipo | Cumple | ADR-0004 argumenta la decisión de aislar proveedores y mantener dependencias por adaptadores; la corrección nueva materializa esa decisión vigente, sin inventar un ADR nuevo de la misma política. [docs/adr/0004-estrategia-de-integracion.md:7–26](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0004-estrategia-de-integracion.md#L7-L26), [docs/adr/0004-estrategia-de-integracion.md:28–85](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0004-estrategia-de-integracion.md#L28-L85). Persistencia MySQL sigue siendo discrepancia global aparte. |
| Prueba que falla ante el defecto que cubre | No verificado | El run rojo/verde citado prueba una ruptura de contrato del 27 de septiembre, anterior a S9. La corrección nueva de dependencias solo declara 14 pruebas verdes, sin mutación específica de esa regla; [docs/evidencias/evidencias_semana9.md:431–473](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L431-L473), [docs/evidencias/evidencias_semana9.md:578–610](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L578-L610). |
| Medición del escenario asociado | No cumple | La medición principal es del 13 de septiembre y el taller serverless del 26; son línea base, aunque el documento del taller se incorporó después. No se aporta medición nueva de la corrección S9 contra su umbral; [docs/evidencias/e1-linea-base.md:3–49](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/e1-linea-base.md#L3-L49), [docs/evidencias/Evidencia_TallerS8.md:3–28](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/Evidencia_TallerS8.md#L3-L28). |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | Registro 24 y 37–40 explican uso, validación/corrección documental y rechazos motivados, incluidos no inventar trazabilidad ni confundir mediciones de entornos distintos; [docs/ia.md:532–551](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/ia.md#L532-L551), [docs/ia.md:831–919](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/ia.md#L831-L919). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | Hallazgo y cambio comprobables: aplicación importaba infraestructura; nuevo puerto elimina el acoplamiento en 0ebb19e. [docs/evidencias/evidencias_semana9.md:540–610](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L540-L610), [backend/app/application/usecases/sync_playstation_catalog.py:3–20](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/application/usecases/sync_playstation_catalog.py#L3-L20). |
| Dependencias propuestas verificadas en su registro oficial | Cumple | Auditoría nueva de inventario preexistente y enlaces oficiales PyPI/npm; [docs/evidencias/evidencias_semana9.md:613–696](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L613-L696). No cambian manifiestos S8→S9, por lo que no se exige añadir paquetes. Consulta oficial: FastAPI 0.141.1, Schemathesis 4.27.5 y Gunicorn 23.0.0 respondieron 200 en PyPI; next/react/react-dom respondieron 200 en npm y corresponden a proyectos oficiales. No se atribuyen altas al periodo. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido de código, ejemplos y docs del snapshot sin credenciales: [.github/workflows/master_drift-utb-202620.yml:27–35](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/.github/workflows/master_drift-utb-202620.yml#L27-L35) contiene permisos y referencias externas; [docs/evidencias/evidencias_semana9.md:698–738](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/evidencias/evidencias_semana9.md#L698-L738) solo ejemplos del patrón. No hay .env versionado. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | ADR-0007 decide no incorporar IA generativa y compara chatbot, recomendaciones y lógica convencional con consecuencias; [docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md:9–83](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0007-evaluacion-de-incorporaci%C3%B3n-coponente-generativo.md#L9-L83). |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público en ISCOUTB con nombre conforme, rama master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Seis rutas presentes; arc42 no incluye sección 11, deuda de completitud aunque existe directorio. [docs/aspectos.md:48–58](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/aspectos.md#L48-L58). |
| Estado calificado identificable | Cumple | Snapshot y fecha completos en encabezado; coincide con la punta actual. |
| Nombres de ADR según la convención | No cumple | ADR-0007 usa acento y nombre no conforme al patrón; [docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md:1–7](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0007-evaluacion-de-incorporaci%C3%B3n-coponente-generativo.md#L1-L7). |
| ADR aceptados no reescritos | No verificado | El historial de ADR previos requiere confirmar inmutabilidad desde aceptación; no se declara resuelto el hallazgo anterior. Los ADR nuevos no reemplazan expresamente los reescritos. |
| docs/ia.md al día para la semana | Cumple | Registros nuevos de revisión y organización S9 con validación y alternativas descartadas por razones técnicas; [docs/ia.md:831–919](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/ia.md#L831-L919). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI y Azure deployment success en el hash, pero el scanner fue añadido y revertido antes del cierre. El workflow actual no invoca SonarCloud; [.github/workflows/ci.yml:1–54](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/.github/workflows/ci.yml#L1-L54), [sonar-project.properties:1–6](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/sonar-project.properties#L1-L6). Archivo de propiedades por sí solo no prueba análisis/Gate. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Snapshot sin credenciales reales; referencias de Actions, permisos y ejemplos de patrón. No se certificó revisión exhaustiva de todos los blobs históricos. |
| Contribución de todos los integrantes | No verificado | Ocho firmas, 384 commits agregados. Sin atribuir variantes por parecido; correspondencia completa con cuatro integrantes no verificada. |

## Actions en el estado congelado

- [CI: success](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/37257975825), 2026-10-05T03:05:21Z, SHA exacto del estado indicado.
- [Build and deploy Python app to Azure Web App - drift-utb-202620: success](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/37257975779), 2026-10-05T03:05:21Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
El barrido del árbol revisado no identificó claves reales. Las coincidencias fueron permisos id-token y textos de ejemplos en documentación; no hay .env versionado. El historial completo no se certifica en esta pasada; no afecta al criterio S9 limitado al snapshot.

## Estado global del proyecto (overall · punta actual)

La punta conserva la corrección de erosión de aplicación hacia infraestructura y añade funcionalidad de catálogo/UI. Los tres cambios de análisis SonarCloud fueron revertidos antes del cierre: CI y despliegue verdes no prueban scanner ni Quality Gate. Las mediciones publicadas son antiguas y se deben distinguir del trabajo S9 y del reto S10. Persiste diferencia entre la persistencia MySQL descrita y los adaptadores en memoria.

El delta S9 contiene 19 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Recuento y nota sugerida

**7 de 10 criterios Cumple. Nota sugerida: 3.8 = 1 + 4 × (7/10).** Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no integra este cálculo.

## Acciones prioritarias

- Cerrar la cadena de la corrección GameCatalogRepository hacia aspecto, ADR, prueba que falle ante erosión y evidencia del escenario.
- Distinguir mediciones de septiembre de un experimento nuevo del reto asignado, con factores de confusión y límites.
- Reintegrar scanner SonarCloud de forma verificable y aportar Quality Gate de la revisión.
- Alinear C4/arc42/ADR con la persistencia y forma de ejecución reales; usar ADR sustituto donde cambie una decisión aceptada.
- Confirmar consigna oficial S10 y demostrar el flujo principal en el despliegue antes de la sustentación.

## Hallazgos cerrados con evidencia nueva

- Erosión aplicación→infraestructura corregida mediante puerto explícito en S9; [backend/app/application/usecases/sync_playstation_catalog.py:3–20](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/backend/app/application/usecases/sync_playstation_catalog.py#L3-L20).
- Decisión explícita de no incorporar IA generativa, [docs/adr/0007-evaluacion-de-incorporación-coponente-generativo.md:17–27](https://github.com/ISCOUTB/AS_202620_Drift/blob/3dee7e265eec021cbbba4af4d337e13c982df316/docs/adr/0007-evaluacion-de-incorporaci%C3%B3n-coponente-generativo.md#L17-L27).
