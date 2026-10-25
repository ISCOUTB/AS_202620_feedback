# Retroalimentación publicable · InvenTrack

## Semana 1 · Equipo, problema y repositorio

Buen arranque: la ficha del problema está bien escrita, con usuarios y alcance claros, y el registro de IA ya nombra la herramienta y el uso concreto. El repositorio es público y correcto.

Para cerrar la semana: declaren en la ficha las dos tensiones de calidad enfrentadas (hoy solo está el aspecto de consistencia), conviertan `aspectos.md` a la tabla de ocho columnas del curso, y monten `docs/arc42/` con la plantilla más `docs/adr/` y `docs/c4/` (suban contenido o un `.gitkeep`, git no guarda carpetas vacías). Revisen también que los cuatro integrantes tengan acceso al repositorio: el historial de la semana solo muestra a una persona.

## Semana 2 · S2

La documentación de la semana 2 está completa y trazable: secciones 1, 2, 3 y 10 del arc42 con contenido real, 5 escenarios con medida numérica, árbol de utilidad priorizado y C4 de contexto en Mermaid. Para próximas entregas, usen archivos por sección (01-objetivos.md, 02-restricciones.md, etc.) y activen el pipeline con pruebas para que la evidencia quede en los runs. El registro de IA y la tabla de aspectos van bien encaminados.
## Semana 3

Qué está bien: entrega completa: ADR 0001 con contexto, alternativas y consecuencias, matriz comparativa por escenario, esqueleto modular con arranque documentado, enlaces del ADR desde `aspectos.md` y ESC-01, `docs/ia.md` al día y CI en verde.

Qué corregir antes del corte 1 (semana 5):
1. Ratifiquen el ADR 0001 como «aceptado» (hoy dice «propuesto, pendiente de ratificación») y ajusten el título para que enuncie la decisión.
2. Mantenimiento: conserven el pipeline en verde en cada entrega y sigan enlazando cada decisión desde su aspecto y su escenario.

## Semana 4 · S4

Buen avance en documentación, C4 y estructura del esqueleto: el arc42, los diagramas y la organización por módulos son sólidos. Para completar la semana 4, redacten las secciones 5 y 6 con la interpretación de los diagramas, inicien el glosario y hagan que la fila de aspectos apunte a una prueba real del corte vertical. Cuiden las convenciones de ADR: un archivo por decisión real y con nombre estandarizado. Aunque los commits posteriores al cierre corrigen varios vacíos, esas correcciones no cuentan para la entrega de la semana.
## Semana 5 · CORTE1

El proyecto está sólido: corte vertical funcional, documentación arc42/C4/ADR completa y trazabilidad de aspectos navegable, con CI en verde. Para el próximo corte: reestructuren correcciones.md como tabla por hallazgo (acción, ruta, commit/run, estado) para que cada corrección sea contrastable. Aporten evidencia de SonarCloud (URL del análisis o workflow), no solo el archivo de propiedades. Equilibren la participación en el historial. Recuerden adjuntar el PDF en Moodle y preparar la sustentación.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya tienen la etiqueta `corte-1` sobre un commit anterior al cierre: bien.

El diagnóstico, el ADR y el reporte de medición del reto de concurrencia están redactados con un nivel técnico muy alto: identifican síntoma, causa raíz y riesgo, comparan tres alternativas con sus ventajas y desventajas, y presentan una tabla de resultados con cifras concretas. El registro de uso de IA también quedó completo, con un rechazo explícito y bien argumentado.

Pero hay un problema serio que hay que resolver antes de la sustentación: revisando el código del repositorio, el mecanismo que describen en el ADR (un lock por SKU) no aparece en ningún archivo. Los módulos de inventario no cambiaron entre la entrega anterior y esta etiqueta — solo se agregó una prueba nueva y la documentación. Las cifras de latencia que reportan tampoco tienen, en el repositorio, ningún código que las calcule. La prueba que sí existe pasa, pero no porque haya un mecanismo de exclusión mutua: simplemente verifica que el stock final quede correcto.

Antes de sustentar, implementen de verdad el mecanismo que describieron (o documenten honestamente cuál es el estado real) y agreguen el código que efectivamente mida la latencia que están reportando. Traigan también, si la tienen, una cifra de línea base real (antes del cambio), no solo la afirmación de que el problema existía.

## Semana 6 · S6

