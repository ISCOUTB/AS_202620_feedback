> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# semana-09-evidencia-s9 · Clubs UTB


| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB` |
| Estado revisado | `652f78b76198ca854f7b3e79b910506e65ee4418` en `origin/master` (2026-09-27T23:39:11-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Esta pasada **no tiene cierre**: se califica la punta actual de `origin/master`. La punta actual es idéntica al estado calificado de S8 (`652f78b76198ca854f7b3e79b910506e65ee4418`) y `git log 652f78b..origin/master` está vacío: no hay ningún commit nuevo desde el cierre de S8. Por eso no hay porción S9 entregada y todas las filas se deciden contra el estado existente.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado (Cumple / No cumple) | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | No cumple | No hay porción S9: `git log 652f78b..origin/master` vacío. El único uso registrado de IA es de S8 (`docs/ia.md`, redacción del ADR-0004 y arc42 §7), que es línea base. |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | No cumple | `docs/aspectos.md` mantiene filas con `Código`/`Pruebas` en «Pendiente» (U3, C1, C2) y no tiene fila de una porción S9. La cadena no llega a la evidencia. |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | No cumple | No se añadió ningún ADR en el periodo: `docs/adr/` llega hasta `0004-despliegue-base-de-datos.md` (fecha 27/09/2026, estado «Propuesto»), de S8. No hay ADR de la porción S9. |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | No cumple | No hay prueba ni procedimiento nuevo del periodo. Existen `backend/tests/test_health.py`, `test_publicaciones.py` y `test_contrato_openapi.py`, anteriores a la punta de S8, sin evidencia de fallo ante un defecto. Los runs en rojo son del pipeline, no un fallo de prueba documentado ante el defecto. |
| Medición del escenario asociado | resultado contrastado con el umbral | No cumple | No hay medición en el periodo ni instrumentación: la dependencia `prometheus-fastapi-instrumentator` está declarada en `backend/requirements.txt:8` pero no se usa (sin ruta `/metrics` ni métrica ligada a un escenario). |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | No cumple | Último commit sobre `docs/ia.md`: `78579b6` (2026-09-27T18:13:03-05:00, fila S8). No hay entrada de S9. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | No cumple | No existe artefacto de auditoría de erosión en el repositorio. Contra el código, la única escritura de persistencia es `backend/src/linkclub/application/use_cases/crear_publicacion.py:33` (`self.repository.guardar(publicacion)`) y `backend/src/linkclub/adapters/inbound/api/publicacion_router.py:77`, sin contraste documentado de propiedad de datos. |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | No cumple | `git diff 652f78b..origin/master -- package.json requirements.txt pyproject.toml pom.xml go.mod Gemfile pubspec.yaml` está vacío: no se añadió ninguna dependencia en el periodo, así que no hay propuesta que verificar. |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | Cumple | El `git grep` de patrones solo coincide con variables y marcadores: `frontend/linkclub/lib/presentation/login_screen.dart:32` (asignación a `_passwordController`), `frontend/linkclub/lib/presentation/signup_screen.dart:32,38`, `infra/terraform/provider.tf:12` (`file("${path.module}/access-token")`, ruta no versionada) y `infra/terraform/resource.tf:14` (`database_password = "placeholder"`). Ningún `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` sin coincidencias. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | No cumple | El sistema no incorpora componente generativo (grep de `openai\|anthropic\|gemini\|llm\|gpt` sobre el backend sin coincidencias). No existe el ADR que justifique no incorporarlo. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_Clubs_UTB`, clon anónimo con `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | Responde sin autenticación y el nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | Árbol con `docs/arc42/`, `docs/adr/`, `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas existen. |
| Estado calificado identificable | `652f78b76198ca854f7b3e79b910506e65ee4418` en `origin/master`, `2026-09-27T23:39:11-05:00`. | Cumple | En esta pasada sin cierre se califica la punta actual; coincide con el hash de S8 y no hay commits posteriores. |
| Nombres de ADR según la convención | `docs/adr/0003- integacion rest openapi.md` (espacio inicial, no kebab-case) y `docs/adr/0003-API.md` duplicando el número 0003; `0004-despliegue-base-de-datos.md` sí conforma. | No cumple | Dos archivos rompen `NNNN-titulo-kebab-case.md` y repiten el 0003. |
| ADR aceptados no reescritos | ADR-0001 aceptado en `2c316f4` (2026-08-23) y editado en `c6c46e3` (2026-08-30); ADR-0002 editado en `e0eaca4` (2026-09-20) después de `743cc1f` (2026-09-13). | No cumple | Las ediciones son posteriores a la aceptación y no declaran ADR de reemplazo (CONTRATO §4). |
| `docs/ia.md` al día para la semana | Último commit `78579b6` (2026-09-27), con la fila S8. | No cumple | No hay entrada de la semana 9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Runs del hash revisado: `.github/workflows/backend-tests.yml` `failure` (https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/36378631444) y `.github/workflows/contrato.yml` `failure` (runs/36378632136). | No cumple | Hay runs en rojo en la rama y no existe `sonar-project.properties` ni invocación del scanner, ni URL pública con Quality Gate. |
| Sin credenciales en el repositorio ni en el historial | Barrido sin credenciales reales (solo `placeholder`, la ruta `access-token` y variables de formularios); ningún `.env` versionado; `git log -S"BEGIN PRIVATE KEY"` vacío. | Cumple | Sin hallazgos de secretos. |
| Contribución de todos los integrantes | `shortlog -sne`: Zavod Dev 73; Josh Ortega 23 + Josh4OP 6 (mismo correo); Luis-Salas-Reyes 9; deortahollman-star 9; Luis Daniel 5. | Cumple | Los cuatro integrantes declarados tienen commits; `Zavod Dev` se atribuye a Diego Andrés Ramos con reserva (no se consolida por parecido de nombre). |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `652f78b76198ca854f7b3e79b910506e65ee4418 2026-09-27T23:39:11-05:00 feat(infra): importar proyecto Supabase LinkClub con Terraform`
- **Veredicto**: sin entrega S9
- **Commits posteriores al cierre de S8**: ninguno; la punta actual es idéntica al hash calificado de S8.
- Resumen: no hay trabajo nuevo desde S8. El repositorio conserva la entrega parcial de S8 (Dockerfile y Terraform de Supabase, arc42 §7 y §2, estimación de costo) y arrastra sus pendientes: ambos workflows en rojo, sin URL pública, sin logs estructurados ni métrica instrumentada, sin ADR de plataforma para el hosting de la API, ADR 0003 duplicado y con nombre fuera de convención, y ADR aceptados editados. Para S9 no hay porción construida con IA, ni cadena, ni ADR, ni prueba, ni medición, ni entrada de IA, ni verificación de dependencias.

