# Retroalimentación publicable · Clubs UTB

## Semana 1

- Está bien: el repositorio existe con el nombre correcto y es público; el problema de la gestión de clubes está bien descrito; `docs/ia.md` arrancó con contenido real.
- Falta: la ficha del problema (usuarios y alcance), las dos tensiones de calidad y la estructura (`docs/arc42/`, `docs/adr/`, `docs/c4/`, y recuperar el README).
- Corregir antes del corte 1: convertir `docs/aspectos.md` en la tabla de 8 columnas del curso con al menos un aspecto, y asegurar que los cuatro integrantes tengan acceso y firmen commits.

## Semana 2

- Está bien: las secciones 1, 2 y 3 de arc42 están redactadas y sólidas (metas con interesado, restricciones clasificadas y justificadas), el árbol de utilidad usa pares importancia/dificultad, el C4 de contexto está como código Mermaid con flechas etiquetadas, y los 6 escenarios tienen las seis partes con medidas numéricas.
- Falta: `docs/aspectos.md` sigue sin la tabla de aspectos ni enlaces a los escenarios; son 6 escenarios y se pedían entre 3 y 5; `docs/ia.md` no registró usos reales de la semana 2; la ficha del problema aún no declara las dos tensiones de calidad.
- Corregir antes del corte 1: elegir los 3–5 escenarios que se conservan, llenar `docs/aspectos.md` con su fila por aspecto y los enlaces, mover el C4 a `docs/c4/`, y declarar si hay o no restricciones legales.

## Semana 3

Qué está bien: la sección 4 justifica la estrategia hexagonal con tácticas nombradas (timeout, reintento, caché, índices), la matriz comparativa va fila por fila contra sus escenarios U1–U3 y C1–C3, y el ADR 0001 está aceptado con alternativas motivadas.

Qué corregir antes del corte 1 (semana 5):
1. El arranque no quedó documentado en el README y `backend/src/main.py` y `tests/test_health.py` están vacíos en la versión calificada: documenten el comando único de arranque y dejen la prueba con asserts reales.
2. Hagan verificable la prueba en verde: agreguen un pipeline o evidencia de ejecución.
3. Hagan alcanzable el ADR: enlácenlo desde `docs/aspectos.md` (con la tabla de 8 columnas) y desde el escenario U2 que lo motiva.
4. Actualicen `docs/ia.md` (sin cambios desde el 9 de agosto) registrando usos y qué se rechazó y por qué, y borren el residuo `docs/adr/.temp`.

Ojo: parte del trabajo llegó después del cierre y no contó para esta entrega; la próxima vez asegúrense de empujar antes de la medianoche del domingo.

## Semana 4 · S4

Entrega S4 completa en lo esencial: arc42 1-6, 9, 10 y glosario redactados; C4 niveles 1-2 coherentes; corte vertical que atraviesa interfaz, lógica y persistencia con prueba en verde; fila U2 de aspectos.md trazable hasta Pruebas. Para cerrar los pendientes: (1) unificar el arranque en un solo comando en el README; (2) configurar SonarCloud para el análisis estático del contrato; (3) declarar explícitamente que el contenedor Flutter aún no tiene código. El registro de IA y los ADR están bien llevados; continúen así.

## Semana 5 · CORTE1

El proyecto está sólido en documentación y corte vertical, con CI pasando. Sin embargo, falta el archivo correcciones.md en la raíz, que es obligatorio para esta entrega. Deben crearlo antes del cierre, listando cada hallazgo de S1-S4 y cómo lo resolvieron, con evidencia. También asegúrense de subir el PDF al aula. El resto de la matriz está bien.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Revisando el repositorio completo hasta el último commit antes del cierre, seguimos sin encontrar una respuesta a la restricción nueva que pedía este corte: no hay etiqueta `corte-1`, no hay un ADR nuevo, no hay una cifra de línea base medida ni un resultado contrastado contra un umbral. Lo único que se agregó en esta semana fue un endpoint de publicaciones (con su prueba y con el pipeline en verde) y un ajuste de una línea en la sección de requisitos de calidad, ninguno de los dos vinculado a una restricción diagnosticada en la documentación.

Un hallazgo nuevo de esta revisión: el ADR-0001, que ya estaba aceptado, se editó otra vez el 30 de agosto para agregarle una sección de trazabilidad. El contrato pide que un ADR aceptado no se toque — si hace falta completar o cambiar algo, se escribe un ADR nuevo que lo reemplace y se enlaza. No hace falta deshacer ese cambio, pero de aquí en adelante cualquier ajuste a esa decisión debe ir en un ADR nuevo, no en el mismo archivo.

