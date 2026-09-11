# semana-06-evidencia-s6 · InvenTrack

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_InvenTrack` |
| Estado revisado | `ac951e3` en `origin/main` (2026-09-08T10:11:58-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | Árbol de ac951e3 no contiene archivo de mapa de contextos; docs/c4/containers.md solo describe contenedores técnicos (Frontend, API, BD) | No cumple | No se nombran contextos del dominio ni relaciones tipo núcleo compartido, cliente-proveedor o capa anticorrupción |
| Tabla módulo a datos con dueño único por entidad | No hay tabla módulo a datos en el repositorio al hash ac951e3 | No cumple | No se identificó dueño único por entidad |
| La tabla cubre las entidades que existen en el código | Sin tabla; entidades reales como app/productos/domain/producto.py y app/inventario/domain/stock.py no están inventariadas | No cumple | No hay cobertura contrastable con el esquema real |
| Violaciones de propiedad de datos detectadas sobre el código actual | No hay lista de violaciones; app/productos/infrastructure/in_memory_verificador_movimientos.py sugiere acceso de productos a movimientos de inventario sin documentar | No cumple | No se documentó el recorrido de verificación |
| Plan de corrección por violación | No existe plan de corrección asociado a violaciones en el repositorio | No cumple | Sin violaciones listadas no hay plan |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | README describe sección 8 como 'Mecanismo de exclusión mutua asíncrona por SKU y manejo unificado de excepciones'; no menciona lenguaje ubicuo ni mapa de contextos | No cumple | docs/arc42/arc42-template-EN.md no evidencia esos contenidos en la sección 8 |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4/containers.md declara el Nivel 3 (Componentes) como pendiente; no hay ADR de reajuste (solo 0001 y 0002) | No cumple | No se pudo contrastar con S5 por falta del hash en la evidencia; el C4 nivel 3 no existe |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md tiene ASP-01 y ASP-02, pero no hay mapa de contextos con el cual contrastar | No cumple | Sin mapa no se puede establecer correspondencia |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_InvenTrack en ISCOUTB, público y visible; autores consolidados: Jose Vargas, Esteban Peluffo, Felix Taborda, Javier Carta | Cumple | Los 4 integrantes declarados aparecen en el historial |
| Estructura mínima | Árbol de ac951e3 incluye docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md | Cumple | ADR con nombres en convención 0001-* y 0002-* |
| Qué estado del repositorio se califica | origin/main, hash ac951e3 (2026-09-08T10:11:58-05:00) anterior al cierre 2026-09-14T05:00:00Z; sin commits posteriores | Cumple | Entrega en modo early, sin diff posterior |
| Convenciones de ADR | docs/adr/0001-usar-monolito-modular-con-hexagonal-por-modulo.md y 0002-control-concurrencia-memoria-inventario.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | No se detectaron ADR reescritos tras su creación |
| La tabla de aspectos | docs/aspectos.md con tabla de 8 columnas (ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia) para ASP-01 y ASP-02 | Cumple | Celdas con enlaces navegables a los artefactos |
| Registro de uso de IA | docs/ia.md con tabla de usos, herramienta, aceptado y rechazado/motivo; 11 commits del archivo entre 2026-08-09 y 2026-09-06 | Cumple | Columna de rechazos con motivo técnico presente |
| README | README.md describe el sistema, comando de arranque (python -m uvicorn app.main:app --reload) y prueba (pytest) | Cumple | Incluye stack, estructura y enlaces a documentación |
| Pipeline y análisis estático | .github/workflows/test.yml solo ejecuta pytest; runs_ci muestran únicamente 'Run Tests' en success, sin runs de SonarCloud | No cumple | Hay sonar-project.properties pero no evidencia de ejecución de SonarCloud (organización isco-utb) en CI |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `ac951e3fc2acf849f2cc89ffb622d392b268672a 2026-09-08T10:11:58-05:00 Update and rename feedback.md to correcciones.md`
- **Veredicto**: con pendientes
- Resumen: El repositorio mantiene una base documental sólida (ADR, aspectos, IA, README, CI en verde), pero la entrega de la semana 6 no contiene ninguno de los artefactos pedidos y arrastra pendientes como el C4 nivel 3.

Pendientes que siguen abiertos:
- Mapa de contextos del dominio con relaciones tipificadas
- Tabla módulo a datos con dueño único por entidad
- Lista de violaciones de propiedad de datos con plan de corrección
- Lenguaje ubicuo y mapa de contextos en arc42 sección 8
- C4 nivel 3
- Evidencia de ejecución de SonarCloud en CI

## Recuento y nota sugerida

0 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 1.0 = 1 + 4 × (0/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Ejecución de SonarCloud: no hay runs de análisis estático; se necesitaría el run de SonarCloud o configuración que lo ejecute.
- Comparación con S5 para detectar cambio de límites: falta el hash de la revisión definitiva de S5 en la evidencia.

## Hallazgos para la planilla

- El commit de la semana 6 (ac951e3) solo renombra feedback.md a correcciones.md; no incorpora artefactos de la semana.
- No existe mapa de contextos del dominio en el repositorio.
- No hay tabla módulo a datos con dueño único por entidad.
- No hay lista de violaciones de propiedad de datos sobre el código actual.
- La sección 8 de arc42 no incluye lenguaje ubicuo ni mapa de contextos.
- El C4 nivel 3 está declarado como pendiente en docs/c4/containers.md.
- Posible violación no documentada: app/productos/infrastructure/in_memory_verificador_movimientos.py sugiere acceso de productos a movimientos de inventario.
- No hay evidencia de ejecución de SonarCloud en CI; solo runs de pytest.
