# Semana 10 · Segundo corte · LaPlacita

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LaPlacita |
| Estado revisado | `3a04706d27e49fb93c90c68f469442fb6f392710` en `origin/master` (2026-10-04T15:39:16-05:00) |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.274455+00:00 |
| Punta revisada para S10 | `3a04706d27e49fb93c90c68f469442fb6f392710` (2026-10-04T15:39:16-05:00) |
| S9 congelado, solo como línea base | `3a04706d27e49fb93c90c68f469442fb6f392710` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** ESC-03/PIN es el escenario de calidad utilizado en S9. No se encontró una fuente que lo declare reto operativo asignado para S10; el plan de identidad/persistencia de Corte 2 tampoco demuestra una asignación. Fuente o búsqueda: [docs/evidencias/evidencias-s9.md:24-39](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L24-L39) y [docs/evidencias/evidencias-s9.md:315-326](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L315-L326); búsqueda en README, ADR, arc42 y evidencias. La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `50b92f8558f2f57d01aeee14dfe202c9e076e74f`: el delta hasta esta punta modifica 64 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta master 3a04706d27e49fb93c90c68f469442fb6f392710, anterior al cierre futuro; debe recongelarse al cierre. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://laplacita-app.graymoss-fdd72159.canadacentral.azurecontainerapps.io/api/v1/health: HTTP 200 en 9.980 s; inicio 2026-10-06T21:24:19Z. URL publicada en [docs/evidencia-despliegue-azure.md:5-9](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencia-despliegue-azure.md#L5-L9). Solo sonda de salud, sin probar flujo de pedidos. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | ESC-03/PIN es el escenario de calidad utilizado en S9. No se encontró una fuente que lo declare reto operativo asignado para S10; el plan de identidad/persistencia de Corte 2 tampoco demuestra una asignación. [docs/evidencias/evidencias-s9.md:24-39](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L24-L39) y [docs/evidencias/evidencias-s9.md:315-326](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L315-L326); búsqueda en README, ADR, arc42 y evidencias |
| Línea base medida y reproducible | No verificado | [docs/evidencias/evidencias-s9.md:129-167](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L129-L167) es línea base/resultado reproducible de S9; falta identificar su pertinencia al reto asignado S10. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:52-124](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L52-L124) registra cambio concreto y alternativas, pero su adecuación al escenario operativo asignado queda pendiente. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [src/modules/pedidos/index.js:83-96](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/src/modules/pedidos/index.js#L83-L96) y [app/api/v1/pedidos/[pedidoId]/route.js:14-28](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/app/api/v1/pedidos/%5BpedidoId%5D/route.js#L14-L28) confirman corrección implementada. No se declara respuesta S10 sin conocer el reto. |
| Resultado contrastado con el umbral | No verificado | [docs/evidencias/evidencias-s9.md:106-174](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L106-L174) contrasta defecto/umbral de S9; faltan identificación y experimento S10 sobre despliegue. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | [.github/workflows/ci.yml:25-78](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/.github/workflows/ci.yml#L25-L78) define pruebas y scanner; [docs/semana-08.md:175-185](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/semana-08.md#L175-L185) documenta métrica. Run/gate actual y métrica específica del reto pendientes; no hay defensa observada. |
| Secretos protegidos | No verificado | El equipo documenta su barrido en [docs/evidencias/evidencias-s9.md:280-295](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L280-L295). La revisión independiente ampliada fue cancelada dos veces por la herramienta y no se repite por otra vía: no se afirma limpieza ni exposición a partir de ese bloqueo; comprobación pendiente del revisor. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/aspectos.md:9-36](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/aspectos.md#L9-L36) sigue sin enlace C4 para A-06 ni evidencia navegable; [docs/evidencias/evidencias-s9.md:325-326](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/evidencias/evidencias-s9.md#L325-L326) y [README.md:247](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/README.md#L247) dicen Sonar informativo aunque el workflow ya eliminó esa condición. Hay avance real, pero documentos no están plenamente reconciliados. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/0013-proyeccion-publica-pedido-sin-pin.md:124](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3a04706d27e49fb93c90c68f469442fb6f392710/docs/adr/0013-proyeccion-publica-pedido-sin-pin.md#L124) precisa 0007 a partir de defecto real; sin asignación confirmada no se da por confirmación/reemplazo del reto S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | La califica el docente en entorno desplegado y pipeline en vivo. |

Recuento descriptivo: 2 Cumple, 1 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación operativa S10 no verificada; ESC-03 no se presume esa asignación. |
| Decisión e implementación | No verificado | Pendiente | Respuesta S9 sólida y acotada, pendiente contraste con el reto S10. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Pipeline y señales existentes, pero gate vigente, secretos y operación del reto pendientes. |
| Evolución arquitectónica trazable | No verificado | Pendiente | Cadena C4/evidencia y coherencia documental aún parciales; no se recalifica S9. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | Pendiente docente. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

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

## Preparación de la sustentación

1. Fallo: si un cliente proporciona tiendaId ajeno o reinicia la instancia, ¿qué protege el pedido y qué observación detectaría el problema?
2. Costo: ¿cómo cambia la cuenta al introducir PostgreSQL y autenticación de tenants y qué supuesto de la capa gratuita deja de valer?
3. Medición: después de observar la exposición del PIN, ¿qué canal o consumidor medirían a continuación y qué evidencia los haría cambiar el diseño?

## Próximos pasos

Para el segundo corte, identifiquen el escenario operativo asignado y prueben su respuesta en el despliegue con línea base reproducible. Actualicen los documentos de Sonar, hagan verificable el Quality Gate y preparen la defensa de identidad por establecimiento, persistencia y costos.
