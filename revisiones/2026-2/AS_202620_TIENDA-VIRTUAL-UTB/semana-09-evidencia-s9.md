# Evidencia S9 definitiva · Tienda virtual UTB

Revisión actualizada tras el cierre. Estado congelado al **2026-10-05T05:00:00Z** (domingo a medianoche en Colombia).

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB |
| Rama principal remota | `main` |
| Base S5 publicada | `3d732d740053c8f10ad4c618d3031024c72630bc` |
| Base S8 | `858e78f9e34ee4e205bdc84982ed8b04bd0dbb0d` |
| Estado revisado | `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33` en `origin/main` (2026-10-04T18:07:32-05:00) |
| Punta actual / S10 preliminar | `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33` · 2026-10-04T18:07:32-05:00 |
| Observado | 2026-10-06T21:28:33.520983Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

El delta se contrasta contra S8; los artefactos previos sirven de línea base y no vuelven a premiarse por existir. Los cambios tardíos se separan en overall.

## Matriz de la ficha S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/entrega-cadena-ia.md:7–23](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L7-L23) y [backend/app/modules/inventory/repository.py:1–13](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/backend/app/modules/inventory/repository.py#L1-L13): separación real de stock respecto de Catálogo, incorporada en el delta S8→S9; apoyo de IA identificado en [docs/ia.md:26](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/ia.md#L26). |
| Cadena completa navegable para esa porción | Cumple | [docs/aspectos.md:37](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/aspectos.md#L37) conduce a ADR 0008, contratos, código y entrega; esta última enlaza la prueba y el medidor. Cadena recorrida y destinos presentes; aceptación del ADR se valora por separado. |
| ADR con la decisión argumentada por el equipo | No cumple | [docs/adr/0008-separar-catalogo-inventario.md:3–6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0008-separar-catalogo-inventario.md#L3-L6) y [docs/adr/0008-separar-catalogo-inventario.md:48–52](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0008-separar-catalogo-inventario.md#L48-L52): hay alternativas y razones del proyecto, pero el documento declara explícitamente que la decisión colectiva está pendiente. El commit no ratifica por sí solo la propuesta. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/entrega-cadena-ia.md:25–51](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L25-L51) documenta cómo reintroducir la columna indebida y el import cruzado, con fallo y restauración; [backend/tests/test_inventory.py:19–22](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/backend/tests/test_inventory.py#L19-L22). Se admite el procedimiento documentado que exige la ficha; no fue ejecutado por el revisor. |
| Medición del escenario asociado | Cumple | [docs/entrega-cadena-ia.md:54–85](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L54-L85): cinco usuarios concurrentes, 5/5 respuestas correctas, cero errores y salud posterior; 173,81 ms total, frente al umbral explícito. Alcance local Uvicorn/SQLite, no producción. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:26](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/ia.md#L26): aceptado para candidato, correcciones de propiedad/imports/documentación y descartes razonados; la validación humana final sigue declarada pendiente, sin ocultarla. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/violaciones-s6.md:7–43](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/violaciones-s6.md#L7-L43) contrastada con [backend/tests/test_inventory.py:19–22](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/backend/tests/test_inventory.py#L19-L22) y [backend/tests/test_architecture.py:33–57](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/backend/tests/test_architecture.py#L33-L57): dueño único, detección AST y límites del método explícitos; V5/V6 siguen como deuda. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/entrega-cadena-ia.md:164–176](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L164-L176): no se añaden dependencias de ejecución y el diff de manifiestos Python/frontend lo confirma; se documenta la revisión de versiones y procedencias PyPI/npm existentes. Cumplimiento documental acotado, sin ejecutar descargas ni auditar todo el árbol transitivo. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido estático del árbol de este hash, incluidos ejemplos y Markdown, sin credenciales reales detectadas. La coincidencia de [compose.yaml:4–8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/compose.yaml#L4-L8) es interpolación obligatoria de entorno; los valores de prueba de [docs/entrega-cadena-ia.md:125–125](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L125-L125) están identificados como efímeros. No prueba revocación de credenciales compartidas fuera de Git. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No cumple | [docs/adr/0009-sin-componente-generativo.md:25–42](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0009-sin-componente-generativo.md#L25-L42): el ADR existe y justifica no generar en producción, pero dice que el equipo aún debe aceptarlo. Ratificar o rechazar; la falta de aceptación no equivale a una decisión aprobada. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público correcto del repositorio vigente ISCOUTB; [README.md:1–3](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L1-L3). |
| Estructura mínima presente | Cumple | Árbol Git con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md; [README.md:224–228](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/README.md#L224-L228). |
| Estado calificado identificable | Cumple | Rama main; hash y fecha exactos del encabezado, último commit ≤ cierre, sin etiquetas. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0009 siguen NNNN-titulo-en-kebab-case.md; [docs/adr/0008-separar-catalogo-inventario.md:3–6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0008-separar-catalogo-inventario.md#L3-L6). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-monolito-modular.md:19–35](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0001-monolito-modular.md#L19-L35): el historial confirma edición posterior a aceptación en e8ae57df776b3d171957f4d0c8a1e19cfb968ba5. El reemplazo 0003–0006 por 0007 sí está declarado en [docs/adr/0007-despliegue-dokploy.md:3–5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0007-despliegue-dokploy.md#L3-L5), pero no cierra la reescritura histórica de 0001. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:26](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/ia.md#L26) añadida en el delta S9, con correcciones y descartes técnicos. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Pruebas del hash en success](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/37242837748); [.github/workflows/tests.yml:64–80](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/.github/workflows/tests.yml#L64-L80) omite el scanner si falta SONAR_TOKEN y [docs/pendientes.md:20–23](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/pendientes.md#L20-L23) aún solicita configurarlo. No se acredita run del scanner más Quality Gate público de la revisión; verde global no basta. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del árbol sin credenciales reales y búsqueda histórica de patrones de alta especificidad sin incidentes confirmados. [compose.yaml:4–8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/compose.yaml#L4-L8). Alcance estático; la rotación externa pendiente en [docs/pendientes.md:17–18](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/pendientes.md#L17-L18) debe verificarse por separado. |
| Contribución de todos los integrantes | No verificado | El historial presenta varias firmas y variantes; no hay correspondencia individual verificada suficiente para afirmar contribución de todos. No se atribuyen cuentas por semejanza de nombre. |

## Recuento y nota sugerida

**8 de 10 criterios Cumple. Nota sugerida: 4.2 = 1 + 4 × (8/10). Propuesta al docente; la nota final se fija en Moodle.** No verificado no se convierte en Cumple ni en una ejecución fallida.

## Estado global del proyecto (overall)

Punta de la misma rama: `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33` (2026-10-04T18:07:32-05:00). Hay **8 commits en el delta S8→S9** y **0 commits posteriores al cierre S9**. El nuevo incremento de inventario ya está presente en S9; no hay commits tardíos en la punta revisada. La migración documental a Dokploy reemplaza Vercel/Render/Neon, pero el dominio continúa pendiente. Las pruebas y mediciones documentadas son locales.



### Hallazgos abiertos

- Ratificar ADR 0008 y 0009 con decisión y razones propias del equipo; ambos se declaran propuestas.
- Registrar dominio público vigente y evidencias fechadas de salud/flujo Dokploy; el costo del servidor y backups está por confirmar.
- Completar SonarCloud: scanner realmente ejecutado y Quality Gate público de la revisión.
- Corregir contradicciones del README y pendientes que todavía presentan Inventario vacío.
- Precisar asignación S10 y registrar línea base, experimento, resultado y límites de validez.
- Confirmar correspondencia de autoría sin inferencias y verificar rotación de credenciales compartidas fuera del repositorio.

### Hallazgos cerrados o sustituidos con evidencia actual

- Cadena, prueba negativa, medición y auditoría S9 ya están documentadas y enlazadas: [docs/entrega-cadena-ia.md:7–23](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/entrega-cadena-ia.md#L7-L23).
- La migración a Terraform pendiente deja de ser el plan vigente: ADR 0007 reemplaza 0003–0006; no se declara ejecutado Terraform. [docs/adr/0007-despliegue-dokploy.md:3–12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33/docs/adr/0007-despliegue-dokploy.md#L3-L12).
- CI del hash actual pasa [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/37242837748); el cron keep-alive fue retirado. Esto no cierra SonarCloud ni demuestra despliegue.

## Próximos pasos

La separación Catálogo–Inventario ya tiene una cadena sólida: prueba negativa, medición local y auditoría de propiedad de datos. Falta que el equipo ratifique las decisiones de separación y de no incorporar generación; ambas siguen como propuestas. Corrijan además el README que aún presenta Inventario vacío y aporten la evidencia pública del scanner y Quality Gate.
