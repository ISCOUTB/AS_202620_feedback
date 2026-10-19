# EnAgenda · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_EnAgenda/tree/4bec22f3821493014e8352ece8274bb2950e97db) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR · avance S12, no calificación final.**

- Repositorio público: https://github.com/ISCOUTB/AS_202620_EnAgenda
- Rama observada: `origin/master`. Estado evaluado: `4bec22f3821493014e8352ece8274bb2950e97db` (2026-10-11T23:47:24-05:00).
- Cierre S11 exclusivo: 2026-10-19T05:00:00Z; solo commits con fecha de commit anterior. Observación S12/overall: 2026-10-19T21:35:00Z.
- Actividad: 0 commits en [2026-10-12T05:00Z, 2026-10-19T05:00Z); 0 posteriores al cierre hasta la observación. Selección por git sobre la rama principal, sin etiquetas.

## Matriz de cumplimiento

| Criterio | Estado | Evidencia y límites |
|---|---|---|
| Tabla operación a garantía de consistencia, con operaciones reales | No cumple | [docs/arc42/08-conceptos-transversales.md:3-52](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/08-conceptos-transversales.md#L3-L52): lenguaje y propiedad de datos, sin tabla operación/garantía. |
| Dos operaciones verificadas contra la implementación | No cumple | Contraste: crear (`gestionar_invitacion.py:16-28`) y responder (`:45-60`) escriben en `repositorio_memoria.py:4-12`. No hay garantía declarada, transacción ni coordinación entre procesos. La creación múltiple ([app/web.py:306-339](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L306-L339)) puede guardar parte del lote antes de un error de validación. |
| Diseño de caché con qué, dónde y cuánto | No cumple | [docs/arc42/08-conceptos-transversales.md:1-52](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/08-conceptos-transversales.md#L1-L52) y [docs/arc42/11-riesgos-y-deuda-técnica.md:58-68](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L58-L68): memoria es el almacén primario temporal, no diseño de caché. No se argumenta expresamente prescindir de caché para S12. |
| Política de invalidación tras escritura | No cumple | [src/invitaciones/infraestructura/repositorio_memoria.py:4-12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/src/invitaciones/infraestructura/repositorio_memoria.py#L4-L12): guarda/busca sin caché separada ni política de invalidación. Debe declarar no aplicabilidad razonada, o definir qué invalidar al responder una invitación; no se inventa un defecto de caché inexistente. |
| Garantías del flujo por eventos, si existe | Cumple | No aplica: [docs/adr/0002-estrategia-integracion-api.md:49-78](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0002-estrategia-integracion-api.md#L49-L78) descarta mensajería justificadamente y el flujo [app/web.py:427-517](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L427-L517) es síncrono. No se exige introducir eventos. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0001-usar-monolito-modular.md:106-157](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L106-L157), `0002-estrategia-integracion-api.md:72-97` y `0003-desplegar-api-flask-en-dokploy.md:64-99`: no existe decisión de datos seleccionada por costo de reversión. |
| Argumento de por qué esa decisión es la más costosa de revertir | No cumple | [docs/arc42/11-riesgos-y-deuda-técnica.md:58-68](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L58-L68) propone sustituir memoria, pero no compara costos de reversión de las decisiones de datos ni cuantifica o desglosa el costo elegido. |
| Almacenes y brokers como contenedores propios en el C4 nivel 2 | Cumple | [docs/c4/nivel-2-contenedores.md:13-24](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/c4/nivel-2-contenedores.md#L13-L24): almacén en memoria separado con tecnología Python y relaciones. No hay broker implementado; representar el módulo como contenedor es una imprecisión de granularidad aparte. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/08-conceptos-transversales.md:33-52](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/08-conceptos-transversales.md#L33-L52): propiedad exclusiva y estado vigente no sustituyen estrategia de consistencia ni caché/no caché justificada. |

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

**2/9 criterios Cumple. Nota sugerida: 1.9/5.0**, calculada como 1 + 4 × (2/9), propuesta al docente autorizada por la ficha. La nota final la fija el profesor en Moodle. La transversal no entra en el cálculo. Esta propuesta S12 es PRELIMINAR y puede cambiar hasta su cierre.

## overall · punta actual de la misma rama

Punta: `4bec22f3821493014e8352ece8274bb2950e97db`.

La punta de `origin/master` coincide con el estado histórico: no hay commits en S11 ni en el avance observado S12. El CI del hash exacto es exitoso, pero [.github/workflows/ci.yml:1-45](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/.github/workflows/ci.yml#L1-L45) solo ejecuta pytest/contrato y build Docker; no contiene scanner ni Quality Gate de SonarCloud.

Erosión arquitectónica: [docs/adr/0001-usar-monolito-modular.md:94-95,116-122](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/adr/0001-usar-monolito-modular.md#L94-L95) todavía prescribe Next.js/Server Actions y ausencia de API, mientras [app/web.py:427-517](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L427-L517) implementa Flask y API JSON. [docs/arc42/11-riesgos-y-deuda-técnica.md:70-79](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/docs/arc42/11-riesgos-y-deuda-t%C3%A9cnica.md#L70-L79) mantiene el despliegue como pendiente, aunque ADR-0003 ya documenta Dokploy. El repositorio en memoria (`repositorio_memoria.py:4-12`) pierde estado al reiniciar; es deuda reconocida, no persistencia durable. [app/web.py:306-339](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/app/web.py#L306-L339) valida y guarda dentro del mismo bucle: un invitado inválido posterior deja altas previas realizadas, sin atomicidad de lote. La capa aplicación depende de la implementación concreta de infraestructura (`gestionar_invitacion.py:7-14`).

## Pendientes y límites de verificación

Completar modos no responde/tarde/duplicado y su correspondencia, ampliar idempotencia a operaciones repetibles reales, y mantener la decisión razonada de no extraer sin exigir microservicios. Un pendiente con plan es aceptable en S11; una intención sin alcance o una afirmación de implementación contradicha por código no lo es. Para S12, añadir tabla de garantías con dos operaciones contrastadas, invalidación tras escritura y ADR comparativo de costo de reversión; sincronizar arc42 §8.

No se ejecutó código estudiantil, pruebas, contenedores, scripts ni PDFs. Comandos no ejecutados: `python -m pytest`, `docker compose up --build`. Las pruebas leídas ([tests/test_invitaciones.py:22-116](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/tests/test_invitaciones.py#L22-L116), [tests/test_api_invitaciones.py:45-96](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/4bec22f3821493014e8352ece8274bb2950e97db/tests/test_api_invitaciones.py#L45-L96)) cubren vigencia, estados y HTTP, no prueban los tres fallos de transporte ni atomicidad del lote. El run exacto acredita CI, no una nueva ejecución local ni comportamiento distribuido.
