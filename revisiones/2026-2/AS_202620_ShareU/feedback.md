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

El repositorio presenta la estructura mínima y archivos esperados, pero no fue posible verificar el contenido de la documentación ni la ejecución de pruebas. Se recomienda incluir en la entrega enlaces directos a los archivos relevantes y a los runs de CI para facilitar la revisión. Además, se observa que solo un integrante aparece en el historial; es necesario que todos los miembros contribuyan con commits para cumplir el criterio de autoría.
