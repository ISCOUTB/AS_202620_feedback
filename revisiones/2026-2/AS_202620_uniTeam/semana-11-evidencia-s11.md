# AS_202620_uniTeam · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_uniTeam/tree/2c73ffce2d9b92e71697a7313f829789b4471639) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA S11.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

- Repositorio público: https://github.com/ISCOUTB/AS_202620_uniTeam
- Rama: `origin/master`.
- Hash S11: `2c73ffce2d9b92e71697a7313f829789b4471639`; fecha del commit: `2026-10-13T10:44:44-05:00`.
- Hash observado S12 / overall: `2c73ffce2d9b92e71697a7313f829789b4471639` (misma punta).
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (domingo 18, medianoche Colombia). Se eligió el último commit con fecha anterior al cierre, consultando solo la rama principal, sin etiquetas.
- Observación del avance S12: `2026-10-19T21:35:00Z`; S12 no se cierra ni se sustituye con esta pasada.
- Commits S11 desde `2026-10-12T05:00:00Z`: 8; posteriores al cierre y hasta observación S12: 0.

## Alcance y evidencia

Se leyeron las fichas S11/S12 y el contrato, el árbol completo del hash y los documentos/código pertinentes. Se contrastaron las evidencias aunque no hubiera avance S12. No se ejecutó código, pruebas, instalaciones, despliegues ni scripts del equipo; no se procesaron PDFs. Las referencias `ruta:línea` pertenecen al hash anterior. Las ausencias se decidieron sobre inventario y búsqueda documental/código, no sobre un nombre de archivo supuesto. La matriz transversal no entra en la nota. Las pruebas presentes, resultados declarados y runs públicos se distinguen expresamente.

## Matriz de la ficha

