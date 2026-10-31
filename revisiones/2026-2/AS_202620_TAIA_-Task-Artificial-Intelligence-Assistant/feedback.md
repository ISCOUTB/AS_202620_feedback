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

El contrato OpenAPI 3.1 es ejecutable y tiene esquemas de entrada y salida; la prueba de contrato se ejecuta en el pipeline, su comparador detecta un cambio incompatible y el ADR explica por qué la integración es síncrona frente a la alternativa asíncrona. El C4 nivel 2 ya etiqueta cada flecha con protocolo y formato, y el contrato tiene historial en git. Queda pendiente el análisis estático público: el pipeline no invoca ningún scanner y no hay una URL con Quality Gate que auditar. En sustentación conviene explicar el demo de ruptura y la correspondencia del archivo de evidencia con el estado calificado.

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

## Semana 8 · S8 (revisión definitiva)

Gran salto en esta entrega: el sistema ya tiene infraestructura como código versionada (imagen Docker y descripción de la máquina con Terraform), un pipeline que corre las pruebas y despliega de forma automática al integrar en la rama principal, logs estructurados en JSON y una métrica de latencia ligada a un escenario de calidad. También quedaron la estimación de costo con supuestos y su punto de ruptura, y un ADR por decisión de plataforma (API y base de datos) con la alternativa descartada y la capa gratuita verificada.

Dos filas de despliegue quedaron pendientes de calificar porque la URL se entrega por Moodle y no se probó ninguna; el repositorio sí declara la URL pública y la ruta de health, lo que deja la comprobación para la segunda pasada.

Para cerrar del todo: (1) versionen un `.env.example` sin valores reales, hoy el archivo no existe y tanto el README como la sección 7 del arc42 lo enlazan; (2) no editen un ADR ya aceptado —si la decisión cambia, escriban uno nuevo y marquen el anterior como reemplazado—; (3) registren en `docs/ia.md` el uso de IA del periodo, que no creció esta semana; y (4) añadan el análisis estático público (configuración, ejecución del scanner y URL con el Quality Gate) para que el pipeline sea auditable de punta a punta.

## Semana 9 · S9 (revisión definitiva)

La nueva porción de confirmación tiene una decisión clara y pruebas rojas y verdes verificables. Ya hay evaluación real del modelo con costo y latencia, y los límites están bien declarados. Para cerrar la medición asociada, comprueben los campos persistidos tras confirmar y el tiempo hasta el canal; no presenten extracción como el escenario completo. Resuelvan CI, los conflictos de documentación y el cierre del valor predeterminado histórico de firma.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Antes fallaban siete de dieciséis variantes; después, la confirmación tiene medición y normalización implementada, con alternativas. Ese logro no se extiende a la persistencia S1 ni a la latencia S3 completas. El CI falla, CD se omite y arc42 contiene conflictos de merge.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

arc42 mantiene repositorios en memoria tras la migración SQL.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · arc42 presenta repositorios volátiles como actuales después de la migración SQL:** Una lectura de la vista de bloques conduce a configurar o evaluar una persistencia distinta de la realmente requerida para arrancar y operar. No es inversión incorrecta de dependencias: el reemplazo por adaptadores sí está realizado. **Acción:** Actualizar arc42 §5.5/5.6 y diagramas a SQLAlchemy/PostgreSQL; conservar InMemory como dobles de prueba. Limpiar los conflictos de merge en §7, manteniendo explícita la precedencia de la guía Dokploy. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Documenten el escenario operativo oficialmente asignado, con un antes y un después reproducibles en el despliegue. El health responde, pero el CI actual falla y CD queda omitido: verifiquen la versión desplegada y repitan el flujo conversacional después de corregirlo. Instrumenten fallos del proveedor y consumo por petición, revisen el timeout y sincronicen la documentación de Dokploy antes de la sustentación.

</details>

## Semana 11 · Integración y resiliencia

S11 cubre integración, modos de fallo, mitigaciones y decisión de no extracción con trazabilidad. El reclamo atómico de confirmación está implementado, pero la escritura posterior de la tarea puede fallar y perder la acción, límite que está declarado. La idempotencia del registro de una notificación no demuestra que Telegram se envíe una sola vez.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Se reconocen dos operaciones locales con transacción y bloqueo, pero falta tabla operación→garantía y una estrategia de caché con invalidación o exclusión justificada. También faltan ADR y costo comparativo de la decisión de datos más costosa de revertir, tecnología de la base en C4 y consolidación en arc42. El cambio posterior del Dockerfile no completa esos entregables.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Presentó avances y despliega bien, según confirmación docente. El README aún publica sslip.io/Render: actualizar la URL oficial bajo iscoutb.dev. Las issues antiguas no invalidan el avance presentado.

