# Primer corte · reto de línea base arquitectónica · uniTeam

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión manual preliminar
> hecha antes del cierre (2026-09-03). Se repite sobre el estado admisible tras
> `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Etiqueta `corte-1` | Ausente — `git tag --list` no devuelve etiquetas |
| Estado calificado (fallback) | `dc14298c32a4fde0956266b0300063c24d7a9486` · 2026-08-29T11:49:10-05:00 · "Línea base de ESC-01 medida..." (último commit ≤ cierre; también es HEAD: sin actividad nueva entre la revisión preliminar y el cierre) |
| Cierre | 2026-09-07T05:00:00Z |
| Comandos ejecutados | `git clone --filter=blob:none`, `git tag --list`, `git log` completo, `ls docs/adr`, lectura de `docs/adr/0005-...`, `docs/aspectos.md`, `docs/calidad/mediciones/esc-01-linea-base.md`, `docs/calidad/escenarios-calidad.md` (ESC-03), `test/test_autenticacion.py`, `test/test_corte_vertical.py`, `docs/ia.md`, `git shortlog -sne HEAD`, `git grep` de credenciales, `curl` a la API de Actions |
| `correcciones.md` | No existe en el repositorio |

## Nota metodológica

No se encontró en el kit ni en el repositorio una declaración explícita de "esta es la
restricción asignada / esta es la respuesta al corte 1". Sin embargo, el commit `984922e`
(2026-08-29T03:20:19-05:00, "Autenticación con OpenID Connect y retirada de la cabecera
X-Usuario") y su ADR (`docs/adr/0005-...`) tienen exactamente la forma de una respuesta a una
restricción: diagnostican un problema real del sistema (identidad falsificable vía cabecera
`X-Usuario`), lo ligan a una restricción legal (L1, protección de datos personales) y a un
escenario de calidad (ESC-03), comparan alternativas, deciden, implementan y prueban. Por
tanto se evalúa este trabajo como la respuesta más plausible al reto del corte 1, en vez de
marcar todo como "No verificado" por falta de una etiqueta explícita — la evidencia es legible
y hay que pronunciarse (CONTRATO §13). Esto es una inferencia razonada, no una confirmación:
se dice así en cada fila y queda como pregunta para la sustentación.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` vacío; fallback `dc14298` (anterior al cierre) | No cumple | Sin etiqueta. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | `docs/ia.md` documenta que el PDF se excluye deliberadamente del repositorio (decisión S2); Moodle fuera del alcance de este kit | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/adr/0005-delegar-la-autenticacion-en-un-proveedor-oidc.md` liga el problema (cabecera `X-Usuario` falsificable) a la restricción legal L1, al escenario ESC-03 y al aspecto A-09 (`docs/aspectos.md:25`); C4 nivel 2 ya declaraba el "Proveedor de identidad" | Cumple | Con la salvedad de la nota metodológica: se infiere que este es el reto, no está declarado como tal. |
| Línea base medida y verificable antes del cambio | No hay medición cuantificada del defecto de autenticación antes del cambio (ni porcentaje de suplantación exitosa, ni prueba de concepto fechada); `docs/calidad/mediciones/esc-01-linea-base.md` mide un escenario distinto (ESC-01, latencia del tablero) | No cumple | El diagnóstico es cualitativo ("cualquiera podía afirmar ser quien quisiera"), no una cifra con procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/0005-...md`: tabla de 3 opciones evaluadas (OIDC / usuarios propios / mantener la cabecera), decisión, consecuencias positivas/negativas/pendientes, trazabilidad a aspecto/C4/código/pruebas/escenario | Cumple | Nivel competente: alternativas, fuerzas y consecuencias ligadas al escenario. |
| Cambio implementado y ejecutable de extremo a extremo | `app/api/seguridad.py`, `web/lib/oidc.ts`, `scripts/emisor_dev.py`; `README.md:17-29` mantiene `docker compose up` como único comando de arranque, incluyendo el emisor OIDC de desarrollo | Cumple | Arranque reproducible verificado en el README; no se ejecutó el código, solo se leyó la documentación y el compose. |
| Límites declarados conservados tras el cambio | C4 nivel 2 (`docs/c4/nivel2-contenedores.md:22,60,62,93`) ya preveía el contenedor "Proveedor de identidad"; el cambio lo hace efectivo sin agregar elementos no declarados | Cumple | Coherente con el C4 previo. |
| Prueba que cubre el cambio, en verde en el pipeline | `test/test_autenticacion.py` cubre rechazo sin credencial, esquema distinto de Bearer, firma ajena y token caducado; run `984922ed` (commit del cambio) concluyó `success`: `https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/33263778285` | Cumple | Run anterior al fallback/HEAD, verde. |
| Resultado contrastado con el umbral del escenario y reproducible | Las pruebas de `test_autenticacion.py` son funcionales (pasa/falla), no una medición de carga contra el umbral de ESC-03 (100% denegado, 0 campos, auditoría ≤ 1 s); no se encontró una medición de ese umbral específico | No cumple | Hay prueba funcional, no medición reproducible con herramienta/carga/procedimiento para ESC-03. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:25` (fila A-09): aspecto → RF-02 → C4 (Proveedor de identidad) → ADR 0005 → `seguridad.py`/`oidc.ts` → `test_autenticacion.py` → ESC-03; cada celda enlaza a un artefacto que existe | Cumple | Fila completa y navegable. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:73` registra el cambio de OIDC como asistido por IA ("Sí, revisado por el equipo") sin detalle de rechazo; las entradas con rechazo y motivo técnico (D-006, D-007) están fechadas el mismo día pero atribuidas a "Entrega S4 — Corte vertical", no al trabajo de autenticación | No cumple | No hay una entrada de `docs/ia.md` que documente qué se aceptó/corrigió/rechazó específicamente sobre el diseño o la implementación de OIDC. |
| Sustentación del reto | No verificable desde el repositorio | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `ISCOUTB/AS_202620_uniTeam` exitoso | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | `git ls-tree` en HEAD: `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md`, `README.md` | Cumple | Las seis rutas están. |
| Estado calificado identificable | Sin etiqueta `corte-1`; fallback `dc14298` = HEAD, anterior al cierre | No cumple | Falta la etiqueta. |
| Nombres de ADR según la convención | `0001-acotar-el-stack-a-cuatro-opciones.md` … `0005-delegar-la-autenticacion-en-un-proveedor-oidc.md` | Cumple | Convención respetada. |
| ADR aceptados no reescritos | `docs/ia.md` (D-003) y el historial no muestran ediciones de un ADR ya aceptado; ADR 0001 declara su propio reemplazo por decisiones posteriores de forma explícita | Cumple | Evolución declarada, sin reescritura silenciosa. |
| `docs/ia.md` al día para la semana | Último cambio en el mismo commit fallback (`dc14298`, 2026-08-29); registra trabajo hasta esa fecha, incluida la mención de OIDC | Cumple parcialmente | Hay actividad de esa fecha, pero sin la entrada específica de aceptación/rechazo de IA para OIDC que exige el criterio 11 de la ficha; a efectos de esta fila transversal (actualización temporal) se considera al día. |
| Sin credenciales en el repositorio ni en el historial | `git grep -nIE …`: única coincidencia son nombres de variable (`token: string`, parámetros de función), sin valores; `.env` no versionado | Cumple | Sin hallazgos reales. |
| Contribución de todos los integrantes | `git shortlog -sne HEAD`: super-gremlin (15), Ian Novoa (11, = Ian Novoa Carrillo), JuanB (10, atribuible por iniciales a Juan Jose Bustamante More, contenido de sus commits es C4/README), Julio Cesar Emiliani (10, = Julio Cesar Emiliani Ramos), Daniel Manjarres Herrera (4, = Daniel Isaac Manjarres Herrera) | Cumple | Los cuatro integrantes tienen una identidad razonablemente atribuible con contribución visible; `super-gremlin` queda como identidad no confirmada adicional (posiblemente una cuenta más de alguno de ellos), sin que eso reste contribución a los cuatro. |

