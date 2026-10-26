# Retroalimentación publicable · LaPlacita

## Semana 1 · Equipo, problema y repositorio

Muy buen montaje: estructura completa desde el primer día, ficha del problema clara con usuarios y alcance, tabla de aspectos con seis filas y una bitácora de IA con herramienta, prompt y validación. Los cuatro integrantes ya aparecen en el historial, que es lo ideal.

Solo dos ajustes: declaren en la ficha las dos tensiones de calidad enfrentadas (hoy tienen criterios de éxito, que no es lo mismo), y en la bitácora de IA añadan por cada uso qué se rechazó y por qué, que es la columna que más se valora.

## Semana 2 · Escenarios de calidad y restricciones

Buen contenido: arc42 con secciones 1, 2, 3 y 10 redactadas, cinco escenarios con medidas numéricas, árbol de utilidad con prioridades y un C4 de contexto como código con flechas etiquetadas.

Antes del corte 1 conviene: (1) completar las seis partes de cada escenario — les falta el «artefacto» en los cinco; (2) añadir la leyenda al diagrama C4 y guardarlo en `docs/c4/`; (3) restaurar en `aspectos.md` los enlaces a los escenarios (existieron y se retiraron en un commit posterior); (4) sacar de las restricciones las dos que están marcadas como funcionales — son requisitos; y (5) cuantificar la condición de carga de las medidas (hoy dice «cantidad elevada de usuarios»).

## Semana 3

Qué está bien: sección 4 con matriz comparativa por escenario, ADR 0001 con alternativas descartadas y trazabilidad, esqueleto de módulos por dominio y enlaces del ADR desde `aspectos.md` y desde cada escenario.

Qué corregir antes del corte 1 (semana 5):
1. Ratifiquen el ADR 0001 como «aceptado» (hoy dice «propuesto»).
2. Monten el pipeline en `.github/workflows/` para que la prueba en verde deje de descansar solo en la declaración de `docs/ia.md`.
3. Enlacen la columna Requisito (RF-xx) de `docs/aspectos.md` a los escenarios correspondientes.

## Semana 4 · S4

Buen avance: C4 como código, corte vertical con pruebas en CI verde y trazabilidad A-01 completa. Para el primer corte, alineen los contenedores del diagrama con lo implementado (Redis, PostgreSQL, App/Web Cliente y Portal aún no existen en el repo) y completen docs/ia.md con lo rechazado y su motivo. Revisen que los ADR pendientes enlacen el commit que los implementa. Las secciones 5-12 de arc42 no se pudieron verificar en esta revisión; asegúrense de que estén redactadas sin texto de plantilla.

## Semana 5 · CORTE1

El corte está al día y el pipeline pasa, pero hay tres frentes por cerrar: (1) el archivo de correcciones debe llamarse exactamente correcciones.md; (2) docs/ia.md debe incluir una columna de lo rechazado con su motivo técnico; (3) SonarCloud requiere configurar SONAR_TOKEN para activar el análisis estático. La trazabilidad en aspectos.md es sólida y el aislamiento por tienda está bien evidenciado con pruebas y medición reproducible. Se recomienda revisar el contenido de correciones.md para que cada hallazgo S1-S4 tenga su verificación.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Este fue, de lejos, el trabajo más completo de este corte: identificaron su restricción (que las operaciones de una tienda nunca deben tocar datos de otra), midieron cuántos accesos cruzados eran posibles antes de tocar el código, escribieron un ADR con tres alternativas comparadas y con criterios claros de cuándo revisar la decisión, cambiaron el código real en los cinco módulos del sistema, y volvieron a medir después del cambio con un script reproducible. La etiqueta `corte-1` quedó puesta antes del cierre, sobre un commit con el pipeline en verde.

Dos cosas menores para pulir: la entrada del registro de IA de esta semana no cierra con el resultado final de la verificación (queda "pendiente de revisión"), y SonarCloud está configurado en el pipeline pero el análisis en vivo todavía no está activado (falta la clave real).

Para la sustentación: expliquen qué pasaría si una tienda concentrara la mayoría del tráfico, como ustedes mismos anticipan en el ADR, y cierren el resultado de la verificación que quedó pendiente en el registro de IA.

## Semana 6 · S6

La entrega S6 está bien estructurada: el mapa de contextos, la tabla de propiedad de datos y la auditoría con plan de corrección son verificables y cubren el código actual. Se recomienda confirmar que la sección 8 de arc42 incluya explícitamente el lenguaje ubicuo y el mapa de contextos, ya que no se pudo verificar en el commit. También conviene activar SonarCloud con el token y projectKey para cerrar el pendiente de S4, y evidenciar la ejecución del pipeline con un run. La deuda V-02/V-04/V-05/V-06 está bien planificada; el cierre de V-01 y V-03 el 13/09 es un buen avance.

## Semana 7 · S7

La entrega S7 sí contiene el contrato ejecutable, esquemas, correspondencia con las rutas, prueba contractual en el pipeline, reproducción del fallo incompatible, ADR, flujos de ejecución y C4 etiquetado. La ficha queda completa. Como no conformidad transversal, el pipeline continúa fallando y todavía falta la evidencia pública del Quality Gate de SonarCloud.

