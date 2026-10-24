# Retroalimentación publicable · Calificación automática

## Semana 1

Excelente montaje: estructura casi completa, plantilla arc42 en Markdown, tabla de aspectos con las ocho columnas y un aspecto bien declarado, registro de IA con qué se aceptó, qué se rechazó y por qué, y dos tensiones de calidad muy bien formuladas.

Ajustes pendientes: la ficha del problema no está en el repositorio (solo se menciona el «Informe Inicial» de Moodle) — súbanla para que la entrega sea defendible desde el repo. `docs/adr/` y `docs/c4/` quedaron como archivos vacíos en lugar de directorios: conviene dejarlos como directorios con `.gitkeep`. Y la contribución sigue concentrada en una sola cuenta: los demás integrantes deben empezar a aparecer en el historial.

## Semana 2

Trabajo sobresaliente: cinco escenarios con las seis partes y medidas numéricas con condición de carga, árbol de utilidad con impacto y riesgo, secciones 1 y 3 redactadas, y C4 de contexto como código Mermaid con flecha etiquetada.

Antes del corte 1: enlacen cada escenario desde la fila de su aspecto en `docs/aspectos.md` (la tabla de trazabilidad sigue en «Pendiente»), completen las restricciones con categorías organizativas y legales (hoy son todas técnicas o de alcance), y repartan las contribuciones entre todos los integrantes, que es lo que más se va a notar en el corte.

## Semana 3

Qué está bien: la documentación quedó sólida: sección 4 con tácticas por escenario, matriz comparativa contra el árbol (§4.1), tres ADR con convención, alternativas descartadas y reemplazo correcto del 0001, y enlaces al ADR desde `aspectos.md` y desde EC-04/EC-05.

Qué corregir antes del corte 1 (semana 5):
1. Al cierre, el README seguía con el checklist «[ ] Código» sin marcar: no había comando de arranque documentado.
2. Al cierre no existían la prueba ni el pipeline, y los paquetes de los 7 módulos del ADR-0002 no estaban en el repo.
3. Para S4 traigan el esqueleto con sus módulos y el run en verde dentro del plazo de la entrega.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

Buen avance: el corte vertical A-01 está construido y documentado, los ADRs son sólidos y el README permite arrancar con un solo comando. Para el primer corte, completen el C4 nivel 2 con su diagrama y actualicen la tabla de niveles; la fila A-01 de aspectos.md debe enlazar un contenedor C4 real, no 'C2 pendiente'. Suban evidencia del run de CI en verde (URL) para confirmar las 34+6 pruebas. Revisen que la sección 9 del arc42 cite los ADRs y que el glosario tenga términos del dominio. El resto de la documentación se ve coherente.

## Semana 5 · CORTE1

El repositorio está bien estructurado y el corte vertical A-01 es sólido, con medición de EC-07 y pruebas. Para el cierre, aseguren que correcciones.md enlace cada hallazgo de S1-S4 con evidencia verificable (commit, ruta o run). Adjunten la URL del run de CI correspondiente al hash calificado, ya que el workflow existe pero no se pudo verificar su ejecución. Revisen docs/ia.md para que cada uso de IA incluya qué se rechazó y por qué. Mantengan el ritmo de contribuciones más equilibrado. El proyecto está al día; solo falta evidencia externa para cerrar los pendientes.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre, sobre la etiqueta `corte-1`, que sí existe y apunta a un commit dentro del plazo.

Qué está bien: el reto quedó resuelto por completo. Midieron el problema antes de decidir (encontraron que, cuando la cola de trabajos se cae a mitad de un lote, el sistema perdía el reporte del 100% de las hojas), compararon cuatro alternativas con argumentos técnicos reales, tomaron una decisión documentada, la implementaron sin romper el arranque de un solo comando, y volvieron a medir para comprobar que el problema quedó resuelto (0% de pérdida) dentro del tiempo permitido. También corrigieron con datos varios señalamientos de la revisión anterior sobre semanas previas (el pipeline sí corría en verde, el diagrama C4 sí estaba completo, el registro de IA sí tenía contenido).

Qué falta: todo el ejercicio del reto quedó en un solo commit muy grande, lo que dificulta ver el proceso paso a paso; en el futuro conviene dividir el trabajo en varios commits. Queda pendiente adjuntar el PDF de dos páginas en Moodle, y una de las pruebas nuevas tiene un hueco de cobertura que el propio equipo ya reconoció (una mutación que ninguna prueba detecta).

Para la sustentación: preparen cómo justifican haber trabajado sobre la deuda declarada (R-06) al no recibir la restricción de Moodle, y qué tan bien encajaría la misma solución si la restricción real resulta ser otra.

## Semana 2 · S2

