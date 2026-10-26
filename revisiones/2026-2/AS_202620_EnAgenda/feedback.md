# Retroalimentación publicable · EnAgenda

## Semana 1 · Equipo, problema y repositorio

El montaje quedó muy bien: ficha del problema con usuarios, alcance y tres tensiones de calidad bien enfrentadas, la tabla de aspectos iniciada y un registro de IA con entradas reales, incluido lo que rechazaron y por qué. La plantilla arc42 está en Markdown y los directorios `adr/` y `c4/` existen.

Dos correcciones menores: varios archivos tienen un espacio antes de la extensión (por ejemplo `aspectos .md`, `ia .md`, el ADR `0001-… .md`); renómbrenlos a la convención para que las herramientas de revisión los encuentren. Y conviene confirmar que los tres integrantes tienen acceso al repositorio, porque el historial de la semana solo muestra a dos.

## Semana 2 · S2

La semana 2 tiene un buen avance en escenarios de calidad: cinco escenarios completos con medida numérica. Para cerrar las brechas: creen docs/arc42/01* con objetivos de negocio e interesados, clasifiquen las restricciones en técnicas, organizativas y legales, y agreguen riesgo al árbol de utilidad. La tabla de aspectos aún no traza nada: cada fila debe enlazar a su escenario. También noten que los commits posteriores al cierre sugieren que muchas correcciones se subieron tarde; procuren dejar la entrega cerrada antes de la fecha límite.
## Semana 3

Qué está bien: la sección 4 ya elige el monolito modular con límites y consecuencias, el ADR es una decisión de estilo aceptada con alternativas motivadas y `aspectos.md` ya usa la tabla de 8 columnas.

Qué corregir antes del corte 1 (semana 5):
1. El esqueleto prometido no existe: creen `src/` con los módulos del ADR (eventos, invitaciones, tareas, agenda, presupuesto, panel, compartido) y retiren los scripts sueltos de `docs/` (`main.py` importa un módulo inexistente).
2. Documenten en el README el comando único de arranque y agreguen una prueba en verde: el ADR promete `tests/` y hoy no hay ninguna.
3. Renombren el ADR a algo como `0001-usar-monolito-modular.md`: el nombre actual tiene espacio, no pasa el filtro y ya no corresponde a lo que decide; arreglen los enlaces internos rotos.
4. La matriz comparativa no referencia los escenarios EC-01…EC-05: pongan una fila por escenario del árbol de utilidad.
5. Hagan alcanzable el ADR: la columna ADR de `aspectos.md` sigue «Pendiente» y `10-requisitos-de-calidad .md` no lo enlaza.
6. Repartan la contribución: en S3 faltó un integrante en el historial (2 de 3).

## Semana 4 · S4

La entrega de la semana 4 está sólida en documentación arc42, glosario, C4 niveles 1 y 2, corte vertical y pruebas en CI. Para el primer corte, revisen la coherencia entre el C4 nivel 2 y el código real: el diagrama muestra API/Backend y Base de Datos, pero la implementación es un monolito Flask con repositorio en memoria; ajusten el diagrama o el código. Completen la celda C4 de docs/aspectos.md con rutas navegables a los diagramas. Agreguen SonarCloud al pipeline como exige el contrato. Eviten versionar archivos .pyc. Finalmente, verifiquen que las secciones 1, 4, 5 y 6 de arc42 estén completamente redactadas y sin texto de plantilla.

## Semana 5 · Primer corte

El proyecto cumple con la línea base arquitectónica del primer corte. La documentación arc42, el ADR y los diagramas C4 están alineados con la implementación real. El corte vertical de invitaciones es reproducible y las pruebas pasan en CI. Se recomienda eliminar los archivos __pycache__ del repositorio y añadir análisis estático con SonarCloud para futuras entregas. Mantener la trazabilidad en aspectos.md es un buen hábito. Sigan así.

### Rectificación del 14 de octubre de 2026

