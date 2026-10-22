# Retroalimentación publicable · Verifacts

## Semanas 1 y 2

Hola equipo: por decisión del profesor, sus evidencias S1 y S2 se revisaron sobre el estado actual
del repositorio (excepción única: su primer commit llegó después de los cierres).

Lo que está bien: repositorio público con la convención, ficha del problema con usuarios y alcance,
restricciones justificadas y separadas de los requisitos, contexto coherente con el C4 (mermaid
con flechas etiquetadas), un ADR bien formado con opciones evaluadas y el README con instrucciones
de ejecución.

Lo que falta y es urgente para el corte 1:

- **Los 5 escenarios de calidad que declara su PDF de entrega no están en el repositorio.** El
  repositorio es la entrega: suban `docs/escenarios-de-calidad.md` con cada escenario en sus seis
  partes (fuente, estímulo, artefacto, entorno, respuesta, medida numérica).
- Priorizar el árbol de utilidad por impacto y riesgo (hoy es una lista plana de atributos).
- La tabla de aspectos con las 8 columnas y enlaces hasta la evidencia (hoy es narrativa).
- Leyenda en el C4 y dos tensiones de calidad enfrentadas en la ficha del problema.
- El registro de IA como uso real (qué se usó, qué se rechazó y por qué), en `docs/ia.md`.
- Los tres integrantes con commits en el repositorio.

Alinéense también a la estructura mínima del curso: `docs/arc42/` como directorio, `docs/c4/` para
los diagramas y `docs/ia.md` en minúsculas.

## Semana 3

Qué está bien: el ADR 0001 tiene contexto, alternativas descartadas con motivo, decisión y consecuencias, la estructura de paquetes coincide con el monolito modular y la documentación arc42 quedó organizada en carpetas.

Qué corregir antes del corte 1 (semana 5):
1. Completar la sección 4 de arc42 con tácticas concretas ligadas a cada escenario Q-01…Q-05 (hoy son principios genéricos).
2. Rehacer `docs/matriz-estilos.md` contra las ramas de su árbol de utilidad, escenario por escenario.
3. Enlazar el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva, y convertir `docs/IA.md` en el registro de uso de IA (aceptado/rechazado con motivo).
4. Documentar el comando único de arranque en el README (existe `run.py`, no se menciona) y acomodar la estructura mínima (`docs/c4/`).
5. Contribución: los tres integrantes deben aparecer en el historial antes del corte 1.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

Qué está bien: la documentación arc42 (1–6, 9, 10) está redactada con contenido propio, la sección 9 enlaza el ADR, el glosario tiene términos del dominio y los C4 de contexto y contenedores están como código Mermaid y son coherentes entre sí. El README documenta el arranque con un solo comando.

Qué corregir antes del corte 1 (semana 5):
1. El corte vertical al cierre solo cubría `GET /health` (sin lógica ni persistencia); el recorrido completo y su prueba llegaron después del cierre y no contaron para esta evidencia. Para el corte 1 ya está avanzado: asegúrense de empujar a tiempo.
2. La tabla de `docs/aspectos.md` no usa las 8 columnas del curso (falta la cadena requisito-C4-ADR-código): rehacerla y hacer navegable la fila completa hasta Pruebas.
3. Aportar evidencia de CI: la URL del run citada en `aspectos.md` da 404 y no hay runs visibles. Un enlace al run en verde (o ejecutar las pruebas en la sustentación) cierra la fila.
4. Limpiar la basura versionada: `__pycache__/`, `*.pyc`, archivos duplicados `« (1).py»` y PDFs en la raíz (el `.gitignore` ya se corrigió, pero lo versionado sigue en el historial).
5. Sigue pendiente desde S1: que el tercer integrante aparezca en el historial de commits.

## Semana 5 · CORTE1

El proyecto tiene una base sólida: arquitectura documentada, ADR, C4, corte vertical con pruebas y trazabilidad en aspectos.md. Para el compendio, revisen que el equipo declarado coincida con README.md y Equipo.md, y que el historial muestre participación de todos los integrantes. Contrasten correcciones.md con cada hallazgo S1-S4 citando rutas, commits o runs. Aporten la URL del run de CI en verde para el hash calificado. Actualicen la documentación que quedó desfasada: glosario, vista de bloques, C4 de componentes y enlaces rotos. Cierren la evidencia pendiente de A-02 con una prueba de modificación de regla.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

No pudimos revisar el corte 1 porque el repositorio del equipo ya no está en la organización del curso: no responde al clonarlo ni a través de la API, y no aparece en el listado completo de repositorios públicos de la organización. No sabemos si esto pasó por un cambio de visibilidad, un traslado a otra cuenta o un borrado — cualquiera de los tres deja el trabajo fuera de nuestro alcance. La última vez que se pudo ver, el 2026-09-02, el repositorio tenía una base de S4 completa (interfaz, lógica y persistencia con su prueba) pero todavía no mostraba una respuesta al reto del corte 1.

