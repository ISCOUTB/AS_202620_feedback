# Evidencia S14 · Medición de atributos de calidad

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s14` |
| Semana | 14 |
| Corte | Tercer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**Resultado de la medición contrastado con el umbral del escenario**, y la incorporación a la
**sección 11 de arc42** de lo que señaló la revisión de los pares, **aunque el equipo no vaya a
corregirlo**: distinguir lo que se conoce y se asume de lo que se ignora es parte de lo que se
evalúa.

La revisión entre pares de esta semana es una actividad **individual** con su propia nota
(`arqsw:workshop-pares`) y no se revisa aquí: lo que llega a esta evidencia es qué hizo el equipo
con lo que le dijeron.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Identifica el escenario medido y su umbral**, tal como estaba declarado en arc42 sección 10.
   La medición se juzga contra ese umbral, no contra uno nuevo inventado después. Si el umbral
   cambió, tiene que haber ADR o nota que lo explique.
3. **Procedimiento de medición.** Herramienta, carga, entorno y número de repeticiones. Sin
   procedimiento, el resultado no es reproducible y así se anota.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -iE 'bench|load|k6|jmeter|locust|gatling|perf|medicion|medición' | head -20
   ```
4. **Resultado contrastado.** El número obtenido frente al umbral, con la conclusión: cumple, no
   cumple, o cumple bajo qué condiciones. Un resultado sin conclusión deja la evidencia a medias.
5. **Entorno de la medición.** Comprueba si midieron sobre el entorno desplegado o en local, y que
   lo digan. Medir en local un escenario de latencia del sistema desplegado cambia el significado
   del número.
6. **Incorporación de la revisión entre pares.** La sección 11 de arc42 debe recoger lo que
   señalaron los pares, con su estado: corregido, asumido o pendiente. Comprueba el cambio en el
   historial.
   ```bash
   git -C "$DIR" log --format='%h %cI %s' -- docs/arc42/11* | head
   git -C "$DIR" diff --stat corte-2..HEAD -- docs/arc42
   ```
7. **Coherencia con la tabla de aspectos.** La columna de evidencia del aspecto medido debe
   apuntar a esta medición.

**Qué no hacer aquí:** no calificar la revisión que hizo el estudiante sobre otros equipos, que es
la actividad individual; no exigir que el sistema cumpla el umbral, que un resultado negativo bien
medido y bien interpretado es evidencia válida.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Escenario medido identificado, con el umbral declarado en arc42 sección 10 | escenario citado y su umbral | | |
| Procedimiento de medición con herramienta, carga y repeticiones | script o apartado del procedimiento | | |
| Medición reproducible por otra persona | artefactos versionados de la medición | | |
| Resultado contrastado con el umbral, con conclusión explícita | cifra obtenida frente al umbral | | |
| Entorno de la medición declarado | apartado que dice si fue local o desplegado | | |
| arc42 sección 11 con lo señalado por los pares | `docs/arc42/11*` y su historial | | |
| Estado de cada señalamiento: corregido, asumido o pendiente | columna o apartado de estado | | |
| Columna de evidencia del aspecto medido, apuntando a esta medición | fila de `docs/aspectos.md` | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente.

Esta es la última evidencia antes del proyecto final. Deja una lista corta de lo que el equipo
tiene que cerrar antes de etiquetar `final`: arc42 completo con glosario, C4 de los tres niveles y
la tabla de aspectos recorrible de punta a punta para **todos** los aspectos declarados.