La entrega de la semana 6 está sólida: el mapa de contextos, la tabla de propiedad de datos y la auditoría de modularidad están bien documentados y trazados. Para cerrar los pendientes: (1) verifica que la sección 8 del arc42 incluya explícitamente el lenguaje ubicuo y el mapa de contextos, y actualiza el README para reflejarlo; (2) deja evidencia de la ejecución del pipeline (enlace a un run de GitHub Actions) y decide si SonarCloud vuelve al workflow; (3) los módulos vacíos (usuarios, proveedores, alertas) deberían tener al menos una nota de estado en el mapa de contextos. El resto cumple con lo pedido.

## Semana 7 · S7

El contrato OpenAPI, sus esquemas, la correspondencia con los routers, la prueba contractual, su ejecución en el pipeline, el ADR, la vista de ejecución y el C4 están presentes y verificables. Para cerrar la única no conformidad de la ficha, conserven una evidencia reproducible de que la prueba falla ante un cambio incompatible. Unifiquen además la versión declarada en el documento de API con la versión del contrato ejecutable y mantengan SonarCloud auditable.

## Semana 8 · S8 (revisión definitiva)

La entrega cubre las diez filas graduables de la ficha. La infraestructura está versionada (imagen y definición de despliegue), el README reproduce el entorno, el pipeline corre en verde con análisis estático público y Quality Gate en orden, y hay logs estructurados, una métrica consultable ligada a un escenario de calidad y secretos tomados del almacén. La documentación de arquitectura incorpora la vista de despliegue con una pieza por nodo, el límite de costo en las restricciones y un ADR de plataforma con la alternativa descartada y la capa gratuita verificada. La estimación mensual parte de un volumen supuesto y fija el punto de ruptura de la capa gratuita.

### Recomendaciones prioritarias

- Mantengan inmutables los ADR aceptados: los cambios de decisión van en un ADR nuevo que reemplace al anterior, no editando el original.
- Repartan la contribución: hoy dos integrantes concentran la mayor parte del historial.
- Conserven la evidencia del pipeline y del análisis estático para el commit que entreguen.

Pendiente de calificar: las filas de URL accesible desde fuera de la red y de health check consultable, porque la URL se entrega por Moodle y no estaba disponible en esta pasada. El repositorio sí declara la URL pública y la ruta de salud, que se verificarán en la segunda pasada.

## Semana 9 · S9 (revisión definitiva)

La porción p95 ya está implementada, enlazada y acompañada de una prueba que distingue el percentil del máximo. La medición debe ejercitar consultas reales de catálogo o stock con la carga declarada: medir /health local no demuestra ese escenario. Mantengan la justificación de no añadir dependencias y completen la trazabilidad de reemplazo de ADR anteriores. La comprobación de credenciales quedó pendiente por una limitación técnica del revisor; no se atribuye al equipo y la propuesta de nota permanece abierta.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El reporte S10 define el escenario y un cambio coherente. La cifra de 28 ms no tiene una prueba o serie que mida latencia; faltan una línea base y una nueva medición demostrada. La documentación continúa parcial.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación sigue pendiente de calificación docente; no se infiere a partir del repositorio. El [informe del corte](semana-10-corte2.md) y la [planilla](planilla.md) separan ese pendiente del componente técnico.

### Deriva arquitectónica al cierre S10

Errores de dominio no se traducen al contrato HTTP.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · Errores de cantidad del dominio escapan al borde HTTP:** El contrato enumera rechazos controlados pero una cantidad 0 o negativa, admitida como int por el esquema HTTP, llega al dominio y lanza ValueError sin traducción. La ruta puede producir un 500 genérico donde debería rechazar una entrada inválida; se debilita la frontera HTTP/dominio. Es deducción estática, no fallo observado en producción. **Acción:** Definir un error de cantidad de dominio y mapearlo a 400/422 en ambos handlers, o validar también cantidad>0 en el esquema conservando la regla de dominio. Actualizar OpenAPI y pruebas negativas HTTP de entrada/salida con 0 y negativos. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Las sondas públicas de salud y métricas responden. Confirmen el escenario operativo asignado, midan una línea base del flujo de negocio y comparen la respuesta con el umbral en el despliegue. Aporten evidencia actual del pipeline y Quality Gate y preparen la defensa del almacenamiento en memoria y de su costo de evolución.

</details>

## Semana 9 · Aclaración de la revisión

La comprobación de credenciales bloqueada por el entorno del revisor queda excluida del cálculo por decisión docente. Sigue sin verificarse y no implica un hallazgo de filtración. Los demás criterios conservan su valoración sobre la entrega de cierre; véase la [matriz actualizada](semana-09-evidencia-s9.md).

