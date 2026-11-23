# Evaluación técnica S16 · Tienda Virtual UTB

Fecha de lectura: 23 de noviembre de 2026. Revisión técnica previa a la sustentación. No se ejecutó código estudiantil ni se modificaron calificaciones. No se califican demostración ni C5. La asignación oficial del desafío final no se encontró acreditada en las fuentes leídas: no se sustituye por el escenario S10.

## Estado y corte

- Repositorio: https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB
- Rama de referencia: main.
- Candidato observado: [6bd72149d51f81285145bccf65719abcdba0dd42](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/6bd72149d51f81285145bccf65719abcdba0dd42); fecha de commit 2026-11-22T19:56:33Z.
- Cierre de referencia: 23 de noviembre, 05:00 UTC, equivalente al final del domingo 22 en Colombia. La captura contemporánea de rama es referencia; no certifica entrega SAVIO ni cierre efectivo de sección.

## Alcance S10 → S16

S10 se centró en AC-04, disponibilidad y coherencia catálogo/inventario. S16 integra identidad, administración por tienda, reserva de productos, pedidos multi-tienda, transacción compartida y RLS. El cierre declara que el pago es en mostrador y excluye pasarela, SSO, aplicación móvil, envíos y recomendaciones IA. Redis, broker y DLQ son propuestas, no componentes desplegados. Esta reducción explícita de alcance se valora como transparencia, no como ocultamiento.

Base S10 publicada: `76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33`. [Comparación de GitHub](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/compare/76a9cae697ec03d65a8b8752e4b0d7c5e49e8a33...6bd72149d51f81285145bccf65719abcdba0dd42) informa 57 commits; la respuesta de archivos llega a 300 y no se trata como inventario completo. No se recalifican entregas previas por existir.

## Decisiones y evolución

Hay 18 ADR. El cierre enlaza 0003–0006 sustituidos por 0007 (Dokploy). ADR-0018 explica transacción compartida Pedidos–Inventario, costo de reversión y límites de extracción; el servicio crear() consulta contratos públicos, genera un pedido por tienda y reduce stock. El C3 refleja estas relaciones y distingue el comando de vencimiento de su programación externa. Varias decisiones siguen pendientes de ratificación colectiva según el propio cierre; no atribuir consenso a partir del archivo.

## Calidad, resiliencia y seguridad

AC-04 tiene medición local del 8 de noviembre: seis corridas, 30/30 cargas correctas, cero errores y salud 200; peor carga 41,78 ms. No es SLA productivo. AC-01 conserva controles y tests de rol/RLS, AC-02 requiere contar los pasos en la interfaz de noviembre y AC-03 requiere medir confirmación→lectura en otra sesión por debajo de 2 s. Se leyeron pruebas de permisos por tienda, carrito y pedidos; incluyen última unidad, reintento con llave, stock insuficiente y cancelación que repone stock. No se ejecutaron. La guía declara pendientes la programación del vencimiento, coherencia del registro público y timeout del proxy/cliente.

## Coherencia y trazabilidad

arc42 contiene las doce secciones y glosario con contenido del proyecto; el nombre arc42-template-EN.md no prueba que esté vacío. Los tres niveles C4 existen y C3 se contrastó con orders/service.py. Se recorrieron 4/4 filas AC-01–AC-04; tres contrastadas en detalle con pruebas de permisos, carrito y pedidos y la cuarta con medición/concurrencia. Las cuatro tienen rutas y límites explícitos, pero solo AC-04 tiene la medición cuantitativa citada; navegabilidad no equivale a cuatro umbrales satisfechos. Workflow valida contrato, migraciones, RLS, arquitectura, frontend y Compose; no se encontró validación específica de enlaces o render de diagramas.

## CI del SHA exacto

