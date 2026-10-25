# Retroalimentación publicable · ShareU

## Semana 1

Buen arranque: repositorio en la organización, ficha del problema con usuarios y alcance claros, un aspecto declarado con su escenario de calidad, y el registro de IA con lineamientos reales.

Les falta montar la estructura completa: la plantilla arc42 debe ir dentro de `docs/arc42/` (en la S1 no estaba), hay que crear `docs/adr/` y `docs/c4/`, armar la tabla de aspectos con las ocho columnas del curso (hoy está en prosa y sin ID) y declarar las dos tensiones de calidad que hacen interesante el problema.

## Semana 2

El escenario de usabilidad está muy bien desglosado: tiene las seis partes y una medida con cifra y unidad. Es el modelo a seguir para el resto.

Antes del corte 1 deben completar mucho de lo exigido: redactar las secciones 2 (restricciones clasificadas y justificadas) y 3 (contexto con actores y sistemas externos) del arc42, rellenar la tabla de interesados, escribir de 3 a 5 escenarios en la sección 10 (que quedó vacía), construir el árbol de utilidad con impacto y riesgo, y crear el C4 de contexto con leyenda y flechas etiquetadas (hoy no existe). Revisen también que toda la documentación hable del mismo proyecto (el problema cambió entre semana 1 y semana 2) y que cada integrante aporte al historial con su cuenta.

## Semana 3

Qué está bien: la sección Solution Strategy liga la decisión al escenario de usabilidad con una matriz comparativa contextualizada, el ADR 0001 tiene contexto, alternativas descartadas con criterio de reapertura y consecuencias, y el esqueleto monta los cinco módulos del ADR con su router.

Qué corregir antes del corte 1 (semana 5):
1. El README termina en el encabezado «Esqueleto ejecutable — arranque» sin ningún comando debajo y no hay manifest de dependencias: documenten el comando único y añadan `requirements.txt`.
2. Estructura mínima incompleta: muevan la plantilla suelta a `docs/arc42/` y creen `docs/c4/`.
3. Enlacen el ADR desde `docs/aspectos.md` y desde el escenario que lo motiva; `aspectos.md` sigue sin la tabla de 8 columnas.
4. Completen `docs/ia.md`: falta la columna de qué se rechazó y por qué, y las entradas de S3 quedaron «pendientes de revisión».
5. Sin pipeline ni evidencia del verde para `tests/test_esqueleto.py`: añadan un workflow con el run.
6. Asegúrense de que todos los integrantes contribuyan al historial con su cuenta antes del corte.

## Semana 4 · S4

El repositorio está en la organización, con el nombre correcto y el commit de la semana es anterior al cierre. Sin embargo, la revisión no pudo verificar el contenido de la documentación ni la ejecución de pruebas porque no hay runs de CI ni se aportaron lecturas de los archivos. Suban evidencia concreta: encabezados de arc42, diagramas C4, rutas del corte vertical, comando de arranque y URL del run en verde. Corrijan la ruta de docs/aspectos.md y aseguren que todos los integrantes aparezcan en el historial.

## Semana 5 · CORTE1

El compendio S1-S4 está sólido: documentación, ADR, C4 y corte vertical presentes. Para cerrar el corte: (1) renombra el archivo a correcciones.md exactamente en minúsculas y verifica que su contenido enlace cada hallazgo con evidencia; (2) revisa el pipeline: el run del commit calificado falla, asegura que pytest pase en CI; (3) convierte las celdas de docs/aspectos/aspectos.md en enlaces reales a ADR, código y pruebas; (4) mueve los PDFs fuera de docs/adr y documenta la trazabilidad en la ruta correcta; (5) añade evidencia de SonarCloud si aplica. El proyecto está bien encaminado; estos ajustes son de verificación y consistencia.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

Se revisó de nuevo después del cierre, sobre la etiqueta `corte-1` que ya existe en el repositorio.

