# Retroalimentación publicable · Drift

## Semana 1

- Está bien: repositorio con el nombre correcto y público; ficha del problema clara con propuesta de solución; `docs/ia.md` iniciado con contenido real; equipo de 4.
- Falta: las dos tensiones de calidad (solo declararon mantenibilidad como aspecto), la tabla de 8 columnas en `docs/aspectos.md`, y la estructura (`docs/arc42/`, `docs/adr/`, `docs/c4/`).
- Corregir antes del corte 1: montar la estructura completa y que los cuatro integrantes firmen commits.

## Semana 2

- Está bien: secciones 1, 2 y 3 redactadas y sin texto de plantilla; 5 escenarios con sus seis partes y medidas numéricas con carga (50 usuarios, p95); restricciones clasificadas por origen y justificadas; contexto coherente con el C4; `docs/ia.md` actualizado.
- Falta: priorizar el árbol de utilidad por impacto y riesgo (hoy es solo una descomposición); añadir leyenda y estilos C4 al diagrama de contexto; llenar `docs/aspectos.md` con la tabla y enlaces a los escenarios; ubicar arc42 y C4 en sus carpetas (`docs/arc42/`, `docs/c4/`).
- Corregir antes del corte 1: completar la trazabilidad aspecto→escenario y definir la herramienta con la que medirán los p95 declarados.

## Semana 3

Qué está bien: la sección 4 liga la estrategia hexagonal a los escenarios con tácticas (aislamiento de adaptadores, mocks/stubs), el ADR 0001 está completo con alternativas motivadas y el backend separa dominio, puertos y adaptadores como pide el estilo.

Qué corregir antes del corte 1 (semana 5):
1. El README documenta dos arranques contradictorios: `mvn spring-boot:run` sin pom.xml y `uvicorn` solo para el backend. Definan un comando único para todo el sistema y borren el que no aplica.
2. La matriz comparativa no referencia los escenarios E1–E5 del árbol de utilidad: digan qué escenario mejora o empeora con cada estilo.
3. El ADR solo se enlaza desde el README: enlácenlo desde `docs/aspectos.md` (y pasen ese archivo a la tabla de 8 columnas) y desde los escenarios que lo motivan.
4. Evidencien la prueba en verde: no hay pipeline ni evidencia de ejecución de `backend/tests/test_health.py`.

## Semana 4 · S4

El corte vertical ya atraviesa interfaz, lógica y persistencia, y la documentación arc42 está completa hasta la sección 12. Para el primer corte: añadan una prueba automatizada que ejercite el recorrido completo de búsqueda (no solo el health check) y evidencien el run en verde. Completen la tabla de trazabilidad de docs/aspectos.md con las columnas Requisito, C4, ADR, Código, Pruebas y Evidencia, verificando que cada enlace exista. Marquen el ADR-0001 como reemplazado por el 0002 y añadan trazabilidad (commit y pruebas) a ambos. Documenten en docs/ia.md lo que se rechazó de la IA y por qué. Incluyan en el README los requisitos previos y el comando único de arranque.

## Semana 5 · CORTE1

El proyecto tiene una base sólida: documentación arc42 completa, C4 claro, corte vertical implementado y pipeline en verde. Sin embargo, hay que corregir la ubicación y nombre de correcciones.md (debe estar en la raíz), arreglar los enlaces rotos en la documentación y completar las celdas pendientes de la tabla de aspectos. Además, los ADR deben seguir la convención de nomenclatura y se debe añadir SonarCloud al pipeline. El equipo ya está trabajando en las correcciones, pero deben asegurarse de que estén en el estado calificado antes del cierre.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Avanzaron bastante en cerrar los pendientes de estructura: `docs/aspectos.md` ya tiene la tabla completa de 8 columnas, `docs/ia.md` registra un rechazo con motivo técnico, el ADR-0001 quedó correctamente marcado como reemplazado por el ADR-0002 (con enlace), el README explica arranque con un único comando y el pipeline de CI corre en verde antes del cierre. Leímos su `docs/correciones.md` completo y la mayoría de esos puntos quedan confirmados por el estado real del repositorio.