Run 45063583758 del SHA exacto exitoso: backend, frontend y sonarcloud; check SonarCloud Code Analysis también exitoso. El historial del cierre menciona fallos Vitest anteriores, pero no se presentan como el estado actual de este run. El éxito no prueba redespliegue, sesión funcional ni que Dokploy sirva este SHA.

- [Pruebas: 45063583758](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/45063583758): success, head_sha 6bd72149d51f81285145bccf65719abcdba0dd42.
- [sonarcloud](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/45063583758/job/137334960801): success.
- [SonarCloud Code Analysis](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/runs/137334928749): success.
- [frontend](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/45063583758/job/137334686043): success.
- [backend](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/45063583758/job/137334685793): success.

La configuración se leyó en [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/.github/workflows/tests.yml). El check Sonar exitoso no equivale a nueva prueba funcional ni a demostrar cobertura de todos los atributos.

## README y despliegue: evidencia separada

El README documenta https://tiendautb.iscoutb.dev/. Esta pasada es documental: **sin sonda HTTP actual, sin credenciales, sin flujo productivo ni correspondencia imagen→SHA comprobados por este revisor**. Las comprobaciones históricas declaradas por el equipo no se presentan como observaciones nuevas. Incorporar aquí por separado las sondas centrales con hora, respuesta y límites; un health 200 no acredita la demostración.

## Colaboración verificable, sin atribución individual

La consulta de historial alcanzable desde el SHA devolvió 99 commits en esta página y cuatro identificadores de autor distintos (cuentas/firmas, no cuatro personas demostradas); la página no alcanzó el límite de 100. Meses visibles: 2026-11, 2026-10, 2026-09, 2026-08. La consulta de comentarios inline devolvió 0; no hay comentarios inline en esa respuesta. Esto no demuestra revisión cruzada humana ni ausencia de otras modalidades de revisión. No se asignan cuentas por parecido de nombre, no se atribuye trabajo individual y no se fija C5.

## Matriz S16

| Comprobación | Estado | Evidencia / límite |
|---|---|---|
| Estado final identificable | Candidato documentado | SHA y fecha arriba; elegibilidad SAVIO pendiente. |
| Despliegue estable durante revisión | No verificado | Incorporar sondas centrales; README no basta. |
| Flujos principales con datos realistas | No verificado en vivo | Código y pruebas documentados no sustituyen sesión funcional. |
| Caminos de error | Evidencia técnica parcial | Pruebas leídas en fuentes; sin ejecución por el revisor. |
| Respuesta al desafío final | No verificado | Falta acreditar asignación oficial. |
| Alcance frente a S10 | Comparado documentalmente | Base, diff y cambios explícitos arriba. |
| Evolución de ADR | Evidencia presente | Decisiones y límites descritos arriba. |
| Decisión confirmada/reemplazada | Evidencia presente con reservas | Revisar conciliación y fuentes de decisiones; no inferir ratificación personal. |
| Atributos contra umbral | Parcial | Mediciones y sus límites en sección de calidad. |
| Fallos y seguridad | Parcial | Controles/tests y deuda explícitos; no ensayo de producción. |
| arc42 1–12 y glosario | Estructura leída | No equivale a coherencia total; contradicciones señaladas. |
| C4 1–3 | Presente | Correspondencia y límites arriba. |
| Aspectos completos y navegables | Cumple documentalmente; mediciones parciales | 4/4 filas inspeccionadas; muestra semántica y huecos detallados arriba. |
| Validación automática arquitectónica/documental | Parcial | Workflow y pruebas; no inferir validador de diagramas/enlaces. |
| Contribución sustantiva semestral | No verificado individualmente | Agregados limitados; sin vinculación cuenta-persona. |
| Revisión cruzada de fondo | No verificado | Comentarios inline encontrados no acreditan discusión humana. |
| Demostración y defensa | Reservado al docente | Sin puntuación ni conclusión desde repositorio. |

## Matriz transversal del CONTRATO

