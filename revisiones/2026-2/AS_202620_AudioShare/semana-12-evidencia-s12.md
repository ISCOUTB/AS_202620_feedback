# AudioShare · Evidencia S12 · PRELIMINAR, avance no final

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_AudioShare/tree/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

- Repositorio público: https://github.com/ISCOUTB/AS_202620_AudioShare
- Rama seleccionada: `origin/master` (HEAD remoto); no se usaron etiquetas ni ramas de trabajo.
- Hash evaluado: `1af6e5ca727e60ef64cda6e31af71ab73bc9c9da` · fecha de commit: `2026-10-19T01:41:04-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche de Colombia). Selección con `--until=2026-10-19T04:59:59Z`.
- Observación S12: `2026-10-19T21:35:00Z`; estado observado, no cierre ni calificación final.
- Commits de la rama entre cierres S10/S11: 25; posteriores al cierre hasta la punta observada: 2.
- Líneas de la matriz corresponden al hash evaluado; las de overall corresponden a la punta `1af6e5ca727e60ef64cda6e31af71ab73bc9c9da`.

S12 queda abierta y puede cambiar hasta su cierre. No se penaliza como entrega final ni se evalúa aquí el taller de mensajes.

## Matriz de la ficha

| Criterio | Estado | Evidencia | Observación |
|---|---|---|---|
| Tabla operación a garantía de consistencia, con operaciones reales | No cumple | [docs/idempotencia-y-saga.md:26-35](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/idempotencia-y-saga.md#L26-L35); [docs/arc42/src/08_concepts.adoc:81-110](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc#L81-L110) | Tabla de idempotencia, sin tabla operación → garantía fuerte/eventual. |
| Dos operaciones verificadas contra la implementación | No cumple | [src/modules/session/infrastructure/persistence/sqlite-room-repository.ts:55-119,131-147](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/modules/session/infrastructure/persistence/sqlite-room-repository.ts#L55-L119); [src/app.ts:239-252](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L239-L252) | Crear sala tiene transacción y PLAY escribe estado y publica aparte. Se contrastaron ambas; falta declarar la garantía de consistencia de cada una, incluido fallo entre persistencia/publicación. |
| Diseño de caché con qué, dónde y cuánto | Cumple | [src/app.ts:365-382](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L365-L382) en punta actual | Caché HTTP de la pista `/track`: archivo MP3, caché pública de cliente/intermediario, max-age=3600. Diseño concreto visible en configuración. |
| Política de invalidación tras escritura | No cumple | [src/app.ts:365-382](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L365-L382); [docs/arc42/src/08_concepts.adoc:94-110](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc#L94-L110) | No hay política al reemplazar la pista en la misma URL: clientes pueden conservar audio anterior hasta una hora. Definir URL versionada o invalidación y su plan. |
| Garantías del flujo por eventos, si existe | No cumple | [docs/contracts/asyncapi.yaml:5-14,34-45](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/contracts/asyncapi.yaml#L5-L14); [docs/adr/0002-estrategia-integracion.md:52-63](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/adr/0002-estrategia-integracion.md#L52-L63) | Canal y desconexión descritos; no elige garantía de entrega ni supuestos de deduplicación/reentrega. No basta tener AsyncAPI. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0001-usar-monolito-modular.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/adr/0001-usar-monolito-modular.md); [docs/adr/0009-no-extraer-modulos-como-servicios.md:49-88](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/adr/0009-no-extraer-modulos-como-servicios.md#L49-L88); inventario ADR | No se identifica ADR específico de la decisión de datos más costosa de revertir. |
| Argumento de por qué esa decisión es la más costosa de revertir | No cumple | [docs/adr/0009-no-extraer-modulos-como-servicios.md:60-88](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/adr/0009-no-extraer-modulos-como-servicios.md#L60-L88) | Hay costos de extracción, pero no comparación que justifique cuál decisión de datos es la más costosa de revertir. |
| Almacenes y brokers como contenedores propios en el C4 nivel 2 | Cumple | `docs/c4/C4 Nivel 2 - Contenedores.mmd:45-67` | SQLite aparece como contenedor con tecnología; eventos van por NDJSON, no existe broker que deba inventarse. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/src/08_concepts.adoc:81-110](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc#L81-L110) | Documenta integración y persistencia general, no estrategia de consistencia y caché actual. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia | Observación y límite |
|---|---|---|---|
| Repositorio público en organización y convención | Cumple | https://github.com/ISCOUTB/AS_202620_AudioShare; clon Git público exitoso; API actions/runs con SHA exacto | Visibilidad comprobada sin pedir acceso. |
| Estructura mínima presente | No cumple | [docs/arc42/arc42-template.adoc:72-74](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/arc42-template.adoc#L72-L74); árbol S11/actual | Rutas principales presentes, pero falta sección 11; arc42 está en AsciiDoc, desviación de formato respecto al Markdown solicitado. |
| Estado evaluado identificable | Cumple | `origin/master` · `1af6e5ca727e60ef64cda6e31af71ab73bc9c9da` · `2026-10-19T01:41:04-05:00` | S11 histórico y S12 preliminar no se mezclan. |
| Nombres ADR según convención | Cumple | Inventario `docs/adr/` del hash evaluado | Archivos de decisiones con numeración de cuatro dígitos y kebab-case. |
| ADR aceptados no reescritos | No cumple | `8f1f1d5`; [docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md:3,66-76](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md#L3) | El padre ya declaraba aceptado y el diff añade/reescribe consecuencias; no hay ADR sustituto para ese cambio. |
| Registro IA al día para la semana | No cumple | [docs/ia.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/ia.md); historial de la punta | No hay entrada S12 específica al momento observado. Es un pendiente preliminar, no cierre. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/; consulta actions/runs exacta descrita abajo | CI de punta exitoso: https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270 ; también Flutter y publicación exitosos. [.github/workflows/ci.yml:18-23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/.github/workflows/ci.yml#L18-L23) invoca scanner; `sonar-project.properties:1-2` usa una organización distinta de isco-utb. Consulta pública de Quality Gate devolvió HTTP 403; no se acredita Gate público. La consulta head_sha no prueba CI del hash histórico S11. |
| Sin credenciales en repositorio e historial | No verificado | Barrido git grep de patrones CONTRATO §9 en `1af6e5ca727e60ef64cda6e31af71ab73bc9c9da` y punta; `git log -S"BEGIN PRIVATE KEY"` en la rama | Sin claves privadas ni tokens inequívocos en patrones revisados; coincidencias de configuración, tipos y ejemplos no prueban filtración. No se certifica todo el historial de todas las clases de secretos con un único patrón. Completar auditoría especializada sin publicar valores. |
| Contribución de todos los integrantes | No verificado | `git shortlog -sn 1af6e5ca727e60ef64cda6e31af71ab73bc9c9da` contrastado con EQUIPOS.md | Hay actividad de varios autores y alias. No se atribuyen por parecido ni se publica identidad. Falta corroborar documentalmente cada alias y la contribución sustantiva código/documentación por integrante; no inferir ausencia por conteo bruto. |

## Recuento y nota sugerida

**2/9 Cumple. Nota sugerida: 1.9 = 1 + 4 × (2/9), propuesta al docente; la nota final se fija en Moodle.** Propuesta PRELIMINAR de avance S12, nunca nota final. La matriz transversal no entra en la fórmula.

## overall · estado actual y erosión arquitectónica

Dos commits posteriores al cierre incorporan reproducción de pista y posición de pausa/reanudación. [src/app.ts:239-252,302-315,365-382](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L239-L252) y [tests/resume-position.test.ts:1-61](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/tests/resume-position.test.ts#L1-L61) en punta muestran el cambio, sin mejorar retrospectivamente S11. Erosión vigente: [src/app.ts:57-64](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L57-L64) concentra mapas de Sync y streams; Session persiste `start_at` (`sqlite-room-repository.ts:35-41,131-147`) aunque arc42 §8 atribuye ese dato a Sync. La documentación sigue describiendo audio simulado y pausa desde cero ([docs/arc42/src/08_concepts.adoc:103-106](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc#L103-L106); [docs/modos-de-fallo.md:39](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/modos-de-fallo.md#L39)), desactualizada frente a la punta. Repetir PLAY aún vuelve a llamar `sync.start`, no es deduplicación por estado. Falta sección 11 de arc42.

## CI, pruebas y límites

CI de punta exitoso: https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270 ; también Flutter y publicación exitosos. [.github/workflows/ci.yml:18-23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/.github/workflows/ci.yml#L18-L23) invoca scanner; `sonar-project.properties:1-2` usa una organización distinta de isco-utb. Consulta pública de Quality Gate devolvió HTTP 403; no se acredita Gate público. La consulta head_sha no prueba CI del hash histórico S11.

Se hizo una sola consulta GitHub actions/runs por equipo con head_sha de la punta y sin filtro de evento; se distingue push de pull_request. Los resultados encontrados son de push. No se usó un wrapper limitado a PR ni se interpretó una lista vacía como ausencia de CI.

Existen [tests/failure-modes.test.ts:161-234](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/tests/failure-modes.test.ts#L161-L234) para reconexión y reinicio. Los demás casos se separan como pruebas propuestas en [docs/modos-de-fallo.md:94-108](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/modos-de-fallo.md#L94-L108). No ejecuté npm, Flutter, servidor, pruebas, contenedores ni dispositivos; CI observado de la punta no acredita reproducción de todos los fallos.

Se leyeron artefactos pertinentes completos por partes y código de integración; búsquedas solo localizaron evidencia. No se ejecutaron scripts de estudiantes ni se abrieron/ejecutaron PDF. Se conservaron hallazgos históricos sin recalificar semanas anteriores.

## Pendientes accionables

Incorporar los modos en arc42 §11; mantener separados diseño e implementación; completar timeout, ACK correlacionado, reconexión y pruebas pendientes. Para S12: tabla de consistencia, garantías de eventos, invalidación de `/track` y ADR de datos con costo comparado de reversión.