## Semana 10 · Actualización docente

Se incorporó la calificación de sustentación comunicada por el docente en la planilla y en el [informe S10](semana-10-corte2.md). La evaluación técnica del repositorio mantiene su fundamento y sus observaciones.

## Semana 11 · Integración y resiliencia

El análisis y la decisión de no extraer están trazados al inventario real. Corrijan la tabla que equipara serialización con prevención de duplicados: el ADR nuevo reconoce correctamente que la idempotencia sigue pendiente. La contención local tiene prueba, pero no demuestra durabilidad ni coordinación entre réplicas.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Todavía faltan la tabla de garantías por operación, una estrategia razonada de caché e invalidación y la decisión de datos con costo de reversión. Los repositorios RAM son el almacenamiento primario y viven dentro de la API. Mantengan explícita la separación entre arquitectura vigente y SQL futuro. Corrijan el límite del contenedor: los repositorios RAM no constituyen un desplegable independiente.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 7 cerradas, 7 en total**. Los 7 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Institucional**. Servicio/API institucional y alternativa Render; distinguir interfaz de API. Dirección(es) documentada(s): https://inventrack.iscoutb.dev ; https://inventrack-api.onrender.com.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

La punta no cambia desde el 19 de octubre y Run Tests termina correctamente. La API utiliza RAM como almacén primario, no como caché; el despliegue de la interfaz Flutter continúa pendiente en la documentación.

**Próximos pasos:**
- Tabla entrada/salida/consulta → garantía real; lock local no da durabilidad ni coordinación entre réplicas.
- Justificar no caché o declarar invalidación por stock/producto; ADR costo de reversión.
- Corregir C4: RAM pertenece al proceso API, SQL futuro no desplegado; actualizar backlog S12 aunquesiete issues cerradas.

**Issues:** 0 abiertas y 7 cerradas; 0 abiertas sin responsable. Cierres: 7 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Institucional. API únicamente, Flutter pendiente; RAM almacén primario, no caché. URL documentada: https://inventrack.iscoutb.dev ; https://inventrack-api.onrender.com. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#inventrack) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Hay avance S12: docs/aspectos.md incorpora una tabla de cinco operaciones y garantías, con límites explícitos de memoria, una instancia y ausencia de deduplicación durable. La lectura de registrar_entrada y registrar_salida confirma el lock por SKU; esto no aporta durabilidad ni coordinación entre réplicas. También se refactorizó el router para centralizar errores. El CI vigente ejecutó Pytest con cobertura, validación del contrato y el paso de scanner correctamente; no se infiere un Quality Gate independiente solo del scanner.

**Próximos pasos:**
- Añadir rutas y pruebas concretas a la tabla para dejar trazables dos operaciones; no confundir respuestas HTTP distintas con pérdida automática de idempotencia del efecto.
- Justificar no caché o definir diseño e invalidación; documentar comparativamente la decisión de datos más costosa de revertir.
- Llevar consistencia/caché a arc42 §8 y alinear C4 con RAM dentro del proceso, diferenciando SQL futuro.

**Issues:** 0 abiertas y 7 cerradas; 0 abiertas sin responsable. Cierres: 7 completed. El estado registrado no acredita por sí solo implementación.

**README:** Institucional. API institucional y alternativa Render; frontend Flutter sigue pendiente en el README. URL documentada: https://inventrack.iscoutb.dev ; https://inventrack-api.onrender.com. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#inventrack) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Avance documental S12 en docs/aspectos.md: declara política efectiva sin caché para el MVP en memoria y diseño futuro cache-aside Redis, claves versionadas, TTL e invalidación tras escritura con tratamiento de fallo. Es diseño condicionado a persistencia compartida, no Redis implementado. El nuevo run ejecuta Pytest con cobertura, contrato y scanner exitosamente; scanner no demuestra por sí solo Quality Gate. README sin cambios: API institucional, Flutter pendiente.

**Próximos pasos:**
- Reconocer el diseño de caché nuevo sin pedirlo como ausente; mantener diferenciada política actual sin caché y evolución Redis.
- Resolver trazabilidad de dos operaciones, ADR comparativo de costo de reversión y alineación de arc42 §8/C4 con RAM actual.
- Probar carreras entre repoblación e invalidación y fallos cuando se implemente caché; TTL/Redis por sí solos no garantizan lectura fuerte.

**Issues GitHub:** 0 abiertas y 7 cerradas; 0 abiertas sin asignar. Cierres: 7 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. API; API alternativa

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#inventrack) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).
