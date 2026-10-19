# AS_202620_LostVault · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_LostVault/tree/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12; no es cierre ni nota final**.

- Rama: `origin/main`; commit evaluado: [`34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f), fecha `2026-10-18T20:43:15-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche Colombia); se excluyen commits con fecha igual o posterior.
- Observación de punta/S12: `2026-10-19T21:35:00Z` (16:35 Colombia).
- Actividad: 4 commits durante S11; 0 posteriores al corte hasta la observación. Un mismo commit puede aportar evidencia adelantada S12.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica y límites |
|---|---|---|
| Tabla operación → garantía con operaciones reales | No cumple | [docs/arc42/11_riesgos.md:10-34](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/arc42/11_riesgos.md#L10-L34). Hay riesgos de RAM/multinstancia, no tabla operación → garantía para búsqueda y reclamación. |
| Dos operaciones verificadas contra implementación | No cumple | [backend/main.py:219-290](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/backend/main.py#L219-L290). Búsqueda y reclamación se inspeccionaron: usan estado y candado por proceso. Falta declaración de garantías por operación S12; no son transacciones PostgreSQL. |
| Caché: qué, dónde y cuánto | No cumple | [docs/fallos-parciales/s11-fallos-parciales.md:48-65](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/fallos-parciales/s11-fallos-parciales.md#L48-L65). Retención 24 h de deduplicación está definida, pero no es una estrategia de caché de consultas ni argumento explícito de no necesitarla. |
| Invalidación tras escritura | No cumple | [docs/arc42/11_riesgos.md:20-34](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/arc42/11_riesgos.md#L20-L34). No hay política de invalidación de búsqueda/objetos tras reclamar, ni justificación S12 de lectura directa sin caché. |
| Garantías de eventos, si existen | Cumple | [docs/fallos-parciales/s11-fallos-parciales.md:118-126](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/fallos-parciales/s11-fallos-parciales.md#L118-L126). Declara que ninguna operación actual publica eventos; outbox solo cuando aparezcan efectos secundarios. No se exige un flujo inexistente. |
| ADR de la decisión de datos más costosa de revertir | No cumple | [docs/adr/0005-no-extraer-verificacion-identidad.md:66-106](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/adr/0005-no-extraer-verificacion-identidad.md#L66-L106). ADR compara extracción, pero no selecciona la decisión de datos de mayor costo de reversión. |
| Razón y costo de reversión | No cumple | [docs/adr/0005-no-extraer-verificacion-identidad.md:100-119](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/adr/0005-no-extraer-verificacion-identidad.md#L100-L119). No compara costo de revertir el almacenamiento/datos elegidos. |
| Almacenes/brokers propios y tecnología en C4 L2 | No cumple | [docs/c4/C4 nivel 2.jpg](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/c4/C4%20nivel%202.jpg). Imagen inspeccionada: caja genérica Base de Datos sin tecnología; no representa memoria por proceso ni marca persistencia futura. No hay broker vigente. |
| arc42 §8: consistencia y caché | No cumple | [docs/arc42/11_riesgos.md:20-34](https://github.com/ISCOUTB/AS_202620_LostVault/blob/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f/docs/arc42/11_riesgos.md#L20-L34). Inventario docs/arc42 no contiene sección 08; riesgos no sustituyen conceptos transversales de consistencia y caché. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia y límite |
|---|---|---|
| Repositorio público y convención | Cumple | Clonación pública por protocolo git y rama remota en [AS_202620_LostVault](https://github.com/ISCOUTB/AS_202620_LostVault); no se usó API de repositorios. |
| Estructura mínima | No cumple | Inventario git ls-tree del hash citado: README.md; docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md presentes. El contrato §2 exige arc42 secciones 1–12: la sección 08 no aparece en el inventario ni se localizó su contenido equivalente. Los demás artefactos están localizados; se registra la incompletitud estructural sin añadir descuentos al recuento de la ficha. |
| Estado identificable | Cumple | Hash/fecha/rama del encabezado; selección sobre rama principal, sin etiquetas. Observación preliminar, no estado futuro de cierre. |
| Nombres de ADR | No cumple | Fuera de convención: docs/adr/000.3-despliegue-busqueda-lostvault.md |
| ADR aceptados no reescritos | No cumple | docs/adr/0002-integracion-reclamacion-api.md:3-4 ya estaba aceptado; 43794ae añade en :83-85 un enlace y una aclaración de idempotencia. Es una edición documental del ADR aceptado, no un cambio probado de la decisión original; el contrato prohíbe editarlo y permite marcar reemplazo con sucesor. |
| Bitácora IA vigente | No cumple | docs/ia.md:225-273, commit d1d20c2: S11, aceptado/rechazado y límites de RAM/cliente documentados. La lectura no encontró registro específico S12 con usos, aceptación/rechazo y motivo; incumplimiento documental preliminar, subsanable durante la semana. |
| Pipeline, Sonar y Quality Gate públicos | No verificado | [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637229): success; [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637112): success; [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39186637073): success Inspección de workflows; no se ejecutó código localmente. [Panel SonarCloud](https://sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_LostVault). Consulta pública de estado devolvió HTTP 403; Quality Gate no verificado en vivo, aun cuando exista paso configurado. |
| Sin credenciales actuales ni históricas | No verificado | Búsqueda estática de patrones de credenciales y revisión de configuraciones; el barrido histórico por git log -S no terminó dentro de esta pasada. No se afirma ausencia exhaustiva; falta cerrar el historial sin divulgar valores. |
| Contribución de todos | No verificado | git shortlog inspeccionado; las firmas pueden incluir alias. No hay correspondencia inequívoca consolidada de todas las firmas con la nómina para certificar contribución de cada integrante. No se publican identidades ni se atribuyen cuentas por parecido. |

## Recuento y propuesta

**1/9 criterios de la ficha. Nota sugerida: 1.4/5.0**, resultado de `1 + 4 × (1/9)`, redondeado a un decimal. Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no entra en este cálculo. S12 es PRELIMINAR y puede cambiar hasta su cierre.

## Overall · punta actual

Punta observada: [`34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f`](https://github.com/ISCOUTB/AS_202620_LostVault/commit/34c2c2ea71bbe0c2ec0ca0332489aeb14e78c79f), `2026-10-18T20:43:15-05:00`, misma rama principal. Punta y corte coinciden. La idempotencia está implementada y probada en memoria de un proceso; reinicios y múltiples funciones Vercel no comparten claves ni objetos. PostgreSQL es plan, no persistencia existente. Flutter sigue con adaptadores en memoria; timeout/backoff/breaker del cliente están especificados, no implementados. Persiste la divergencia entre modularidad Flutter y backend concentrado en main.py.

## Fallos probados frente a descritos

backend/test_api.py:125-217 cubre reintento, clave conflictiva, expiración y concurrencia dentro del proceso; Backend checks del hash es exitoso. No acredita múltiples instancias, reinicio con recuperación ni red Flutter→API. Estos modos deben conservarse como pendientes, no como resiliencia desplegada.

## Pendientes prioritarios

Faltan tabla de garantías, contraste de operaciones, caché e invalidación y decisión de datos con costo de reversión. El C4 necesita identificar la tecnología y distinguir el almacenamiento RAM vigente de la base de datos prevista. Incorporen esas decisiones a la sección de conceptos de arc42.

## Método y alcance

Lectura estática de fuentes y documentos versionados; sin ejecutar aplicación, pruebas, scripts o migraciones del equipo, y sin usar PDFs. Los ejemplos de comandos no se ejecutaron. Se inspeccionaron código, configuración, contratos y pruebas fuente; un test existente no se da por ejecutado sin evidencia de CI pertinente. Las métricas declaradas no se consideran mediciones independientes. Solo una consulta actions/runs por repositorio; sin API para commits, autores o ramas. El clon es efímero y se elimina al terminar. Los pendientes explícitos con plan cuentan como evidencia válida S11; no se exige extraer servicios ni implementar toda mitigación. Ausencia de flujo por eventos no obliga a inventar un broker.
