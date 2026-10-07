# Semana 9 · Generación verificada y trazable · Recobra

Revisión definitiva; reemplaza la preliminar.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_Recobra |
| Rama principal remota | `master` |
| Estado revisado | `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` en `origin/master` (2026-10-04T23:40:37-05:00) |
| Línea base S8 | `5c7f77b3da94ed019ade4b959c723444a2ee7c02` |
| Punta actual / S10 preliminar | `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` · 2026-10-04T23:40:37-05:00 |
| Cierre S9 | 2026-10-05T05:00:00Z |
| Cierre eventual S10 | 2026-10-12T05:00:00Z |
| Revisión | 2026-10-06 (UTC) |

## Alcance y método

Se consultó la rama principal remota mediante git y se eligió su último commit anterior o igual al cierre S9; no se consultaron etiquetas. S10 es preliminar y usa la punta actual. Se comparó S9 con la línea base S8; no se vuelven a puntuar entregas anteriores por existir. No se ejecutó código, pruebas ni despliegues del equipo. Los registros de ejecución del repositorio se distinguen de la comprobación externa. Por exclusión docente no se abrieron PDFs ni se evaluó su presencia, contenido, extensión o ubicación.

La consulta general de Actions se verificó mediante GET /actions/runs (100 registros como máximo); se distinguen el hash, la rama y la conclusión de cada run. Un intento inicial filtrado a pull requests no se usó para decidir. No se consultaron jobs ni logs adicionales.

El delta S8→S9 contiene 24 commits. La nueva porción es búsqueda con filtros A6 (d6e56df), acompañada de ADR, mutación y carga; Emparejamiento previo queda como línea base.

