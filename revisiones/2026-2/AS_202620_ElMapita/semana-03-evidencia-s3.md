# Evidencia S3 · ElMapita

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `8e30f616` · 2026-08-22T16:12:55-06:00 (último commit ≤ cierre 2026-08-24T05:00:00Z) |
| Fecha/hora de revisión | 2026-08-23 22:25 (UTC-5), ANTES del cierre: si el equipo empuja antes de medianoche, el hash calificado puede cambiar |
| Comandos | `git clone --filter=blob:none --no-checkout`; `git log -1 --until='2026-08-24T05:00:00Z'`; `git ls-tree -r --name-only 8e30f616`; `git show 8e30f616:<ruta>`; sin llamada a la API (no hay `.github/workflows/`) |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md` → `# Solution Strategy {#section-solution-strategy}` | No cumple | La sección 4 de arc42 está VACÍA: solo el encabezado, seguido directamente de «Building Block View». La estrategia está bien documentada en el ADR y en la matriz, pero no en la sección 4. El ADR además referencia la sección como «Contexto y Fronteras» (etiqueta equivocada). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/comparativa-de-arquitecturas.md` | No cumple | Matriz ponderada (51/68/67) hecha a medida del proyecto y de alta calidad, pero compara sobre criterios C1–C7, no sobre los escenarios EC-01…EC-04 del árbol de utilidad: no se lee qué escenario mejora/empeora cada estilo. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico-propuesto.md` | Cumple | Nombre conforme a la convención. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico-propuesto.md` | Cumple | Título enuncia la decisión; contexto ligado a EC-01…EC-04 y a las restricciones, 3 alternativas con pros/contras, decisión con estructuras BE/FE, consecuencias positivas/negativas con mitigaciones. |
| Alternativas descartadas con su motivo | ADR §Alternativas Consideradas | Cumple | Capas descartada por acoplar Supabase y mezclar lógica 3D/geo con el framework; hexagonal por curva alta y boilerplate excesivo para 3 devs. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md:3` (columna ADR = «Pendiente»); `git grep -i 'adr' docs/arc42/arc42-template-EN.md` sin enlaces a `docs/adr/` | No cumple | La tabla de 8 columnas de `docs/aspectos.md` tiene ADR «Pendiente» aunque el ADR existe; los escenarios EC-01…EC-04 (en `arc42-template-EN.md` §10.2) no enlazan el ADR. Solo enlazan el ADR la matriz y el README. |
| Arranque con un solo comando documentado en el README | `README.md` §Inicio Rápido + `scripts/dev.sh` y `scripts/dev.ps1` | Cumple | El README documenta `./scripts/dev.sh` (y `dev.ps1` para Windows) como comando único que levanta backend+frontend; ambos scripts existen en la raíz de `scripts/`. Ejecución real: No verificado (regla del kit: no se ejecuta código del estudiante; comando anotado: `./scripts/dev.sh`). |
| Prueba automatizada en verde | `backend/src/app.controller.spec.ts`, `backend/test/app.e2e-spec.ts`, `frontend/test/widget_test.dart` | No verificado | Las pruebas existen y el README documenta `npm run test` y `flutter test`, pero no hay `.github/workflows/` ni run de CI y no se aportó evidencia de ejecución: el «verde» no se puede comprobar. Haría falta un pipeline o evidencia de ejecución entregada. |
| Estructura de paquetes correspondiente al estilo del ADR | `backend/src/modules/{auth,mapas,pois,ubicacion}/{domain,application,infrastructure}` · `frontend/lib/features/*` con domain/application/infrastructure/presentation · `src/shared/` y `lib/core/` | Cumple | Los módulos por feature con fronteras internas coinciden con el monolito modular del ADR. El ADR decía «semana 4: crear repositorios base», pero el esqueleto ya existe. |

Recuento: **4 de 9** criterios cumplidos.

## Matriz transversal (CONTRATO)

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | clon anónimo OK de `ISCOUTB/AS_202620_ElMapita` | Cumple | Público y con el nombre de la convención. |
| Estructura mínima presente | `git ls-tree -r --name-only 8e30f616` | Cumple | Las seis rutas existen (arc42 dentro de una plantilla única; C4 solo como PNG — desviaciones anotadas desde S2). |
| Estado calificado identificable | `8e30f616` 2026-08-22T16:12:55-06:00 | Cumple | Sin etiqueta; se registra hash+fecha del último commit anterior al cierre. |
| Nombres de ADR según la convención | `ls docs/adr` | Cumple | `0001-estilo-arquitectonico-propuesto.md` conforme. |
| ADR aceptados no reescritos | `git log --follow -- docs/adr/...`: un solo commit `aa16382` 2026-08-22 | Cumple | Creado de una vez, sin reescrituras. |
| `docs/ia.md` al día para la semana | `git show 8e30f616:docs/ia.md` → 0 bytes; último commit `df1e2f7` 2026-08-07 | No cumple | Sigue vacío desde S1; sin usos ni rechazos. |
| Sin credenciales en el repositorio ni en el historial | `git grep` con coincidencias solo en tipos y placeholders | Cumple | Las coincidencias son declaraciones de tipos (`password: string` en TS/Dart) y un badge placeholder (`token=abc123def456` en `backend/README.md:5`, del boilerplate de NestJS). No hay credenciales reales ni `.env` versionado (solo `.env.example`). |
| Contribución de todos los integrantes | `shortlog`: `RobotDRMX` (9) y «Rodrigo Vazquez Rico» (1); en S3 solo `RobotDRMX` (2 commits) | No cumple | 2 identidades para 3 integrantes; Angel Fabian Gutierrez Gomez y Diego Rosales Garza sin cuenta identificada; en el periodo S3 solo firma una cuenta. |

## Recuento

**4 de 9** criterios de la ficha cumplidos. La nota la fija el profesor (sin rúbrica publicada).

## No verificado / pendientes

- Prueba en verde: no verificable sin pipeline ni evidencia de ejecución (ver fila de la matriz).
- Ejecución real del arranque: no verificada por regla del kit (comando declarado: `./scripts/dev.sh`).
- Si el equipo empuja antes del cierre (2026-08-24T05:00:00Z), el hash calificado cambia.

## Hallazgos para la planilla

- La sección 4 de arc42 está vacía (solo el encabezado): la estrategia vive en el ADR y la matriz, no donde la ficha la pide.
- La matriz ponderada es excelente pero no referencia los escenarios EC-01…EC-04 del árbol de utilidad.
- El ADR no es alcanzable desde `docs/aspectos.md` (columna ADR «Pendiente») ni desde los escenarios.
- `docs/ia.md` sigue vacío (0 bytes) desde S1.
- Contribución: solo una cuenta firma en S3; dos integrantes sin identidad en el historial (arrastrado desde S1).
- Sin pipeline: pruebas existen pero el verde no está evidenciado.
- Lo positivo: ADR muy completo (consecuencias con mitigaciones, reglas de límites, plan de implementación), esqueleto BE/FE coherente con el monolito modular y scripts de arranque documentados.
