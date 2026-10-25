# Retroalimentación publicable · Recobra

## Semanas 1 y 2

## Evidencia S1

El repositorio está en la organización, es público y el README funciona como ficha del problema con objetivos claros (centralizar, emparejar, notificar, trazabilidad). Les faltó casi todo el montaje: las dos tensiones de calidad, la tabla de ocho columnas en `docs/aspectos.md` (hoy es texto), la plantilla arc42 y las carpetas `docs/adr/` y `docs/c4/`. El archivo `docs/ia` está vacío: regístrenlo con usos reales (o declaren que aún no han usado IA) y pónganle la extensión `.md`.

## Evidencia S2

Las restricciones están bien trabajadas: clasificadas (técnicas, organizativas, legales), justificadas y vinculadas al escenario que las comprueba. El árbol de utilidad prioriza por impacto y riesgo con tabla de priorización, y la mayoría de escenarios tiene sus seis partes con medidas numéricas. Para corregir antes del corte 1: (1) la ficha pide entre 3 y 5 escenarios y tienen 7 (más sub-escenarios): prioricen y quédense con los más importantes; (2) el escenario S2 de seguridad no tiene medida numérica — exprésenla con cifra, unidad y condición; (3) el C4 no es un diagrama: `docs/C4.md` es solo texto, háganlo como código con leyenda y flechas etiquetadas; (4) actualicen `docs/aspectos.md` con la tabla de ocho columnas y enlaces a los escenarios; (5) llenen `docs/ia.md`; (6) organicen la documentación en `docs/arc42/`, `docs/adr/` y `docs/c4/`; (7) dos integrantes no aparecen en el historial.

## Semana 3

Qué está bien: el ADR 0001 sigue la convención y trae contexto, alternativas descartadas con motivo y consecuencias; el README documenta el arranque con un solo comando y `docs/ia.md` ya registra la semana 3 con lo aceptado y lo rechazado.

Qué corregir antes del corte 1 (semana 5):
1. Sección 4: faltan tácticas concretas ligadas a los escenarios S1–S7 (timeouts, reintentos, colas…); §4.4 son principios de paquetes, no tácticas.
2. La matriz comparativa de §4.2 no evalúa contra el árbol de utilidad (no hay filas por escenario); además `docs/matriz_arquitectura.md` quedó obsoleto y contradice el ADR: bórrenlo o alinéenlo.
3. Enlacen el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva; hoy solo se alcanza desde §4.3.
4. Materialicen los paquetes `domain/ports` y `application/use-cases` que declaran el ADR y el README (solo existe el adaptador HTTP) y aporten evidencia del verde (workflow o run).
5. Higiene del repo: saquen `node_modules/` con un `.gitignore` y registren el ADR anterior como «reemplazado» en lugar de borrarlo (contrato del curso).

## Semana 4 · S4

La documentación arc42 (secciones 1-6 y 10), el glosario y los C4 en Mermaid son un buen avance. Para la próxima entrega, completen la sección 9 enlazando los ADR existentes, ajusten el C4 nivel 2 para que coincida con el código real del repositorio y amplíen docs/aspectos.md a las 8 columnas del contrato con enlaces verificables. También es necesario dejar evidencia pública de que las pruebas corren en CI y evitar versionar node_modules. Mantengan el ritmo y prioricen que la documentación refleje exactamente lo que hay en el código al cierre.
## Semana 5 · CORTE1

El proyecto está sólido en arquitectura, documentación y CI. Para el corte 1, falta el archivo correcciones.md en la raíz, que debe listar cada hallazgo de S1-S4 con su evidencia de corrección. Asegúrense de subir el PDF a Moodle y preparen la sustentación. El resto de la matriz está al día.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