| Criterio | Estado | Evidencia técnica | Observaciones y límites |
|---|---|---|---|
| Integración principal identificada en el código | Cumple | `web/lib/api.ts:85-118; app/api/seguridad.py:52-82; app/application/bus.py:26-35` | Se identifican Web→API, API→OIDC y despacho síncrono interno. |
| Tabla de modos de fallo: no responde, responde tarde y responde dos veces | No cumple | `docs/arc42/arc42-uniteam.md:627-639; docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:67-92` | Los riesgos y condiciones del bus no constituyen la tabla con los tres modos de fallo. |
| Mitigación asignada a cada modo de fallo | No cumple | [docs/arc42/arc42-uniteam.md:631-639](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/arc42/arc42-uniteam.md#L631-L639) | Hay mitigaciones de disponibilidad, pero falta asociarlas a no respuesta, tardanza y duplicación de la integración principal. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | No cumple | `docs/arc42/arc42-uniteam.md:174-180; app/application/bus.py:26-35; docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:69-82` | Se mencionan reintentos en estrategia, mientras el ADR y bus dicen sin reintentos. Falta conciliación de todas las mitigaciones con estado/plan S11. |
| Diseño de idempotencia o saga, o argumento de no aplicabilidad | No cumple | `app/application/servicio_tareas.py:52-83; docs/adr/0003-usar-eventos-de-dominio-en-proceso.md:105-111` | Cada creación genera UUID nuevo; repetir el POST puede crear otra tarea. Mencionar idempotencia cuando sea necesario no es diseño ni argumento de no aplicabilidad. |
| ADR con decisión de extraer o no extraer y sus criterios | No cumple | `docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:18-92; inventario git docs/adr/` | ADR 0006 decide sincronía en proceso, no evalúa extracción de un módulo y criterios frente a servicios independientes. |
| Alternativa no extraer evaluada explícitamente | No cumple | [docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:18-55](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md#L18-L55) | Las opciones son variantes síncronas/asíncronas; no hay comparación explícita extraer/no extraer. |
| arc42 sección 11 con los modos de fallo | No cumple | [docs/arc42/arc42-uniteam.md:627-639](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/arc42/arc42-uniteam.md#L627-L639) | Sección 11 mantiene riesgos anteriores, sin incorporar los tres modos parciales de S11. |
| Filas de aspectos afectadas por la integración al día | No cumple | [docs/aspectos.md:18-29,38-41](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/aspectos.md#L18-L29) | Trazabilidad funcional y de calidad existente, sin diseño/decisión ni modos de fallo S11 enlazados. La propia fila ESC-04 declara prueba de resiliencia pendiente. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia | Observaciones y límites |
|---|---|---|---|
| Repositorio en organización, nombre de convención y público | Cumple | https://github.com/ISCOUTB/AS_202620_uniTeam | Clon público por protocolo git sin pedir acceso; API de runs respondió HTTP 200. No se consultó API de metadatos. |
| Estructura mínima presente | Cumple | git ls-tree -r 2c73ffce2d9b92e71697a7313f829789b4471639; README.md:1; docs/aspectos.md:1; docs/ia.md:1 | Existen docs/arc42/, docs/adr/, docs/c4/, aspectos, IA y README. Presencia no implica que todas las secciones estén completas. |
| Estado calificado identificable | Cumple | refs/remotes/origin/master 2c73ffce2d9b92e71697a7313f829789b4471639 2026-10-13T10:44:44-05:00 | Commit anterior al cierre y punta actual coincidentes; cero commits tardíos observados. |
| Nombres de ADR según convención | Cumple | inventario git docs/adr/ en 2c73ffce2d9b92e71697a7313f829789b4471639 | Archivos Markdown numerados con cuatro dígitos y nombres kebab-case; .gitkeep no se evalúa como ADR. |
| ADR aceptados no reescritos | No verificado | docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:3; diff 2b22db0 | El cambio comprobado pasa Propuesta→Aceptada, no reescribe una decisión ya aceptada. Falta comprobar exhaustivamente las otras modificaciones históricas; no se concluye incumplimiento por el mero número de commits. |
| Registro de IA al día para la semana | No cumple | docs/ia.md:182; último cambio 6e04b35 del 2026-10-04 | Hay registro histórico con descartes, pero no actualización en el periodo S11 pese a actividad del repositorio; no se infiere uso no declarado, se señala falta de registro semanal. |
| Pipeline, SonarCloud y Quality Gate públicos | No verificado | .github/workflows/ci.yml:175-179; sonar-project.properties:4-8: scanner y espera de gate configurados; no hay run de scanner en los cinco resultados consultados. Comprobador de despliegue failure, sin atribuirlo a tests. | La muestra de cinco runs no permite verificar el scanner y el Quality Gate correspondientes ni demostrar su ausencia o fallo. La configuración sí está presente; el estado de otros workflows no sustituye esa comprobación. |
| Sin credenciales en repositorio ni historial | No verificado | git grep -nIE sobre 2c73ffce2d9b92e71697a7313f829789b4471639; inventario .env; revisión histórica parcial | Barrido de patrones en la punta sin secreto real confirmado; coincidencias de código, pruebas o documentación no se publican como credenciales. El barrido histórico no pudo completarse por demoras/aborto de conexión al recuperar blobs antiguos; faltaría cerrar la revisión del historial, no solo comprobar la punta. |
| Contribución de todos los integrantes | No verificado | git shortlog -sne 2c73ffce2d9b92e71697a7313f829789b4471639; EQUIPOS.md | Se examinó distribución de identidades del historial. No se atribuyen cuentas a personas por parecido ni se equipara número de correos con integrantes. Falta correspondencia consolidada/verificada para certificar aportes de todos; se omiten nombres, correos e identificadores personales. |

## Recuento y nota sugerida

**1/9 Cumple. Nota sugerida: 1.4/5.0**, calculada como `1 + 4 × (1/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** Esta revisión S11 es definitiva respecto del cierre indicado.

## overall · proyecto en la punta actual

Existe un producto con tareas, autorización por proyecto, persistencia MySQL, integración OIDC y eventos en proceso. Es una línea base sustancial, pero no sustituye los artefactos específicos S11/S12. El bus captura errores del consumidor, sin persistencia ni reentrega: hay que delimitar la afirmación del ADR 0006 de que no puede confirmarse una operación sin auditoría. La caché JWKS y la caché del flujo ya existen y merecen una política explícita de invalidación.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

test/test_robustez.py:28-133 cubre regresiones de identidad, validación y fechas, no una demostración de los tres fallos de integración. docs/aspectos.md:41 reconoce resiliencia sin medir. La consulta pública devuelve ejecuciones fallidas del comprobador de despliegue para el hash: https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/39303452475. Esto prueba un comprobador fallido, no la causa ni un fallo de la suite unitaria. El muestreo de cinco runs no contiene el run del scanner; no se acreditan Sonar/Quality Gate.

## Pendientes prioritarios

- Tabla de modos de fallo: no responde, responde tarde y responde dos veces: Los riesgos y condiciones del bus no constituyen la tabla con los tres modos de fallo.
- Mitigación asignada a cada modo de fallo: Hay mitigaciones de disponibilidad, pero falta asociarlas a no respuesta, tardanza y duplicación de la integración principal.
- Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado: Se mencionan reintentos en estrategia, mientras el ADR y bus dicen sin reintentos. Falta conciliación de todas las mitigaciones con estado/plan S11.
- Diseño de idempotencia o saga, o argumento de no aplicabilidad: Cada creación genera UUID nuevo; repetir el POST puede crear otra tarea. Mencionar idempotencia cuando sea necesario no es diseño ni argumento de no aplicabilidad.
- ADR con decisión de extraer o no extraer y sus criterios: ADR 0006 decide sincronía en proceso, no evalúa extracción de un módulo y criterios frente a servicios independientes.
- Alternativa no extraer evaluada explícitamente: Las opciones son variantes síncronas/asíncronas; no hay comparación explícita extraer/no extraer.
- arc42 sección 11 con los modos de fallo: Sección 11 mantiene riesgos anteriores, sin incorporar los tres modos parciales de S11.
- Filas de aspectos afectadas por la integración al día: Trazabilidad funcional y de calidad existente, sin diseño/decisión ni modos de fallo S11 enlazados. La propia fila ESC-04 declara prueba de resiliencia pendiente.
- Para el proyecto final, incorporar pruebas de no respuesta, respuesta tardía y duplicación sobre la integración real, y conservar evidencia ejecutada citable. S11 acepta planes pendientes bien declarados; no obliga a extraer servicios ni a implementar mensajería.
