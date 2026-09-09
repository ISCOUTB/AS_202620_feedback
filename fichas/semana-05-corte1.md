# Primer corte · compendio de la línea base arquitectónica

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:corte1` |
| Semana | 5 |
| Corte | Primer corte (actividad de corte) |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio, PDF exigido por el aula y `correcciones.md` en la raíz del repositorio |
| Estado que se califica | último commit de `master` o `main` anterior o igual al cierre |
| Acceso | requiere haber entregado la evidencia S4 |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md) y las fichas de las evidencias S1 a S4. Su
matriz transversal se rellena además de la de esta ficha.

## Qué se evalúa

La **pasada definitiva y completa de la semana 5** es el compendio del primer corte: comprueba que
el proyecto esté al día con lo pedido en S1, S2, S3 y S4 y que las correcciones anunciadas por el
equipo estén realmente aplicadas. No se evalúa una supuesta «restricción nueva asignada» ni un
reto distinto por equipo, salvo que el aula aporte explícitamente ese enunciado y su asignación.

Las notas históricas de S1 a S4 no se reabren. La matriz de S5 sí valora el estado consolidado del
proyecto al cierre: una carencia anterior todavía presente afecta el compendio; una corrección
hecha antes del cierre puede cerrar el hallazgo para S5, con evidencia verificable.

Esta regla especial se aplica **solo a la evaluación definitiva completa de S5**. Las pasadas
tempranas siguen siendo diagnósticos preliminares en delta y no deben cerrar ni rechazar
correcciones de forma definitiva.

## `correcciones.md` en la raíz

En el estado calificado debe existir exactamente `correcciones.md` en la raíz del repositorio.
El nombre mal escrito, una ubicación distinta, otra rama o un archivo añadido después del cierre
no cumplen esta fila.

El archivo debe responder de forma trazable a los hallazgos publicados en S1–S4 y, si existió una
pasada temprana de S5, a sus hallazgos preliminares. Para cada corrección debe indicar:

- hallazgo o fila que responde;
- acción realizada, o motivo técnico para no aplicarla;
- ruta y sección, prueba, commit o run de CI que permite verificarla;
- estado declarado: corregida, parcial, pendiente o rechazada con justificación.

`correcciones.md` es un índice de verificación, no evidencia suficiente por sí solo. Cada
afirmación se contrasta con el archivo, historial, prueba o run citado. Si falta, se marca **No
cumple** únicamente su fila y se continúa revisando el proyecto completo; no se invalida
automáticamente toda la entrega.

## Instrucciones para la revisión definitiva

1. **Fija el estado calificado.** Identifica la rama principal `master` o `main` y toma su último
   commit anterior o igual al cierre. No consultes ni uses etiquetas. Si existen ambas ramas, usa
   la declarada como principal por el remoto y anótala; si no existe ninguna, marca No verificado.
   ```bash
   git -C "$DIR" show-ref --verify refs/remotes/origin/master
   git -C "$DIR" show-ref --verify refs/remotes/origin/main
   git -C "$DIR" log -1 --format='%H %cI %s' --until="$CIERRE_S5" origin/master
   ```
2. **Comprueba `correcciones.md` en la raíz del estado calificado.** No uses la versión de la
   punta actual de la rama si fue añadida después del cierre.
   ```bash
   git -C "$DIR" ls-tree --name-only "$HASH"
   git -C "$DIR" show "$HASH:correcciones.md"
   ```
3. **Recorre las revisiones publicadas S1–S4.** Construye una lista de hallazgos y verifica si
   `correcciones.md` responde a cada uno. No aceptes una autoevaluación genérica de «Cumple».
4. **Contrasta cada corrección.** Abre la ruta citada en el hash calificado, revisa el cambio en el historial
   y busca la prueba o el run de CI correspondiente. Clasifica la respuesta como verificada,
   parcial, pendiente, rechazada con fundamento o no sustentada.
5. **Revisa el compendio S1–S4 en su estado actual.** Aplica las matrices de las cuatro fichas al
   estado calificado, sin copiar sus notas históricas: problema y equipo; atributos de calidad y
   restricciones; estrategia y ADR; arc42, C4 y corte vertical.
6. **Revisa el contrato transversal.** Comprueba estructura, ADR, `docs/ia.md`, secretos,
   contribución y CI de acuerdo con [CONTRATO.md](../CONTRATO.md).
7. **Separa corte y estado actual.** La matriz S5 se decide con el hash calificado. En `overall`,
   revisa la punta actual de la misma rama `master` o `main` para registrar correcciones o
   deterioros posteriores como hallazgo, sin cambiar la nota del corte.
8. **Deja trazabilidad en el informe.** Incluye una tabla específica para `correcciones.md` y cita
   evidencia por cada conclusión. Añade preguntas de sustentación para lo que no pueda verificarse
   desde el repositorio.

## Matriz de cumplimiento S5

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple / No verificado) | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama `master` o `main`, hash y fecha | | |
| `correcciones.md` existe en la raíz del estado calificado | `git show <hash>:correcciones.md` | | |
| Correcciones trazables y contrastadas | cada hallazgo S1–S4 enlazado con evidencia real o justificación técnica | | |
| S1 al día: equipo, problema y repositorio | matriz vigente de `semana-01-evidencia-s1.md` | | |
| S2 al día: escenarios de calidad y restricciones | matriz vigente de `semana-02-evidencia-s2.md` | | |
| S3 al día: estrategia de solución y decisiones | matriz vigente de `semana-03-evidencia-s3.md` | | |
| S4 al día: arc42, C4 y corte vertical | matriz vigente de `semana-04-evidencia-s4.md` | | |
| Corte vertical reproducible y coherente con la arquitectura | README, código, pruebas y correspondencia con C4 | | |
| Pipeline y pruebas respaldan el estado calificado | ruta de pruebas y URL de run asociado al hash o anterior al corte | | |
| Trazabilidad consolidada navegable | aspectos, requisitos, C4, ADR, código, pruebas y evidencias | | |
| PDF u otro adjunto exigido por el aula | documento entregado en Moodle; No verificado si no está disponible | | |
| Sustentación del corte | sesión de sustentación | No verificado | lo resuelve el docente en la sesión |

## Tabla obligatoria de seguimiento de correcciones

| Origen | Hallazgo o fila | Respuesta en `correcciones.md` | Evidencia contrastada | Resultado |
|---|---|---|---|---|
| S1–S4 o preliminar S5 | | | | Verificada / Parcial / Pendiente / Rechazada con fundamento / No sustentada |

## Criterio para la propuesta al docente

La propuesta de S5 debe reflejar el estado consolidado del primer corte y usar la escala o rúbrica
publicada en el aula. No inventes un reto, una restricción ni ponderaciones ausentes. Si la rúbrica
del aula no está disponible, entrega la matriz y deja la nota o nivel como **No verificado** para
que lo resuelva el docente.