El contenido del reto es de muy buen nivel: identificaron con precisión que el curso les exigía un cambio de tecnología obligatorio, midieron cómo estaba el sistema antes del cambio con un procedimiento reproducible (y hasta corrigieron ustedes mismos una cifra que habían puesto sin medir), compararon alternativas con ventajas y desventajas reales, documentaron la decisión con el dato que la haría reconsiderar, y migraron el backend y agregaron el cliente móvil sin romper el dominio ni las pruebas. Incluso agregaron una prueba que demuestra que el sistema se degrada de forma controlada si falla el almacenamiento. El problema es la etiqueta `corte-1`: quedó fijada casi diez horas después del cierre, así que formalmente la entrega llegó tarde aunque el trabajo ya estuviera casi completo antes. Además, sigue pendiente un asunto serio de seguridad: un token de un servicio externo quedó expuesto en el historial del repositorio hace semanas (dentro de una carpeta que ya no se versiona, pero que sigue siendo visible en commits anteriores) y ustedes mismos lo reconocieron en su documentación sin confirmar que lo rotaron. Prioricen eso antes de la sustentación. También sigue habiendo un integrante con una sola contribución en todo el semestre.

## Semana 7 · S7

El avance está bien encaminado: el contrato OpenAPI 3.0.3 con rutas y esquemas, la prueba de contrato y el ADR-0004 con la alternativa descartada quedan documentados y son defendibles, y hay evidencia de que la prueba falla ante un cambio incompatible, que es justo lo que separa el nivel competente del sobresaliente. Para cerrar la trazabilidad: 1) dejen explícito en el workflow el paso que ejecuta la prueba de contrato y adjunten el enlace del run verde y del run en rojo; 2) publiquen la URL del análisis de SonarCloud con el estado del Quality Gate para el hash revisado; 3) adjunten el historial git del archivo de contrato, porque la versión declarada no basta; 4) revisen que el registro de IA incluya, por cada uso, qué se rechazó y por qué; 5) en la tabla de aspectos, marquen con claridad las filas cuyo eslabón aún no existe para que la cadena no parezca rota. Los flujos de arc42 y las flechas etiquetadas del C4 nivel 2 están bien resueltos.
## Semana 6 · S6

El mapa de contextos y la tabla módulo-datos están bien encaminados. Para cerrar S6, documenten el recorrido de búsqueda de escrituras y las no conformidades de propiedad con entidad, dueño esperado y ubicación. Añadan la sección 8 de arc42 con lenguaje ubicuo y mapa de contextos. Si los límites cambiaron desde el primer corte, incluyan el diff, C4 nivel 3 y ADR. Completen la evidencia de SonarCloud con run exitoso y URL pública del Quality Gate. Rote el token expuesto en el historial y dejen constancia; no basta con retirarlo del HEAD.

## Semana 8 · S8

### Recomendaciones prioritarias

- Cierren la evidencia de SonarCloud: falta el paso que invoca el scanner en el workflow y la URL pública del análisis con su Quality Gate. Tener el archivo de configuración no basta.
- Dejen de editar ADR ya aceptados: cuando cambie una decisión, escriban un ADR nuevo y marquen el anterior como reemplazado. Hoy dos ADR se editaron después de aceptarse sin ese enlace.
- La URL del sistema y la respuesta del health check quedan pendientes de calificar en esta pasada porque se entregan por Moodle.

La entrega cambió de forma notable respecto de la revisión anterior: el proyecto ya tiene infraestructura como código, procedimiento de recreación en el README, pipeline en verde, logs estructurados en JSON, una métrica consultable ligada al escenario de mantenibilidad, el secreto de base de datos tomado de la configuración del proveedor, estimación de costo con supuestos y punto de ruptura, arc42 con una caja por pieza y su ubicación real, restricciones de costo y «sin tarjeta» en la sección 2, y un ADR por cada decisión de plataforma con la alternativa descartada y la capa gratuita verificada. Conserven el CI en verde y cierren las dos no conformidades transversales.

## Semana 9 · S9 (revisión definitiva)

