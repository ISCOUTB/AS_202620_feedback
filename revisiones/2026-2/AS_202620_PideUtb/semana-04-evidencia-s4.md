# semana-04-evidencia-s4 · PideUtb

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `b5f0310` (2026-08-23T19:42:42-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | No se pudo acceder al contenido de arc42.md; el árbol solo muestra arc42.md en la raíz, sin docs/arc42/. | No verificado | Haría falta el contenido del archivo para comprobar secciones 1-6 y ausencia de plantilla. |
| arc42 sección 9 al día y enlazada con los ADR existentes | Sin contenido de arc42.md; existe docs/adr/0001-estilo-arquitectonico.md. | No verificado | No se puede verificar enlace desde sección 9. |
| arc42 sección 10 coherente con los escenarios de la semana 2 | Sin contenido de arc42.md; docs/aspectos.md menciona escenarios pero no sección 10. | No verificado | Falta evidencia de coherencia. |
| Glosario iniciado con términos del dominio | Sin contenido de arc42.md; no se localiza sección 12. | No verificado | No se puede comprobar glosario. |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | El árbol no incluye docs/c4/ ni archivos de diagramas C4. | No cumple | No hay diagramas C4. |
| Límites del C4 nivel 2 correspondientes a la estructura del código | Sin C4 nivel 2; estructura de código solo tiene paquetes vacíos. | No cumple | No aplica correspondencia. |
| Corte vertical que atraviesa interfaz, lógica y persistencia | README.md indica 'No incluye lógica de negocio'; módulos __init__.py vacíos; solo main.py con health. | No cumple | No hay recorrido interfaz-lógica-persistencia. |
| Arranque documentado con un solo comando | README.md declara Python 3.11+ y comando único: python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload | Cumple | Cumple requisitos previos y un comando. |
| Prueba automatizada del recorrido completo, en verde | Solo existe backend/tests/test_health.py; no hay prueba del recorrido completo ni evidencia de CI. | No cumple | Falta prueba de punta a punta y run verde. |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md es narrativo, sin tabla con columnas ID, Aspecto, Requisito, C4, ADR, Código, Pruebas, Evidencia. | No cumple | No hay fila con celdas navegables. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Autores consolidados: daniarriet y Santiago Cuesta (mismo correo sjcm082005@gmail.com); falta Ruddy Rodriguez Romero. | No cumple | No todos los integrantes aparecen en historial. |
| Estructura mínima | Faltan docs/arc42/ y docs/c4/; arc42.md está en raíz. | No cumple | Desviación de estructura. |
| Estado del repositorio calificado | Commit b5f0310 sin etiqueta corte-1; fecha 2026-08-23 antes del cierre. | No cumple | Etiqueta ausente. |
| Convenciones de ADR | ADR 0001 título 'Estilo arquitectónico del backend de PideUTB' no enuncia decisión; falta trazabilidad con commit/PR. | No cumple | No sigue convención completa. |
| Tabla de aspectos | docs/aspectos.md sin tabla de 8 columnas. | No cumple | Formato incorrecto. |
| Registro de uso de IA | docs/ia.md no menciona herramienta específica ni qué se rechazó y por qué. | No cumple | Falta columna de rechazo. |
| README | README.md con requisitos y comando único. | Cumple | Cumple. |
| Pipeline y análisis estático | No hay .github/workflows/ ni evidencia de CI/SonarCloud. | No cumple | Sin pipeline. |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 secciones 1-6: sin contenido de arc42.md
- arc42 sección 9: sin contenido de arc42.md
- arc42 sección 10: sin contenido de arc42.md
- Glosario: sin contenido de arc42.md

## Hallazgos para la planilla

- Falta documentación arc42 completa
- No hay diagramas C4
- No hay corte vertical
- Falta prueba de recorrido completo
- Tabla de aspectos no cumple formato
- Integrante Ruddy sin commits
- Estructura desviada
- ADR sin trazabilidad
- IA sin rechazos
- Sin pipeline