## Estado global del proyecto en HEAD

- HEAD = fallback `dc14298` (sin commits nuevos desde la revisión preliminar del 2026-08-29 hasta el cierre).
- El proyecto tiene una base técnica sólida: corte vertical completo (proyectos, tareas, autorización por pertenencia, auditoría), aplicación web, CI en verde, trazabilidad amplia en `docs/aspectos.md` y una medición reproducible de ESC-01.
- El trabajo de autenticación OIDC (ADR 0005) es, con inferencia razonada, la respuesta más plausible al reto del corte 1: diagnostica un defecto real de seguridad, decide entre alternativas y lo implementa con pruebas en verde. Lo que le falta para un corte 1 completo es una etiqueta `corte-1`, una línea base cuantificada del defecto de autenticación, una medición posterior contrastada contra el umbral de ESC-03 y una entrada de `docs/ia.md` específica sobre esa pieza de trabajo.
- Sigue sin resolverse la identidad `super-gremlin`, con más commits que ningún otro colaborador nombrado.

## Nivel de rúbrica sugerido (propuesta al docente; la nota final se fija en Moodle)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Básico | 0,60 | Localiza el problema y su impacto en C4/ADR/aspectos, pero sin una línea base medida (cifra + procedimiento) del defecto de autenticación. |
| Alternativas y decisión | Competente | 0,80 | ADR 0005 registra alternativas, fuerzas, decisión y consecuencias ligadas a ESC-03; no llega a sobresaliente por no declarar qué dato revisaría la decisión ni el costo de reversión. |
| Aplicación sobre el corte vertical | Competente | 0,80 | Funciona de extremo a extremo, arranca con un comando y conserva los límites del C4; no se observó degradación controlada ante condición adversa (sobresaliente). |
| Pruebas, medición y trazabilidad | Básico | 0,60 | Cadena navegable en `docs/aspectos.md` y CI en verde, pero sin contraste contra el umbral específico de ESC-03 (competente exige esa comparación). |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico** |  | **2,80 / 4,00** | Propuesta al docente; no es la nota final. |