La búsqueda con filtros ya es una porción nueva y trazable: la mutación detectó una prueba débil y la corrigieron. Mantengan la separación explícita entre las mediciones locales y la brecha de producción. Sincronicen los C4 con la persistencia real, completen la sucesión de ADR y acrediten el scanner y Quality Gate del commit entregado.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Hay mejora operativa y un experimento S1, con límites de causalidad. Se corrigieron arc42, C4, readiness, medición GET, filtro 503 y contrato, y se enlazó la sucesión de ADR con la evidencia.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Sin deriva material observada; acoplamientos aceptados por ADR.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

No se observó deriva material en los recorridos revisados; se conservan los límites y deudas explícitos del diseño.

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Documenten cuál es el escenario operativo asignado y preparen una línea base y un resultado comparables en el despliegue. La salud responde, pero eso no prueba el flujo principal. Añadan la métrica del escenario al entorno, resuelvan la brecha de capacidad que midieron y expliquen la decisión frente al presupuesto antes de la sustentación.

### Actualización del 10 de octubre de 2026

La actualización del segundo corte incorpora un experimento propio sobre Dokploy, una decisión de plataforma con alternativas y costo, la métrica de búsqueda y la separación entre proceso vivo y disponibilidad de la base. La comprobación actual de salud y readiness responde correctamente; C4 ya incluye PostgreSQL, búsqueda y Emparejamiento, y los antecedentes de los ADR tienen enlaces de sucesión.

La elección de S1 está explicada como una indicación del docente comunicada por el equipo. Falta corroborar esa procedencia. Para defender el experimento, conserven las salidas originales y el estado desplegado exacto: la tabla declara mejora y cumplimiento a doscientas conexiones, pero cambia el volumen respecto de la base y solo hay una corrida por nivel. El percentil del servidor, calculado sobre éxitos recientes, no sustituye la latencia de extremo a extremo ni demuestra por sí solo que toda la diferencia sea red.

Completen las vistas de construcción y ejecución de arc42, actualicen C4-C3 con readiness, la medición GET de la búsqueda ya representada y el filtro 503 de almacenamiento no disponible, y añadan al contrato la respuesta de indisponibilidad al consultar por identificador. SonarCloud sigue pendiente de evidencia actual de análisis y Quality Gate bloqueante; el verde general de CI no lo acredita cuando el scanner admite fallos. Las correcciones actuales no modifican la evaluación definitiva de la semana anterior.

Para la sustentación, preparen una demostración de fallo y recuperación de la base, expliquen el costo y los riesgos del servidor compartido y diseñen una comparación controlada que permita distinguir plataforma, datos y red.

</details>

## Semana 11 · Integración y resiliencia

La entrega tiene evidencia sustantiva de idempotencia, límites de espera y recuperación, junto con una decisión fundamentada de no extraer Emparejamiento. Mantengan diferenciados eventos perdidos, mitigaciones probadas y planes pendientes. Actualicen las frases antiguas sobre ausencia de cuentas, única escritura y avisos no recuperables para que coincidan con el producto actual.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Se reconoce el avance anticipado de consistencia eventual entre publicaciones y reclamaciones, con pasos retomables y reconciliadores, además de recuperación acotada de avisos. Faltan diseño de caché e invalidación o su exclusión argumentada, ADR de la decisión de datos más costosa de revertir y ambas estrategias en arc42 sección 8. Corrijan también la referencia residual a coincidencias en memoria en el C4.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Presentó, según confirmación docente. El README publica dirección institucional. No se infiere funcionamiento integral ni calificación de la presentación.

Issues al corte de consulta: **0 abiertas, 0 cerradas, 0 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Institucional**. Presentación confirmada por docente; no se infiere demostración funcional adicional. Dirección(es) documentada(s): https://recobra.iscoutb.dev ; https://recobra.iscoutb.dev/app/.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Avance sustancial del 21 de octubre: ADR0025 documenta caché HTTP/ETag e invalidación; ADR0026 define cuatro eventos, tres reintentos, cola de fallidos y reproceso cada cinco minutos; ADR0027 compara seis decisiones y estima reversión en 6–9 días-persona. arc42 §8 contiene la tabla de garantías y C4 corrige coincidencias en memoria. El CI incluye backend, Flutter, adaptadores contra PostgreSQL real, scanner y Quality Gate exitosos. Se contrastaron middleware, pruebas de caché, entrega de eventos y persistencia de la cola.

