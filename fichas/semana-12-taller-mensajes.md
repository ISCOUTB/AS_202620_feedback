# Taller aplicado · Mensajes y consistencia

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:taller-mensajes` |
| Semana | 12 |
| Corte | Tercer corte |
| Tipo | grupal, calificado una sola vez |
| Qué sube el estudiante | enlace al commit, contrato, pruebas, evidencia de ejecución, ADR y una nota con los límites del experimento |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Seleccionar **una operación real del proyecto** donde haya desacoplamiento temporal, reintento o
procesamiento en segundo plano. Si ninguna lo justifica, construir un **prototipo mínimo aislado**
y registrar la decisión de no incorporarlo al sistema.

El taller debe demostrar siete cosas:

1. Contrato del mensaje y criterio de compatibilidad.
2. Garantía de entrega elegida y consecuencias asumidas.
3. Manejo de duplicados mediante idempotencia o deduplicación.
4. Política de reintentos, espera creciente y cola de mensajes fallidos o mecanismo equivalente.
5. Prueba automatizada de al menos **un duplicado** y **un fallo recuperable**.
6. Métrica o log que permita seguir un mensaje de productor a consumidor.
7. ADR que compare la solución con una alternativa síncrona.

La tecnología la elige el equipo. **No se califica la marca ni la cantidad de contenedores**, y no
se exige un proyecto paralelo ni un vídeo.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Identifica la operación elegida** y comprueba que es real y del proyecto. Si es un prototipo
   aislado, exige la decisión registrada de no incorporarlo, que la consigna pide expresamente.
3. **Contrato del mensaje.** Estructura del mensaje y criterio de compatibilidad: qué cambio se
   considera compatible y cuál no. Cita el archivo.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -iE 'event|message|schema|avro|asyncapi' | head -20
   ```
4. **Garantía de entrega y consecuencias.** Al menos una vez, como máximo una vez o exactamente
   una vez, con lo que el equipo asume al elegirla. La consecuencia asumida es la parte que suele
   faltar.
5. **Duplicados.** Idempotencia o deduplicación implementada, con la clave que la sostiene. Cita
   la ruta.
   ```bash
   git -C "$DIR" grep -nIE '(idempoten|dedup|message_id|correlation)' HEAD -- . ':!docs' | head -20
   ```
6. **Reintentos y cola de fallidos.** Política declarada e implementada: cuántos intentos, con qué
   espera y a dónde va lo que no se pudo procesar.
   ```bash
   git -C "$DIR" grep -nIE '(retry|backoff|dead.?letter|dlq|requeue)' HEAD -- . ':!docs' | head -20
   ```
7. **Las dos pruebas.** Una que ejercite un **duplicado** y otra un **fallo recuperable**.
   Compruébalas por nombre y contenido, y localiza el run que las ejecutó.
   ```bash
   git -C "$DIR" grep -rniE 'duplicad|duplicate|retry|redelivery' HEAD -- '*test*' | head -20
   ```
8. **Trazabilidad del mensaje.** Métrica o log que permita seguir un mensaje de productor a
   consumidor: identificador de correlación, o traza. Cita el ejemplo.
9. **ADR contra la alternativa síncrona.** Comprueba que compara de verdad, con el trade-off de
   acoplamiento y latencia, y no solo describe la solución elegida.
10. **Nota de límites del experimento.** Qué no cubre el montaje y qué haría falta en producción.

**Qué no hacer aquí:** no exigir una tecnología concreta ni penalizar un simulador local, que la
consigna admite; no contar contenedores; no exigir que el flujo esté en producción.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Operación real del proyecto, o prototipo con la decisión registrada de no incorporarlo | operación citada, o ADR o nota de la decisión | | |
| Contrato del mensaje con criterio de compatibilidad | archivo del contrato o esquema | | |
| Garantía de entrega elegida y consecuencias asumidas | apartado con la garantía y lo que implica | | |
| Idempotencia o deduplicación implementada, con su clave | ruta del código | | |
| Política de reintentos con espera creciente | ruta del código o configuración | | |
| Cola de mensajes fallidos o mecanismo equivalente | ruta del código o configuración | | |
| Prueba automatizada de un duplicado | ruta de la prueba y URL del run | | |
| Prueba automatizada de un fallo recuperable | ruta de la prueba y URL del run | | |
| Métrica o log que permite seguir un mensaje de productor a consumidor | ejemplo de línea con identificador de correlación | | |
| ADR que compara con la alternativa síncrona | `docs/adr/NNNN-*.md` con el trade-off | | |
| Nota con los límites del experimento | apartado citado | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

El taller **no tiene rúbrica publicada**: se califica con calificación directa sobre la escala UTB
y la nota la fija el docente.

Si las dos pruebas no existen, dilo con precisión: son la única evidencia de que las propiedades
declaradas (no duplicar, recuperarse) se cumplen de verdad, y sin ellas el resto del taller es una
descripción.
