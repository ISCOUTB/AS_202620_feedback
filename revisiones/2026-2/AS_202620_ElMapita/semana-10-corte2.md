# Segundo corte S10 · avance preliminar · ElMapita

**Preliminar, no es cierre ni calificación final.** Cierre previsto: **2026-10-12T05:00:00Z**.

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_ElMapita](https://github.com/ISCOUTB/AS_202620_ElMapita) |
| Rama remota principal | `main` |
| Base S5 del segundo corte | `b28e0684d4b38267c0a7d48152b0f5558a789b8c` |
| Base S8 | `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4` |
| Estado revisado | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` en `origin/main` (2026-10-04T21:11:20-06:00) |
| S9 congelada | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 |
| Punta actual / S10 preliminar | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 |
| Comprobación | 2026-10-06T21:27:01Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Evolución desde S5 hasta la punta

Base tomada del informe S5 publicado y resuelta por Git, sin etiquetas: `b28e0684d4b38267c0a7d48152b0f5558a789b8c`. En el delta S5→HEAD cambian 87 rutas no PDF (conteo de árboles; no mide mérito). Desde S5 se incorporan contrato API comprobable, despliegue Render y observabilidad, correcciones de inyección/rutas y la porción de ubicación de S9 con sus pruebas, mediciones y ADR sustitutos. Los escenarios fallidos siguen abiertos; la evolución no se confunde con cumplimiento del reto asignado.

## Escenario operativo asignado

No verificado. README, ADR, IA, aspectos y evidencias documentan EC-01..04, pero no contienen la asignación docente del escenario operativo S10. No se toma el plan S9 ni los escenarios genéricos como consigna del segundo corte.

## Matriz de evidencia S10

Se omite la fila de PDF de dos páginas por exclusión docente. Quedan 12 filas observables o pendientes; este recuento no es una fórmula de nota.

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta main identificada, anterior al cierre S10; preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://elmapita-utb-api.onrender.com/health iniciado 2026-10-06T21:27:01Z: HTTP 200 en 19.699114 s, JSON status=ok y checks.supabase=ok. Health disponible; no se ejecutó el flujo de mapa/GPS ni se prueba disponibilidad sostenida. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | EC-01..04 son objetivos generales del producto; no se localizó asignación oficial S10; [docs/aspectos.md:3–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L3-L8). |
| Línea base medida y reproducible | No verificado | Hay mediciones identificadas y reproducibles de EC-01 y offline, pero sin conocer el escenario asignado no se las adopta como línea base del corte; [docs/evidencia/s9-ec01-benchmark.json:1–15](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-ec01-benchmark.json#L1-L15), [docs/evidencia/s9-ec04-offline-dispositivo.txt:1–31](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-ec04-offline-dispositivo.txt#L1-L31). |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | ADR-0005/0006 y ADR-0007 son decisiones justificadas; falta identificar la respuesta al escenario operativo asignado. [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:19–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L19-L33). |
| Respuesta implementada o configurada sobre el MVP | No verificado | Hay validador, corrección de error 500 y arneses, pero el validador no es llamado por el controlador; tampoco se identifica el cambio del reto asignado. [backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts:12–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts#L12-L24), [backend/src/modules/ubicacion/ubicacion.module.ts:15–35](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/ubicacion.module.ts#L15-L35). |
| Resultado contrastado con el umbral | No verificado | Resultados francos: EC-01 sin éxito, EC-02 solo placeholder, EC-04 0/20. Son evidencia útil, no cumplimiento del reto S10 aún desconocido; [docs/ia.md:464–469](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L464-L469). |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No cumple | Health y métricas existen, pero el gate ignora fallo de Sonar y la operación crítica de mapas/offline no satisface escenarios declarados; [.github/workflows/ci.yml:297–313](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L297-L313), [docs/aspectos.md:5–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L5-L8). Métrica vinculada al escenario asignado no verificada. |
| Secretos protegidos | Cumple | No se encontraron secretos reales en snapshot. No se equipara un identificador público projectKey con credencial. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | Parte documental avanza con ADR sustitutos, pero aspectos conserva rutas antiguas y el validador no está en el flujo del controlador. El modelo/operación completa aún no representa lo prometido en escenarios; [docs/aspectos.md:5–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L5-L8), [backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts:12–24](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/interfaces/ubicacion.controller.ts#L12-L24). |
| Decisión anterior confirmada o reemplazada con evidencia | Cumple | ADR-0005 confirma DEC-01..06 y ADR-0006 reemplaza estado de RSK-04 con evidencias de contrato/DI; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:19–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L19-L33), [docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md:17–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md#L17-L26). Se acredita la sustitución trazable concreta, sin atribuirle el reto S10. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Pendiente de sustentación con entorno desplegado y pipeline en vivo. |

## Rúbrica específica de cinco criterios

| Criterio | Nivel sugerido | Puntaje | Fundamento |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | No se localizó evidencia de asignación oficial del escenario; no se sustituye por un escenario genérico. |
| Decisión e implementación | No verificado | Pendiente | No se puede juzgar la respuesta al escenario asignado hasta identificarlo. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Hay evidencia técnica parcial descrita en la matriz; falta vincularla con el escenario asignado y verificar la operación completa. |
| Evolución arquitectónica trazable | No verificado | Pendiente | La coherencia documental se informa en la matriz; falta demostrar la evolución específica exigida por el reto. |
| Sustentación del reto | Pendiente del docente | Pendiente | Sustentación sobre el entorno desplegado y pipeline en vivo; no se puntúa desde el repositorio. |

Escala aplicable: 0,00 / 0,60 / 0,80 / 1,00 por criterio. **No se calcula total mientras haya criterios pendientes.** No se usa la fórmula semanal. Cualquier nivel es propuesta al docente; la sustentación queda a su cargo.

## Matriz transversal · punta actual

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Repositorio público ISCOUTB/AS_202620_ElMapita, rama main; [README.md:1–7](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/README.md#L1-L7). |
| Estructura mínima presente | Cumple | README, arc42 en plantilla única, ADR, C4, aspectos e IA presentes; [docs/aspectos.md:1–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L1-L8). |
| Estado calificado identificable | Cumple | Hash main congelado y fecha en encabezado; coincide con punta actual. |
| Nombres de ADR según la convención | Cumple | ADR-0001 a 0007 usan NNNN-kebab-case; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:1–11](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L1-L11). |
| ADR aceptados no reescritos | Cumple | Se verificó diff de ADR-0001 contra aa16382 y ADR-0003 contra afae3be: únicamente cambia status a Superseded. Los cambios viven en ADR-0005/0006; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:13–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L13-L33), [docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md:13–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md#L13-L26). Arrastre corregido, sin borrar que ocurrió históricamente. |
| docs/ia.md al día para la semana | Cumple | Entradas S9 distinguen aceptado, corregido y rechazos técnicos, incluidas mediciones falsas y pruebas que no representan producto; [docs/ia.md:395–419](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L395-L419), [docs/ia.md:452–469](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L452-L469). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Workflow CI general success, pero Sonar es no bloqueante y está excluido del fallo del gate; [.github/workflows/ci.yml:254–283](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L254-L283), [.github/workflows/ci.yml:297–313](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L297-L313). El equipo documenta fallo por permisos, [docs/ia.md:434–439](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L434-L439); no se acredita análisis/Gate ejecutado. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Snapshot sin valores de credencial reales. Gitleaks excluye fingerprints de ejemplos y projectKey públicos; historial completo independiente no certificado. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas visibles tras .mailmap: 40 commits agregados. La correspondencia RobotDRMX con integrante queda explícita en .mailmap, pero no se inventa un mapa completo del resto; [docs/ia.md:397–402](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L397-L402). Punta actual: 4 firmas y 40 commits agregados; no equivalen automáticamente a personas. |

## Actions en la punta actual

- [CI: success](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/37258414405), 2026-10-05T03:11:23Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Se revisó el texto del snapshot, incluidos ejemplos/docs. Las coincidencias corresponden a interfaces password/token, variables de entorno, fixtures y referencias al almacén de Actions. No hay .env versionado. Las exclusiones de gitleaks para projectKey/documentación deben seguir justificadas; no se certifica el historial exhaustivo independiente.

## Estado global del proyecto (overall)

El avance S9 es sustantivo y honesto sobre sus límites: nuevo validador, rojo→verde documentado, corrección 500→404, pruebas en dispositivo y ADR sustitutos. La medición descubre defectos reales, no demuestra éxito del producto: EC-04 falla 20/20 y el rendimiento de un placeholder no representa render 3D. El validador está registrado pero el controlador sigue usando el caso de uso anterior. La punta coincide con S9, y SonarCloud está no bloqueante pese al CI general verde.

El delta S9 contiene 9 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Antes del cierre

- Integrar GetValidatedLocationUseCase en el recorrido real y medir el fallback de Flutter; no basta registrarlo como provider.
- Completar enlaces de código/pruebas/medición y actualizar EC-03 hacia los archivos nuevos.
- Corregir acceso a modelo/edificio, repetir EC-01 con respuestas exitosas y medir render 3D real; implementar caché de datos y banner offline antes de cerrar EC-04.
- Resolver permiso de análisis SonarCloud con quien administra la organización; retirar continue-on-error solo cuando exista run/Gate verificable.
- Aportar consigna oficial S10 y conectar hipótesis, línea base, cambio y experimento con esa asignación.

## Tres preguntas de sustentación

1. ¿Qué recibe hoy el usuario si GPS entrega 999 m y por qué el controlador no llama al validador nuevo?
2. ¿Qué costo de almacenamiento/egreso tendría descargar modelos sin caché y qué supuesto cambia al habilitar modo offline real?
3. Las pruebas detectaron HTTP500 y 0/20 offline: ¿qué cambiarían primero y cómo evitarían medir un placeholder como si fuera el mapa3D?