## Recuento

6 de 12 criterios de la ficha cumplen. En la matriz transversal: 7 de 8 cumplen (1 parcial).

## No verificado

- PDF de dos páginas en Moodle.
- Que el trabajo de OIDC sea, formalmente, "el reto asignado" (inferencia razonada, no confirmada por el equipo).
- Identidad de `super-gremlin`.
- Sustentación del reto.

## Hallazgos

- Sin etiqueta `corte-1`; se calificó sobre el último commit ≤ cierre (`dc14298`), idéntico al HEAD actual — sin actividad nueva desde la revisión preliminar.
- El trabajo de autenticación OIDC tiene la forma de una respuesta sólida a una restricción (diagnóstico, ADR competente, implementación end-to-end, pruebas en verde), pero le falta línea base cuantificada, medición posterior contra el umbral de ESC-03 y una entrada de IA propia.
- Contribución de los cuatro integrantes razonablemente identificable, con una identidad adicional (`super-gremlin`) sin confirmar.
- Sin credenciales en el repositorio ni en su historial.

## Preguntas para la sustentación

- ¿Fue la vulnerabilidad de la cabecera `X-Usuario` la restricción que les asignó el docente, o responde a otra cosa? ¿Cuál fue la restricción formalmente asignada?
- ¿Cómo midieron —con cifra y procedimiento— qué tan explotable era la cabecera `X-Usuario` antes del cambio?
- ¿Ejecutaron alguna medición de ESC-03 (porcentaje de solicitudes denegadas, tiempo de auditoría) después del cambio, distinta de las pruebas funcionales?
- ¿A qué integrante corresponde la identidad `super-gremlin`, con más commits que cualquier otro colaborador nombrado?
