# semana-06-evidencia-s6 · EnAgenda

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_EnAgenda` |
| Estado revisado | `0a58de8` en `origin/master` (2026-09-13T23:38:41-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/arquitectura/contextos-y-propiedad-de-datos.md (mapa Mermaid y tabla de relaciones tipificadas) | Cumple | Nombra Eventos, Invitaciones, Tareas, Agenda, Presupuesto, Panel y Compartido con relaciones cliente-proveedor, proveedor-consumidor y núcleo compartido; menciona capa anticorrupción. |
| Tabla módulo a datos con dueño único por entidad | docs/arquitectura/contextos-y-propiedad-de-datos.md (tabla 'Propiedad de datos y permisos') | Cumple | Cada entidad o dato tiene un único contexto dueño y se indica quién puede consultarlo y modificarlo. |
| La tabla cubre las entidades que existen en el código | docs/arquitectura/contextos-y-propiedad-de-datos.md ('Cobertura frente al código actual') y src/invitaciones/dominio/invitaciones.py | Cumple | La única entidad implementada (Invitacion) está cubierta; los demás contextos se declaran planificados. |
| Violaciones de propiedad de datos detectadas sobre el código actual | docs/arquitectura/contextos-y-propiedad-de-datos.md (tabla 'Verificación de violaciones de propiedad') | Cumple | Documenta el recorrido de verificación (escrituras y referencias) y concluye sin violaciones en el código actual. |
| Plan de corrección por violación | docs/arquitectura/contextos-y-propiedad-de-datos.md (sección 'Plan de corrección') | Cumple | Define acción correctiva y responsable por tipo de violación, aunque no haya violaciones activas. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-conceptos-transversales.md | Cumple | Incluye lenguaje ubicuo en 8.1 y referencia al mapa de contextos en 8.2; el mapa está enlazado, no incrustado. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/nivel-3-componentes.md existe; falta hash de S5 para comparar | No verificado | No se pudo verificar si los límites cambiaron porque no se aportó el hash de la revisión definitiva de S5. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md (fila A-01) y docs/arquitectura/contextos-y-propiedad-de-datos.md | Cumple | A-01 se relaciona con Invitaciones; los demás contextos aún no tienen aspectos, lo que es esperable en esta etapa. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio ISCOUTB/AS_202620_EnAgenda visible; autores consolidados: Daoisttl0FB3/GabrielaMorales Cancino (mismo correo), Jein-12, eliabarnedocondef10-gif | Cumple | Tres identidades consolidadas coinciden con los integrantes declarados. |
| Estructura mínima | docs/arc42/ (01-12), docs/adr/0001-usar-monolito-modular.md, docs/c4/nivel-1..3, docs/aspectos.md, docs/ia.md, README.md | Cumple | Estructura mínima presente; se versionan archivos __pycache__ que deberían ignorarse. |
| Estado del repositorio calificado | Hash 0a58de8 (2026-09-13T23:38:41-05:00) en origin/master, anterior al cierre; sin commits posteriores | Cumple | Commit vigente correcto para la semana 6. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Nombre y estructura cumplen la convención; no se observan reescrituras. |
| Tabla de aspectos | docs/aspectos.md con fila A-01 y 8 columnas navegables (C4, ADR, código, pruebas, evidencia) | Cumple | Solo una fila; el resto de contextos aún sin aspectos asociados. |
| Registro de uso de IA | docs/ia.md con usos, aceptaciones, rechazos y verificación; log con commits en varias fechas | Cumple | Incluye rechazos con motivo técnico, como exige el contrato. |
| README | README.md con descripción, requisitos, instalación, arranque (python app\web.py) y pruebas (pytest -q) | Cumple | Arranque con un solo comando y pruebas documentadas. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta pytest; runs_ci con conclusión success (ej. run 34806818454) | No cumple | Falta el análisis estático con SonarCloud (organización isco-utb) exigido por el contrato. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0a58de865e0ddcde35c2b6fb73433c8611752219 2026-09-13T23:38:41-05:00 Update ia.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto EnAgenda con monolito modular, corte vertical de invitaciones implementado y documentación arc42 completa. Mapa de contextos y propiedad de datos definidos para la semana 6.

Pendientes que siguen abiertos:
- SonarCloud no configurado en el pipeline.
- Pendientes de la semana 5: reto nuevo, medición, incremento y umbral.
- Ampliar la tabla de aspectos a más contextos.
- Eliminar archivos __pycache__ del repositorio.

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Criterio 7 de la ficha: comparación de límites con S5 requiere el hash de la revisión definitiva de S5.

## Hallazgos para la planilla

- Archivos __pycache__ versionados en src/ y tests/.
- SonarCloud no configurado en el pipeline; solo pytest.
- Pendientes de la semana 5 (reto nuevo, medición, incremento, umbral) declarados en docs/correcciones.md sin resolver.
- Solo un aspecto (A-01) en docs/aspectos.md; Eventos, Tareas, Agenda, Presupuesto y Panel sin aspectos asociados.
- C4 nivel 3 existe pero no se pudo verificar reajuste de límites por falta del hash de S5.
