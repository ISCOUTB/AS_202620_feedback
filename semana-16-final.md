# Proyecto final · integración y desafío arquitectónico

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:final` |
| Semana | 16 |
| Corte | Tercer corte (actividad de corte) |
| Tipo | grupal, nota única del equipo, con rúbrica de 5 criterios |
| Qué sube el estudiante | enlace al repositorio en el commit etiquetado `final`, la URL del sistema y un documento guía de tres páginas |
| Estado que se califica | la etiqueta `final` y el sistema desplegado |

Antes de empezar, lee [CONTRATO.md](CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Entrega del **sistema integrado** y respuesta al **desafío final asignado**. Las evidencias S11 a
S14, el taller y la revisión entre pares conservan sus propias notas: aquí se evalúan su
integración, el comportamiento actual del sistema y la capacidad de justificar su evolución.

Es la **única sustentación final**: 15 minutos de exposición y 10 de preguntas ante docente y
jurado, con demostración en vivo obligatoria sobre el sistema desplegado. La semana siguiente
aplica lo recomendado y no repite la defensa.

Antes de revisar, consigue **cuál fue el desafío final asignado a ese equipo**.

La última verificación que el aula pide antes de etiquetar `final` marca el listón documental:
arc42 completo (secciones 1 a 12, incluido glosario), C4 niveles 1 a 3 correspondientes al sistema
entregado, y la tabla de aspectos recorrible de punta a punta **para todos** los aspectos
declarados.

## Instrucciones para el agente de revisión

1. **Sitúate en la etiqueta `final`** y comprueba que apunta a un commit anterior al cierre.
   ```bash
   git -C "$DIR" log -1 --format='%H %cI %s' final && git -C "$DIR" checkout final
   ```
2. **Comprueba el sistema desplegado**, con la hora anotada: flujos principales, health check y
   al menos un camino de error (entrada inválida, recurso inexistente).
   ```bash
   curl -sS -o /dev/null -w 'http=%{http_code} tiempo=%{time_total}s\n' "$URL"
   curl -sS -o /dev/null -w 'error=%{http_code}\n' "$URL/<ruta inexistente>"
   ```
3. **Respuesta al desafío final.** Localiza dónde está implementada y con qué evidencia se
   demuestra. Comprueba si está cuantificada frente a la línea base, que es lo que separa
   competente de sobresaliente.
4. **Alcance comprometido frente a entregado.** Compara con lo prometido en el segundo corte y
   comprueba que lo no hecho está **declarado**. Un alcance recortado y declarado puntúa mejor que
   uno recortado en silencio.
   ```bash
   git -C "$DIR" diff --stat corte-2..final | tail -5
   git -C "$DIR" log --format='%h %cI %an %s' corte-2..final | head -40
   ```
5. **Decisiones y evolución.** Recorre los ADR del semestre en orden y comprueba que se puede
   reconstruir por qué el sistema es como es. Busca al menos uno **confirmado o reemplazado con
   evidencia**.
   ```bash
   ls docs/adr/ | sort
   grep -rniE 'superseded|reemplaza|reemplazado por|confirmad' docs/adr/ | head
   ```
6. **Calidad, resiliencia y seguridad verificadas.** Atributos prioritarios contrastados con
   umbral, modos de fallo probados y mitigaciones de seguridad relevantes. Comprueba que las
   mediciones son reproducibles y que los riesgos residuales están documentados.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=20" \
     | python -c "import json,sys;[print(r['created_at'],r['name'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   ```
7. **Documentación completa y coincidente.** arc42 secciones 1 a 12 con glosario, C4 niveles 1 a
   3 correspondientes al sistema entregado, contratos al día, y la tabla de aspectos recorrible
   **para todos** los aspectos. Recorre al menos tres filas completas y di cuántas de las
   declaradas verificaste.
   ```bash
   ls docs/arc42/ docs/c4/
   grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|arc42 template' docs/arc42/ | head
   ```
8. **Validación automática de documentación**, si existe: diagramas como código generados en el
   pipeline, enlaces verificados, reglas de arquitectura comprobadas. Es lo que distingue el nivel
   sobresaliente del criterio de trazabilidad.
9. **Contribuciones verificables.** Aporte de cada integrante a lo largo del semestre, PR con
   revisión cruzada y comentarios de fondo, y reparto de responsabilidades documentado. Esta parte
   **sí** se verifica desde el repositorio. Contrasta contra los integrantes de
   [EQUIPOS.md](EQUIPOS.md) y contra la correspondencia entre cuenta y persona que la planilla del
   equipo haya ido fijando durante el semestre.
   ```bash
   git -C "$DIR" shortlog -sne final
   git -C "$DIR" log --format='%cI %an' | cut -c1-7 | sort | uniq -c
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/pulls?state=all&per_page=100" \
     | python -c "import json,sys;[print(p['number'],p['user']['login'],p['merged_at'],p['title']) for p in json.load(sys.stdin)]"
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/pulls/comments?per_page=100" \
     | python -c "import json,sys;[print(c['user']['login'],c['path'],c['body'][:80].replace(chr(10),' ')) for c in json.load(sys.stdin)]"
   ```