## Matriz de la ficha S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [src/application/use-cases/buscar-publicaciones.ts:15–55](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/application/use-cases/buscar-publicaciones.ts#L15-L55) y [src/publicaciones/publicaciones.controller.ts:37–44](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/publicaciones/publicaciones.controller.ts#L37-L44). La búsqueda se incorpora en d6e56df dentro del delta S9; [docs/ia.md:63](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/ia.md#L63) atribuye apoyo de IA y revisión humana. |
| Cadena completa navegable para esa porción | Cumple | [docs/aspectos.md:15](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/aspectos.md#L15) enlaza S1, contenedor API, ADR-0008/0009, código, pruebas, mutación y medición. Se recorrieron los destinos. Los C4 detallados están desactualizados (hallazgo transversal/S10), pero el contenedor API citado y el recorrido A6 existen. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md:11–94](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md#L11-L94). Alternativas de filtrado en repositorio, aplicación y motor externo; decisión con presupuesto cero, costo de transferencia, límites y reversión. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/ia-auditoria-mutacion-busqueda.txt:1–76](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/ia-auditoria-mutacion-busqueda.txt#L1-L76): inversión del filtro de categoría provoca un fallo unitario y uno e2e; [docs/auditoria-generacion-ia.md:149–160](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/auditoria-generacion-ia.md#L149-L160) explica el refuerzo del e2e originalmente débil. Evidencia documental admitida por la ficha, no ejecutada por el revisor. |
| Medición del escenario asociado | Cumple | [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80). Tres corridas locales a 200 conexiones con p97,5 de 43/53/67 ms frente a 400 ms; producción a 1/5/20 conexiones y límite declarado. Medir y contrastar se cumple aunque producción no demuestre el umbral de S1 a 200 usuarios; no se presenta éxito de producción. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:63](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/ia.md#L63). Acepta consulta parametrizada y límite; corrige test débil y SQL; rechaza concatenación y carga secuencial por motivos técnicos. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/auditoria-generacion-ia.md:107–121](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/auditoria-generacion-ia.md#L107-L121) contrastado con [src/application/use-cases/buscar-publicaciones.ts:1–30](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/application/use-cases/buscar-publicaciones.ts#L1-L30) y [src/infrastructure/persistence/postgres-publicacion.repository.ts:44–85](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/infrastructure/persistence/postgres-publicacion.repository.ts#L44-L85): lectura por puerto y escrituras dentro del adaptador propietario. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/auditoria-generacion-ia.md:123–142](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/auditoria-generacion-ia.md#L123-L142). El diff S8→S9 añade autocannon como dependencia de desarrollo. Consulta externa al [registro oficial npm](https://registry.npmjs.org/autocannon) el 2026-10-06 confirma nombre autocannon y repositorio mcollina/autocannon; no se instaló ni ejecutó. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | [.env.example:1–5](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/.env.example#L1-L5) y [src/infrastructure/persistence/postgres-publicacion.repository.ts:19–24](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/src/infrastructure/persistence/postgres-publicacion.repository.ts#L19-L24). Barrido de HEAD, ejemplos y documentación, sin credenciales reales identificadas; no hay .env versionado. Las variables y ejemplos no se confunden con secretos. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0007-no-incorporar-componente-generativo.md:25–97](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0007-no-incorporar-componente-generativo.md#L25-L97). ADR aceptado del periodo decide no incorporar LLM en ejecución; justifica costo, latencia, confiabilidad y condiciones para reconsiderar. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon anónimo de https://github.com/ISCOUTB/AS_202620_Recobra; nombre y organización conformes. |
| Estructura mínima presente | Cumple | [README.md:163–180](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L163-L180). Árbol con README, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md. |
| Estado calificado identificable | Cumple | origin/master, ebe6cca7a903bb333678bd20ba5327d8fcb127f7, 2026-10-04T23:40:37-05:00, último commit ≤ cierre S9. Para S10 es la punta preliminar actual. |
| Nombres de ADR según la convención | Cumple | [docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md:1–9](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0008-busqueda-con-filtros-en-el-repositorio.md#L1-L9); nueve archivos Markdown con NNNN-kebab-case. |
| ADR aceptados no reescritos | No cumple | [docs/no-conformidades.md:167–194](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L167-L194). Historial leído: ADR-0002/0003 editados en f7c1a6c tras aceptación; ADR-0004 modificado en 34ab8f2. [docs/adr/0009-versionado-del-contrato-y-error-unico.md:3–31](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/adr/0009-versionado-del-contrato-y-error-unico.md#L3-L31) registra sucesión parcial de 0004; falta enlace de reemplazo en el antecedente y no regulariza todos los ADR. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:63](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/ia.md#L63). Registro actualizado en S9 con aceptado, corregido, rechazado y motivo; no hay actividad posterior en S10 aún. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:31–49](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/.github/workflows/ci.yml#L31-L49). Scanner explícito pero continue-on-error; [docs/no-conformidades.md:98–110](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L98-L110) declara token pendiente. Configuración en [sonar-project.properties:1–8](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/sonar-project.properties#L1-L8). No hay run exitoso del scanner y Quality Gate de esta revisión acreditados; CI general verificado success para el hash en [run 37264560596](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/37264560596), creado 2026-10-05T04:40:41Z; no acredita el scanner, que admite fallo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido del contrato en HEAD, ejemplos y docs sin secretos del equipo identificados; búsqueda histórica de claves privadas/tokens de alta confianza sin coincidencias fuera de dependencias. [docs/no-conformidades.md:8–40](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/no-conformidades.md#L8-L40) identifica el artefacto histórico Coveralls de un paquete tercero; no se publica su valor ni se atribuye al equipo. Alcance de barrido, no garantía universal. |
| Contribución de todos los integrantes | No verificado | Historial agregado: 128 commits; cinco grupos por identidad de correo, con .mailmap que vincula dos firmas. Se observan aportes de cuatro grupos consolidados. La correspondencia completa grupo→integrante y la sustantividad individual requieren validación docente; no se infieren identidades por parecido. |

## Estado global del proyecto (overall)

La punta actual de `master` es `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` (2026-10-04T23:40:37-05:00) y coincide con S9 congelada: no hay commits tardíos hasta esta revisión. La entrega S9 aporta evidencia documental consistente y una porción nueva. La medición distingue local de producción y reconoce su brecha. Para el corte permanecen diferencias entre C4 y MVP, trazabilidad de la asignación y observabilidad del reto.

### Hallazgos abiertos

- Identificar y documentar la asignación oficial de S10 antes de juzgar su hipótesis, línea base y resultado.
- SonarCloud: falta evidencia del scanner exitoso y Quality Gate de la revisión; continue-on-error no impone bloqueo de integración. [.github/workflows/ci.yml:31–49](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/.github/workflows/ci.yml#L31-L49)
- C4-C2/C3 no representan PostgreSQL en producción ni todos los componentes actuales. [docs/c4/C4-C2.md:9–34](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/c4/C4-C2.md#L9-L34)
- S1 no está demostrado en producción: a 20 conexiones el documento informa p97,5=1113 ms; no se midieron 200. [docs/medicion-busqueda.md:27–80](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/medicion-busqueda.md#L27-L80)
- Regularizar sucesión de ADR-0002/0003 y el enlace del antecedente 0004 sin reescribir el historial.
- README mantiene descripción sin variables pese a DATABASE_URL y un ejemplo de error antiguo. [README.md:82–86](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L82-L86); [README.md:135](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/README.md#L135)

### Hallazgos cerrados o corregidos en esta revisión

- La porción nueva S9 queda acreditada por búsqueda A6; el hallazgo preliminar de porción únicamente anterior a S8 se cierra. [docs/aspectos.md:15](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ebe6cca7a903bb333678bd20ba5327d8fcb127f7/docs/aspectos.md#L15)
- La dependencia nueva autocannon está identificada y verificada en npm; no se exige añadir dependencias para aprobar una auditoría.
- Health público comprobado HTTP 200. Esto cierra la falta de comprobación puntual, sin cambiar retroactivamente las filas S8 diferidas.
- ADR-0009 documenta sucesión parcial y reconoce la edición de ADR-0004; cierre parcial de ese hallazgo, sin ocultar incumplimientos históricos.

## Recuento y nota sugerida

**10 de 10 criterios Cumple. Propuesta al docente: 5.0 = 1 + 4 × (10/10).** La nota final la fija el profesor en Moodle; la matriz transversal no entra en esta fórmula.

## Próximo paso

La búsqueda con filtros ya es una porción nueva y trazable: la mutación detectó una prueba débil y la corrigieron. Mantengan la separación explícita entre las mediciones locales y la brecha de producción. Sincronicen los C4 con la persistencia real, completen la sucesión de ADR y acrediten el scanner y Quality Gate del commit entregado.
