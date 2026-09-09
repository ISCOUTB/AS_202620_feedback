# semana-05-corte1 · AudioShare

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_AudioShare` |
| Estado revisado | `cb65d13` (2026-09-06T22:00:48-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | rama master, hash cb65d13, fecha 2026-09-06T22:00:48-05:00 (anterior al cierre 2026-09-07T05:00:00Z) | Cumple | El hash citado es el último commit de master anterior al cierre. |
| correcciones.md existe en la raíz del estado calificado | arbol del hash cb65d13 no contiene correcciones.md | No cumple | No existe correcciones.md en la raíz del estado calificado ni en HEAD. |
| Correcciones trazables y contrastadas | correcciones.md ausente en cb65d13; no hay índice que responda a hallazgos S1-S4 | No cumple | Sin archivo índice no se puede contrastar trazabilidad de correcciones. |
| S1 al día: equipo, problema y repositorio | docs/ficha-problema.md en cb65d13 describe problema, prototipo, usuarios y tensiones; autores en shortlog: Santiago, Vincent, Elian, Yeiver | Cumple | Contenido acorde y autores visibles en historial. |
| S2 al día: escenarios de calidad y restricciones | docs/arbol_utilidad.md, docs/escenarios_calidad.md con EC-01 a EC-04 y docs/Restricciones_justificadas.md en cb65d13 | Cumple | Atributos priorizados, métricas y restricciones documentadas. |
| S3 al día: estrategia de solución y decisiones | docs/Matriz_Comparativa.md y docs/adr/0001-usar-monolito-modular.md (aceptado) en cb65d13; sección 4 de arc42 coherente | Cumple | Comparación de alternativas, decisión monolito modular y consecuencias documentadas. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/src/ contiene 01-06, 09, 10, 12; docs/c4/ con niveles 1 y 2; tests/a01.test.ts recorre el flujo | Cumple | arc42 con secciones relevantes; C4 alineado con código; corte A-01 implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md documenta npm run dev y npm run verify; tests/a01.test.ts prueba flujo HTTP-Session-RoomRepository-SQLite-Sync-Audio | Cumple | Coherente con monolito modular y trazable en docs/aspectos.md. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml ejecuta npm run verify; runs CI success 2026-09-07T02:57Z y 03:00Z y 03:21Z (URLs 34077992645, 34078177649, 34079348567) | Cumple | Runs posteriores al hash calificado y anteriores al cierre verifican el estado. |
| Trazabilidad consolidada navegable | docs/aspectos.md contiene tabla por filas A-01 con enlaces a EC, ADR, C4, src y tests | Cumple | Todos los eslabones apuntan a rutas existentes en cb65d13. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; corresponde a Moodle | No verificado | Se requiere el adjunto en el aula para verificar. |
| Sustentación del corte | No hay sesión de sustentación en el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura del repositorio | cb65d13 contiene README.md, docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md | Cumple | Estructura mínima presente en la raíz. |
| Estado del repositorio evaluado y rama | rama master con hash cb65d13 (2026-09-06T22:00:48-05:00), anterior al cierre S5 | Cumple | Estado identificable y sin commits posteriores al cierre. |
| ADR | docs/adr/0001-usar-monolito-modular.md con estado aceptado, contexto, alternativas, consecuencias y trazabilidad en cb65d13 | Cumple | Un ADR bien formado y en la ruta esperada. |
| docs/ia.md | docs/ia.md en cb65d13 con propósito, usos, herramientas, verificación y tabla de usos aceptados/rechazados; log con 9 commits entre 2026-08-09 y 2026-09-04 | Cumple | Registro de IA con evidencia de criterio y crecimiento en el tiempo. |
| Secretos | grep de patrones de secretos sin coincidencias y sin .env versionados en cb65d13 | Cumple | No se detectaron credenciales ni archivos .env. |
| Autoría y colaboración | shortlog del HEAD: 45 Elian Daniel Perea Vanegas, 38 Yeiver Andrés Vergel Pérez, 36 cardonavincent26-design, 30 Santiago Adolfo Camacho Hernández | Cumple | Los cuatro integrantes contribuyen en el historial con participación repartida; identidades consolidadas por nombre visible. |
| README y reproducibilidad | README.md en cb65d13 indica Node.js 22+, instalar con npm install, arrancar con npm run dev y probar con npm test / npm run verify | Cumple | Único comando de arranque y de pruebas documentado. |
| Pipeline y análisis estático | .github/workflows/ci.yml ejecuta npm ci y npm run verify; run CI success del 2026-09-07T03:21:03Z (https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/34079348567) | Cumple | CI en cada push y pull request; análisis estático SonarCloud no evidenciado, pendiente si el contrato lo exige. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `cb65d13134b220c020d0facaa00d0a779d584245 2026-09-06T22:00:48-05:00 Update README.md`
- **Veredicto**: al dia
- Resumen: En HEAD (cb65d13) el proyecto integra S1 a S4 con documentación de problema, calidad, restricciones, ADR, arc42, C4 y corte vertical A-01 ejecutable con pruebas automatizadas. La única no conformidad del compendio es la ausencia de correcciones.md en la raíz. No hay pendientes de semanas anteriores sin resolver; no quedan correcciones tardías que reportar.

Pendientes que siguen abiertos:
- Crear correcciones.md en la raíz del repositorio con respuesta trazable a los hallazgos S1-S4.
- Verificar PDF adjunto en Moodle y sustentación oral.

## Recuento y nota sugerida

8 de 12 criterios Cumple.

## No verificado / pendientes

- PDF u otro adjunto exigido por el aula: requiere revisar Moodle.
- Sustentación del corte: requiere sesión oral.
- Análisis estático SonarCloud: no hay evidencia en el repositorio.

## Hallazgos para la planilla

- Falta correcciones.md en la raíz del estado calificado cb65d13.
- Sin correcciones.md no es posible verificar trazabilidad de correcciones S1-S4.
- El corte vertical A-01 y su prueba están implementados y el CI pasa en verde.
- La documentación arc42, C4 y aspectos está alineada con el código real.
- No hay commits posteriores al cierre; el estado calificado coincide con HEAD.
- PDF adjunto y sustentación no verificables desde el repositorio.