El documento de correcciones está en `docs/correcciones.md`, dentro de `docs/`, y no en la raíz como decía el informe. Se corrige la descripción. La evaluación definitiva del primer corte es el compendio de las entregas iniciales; la exigencia anterior de resolver un reto nuevo no queda como pendiente de esa evaluación.

<details>
<summary>Comentario del 7 de septiembre, superado por la evaluación definitiva y esta rectificación</summary>

Se conserva como historial. Las exigencias de un reto nuevo y los pendientes descritos aquí no sustituyen la evaluación definitiva del primer corte.

### Comentario histórico · 7 de septiembre de 2026

Ya crearon la etiqueta `corte-1` sobre un commit anterior al cierre, y eso está bien: quedó un estado identificable para calificar.

Lo que falta: el trabajo de la última noche antes del cierre se dedicó a corregir observaciones de la semana 4 (arreglar el diagrama C4 para que coincida con la aplicación Flask, y enlazar la fila de aspectos), y ustedes mismos lo dejan escrito con honestidad en su documento de correcciones: no llegaron a plantear ni resolver el reto propio del primer corte. Falta identificar la restricción nueva asignada, medir cómo estaba el sistema antes de tocarlo, escribir la decisión en un ADR nuevo, hacer el cambio sobre el corte vertical existente y medir el resultado contra un umbral.

Dos cosas puntuales para corregir ya: el enlace de "Evidencia" en la fila de aspectos apunta a un archivo que no existe en el repositorio (el archivo real tiene otro nombre); y el registro de uso de IA no tiene ninguna entrada de esta semana, ni de las correcciones que sí hicieron el 6 de septiembre.

Para la sustentación: lleven claro qué restricción les tocó, qué medida inicial tomaron y con qué procedimiento, y qué cambio de código (no solo de documentación) responde a esa restricción.

</details>

## Semana 6 · S6

El mapa de contextos y la tabla de propiedad de datos están bien elaborados y contrastados con el código del cierre. La verificación de violaciones está documentada y el plan de corrección es claro. La revisión de la apelación confirmó que la base del primer corte sí estaba identificada: el C4 de componentes completa la representación sin cambiar los límites implementados, por lo que no se activaba la condición de un ADR nuevo. Las observaciones tempranas sobre C4 vacío, arc42 sección 8 vacía y mapa o tabla ausentes quedan superadas. Pendientes: integrar SonarCloud al pipeline y evitar versionar archivos __pycache__. A medida que se implementen más contextos, conviene ampliar la tabla de aspectos para mantener la trazabilidad completa.

## Semana 7 · S7

El contrato OpenAPI está versionado, incluye rutas y esquemas, y la vista de ejecución describe el flujo implementado. La apelación corrige la observación sobre las rutas HTML: están fuera de la API JSON y su ausencia en OpenAPI no invalida la correspondencia de las operaciones contratadas. Permanece una salvedad de fecha y hora: el esquema exige `date-time` y la serialización no declara zona horaria. La prueba actual comprueba respuestas funcionales, pero no valida la especificación. Alineen el formato temporal, incorporen una prueba contractual explícita al pipeline y conserven la evidencia de que falla ante un cambio incompatible. El ADR de integración y el ajuste del C4 llegaron después del cierre. Falta también SonarCloud con su run y Quality Gate públicos.

## Semana 8 · S8

Está bien: se añadió un ADR de plataforma con su alternativa descartada y la capa gratuita verificada; la vista de despliegue identifica cada pieza y dónde se ejecuta; la restricción de costo cero y sin cuentas de pago quedó recogida en arc42; existen rutas de salud y de métricas; y el entorno local se reproduce desde el README.

Qué corregir, por prioridad: el commit revisado es un merge con conflictos sin resolver en varios archivos de infraestructura (Dockerfile, compose, blueprint de despliegue, ejemplo de variables y evidencia), lo que deja la infraestructura como código inválida y el pipeline en rojo; resuelvan los conflictos y vuelvan a dejar el CI en verde. Tampoco hay logs estructurados, aunque la documentación afirma que sí; la métrica expuesta no se ata a un escenario de calidad real, porque cita un escenario que no existe en arc42; y la estimación de costo deja sin completar los supuestos de volumen. Sigue pendiente SonarCloud con su URL y el estado del Quality Gate.

