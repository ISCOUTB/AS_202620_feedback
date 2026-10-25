# Retroalimentación publicable · uniTeam

## Semanas 1 y 2

## Evidencia S1

Bien: repositorio con el nombre de la convención, ficha del problema con usuarios y alcance, plantilla arc42 descomprimida, `docs/adr/` y `docs/c4/` creados, y registro de IA iniciado.

Corregir: la ficha del problema debe declarar las dos tensiones de calidad enfrentadas (dos atributos en conflicto); `docs/aspectos.md` debe ser la tabla de ocho columnas del curso con al menos una fila con ID y aspecto; y en `docs/ia.md` conviene registrar entradas por uso y qué se rechazó y por qué. Confirmen también que todos los integrantes tienen acceso al repositorio y hagan que cada uno firme commits con su propia cuenta.

## Evidencia S2

Bien: secciones 1, 2 y 3 del arc42 redactadas y coherentes, restricciones clasificadas (técnicas, organizativas, legales) y justificadas, cinco escenarios con sus seis partes y medida numérica —y además con método de verificación—, árbol de utilidad priorizado con justificación, C4 de contexto como código con leyenda y flechas etiquetadas, y aspectos enlazados a sus escenarios. Nivel sobresaliente.

Corregir antes del corte 1: renombrar el ADR a la convención `NNNN-titulo-en-kebab-case.md` (sin el prefijo «ADR-»), asegurar que los cuatro integrantes aparezcan en el historial de commits, y revisar que el historial del repositorio no conserve archivos de un proyecto anterior.

## Semana 3

Qué está bien: la sección 4 de arc42 trae tácticas por escenario, la matriz compara los tres estilos contra sus propios escenarios, el ADR-003 justifica la decisión con alternativas descartadas y la estructura de paquetes es coherente con el estilo elegido.

Qué corregir antes del corte 1 (semana 5):
1. Renombrar los ADR a la convención `NNNN-titulo-en-kebab-case.md` (quitar «ADR-» y el « (1)») y marcar ADR-001 como reemplazado por ADR-002.
2. Enlazar el ADR-003 desde `docs/aspectos.md` y desde el escenario que lo motiva.
3. Documentar en el README el comando único de arranque de la app (hoy solo está el de la prueba) y corregir el paquete `httpx2` de `requirements.txt`.
4. Registrar en `docs/ia.md` el uso de IA de esta semana con lo rechazado y su motivo.
5. Contribución: solo una persona firmó los commits de esta semana; todos los integrantes deben aparecer en el historial antes del corte 1.

## Semana 4 · S4

La entrega de la semana 4 está sólida en lo que se pudo verificar: C4 como código con coherencia entre niveles, corte vertical con las tres capas citadas, arranque con un solo comando y tabla de aspectos con enlaces navegables. Para cerrar los huecos de verificación, conviene que la sección 9 de arc42 cite explícitamente los ADR, que la sección 10 referencie los escenarios de calidad y que el glosario use términos propios del dominio. Aporten también la URL del run de CI en verde que ejecuta la prueba del recorrido completo; el badge del README no es evidencia de ejecución. El registro de IA debe mostrar lo aceptado y lo rechazado con su motivo. La medición de ESC-01 es un buen cierre y deja la línea base lista para el corte.

## Semana 5 · CORTE1

Sin actividad CORTE1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

El repositorio no tiene la etiqueta `corte-1` y no cambió entre la revisión de antes del cierre y el cierre mismo. Dicho eso: encontramos un trabajo (la decisión de delegar la autenticación en un proveedor externo, en vez de confiar en una cabecera que cualquiera podía falsificar) que tiene toda la forma de una buena respuesta a una restricción — diagnóstico claro, comparación real de alternativas con sus costos, decisión documentada, implementación de punta a punta que arranca con un solo comando, y pruebas en verde. Lo evaluamos como su respuesta más probable al reto, aunque el repositorio no lo declara explícitamente como tal — en la sustentación conviene confirmar si esa fue, en efecto, la restricción asignada.

Lo que le falta a esa respuesta para estar completa: (1) medir con una cifra cómo de explotable era el problema antes del cambio, no solo describirlo; (2) medir el resultado después del cambio y compararlo contra el umbral de ese escenario de seguridad; y (3) una entrada en el registro de uso de IA que hable puntualmente de esta pieza de trabajo (qué se aceptó, qué se corrigió o rechazó y por qué), no solo de las decisiones de otras semanas.

