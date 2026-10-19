# AS_202620_PideUtb · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_PideUtb/tree/2395d7812aa86ae98c177d58cbea0e927d9593d5) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12; no es cierre ni nota final**.

- Rama: `origin/master`; commit evaluado: [`2395d7812aa86ae98c177d58cbea0e927d9593d5`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2395d7812aa86ae98c177d58cbea0e927d9593d5), fecha `2026-10-18T18:40:46-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 44 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Tabla operación → garantía con operaciones reales | Cumple | [docs/arc42/arc42.md:1332-1346](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L1332-L1346). Tabla sobre operaciones reales del sistema. Corregir garantías sobregeneralizadas: entrega al menos una vez no es nivel de consistencia; el webhook mantiene ventana entre dos transacciones. |
| Dos operaciones verificadas contra implementación | No cumple | [backend/app/pedidos/repository.py:53-121](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/backend/app/pedidos/repository.py#L53-L121). Contraste 1: crear pedido usa INSERT en transacción (84-98), consistente. Contraste 2: avanzar estado lee/valida en service.py:232-267 y guardar actualiza solo por id (111-115), no WHERE estado esperado como promete arc42:1340. No se ejecutó una carrera; divergencia estática comprobada. |
| Caché: qué, dónde y cuánto | Cumple | [docs/arc42/arc42.md:1391-1438](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L1391-L1438). No caché de aplicación razonada con medición y riesgo de precios obsoletos; ficha permite esta decisión. Cabeceras de estáticos diferenciadas. |
| Invalidación tras escritura | Cumple | [docs/arc42/arc42.md:1409-1438](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L1409-L1438). La decisión no cachear lecturas evita invalidación de datos tras escritura; config.js revalida. No exigir Redis ni TTL arbitrario donde el equipo justifica no cachear. |
| Garantías de eventos, si existen | Cumple | [docs/api/asyncapi.yaml:1-90](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/api/asyncapi.yaml#L1-L90). Contrato de webhook repetible y bus en proceso, deduplicación y límites enlazados con arc42 §8.5 y §6.7; bus sin suscriptores no equivale a broker durable. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0010-notificar-al-panel-por-sondeo.md:53-148](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/adr/0010-notificar-al-panel-por-sondeo.md#L53-L148). ADR-0010 decide sondeo frente a SSE/broker; no selecciona la decisión de datos más costosa de revertir. ADRs restantes no cubren explícitamente esa selección. |
| Razón y costo de reversión | No cumple | [docs/adr/0010-notificar-al-panel-por-sondeo.md:79-133](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/adr/0010-notificar-al-panel-por-sondeo.md#L79-L133). Costo operativo de broker y conservación de contratos no sustituyen explicar por qué una decisión de datos es la más costosa de revertir ni su migración/costo. |
| Almacenes/brokers propios y tecnología en C4 L2 | Cumple | [docs/c4/nivel2-contenedores.md:19-34](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/c4/nivel2-contenedores.md#L19-L34). PostgreSQL 16 como ContainerDb propio y volumen; bus interno no es broker separado (§116-120). Corregir flecha API→pasarela que todavía contradice código. |
| arc42 §8: consistencia y caché | Cumple | [docs/arc42/arc42.md:1313-1455](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/2395d7812aa86ae98c177d58cbea0e927d9593d5/docs/arc42/arc42.md#L1313-L1455). Sección 8 contiene consistencia por operación y no-caché razonada. Actualizar desfase de sondeo: texto 8 s frente a 5 s ya implementados en avance S14. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_PideUtb](https://github.com/ISCOUTB/AS_202620_PideUtb); no se usó API de repositorios. |
| Estructura mínima | Cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. Esto no acredita completitud de sus secciones. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Observación preliminar, no estado futuro de cierre. |
| Nombres de ADR | Cumple | Inventario completo docs/adr/ del hash citado: nombres NNNN-titulo-en-kebab-case.md. |
| ADR aceptados no reescritos | No cumple | Historial 32abc9d modifica ADR-0007 aceptado; 59ec90c cambia el título de ADR-0008 y documenta la reversión de la decisión de origen único. La sustitución declarada ADR-0004→0008 es distinta y válida; no justifica reescrituras de otros ADR. |
| Bitácora IA vigente | No cumple | docs/ia.md termina en S9 (últimas secciones:259-353); commit 07dc813 del periodo corrige información previa, pero no registra usos/aceptados/rechazados correspondientes a S11/S12. No se encontró registro específico S12 con usos, aceptación/rechazo y motivo; incumplimiento documental preliminar, subsanable durante la semana. No se acredita tampoco registro S11. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39177528726): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_PideUtb). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No cumple | backend/pagos/service.py:27-43 documenta exposición histórica y retirada/rotación de credencial. La rotación declarada reduce el riesgo actual, pero no demuestra ausencia histórica; no se publica ningún valor. No se verificó su vigencia contra el servicio. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**6/9 criterios de la ficha. Nota sugerida: 3.7/5.0**, resultado de `1 + 4 × (6/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo. S12 es PRELIMINAR y puede cambiar hasta su cierre.

## Overall · punta actual

Punta observada: [`2395d7812aa86ae98c177d58cbea0e927d9593d5`](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/2395d7812aa86ae98c177d58cbea0e927d9593d5), `2026-10-18T18:40:46-05:00`, misma rama principal. Punta y corte coinciden. PR 24, PR 25 (datos y eventos), PR 26 (rama de fallos parciales) y PR 27 (corrección migración) constan integrados antes del corte; se evalúa su código, no solo la etiqueta semanal. El bus carece de suscriptores; el panel usa sondeo, ahora 5 s, mientras S12/ADR-0010 conservan 8 s. La tabla sobrestima atomicidad del avance de estado y el C4 mantiene una llamada a pasarela inexistente. El equipo documenta caída 404 de unos 30 minutos por checksum de migración; el fix está versionado, pero la recuperación pública no fue verificada en esta auditoría. CI exitoso no acredita servicio recuperado.

## Fallos probados frente a descritos

backend/tests/test_fallos_parciales.py:71-174 inyecta fallo entre escrituras, detecta conciliación y verifica reintento sin segundo código; :176-226 cubre publicación tras persistir, suscriptor fallido y ausencia de suscriptores. CI exitoso del hash es citable. No se ejecutó código ni se prueba desde aquí disponibilidad, restauración de backup o carrera entre avances de estado.

## Pendientes prioritarios

La estrategia de no caché y los límites del bus están documentados. Corrijan la garantía de avance de estado: se valida antes de un UPDATE por identificador, sin la condición de estado prometida en la tabla. Falta un ADR que justifique la decisión de datos más costosa de revertir y su costo; alineen además el intervalo de sondeo y la flecha a la pasarela con el código vigente.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
