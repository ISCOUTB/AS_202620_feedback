# semana-06-evidencia-s6 · ShareU

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `c389364` en `origin/master` (2026-09-13T23:21:08-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/ddd/contextos.md (c389364): tabla de 5 contextos y tabla de relaciones con tipos Customer/Supplier y capa anticorrupción candidata. | Cumple | Tipifica cada relación y marca cuáles están implementadas y cuáles no. |
| Tabla módulo a datos con dueño único por entidad | docs/ddd/propiedad-datos.md (c389364): columna 'Dueño (único escritor)' y 'Cómo lee' por dato. | Cumple | Declara un solo escritor por dato y el mecanismo de lectura permitido. |
| La tabla cubre las entidades que existen en el código | docs/ddd/propiedad-datos.md cubre la tabla documentos y la columna calificacion de app/documentos/repository.py, y marca usuarios/calificaciones/administracion como sin tabla. | Cumple | Contrasta con la única tabla real del corte vertical. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/ddd/auditoria-violaciones.md V1-V4, con ubicación en app/documentos/repository.py (columnas calificacion y autor). | Cumple | V1 documenta la ambigüedad de 'calificación' dentro del contexto Documentos. |
| Plan de corrección por no conformidad | docs/ddd/auditoria-violaciones.md: pasos 1-6 de V1 y plan preventivo de V2, V3 y V4. | Cumple | El plan de V1 queda como ADR 0003 propuesto, aún sin ejecutar. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42.md sección 8 remite a docs/ddd/contextos.md, propiedad-datos.md y auditoria-violaciones.md. | Cumple | Se incorpora por enlace; la sección no incrusta el diagrama ni un glosario propio. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/adr/0003-separacion-contexto-calificaciones.md existe, pero el árbol c389364 solo tiene docs/c4/nivel1.mmd, nivel2.mmd, nivel-2.md y NIVEL2.png, sin nivel 3. | No cumple | Además no se aportó el hash de la revisión de S5 para ejecutar el diff. |
| Aspectos relacionables con los contextos del mapa | docs/ddd/contextos.md cita docs/aspectos/aspectos.md como fuente del lenguaje; la fila '≤ 3 interacciones · Usabilidad · ADR 0002' se relaciona con el contexto Búsqueda. | Cumple | Usuarios, Calificaciones y Administración no tienen fila de aspecto asociada. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo ISCOUTB/AS_202620_ShareU, visible:true; historial c389364 con las cuentas Dayana, luiscorredor, Nicolas-HH, daynarvaez y steven. | Cumple | Cuatro integrantes declarados frente a cinco cuentas de git; no se atribuyen cuentas a personas por parecido de nombre. |
| Estructura mínima | Árbol c389364 con README.md, docs/arc42/arc42.md, docs/adr/, docs/c4/, docs/aspectos/aspectos.md y docs/ia/ia.md. | Cumple | aspectos e ia están en subcarpeta (desviación de ruta, no ausencia); hay un PDF dentro de docs/adr. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md, 0002-usabilidad-busqueda-en-una-solicitud.md y 0003-separacion-contexto-calificaciones.md, numerados en kebab-case y con contexto, opciones, decisión, consecuencias y trazabilidad. | Cumple | 0003 está en estado Propuesto y no se aporta log de ediciones posteriores a su aceptación. |
| Tabla de aspectos | docs/aspectos/aspectos.md: la tabla de trazabilidad tiene 6 columnas (Requisito, Aspecto, ADR, Código, Prueba, Evidencia) y 2 filas, sin ID ni C4. | No cumple | Faltan dos de las ocho columnas del contrato y no hay filas navegables por aspecto. |
| Registro de uso de IA | docs/ia/ia.md registra tarea, herramienta, qué se aceptó y qué se rechazó con motivo (por ejemplo, descartar hexagonal y no quitar --require-hashes). | Cumple | Vive en docs/ia/ia.md, no en docs/ia.md; el comando del contrato sobre esa ruta no devuelve historial. |
| README | README.md declara qué es, requisitos previos, instalación, arranque con 'uvicorn app.main:app --reload' y pruebas con 'pytest -q'. | Cumple | El arranque queda en un solo comando reproducible. |
| Pipeline y análisis estático | .github/workflows/tests.yml ejecuta pytest y el run 'Tests' del 2026-09-14T04:21:11Z concluye success (https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/34805722952), pero el workflow no tiene paso de scanner ni existe sonar-project.properties. | No cumple | El README solo aporta un badge; falta la URL del run del scanner y la URL pública del análisis con su Quality Gate. |
| Secretos | Sin coincidencias de patrones de secretos y sin .env versionado en c389364. | Cumple | La comprobación es sobre HEAD; si apareciera un secreto habría que rotarlo, no solo borrarlo. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `0bae18410091824e51739f1bfc6fe0eabf954013 2026-09-14T15:26:52-05:00 Delete docs/adr/ShareU_Trazabilidad.pdf`
- **Veredicto**: con pendientes
- Resumen: En la punta actual (0bae184, 2026-09-14T15:26:52-05:00) el trabajo de S6 sobre contextos y propiedad de datos está bien documentado y es citable, pero falta el C4 nivel 3 exigido por el cambio de límites, la tabla de aspectos está incompleta y SonarCloud no es auditable; siguen abiertos pendientes de S5.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- 0bae184 (2026-09-14T15:26:52-05:00, posterior al cierre 2026-09-14T05:00:00Z): elimina docs/adr/ShareU_Trazabilidad.pdf; es exactamente el diff respecto del estado calificado c389364.

Pendientes que siguen abiertos:
- C4 nivel 3 del reajuste de límites de Calificaciones (ADR 0003 sigue en estado Propuesto).
- Columnas ID y C4 en docs/aspectos/aspectos.md para completar las ocho del contrato.
- Paso del scanner de SonarCloud en el workflow y URL pública del análisis con su Quality Gate.
- Puntos 1 y 2 de correcciones.md: ADR/diagnóstico de la restricción del corte 1 y definición del mecanismo de cierre, aún sin resolver en el repositorio.
- Implementación del plan de corrección V1 (tabla y servicio propios de calificaciones).

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Diff contra el hash de la revisión definitiva de S5: no se aportó ese hash, no se pudo ejecutar git diff --stat (comando anotado: git -C "$DIR" diff --stat <HASH_S5>..c389364 -- docs/c4 docs/arc42 docs/adr).
- URL pública del análisis en SonarCloud y estado del Quality Gate: no aparece en la evidencia; el README solo trae un badge.
- Ejecución del scanner SonarCloud en el run revisado: el workflow solo ejecuta pytest.
- Pertenencia de las cuentas de git a la organización ISCOUTB: no verificable con la evidencia entregada.

## Hallazgos para la planilla

- El C4 nivel 3 no existe en el árbol aunque el ADR 0003 propone cambiar el límite de Calificaciones.
- La tabla de aspectos cubre 6 de las 8 columnas del contrato y solo 2 filas.
- El workflow de CI no invoca ningún scanner: no hay evidencia auditable de SonarCloud ni Quality Gate.
- Después del cierre se borró docs/adr/ShareU_Trazabilidad.pdf, que docs/evidencia/evidencia.md decía conservar.
- El historial muestra cinco cuentas de git y hay cuatro integrantes declarados, sin evidencia para mapearlas.
- docs/aspectos.md y docs/ia.md están en subcarpetas: desviación de ruta registrada.
- Los planes de corrección de la auditoría quedan documentados pero sin implementar.
- Commits posteriores al cierre (no calificados): 0bae184 2026-09-14T15:26:52-05:00 Delete docs/adr/ShareU_Trazabilidad.pdf
