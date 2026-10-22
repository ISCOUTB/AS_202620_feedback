# Retroalimentación publicable · DinamikUTB

## Semana 1

- Está bien: estructura completa desde la semana 1 (arc42 con plantilla, adr, c4, aspectos, ia), `docs/aspectos.md` con la tabla de 8 columnas y 6 aspectos, `docs/ia.md` con una entrada real, y la ficha del problema con usuarios y alcance.
- Falta: una segunda tensión de calidad (solo declararon consistencia vs. disponibilidad), y que los cuatro integrantes firmen commits.
- Corregir antes del corte 1: declarar las dos tensiones y preferir la ficha en Markdown dentro del repositorio (hoy es un PDF).

## Semana 2

- Está bien: secciones 1, 2 y 3 redactadas y sin texto de plantilla; restricciones clasificadas (técnicas, organizativas, legales) y justificadas; 3 escenarios con sus seis partes y medidas numéricas (100 %, 100 %, 80 %); árbol de utilidad con impacto y riesgo técnico; C4 de contexto como PlantUML con leyenda y flechas etiquetadas; aspectos enlazando escenarios.
- Falta: enlazar los escenarios con hipervínculos reales desde `docs/aspectos.md` (hoy son ID de texto), registrar en `docs/ia.md` qué se rechazó de la IA y por qué, y equilibrar la participación (casi todo el trabajo de la semana lo subió una sola persona).
- Corregir antes del corte 1: definir cómo se medirán los escenarios (herramienta y carga) y repartir los commits de la próxima entrega entre los cuatro.

## Semana 3

Qué está bien: el ADR 0001 enuncia la decisión con contexto, alternativas motivadas y consecuencias, el README documenta el arranque único con `start.bat` y la estructura de paquetes coincide con el monolito modular decidido.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 no nombra tácticas concretas: liguen cada táctica a Q-01, Q-02 y Q-03 en `docs/arc42/04-solution-strategy.md`.
2. La matriz comparativa usa criterios genéricos con puntaje 1–5: háganla contra el árbol de utilidad, fila por fila con los escenarios Q-01…Q-03 (qué mejora y qué empeora con cada estilo).
3. Completen el enlace del ADR: la columna ADR de `docs/aspectos.md` sigue en «Pendiente» y el escenario Q-01 no lo enlaza (el ADR 0001 ya existe).
4. Evidencien el verde de las pruebas: hoy no hay pipeline ni evidencia de ejecución; agreguen un workflow antes del corte.

## Semana 4 · S4

La documentación arc42 y el C4 están bien avanzados y el corte vertical es trazable en el código. Para el primer corte: enlacen el ADR-0002 desde la sección 9 y añadan trazabilidad con commits y pruebas en los ADR. Ejecuten el pipeline y dejen visible el run en verde como evidencia de las pruebas. Completen la fila de aspectos con enlaces verificables. Eviten commits después del cierre; el arranque con start.bat debe quedar cerrado antes. El glosario y la coherencia C4-código son un buen punto de partida.

## Semana 5 · CORTE1

El repositorio tiene una base sólida: estructura completa, ADR bien formados, README claro y un corte vertical coherente con la arquitectura.
Sin embargo, hay secciones arc42 vacías (07 y 08) que deben completarse para cerrar S4.
Falta poder contrastar correcciones.md con los hallazgos previos y verificar la trazabilidad de aspectos.md.
Aporten el contenido de esos archivos y un run de CI del commit evaluado.
También deben entregar el PDF en Moodle y preparar la sustentación.
El historial muestra participación de todo el equipo y no se detectaron secretos.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Buenas noticias primero: el pipeline sigue en verde antes del cierre y `docs/ia.md` sí tiene una entrada fechada de esta semana con su justificación, así que ese punto queda resuelto. Lo que preocupa es que el trabajo que hicieron en esta semana (el ADR-0003 sobre el motor de base de datos) formaliza una decisión que ya venía pendiente desde varias semanas atrás, no responde a la restricción nueva que debía asignárseles para este corte. No encontramos en el repositorio ningún diagnóstico de esa restricción, ninguna cifra de línea base medida, ni un resultado comparado contra un umbral. Tampoco existe todavía la etiqueta `corte-1`.

