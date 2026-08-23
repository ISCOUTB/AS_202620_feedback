# Primer corte · reto de línea base arquitectónica

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:corte1` |
| Semana | 5 |
| Corte | Primer corte (actividad de corte) |
| Tipo | grupal, nota única del equipo, con rúbrica de 5 criterios |
| Qué sube el estudiante | enlace al repositorio en el commit etiquetado `corte-1` y un PDF de dos páginas |
| Estado que se califica | la etiqueta `corte-1` |
| Acceso | requiere haber entregado la evidencia S4 |

Antes de empezar, lee [CONTRATO.md](CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

El equipo responde a **una restricción nueva asignada** según su proyecto: diagnostica su
impacto, compara alternativas, registra la decisión, implementa el cambio sobre el corte vertical
y aporta pruebas y mediciones. El PDF de dos páginas recoge diagnóstico, decisión, cambio
aplicado, medición y enlaces de trazabilidad.

Dos reglas que cambian lo que hay que mirar:

- **Las evidencias S1 a S4 son línea base y no se vuelven a calificar por existir.** Si un
  artefacto anterior se deterioró, eso afecta a la coherencia del sistema, pero su nota ya está
  puesta. Lo que se califica aquí es la respuesta al reto.
- **La sustentación es el quinto criterio de la rúbrica** y no se puede verificar desde el
  repositorio: se resuelve en la sesión, con nota única del equipo.

Antes de revisar, consigue **cuál fue la restricción asignada a ese equipo**: sin ella no se
puede juzgar si el diagnóstico localiza lo que debía.

## Instrucciones para el agente de revisión

1. **Sitúate en la etiqueta.** Comprueba que existe y que apunta a un commit anterior al cierre.
   Si no existe, revisa el último commit anterior al cierre y regístralo.
   ```bash
   git -C "$DIR" tag --list
   git -C "$DIR" log -1 --format='%H %cI %s' corte-1
   git -C "$DIR" checkout corte-1
   ```
2. **Localiza la respuesta al reto en el historial.** Acota los commits entre la evidencia S4 y la
   etiqueta: ahí está lo que se califica.
   ```bash
   git -C "$DIR" log --format='%h %cI %an %s' --since="$INICIO_SEMANA_5" corte-1
   ```
3. **Diagnóstico.** Busca dónde el equipo declara qué parte del sistema y qué escenario de
   calidad afecta la restricción, y con qué **estado inicial medido**. Puede estar en el PDF, en
   arc42 sección 11 o en el propio ADR. Comprueba que la línea base sea verificable: una cifra
   con su procedimiento, no una afirmación.
4. **Alternativas y decisión.** Abre el ADR del reto y comprueba que registra alternativas,
   fuerzas, decisión y consecuencias, y que la liga al escenario de calidad. Un ADR que solo
   enuncia lo elegido cubre el nivel básico, no el competente.
   ```bash
   ls docs/adr/
   git -C "$DIR" log --format='%h %cI %s' --diff-filter=A -- docs/adr/    # cuándo apareció cada ADR
   ```
5. **Cambio aplicado.** Sigue el ADR hasta el commit que lo implementa y comprueba que el cambio
   funciona de extremo a extremo y que el arranque sigue siendo reproducible con el comando del
   README. Verifica que los límites declarados en el C4 se conservan tras el cambio.
6. **Pruebas.** Localiza la prueba que cubre el cambio y comprueba que el pipeline la ejecutó en
   verde en un run anterior a la etiqueta.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=30" \
     | python -c "import json,sys;[print(r['created_at'],r['head_sha'][:8],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   ```
7. **Medición contra umbral.** Comprueba que hay resultado contrastado con el umbral del escenario
   y que la evidencia permite **reproducir** la medición: herramienta, carga y procedimiento. Una
   captura sin procedimiento no es reproducible.
8. **Cadena de trazabilidad.** Recorre la fila de `docs/aspectos.md` del aspecto tocado por el
   reto, de punta a punta, comprobando cada celda. Cita dónde se rompe si se rompe.
9. **Registro de IA.** Comprueba que `docs/ia.md` incluye al menos una salida **aceptada,
   corregida o rechazada** con su motivo técnico, referida al trabajo de este corte.
10. **Prepara la sustentación.** Deja escritas dos o tres preguntas concretas para el equipo,
    salidas de lo que encontraste: un tramo sin prueba, una alternativa descartada sin motivo, una
    medición no reproducible. El criterio 5 se califica en la sesión.

**Qué no hacer aquí:** no recalificar arc42, C4 ni el corte vertical por existir, que es lo que
midieron S2 a S4; no exigir despliegue en línea, que empieza en el segundo corte; no puntuar la
sustentación desde el repositorio.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' corte-1` | | |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | documento adjunto en la entrega de Moodle | | |
| Impacto de la restricción localizado en requisitos, C4 y código | apartado de diagnóstico citando elemento y escenario afectados | | |
| Línea base medida y verificable antes del cambio | cifra con herramienta y procedimiento | | |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/NNNN-*.md` ligado al escenario de calidad | | |
| Cambio implementado y ejecutable de extremo a extremo | commit que implementa el ADR y comando de arranque del README | | |
| Límites declarados conservados tras el cambio | correspondencia del C4 con la estructura del código | | |
| Prueba que cubre el cambio, en verde en el pipeline | ruta de la prueba y URL del run anterior a la etiqueta | | |
| Resultado contrastado con el umbral del escenario y reproducible | medición con herramienta, carga y procedimiento | | |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | fila de `docs/aspectos.md` recorrida celda a celda | | |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | entrada de `docs/ia.md` de este corte | | |
| Sustentación del reto | sesión de sustentación, no verificable desde el repositorio | No verificado | lo resuelve el docente en la sesión |

## Nivel de rúbrica sugerido

Rúbrica desplegada en el aula, cinco criterios de máximo 1,00 cada uno. Los niveles puntúan
0,00 · 0,60 · 0,80 · 1,00 y la suma **es** la nota en la escala UTB. Esto es una **propuesta al
docente**, no una nota aplicada.

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | | | |
| Alternativas y decisión | | | |
| Aplicación sobre el corte vertical | | | |
| Pruebas, medición y trazabilidad | | | |
| Sustentación del reto | lo fija el docente | | |
| **Total** | | **/ 5,00** | |

Anclas rápidas, tomadas de la rúbrica del aula:

- **Diagnóstico.** Básico si describe el reto sin evidencia del estado inicial; competente si
  localiza el impacto en requisitos, C4 y código con línea base verificable; sobresaliente si
  además distingue síntomas, causas y supuestos y prioriza el riesgo con evidencia del proyecto.
- **Alternativas y decisión.** Básico si compara dos alternativas en general; competente si el
  ADR registra alternativas, fuerzas, decisión y consecuencias ligadas al escenario;
  sobresaliente si además declara qué dato haría revisar la decisión y qué costo de reversión
  acepta.
- **Aplicación.** Básico si la implementación es parcial o exige pasos no documentados;
  competente si funciona de extremo a extremo, arranca de forma reproducible y conserva los
  límites declarados; sobresaliente si además degrada de forma controlada ante una condición
  adversa pertinente.
- **Pruebas, medición y trazabilidad.** Básico si hay prueba funcional que no demuestra el
  escenario; competente si la cadena completa es navegable y contrasta el resultado con un
  umbral; sobresaliente si además la evidencia permite reproducir la medición y muestra una
  salida de IA aceptada, corregida o rechazada con justificación técnica.
- **Sustentación.** Se califica en la sesión: competente exige que todos intervengan y justifiquen
  trade-offs, límites y consecuencias sobre su sistema.
