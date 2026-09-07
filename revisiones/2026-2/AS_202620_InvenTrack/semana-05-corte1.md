# Semana 05 · Primer corte · InvenTrack

> **Revisión definitiva post-cierre — 2026-09-07.** Reemplaza la revisión preliminar del 2026-09-03, previa al cierre `2026-09-07T05:00:00Z`.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | etiqueta `corte-1` → `2988b03c39de2809371f4a21cf94f99cbe290ccd` · 2026-09-06T23:35:40-05:00 (anterior al cierre) |
| Cierre | `2026-09-07T05:00:00Z` |
| Comandos ejecutados | `git clone --filter=blob:none`; `git tag --list`; `git log`; `git checkout corte-1`; `git diff --stat ee484bf..corte-1`; `git grep` de secretos; `curl` a `actions/runs?per_page=10` (1 llamada) |
| Restricción asignada | No disponible en el kit, pero el repositorio sí declara su propio reto: **ASP-02, control de concurrencia en el módulo de inventario** (20 escrituras simultáneas sobre el mismo SKU, umbral p95 ≤ 400 ms) |

## ⚠️ Hallazgo crítico (léase antes que la matriz)

El equipo produjo una documentación excelente y muy completa del reto (ADR-0002, reporte de medición, comparación C4 línea-base-vs-post-reto, fila de aspectos, entrada de IA), pero **el mecanismo de solución que describen no existe en el código**:

- `git diff --stat ee484bf..corte-1` (línea base S4 → etiqueta `corte-1`) muestra que el **único código fuente tocado es un archivo de prueba nuevo** (`tests/inventario/test_concurrencia.py`, 39 líneas). Ningún archivo bajo `app/` cambió.
- `grep -rni "lock" --include=*.py .` no encuentra la palabra `lock` en ningún archivo Python del repositorio. El ADR-0002 dice textualmente que se adoptó un "Mecanismo de Exclusión Mutua en Memoria (Mutex/Lock asíncrono por SKU)" mediante `asyncio.Lock()`, pero `app/inventario/application/registrar_movimiento.py` y `app/inventario/infrastructure/in_memory_repository.py` son código síncrono plano, sin ningún lock, semáforo ni sección crítica protegida.
- `docs/retos/corte-1-medicion.md` reporta cifras exactas (p95 = 28 ms, p50 = 12 ms, 0 inconsistencias) pero no existe en el repositorio ningún código que mida tiempo (`grep -rn "p95|percentile|time\.|perf_counter" tests/ app/` no encuentra nada): esas cifras no son reproducibles a partir de lo que hay en el repositorio.
- La prueba (`tests/inventario/test_concurrencia.py`) sí existe, corre en CI y pasa, pero solo verifica que el stock final sea 80 tras 20 llamadas concurrentes — no mide latencia y no depende de ningún mecanismo de exclusión mutua, porque no hay ninguno que ejercer.