| Criterio | Estado | Observación |
|---|---|---|
| Organización y convención de nombre | Cumple para ubicación/nombre | URL ISCOUTB; visibilidad anónima no probada en esta consulta autenticada. |
| Estructura mínima | Presente | README, arc42, ADR, C4, aspectos e IA en árbol exacto; rutas alternativas no cuentan como ausencia. |
| Estado identificado | Candidato explícito | No confundir fecha de commit con momento de push. |
| Convención de nombres ADR | Cumple en archivos de decisión observados | Numeración de cuatro dígitos; índices/.gitkeep no son decisiones. |
| Inmutabilidad de ADR aceptados | No verificado | No se realizó auditoría completa por archivo y fecha de aceptación. |
| Uso de IA actualizado y rechazo razonado | No verificado íntegramente | Archivo localizado; no se certifica cada entrada de todo el semestre. |
| CI/Sonar/Quality Gate | Evidencia exacta arriba, alcance limitado | Sin extrapolar pruebas del padre ni producción. |
| Sin secretos en todo el historial | No verificado | No se hizo barrido completo; no se afirma ausencia ni se reproducen valores. |
| Todos los integrantes contribuyen | No verificado | Agregados no resuelven identidad ni sustancia individual. |

## Niveles técnicos sugeridos para C2–C4

- **C2, decisiones y evolución: Competente, provisional.** Hay decisiones con alternativas y consecuencias, evolución concreta y contraste con implementación. Las reservas documentales indicadas impiden sugerir sobresaliente automático.
- **C3, calidad/resiliencia/seguridad: Básico, provisional.** Existen pruebas y mediciones, pero no se acreditan íntegramente todos los umbrales prioritarios ni la recuperación operativa; ver los límites específicos, no una penalización por no ejecutar durante esta lectura.
- **C4, coherencia/trazabilidad: Competente, provisional.** Cuatro filas recorribles con límites honestos, C1–C3 y arc42 conciliados en la muestra, y reglas automáticas en workflow. No se propone sobresaliente sin cerrar la verificación completa de evidencias.

No se propone C1 completo sin desafío acreditado y evidencia funcional vigente; no se asignan puntos, subtotal, nota total ni C5.

## Tres preguntas de defensa

1. Si dos compradores reservan la última unidad y uno repite la petición tras perder la respuesta, ¿qué restricción y transacción evitan doble descuento sin duplicar el pedido?
2. Si el vencimiento deja de ejecutarse en Dokploy durante dos días, ¿cómo detectan reservas retenidas y recuperan stock de forma segura e idempotente?
3. Si Inventario pasa a otro servicio, ¿qué garantía del ADR-0018 deja de ser local y cómo cambiarían contratos, compensación y medición de AC-03?

## Fuentes del SHA revisado

- [docs/cierre-proyecto.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/docs/cierre-proyecto.md)
- [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/docs/aspectos.md)
- [docs/medicion-escenario-4.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/docs/medicion-escenario-4.md)
- [docs/adr/0018-transaccion-compartida-pedidos-inventario.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/docs/adr/0018-transaccion-compartida-pedidos-inventario.md)
- [backend/app/modules/orders/service.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/backend/app/modules/orders/service.py)
- [backend/tests/test_orders.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/backend/tests/test_orders.py)
- [backend/tests/test_admin_por_tienda.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/backend/tests/test_admin_por_tienda.py)
- [backend/tests/test_concurrencia.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/backend/tests/test_concurrencia.py)
- [frontend/tests/carrito.test.ts](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/frontend/tests/carrito.test.ts)
- [docs/c4/component.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/docs/c4/component.md)
- [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/6bd72149d51f81285145bccf65719abcdba0dd42/docs/arc42/arc42-template-EN.md)

## Verificación independiente del corte y del despliegue

El historial de `origin/main` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://tiendautb.iscoutb.dev/](https://tiendautb.iscoutb.dev/) → HTTP 200 (13:28:13 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
