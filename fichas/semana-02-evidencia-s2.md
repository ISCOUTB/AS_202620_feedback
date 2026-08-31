# Evidencia S2 · Escenarios de calidad y restricciones

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s2` |
| Semana | 2 |
| Corte | Primer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

arc42 **secciones 1, 2, 3 y 10** redactadas, **árbol de utilidad**, **3 a 5 escenarios de calidad
con medida**, restricciones justificadas y separadas de los requisitos, y el **C4 de contexto**
(nivel 1). Cada escenario se enlaza desde la fila correspondiente de `docs/aspectos.md`.

Un escenario de calidad tiene seis partes: fuente, estímulo, artefacto, entorno, respuesta y
**medida de respuesta numérica**. «El sistema debe ser rápido» no es un escenario.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Secciones 1, 2, 3 y 10 redactadas y sin texto de plantilla.**
   ```bash
   ls docs/arc42/
   grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template' docs/arc42/ | head -20
   ```
3. **Objetivos con interesado.** La sección 1 declara objetivos de negocio, no funcionalidades, y
   dice a quién le importa cada uno.
4. **Restricciones separadas de requisitos y justificadas.** La sección 2 clasifica técnicas,
   organizativas y legales, y dice de dónde viene cada una. Si una restricción es en realidad un
   requisito funcional, anótalo.
5. **Contexto coherente con el diagrama.** La sección 3 identifica actores y sistemas externos, y
   tiene que corresponder con el C4 de contexto: mismos actores, mismos sistemas.
6. **Escenarios de calidad.** Cuenta cuántos hay y comprueba las **seis partes** en cada uno,
   sobre todo la medida: cifra con unidad y condición de carga. Sin medida, el escenario cuenta
   como enunciado.
   ```bash
   grep -rniE 'fuente|estimulo|estímulo|artefacto|entorno|respuesta|medida' docs/arc42/ | head -30
   ```
7. **Árbol de utilidad.** Prioriza por impacto y riesgo, no es una lista plana de atributos.
   Comprueba que los escenarios priorizados son los mismos que están redactados.
8. **C4 de contexto.** El sistema, sus usuarios y los sistemas externos, con leyenda y flechas
   etiquetadas. Anota si está como código o solo como imagen, y en qué ruta está guardado.
9. **Enlace desde la tabla de aspectos.** Cada escenario debe alcanzarse desde la fila de su
   aspecto en `docs/aspectos.md`. Sigue dos filas al azar hasta el escenario.

**Qué no hacer aquí:** no exigir secciones 4 a 12, ADR, código ni C4 de contenedores; no exigir
mediciones ejecutadas, que llegan más adelante.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| arc42 sección 1 con objetivos de negocio y su interesado | `docs/arc42/01*` con objetivos, no funcionalidades | | |
| arc42 sección 2 con restricciones clasificadas y justificadas | `docs/arc42/02*` con técnicas, organizativas y legales | | |
| Restricciones separadas de los requisitos | comparación entre la sección 2 y los requisitos declarados | | |
| arc42 sección 3 con actores y sistemas externos | `docs/arc42/03*` coherente con el diagrama de contexto | | |
| Entre 3 y 5 escenarios de calidad redactados | `docs/arc42/10*` con los escenarios numerados | | |
| Cada escenario con sus seis partes y medida numérica | cita de un escenario completo, con su cifra y unidad | | |
| Árbol de utilidad que prioriza por impacto y riesgo | tabla o diagrama del árbol, con la priorización visible | | |
| C4 de contexto con leyenda y flechas etiquetadas | archivo del diagrama, con su ruta | | |
| Escenarios alcanzables desde la fila de su aspecto | dos filas de `docs/aspectos.md` seguidas hasta el escenario | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. La nota sugerida, `1 + 4 × (n/m)` sobre esta
matriz, se publica como propuesta al docente (decisión del profesor): la nota final la fija el
profesor en Moodle.

Deja anotado, para el primer corte: cuántos escenarios tienen medida comprobable y si alguno
declara ya **cómo** se medirá, con herramienta, carga y umbral. Es lo que separa el nivel
competente del sobresaliente en el criterio de diagnóstico.
