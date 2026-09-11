# semana-05-corte1 · ShareU

> Revision automatica definitiva (GitHub Actions, posterior al cierre).

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_ShareU` |
| Estado revisado | `19ce719` en `origin/master` (2026-09-07T22:41:14-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/master 19ce719 2026-09-07T22:41:14-05:00, anterior al cierre 2026-09-10T17:00:00Z | Cumple | Hash y fecha verificados en el estado calificado. |
| correcciones.md existe en la raíz del estado calificado | Árbol del hash 19ce719 contiene 'Correcciones.md' con C mayúscula | No cumple | El nombre no es exactamente 'correcciones.md' como exige la ficha. |
| Correcciones trazables y contrastadas | Contenido de Correcciones.md no disponible en la evidencia proporcionada | No verificado | Se requiere el contenido del archivo para contrastar cada hallazgo S1-S4. |
| S1 al día: equipo, problema y repositorio | README.md describe el problema; shortlog con 4 autores; repo ISCOUTB/AS_202620_ShareU visible | Cumple | Equipo, problema y repositorio presentes y coherentes. |
| S2 al día: escenarios de calidad y restricciones | docs/aspectos/aspectos.md contiene escenario de usabilidad completo y restricción de ≤3 interacciones | Cumple | Escenario con fuente, estímulo, artefacto, entorno, respuesta y medida. |
| S3 al día: estrategia de solución y decisiones | docs/adr/0001 y 0002 documentan decisión, alternativas y consecuencias; docs/arc42/arc42.md sección 4 | Cumple | Estrategia de monolito modular y decisión de búsqueda en una solicitud. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42.md con secciones 1-12; docs/c4/nivel1.mmd, nivel2.mmd, nivel-2.md; app/busqueda y app/documentos implementan el corte | Cumple | Documentación y código del corte vertical presentes. |
| Corte vertical reproducible y coherente con la arquitectura | README documenta arranque y pruebas, pero run de CI 'Tests' 34184368396 (asociado al hash) concluye failure | No cumple | La reproducibilidad no está respaldada por un pipeline en verde. |
| Pipeline y pruebas respaldan el estado calificado | Run 'Tests' 34184368396 failure (https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/34184368396); runs recientes también failure | No cumple | El único run success (34180022977) es anterior al hash calificado. |
| Trazabilidad consolidada navegable | docs/aspectos/aspectos.md tabla con celdas de texto sin enlaces (ADR 0002, app/frontend/, test_busqueda_combina_filtros no son navegables) | No cumple | La cadena aspecto-requisito-C4-ADR-código-prueba-evidencia tiene huecos. |
| PDF u otro adjunto exigido por el aula | No hay adjunto disponible en el repositorio; depende de Moodle | No verificado | Se requiere acceso al aula para verificar. |
| Sustentación del corte | Sesión de sustentación no evaluable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | ISCOUTB/AS_202620_ShareU visible; shortlog con 4 autores que coinciden en número con los integrantes declarados | Cumple | Nombre y organización correctos. |
| Estructura mínima | README.md, docs/arc42, docs/adr, docs/c4, docs/aspectos, docs/ia presentes en el árbol | Cumple | Desviación: docs/aspectos/aspectos.md y docs/ia/ia.md en subcarpetas; PDFs en docs/adr. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md y 0002-usabilidad-busqueda-en-una-solicitud.md siguen nomenclatura y contenido | Cumple | PDFs ShareU_Trazabilida.pdf y ShareU_Trazabilidad.pdf no siguen la convención. |
| Registro de uso de IA | docs/ia/ia.md con tabla de usos, herramienta, aceptado y rechazado con motivo | Cumple | Ruta distinta a docs/ia.md pero artefacto presente. |
| README | README.md explica qué es, arranque con uvicorn y pruebas con pytest | Cumple | Requisitos previos declarados. |
| Pipeline y análisis estático | .github/workflows/tests.yml existe pero run 'Tests' 34184368396 del hash calificado falla; sin evidencia de SonarCloud en el repo | No cumple | El pipeline no respalda el estado calificado. |
| Secretos | git grep sin coincidencias de credenciales; sin .env versionado | Cumple | Sin incidentes de secretos. |
| Autoría y colaboración | shortlog: Dayana 13, luiscorredor 8, Nicolas-HH 7, steven 2 | Cumple | Cuatro identidades con contribuciones repartidas. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `19ce7197b4bc53c0a685f4722e0f3ae5538750be 2026-09-07T22:41:14-05:00 Update Correcciones.md`
- **Veredicto**: con pendientes
- Resumen: El proyecto a HEAD (19ce719) es el mismo del corte; sin commits posteriores al cierre. La base arquitectónica S1-S4 está completa, pero el pipeline falla y correcciones.md no cumple el nombre exacto.

Pendientes que siguen abiertos:
- Correcciones.md debe llamarse exactamente correcciones.md.
- Pipeline de CI debe pasar en el hash calificado.
- Trazabilidad de aspectos debe ser navegable.
- PDFs fuera de docs/adr.
- Evidencia de SonarCloud pendiente.

## Recuento y nota sugerida

5 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 2.7 = 1 + 4 × (5/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Contenido de Correcciones.md para contrastar correcciones S1-S4.
- PDF adjunto entregado en Moodle.
- Sustentación del corte.

## Hallazgos para la planilla

- Correcciones.md con mayúscula no cumple el nombre exacto exigido.
- El run de CI del hash calificado (34184368396) falla.
- La tabla de aspectos tiene celdas sin enlaces navegables.
- docs/adr contiene PDFs que no siguen la convención de ADR.
- docs/aspectos y docs/ia están en subcarpetas, desviación de estructura.
- Sin evidencia de análisis estático SonarCloud en el repositorio.
