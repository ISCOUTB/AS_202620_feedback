# Evidencia S4 · arc42, C4 y corte vertical

| | |
|---|---|
| `idnumber` en Moodle | `arqsw:evidencia-s4` |
| Semana | 4 |
| Corte | Primer corte |
| Tipo | grupal, nota única del equipo |
| Qué sube el estudiante | enlace al repositorio o al commit, y opcionalmente un PDF de una página |
| Estado que se califica | commit vigente al cierre de la actividad |
| Consecuencia | es **requisito de acceso** al primer corte: sin ella el equipo no ve la tarea de corte |

Antes de empezar, lee [CONTRATO.md](../CONTRATO.md). Su matriz transversal se rellena además de la
de esta ficha.

## Qué se pidió

Incremento de arc42 en las **secciones 1 a 6, 9 y 10**, con el **glosario iniciado**; **C4
niveles 1 y 2**; **corte vertical ejecutable** documentado en el README; y **una fila de
`docs/aspectos.md` completa hasta la columna Pruebas**.

El corte vertical se construye sobre el esqueleto de la semana 3 y atraviesa interfaz, lógica y
persistencia, con al menos una prueba automatizada que ejercite el recorrido completo. El
recordatorio de la semana pide además verificar que **los límites del código coincidan con los
del diagrama**, porque es lo primero que se revisa en el corte.

Fuente canónica: la actividad en el aula y su sección en `docs/curso-arqsw-guia.md`. Si divergen,
manda el aula.

## Instrucciones para el agente de revisión

1. **Sitúate en el estado que se califica.** Clona y posiciónate en el último commit anterior al
   cierre que publica la actividad. Registra hash y `%cI`; todo lo que sigue se mira ahí.
   ```bash
   git -C "$DIR" log -1 --format='%H %cI' --until="$CIERRE"
   git -C "$DIR" checkout <hash>
   ```
2. **Inventaría arc42.** Lista los archivos de `docs/arc42/` y localiza cada sección exigida. La
   plantilla oficial reparte una sección por archivo, pero un solo archivo con encabezados
   también vale: lo que se comprueba es que la sección esté **redactada**, no el número de
   archivos.
   ```bash
   ls docs/arc42/
   grep -rniE '^#{1,3} ?(1|2|3|4|5|6|9|10|12)[.)]? ' docs/arc42/ | head -40
   ```
3. **Descarta texto de plantilla.** Una sección con el texto de arc42 sin sustituir cuenta como
   no redactada. Busca los rastros habituales y comprueba a ojo las secciones cortas.
   ```bash
   grep -rniE '<[a-z ]+>|\bTODO\b|lorem ipsum|Contents\b|Motivation\b|Form\b|Examples\b|arc42 template' docs/arc42/ | head -40
   ```
4. **Comprueba las secciones 5 y 6, que son las nuevas de la semana.** La 5 (bloques de
   construcción) debe descomponer el sistema en partes con responsabilidad declarada; la 6 (vista
   de ejecución) debe describir al menos un escenario de interacción entre esas partes. Un
   diagrama sin texto que lo interprete no basta.
5. **Comprueba la 9 y la 10.** La 9 (decisiones) tiene que apuntar a los ADR existentes, no
   repetirlos. La 10 (requisitos de calidad) tiene que seguir siendo coherente con los escenarios
   de la semana 2: si el alcance cambió, la sección lo refleja.
6. **Glosario iniciado.** Sección 12 con términos del dominio propio del proyecto. Una lista de
   términos genéricos de arquitectura no es el glosario del sistema.
7. **C4 niveles 1 y 2.** Localiza los diagramas y verifica coherencia entre niveles: todo
   contenedor del nivel 2 pertenece al sistema que el nivel 1 dibuja, y los actores externos del
   nivel 1 reaparecen conectados en el 2. Comprueba leyenda y flechas etiquetadas.
   ```bash
   ls docs/c4/
   ```
   Anota si los diagramas están **como código** (`.puml`, `.dsl`, `.mmd`, Structurizr) o solo como
   imagen: no se exige aquí, pero cuenta en el criterio de trazabilidad del primer corte.
