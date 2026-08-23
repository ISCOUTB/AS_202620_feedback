# Evidencia S9 · Generación verificada y trazable

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s9` |
| Semana | 9 |
| Corte | Segundo corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Una **porción real del sistema construida con apoyo de IA**, con su cadena completa: la fila de
`docs/aspectos.md`, el ADR con la decisión que tomó **el equipo** y no la herramienta, el enlace
al código, **una prueba que falla ante el defecto que cubre** y la medición del escenario
asociado.

Se añade el extracto de `docs/ia.md` con lo aceptado, lo corregido y lo **rechazado con su
motivo**, y la **auditoría de erosión**: si la generación cruzó un límite de contexto o una regla
de propiedad de datos de la semana 6, cómo se detectó y cómo se corrigió. Más la verificación de
lo que el modelo trajo consigo: que **cada dependencia propuesta exista y sea la legítima**, y que
no haya quedado ninguna credencial en el código ni en los ejemplos.

Si el sistema incorpora o va a incorporar un componente generativo, se suma su conjunto de
evaluación con resultados y la estimación de costo por operación y latencia; si se decidió no
incorporarlo, **el ADR que lo justifica**.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Identifica la porción construida con IA** y comprueba que es real y del sistema, no un
   ejercicio aparte. Cita las rutas del código y los commits.
3. **Recorre la cadena entera** para esa porción: fila de aspectos, ADR, código, prueba y
   medición. Cada eslabón se sigue hasta su destino; anota dónde se rompe.
4. **La decisión es del equipo.** Comprueba que el ADR argumenta con las restricciones del
   proyecto. Un ADR que dice que se eligió lo que propuso la herramienta, sin más, no cumple.
5. **La prueba tiene que fallar ante el defecto que cubre.** Busca la evidencia: un run en rojo,
   una prueba de mutación, o el procedimiento documentado por el equipo. Si no la hay, márcalo
   como No verificado y déjalo de pregunta para la sustentación.
6. **Extracto de `docs/ia.md`.** Con lo aceptado, lo corregido y **al menos una salida rechazada
   con su motivo técnico**. Es la columna que demuestra criterio, y su ausencia es hallazgo.
   ```bash
   git -C "$DIR" log --format='%h %cI' -- docs/ia.md | head
   git -C "$DIR" diff --stat corte-1..HEAD -- docs/ia.md
   ```
7. **Auditoría de erosión.** Comprueba si la generación cruzó los límites de contexto o las reglas
   de propiedad de datos de la semana 6, y qué se hizo. Contrástalo tú mismo sobre el código
   generado.
   ```bash
   git -C "$DIR" grep -nIE '(INSERT INTO|UPDATE |\.save\(|\.create\(|repository\.)' HEAD -- . ':!docs' | head -30
   ```
8. **Dependencias propuestas por el modelo.** Toma las dependencias añadidas en el periodo y
   comprueba que existen en su registro oficial y que el nombre es el legítimo. Los nombres
   inventados por un modelo y registrados después por un tercero son el caso que la semana
   estudia.
   ```bash
   git -C "$DIR" diff corte-1..HEAD -- package.json requirements.txt pyproject.toml pom.xml go.mod Gemfile 2>/dev/null | grep -E '^\+' | head -30
   curl -s "https://registry.npmjs.org/<paquete>" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'),list(d.get('time',{}))[:1])"
   curl -s "https://pypi.org/pypi/<paquete>/json" | python -c "import json,sys;d=json.load(sys.stdin);print(d['info']['name'],d['info']['home_page'])"
   ```
9. **Credenciales en código y en ejemplos.** Repite el barrido del contrato, incluidos los
   archivos de ejemplo y la documentación generada, que es donde suelen quedar.
10. **Componente generativo, si lo hay.** Conjunto de evaluación con resultados, costo por
    operación, latencia, y su aparición en el C4 nivel 2 como contenedor externo con protocolo y
    costo anotados, más el ADR que declara el comportamiento ante fallo o degradación del
    proveedor. **Si el equipo decidió no incorporarlo, exige el ADR que lo justifica**: la
    ausencia de decisión no es lo mismo que la decisión de no hacerlo.

**Qué no hacer aquí:** no juzgar si usaron IA o cuánta, que el curso espera que la usen; no
modelar amenazas del componente generativo, que es la semana 13; no exigir que el componente
generativo exista.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | | |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | | |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | | |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | | |
| Medición del escenario asociado | resultado contrastado con el umbral | | |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | | |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | | |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | | |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | | |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente.

Esta evidencia es la que alimenta el criterio de trazabilidad del segundo corte y la política de
uso de IA del curso: si aparece código generado que el equipo no puede explicar, no es un
hallazgo de forma, y hay que dejarlo escrito para la sustentación.
