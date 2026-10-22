# Retroalimentación publicable · XALD

## Semanas 1 y 2

## Evidencia S1

Bien: repositorio con el nombre de la convención, los cuatro integrantes aparecen en el historial desde la primera semana, plantilla arc42 descomprimida y un registro de IA con entradas reales y rechazos justificados.

Corregir: la ficha del problema debe declarar usuarios, alcance y las dos tensiones de calidad enfrentadas (hoy son dos limitaciones sueltas, no un tradeoff); `docs/aspectos.md` debe ser la tabla de ocho columnas (hoy tiene dos); `docs/adr/` y `docs/c4/` deben existir en el repositorio (git no guarda carpetas vacías: usen un archivo de marcador); y limpien los restos de edición de herramientas de IA en los documentos.

## Evidencia S2

Bien: restricciones separadas de los requisitos, C4 de contexto como código con flechas etiquetadas, cinco ADR con contexto y consecuencias, tabla de aspectos con las ocho columnas, y los cuatro integrantes contribuyendo con un PR en el historial.

Corregir antes del corte 1 (es lo más urgente del curso): la entrega pedía los escenarios de calidad — entre 3 y 5, cada uno con sus seis partes (fuente, estímulo, artefacto, entorno, respuesta y medida numérica) — y el árbol de utilidad priorizado por impacto y riesgo; hoy la sección 10 del arc42 está vacía y solo hay una tabla de resúmenes en la sección 1. También: la sección 2 debe clasificar las restricciones técnicas, organizativas y legales con su origen (la Ley 1581 está citada fuera de la sección), la sección 3 debe coincidir con el C4 (el backend aparece en una y no en el otro), el C4 necesita leyenda, los ADR deben llamarse `NNNN-titulo-en-kebab-case.md`, y cada aspecto debe enlazar a su escenario.

## Semana 3

Qué está bien: la sección 4 de arc42 liga tácticas concretas a las metas de calidad, el ADR-006 tiene contexto, opciones, decisión y consecuencias, el README documenta el comando de verificación y el esqueleto Android/Kotlin coincide con los paquetes del ADR.

Qué corregir antes del corte 1 (semana 5):
1. Subir los escenarios de calidad y el árbol de utilidad (pendientes desde S2) y anclar a ellos la matriz comparativa; corregir en la matriz la referencia al «ADR 0001» (la decisión es el ADR-006).
2. Renombrar los seis ADR a `NNNN-titulo-en-kebab-case.md`.
3. En `docs/aspectos.md`, enlazar de verdad la columna ADR (incluido el ADR-006) y limpiar el resto `[cite: 1]`.
4. Registrar en `docs/ia.md` el trabajo de esta semana con lo aceptado y lo rechazado con motivo.

## Semana 4 · S4

El C4 en Mermaid es claro y coherente entre niveles, y los cinco módulos Gradle corresponden a la estructura dibujada. El CI ejecuta las pruebas en verde y la fila A-01 de aspectos está completa hasta Pruebas. Para el próximo corte: completar y verificar las secciones 3-6, 9, 10 y el glosario del arc42; asegurar que la prueba de corte vertical invoque explícitamente la persistencia; implementar o justificar el contenedor Backend XALD; añadir análisis estático con SonarCloud; y enriquecer los ADR con opciones evaluadas y trazabilidad a commits y pruebas.

## Semana 5 · CORTE1

El repositorio está al día en documentación, ADR, C4 y corte vertical, y el CI corre en verde. Para el compendio falta cerrar la trazabilidad: completar las columnas pendientes de docs/aspectos.md y enlazar cada corrección de correcciones.md a un commit o run concreto. El pipeline necesita el análisis estático prometido (SonarCloud) para cumplir el contrato. Revisen también que los enlaces de la tabla de aspectos apunten a la rama principal y no a experimental. El PDF del aula debe quedar disponible para la verificación del corte.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Buena noticia primero: ya existe la etiqueta `corte-1`, sobre un commit de la noche antes del cierre. Y en esa noche el equipo hizo un trabajo real: completaron las secciones de alternativas de los seis ADR, alinearon el código con el backend que el diagrama C4 ya mostraba, corrigieron varias advertencias de seguridad que señalaba el análisis estático, y dejaron un registro de IA con el detalle de qué se aceptó y por qué.

