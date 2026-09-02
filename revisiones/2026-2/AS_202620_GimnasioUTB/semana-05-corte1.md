# semana-05-corte1 · GimnasioUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `38f0031` (2026-09-01T12:07:42-05:00) |
| Cierre | 2026-09-07T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Etiqueta `corte-1` sobre un commit anterior al cierre | Sin tag `corte-1` en la lista; HEAD 38f0031 (2026-09-01T12:07:42-05:00) anterior al cierre 2026-09-07T05:00:00Z | No cumple | Etiqueta ausente; se revisa el último commit anterior al cierre. |
| PDF de dos páginas con diagnóstico, decisión, cambio, medición y trazabilidad | Adjunto en Moodle, no accesible desde el repositorio | No verificado | Requiere revisar la entrega en la plataforma. |
| Impacto de la restricción localizado en requisitos, C4 y código | No hay diagnóstico de restricción nueva en el repo; docs/adr/0001-arquitectura-hexagonal.md es de la semana 4 | No cumple | No se informó la restricción asignada y no hay rastro de su análisis. |
| Línea base medida y verificable antes del cambio | No hay cifra con herramienta y procedimiento en el repositorio | No cumple | Falta la medición inicial del escenario afectado. |
| ADR del reto con alternativas, fuerzas, decisión y consecuencias | Solo existe docs/adr/0001-arquitectura-hexagonal.md; no hay ADR nuevo del reto | No cumple | El ADR 0001 no está ligado a una restricción nueva. |
| Cambio implementado y ejecutable de extremo a extremo | No hay commit que implemente un ADR del reto; el corte vertical existente no es el cambio pedido | No cumple | README documenta arranque, pero no hay cambio del reto. |
| Límites declarados conservados tras el cambio | No hay cambio del reto que evaluar; C4 nivel 2 declara PostgreSQL y el código usa memoria (discrepancia de línea base) | No verificado | Sin cambio no se puede comprobar conservación de límites. |
| Prueba que cubre el cambio, en verde en el pipeline | Runs CI success (33535934343, 2026-09-01T17:07:45Z) cubren el corte vertical, no un cambio del reto | No cumple | No hay prueba asociada al reto. |
| Resultado contrastado con el umbral del escenario y reproducible | No hay medición con herramienta, carga y procedimiento en el repo | No cumple | Falta el contraste contra umbral. |
| Cadena aspecto, requisito, C4, ADR, código, pruebas y evidencia navegable | docs/aspectos.md fila S1 enlaza ADR-0001, código y pruebas, pero no incluye C4 ni evidencia de calidad | No cumple | Cadena incompleta y sin fila del reto. |
| Salida de IA aceptada, corregida o rechazada con motivo técnico | docs/ia.md última entrada 2026-08-30 (semana 4); sin registro del corte 1 | No cumple | Falta el uso de IA de este corte. |
| Sustentación del reto | Sesión de sustentación en el aula | No verificado | Lo resuelve el docente en la sesión. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad y estructura | Repo AS_202620_GimnasioUTB en ISCOUTB visible; árbol con docs/arc42, docs/adr, docs/c4, docs/aspectos.md, docs/ia.md, README.md | Cumple | Integrantes declarados aparecen en el historial (PedroPambi, RodrigoFacioLince, sebastian-caicedo). |
| Versionado | Sin etiqueta corte-1; HEAD 38f0031 | No cumple | Etiqueta ausente; se revisa el último commit anterior al cierre. |
| Convenciones de ADR | docs/adr/0001-arquitectura-hexagonal.md con contexto, alternativas, decisión, consecuencias y trazabilidad | Cumple | Solo existe un ADR; no hay reescrituras detectadas. |
| Tabla de aspectos | docs/aspectos.md con fila S1 que enlaza ADR-0001, código y pruebas, pero sin columnas Requisito/C4/Evidencia | No cumple | Formato no coincide con las 8 columnas del contrato. |
| Registro de uso de IA | docs/ia.md con entradas de semanas 2-4, incluye aceptado/rechazado con motivos | Cumple | Sin entradas del corte 1; se refleja en la ficha. |
| README | README.md documenta arranque (npm install && npm start) y pruebas (npm test) | Cumple | Comando reproducible. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta npm test; runs CI success (33535934343) sin SonarCloud | No cumple | Falta el análisis estático exigido por el contrato. |
| Secretos y autoría | Grep sin secretos, sin .env versionado; shortlog muestra contribuciones de los tres integrantes | Cumple | sebastian-caicedo y Sebastian Felipe Caicedo Acosta se consolidan como una persona. |

## Estado global del proyecto (overall · revisado en HEAD)

Mira el repositorio **entero en su estado actual** (HEAD), no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **HEAD revisado**: `38f00318edff1334fe5092eba6bff30658fc4e97 2026-09-01T12:07:42-05:00 Actualización del README`
- **Veredicto**: con pendientes
- Resumen: El proyecto entero a HEAD (38f0031) conserva la línea base de S1-S4, pero la entrega del reto del corte 1 no está implementada: sin etiqueta, sin ADR nuevo, sin diagnóstico, sin cambio, sin medición.

Pendientes que siguen abiertos:
- Etiqueta corte-1
- ADR del reto
- Diagnóstico con línea base
- Implementación del cambio
- Prueba y medición
- Registro de IA del corte
- Tabla de aspectos completa

## Recuento y nota sugerida

0 de 12 criterios Cumple.

## No verificado / pendientes

- PDF de dos páginas: adjunto en Moodle, no accesible desde el repositorio.
- Límites conservados tras el cambio: no hay cambio del reto que evaluar.
- Sustentación del reto: se resuelve en sesión.
- Restricción asignada al equipo: no fue proporcionada; impide juzgar el diagnóstico.

## Hallazgos para la planilla

- No existe la etiqueta corte-1; HEAD 38f0031 es anterior al cierre.
- No hay ADR nuevo para la restricción del reto; solo el 0001 de la semana 4.
- No hay diagnóstico, línea base ni medición del reto en el repositorio.
- docs/ia.md no registra usos de IA del corte 1.
- docs/aspectos.md no tiene las 8 columnas del contrato ni enlace a C4/evidencia.
- El pipeline no incluye SonarCloud.