Issues al corte de consulta: **3 abiertas, 4 cerradas, 7 en total**. Los 4 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Externo**. Actualizar URL oficial; el docente confirmó avance y despliegue funcionando. Dirección(es) documentada(s): http://taia-sistema-jkbo9i-ec2cd4-144-24-4-187.sslip.io ; https://taia-backend-latest.onrender.com/health.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Se reconoce la presentación y el despliegue funcionando confirmados por el docente. El README ya publica la API en https://taia-sistema.iscoutb.dev y sus rutas de salud/documentación; es evidencia del backend, no de una aplicación Flutter ya entregada. CI y CD del último commit terminaron correctamente. No se mantienen como vigentes las comprobaciones fallidas sobre el antiguo dominio sslip. Para S12, completar la tabla operación→garantía, acotar las transacciones de confirmación y notificación frente a crear tareas/enviar Telegram, justificar no usar caché o definir invalidación, y seleccionar comparativamente la decisión de datos más costosa de revertir. Anotar PostgreSQL en C4 nivel2 y consolidar consistencia/caché en arc42 §8. Actualizar las tres issues abiertas antiguas y asignar las dos sin responsable; su antigüedad no niega el avance demostrado.

**Issues:** 3 abiertas y 4 cerradas; 2 abiertas sin responsable. Cierres: 4 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Institucional. Ahora publica API institucional, salud y documentación; no acredita entrega de una interfaz Flutter. Despliegue funcionando confirmado por docente. URL documentada: https://taia-sistema.iscoutb.dev ; https://taia-sistema.iscoutb.dev/health ; https://taia-sistema.iscoutb.dev/docs ; https://taia-backend-latest.onrender.com/health. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#taia_-task-artificial-intelligence-assistant) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Desde el corte previo se actualizaron Dockerfile y documentación de Dokploy, conservando la URL institucional de la API. Se mantiene la confirmación docente de presentación y despliegue funcionando. No hay run de CI/CD para la punta nueva entre los runs consultados: los últimos exitosos corresponden al 20 de octubre, no al commit actual. El filtro paths agregado al workflow se interpreta como una cadena, no como lista YAML, por falta de espacio tras los guiones; además las rutas de workflow deben apuntar a su ubicación real. Esto requiere corregir el disparador y obtener evidencia nueva, sin concluir que el sitio esté caído.

Presentación y despliegue funcionando confirmados por el docente.

**Próximos pasos:**
- Corregir paths en CI y verificar un run sobre la punta actual, distinguiendo validación del repositorio y funcionamiento del despliegue.
- Completar tabla de garantías y dos operaciones contrastadas: límites transaccionales de confirmar/notificar frente a crear tarea y enviar Telegram.
- Justificar caché/no caché, comparar costo de reversión en ADR y alinear PostgreSQL en C4 y consistencia/caché en arc42 §8.

**Issues:** 3 abiertas y 4 cerradas; 2 abiertas sin responsable. Cierres: 4 completed. El estado registrado no acredita por sí solo implementación.

**README:** Institucional. API institucional; Flutter sigue descrito como arquitectura objetivo. Presentación y funcionamiento confirmados por el docente. URL documentada: https://taia-sistema.iscoutb.dev ; https://taia-sistema.iscoutb.dev/health ; https://taia-sistema.iscoutb.dev/docs ; https://taia-backend-latest.onrender.com/health. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#taia_-task-artificial-intelligence-assistant) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin cambios de punta, README, issues o PR relevantes desde el corte anterior. La API institucional permanece documentada y se conserva la confirmación docente de presentación y funcionamiento. No aparece un run para la punta actual: los últimos CI/CD exitosos son de otra revisión. El workflow mantiene paths sin espacio tras los guiones y rutas que requieren alineación, por lo que no se da por corregido el disparador ni se infiere caída del servicio.

**Próximos pasos:**
- Corregir paths en CI y verificar un run sobre la punta actual.
- Completar garantías por operación y pruebas de confirmar/notificar frente a crear tarea y Telegram.
- Justificar caché/no caché y costo de reversión; mantener PostgreSQL, C4 y arc42 alineados.

