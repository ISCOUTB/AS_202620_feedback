# Retroalimentación publicable · AudioShare

## Semana 1

- Está bien: el repositorio existe, es público y el problema de AudioShare (audio en tiempo real por Wi-Fi) está descrito con un prototipo claro; `docs/ia.md` arrancó con contenido real.
- Falta: la ficha del problema no dice quiénes son los usuarios ni cuáles son las dos tensiones de calidad.
- Corregir antes del corte 1: montar la estructura completa (`docs/arc42/` con plantilla, `docs/adr/`, `docs/c4/`), poner `docs/aspectos.md` como la tabla de 8 columnas del curso y asegurar que las cuatro personas tengan acceso y firmen commits.

## Semana 2

- Está bien: 4 escenarios de calidad con medidas numéricas con unidad, un árbol de utilidad con prioridades y escenarios enlazados desde el aspecto, C4 de contexto como código Mermaid, restricciones separadas de los requisitos y `docs/ia.md` actualizado.
- Falta: cada escenario debe declarar fuente, artefacto y entorno (hoy solo tienen estímulo, respuesta y medida); las restricciones deben clasificarse (técnica, organizativa, legal) y una de ellas es en realidad un requisito funcional; los objetivos de la sección 1 deben decir a quién le importan.
- Corregir antes del corte 1: alinear el C4 con la sección 3 (misma red Wi-Fi, mismo moderador), añadir leyenda al diagrama, y empezar a registrar en `docs/ia.md` qué se rechazó de la IA y por qué.

## Semana 3

Qué está bien: el ADR 0001 está completo (contexto, alternativas con motivo, decisión y consecuencias), el README documenta el arranque con un solo comando y el esqueleto monolito modular con paquetes por frontera coincide con lo decidido.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 quedó desincronizada: aún declara «pendiente» la selección del estilo que el ADR ya decidió; actualícenla y nombren tácticas concretas contra EC-01…EC-04.
2. Rehagan la matriz comparativa contra el árbol de utilidad: una fila por escenario (EC-01…EC-04) que diga qué mejora y qué empeora con cada estilo.
3. Hagan alcanzable el ADR: enlácenlo desde `docs/aspectos.md` (además, con la tabla de 8 columnas) y desde el escenario que lo motiva; reemplacen el «EC-nn» del ADR por el escenario real.
4. Registren en `docs/ia.md` qué se rechazó y por qué en cada uso (arrastrado desde S2).

## Semana 4 · S4

La documentación arc42 y los diagramas C4 están avanzados, pero el corte vertical no atraviesa persistencia y el C4 nivel 2 dibuja contenedores que aún no existen en el código. La sección 9 debe enlazar los ADR reales en docs/adr/ en lugar de repetirlos o crear ADR sin archivo. Completen la fila de aspectos con las columnas Requisito y C4, y citen la prueba del recorrido (tests/a01.test.ts) en la celda de Pruebas. El README debería declarar un único comando de arranque. Configuren integración continua y dejen evidencia del run en verde. Revisen que el ADR-0001 refleje el estado actual o creen uno nuevo si la decisión cambió.

## Semana 5 · CORTE1

El proyecto está sólido: repositorio correcto, documentación arc42/C4/ADR presente, corte vertical A-01 implementado y CI en verde. El pendiente principal es crear correcciones.md en la raíz del estado calificado, con una fila por hallazgo de S1-S4, indicando acción, evidencia y estado. Revisen también la consistencia del nombre de un integrante entre la declaración y el historial de git. Completen las secciones arc42 faltantes si la ficha S4 las exige. El PDF y la sustentación se verifican en el aula.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Ya existe la etiqueta `corte-1` y apunta a un commit anterior al cierre: eso quedó resuelto. Pero, revisando el repositorio completo hasta esa etiqueta, no encontramos ninguna señal de que el equipo haya recibido o trabajado la restricción nueva que pedía este corte: no hay un ADR nuevo, no hay una cifra de línea base medida, no hay una prueba nueva, y el pipeline de integración continua corre en verde pero sobre el mismo contenido de siempre, no sobre un cambio del reto. Lo que sí se hizo en esta semana fue terminar de integrar el corte vertical (que en rigor pertenece a la semana anterior), ajustar diagramas C4 y hacer limpieza de README y de la versión de Node en el CI.

