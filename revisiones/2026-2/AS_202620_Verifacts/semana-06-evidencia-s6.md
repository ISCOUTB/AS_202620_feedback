# semana-06-evidencia-s6 · Verifacts

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Estado revisado | `67f8cea` en `origin/master` (2026-09-09T16:30:01-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/mapa-contextos.md (hash 67f8cea, 2026-09-09): diagrama mermaid con 3 contextos y relaciones Customer/Supplier, Published Language, Conformist | Cumple | Usa patrones DDD; no menciona explícitamente 'núcleo compartido' ni 'capa anticorrupción' |
| Tabla módulo a datos con dueño único por entidad | docs/propiedad-datos.md (hash 67f8cea): tabla con dueño único para tabla analyses | Cumple | Dueño único: Historial de Análisis; lectura por Ingesta |
| La tabla cubre las entidades que existen en el código | app/persistence/repository.py (hash 67f8cea) define CREATE TABLE analyses; docs/propiedad-datos.md la cubre | Cumple | Coincide con el esquema real sqlite3 |
| Violaciones de propiedad de datos detectadas sobre el código actual | docs/propiedad-datos.md (hash 67f8cea) documenta verificación: solo repository.py abre conexión; no se encontraron violaciones | Cumple | Recorrido de verificación documentado (pasos 1-3) |
| Plan de corrección por violación | docs/violaciones-modularidad.md (hash 67f8cea) y docs/propiedad-datos.md: lista vacía con verificación documentada | Cumple | No hay violaciones declaradas; la ficha permite lista vacía si el recorrido está documentado |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/08-conceptos transversales.md (hash 67f8cea): subsección S6 con lenguaje ubicuo y referencia a mapa-contextos.md | Cumple | Incluye tabla de términos y regla transversal de propiedad de datos |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/03-componentes.md (hash 67f8cea) actualizado con contextos; no se encontró ADR de reajuste | No verificado | Falta hash de S5 para comparar; si los límites cambiaron, falta ADR del reajuste |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md (hash 67f8cea) no referencia los contextos del mapa; filas A-00 a A-04 usan C4 Nivel 2 | No cumple | La relación solo es indirecta vía C4 Nivel 3; no hay columna de contexto en aspectos.md |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | README.md (hash 67f8cea) lista 2 integrantes; autores en git: PedroC1213 y Cristian Cardeño; Julian Samuel Cabeza Pena no aparece en historial | No cumple | Integrante declarado sin commits |
| Estructura mínima | Árbol del repo (hash 67f8cea): docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Rutas y archivos mínimos presentes |
| Qué estado del repositorio se califica | Hash calificado 67f8cea (2026-09-09T16:30:01-05:00) anterior al cierre 2026-09-14T05:00:00Z; commits_tardios_post_cierre vacío | Cumple | Modo early, sin commits posteriores al cierre |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md (hash 67f8cea) sigue nomenclatura NNNN-titulo-kebab-case; título enuncia decisión | Cumple | Un solo ADR, aceptado |
| La tabla de aspectos | docs/aspectos.md (hash 67f8cea): fila A-02 tiene 'Pendiente' en evidencia de pruebas | No cumple | Fila con hueco no defendible según contrato |
| Registro de uso de IA | docs/ia.md (hash 67f8cea): bitácora con fechas, herramientas, propósito, aceptado/rechazado | Cumple | Incluye rechazo de LLM como clasificador con motivo |
| README | README.md (hash 67f8cea): describe qué es, arranque con python run.py y npm run dev, pruebas con pytest | Cumple | Comandos de arranque y prueba documentados |
| Pipeline y análisis estático | .github/workflows/tests.yml existe (hash 67f8cea); sin runs_ci en la evidencia | No verificado | Falta enlace a run de GitHub Actions o SonarCloud; comando: curl a actions/runs |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `67f8cea03e6a7b827aced6b60d3af8cf4307b237 2026-09-09T16:30:01-05:00 feat: integrate backend URL analysis contract and align frontend`
- **Veredicto**: con pendientes
- Resumen: Proyecto con avance sólido en S6: mapa de contextos, propiedad de datos y arc42 §8 completos. Persisten pendientes de trazabilidad (aspectos.md sin contexto, A-02 sin evidencia) y de identidad (integrante sin commits).

Pendientes que siguen abiertos:
- Fila A-02 de aspectos.md sin evidencia de prueba
- aspectos.md sin relación explícita con contextos del mapa
- Posible ADR de reajuste de límites si cambiaron
- Integrante declarado sin commits
- Evidencia de runs de CI

## Recuento y nota sugerida

6 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.0 = 1 + 4 × (6/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 3 y ADR si los límites cambiaron: falta hash de S5 para comparar
- Pipeline y análisis estático: falta runs_ci

## Hallazgos para la planilla

- Integrante declarado Julian Samuel Cabeza Pena sin commits en el historial
- Fila A-02 de aspectos.md sin evidencia de prueba (pendiente)
- aspectos.md no referencia los contextos del mapa de contextos
- No hay ADR de reajuste de límites; C4 Nivel 3 actualizado pero sin hash S5 para comparar
- Sin evidencia de runs de CI en la entrega