## Semana 8 · S8 (revisión definitiva)

Gran salto de esta entrega: el sistema quedó desplegado en Azure Container Apps con URL pública documentada, el pipeline del estado calificado está en verde y la observabilidad se incorporó de verdad (bitácora JSON con campos y un endpoint de métricas ligado a los escenarios). También quedaron versionados el Dockerfile, el workflow, la vista de despliegue de arc42 con una caja por pieza, la restricción económica con tope y condición de no usar tarjeta, y un ADR por cada decisión de plataforma (alojamiento, análisis estático y base de datos), cada uno con su alternativa descartada y su capa gratuita verificada. La estimación de costos parte de supuestos de volumen propios y declara el punto de ruptura de la capa gratuita.

Quedan tres frentes:
1. SonarCloud sigue como paso informativo y no hay URL pública del Quality Gate; vincular la organización y publicar el resultado cierra la deuda transversal abierta desde S6.
2. Se editaron ADR ya aceptados (alojamiento, análisis estático y uno anterior) sin declarar un reemplazo. Un ADR aceptado no se reescribe: si la decisión cambia, se escribe otro y el anterior se marca como reemplazado.
3. La URL desplegada y su health check se entregan por Moodle y quedan pendientes de calificar; conserven la hora de la comprobación.

La base de infraestructura, observabilidad, costos y documentación operativa es sólida. Cierren el Quality Gate público y la disciplina de ADR.

## Semana 9 · S9 (revisión definitiva)

La corrección del borde HTTP ya tiene decisión, pruebas negativas y comparación antes/después. Completen la fila del aspecto con C4 y enlaces directos a la medición. Mantengan explícito que retirar el PIN del GET no resuelve la identidad del establecimiento. La revisión independiente de credenciales quedó bloqueada por una limitación del revisor, así que la propuesta de nota sigue pendiente.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El nuevo ensayo de staging acredita tres supervivientes de tres y corrige el arranque antes del POST. El UPSERT sigue sin orden garantizado y la respuesta HTTP no espera la durabilidad. C4 conserva PostgreSQL como planeado.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

C4 rezagado y persistencia sin el orden de escritura prometido.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Baja · C4 conserva PostgreSQL planeado y un protocolo de persistencia incorrecto:** La vista de contenedores clasifica PostgreSQL como futuro y dibuja HTTP REST/JSON a la BD; la de componentes también lo marca planeado. ADR0014 y el adaptador actual ya contienen conexión pg y SQL, por lo que onboarding y análisis de fallos parten de una topología vieja. **Acción:** Actualizar C4 con PostgreSQL implementado condicional a DATABASE_URL, relación PostgreSQL/TCP mediante pg, Maps como cache/estado local y espejo asíncrono. Mantener Redis y auth marcados futuros. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La supuesta cola de persistencia inicia UPSERT independientes:** El objetivo de conservar el último estado confirmado y el comentario de serialización no se sustentan en la ruta de escritura: cada llamada invoca escribirFila inmediatamente; ultimaEscritura solo se reasigna. Un pool puede solapar escrituras y no se impone orden causal por pedido. Existe riesgo de persistir una instantánea atrasada sin caída de proceso, distinto de la ventana de pérdida ya aceptada. No se afirma que haya ocurrido. **Acción:** Capturar una instantánea inmutable por mutación y encadenar su persistencia a la promesa anterior (idealmente por pedido), o usar versión creciente/UPDATE condicional. Añadir prueba que retrase y reordene dos escrituras y compruebe el estado final; conservar documentado el límite fire-and-forget. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Para el segundo corte, identifiquen el escenario operativo asignado y prueben su respuesta en el despliegue con línea base reproducible. Actualicen los documentos de Sonar, hagan verificable el Quality Gate y preparen la defensa de identidad por establecimiento, persistencia y costos.

</details>

## Semana 9 · Aclaración de la revisión

La comprobación de credenciales bloqueada por el entorno del revisor queda excluida del cálculo por decisión docente. Sigue sin verificarse y no implica un hallazgo de filtración. Los demás criterios conservan su valoración sobre la entrega de cierre; véase la [matriz actualizada](semana-09-evidencia-s9.md).

## Semana 11 · Integración y resiliencia

La evidencia distingue los mecanismos presentes de las mitigaciones planificadas y evalúa explícitamente no extraer. La deduplicación actual está limitada a memoria del proceso y no ofrece durabilidad tras reinicio. Mantengan trazabilidad e inmutabilidad de decisiones históricas, sin presentar una ratificación como eliminación de las ediciones anteriores.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

La siguiente entrega necesita tabla operación–consistencia y contraste de dos operaciones, especialmente el desacople entre memoria y escritura PostgreSQL. Faltan política de caché/invalidación y ADR de la decisión de datos más costosa de revertir. Redis y outbox deben conservarse identificados como futuros mientras no estén implementados.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 14 cerradas, 14 en total**. Los 14 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. La URL Azure histórica se declara retirada el 13/oct; falta la vigente de Dokploy.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

