# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | Recobra |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Recobra` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Camilo Andres Conde Corrales · Fernando Isacc Conde Herrera · Miguel Alejandro Iii Jacome Yanez · Veronica Ubarne Reyes — cuentas consolidadas: `Cconde31` (incluye la identidad `Steamlinker`, unificada por `.mailmap` el 05/09), `MiguelJacome`, `vylrir` (Verónica Ubarne), y un commit identificado con el nombre real de Fernando Isacc Conde Herrera; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://recobra.iscoutb.dev · salud/readiness observados el 2026-10-10; ver límites en S10 |
| Última revisión | 2026-10-10 · actualización S10 preliminar; S9 definitiva del 2026-10-06 sin cambios |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `ebe6cca7a903bb333678bd20ba5327d8fcb127f7` · 2026-10-04T23:40:37-05:00 | 10/10 | 5.0 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `ac3cbb64a70fa5f23d270ab83b0a210106aded28` · 2026-10-08T18:26:27-05:00 | 9/12 de comprobación (sin PDF): 9 Cumple, 1 No cumple, 2 No verificado | C1/C2 pendientes; C3/C4 Básico (0,60 cada uno), propuestas al docente. Sin total; sustentación pendiente. Ver [S10](semana-10-corte2.md) | sí, avance 2026-10-10 |
| 1 | Evidencia S1 · Equipo, problema y repositorio | `da5c15d` · 2026-08-07T17:54:04-05:00 | 3/9 | no se publica | sí |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `d2dac73` · 2026-08-16T23:44:54-05:00 | 4/9 | no se publica | sí |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `cb5c579` · 2026-08-23T23:44:12-05:00 | 4/9 | no se publica | sí |
| 4 | S4 | `2268b33` (2026-08-30T22:34:56-05:00) | 6/10 | 3.4 | si |
| 5 | CORTE1 | `f7c1a6c` (2026-09-07T09:59:41-05:00) | 8/12 | 3.7 | si |
| 6 | S6 | `47fb44b` (2026-09-13T16:58:53-05:00) | 4/8 | 3.0 (prelim.) | si |
| 7 | S7 | `8f25313` (2026-09-19T13:37:58-05:00) | 10/10 | 5.0 | si |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `5c7f77b` (2026-09-27T19:55:59-05:00) | 10/10 (2 filas de despliegue diferidas) | 5.0 (provisional) | si |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

