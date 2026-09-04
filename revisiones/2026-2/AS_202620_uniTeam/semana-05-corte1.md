# Primer corte · reto de línea base arquitectónica · uniTeam

> Revisión manual preliminar completa, realizada antes del cierre. El equipo puede cambiar el repositorio y la valoración debe repetirse después del 2026-09-07T05:00:00Z.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_uniTeam` |
| Estado revisado | `dc14298c32a4fde0956266b0300063c24d7a9486` (2026-08-29T11:49:10-05:00) |
| Etiqueta `corte-1` | Ausente |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | Revisión manual con Codex, sin ejecutar código estudiantil |

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | `git tag --list` no devolvió etiquetas; HEAD `dc14298` | No cumple | La valoración preliminar usa HEAD. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | El PDF se excluye del repositorio según `docs/ia.md:55`; Moodle no está disponible | No verificado | Debe comprobarse en Moodle. |
| Impacto de la restricción localizado en requisitos, C4 y código | Hay trazabilidad interna para OIDC en `docs/aspectos.md:25`, pero la restricción asignada no está en el kit ni se identifica como reto S5 | No verificado | No puede confirmarse que sea la respuesta solicitada. |
| Línea base medida y verificable antes del cambio | `docs/calidad/mediciones/esc-01-linea-base.md:10-15` documenta carga, resultado y umbrales; `README.md:189-191` resume p95 de 762 ms | Cumple | La medición declara además sus límites de validez. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | `docs/adr/0005-delegar-la-autenticacion-en-un-proveedor-oidc.md:3-44` está aceptado y registra opciones, decisión y consecuencias | No verificado | Es sólido internamente, pero el repositorio no lo declara como el reto asignado. |
| Cambio implementado y ejecutable de extremo a extremo | OIDC aparece en `app/api/seguridad.py`, `web/lib/oidc.ts` y `test/test_autenticacion.py`; no se identifica como cambio S5 | No verificado | Falta la relación explícita con el reto. |
| Límites declarados conservados tras el cambio | C4 y código representan proveedor de identidad, aplicación web y API (`docs/c4/nivel1-contexto.md:56-60`; `nivel2-contenedores.md:95-112`) | No verificado | Sin reto identificado no se puede cerrar el antes/después. |
| Prueba que cubre el cambio, en verde en el pipeline | Run CI exitoso para HEAD: `https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/33263993238`; workflow en `.github/workflows/ci.yml:42-45` | No verificado | El verde es verificable, pero no se conoce cuál cambio constituye el reto. |
| Resultado contrastado con el umbral del escenario y reproducible | La medición de ESC-01 es una línea base previa; no se encontró resultado posterior a un cambio del reto | No cumple | Falta comparación antes/después. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | `docs/aspectos.md:25` enlaza la cadena de autenticación hasta la prueba y ESC-03 | No verificado | La cadena existe, pero no se acredita que corresponda al reto asignado. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | `docs/ia.md:55-56` contiene decisiones y rechazos de S2/S4; no hay entrada identificada como corte 1 | No cumple | El último cambio del archivo es anterior al inicio de S5. |
| Sustentación del reto | Requiere la sesión con el equipo | No verificado | Lo fija el docente. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Clon anónimo de `ISCOUTB/AS_202620_uniTeam` | Cumple | Nombre y visibilidad correctos. |
| Estructura mínima presente | Las seis rutas obligatorias están en HEAD | Cumple | Incluye documentación, código, pruebas y CI. |
| Estado calificado identificable | HEAD `dc14298`, sin etiqueta `corte-1` | No cumple | En el corte se exige la etiqueta. |
| Nombres de ADR según la convención | `docs/adr/0001-...` a `0005-...` | Cumple | Convención corregida. |
| ADR aceptados no reescritos | ADR 0001 declara reemplazo por 0002; los demás conservan estados aceptados | Cumple | La evolución queda explícita. |
| `docs/ia.md` al día para la semana | Último cambio del archivo: `dc14298`, 2026-08-29, antes del periodo S5 | No cumple | Falta una entrada del corte. |
| Sin credenciales en el repositorio ni en el historial | Barridos en HEAD e historial sin valores de credenciales | Cumple | Las apariciones de `token` son identificadores de código. |
| Contribución de todos los integrantes | El historial muestra cinco identidades; tres son atribuibles por nombre y las restantes no pueden asignarse por parecido | No verificado | El docente debe confirmar la correspondencia de `super-gremlin` y `JuanB`. |

## Estado global del proyecto en HEAD

- **Veredicto:** base técnica sólida, corte 1 todavía no identificable.
- El proyecto tiene documentación coherente, CI verde, trazabilidad amplia y una línea base reproducible.
- No hay etiqueta ni commits posteriores al inicio de S5; tampoco se declara cuál artefacto responde a la restricción asignada.
- Las evidencias existentes pueden convertirse en una respuesta fuerte si el equipo explicita el reto y aporta resultado posterior al cambio.

## Nivel de rúbrica sugerido

| Criterio | Nivel sugerido | Puntaje preliminar | Evidencia que lo sostiene |
|---|---|---:|---|
| Diagnóstico del reto | Insuficiente | 0,00 | Existe línea base, pero no se identifica el reto ni su impacto. |
| Alternativas y decisión | Insuficiente | 0,00 | El ADR OIDC es sólido, pero no está acreditado como respuesta al reto. |
| Aplicación sobre el corte vertical | Insuficiente | 0,00 | No se identifica un cambio S5. |
| Pruebas, medición y trazabilidad | Básico | 0,60 | Hay CI verde, trazabilidad y línea base, sin resultado posterior vinculado al reto. |
| Sustentación del reto | Pendiente del docente | — | No verificable desde el repositorio. |
| **Subtotal técnico preliminar** |  | **0,60 / 4,00** | No es la nota final del corte. |

## Recuento

1 de 12 criterios de la ficha cumple. El recuento no se convierte mediante la fórmula semanal porque este corte tiene rúbrica propia.

## Pendientes y preguntas para la sustentación

- ¿Cuál fue la restricción asignada y qué ADR contiene su decisión?
- ¿Qué parte del sistema cambió después de medir la línea base?
- ¿Cuál es el resultado posterior y cómo se contrasta con el umbral?
- ¿A qué integrantes corresponden las identidades de Git no confirmadas?