La URL del despliegue y la comprobación de salud quedan diferidas por decisión docente: se entregan por Moodle.

## Semana 9 · S9 (revisión definitiva)

La creación múltiple de invitaciones es trabajo nuevo y el registro de IA explica decisiones y rechazos. La apelación permitió consolidar las firmas de autor del historial y verificar la contribución de todos los integrantes; esta corrección transversal no modifica la evaluación de la ficha. Falta completar la cadena con ADR coherente, prueba que demuestre el defecto, medición y auditoría de erosión. La plantilla intermedia faltaba al cierre y llegó después. Revisen además la exposición de tokens en las rutas publicadas por métricas.

## Semana 10 · Segundo corte

### Rectificación vigente · 14 de octubre de 2026

Se reconoce la decisión e implementación del despliegue, incluida la comparación de una alternativa viable. La protección y normalización de métricas y la prueba de no filtración están presentes; el CI citado pasa. arc42 sí fija un objetivo de latencia, pero el documento operativo no lo concreta en una línea base y un resultado reproducible del despliegue. Siguen pendientes logs estructurados, instrumentación de latencia y reconciliar los documentos históricos con Flask/REST y la autorización de métricas.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial; la evaluación de la ficha anterior permanece congelada y su autoría se rectifica de forma transversal.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

ADR de stack y guía de métricas desactualizados.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · ADR1 conserva Next.js/Server Actions y prohibición de API mientras el sistema vigente es Flask con REST:** Las decisiones vigentes parecen contradictorias sobre cliente, entrada HTTP y contrato, dificultando futuras modificaciones. **Acción:** Registrar aclaración/supersesión parcial de ADR1: mantener monolito modular, sustituir Next.js/Server Actions y actualizar exposición REST. No cambiar la implementación solo para seguir una decisión histórica. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Baja · El procedimiento operativo aún espera /metrics 200 sin explicar el token:** Un operador siguiendo README/arc42 interpreta 401/503 esperado como fallo del servicio o no configura el secreto requerido. **Acción:** Actualizar smoke check para configurar ENAGENDA_METRICS_TOKEN, enviar Bearer de forma segura y distinguir 401/503 de liveness /health. No desproteger métricas para satisfacer el ejemplo antiguo. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación y la rectificación del 14 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

La plantilla faltante ya está en la punta y CI está en verde. Siguen pendientes URL pública, umbral y medición del escenario asignado. Normalicen las rutas de métricas para no divulgar tokens de invitación, completen la prueba del flujo entero y conserven las decisiones anteriores mediante ADR sustitutos.

</details>


## Semana 11 · Integración y resiliencia

La integración HTTP con los casos de uso es identificable, pero faltan los artefactos específicos de fallos parciales, idempotencia y decisión de extracción. La deuda de persistencia reconocida no reemplaza una matriz de mitigaciones por modo. Actualizar aspectos, preservar ADR sustituidos y reconciliar la documentación con Flask y el despliegue vigente.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

El avance sigue siendo preliminar y no registra cambios posteriores al cierre. Completar garantías por operación, contrastar lecturas y escrituras reales, decidir caché e invalidación y justificar la decisión de datos más costosa de revertir. Revisar especialmente la creación de invitaciones en lote, que puede dejar efectos parciales ante una validación tardía.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **1 abiertas, 0 cerradas, 1 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Declara contenedor desplegado, pero dirección pendiente de asignar.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Dos commits 21 de octubre añaden PostgreSQL/SQLAlchemy/Alembic para usuarios y rutas/templates de registro/login/panel/logout con CSRF. Registrar_usuario hace commit/rollback y unicidad correo. Invitaciones siguen memoria; README y arc42 no reflejan nuevo módulo. Último CI falla Ejecutar pruebas, contrato/build skipped; Pages success no sustituye tests.

