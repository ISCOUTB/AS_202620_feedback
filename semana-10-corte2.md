# Segundo corte · reto aplicado sobre el MVP

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:corte2` |
| Semana | 10 |
| Corte | Segundo corte (actividad de corte) |
| Tipo | grupal, nota única del equipo, con rúbrica de 5 criterios |
| Qué sube el estudiante | enlace al repositorio en el commit etiquetado `corte-2`, la URL del despliegue y un PDF de dos páginas |
| Estado que se califica | la etiqueta `corte-2` y el despliegue en el momento de la revisión |
| Acceso | requiere el primer corte |

Antes de empezar, lee [CONTRATO.md](CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Responder al **escenario operativo asignado** sobre el MVP desplegado: declarar hipótesis y línea
base, justificar la decisión, implementar o configurar la respuesta, ejecutar el experimento y
contrastar el resultado con el umbral. El PDF de dos páginas recoge el resultado del experimento.

S6 a S9, el taller y el cuestionario **no se vuelven a calificar por existir**. La sustentación es
el quinto criterio, se hace **sobre el entorno desplegado y no sobre capturas**, y exige ejecutar
el pipeline en vivo.

Consigue **cuál fue el escenario operativo asignado a ese equipo** antes de revisar.

## Instrucciones para el agente de revisión

1. **Sitúate en la etiqueta `corte-2`** y comprueba que apunta a un commit anterior al cierre. Sin
   etiqueta, revisa el último commit anterior al cierre y regístralo.
   ```bash
   git -C "$DIR" log -1 --format='%H %cI %s' corte-2 && git -C "$DIR" checkout corte-2
   ```
2. **Comprueba el despliegue en ese momento**, con la hora anotada. Prueba el flujo principal y el
   health check.
   ```bash
   curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s\n' "$URL"
   ```
3. **Caracterización del escenario.** Hipótesis, montaje, variables, umbral y **estado inicial
   medido**. Comprueba que la línea base es reproducible: herramienta, carga y procedimiento.
4. **Decisión e implementación.** Localiza el cambio y el ADR que lo registra, y comprueba que la
   decisión es coherente con dominio, contratos, despliegue y costo. Si el equipo decidió **no
   cambiar**, exige la demostración de que es la mejor decisión, que la rúbrica admite.
   ```bash
   git -C "$DIR" log --format='%h %cI %an %s' corte-1..corte-2 | head -40
   git -C "$DIR" diff --stat corte-1..corte-2 -- docs/adr docs/arc42 docs/c4
   ```
5. **Ejecución del experimento.** Resultado contrastado con el umbral, con evidencia que permita
   repetirlo. Comprueba si el equipo controla factores de confusión y declara los límites de
   validez, que es lo que distingue el nivel sobresaliente.
6. **Operación y observabilidad.** Pipeline, health check, logs estructurados y **métrica ligada
   al escenario** que permita verificar la respuesta. Comprueba si hay alerta, correlación de
   peticiones o análisis de dependencias, que suben el nivel.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=20" \
     | python -c "import json,sys;[print(r['created_at'],r['name'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   grep -rniE 'sonar|snyk|dependabot|trivy|osv|pip-audit|npm audit' .github/workflows/ | head
   ```
7. **Secretos.** Repite el barrido del contrato. El criterio de operación baja a insuficiente si el
   escenario no se puede observar **o si expone secretos**.
8. **Evolución trazable.** C4, arc42, ADR y contratos representan el MVP, y el cambio enlaza con
   pruebas y mediciones. Comprueba si alguna decisión anterior queda confirmada o **reemplazada**
   explícitamente a partir de la evidencia.
   ```bash
   grep -rniE 'superseded|reemplaza|reemplazado por' docs/adr/ | head
   ```
9. **Prepara la sustentación.** Deja tres preguntas concretas: una sobre un modo de fallo, una
   sobre costo y una sobre qué harían distinto a la luz de lo medido.

**Qué no hacer aquí:** no recalificar S6 a S9 ni el taller por existir; no puntuar la sustentación
desde el repositorio; no dar por bueno un experimento sin línea base, por bien redactado que esté.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Etiqueta `corte-2` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' corte-2` | | |
| Despliegue accesible en el momento de la revisión | código de respuesta, tiempo y hora de la comprobación | | |
| PDF de dos páginas con el resultado del experimento | documento adjunto en la entrega de Moodle | | |
| Hipótesis, montaje, variables y umbral declarados | apartado de caracterización del escenario | | |
| Línea base medida y reproducible | cifra con herramienta, carga y procedimiento | | |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | `docs/adr/NNNN-*.md` del periodo | | |
| Respuesta implementada o configurada sobre el MVP | commits entre `corte-1` y `corte-2` | | |
| Resultado contrastado con el umbral | medición final frente a la línea base | | |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | URL del run, ruta del health check, configuración de logs | | |
| Secretos protegidos | barrido del contrato sin coincidencias | | |
| C4, arc42, ADR y contratos correspondientes al MVP | diferencia documental entre `corte-1` y `corte-2` | | |
| Decisión anterior confirmada o reemplazada con evidencia | ADR marcado como reemplazado, con enlace | | |
| Sustentación del reto sobre el entorno desplegado | sesión de sustentación, no verificable desde el repositorio | No verificado | lo resuelve el docente en la sesión |

## Nivel de rúbrica sugerido

Rúbrica desplegada en el aula, cinco criterios de máximo 1,00 cada uno. Los niveles puntúan
0,00 · 0,60 · 0,80 · 1,00 y la suma **es** la nota en la escala UTB. Es una **propuesta al
docente**, no una nota aplicada.

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Caracterización del escenario operativo | | | |
| Decisión e implementación | | | |
| Operación, seguridad y observabilidad | | | |
| Evolución arquitectónica trazable | | | |
| Sustentación del reto | lo fija el docente | | |
| **Total** | | **/ 5,00** | |

Anclas rápidas, tomadas de la rúbrica del aula:

- **Caracterización.** Básico si formula el escenario sin línea base reproducible; competente si
  declara hipótesis, montaje, variables, umbral y estado inicial medido; sobresaliente si además
  controla factores de confusión y explica los límites de validez.
- **Decisión e implementación.** Básico si la respuesta es parcial y las consecuencias quedan sin
  analizar; competente si la decisión es coherente con dominio, contratos, despliegue y costo y
  está en un ADR; sobresaliente si además compara con una alternativa viable o demuestra por qué
  no cambiar es lo mejor.
- **Operación, seguridad y observabilidad.** Insuficiente si el escenario no se puede observar o
  se exponen secretos; competente con pipeline, health check, logs estructurados y métrica ligada
  al escenario; sobresaliente si además hay alerta, correlación o análisis de dependencias y se
  demuestra degradación o recuperación controlada.
- **Evolución trazable.** Básico si la documentación se actualiza a medias; competente si C4,
  arc42, ADR y contratos representan el MVP y enlazan el cambio con pruebas y mediciones;
  sobresaliente si una decisión anterior queda confirmada o reemplazada con la evidencia.
- **Sustentación.** Se califica en la sesión, sobre el entorno desplegado y con el pipeline en
  vivo.
