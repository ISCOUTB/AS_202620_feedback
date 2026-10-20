# Retroalimentación publicable · LostVault

## Semanas 1 y 2

## Evidencia S1

Buen punto de partida: el repositorio está en la organización, es público y tiene la ficha del problema con usuarios, alcance y propuesta clara, además de un registro de IA con contenido real. Les faltó la estructura de documentación que pide la semana (carpetas `docs/arc42/` con la plantilla, `docs/adr/` y `docs/c4/`), y la ficha no declara las dos tensiones de calidad enfrentadas: declaran disponibilidad como atributo prioritario, pero no un segundo atributo en tensión con él. La tabla de `docs/aspectos.md` debe tener las ocho columnas del curso con una fila iniciada, no solo texto narrativo.

## Evidencia S2

Las secciones 1, 2 y 3 de arc42 están redactadas con sustancia: objetivos de negocio, restricciones clasificadas y justificadas, y contexto con actores. Los cuatro escenarios tienen sus seis partes y medidas numéricas con cifra, unidad y condición de carga: muy bien. Para corregir antes del corte 1: (1) el árbol de utilidad ordena los atributos pero no los valora por impacto y riesgo; (2) el C4 de contexto solo existe como imagen — súbanlo como código y a `docs/c4/` para que sea revisable; (3) actualicen `docs/ia.md` con el uso de IA de esta semana e incluyan qué rechazaron y por qué; (4) repartan el historial: todo el trabajo aparece firmado por una sola cuenta.

## Semana 3

Qué está bien: ADR 0001 aceptado con alternativas descartadas con motivo, y README reescrito como guía del esqueleto con comando único y prueba inicial.

Qué corregir antes del corte 1 (semana 5):
1. Reescriban la sección 4 y la matriz comparativa ligándolas a sus escenarios 1-4, fila por escenario del árbol de utilidad (hoy describen los estilos en abstracto).
2. Enlacen el ADR 0001 desde `docs/aspectos.md` y desde los escenarios que lo motivan.
3. Creen los paquetes que declara el ADR (`lib/core` y `lib/features/…` con `.gitkeep`): hoy solo existe `lib/main.dart`, y borren los archivos residuales `front_end` y `ejecutable` de la raíz.
4. Actualicen `docs/ia.md` (última entrada del 08-ago) con los usos de S3 y lo rechazado con motivo; muevan el C4 a `docs/c4/`.
5. Evidencien la prueba en verde (pipeline o run) antes del corte 1.

## Semana 4 · S4

Entrega sólida de la semana 4: arc42 1-6, 9, 10 y glosario redactados con contenido propio, corte vertical AS-03 que atraviesa UI, lógica y persistencia, y fila de aspectos completa con pruebas en verde en CI. Para el primer corte, conviertan el C4 nivel 2 a código (puml, mmd o Structurizr) para que sea trazable y revisable, y añadan la integración con SonarCloud al pipeline según el contrato. Ejecuten y verifiquen el arranque con flutter run -d chrome para dejar evidencia de que el comando funciona. Los demás aspectos (AS-01, AS-02, AS-04) quedan pendientes de cortes ejecutables, como indica la propia tabla.

## Semana 5 · CORTE1

El corte vertical AS-03 está bien implementado y documentado, con pruebas y pipeline en verde. La documentación arc42, el ADR y el registro de IA son sólidos. Para cerrar el corte, falta crear correcciones.md en la raíz con el formato exigido (hallazgo, acción, evidencia, estado) y completar la trazabilidad de docs/aspectos.md incluyendo el eslabón C4. También conviene limpiar archivos residuales como lib/search/domain/entities/lost_object.dart y documentar o eliminar las carpetas ejecutable y front_end. El resto de la línea base cumple.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre y no hay cambios: el repositorio quedó exactamente igual a como estaba el 3 de septiembre, cuando se hizo la revisión preliminar. No hubo ningún commit nuevo entre esa fecha y el cierre del corte.

Esto significa que sigue faltando todo lo que se pidió para el reto: identificar la restricción, medir cómo estaba el sistema antes, escribir un ADR con la decisión, hacer el cambio de código y medir el resultado. La línea base (corte vertical de seguridad, AS-03) sigue firme y probada, pero eso ya se evaluó en semanas anteriores.

De paso, noten que un documento propio del equipo (`REVISION_CORREGIDA.md`, escrito en agosto) dice que ya habían eliminado unas carpetas residuales (`front_end`, `ejecutable`), pero esas carpetas todavía están en el repositorio.

Antes de la sustentación, sería importante que el equipo pueda mostrar avance real sobre el reto, aunque sea parcial, y explicar qué pasó durante estos días adicionales.

## Semana 7 · S7

El contrato OpenAPI 3.1.1, la prueba de consumidor y el ADR de integración síncrona son un avance sólido y están bien enlazados con el corte vertical. Para cerrar la brecha: (1) documenten la correspondencia real entre cada ruta del contrato y el código, o declaren con precisión que la frontera HTTP aún no existe; (2) aporten la ejecución que muestre la prueba en rojo al romper el contrato, por ejemplo un PR con cambio incompatible y su run fallido; (3) publiquen la URL del análisis en SonarCloud con el estado del Quality Gate y revisen el run de Build que falla; (4) guarden el C4 nivel 2 como código para que el etiquetado de protocolo y formato sea revisable; (5) agreguen la columna C4 en la tabla de aspectos y actualicen la lista de ADR en la sección 9 de arc42.
## Semana 6 · S6