**Próximos pasos:**
- Corregir CI y agregar pruebas registro/login/migración; diferenciar persistencia PostgreSQL de Usuarios y memoria de Invitaciones.
- Tabla registrar usuario/crear y responder invitaciones → garantías, incluida atomicidad de lote y concurrencia; contrastar dos operaciones.
- Decidir caché/no caché, ADR comparativo persistencia/identidad, actualizar C4/arc42 §8 y README con URL pública iscoutb.dev real.

**Issues:** 1 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Sin URL concreta. README declara contenedor desplegado, pero no publica dirección concreta. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#enagenda) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

No hay cambios en la rama principal respecto al 22 de octubre. Se conserva el avance de registro/login y usuarios PostgreSQL, mientras Invitaciones sigue en memoria. El CI de esa punta sigue fallido y Pages figura exitoso; esto no equivale a pruebas aprobadas ni demuestra la disponibilidad del backend. El README todavía no describe el nuevo módulo ni una URL pública concreta.

**Próximos pasos:**
- Corregir CI y agregar pruebas registro/login/migración; diferenciar persistencia PostgreSQL de Usuarios y memoria de Invitaciones.
- Tabla registrar usuario/crear y responder invitaciones → garantías, incluida atomicidad de lote y concurrencia; contrastar dos operaciones.
- Decidir caché/no caché, ADR comparativo persistencia/identidad, actualizar C4/arc42 §8 y README con URL pública iscoutb.dev real.

**Issues:** 1 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Sin URL concreta. Declara contenedor Dokploy desplegado, pero URL pública pendiente; no hay host concreto. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#enagenda) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Avance integrado: panel del organizador, creación de eventos e invitaciones por evento con modelos/migraciones PostgreSQL. Los casos de uso bloquean filas con FOR UPDATE antes de contar y escribir, con límites de cuatro eventos activos y treinta invitados. En app/web.py conviven las nuevas rutas /eventos/invitacion/<token> sobre PostgreSQL y las rutas heredadas /invitacion y /api/v1/invitaciones sobre memoria: no declarar toda Invitaciones persistida ni toda Invitaciones en memoria. El CI falla durante colección de cuatro módulos porque DATABASE_URL no está configurada; contrato y build Docker se omiten. Pages exitoso es publicación estática, no aceptación del backend. README no se actualizó ni publica URL concreta.

**Próximos pasos:**
- Configurar una base aislada de pruebas y migraciones en CI antes de ejecutar la suite; verificar contrato y build omitidos.
- Probar concurrencia y límites de eventos/invitados contra PostgreSQL y documentar coexistencia o migración de rutas heredadas en memoria.
- Actualizar README, C4/arc42 y URL iscoutb.dev; no confundir Pages con despliegue funcional del backend.

**Issues GitHub:** 1 abiertas y 0 cerradas; 0 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#enagenda) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).


## Seguimiento actual · 26 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

PR3 integra documentación de consistencia y prototipo aislado de envío automático de invitaciones, con proveedor simulado, deduplicación, reintentos y DLQ en memoria. Su workflow específico ejecuta pruebas y demo con éxito; no envía correos reales ni integra Flask/BD/Dokploy. El CI general ahora falla al recolectar test_simulador.py por import relativo sin paquete reconocido, no por el error DATABASE_URL del corte anterior; contrato y Docker quedan omitidos. Pages publica documentación estática, no aceptación de la API. README mantiene host pendiente, sin URL pública concreta.

**Próximos pasos:**
- Corregir empaquetado/import del prototipo para que pytest general pueda recolectarlo y repetir contrato/build.
- Mantener separada evidencia de correo simulado de envío real; definir persistencia/proveedor antes de integrar.
- Documentar URL institucional concreta y alcance de rutas PostgreSQL frente a las heredadas en memoria.

**Issues GitHub:** 1 abiertas y 0 cerradas; 0 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

[Fuentes y alcance](../seguimiento-s12-2026-10-26.md#enagenda) · [Issues](../seguimiento-issues-2026-10-26.md) · [URL y dominio](../seguimiento-despliegues-2026-10-26.md).