Lo que falta, y es lo central del corte: todo ese trabajo mejora la arquitectura que ya tenían, pero no encontramos una restricción **nueva** diagnosticada, con su estado inicial medido, comparada contra alternativas en un ADR propio del reto, y con un resultado posterior medido contra un umbral. Eso es distinto de mejorar lo que ya existía, y es lo que pide este corte.

Dos detalles técnicos que vale la pena que revisen: la prueba que presentan como "corte vertical ejecutable" solo comprueba que `true` es igual a `true` — no demuestra que los cinco módulos se pasen datos entre sí. Y el pipeline de integración continua está configurado para dispararse en las ramas `experimental` y `main`, pero el proyecto vive en `master`: eso significa que los commits de la noche del cierre, incluida la propia etiqueta `corte-1`, no tienen un run de CI que los respalde directamente, aunque el código que traían ya se había probado en verde antes de fusionarse.

También revisamos el documento de correcciones que dejaron en el repositorio. La mayoría de lo que prometieron para antes del cierre (opciones evaluadas en los ADR, la carpeta del backend) sí se hizo y quedó verificado. Lo que no pudimos confirmar es que el corte vertical ejercite los cinco módulos con dobles de prueba, como afirma el documento — la prueba que encontramos no lo demuestra.

## Semana 7 · S7

El contrato OpenAPI 3.1.0 está bien construido: versión declarada, esquemas completos y rutas alineadas con el backend. Para cerrar el nivel de dominio, versionen la prueba de contrato como archivo (por ejemplo con redocly o schemathesis) e invóquenla desde el workflow, citando el run correspondiente al hash revisado. La captura del CI en rojo es un buen indicio, pero necesita respaldo: adjunten la URL del run fallido o el commit del cambio incompatible. Publiquen la evidencia de SonarCloud con sus tres piezas (configuración, línea del workflow y URL pública con Quality Gate). Completen la sección 7 de arc42 y limpien la sección 6 de instrucciones de copia/pegar. Verifiquen que cada flecha del nivel 2 y cada fila de la tabla de aspectos sean navegables.
## Semana 6 · S6

El mapa de contextos, la matriz de propiedad y la auditoría de no conformidades están bien conectados: los módulos, contratos públicos y DTO de tránsito tienen dueño explícito. Para cerrar la evidencia: incorporen SonarCloud al pipeline y publiquen el scanner, un run y el Quality Gate; además, completen A-04 y hagan que los enlaces de aspectos apunten a la rama principal, no a `experimental`.

## Semana 8 · S8 (revisión definitiva)

La entrega cambió por completo respecto de la revisión temprana: ahora hay un backend desplegado en Render, descrito como código (un archivo de Blueprint más su Dockerfile), con health check, logs en una línea JSON por evento, una métrica ligada a la resolución de conflictos de sincronización, secretos fuera del código y una estimación de costo con su volumen supuesto y el punto en que se agota cada capa gratuita. La sección 7 de arc42 quedó completa con una caja por pieza y su ubicación, la sección 2 recoge la restricción de costo cero y la de no usar tarjeta, y cada decisión de plataforma tiene su propio ADR con alternativas descartadas.

Para cerrar: integren el análisis estático de SonarCloud al pipeline y publiquen el análisis con su Quality Gate; dejen de editar los ADR ya aceptados —si una decisión cambia, escriban uno nuevo y marquen el anterior como reemplazado—; y retiren del control de versiones los archivos compilados de Python que siguen en `__pycache__`. Las filas de URL desplegada y de health quedan pendientes de calificar porque la URL se entrega por Moodle.

## Semana 9 · S9 (revisión definitiva)

Hay avances verificables en pruebas, auditoría y decisiones, pero el handler LWW no cambió respecto a la semana anterior. La medición 30/30 procesa pares en secuencia y solo observa aceptaciones y un contador; no demuestra conflictos simultáneos ni el estado ganador completo. Repitan ese experimento, precisen lo corregido en el registro de IA y actualicen los enlaces y las discrepancias de la arquitectura.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

LWW y el contador existen, pero 30/30 no demuestra concurrencia ni la versión ganadora: el script cuenta respuestas 202 y conflictos y no comprueba el estado final. Falta línea base. Cliente HTTP, persistencia, cifrado y coherencia documental siguen parciales.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación sigue pendiente de calificación docente; no se infiere a partir del repositorio. El [informe del corte](semana-10-corte2.md) y la [planilla](planilla.md) separan ese pendiente del componente técnico.

