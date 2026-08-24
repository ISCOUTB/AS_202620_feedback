# Evidencia S3 · Recobra

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `cb5c57956e2b712a965b624364831ecf2fed93ac` · 2026-08-23T23:44:12-05:00 (`segunda parte , funcional del esqueleto , con instalacion de npm en node`) |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre 2026-08-24T05:00:00Z) |
| Revisión actualizada tras el cierre | el equipo empujó después de la primera revisión (que vio `f31607e`); hash calificado definitivo `cb5c579`, último commit ≤ cierre. Sin commits posteriores al cierre. |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`. Sin API de CI (no hay `.github/workflows/`). |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04-estrategia-solucion.md`: §4.1 contexto y restricciones, §4.3 decisión, §4.4 principios derivados, §4.5 consecuencias | No cumple | La estrategia está ahora bien fundamentada (atributo prioritario disponibilidad, restricciones S1/S2), pero siguen faltando tácticas concretas ligadas a los escenarios S1–S7 (timeouts, reintentos, colas, verificación de reclamación…); §4.4 son principios de paquetes, no tácticas. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | §4.2 tabla ponderada (testabilidad, aislamiento, curva, velocidad, disponibilidad, mantenimiento) | No cumple | Mejora sustancial frente a la matriz genérica anterior: pesos derivados de las prioridades del proyecto y celdas justificadas. Pero no compara contra el árbol de utilidad: ninguna fila por escenario S1–S7 que diga qué escenario mejora/empeora con cada estilo. Además queda `docs/matriz_arquitectura.md` con la matriz genérica vieja y una decisión («hexagonal como monolito modular») que contradice el ADR actual. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Pasa el filtro (el viejo `docs/ADR/01-arquitectura-base.md` se eliminó en `cb5c579`). |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md`: Contexto, Alternativas consideradas (3), Decisión, Consecuencias, Referencias | Cumple | Contexto con atributos priorizados y restricciones reales; consecuencias con ganancias, riesgos y criterio de reapertura. |
| Alternativas descartadas con su motivo | ídem: capas («En contra: … juega en contra de la disponibilidad») y monolito modular («En contra: sin puertos explícitos…») | Cumple | Motivos de descarte explícitos y ligados a los atributos priorizados; la decisión justifica el rechazo. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (narrativo, sin tabla y sin ningún enlace); `docs/escenarios_calidad.md` sin enlace al ADR; el ADR solo es alcanzable desde §4.3 | No cumple | Ni aspectos ni los escenarios enlazan al ADR. |
| Arranque con un solo comando documentado en el README | `README.md` «Cómo levantar el esqueleto»: `npm install && npm start` + `package.json` (scripts start/dev/test) | Cumple | Comando documentado con requisitos (Node 18+). Ejecución real: No verificado por regla del kit (no se ejecuta código del estudiante). |
| Prueba automatizada en verde | `tests/health.test.js` (`node --test` sobre GET /health) | No verificado | La prueba existe, pero no hay `.github/workflows/` ni evidencia de ejecución aportada. Haría falta un run de CI o la evidencia de Moodle. |
| Estructura de paquetes correspondiente al estilo del ADR | `src/server.js` y `src/infrastructure/adapters/http/server.js` únicamente | No cumple | El ADR y el README declaran `domain/entities`, `domain/ports`, `application/use-cases`, `infrastructure/adapters/persistence`… que no existen en git (solo directorios declarados, sin archivos). Con un solo adaptador HTTP no se materializa la separación puertos/adaptadores que exige el estilo. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, nombre de convención y público | Cumple | clon sin autenticación de `github.com/ISCOUTB/AS_202620_Recobra`. |
| Estructura mínima presente | Cumple | `docs/arc42/`, `docs/adr/`, `docs/c4/` (C4 como Mermaid en `docs/c4/README.md`), `docs/aspectos.md`, `docs/ia.md`, `README.md` en `cb5c579`. Quedan residuos: `docs/ia` (vacío, sin extensión) y `docs/C4.md` antiguo junto al nuevo. |
| Estado calificado identificable | Cumple | Sin etiquetas; hash `cb5c579` `2026-08-23T23:44:12-05:00`, último ≤ cierre. |
| Nombres de ADR según la convención | Cumple | `ls docs/adr` sin salida en el filtro. |
| ADR aceptados no reescritos | No cumple | El ADR aceptado `docs/ADR/01-arquitectura-base.md` (decisión híbrida, `f45f002`) se **borró** en `cb5c579` y la decisión cambió a hexagonal puro sin marcarlo como «reemplazado» (CONTRATO §4). |
| `docs/ia.md` al día para la semana | Cumple | Actualizado en `cb5c579` con entrada del 23-ago que incluye lo rechazado y su motivo. Observación: una sola fila llena, redactada como ejemplo, y solo dos integrantes citados. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias (exit 1) fuera de `node_modules/`; `.env.example` solo con `PORT=3000`; sin `.env` versionado. |
| Contribución de todos los integrantes | No cumple | 3 identidades / 4 integrantes: Cconde31 12 · MiguelJacome 4 · Steamlinker 1 (nueva, correo `camilandre0510@gmail.com`, sin atribuir). Un integrante sigue sin aparición. |

## Recuento

**4 de 9** criterios cumplidos.

## No verificado / pendientes

- Prueba en verde: sin pipeline ni evidencia de ejecución; haría falta el run de CI o la evidencia de Moodle.
- Ejecución real del arranque: No verificado por regla del kit (comando declarado: `npm install && npm start`).

## Hallazgos para la planilla

- El empujón de última hora trajo lo que faltaba de esqueleto: código Node/Express con comando único, prueba automatizada, ADR renombrado a la convención y reescrito (ahora hexagonal puro), sección 4 nueva, C4 como código en `docs/c4/` e `ia.md` con entrada de S3.
- `node_modules/` completo versionado en el repositorio: higiene grave (miles de archivos de terceros), y `docs/matriz_arquitectura.md` quedó obsoleto contradiciendo el ADR (dice «hexagonal implementada como monolito modular»).
- El ADR anterior se borró sin marcar el reemplazo (CONTRATO §4) aunque la decisión cambió.
- Faltan por aterrizar: tácticas por escenario, matriz contra el árbol (S1–S7), enlaces del ADR desde aspectos y escenarios, y los paquetes `domain/`/`application/` declarados (solo existe el adaptador HTTP).
- Sin commits posteriores al cierre.
