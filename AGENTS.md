# AGENTS.md · Cómo operar este repositorio semana a semana

Instrucciones para el agente que revisa los repositorios de los equipos. Leer antes de cada
sesión de revisión; vale más que cualquier intuición.

## Qué es esto

Repositorio público `ISCOUTB/AS_202620_feedback`: kit de revisión (fichas y contrato) + las
revisiones publicadas de cada equipo. Los estudiantes lo leen; por eso hay reglas estrictas de
qué se publica y qué no (ver «Publicación»).

## Automatización (GitHub Actions)

La revisión semanal corre sola desde la nube: `.github/workflows/revision-semanal.yml` se dispara
el **lunes 06:00 COT** (pasada definitiva **completa** con `deepseek-v4-pro`: re-evalúa los 23
equipos sobre el último commit ≤ cierre) y el **miércoles y viernes 06:00 COT** (pasadas tempranas
en delta con `deepseek-v4-flash`: solo equipos con commits nuevos, notas preliminares), más
`workflow_dispatch` manual. El núcleo es `scripts/cron/evaluar-semana.py` con el calendario de
`scripts/cron/calendario.json` y el LLM del secret `OPENCODE_GO_API_KEY` (suscripción OpenCode Go,
endpoint `https://opencode.ai/zen/go/v1`). Escribe matrices, planillas, feedback, resumen y README,
y hace commit+push a master. Cada informe lleva una sección **overall** que revisa el proyecto
entero en HEAD, para notar entregas subidas tarde o correcciones posteriores al cierre. Guardas:
`estado-sX.json` e informes definitivos impiden re-procesar semanas cerradas.

**Rol del agente humano**: supervisar el output de Actions, corregir casos especiales (repo
invisible, excepción docente, re-barridos inesperados) y mantener calendario y fichas. El
procedimiento manual completo, por si hay que repetir algo a mano, sigue abajo.

## Ciclo semanal

Cada entrega cierra el **domingo a medianoche (Colombia, UTC-5)**. El trabajo automático es:

1. **Pasadas tempranas (miércoles y viernes 06:00 COT)**: revisión delta con `deepseek-v4-flash`
   de los equipos con commits nuevos desde la pasada anterior; las notas quedan marcadas como
   preliminares y pueden cambiar hasta el cierre.
2. **Pasada definitiva (lunes 06:00 COT)**: evaluación completa de los 23 equipos con
   `deepseek-v4-pro` sobre el último commit ≤ cierre. Es la que queda publicada y la que cuenta.

## Paso a paso

### 1. Cierres

`revisiones/<periodo>/cierres.env` guarda cada cierre como `CIERRE_SN=<ISO 8601>` (ej.
`CIERRE_S3=2026-08-24T05:00:00Z`). Añadir la línea de la semana nueva ANTES de revisar. Regla:
medianoche del domingo en UTC-5 → sumar 5 horas en Z.

### 2. Detectar actividad

```bash
python scripts/barrido-actividad.py --cierre "2026-08-31T05:00:00Z" --desde "2026-08-24T05:00:00Z"
```

Imprime, por repositorio: último commit ≤ cierre, commits nuevos desde el cierre anterior y
guarda el volcado en `revisiones/<periodo>/_meta/actividad-<semana>.txt` (gitignored). Los
equipos sin commits nuevos desde el cierre anterior se marcan «pendiente» y se revisan solo si
empujan antes del cierre.

### 3. Evaluar con agentes paralelos

Por cada equipo con actividad, un agente por lote (4-5 equipos). Prompt base (adaptar semana,
ficha y cierres):