El mapa de contextos y la auditoría sobre el código son el punto fuerte de la entrega: tipifican las relaciones, reconocen el núcleo compartido y convierten hallazgos reales en no conformidades con acción de corrección. Para cerrar la semana falta la sección 8 de arc42 con el lenguaje ubicuo y el mapa incorporado, y la evidencia de SonarCloud (URL pública del análisis y estado del Quality Gate). Si los límites cambiaron respecto al primer corte, agreguen el C4 nivel 3 y el ADR del reajuste. Alineen la tabla de aspectos con las columnas del contrato (falta Requisito y C4) y eviten celdas pendientes en las filas que ya defienden. Mantengan cada no conformidad con su ubicación y su corrección, y verifiquen su cierre en el código, no solo en el documento.

## Semana 8 · S8 (revisión definitiva)

La entrega cambió por completo frente a la revisión preliminar: la API quedó desplegada en Vercel con URL pública documentada, se versionaron Dockerfile, Compose y Terraform, y la vista de despliegue de arc42 describe una pieza por fila con su ubicación real. La observabilidad está resuelta con logs JSON por request (con identificador de petición y duración) y un endpoint de métricas p95 ligado al escenario de rendimiento. La estimación de costos parte de supuestos de volumen propios, verifica la capa gratuita y declara el punto de cruce. Hay un ADR de plataforma con las alternativas descartadas y la capa gratuita comprobada. El pipeline del estado calificado está en verde, incluido el paso de Quality Gate.

Tres correcciones:
1. Hay un ADR con numeración fuera de la convención (termina en `.3`): renómbrenlo al formato `NNNN-titulo-en-kebab-case.md`.
2. Se editaron ADR ya aceptados sin declarar un reemplazo. Un ADR aceptado no se reescribe: si la decisión cambia, se escribe otro y el anterior se marca como reemplazado.
3. Falta publicar la URL del análisis en SonarCloud con el estado del Quality Gate; además, la vista de despliegue y el Terraform citan un archivo de configuración de Vercel que no está en el repositorio.

La métrica p95 no acumula en producción por el estado en memoria de la función serverless, y está bien que lo hayan documentado. Cierren el enlace público del Quality Gate y la disciplina de ADR.

## Semana 9 · S9 (revisión definitiva)

La entrega ya incorpora métricas, prueba nueva, auditoría y una medición real del despliegue. Completen el ADR y la cadena de esa porción, muestren la prueba ante un defecto concreto y registren un rechazo técnico de la IA. NC6 sigue siendo una corrección propuesta, no implementada. La comprobación independiente de credenciales quedó pendiente por una limitación del revisor, sin atribuirla al equipo.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Se comparan cargas en Vercel y un proxy local, sin un antes y después equivalente. Con 200 conexiones se reconocen fallos; el p95 en memoria no se acumula entre invocaciones. El código y la arquitectura documentada divergen.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Handler Python cruza límites modulares; README anterior al proveedor.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · La reclamación HTTP evita los límites de aplicación y propiedad del monolito modular:** El handler create_claim mezcla HTTP, autenticación, regla de disponibilidad, verificación y escritura directa de _claims/_objects. A diferencia del flujo Dart por interfaces, el backend carece de un dueño encapsulado de Objects que reciba la transición; cambios de persistencia y reglas afectan la frontera HTTP. Es una deuda ya reconocida como NC6, todavía presente en el SHA. **Acción:** Extraer caso de uso Python y servicio/repositorio dueño de objetos; el router traduce HTTP, Claims solicita reserva al contrato de Objects y la atomicidad permanece en una unidad de trabajo. Probar la ruta HTTP y los límites de imports, no solo la estructura Dart. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Baja · README aún describe como futuro un proveedor HTTP que ya tiene implementación:** El lector del README recibe una arquitectura anterior: contrato previo a implementar el proveedor, mientras ADR0003 y backend/main.py ya definen API separada. Puede confundirse el demo Flutter en memoria con un flujo móvil conectado a esa API. **Acción:** Actualizar README y vistas con dos rutas actuales: demo Flutter local y proveedor FastAPI; señalar explícitamente que el cliente aún no lo consume. Separar diagrama implementado de integración futura y corregir la referencia obsoleta a vercel.json. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

La sonda de salud responde, pero el experimento documenta fallos importantes con 200 conexiones: el p95 de respuestas exitosas no demuestra disponibilidad. Identifiquen el reto asignado, resuelvan persistencia y agregación de métricas entre instancias y documenten qué decisión cambia a la luz de los fallos medidos.

</details>

## Semana 9 · Aclaración de la revisión

La comprobación de credenciales bloqueada por el entorno del revisor queda excluida del cálculo por decisión docente. Sigue sin verificarse y no implica un hallazgo de filtración. Los demás criterios conservan su valoración sobre la entrega de cierre; véase la [matriz actualizada](semana-09-evidencia-s9.md).

## Semana 11 · Integración y resiliencia

El backend tiene deduplicación y exclusión mutua locales, y el diseño reconoce sus límites frente a reinicio o varias instancias. Actualicen aspectos para enlazar los fallos, la decisión de extracción y sus pruebas. La propagación de la clave desde Flutter sigue pendiente y no debe presentarse como completada.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Faltan tabla de garantías, contraste de operaciones, caché e invalidación y decisión de datos con costo de reversión. El C4 necesita identificar la tecnología y distinguir el almacenamiento RAM vigente de la base de datos prevista. Incorporen esas decisiones a la sección de conceptos de arc42.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 1 cerradas, 1 en total**. Los 1 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. No publica dirección HTTP/HTTPS de despliegue.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.
