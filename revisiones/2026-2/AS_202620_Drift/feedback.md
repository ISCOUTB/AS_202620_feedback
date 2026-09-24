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

El contrato ejecutable, su versión y el ADR de integración están bien resueltos y son defendibles. Lo que falta es la evidencia de ejecución: no se ve la línea del workflow que corre la prueba de contrato, ni el run del pipeline, ni la URL pública del análisis con su Quality Gate. Tampoco se pudo leer la evidencia del cambio incompatible: suban el registro del fallo (salida del pipeline en rojo o diff del cambio que rompió el contrato), porque una prueba que nunca falla no demuestra nada. Completen lo que no llegó legible: código del endpoint frente al contrato, sección 6 de arc42, C4 de contenedores con protocolo y formato en cada flecha, y la tabla de aspectos con sus ocho columnas navegables. Con eso el corte queda sostenible.

## Semana 8 · S8

### Recomendaciones prioritarias

- Expliciten en la sección 2 el límite de costo y la condición de tarjeta; documenten en la sección 7 la topología de despliegue elegida.
- Publiquen URL, respuesta de salud y hora; versionen el despliegue y tomen los secretos del almacén del proveedor.
- Hagan consultables logs estructurados y una métrica de calidad; documenten costo mensual, punto de ruptura y ADR de cada plataforma.
- Enlacen el run de la rama principal para verificar su resultado, sin sustituirlo por una afirmación de estado.

El nucleo del sistema avanza bien y el repositorio esta ordenado, pero la entrega de despliegue aun no esta cerrada. Hoy todo corre en local: publiquen una URL accesible desde fuera y documenten la ruta de health check con su codigo de respuesta. Suban la infraestructura como codigo (Dockerfile o compose y el manifiesto del proveedor) para que el entorno se recree sin pasos manuales, y alinien el README con ese procedimiento. Citen el run de CI sobre la rama principal para verificar su resultado y enlacen el analisis publico con su Quality Gate. Agreguen registro estructurado con campos y una metrica ligada al escenario E1 consultable en el entorno desplegado. Documenten la estimacion de costo mensual con volumen supuesto y el punto de ruptura de la capa gratuita, recojan el limite de costo y la restriccion de 'sin tarjeta' en la seccion 2, y creen un ADR por decision de plataforma con su alternativa descartada. Mantengan el repositorio sin credenciales y sumen un .env.example con las variables requeridas.