Sobre la autoría: con esta revisión pudimos atribuir contribución a los cuatro integrantes declarados, algo que antes no se había podido confirmar del todo. Queda pendiente identificar a quién corresponde una cuenta adicional que aparece en el historial con más commits que cualquier otra.

## Semana 6 · S6

El mapa de contextos y la tabla inicial de dueño único tienen una estructura clara: distinguen relaciones síncronas, eventos y consumidores de solo lectura. El siguiente paso indispensable es convertir la auditoría prevista en evidencia real: contrasten cada entidad con el esquema y los modelos, reemplacen los marcadores “revisar” por no conformidades con ruta y línea, y enlacen cada corrección con una acción concreta. Incorporen el mapa y el lenguaje ubicuo en la sección 8 de arc42, relacionen los contextos con la tabla de aspectos y publiquen el análisis SonarCloud con su Quality Gate.

## Semana 7 · S7

Sin actividad S7: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 8 · S8 (revisión definitiva)

El proyecto ya se despliega en cuatro piezas (sitio estático, API en contenedor, base de datos gestionada y proveedor de identidad), con infraestructura como código, un health que además comprueba la base de datos, logs en una línea JSON por petición, métricas ligadas a sus escenarios, secretos fuera del código, la sección 7 de arc42 con una caja por pieza y la sección 2 con el límite de costo y la restricción de tarjeta; cada pieza de plataforma tiene su ADR con alternativas. El cálculo de costo parte del volumen del escenario y describe en qué punto se agota cada capa gratuita.

Lo prioritario: reparen el workflow de integración continua en la rama principal, que en el estado calificado termina en rojo (incluido el Quality Gate), y no editen ADR ya aceptados —si una decisión cambia, escriban uno nuevo y marquen el anterior como reemplazado—. Queda pendiente confirmar con el docente a qué integrante corresponde cada cuenta del historial. Las filas de URL desplegada y de health quedan pendientes de calificar porque la URL se entrega por Moodle.

## Semana 9 · S9 (revisión definitiva)

La nueva porción de Mis tareas completa la cadena exigida: decisión aceptada, código, prueba que detecta el defecto, medición y auditoría de erosión. Mantengan explícito que la medición es SQLite en proceso; todavía falta comprobar el costo de la consulta extra en MySQL. El cumplimiento de S9 no cierra los fallos actuales del pipeline ni el Quality Gate.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El ensayo antes y después tiene tres corridas de 300 peticiones y está separado de producción, MySQL, red y concurrencia. ADR-0013 justifica el costo de una consulta adicional y la separación implementada. El CI falla y permanecen incompletos la documentación transversal y el esquema.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Consumidores comparten sesión SQL pese a garantía de aislamiento de fallos.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · Capturar la excepción del consumidor no aísla un fallo SQL de la sesión compartida:** Los consumidores de auditoría de operaciones permitidas (TareaCreada/EstadoCambiado) pueden fallar en flush y dejar fallida la misma unidad de trabajo que el handler intentará confirmar. El consumidor de acceso denegado sí crea y confirma una sesión propia (consumidores.py:27–37), por lo que no está incluido en este riesgo de sesión compartida. Por tanto, la garantía general de que un consumidor no tumba la petición no está sustentada para errores SQL. Es un riesgo estático condicionado al fallo, no una caída observada. **Acción:** Elegir y documentar una semántica única: si auditoría es atómica, propagar el fallo y retirar la promesa de disponibilidad independiente; si es secundaria, usar savepoint correctamente delimitado u outbox/otra unidad de trabajo. Añadir prueba de fallo real de flush/commit del consumidor, no solo excepción Python. No introducir asincronía sin nuevo ADR. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Identifiquen la consigna operativa asignada y diseñen su experimento con línea base en el MVP desplegado. Recuperen CI y los chequeos de despliegue, repitan la medición relevante con MySQL y carga de red, y completen arc42 y propiedad de datos. La comparación local es un buen punto de partida, pero no sustituye el resultado operativo ni la sustentación.

</details>

## Semana 11 · Integración y resiliencia

