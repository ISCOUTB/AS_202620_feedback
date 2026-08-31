# Evidencia S13 · Modelado de amenazas y plan de mitigación

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s13` |
| Semana | 13 |
| Corte | Tercer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**Tabla de amenazas priorizadas con mitigación asignada**, **resultado del análisis de
dependencias** y **sección de privacidad**: qué datos personales se tratan y con qué base.

El modelado se hace con STRIDE **sobre el propio C4** del equipo, priorizando por probabilidad e
impacto. El recordatorio de la semana pide documentar la arquitectura de seguridad en la sección
8 de arc42 y las amenazas aceptadas en la 11, y exige ADR para toda mitigación que cambie la
estructura.

Si el sistema incorpora un componente generativo, aquí se modelan sus riesgos propios: inyección
de prompt, fuga de datos y envenenamiento del contexto.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Tabla de amenazas.** Comprueba que las amenazas están ancladas en elementos concretos del C4
   del equipo, no en una lista genérica de OWASP copiada. Cada fila con categoría, elemento
   afectado, probabilidad, impacto y mitigación asignada.
3. **Priorización efectiva.** Que la tabla tenga columnas de probabilidad e impacto no basta: el
   plan debe atacar primero lo priorizado. Comprueba la correspondencia entre la prioridad y lo
   que se hizo.
4. **Mitigaciones con dueño y estado.** Cada mitigación dice quién la aplica y si está hecha,
   pendiente o aceptada como riesgo. Una mitigación sin estado no se puede seguir.
5. **Análisis de dependencias ejecutado.** Comprueba la herramienta en el pipeline y **el
   resultado**, con los hallazgos revisados. La ejecución sin revisión de hallazgos es media
   evidencia.
   ```bash
   grep -rniE 'snyk|dependabot|trivy|osv|pip-audit|npm audit|owasp|sonar' .github/workflows/ | head
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=30" \
     | python -c "import json,sys;[print(r['created_at'],r['name'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   ls .github/dependabot.yml 2>/dev/null
   ```
6. **Sección de privacidad.** Qué datos personales trata el sistema y con qué base los trata. Si
   el equipo sostiene que no trata ninguno, comprueba el modelo de datos antes de darlo por bueno:
   un correo o un nombre ya son datos personales.
   ```bash
   git -C "$DIR" grep -nIE '(email|correo|telefono|teléfono|cedula|cédula|documento|direccion|dirección|nombre_completo)' HEAD -- . ':!docs' | head -20
   ```
7. **Riesgos del componente generativo, si lo hay.** Inyección de prompt, fuga de datos y
   envenenamiento del contexto, con su mitigación.
8. **arc42 secciones 8 y 11.** Arquitectura de seguridad en la 8; amenazas aceptadas en la 11, con
   el motivo de aceptarlas.
9. **ADR de las mitigaciones estructurales.** Toda mitigación que cambie la estructura necesita el
   suyo.
10. **Secretos.** Repite el barrido del contrato. Encontrar una credencial en la semana del
    modelado de amenazas es un hallazgo que conviene señalar con nombre propio.

**Qué no hacer aquí:** no exigir pruebas de penetración ni auditoría externa; no confundir el
análisis de dependencias con el análisis estático del código, que ya está en el pipeline desde el
segundo corte.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Tabla de amenazas anclada en elementos del C4 del equipo | tabla citada, con el elemento afectado por fila | | |
| Priorización por probabilidad e impacto | columnas de la tabla, con el orden resultante | | |
| Mitigación asignada a cada amenaza, con dueño y estado | columnas de mitigación y estado | | |
| El plan ataca primero lo priorizado | correspondencia entre prioridad y trabajo hecho | | |
| Análisis de dependencias ejecutado en el pipeline | línea del workflow y URL del run | | |
| Hallazgos del análisis revisados y decididos | apartado con los hallazgos y qué se hizo con cada uno | | |
| Sección de privacidad con datos personales tratados y su base | apartado citado, contrastado con el modelo de datos | | |
| Riesgos del componente generativo, si el sistema lo incorpora | apartado con inyección, fuga y envenenamiento | | |
| arc42 sección 8 con la arquitectura de seguridad | `docs/arc42/08*` | | |
| arc42 sección 11 con las amenazas aceptadas y su motivo | `docs/arc42/11*` | | |
| ADR de las mitigaciones que cambian la estructura | archivos de `docs/adr/` del periodo | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. La nota sugerida, `1 + 4 × (n/m)` sobre esta
matriz, se publica como propuesta al docente (decisión del profesor): la nota final la fija el
profesor en Moodle.

Si aparece una credencial en el repositorio, dilo aquí y avisa al equipo el mismo día: el
repositorio es público y quitarla del último commit no la quita del historial. Es además el
hallazgo que hunde el criterio de operación y seguridad en el proyecto final.
