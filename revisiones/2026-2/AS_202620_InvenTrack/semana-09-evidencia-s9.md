> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# Semana 9 · Generación verificada y trazable · InvenTrack

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `f12bba8f14fe5a62b2edac91387a014f83c04600` en `origin/main` (2026-09-30T00:41:30-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene cierre**: se califica la punta actual de `origin/main`. El baseline del periodo
S9 es el hash calificado de S8 (`48aeecf94e590088b21e1c4c63dee8d2feb79f11`). Entre ese hash y la
punta hay cuatro commits (2026-09-29/30): `417cb69` (instrucciones de despliegue para `iscoutb.dev`
y Compose), `f9851ba`, `d1a6b6f` (documentación de despliegue con Dokploy) y `f12bba8` (contexto
técnico del arc42 y refinamiento de Render). Todos son documentación y configuración de despliegue:
el diff del periodo solo toca `README.md`, `deploy/compose.lab.yaml`, `docs/`, `render.yaml`; no hay
cambios en `app/` ni en `tests/`. Bajo CONTRATO §12 la evidencia previa es línea base y no se
recalifica por existir.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | No cumple | El periodo no introduce una porción de sistema: `git diff 48aeecf..origin/main` no toca `app/` ni `tests/`; solo documentación y `deploy/compose.lab.yaml`. No hay código nuevo con su cadena. |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | No cumple | `docs/aspectos.md` no se modificó en el periodo; no hay una fila nueva que recorrer hasta una porción de S9. |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | Cumple | `docs/adr/0006-desplegar-en-dokploy-institucional.md` (nuevo en `417cb69`, actualizado en `d1a6b6f`) decide un segundo destino operativo con contexto, opciones evaluadas (A Render, B Dokploy, C Azure descartada), consecuencias y restricciones del servidor (C5 costo cero, 512 MB, 0.5 CPU). Es un ADR de despliegue, no de una porción de código: las filas 1 y 2 igualmente fallan. |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | No cumple | No hay prueba ni procedimiento nuevo en el periodo; el diff no toca `tests/`. |
| Medición del escenario asociado | resultado contrastado con el umbral | No cumple | No hay medición del periodo. La medición de p95 de `docs/retos/corte-1-medicion.md` es línea base de S7 y no se actualiza en este periodo. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | Cumple | `d1a6b6f` añade la entrada del 2026-09-29 «Despliegue institucional en Dokploy posterior al cierre de S8»: acepta el `compose.lab.yaml` y ADR-0006, y rechaza con motivo reescribir ADR-0005 y reactivar el workflow de Azure. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | No cumple | No hay artefacto de auditoría de erosión del periodo; los documentos de contexto y propiedad de datos (`docs/context-map.md`, `docs/propiedad-datos.md`, `docs/auditoria-modularidad.md`) son de S6 y no se refrescaron. |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | No cumple | `git diff 48aeecf..origin/main` sobre `requirements.txt`, `requirements.in` y `pyproject.toml` está vacío: no se añadió ninguna dependencia en el periodo, así que no hay propuesta que verificar. |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | Cumple | `git grep` de CONTRATO §9 sobre la punta solo coincide con `.github/workflows/deploy.yml:28` (`password: ${{ secrets.GITHUB_TOKEN }}`), referencia a secreto y no credencial; sin `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` vacío. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | No cumple | El sistema no incorpora componente generativo (grep de `openai\|anthropic\|gemini\|llm\|gpt\|generative` sin coincidencias) y no existe el ADR que justifique no incorporarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_InvenTrack`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/main`. |
| Estructura mínima presente | Cumple | `README.md`, `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` presentes en la punta. |
| Estado calificado identificable | Cumple | En esta pasada sin cierre se califica la punta: `f12bba8` en `origin/main` (2026-09-30T00:41:30-05:00). |
| Nombres de ADR según la convención | Cumple | `docs/adr/0001`…`0006` siguen `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | No cumple | ADR-0002 fue editado tras su aceptación (`7aae9a8`, `66116c6`, `7b0aad5` del 2026-09-06 y `af24edb` del 2026-09-19); ADR-0004 (`f62ad34`, 2026-09-23) y ADR-0005 (`c692d9e`, 2026-09-27) también acumulan ediciones posteriores a su aceptación, sin ADR de reemplazo declarado. Arrastre de S8. |
| `docs/ia.md` al día para la semana | Cumple | `d1a6b6f` (2026-09-29) añade la entrada de la semana con lo aceptado y lo rechazado con su motivo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Cumple | `sonar-project.properties` (projectKey `ISCOUTB_AS_202620_InvenTrack`, organización `isco-utb`) y scanner en `.github/workflows/test.yml`; run en verde sobre `f12bba8`: https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/36674581931; análisis público con Quality Gate `OK` y cobertura 93.8 % (`sonarcloud.io/dashboard?id=ISCOUTB_AS_202620_InvenTrack`, HTTP 200). |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido sin credenciales reales (solo `${{ secrets.GITHUB_TOKEN }}`); sin `.env` versionado; `git log -S` vacío. |
| Contribución de todos los integrantes | Cumple | `shortlog -sne` consolida por correo en cuatro personas para los cuatro integrantes declarados (una de ellas firma con dos correos). La contribución sigue concentrada en dos integrantes. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `f12bba8` en `origin/main` (2026-09-30T00:41:30-05:00).
- **Commits del periodo S9** (posteriores al hash calificado de S8 `48aeecf`): `417cb69`, `f9851ba`,
  `d1a6b6f`, `f12bba8`.
- **Veredicto**: sin entrega del entregable S9. El periodo es una migración de despliegue a Dokploy
  documentada y trazable (ADR-0006, `deploy/compose.lab.yaml`, README, arc42 y `docs/ia.md`), pero no
  contiene una porción de sistema construida con apoyo de IA ni su cadena (aspectos → ADR → código →
  prueba → medición). El repositorio conserva las piezas de S8, que son línea base.
- Resumen: se mantienen las piezas técnicas de S8 (IaC, logs estructurados, `/metrics`, costo,
  arc42 §7, ADR de plataforma, SonarCloud en CI). Transversalmente sigue abierto el hallazgo de ADR
  aceptados editados sin reemplazo.

## Recuento y nota sugerida

**3 de 10 criterios cumplidos** (filas 3, 6 y 9).

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.2 = 1 + 4 × (3/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Este informe no contiene filas No verificado: todas las comprobaciones se resolvieron leyendo el
  árbol de la punta. La ausencia del entregable S9 es evidencia de ausencia, no una imposibilidad de
  comprobar.

## Hallazgos para la planilla

- El periodo S9 es solo documentación y configuración de despliegue (Dokploy): no hay porción de
  sistema, ni cadena, ni prueba, ni medición, ni dependencias nuevas. La nota preliminar queda cerca
  del piso y sube si el equipo empuja la porción con su cadena antes del cierre.
- Se reconoce un ADR nuevo y bien argumentado (ADR-0006) y una entrada de `docs/ia.md` del periodo
  con rechazo motivado.
- Transversal: ADR-0002, ADR-0004 y ADR-0005 editados después de su aceptación, sin ADR de reemplazo
  (arrastre de S8). SonarCloud, credenciales y contribución se mantienen en orden.