### Deriva arquitectónica al cierre S10

Vistas mezclan objetivo y prototipo; ACK promete un encolado inexistente.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · La arquitectura de ejecución publicada mezcla diseño objetivo con prototipo en memoria:** Las vistas atribuyen al artefacto garantías offline-first, cifrado y conectividad no implementadas. La auditoría S9 ya reconoce la brecha, pero no sustituye una vista de ejecución consistente. No se afirma fuga de datos reales ni se penaliza el aplazamiento explícito de Gemini. **Acción:** Separar claramente vista actual y objetivo; marcar UI/SMS, Room/cifrado y envío HTTP como pendientes. Documentar que el flujo es de componentes/pruebas, no integrado a la actividad Android. Para reclamar end-to-end, cablear la entrada real al caso de uso y demostrar persistencia/reinicio y envío autenticado. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · El ACK de sincronización promete encolado aunque únicamente guarda una marca temporal:** El consumidor recibe ACEPTADO/encolada sin que exista cola ni almacenamiento del cuerpo de la transacción en el handler. Si un futuro cliente usa ese ACK para retirar su copia pendiente, no hay respaldo recuperable del payload en este backend. La app actual no implementa ese consumidor; no se afirma pérdida real en producción. **Acción:** Alinear semántica de API/ADR: declarar aceptación de una simulación de versiones, sin promesa de cola, o conservar payload completo y encolarlo antes del ACK. Añadir una prueba de recuperación del cuerpo aceptado/estado de cola, sin exigir persistencia durable si sigue fuera del corte. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Confirmen la consigna operativa asignada y registren una línea base antes de cambiar el MVP. El experimento debe reproducir la carga real y verificar estado final, pérdida y recuperación, además de respuestas HTTP. Mantengan visible que los datos siguen en memoria y que Gemini es un mock. Falta la evidencia pública de SonarCloud y demostrar el flujo del despliegue, además del health check.

</details>

## Semana 10 · Actualización docente

Se incorporó la calificación de sustentación comunicada por el docente en la planilla y en el [informe S10](semana-10-corte2.md). La evaluación técnica del repositorio mantiene su fundamento y sus observaciones.

## Semana 11 · Integración y resiliencia

La evidencia distingue correctamente lo implementado y lo pendiente, con modos de fallo concretos, planes y pruebas de cierre. La decisión de no extraer está justificada; esos pendientes declarados son válidos para esta entrega. Acoten la deduplicación al proceso vivo, corrijan las referencias a otra rama y no describan el bucle secuencial de pruebas como carga concurrente.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Avance preliminar: el diseño de sincronización declara al menos una vez y sus límites, pero aún faltan las garantías por operación y dos verificaciones completas. Definan caché e invalidación o argumenten su ausencia, y seleccionen la decisión de datos de mayor costo de reversión. El C4 debe separar almacenes propios con tecnología y distinguir memoria actual de persistencia futura.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 6 cerradas, 6 en total**. Cinco cierres figuran como completed y uno como duplicate. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Externo**. Backend en Render. Dirección(es) documentada(s): https://xald-backend.onrender.com.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Se mantiene la documentación de idempotencia/sincronización del 18 de octubre (Colombia) y CI Android/backend exitoso; no hay cambios nuevos en la rama principal desde el seguimiento anterior. El README publica backend Render, pero no subdominio iscoutb.dev. Para S12, transformar la tabla de casos de idempotencia en operación→garantía y contrastar guardar local/registrar remoto sin prometer durabilidad o convergencia que no ofrece el almacenamiento en memoria. Justificar no usar caché o definir su invalidación, comparar el costo de reversión de las decisiones de datos y actualizar C4 nivel2 con almacenes propios/tecnología, distinguiendo memoria actual de Room futuro. Las seis issues están cerradas, pero una tiene razón duplicate y solo cinco completed; ese cierre no acredita pendientes S12 resueltos.

**Issues:** 0 abiertas y 6 cerradas; 0 abiertas sin responsable. Cierres: 5 completed, 1 duplicate. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Externo. Backend Render, fuera del dominio requerido. URL documentada: https://xald-backend.onrender.com ; https://xald-backend.onrender.com/health. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#xald) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).
