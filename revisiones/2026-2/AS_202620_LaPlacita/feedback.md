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

## Semana 9 · S9 (pasada temprana, preliminar)

Esta entrega es una lectura **preliminar**: la actividad S9 aún no ha cerrado (corte el 2026-10-05) y lo revisado es la punta actual de la rama principal, no un estado congelado; la valoración puede cambiar si el equipo empuja antes del cierre.

La evidencia de S9 se lee con una regla decisiva: una fila solo se satisface con trabajo **del periodo S9**. Lo que ya estaba en el repositorio es línea base y se puede citar como contexto, pero no cuenta dos veces. Al momento de esta pasada, la punta de la rama principal no registra commits posteriores al estado con que se calificó S8, así que la mayor parte de la matriz de esta semana todavía no tiene material propio del periodo.

**Qué falta para esta evidencia**
- Una porción real del sistema construida con IA durante S9, con su cadena navegable en `docs/aspectos.md` hasta código, prueba y medición.
- La prueba que falle ante el defecto que cubre: no hay run en rojo, prueba de mutación ni procedimiento documentado; la fila queda como pregunta de sustentación.
- La medición del escenario asociado, contrastada con su umbral.
- La actualización de `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con su motivo, incluyendo al menos una entrada del periodo.
- El ADR que decida sobre el componente generativo: evaluarlo con costo y latencia, o argumentar por qué no se incorpora.
- La auditoría de erosión sobre límites de contexto y propiedad de datos del código generado en S9.
- La verificación, contra su registro oficial, de las dependencias que se propongan en S9.

**Recordatorios transversales que siguen abiertos**
- Hay ADR ya aceptados que se editaron sin declarar un reemplazo. Un ADR aceptado no se reescribe: cuando la decisión cambia, se escribe uno nuevo y el anterior se marca como reemplazado.
- `docs/ia.md` debe quedar al día para la semana.
- El paso de SonarCloud en el pipeline sigue siendo informativo y falta publicar la URL del Quality Gate.