Para la sustentación: preparen quién puede explicar qué restricción les asignaron, qué se midió antes del cambio, y por qué el endpoint agregado no aparece documentado como respuesta a ella.

## Semana 3 · S3

El ADR y la matriz comparativa están bien orientados y la estructura de paquetes refleja la decisión hexagonal. Para las próximas entregas: automaticen la prueba en un pipeline visible, documenten el arranque en el README desde el primer commit, y hagan navegable la trazabilidad en docs/aspectos.md y en los escenarios de calidad. Cuiden también las convenciones de nombres de ADR y el orden del repositorio. Varios de estos puntos se corrigieron después del cierre; procuren que los arreglos lleguen antes del cierre en las siguientes semanas.

## Semana 6 · S6

El mapa de contextos con relaciones tipificadas, la tabla de dueño único, el ADR del reajuste y la lista de no conformidades muestran un avance sólido en la entrega. Para cerrar del todo:
1) Agreguen el scanner de SonarCloud al workflow y publiquen la URL del análisis con su Quality Gate; hoy solo hay pruebas.
2) Completen docs/aspectos.md con la columna de evidencia y eliminen las celdas 'Pendiente' que dejan filas sin defender.
3) Escriban explícitamente qué fila de aspectos corresponde a cada contexto del mapa (hoy la relación queda implícita).
4) Corrijan el enlace roto a la tabla de módulos y las menciones que aún declaran pendiente una alineación ya aplicada.
5) Cierren NC-01 y NC-02 o actualicen su plan con fecha y responsable.
6) Dejen registrado el recorrido de auditoría (comando y alcance) para que la lista de no conformidades sea repetible.
## Semana 7 · S7

Buen avance del corte: el contrato OpenAPI está versionado con CHANGELOG y esquemas, corresponde con la API implementada, el workflow de contrato invoca la prueba, el ADR de integración compara alternativas síncronas y asíncronas, y la vista de ejecución describe un flujo con diagrama de secuencia. Para cerrar la evidencia: (1) adjunten un run en rojo provocado por un cambio incompatible, que es lo que demuestra que la prueba protege de verdad; (2) publiquen la URL del análisis estático con su Quality Gate y la línea del workflow que invoca el scanner, hoy no hay configuración en el repositorio; (3) unifiquen el ADR de integración en un solo archivo con nombre NNNN-en-kebab-case y corrijan el enlace roto que apunta a él; (4) etiqueten cada flecha del diagrama de contenedores con protocolo y formato, incluidas las que llegan a Supabase; (5) completen la tabla de aspectos con las ocho columnas del curso y sin celdas «Pendiente»; (6) actualicen la tabla de módulos y cierren las no conformidades registradas. ¿Pueden documentar también el flujo de publicaciones en la vista de ejecución y subir la evidencia del cambio que hizo fallar la prueba?

## Semana 8 · S8 (revisión definitiva)

La entrega llegó parcialmente. Está bien: la infraestructura como código versionada (Dockerfile y Terraform de Supabase), la vista de despliegue con una caja por pieza y su entorno, las restricciones de costo y «sin tarjeta» en la sección 2, la estimación de costo con volumen propio y el punto de ruptura de la capa gratuita, y los secretos fuera del código.

Falta:
1. Desplegar y publicar la URL pública con la hora y el código de respuesta de `/health`.
2. Poner en verde los workflows de pruebas y de contrato sobre la rama principal.
3. Añadir configuración de logs estructurados con una línea de ejemplo y una métrica consultable ligada a un escenario de calidad.
4. Documentar en el README cómo recrear el entorno desplegado a partir del Dockerfile y del Terraform.
5. Escribir un ADR de plataforma para el hosting de la API, con alternativa descartada; hoy solo hay un ADR de la base de datos y está en estado «Propuesto».
6. Unificar los ADR 0003 duplicados y con nombre fuera de la convención, y no editar un ADR aceptado: cuando cambie una decisión, escriban uno nuevo que la reemplace.

La URL del despliegue se entrega por Moodle y no se califica en esta pasada.

## Semana 9 · S9 (revisión definitiva)

La auditoría del health check, el rechazo de una dependencia inexistente y la decisión de no incorporar IA generativa aportan evidencia útil. La cadena sigue rota y falta medición frente al umbral. La implementación completa de autenticación llegó después del cierre; el estado congelado aún contiene una referencia a autor_id sin definir.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

