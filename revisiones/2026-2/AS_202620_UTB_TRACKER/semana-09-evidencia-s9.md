# Evidencia S9 definitiva · UTB Tracker

Revisión actualizada tras el cierre. Estado congelado al **2026-10-05T05:00:00Z** (domingo a medianoche en Colombia).

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_UTB_TRACKER |
| Rama principal remota | `main` |
| Base S5 publicada | `7cfb8729db79435bf9de7d3975a9a3bd7ac5b849` |
| Base S8 | `ae526db29b4f2d1f5981536e18438f9a62b1516d` |
| Estado revisado | `ae526db29b4f2d1f5981536e18438f9a62b1516d` en `origin/main` (2026-09-25T11:36:43-05:00) |
| Punta actual / S10 preliminar | `d17c9eb241e56755d48b022dc00ddb865e40c391` · 2026-10-06T01:08:05-05:00 |
| Observado | 2026-10-06T21:28:33.555768Z |

## Alcance y método

Revisión de archivos y del historial mediante Git, sin ejecutar código, pruebas, scripts ni despliegues de estudiantes. Se consultó una vez el listado de runs de GitHub Actions; un run verde se limita a los pasos que declara su workflow y no acredita la sustentación, el flujo desplegado ni un Quality Gate omitido. No se consultaron etiquetas. No se leyó ningún PDF; el criterio PDF se excluye por decisión docente, sin penalización. Las mediciones documentadas se atribuyen al equipo y no se presentan como ejecuciones del revisor.

El delta se contrasta contra S8; los artefactos previos sirven de línea base y no vuelven a premiarse por existir. Los cambios tardíos se separan en overall.