Qué falta para la sustentación: quién puede explicar cuál fue la restricción asignada, qué se midió antes del cambio, qué decisión se tomó y con qué alternativas se comparó, y qué prueba demuestra que el cambio funciona — porque ninguna de esas cuatro cosas aparece hoy en el repositorio. Además, sigue pendiente conciliar el C4 de contenedores (describe cuatro contenedores) con la implementación real (un monolito de un solo proceso), y agregar en `docs/ia.md` una entrada propia de esta semana.

## Semana 7 · S7

El contrato OpenAPI/AsyncAPI con rutas y esquemas, la prueba de contrato, su ejecución en el pipeline y el ADR de integración están versionados, y la justificación de la estrategia híbrida frente a EC-01, EC-03 y EC-04 es sólida. Para que la prueba de contrato demuestre algo, falta la evidencia de que falla con un cambio incompatible: un run en rojo en el pipeline o el registro del cambio que la hizo fallar. Sigue pendiente la URL pública del análisis de SonarCloud con su Quality Gate, junto con la columna de evidencia en la tabla de aspectos y la limpieza de los marcadores de conflicto de fusión y de los enlaces a un ADR que no existe. Conviene que los diagramas C4 y arc42 usen los mismos nombres de módulo que el código y que todas las flechas del nivel 2 indiquen protocolo y formato.
## Semana 6 · S6

Buen avance: el mapa de contextos, la tabla módulo a datos y el plan de corrección ya están en el repositorio, y la trazabilidad de A-01 enlaza ADR, C4, código y pruebas. Para cerrar el corte: tipifiquen cada relación del mapa con el vocabulario de la semana (núcleo compartido, cliente-proveedor, capa anticorrupción), no solo flechas. Registren el recorrido de la auditoría de propiedad (comandos, hash y rutas) y declaren como no conformidad la escritura de startAt y del estado de reproducción desde la persistencia de Session. Falta incorporar la sección 8 de arc42: el lenguaje ubicuo y el mapa existen, pero en documentos sueltos y con un include roto. Si los límites cambiaron desde el primer corte, suban el C4 nivel 3 y el ADR del reajuste. Completen la evidencia pública de SonarCloud (workflow, run y URL con Quality Gate) y las pruebas de EC-02 y EC-03.

## Semana 8 · S8 (revisión definitiva)

La entrega de despliegue llegó y es la más completa del corte: infraestructura versionada (Dockerfile, compose y el workflow que publica la imagen), procedimiento de recreación enlazado desde el README, logs JSON con campos, una métrica ligada a los escenarios de sincronización, secretos tomados del almacén, estimación de costo con supuestos propios y punto de ruptura, la vista de despliegue con una caja por pieza y las restricciones de costo y tarjeta, y un ADR de plataforma con la alternativa descartada y la capa gratuita verificada.

Para cerrar del todo:
1. Pongan en verde el workflow de Flutter sobre la rama principal: es el único pipeline que falla en el último push.
2. Publiquen la URL pública del análisis estático con el estado del Quality Gate y alineen la organización del proyecto con la del curso.
3. Actualicen `docs/ia.md` con el uso de IA de esta semana.
4. Un ADR aceptado no se edita: cuando la decisión cambie, escriban un ADR nuevo que lo reemplace y marquen el anterior como reemplazado.

La URL del despliegue se entrega por Moodle y no se califica en esta pasada.

## Semana 9 · S9 (revisión definitiva)

Hay dos decisiones nuevas y una URL accesible. La prueba de sincronización calcula números fijos sin llamar al sistema, así que todavía no demuestra el comportamiento del producto. Conecten la cadena del aspecto con el ADR nuevo, código real, prueba que falle ante el defecto y medición. Precisen la auditoría y las propuestas de IA rechazadas.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El protocolo de sincronización incorpora medición y mutación, pero la comparación mezcla relojes. Flutter aún no integra /time ni ACK, y la arquitectura conserva desalineaciones.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

