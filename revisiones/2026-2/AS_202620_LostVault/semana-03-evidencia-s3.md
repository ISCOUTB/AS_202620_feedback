# Evidencia S3 · LostVault

## Datos

| | |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `1ddb82624ec123d21c1fff06bb3bc9890b8326f4` · 2026-08-23T23:57:37-05:00 (`Create front_end`) |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre 2026-08-24T05:00:00Z) |
| Revisión actualizada tras el cierre | el equipo empujó después de la primera revisión (que vio `2968d88f`); hash calificado definitivo `1ddb826`, último commit ≤ cierre. Sin commits posteriores al cierre. |
| Comandos | clon efímero `--filter=blob:none --no-checkout`; `git log -1 --until=2026-08-24T05:00:00Z`; `git ls-tree`; `git show`; `git grep`. Sin API de CI (no hay `.github/workflows/`). |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/04_estilo_arquitectonico.md` en `1ddb826` | No cumple | Sigue describiendo los tres estilos en abstracto (ventajas/desventajas genéricas); no hay estrategia ni tácticas ligadas a los escenarios 1-4 de `10_requisitos_calidad.md`. |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/arc42/04_estilo_arquitectonico.md` (tabla) | No cumple | Tabla genérica (Simplicidad, Testabilidad, Facilidad de evolución…); la fila «Adecuación a LostVault» no compara contra los escenarios del equipo. Es el caso de tabla genérica que la ficha descarta. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Pasa el filtro; sin cambios respecto a la revisión anterior. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Estado «Aceptado»; decisión clara con regla de dependencias por módulo. El título («Estilo arquitectónico base de LostVault») enuncia el tema, no la decisión con verbo. |
| Alternativas descartadas con su motivo | `docs/adr/0001-estilo-arquitectonico.md` | Cumple | Capas y hexagonal descartadas cada una con «Por qué no se eligió» explícito. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` en `1ddb826` (enlaza a los escenarios 1-4, no al ADR); `docs/arc42/10_requisitos_calidad.md` (escenarios sin enlace al ADR) | No cumple | El ADR solo es alcanzable desde la nota de la matriz (`04_estilo_arquitectonico.md`). Ni aspectos ni los escenarios enlazan al ADR. |
| Arranque con un solo comando documentado en el README | `README.md` en `1ddb826` («Ejecutar»: `flutter run`, con `flutter pub get` previo) + `pubspec.yaml` | Cumple | El README se reescribió como guía del esqueleto con comando único y requisitos previos. Ejecución real: No verificado por regla del kit (no se ejecuta código del estudiante). |
| Prueba automatizada en verde | `test/widget_test.dart` en `1ddb826` (verifica que `LostVaultApp` renderiza) | No verificado | La prueba existe, pero no hay `.github/workflows/` ni evidencia de ejecución aportada. Haría falta un run de CI o la evidencia de ejecución de Moodle. |
| Estructura de paquetes correspondiente al estilo del ADR | `git ls-tree -r --name-only 1ddb826` en `lib/`: solo `lib/main.dart` | No cumple | El ADR y el README declaran `lib/core` y `lib/features/{authentication,objects,search,claims,identity_verification,users}`, pero git no versiona directorios vacíos: esos paquetes no existen. Además quedaron en la raíz dos archivos basura de 1 byte (`front_end`, `ejecutable`). |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | `ISCOUTB/AS_202620_LostVault`, clonado sin autenticación. |
| Estructura mínima presente | No cumple | Faltan `docs/c4/` (el C4 está en `docs/arc42/c4_contexto.png`); las otras cinco rutas existen. |
| Estado calificado identificable | Cumple | Sin etiqueta (no exigible en evidencia semanal); hash `1ddb826` y `%cI` 2026-08-23T23:57:37-05:00, último ≤ cierre. |
| Nombres de ADR según la convención | Cumple | `ls docs/adr` sin salida en el filtro. |
| ADR aceptados no reescritos | Cumple | Historial con dos commits: creación (`723d9e6`) y renombrado (`d0e7078`); sin reescritura de contenido. |
| `docs/ia.md` al día para la semana | No cumple | Última entrada del 08-ago; sin entradas de S3 y sin lo rechazado con motivo. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` de secretos sin coincidencias (exit 1); sin `.env` versionado. |
| Contribución de todos los integrantes | Cumple | 4 identidades / 4 integrantes: Roy Gonzalez 24; `shamarallorente-blip` 1 (PR #1); `Fausto-4` 1 (PR #3, correo `ganonimo2504`); `weller-rar` 1 (PR #4, correo `pelu.kiefer@gmail.com`, primera aparición en la actualización). Correspondencias por confirmar con el docente (Fausto-4→España, weller-rar→Monterroza parecen plausibles). |

## Recuento

**4 de 9** criterios cumplidos.

## No verificado / pendientes

- Prueba en verde: sin pipeline ni evidencia de ejecución; haría falta el run de CI o la evidencia de Moodle.
- Ejecución real del arranque: No verificado por regla del kit (comando declarado: `flutter run`).

## Hallazgos para la planilla

- Lo nuevo tras la primera revisión (commits `f0d6e01`…`1ddb826`): README del esqueleto con comando único, `pubspec.yaml` y `test/widget_test.dart`; el cuarto integrante (`weller-rar`, PR #4) aparece por primera vez.
- La sección 4 y la matriz siguen siendo la descripción genérica de estilos que la ficha descarta: falta comparar contra los escenarios 1-4.
- Los paquetes de módulos declarados en el ADR siguen sin existir: solo `lib/main.dart`; el checklist del README los da por creados.
- Quedaron dos archivos basura en la raíz (`front_end` y `ejecutable`, 1 byte cada uno), residuo de los intentos de subir el front por zip (`cd5ee95`, `c96e048`, `4f243e0`, `b16fcf0`, `9038dc2`).
- El ADR no es alcanzable desde `aspectos.md` ni desde los escenarios.
- `ia.md` sin actualizar desde el 08-ago. Sigue faltando `docs/c4/`.
- Sin commits posteriores al cierre.
