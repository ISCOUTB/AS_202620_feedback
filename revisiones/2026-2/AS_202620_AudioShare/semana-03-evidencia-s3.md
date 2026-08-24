# Evidencia S3 · AudioShare

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `024ae3435` · 2026-08-23T23:47:38-05:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-24, DESPUÉS del cierre. Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo |
| Primera revisión | `419814fe` · 2026-08-23T21:15:38-05:00 (quedó sin efecto; todo se recalifica sobre el hash definitivo) |
| Commits tardíos | ninguno: `git log --after='2026-08-24T05:00:00Z'` no devuelve commits |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git ls-tree -r --name-only`; `git show`; `git grep` de secretos (exit 1). Sin API de actions: el árbol no tiene `.github/workflows/` |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/src/04_solution_strategy.adoc` | No cumple | La sección quedó desincronizada con el ADR: §4.1 dice «Se evaluarán tres alternativas… la decisión se documentará en el ADR» y §4.7 lista como pendiente la «Selección definitiva entre capas, hexagonal o monolito modular», cuando el ADR 0001 ya existe y el esqueleto ya está montado. Los umbrales de §4.2 (100 ms, 200 ms) sí están atados a EC-01…EC-03, pero no se nombran tácticas concretas (p. ej. reloj común, buffer de jitter), solo objetivos. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/Matriz_Comparativa.md` | No cumple | Los tres estilos están y las filas son propias del proyecto (aislamiento de la lógica de sincronización, intercambiabilidad de protocolos, eventos en tiempo real…), pero ninguna fila es un escenario del árbol de utilidad: no hay EC-01…EC-04 ni se lee qué escenario mejora/empeora con cada estilo. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-usar-monolito-modular.md` | Cumple | Nombre conforme al filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$` y enuncia la decisión. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-usar-monolito-modular.md` | Cumple | Contexto, Alternativas A/B/C, Decisión («Se elige Monolito Modular») y Consecuencias (positivas, negativas, riesgos, qué revisar si cambia) presentes. Observaciones: el H1 «Selección del estilo arquitectónico» no enuncia la decisión; estado «propuesto»; el campo «Escenario de calidad relacionado» dice «EC-nn» (placeholder). |
| Alternativas descartadas con su motivo | ADR §A y §B | Cumple | Capas descartada por separación menos orientada a las funcionalidades; hexagonal por complejidad inicial innecesaria para la etapa actual. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (sin enlace al ADR); `docs/escenarios_calidad.md` (sin enlace al ADR) | No cumple | `aspectos.md` enlaza EC-01…EC-04 pero no el ADR, y no usa la tabla de 8 columnas; ningún escenario enlaza al ADR, y el propio ADR referencia «EC-nn» en vez del escenario que lo motiva. Solo lo enlazan README y la sección 4. |
| Arranque con un solo comando documentado en el README | `README.md` §Cómo arrancar + `package.json` | Cumple | Documenta requisitos (Node 20+), `npm install`, `npm run dev` y comprobación con `curl http://localhost:3000/health`. `package.json` existe con el script `dev` (tsx). Ejecución real: No verificado (regla del kit: no se ejecuta código del estudiante). |
| Prueba automatizada en verde | `tests/health.test.ts` + `vitest.config.ts` + script `test` | No verificado | La prueba existe (verifica `/health` y los tres módulos del ADR) y `npm test` está documentado, pero no hay `.github/workflows/` ni run de CI ni evidencia de ejecución aportada: el «verde» no se puede comprobar. |
| Estructura de paquetes correspondiente al estilo del ADR | `src/modules/{session,audio,sync}/index.ts`, `src/shared/`, `src/app.ts`, `src/server.ts` | Cumple | Monolito modular con fronteras declaradas: cada módulo expone su API solo por `index.ts`; `app.ts` es el composition root que cablea los módulos sin lógica de negocio, tal como lo documenta el README. Coherente con el ADR. |

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_AudioShare` | Cumple | Nombre correcto, público. |
| Estructura mínima presente | `git ls-tree -r --name-only 024ae3435` | Cumple | Las seis rutas existen; arc42 sigue en AsciiDoc (`docs/arc42/src/*.adoc` + `arc42-template.adoc`), desviación de formato ya anotada, no ausencia. |
| Estado calificado identificable | `024ae3435` · 2026-08-23T23:47:38-05:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | Cumple | `0001-usar-monolito-modular.md` conforme. |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/0001-usar-monolito-modular.md` | Cumple | Iterado 5 veces el mismo día de su creación (`84e2e03`→`f5641c8`, 2026-08-23 21:45–23:13), pre-aceptación (estado «propuesto»), así que no viola la regla de aceptados. |
| `docs/ia.md` al día para la semana | `git log -- docs/ia.md`: `024ae34` 2026-08-23; fila «Semana 3» presente | No cumple | Se actualizó en S3 (consulta sobre estilos → matriz), pero la tabla sigue sin registrar qué se rechazó y por qué en ningún uso. |
| Sin credenciales en el repositorio ni en el historial | `git grep` de secretos (exit 1), sin `.env` versionado (solo `.env.example`) | Cumple | Sin coincidencias. |
| Contribución de todos los integrantes | commits en el periodo S3: Santiago (11), Elian (11), Yeiver (7), Vincent (6) | Cumple | Los 4 integrantes firman commits dentro del periodo S3 (17–23 ago). Yeiver, ausente en la primera revisión, reapareció con el ADR. |

## Recuento

**5 de 9** criterios de la ficha cumplidos (1 No verificado). La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Prueba en verde: sin pipeline ni evidencia de ejecución (ver fila de la matriz).
- Ejecución real del arranque: No verificado por regla del kit (comando declarado: `npm run dev`).
- Sin llamada a la API de actions: el repositorio no tiene `.github/workflows/`.

## Hallazgos para la planilla

- El equipo cerró el hueco de la primera revisión: ADR 0001 completo, esqueleto monolito modular con paquetes coherentes, README con comando de arranque y prueba, y los 4 integrantes con commits en S3.
- La sección 4 quedó desincronizada: sigue diciendo que la selección del estilo está «pendiente» aunque el ADR ya decide y el esqueleto ya existe; además no nombra tácticas.
- La matriz comparativa no referencia los escenarios del árbol de utilidad (EC-01…EC-04).
- El ADR no es alcanzable desde `aspectos.md` ni desde el escenario que lo motiva; el campo «Escenario de calidad relacionado» es el placeholder «EC-nn»; estado «propuesto» en vez de aceptado.
- `docs/aspectos.md` sigue sin la tabla de 8 columnas (arrastrado desde S1).
- `docs/ia.md` sigue sin la columna de qué se rechazó y por qué (arrastrado desde S2).
- Sin commits tardíos: todo lo empujado entró antes del cierre.
