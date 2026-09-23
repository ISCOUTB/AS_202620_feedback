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

El contrato OpenAPI versionado con esquemas y la prueba de contrato que falla ante un cambio incompatible están muy bien resueltos y son la mejor evidencia de esta semana. Para cerrar la entrega, suban la salida de git log del archivo de contrato para demostrar su historial junto con la versión, y compartan el contenido de la sección 6 de arc42 y del C4 nivel 2 para comprobar que cada flecha lleva protocolo y formato. La tabla de aspectos necesita sus ocho columnas navegables y sin huecos. El pendiente más importante es el análisis estático: hoy hay configuración y un bloqueo de permisos documentado, pero se necesita un run que invoque el scanner y la URL pública del análisis con el estado del Quality Gate. Cuiden también los commits de último minuto sobre el cierre, que dejan la entrega al borde del límite.

## Semana 8 · S8

El trabajo de arquitectura, ADR y pruebas de semanas anteriores se sostiene, pero el commit revisado aún no incluye las piezas de S8. Para cerrar el corte: (1) desplegar el sistema en un proveedor y publicar la URL con la hora de comprobación; (2) exponer un endpoint de health check y registrar su código de respuesta; (3) versionar la infraestructura (Dockerfile/compose o IaC del proveedor) y enlazarla desde el README; (4) configurar logs estructurados con una línea de ejemplo y una métrica consultable atada a un escenario de calidad; (5) declarar las variables de entorno en un .env.example y tomarlas del almacén del proveedor; (6) añadir la estimación de costo mensual con volumen supuesto, costo por pieza y punto de ruptura de la capa gratuita; (7) completar arc42 §7 con una caja por pieza y recoger en §2 el límite de costo y la restricción de tarjeta; (8) registrar un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada. Queda pendiente de semanas anteriores publicar la URL del análisis de SonarCloud con su Quality Gate.