En síntesis: el diagnóstico y la decisión están narrados con gran detalle técnico, pero el "cambio implementado" y la "medición" que describen no están soportados por el código del repositorio. Esto es distinto de simplemente "no responder al reto": aquí se documenta una solución y un resultado que la evidencia del propio repositorio contradice.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` → `corte-1` → `2988b03` (2026-09-06T23:35:40-05:00), anterior al cierre | Cumple | — |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | No hay ruta en el repo | No verificado | Adjunto de Moodle no accesible desde el kit. |
| Impacto de la restricción localizado en requisitos, C4 y código | `docs/aspectos.md` (ASP-02/ESC-01), `docs/c4/containers.md:77-90` ("Línea Base vs. Estado Posterior al Reto") localizan el aspecto en requisitos y C4; pero la celda "Código" apunta a `app/inventario/`, que **no cambió** entre S4 y `corte-1` | No cumple | El impacto está bien situado en requisitos y C4, pero la celda de código no refleja ningún cambio real: el hueco de la cadena es precisamente ahí. |
| Línea base medida y verificable antes del cambio | `docs/adr/0002-...md` y `docs/retos/corte-1-medicion.md` solo afirman que "la ejecución previa sin control de concurrencia permitía condiciones de carrera", sin cifra ni procedimiento de la medición previa | No cumple | Afirmación cualitativa, no una cifra obtenida con herramienta y procedimiento. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/0002-control-concurrencia-memoria-inventario.md`: 3 alternativas con ventajas/desventajas, decisión, consecuencias, gobernanza y costo de reversión, ligado a ASP-02/ESC-01 | Cumple | Estructuralmente el mejor ADR de este lote; el problema no es su redacción sino que la decisión que documenta nunca se llevó a código (ver hallazgo crítico). |
| Cambio implementado y ejecutable de extremo a extremo | `git diff --stat ee484bf..corte-1` no muestra cambios en `app/`; no existe ningún `Lock`/`asyncio.Lock` en el código Python | No cumple | El mecanismo descrito en el ADR-0002 no está implementado; solo se agregó una prueba y documentación. |
| Límites declarados conservados tras el cambio | Sin cambio de código no hay límites nuevos que verificar; la arquitectura hexagonal (puertos/adaptadores) del ADR-0001 permanece intacta | No verificado | No aplica una comparación antes/después porque no hubo cambio de código. |
| Prueba que cubre el cambio, en verde en el pipeline | Run sobre `2988b03`, éxito, 2026-09-07T04:32:21Z; `tests/inventario/test_concurrencia.py` corre y pasa, verificando que 20 llamadas concurrentes dejan el stock en 80 | No cumple | La prueba pasa, pero no cubre el mecanismo que el ADR dice haber implementado (no existe), y no mide latencia. |
| Resultado contrastado con el umbral del escenario y reproducible | `docs/retos/corte-1-medicion.md` reporta p95=28ms, p50=12ms; no hay código de medición de tiempo en el repositorio que produzca esas cifras | No cumple | Cifras no reproducibles a partir del repositorio: no hay instrumentación de tiempo en `tests/` ni en `app/`. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md` enlaza ASP-02→ESC-01→ADR-0002→`app/inventario/`→prueba→`docs/retos/corte-1-medicion.md`, formalmente completa | No cumple | La cadena es navegable en forma, pero la celda "Código" no lleva a una implementación real del mecanismo declarado: la cadena se rompe en sustancia, no en forma. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md`, entrada "2026-09-06 · Reto Corte 1": acepta apoyo en pruebas y ADR, y **rechaza explícitamente** la sugerencia de usar Redis Distributed Locks o transacciones SQL pesimistas, "por considerar que agregaban infraestructura innecesaria al esqueleto actual en memoria" | Cumple | Entrada completa, referida a esta semana, con motivo técnico explícito. |
| Sustentación del reto | Sesión de sustentación | No verificado | Lo fija el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `https://github.com/ISCOUTB/AS_202620_InvenTrack` sin autenticación | Cumple | — |
| Estructura mínima presente | `git ls-tree -r --name-only corte-1` devuelve README.md, docs/adr/, docs/arc42/, docs/aspectos.md, docs/c4/, docs/ia.md | Cumple | arc42 es un único archivo `arc42-template-EN.md`, no secciones 1-12 separadas: desviación de forma. |
| Estado calificado identificable | Etiqueta `corte-1` → `2988b03`, anterior al cierre | Cumple | — |
| Nombres de ADR según la convención | `0001-usar-monolito-modular-con-hexagonal-por-modulo.md`, `0002-control-concurrencia-memoria-inventario.md` | Cumple | — |
| ADR aceptados no reescritos | ADR-0001 sin cambios posteriores a su aceptación (no verificado exhaustivamente su historial completo); ADR-0002 es nuevo, no reescribe al 0001 | Cumple | — |
| `docs/ia.md` al día para la semana | Entrada fechada 2026-09-06, referida explícitamente al "Reto Corte 1: Concurrencia y Medición de Inventario" | Cumple | — |
| Sin credenciales en el repositorio ni en el historial | `git grep` de patrones de secretos sin coincidencias (exit 1); sin `.env` versionado | Cumple | — |
| Contribución de todos los integrantes | `git shortlog -sne corte-1`: Jose Vargas/Josephva24 99, Esteban Peluffo 13, Felix Taborda/negro/FlexT21 22, jxviercarta-a11y 3 | Cumple | Los 4 integrantes tienen commits, aunque muy desigual (Javier Carta con solo 3). |

