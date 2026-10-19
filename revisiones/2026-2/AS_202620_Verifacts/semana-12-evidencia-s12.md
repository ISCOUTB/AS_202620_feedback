# AS_202620_Verifacts · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Verifacts/tree/e98575318f313fde96ef4c56603fbbc4f2984ae3) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12 — aún abierta.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

- Repositorio público: https://github.com/ISCOUTB/AS_202620_Verifacts
- Rama: `origin/master`.
- Hash S11: `e98575318f313fde96ef4c56603fbbc4f2984ae3`; fecha del commit: `2026-10-18T12:39:38-05:00`.
- Hash observado S12 / overall: `e98575318f313fde96ef4c56603fbbc4f2984ae3` (misma punta).
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (domingo 18, medianoche Colombia). Se eligió el último commit con fecha anterior al cierre, consultando solo la rama principal, sin etiquetas.
- Observación del avance S12: `2026-10-19T21:35:00Z`; S12 no se cierra ni se sustituye con esta pasada.
- Commits S11 desde `2026-10-12T05:00:00Z`: 2; posteriores al cierre y hasta observación S12: 0.

## Alcance y evidencia

Se leyeron las fichas S11/S12 y el contrato, el árbol completo del hash y los documentos/código pertinentes. Se contrastaron las evidencias aunque no hubiera avance S12. No se ejecutó código, pruebas, instalaciones, despliegues ni scripts del equipo; no se procesaron PDFs. Las referencias `ruta:línea` pertenecen al hash anterior. Las ausencias se decidieron sobre inventario y búsqueda documental/código, no sobre un nombre de archivo supuesto. La matriz transversal no entra en la nota. Las pruebas presentes, resultados declarados y runs públicos se distinguen expresamente.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica | Observaciones y límites |
|---|---|---|---|
| Tabla operación a garantía de consistencia con operaciones reales | No cumple | `docs/entregas/entrega-modos-fallo-idempotencia-adr.md:53-60; docs/arc42/08-conceptos-transversales.md:1-78` | Tabla de fallos, no operación→garantía. No se halló matriz de consistencia para creación y consulta de análisis. |
| Dos operaciones verificadas contra la implementación | No cumple | `app/persistence/repository.py:95-166; app/api/routes.py:62-126` | Se contrastaron guardar y consultar análisis: INSERT/commit y SELECT por otra conexión. Sin garantía por operación no se acreditan dos verificaciones; tampoco se prueba idempotencia de escritura. |
| Diseño de caché: qué, dónde y cuánto | No cumple | `docs/arc42/08-conceptos-transversales.md:1-78; docs/entregas/entrega-modos-fallo-idempotencia-adr.md:86-128` | Respuesta guardada en diseño de idempotencia no constituye una política completa de caché; falta qué/dónde/duración o justificación de no caché. |
| Política de invalidación tras escritura | No cumple | `app/persistence/repository.py:95-136,169-194; docs/arc42/08-conceptos-transversales.md:1-78` | Falta definir refresco/invalidación del historial tras crear análisis si se cachea; hoy no hay evidencia de una caché implantada que se haya demostrado obsoleta. |
| Garantías del flujo por eventos, si existe | Cumple | `docs/c4/02-contenedores.md:15-18,64-67; docs/adr/0009-decision-extraccion-modulo-analisis.md:39-44,55` | No aplica a flujo actual: integración síncrona y broker descartado. Saga distribuida es exclusivamente conceptual futura. |
| ADR de la decisión de datos más costosa de revertir | No cumple | `docs/adr/0009-decision-extraccion-modulo-analisis.md:25-66; inventario git docs/adr/` | No extracción no equivale a identificar la decisión de datos de mayor costo de reversión. |
| Argumento y costo de reversión de esa decisión | No cumple | [docs/adr/0009-decision-extraccion-modulo-analisis.md:58-73](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/docs/adr/0009-decision-extraccion-modulo-analisis.md#L58-L73) | No se compara costo de reversión/migración de datos frente a otras decisiones. |
| Almacenes y brokers como contenedores propios en C4 nivel 2 | Cumple | [docs/c4/02-contenedores.md:26-38,43-47](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/docs/c4/02-contenedores.md#L26-L38) | SQLite figura como almacén propio con tecnología; no hay broker implementado que deba añadirse. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/08-conceptos-transversales.md:1-78](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/e98575318f313fde96ef4c56603fbbc4f2984ae3/docs/arc42/08-conceptos-transversales.md#L1-L78) | Sección 8 reúne validación, errores, pruebas y propiedad de datos, sin estrategia de consistencia/caché S12. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia | Observaciones y límites |
|---|---|---|---|
| Repositorio en organización, nombre de convención y público | Cumple | https://github.com/ISCOUTB/AS_202620_Verifacts | Clon público por protocolo git sin pedir acceso; API de runs respondió HTTP 200. No se consultó API de metadatos. |
| Estructura mínima presente | Cumple | git ls-tree -r e98575318f313fde96ef4c56603fbbc4f2984ae3; README.md:1; docs/aspectos.md:1; docs/ia.md:1 | Existen docs/arc42/, docs/adr/, docs/c4/, aspectos, IA y README. Presencia no implica que todas las secciones estén completas. |
| Estado calificado identificable | Cumple | refs/remotes/origin/master e98575318f313fde96ef4c56603fbbc4f2984ae3 2026-10-18T12:39:38-05:00 | Commit anterior al cierre y punta actual coincidentes; cero commits tardíos observados. |
| Nombres de ADR según convención | Cumple | inventario git docs/adr/ en e98575318f313fde96ef4c56603fbbc4f2984ae3 | Archivos Markdown numerados con cuatro dígitos y nombres kebab-case; .gitkeep no se evalúa como ADR. |
| ADR aceptados no reescritos | No cumple | docs/adr/0003-integracion-sincrona.md:120-128; diff 9430845 | Se añadió contenido al ADR aceptado sin adenda fechada/reemplazo formal; preservar el registro aceptado y enlazar la actualización en otro ADR. Se distingue de una modificación de estado de propuesta. |
| Registro de IA al día para la semana | No cumple | docs/ia.md:24-25; último cambio 5c643bd del 2026-10-07 | Registro llega a S9, sin actualización del periodo S11; no se presume uso de IA no declarado, falta evidencia semanal. |
| Pipeline, SonarCloud y Quality Gate públicos | No verificado | .github/workflows/sonarcloud.yml:29-39 y sonar-project.properties:1-6: configuración presente; cinco runs muestreados son keep-alive. Falta run exitoso de scanner y estado público del Quality Gate de la revisión. | La muestra de cinco runs no permite verificar el scanner y el Quality Gate correspondientes ni demostrar su ausencia o fallo. La configuración sí está presente; el estado de otros workflows no sustituye esa comprobación. |
| Sin credenciales en repositorio ni historial | No verificado | git grep -nIE sobre e98575318f313fde96ef4c56603fbbc4f2984ae3; inventario .env; revisión histórica parcial | Barrido de patrones en la punta sin secreto real confirmado; coincidencias de código, pruebas o documentación no se publican como credenciales. El barrido histórico no pudo completarse por demoras/aborto de conexión al recuperar blobs antiguos; faltaría cerrar la revisión del historial, no solo comprobar la punta. |
| Contribución de todos los integrantes | No verificado | git shortlog -sne e98575318f313fde96ef4c56603fbbc4f2984ae3; EQUIPOS.md | Se examinó distribución de identidades del historial. No se atribuyen cuentas a personas por parecido ni se equipara número de correos con integrantes. Falta correspondencia consolidada/verificada para certificar aportes de todos; se omiten nombres, correos e identificadores personales. |

## Recuento y nota sugerida

**2/9 Cumple. Nota sugerida: 1.9/5.0**, calculada como `1 + 4 × (2/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** La nota S12 es PRELIMINAR y puede cambiar hasta el cierre; no constituye entrega vencida.

## overall · proyecto en la punta actual

El pipeline de ingesta y persistencia existe y la decisión de no extraer es pertinente. El documento de S11 mezcla diseño futuro con lenguaje de mitigaciones aplicadas: ni timeout configurable de 4 s, ni respuestas 504/422 de extracción, ni WAL/retry constan en la implementación citada. La idempotencia se diseña pero POST /analysis aún inserta un nuevo registro por invocación. Corregir la correspondencia documental, añadir sección 11 de riesgos y actualizar aspectos antes de presentar el diseño como resiliencia ya probada.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

tests/test_url_ingestion.py:33-55 verifica fallos simulados de descarga/extracción con respuesta 400; no prueba el timeout 4 s ni respuesta 504. Las pruebas de umbrales son otro modo distinto. La consulta de cinco runs devolvió solo Keep-alive exitosos (por ejemplo https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/39328160836), no la suite ni scanner. Un ping exitoso no acredita pruebas de fallos ni Quality Gate. Configuración scanner: .github/workflows/sonarcloud.yml:29-39; no se ejecutó código ni se abrieron PDFs.

## Pendientes prioritarios

- Tabla operación a garantía de consistencia con operaciones reales: Tabla de fallos, no operación→garantía. No se halló matriz de consistencia para creación y consulta de análisis.
- Dos operaciones verificadas contra la implementación: Se contrastaron guardar y consultar análisis: INSERT/commit y SELECT por otra conexión. Sin garantía por operación no se acreditan dos verificaciones; tampoco se prueba idempotencia de escritura.
- Diseño de caché: qué, dónde y cuánto: Respuesta guardada en diseño de idempotencia no constituye una política completa de caché; falta qué/dónde/duración o justificación de no caché.
- Política de invalidación tras escritura: Falta definir refresco/invalidación del historial tras crear análisis si se cachea; hoy no hay evidencia de una caché implantada que se haya demostrado obsoleta.
- ADR de la decisión de datos más costosa de revertir: No extracción no equivale a identificar la decisión de datos de mayor costo de reversión.
- Argumento y costo de reversión de esa decisión: No se compara costo de reversión/migración de datos frente a otras decisiones.
- arc42 sección 8 con consistencia y caché: Sección 8 reúne validación, errores, pruebas y propiedad de datos, sin estrategia de consistencia/caché S12.
- El taller de mensajes se evalúa aparte. No se exige introducir caché o broker si su ausencia está razonada; sí precisar las garantías, los límites y las decisiones de datos.