Pendientes que siguen abiertos:
- Entregar la porción S9 con su cadena completa (aspectos → ADR → código → prueba que falle ante el defecto → medición).
- Añadir a `docs/ia.md` lo aceptado, lo corregido y lo rechazado con motivo de la generación del periodo.
- Documentar la auditoría de erosión si la generación cruzó límites de contexto o las reglas de propiedad de datos de la semana 6.
- Poner en verde los workflows `backend-tests.yml` y `contrato.yml` sobre `origin/master`.
- Aportar la configuración de SonarCloud y la URL pública con Quality Gate.
- Unificar los ADR 0003 duplicados y no editar ADR aceptados sin declarar reemplazo.

## Recuento y nota sugerida

**1 de 10 criterios cumplidos.**

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Este informe no contiene filas No verificado: todas las comprobaciones se resolvieron leyendo el árbol de la punta. La ausencia de la entrega S9 es evidencia de ausencia, no una imposibilidad de comprobar.

## Hallazgos para la planilla

- La punta actual de `origin/master` es idéntica al hash calificado de S8: no hay ningún commit desde el cierre de S8, por lo que S9 no está entregada a la fecha de esta pasada temprana.
- No hay porción S9 ni su cadena; se arrastran los pendientes de S8 (workflows en rojo, SonarCloud ausente, métrica y logs pendientes, ADR 0003 duplicado, ADR aceptados editados).
- El barrido de credenciales sigue limpio (solo variables y `placeholder`) y la contribución sigue repartida entre los cuatro integrantes.
