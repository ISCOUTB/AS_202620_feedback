# Contrato del repositorio · Arquitecturas de Software

Lo que toda entrega del curso debe cumplir, con el comando que lo comprueba. Las 18 fichas de
revisión lo citan en vez de repetirlo, así que **esto se lee una vez y se aplica a todas**.

Nada de aquí es invención del kit: sale del aula, del capítulo «El proyecto integrador», de
«Plantilla de ADR», de «Guía de Aspect Driven Development con IA» y de «Política de uso
responsable de IA». Si el aula y este documento divergen, **manda el aula** y hay que corregir
este archivo.

## 1. Identidad del repositorio

| Qué | Valor |
|---|---|
| Organización | `ISCOUTB` en GitHub |
| Nombre | `AS_202620_<PROYECTO>`, con `PROYECTO` el nombre o acrónimo del trabajo |
| Visibilidad | público |
| Integrantes | todos pertenecen a la organización y aparecen en el historial |

Un repositorio fuera de la organización, con otro nombre o privado no se revisa a ciegas: se
registra el hallazgo con el motivo y se sigue con el resto de la matriz sobre lo que sí sea
visible.

## 2. Estructura mínima

```text
/                     código del sistema
/docs/arc42/          documentación arquitectónica (secciones 1 a 12)
/docs/adr/            un archivo por decisión: NNNN-titulo-en-kebab-case.md
/docs/c4/             diagramas (preferiblemente como código)
/docs/aspectos.md     tabla de trazabilidad aspecto hasta evidencia
/docs/ia.md           registro de uso de IA
README.md             qué es, cómo se arranca, cómo se prueba
```

```bash
git -C "$DIR" ls-tree -r --name-only HEAD | grep -E '^(docs/(arc42|adr|c4)/|docs/(aspectos|ia)\.md|README\.md)'
```

Una ruta distinta a la mínima es **desviación de estructura, no ausencia del artefacto**: un C4
guardado en `docs/arc42/` sigue siendo el C4. Se registra en la fila de estructura de la matriz
transversal y el artefacto se evalúa donde esté. Lo mismo con la extensión: la plantilla arc42 se
entrega en Markdown, y un PDF o un `.docx` en su lugar se anota, porque el curso pide que la
documentación sea revisable en el repositorio.

**Convención de los comandos.** `$DIR` es el clon local, `$REPO` el nombre del repositorio
y `$URL` la del sistema desplegado. Los comandos que no llevan `git -C "$DIR"` suponen que
estás dentro del clon: `cd "$DIR"` antes de ejecutarlos.

## 3. Qué estado del repositorio se califica

Las entregas de corte se califican en el **commit etiquetado**: `corte-1`, `corte-2`, `final`.
Las evidencias semanales y los talleres se califican en el **commit vigente al cierre de la
actividad**, y ese cierre lo publica la propia actividad en el aula.

```bash
git -C "$DIR" tag --list
git -C "$DIR" log -1 --format='%H %cI %s' "corte-1"        # fecha real del commit etiquetado
git -C "$DIR" log -1 --format='%H %cI' --until="$CIERRE"    # sin etiqueta: el último antes del cierre
```

Tres situaciones y su resolución, para que no dependan del criterio del momento:

- **Etiqueta ausente.** Se revisa el último commit anterior al cierre, se anota el hash en
  Observaciones y la fila de versionado de la matriz transversal queda en No cumple.
- **Etiqueta posterior al cierre.** El contenido se revisa igual, y la fila de versionado
  registra la diferencia entre `%cI` y el cierre de la actividad.
- **Etiqueta movida después de calificar.** Se compara con el hash citado en la revisión previa,
  que por eso se guarda siempre.

## 4. Convenciones de ADR

- Un archivo por decisión en `/docs/adr/`, numerado: `0001-usar-monolito-modular.md`.
- El título enuncia la decisión, no el tema: «Usar monolito modular», no «Sobre el estilo».
- **Un ADR aceptado no se edita ni se borra.** Si la decisión cambia, se escribe otro y el
  anterior queda marcado como reemplazado, con enlace al que lo sustituye.
- Cada ADR lleva contexto, opciones evaluadas, decisión, consecuencias y trazabilidad
  (requisito o aspecto, elementos C4, commit o PR que lo implementa, pruebas que lo cubren).

```bash
# Nombres que no siguen la convención: la salida debe estar vacía
ls docs/adr | grep -Ev '^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$'

# ADR reescritos después de aceptarse (mirar los commits posteriores al de creación)
git -C "$DIR" log --follow --format='%h %cI %s' -- docs/adr/0001-*.md
```

## 5. La tabla de aspectos

`/docs/aspectos.md`, una fila por aspecto, con las ocho columnas del curso:

`ID · Aspecto · Requisito · C4 · ADR · Código · Pruebas · Evidencia`

La cadena completa es **aspecto, requisito, elementos C4, ADR, código, pruebas, evidencia de
calidad**, y cada eslabón tiene que ser navegable. Una celda con un texto que no lleva a ninguna
parte cuenta como hueco: **una fila con huecos es una fila que no se puede defender**. Cuántas
filas y hasta qué columna se exige depende de la semana, y eso lo dice cada ficha.

## 6. Registro de uso de IA

`docs/ia.md` con, para cada uso: para qué, qué herramienta, qué se aceptó, y **qué se rechazó y
por qué**. Es evidencia de criterio, no un trámite: la columna de lo rechazado con su motivo
técnico es la que se mira primero.

