# Taller aplicado de despliegue

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:taller-docker` |
| Semana | 8 |
| Corte | Segundo corte |
| Tipo | grupal, calificado una sola vez |
| Qué sube el estudiante | la comparación con sus supuestos, el prototipo o plan reproducible, y el ADR |
| Estado que se califica | commit vigente al cierre de la actividad |

La clave `taller-docker` es el `idnumber` con el que Moodle localiza la actividad y **no se
renombra**, aunque el taller no vaya de Docker.

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

A partir de la **condición operativa asignada** al equipo (límite de costo, necesidad de
reversión, patrón de carga o tiempo de recuperación), comparar **dos alternativas de despliegue
para una pieza concreta y nombrada** del sistema: el sitio, la API, la base de datos, los
ficheros o los trabajos programados. **No para el sistema entero.**

Condiciones explícitas de la consigna:

- **Al menos una de las dos alternativas debe poder usarse sin tarjeta**; el servidor del
  laboratorio siempre cumple.
- Si una de las dos es una función, hay que contrastar su **arranque en frío medido** con el p95
  del escenario de esa pieza.
- Se incluyen supuestos, prototipo o plan reproducible, estimación de costo con el punto en que
  se rompe la capa gratuita, procedimiento de reversión y un ADR que justifique la elección.
- **Las capturas de un tutorial no constituyen evidencia suficiente.**

Esta nota corresponde al análisis comparativo. La operación del sistema real la califica la
evidencia S8, y son dos cosas distintas.

## Instrucciones para el agente de revisión

1. **Consigue la condición operativa asignada al equipo** antes de leer nada: sin ella no se puede
   juzgar si la comparación responde a lo que se pidió.
2. **Comprueba que la pieza está nombrada.** Una comparación sobre «el sistema» incumple la
   consigna aunque esté bien hecha. Cita la frase donde el equipo nombra la pieza.
3. **Dos alternativas, no una.** Comprueba que ambas se describen con el mismo nivel de detalle y
   que la descartada tiene un motivo técnico, no una preferencia.
4. **Alternativa sin tarjeta.** Al menos una debe poder usarse sin tarjeta, y el equipo debe
   decir cuál y cómo lo verificó. Si las dos exigen tarjeta, es No cumple, y la política de costos
   del curso obliga a ofrecer alternativa al equipo.
5. **Arranque en frío frente al p95**, solo si una alternativa es una función. Comprueba que hay
   **medida**, no estimación de manual, y que se contrasta con el p95 del escenario de esa pieza.
6. **Supuestos declarados.** Volumen, concurrencia, tamaño de datos y frecuencia. Sin supuestos,
   la estimación de costo no se puede juzgar.
7. **Prototipo o plan reproducible.** Un prototipo con su configuración versionada, o un plan que
   otra persona pueda ejecutar paso a paso. Cita las rutas.
   ```bash
   git -C "$DIR" log --format='%h %cI %s' --since="$INICIO_SEMANA_8" HEAD | head -20
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -iE 'taller|deploy|infra|\.tf$|docker-compose' | head -20
   ```
8. **Estimación de costo con punto de ruptura.** Cuánto cuesta cada alternativa al volumen
   supuesto y **en qué punto se rompe la capa gratuita**. Sin el punto de ruptura, la comparación
   no decide nada.
9. **Procedimiento de reversión.** Qué se hace si la alternativa elegida falla o se encarece.
   Tiene que ser accionable, no una intención.
10. **ADR de la elección.** Con contexto, las dos opciones, la decisión y las consecuencias, y
    ligado a la condición operativa asignada.
11. **Descarta el tutorial.** Si la evidencia son capturas de una guía del proveedor sin datos del
    proyecto, marca No cumple en la fila de evidencia y dilo con esas palabras: la consigna lo
    excluye expresamente.

**Qué no hacer aquí:** no evaluar el despliegue real del sistema, que es la evidencia S8; no
exigir que la alternativa elegida esté implementada; no penalizar la elección del proveedor, sino
la calidad del criterio.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| La comparación responde a la condición operativa asignada | condición citada y respuesta correspondiente | | |
| Pieza concreta y nombrada, no el sistema entero | frase donde se nombra la pieza | | |
| Dos alternativas descritas con el mismo detalle | apartados de ambas alternativas | | |
| Al menos una alternativa utilizable sin tarjeta, verificada | declaración del equipo y cómo lo comprobó | | |
| Arranque en frío medido frente al p95 del escenario, si hay función | medición con procedimiento | | |
| Supuestos declarados: volumen, concurrencia, datos, frecuencia | apartado de supuestos | | |
| Prototipo o plan reproducible versionado | rutas de configuración o pasos ejecutables | | |
| Estimación de costo con el punto de ruptura de la capa gratuita | cálculo con el umbral | | |
| Procedimiento de reversión accionable | apartado de reversión | | |
| ADR que justifica la elección, ligado a la condición asignada | `docs/adr/NNNN-*.md` | | |
| La evidencia es del proyecto, no capturas de un tutorial | artefactos citados con su ruta | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

El taller **no tiene rúbrica publicada**: se califica con calificación directa sobre la escala UTB
y la nota la fija el docente.

Si el equipo declara que necesita el servidor del laboratorio, comprueba que quedó registrado en
la consulta de disponibilidad técnica de la semana 1: la promesa de que ninguna cuenta personal
de pago es obligatoria solo se puede cumplir si se sabe a quién hay que darle la alternativa.