Esto es urgente y no depende de esta revisión: hablen con el docente cuanto antes para restablecer el acceso público al repositorio, con el historial completo tal como estaba. Sin eso no hay manera de calificar el corte, y tampoco de que ustedes mismos demuestren el trabajo que hicieron.

## Semana 1 · S1

Sin actividad S1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 2 · S2

Sin actividad S2: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 6 · S6

El mapa de contextos, la tabla de propiedad y el registro de violaciones muestran que la auditoría se hizo sobre el código actual y con el alcance descrito; buen trabajo en la trazabilidad. Para cerrar: reemplacen el marcador pendiente de la evidencia de CI por la URL de un run concreto y agreguen la fila del aspecto que hoy solo se menciona en el texto; amplíen la auditoría de propiedad a las escrituras (INSERT/UPDATE/.save) en los módulos de negocio; completen el registro de IA con al menos un uso rechazado y su motivo técnico; corrijan la nota que dice que el historial no está implementado; revisen los enlaces del README que apuntan a documentos inexistentes; aporten la URL pública del análisis estático con su Quality Gate; y confirmen que todo el equipo figure en el historial. Los commits subidos después del cierre quedan registrados como correcciones tardías.
## Semana 7 · S7

El contrato OpenAPI 3.1, la prueba de contrato y el ADR de integración están bien construidos y trazados: hay esquemas de datos, correspondencia con los endpoints y el escenario de calidad que motiva la decisión síncrona. La versión del contrato y su historial están en el repositorio, y el workflow de tests ejecuta la prueba de contrato vía pytest. Queda como evidencia externa aportar la URL del run y la URL pública del análisis en SonarCloud con su Quality Gate. Conviene además respaldar el fallo inducido con un run en rojo o un commit que rompa el contrato, en lugar de describirlo únicamente, alinear los documentos rezagados (arc42 §3 y §5 y la fila Q-03, que dice 'Pendiente' mientras la tabla de aspectos afirma que ya hay prueba) y cerrar la medición de P95 y la prueba de usuario de Q-04, que siguen abiertas.

## Semana 8 · S8

La evidencia de despliegue se sostiene: el entorno se define como código versionado, el README documenta el arranque con un único comando Docker, el pipeline del estado calificado está en verde, hay logs estructurados y una métrica de latencia ligada al escenario de calidad pertinente, el documento de costos parte del volumen del sistema e identifica el punto de ruptura de la capa gratuita, y las secciones 2 y 7 del arc42 ya representan las piezas desplegadas, el límite de costo y la condición de tarjeta. El ADR de plataforma compara alternativas y el ADR comparativo del reto mide el arranque en frío del prototipo serverless.

Queda pendiente de calificación, por decisión docente, la comprobación externa fechada de la URL y del health check: la URL del despliegue se entrega por Moodle. Mantengan esos enlaces con hora para el próximo cierre.

Para cerrar en el corte: corrijan el Quality Gate de SonarCloud, que sigue documentado en rojo; dejen de editar ADR ya aceptados (los enlaces de implementación posteriores no sustituyen un ADR de reemplazo); y confirmen la contribución del integrante que aún no aparece en el historial. La medición formal del P95 de Q-01 sigue abierta y conviene cerrarla para que el despliegue sea defendible.

## Semana 9 · S9 (revisión definitiva)

Las pruebas de frontera, las mutaciones y la medición local aportan evidencia sólida. Quedan tres faltantes: la cadena de enlaces de la nueva porción, el registro de IA del periodo y la decisión real sobre componente generativo. La auditoría afirma que varios ya se corrigieron, pero los archivos del repositorio todavía no reflejan esas correcciones; revisen cada cierre contra su destino.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Se documentan estados warm y cold, pero faltan POST en frío, hash desplegado y efecto tras la mitigación. Persisten afirmaciones de causalidad y costo incompatibles con la rectificación del ADR-0008, además de documentación parcial.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación sigue pendiente de calificación docente; no se infiere a partir del repositorio. El [informe del corte](semana-10-corte2.md) y la [planilla](planilla.md) separan ese pendiente del componente técnico.

### Deriva arquitectónica al cierre S10