## Estado global del proyecto (overall · HEAD)

- **HEAD**: `c837d7d6e4979032303db407283aafbcee75a827` · 2026-09-07T01:12:16-05:00 (= 06:12:16Z), **posterior al cierre** (`2026-09-07T05:00:00Z`).
- Entre la etiqueta `corte-1` y HEAD hay 2 commits más ("Pequenos detalles", "docs: definir Flutter como frontend", "datalle") que llegaron después del cierre: no se calificaron, pero quedan anotados como entrega tardía.
- CI en verde tanto en `corte-1` como en HEAD.
- El estado post-cierre agrega una definición de frontend (Flutter) que no estaba en `corte-1`.

## Nivel de rúbrica sugerido (propuesta al docente, NO nota aplicada)

| Criterio | Nivel sugerido | Puntaje | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Básico | 0,60 | Distingue síntoma/causa/riesgo con redacción sofisticada, pero sin una cifra de línea base medida (solo afirmación cualitativa). |
| Alternativas y decisión | Competente | 0,80 | ADR-0002 con 3 alternativas, fuerzas, decisión y consecuencias ligadas al escenario ASP-02/ESC-01; **pero la decisión documentada nunca se implementó** (ver hallazgo crítico), lo que el docente puede considerar al ponderar este puntaje. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | `git diff --stat` confirma cero cambios en `app/`; el mecanismo de concurrencia declarado no existe en el código. |
| Pruebas, medición y trazabilidad | Básico | 0,60 | Existe una prueba funcional en verde que no demuestra el mecanismo declarado; las cifras de latencia reportadas no son reproducibles desde el repositorio. |
| Sustentación del reto | Lo fija el docente | pendiente | No se puntúa desde el repositorio. |
| **Subtotal técnico** | | **2,00 / 4,00** | Propuesta al docente; la nota final se fija en Moodle. **Se recomienda al docente verificar en sustentación, en vivo, dónde está implementado el lock que el ADR-0002 describe**, dado que el repositorio no lo muestra. |

## Recuento

3 de 12 criterios Cumple (etiqueta, calidad estructural del ADR, registro de IA).

## No verificado

- PDF de dos páginas en Moodle.
- Conservación de límites tras el cambio (no hubo cambio de código que verificar).
- Sustentación del equipo.

## Hallazgos

- **Crítico:** el ADR-0002 y el reporte de medición describen un mecanismo de exclusión mutua (`asyncio.Lock()` por SKU) y cifras de latencia (p95=28ms) que no están respaldados por ningún código del repositorio; `app/inventario/` no cambió entre la línea base S4 y la etiqueta `corte-1`.
- La prueba de concurrencia sí existe, corre en CI y pasa, pero no mide latencia y no depende de ningún lock real.
- El resto de la documentación del reto (C4 línea-base-vs-post-reto, utility-tree, matriz comparativa de estilos, aspectos.md) es de buena calidad formal y consistente entre sí, lo que hace más difícil detectar a simple vista que el código no acompaña la narrativa.
- 2 commits llegaron después del cierre (definición de Flutter como frontend); no afectan la calificación de `corte-1` pero quedan anotados.
- arc42 en archivo único en vez de secciones 1-12 separadas.
- Contribución desigual entre integrantes (Javier Carta con solo 3 commits en todo el historial).

## Correcciones del equipo

No se encontró `correcciones.md` en la raíz del repositorio ni en HEAD. No aplica esta sección.

## Preguntas para la sustentación

1. Muestren en vivo, en el código, dónde está implementado el mecanismo de exclusión mutua (`asyncio.Lock()` por SKU) que describe el ADR-0002: `app/inventario/application/registrar_movimiento.py` y `app/inventario/infrastructure/in_memory_repository.py` no contienen ningún lock.
2. ¿Con qué herramienta y procedimiento obtuvieron las cifras p95=28ms y p50=12ms del reporte de medición? El repositorio no contiene código de instrumentación de tiempo.
3. ¿Cuál fue el resultado de ejecutar la prueba de concurrencia *antes* de cualquier cambio, como línea base cuantitativa (no solo la afirmación de que "permitía condiciones de carrera")?