Sobre `correcciones.md`: lo leímos completo. Es una autoevaluación de las semanas 1 a 4 donde ustedes mismos marcan todo como "Cumple", pero esas semanas ya fueron calificadas y no se vuelven a calificar por existir el documento — necesitábamos que el archivo respondiera a la revisión preliminar de este corte (semana-05-corte1), y no encontramos ningún punto que lo hiciera. Para la próxima entrega, si quieren disputar una fila concreta de una revisión ya publicada, cítenla y aporten la evidencia puntual que la contradice, en vez de una lista general de "cumple" sin evidencia verificable.

Preparen para la sustentación: cuál era la restricción asignada, qué midieron antes de cualquier cambio y con qué procedimiento, y por qué el ADR-0003 no aparece conectado a esa restricción.

## Semana 6 · S6

La documentación de la semana 6 está parcialmente visible: la sección 8 de arc42 ya incorpora lenguaje ubicuo con los términos de contextos delimitados, pero no se pudo verificar el mapa de contextos completo ni la tabla módulo-datos. Se recomienda asegurar que el mapa nombre explícitamente los contextos y el tipo de relación entre ellos, y que la tabla de dueño único se contraste con los modelos reales del backend. También conviene documentar el recorrido de la auditoría de violaciones con ubicaciones concretas en el código. Para el pipeline, adjuntar el enlace a un run de GitHub Actions. El repositorio cumple con la estructura, los ADR y el registro de IA.

## Semana 5 · corte actualizado

Esta revisión sustituye las conclusiones anteriores de S5. El corte es un compendio de S1 a S4: no se evaluó un reto ni una restricción nueva. La documentación de problema, calidad, estrategia, ADR, C4 y el corte vertical está presente, y las correcciones están organizadas con rutas verificables; también hay evidencia de CI en verde.

Queda por completar la trazabilidad de los aspectos que aún conservan celdas pendientes, verificar el arranque completo en un entorno limpio y resolver el PDF y la sustentación fuera del repositorio. Si una decisión aceptada cambia, registren la sustitución en un ADR nuevo en vez de editar el ADR original.

## Semana 7 · S7

El contrato OpenAPI versionado con esquemas y la prueba de contrato que falla ante un cambio incompatible están muy bien resueltos y son la mejor evidencia de esta semana; la sección 6 de arc42 describe tres flujos de interacción y el C4 nivel 2 etiqueta con protocolo y formato las relaciones entre contenedores. Para cerrar la entrega: (1) completen la tabla de aspectos con las ocho columnas navegables y sin celdas «Pendiente»; (2) el pendiente más importante es el análisis estático: hoy hay configuración y un bloqueo de permisos documentado, pero se necesita un run que invoque el scanner y la URL pública del análisis con el estado del Quality Gate; (3) cuiden los commits de último minuto sobre el cierre, que dejan la entrega al borde del límite.

## Semana 8 · S8

El despliegue reproducible quedó resuelto y es el avance más claro de la semana: la infraestructura está versionada como código, el entorno se recrea siguiendo el README y el pipeline corre en verde sobre la rama principal. También quedaron bien los logs estructurados en JSON, la métrica consultable ligada al escenario de disponibilidad, las variables declaradas fuera del código y tomadas del proveedor, la estimación de costo con sus puntos de ruptura, la vista de despliegue y las restricciones de costo en arc42, y los ADR por decisión de plataforma. El análisis estático ya tiene Quality Gate público, con lo que se cierra el pendiente que venía desde semanas atrás.

Lo que hay que corregir: varios ADR aceptados fueron editados después de su aceptación. Un ADR aceptado no se edita ni se borra; si la decisión cambia, se escribe uno nuevo y el anterior queda marcado como reemplazado. Quedan además pendientes de calificar la URL del despliegue y la comprobación del health check, que se entregan por Moodle y no se abren en esta pasada.

## Semana 9 · S9 (revisión definitiva)