Vistas asignan la orquestación del análisis al componente equivocado.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · Las vistas de bloques y componentes no reflejan quién orquesta el análisis:** Asignan las dependencias a componentes que no las tienen y presentan POST /analysis como futuro; un mantenedor puede extender el módulo equivocado o evaluar una frontera inexistente. No se evidencia acceso SQL fuera del dueño de Historial. **Acción:** Actualizar C4 con Ingesta/API→Análisis y API→Historial, y arc42 §5 con POST/GET /analysis implementados; remitir a la vista de ejecución §6 que ya explica la orquestación. No forzar una capa nueva si la orquestación actual sigue siendo la decisión elegida. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Confirmen si Render frente a Lambda es la consigna operativa asignada. La comparación debe medir la misma operación y carga: GET /health local en SAM no es equivalente al análisis de texto que exige Q-01. Añadan línea base comparable, resultado y límites, reparen enlaces y confirmen el Quality Gate y la disponibilidad del entorno. El pipeline verde y la cobertura no sustituyen la sustentación.

### Actualización del 10 de octubre de 2026

En esta actualización sí aparecen las correcciones anunciadas: el ADR de semántica y la auditoría resuelven sus rutas, existe el ADR de no incorporar un componente generativo, se rectifica MLAnalyzer y se amplía el registro de IA. También están la tabla de enmiendas y la distinción entre fallos de prueba y errores de infraestructura en el script de mutaciones. Las pruebas y el scanner del estado actual concluyen satisfactoriamente. Estas correcciones actualizan el estado del proyecto; la evaluación histórica de la semana anterior permanece igual.

El reto ya tiene hipótesis, variables y umbral declarados, pero aún deben confirmar su correspondencia con la consigna asignada y medir una comparación equivalente. El evento serverless contiene 63 caracteres, mientras el ADR declara 10.000; la referencia de 46,9 ms es local y usa otro runtime, y el mismo P95 de SAM se asigna a dos operaciones sin series separadas. Publiquen resultados identificados por operación, entorno, fecha y versión, y distingan frío/caliente, duración interna y latencia del usuario. No basta renombrar la medición existente como resultado de otra plataforma.

La API respondió al health check público, pero una respuesta de salud no prueba el flujo de análisis ni recuperación de datos. El equipo ahora documenta un Quality Gate satisfactorio; la consulta pública del evaluador fue bloqueada, por lo que falta verificación independiente de su revisión. Actualicen las vistas que aún niegan el soporte de URL o dejan la medición local como inexistente, mantengan el historial de ADR mediante decisiones nuevas y fijen la versión de pytest-cov. Los límites de comprobación de seguridad y de autoría quedan pendientes, sin presumir una exposición ni atribuir cuentas a personas.

</details>

## Semana 10 · Actualización docente

Se incorporó la calificación de sustentación comunicada por el docente en la planilla y en el [informe S10](semana-10-corte2.md). La evaluación técnica del repositorio mantiene su fundamento y sus observaciones.

## Semana 11 · Integración y resiliencia

La integración, los modos de fallo y la decisión de no extraer están documentados, y hay un diseño explícito de idempotencia. Corrijan las afirmaciones de timeout, códigos de error y WAL/reintentos que todavía no corresponden al código: pueden declararlos pendientes con su plan. Falta incorporar los riesgos en arc42 y enlazar la entrega desde aspectos.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Avance preliminar: SQLite está representado en C4 y el flujo actual es síncrono. Faltan tabla de consistencia por operación, dos contrastes de implementación, estrategia de caché e invalidación y una decisión de datos con costo de reversión argumentado. La sección 8 debe consolidar estas estrategias; los pings de mantenimiento no acreditan la suite ni el Quality Gate.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 0 cerradas, 0 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Solo URLs locales; enlaza guía, pero no dirección pública en README raíz.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Se reconoce avance sustancial de S12: arc42 §8.6–8.9 ya contiene la tabla operación→garantía, contraste de crear/consultar, justificación de no usar caché de aplicación, diseño condicional e invalidación; ADR0012 compara cinco decisiones y argumenta el mayor costo de revertir contenido completo sin propietario. La revisión estática confirma INSERT/commit y lectura por otra conexión, seis pruebas de consistencia, refresh del historial tras POST y caché de estáticos nginx. El run Sonar del 22 de octubre registra 50 pruebas aprobadas y QUALITY GATE STATUS: PASSED; ya no corresponde afirmar que solo hay pings o scanner no verificado. Pendientes: publicar dominio iscoutb.dev con certificado válido; actualizar README que aún mezcla 20/44 pruebas y token Sonar pendiente; acotar la palabra linearizable al modelo y pruebas realmente observados, sin equiparar pruebas secuenciales a prueba de concurrencia. Alinear C4 con el proxy nginx de despliegue y continuar las mitigaciones SSRF/historial sin propietario declaradas pendientes, sin tratar el ADR como corrección de código.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Externo. URL pública HTTP sslip; falta dominio institucional con certificado válido. URL documentada: http://verifacts-sistema-ju3vi7-444522-144-24-4-187.sslip.io. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#verifacts) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).
