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

## Semana 8 · S8

### Recomendaciones prioritarias

- La sección 2 sí existe en el arc42 principal: agreguen allí el límite de costo y la condición de tarjeta. Sustituyan la sección 7 pendiente por las piezas, plataformas y ubicaciones del despliegue real.
- Publiquen URL, respuesta de salud y hora; distingan la infraestructura local ya versionada de la necesaria para recrear producción.
- Estimen costo mensual y punto de ruptura desde un volumen explícito y documenten cada elección de plataforma en un ADR.
- Mantengan la evidencia del CI en verde junto a la evidencia operativa.

El repositorio esta bien armado: infraestructura como codigo, arranque con un solo comando y secretos fuera del control de versiones; la metrica de EC-07 esta bien atada a su escenario. Lo que sostiene este corte es el entorno desplegado y eso todavia no se puede acreditar: falta la URL publica y la comprobacion del health check con su hora y codigo de respuesta. El CI está en verde; enlacen el run y el análisis estático público como evidencia. La seccion 7 de arc42 sigue pendiente y no hay un ADR por decision de plataforma. Falta la estimacion de costo mensual con supuestos, volumen del escenario y punto de ruptura de la capa gratuita. Prioridad: desplegar, publicar las URLs y cerrar la vista de despliegue.