```bash
git -C "$DIR" log --format='%cI %h' -- docs/ia.md    # crece a lo largo del semestre, o no
```

## 7. README

Qué es el sistema, **cómo se arranca con un solo comando** y cómo se prueba, con los requisitos
previos declarados. Es el documento contra el que se comprueba si el proyecto arranca, así que un
README que remite a pasos manuales no documentados afecta a la fila de reproducibilidad.

## 8. Pipeline y análisis estático

Pruebas automatizadas ejecutadas por integración continua en cada push, más análisis estático en
SonarCloud (organización `isco-utb`). Desde el segundo corte se espera además que el pipeline
bloquee la integración cuando falla.

```bash
ls .github/workflows/ 2>/dev/null
curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=5" \
  | python -c "import json,sys;[print(r['name'],r['head_branch'],r['status'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
```

Si el equipo usa otra plataforma de CI, la evidencia es el enlace al run que entregó en Moodle
más el archivo de configuración en el repositorio. Un badge en el README no es evidencia de
ejecución.

## 9. Secretos

Ninguna credencial en el repositorio. **El repositorio es público**, de modo que un secreto
encontrado es incidente, no descuido de forma: se anota en la matriz y se avisa al equipo para
que lo rote, porque quitarlo del último commit no lo quita del historial.

```bash
git -C "$DIR" grep -nIE '(AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{36}|xox[baprs]-|sk-[A-Za-z0-9]{20,}|(password|passwd|secret|token|api_?key)\s*[:=]\s*.{6,})' HEAD
git -C "$DIR" ls-files | grep -E '(^|/)\.env$'          # .env versionado
git -C "$DIR" log --oneline -S'BEGIN PRIVATE KEY'        # lo que se retiró pero sigue en el historial
```

`git grep` termina con código 1 cuando no encuentra nada, que aquí es el resultado bueno: no lo
confundas con un fallo del comando.

## 10. Autoría y colaboración

Todos los integrantes contribuyen con código y con documentación, y el historial lo muestra
repartido a lo largo del semestre. Es criterio calificado en el proyecto final.

```bash
git -C "$DIR" shortlog -sne HEAD
git -C "$DIR" log --format='%cI %an' | cut -c1-7 | sort | uniq -c    # actividad por mes
curl -s "https://api.github.com/repos/ISCOUTB/$REPO/pulls?state=all&per_page=100" \
  | python -c "import json,sys;[print(p['number'],p['user']['login'],p['title']) for p in json.load(sys.stdin)]"
```

Un solo autor para todo el equipo, o todo el trabajo en una entrega masiva al final, es hallazgo
de esta fila aunque el contenido esté completo.

**Consolida las identidades antes de contar.** `git shortlog -sne` separa por nombre y correo, de
modo que la misma persona aparece dos veces si empuja con el correo personal y con el
institucional, y eso se lee como un integrante de más y otro de menos. Agrupa por persona, con el
listado de equipos delante, y solo entonces concluye quién falta.

## 11. Matriz transversal

Se aplica en **todas** las entregas, además de la matriz propia de la ficha.

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | URL `github.com/ISCOUTB/AS_202620_<PROYECTO>` y respuesta de la API sin autenticación | | |
| Estructura mínima presente | salida de `git ls-tree` con las seis rutas del apartado 2 | | |
| Estado calificado identificable | etiqueta de la entrega, o hash y `%cI` del último commit anterior al cierre | | |
| Nombres de ADR según la convención | `ls docs/adr` sin salida en el filtro del apartado 4 | | |
| ADR aceptados no reescritos | historial de cada ADR anterior sin commits de reescritura, o reemplazo declarado | | |
| `docs/ia.md` al día para la semana | commits sobre el archivo dentro del periodo revisado, con lo rechazado y su motivo | | |
| Sin credenciales en el repositorio ni en el historial | `git grep` y `git log -S` sin coincidencias | | |
| Contribución de todos los integrantes | `git shortlog -sne` con todos los integrantes del equipo | | |

## 12. Reglas de evaluación que fija el curso

- **Lo anterior no se recalifica por existir.** Los cortes evalúan la respuesta a un reto nuevo;
  las evidencias de semanas previas son línea base. Si un artefacto anterior se deterioró, eso
  afecta a la coherencia del sistema, pero su nota original no se duplica.
- **Si no lo entiende, no lo entrega.** Código o documento que el equipo no pueda explicar en la
  sustentación tiene el mismo efecto que no haberlo entregado. Por eso hay filas que solo se
  resuelven en la sustentación, y el kit las marca así en vez de adivinarlas.
- **El repositorio es la entrega.** Lo que se sube a Moodle es el enlace más un PDF corto que
  sitúa al lector; el PDF no sustituye evidencia que deba estar en el repositorio.

## 13. Estados de la matriz

- **Cumple.** Hay evidencia citada y satisface el criterio.
- **No cumple.** Hay evidencia citada de que falta o no satisface.
- **No verificado.** No se pudo comprobar, con el motivo y qué haría falta. Se usa cuando la
  comprobación exige ejecutar el sistema, credenciales del equipo o la sustentación. **No se
  usa para evitar decidir**: si la evidencia está y se puede leer, hay que pronunciarse.

Toda fila cita evidencia concreta: `ruta:línea`, hash de commit, URL del run, código HTTP. Sin
evidencia citable el estado es No verificado, nunca Cumple.