La entrega de la semana 2 deja la documentación base (C4 nivel 1, contexto y restricciones) y un primer aspecto en aspectos.md, pero los escenarios de calidad y el árbol de utilidad están pendientes. Para la próxima entrega: redacten 3 a 5 escenarios completos en la sección 10 con medida numérica (cifra, unidad y condición de carga), clasifiquen las restricciones en técnicas/organizativas/legales, y hagan navegable la tabla de aspectos. Revisen también que el README diga cómo arrancar y probar, y que el registro de IA siga creciendo con cada uso. Los cambios recientes van en la dirección correcta: los ADR, el pipeline y el corte vertical de A-01 deben quedar evidenciados con sus runs. Sigan consolidando los commits de todo el equipo.

## Semana 7 · S7

La entrega resolvió de forma completa el objetivo de la semana: el contrato OpenAPI está versionado, coincide automáticamente con la API y tiene pruebas propias en el pipeline. La evidencia del cambio incompatible es especialmente sólida: registra una ruptura deliberada, el fallo contractual que produjo y la recuperación posterior. El ADR justifica la integración contra escenarios concretos, la sección 6 de arc42 describe los flujos y el C4 nivel 2 explicita protocolo y formato en sus relaciones.

La no conformidad pendiente es transversal: todavía falta evidencia pública y auditable de SonarCloud con su configuración, la ejecución del scanner y el Quality Gate. También deben confirmar de forma explícita la asociación de las cuentas que aún no están mapeadas en el registro del curso.

## Semana 6 · S6

El avance en contextos delimitados y propiedad de datos es visible: el ADR-0007 y el documento 08-propiedad-de-datos.md dan una base sólida para discutir límites. Para cerrar la evidencia, adjunten el run de CI y la URL pública de SonarCloud con el Quality Gate, ya que sin ellos la verificación transversal queda incompleta. También falta poder revisar el contenido de aspectos.md y ia.md, y la sección 8 del arc42 con lenguaje ubicuo y mapa. Si los límites cambiaron desde el primer corte, dejen el diff contra el hash revisado en S5 y el C4 nivel 3 actualizado. Documentar explícitamente las no conformidades encontradas, o el recorrido que descartó su presencia, reforzará la sustentación. Buen trabajo de documentación; completen la evidencia verificable.

## Semana 8 · S8 · revisión definitiva

La evidencia queda completa en todo lo que depende del repositorio. La infraestructura como código está versionada para local y para producción (un descriptor de plataforma y dos imágenes), el arranque con un solo comando está documentado y el despliegue se puede recrear paso a paso. La observabilidad subió de nivel: los logs salen como una línea JSON por evento con campos con nombre y la métrica de confirmación del lote está atada explícitamente al escenario de calidad con su umbral. La estimación de costo sale del volumen del proyecto y dice en qué punto se rompe cada capa gratuita. Las secciones 2 y 7 del arc42 recogen la restricción de costo cero y las piezas del despliegue con su ubicación, y hay un ADR por cada decisión de plataforma con su alternativa descartada. El pipeline de la rama principal está en verde para el commit calificado y los cuatro integrantes contribuyen en el historial.

Dos no conformidades quedan abiertas. La primera es transversal y viene de atrás: SonarCloud no es auditable desde el pipeline. El análisis corre desde la interfaz del servicio, pero el workflow no invoca el scanner y no hay archivo de configuración del análisis, que son dos de las tres evidencias que el contrato pide desde la semana 6. Conviene cerrarla agregando el paso del scanner al workflow y publicando el análisis con su Quality Gate.

La segunda es pequeña pero conviene corregirla: un ADR ya aceptado se editó después para actualizar enlaces de documentación, sin escribir un ADR de reemplazo. La convención es no tocar un ADR aceptado; si solo cambian referencias internas, háganlo con un nuevo ADR que lo precise, o dejen constancia del ajuste, para que el historial de decisiones se mantenga íntegro.

En resumen: la semana está completa en la ficha y muy bien evidenciada. Cierren SonarCloud y cuiden la inmutabilidad de los ADR de cara a la sustentación del corte.

## Semana 9 · S9 (revisión definitiva)

RF-11 ya cuenta con cadena completa, prueba de defecto, auditoría de fronteras y evaluación generativa con datos versionados, costo y latencia. La lectura del resultado confirma las cifras de cuarenta solicitudes y distingue medición interna de experiencia pública. Conservan límites importantes: propuestas revisadas por una persona, equivalencias matemáticas y ruta que consume cuota sin autenticación. Cierren Sonar y la prueba de dueño único. El barrido independiente de secretos quedó pendiente por el entorno revisor, sin una credencial encontrada.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El presupuesto atómico responde al escenario con línea base, degradación medida y arquitectura y contrato actualizados. La auditoría de dependencias sigue vigente: los manifiestos no cambiaron de S9 a S10 y el código nuevo utiliza la biblioteca estándar. No se exige una auditoría nueva ni se añaden requisitos de vulnerabilidades ajenos a la ficha.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Sin deriva material observada en los recorridos inspeccionados.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