La nueva política de verificación, la auditoría de escrituras y el ADR de no incorporar IA generativa están sustentados. La porción y la prueba reutilizadas son de entregas anteriores, y la medición al cierre cubre cinco de los veinte casos previstos. Completen la cadena navegable y distingan el trabajo nuevo de la línea base.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El resultado declarado de 20/20 no coincide con el CI fallido y no constituye una línea base operacional. Hay health check, JSON y métricas, pero las cadenas arquitectónicas están incompletas y algunos controles documentados no están implementados.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

C4 no distingue SQLite local de PostgreSQL desplegado.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Baja · C4 muestra SQLite sin distinguir PostgreSQL del ambiente desplegado:** Puede inducir una configuración de almacenamiento equivocada si C4 se lee de forma aislada. **Acción:** Separar en C4 SQLite local y PostgreSQL desplegado y marcar como previstos los módulos sin implementación. Conservar ADR3 como historia y enlazar ADR7 vigente. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

La punta amplía pruebas y mejora documentación, pero el CI falla mientras la evidencia afirma que todos los casos pasan. Corrijan esa contradicción y documenten el experimento del escenario asignado. No carguen datos reales mientras lectura y escritura sigan sin autenticación. La sustentación queda pendiente.

</details>

## Semana 6 · Rectificación de la revisión

La lectura completa confirma que el mapa de contextos, la propiedad de datos, los hallazgos con plan y la correspondencia de aspectos estaban en la entrega original. Se corrigen las observaciones producidas por una lectura parcial; no se exige un ADR de reajuste cuando no cambiaron los límites. Consulta la [matriz rectificada](semana-06-evidencia-s6.md) para los alcances y pendientes transversales.

## Semana 9 · Rectificación de la revisión

Se reconocen la porción real apoyada por IA, la prueba contractual que falló ante un defecto y los rechazos técnicos ya registrados antes del cierre. Quedan pendientes completar enlaces de la cadena y medir todos los casos del escenario. Consulta la [evidencia rectificada](semana-09-evidencia-s9.md).

## Semana 11 · Integración y resiliencia

La ficha queda cubierta con modos de fallo concretos, timeout y reintentos contrastados, idempotencia de la actualización absoluta y decisión razonada de mantener el monolito. Los pendientes están declarados y no obligan a una extracción prematura. Mantener la deuda de autenticación, concurrencia y diferencias entre bases de pruebas y despliegue visible y comprobable.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Hay dos operaciones contrastables con la garantía declarada, un flujo síncrono justificado y almacenes separados en C4. Falta sistematizar la tabla operación-garantía, decidir caché e invalidación y justificar comparativamente la decisión de datos más costosa de revertir. Incorporar estos conceptos en arc42 sección 8.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **2 abiertas, 15 cerradas, 17 en total**. Los 15 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Externo**. Frontend y API fuera del dominio requerido. Dirección(es) documentada(s): https://iscoutb.github.io/AS_202620_DinamikUTB/ ; https://dinamikutb-api.onrender.com.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Master no cambió; PR #35 abierta en su rama de trabajo incorpora PostgreSQL 16 Compose, no MySQL 8.4 pese título. No equivale a despliegue fusionado. README declara expiración el 27 de octubre y plan recrear/resembrar el 25 de octubre, no verificado con proveedor.

**Próximos pasos:**
- Completar tabla GET/PUT de requisitos → garantía, probar concurrencia y evitar inferir serializabilidad del commit.
- Justificar no caché o definir invalidación tras PUT, y reflejarlo en arc42 §8.
- Comparar costo de revertir motor/esquema/persistencia en ADR; revisar PR #35 título/diff, respaldo y restauración antes del plazo declarado y publicar dominio institucional real.

**Issues:** 2 abiertas y 15 cerradas; 1 abiertas sin responsable. Cierres: 15 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Externo. Frontend en GitHub Pages y API en Render. Expiración del 27/oct y plan del 25/oct declarados por el equipo, no verificados con el proveedor. URL documentada: https://iscoutb.github.io/AS_202620_DinamikUTB/ ; https://dinamikutb-api.onrender.com. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#dinamikutb) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).
