# InvenTrack · Revisión técnica S16
**Rama:** `main` · [`51f353704cabdd0100c082d6af3912d18dc83795`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/51f353704cabdd0100c082d6af3912d18dc83795) · fecha Git 22/nov 23:37:59 COT. Candidato observado inmediatamente después del corte de referencia del 22 de noviembre, 23:59:59 COT; no certifica la entrega ni la hora efectiva de SAVIO. Comparación contra [S10 `539840be57f8a0b719bb33e19d05031489a25b86`](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/539840be57f8a0b719bb33e19d05031489a25b86): 203 archivos, +20475/−507. El documento del equipo contiene resultados sobre revisiones anteriores también; no se reasignan al SHA de cierre sin contraste.

**Alcance:** inspección estática de objetos Git fijados, CI público y, donde hubo URL, sondas HTTPS de lectura del 23/nov a las 13:27 UTC. No se ejecutó código del equipo ni se modificaron datos. No se verificó documento guía de SAVIO, asignación docente del desafío ni revisión servida; no se califica ni se infiere la sustentación. [Ficha S16](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/fichas/semana-16-final.md) · [Contrato](https://github.com/ISCOUTB/AS_202620_feedback/blob/master/CONTRATO.md).

**Publicación frente a CI:** [`README.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/README.md) L50–55, 322 y 462 separa API https://inventrack.iscoutb.dev (Dokploy) de cliente Flutter nativo, sin web independiente.

## Matriz S16
| Criterio | Estado y evidencia |
|---|---|
| Estado al cierre identificable | Cumple para candidato documental: rama, hash y captura indicados; entrega SAVIO por contrastar. |
| Despliegue estable | No verificado como estabilidad o SHA servido; se observó /health 200 (2,950 s), no prueba la operación integral. |
| Flujos con datos realistas | Parcial: [`docs/verificacion-final.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/verificacion-final.md) L80–94 reporta Gestión autenticada, alta/entrada/salida y SMTP; no se repitieron operaciones autenticadas o de escritura. [`app/inventario/infrastructure/cierres.py`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/app/inventario/infrastructure/cierres.py) sustenta conciliación en código. |
| Caminos de error | Parcial: /sesion sin credencial 401 (2,947 s) y ruta inexistente 404 (2,947 s); el documento reporta además 409 por stock y 503 previo, sin inferir caída actual. |
| Desafío final | No verificado como asignación docente. El equipo documenta conciliación por SKU: totales iguales de 35 ocultaban cuatro divergencias, y una venta posterior no modifica el cierre. [`docs/verificacion-final.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/verificacion-final.md) L23–27, [`tests/inventario/test_conciliacion_turno.py`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/tests/inventario/test_conciliacion_turno.py); no se rerun. |
| Alcance entregado frente a S10 | Parcial: S10 stock concurrente/observabilidad en memoria, S16 SQLite durable, autenticación, conciliación, proveedores y avisos. [`docs/arc42/arc42-template-EN.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/arc42/arc42-template-EN.md) §11 declara límites; [`docs/verificacion-final.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/verificacion-final.md) L94 distingue restauración con copia disponible y recuperación pública no medida. Sin documento guía no se certifica alcance completo. |
| ADR y evolución | Cumple: serie 0001–0024 permite seguir monolito, memoria, idempotencia, persistencia, autenticación, serialización y un solo despliegue. [`docs/adr/0024-usar-solo-dokploy-institucional.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/adr/0024-usar-solo-dokploy-institucional.md). |
| Decisión confirmada o reemplazada con evidencia | Cumple: [`docs/adr/0021-serializar-escrituras-sqlite.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/adr/0021-serializar-escrituras-sqlite.md) explica ajuste del escritor; [`docs/verificacion-final.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/verificacion-final.md) L61–78 registra variantes, tres corridas y comparación frente al perfil durable anterior. |
| Umbrales y atributos medidos | Cumple en ensayo delimitado: p95 escrituras 98,660/98,089/102,243 ms con umbral 400 ms; p95 lectura HTTP loopback 5,644/6,057/8,336 ms; 50 solicitudes sobre 40 unidades → 40 éxitos y 10 conflictos. Reproducibilidad descrita, no rendimiento producción ni confirmación independiente. [`docs/retos/comparacion-s16-final.json`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/retos/comparacion-s16-final.json). |
| Modos de fallo y mitigaciones probados | Cumple para pruebas de repositorio: [`tests/test_perfil_durable.py`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/tests/test_perfil_durable.py) y [`tests/test_gestion_integrada.py`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/tests/test_gestion_integrada.py) cubren restauración/idempotencia, autorización y alertas; ensayo de recuperación local 1,738 s con copia ya presente, no RTO del servicio remoto. |
| arc42 1–12 y glosario | Cumple estructura: [`docs/arc42/arc42-template-EN.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/arc42/arc42-template-EN.md) 1–12 y glosario L934; antecedentes de memoria deben leerse como perfil inicial, no perfil durable vigente. |
| C4 1–3 frente a código | Cumple sobre paquete actual: [`c4-actual/01-contexto.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/c4-actual/01-contexto.md), [`c4-actual/02-contenedores.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/c4-actual/02-contenedores.md), [`c4-actual/03-componentes.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/c4-actual/03-componentes.md); contrastar diferencias con Vistas C4 históricas en docs. |
| Trazabilidad de aspectos | Leídas 5/5 filas de [`docs/aspectos.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/aspectos.md) L15–21. ASP-01/02 stock y escrituras, ASP-03 métricas, ASP-04 auditoría/perfil durable, ASP-05 control de acceso remiten a código, pruebas y resultados. La descripción de broker simulado es histórica para una parte del sistema, no un broker productivo. |
| Validación automatizada | Cumple en run exacto: [`.github/workflows/test.yml`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/.github/workflows/test.yml) L37–38 invoca script de enlaces/trazabilidad; hay validación de contrato versionado y análisis estático. |
| Contribución sustantiva de todos | No verificado para el pleno: ocho firmas Git brutas, 343 commits del semestre ago–nov (99/125/59/60; otros dos fechados antes). [`docs/verificacion-final.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/verificacion-final.md) L98–107 documenta correspondencias y una provisional; confirmar con planilla y docente. Cambios de dominios, móvil, arquitectura y QA. |
| Revisión cruzada técnica | Parcial: [PR #15](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/15) y [PR #16](https://github.com/ISCOUTB/AS_202620_InvenTrack/pull/16) tienen registros humanos de comentario vacíos y comentarios automáticos; no se encontraron hilos de revisión sustantiva en la consulta. |
| Demo y sustentación | No verificado. Corresponde al docente y jurado ante la instancia desplegada; sin valoración C5. |

## Matriz transversal
| Criterio | Estado y evidencia |
|---|---|
| Convención y visibilidad | Cumple: [repositorio público](https://github.com/ISCOUTB/AS_202620_InvenTrack) de la organización. |
| Estructura mínima | Cumple: README, arc42, ADR, C4, aspectos e IA en el árbol. |
| Estado revisado identificable | Cumple para la referencia Git descrita; SAVIO pendiente. |
| Nombres ADR | Cumple patrón para los 24 ADR numerados. |
| Inmutabilidad ADR aceptados | No cumple históricamente según [`docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/adr/0009-consolidacion-inmutabilidad-adrs-previos.md); se distinguen ratificaciones de estado y política posterior de agregar sucesores. |
| Registro IA de cierre | Parcial: [`docs/ia.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/ia.md) actualizado el 22/nov, con entradas del cierre; resto del historial no se consolidó. |
| Pipeline, SonarCloud y Quality Gate | Cumple CI exacto en trabajos [45112590983](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/45112590983): flutter, test y dependencias. El workflow espera gate; ID de análisis público del SHA exacto no corroborado aparte, no usar el del SHA previo. |
| Credenciales en archivos e historial | No verificado para historial completo; pip-audit trata dependencias, no ausencia de secretos. |
| Contribución de todos | No verificado para el pleno: ocho firmas Git brutas, 343 commits del semestre ago–nov (99/125/59/60; otros dos fechados antes). [`docs/verificacion-final.md`](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/51f353704cabdd0100c082d6af3912d18dc83795/docs/verificacion-final.md) L98–107 documenta correspondencias y una provisional; confirmar con planilla y docente. Cambios de dominios, móvil, arquitectura y QA. |

## Preguntas para jurado
1. Dos SKU compensan faltantes y sobrantes con totales iguales: ¿cómo se conserva la foto del cierre ante movimientos posteriores?
2. Si el escritor SQLite se bloquea o llegan dos réplicas, ¿qué ocurre con timeouts, stock y claves idempotentes y qué probarían?
3. Si se pierde el host y no se descargó la copia, ¿qué RPO/RTO demostrarían desde cero y cómo evitarían alertas duplicadas al restaurar?

## Lectura cualitativa de rúbrica

C1 y C5 quedan pendientes de la verificación del aula y la defensa. No se asignan puntajes.

- **C2:** Sobresaliente en evidencia estática del repositorio: ADR-0021 vincula elección de escritor a variantes cuantificadas y reproducibles, en un ensayo acotado.
- **C3:** Sobresaliente en ensayos reportados: p95 con muestras, concurrencia, restauración y residuos explícitos; no equivale a alta disponibilidad, RTO público ni pruebas independientes.
- **C4:** Competente en coherencia; automatización de enlaces/contrato verificada y cinco trazas recorridas, pero falta reconciliar la descripción histórica de mensajería y el perfil actual en todas las vistas.

## Verificación independiente del corte y del despliegue

El historial de `origin/main` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.
[Diferencias frente a la revisión S10](https://github.com/ISCOUTB/AS_202620_InvenTrack/compare/539840be57f8a0b719bb33e19d05031489a25b86...51f353704cabdd0100c082d6af3912d18dc83795); es evidencia de cambio, no medida de mérito ni certificación de alcance acordado.

**Sondas de solo lectura del 23 de noviembre:**

- salud: [https://inventrack.iscoutb.dev/health](https://inventrack.iscoutb.dev/health) → HTTP 200, estado declarado `ok` (13:28:10 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
