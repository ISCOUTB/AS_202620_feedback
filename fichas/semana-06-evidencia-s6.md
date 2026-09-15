# Evidencia S6 · Contextos delimitados y propiedad de datos

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s6` |
| Semana | 6 |
| Corte | Segundo corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**Mapa de contextos**, **tabla módulo a datos con dueño único**, y **lista de no conformidades
detectadas en el código actual con su plan de corrección**.

El recordatorio de la semana añade que la sección 8 de arc42 (conceptos transversales) recoja el
lenguaje ubicuo y el mapa de contextos, y que si los límites cambian respecto al primer corte se
actualice el **C4 nivel 3** y se escriba un ADR explicando el reajuste.

La clave de esta evidencia es que la auditoría se hace **sobre el código actual**, no sobre el
diseño ideal: una lista vacía de no conformidades solo vale si el recorrido que la produjo está
documentado.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Mapa de contextos.** Comprueba que nombra los contextos del dominio propio y el tipo de
   relación entre ellos, con el vocabulario de la semana: núcleo compartido, cliente y proveedor,
   capa anticorrupción. Un diagrama de módulos técnicos (interfaz, servicios, datos) no es un mapa
   de contextos.
3. **Tabla módulo a datos.** Cada entidad o tabla con **un solo dueño**. Comprueba que la tabla
   cubre las entidades que existen de verdad en el código.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -iE 'migrat|schema|models?/|entit|\.sql$' | head -30
   ```
4. **Contrasta la tabla con el código.** Busca no conformidades de propiedad: escrituras a la
   misma entidad desde módulos distintos, o una escritura desde un módulo que no es su dueño.
   Cita rutas concretas.
   ```bash
   git -C "$DIR" grep -nIE '(INSERT INTO|UPDATE |\.save\(|\.create\(|\.update\(|repository\.)' HEAD -- . ':!docs' | head -40
   ```
5. **Lista de no conformidades con plan de corrección.** Cada no conformidad identifica la
   entidad, el módulo dueño esperado, la ubicación observada y la acción de corrección. Si el
   equipo declara que no hay ninguna, comprueba que documenta cómo lo verificó, y contrasta con
   lo que encontraste en el paso anterior.
6. **arc42 sección 8.** Lenguaje ubicuo con términos del dominio y el mapa de contextos
   incorporado.
7. **Coherencia con el corte anterior.** Si los límites cambiaron respecto al primer corte, tiene
   que haber C4 nivel 3 actualizado y un ADR del reajuste. Compara con el hash de `master` o
   `main` citado en la revisión definitiva de S5.
   ```bash
   git -C "$DIR" diff --stat <HASH_S5>..<HASH_ACTUAL> -- docs/c4 docs/arc42 docs/adr
   ```
8. **Correspondencia con la tabla de aspectos.** Los contextos que aparecen en el mapa deben poder
   relacionarse con las filas de `docs/aspectos.md`; anota los aspectos que quedan sin contexto.
9. **SonarCloud público.** Aplica la comprobación transversal del contrato: localiza el scanner
   en el workflow, un run exitoso para la rama o hash revisados y la URL pública del análisis con
   su *Quality Gate*. Si alguno falta o el gate falla, reporta la no conformidad con la evidencia
   esperada y no encontrada.

### Cómo reportar una ausencia o no conformidad

Para cada fila que no cumpla, o para cada resultado de auditoría que concluya que no se halló una
no conformidad, el informe debe dejar explícitos:

- **Qué se esperaba encontrar:** por ejemplo, la entidad `Reserva` con un solo módulo dueño, una
  ruta de escritura, o una entrada en la tabla módulo a datos.
- **Dónde y cómo se buscó:** hash revisado, rutas, patrón de búsqueda o recorrido de código.
- **Qué no se encontró o qué difiere de lo esperado:** la evidencia ausente, la segunda escritura,
  el dueño no declarado o la fila incompleta.

No basta escribir «sin no conformidades»: hay que dejar el alcance de la comprobación para que el
resultado pueda repetirse.

**Qué no hacer aquí:** no exigir extracción de servicios ni microservicios, que se deciden en la
semana 11; no penalizar que el mapa cambie respecto al primer corte, que es justamente lo que se
espera cuando se aprende el dominio, siempre que quede el ADR.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | diagrama o tabla con contextos y tipo de relación | | |
| Tabla módulo a datos con dueño único por entidad | tabla citada, contrastada con el esquema real | | |
| La tabla cubre las entidades que existen en el código | migraciones, modelos o esquema del repositorio | | |
| No conformidades de propiedad de datos detectadas sobre el código actual | lista con entidad, módulo dueño esperado y ubicación observada | | |
| Plan de corrección por no conformidad | acción concreta asociada a cada una | | |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | `docs/arc42/08*` | | |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | diferencia contra el hash revisado en S5, con el ADR del reajuste | | |
| Aspectos relacionables con los contextos del mapa | filas de `docs/aspectos.md` frente al mapa | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. La nota sugerida, `1 + 4 × (n/m)` sobre esta
matriz, se publica como propuesta al docente (decisión del profesor): la nota final la fija el
profesor en Moodle.

Anota para el segundo corte, criterio de arquitectura de dominio: si hay dos módulos escribiendo
la misma entidad y el equipo no lo reporta como no conformidad, es el punto que más pesa en la
sustentación.
