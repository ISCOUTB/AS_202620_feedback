# Evidencia S3 · Estrategia de solución y primer ADR

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s3` |
| Semana | 3 |
| Corte | Primer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

arc42 **sección 4**, matriz comparativa de los tres estilos (capas, hexagonal y monolito
modular) contra el árbol de utilidad, `docs/adr/0001-*.md` con **alternativas y consecuencias**,
y el **esqueleto ejecutable**: el repositorio arranca con un solo comando documentado en el
README, tiene una prueba automatizada en verde y los paquetes vacíos que impone el estilo elegido
en el ADR.

No se pide lógica de negocio. El esqueleto existe para que la semana 4 empiece por la
arquitectura y no por el montaje. El ADR se enlaza desde `docs/aspectos.md` y desde el escenario
de calidad que lo motiva.

## Instrucciones para el agente de revisión

1. **Sitúate en el commit vigente al cierre** de la actividad y registra hash y fecha.
2. **Sección 4 de arc42.** Explica la estrategia elegida y las tácticas que atacan los escenarios
   priorizados; no describe el estilo en abstracto.
3. **Matriz comparativa de los tres estilos.** Tiene que comparar **contra el árbol de utilidad**
   del equipo: qué escenario mejora y qué empeora cada estilo. Una tabla de ventajas y desventajas
   genéricas, copiada de un manual, no cumple.
4. **ADR 0001.** Nombre según la convención, título que enuncia la decisión, y contenido con
   contexto, opciones evaluadas, decisión y consecuencias. Comprueba que las **alternativas
   descartadas** están con su motivo.
   ```bash
   ls docs/adr/
   sed -n '1,80p' docs/adr/0001-*.md
   ```
5. **Enlaces del ADR.** Debe alcanzarse desde la fila de su aspecto en `docs/aspectos.md` y desde
   el escenario de calidad que lo motiva. Sigue los dos enlaces.
6. **Esqueleto ejecutable.** Comprueba el comando único de arranque documentado en el README y la
   presencia del archivo que lo soporta.
   ```bash
   grep -niE 'docker compose up|make |npm |mvn |gradle|dotnet |uvicorn|docker run' README.md | head
   ls docker-compose.y*ml Makefile package.json pom.xml build.gradle* pyproject.toml 2>/dev/null
   ```
   Si vas a ejecutarlo, hazlo en contenedor desechable; si no, marca No verificado y anota el
   comando declarado.
7. **Prueba automatizada en verde.** Localiza la prueba y el run del pipeline que la ejecutó.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=20" \
     | python -c "import json,sys;[print(r['created_at'],r['name'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
   ```
   Si el equipo todavía no tiene pipeline, vale la evidencia de ejecución que aporte, y se anota.
8. **Paquetes del estilo elegido.** La estructura de directorios corresponde con el estilo del
   ADR: si dice hexagonal, separación de dominio, puertos y adaptadores; si dice monolito modular,
   módulos con frontera declarada. Cita las rutas.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -v '^docs/' | awk -F/ 'NF>1 {print $1"/"$2}' | sort -u | head -30
   ```

**Qué no hacer aquí:** no exigir lógica de negocio ni corte vertical, que son de la semana 4; no
juzgar qué estilo eligieron, sino la coherencia entre el ADR, la matriz y la estructura.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04*` | | |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | tabla con los tres estilos y los escenarios del equipo | | |
| `docs/adr/0001-*.md` con el nombre de la convención | listado de `docs/adr/` | | |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | secciones del propio ADR | | |
| Alternativas descartadas con su motivo | apartado de opciones del ADR | | |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | los dos enlaces, seguidos | | |
| Arranque con un solo comando documentado en el README | sección del README y archivo de arranque | | |
| Prueba automatizada en verde | ruta de la prueba y URL del run, o evidencia de ejecución aportada | | |
| Estructura de paquetes correspondiente al estilo del ADR | rutas de primer y segundo nivel del repositorio | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. La nota sugerida, `1 + 4 × (n/m)` sobre esta
matriz, se publica como propuesta al docente (decisión del profesor): la nota final la fija el
profesor en Moodle.

Si el esqueleto no arranca, dilo en Observaciones con el error exacto: la semana 4 construye el
corte vertical encima, y arrastrar el montaje roto es lo que hace que esa evidencia llegue tarde.