10. **Prepara la sustentación.** Deja escritas al menos tres preguntas contrafactuales sacadas de
    lo que encontraste: qué pasa si se multiplica la carga, si cae ese componente, si cambia el
    proveedor. El jurado las necesita el mismo día.

**Qué no hacer aquí:** no recalificar S11 a S14 ni el taller por existir; no puntuar la
demostración desde el repositorio; no exigir que el sistema esté libre de deuda técnica, que
declararla con honestidad es parte de lo que se evalúa.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Etiqueta `final` sobre un commit anterior al cierre | `git log -1 --format='%H %cI' final` | | |
| Sistema desplegado y estable en el momento de la revisión | códigos de respuesta y hora de la comprobación | | |
| Flujos principales funcionando con datos realistas | rutas probadas y su resultado | | |
| Caminos de error atendidos: validaciones, entradas inválidas, tiempos de espera | respuestas de las rutas de error | | |
| Respuesta al desafío final implementada y evidenciada | rutas del código y evidencia de ejecución | | |
| Alcance entregado frente al comprometido, con lo no hecho declarado | documento guía y diferencia entre `corte-2` y `final` | | |
| ADR que permiten reconstruir la evolución del sistema | listado de `docs/adr/` recorrido en orden | | |
| Al menos una decisión confirmada o reemplazada con evidencia | ADR marcado, con el enlace al que lo sustituye | | |
| Atributos prioritarios medidos y contrastados con su umbral | mediciones con procedimiento reproducible | | |
| Modos de fallo probados y mitigaciones de seguridad aplicadas | pruebas y su run en el pipeline | | |
| arc42 secciones 1 a 12 completas, con glosario y sin texto de plantilla | listado de `docs/arc42/` y barrido de plantilla | | |
| C4 niveles 1 a 3 correspondientes al sistema entregado | archivos de `docs/c4/` frente a la estructura del código | | |
| Tabla de aspectos recorrible para todos los aspectos declarados | número de filas verificadas sobre el total | | |
| Validación automática de diagramas, enlaces o reglas en el pipeline | paso del workflow que la ejecuta | | |
| Contribución sustantiva de todos los integrantes a lo largo del semestre | `git shortlog` y actividad por mes | | |
| Revisión cruzada con comentarios de fondo en los PR | comentarios de revisión citados | | |
| Demostración y sustentación | sesión ante docente y jurado, no verificable desde el repositorio | No verificado | lo resuelve el docente en la sesión |

## Nivel de rúbrica sugerido

Rúbrica desplegada en el aula, cinco criterios. Los niveles puntúan 0,00 y después el 60 %, el
80 % y el 100 % del máximo de cada criterio; la suma **es** la nota en la escala UTB. Es una
**propuesta al docente**, no una nota aplicada.

| Criterio | Máximo | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---:|---|---:|---|
| Sistema funcional y respuesta al desafío | 1,25 | | | |
| Decisiones y evolución | 1,00 | | | |
| Calidad, resiliencia y seguridad verificadas | 1,00 | | | |
| Coherencia y trazabilidad arquitectónica | 0,75 | | | |
| Demostración, sustentación y colaboración verificable | 1,00 | lo fija el docente | | aporta aquí la evidencia de colaboración |
| **Total** | **5,00** | | **/ 5,00** | |

Puntajes por nivel: para máximo 1,25 son 0,00 · 0,75 · 1,00 · 1,25; para 1,00 son 0,00 · 0,60 ·
0,80 · 1,00; para 0,75 son 0,00 · 0,45 · 0,60 · 0,75.

Anclas rápidas, tomadas de la rúbrica del aula:

- **Sistema y desafío.** Básico si los flujos funcionan pero la respuesta al desafío es parcial o
  manual; competente si responde al escenario con datos realistas y caminos de error verificables;
  sobresaliente si además muestra degradación, recuperación o adaptación controlada y cuantifica
  el resultado frente a la línea base.
- **Decisiones y evolución.** Competente si los ADR muestran alternativas, consecuencias y una
  evolución motivada por escenarios, mediciones o incidentes; sobresaliente si el equipo demuestra
  haber confirmado, rechazado o reemplazado una decisión con evidencia cuantificada.
- **Calidad, resiliencia y seguridad.** Competente si los atributos prioritarios se contrastan con
  umbrales y se prueban modos de fallo y mitigaciones; sobresaliente si las mediciones son
  reproducibles y los límites, el costo y los riesgos residuales están documentados.
- **Coherencia y trazabilidad.** Competente si arc42, C4, ADR, contratos y tabla de aspectos
  coinciden con el sistema y son navegables; sobresaliente si el repositorio valida
  automáticamente diagramas, enlaces o reglas arquitectónicas.
- **Demostración y colaboración.** Insuficiente si la demostración depende de capturas o no se
  puede atribuir el trabajo; competente si la demostración va guiada por escenarios y hay
  contribuciones y revisiones sustantivas trazables; sobresaliente si además el equipo razona ante
  contrafactuales, reconoce deuda y evidencia discusión técnica y rotación de responsabilidades.
