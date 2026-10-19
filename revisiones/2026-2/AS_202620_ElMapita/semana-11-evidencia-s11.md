# ElMapita · Evidencia S11

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_ElMapita/tree/f3bcfa83e80f5c8d0e30a01b656d89160c907d64) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

**Estado: DEFINITIVA · estado histórico al cierre S11.**

- Repositorio público: https://github.com/ISCOUTB/AS_202620_ElMapita
- Rama observada: `origin/main`. Estado evaluado: `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` (2026-10-04T21:11:20-06:00).
- Cierre S11 exclusivo: 2026-10-19T05:00:00Z; solo commits con fecha de commit anterior. Observación S12/overall: 2026-10-19T21:35:00Z.
- Actividad: 0 commits en [2026-10-12T05:00Z, 2026-10-19T05:00Z); 2 posteriores al cierre hasta la observación. Selección por git sobre la rama principal, sin etiquetas.

## Matriz de cumplimiento

| Criterio | Estado | Evidencia y límites |
|---|---|---|
| Integración principal identificada en el código | Cumple | [frontend/lib/features/mapas/infrastructure/api/mapas_api.dart:12-45](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/lib/features/mapas/infrastructure/api/mapas_api.dart#L12-L45) y [backend/src/modules/mapas/infrastructure/persistence/supabase-repositories.ts:49-126](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/mapas/infrastructure/persistence/supabase-repositories.ts#L49-L126): consultas Flutter → API → Supabase concretas. |
| Tabla de modos de fallo con no responde, responde tarde y responde dos veces | No cumple | [docs/arc42/arc42-template-EN.md:654-660](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L654-L660) en el hash histórico contiene riesgos de Supabase y cold start, pero no una tabla que cubra también respuesta duplicada. La tabla añadida en la punta es posterior al cierre. |
| Mitigación asignada a cada modo de fallo | No cumple | [docs/arc42/arc42-template-EN.md:658-660](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L658-L660): caché y medición de latencia aparecen, pero falta asignación para el tercer modo, respuesta duplicada. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | No cumple | [docs/aspectos.md:5-8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L5-L8) declara planes honestos para offline y mediciones; se aceptan como pendientes válidos, sin exigir implementación completa. No cubren una correspondencia para los tres modos exigidos; `load_building_use_case.dart:18-23` sale con error antes de consultar la caché. |
| Diseño de idempotencia o saga, o argumento de por qué no aplica | No cumple | El árbol `docs/adr/` del hash histórico termina en 0007; no contiene el diseño de idempotencia de 0008. [backend/src/modules/auth/application/use-cases.ts:48-68,145-157](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/auth/application/use-cases.ts#L48-L68) ya expone registro y cambio de rol: no basta inferir que todas las operaciones son lecturas. |
| ADR con la decisión de extraer o no extraer, y sus criterios | No cumple | `git ls-tree -r f3bcfa83 -- docs/adr` y [docs/adr/0001-estilo-arquitectonico-propuesto.md:26-38,144-167](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0001-estilo-arquitectonico-propuesto.md#L26-L38): selección de estilo previa; no está el ADR específico de extracción 0008 al cierre. |
| La alternativa no extraer aparece evaluada, no omitida | No cumple | [docs/adr/0001-estilo-arquitectonico-propuesto.md:26-38](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0001-estilo-arquitectonico-propuesto.md#L26-L38): compara estilos, no la extracción de un módulo real frente a no extraer; 0008 solo existe después del cierre. |
| arc42 sección 11 con los modos de fallo | No cumple | [docs/arc42/arc42-template-EN.md:651-660](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L651-L660): faltan los tres modos S11 en la sección histórica; los apartados 11.1/11.2 actuales son incorporación tardía. |
| Filas de aspectos afectadas por la integración, al día | Cumple | [docs/aspectos.md:5-8,26-43](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L5-L8): las filas afectadas enlazan requisito, C4, ADR, código y pruebas; distinguen mediciones fallidas y pendientes con corrección concreta. No se confunde la trazabilidad honesta con calidad ya alcanzada. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y límites |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon git público exitoso de `https://github.com/ISCOUTB/AS_202620_ElMapita.git`; API actions/runs sin autenticación HTTP 200. |
| Estructura mínima presente | Cumple | `git ls-tree -r` en el hash citado: README, código, docs/arc42, docs/adr, docs/c4, docs/aspectos.md y docs/ia.md presentes. arc42 consolidado en [docs/arc42/arc42-template-EN.md:16-660](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/arc42/arc42-template-EN.md#L16-L660); se evalúa allí y no se confunde ubicación con ausencia. |
| Estado calificado identificable | Cumple | `git log -1 --until=2026-10-19T04:59:59Z origin/main` fija S11; punta observada fija S12. Hash y fecha completos arriba. |
| Nombres de ADR según la convención | Cumple | `git ls-tree --name-only` de docs/adr: archivos de decisión NNNN-kebab-case.md; archivos auxiliares .gitkeep no cuentan como decisiones. |
| ADR aceptados no reescritos | No cumple | `git log -p -- docs/adr/0004-despliegue-render-docker.md`: b35f784 reescribe decisiones de runtime/health tras su aceptación en 30499d5, sin reemplazo de 0004. Los reemplazos explícitos 0005/0006 sí reparan 0001/0003, no este caso. |
| docs/ia.md al día para la semana | No cumple | `git log -- docs/ia.md`: no actualización dentro de S11; la incorporación de 2026-10-19T08:33:59Z es tardía. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | API pública actions/runs HTTP 200, una consulta; run [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/37258414405) success con head_sha `f3bcfa83e80f5c8d0e30a01b656d89160c907d64`. Scanner en [.github/workflows/ci.yml:274-283](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L274-L283), pero job no bloqueante `:253-260` y gate omite Sonar `:297-309`; falta análisis público exitoso y Quality Gate verificable de esta revisión. CI verde no certifica Sonar. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Inspección de configuración y ejemplos no identifica una credencial activa; no se certifica ausencia absoluta en todo el historial. Escaneo exhaustivo de blobs/historial pendiente de completar; no se reproducen valores sospechosos. Debe cerrarse con escaneo redactado del historial, no solo del árbol actual. |
| Contribución de todos los integrantes | No verificado | `git shortlog -sne` y `.mailmap:1-4` permiten consolidar aliases del mismo correo, pero persiste una cuenta cuya atribución personal no está establecida explícitamente en el listado. No se equiparan cuentas por parecido del nombre. Falta validar el mapeo completo y el reparto sustantivo de código/documentación; no se publican identidades. |

## Recuento y nota sugerida

**2/9 criterios Cumple. Nota sugerida: 1.9/5.0**, calculada como 1 + 4 × (2/9), propuesta al docente autorizada por la ficha. La nota final la fija el profesor en Moodle. La transversal no entra en el cálculo. La condición definitiva corresponde al estado histórico revisado, no sustituye la decisión docente.

## overall · punta actual de la misma rama

Punta: `0421885424d13478cf33c717fdd933a4748d9025`.

Dos commits posteriores al cierre: `d77eb7132df6e9dc33001686d47fb50babdc405f` (2026-10-19T08:24:11Z) y `0421885424d13478cf33c717fdd933a4748d9025` (08:33:59Z). El segundo incorpora ADR-0008 con criterios y alternativa no extraer ([docs/adr/0008-decision-extraccion.md:18-41](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/docs/adr/0008-decision-extraccion.md#L18-L41)), tabla de fallos y argumento sobre sagas (`arc42-template-EN.md:664-679`) y enlace en aspectos (`:45-47`); no cambia S11 histórica. Incluso ahora la tabla no incluye explícitamente respuesta duplicada, y el argumento de escrituras futuras debe reconciliarse con registro/cambio de rol existentes ([backend/src/modules/auth/application/use-cases.ts:48-68,145-157](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/backend/src/modules/auth/application/use-cases.ts#L48-L68)).

Erosión arquitectónica: arc42 describe recuperación offline y caché de metadatos, pero `load_building_use_case.dart:18-23` exige primero la API y `model_cache.dart:69-75` no invalida. [docs/aspectos.md:5-8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/docs/aspectos.md#L5-L8) reconoce medición HTTP 500, visualización placeholder y 0/20 offline; esos resultados previos no se presentan como nuevas pruebas de esta revisión. Se preservan los límites de módulos del backend, mientras el caso de uso Flutter importa adaptadores concretos (`load_building_use_case.dart:5-16`), divergencia respecto al desacoplo proclamado. CI verde no demuestra todo: pruebas Flutter/E2E y Sonar pueden no bloquear ([.github/workflows/ci.yml:68-74,189-211,253-260,297-309](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/.github/workflows/ci.yml#L68-L74)).

## Pendientes y límites de verificación

Completar modos no responde/tarde/duplicado y su correspondencia, ampliar idempotencia a operaciones repetibles reales, y mantener la decisión razonada de no extraer sin exigir microservicios. Un pendiente con plan es aceptable en S11; una intención sin alcance o una afirmación de implementación contradicha por código no lo es. Para S12, añadir tabla de garantías con dos operaciones contrastadas, invalidación tras escritura y ADR comparativo de costo de reversión; sincronizar arc42 §8.

No se ejecutó código estudiantil, pruebas, contenedores, scripts ni PDFs. Comandos no ejecutados: `npm run test:cov`, `npm run test:contracts`, `flutter test` y pruebas de dispositivo/offline. Se leyó el código y se consultó un run exacto; no se inspeccionaron sus logs de jobs. Las mediciones anteriores citadas por aspectos conservan su fecha y limitaciones.
