# Retroalimentación publicable · TAIA

## Semana 1

Muy buen inicio: ficha del problema con usuarios y alcance claros, tabla de aspectos con las ocho columnas, registro de IA ejemplar (con lo aceptado, lo rechazado y su verificación) y plantilla arc42 montada.

Les falta crear `docs/adr/` y `docs/c4/`, declarar en la ficha las dos tensiones de calidad que hacen interesante el problema (por ejemplo, rapidez de captura frente a privacidad del contexto que se envía al LLM), y que los demás integrantes empiecen a aparecer en el historial.

## Semana 2

La sección 1 está muy bien lograda (requisitos con horizonte MVP, objetivos de calidad con métricas, interesados con expectativas), las restricciones están muy bien justificadas y los cinco escenarios desglosan las seis partes.

Antes del corte 1: completen la sección 3 (quedó con texto de plantilla), denle medida numérica al escenario de sustitución del LLM, prioricen el árbol de utilidad por impacto y riesgo, muevan los escenarios y el árbol a la sección 10 del arc42 (hoy están en `docs/calidad/` y la sección quedó vacía), reemplacen el PNG del C4 por un diagrama como código (Mermaid) con leyenda y flechas etiquetadas, añadan restricciones legales y enlacen los escenarios desde `docs/aspectos.md`. Crear `docs/adr/` sigue pendiente desde la semana 1.

## Semana 3

Qué está bien: la sección 4 liga la estrategia a los escenarios S1–S5 con mecanismos concretos, la matriz del ADR compara los tres estilos contra su árbol de utilidad con justificación por escenario, `run.bat` documenta el arranque en un solo comando y los paquetes `domain/application/adapters` por módulo coinciden con el ADR.

Qué corregir antes del corte 1 (semana 5):
1. Renombren `docs/adr/0001.md` a la convención `0001-<kebab-case>.md` y corrijan los enlaces rotos que apuntan a `0001-estilo-arquitectonico.md` (en `aspectos.md` y README) y el placeholder `ruta/al/escenario.md`.
2. El ADR no tiene título que enuncie la decisión ni sección de contexto: complétenlos.
3. Completen la entrada 03 de `docs/ia.md` anotando qué se aceptó y qué se rechazó con su motivo.
4. Monten un workflow para que `backend/tests/test_entrega3.py` corra en cada push y quede evidencia del verde.

## Semana 4 · S4

La entrega tiene un corte vertical claro (HTTP → caso de uso → dominio → persistencia en memoria) y la fila A-01 de aspectos está completa y navegable. Para el primer corte: (1) dejen visible el contenido de las secciones 3, 4, 9, 10 y 12 de arc42 y eliminen restos de plantilla (el archivo aún se llama template); (2) agreguen al ADR-0001 la trazabilidad exigida (requisito, C4, commit, pruebas); (3) ejecuten pytest y suban el run en verde o configuren GitHub Actions, porque hoy no hay evidencia de CI; (4) ajusten el C4 nivel 2 para marcar App Móvil y Base de Datos como objetivo, o no dibujarlas como contenedores actuales. El README documenta bien el arranque con run.bat. Sigan así.

## Semana 5 · CORTE1

El proyecto está mayormente al día: S1-S4 completos, corte vertical A-01 implementado y CI en verde. El correcciones.md debe reestructurarse como índice de verificación: por cada hallazgo, indicar acción, evidencia (commit/run/ruta) y estado. Se recomienda equilibrar la distribución de contribuciones y documentar el historial del ADR. Los commits posteriores al cierre deben evitarse o justificarse. La sustentación y el PDF se resolverán en el aula.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre. Como no existe la etiqueta `corte-1`, se tomó el último commit subido antes del cierre.

Qué está bien: por fin hay un pipeline de integración continua configurado y corriendo en verde, algo que faltaba desde antes. También completaron bastante el arc42.

Qué falta, y es lo más importante: el trabajo de la última noche no atacó el reto de este corte. No hay ninguna restricción nueva diagnosticada, no hay ADR del reto, no hay cambio de código, no hay medición contra un umbral. En cambio, editaron el ADR ya aceptado para añadirle una sección, en vez de crear un ADR nuevo — un ADR aceptado no se edita; si algo cambia, se escribe otro y el anterior queda marcado como reemplazado.

