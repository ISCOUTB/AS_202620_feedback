> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · Tienda virtual UTB

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB` |
| Estado revisado | `bc38c9bab2830e8f2c855c0e36542d849565955e` en `origin/main` (2026-09-28T10:22:29-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene corte**: se califica la punta actual del 2026-10-01. El periodo S9
(`858e78f..bc38c9b`) tiene **cuatro commits** del 2026-09-28 que declaran la infraestructura de
producción como código con Terraform (`4904d94`, `4665f80`, `f28563b`, `bc38c9b`), más un quinto
commit `858e78f` ya calificado en S8. Bajo CONTRATO §12 las filas que describen la entrega S9 se
deciden con la evidencia del periodo; la fila de credenciales y la matriz transversal se deciden
sobre el estado en la punta. Existe también `master`, residual (2026-08-09): la rama principal es
`main`.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | En el periodo: `infra/providers.tf`, `infra/neon-project.tf`, `infra/render-web-service.tf`, `infra/vercel-project.tf`, `infra/github-branch-protection.tf` y `.github/workflows/terraform.yml`; commits `4904d94`…`bc38c9b`; `docs/ia.md` (entrada 2026-09-28, herramienta «OpenCode (big-pickle)»). | Cumple | Porción real del sistema (IaC de despliegue) versionada en el periodo y construida con apoyo de IA declarado. |
| Cadena completa navegable para esa porción | `docs/aspectos.md` no se modificó en el periodo (diff `858e78f..bc38c9b` vacío para ese archivo); sus filas `AC-01`…`AC-04` siguen siendo de S6/S8. | No cumple | No hay fila de aspectos que lleve a la porción S9; la cadena no existe para esta evidencia. |
| ADR con la decisión argumentada por el equipo | `docs/adr/0006-infra-como-codigo-terraform.md`: contexto de los cinco sitios dispersos, alternativas (OpenTofu, Pulumi, Terraform Cloud, estado versionado) con motivo de descarte, decisión y consecuencias con las restricciones del proyecto (cuatro capas gratuitas, «secretos nunca en el repo»). | Cumple | ADR del periodo que argumenta la decisión con alternativas y restricciones; el propio documento se declara pendiente de aprobación final del equipo. |
| Prueba que falla ante el defecto que cubre | El workflow `terraform.yml` corre `fmt`, `validate` y `tflint`, pero no hay run en rojo, prueba de mutación ni procedimiento documentado que demuestre un fallo inducido en el periodo. | No verificado | La verificación estática es correcta pero no es la prueba que falla ante el defecto; queda como pregunta de sustentación (CONTRATO §13). |
| Medición del escenario asociado | No hay medición nueva del periodo contrastada con umbral; `docs/despliegue-terraform.md` documenta el runbook, no una medición. | No cumple | Sin medición del escenario asociado a la porción S9. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | `docs/ia.md` (entrada 2026-09-28) documenta lo aceptado y varios rechazos con motivo técnico: descarta `terraform import`, Terraform Cloud, el estado cifrado/versionado, el subdirectorio por proveedor, `terraform plan` en CI y exigir el check `sonarcloud`. | Cumple | Extracto del periodo con lo aceptado y lo rechazado con su motivo técnico. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | El barrido `erosión\|límite de contexto` en `docs/` (excluido `docs/openapi`) no devuelve coincidencias. | No cumple | No hay auditoría de erosión del periodo; la deuda de esquema (V6) se menciona en ADR-0006 pero no es una auditoría de erosión. |
| Dependencias propuestas verificadas en su registro oficial | El diff del periodo contra `858e78f` está vacío en `package.json`, `backend/requirements.txt`, `frontend/package.json` y demás manifiestos. | No cumple | La porción S9 añade proveedores Terraform (`infra/.terraform.lock.hcl`), fuera de los registros npm/PyPI que designa el método; no hay dependencias de esos manifiestos que verificar. |
| Sin credenciales en código, ejemplos ni documentación generada | Barrido de patrones de credenciales sobre la punta: sin coincidencias; `infra/terraform.tfvars.example` sin valores reales y `infra/README.md` indica exportar los tokens por shell; `.gitignore` excluye `*.tfstate` y `terraform.tfvars`; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | Sin credenciales reales; `.env.example` versionado sin valores. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No hay componente generativo en el sistema ni ADR que decida no incorporarlo; el barrido `generativ\|llm\|openai\|anthropic\|gemini` no devuelve coincidencias en `docs/`. | No cumple | La porción S9 es IaC; no hay decisión registrada sobre un componente generativo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB`, clonado sin autenticación; rama principal `origin/main`. | Cumple | Nombre `AS_202620_<PROYECTO>` conforme y visibilidad pública. |
| Estructura mínima presente | En `bc38c9b`: `README.md`, `docs/arc42/`, `docs/adr/` (0001-0006), `docs/c4/`, `docs/aspectos.md` y `docs/ia.md`. | Cumple | Las seis rutas; arc42 vive en un único archivo (desviación de ruta admitida por CONTRATO §2). |
| Estado calificado identificable | `origin/main`, `bc38c9bab2830e8f2c855c0e36542d849565955e`, 2026-09-28T10:22:29-05:00. | Cumple | Sin cierre en esta pasada: se identifica la punta actual. |
| Nombres de ADR según la convención | `docs/adr/0001`…`0006` en kebab-case; el filtro de la convención no devuelve residuos. | Cumple | — |
| ADR aceptados no reescritos | `git log --follow`: ADR-0001 creado `f4602a3` (2026-08-21) y editado `e8ae57d` (2026-08-31); ADR-0002 creado `0416e62` (2026-09-15) y editado `befb0bc` (2026-09-27), sin ADR sucesor declarado. | No cumple | Se editaron ADR aceptados sin declarar reemplazo; ya venía registrado desde S7/S8. |
| `docs/ia.md` al día para la semana | Commit `4904d94` (2026-09-28) añade la entrada del periodo, con lo aceptado y lo rechazado con motivo. | Cumple | El registro creció dentro del periodo S9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del hash revisado (`head_sha=bc38c9b`): 324 runs, en su mayoría del cron `Keep-alive`; hay al menos dos en `failure` ([36826802735](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/36826802735) y [36802694698](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/36802694698)). No hay URL pública de análisis con Quality Gate verificable. | No cumple | Hay runs en rojo sobre el hash revisado y falta la evidencia de SonarCloud que exige CONTRATO §8. |
| Sin credenciales en el repositorio ni en el historial | Barridos de credenciales sobre `bc38c9b` sin coincidencias más allá de variables `token` de un HTML de terceros en `docs/openapi/`; sin `.env` versionado; `.gitignore` cubre el estado de Terraform. | Cumple | Sin credenciales reales. |
| Contribución de todos los integrantes | `git shortlog -sne bc38c9b` consolidado por correo idéntico: Jasen/Jasen Yukopila (15), RAZOR7150 (11), pxtroniwnl (10) y shalom-A26 (2). | Cumple | Los cuatro integrantes declarados en EQUIPOS.md tienen commits. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `bc38c9bab2830e8f2c855c0e36542d849565955e` 2026-09-28T10:22:29-05:00 `Corrige la region de Render, que estaba sin verificar, y registra el estado real de las credenciales` (`origin/main`)
- **Veredicto**: con avance de S9 (IaC con Terraform) y pendientes operativos
- Resumen: la punta de `main` va cuatro commits por delante del hash calificado de S8. El periodo
  declara la infraestructura de producción como código con Terraform (cuatro proveedores), con
  workflow de verificación estática, ADR-0006, runbook de corte, `docs/pendientes.md` y una entrada
  de `docs/ia.md` que documenta lo aceptado y lo rechazado. Ese avance satisface la porción real con
  IA (fila 1), el ADR (fila 3) y el extracto de `docs/ia.md` (fila 6); no cumple la cadena de
  aspectos (fila 2, `docs/aspectos.md` sin tocar), la prueba que falla (fila 4), la medición (fila 5),
  la auditoría de erosión (fila 7), las dependencias de los manifiestos (fila 8) ni la decisión sobre
  el componente generativo (fila 10). Se mantienen las no conformidades transversales: ADR aceptados
  reescritos, `docs/ia.md` con pendientes, y pipeline con runs en rojo y sin Quality Gate público. El
  despliegue real sigue siendo el del 2026-09-27: **no se ejecutó ningún `apply`**.

