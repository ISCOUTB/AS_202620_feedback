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

La entrega S6 no incluye los artefactos centrales de la semana: mapa de contextos, tabla módulo-datos, lista de violaciones con plan y sección 8 de arc42.
La documentación base (arc42, C4 niveles 1-2, ADR) está presente, pero falta el análisis de dominio solicitado.
Se recomienda crear el mapa de contextos con relaciones tipificadas (núcleo compartido, cliente-proveedor, capa anticorrupción).
Elaborar la tabla módulo-datos contrastada con los modelos reales (backend/app/domain/model/game.py, frontend/domain/model/Game.js).
Documentar las violaciones encontradas con su plan de corrección y añadir la sección 8 de arc42.
Completar la trazabilidad de aspectos.md (celdas pendientes) y documentar lo rechazado en ia.md.
Añadir instrucciones de arranque y prueba al README y revisar los títulos de los ADR para que enuncien la decisión.
