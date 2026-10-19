# AS_202620_uniTeam · Evidencia S12

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_uniTeam/tree/2c73ffce2d9b92e71697a7313f829789b4471639) · [Ficha S12](../../../fichas/semana-12-evidencia-s12.md)

**Estado: PRELIMINAR S12 — aún abierta.** Revisión académica del contenido completo disponible en la rama principal; no se toma la falta de commits como ausencia de revisión.

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
| Tabla operación a garantía de consistencia con operaciones reales | No cumple | `docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:59-65; docs/arc42/arc42-uniteam.md:557-560` | Tabla por componentes, no tabla de operaciones reales con garantías de consistencia. |
| Dos operaciones verificadas contra la implementación | No cumple | `app/application/servicio_tareas.py:52-83,148-163; app/api/dependencias.py:24-33; app/events/consumidores.py:40-54` | Crear tarea y cambiar estado comparten sesión con auditoría y commit al finalizar. Se contrastó el código, pero falta garantía por operación; el bus captura fallos y requiere aclarar límites de atomicidad prometida. |
| Diseño de caché: qué, dónde y cuánto | Cumple | `app/api/seguridad.py:65-82; web/lib/api.ts:120-137; docs/arc42/arc42-uniteam.md:512` | Hay caché de claves JWKS en API con lifespan=600 y caché de flujo por carga en cliente. Evidencia de diseño en comentarios de código; falta consolidarla en sección 8. |
| Política de invalidación tras escritura | No cumple | `app/api/seguridad.py:78-80,97-100; web/lib/api.ts:122-137` | Se documenta recarga por kid desconocido y reinicio en pruebas, pero no política completa para claves revocadas con mismo kid ni para flujo modificado en redespliegue con cliente abierto. TTL/refresco parcial no cubre todas las escrituras. |
| Garantías del flujo por eventos, si existe | Cumple | `docs/adr/0006-estilo-sincrono-con-eventos-en-proceso.md:69-82; app/application/bus.py:26-35` | Entrega en proceso, sin persistencia ni reintento; queda explícito que no se garantiza al menos una vez y que un fallo puede perder la reacción. Se acepta la semántica limitada declarada, sin inferir exactamente una vez. |
| ADR de la decisión de datos más costosa de revertir | No cumple | `docs/adr/0004-usar-mysql-como-base-de-datos.md:20-47; docs/adr/0009-usar-aiven-for-mysql-como-base-de-datos-gestionada.md:74-78` | Hay decisiones de motor/proveedor y procedimiento de reversión; no se selecciona justificadamente la más costosa. |
| Argumento y costo de reversión de esa decisión | No cumple | [docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md:21-31,53-55](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/adr/0013-tareas-no-lee-las-tablas-de-proyectos.md#L21-L31) | La alternativa descartada se califica costosa, pero la elegida se revierte sin migración. Falta comparación del mayor costo real y su alcance. |
| Almacenes y brokers como contenedores propios en C4 nivel 2 | Cumple | [docs/c4/nivel2-contenedores.md:16-20,82-89](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/c4/nivel2-contenedores.md#L16-L20) | MySQL aparece como contenedor propio; se explica que el bus vive en proceso, sin broker externo. |
| arc42 sección 8 con consistencia y caché | No cumple | [docs/arc42/arc42-uniteam.md:557-560](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/2c73ffce2d9b92e71697a7313f829789b4471639/docs/arc42/arc42-uniteam.md#L557-L560) | La sección 8 figura expresamente pendiente; debe recoger consistencia y caché. |

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

**3/9 Cumple. Nota sugerida: 2.3/5.0**, calculada como `1 + 4 × (3/9)`, redondeada a un decimal. **Propuesta al docente; la nota final la fija el profesor en Moodle.** La nota S12 es PRELIMINAR y puede cambiar hasta el cierre; no constituye entrega vencida.

## overall · proyecto en la punta actual

Existe un producto con tareas, autorización por proyecto, persistencia MySQL, integración OIDC y eventos en proceso. Es una línea base sustancial, pero no sustituye los artefactos específicos S11/S12. El bus captura errores del consumidor, sin persistencia ni reentrega: hay que delimitar la afirmación del ADR 0006 de que no puede confirmarse una operación sin auditoría. La caché JWKS y la caché del flujo ya existen y merecen una política explícita de invalidación.

No hay cambios posteriores al cierre en la rama principal observada. La revisión S12 aplica sus criterios al estado completo actual; no modifica la nota de S11 ni recalifica entregas anteriores.

## Fallos probados, documentados y límites de CI

test/test_robustez.py:28-133 cubre regresiones de identidad, validación y fechas, no una demostración de los tres fallos de integración. docs/aspectos.md:41 reconoce resiliencia sin medir. La consulta pública devuelve ejecuciones fallidas del comprobador de despliegue para el hash: https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/39303452475. Esto prueba un comprobador fallido, no la causa ni un fallo de la suite unitaria. El muestreo de cinco runs no contiene el run del scanner; no se acreditan Sonar/Quality Gate.

## Pendientes prioritarios

- Tabla operación a garantía de consistencia con operaciones reales: Tabla por componentes, no tabla de operaciones reales con garantías de consistencia.
- Dos operaciones verificadas contra la implementación: Crear tarea y cambiar estado comparten sesión con auditoría y commit al finalizar. Se contrastó el código, pero falta garantía por operación; el bus captura fallos y requiere aclarar límites de atomicidad prometida.
- Política de invalidación tras escritura: Se documenta recarga por kid desconocido y reinicio en pruebas, pero no política completa para claves revocadas con mismo kid ni para flujo modificado en redespliegue con cliente abierto. TTL/refresco parcial no cubre todas las escrituras.
- ADR de la decisión de datos más costosa de revertir: Hay decisiones de motor/proveedor y procedimiento de reversión; no se selecciona justificadamente la más costosa.
- Argumento y costo de reversión de esa decisión: La alternativa descartada se califica costosa, pero la elegida se revierte sin migración. Falta comparación del mayor costo real y su alcance.
- arc42 sección 8 con consistencia y caché: La sección 8 figura expresamente pendiente; debe recoger consistencia y caché.
- El taller de mensajes se evalúa aparte. No se exige introducir caché o broker si su ausencia está razonada; sí precisar las garantías, los límites y las decisiones de datos.
