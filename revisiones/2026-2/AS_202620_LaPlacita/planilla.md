# Planilla de equipo · Arquitecturas de Software

Hoja consolidada del equipo LaPlacita. Se actualiza tras cada revisión.

## Identificación

| | |
|---|---|
| Equipo | LaPlacita |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LaPlacita` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Mateo Josue Buendia Barrios · Miguel Angel Isaza Montalvo · Samuel David Jimenez Alvarez · Jorge Alberto Martinez Castillo — cuentas abajo; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://laplacita-app.graymoss-fdd72159.canadacentral.azurecontainerapps.io · ver comprobación y límites en S10 |
| Última revisión | 2026-10-19 · S11 definitiva y S12 preliminar (observación 21:35 UTC); rectificaciones aprobadas sincronizadas |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 12 | [S12 · preliminar](semana-12-evidencia-s12.md) | `master` · `0c9ce082b5850baf1ecda75e82d20757d0101234` | 2/9 | 1.9 (propuesta al docente; preliminar) | sí, 2026-10-19 |
| 11 | [S11 · definitiva](semana-11-evidencia-s11.md) | `master` · `0c9ce082b5850baf1ecda75e82d20757d0101234` | 9/9 | 5.0 (propuesta al docente) | sí, 2026-10-19 |
| 9 | S9 · definitiva | `master` · `3a04706d27e49fb93c90c68f469442fb6f392710` · 2026-10-04T15:39:16-05:00 | 8/9 (una comprobación excluida por decisión docente) | 4.6 | sí, rectificación aprobada; sincronizada 2026-10-19 |
| 10 | Segundo corte · consolidado al cierre | `master` · `2c711d44b31a41a09306f7840da480a21e8c749a` · 2026-10-12T17:41:41-05:00 | C1 0,80; C2 0,60; C3 0,80; C4 0,60 (cada uno /1) | Total 3,60/5; técnica 2,80/4 + C5 docente 0,80/1; ver [S10](semana-10-corte2.md) | sí, 2026-10-13 |
| 8 | S8 (definitiva) | `b03a797` (2026-09-27T19:00:57-05:00) | 10/10 | 5.0 (provisional; 2 filas de despliegue pendientes) | sí, definitiva |
| 7 | S7 | `8c2e1bc` (2026-09-20T22:47:32-05:00) | 10/10 | 5.0 | sí, auditada |
| 6 | S6 | `2c0eb01` (2026-09-13T21:28:00-05:00) | 7/8 | 4.5 | si |
| 5 | CORTE1 | `50b92f8` (2026-09-06T17:45:05-05:00) | 8/12 | 3.7 | si |
| 4 | S4 | `745e799` (2026-08-30T21:52:41-05:00) | 4/10 | 2.6 | si |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `37f1deb8` · 2026-08-08T15:37:16-05:00 | 8/9 | 4,6 * | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `fa7e13bc` · 2026-08-15T18:13:29-05:00 | 5/9 | 3,2 * | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `014751df` · 2026-08-23T19:30:17-05:00 | 9/9 | no se publica | sí |

## Seguimiento vigente · S11 y avance S12 · 19 de octubre de 2026

S11 se fija antes del límite exclusivo 2026-10-19T05:00:00Z. S12 es preliminar, observada a las 21:35 UTC del 19 de octubre, y cierra el 26 de octubre a las 05:00 UTC. Las matrices transversales actuales están en [S11](semana-11-evidencia-s11.md) y [S12](semana-12-evidencia-s12.md). Sus estados y límites sustituyen las inferencias de arrastre que no hayan sido revalidadas; el historial conserva su fecha.

Punta y corte coinciden. Backend y PWA han avanzado, con claves idempotentes limitadas a memoria y escritura FIFO por pedido; el 201 todavía no garantiza persistencia PostgreSQL. La cola ordena las escrituras, pero no equivale a outbox durable. Redis, push y pasarela real siguen declarados como futuros/no integrados. Completar S12 desde esta semántica real.

Actividad en principal: 52 commits en la ventana S11 y 0 posteriores al cierre hasta la observación. El número de commits no determina la nota: se contrasta el contenido completo con la ficha.

| Seguimiento | Estado y evidencia |
|---|---|
| Integración, modos de fallo y extracción | [Matriz S11](semana-11-evidencia-s11.md): distingue diseño, código y pendientes explícitos. |
| Consistencia, caché y reversibilidad | [Matriz S12 preliminar](semana-12-evidencia-s12.md): completar los criterios pendientes antes del cierre. |
| CI, seguridad, contribución y decisiones inmutables | Revisar la matriz transversal del informe actual; no se cierran por un CI verde genérico ni por la existencia de archivos. |

## Feedback S10 vigente · 13 de octubre de 2026

Límite exclusivo: **2026-10-13T05:00:00Z**, fin del 12 de octubre en Colombia. Los criterios C1–C4 son la evaluación técnica del repositorio, cada uno sobre 1,00; el subtotal se conserva sobre 4,00, sin reescalarlo. Se evalúa el escenario documentado bajo el **supuesto explícito de pertinencia**. Su asignación oficial no fue verificada de forma independiente y no se presenta como una confirmación docente. A diferencia de las pasadas preliminares archivadas, esta consolidación expresa la valoración técnica bajo ese supuesto.

**Subtotal técnico: 2,80 / 4,00. Total consolidado C1–C5: 3,60 / 5,00.**

Calificación de sustentación comunicada por el docente: **4,00 / 5,00**, incorporada como **C5 = 0,80 / 1,00**. La conversión proporcional se conserva sin redondearla a los niveles de los criterios técnicos.

El nuevo ensayo de staging acredita tres supervivientes de tres y corrige el arranque antes del POST. El UPSERT sigue sin orden garantizado y la respuesta HTTP no espera la durabilidad. C4 conserva PostgreSQL como planeado.

Fuentes y alcance completos: [informe S10](semana-10-corte2.md#fundamento-técnico-y-comentarios-vigentes). Las referencias de identidad, contribución y despliegue heredadas conservan sus fechas originales; no constituyen una nueva verificación en esta consolidación.

### Deriva arquitectónica al cierre S10

C4 rezagado y persistencia sin el orden de escritura prometido.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Baja · C4 conserva PostgreSQL planeado y un protocolo de persistencia incorrecto:** La vista de contenedores clasifica PostgreSQL como futuro y dibuja HTTP REST/JSON a la BD; la de componentes también lo marca planeado. ADR0014 y el adaptador actual ya contienen conexión pg y SQL, por lo que onboarding y análisis de fallos parten de una topología vieja. **Acción:** Actualizar C4 con PostgreSQL implementado condicional a DATABASE_URL, relación PostgreSQL/TCP mediante pg, Maps como cache/estado local y espejo asíncrono. Mantener Redis y auth marcados futuros. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La supuesta cola de persistencia inicia UPSERT independientes:** El objetivo de conservar el último estado confirmado y el comentario de serialización no se sustentan en la ruta de escritura: cada llamada invoca escribirFila inmediatamente; ultimaEscritura solo se reasigna. Un pool puede solapar escrituras y no se impone orden causal por pedido. Existe riesgo de persistir una instantánea atrasada sin caída de proceso, distinto de la ventana de pérdida ya aceptada. No se afirma que haya ocurrido. **Acción:** Capturar una instantánea inmutable por mutación y encadenar su persistencia a la promesa anterior (idealmente por pedido), o usar versión creciente/UPDATE condicional. Añadir prueba que retrase y reordene dos escrituras y compruebe el estado final; conservar documentado el límite fire-and-forget. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Seguimiento anterior a la consolidación S10; estados históricos superados</summary>

**Historial superado por la consolidación del 13 de octubre de 2026.** Se conserva lo publicado como registro de las observaciones de cada fecha, no como la evaluación vigente. El cierre preliminar 2026-10-12T05:00:00Z que aparece abajo fue sustituido para S10 por el límite exclusivo 2026-10-13T05:00:00Z. Las notas parciales, pendientes de sustentación y bloqueos por asignación del escenario de ese historial no reemplazan la tabla actual.

## Lo que se arrastra

Estado vigente observado en la punta citada en [S10](semana-10-corte2.md). Las correcciones tardías no cambian S9. El registro histórico siguiente conserva su contexto, pero no sustituye esta actualización ni implica cerrar hallazgos no revalidados.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Completar C4 y enlaces de evidencia en A-06. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Resolver identidad de tenant y persistencia antes de declarar seguridad integral. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Acreditar scanner/run/Quality Gate y corregir documentos que aún llaman informativo al job. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Resolver historial de ADR aceptados y confirmar autoría sin inferencias. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| Asignación S10 y comprobación independiente de credenciales pendientes. | Abierto / pendiente de verificar según la matriz | Ver [S9](semana-09-evidencia-s9.md), [S10](semana-10-corte2.md) y retroalimentación |
| La ausencia preliminar de entrega S9 queda cerrada: existe porción real, ADR y evidencia de defecto/medición. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se corrige la exposición del PIN en GET y el setter genérico del borde HTTP; no se da por resuelta autorización. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Registro IA y ADR de no generación incorporados. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |
| Se retiró continue-on-error del job Sonar; falta demostrar el gate y su bloqueo. | Cierre o corrección documentada | Ver evidencia en [overall S10](semana-10-corte2.md) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `ia.md` sin registro de lo rechazado y su motivo | S1 | Cerrado en S3 (entradas del 23/08 con rechazos y motivos) | Resuelto |
| C4 de contexto sin leyenda y guardado dentro del arc42 (§3.3), no en `docs/c4/` | S2 | Cerrado en S3 (`docs/c4/contexto.md` con leyenda, `340c22a`) | Resuelto |
| Escenarios sin la parte «artefacto» | S2 | Cerrado en S3 (ESC-01…ESC-05 con artefacto) | Resuelto |
| `aspectos.md` sin enlaces a los escenarios | S2 | Sí (parcial: ya es tabla de 8 columnas con enlaces al ADR y al código; la columna Requisito sigue sin enlazar a los escenarios) | Enlazar RF-xx a los escenarios correspondientes |
| Ficha del problema sin dos tensiones de calidad (S1) | S1 | Cerrado en S2 parcialmente | Las tensiones aparecen implícitas en el arc42 (objetivos 1.2); declararlas explícitas si vuelven a pedirse |
| ADR 0001 en estado «propuesto» | S3 | No (resuelto en el corte 1, `95ec841`) | Resuelto: ahora dice "aceptado (ratificado por ADR-0002)". |
| Sin pipeline: el verde descansa en evidencia declarada en `ia.md` | S3 | No (resuelto en S4) | Pipeline añadido y en verde desde S4; confirmado en verde también en `corte-1`. |
| Contenedores C4 sin código | S4 | si | |
| docs/ia.md sin columna de rechazo | S4 | si | |
| Trazabilidad ADR-0001/0003 pendiente | S4 | si | |
| Verificación de secciones arc42 5-12 | S4 | si | |
| Etiqueta `corte-1` | S5 | No (resuelto, `50b92f8` antes del cierre) | Resuelto. |
| Declarar restricción asignada | S5 | No (resuelto: RES-05, aislamiento por establecimiento) | Resuelto, con ADR-0004 y línea base medida. |
| Completar trazabilidad en aspectos.md | S5 | No (resuelto, fila A-02 completa) | Resuelto. |
| Registrar motivos técnicos en ia.md | S5 | Parcial | Hay entrada del Corte 1, pero su columna Validación no cierra con el resultado final; completarla. |
| Configurar SonarCloud | S5 | Parcial | `sonar-project.properties` y el paso en CI existen; falta activar `SONAR_TOKEN` para el análisis en vivo. |
| Aportar mediciones reproducibles | S5 | No (resuelto, scripts/medir-aislamiento.js) | Resuelto: 2/2 línea base -> 0/300 post-cambio, reproducible. |
| correcciones.md con nombre incorrecto | S5 | si | |
| docs/ia.md sin sección de rechazos | S5 | si | |
| docs/aspectos.md con Evidencia no navegable | S5 | si | |
| SonarCloud sin token/projectKey | S5 | si | |
| PDF adjunto no verificado | S5 | si | |
| Configurar SONAR_TOKEN para activar SonarCloud | S6 | si | |
| Crear C4 nivel 3 (componentes) | S6 | si | |
| Documentar mapa de contextos con relaciones tipificadas | S6 | si | |
| Crear tabla módulo a datos con dueño único | S6 | si | |
| Completar sección 8 de arc42 con lenguaje ubicuo | S6 | si | |
| Renombrar correciones.md a correcciones.md. | S5 | si | |
| Completar docs/ia.md con columna de rechazado. | S5 | si | |
| Configurar SONAR_TOKEN para activar SonarCloud. | S5 | si | |
| Configurar SONAR_TOKEN y projectKey para activar SonarCloud (desde S4) | S6 | si | |
| Verificar que arc42 §8 contenga lenguaje ubicuo y mapa de contextos | S6 | si | |
| Evidenciar la ejecución del pipeline CI en el commit actual | S6 | si | |
| Deuda de propiedad V-02/V-04/V-05/V-06 planificada para Corte 2 | S6 | si | |
| SonarCloud sin URL de análisis ni Quality Gate (ADR-0003 lo declara pendiente del secreto) | S7 | si | |
| V-02 ACL Pedidos→Catálogo | S7 | si | |
| V-04 Shared Kernel tiendaId | S7 | si | |
| V-05 OHS evento notificaciones | S7 | si | |
| V-06 orquestador | S7 | si | |
| Enlaces tabla aspectos | S7 | si | |
| Despliegue público y health check ausentes; pipeline en rojo | S8 | No (resuelto en S8) | Desplegado en Azure Container Apps y workflow del hash calificado en verde; queda calificar la URL por Moodle. |
| Sin logs estructurados, métrica consultable ni estimación de costo | S8 | No (resuelto en S8) | `src/logger.js` + `GET /api/v1/metricas` ligado a ESC-01/03/04 + estimación con supuestos y ruptura ×36. |
| arc42 §7, restricción económica y ADR separados por plataforma ausentes | S8 | No (resuelto en S8) | §7 y RES-06 añadidos; ADR-0009/0010/0011 por decisión de plataforma. |
| ADR aceptados editados sin reemplazo declarado (0003, 0009, 0010) | S8 | Sí | No editar ADR aceptados: si cambia la decisión, escribir otro y marcar el anterior como reemplazado. |
| Quality Gate de SonarCloud sin URL pública (job `sonar` informativo) | S8 | Sí | Vincular org/proyecto y publicar la URL del Quality Gate. |
| Sin entrega S9 en la punta: 0 commits entre el hash de S8 (`b03a797`) y `origin/master` | S9 | Sí (preliminar) | Empujar la porción construida con IA, su ADR, la prueba que falla y la medición antes del cierre del 2026-10-05T05:00:00Z. |
| ADR aceptados editados sin reemplazo declarado (0001, 0003, 0009, 0010) | S8 | Sí | Persiste en S9; si la decisión cambia, escribir otro ADR y marcar el anterior como reemplazado. |

</details>

## Estado del contrato del repositorio

Actualizado desde la evaluación de la punta actual; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
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

## Contribución por integrante

Actualización agregada del 2026-10-06: Historial de la punta: 156 commits y 5 firmas de autor distintas (firmas, no personas). Las correspondencias de la planilla anterior están declaradas inferidas y pendientes de docente. No se convierten cuatro firmas en cuatro personas verificadas; confirmar atribución y contribución sustantiva.

La tabla individual conservada abajo corresponde al registro histórico anterior; no se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Mateo Josue Buendia Barrios | matbuendia (dos correos consolidados) | 3 | 0 | — | Sin commits en S3 |
| Miguel Angel Isaza Montalvo | Isaza927 + `isaza927` (mismo correo, consolidado) | 21 | 0 | — | Motor de S3: esqueleto, §4, enlaces del ADR |
| Samuel David Jimenez Alvarez | samulssl (correo omitido) | 18 | 0 | — | Creó el ADR 0001 (`bf94244`) |
| Jorge Alberto Martinez Castillo | Jorge M. Castillo (correo omitido) | 53 | 0 | — | Mayor contribuidor; redacción final de S3 |

Correspondencia cuenta↔persona inferida del correo de los commits; la confirma el docente.

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Fallo: si un cliente proporciona tiendaId ajeno o reinicia la instancia, ¿qué protege el pedido y qué observación detectaría el problema?
- Costo: ¿cómo cambia la cuenta al introducir PostgreSQL y autenticación de tenants y qué supuesto de la capa gratuita deja de valer?
- Medición: después de observar la exposición del PIN, ¿qué canal o consumidor medirían a continuación y qué evidencia los haría cambiar el diseño?

</details>
