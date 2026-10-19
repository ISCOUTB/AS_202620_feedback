# Clubs_UTB · Evidencia S12 · PRELIMINAR, avance no final

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/tree/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

- Repositorio público: https://github.com/ISCOUTB/AS_202620_Clubs_UTB
- Rama seleccionada: `origin/master` (HEAD remoto); no se usaron etiquetas ni ramas de trabajo.
- Hash evaluado: `1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f` · fecha de commit: `2026-10-18T20:35:24-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche de Colombia). Selección con `--until=2026-10-19T04:59:59Z`.
- Observación S12: `2026-10-19T21:35:00Z`; estado observado, no cierre ni calificación final.
- Commits de la rama entre cierres S10/S11: 18; posteriores al cierre hasta la punta observada: 0.
- Líneas de la matriz corresponden al hash evaluado; las de overall corresponden a la punta `1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f`.

S12 queda abierta y puede cambiar hasta su cierre. No se penaliza como entrega final ni se evalúa aquí el taller de mensajes.

## Matriz de la ficha

| Criterio | Estado | Evidencia | Observación |
|---|---|---|---|
| Tabla operación a garantía de consistencia, con operaciones reales | No cumple | [docs/arc42/08_conceptos_transversales.md:1-73](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/arc42/08_conceptos_transversales.md#L1-L73); [docs/adr/0008-no-extraer-publicaciones.md:24-26,54-63](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/adr/0008-no-extraer-publicaciones.md#L24-L26) | No hay tabla operación → garantía; afirmar transacción PostgreSQL no representa el adaptador conectado. |
| Dos operaciones verificadas contra la implementación | No cumple | [backend/src/linkclub/adapters/inbound/api/publicacion_router.py:15-16,61-88](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/backend/src/linkclub/adapters/inbound/api/publicacion_router.py#L15-L16); [backend/src/linkclub/adapters/outbound/persistence/in_memory_publicacion_adapter.py:9-14](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/backend/src/linkclub/adapters/outbound/persistence/in_memory_publicacion_adapter.py#L9-L14) | Crear y listar publicaciones usan lista en memoria, no transacción persistente. No se sostienen garantías de PostgreSQL ni sobreviven reinicios. |
| Diseño de caché con qué, dónde y cuánto | No cumple | [docs/arc42/08_conceptos_transversales.md:1-73](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/arc42/08_conceptos_transversales.md#L1-L73) | No se encontró diseño qué/dónde/cuánto ni justificación explícita de no caché. |
| Política de invalidación tras escritura | No cumple | [backend/src/linkclub/adapters/outbound/persistence/in_memory_publicacion_adapter.py:9-14](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/backend/src/linkclub/adapters/outbound/persistence/in_memory_publicacion_adapter.py#L9-L14); [docs/arc42/08_conceptos_transversales.md:1-73](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/arc42/08_conceptos_transversales.md#L1-L73) | No hay política de caché tras crear publicación. Definirla o justificar no caché; no se inventa un defecto de invalidación sobre una caché inexistente. |
| Garantías del flujo por eventos, si existe | Cumple | `docs/adr/0003- integacion rest openapi.md:14-22,30-47` | Mensajería diferida por falta de consumidor/transporte; integración REST síncrona. No se exige implementar eventos. |
| ADR de la decisión de datos más costosa de revertir | No cumple | Inventario `docs/adr/`; [docs/adr/0008-no-extraer-publicaciones.md:51-67](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/adr/0008-no-extraer-publicaciones.md#L51-L67) | ADR de despliegue/extracción no identifica la decisión de datos más costosa de revertir. |
| Argumento de por qué esa decisión es la más costosa de revertir | No cumple | [docs/adr/0008-no-extraer-publicaciones.md:22-29](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/adr/0008-no-extraer-publicaciones.md#L22-L29) | Costos de extraer descritos, sin comparación de reversión de decisiones de datos. |
| Almacenes y brokers como contenedores propios en el C4 nivel 2 | No cumple | [docs/c4/contexto.md:22-48](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/c4/contexto.md#L22-L48); [backend/src/linkclub/adapters/inbound/api/publicacion_router.py:15-16](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/backend/src/linkclub/adapters/inbound/api/publicacion_router.py#L15-L16) | Agrupa Auth y PostgreSQL en Supabase externo, no representa almacén real en memoria ni PostgreSQL/Dokploy separado con estado claro. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/08_conceptos_transversales.md:1-73](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/arc42/08_conceptos_transversales.md#L1-L73) | Lenguaje y contextos, sin estrategia de consistencia/caché. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia | Observación y límite |
|---|---|---|---|
| Repositorio público en organización y convención | Cumple | https://github.com/ISCOUTB/AS_202620_Clubs_UTB; clon Git público exitoso; API actions/runs con SHA exacto | Visibilidad comprobada sin pedir acceso. |
| Estructura mínima presente | Cumple | Árbol del hash; [docs/arc42/01_introduccion_y_metas.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/arc42/01_introduccion_y_metas.md) a `12_glosario.md`; `docs/adr/`, [docs/c4/contexto.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/c4/contexto.md), [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/aspectos.md), [docs/ia.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/ia.md), `README.md` | Las seis rutas mínimas están presentes; calidad y enlaces se evalúan por separado. |
| Estado evaluado identificable | Cumple | `origin/master` · `1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f` · `2026-10-18T20:35:24-05:00` | S11 histórico y S12 preliminar no se mezclan. |
| Nombres ADR según convención | No cumple | Inventario `docs/adr/` del hash evaluado | `0003- integacion rest openapi.md` contiene espacios; corregir sin perder historial. |
| ADR aceptados no reescritos | No cumple | `c6c46e3`; [docs/adr/0001-hexagonal.md:2-3,36-42](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/adr/0001-hexagonal.md#L2-L3) | ADR ya aceptado en el padre; se añadió trazabilidad al mismo archivo. Conservar ADR aceptado y registrar cambios mediante sustitución. |
| Registro IA al día para la semana | No cumple | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/ia.md); historial de la punta | No hay entrada S12 específica al momento observado. Es un pendiente preliminar, no cierre. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/; consulta actions/runs exacta descrita abajo | Dos runs push del SHA exacto fallaron: https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186049497 y https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186048698 . [.github/workflows/backend-tests.yml:26-30](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/.github/workflows/backend-tests.yml#L26-L30) y `contrato.yml:19-36` prueban backend/contrato; no hay invocación SonarCloud ni configuración de análisis identificada. |
| Sin credenciales en repositorio e historial | No verificado | Barrido git grep de patrones CONTRATO §9 en `1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f` y punta; `git log -S"BEGIN PRIVATE KEY"` en la rama | Sin claves privadas ni tokens inequívocos en patrones revisados; coincidencias de configuración, tipos y ejemplos no prueban filtración. No se certifica todo el historial de todas las clases de secretos con un único patrón. Completar auditoría especializada sin publicar valores. |
| Contribución de todos los integrantes | No verificado | `git shortlog -sn 1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f` contrastado con EQUIPOS.md | Hay actividad de varios autores y alias. No se atribuyen por parecido ni se publica identidad. Falta corroborar documentalmente cada alias y la contribución sustantiva código/documentación por integrante; no inferir ausencia por conteo bruto. |

## Recuento y nota sugerida

**1/9 Cumple. Nota sugerida: 1.4 = 1 + 4 × (1/9), propuesta al docente; la nota final se fija en Moodle.** Propuesta PRELIMINAR de avance S12, nunca nota final. La matriz transversal no entra en la fórmula.

## overall · estado actual y erosión arquitectónica

La punta no cambió después del cierre. Erosión: [docs/adr/0008-no-extraer-publicaciones.md:24-26](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/docs/adr/0008-no-extraer-publicaciones.md#L24-L26) habla de transacción y FK actuales, pero router usa `InMemoryPublicacionAdapter` (`publicacion_router.py:15-16`) y `guardar` hace append (`in_memory_publicacion_adapter.py:9-11`). La llave viaja hasta la entidad sin deduplicar. [frontend/linkclub/lib/presentation/clubs_page.dart:15-91](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/frontend/linkclub/lib/presentation/clubs_page.dart#L15-L91) conserva datos hardcodeados y el C4 sigue apuntando a Supabase frente a la decisión Dokploy. El CI exacto está fallido; no se atribuye una causa concreta sin logs.

## CI, pruebas y límites

Dos runs push del SHA exacto fallaron: https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186049497 y https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/39186048698 . [.github/workflows/backend-tests.yml:26-30](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/1642a9c1a0a99ef766cd6e27460d9b8b8cd3312f/.github/workflows/backend-tests.yml#L26-L30) y `contrato.yml:19-36` prueban backend/contrato; no hay invocación SonarCloud ni configuración de análisis identificada.

Se hizo una sola consulta GitHub actions/runs por equipo con head_sha de la punta y sin filtro de evento; se distingue push de pull_request. Los resultados encontrados son de push. No se usó un wrapper limitado a PR ni se interpretó una lista vacía como ausencia de CI.

No ejecuté pytest, Flutter, SQL ni Terraform. No se acredita prueba de doble envío con persistencia por pasar una llave; lectura del adaptador muestra ausencia de deduplicación. El fallo de CI es observado, su diagnóstico exacto requiere logs.

Se leyeron artefactos pertinentes completos por partes y código de integración; búsquedas solo localizaron evidencia. No se ejecutaron scripts de estudiantes ni se abrieron/ejecutaron PDF. Se conservaron hallazgos históricos sin recalificar semanas anteriores.

## Pendientes accionables

Alinear tabla, arc42 §11 y aspectos con la integración real. Marcar idempotencia como pendiente y planificar deduplicación persistente/atómica y pruebas de repetición; corregir CI. S12 requiere matriz de consistencia, decisión de caché, C4 con estado real y ADR de datos.
