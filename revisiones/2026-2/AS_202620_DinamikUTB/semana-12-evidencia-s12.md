# DinamikUTB · Evidencia S12 · PRELIMINAR, avance no final

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_DinamikUTB/tree/37872ff7dbb08be833b92c0a4b6d1ca3152464a1) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

- Repositorio público: https://github.com/ISCOUTB/AS_202620_DinamikUTB
- Rama seleccionada: `origin/master` (HEAD remoto); no se usaron etiquetas ni ramas de trabajo.
- Hash evaluado: `37872ff7dbb08be833b92c0a4b6d1ca3152464a1` · fecha de commit: `2026-10-18T23:58:04-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche de Colombia). Selección con `--until=2026-10-19T04:59:59Z`.
- Observación S12: `2026-10-19T21:35:00Z`; estado observado, no cierre ni calificación final.
- Commits de la rama entre cierres S10/S11: 24; posteriores al cierre hasta la punta observada: 0.
- Líneas de la matriz corresponden al hash evaluado; las de overall corresponden a la punta `37872ff7dbb08be833b92c0a4b6d1ca3152464a1`.

S12 queda abierta y puede cambiar hasta su cierre. No se penaliza como entrega final ni se evalúa aquí el taller de mensajes.

## Matriz de la ficha

| Criterio | Estado | Evidencia | Observación |
|---|---|---|---|
| Tabla operación a garantía de consistencia, con operaciones reales | No cumple | [docs/arc42/08-cross-cutting-concepts.md:55-113](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/08-cross-cutting-concepts.md#L55-L113); [docs/arc42/11-risks-and-technical-debt.md:68-75](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/11-risks-and-technical-debt.md#L68-L75) | Propiedad e idempotencia no sustituyen tabla de garantías de consistencia por operación. |
| Dos operaciones verificadas contra la implementación | Cumple | [docs/adr/0004-comunicacion-sincrona-frontend-backend.md:29,40-57](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0004-comunicacion-sincrona-frontend-backend.md#L29); [backend/app/requisitos/service.py:6-20](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/backend/app/requisitos/service.py#L6-L20) | Contrastadas consulta GET autoritativa desde BD y PUT absoluto con commit antes de devolver. Satisface consistencia inmediata declarada para ese flujo único; no se infiere aislamiento serializable ni ausencia de escrituras concurrentes perdidas. |
| Diseño de caché con qué, dónde y cuánto | No cumple | [docs/adr/0004-comunicacion-sincrona-frontend-backend.md:70-73](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0004-comunicacion-sincrona-frontend-backend.md#L70-L73); [docs/arc42/08-cross-cutting-concepts.md:1-114](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/08-cross-cutting-concepts.md#L1-L114) | Declara ausencia de caché local como limitación, no decisión razonada de no necesitar caché ni diseño qué/dónde/cuánto. |
| Política de invalidación tras escritura | No cumple | [backend/app/requisitos/service.py:13-20](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/backend/app/requisitos/service.py#L13-L20); [docs/arc42/08-cross-cutting-concepts.md:55-113](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/08-cross-cutting-concepts.md#L55-L113) | Falta regla tras PUT o justificación completa de no caché. Sin caché implementada, no se inventa un dato obsoleto comprobado. |
| Garantías del flujo por eventos, si existe | Cumple | [docs/adr/0004-comunicacion-sincrona-frontend-backend.md:29-32,43-57,67-68](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0004-comunicacion-sincrona-frontend-backend.md#L29-L32) | Justifica REST síncrono y no broker; alertas aún fuera del alcance implementado. |
| ADR de la decisión de datos más costosa de revertir | No cumple | Inventario `docs/adr/`; [docs/adr/0003-seleccion-motor-de-base-de-datos.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0003-seleccion-motor-de-base-de-datos.md) | Decisión de motor existente, sin identificarla y compararla como la más costosa de revertir. |
| Argumento de por qué esa decisión es la más costosa de revertir | No cumple | [docs/adr/0010-extraccion-de-modulo.md:23-59](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0010-extraccion-de-modulo.md#L23-L59); inventario ADR | Costo de extraer módulos no es argumento del mayor costo de reversión de datos. |
| Almacenes y brokers como contenedores propios en el C4 nivel 2 | Cumple | [docs/c4/contenedores.puml:11-23](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/c4/contenedores.puml#L11-L23) | SQLite local/CI y PostgreSQL desplegado como contenedores propios con tecnología; sin broker por decisión explícita. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/08-cross-cutting-concepts.md:1-114](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/08-cross-cutting-concepts.md#L1-L114) | Propiedad y contextos completos, pero no estrategias de consistencia y caché de S12. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia | Observación y límite |
|---|---|---|---|
| Repositorio público en organización y convención | Cumple | https://github.com/ISCOUTB/AS_202620_DinamikUTB; clon Git público exitoso; API actions/runs con SHA exacto | Visibilidad comprobada sin pedir acceso. |
| Estructura mínima presente | Cumple | Árbol del hash; [docs/arc42/01-introduction-and-goals.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/01-introduction-and-goals.md) a `12-glossary.md`; `docs/adr/`, `docs/c4/`, [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/aspectos.md), [docs/ia.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/ia.md), `README.md` | Rutas mínimas y doce secciones presentes. |
| Estado evaluado identificable | Cumple | `origin/master` · `37872ff7dbb08be833b92c0a4b6d1ca3152464a1` · `2026-10-18T23:58:04-05:00` | S11 histórico y S12 preliminar no se mezclan. |
| Nombres ADR según convención | Cumple | Inventario `docs/adr/` del hash evaluado | Archivos de decisiones con numeración de cuatro dígitos y kebab-case. |
| ADR aceptados no reescritos | No cumple | `bc70d93`; [docs/adr/0002-seleccion-tecnologia-backend-frontend.md:4,117-133](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/adr/0002-seleccion-tecnologia-backend-frontend.md#L4) | El padre ya estaba aceptado y el commit añadió trazabilidad al archivo; es hallazgo histórico del contrato, no descuento adicional en S11. |
| Registro IA al día para la semana | No cumple | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/ia.md); historial de la punta | No hay entrada S12 específica al momento observado. Es un pendiente preliminar, no cierre. |
| Pipeline, SonarCloud y Quality Gate públicos | No verificado | .github/workflows/; consulta actions/runs exacta descrita abajo | Run CI del SHA exacto exitoso: https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/39202115357 . [.github/workflows/ci.yml:29-30,49-53,55-78](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/.github/workflows/ci.yml#L29-L30) incluye pruebas y scanner; `sonar-project.properties:1-2` identifica isco-utb. Consulta pública del Quality Gate HTTP 403; no se pudo verificar el estado/fecha del análisis público. Un run verde no sustituye ese dato. |
| Sin credenciales en repositorio e historial | No verificado | Barrido git grep de patrones CONTRATO §9 en `37872ff7dbb08be833b92c0a4b6d1ca3152464a1` y punta; `git log -S"BEGIN PRIVATE KEY"` en la rama | Sin claves privadas ni tokens inequívocos en patrones revisados; coincidencias de configuración, tipos y ejemplos no prueban filtración. No se certifica todo el historial de todas las clases de secretos con un único patrón. Completar auditoría especializada sin publicar valores. |
| Contribución de todos los integrantes | No verificado | `git shortlog -sn 37872ff7dbb08be833b92c0a4b6d1ca3152464a1` contrastado con EQUIPOS.md | Hay actividad de varios autores y alias. No se atribuyen por parecido ni se publica identidad. Falta corroborar documentalmente cada alias y la contribución sustantiva código/documentación por integrante; no inferir ausencia por conteo bruto. |

## Recuento y nota sugerida

**3/9 Cumple. Nota sugerida: 2.3 = 1 + 4 × (3/9), propuesta al docente; la nota final se fija en Moodle.** Propuesta PRELIMINAR de avance S12, nunca nota final. La matriz transversal no entra en la fórmula.

## overall · estado actual y erosión arquitectónica

Sin commits posteriores al cierre. El código de resiliencia coincide con arc42 y ADR-0010; el acceso SQL revisado permanece en el servicio dueño de Requisito. Hay deuda explícita, no microservicios obligatorios: sin autenticación en lectura/escritura y riesgo de última escritura gana, documentados en [docs/arc42/11-risks-and-technical-debt.md:11-12,51](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/11-risks-and-technical-debt.md#L11-L12). SQLite en CI frente a PostgreSQL desplegado exige validación adicional ([backend/app/core/database.py:16-22](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/backend/app/core/database.py#L16-L22)). El mapa describe módulos todavía vacíos con ese límite explícito ([docs/arc42/08-cross-cutting-concepts.md:49-53](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/docs/arc42/08-cross-cutting-concepts.md#L49-L53)); no tratarlos como implementación. Fecha de recreación de BD antes del 25/10 declarada por el equipo en §11.2: comprobar operativamente, sin asumir estado del proveedor.

## CI, pruebas y límites

Run CI del SHA exacto exitoso: https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/39202115357 . [.github/workflows/ci.yml:29-30,49-53,55-78](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/.github/workflows/ci.yml#L29-L30) incluye pruebas y scanner; `sonar-project.properties:1-2` identifica isco-utb. Consulta pública del Quality Gate HTTP 403; no se pudo verificar el estado/fecha del análisis público. Un run verde no sustituye ese dato.

Se hizo una sola consulta GitHub actions/runs por equipo con head_sha de la punta y sin filtro de evento; se distingue push de pull_request. Los resultados encontrados son de push. No se usó un wrapper limitado a PR ni se interpretó una lista vacía como ausencia de CI.

Leídas pruebas [backend/tests/test_idempotencia.py:23-55](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/37872ff7dbb08be833b92c0a4b6d1ca3152464a1/backend/tests/test_idempotencia.py#L23-L55); F1/F2 tienen pruebas declaradas del cliente. No ejecuté pytest, flutter analyze/test, servidor ni PostgreSQL. El test llamado última escritura gana usa dos peticiones secuenciales: no prueba carrera concurrente. La suite CI verde sí corresponde al SHA observado.

Se leyeron artefactos pertinentes completos por partes y código de integración; búsquedas solo localizaron evidencia. No se ejecutaron scripts de estudiantes ni se abrieron/ejecutaron PDF. Se conservaron hallazgos históricos sin recalificar semanas anteriores.

## Pendientes accionables

Conservar la distinción entre diseño y ejecución. Medir arranque frío real y concurrencia, probar en PostgreSQL y atender autenticación antes de datos reales. S12: tabla operación/garantía, decisión argumentada sobre caché e invalidación y ADR del mayor costo de reversión.
