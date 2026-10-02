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

## Semana 9 · S9 (revisión preliminar)

Esta revisión es preliminar y no tiene corte todavía: se califica la punta actual de la rama principal y la nota puede cambiar si empujan antes del cierre del 2026-10-05.

El trabajo de esta semana responde exactamente a lo que la evidencia pide. La auditoría de erosión encontró un cruce de frontera real —un módulo importaba un archivo interno de otro— y lo corrigió con una interfaz de servicio pública, acompañada de una prueba que falla si el atajo vuelve a aparecer. Eso convierte una regla que estaba solo escrita en un ADR en una regla que el repositorio hace cumplir. La cadena del aspecto nuevo es navegable de extremo a extremo: aspecto, ADR, código, pruebas y medición. Los dos ADR argumentan la decisión con las restricciones del proyecto —costo cero, sin disco persistente, latencia— y no se limitan a lo que propuso la herramienta. La prueba de mutación está documentada como debe: el defecto introducido, la prueba que falla y el mensaje de fallo.

Hay tres cosas que cerrar. La primera es la más importante: el pipeline de la rama principal está en rojo en el commit revisado, y sin un run en verde no se puede acreditar el análisis estático ni su Quality Gate; además, un CI rojo no permite confirmar desde el repositorio las pruebas que la evidencia da por verdes. La segunda: la evidencia verificó dependencias de semanas anteriores, pero el periodo no añadió ninguna, así que no hay una verificación propia de esta semana. Y la tercera, de forma: la tabla de aspectos y el registro de IA siguen fuera de las rutas contractuales, la carpeta de ADR conserva un PDF ajeno a la convención, y quedan referencias a archivos que no están en el repositorio junto con marcadores sin resolver. Ordenen esas referencias antes del cierre.