El docente confirmó presentación.

**Próximos pasos:**
- Extender suite PostgreSQL de 7/9 adaptadores a Reclamaciones/Sesiones y e2e completos; hoy estos últimos RAM.
- Conservar límites: EventEmitter no durable; publicacion.creada fuera del nuevo contrato sin recálculo de coincidencias; fallo al guardar cola depende conciliación de 3 días y cola de 7 días.
- Corregir afirmación 'despliegue invalida lugares': navegador con max-age=3600 puede conservar durante 1 hora; TTL de 60 s miniaturas tras borrado aceptado explícitamente, no invalidación inmediata.
- Añadir evidencia de backup/restauración y alerta cola; son próximos pasos, no negar que ahora existen caché, ADR y arc42 §8.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Institucional. Docente confirmó presentación, no una certificación de funcionamiento por auditoría. URL documentada: https://recobra.iscoutb.dev ; https://recobra.iscoutb.dev/app/. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#recobra) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Sin nuevos commits respecto al seguimiento del 22 de octubre. Se mantienen los avances S12 ya reconocidos: caché HTTP/ETag, estrategia de eventos y ADR comparativo de reversión. El CI de esa punta continúa exitoso; no se presenta como una nueva ejecución de hoy. Siguen siendo relevantes los límites declarados de EventEmitter no durable y la cobertura PostgreSQL de siete de nueve adaptadores; los e2e completos aún usan RAM. Presentación confirmada por el docente.

El docente confirmó presentación.

**Próximos pasos:**
- Extender pruebas PostgreSQL a Reclamaciones y Sesiones y a los e2e completos.
- Corregir la afirmación de que desplegar invalida lugares: un navegador puede conservar la respuesta durante max-age; mantener explícito el TTL de miniaturas tras borrado.
- Conservar límites de cola/eventos, y aportar evidencia de restauración de backups y alertas operativas sin negar los artefactos S12 existentes.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Institucional. Vitrina y app institucionales. Docente confirmó presentación; no se añadió una auditoría funcional. URL documentada: https://recobra.iscoutb.dev ; https://recobra.iscoutb.dev/app/. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#recobra) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Dos commits posteriores al corte anterior responden al feedback: se corrigió la invalidación de /lugares (el despliegue no borra caché del navegador), se ampliaron los adaptadores PostgreSQL a nueve de nueve, se añadió verificación de respaldo/restauración y alerta de cola de fallidos. El run exacto la revisión citada registra 37 pruebas de adaptadores aprobadas y restauración de 23 filas en nueve tablas sin diferencias; Quality Gate aprobado. Los e2e nuevos prueban mensajes en la aplicación con fallos simulados; los e2e generales siguen en memoria. No confundir procedimiento CI con respaldos programados de producción: estos siguen pendientes, igual que alerta hacia personas y RTO real. README ahora separa explícitamente vitrina, Flutter Web y API. Presentación confirmada por docente.

**Próximos pasos:**
- Configurar y evidenciar respaldo programado de producción y ensayo controlado con tiempos; CI valida procedimiento, no operación productiva.
- Conectar alerta de cola a una notificación operativa; hoy solo log/métrica.
- Mantener explícitos límites de EventEmitter, una instancia y e2e en memoria; complementar cobertura del flujo completo contra PostgreSQL.

**Issues GitHub:** 0 abiertas y 0 cerradas; 0 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Institucional. README aclara vitrina, Flutter Web y API en mismo host institucional; no se añade auditoría funcional.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#recobra) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).