Qué corregir: crear la etiqueta `corte-1` sobre un commit que sí resuelva el reto (restricción, diagnóstico medido, ADR nuevo, cambio implementado, prueba y medición contra el umbral), y revertir o formalizar correctamente la edición del ADR-0001.

## Semana 2 · S2

Buen avance en la definición de calidad: el problema y los interesados están claros y los escenarios 1 a 4 muestran medida. Para la próxima entrega, aseguren que la documentación arc42 esté en archivos propios y en español, agreguen el directorio docs/adr con decisiones reales y lleven la trazabilidad de docs/aspectos.md hasta sus enlaces: una fila sin evidencia navegable no es defendible. El árbol de utilidad debe priorizar por impacto y riesgo, y los cinco escenarios necesitan medida numérica explícita con unidad y condición de carga. Faltó CI en el commit calificado: el repositorio no muestra pruebas ejecutadas en GitHub Actions antes del cierre. Sigan consolidando la identidad de cada integrante en el historial para que se vea el trabajo de todo el equipo.

## Semana 6 · S6

El mapa de contextos, la tabla de propiedad de datos y la auditoría están bien encaminados y trazados a los módulos reales del código. Pendientes concretos: (1) el reajuste de fronteras que documentan necesita un ADR propio que enlace al anterior y deje marcado el reemplazo; (2) si el C4 nivel 3 cambió, actualícenlo en el mismo commit que ese ADR; (3) dejen la tabla de aspectos con sus ocho columnas navegables y la columna de lo rechazado en el registro de IA; (4) falta evidencia auditable de CI y SonarCloud: línea del scanner en el workflow, URL del run del hash revisado y URL pública del análisis con el estado del Quality Gate; (5) hagan reproducible el recorrido de la auditoría de propiedad (comando y rutas citadas) para que una lista sin hallazgos sea defendible.
## Semana 7 · S7

El contrato OpenAPI 3.1 esta bien encaminado: es ejecutable, tiene esquemas de entrada y salida, y el ADR explica por que la integracion es sincrona frente a la alternativa asincrona. Falta cerrar la parte que mas peso tiene en esta semana: que la prueba de contrato se ejecute en el pipeline y que exista una ejecucion en rojo, o la evidencia del cambio incompatible que la hizo fallar, porque hoy solo se ve un archivo de evidencia sin contenido publico. Suban tambien el diagrama C4 nivel 2 con cada flecha etiquetada con protocolo y formato, la salida del historial git del contrato y la evidencia publica de SonarCloud (configuracion, run y Quality Gate). Con esos cuatro cierres la entrega pasa de correcta a defendible en sustentacion.

## Semana 8 · S8

### Recomendaciones prioritarias

- Las secciones 2 y 7 del arc42 ya cubren las restricciones y la topología; el foco pendiente es publicar la URL y comprobar externamente el health check con hora y respuesta.
- Versionen la infraestructura de producción y expliquen cómo recrearla sin pasos manuales.
- Muestren logs estructurados y una métrica consultable ligada a un escenario; calculen costo mensual y punto de ruptura.
- Documenten en ADR la decisión de plataforma y conserven la evidencia del CI en verde.

El avance del backend es sólido: módulos separados, suite de pruebas amplia y documentación arc42 completa y trazable.
Lo central de esta entrega falta: publicar el sistema en una URL accesible desde fuera de la red de la universidad, con hora y código de respuesta anotados.
Versionen la infraestructura (Dockerfile, compose o equivalente) para que el entorno se recree con un comando en lugar de pasos manuales.
Conserven el pipeline en verde y citen el run con su URL y conclusión; enlacen también el análisis estático público para que ambas evidencias sean auditables.
Añadan logs estructurados con campos y una métrica consultable ligada a un escenario de calidad del equipo.
Documenten la estimación de costo mensual desde el volumen esperado, indicando dónde se rompe la capa gratuita.
Escriban un ADR por decisión de plataforma, con la alternativa descartada y la verificación de la capa gratuita.
Declaren las variables de entorno en un .env.example y dejen su valor en el almacén del proveedor.
Mantengan navegables los aspectos y el registro de IA, incluida la columna de lo rechazado y su motivo.
