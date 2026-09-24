# Semana 07 · Evidencia S7 · Recobra

> Revisión definitiva auditada localmente. Se corrigió el resultado automático porque omitió evidencia legible en el repositorio.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Estado revisado | `8f25313` en `origin/master` (2026-09-19T13:37:58-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | auditoría local sobre clon público, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Contrato ejecutable versionado | `docs/contracts/openapi.yaml` declara un contrato OpenAPI con versión. | Cumple | El archivo está versionado en Git. |
| Rutas y esquemas de datos | El contrato contiene rutas, respuestas y esquemas reutilizables. | Cumple | No es una descripción narrativa. |
| Correspondencia contrato–API | Las operaciones declaradas se corresponden con los endpoints implementados. | Cumple | El cotejo está además cubierto por la prueba contractual. |
| Versión e historial | El historial muestra alta `d51910b`, ruptura deliberada `8f227e3` y restauración `e1dfeaf`. | Cumple | La evolución es trazable. |
| Prueba de contrato presente | La suite incluye la comparación automática del contrato con la API. | Cumple | Comprueba rutas y esquemas. |
| Pipeline ejecuta la prueba | `.github/workflows/ci.yml:20-25`; run exitoso del estado revisado: https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/35461821663 | Cumple | La suite se ejecuta sobre la rama principal. |
| Falla ante cambio incompatible | `docs/contracts/evidencia-fallo-2026-09-19.txt:5-95` y run rojo https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/35411238008 | Cumple | Se documenta la falla y posterior restauración. |
| ADR de integración ligado a escenario | `docs/adr/` contiene la decisión de integración con alternativas y consecuencias. | Cumple | Se enlaza con el escenario pertinente. |
| arc42 sección 6 | La sección 6 describe flujos de éxito y error con participantes y mensajes. | Cumple | Los recorridos son verificables. |
| C4 nivel 2 etiquetado | `docs/c4/C4-C2.md:30-34` explicita protocolo/formato en las relaciones. | Cumple | Todas las flechas relevantes están etiquetadas. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia u observación |
|---|---|---|
| Repositorio público con nombre de convención | Cumple | Clon público `ISCOUTB/AS_202620_Recobra`. |
| Estructura mínima | Cumple | Las rutas obligatorias están presentes. |
| Estado calificado identificable | Cumple | `origin/master`, `8f25313`, fecha y cierre consignados. |
| Nombres de ADR | Cumple | Los ADR siguen numeración y kebab-case. |
| ADR aceptados sin reescribir | Cumple | Las decisiones conservan trazabilidad histórica. |
| `docs/ia.md` al día | Cumple | `docs/ia.md:11` registra la actividad S7. |
| Pipeline, SonarCloud y Quality Gate públicos | No cumple | El workflow no invoca un scanner ni acredita Quality Gate público. |
| Sin credenciales expuestas | Cumple | No se hallaron secretos reales versionados. |
| Contribución de todo el equipo | Cumple | El historial muestra participación de todos los integrantes. |

## Estado global del proyecto

La punta actual coincide con el estado calificado. El contrato, su prueba, el ciclo rojo–verde y la documentación arquitectónica S7 son verificables; permanece abierta la integración pública de SonarCloud.

## Recuento y nota sugerida

**10 de 10 criterios Cumple.**

**Nota sugerida (propuesta al docente; la nota final se fija en Moodle): 5.0 = 1 + 4 × (10/10).**
