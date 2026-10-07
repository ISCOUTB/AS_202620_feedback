# Semana 9 · Generación verificada y trazable · LaPlacita

Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LaPlacita |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.274455+00:00 |
| Cierre S9 | 2026-10-05T05:00:00Z (medianoche de Colombia) |
| Estado revisado | `3a04706d27e49fb93c90c68f469442fb6f392710` en `origin/master` (2026-10-04T15:39:16-05:00) |
| Línea base S8 | `b03a79783e5675b6251d14af5edee077de86e3bd` |
| Commits del delta S8 → S9 | 9 |

## Alcance y método

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

La preliminar anterior coincidía con S8 y quedó superada: el delta incorpora ADR-0012/0013, endurecimiento del borde HTTP, prueba roja/verde documentada, medición y registro IA. La comparación no vuelve a calificar el aislamiento de S5.

## Matriz de la ficha (10 criterios)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/ia.md:54-58](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/ia.md#L54-L58) registra auditoría/generación; [src/modules/pedidos/index.js:83-96](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/src/modules/pedidos/index.js#L83-L96) introduce vistaPublica y [app/api/v1/pedidos/[pedidoId]/route.js:14-28](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/app/api/v1/pedidos/%5BpedidoId%5D/route.js#L14-L28) la usa. El commit de corrección [e0542ce4](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/e0542ce40869dbf61580192cbe0a9fa65ef7113b) está dentro del periodo. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos.md:9-16](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L9-L16) mejora A-06 y enlaza ADR/código/prueba, pero tiene siete columnas, sin C4; [docs/aspectos.md:27-36](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L27-L36) deja C4-3 vacío para A-06 y la medición sigue en texto, sin enlace. Existe evidencia S9, pero la fila no forma todavía la cadena navegable completa exigida. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:11-45](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L11-L45) identifica los dos defectos y [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:52-124](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L52-L124) compara cuatro alternativas, preserva dueño de PIN y decide proyección pública/retiro de PUT. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/evidencias/evidencias-s9.md:68-98](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L68-L98) documenta commit rojo, cuatro aserciones fallidas y verde tras fix; [tests/contract-openapi.test.js:362-434](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/tests/contract-openapi.test.js#L362-L434) contiene esas aserciones. Se contrastaron commits por Git; los enlaces de runs son evidencia aportada por el equipo, no una consulta independiente exitosa del conector. El procedimiento documentado satisface la alternativa permitida en la ficha. |
| Medición del escenario asociado | Cumple | [docs/evidencias/evidencias-s9.md:106-174](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L106-L174) define umbral cero, comandos, línea base y resultado corregido sobre dominio/contrato/HTTP. Contraste documental 303→0; los 303 agregan tipos de comprobación y no deben describirse como una tasa homogénea de 303 solicitudes. No se ejecutó el experimento en esta revisión. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:54-58](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/ia.md#L54-L58) documenta aceptación, corrección de numeración/anclas y rechazos técnicos de JWT sin identidad y ocultar PIN solo en cliente. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/dominio/auditoria-modularidad.md:49-60](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/dominio/auditoria-modularidad.md#L49-L60) toma reglas S6 y [docs/dominio/auditoria-modularidad.md:64-148](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/dominio/auditoria-modularidad.md#L64-L148) identifica/restaura V-03 y declara deuda de autorización. Se contrastó vistaPublica, ruta sin PUT y dueño único de escritura; no se interpreta como autenticación resuelta. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/evidencias/evidencias-s9.md:236-276](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L236-L276) declara cero dependencias incorporadas y registra consulta npm de jsonwebtoken rechazado. Diff de package.json/lock del periodo sin cambios; [registro npm](https://registry.npmjs.org/jsonwebtoken) consultado: nombre exacto y repositorio auth0/node-jsonwebtoken. No añadir dependencia no es un incumplimiento. |
| Sin credenciales en código, ejemplos ni documentación generada | No verificado | El equipo documenta su barrido en [docs/evidencias/evidencias-s9.md:280-295](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L280-L295). La revisión independiente ampliada fue cancelada dos veces por la herramienta y no se repite por otra vía: no se afirma limpieza ni exposición a partir de ese bloqueo; comprobación pendiente del revisor. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0012-no-incorporar-componente-generativo.md:18-32](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0012-no-incorporar-componente-generativo.md#L18-L32) y [docs/adr/0012-no-incorporar-componente-generativo.md:84-111](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0012-no-incorporar-componente-generativo.md#L84-L111) decide no incorporar, con restricciones de identidad, persistencia, costo y latencia, más condiciones para reevaluarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_LaPlacita; [docs/evidencias/evidencias-s9.md:8-10](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L8-L10). |
| Estructura mínima presente | Cumple | Árbol Git con las seis rutas mínimas; [docs/aspectos.md:9-17](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L9-L17) y ADR/código/evidencia enlazados existentes. |
| Estado calificado identificable | Cumple | origin/master 3a04706d27e49fb93c90c68f469442fb6f392710; hash/fecha y corte en cabecera. |
| Nombres de ADR según la convención | Cumple | Los archivos 0001–0013 de docs/adr siguen NNNN-titulo-en-kebab-case; [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:1-7](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L1-L7). |
| ADR aceptados no reescritos | No cumple | Historial verificado de 0003/0009/0010 contiene ediciones posteriores a aceptación, por ejemplo [4f380512](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/4f3805127ec8e55890ea029b8c4489c1c7932753) y [c99f542b](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/c99f542b48b9b51f93da24464cfa7250091fa00d). [docs/aspectos.md:23-25](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L23-L25) reconoce arrastre; ADR-0013 sí complementa sin reescribir 0007. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:54-58](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/ia.md#L54-L58) registra S9 y rechazo técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:51-78](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/.github/workflows/ci.yml#L51-L78) ya no contiene continue-on-error, pero scanner sigue condicionado a token y no espera Quality Gate. [docs/semana-08.md:119-129](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/semana-08.md#L119-L129) mantiene ejecución/URL de gate pendientes. Única consulta PR del hash vacía; no se infiere inexistencia de runs push. No hay trío verificable del contrato para este cierre. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo documenta su barrido en [docs/evidencias/evidencias-s9.md:280-295](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L280-L295). La revisión independiente ampliada fue cancelada dos veces por la herramienta y no se repite por otra vía: no se afirma limpieza ni exposición a partir de ese bloqueo; comprobación pendiente del revisor. |
| Contribución de todos los integrantes | No verificado | Las correspondencias de la planilla anterior están declaradas inferidas y pendientes de docente. No se convierten cuatro firmas en cuatro personas verificadas; confirmar atribución y contribución sustantiva. |

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `3a04706d27e49fb93c90c68f469442fb6f392710` (2026-10-04T15:39:16-05:00). Hay 0 commits posteriores al estado congelado S9. La punta coincide con el estado S9. Se retiró el setter genérico HTTP y el PIN deja de salir por la lectura de pedido. Persisten tiendaId suministrado por el llamante, estado en memoria y deuda declarada V-02/V-04/V-05/V-06. La eliminación de continue-on-error es un avance específico, no prueba Quality Gate ni protección de rama.

- Completar C4 y enlaces de evidencia en A-06.
- Resolver identidad de tenant y persistencia antes de declarar seguridad integral.
- Acreditar scanner/run/Quality Gate y corregir documentos que aún llaman informativo al job.
- Resolver historial de ADR aceptados y confirmar autoría sin inferencias.
- Asignación S10 y comprobación independiente de credenciales pendientes.

### Hallazgos anteriores cerrados o delimitados

- La ausencia preliminar de entrega S9 queda cerrada: existe porción real, ADR y evidencia de defecto/medición.
- Se corrige la exposición del PIN en GET y el setter genérico del borde HTTP; no se da por resuelta autorización.
- Registro IA y ADR de no generación incorporados.
- Se retiró continue-on-error del job Sonar; falta demostrar el gate y su bloqueo.

## Recuento y nota sugerida

**8 de 10 criterios Cumple**,  1 No cumple y 1 No verificado. La transversal no entra en el cálculo.

**Nota propuesta pendiente de completar la comprobación bloqueada del revisor.** El recuento documental es 8/10; si las 1 comprobaciones bloqueadas resultan conformes, el intervalo resultante es 4.2–4.6. No es una nota cerrada ni se atribuye el bloqueo al equipo. La nota final la fija el docente en Moodle.

## Próximos pasos

La corrección del borde HTTP ya tiene decisión, pruebas negativas y comparación antes/después. Completen la fila del aspecto con C4 y enlaces directos a la medición. Mantengan explícito que retirar el PIN del GET no resuelve la identidad del establecimiento. La revisión independiente de credenciales quedó bloqueada por una limitación del revisor, así que la propuesta de nota sigue pendiente.