La aplicación y sus integraciones están presentes, pero falta la entrega específica de fallos parciales. Documenten los tres modos con mitigaciones, diseñen la idempotencia de creación de tareas y evalúen extraer o no un módulo. La sección de riesgos y la tabla de aspectos deben incorporar ese análisis; el comprobador público de despliegue está fallando.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Avance preliminar: existen caché JWKS, caché de flujo y eventos síncronos con límites declarados. Falta la política completa de invalidación, la tabla de garantías y el contraste de dos operaciones; la sección 8 sigue pendiente. Comparen las decisiones de datos para justificar cuál sería más costosa de revertir, sin confundir el costo operativo con el de migración.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 1 cerradas, 1 en total**. Los 1 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Externo**. Frontend y API en Render. Dirección(es) documentada(s): https://uniteam-web.onrender.com ; https://uniteam-api.onrender.com.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

La rama principal sigue en el despliegue Dokploy integrado el 13 de octubre, pero el README conserva URLs Render y no publica un subdominio iscoutb.dev. La comprobación programada del 22 de octubre a las 07:38 Colombia falla en sus seis verificaciones de esos endpoints; es evidencia de ese sondeo, no una certificación de indisponibilidad permanente ni del estado de un dominio Dokploy no documentado. Para S12, completar la tabla de garantías para crear tarea y cambiar estado, aclarando el límite del bus en proceso ante fallos de consumidores; completar invalidación de JWKS y del flujo de estados en clientes abiertos, comparar costos de reversión de datos y terminar arc42 §8. La única issue cerrada es de prueba (hola mundo); registrar pendientes reales y enlazar evidencia.

**Issues:** 0 abiertas y 1 cerradas; 0 abiertas sin responsable. Cierres: 1 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Externo. README conserva Render aunque hay configuración Dokploy; no inventar el dominio actual. URL documentada: https://uniteam-web.onrender.com ; https://uniteam-api.onrender.com ; https://uniteam-api.onrender.com/health. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#uniteam) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Las PR #6, #7 y #8 se fusionaron; hay ajustes de código/nginx y cambio a análisis automático de SonarCloud. El README ya publica dominios DuckDNS. El CI vigente pasa pruebas MySQL, compilación frontend e imágenes; conserva generación de cobertura con --cov, pero eliminó su publicación y el job Sonar con espera del Quality Gate. El README afirma que no existe CI, en contradicción con workflow y run actuales. El sondeo del 24 de octubre falla seis verificaciones, pero sigue consultando Render: ese resultado no demuestra caída de los dominios DuckDNS.

**Próximos pasos:**
- Alinear sonda, README y guía con los dominios reales; publicar el subdominio iscoutb.dev requerido sin inventarlo.
- Restablecer trazabilidad de análisis/cobertura y verificar por separado el Quality Gate; no equiparar CI verde con gate aprobado.
- Completar tabla de garantías de crear tarea/cambiar estado y límites del bus en proceso; invalidación de JWKS y clientes abiertos, ADR comparativo de reversión y arc42 §8.

**Issues:** 0 abiertas y 1 cerradas; 0 abiertas sin responsable. Cierres: 1 completed. El estado registrado no acredita por sí solo implementación.

**README:** Externo. README ahora publica DuckDNS, no Render ni iscoutb.dev. La sonda aún apunta a Render. URL documentada: https://uniteam-web.duckdns.org ; https://uniteam-api.duckdns.org ; https://uniteam-api.duckdns.org/health. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#uniteam) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin cambios de punta, README o PR desde el corte previo. La sonda más reciente falla, pero sigue apuntando a Render mientras el README publica DuckDNS: no prueba una caída del dominio actual. Se mantiene separado el CI exitoso del código de la comprobación de despliegue fallida; no se verificó funcionamiento en vivo.

**Próximos pasos:**
- Actualizar la sonda a los destinos documentados y publicar subdominios iscoutb.dev.
- Alinear la afirmación del README sobre CI con el workflow existente y recuperar trazabilidad de cobertura/Quality Gate.
- Completar garantías por operación, invalidación y ADR de reversión con evidencia concreta.

**Issues GitHub:** 0 abiertas y 1 cerradas; 0 abiertas sin asignar. Cierres: 1 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Externo. Frontend y API DuckDNS. Sonda sigue consultando Render; su fallo no determina disponibilidad de DuckDNS.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#uniteam) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).
