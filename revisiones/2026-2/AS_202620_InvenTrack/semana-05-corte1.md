# semana-05-corte1 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `ac951e3` en `origin/main` (2026-09-08T10:11:58-05:00) |
| Cierre | 2026-09-10T17:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Estado de corte identificable y anterior al cierre | origin/main ac951e3 (2026-09-08T10:11:58-05:00) anterior al cierre 2026-09-10T17:00:00Z | Cumple | Rama principal main; sin commits posteriores al cierre. |
| correcciones.md existe en la raíz del estado calificado | correcciones.md presente en el árbol de ac951e3 (git ls-tree) | Cumple | Archivo en la raíz con nombre exacto. |
| Correcciones trazables y contrastadas | correcciones.md (ac951e3) responde a S1-S4 en prosa, sin tabla hallazgo→acción→ruta/commit/run→estado | No cumple | No cita commits ni runs por corrección; no es un índice de verificación. |
| S1 al día: equipo, problema y repositorio | docs/ficha_problema.md, README.md (equipo), docs/aspectos.md (tabla 8 columnas), shortlog con 4 autores | Cumple | Problema, tensiones, alcance y contribución de los 4 integrantes presentes. |
| S2 al día: escenarios de calidad y restricciones | docs/arc42/arc42-template-EN.md (secciones 1,2,3,10), docs/utility-tree.md (ESC-01 a ESC-05), docs/c4/context.md | Cumple | Restricciones C1-C7 y escenarios medibles documentados. |
| S3 al día: estrategia de solución y decisiones | docs/matriz-comparativa-estilos.md, docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md, app/ con módulos | Cumple | Estrategia comparada y ADR-0001 aceptado con consecuencias. |
| S4 al día: arc42, C4 y corte vertical | docs/arc42/arc42-template-EN.md (secciones 4,5,6,9,12), docs/c4/containers.md, app/productos/, tests/productos/test_api_corte_vertical.py | Cumple | Vistas completas y corte vertical hexagonal implementado. |
| Corte vertical reproducible y coherente con la arquitectura | README.md (arranque y pruebas), requirements.txt, app/productos/ (domain/application/infrastructure), tests/productos/ | Cumple | Corresponde al C4 containers.md y al ADR-0001. |
| Pipeline y pruebas respaldan el estado calificado | Run 'Run Tests' success 2026-09-08T15:12:02Z (https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/34243208383) | Cumple | Run posterior al hash por 1 min y anterior al corte; suite pytest en verde. |
| Trazabilidad consolidada navegable | docs/aspectos.md con cadena Aspecto→Requisito→C4→ADR→Código→Pruebas→Evidencia para ASP-01 y ASP-02 | Cumple | Celdas enlazadas a artefactos reales. |
| PDF u otro adjunto exigido por el aula | No disponible en el repositorio; se entrega en Moodle | No verificado | Requiere revisar el aula. |
| Sustentación del corte | Sesión de sustentación no evaluable desde el repositorio | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Estructura mínima | docs/arc42/, docs/adr/ (0001, 0002), docs/c4/ (context, containers), docs/aspectos.md, docs/ia.md, README.md en ac951e3 | Cumple | Estructura completa en Markdown. |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md y 0002-control-concurrencia-memoria-inventario.md | Cumple | Nombres kebab-case, numerados, con contexto, alternativas, decisión, consecuencias y trazabilidad. |
| Tabla de aspectos | docs/aspectos.md con 8 columnas y 2 filas (ASP-01, ASP-02) enlazadas | Cumple | Cadena navegable completa. |
| Registro de uso de IA | docs/ia.md con tabla de usos, aceptado/rechazado y motivo; 11 commits en su historial | Cumple | Incluye rechazos con justificación técnica. |
| README | README.md con descripción, arranque (python -m uvicorn app.main:app --reload) y pruebas (pytest) | Cumple | Requisitos previos declarados en requirements.txt. |
| Pipeline y análisis estático | .github/workflows/test.yml y runs exitosos; sonar-project.properties presente pero sin run de SonarCloud | No cumple | Falta evidencia de ejecución de SonarCloud (URL o workflow). |
| Secretos | git grep sin coincidencias; sin .env versionados en ac951e3 | Cumple | Sin credenciales en el repositorio público. |
| Autoría y colaboración | shortlog: Jose Vargas 99, Felix Taborda 23, Esteban Peluffo 16, Javier Carta 3 commits | Cumple | Los 4 integrantes contribuyen; distribución desbalanceada. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `ac951e3fc2acf849f2cc89ffb622d392b268672a 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: Proyecto completo en S1-S4 con corte vertical y CI en verde; correcciones.md existe pero no es un índice trazable; falta evidencia de SonarCloud.

Resuelto tarde (corregido despues del cierre, ahora al dia):
- Tabla de aspectos convertida a 8 columnas después del cierre de S2 (correcciones.md, sección Semana 2); verificada en docs/aspectos.md de ac951e3.
- ADR-0001 actualizado a Aceptado después del cierre de S3 (correcciones.md, sección Semana 3); verificado en docs/adr/0001 de ac951e3.
- Corte vertical y mecanismo de consistencia implementados después de S4 (correcciones.md, sección Semana 4); verificados en app/productos, app/inventario y tests de ac951e3.

Pendientes que siguen abiertos:
- correcciones.md sin estructura de índice trazable (criterio 3 de la ficha S5).
- Sin evidencia de ejecución de SonarCloud.
- PDF en Moodle y sustentación pendientes de verificación.

## Recuento y nota sugerida

9 de 12 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.0 = 1 + 4 × (9/12).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- PDF u adjunto en Moodle.
- Sustentación del corte.
- Análisis estático SonarCloud (sin run visible).

## Hallazgos para la planilla

- correcciones.md no sigue la estructura de índice trazable exigida.
- Sin evidencia de ejecución de SonarCloud.
- Contribución muy desbalanceada: un integrante con 3 commits frente a 99 de otro.
- PDF y sustentación no verificables desde el repositorio.
