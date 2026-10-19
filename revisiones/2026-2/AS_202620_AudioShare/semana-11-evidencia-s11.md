# AudioShare · Evidencia S11 · DEFINITIVA, estado histórico al cierre

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_AudioShare/tree/a0834d568625bca8094c17b736d93978ad812430) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

- Repositorio público: https://github.com/ISCOUTB/AS_202620_AudioShare
- Rama seleccionada: `origin/master` (HEAD remoto); no se usaron etiquetas ni ramas de trabajo.
- Hash evaluado: `a0834d568625bca8094c17b736d93978ad812430` · fecha de commit: `2026-10-18T23:16:26-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche de Colombia). Selección con `--until=2026-10-19T04:59:59Z`.
- Observación S12: `2026-10-19T21:35:00Z`; estado observado, no cierre ni calificación final.
- Commits de la rama entre cierres S10/S11: 25; posteriores al cierre hasta la punta observada: 2.
- Líneas de la matriz corresponden al hash evaluado; las de overall corresponden a la punta `1af6e5ca727e60ef64cda6e31af71ab73bc9c9da`.

## Matriz de la ficha

| Criterio | Estado | Evidencia | Observación |
|---|---|---|---|
| Integración principal identificada en el código | Cumple | [lib/core/network/api_client.dart:53-98](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/lib/core/network/api_client.dart#L53-L98); [src/app.ts:157-270](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/src/app.ts#L157-L270) | Cliente HTTP/NDJSON, servidor y distribución PLAY están localizados. |
| Tabla de modos de fallo con no responde, responde tarde y responde dos veces | Cumple | [docs/modos-de-fallo.md:32-46](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/modos-de-fallo.md#L32-L46) | FM-13 cubre falta de respuesta; FM-06/11 llegada tardía; FM-04/07 repetición. Casos específicos del sistema, no catálogo genérico. |
| Mitigación asignada a cada modo de fallo | Cumple | [docs/modos-de-fallo.md:30-59](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/modos-de-fallo.md#L30-L59) | Cada caso tiene mitigación y orden de trabajo. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | Cumple | [src/app.ts:65-77,203-216](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/src/app.ts#L65-L77); [lib/core/network/api_client.dart:70-98](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/lib/core/network/api_client.dart#L70-L98); [docs/modos-de-fallo.md:23-24,48-59](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/modos-de-fallo.md#L23-L24) | FM-01/02 implementados; timeout/reintento e idempotencia restantes reconocidos como pendientes con plan. Esa transparencia satisface S11; no se exige terminarlos. |
| Diseño de idempotencia o saga, o argumento de por qué no aplica | Cumple | [docs/idempotencia-y-saga.md:3-35,45-121](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/idempotencia-y-saga.md#L3-L35) | Diseño por operación, clave natural, estados, orden de efectos y saga no aplicable hoy; no se confunde diseño con implementación. |
| ADR con la decisión de extraer o no extraer, y sus criterios | Cumple | [docs/adr/0009-no-extraer-modulos-como-servicios.md:25-110](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/adr/0009-no-extraer-modulos-como-servicios.md#L25-L110) | Decisión de conservar proceso único, costo de distribución y disparadores de revisión. |
| La alternativa no extraer aparece evaluada, no omitida | Cumple | [docs/adr/0009-no-extraer-modulos-como-servicios.md:49-88](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/adr/0009-no-extraer-modulos-como-servicios.md#L49-L88) | Mantener monolito evaluado frente a extraer Sync/Audio. |
| arc42 sección 11 con los modos de fallo | No cumple | [docs/arc42/arc42-template.adoc:72-74](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/arc42/arc42-template.adoc#L72-L74); árbol del hash S11 | La sección 11 referenciada no existe. El análisis independiente es útil, pero no está incorporado en riesgos y deuda de arc42. |
| Filas de aspectos afectadas por la integración, al día | Cumple | [docs/aspectos.md:38-43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/aspectos.md#L38-L43) | Fila principal enlaza ADR-0009, integración y pruebas de fallos; otras métricas y pruebas físicas están honestamente pendientes. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia | Observación y límite |
|---|---|---|---|
| Repositorio público en organización y convención | Cumple | https://github.com/ISCOUTB/AS_202620_AudioShare; clon Git público exitoso; API actions/runs con SHA exacto | Visibilidad comprobada sin pedir acceso. |
| Estructura mínima presente | No cumple | [docs/arc42/arc42-template.adoc:72-74](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/arc42/arc42-template.adoc#L72-L74); árbol S11/actual | Rutas principales presentes, pero falta sección 11; arc42 está en AsciiDoc, desviación de formato respecto al Markdown solicitado. |
| Estado evaluado identificable | Cumple | `origin/master` · `a0834d568625bca8094c17b736d93978ad812430` · `2026-10-18T23:16:26-05:00` | S11 histórico y S12 preliminar no se mezclan. |
| Nombres ADR según convención | Cumple | Inventario `docs/adr/` del hash evaluado | Archivos de decisiones con numeración de cuatro dígitos y kebab-case. |
| ADR aceptados no reescritos | No cumple | `8f1f1d5`; [docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md:3,66-76](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/adr/0007-correccion-de-reloj-y-ack-de-arranque.md#L3) | El padre ya declaraba aceptado y el diff añade/reescribe consecuencias; no hay ADR sustituto para ese cambio. |
| Registro IA al día para la semana | No cumple | [docs/ia.md:122](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/docs/ia.md#L122) | Registro S11 explícito, pero dice que no incluye propuestas rechazadas; los rechazos antiguos no cubren esta semana. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | .github/workflows/; consulta actions/runs exacta descrita abajo | CI de punta exitoso: https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270 ; también Flutter y publicación exitosos. [.github/workflows/ci.yml:18-23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/a0834d568625bca8094c17b736d93978ad812430/.github/workflows/ci.yml#L18-L23) invoca scanner; `sonar-project.properties:1-2` usa una organización distinta de isco-utb. Consulta pública de Quality Gate devolvió HTTP 403; no se acredita Gate público. La consulta head_sha no prueba CI del hash histórico S11. |
| Sin credenciales en repositorio e historial | No verificado | Barrido git grep de patrones CONTRATO §9 en `a0834d568625bca8094c17b736d93978ad812430` y punta; `git log -S"BEGIN PRIVATE KEY"` en la rama | Sin claves privadas ni tokens inequívocos en patrones revisados; coincidencias de configuración, tipos y ejemplos no prueban filtración. No se certifica todo el historial de todas las clases de secretos con un único patrón. Completar auditoría especializada sin publicar valores. |
| Contribución de todos los integrantes | No verificado | `git shortlog -sn a0834d568625bca8094c17b736d93978ad812430` contrastado con EQUIPOS.md | Hay actividad de varios autores y alias. No se atribuyen por parecido ni se publica identidad. Falta corroborar documentalmente cada alias y la contribución sustantiva código/documentación por integrante; no inferir ausencia por conteo bruto. |

## Recuento y nota sugerida

**8/9 Cumple. Nota sugerida: 4.6 = 1 + 4 × (8/9), propuesta al docente; la nota final se fija en Moodle.** Resultado definitivo de esta revisión histórica S11; la propuesta no reemplaza la decisión docente. La matriz transversal no entra en la fórmula.

## overall · estado actual y erosión arquitectónica

Dos commits posteriores al cierre incorporan reproducción de pista y posición de pausa/reanudación. [src/app.ts:239-252,302-315,365-382](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L239-L252) y [tests/resume-position.test.ts:1-61](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/tests/resume-position.test.ts#L1-L61) en punta muestran el cambio, sin mejorar retrospectivamente S11. Erosión vigente: [src/app.ts:57-64](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/src/app.ts#L57-L64) concentra mapas de Sync y streams; Session persiste `start_at` (`sqlite-room-repository.ts:35-41,131-147`) aunque arc42 §8 atribuye ese dato a Sync. La documentación sigue describiendo audio simulado y pausa desde cero ([docs/arc42/src/08_concepts.adoc:103-106](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/arc42/src/08_concepts.adoc#L103-L106); [docs/modos-de-fallo.md:39](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/modos-de-fallo.md#L39)), desactualizada frente a la punta. Repetir PLAY aún vuelve a llamar `sync.start`, no es deduplicación por estado. Falta sección 11 de arc42.

## CI, pruebas y límites

CI de punta exitoso: https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270 ; también Flutter y publicación exitosos. [.github/workflows/ci.yml:18-23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/.github/workflows/ci.yml#L18-L23) invoca scanner; `sonar-project.properties:1-2` usa una organización distinta de isco-utb. Consulta pública de Quality Gate devolvió HTTP 403; no se acredita Gate público. La consulta head_sha no prueba CI del hash histórico S11.

Se hizo una sola consulta GitHub actions/runs por equipo con head_sha de la punta y sin filtro de evento; se distingue push de pull_request. Los resultados encontrados son de push. No se usó un wrapper limitado a PR ni se interpretó una lista vacía como ausencia de CI.

Existen [tests/failure-modes.test.ts:161-234](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/tests/failure-modes.test.ts#L161-L234) para reconexión y reinicio. Los demás casos se separan como pruebas propuestas en [docs/modos-de-fallo.md:94-108](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/docs/modos-de-fallo.md#L94-L108). No ejecuté npm, Flutter, servidor, pruebas, contenedores ni dispositivos; CI observado de la punta no acredita reproducción de todos los fallos.

Se leyeron artefactos pertinentes completos por partes y código de integración; búsquedas solo localizaron evidencia. No se ejecutaron scripts de estudiantes ni se abrieron/ejecutaron PDF. Se conservaron hallazgos históricos sin recalificar semanas anteriores.

## Pendientes accionables

Incorporar los modos en arc42 §11; mantener separados diseño e implementación; completar timeout, ACK correlacionado, reconexión y pruebas pendientes. Para S12: tabla de consistencia, garantías de eventos, invalidación de `/track` y ADR de datos con costo comparado de reversión.