**Issues GitHub:** 3 abiertas y 4 cerradas; 2 abiertas sin asignar. Cierres: 4 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. API institucional; Render como respaldo. Flutter es arquitectura objetivo, no frontend web verificado. Presentación y funcionamiento confirmados por docente.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#taia_-task-artificial-intelligence-assistant) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).


## Seguimiento actual · 26 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Corrige el disparador YAML de CI, construye y arranca la imagen contra PostgreSQL de prueba, incorpora comprobación del Quality Gate para el commit y alinea despliegue/C4 con Dokploy mediante ADR-0010. Retira Terraform histórico y añade consistencia y decisión de no cachear lecturas. CI/CD exitosos consultados corresponden a la revisión citada, no a la punta documental posterior; el CD acredita solicitud por webhook, no finalización ni salud del despliegue. Se conserva funcionamiento y presentación confirmados por el docente.

**Próximos pasos:**
- Verificar en Dokploy la revisión efectivamente desplegada y su salud; el webhook exitoso no lo acredita por sí solo.
- Reconciliar README y ADR sobre respaldo Render/TLS, y mantener la distinción entre API entregada y Flutter objetivo.

**Issues GitHub:** 3 abiertas y 4 cerradas; 2 abiertas sin asignar. Cierres: 4 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. API institucional; README también enlaza Render como alternativa histórica, sin confirmar respaldo activo. Flutter sigue arquitectura objetivo. Funcionamiento confirmado por docente; webhook CD no acredita fin del despliegue.

[Fuentes y alcance](../seguimiento-s12-2026-10-26.md#taia_-task-artificial-intelligence-assistant) · [Issues](../seguimiento-issues-2026-10-26.md) · [URL y dominio](../seguimiento-despliegues-2026-10-26.md).


## Seguimiento actual · 31 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Frente al 30/oct, 26 commits y la PR de frontend fusionada incorporan un cliente Flutter inicial de splash/bienvenida, webhook Telegram protegido, límites de login y mensajes al asistente, métricas con JWT, separación de instrucciones/texto del usuario, auditoría de dependencias y respaldo Gemini→Groq. El CI del padre inmediato de la punta documental acredita 283 pruebas backend, build/smoke, ambos locks sin vulnerabilidades conocidas y Quality Gate OK; no ejecuta las pruebas Flutter. El CD solicita el webhook de Dokploy, sin acreditar por sí solo finalización. README sigue intacto y ADR-0011 aún dice implementación pendiente pese al código y pruebas del respaldo. La activación y comprobaciones de producción son reportes del equipo; no se repitieron. Se conserva que TAIA presentó y funciona, confirmado por el docente. Siguen pendientes consentimiento, renovación/revocación y alertas; el respaldo incorpora riesgo de latencia y no convierte el inicio Flutter en app funcional completa.

**Próximos pasos:**
- Actualizar README y ADR-0011 con el alcance real del cliente inicial, webhook, autenticación de métricas y respaldo implementado; conciliar su estado con las pruebas y reportes del equipo, sin borrar el histórico.
- Agregar ejecución verificable de pruebas/análisis Flutter al pipeline y validar en dispositivo los flujos funcionales cuando existan; tres pruebas de splash no acreditan una app académica integrada.
- Cerrar el consentimiento documentado en RF-USR-10, renovación/revocación y alertas con código y evidencia; mantener explícitos los riesgos aceptados y sus disparadores de revisión.
- Vincular la revisión efectivamente servida por Dokploy con evidencia de salud y recorrido; medir latencia del respaldo, conservar la limitación de la evaluación con árbol modificado y distinguir comprobación del equipo de aceptación independiente.

**Issues GitHub:** 3 abiertas y 4 cerradas; 2 abiertas sin asignar. Cierres: 4 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. API institucional. README conserva Render como alternativa y la descripción antigua de Flutter; ahora hay splash/bienvenida en código, no evidencia de app integrada ni de frontend público. El equipo documenta TLS y activación del respaldo; el webhook CD solo acredita solicitud. Presentación y funcionamiento confirmados por el docente, sin nueva prueba viva propia.

[Fuentes y alcance](../seguimiento-s12-2026-10-31.md#taia_-task-artificial-intelligence-assistant) · [Issues](../seguimiento-issues-2026-10-31.md) · [URL y dominio](../seguimiento-despliegues-2026-10-31.md).
