# Evidencia S3 · TRACTAR

## Datos

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TRACTAR` |
| Estado revisado | `5f923cdcc4d30de8b78b234f4974547eb6027aa8` · 2026-08-23T22:40:51-05:00 («Feature: The S3 advances») |
| Cierre | 2026-08-24T05:00:00Z |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. Sin llamadas a la API (no hay `.github/workflows/`). |
| Nota de actualización | **Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo.** La revisión previa (22:00 COT del 23-ago) encontró el repo sin actividad de S3; el equipo subió el esqueleto completo el 23-ago a las 22:40 COT, dentro del cierre. No hay commits posteriores al cierre. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42.md:119-155` (§ Solution Strategy) | Cumple | Estrategia de solución con tabla «Cómo se logran los objetivos de calidad principales»: tácticas ligadas a QS-01 (offline encapsulado por módulo), QS-05 (menos indirección), QS-04 (autorización por módulo + hash de contraseñas) y QS-02/03 declarados pendientes para S4/S6, honesto. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/matriz_estilos.md` | Cumple | Los tres estilos (capas, hexagonal, monolito modular) contrastados contra los escenarios del equipo (QS-01 y QS-05 explícitos) y contra las restricciones de la sección 2; no es una tabla genérica de manual. Nota: QS-02/03/04 no se contrastan estilo por estilo; el árbol completo está en `docs/arc42/arc42.md` §10. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | kebab-case correcto. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Contexto, Decisión, Alternativas consideradas y Consecuencias (se gana / se asume / deuda aceptada). Observación menor: el título «Estilo arquitectónico: Monolito Modular» enuncia el tema con la decisión, pero sería más directo «Usar monolito modular» (CONTRATO §4). |
| Alternativas descartadas con su motivo | `docs/adr/0001-estilo-arquitectonico.md` («Alternativas consideradas») | Cumple | Capas descartado por el coste transversal de la sincronización offline (QS-01); hexagonal por costo/tiempo del equipo. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md:29-33` → `[ADR-0001](adr/0001-estilo-arquitectonico.md)`; `docs/arc42/arc42.md` QS-01 y QS-05 → `../adr/0001-estilo-arquitectonico.md` | Cumple | Ambos enlaces resuelven. Hallazgo: dentro del ADR, el enlace a `../arc42/10_requisitos_calidad.md` está roto (ese archivo no existe; el contenido vive en `arc42.md`); y en `aspectos.md` los enlaces a requisitos (`arc42.md#qs-…`) apuntan a una ruta inexistente (`docs/arc42.md`). |
| Arranque con un solo comando documentado en el README | `README.md` («Cómo arrancar (un solo comando)») + `run.sh` | Cumple | `./run.sh` crea venv, instala, migra, corre pruebas y levanta el servidor; documentado paso a paso con verificación vía `curl /salud/`. No ejecutado (regla del kit). |
| Prueba automatizada en verde | `apps/core/tests.py` (`test_health_check_responde_200`); sin `.github/workflows/` | No verificado | La prueba existe y `run.sh` la ejecuta como parte del arranque, pero no hay pipeline ni evidencia de ejecución aportada (URL de run o captura) que pruebe el verde. |
| Estructura de paquetes correspondiente al estilo del ADR | `apps/{core,usuarios,vehiculos,viajes,facturacion}/` + `config/` | Cumple | Coincide con el monolito modular del ADR sobre Django: un módulo por dominio con frontera declarada. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación; `ISCOUTB/AS_202620_TRACTAR`. |
| Estructura mínima presente | No cumple | Desviaciones: sin `docs/c4/` (el C4 está en `docs/arc42/images/c4_nivel1_contexto.png`); `ficha_problema.md` en la raíz. El artefacto se evalúa donde está, pero la ruta mínima no se cumple. |
| Estado calificado identificable | Cumple | `5f923cd` · 2026-08-23T22:40:51-05:00 ≤ cierre; sin etiqueta (evidencia semanal, correcto). |
| Nombres de ADR según la convención | Cumple | `0001-estilo-arquitectonico.md` pasa el filtro. |
| ADR aceptados no reescritos | Cumple | Un solo commit sobre el ADR (`5f923cd`, el de creación). Estado «Aceptado». |
| `docs/ia.md` al día para la semana | No cumple | Último commit sobre el archivo: `e84871f` 2026-08-16; sin entradas del trabajo S3 (ADR, matriz, esqueleto) y sin rechazos con motivo técnico. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. |
| Contribución de todos los integrantes | No cumple | `git shortlog -sne` → 16 commits, todos de Sebastian Garcia Devoz (dos identidades + correo institucional); 3 de 4 integrantes sin aparición. |

## Recuento

**7 de 9** criterios de la ficha cumplidos (1 no verificado, 0 no cumplidos).

## No verificado / pendientes

- Test en verde: existe `apps/core/tests.py` y `run.sh` lo ejecuta, pero sin pipeline ni run aportado no se puede certificar el verde. Vale el comando declarado; la comprobación requiere ejecutar (se hará en la revisión del corte si ya hay CI).

## Hallazgos para la planilla

- Sin commits posteriores al cierre: todo lo evaluado entró antes de la medianoche (bien).
- `docs/adr/0001-estilo-arquitectonico.md`: enlace roto a `../arc42/10_requisitos_calidad.md` (el archivo no existe; es `arc42.md`).
- `docs/aspectos.md`: los enlaces a requisitos usan `arc42.md#qs-…`, ruta inexistente (debería ser `arc42/arc42.md`).
- Basura versionada: `__pycache__/*.pyc` (en todos los paquetes) y `db.sqlite3`; `.gitignore` solo ignora `venv/`.
- `docs/ia.md` sin entradas del trabajo S3 (ADR, matriz, esqueleto) y sin rechazos con motivo.
- 3 de 4 integrantes sin commits en el repositorio; urge antes del corte 1.

## Estado del contrato del repositorio

Ver la matriz transversal arriba.