## Matriz de la ficha S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | No cumple | Delta Git S8→S9 vacío: ambos hashes son ae526db29b4f2d1f5981536e18438f9a62b1516d. [README.md:5–15](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/README.md#L5-L15) describe el corte S4 y [docs/ia.md:11–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/ia.md#L11-L14) usos de agosto; no hay porción S9 identificada. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/aspectos.md#L65-L82): persisten celdas vacías y rutas a arc42 inexistentes; el material corresponde a entregas previas y no hay cadena nueva S9. |
| ADR con la decisión argumentada por el equipo | No cumple | [docs/adr/0003-integracion-sincrona.md:7–25](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L7-L25): decisión anterior de integración síncrona, sin ADR de una porción S9; el delta es vacío. |
| Prueba que falla ante el defecto que cubre | No verificado | [tests/test_loans.py:32–49](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/tests/test_loans.py#L32-L49) comprueba rechazo de un segundo préstamo, pero no hay evidencia de que una prueba detecte un defecto inducido para S9. Un CI fallido no demuestra por sí solo esta sensibilidad. |
| Medición del escenario asociado | No cumple | [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/aspectos.md#L65-L82): evidencia narrativa del corte vertical, sin cifra, herramienta/carga y umbral medidos en S9. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | No cumple | [docs/ia.md:11–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/ia.md#L11-L14): registro limitado a dos entradas de agosto, sin aceptado/corregido/rechazado con motivo para el periodo. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | No cumple | El [árbol congelado](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/tree/ae526db29b4f2d1f5981536e18438f9a62b1516d) y [docs/aspectos.md:65–82](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/aspectos.md#L65-L82) no contienen una auditoría de erosión S9 ni contraste de propiedad de datos para una porción del periodo. |
| Dependencias propuestas verificadas en su registro oficial | No verificado | No hay dependencias añadidas en el delta vacío; no se penaliza esa ausencia. [requirements.txt:1–7](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/requirements.txt#L1-L7) lista dependencias previas, pero no identifica propuestas del modelo ni su verificación oficial en una porción S9. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido del árbol congelado sin credenciales reales detectadas; sin .env versionado. [app/database.py:15–18](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/app/database.py#L15-L18) toma DATABASE_URL del entorno. No se ejecutó el sistema. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No cumple | Los únicos ADR del [árbol](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/tree/ae526db29b4f2d1f5981536e18438f9a62b1516d) son 0001–0003; [docs/adr/0003-integracion-sincrona.md:7–25](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L7-L25) no decide un componente generativo ni justifica no incorporarlo. |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público correcto del repositorio vigente AS_202620_UTB_TRACKER; no se usó el nombre histórico TRACTAR como destino. |
| Estructura mínima presente | Cumple | Las seis rutas mínimas están presentes en el [árbol congelado](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/tree/ae526db29b4f2d1f5981536e18438f9a62b1516d); los enlaces rotos se registran aparte. |
| Estado calificado identificable | Cumple | main, hash y fecha exactos del encabezado. El estado S9 es anterior al cierre y no incluye los siete commits tardíos. |
| Nombres de ADR según la convención | Cumple | Tres nombres conformes: 0001-estilo-arquitectonico.md, 0002-cambio-stack-fastapi-flutter.md y 0003-integracion-sincrona.md; [docs/adr/0003-integracion-sincrona.md:7–25](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L7-L25). |
| ADR aceptados no reescritos | Cumple | Historial de los tres ADR: solo sus commits de creación (5f923cd, e88a3d6, 9cf1ac9); sin ediciones posteriores. [docs/adr/0003-integracion-sincrona.md:3–5](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/adr/0003-integracion-sincrona.md#L3-L5). |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:11–14](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/docs/ia.md#L11-L14): sin actualización del periodo ni rechazo con motivo técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [Run del hash S9](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/36161882569) en failure; [.github/workflows/ci.yml:1–15](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/.github/workflows/ci.yml#L1-L15). No hay scanner ni configuración o resultado público de SonarCloud. |
| Sin credenciales en el repositorio ni en el historial | Cumple | Barrido estático de árbol e historial de patrones de alta especificidad sin incidentes confirmados; [app/database.py:15–18](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/ae526db29b4f2d1f5981536e18438f9a62b1516d/app/database.py#L15-L18) usa entorno. Alcance estático, no auditoría de los secretos externos. |
| Contribución de todos los integrantes | No verificado | Firmas del historial agregadas, con variantes de identidad; correspondencia con toda la matrícula no verificada. No se mantienen inferencias individuales de informes anteriores. |

## Recuento y nota sugerida

**1 de 10 criterios Cumple. Nota sugerida: 1.4 = 1 + 4 × (1/10). Propuesta al docente; la nota final se fija en Moodle.** No verificado no se convierte en Cumple ni en una ejecución fallida.

## Estado global del proyecto (overall)

Punta de la misma rama: `d17c9eb241e56755d48b022dc00ddb865e40c391` (2026-10-06T01:08:05-05:00). Hay **0 commits en el delta S8→S9** y **7 commits posteriores al cierre S9**. S9 está congelada sin cambios respecto de S8. Después del cierre hay siete commits, incluida reorganización del backend y autenticación JWT. El CI sigue fallando y la documentación no refleja todavía la nueva estructura.



### Hallazgos abiertos

- S9 no incorpora commits nuevos frente a S8; la autenticación de octubre es tardía y solo se valora en overall/S10.
- Recuperar el CI y ejecutar también tests/ de contratos, préstamos y recursos; actualmente solo se invoca app/tests/.
- Actualizar README, enlaces de aspectos y C4 para la nueva estructura; completar arc42 de despliegue.
- Publicar URL de despliegue, procedimiento reproducible, logs estructurados, métricas y costo.
- Registrar la asignación S10, la línea base, ADR y experimento con resultados.
- Actualizar docs/ia.md, auditar propiedad de datos y decidir sobre componente generativo.
- Corregir configuración de expiración JWT: [app/core/config.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/config.py#L10) devuelve texto y [app/core/security.py:10](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/app/core/security.py#L10) lo pasa a timedelta(minutes=...). Hallazgo estático; no se ejecutó.
- Verificar correspondencia de las identidades del historial con los integrantes.

### Hallazgos cerrados o sustituidos con evidencia actual

- El workflow actual coloca preparación de Python y pruebas antes del despliegue mediante needs: test: [.github/workflows/ci.yml:7–26](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/d17c9eb241e56755d48b022dc00ddb865e40c391/.github/workflows/ci.yml#L7-L26). Es una mejora tardía; el run aún falla y no cierra CI.
- Aparecen firmas adicionales en el historial actual; se retira la afirmación categórica antigua de que solo una persona ha contribuido. No se atribuye por nombre una firma a una persona.

## Próximos pasos

El estado al cierre es el mismo de la semana anterior y no contiene una porción nueva S9. Falta la cadena con ADR, prueba sensible al defecto, medición y auditoría de erosión, además del registro de IA y la decisión sobre componente generativo. La reorganización y autenticación de octubre llegan después del cierre y se reconocen en el estado actual, sin cambiar esta revisión.
