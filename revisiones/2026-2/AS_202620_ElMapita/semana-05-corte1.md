# semana-05-corte1 · ElMapita

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `b28e068` en `origin/main` (2026-09-07T14:57:28-06:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main b28e068 2026-09-07T14:57:28-06:00, anterior al cierre 2026-09-10T17:00:00Z | Cumple | Rama principal main con hash y fecha verificados. |
| correcciones.md existe en la raíz del estado calificado | correcciones.md presente en árbol de b28e068 | Cumple | Archivo en raíz y en el hash calificado. |
| Correcciones trazables y contrastadas | correcciones.md no fue incluido en la evidencia; no se pudo contrastar cada hallazgo S1-S4 | No cumple | Falta el contenido del archivo para verificar trazabilidad. |
| S1 al día: equipo, problema y repositorio | README.md lista equipo y problema; repo en ISCOUTB/AS_202620_ElMapita | Cumple | Equipo declarado y repositorio correcto. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-EN.md secciones 2 y 10 con EC-01 a EC-04 y RES-04 | Cumple | Escenarios y restricciones documentados. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001 y 0002 con decisiones aceptadas y alternativas | Cumple | ADR-0001 y ADR-0002 presentes y coherentes. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md, docs/c4/C4_L1_Context.md y C4_L2_Container.md, docs/CorteVertical_ElMapitaUTB.docx | Cumple | Documentación completa y corte vertical en .docx. |
| Corte vertical reproducible y coherente con la arquitectura | README.md describe arranque con scripts/dev.sh y pruebas, pero no hay runs_ci | No verificado | No se ejecutó código; se requiere run de CI o ejecución local. |
| Pipeline y pruebas respaldan el estado calificado | .github/workflows/ci.yml existe pero no hay runs_ci citados | No verificado | Falta URL de run asociado al hash. |
| Trazabilidad consolidada navegable | docs/aspectos.md con enlaces a C4, ADR, código y pruebas (aunque pruebas pendientes) | Cumple | Tabla de aspectos con columnas completas, aunque algunas celdas dicen 'pendiente'. |
| PDF u otro adjunto exigido por el aula | docs/cortes/corte-1.pdf en el árbol, pero no se confirma entrega en Moodle | No verificado | PDF presente en repo, pero la entrega en Moodle no es verificable desde aquí. |
| Sustentación del corte | No hay evidencia de sesión de sustentación | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_ElMapita, público, integrantes en README y autores en historial | Cumple | Nombre y organización correctos. |
| Estructura mínima | docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md presentes | Cumple | Estructura cumple con la mínima. |
| Estado del repositorio calificado | b28e068 en origin/main anterior al cierre | Cumple | Hash correcto y sin commits posteriores al cierre. |
| Convenciones de ADR | docs/adr/0001-*.md y 0002-*.md con nombres en kebab-case y formato | Cumple | Dos ADR válidos, sin ediciones posteriores. |
| Tabla de aspectos | docs/aspectos.md con filas EC-01 a EC-04 y columnas completas | Cumple | Aunque algunas celdas de pruebas dicen 'pendiente', la estructura es correcta. |
| Registro de uso de IA | docs/ia.md con 3 commits (df1e2f7, 07b36f4, b28e068) | Cumple | Registro presente y con historial. |
| README | README.md con descripción, stack, arranque con scripts/dev.sh y pruebas | Cumple | Incluye comandos de arranque y prueba. |
| Pipeline y análisis estático | .github/workflows/ci.yml existe, pero sin runs_ci citados | No verificado | No se pudo verificar ejecución; falta URL de run. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `b28e0684d4b38267c0a7d48152b0f5558a789b8c 2026-09-07T14:57:28-06:00 Se agrego correcciones.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto está bien documentado pero con deudas de implementación y verificación.

Pendientes que siguen abiertos:
- Pruebas de EC-01 a EC-04 pendientes
- Implementación de LOD y degradación progresiva (ADR-0002)
- Verificación de pipeline y CI
- Correcciones.md sin contrastar

## Recuento y nota sugerida

7 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.3 = 1 + 4 × (7/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Corte vertical reproducible y coherente con la arquitectura
- Pipeline y pruebas respaldan el estado calificado
- PDF u otro adjunto exigido por el aula
- Sustentación del corte
- Pipeline y análisis estático (transversal)

## Hallazgos para la planilla

- correcciones.md no se pudo contrastar por falta de contenido en la evidencia.
- No hay runs de CI citados para verificar pipeline y pruebas.
- Corte vertical no reproducible sin evidencia de ejecución.
- Pruebas de aspectos EC-01 a EC-04 marcadas como 'pendiente' en docs/aspectos.md.
- ADR-0002 declara implementación pendiente de LOD y degradación progresiva.
- Secretos: se detectó un token de ejemplo en backend/README.md (abc123def456), no es credencial real.
- Autores: solo 3 contribuyentes, pero RobotDRMX tiene 13 commits, posible desbalance.
- PDF de corte presente en repo, pero entrega en Moodle no verificable.
