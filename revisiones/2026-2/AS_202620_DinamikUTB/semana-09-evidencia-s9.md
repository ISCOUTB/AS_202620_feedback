# Evidencia S9 definitiva · DinamikUTB

Revisión actualizada tras el cierre del **2026-10-05T05:00:00Z** (domingo a medianoche COT).

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_DinamikUTB](https://github.com/ISCOUTB/AS_202620_DinamikUTB) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `72bfc7e206eac4147dd244c03fa09b4b32b9a7e7` |
| Base S8 | `287c65d46a8469142baf5dc57da296c0bc80e0fb` |
| Estado revisado | `2326dd7f9d4dda08ba557ea6602b0a7085c97bee` en `origin/master` (2026-10-04T21:47:16-05:00) |
| S9 congelada | `2326dd7f9d4dda08ba557ea6602b0a7085c97bee` · 2026-10-04T21:47:16-05:00 |
| Punta actual / S10 preliminar | `5dc9acf9335fec70e274a2e5c494b3805b0e9646` · 2026-10-05T22:06:45-05:00 |
| Comprobación | 2026-10-06T21:23:08Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Matriz S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | No cumple | La porción señalada es el endpoint construido en S4 y la prueba de S7, como reconoce [docs/evidencia-s9.md:3–8](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L3-L8). En S9 solo cambia documentación: no hay implementación/corrección nueva de esa porción. |
| Cadena completa navegable para esa porción | No cumple | La fila A-01 mejora con enlace al ADR-0008 y evidencia, pero código/pruebas son textos no navegables, el run enlazado es previo y la medición solo cubre 5 de 20 casos; [docs/aspectos.md:9–11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/aspectos.md#L9-L11), [docs/evidencia-s9.md:25–29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L25-L29). La mejora documental no acredita cadena completa de una porción nueva. |
| ADR con la decisión argumentada por el equipo | Cumple | ADR-0008 decide verificar identificadores oficiales, compara tres opciones, justifica costo/esfuerzo y reconoce alcance de proceso; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:17–69](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L17-L69). |
| Prueba que falla ante el defecto que cubre | No verificado | La evidencia remite al fallo contractual real de S7, sin nueva mutación/procedimiento ejecutado sobre una corrección del periodo S9; [docs/evidencia-s9.md:19–24](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L19-L24). Falta demostración específica de esta entrega. |
| Medición del escenario asociado | No cumple | Se documenta 5/5 frente a objetivo de 20 casos; el propio equipo deja la carga completa pendiente. No se acredita el umbral completo de Q-01; [docs/evidencia-s9.md:25–29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L25-L29). |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | No cumple | La nueva entrada solo declara Aceptado. Los rechazos citados en el extracto son de S4/S7 y uno no estaba registrado aún en docs/ia.md congelado; [docs/evidencia-s9.md:31–38](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L31-L38), [docs/ia.md:41–41](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/ia.md#L41-L41). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | Auditoría nueva declara comando, alcance y ausencia de escrituras cruzadas; [docs/evidencia-s9.md:40–51](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L40-L51). Contraste estático: actualizar_estado_requisito escribe Requisito dentro de su módulo dueño, [backend/app/requisitos/service.py:13–20](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/backend/app/requisitos/service.py#L13-L20). |
| Dependencias propuestas verificadas en su registro oficial | Cumple | Inventario nuevo de pytest-cov 7.1.0 y coverage 7.16.2 con verificación PyPI; [docs/evidencia-s9.md:53–59](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L53-L59). Consultas oficiales /pypi/pytest-cov/7.1.0/json y /pypi/coverage/7.16.2/json respondieron HTTP 200 y proyectos legítimos. Sin altas de dependencias en S9, lo que no se penaliza. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido del snapshot sin credenciales reales, .env no versionado; variables/secretos se toman del entorno, [render.yaml:1–25](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/render.yaml#L1-L25), [.github/workflows/ci.yml:75–78](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/.github/workflows/ci.yml#L75-L78). |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | ADR-0009 compara alternativas y decide no incorporar componente generativo por determinismo, costos, disponibilidad y alcance de A-03; [docs/adr/0009-no-incorporacion-componente-generativo.md:17–68](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0009-no-incorporacion-componente-generativo.md#L17-L68). |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público ISCOUTB/AS_202620_DinamikUTB, rama master; [README.md:1–5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Las seis rutas mínimas están presentes; arc42 01–12 y C4 en fuentes PlantUML, [docs/aspectos.md:9–18](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/aspectos.md#L9-L18). |
| Estado calificado identificable | Cumple | Estado S9 y base S8 identificados por Git en el encabezado; cambios del 5 de octubre separados. |
| Nombres de ADR según la convención | Cumple | Los nueve ADR cumplen NNNN-kebab-case; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:1–9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L1-L9), [docs/adr/0009-no-incorporacion-componente-generativo.md:1–9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0009-no-incorporacion-componente-generativo.md#L1-L9). |
| ADR aceptados no reescritos | No verificado | Hay ediciones históricas de ADR-0001/0002/0005/0006; falta terminar contraste independiente de las versiones aceptadas. No se presume cerrado el arrastre de inmutabilidad. |
| docs/ia.md al día para la semana | No cumple | Hay entrada S9 de aceptación, pero no documenta rechazo técnico propio de esa verificación. El incidente que se atribuye a IA en ADR-0008 aún no aparece como entrada en docs/ia.md del snapshot S9; [docs/ia.md:37–41](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/ia.md#L37-L41), [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:93–95](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L93-L95). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | Configuración de isco-utb en [sonar-project.properties:1–11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/sonar-project.properties#L1-L11), scanner en [.github/workflows/ci.yml:55–78](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/.github/workflows/ci.yml#L55-L78) y run CI success del hash. Consultas públicas de Quality Gate y último análisis respondieron HTTP 403 a las 21:23 UTC del 6 de octubre; no se pudo comprobar el Gate/revisión. No se infiere del badge. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Barrido del snapshot sin valores de credencial: solo secretos de Actions y permisos id-token. Sin .env versionado. Historial completo no certificado. |
| Contribución de todos los integrantes | No verificado | Siete firmas, 294 commits agregados en S9. Variantes de identidad no equivalen a siete personas; falta correspondencia verificable completa con los cuatro integrantes. |

## Actions en el estado congelado

- [Deploy frontend (GitHub Pages): success](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/37256763460), 2026-10-05T02:47:18Z, SHA exacto del estado indicado.
- [CI: success](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/37256763408), 2026-10-05T02:47:18Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Lectura estática del código, ejemplos y documentación: las coincidencias son SONAR_TOKEN del almacén de Actions y permiso id-token, no valores de secretos. No hay .env versionado. No se certificó todo el historial; esa limitación es transversal, no se descuenta de la fila S9 comprobada en snapshot.

## Estado global del proyecto (overall · punta actual)

S9 aporta nueva verificación documental, política de identificadores oficiales, auditoría y decisión sobre IA generativa; no cambia producción. Después del cierre se añadieron casos para Q-01, entradas de IA, ampliación de inventario y documentación de despliegue. Esa mejoría es tardía y no cambia S9. La punta declara 20/20, pero su CI falla: hay que conciliar la afirmación con un run exacto y corregir el caso de id no entero. Las rutas académicas siguen sin autenticación; los documentos limitan el despliegue a datos ficticios, sin que el revisor consulte registros personales.

El delta S9 contiene 9 commits respecto de S8; hay 5 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Recuento y nota sugerida

**5 de 10 criterios Cumple. Nota sugerida: 3.0 = 1 + 4 × (5/10).** Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no integra este cálculo.

## Acciones prioritarias

- Aportar escenario S10 asignado, línea base y experimento reproducible sobre el MVP.
- Corregir CI HEAD y adjuntar resultados de las pruebas ampliadas; no declarar 20/20 solo por contarlas.
- Convertir rutas de código/pruebas de A-01 en enlaces y verificar cadena completa con medición.
- Terminar controles de identidad y autorización antes de cargar información real; mantener datos ficticios mientras tanto.
- Comprobar Quality Gate público y fijar fecha real de vencimiento/renovación de la base Render.

## Hallazgos cerrados con evidencia nueva

- Se añade auditoría S9 de propiedad de datos con comando y localización; [docs/evidencia-s9.md:40–51](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/evidencia-s9.md#L40-L51).
- Se incorporan ADR de verificación de artefactos y no incorporación generativa; [docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md:51–69](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0008-verificacion-de-artefactos-sugeridos-por-ia.md#L51-L69), [docs/adr/0009-no-incorporacion-componente-generativo.md:52–68](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/2326dd7f9d4dda08ba557ea6602b0a7085c97bee/docs/adr/0009-no-incorporacion-componente-generativo.md#L52-L68).
- Después del cierre se incorpora rechazo explícito de hash inventado al registro de IA; [docs/ia.md:14–16](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/5dc9acf9335fec70e274a2e5c494b3805b0e9646/docs/ia.md#L14-L16).