Qué está bien: ahora los cuatro integrantes tienen commits propios en el historial, y no hay credenciales expuestas.

Qué falta: la etiqueta `corte-1` quedó puesta sobre un commit de más de 7 horas después del cierre, así que la entrega se considera tardía. Además, subir el proyecto como archivos ZIP por la interfaz web dejó el árbol triplicado (el mismo proyecto repetido dentro de varias carpetas), y después de la etiqueta se siguió reorganizando todo sin resolverlo. Sobre todo: no hay ninguna señal de que se haya trabajado el reto del corte — no hay diagnóstico de una restricción nueva, no hay ADR nuevo, no hay cambio de código, no hay medición, y el pipeline de pruebas nunca se ha ejecutado ni una sola vez en todo el repositorio.

Qué corregir: dejar una sola copia del proyecto en la raíz, mover la etiqueta a un commit dentro del plazo la próxima vez, configurar y correr el pipeline, y sobre todo hacer el ejercicio completo del reto (diagnóstico con cifra, ADR con alternativas, cambio implementado, prueba y medición) antes de la sustentación.

## Semana 1 · S1

Sin actividad S1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 2 · S2

Sin actividad S2: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 3 · S3

Sin actividad S3: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semanas 3 y 4 · revisión excepcional de entregables

Esta revisión sustituye las conclusiones automáticas de S3 y S4 para estos dos avances: se miró únicamente el estado actual de los entregables, sin usar fechas, actividad de commits, etiquetas ni contribuciones como criterio.

En S3, el ADR 0001 está bien estructurado, el esqueleto modular está presente, el README ya documenta el arranque y hay pruebas en verde. Falta una matriz explícita que contraste capas, hexagonal y monolito modular con el árbol de utilidad; además, el escenario de usabilidad debe enlazar directamente el ADR que motiva.

En S4, arc42, el corte vertical de búsqueda, el arranque y las pruebas están documentados. Aún falta un C4 de contexto real: los dos diagramas actuales son de contenedores. Completen también la trazabilidad en la ruta `docs/aspectos.md` con las ocho columnas del curso, incluyendo ID y C4, y mantengan la sección 9 de arc42 enlazada a todos los ADR vigentes.

## Semana 7 · S7

Buen avance: el contrato OpenAPI 3.1 está versionado en docs/api/openapi.yaml con rutas, esquemas, ejemplos y versión declarada, y el ADR 0004 justifica la integración síncrona y asíncrona con las alternativas descartadas y sus consecuencias de acoplamiento. Lo que falta es el núcleo de la semana: una prueba de contrato invocada desde el workflow (schemathesis, dredd, pact o prism) y la evidencia de que esa prueba falla cuando se introduce un cambio incompatible; hoy el pipeline solo ejecuta pytest, así que el contrato no se está verificando. Complementen el C4 nivel 2 etiquetando con protocolo y formato todas las flechas, y la tabla de aspectos con las columnas ID y C4. En la verificación transversal, el análisis estático aún no es auditable: agreguen el paso del scanner en el workflow y referencien la URL pública del análisis con su Quality Gate para el commit revisado; un badge no cuenta como ejecución. Revisen también que la carpeta de ADR solo contenga archivos NNNN-titulo.md. Son correcciones acotadas y elevan directamente la defensa del criterio de dominio e interfaces.
## Semana 6 · S6

La auditoría sobre el código actual está bien hecha: el mapa de contextos, la tabla de dueño único y las violaciones con su plan citan rutas reales y son repetibles. Para cerrar el corte, incrusten el mapa de contextos en la sección 8 de arc42 y añadan el C4 nivel 3 que implica el reajuste de límites. La tabla de aspectos necesita las columnas ID y C4 para que cada fila sea navegable. SonarCloud no queda demostrado: incorporen el paso del scanner al workflow y la URL pública del análisis con su Quality Gate. Verifiquen también que lo afirmado en la evidencia siga siendo cierto tras los cambios posteriores al cierre. Buen trabajo de trazabilidad; el siguiente paso natural es ejecutar el plan de corrección ya redactado.

