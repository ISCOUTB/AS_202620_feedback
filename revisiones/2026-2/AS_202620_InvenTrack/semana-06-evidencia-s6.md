# semana-06-evidencia-s6 · InvenTrack

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `d6f2b19` en `origin/main` (2026-09-13T23:37:36-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/context-map.md (d6f2b19): contextos productos, inventario, usuarios, proveedores, alertas; relaciones cliente-proveedor, capa anticorrupción, núcleo compartido. | Cumple | Usa vocabulario de la semana; no es un diagrama de módulos técnicos. |
| Tabla módulo a datos con dueño único por entidad | docs/propiedad-datos.md (d6f2b19): Producto→app/productos, StockProducto→app/inventario, Movimiento→app/inventario, Usuario/Rol→app/usuarios, AlertaStock→app/alertas. | Cumple | Cada entidad tiene un solo dueño; incluye lectores y canales de consulta. |
| La tabla cubre las entidades que existen en el código | docs/propiedad-datos.md (d6f2b19) vs app/productos/domain/producto.py, app/inventario/domain/stock.py, app/inventario/domain/movimiento.py. | Cumple | Entidades reales cubiertas; módulos vacíos declarados como pendientes. |
| Violaciones de propiedad de datos detectadas sobre el código actual | docs/auditoria-modularidad.md (d6f2b19): VIO-01 en app/productos/infrastructure/in_memory_verificador_movimientos.py; VIO-02 en app/usuarios. | Cumple | VIO-01 resuelta con ADR-0003; VIO-02 pendiente por diseño. |
| Plan de corrección por violación | docs/auditoria-modularidad.md (d6f2b19): plan VIO-01 con puertos de aplicación y adaptadores; VIO-02 diferido. | Cumple | Cada violación tiene acción concreta. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42-template-EN.md (d6f2b19); README.md describe sección 8 solo como exclusión mutua. | No verificado | No se pudo confirmar que la sección 8 incluya lenguaje ubicuo y mapa de contextos; el registro de IA lo afirma pero el README no lo refleja. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/components.md (d6f2b19) y docs/adr/0003-integracion-productos-inventario-via-puertos-de-aplicacion.md (d6f2b19). | Cumple | ADR-0003 documenta el reajuste de límites; C4 Nivel 3 actualizado con adaptadores cruzados. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md (d6f2b19): ASP-01 y ASP-02 enlazan al mapa de contextos y a módulos productos/inventario. | Cumple | Contextos vacíos (usuarios, proveedores, alertas) sin aspectos, consistente con su estado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_InvenTrack en ISCOUTB, público; autores consolidados: Jose Vargas, Felix Taborda, Esteban Peluffo, Javier Carta (d6f2b19). | Cumple | 4 integrantes con commits en el historial. |
| Estructura mínima | docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md, README.md presentes (d6f2b19). | Cumple | Estructura completa según contrato. |
| Estado del repositorio calificado | origin/main, hash d6f2b19, fecha 2026-09-13T23:37:36-05:00, anterior al cierre 2026-09-14T05:00:00Z. | Cumple | Commit vigente al cierre. |
| Convenciones de ADR | docs/adr/0001, 0002, 0003 con nombres kebab-case y contenido (contexto, alternativas, decisión, consecuencias, trazabilidad) (d6f2b19). | Cumple | Cumplen la convención. |
| Tabla de aspectos | docs/aspectos.md (d6f2b19): ASP-01 y ASP-02 con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia. | Cumple | Celdas enlazan a artefactos. |
| Registro de uso de IA | docs/ia.md (d6f2b19): tabla con usos, aceptado/rechazado y motivos; log con 12 commits. | Cumple | Incluye columna de rechazos con criterio técnico. |
| README | README.md (d6f2b19): descripción, arranque con python -m uvicorn app.main:app --reload, pruebas con pytest. | Cumple | Documenta cómo arrancar y probar. |
| Pipeline y análisis estático | .github/workflows/test.yml existe (d6f2b19), pero no hay runs_ci citados. | No verificado | No se pudo confirmar ejecución de CI; el registro de IA menciona retiro temporal de SonarCloud. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `d6f2b1905909f89eae41f36e1963a0fc688618e7 2026-09-13T23:37:36-05:00 fix: update aspectos, ia and readme`
- **Veredicto**: al dia
- Resumen: Proyecto en buen estado; entrega S6 cumple 7/8 criterios de la ficha y 7/8 transversales, con dos aspectos no verificados.

Pendientes que siguen abiertos:
- Verificar sección 8 de arc42 (lenguaje ubicuo y mapa de contextos)
- Evidenciar ejecución del pipeline CI

## Recuento y nota sugerida

7 de 8 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 4.5 = 1 + 4 × (7/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 8 con lenguaje ubicuo y mapa de contextos (docs/arc42/arc42-template-EN.md)
- Pipeline y análisis estático (.github/workflows/test.yml)

## Hallazgos para la planilla

- Sección 8 de arc42 no verificada: README la describe solo como exclusión mutua, sin lenguaje ubicuo.
- Pipeline CI sin evidencia de ejecución; workflow existe pero no hay runs citados.
- Registro de IA indica retiro temporal de SonarCloud del workflow.
- Módulos usuarios, proveedores y alertas declarados en el mapa pero sin código.
