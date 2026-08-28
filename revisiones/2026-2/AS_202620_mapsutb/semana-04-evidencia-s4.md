# semana-04-evidencia-s4 · mapsutb

> Pasada temprana (GitHub Actions, previa al cierre): los hashes son provisionales y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `75ca174` (2026-08-28T10:17:59-05:00) |
| Cierre | 2026-08-31T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| arc42 secciones 1 a 6 redactadas, sin texto de plantilla | docs/Arc42/ solo contiene Estrategias_Solucion.md (sección 4), Objetivos de Calidad y Stakeholders.md (secciones 1-2) y restricciones.md (sección 3); faltan secciones 5 y 6 | No cumple | No hay archivos para las secciones 5 y 6 de arc42 |
| arc42 sección 9 al día y enlazada con los ADR existentes | No existe archivo de sección 9 en docs/Arc42/; ADR 0001 existe pero no hay sección 9 que lo cite | No cumple | Falta la sección 9 de decisiones |
| arc42 sección 10 coherente con los escenarios de la semana 2 | No existe archivo de sección 10 en docs/Arc42/ | No cumple | Falta la sección 10 de requisitos de calidad |
| Glosario iniciado con términos del dominio | No existe sección 12 ni archivo de glosario en docs/Arc42/ | No cumple | Falta glosario con términos propios del sistema |
| C4 nivel 1 y nivel 2 presentes y coherentes entre sí | docs/C4/C1.md y C2.md existen, pero los actores externos del nivel 1 (aspirante, intercambio, comunidad) no reaparecen en el nivel 2; se fusionan en un único 'usuario' | No cumple | Incoherencia de actores entre niveles; las flechas sí están etiquetadas |
| Límites del C4 nivel 2 correspondientes a la estructura del código | C2 dibuja contenedores 'Activos del mapa' y 'Datos de zonas y puntos de interés', pero el árbol del repositorio no tiene directorios assets/ ni datos/; solo lib/ con carpetas vacías | No cumple | Dos contenedores del diagrama no tienen código correspondiente |
| Corte vertical que atraviesa interfaz, lógica y persistencia | lib/main.dart existe, pero lib/features, repositories, services, strategies están vacíos (.gitkeep); no hay lógica ni persistencia implementadas | No cumple | No hay recorrido completo; solo esqueleto |
| Arranque documentado con un solo comando | README.md incluye requisitos previos y comando único ./scripts/start.sh; scripts/start.sh existe en el árbol | Cumple | Documentación de arranque correcta |
| Prueba automatizada del recorrido completo, en verde | test/app_smoke_test.dart es solo smoke test, no ejercita corte vertical; no se proporciona URL de run de CI | No cumple | Falta prueba de recorrido completo y evidencia de ejecución en verde |
| Fila de docs/aspectos.md completa hasta la columna Pruebas | docs/aspectos.md fila A-01 tiene C4 'Por definir', ADR 'Sin ADR aún', Código 'Aún no iniciado', Pruebas 'Aún no iniciado', Evidencia 'Aún no iniciado' | No cumple | La fila no está completa; celdas sin destino navegable |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | git shortlog muestra 3 autores: CarlosManrique-1397, charlygz21, nerlis-otero; declarados 4 integrantes, falta Isabel Sofia Paez Matallana | No cumple | Un integrante no aparece en el historial |
| Estructura mínima | Árbol incluye docs/Arc42/, docs/adr/0001-patrones-de-diseno.md, docs/C4/, docs/aspectos.md, docs/ia.md, README.md | Cumple | Cumple aunque con mayúsculas en Arc42 y C4 (desviación menor) |
| Estado del repositorio calificado | Hash 75ca174, fecha 2026-08-28T10:17:59-05:00, anterior al cierre 2026-08-31T05:00:00Z | Cumple | Commit correcto para la semana 4 |
| Convenciones de ADR | docs/adr/0001-patrones-de-diseno.md existe y nombre sigue patrón; no se pudo verificar historial de ediciones post-aceptación | No verificado | Falta ejecutar git log --follow sobre el ADR para confirmar que no fue reescrito |
| Tabla de aspectos | docs/aspectos.md existe con encabezado de 8 columnas y una fila A-01 | Cumple | Estructura correcta; completitud evaluada en ficha |
| Registro de uso de IA | docs/ia.md tiene tabla con columnas Fecha, Etapa, Herramienta, Uso, Resultado, Aceptado/Rechazado, Motivo; tres entradas con motivos | Cumple | Incluye rechazos con justificación técnica |
| README | README.md describe qué es, requisitos previos, arranque con un solo comando y cómo probar | Cumple | Documentación de reproducibilidad adecuada |
| Pipeline y análisis estático | No existe .github/workflows/ en el árbol; no se proporcionan runs de CI | No cumple | Falta integración continua y análisis estático |

## Recuento y nota sugerida

1 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 1.4 = 1 + 4 × (1/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Historial de ediciones del ADR 0001: falta git log --follow para confirmar que no fue modificado tras aceptarse

## Hallazgos para la planilla

- Faltan secciones 5, 6, 9, 10 y 12 de arc42
- C4 nivel 2 no conserva los actores del nivel 1
- Contenedores de C4 sin código correspondiente
- No hay corte vertical implementado
- Fila de aspectos incompleta con celdas placeholder
- Un integrante declarado no aparece en el historial
- No hay pipeline de CI ni análisis estático
