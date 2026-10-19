# EnAgenda · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_EnAgenda/tree/4bec22f3821493014e8352ece8274bb2950e97db) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA · estado histórico al cierre S11.**

- Repositorio público: https://github.com/ISCOUTB/AS_202620_EnAgenda
- Rama observada: `origin/master`. Estado evaluado: `4bec22f3821493014e8352ece8274bb2950e97db` (2026-10-11T23:47:24-05:00).
- Cierre S11 exclusivo: 2026-10-19T05:00:00Z; solo commits con fecha de commit anterior. Observación S12/overall: 2026-10-19T21:35:00Z.
- Actividad: 0 commits en [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 posteriores al cierre hasta la observación. Selección por git sobre la rama principal, sin etiquetas.

## Matriz de cumplimiento

| Criterio | Estado | Evidencia y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [app/web.py:22-35,427-517](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L22-L35) y [src/invitaciones/aplicacion/gestionar_invitacion.py:16-60](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/src/invitaciones/aplicacion/gestionar_invitacion.py#L16-L60): integración HTTP → casos de uso → repositorio de invitaciones identificable. |
| Tabla de modos de fallo con no responde, responde tarde y responde dos veces | No cumple | [docs/arc42/11-riesgos-y-deuda-técnica.md:7-38](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L7-L38): riesgos generales y de consistencia, sin tabla no responde/tarde/dos veces de esta integración. |
| Mitigación asignada a cada modo de fallo | No cumple | [docs/arc42/11-riesgos-y-deuda-técnica.md:9-30](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L9-L30): mitigaciones genéricas de límites y estado vigente no asignan respuesta a cada uno de los tres fallos HTTP. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | No cumple | [app/web.py:238-345,427-517](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L238-L345) y `gestionar_invitacion.py:16-60`: existen validaciones y errores, pero falta matriz que distinga mitigaciones implementadas y pendientes con plan por modo. La deuda de persistencia `arc42/11*:58-68` sí es un pendiente declarado válido, aunque no resuelve por sí sola esta fila. |
| Diseño de idempotencia o saga, o argumento de por qué no aplica | No cumple | `gestionar_invitacion.py:16-28,45-60` crea y responde; [app/web.py:306-339](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L306-L339) puede repetir creaciones. [docs/arc42/11-riesgos-y-deuda-técnica.md:25-30](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L25-L30) pide un estado vigente, pero no diseña deduplicación/reintento ni explica no aplicabilidad. |
| ADR con la decisión de extraer o no extraer, y sus criterios | No cumple | [docs/adr/0001-usar-monolito-modular.md:147-157](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L147-L157) deja extracción para evaluación futura. Inventario de tres ADR: estilo, HTTP y Dokploy; no contiene decisión S11 de extracción con criterios aplicada a un módulo. |
| La alternativa no extraer aparece evaluada, no omitida | No cumple | [docs/adr/0001-usar-monolito-modular.md:30-108](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L30-L108) compara capas, hexagonal y monolito; no evalúa explícitamente extraer/no extraer un módulo de la integración actual. |
| arc42 sección 11 con los modos de fallo | No cumple | [docs/arc42/11-riesgos-y-deuda-técnica.md:1-105](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L1-L105) describe riesgos generales y deuda; faltan los tres modos parciales exigidos. |
| Filas de aspectos afectadas por la integración, al día | No cumple | [docs/aspectos.md:5-12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/aspectos.md#L5-L12) enlaza funcionalidades y contrato, pero no incorpora fallos parciales, mitigaciones o diseño de idempotencia de la integración; las filas siguen remitiendo solo al ADR de estilo. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y límites |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon git público exitoso de `https://github.com/ISCOUTB/AS_202620_EnAgenda.git`; API actions/runs sin autenticación HTTP 200. |
| Estructura mínima presente | Cumple | `git ls-tree -r` en el hash citado: README, código, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md presentes. arc42 contiene secciones 01–12; nombres con espacios/acentos no eliminan los artefactos. |
| Estado calificado identificable | Cumple | `git log -1 --until=2026-10-19T04:59:59Z origin/master` fija S11; punta observada fija S12. Hash y fecha completos arriba. |
| Nombres de ADR según la convención | Cumple | `git ls-tree --name-only` de docs/adr: archivos de decisión NNNN-kebab-case.md; archivos auxiliares .gitkeep no cuentan como decisiones. |
| ADR aceptados no reescritos | No cumple | [docs/adr/0003-desplegar-api-flask-en-render.md:1-4,54-77](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0003-desplegar-api-flask-en-render.md#L1-L4) en f7bc011 estaba aceptado; `git log --name-status` registra su eliminación en 1da7fb9 y reutilización del número 0003 para Dokploy, completado en 02940e0. Falta conservar la decisión previa marcada como reemplazada y enlazar un ADR nuevo. |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:43-47](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/ia.md#L43-L47): últimas entradas de 04-Oct; último commit del archivo c2077ac (05-Oct), anterior a ambas ventanas. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | API pública actions/runs HTTP 200, una consulta; run [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/38205222318) success con head_sha `4bec22f3821493014e8352ece8274bb2950e97db`. [.github/workflows/ci.yml:1-45](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/.github/workflows/ci.yml#L1-L45) no contiene SonarCloud; faltan configuración/scanner, análisis público y Quality Gate. El run de Pages no se usó como prueba de tests. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Inspección de configuración y ejemplos no identifica una credencial activa; no se certifica ausencia absoluta en todo el historial. Escaneo exhaustivo de blobs/historial pendiente de completar; no se reproducen valores sospechosos. Debe cerrarse con escaneo redactado del historial, no solo del árbol actual. |
| Contribución de todos los integrantes | No verificado | Historial git y listado institucional contrastados: tres integrantes observables tras consolidar aliases por correo coincidente y, donde existe, .mailmap. No se publican identidades. La presencia histórica no demuestra reparto sustantivo de código/documentación en esta semana sin actividad. |

## Recuento y nota sugerida

**1/9 criterios Cumple. Nota sugerida: 1.4/5.0**, calculada como 1 + 4 × (1/9), propuesta al docente autorizada por la ficha. La nota final la fija el profesor en Moodle. La transversal no entra en el cálculo. La condición definitiva corresponde al estado histórico revisado, no sustituye la decisión docente.

## overall · punta actual de la misma rama

Punta: `4bec22f3821493014e8352ece8274bb2950e97db`.

La punta de `origin/master` coincide con el estado histórico: no hay commits en S11 ni en el avance observado S12. El CI del hash exacto es exitoso, pero [.github/workflows/ci.yml:1-45](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/.github/workflows/ci.yml#L1-L45) solo ejecuta pytest/contrato y build Docker; no contiene scanner ni Quality Gate de SonarCloud.

Erosión arquitectónica: [docs/adr/0001-usar-monolito-modular.md:94-95,116-122](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L94-L95) todavía prescribe Next.js/Server Actions y ausencia de API, mientras [app/web.py:427-517](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L427-L517) implementa Flask y API JSON. [docs/arc42/11-riesgos-y-deuda-técnica.md:70-79](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L70-L79) mantiene el despliegue como pendiente, aunque ADR-0003 ya documenta Dokploy. El repositorio en memoria (`repositorio_memoria.py:4-12`) pierde estado al reiniciar; es deuda reconocida, no persistencia durable. [app/web.py:306-339](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L306-L339) valida y guarda dentro del mismo bucle: un invitado inválido posterior deja altas previas realizadas, sin atomicidad de lote. La capa aplicación depende de la implementación concreta de infraestructura (`gestionar_invitacion.py:7-14`).

## Pendientes y límites de verificación

Completar modos no responde/tarde/duplicado y su correspondencia, ampliar idempotencia a operaciones repetibles reales, y mantener la decisión razonada de no extraer sin exigir microservicios. Un pendiente con plan es aceptable en S11; una intención sin alcance o una afirmación de implementación contradicha por código no lo es. Para S12, añadir tabla de garantías con dos operaciones contrastadas, invalidación tras escritura y ADR comparativo de costo de reversión; sincronizar arc42 §8.

No se ejecutó código estudiantil, pruebas, contenedores, scripts ni PDFs. Comandos no ejecutados: `python -m pytest`, `docker compose up --build`. Las pruebas leídas ([tests/test_invitaciones.py:22-116](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/tests/test_invitaciones.py#L22-L116), [tests/test_api_invitaciones.py:45-96](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/tests/test_api_invitaciones.py#L45-L96)) cubren vigencia, estados y HTTP, no prueban los tres fallos de transporte ni atomicidad del lote. El run exacto acredita CI, no una nueva ejecución local ni comportamiento distribuido.
