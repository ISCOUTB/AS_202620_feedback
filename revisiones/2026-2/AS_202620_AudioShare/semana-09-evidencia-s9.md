# Evidencia S9 definitiva · AudioShare

Revisión actualizada tras el cierre del **2026-10-05T05:00:00Z** (domingo a medianoche COT).

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_AudioShare](https://github.com/ISCOUTB/AS_202620_AudioShare) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `cb65d13134b220c020d0facaa00d0a779d584245` |
| Base S8 | `e4789d887fe59b2ace65bd1d2680f79758db5b54` |
| Estado revisado | `6a03a9718776420d46ed40f7addc5667206908cd` en `origin/master` (2026-10-04T23:15:57-05:00) |
| S9 congelada | `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 |
| Punta actual / S10 preliminar | `6a03a9718776420d46ed40f7addc5667206908cd` · 2026-10-04T23:15:57-05:00 |
| Comprobación | 2026-10-06T21:16:50Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Matriz S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | No cumple | El delta contra S8 no cambia código de producción; solo añade la prueba [tests/sync-a01.test.ts:1–20](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/tests/sync-a01.test.ts#L1-L20), que calcula constantes sin importar módulos del sistema. La porción previa no se recalifica por existir. |
| Cadena completa navegable para esa porción | No cumple | La fila A-01 sigue apuntando a ADR-0001/0003 y pruebas Flutter previas, sin ADR-0005 ni prueba nueva ni medición navegable; [docs/aspectos.md:38–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L38-L43). |
| ADR con la decisión argumentada por el equipo | Cumple | ADR-0005 elige referencia startAt y compara reproducción al recibir y reloj local, con límites explícitos; [docs/adr/0005 Validación-sincronización-inicial.md:9–69](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L9-L69). Esto acredita la decisión documental, no la medición. |
| Prueba que falla ante el defecto que cubre | No verificado | La prueba nueva obtiene siempre 40 ms a partir de 20/35/60; no ejercita el sistema ni documenta una mutación aplicada al código real. Falta run rojo, mutación o procedimiento reproducible del defecto; [tests/sync-a01.test.ts:5–18](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/tests/sync-a01.test.ts#L5-L18). |
| Medición del escenario asociado | No cumple | No hay medición de receptores: el resultado aritmético es sintético. El propio README mantiene pendientes las mediciones físicas; [tests/sync-a01.test.ts:5–18](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/tests/sync-a01.test.ts#L5-L18), [README.md:203–210](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L203-L210). |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | No cumple | La fila añadida registra aceptación parcial y correcciones, pero no una salida rechazada del alcance S9 con razón técnica diferenciada; [docs/ia.md:112–112](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L112-L112). Los rechazos de semanas previas son línea base. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | No cumple | La auditoría es una declaración general de revisión sin hallazgo localizado, propuesta concreta ni corrección contrastable del periodo; [docs/ia.md:253–294](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L253-L294). |
| Dependencias propuestas verificadas en su registro oficial | No verificado | No cambiaron package.json ni pubspec.yaml en S9. No se penaliza ese delta vacío: falta un inventario explícito de propuestas auditadas y su comprobación oficial; la declaración genérica no cita paquetes ni registros, [docs/ia.md:296–318](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L296-L318). |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido estático de código, ejemplos y documentación del hash sin credenciales reales. [.env.example:1–3](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/.env.example#L1-L3) y [.github/workflows/ci.yml:20–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/.github/workflows/ci.yml#L20-L23) usan configuración/secretos externos; este resultado se limita al snapshot. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | ADR-0006 justifica no incorporar modelo generativo por alcance, costo, latencia y mantenimiento; [docs/adr/0006-no-incorporar-componente-generativo.md:8–63](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0006-no-incorporar-componente-generativo.md#L8-L63). |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público por HTTPS y rama remota master; [README.md:1–10](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/README.md#L1-L10). |
| Estructura mínima presente | Cumple | Presentes README, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md; [docs/aspectos.md:36–43](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/aspectos.md#L36-L43). arc42 usa AsciiDoc, desviación de formato frente a Markdown. |
| Estado calificado identificable | Cumple | Hash y fecha completos en el encabezado, elegidos por git log --until sobre origin/master. |
| Nombres de ADR según la convención | No cumple | El nombre [docs/adr/0005 Validación-sincronización-inicial.md:1–7](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0005%20Validaci%C3%B3n-sincronizaci%C3%B3n-inicial.md#L1-L7) contiene espacio y acentos; no pasa NNNN-kebab-case. |
| ADR aceptados no reescritos | No cumple | ADR-0001 ya estaba aceptado en 924d133 y fue modificado en 354f1f5: se verificaron ambas versiones y el diff. El texto actual solo dice complementado, sin preservar la versión aceptada mediante reemplazo; [docs/adr/0001-usar-monolito-modular.md:1–8](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0001-usar-monolito-modular.md#L1-L8). |
| docs/ia.md al día para la semana | No cumple | Hubo cambios de S9, pero el registro específico no separa una salida rechazada con motivo técnico y mantiene Estado «semana 7»; [docs/ia.md:112–112](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L112-L112), [docs/ia.md:363–389](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/ia.md#L363-L389). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Scanner configurado en [sonar-project.properties:1–5](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/sonar-project.properties#L1-L5) y [.github/workflows/ci.yml:18–23](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/.github/workflows/ci.yml#L18-L23); la organización configurada no es isco-utb. CI success, Flutter failure en el hash. Falta análisis público y Quality Gate atribuibles a esta revisión. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Sin credenciales reales en el árbol: coincidencias solo con referencias a secrets de Actions. Barrido histórico completo no concluyó; no se certifica el historial. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas de autor visibles, distribuidas en el historial. No se inventa la correspondencia entre cuentas y los cuatro integrantes; falta mapa verificable para acreditar a todas las personas. |

## Actions en el estado congelado

- [Flutter: failure](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748991), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
- [Publicar imagen: success](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748932), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
- [CI: success](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/37262748924), 2026-10-05T04:16:00Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido del snapshot completo de texto, incluidos docs y ejemplos: las coincidencias fueron referencias a secretos del almacén de Actions, no valores. No hay .env versionado. El recorrido histórico con git log -S no terminó por cancelación del entorno: la fila transversal conserva No verificado.

## Estado global del proyecto (overall · punta actual)

La punta coincide con S9. Se incorporaron dos ADR y una prueba adicional, pero esta no valida la sincronización real. La aplicación responde al health check actual, lo cual no demuestra flujo de audio ni identidad entre despliegue y commit. La documentación reconoce audio simulado y mediciones pendientes. CI de backend e imagen están en verde; Flutter sigue en rojo. La plataforma declarada cambió a Dokploy sin alinear completamente la vista de despliegue y ADR.

El delta S9 contiene 9 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Recuento y nota sugerida

**3 de 10 criterios Cumple. Nota sugerida: 2.2 = 1 + 4 × (3/10).** Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no integra este cálculo.

## Acciones prioritarias

- Sustituir la prueba de constantes por una que invoque la lógica real y falle al introducir un defecto de sincronización; registrar procedimiento y resultado.
- Completar la cadena A-01 hacia ADR-0005, código exacto, prueba y medición reproducible.
- Aportar mediciones de receptores y comparación con umbral, sin presentar un ejemplo sintético como experimento.
- Localizar la consigna oficial S10 y definir línea base, hipótesis, variables y montaje.
- Corregir Flutter CI, evidenciar SonarCloud/Quality Gate del hash y alinear Dokploy con ADR/C4/arc42.
- Hacer específica la auditoría de erosión y la verificación de dependencias; registrar rechazo técnico propio de la entrega.

## Hallazgos cerrados con evidencia nueva

- Existe decisión explícita de no incorporar componente generativo: [docs/adr/0006-no-incorporar-componente-generativo.md:22–45](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/6a03a9718776420d46ed40f7addc5667206908cd/docs/adr/0006-no-incorporar-componente-generativo.md#L22-L45).
- URL y health check accesibles en la comprobación actual; no cambia retrospectivamente S8.