No se observó deriva material en los recorridos revisados; se conservan los límites y deudas explícitos del diseño.

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Antes de evaluar el segundo corte identifiquen la asignación operativa oficial. La evaluación de distractores es una buena base de S9, pero no prueba por sí sola una línea base y respuesta al reto S10. Frontend y salud responden; falta demostrar el flujo principal, seguridad de acceso/cuota, métrica del reto y pipeline en vivo. La sustentación queda pendiente.

</details>

## Semana 9 · Aclaración de la revisión

La comprobación de credenciales bloqueada por el entorno del revisor queda excluida del cálculo por decisión docente. Sigue sin verificarse y no implica un hallazgo de filtración. Los demás criterios conservan su valoración sobre la entrega de cierre; véase la [matriz actualizada](semana-09-evidencia-s9.md).

## Semana 6 · Rectificación de la revisión

La lectura completa confirma que el mapa de contextos, la propiedad de datos, los hallazgos con plan y la correspondencia de aspectos estaban en la entrega original. Se corrigen las observaciones producidas por una lectura parcial; no se exige un ADR de reajuste cuando no cambiaron los límites. Consulta la [matriz rectificada](semana-06-evidencia-s6.md) para los alcances y pendientes transversales.

## Semana 11 · Integración y resiliencia

S11 presenta una tabla completa de fallos, mitigaciones coherentes y una comparación seria que justifica no extraer módulos. Los límites de BLPOP, premarcado y deduplicación temporal se reconocen, sin exigir que se implemente ahora toda la solución futura. Conserven la distinción entre el worker que consume y registra y el procesamiento de calificaciones aún previsto.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

El avance distingue almacenes y broker en C4 y declara pérdidas y duplicados posibles del flujo Redis. Aún faltan tabla de consistencia con dos operaciones verificables, diseño de caché e invalidación, ADR del mayor costo de reversión y estrategia completa en arc42. Una marca de deduplicación con expiración no sustituye el diseño de caché de datos.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 0 cerradas, 0 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Externo**. Frontend y API en Render. Dirección(es) documentada(s): https://quantia-utb.onrender.com ; https://quantia-utb-api.onrender.com/health.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Sin commits nuevos desde 20 de octubre; CI success. README sigue con Render y riesgos reconocidos de almacén efímero.

**Próximos pasos:**
- Tabla recepción/encolado/consumo → garantía, distinguir bitácora, BLPOP sin ack y deduplicación TTL de persistencia durable.
- Decidir caché o no caché con motivo e invalidación tras cambios de examen/carga, no confundir marca de deduplicación con caché de lectura.
- ADR comparativo de decisión de datos/reversión, cerrar R-06 y reflejar consistencia/caché en arc42 §8.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Externo. Frontend y API en Render, fuera del dominio requerido. URL documentada: https://quantia-utb.onrender.com ; https://quantia-utb-api.onrender.com/health. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#sistema-de-calificacion-automatica) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Hay avances nuevos en recepción de lotes: errores de almacenamiento/bitácora se reportan por hoja sin abortar todo el lote, el encolado tiene un presupuesto temporal de lote, las hojas se leen de una en una con límite de 20 MB y la confirmación pasa a un hilo fuera del event loop. Se reutiliza el cliente Redis y un timeout al consumir ya no se trata como cola vacía. También se corrigen equivalencias/distractores, mensajes de carga, límite diario y división por cero en el panel. CI actual registra frontend y backend exitosos, incluida la suite completa, contrato y modos de fallo. README y documentos de arquitectura no cambiaron: conservan deuda de almacenamiento efímero, falta de acuse en la cola y reintento no automatizado. Estas mejoras no acreditan persistencia durable ni cierran S12 por sí solas.

**Próximos pasos:**
- Actualizar la tabla operación→garantía para recibir, registrar y consumir hojas, diferenciando archivo/bitácora, publicación y BLPOP sin acuse; contrastar al menos dos recorridos con el código nuevo.
- Volver a medir EC-07 con almacenamiento y Redis reales: el plazo de encolado no limita por sí solo la lectura/escritura completa del lote. Conservar límites de disco efímero, reconciliación y entrega ante pérdida del worker.
- Resolver el ADR comparativo de persistencia/R-06 y justificar caché o no caché con política de invalidación; sincronizar README, arc42 §8 y C4 con la implementación actual. Publicar dominio institucional.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Externo. Sitio y API en Render, sin subdominio institucional. URL documentada: https://quantia-utb.onrender.com ; https://quantia-utb-api.onrender.com/health. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#sistema-de-calificacion-automatica) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).