C4 y despliegue rezagados; Session aún escribe el estado asignado a Sync.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · C4 omite Flutter y conserva solo la vista del cliente web legado:** La vista incompleta de las alternativas de cliente no permite distinguir el fallback public/ del cliente Flutter preferido por el bootstrap ni qué alternativa consume actualmente NDJSON. **Acción:** Actualizar L2 con Flutter y web legado como alternativas; marcar NDJSON, /time y ACK como pendientes de integrar en Flutter. No presentar ADR-0007 propuesto como decisión ya aceptada. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · Session sigue escribiendo el estado que el diseño asigna a Sync:** La evolución del estado de sincronización exige modificar también el modelo y persistencia de Session; existen dos representaciones acopladas. **Acción:** Cerrar NC-10: hacer a Sync dueño del estado persistido y publicar una interfaz que Session consulte, o registrar formalmente un modelo compartido deliberado con responsabilidades y pruebas. La no conformidad ya estaba reconocida; no se presenta como descubrimiento nuevo. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Baja · La plataforma principal de arc42/ADR no coincide con la guía operativa vigente:** Una persona que siga arc42 puede preparar Azure cuando README guía a Dokploy. **Acción:** Registrar Dokploy como entorno principal actual, conservar Azure como alternativa si sigue vigente y enlazar la decisión de transición sin reescribir la historia. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Antes del corte, identifiquen el escenario operativo asignado y midan una línea base reproducible. El health check responde, pero falta demostrar el flujo principal, corregir el pipeline Flutter y alinear la documentación con Dokploy. La sustentación y los niveles dependientes del reto quedan pendientes.

</details>

## Semana 11 · Integración y resiliencia

El análisis de fallos, diseño de idempotencia y decisión de no extraer satisfacen la ficha, distinguiendo correctamente implementación y pendientes con plan. Falta incorporar los modos de fallo en la sección 11 de arc42. Los cambios posteriores al cierre quedan únicamente en overall y no modifican esta revisión histórica.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

La vista de contenedores y la caché HTTP de la pista aportan evidencia inicial. Falta explicitar garantías por operación, contrastar dos operaciones, definir invalidación y entrega de eventos, y justificar la decisión de datos más costosa de revertir. Actualizar arc42 y la documentación de audio para que reflejen el comportamiento actual.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **2 abiertas, 2 cerradas, 4 en total**. Los 2 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Institucional**. Cliente legado; no acredita Flutter web. Dirección(es) documentada(s): https://audioshare.iscoutb.dev.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Sin commits nuevos desde 20 de octubre. Audio de pista y pausa/reanudación ya constaban en punta 19 de octubre. README reconoce que la imagen sirve cliente legado, no Flutter Web.

**Próximos pasos:**
- Tabla crear sala/PLAY/pausa → garantía, separando transacción SQLite y publicación NDJSON; declarar comportamiento si falla entre ambos.
- Definir invalidación o URL versionada de /track (max-age=3600), y actualizar arc42 §8 que aún describe MockAudioService.
- ADR de decisión de datos más costosa de revertir con comparación y garantías de entrega/reconexión de eventos.

**Issues:** 2 abiertas y 2 cerradas; 2 abiertas sin responsable. Cierres: 2 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Institucional. URL institucional del cliente legado; no acredita despliegue de Flutter web. URL documentada: https://audioshare.iscoutb.dev. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#audioshare) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

La rama principal y el README no cambian respecto al seguimiento del 22 de octubre. Se mantienen la pista compartida y los controles de pausa/reanudación, con CI, Flutter y publicación de imagen exitosos para esa misma punta. La URL institucional sigue sirviendo el cliente legado según el README; no atribuirle automáticamente el build Flutter web.

**Próximos pasos:**
- Tabla crear sala/PLAY/pausa → garantía, separando transacción SQLite y publicación NDJSON; declarar comportamiento si falla entre ambos.
- Definir invalidación o URL versionada de /track (max-age=3600), y actualizar arc42 §8 que aún describe MockAudioService.
- ADR de decisión de datos más costosa de revertir con comparación y garantías de entrega/reconexión de eventos.

**Issues:** 2 abiertas y 2 cerradas; 2 abiertas sin responsable. Cierres: 2 completed. El estado registrado no acredita por sí solo implementación.

**README:** Institucional. Endpoint institucional; la imagen publicada sirve cliente legado, no Flutter web. URL documentada: https://audioshare.iscoutb.dev. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#audioshare) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).
