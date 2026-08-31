# Evidencia S7 · Contrato de API y prueba de contrato

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s7` |
| Semana | 7 |
| Corte | Segundo corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

**Contrato de la API principal en OpenAPI o AsyncAPI, versionado en el repositorio**, **prueba de
contrato en el pipeline** y **ADR que justifica la estrategia de integración** (síncrona o
asíncrona).

El laboratorio de la semana pide además comprobar que la prueba de contrato **falla** al
introducir un cambio incompatible: una prueba que pasa siempre no prueba nada. El recordatorio de
documentación añade la sección 6 de arc42 con los flujos de interacción y el C4 nivel 2 con cada
flecha etiquetada con su protocolo y su formato.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Localiza el contrato y comprueba que es ejecutable**, no prosa: un archivo OpenAPI, AsyncAPI
   o proto, versionado en el repositorio.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -iE '(openapi|swagger|asyncapi).*\.(ya?ml|json)$|\.proto$'
   python -c "import json,sys;d=json.load(open(sys.argv[1]));print(d.get('openapi'),len(d.get('paths',{})))" <archivo.json>
   ```
   Para YAML, comprueba a lectura la versión de la especificación, las rutas y los esquemas de
   respuesta. Un contrato con rutas pero sin esquemas de datos se anota.
3. **Comprueba que el contrato corresponde con la API implementada.** Toma dos rutas del contrato
   y localízalas en el código; toma una ruta del código y comprueba que está en el contrato. La
   desincronización en cualquiera de los dos sentidos es hallazgo.
4. **Versionado del contrato.** Debe verse la versión de la API (en el propio archivo o en la
   ruta) y su historial en git.
   ```bash
   git -C "$DIR" log --format='%h %cI %s' -- <ruta del contrato>
   ```
5. **Prueba de contrato en el pipeline.** Localiza la prueba y comprueba que el workflow la
   ejecuta, no solo que existe el archivo.
   ```bash
   ls .github/workflows/
   grep -rniE 'contract|dredd|schemathesis|pact|prism|spectral|openapi' .github/workflows/ | head
   ```
6. **Comprueba que la prueba puede fallar.** Busca en el historial una ejecución en rojo, o la
   evidencia que el equipo aporte del cambio incompatible que la hizo fallar. Si no hay ninguna de
   las dos, márcalo como No verificado y déjalo como pregunta de sustentación.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=50" \
     | python -c "import json,sys;[print(r['created_at'],r['name'],r['conclusion']) for r in json.load(sys.stdin)['workflow_runs'] if r['conclusion']!='success']"
   ```
7. **ADR de la estrategia de integración.** Justifica síncrono o asíncrono contra un escenario de
   calidad concreto, con la alternativa descartada y sus consecuencias de acoplamiento.
8. **arc42 sección 6 y C4 nivel 2.** Flujos de interacción descritos, y cada flecha del nivel 2
   etiquetada con protocolo y formato.

**Qué no hacer aquí:** no exigir mensajería ni eventos, que son de la semana 12; no exigir
despliegue de la API, que es de la semana 8; no puntuar la cantidad de endpoints.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | ruta del archivo OpenAPI, AsyncAPI o proto | | |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | fragmento del contrato citado | | |
| Correspondencia entre el contrato y la API implementada | dos rutas del contrato en el código y una del código en el contrato | | |
| Versión de la API declarada y con historial | campo de versión y `git log` del archivo | | |
| Prueba de contrato presente | ruta de la prueba | | |
| El pipeline ejecuta la prueba de contrato | línea del workflow que la invoca y URL del run | | |
| Evidencia de que la prueba falla ante un cambio incompatible | run en rojo o evidencia aportada por el equipo | | |
| ADR de la estrategia de integración ligado a un escenario | `docs/adr/NNNN-*.md` con alternativa descartada | | |
| arc42 sección 6 con los flujos de interacción | `docs/arc42/06*` | | |
| C4 nivel 2 con protocolo y formato en cada flecha | diagrama del nivel 2 | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. La nota sugerida, `1 + 4 × (n/m)` sobre esta
matriz, se publica como propuesta al docente (decisión del profesor): la nota final la fija el
profesor en Moodle.

Para el segundo corte, criterio de dominio, interfaces y datos: la diferencia entre competente y
sobresaliente está justamente en que exista prueba de contrato **que falle** cuando el proveedor
rompe el contrato. Deja registrado si esa evidencia apareció aquí.