Lo que falta, y que ustedes mismos ya habían identificado en ese mismo documento, sigue sin resolverse: no existe la etiqueta `corte-1` (tienen el procedimiento escrito, pero nunca lo ejecutaron), no hay un ADR que registre la restricción nueva que debía asignárseles para este corte, y la medición de línea base quedó en el método definido, sin ejecutar ni registrar un resultado. Esos tres puntos son justamente los que definen si hubo o no una respuesta al reto — el resto del trabajo, aunque valioso, es consolidación de la línea base.

Una observación menor: los títulos de los dos ADR ("Selección de Arquitectura Base") describen el tema, no la decisión — convendría renombrarlos para que el título diga qué se decidió.

Noten también que tres commits llegaron después del cierre del corte (corrección de duplicación en pruebas y documentación en ia.md); no afectan la nota de este corte, pero no cuentan como parte de la entrega.

Para la sustentación: preparen quién explica cuál era la restricción asignada y qué impidió completar su ADR y su medición si ya tenían todo el resto de la infraestructura lista.

## Semana 6 · S6

El repositorio está bien organizado y la trazabilidad de aspectos, C4 y arc42 es clara; se nota trabajo real en la delimitación de contextos y en la tabla de propiedad de datos. Para cerrar la evidencia, el mapa de contextos debe etiquetar el tipo de relación entre contextos (cliente-proveedor, núcleo compartido, capa anticorrupción), no solo el flujo de datos. La auditoría de propiedad gana mucho si el documento deja explícitos el hash revisado, el patrón de búsqueda usado y cada ruta de escritura encontrada, incluso cuando la lista de no conformidades quede vacía. Falta la evidencia pública de integración continua y del análisis estático: el run exitoso y la URL del análisis con su Quality Gate para el commit revisado; un token configurado o un workflow sin ejecución no lo demuestran. Revisen también la trazabilidad de los ADR (enlaces y commit de implementación) y eviten dejar correcciones de la entrega para después del cierre.
## Semana 7 · S7

El contrato ejecutable, su versión y el ADR de integración están bien resueltos y son defendibles. Revisión actualizada tras el cierre: al releer en el repositorio lo que la pasada automática no había podido abrir, se confirma que el pipeline ejecuta la prueba de contrato (instala Schemathesis y corre las pruebas del backend), que el fallo ante el cambio incompatible quedó documentado y corroborado por un run en rojo, que las rutas del contrato corresponden con el código implementado, que la sección 6 de arc42 describe los flujos de interacción, que el C4 de contenedores etiqueta protocolo y formato y que la tabla de aspectos tiene sus ocho columnas y enlaces. Lo único que sigue pendiente es la evidencia pública de SonarCloud: el run del scanner y la URL del análisis con el estado del Quality Gate. Con eso el corte queda completo.

## Semana 8 · S8

La entrega de despliegue quedó resuelta y ordenada: la infraestructura está versionada como código, el entorno de backend se recrea siguiendo el procedimiento documentado, el pipeline corre en verde sobre la rama principal, los logs son estructurados en JSON y la métrica consultable está ligada al escenario de rendimiento. También están bien la estimación de costo con sus supuestos, el límite de costo y la restricción de tarjeta en la sección 2, la vista de despliegue de la sección 7 y los ADR por decisión de plataforma con su alternativa descartada.

Lo que hay que corregir: integren SonarCloud al pipeline con un paso que ejecute el scanner; hoy existe la configuración del proyecto y el Quality Gate es público, pero ningún workflow lo ejecuta, así que el análisis no queda atado a lo revisado. No editen un ADR aceptado: el ADR vigente fue editado después de su aceptación y, si la decisión cambia, debe escribirse uno nuevo que lo reemplace. El archivo de ejemplo de variables que cita la evidencia no está en el repositorio; conviene versionarlo. En la estimación de costos, cuantifiquen el punto de ruptura de la capa gratuita en lugar de describirlo solo de forma cualitativa. Quedan pendientes de calificar la URL del despliegue y la comprobación del health check, que se entregan por Moodle y no se abren en esta pasada.