> Rol: agente de revisión académica. Evalúa la Evidencia S<X> de N equipos clonando sus repos
> públicos de forma EFÍMERA (clon temporal que se BORRA al final) y escribiendo informes locales.
> NO modifiques repos de estudiantes (solo lectura). NO ejecutes su código.
>
> Kit: C:\Users\jairo\OneDrive - Universidad Tecnológica de Bolívar\Academia\Arquitectura de Software\arqsw-kit-revision
>
> LEE PRIMERO: fichas/semana-0X-evidencia-sX.md, CONTRATO.md, EQUIPOS.md, plantillas/planilla-equipo.md.
>
> - Cierre: `--until='<CIERRE_SX>'` con `git log -1 --format='%H %cI %s'` = estado calificado.
>   Commits posteriores (`--after`) = tardíos, solo hallazgo.
> - API de GitHub: úsala SOLO para `actions/runs` (1 llamada por equipo con workflow). Si 403,
>   sigue sin API y anótalo. Todo lo demás por protocolo git (no consume rate limit).
> - Clon: `DIR="$(mktemp -d)"; git clone --filter=blob:none --no-checkout -q "https://github.com/ISCOUTB/$REPO.git" "$DIR"`.
>   Lecturas con `git -C "$DIR" show "$HASH:ruta"`, `ls-tree`, `shortlog -sne HEAD`, `grep` de
>   secretos (CONTRATO §9). Al terminar cada equipo: `rm -rf "$DIR"`.
> - Estados: Cumple solo con evidencia citada (ruta:línea, hash, fecha, URL); No cumple con
>   evidencia; No verificado con motivo y qué haría falta.
> - Consolidar identidades (2 correos = 1 persona); NO atribuir cuentas por parecido de nombre.
> - Escribe `revisiones/<periodo>/<repo>/semana-0X-evidencia-sX.md` (encabezado, matriz de la
>   ficha, matriz transversal CONTRATO §11, sección **overall** del proyecto en HEAD, recuento
>   n/m con la nota sugerida marcada como propuesta al docente, pendientes, hallazgos), actualiza
>   `planilla.md` (fila de la semana, Sugerido = nota propuesta, tabla de contrato y arrastres con
>   lo que dice el overall) y añade la sección de la semana a `feedback.md` (sin nombres,
>   sin correos).
> - Al terminar, responde UNA línea por equipo: `<equipo> | <repo> | S<X> <hash8> <n>/<m> nota <x.x> | <hallazgos>`
>   con nota = 1 + 4×(n/m) (1 decimal), para el `resumen-sX.md` consolidado.

### 4. Nota sugerida (regla del docente, pública)

`nota = 1 + 4 × (filas Cumple ÷ total)` sobre la matriz DE LA FICHA (la transversal no entra),
redondeada a 1 decimal. **Por decisión del profesor se publica**, marcada siempre como «propuesta
al docente; la nota final se fija en Moodle»: va en el informe (`Recuento y nota sugerida`), en la
fila de la planilla y en el `resumen-sX.md` consolidado. En los cortes con escala publicada no se
aplica la fórmula; el nivel sugerido lo propone la ficha del corte.

### 5. Re-barrido post-cierre

Si hubo pasada temprana, repetir la detección tras el cierre y reevaluar SOLO a los equipos cuyo
hash calificado cambió o que no se habían revisado (delta). Sobre los informes existentes,
marcando «Revisión actualizada tras el cierre».

### 6. Publicación

```bash
git add README.md revisiones/ && git commit -m "Publicar revisión S<X> (N equipos)" && git push origin master
```

Qué SÍ se publica: fichas, contrato, EQUIPOS, matrices, planillas, feedback, resumen con notas
sugeridas (marcadas como propuesta) y `estado-sX.json`. Qué NO: correos, `cierres.env`, `_meta/`
(gitignored). Antes de empujar: `grep -rnE "[a-z0-9._%+-]+@[a-z0-9.-]+" revisiones/` debe dar
vacío o solo correos de bots.

### 7. Mantener el README

Al publicar una semana nueva: añadir columna «Matriz S<X>» a la tabla de evaluaciones publicadas
(cuidando el separador: una celda más), fusionar la sección de la semana en el `feedback.md` de
cada equipo y actualizar el árbol de estructura si cambió.

## Convenciones por equipo

`revisiones/<periodo>/<repositorio>/`:

- `feedback.md` — ÚNICO archivo de retroalimentación, una sección por semana (se añade, no se
  reemplaza). Sin nombres, notas, correos ni hashes.
- `semana-0X-evidencia-sX.md` — matriz de la ficha + transversal + recuento n/m + sección
  **overall** (estado global del proyecto en HEAD).
- `planilla.md` — acumulado del semestre: estado por entrega, lo que se arrastra, contrato,
  contribución.

## Casos especiales

- **Repo no visible** (`git ls-remote` falla): hallazgo «no visible», matriz en No verificado
  con motivo. No se pide acceso.
- **Sin commits antes del cierre**: semana No evaluable, matriz No verificado con motivo.
- **Entrega tardía**: se califica el último commit ≤ cierre; lo posterior es hallazgo.
- **Excepción docente** (ej. Verifacts S1-S2): solo si el docente lo pide; evaluar en HEAD y
  dejarlo escrito en el informe.
- **API agotada (403)**: todo por protocolo git; el «verde» de CI queda No verificado con motivo.
- **Sin ejecutar código de estudiantes, jamás.** Arranque/pruebas = No verificado con el comando
  anotado, salvo run de CI citable.

## Mantenimiento de fichas

Las fichas son a mano. Si cambia consigna/rúbrica en el aula, corregir la ficha (manda el aula).
No escribir pesos ni fechas en las fichas; los cierres viven en `cierres.env`.
