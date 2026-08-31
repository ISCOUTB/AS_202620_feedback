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
