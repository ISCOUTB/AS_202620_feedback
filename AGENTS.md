# AGENTS.md · Cómo operar este repositorio semana a semana

Instrucciones para el agente que revisa los repositorios de los equipos. Leer antes de cada
sesión de revisión; vale más que cualquier intuición.

## Qué es esto

Repositorio público `ISCOUTB/AS_202620_feedback`: kit de revisión (fichas y contrato) + las
revisiones publicadas de cada equipo. Los estudiantes lo leen; por eso hay reglas estrictas de
qué se publica y qué no (ver «Publicación»).

## Ciclo semanal

Cada entrega cierra el **domingo a medianoche (Colombia, UTC-5)**. El trabajo es:

1. **Pasada temprana (opcional)**: el mismo domingo antes de la medianoche, para dar feedback
   rápido. Anotar que los hashes pueden cambiar.
2. **Pasada definitiva**: después del cierre (lunes), sobre el último commit ≤ cierre. Es la que
   queda publicada y la que cuenta.

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
>   ficha, matriz transversal CONTRATO §11, recuento n/m SIN nota, pendientes, hallazgos),
>   actualiza `planilla.md` (fila de la semana, Sugerido = «no se publica») y añade la sección
>   de la semana a `feedback.md` (sin nombres, sin notas, sin correos).
> - Al terminar, responde UNA línea por equipo: `<equipo> | <repo> | S<X> <hash8> <n>/<m> nota <x.x> | <hallazgos>`
>   con nota = 1 + 4×(n/m) (1 decimal). La nota SOLO va en esa línea: es registro local.

### 4. Nota sugerida (regla local del docente)

`nota = 1 + 4 × (filas Cumple ÷ total)` sobre la matriz DE LA FICHA (la transversal no entra).
Solo en `revisiones/<periodo>/resumen-sX.md`, **gitignored**. En los archivos publicados la
planilla dice «no se publica» y el informe solo «n de m».

### 5. Re-barrido post-cierre

Si hubo pasada temprana, repetir la detección tras el cierre y reevaluar SOLO a los equipos cuyo
hash calificado cambió o que no se habían revisado (delta). Sobre los informes existentes,
marcando «Revisión actualizada tras el cierre».

### 6. Publicación

```bash
git add README.md revisiones/ && git commit -m "Publicar revisión S<X> (N equipos)" && git push origin master
```

Qué SÍ se publica: fichas, contrato, EQUIPOS, matrices, planillas y feedback. Qué NO: notas
sugeridas, correos, `resumen-*.md`, `cierres.env`, `_meta/` (gitignored). Antes de empujar:
`grep -rn "1 + 4" revisiones/` debe dar vacío.

### 7. Mantener el README

Al publicar una semana nueva: añadir columna «Matriz S<X>» a la tabla de evaluaciones publicadas
(cuidando el separador: una celda más), fusionar la sección de la semana en el `feedback.md` de
cada equipo y actualizar el árbol de estructura si cambió.

## Convenciones por equipo

`revisiones/<periodo>/<repositorio>/`:

- `feedback.md` — ÚNICO archivo de retroalimentación, una sección por semana (se añade, no se
  reemplaza). Sin nombres, notas, correos ni hashes.
- `semana-0X-evidencia-sX.md` — matriz de la ficha + transversal + recuento n/m.
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