## Semana 8 · S8 · revisión definitiva

El avance respecto de la revisión preliminar es grande y se nota en las piezas de observabilidad: los logs ya salen como una línea JSON por solicitud con campos con nombre, hay una métrica consultable de búsquedas sin resultados atada explícitamente al escenario de usabilidad, existe una estimación de costo mensual con supuestos y punto de ruptura, y las secciones 2 y 7 del arc42 ya recogen la restricción de costo cero y una vista de despliegue con las piezas y dónde corren. El README explica cómo se arranca y cómo se ejecuta el frontend, y todos los integrantes aparecen contribuyendo en el historial.

Lo que impide cerrar la semana es la infraestructura y el pipeline. El repositorio no contiene ningún archivo de infraestructura versionado —ni Dockerfile, ni `docker-compose`, ni un descriptor de plataforma—, aunque el README y la vista de despliegue los mencionan y el propio registro de IA los da por redactados. Lo mismo pasa con los ADR de plataforma citados: los archivos referenciados no existen en el repositorio, así que no se puede evaluar ninguna decisión de despliegue con su alternativa descartada. Cierren esa brecha: versionen lo que prometen o retiren las referencias; hoy la documentación describe un entorno que el repositorio no contiene.

Segundo punto crítico: el pipeline de la rama principal está en rojo en el estado calificado. La observabilidad y la documentación subieron de nivel, pero un CI fallido bloquea el criterio de pipeline en verde. Revisen el workflow y dejen el commit calificado en verde.

Quedan además desviaciones de estructura: la tabla de aspectos y el registro de IA siguen fuera de las rutas contractuales, y la carpeta de ADR vuelve a contener un PDF ajeno a la convención de nombres. Son ajustes de forma acotados que conviene ordenar antes del próximo corte. Finalmente, SonarCloud sigue sin ser auditable: hay scanner declarado en el workflow, pero sin un run exitoso que lo ejecute para el hash revisado ni una URL pública del análisis con su Quality Gate.

## Semana 9 · S9 (revisión definitiva)

La corrección de frontera está implementada y respaldada por pruebas que documentan el fallo esperado. Completen el eslabón C4 en la fila de aspectos y ratifiquen los ADR propuestos. La auditoría de dependencias es válida aunque no hayan añadido paquetes; atiendan la vulnerabilidad registrada de Next y las referencias a archivos todavía ausentes.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

La muestra sintética de 2≤3 no aporta una línea base operacional. La fachada, la métrica real de búsquedas sin resultados, JSON y request_id dan observabilidad parcial. CI, URL y archivos declarados ausentes impiden el nivel competente. La consolidación reconoce esa observabilidad parcial bajo el alcance de revisión del repositorio.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Documentación de despliegue y prueba de contrato sobrestima el snapshot.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Media · La vista de despliegue afirma artefactos y rutas que este snapshot no contiene:** No permite reproducir desde el repositorio la topología Render/Vercel descrita; dificulta distinguir despliegue real de diseño. No demuestra que un servicio remoto esté caído. **Acción:** Marcar el despliegue como no verificable hasta aportar manifiestos y URL comprobable; corregir ruta a app/frontend y documentar comandos realmente disponibles. La inspección completa de ls-tree no encontró Dockerfile, compose ni render.yaml. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La prueba de contrato anunciada no está implementada en la suite versionada:** Se declara una protección contra incompatibilidades que pytest no aporta: un cambio de esquema puede no ser detectado por las aserciones funcionales parciales. **Acción:** Añadir una prueba que cargue docs/api/openapi.yaml, resuelva referencias y valide respuestas/casos inválidos, más una mutación incompatible; mientras tanto retirar la garantía. Inspeccionados los cinco archivos de tests: ninguno carga OpenAPI/YAML/JSON Schema y test_contrato.py no existe. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Antes del corte, documenten el escenario operativo asignado y su línea base reproducible. La URL de salud respondió 404 y el pipeline de la punta falla: corrijan ambos y aporten el run exitoso. Sincronicen la documentación con los archivos realmente versionados, y midan la respuesta al reto sobre el MVP desplegado.