La punta no cambia desde el 19 de octubre. Ya existe portal de tienda y catálogo PostgreSQL; el README desactualizado no demuestra ausencia de funcionalidad. El workflow de despliegue Dokploy figura exitoso, pero falta publicar su URL vigente.

**Próximos pasos:**
- Publicar URL real iscoutb.dev en README; actualizar instrucciones Azure y limitación antigua 'persistencia pendiente'.
- Tabla garantías crear/cambiar pedido distinguiendo RAM y escritura asíncrona PostgreSQL; verificardos operaciones.
- Caché/invalidación o exclusión justificada; ADR decisión de datos más costosa y arc42 §8; Redis/outbox siguen futuros.

**Issues:** 0 abiertas y 14 cerradas; 0 abiertas sin responsable. Cierres: 14 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Sin URL concreta. README declara Azure retirado13-oct y Dokploy actual, dice URL arriba sin darla. No afirmar ausencia de despliegue: CI Deploy Dokploy success. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#laplacita) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Avance sustancial S12: ya existe tabla de 14 operaciones, caché de catálogo write-through, política tras escritura, C4 sin Redis y ADR de identidad del pedido como decisión de datos más costosa de revertir. La creación ahora espera confirmación de PostgreSQL y el seguimiento exige token o sesión del dueño; se contrastaron esas rutas con código. La cola incorpora reintentos y DLQ, pero ambas son en memoria y no garantizan entrega tras caída del proceso. La PR de actualización de Next/React está fusionada. El CI y el despliegue Dokploy figuran exitosos; el job de despliegue pasó pruebas con base real, contrato y health check.

**Próximos pasos:**
- Publicar la URL institucional vigente y corregir frases históricas del README que aún llaman al frontend placeholder y a la persistencia pendiente.
- Añadir prueba de caída de PostgreSQL durante actualizarProducto para demostrar que no cambia la caché; mantener explícito el límite de un solo proceso y la ausencia de invalidación entre réplicas.
- Ratificar ADR0024, hoy propuesto, y actualizar su alternativa SERIAL que todavía dice que esperar la base contradice la creación, pese al cambio de ADR0026.
- Acotar at-least-once a reintentos/cola volátil, probar recuperación o documentar pérdida de pendientes/DLQ tras reinicio; no equiparar polling con un plazo extremo a extremo garantizado.

**Issues:** 0 abiertas y 14 cerradas; 0 abiertas sin responsable. Cierres: 14 completed. El estado registrado no acredita por sí solo implementación.

**README:** Sin URL concreta. README raíz aún sin URL vigente concreta. Azure figura retirado; el CI de Dokploy exitoso no sustituye publicar la dirección. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#laplacita) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Avance real incorporado después del corte del 24: almacenamiento de imágenes del catálogo con módulo Garage S3 y referencias PostgreSQL; rutas de pago exigen dueño y se retiraron las dos mutaciones públicas legacy de entrega. Se añadió auditoría de dependencias a CI, STRIDE y transcripción Markdown del plan. Los ADR 0024–0026 ya constan aceptados por el equipo, no pendientes de validación. El run exacto de master pasa frontend, pruebas, contrato y audit; log Sonar confirma QUALITY GATE STATUS: PASSED. Las ocho PR de dependencias #16–23 siguen abiertas, no son funcionalidades integradas. README todavía solo tiene la URL Azure retirada, no publica URL vigente. La integración Garage/recorrido desplegado se reporta por el equipo; esta revisión no ejecutó una prueba funcional en vivo.

**Próximos pasos:**
- Publicar en README las URL vigentes separando API y PWA bajo iscoutb.dev; retirar la referencia ambigua «URL arriba».
- Distinguir configuración real de Garage del modo memoria sin GARAGE_* y aportar prueba de persistencia tras reinicio; mantener deuda de limpieza de objetos huérfanos.
- Completar lecturas por dueño, validación del modelo STRIDE y aceptación móvil; revisar las PR de dependencias sin atribuir al master sus fallos.

**Issues GitHub:** 0 abiertas y 14 cerradas; 0 abiertas sin asignar. Cierres: 14 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#laplacita) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).


## Seguimiento actual · 26 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin nueva punta ni README desde el corte del 25. Se mantienen la integración Garage/PostgreSQL, protecciones de pago/entrega y evidencia de CI de la misma punta. Las ocho PR de dependencias #16–23 siguen abiertas; no se cuentan como funcionalidades fusionadas. README continúa sin URL pública vigente concreta. No se repitió aceptación funcional en vivo.

**Próximos pasos:**
- Publicar en README la URL vigente de frontend y API bajo iscoutb.dev, diferenciándola del despliegue Azure retirado.
- Cerrar las deudas de persistencia de idempotencia y reintentos con evidencia ejecutada; revisar las actualizaciones de dependencias sin confundirlas con avances integrados.

**Issues GitHub:** 0 abiertas y 14 cerradas; 0 abiertas sin asignar. Cierres: 14 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

[Fuentes y alcance](../seguimiento-s12-2026-10-26.md#laplacita) · [Issues](../seguimiento-issues-2026-10-26.md) · [URL y dominio](../seguimiento-despliegues-2026-10-26.md).
