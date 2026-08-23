# Evidencia S1 · Equipo, problema y repositorio

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s1` |
| Semana | 1 |
| Corte | Primer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |

Antes de empezar, lee [CONTRATO.md](CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Repositorio `AS_202620_PROYECTO` creado en la organización ISCOUTB **con los integrantes ya
añadidos**, ficha del problema de una página, `docs/aspectos.md` con **un** aspecto declarado y
sus dos primeras columnas, y `docs/ia.md` iniciado.

El recordatorio de la semana añade el montaje de la estructura: `/docs/arc42/` con la plantilla
ya descomprimida dentro, más `/docs/adr/` y `/docs/c4/` creados aunque estén vacíos. La ficha del
problema declara usuarios, alcance y **las dos tensiones de calidad** que hacen interesante el
problema. Los equipos son de 3 o 4 personas.

Esta es la semana del montaje: **no se exige documentación arquitectónica todavía**. Lo que se
revisa es que el instrumento esté listo para la semana 2.

## Instrucciones para el agente de revisión

1. **Confirma identidad y visibilidad del repositorio** contra el listado de la organización, y
   que el nombre sigue la convención sin excepciones.
   ```bash
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO" \
     | python -c "import json,sys;d=json.load(sys.stdin);print(d['name'],d['private'],d['created_at'])"
   ```
2. **Comprueba que el equipo está en el historial o en los colaboradores.** En la primera semana
   es normal que solo haya empujado una persona; lo que se mira aquí es que los demás tengan
   acceso, no que ya hayan trabajado.
   ```bash
   git -C "$DIR" shortlog -sne HEAD
   curl -s "https://api.github.com/repos/ISCOUTB/$REPO/contributors" \
     | python -c "import json,sys;[print(c['login'],c['contributions']) for c in json.load(sys.stdin)]"
   ```
   Contrasta con los integrantes que declara [EQUIPOS.md](EQUIPOS.md), y ante cualquier duda con
   la matrícula y el foro de conformación de equipos del aula, que son la fuente. Si falta
   alguien, anota el nombre: sin acceso a la organización no puede aparecer en el historial, y la
   contribución individual se califica en el proyecto final. Las cuentas de GitHub **no se
   atribuyen por parecido con el nombre**: si no se puede establecer la correspondencia, se dice.
3. **Ficha del problema.** Localízala (en `docs/`, en el README o como PDF de la entrega) y
   comprueba que declara usuarios, alcance y **dos tensiones de calidad**. Una lista de
   funcionalidades no es una ficha del problema: la tensión enfrenta dos atributos, del tipo
   «tiempo de respuesta frente a costo de infraestructura».
4. **Tabla de aspectos iniciada.** `docs/aspectos.md` con la tabla de ocho columnas y **al menos
   una fila** con ID y aspecto rellenos. Las demás columnas pueden estar vacías esta semana.
5. **Registro de IA iniciado.** `docs/ia.md` existe y tiene contenido real, no un encabezado
   vacío. Si el equipo declara no haber usado IA todavía, eso es una entrada válida.
6. **Estructura montada.** `docs/arc42/` con la plantilla dentro, y `docs/adr/` y `docs/c4/`
   creados. **Git no versiona directorios vacíos**: si faltan porque no tienen contenido ni
   `.gitkeep`, anótalo como observación de montaje, no como plantilla ausente.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep '^docs/' | sed 's|/[^/]*$||' | sort -u
   ```
7. **Plantilla arc42 presente y en Markdown.** Doce secciones, o un archivo con los doce
   encabezados. Que esté sin rellenar es lo esperado esta semana.

**Qué no hacer aquí:** no exigir arc42 redactado, ni diagramas, ni ADR, ni código; no penalizar
que solo un integrante haya empujado commits, siempre que el resto tenga acceso.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Repositorio creado en la organización con el nombre de la convención | respuesta de la API para `ISCOUTB/$REPO`, pública | | |
| Integrantes del equipo con acceso | contribuidores o colaboradores frente a los integrantes de `EQUIPOS.md` | | |
| Equipo de 3 o 4 personas | integrantes declarados en `EQUIPOS.md`, la matrícula o la ficha | | |
| Ficha del problema con usuarios y alcance | documento citado, con su ruta o su adjunto en Moodle | | |
| Dos tensiones de calidad declaradas y enfrentadas entre sí | párrafo o tabla de la ficha del problema | | |
| `docs/aspectos.md` con la tabla y un aspecto en sus dos primeras columnas | fila citada del archivo | | |
| `docs/ia.md` iniciado con contenido real | primeras entradas del archivo | | |
| Plantilla arc42 descomprimida en `docs/arc42/`, en Markdown | listado del directorio | | |
| `docs/adr/` y `docs/c4/` creados | listado de directorios de `docs/` | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. El kit no propone nota aquí, porque sería
calificar con una regla que el estudiante no vio.

Anota para las semanas siguientes cualquier integrante sin acceso a la organización: es el
problema que más tarde se detecta y más caro sale, porque la contribución individual se califica
sobre el historial.
