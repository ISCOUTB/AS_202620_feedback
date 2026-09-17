# semana-06-evidencia-s6 · ElMapita

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ElMapita` |
| Estado revisado | `a22f0a4` en `origin/main` (2026-09-13T22:21:07-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | a22f0a4 lista docs/c4/C4_L1_Context.md, docs/c4/C4_L2_Container.md, docs/c4/C4_L3_Component_Backend.md, docs/c4/contexto.md y docs/arc42/arc42-template-EN.md (extracto §§1-3, contexto de negocio con actores y Supabase como sistema externo). | No verificado | Falta el contenido de docs/c4/contexto.md; no hay artefacto citable con relaciones núcleo compartido, cliente-proveedor o capa anticorrupción. |
| Tabla módulo a datos con dueño único por entidad | Existe docs/TablaModulos_ElMapitaUTB.docx en a22f0a4 (binario, contenido no incluido en la evidencia). | No verificado | Sin version Markdown ni texto extraido no se puede comprobar el dueño único por entidad. |
| La tabla cubre las entidades que existen en el código | El árbol a22f0a4 no tiene migraciones ni archivos .sql; las entidades viven en backend/src/modules/*/domain/index.ts y frontend/lib/features/*/domain/entities.dart. | No verificado | Falta la tabla legible y un esquema/migraciones contra los que contrastar la cobertura. |
| No conformidades de propiedad de datos detectadas sobre el código actual | Hay adaptadores de escritura en backend/src/modules/mapas/infrastructure/persistence/supabase-repositories.ts y backend/src/modules/pois/infrastructure/supabase-poi-repository.ts; existe correcciones.md en la raíz. | No verificado | Contenido de correcciones.md no aportado; no se pudo correr el grep de escrituras ni revisar la lista. |
| Plan de corrección por no conformidad | No se aporta ninguna lista de no conformidades ni plan asociado en la evidencia recibida. | No verificado | Depende de la fila anterior; hace falta la lista con entidad, dueño esperado, ubicación y acción. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42-template-EN.md existe en a22f0a4, pero el extracto recibido solo cubre las secciones 1 a 3. | No verificado | Falta el contenido de la sección 8 para verificar lenguaje ubicuo y mapa de contextos incorporado. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | Existen docs/c4/C4_L3_Component_Backend.md/.png y docs/adr/0001 y 0002; no se aporta el hash de S5 ni un ADR de reajuste de límites. | No verificado | Sin el hash revisado en S5 no hay diff comparable contra docs/c4, docs/arc42 y docs/adr. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md existe en a22f0a4 (contenido no incluido en la evidencia). | No verificado | Sin el contenido de aspectos.md ni el mapa verificado no se puede emparejar fila por fila. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_ElMapita en ISCOUTB, público y visible, rama principal origin/main; autores en a22f0a4: RobotDRMX, Rodrigo Vazquez Rico y dgarza2705. | Cumple | No se atribuye ninguna cuenta a una persona por parecido de nombre; la pertenencia a la organización no se pudo comprobar desde la evidencia. |
| Estructura mínima | a22f0a4 incluye README.md, docs/arc42/arc42-template-EN.md, docs/adr/0001 y 0002, docs/c4/*.md, docs/aspectos.md y docs/ia.md. | Cumple | Desviaciones: entregables en .docx (docs/TablaModulos_ElMapitaUTB.docx, docs/CorteVertical_ElMapitaUTB.docx) y un temporal de Office docs/~$blaModulos_ElMapitaUTB.docx. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico-propuesto.md y docs/adr/0002-restriccion-rendimiento-compatibilidad-dispositivos.md cumplen el patrón NNNN-kebab-case y traen contexto, alternativas, decisión y consecuencias. | Cumple | No se aportó el log --follow para descartar reescrituras de un ADR ya aceptado. |
| La tabla de aspectos | docs/aspectos.md existe en a22f0a4, pero su contenido no viene en la evidencia. | No verificado | No se pueden comprobar las ocho columnas ni que no haya celdas huecas. |
| Registro de uso de IA | docs/ia.md aparece en seis commits a lo largo del semestre, el último en a22f0a4 (2026-09-13T22:21:07-05:00). | Cumple | Sin el contenido no se pudo verificar la columna de lo rechazado y su motivo. |
| README | README.md describe el sistema, prerequisitos, arranque con un solo comando (scripts/dev.sh o scripts/dev.ps1) y cómo se prueba (npm run test, flutter test). | Cumple | El arranque depende de un .env con credenciales Supabase propias del equipo. |
| Pipeline y análisis estático | Existe .github/workflows/ci.yml en a22f0a4; no hay runs_ci, ni sonar-project.properties, ni URL de análisis citados. | No verificado | Faltan el run exitoso del scanner y la URL pública de SonarCloud con Quality Gate; comprobar con curl a api.github.com/repos/ISCOUTB/AS_202620_ElMapita/actions/runs. |
| Secretos | envs_versionados vacío; las coincidencias del grep son un badge de ejemplo (backend/README.md:5, token=abc123def456) y parámetros password: string en el código de auth. | Cumple | Ninguna credencial real en a22f0a4; no se aportó la búsqueda de claves privadas en el historial. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `a22f0a43f2e93730d9df5d112f03687854639ea7 2026-09-13T22:21:07-05:00 docs(ia): actualizar registro de uso de IA`
- **Veredicto**: con pendientes
- Resumen: La entrega se registra antes del cierre (a22f0a4, 2026-09-13T22:21:07-05:00) sobre origin/main, y el repositorio sostiene estructura, ADR, README, registro de IA y workflow de CI; sin embargo los entregables propios de S6 no son auditables en la evidencia y falta la prueba pública de SonarCloud.

Pendientes que siguen abiertos:
- Mapa de contextos con relaciones tipificadas en formato revisable.
- Tabla módulo a datos con dueño único y su contraste con las entidades del código.
- Lista de no conformidades de propiedad de datos con ubicación y plan de corrección.
- arc42 sección 8 con lenguaje ubicuo y mapa de contextos.
- ADR de reajuste y diff de C4 Nivel 3 si los límites cambiaron desde el primer corte.
- Evidencia de SonarCloud: configuración, run de CI y URL pública con Quality Gate.

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Mapa de contextos con relaciones tipificadas: falta el contenido de docs/c4/contexto.md.
- Tabla módulo a datos y dueño único: solo existe el .docx binario, sin versión revisable.
- Cobertura de entidades: no hay migraciones ni esquema en el árbol a22f0a4.
- Lista de no conformidades de propiedad de datos: contenido de correcciones.md no aportado.
- Plan de corrección por no conformidad: no se aporta lista ni acciones.
- arc42 sección 8 con lenguaje ubicuo y mapa de contextos: el extracto solo cubre §§1-3.
- Comparación C4 Nivel 3 y ADR contra el hash revisado en S5: falta ese hash.
- docs/aspectos.md: contenido y columnas sin aportar.
- Pipeline y SonarCloud: falta el run de CI y la URL pública del análisis con su Quality Gate.

## Hallazgos para la planilla

- Los entregables de S6 sobre mapa de contextos y tabla módulo a datos no son auditables en la evidencia recibida.
- No hay evidencia de SonarCloud: falta configuración, run de CI y URL pública con Quality Gate.
- docs/ contiene un archivo temporal de Office y entregables duplicados en .docx y .md (glosario).
- Existe C4 Nivel 3, pero no se aporta ADR de reajuste ni hash de S5 para comparar límites.
- docs/ia.md se mantiene a lo largo del semestre con seis actualizaciones.
- El pipeline de CI está configurado en el repositorio, pero no se cita ningún run.
- No hay migraciones ni esquema versionado, lo que impide contrastar la tabla contra los datos reales.