Estado vigente observado el 2026-10-10 en la punta citada en [S10](semana-10-corte2.md). Las correcciones posteriores al cierre no cambian S9. El registro histórico siguiente conserva la fecha de cada observación.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Corroborar mediante fuente docente la autorización para que el equipo elija S1. La declaración nueva existe; no seguir afirmando que falta todo escenario. [docs/medicion-s10.md:3–43](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/medicion-s10.md#L3-L43) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Conservar JSON bruto de cada corrida, hora, entorno, versiones y SHA exacto desplegado. “a8068df o posterior” no fija el artefacto medido. Una sola corrida y el cambio de 1 a 1.000 filas impiden atribuir la mejora exclusivamente a la plataforma. [docs/medicion-s10.md:28–40](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/medicion-s10.md#L28-L40); [docs/medicion-s10.md:78–96](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/medicion-s10.md#L78-L96) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Separar inferencia de medición: la resta aproximada entre p50 cliente y media/p95 servidor no aísla red ni descarta CPU/SQL; provienen de estadísticas/ventanas diferentes. La ventana contiene hasta 200 éxitos recientes, los errores son acumulados desde el arranque y cumpleObjetivo solo mira latencia. [docs/medicion-s10.md:67–76](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/medicion-s10.md#L67-L76); [src/observabilidad/metricas.service.ts:3–50](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/observabilidad/metricas.service.ts#L3-L50); [src/observabilidad/latencia-busqueda.interceptor.ts:15–25](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/observabilidad/latencia-busqueda.interceptor.ts#L15-L25) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Completar arc42§5/§6 y C4-C3 con PostgreSQL vigente, búsqueda, Emparejamiento, /health/ready, métrica GET y filtro 503. Ya no procede el hallazgo viejo de PostgreSQL planeado en C4-C2. [docs/arc42/arc42.md:141–183](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/arc42/arc42.md#L141-L183); [docs/c4/C4-C3.md:39–72](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/c4/C4-C3.md#L39-L72) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Declarar 503 en GET /publicaciones/{id} y probarlo contra OpenAPI. La ruta usa el mismo repositorio y filtro global, pero el contrato solo declara 200/404. [docs/contracts/openapi.yaml:160–183](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/contracts/openapi.yaml#L160-L183); [src/application/use-cases/consultar-publicacion.ts:5–11](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/application/use-cases/consultar-publicacion.ts#L5-L11); [src/publicaciones/publicaciones.module.ts:27–34](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/publicaciones/publicaciones.module.ts#L27-L34) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| No confundir SELECT 1 con esquema listo: readiness comprueba conectividad, mientras la creación de tabla/índice puede seguir fallando en el reintento. Mostrar fallo y recuperación de la dependencia, incluyendo un esquema no preparado, en la sustentación. [src/infrastructure/persistence/postgres-publicacion.repository.ts:51–78](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/infrastructure/persistence/postgres-publicacion.repository.ts#L51-L78); [src/infrastructure/persistence/postgres-publicacion.repository.ts:104–118](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/infrastructure/persistence/postgres-publicacion.repository.ts#L104-L118) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Mantener abierto SonarCloud/QG: éxito global no prueba el scanner con continue-on-error. Actualizar correcciones.md, que aún dice que falta crear SONAR_TOKEN, frente a la explicación más reciente de permisos. No se propone reejecutar ni cambiar credenciales desde esta revisión. [correcciones.md:122–137](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/correcciones.md#L122-L137); [docs/no-conformidades.md:107–118](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/no-conformidades.md#L107-L118) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Revisar garantías de transporte: DATABASE_SSL=false es una decisión explícita para red interna; con TLS activado el adaptador usa rejectUnauthorized:false, por lo que no valida el certificado del servidor. No describir ese valor como verificación de identidad de la base. [src/infrastructure/persistence/postgres-publicacion.repository.ts:29–41](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/infrastructure/persistence/postgres-publicacion.repository.ts#L29-L41). No se verificó aislamiento de red ni se cambió esa configuración. | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Persistencia de coincidencias, copias de seguridad y cortes de redespliegue siguen como riesgos declarados. No hay experimento independiente de recuperación ni prueba de persistencia ejecutada por el revisor. [docs/arc42/arc42.md:191–208](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/arc42/arc42.md#L191-L208); [docs/arc42/arc42.md:264–269](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/arc42/arc42.md#L264-L269) | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Contribución sustantiva individual y sustentación siguen por validar; la actualización agregada no reasigna identidades. | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Se incorpora un experimento S10 específico, con hipótesis, montaje, variables, umbral, línea base, resultado y límites. Se cierra la ausencia documental, no la procedencia oficial ni la validación independiente de la carga. [docs/medicion-s10.md:3–43](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/medicion-s10.md#L3-L43); [docs/medicion-s10.md:45–108](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/medicion-s10.md#L45-L108) | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| La ausencia de métrica de búsqueda queda corregida en fuente: interceptor GET, ventana separada S1, umbral 400 ms y contador de errores; existen pruebas unitarias/e2e. [src/observabilidad/latencia-busqueda.interceptor.ts:5–27](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/observabilidad/latencia-busqueda.interceptor.ts#L5-L27); [src/observabilidad/metricas.service.spec.ts:4–39](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/src/observabilidad/metricas.service.spec.ts#L4-L39); [test/publicaciones.e2e-spec.ts:97–108](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/test/publicaciones.e2e-spec.ts#L97-L108) | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| Salud y readiness del despliegue nuevo responden 200 en la observación actual. El chequeo Render de 2026-10-06 queda solo como antecedente histórico. | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| C4-C2/C3 ya incorporan PostgreSQL, búsqueda y Emparejamiento; se cierra esa omisión concreta, aunque permanecen los desajustes listados. [docs/c4/C4-C2.md:6–17](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/c4/C4-C2.md#L6-L17); [docs/c4/C4-C3.md:18–42](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/c4/C4-C3.md#L18-L42) | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| README corrige variables, URL de producción y esquema de error; Render se rotula histórico. [README.md:68–111](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/README.md#L68-L111); [README.md:150](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/README.md#L150); [render.yaml:1–4](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/render.yaml#L1-L4) | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| La sucesión de ADR-0004 a 0009 y de ADR-0005/0006 a 0010 está enlazada; ADR-0011 registra enmiendas de 0002/0003 y demás antecedentes sin reescribir git. Se cierra el trabajo de declaración/enlace, no se cambia el hecho histórico. [docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md:53–71](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md#L53-L71) | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/ia` vacío (y sin extensión .md) | S1 | no (resuelto: `docs/ia.md` con entradas por integrante y por semana, incluida S5) | Borrar el `docs/ia` vacío y completar el registro con todos los integrantes |
| `docs/aspectos.md` narrativo, sin tabla ni enlaces | S1 | no (resuelto: tabla de 8 columnas, filas A1-A4, navegable) | Tabla de 8 columnas y enlaces a escenarios y ADR |
| Sin diagrama C4 (solo descripción textual) | S1 | no (resuelto: `docs/c4/README.md`) | Borrar el C4 textual antiguo |
| Fernando Isacc Conde Herrera y Veronica Ubarne Reyes sin aparición en el historial | S1 | parcial (Verónica consolidada como `vylrir`, 9 commits; Fernando sigue con 1 solo commit en todo el semestre) | Confirmar acceso, contribución sustantiva y reparto real de trabajo con Fernando |
| ADR fuera de convención (`docs/ADR/01-…`, sin motivo de descarte); el ADR viejo se borró sin marcarlo reemplazado | S3 | no (resuelto: ADR-0001 ahora dice explícitamente "Reemplazada por ADR-0002 - 2026-09-05" en vez de borrarse) | Mantener la práctica en ADR futuros: nunca borrar un ADR aceptado |
| Matriz comparativa genérica, no contra el árbol de utilidad | S3 | sin verificar en esta pasada (foco de esta revisión fue el reto de S5) | Revisar en el próximo corte |
| Sin esqueleto ejecutable (código, prueba, comando de arranque) | S3 | no (resuelto: NestJS + Flutter ejecutables, con pruebas y CI) | — |
| `node_modules/` completo versionado | S3 (cierre) | no en HEAD, pero **el token de Coveralls que contenía sigue en el historial sin rotar** (`905f546:node_modules/debug/.coveralls.yml`) | Rotar el token de Coveralls y confirmarlo en la sustentación; valorar limpiar el historial con `git filter-repo` si el docente lo pide |
| Implementar el corte vertical real (src/domain, src/application, src/infrastructure, tests/) | S4 | no (resuelto en la migración a NestJS de S5) | — |
| Corregir secciones 5 y 6 de arc42 y añadir la sección 9 | S4 | parcial (`docs/arc42.md` suelto convive con `docs/arc42/04-estrategia-solucion.md`) | Consolidar en una sola ubicación (`docs/arc42/` con secciones) |
| Completar tabla de aspectos con las 8 columnas | S4 | no (resuelto) | — |
| Alinear C4 con el código real o reducir alcance | S4 | no (resuelto: C4 refleja NestJS/Flutter) | — |
| Configurar CI y ejecutar pruebas en verde | S4 | no (resuelto: `.github/workflows/ci.yml`, runs en verde antes y después del cierre) | — |
| Eliminar node_modules del repositorio y rotar el token expuesto | S4 | parcial (node_modules ya no se versiona; el token sigue sin rotar) | Rotar el token — sigue pendiente |
| Confirmar etiqueta corte-1 | S5 | sí, con matiz: existe pero es **posterior al cierre** | La etiqueta debe fijarse antes del cierre, no seguir moviéndose después |
| PDF de dos páginas | S5 | no (resuelto: `docs/entrega-corte1-moodle.pdf`, 2 páginas, en el propio repo) | Regenerar el PDF: la página 2 todavía cita la latencia vieja "8-15 ms" en vez de la medición reproducible corregida |
| ADR del reto con alternativas y consecuencias | S5 | no (resuelto: ADR-0003, nivel sobresaliente) | — |
| Línea base medida y reproducible | S5 | no (resuelto: `docs/medicion-corte1.md` con script y 3 corridas) | — |
| Pipeline con pruebas en verde | S5 | no (resuelto: runs verdes antes y después del cierre) | — |
| docs/aspectos.md con 8 columnas | S5 | no (resuelto) | — |
| Registro de IA del corte | S5 | no (resuelto: entradas del 05/09 con rechazos justificados) | — |
| Rotar token de Coveralls | S5 | sí | Rotar el token — no se ha confirmado |
| Corte vertical y documentación de publicación: commits 87ada13, 10c239b, 905f546 del 31 ago/1 sep (posteriores al cierre). | S4 | no (resuelto tarde) | — |
| Migración a NestJS/Flutter, CI y ADR 0002/0003: commits 3a82ca6, 316a994, dc91a8b, e68eb8e, 25525ae, 6ee5b66, f7c1a6c del 5 al 7 de septiembre. | S4 | no (resuelto tarde) | — |
| Corrección de identidad de autor con .mailmap: 6ee5b66 (posterior al cierre). | S4 | no (resuelto tarde) | — |
| Redactar sección 9 de arc42 enlazada a los ADR (sigue ausente en HEAD). | S4 | si | |
| Completar docs/aspectos.md con las 8 columnas y enlaces verificables. | S4 | si | |
| Dejar evidencia de CI en verde para el commit de la entrega (no solo en HEAD). | S4 | si | |
| Corregir correspondencia entre C4 nivel 2 y el código real. | S4 | si | |
| Eliminar node_modules del repositorio y aplicar .gitignore. | S4 | si | |
| f7c1a6c 2026-09-07T09:59:41-05:00 enlaza ADR y cubre criterios 1-3 de la rúbrica, pero es posterior al cierre del corte 1. | S5 | no (resuelto tarde) | — |
| correcciones.md no existe en HEAD. | S5 | si | |
| arc42 no está completo en HEAD. | S5 | si | |
| CI sin SonarCloud en HEAD. | S5 | si | |
| README sin comando único de arranque en HEAD. | S5 | si | |
| Commit f7c1a6c (2026-09-07) posterior al cierre enlaza ADR a commits y cubre criterios de rúbrica; no afecta la nota del corte pero es tardío. | S5 | no (resuelto tarde) | — |
| Crear correcciones.md en la raíz antes del cierre. | S5 | si | |
| Verificar entrega del PDF en Moodle. | S5 | si | |
| Sustentación pendiente. | S5 | si | |
| Crear correcciones.md en la raíz del repositorio con trazabilidad de hallazgos S1-S4. | S5 | si | |
| Contrato OpenAPI/AsyncAPI en formato ejecutable versionado | S7 | si | |
| Prueba de contrato y su invocación en el pipeline | S7 | si | |
| Evidencia de fallo de la prueba ante cambio incompatible | S7 | si | |
| ADR de estrategia de integración (síncrona/async) | S7 | si | |
| Flechas del C4 nivel 2 con protocolo y formato | S7 | si | |
| Secciones de arc42 faltantes (7, 8, 11, 12) | S7 | si | |
| Evidencia auditable de CI y Quality Gate de SonarCloud | S7 | si | |
| Token de Coveralls expuesto en el historial, declarado abierto en docs/no-conformidades.md. | S6 | si | |
| Run de CI y URL pública de SonarCloud con Quality Gate para 47fb44b. | S6 | si | |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos. | S6 | si | |
| Diff contra hash S5, C4 nivel 3 y ADR si cambiaron los límites. | S6 | si | |
| Auditoría de no conformidades de propiedad de datos y su plan de corrección. | S6 | si | |
| Verificación de correspondencia entre integrantes declarados y cuentas del historial. | S6 | si | |
| 8f25313 2026-09-19T13:37:58-05:00 «Registrar en ia.md el uso de IA de esta semana (S6/S7)»: cierra la falta de registro de IA (contenido no aportado para verificar). | S7 | no (resuelto tarde) | — |
| 3d9da06 2026-09-19T13:37:14-05:00 «Corregir hallazgo de SonarCloud: ya corre y esta en verde (GitHub App)»: corrige un hallazgo transversal anterior solo de forma declarativa, sin run ni URL pública. | S7 | no (resuelto tarde) | — |
| 573e512 2026-09-19T13:04:46-05:00 «Agregar secciones 8 y 11 de arc42»: completa documentación de semanas anteriores al final de la ventana. | S7 | no (resuelto tarde) | — |
| c7bf54c 2026-09-19T11:26:41-05:00 «Agregar flujo de interaccion a seccion 6 y nueva seccion 7 de arc42»: cubre el recordatorio de documentación de S7 sobre la marcha. | S7 | no (resuelto tarde) | — |
| 667d66f 2026-09-19T13:33:47-05:00 «Limpiar formato de las secciones 6-12 de arc42 y del diagrama C4-C2»: ajuste de entregables previos. | S7 | no (resuelto tarde) | — |
| No hay commits posteriores al cierre de S7 (commits_tardios_post_cierre vacío). | S7 | no (resuelto tarde) | — |
| Añadir la evidencia verificable de CI: contenido de .github/workflows/ci.yml con el paso de contrato y enlaces de los runs (verde y rojo). | S7 | si | |
| Publicar la URL del análisis de SonarCloud con el estado del Quality Gate para el hash revisado. | S7 | si | |
| Aportar el historial git de docs/contracts/openapi.yaml para respaldar la versión declarada. | S7 | si | |
| Aportar el contenido de docs/ia.md con lo rechazado y su motivo por cada uso. | S7 | si | |
| Consolidar las cuentas del historial con los integrantes declarados y confirmar la rotación del token de Coveralls mencionado en el checklist. | S7 | si | |
| Publicar el despliegue y su health check verificables. | S8 | sí (diferido) | Fila diferida por decisión docente: la URL se entrega por Moodle. El README ya declara la URL y la ruta `/health` existe. |
| SonarCloud sin invocación en el workflow ni URL pública del Quality Gate. | S6 | si | Falta la evidencia del contrato §8. |
| ADR-0002 y ADR-0003 editados después de aceptarse sin reemplazo declarado. | S8 | si | Crear un ADR sucesor en vez de editar uno aceptado. |
| La porción de código que la cadena S9 presenta (Emparejamiento + PostgreSQL) se creó en `e952f5b`, antes del hash de S8: es línea base y no satisface la fila 1. | S9 (prelim.) | si | Para S9 hace falta una porción construida en el periodo, con sus rutas y commits. |
| Sin dependencias añadidas en el periodo S9 que verificar en el registro oficial. | S9 (prelim.) | si | Añadir en el periodo las dependencias que se quieran respaldar, o dejar constancia de que no hubo. |
| SonarCloud: scanner en `continue-on-error` y sin URL pública del Quality Gate. | S6 | si | Falta la evidencia auditable del contrato §8. |
| ADR-0004 editado el 2026-09-28 (`34ab8f2`) después de aceptarse, sin reemplazo declarado. | S9 (prelim.) | si | Crear un ADR sucesor en vez de editar uno aceptado. |

</details>

## Estado del contrato del repositorio

Actualización S10 del 2026-10-10; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Repositorio público https://github.com/ISCOUTB/AS_202620_Recobra, accesible por clon de lectura y rama master identificada mediante git. Nombre y organización conformes. |
| Estructura mínima presente | Cumple | Árbol actual conserva README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md. [README.md:179–195](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/README.md#L179-L195); [docs/aspectos.md:1–16](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/aspectos.md#L1-L16). El cumplimiento estructural no asegura que todas las vistas estén alineadas. |
| Estado calificado identificable | Cumple | origin/master `ac3cbb64a70fa5f23d270ab83b0a210106aded28`, 2026-10-08T18:26:27-05:00, punta observada antes del cierre futuro S10. Esta revisión preliminar no cambia el hash definitivo S9. |
| Nombres de ADR según la convención | Cumple | Once archivos Markdown en docs/adr/ con prefijo de cuatro cifras y kebab-case. Nuevos ADR: [docs/adr/0010-despliegue-en-dokploy-servidor-del-laboratorio.md:1–10](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/adr/0010-despliegue-en-dokploy-servidor-del-laboratorio.md#L1-L10); [docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md:1–6](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md#L1-L6). |
| ADR aceptados no reescritos | No cumple | El historial conserva las ediciones posteriores a aceptación; no se puede declarar que nunca ocurrieron. Ahora están regularizadas documentalmente: [docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md:10–24](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md#L10-L24) y [docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md:53–71](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/adr/0011-registro-de-enmiendas-a-adrs-aceptados.md#L53-L71). El delta de los ADR-0002…0006 añade solo notas de estado/sucesión, sin reescribir sus cuerpos. Se cierra el pendiente de declarar/enlazar antecedentes; se conserva la no conformidad histórica sin pedir reescribir git ni penalizar otra vez S9. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:63](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/ia.md#L63) contiene uso S10, aceptado, corregido y rechazado con razones técnicas. Hay entradas complementarias de revisión de costo, ADR y C4 en [docs/ia.md:45](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/ia.md#L45), [docs/ia.md:86](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/ia.md#L86) y [docs/ia.md:102](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/ia.md#L102). Se verifica contenido y actualización, no identidad ni comprensión individual por inferencia. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [CI 37859444538](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/37859444538) success en el hash actual; [CI 37858210549](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/37858210549) failure en 34b123ab1081f5784b822750294391d1135af754, que había quitado continue-on-error. En HEAD el scanner permite fallo: [.github/workflows/ci.yml:31–48](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/.github/workflows/ci.yml#L31-L48). [docs/no-conformidades.md:107–118](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/no-conformidades.md#L107-L118) declara token existente pero falta de Execute Analysis; la causa proviene del equipo, no se verificó en logs. La URL pública citada y el OK en [docs/no-conformidades.md:76–87](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/docs/no-conformidades.md#L76-L87) corresponden a 2026-09-19, no al hash actual. Falta scanner exitoso y Quality Gate actual citable y bloqueo efectivo. No se reejecutó ni reconfiguró ningún scanner. |
| Sin credenciales en el repositorio ni en el historial | No verificado | [.env.example:1–8](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/.env.example#L1-L8) mantiene DATABASE_URL vacía; [deploy/compose.lab.yaml:20–25](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/deploy/compose.lab.yaml#L20-L25) interpola variables; [.github/workflows/ci.yml:44–48](https://github.com/ISCOUTB/AS_202620_Recobra/blob/ac3cbb64a70fa5f23d270ab83b0a210106aded28/.github/workflows/ci.yml#L44-L48) usa el almacén de secretos. En los archivos del delta leídos no se identificaron valores de credenciales del equipo. Esta pasada incluyó lectura estática del delta, sin un barrido completo del historial. El resultado histórico de octubre 6 no se convierte en certificación nueva. NV expresa límite de verificación, no exposición inferida. La observación histórica sobre un artefacto Coveralls de una dependencia no se convierte en acusación de una credencial del equipo ni se reproduce su valor. |
| Contribución de todos los integrantes | No verificado | Actualización del 2026-10-10: 143 commits en la punta; cinco identidades de correo brutas, consolidadas por .mailmap en cuatro grupos, con 73, 29, 27 y 14 commits. En el delta hay 15 commits distribuidos en cuatro grupos (12, 1, 1 y 1). No se infieren correspondencias nuevas entre cuenta e integrante por parecido de nombre. El recuento no acredita por sí solo aporte sustantivo de código y documentación de cada integrante; esa comprobación queda NV. La tabla individual histórica se conserva con las cifras de su observación original; no se reasignan identidades. |

## Contribución por integrante

Actualización del 2026-10-10: 143 commits en la punta; cinco identidades de correo brutas, consolidadas por .mailmap en cuatro grupos, con 73, 29, 27 y 14 commits. En el delta hay 15 commits distribuidos en cuatro grupos (12, 1, 1 y 1). No se infieren correspondencias nuevas entre cuenta e integrante por parecido de nombre. El recuento no acredita por sí solo aporte sustantivo de código y documentación de cada integrante; esa comprobación queda NV. La tabla individual histórica se conserva con las cifras de su observación original; no se reasignan identidades.

La tabla individual siguiente es histórica; sus cifras no son el recuento de la punta actual. No se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits (HEAD) | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Camilo Andres Conde Corrales | `Cconde31` (incluye `Steamlinker`, consolidado) | 44+1 | — | — | Autor de casi todo el reto S5 |
| Fernando Isacc Conde Herrera | commit identificado con nombre real | 24 | — | — | Ya no queda con contribución mínima |
| Miguel Alejandro Iii Jacome Yanez | `MiguelJacome` | 10 | — | — | — |
| Veronica Ubarne Reyes | `vylrir` | 25 | — | — | Consolidada desde S3-S4 |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- Si PostgreSQL acepta SELECT 1 pero la creación de la tabla o del índice sigue fallando, ¿qué devolverán /health/ready, la búsqueda y la consulta por id? Demuestren detección, respuesta contractual y recuperación sin confundir conectividad con servicio útil.
- La solución cuesta cero para el equipo, pero depende del servidor compartido y no tiene backups configurados. ¿Qué costo de operación, recuperación y alternativa asumirían si el laboratorio se retira o exige redespliegues sin corte, y qué evidencia fija hoy el límite de capacidad?
- ¿Qué repetirían para probar la causa de la mejora entre Render y Dokploy? Usen el mismo conjunto de datos, cliente, carga, versión y varias corridas; expliquen por qué el p95 de las últimas doscientas búsquedas exitosas del servidor no es el p95 cliente de toda la prueba.