Se reconoce la decisión de autenticación JWT/JWKS y su implementación mediante puertos y adaptadores. La regresión funcional está documentada; falta validación con sesión real y medición operacional. Completen logs de intentos rechazados, métrica del escenario y trazabilidad documental. Los workflows son rechazados por YAML inválido antes de ejecutar jobs; esto no demuestra fallos del código ni de las pruebas.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Documentación sobrestima persistencia y comprobación del proveedor en health.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · La persistencia de publicaciones es memoria, no el adaptador Supabase dibujado:** Las publicaciones de la API no tienen durabilidad entre procesos/reinicios ni el respaldo PostgreSQL que un lector inferiría del C4. **Acción:** Dibujar InMemoryPublicacionAdapter como implementación vigente y Supabase datos como objetivo; o conectar un adaptador durable detrás del puerto y probar reinicio. Separar Supabase Auth efectivamente usado de persistencia de publicaciones. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · El health declarado como comprobación real del proveedor retorna un valor fijo:** Un /health 200 demuestra respuesta de la API, no disponibilidad de Supabase; usarlo como readiness de BD puede ocultar una dependencia inaccesible. **Acción:** Llamarlo liveness y corregir el ADR con una aclaración posterior; implementar readiness separado mediante un puerto real si el servicio depende de la BD. No afirmar que se probó Supabase con este health. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

El avance de autenticación ya separa puertos y adaptadores, pero los pipelines siguen fallando. Aporten URL pública y escenario operativo asignado, validen con un token real y midan el comportamiento ante caída de JWKS. Falta autorización por rol y una línea base para el experimento.

</details>


## Rectificación de la revisión · 14 de octubre de 2026

La comparación del primer corte con la semana seis permite acreditar el diagrama de componentes y el ADR del reajuste que habían quedado pendientes de verificación. Se corrige también la atribución de la no conformidad de errores de conexión: la solución identificada está en la interfaz Flutter y llegó después de los cierres de las semanas seis y siete.

En la semana nueve, la decisión arquitectónica debe ser pertinente a la porción revisada; no se exige que sea nueva. La decisión de no incorporar IA generativa ya había recibido reconocimiento en su criterio específico. Un fallo de configuración del workflow no demuestra que las pruebas fallen.

En el segundo corte se reconoce plenamente la decisión JWT/JWKS y su materialización. La documentación funcional de regresión existe; las limitaciones restantes son su representatividad operacional, la observabilidad y la coherencia documental. Las matrices y la planilla contienen la rectificación aprobada y conservan los estados anteriores como historial.

## Semana 11 · Integración y resiliencia

Se identifica la integración, hay mitigaciones, diseño de idempotencia y una decisión argumentada de no extraer. La tabla debe cubrir explícitamente la respuesta duplicada y separar lo implementado de lo pendiente: el adaptador actual agrega registros en memoria sin deduplicar, pese a las afirmaciones de persistencia transaccional. Actualizar riesgos y aspectos y corregir el CI fallido.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

El flujo síncrono justifica que no se exijan garantías de un broker inexistente. Faltan tabla de consistencia, contraste de dos operaciones, diseño e invalidación de caché y ADR comparativo de costo de reversión. Reconciliar C4 y arc42 con la persistencia y el despliegue reales.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **0 abiertas, 0 cerradas, 0 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Sin dirección pública concreta.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Punta 20 de octubre actualiza registro IA solamente; publicaciones siguen InMemoryPublicacionAdapter en router. README no URL pública. Dos últimos runs failure; jobs de uno vacíos, causa no verificada.

**Próximos pasos:**
- Contrastar crear/listar publicaciones y declarar garantía real en memoria, no atribuir transacción PostgreSQL al adaptador conectado.
- Definir caché/no caché y política tras escritura; sincronizar C4 con almacén real y estado planeado de PostgreSQL/Dokploy.
- ADR comparativo de decisión de datos/reversión; actualizar arc42 §8 y documentar URL iscoutb.dev.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Sin URL concreta. Sin URL pública concreta en el README raíz. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#clubs_utb) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

La rama principal y el README permanecen sin cambios respecto al 22 de octubre. Los dos workflows consultados continúan fallidos y la PR #1 sigue abierta; no se atribuye integración por la existencia de la PR. Sigue siendo necesario conciliar las afirmaciones de PostgreSQL/Supabase con el adaptador en memoria conectado al flujo de publicaciones, y documentar la URL pública real.

**Próximos pasos:**
- Contrastar crear/listar publicaciones y declarar garantía real en memoria, no atribuir transacción PostgreSQL al adaptador conectado.
- Definir caché/no caché y política tras escritura; sincronizar C4 con almacén real y estado planeado de PostgreSQL/Dokploy.
- ADR comparativo de decisión de datos/reversión; actualizar arc42 §8 y documentar URL iscoutb.dev.

**Issues:** 0 abiertas y 0 cerradas; 0 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Sin URL concreta. README raíz sin URL pública concreta. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#clubs_utb) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).
