# Aplicación de cambios y cierre arquitectónico

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:cierre` |
| Semana | 17 |
| Corte | Tercer corte |
| Tipo | grupal, nota única del equipo, con calificación directa sobre la escala UTB |
| Qué sube el estudiante | la matriz de retroalimentación y los enlaces a commits, PR, ADR y run del pipeline |
| Estado que se califica | commit vigente al cierre de la actividad, posterior a la etiqueta `final` |
| Acceso | requiere el proyecto final |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Aplicar la retroalimentación recibida en las sustentaciones finales y en la revisión entre pares.
**No hay segunda sustentación**: la entrega es documental y de código, y debe incluir los ocho
elementos de la consigna.

1. **Matriz de retroalimentación**, con cada recomendación recibida y su origen.
2. **Clasificación** de cada una: aceptada, rechazada o aplazada.
3. **Justificaciones**, con el motivo técnico de cada rechazo o aplazamiento. «Falta de tiempo» a
   secas no cuenta.
4. **Código y pruebas modificados**, con enlaces a los commits o PR de cada cambio aceptado.
5. **ADR actualizados**, nuevos o marcados como reemplazados, enlazados desde la matriz.
6. **Diagramas y arc42 actualizados**, coherentes con el código tras los cambios.
7. **Evidencia de ausencia de regresiones**, con el pipeline en verde tras los cambios y el enlace
   al run.
8. **Retrospectiva**, con al menos una lección por integrante.

El insumo es el formulario «Recomendaciones del jurado» de la semana anterior, más las revisiones
entre pares de la semana 14. Consíguelos antes de revisar: sin la lista de recomendaciones
recibidas no se puede comprobar que la matriz esté completa.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** y comprueba que es **posterior a la etiqueta
   `final`**: lo que se califica aquí es lo que pasó después.
   ```bash
   git -C "$DIR" log --format='%h %cI %an %s' final..HEAD | head -40
   git -C "$DIR" diff --stat final..HEAD | tail -5
   ```
2. **Cotejo de la matriz con lo recibido.** Cada recomendación del jurado y de los pares debe
   aparecer en la matriz, con su origen. Cuenta cuántas recibió y cuántas están: la diferencia es
   el hallazgo.
3. **Clasificación completa.** Toda fila clasificada como aceptada, rechazada o aplazada. Una fila
   sin clasificar es una fila sin decidir.
4. **Justificación técnica de rechazos y aplazamientos.** Comprueba que el motivo es técnico y
   específico. Marca las que digan solo falta de tiempo.
5. **Cambios aceptados con su enlace.** Para cada aceptada, sigue el enlace al commit o PR y
   comprueba que el cambio es el que dice ser. Cita los que no correspondan.
6. **Pruebas modificadas.** Los cambios aceptados que tocan comportamiento deben venir con su
   prueba. Anota los cambios sin prueba.
7. **ADR nuevos o reemplazados, enlazados desde la matriz.** Comprueba que el ADR reemplazado
   apunta al que lo sustituye y que la matriz enlaza a ambos.
   ```bash
   git -C "$DIR" log --format='%h %cI %s' final..HEAD -- docs/adr/
   grep -rniE 'superseded|reemplaza|reemplazado por' docs/adr/ | head
   ```
8. **Diagramas y arc42 coherentes tras los cambios.** Comprueba que la documentación cambió donde
   el código cambió.
   ```bash
   git -C "$DIR" diff --stat final..HEAD -- docs/
   ```
9. **Ausencia de regresiones.** Run del pipeline en verde **posterior** al último cambio, con su
   enlace. Un run anterior a los cambios no demuestra nada.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=20" \
     | python -c "import json,sys;[print(r['created_at'],r['head_sha'][:8],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   ```
10. **Retrospectiva.** Qué funcionó, qué no y qué harían distinto, con **al menos una lección por
    integrante**. Cuenta las lecciones y compáralas con el número de integrantes; valora si son
    específicas del proyecto o genéricas.

**Qué no hacer aquí:** no volver a evaluar el sistema completo, que ya se calificó en el proyecto
final; no exigir que acepten todas las recomendaciones, que rechazar con argumento técnico es lo
que se evalúa; no pedir una segunda sustentación, que el curso descarta expresamente.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Trabajo posterior a la etiqueta `final` | commits entre `final` y el estado revisado | | |
| Matriz de retroalimentación con todas las recomendaciones recibidas y su origen | matriz frente al formulario del jurado y las revisiones entre pares | | |
| Cada recomendación clasificada como aceptada, rechazada o aplazada | columna de clasificación completa | | |
| Motivo técnico de cada rechazo o aplazamiento | columna de justificación, sin «falta de tiempo» a secas | | |
| Cambios aceptados con enlace al commit o PR que los implementa | enlaces seguidos y verificados | | |
| Pruebas modificadas donde el comportamiento cambió | rutas de las pruebas tocadas | | |
| ADR nuevos o marcados como reemplazados, enlazados desde la matriz | archivos de `docs/adr/` posteriores a `final` | | |
| Diagramas y arc42 coherentes con el código tras los cambios | diferencia documental entre `final` y el estado revisado | | |
| Pipeline en verde posterior al último cambio | URL del run y su fecha frente a la del último commit | | |
| Retrospectiva con al menos una lección por integrante | apartado citado, con el recuento de lecciones | | |

## Nivel sugerido

Esta entrega **no lleva rúbrica**: se califica con calificación directa sobre la escala UTB, con
la referencia publicada en la consigna. Es una **propuesta al docente**, no una nota aplicada.

| Referencia | Cuándo aplica | Nota |
|---|---|---:|
| Sin entrega o sin cambios aplicados | no hay trabajo posterior a `final` | 0,0 |
| Los ocho elementos presentes de forma mínima | están todos, aunque escuetos | 3,0 |
| Cambios implementados y trazados con documentación coherente | cada aceptada llega al código y la documentación acompaña | 4,0 |
| Además, retrospectiva autocrítica y específica, y rechazos bien argumentados | lecciones concretas del proyecto y motivos técnicos sólidos | 5,0 |

Deja escrito cuál de los ocho elementos falta, si falta alguno: la referencia de 3,0 exige los
ocho, y ese es el corte que más discusión genera.