8. **Correspondencia diagrama y código.** Contrasta los contenedores y componentes del C4 con la
   estructura de directorios del repositorio. Nombra en Observaciones al menos una
   correspondencia concreta encontrada y cualquier contenedor dibujado que no tenga código.
   ```bash
   git -C "$DIR" ls-tree -r --name-only HEAD | grep -v '^docs/' | awk -F/ 'NF>1{print $1"/"$2}' | sort -u | head -30
   ```
9. **Corte vertical.** Sigue el recorrido en el código: punto de entrada de interfaz, lógica que
   decide y persistencia que guarda. Cita las tres rutas. Si falta un tramo, di cuál.
10. **Arranque con un solo comando.** El README declara requisitos previos y **un** comando de
    arranque. Compruébalo por lectura y, si vas a ejecutarlo, hazlo en contenedor desechable; si
    no lo ejecutas, marca No verificado y anota el comando declarado.
11. **Prueba del recorrido completo.** Localiza la prueba que ejercita el corte vertical de punta
    a punta y comprueba que el pipeline la ejecutó en verde en un run de esa semana.
    ```bash
    curl -s "https://api.github.com/repos/ISCOUTB/$REPO/actions/runs?per_page=20" \
      | python -c "import json,sys;[print(r['created_at'],r['name'],r['conclusion'],r['html_url']) for r in json.load(sys.stdin)['workflow_runs']]"
    ```
12. **Fila de aspectos completa hasta Pruebas.** Al menos una fila de `docs/aspectos.md` con ID,
    aspecto, requisito, C4, ADR, código y pruebas. Sigue cada celda hasta donde apunta: una ruta
    que no existe o un ADR que no está es un hueco, aunque la celda tenga texto.

**Qué no hacer aquí:** no evaluar la calidad del código ni el estilo, que no es lo que pide la
evidencia; no exigir C4 nivel 3, que se pospone a la semana 6; no penalizar la ausencia de lógica
de negocio más allá del corte vertical.

## Matriz de cumplimiento

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | rutas y encabezados en `docs/arc42/`, con el filtro de plantilla sin coincidencias | | |
| arc42 sección 9 al día y enlazada con los ADR existentes | sección 9 citando `docs/adr/NNNN-*.md` | | |
| arc42 sección 10 coherente con los escenarios de la semana 2 | sección 10 y su correspondencia con la tabla de escenarios | | |
| Glosario iniciado con términos del dominio | sección 12 con términos propios del sistema | | |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | archivos en `docs/c4/` y correspondencia de actores y contenedores | | |
| Límites del C4 nivel 2 correspondientes a la estructura del código | contenedor del diagrama frente a directorio o servicio del repositorio | | |
| Corte vertical que atraviesa interfaz, lógica y persistencia | las tres rutas del recorrido, citadas | | |
| Arranque documentado con un solo comando | sección del README con requisitos previos y comando | | |
| Prueba automatizada del recorrido completo, en verde | ruta de la prueba y URL del run que la ejecutó | | |
| Fila de `docs/aspectos.md` completa hasta la columna Pruebas | fila citada, con cada celda verificada hasta su destino | | |

## Cierre

Recuento: **n de m criterios cumplidos**, con m el número de filas de esta matriz.

Las evidencias semanales **no tienen rúbrica publicada**: se califican con calificación directa
sobre la escala UTB y la nota la fija el docente. El kit no propone nota aquí, porque sería
calificar con una regla que el estudiante no vio.

Deja anotado para el primer corte, que sí tiene rúbrica: si los diagramas están como código, si
cada ADR enlaza el commit que lo implementa y si ya hay alguna medición de línea base.