</details>

## Semana 11 · Integración y resiliencia

La línea base permite identificar la integración de búsqueda, pero no hay entrega nueva de S11 en la rama principal. Faltan tabla de tres fallos, mitigaciones concretas, diseño de idempotencia o inaplicabilidad y evaluación de extracción con criterios, además de actualizar riesgos y aspectos. Las listas genéricas de fallos y el correo previsto no sustituyen ese análisis.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Se reconoce SQLite como almacén propio en C4. Faltan tabla de consistencia, dos operaciones contrastadas, caché e invalidación, garantías concretas para el correo previsto, ADR del mayor costo de reversión y estrategias en arc42. La evaluación sigue siendo un diagnóstico preliminar sobre la línea base disponible.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **10 abiertas, 10 cerradas, 20 en total**. Los 10 cierres figuran como completed. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Campos «URL Vercel» y «URL Render» sin completar.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Se mantiene el corte vertical de búsqueda con SQLite, pero la rama principal no registra cambios desde el 28 de septiembre (Colombia). El README aún contiene marcadores URL Vercel/URL Render, no enlaces desplegados concretos. Las PR #22 y #23 siguen abiertas; no se deben presentar como incorporadas. El último workflow tests.yml sigue fallido. Para S12, elaborar la tabla operación→garantía y contrastar dos operaciones reales; justificar no usar caché o definir invalidación tras modificar documentos/metadatos, y comparar el costo de reversión de las decisiones de datos. Consolidar estas decisiones en arc42 §8 y distinguir correo/outbox previsto de mensajería implementada. Revisar los solapamientos de issues #12/#18 y asignar las cinco abiertas sin responsable.

**Issues:** 10 abiertas y 10 cerradas; 5 abiertas sin responsable. Cierres: 10 completed. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Sin URL concreta. Los campos URL Vercel/URL Render siguen sin completar. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#shareu) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

La rama principal no ha cambiado desde el seguimiento del 22 de octubre. Se mantiene el corte vertical de búsqueda SQLite, las PR #22 y #23 abiertas y el último workflow de pruebas fallido. No atribuir a master cambios que continúan en esas PR. Las diez issues abiertas incluyen cinco sin responsable; el tablero no certifica el estado de implementación.

**Próximos pasos:**
- Completar la tabla operación→garantía y contrastar dos operaciones reales; justificar no caché o definir invalidación de documentos/metadatos.
- Comparar el costo de reversión de decisiones de datos en un ADR y consolidar consistencia/caché en arc42 §8.
- Publicar URL oficial iscoutb.dev, resolver el pipeline y conciliar issues solapadas con evidencia.

**Issues:** 10 abiertas y 10 cerradas; 5 abiertas sin responsable. Cierres: 10 completed. El estado registrado no acredita por sí solo implementación.

**README:** Sin URL concreta. README mantiene placeholders Vercel/Render, no URL pública concreta. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#shareu) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin cambios en master, README, PR ni último CI respecto al corte anterior. #22 y #23 siguen abiertas; no atribuir sus propuestas a master. El último workflow de la punta permanece fallido y diez issues siguen abiertas, cinco sin responsable. README conserva placeholders Vercel/Render.

**Próximos pasos:**
- Resolver pipeline y conciliar issues con evidencia; no contar propuesta de PR como integrada.
- Sustituir placeholders con URL oficial iscoutb.dev.
- Completar garantías por operación, caché/no caché y ADR de reversión.

**Issues GitHub:** 10 abiertas y 10 cerradas; 5 abiertas sin asignar. Cierres: 10 completed. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#shareu) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).