Pendientes que siguen abiertos:
- Cadena de aspectos para la porción S9: `docs/aspectos.md` no se actualizó en el periodo.
- Prueba que falle ante el defecto: solo hay `fmt`/`validate`/`tflint`, no un defecto inducido.
- Medición del escenario asociado a la porción S9.
- Auditoría de erosión del periodo.
- Verificación de las dependencias de los manifiestos del periodo (no hubo).
- Decisión registrada sobre el componente generativo.
- Runs `Keep-alive` en rojo y falta el Quality Gate público de SonarCloud.
- ADR-0001 (`e8ae57d`) y ADR-0002 (`befb0bc`) editados tras aceptarse sin sucesor.
- El despliegue de producción no se migró: falta crear los cuatro tokens de Terraform y ejecutar el `apply`.

## Recuento y nota sugerida

**4 de 10 criterios** de la ficha en Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

Bajo CONTRATO §12, las filas 1, 3 y 6 se resuelven con evidencia del periodo S9 (la IaC con Terraform,
su ADR-0006 y la entrada de `docs/ia.md`), y el barrido de credenciales sobre la punta; las demás
filas de la entrega S9 carecen de artefacto del periodo y quedan en No cumple o No verificado.

## No verificado / pendientes

- Prueba que falla ante el defecto: **No verificado**. El workflow `terraform.yml` valida estáticamente
  pero no hay run en rojo, prueba de mutación ni procedimiento documentado del periodo. Queda como
  pregunta de sustentación.
- Medición de escenarios: no hay medición nueva del periodo.
- Auditoría de erosión: no existe artefacto del periodo que la documente.
- Dependencias del periodo: los manifiestos npm/PyPI no cambiaron; los proveedores Terraform quedan
  fuera de los registros que designa el método.
- Componente generativo: no existe ni hay ADR de no incorporarlo.
- La migración a Terraform no se aplicó: producción sigue siendo la del 2026-09-27.

## Hallazgos para la planilla

- S9 con avance real: IaC de despliegue con Terraform en `infra/` (cuatro proveedores), workflow de verificación estática, ADR-0006 con alternativas y `docs/ia.md` actualizado con rechazos motivados.
- `docs/aspectos.md` no se tocó en el periodo: no hay fila de trazabilidad para la porción S9.
- No hay prueba que falle ante el defecto, medición del escenario, auditoría de erosión ni decisión sobre componente generativo.
- Pipeline del hash revisado con runs `Keep-alive` en rojo y sin Quality Gate público de SonarCloud.
- ADR-0001 y ADR-0002 editados tras aceptarse sin declarar reemplazo.
- El `apply` de Terraform no se ejecutó: el despliegue real sigue siendo el del 2026-09-27.
