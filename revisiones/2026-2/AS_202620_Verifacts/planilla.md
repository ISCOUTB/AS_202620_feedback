# Planilla de equipo · Verifacts

## Identificación

| | |
|---|---|
| Equipo | Verifacts |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_Verifacts` |
| Integrantes y su usuario de GitHub | Identificación histórica (no acredita por sí sola la correspondencia actual): Ver [EQUIPOS.md](../../../EQUIPOS.md); recuento histórico heredado (no vigente): `PedroC1213` (240 commits, dos correos consolidados) y `Cristian Cardeño` (31 commits, dos correos con la misma firma), sin correspondencia individual confirmada; falta una tercera identidad atribuible.; ver comprobación actual de contribución más abajo. |
| URL del sistema desplegado | https://verifacts-web.onrender.com · ver comprobación y límites en S10 |
| Última revisión | 2026-10-10 · actualización S10 preliminar; S9 definitiva del 2026-10-06 sin cambios |

## Estado por entrega

| Semana | Entrega | Estado revisado (rama y hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 9 | S9 · definitiva | `master` · `4f0652291c47f5093da1230b245a980614220e80` · 2026-10-02T00:01:45-05:00 | 7/10 | 3.8 (propuesta al docente) | sí, 2026-10-06 |
| 10 | Segundo corte · preliminar | `master` · `5c643bd03f19630d6459da79fb13fb2d5f943c7b` · 2026-10-07T15:32:38-05:00 | 3/12 de comprobación (sin PDF): 3 Cumple, 6 No cumple, 3 No verificado | C1/C2 pendientes; C3/C4 Básico (0,60 cada uno), propuestas al docente. Sin total; sustentación pendiente. Ver [S10](semana-10-corte2.md) | sí, avance 2026-10-10 |
| 8 | S8 | `d2d7b5c` (2026-09-25T16:38:43-05:00) | 10/10 | 5.0 (provisional; 2 filas de despliegue pendientes) | sí (definitiva) |
| 7 | S7 | `635f9b7` (2026-09-16T00:52:52-05:00) | 10/10 | 5.0 (auditada) | sí, auditada |
| 6 | S6 | `5941c33` (2026-09-12T02:00:20-05:00) | 8/8 | 5.0 (prelim.) | si |
| 1 | S1 | `(sin commits)` () | sin actividad | no aplica | si |
| 2 | S2 | `(sin commits)` () | sin actividad | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `8259b75` · 2026-08-23T23:50:00-05:00 | 4/9 | no se publica | sí |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | `443e908` · 2026-08-29T18:17:18-05:00 | 7/10 | 3.8 | sí |
| 5 | CORTE1 | `67f8cea` (2026-09-09T16:30:01-05:00) | 8/12 | 3.7 | si |

S8 se califica sobre 10 filas graduables. Quedan **pendientes de calificar** las dos filas de despliegue («URL del sistema accesible desde fuera de la red de la universidad» y «Health check consultable»): la URL se entrega por Moodle y no está disponible en esta pasada.

## Lo que se arrastra

Estado vigente observado el 2026-10-10 en la punta citada en [S10](semana-10-corte2.md). Las correcciones posteriores al cierre no cambian S9. El registro histórico siguiente conserva la fecha de cada observación.

| Hallazgo actual | Estado | Evidencia y próximo paso |
|---|---|---|
| Confirmar mediante la consigna docente que la comparación Render/Lambda es el escenario operativo asignado S10; el nuevo rótulo del equipo no basta como prueba independiente. | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Construir comparación realmente equivalente: mismo payload de 10.000 caracteres, runtime/carga definidos, cliente y métricas comparables; distinguir Render público, aplicación local y SAM emulado; separar frío/caliente y publicar series por operación con fecha y commit. [docs/adr/0005-comparacion-lambda-render.md:27–35](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L27-L35); [serverless-prototype/events/analysis_event.json:19](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/events/analysis_event.json#L19). | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| No reutilizar como POST /analysis el P95 anteriormente rotulado GET /health sin nuevas series verificables; conservar salidas distintas con --out y explicar por qué Duration SAM no es automáticamente latencia real ni costo facturable AWS. [docs/adr/0005-comparacion-lambda-render.md:64–101](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L64-L101); [serverless-prototype/medir_cold_start.py:66–93](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/medir_cold_start.py#L66-L93). | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Registrar la evolución del ADR-0005 mediante nuevo ADR/reemplazo trazable y corregir causalidad de imports; la tabla de enmiendas ya existe, pero no cubre esa reescritura. [docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27); [serverless-prototype/lambda_handler.py:1–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/serverless-prototype/lambda_handler.py#L1-L5). | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Actualizar arc42 §3/§10 y pendientes de aspectos/README para distinguir lo implementado, la medición local ya publicada y lo aún no medido en producción. [docs/arc42/03-contexto-y-alcance.md:112–118](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/03-contexto-y-alcance.md#L112-L118); [docs/arc42/10-requisitos-de-calidad.md:41–54](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/10-requisitos-de-calidad.md#L41-L54); [README.md:622–630](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L622-L630). | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Proporcionar evidencia pública del Quality Gate asociada a la revisión y aclarar bloqueo de integración; la declaración OK es nueva, el revisor obtuvo 403. Scanner success no acredita gate ni protección de rama. [docs/despliegue.md:37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L37). | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Fijar pytest-cov en el cierre de dependencias: ya aparece en el inventario de auditoría, pero el workflow conserva pip install pytest-cov sin versión y no está en requirements.txt. [docs/auditoria-s9.md:44–51](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L44-L51); [.github/workflows/sonarcloud.yml:26–32](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L32); [requirements.txt:1–7](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/requirements.txt#L1-L7). | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Demostrar persistencia/recuperación tras reinicio/redeploy y separar su costo del escenario gratuito: [docs/costos.md:14–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/costos.md#L14-L18) y [docs/costos.md:29–35](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/costos.md#L29-L35) reconocen almacenamiento efímero y despertar lento. Health puntual no prueba recuperación de datos. | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Aclarar matrícula y correspondencia de las firmas de Git con los integrantes; el recuento de firmas no permite concluir quién contribuyó o faltó. | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| Completar la verificación de seguridad de árbol/historial fuera del alcance acotado de esta pasada; NV no es exposición confirmada. | Abierto o pendiente de verificación, según la evidencia | Ver [S10](semana-10-corte2.md) y la actualización de retroalimentación |
| ADR-0006 renombrado a 0006-semantica-del-resultado.md sin alterar su contenido; auditoría trasladada a docs/ y arc42 §8 a nombre con guiones. Se resuelven las rutas específicas citadas antes en A-06/README; no se afirma que todos los enlaces estén comprobados. [docs/aspectos.md:25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/aspectos.md#L25); [README.md:185–191](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L185-L191). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| ADR-0007 existe realmente y está indexado; evalúa alternativas generativas y mantiene el motor determinista. [docs/adr/0007-no-incorporar-componente-generativo.md:1–40](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0007-no-incorporar-componente-generativo.md#L1-L40); [docs/arc42/09-decisiones-arquitectonicas.md:18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L18). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| MLAnalyzer queda rectificado como no implementado en IA y nota fechada de ADR-0002. [docs/ia.md:19](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L19); [docs/adr/0002-contextos-sin-cambios.md:36–43](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0002-contextos-sin-cambios.md#L36-L43). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| IA ya contiene el balance aceptado/corregido/rechazado con motivos y entradas del periodo; es corrección tardía respecto de S9. [docs/ia.md:23–46](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L23-L46). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| La tabla de enmiendas existe y declara adiciones históricas. Se cierra solo su ausencia documental, no la infracción de inmutabilidad. [docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| pytest-cov se añade al inventario de dependencias; persiste falta de versión fijada. [docs/auditoria-s9.md:44–51](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L44-L51). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| El script de mutaciones distingue ahora retorno 1 de pytest (fallo de prueba) de otros códigos de infraestructura. Corrección estática real; no se ejecutó y no cambia la evaluación S9. [scripts/mutaciones_s9.py:33–40](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/scripts/mutaciones_s9.py#L33-L40). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211) están success para el nuevo hash. Sustituye las URLs de la punta anterior como evidencia CI actual; no cierra Gate. | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |
| ADR-0005 ya identifica S10 y enumera hipótesis/variables/umbral. Cierra la ausencia de esos elementos declarativos, sin confirmar origen oficial ni validez experimental. [docs/adr/0005-comparacion-lambda-render.md:7–36](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L7-L36). | Corrección documentada en la punta actual, con el alcance indicado | Ver [overall S10](semana-10-corte2.md#estado-global-del-proyecto-overall) |

<details>
<summary>Registro histórico previo a esta revisión (estados a la fecha de cada observación)</summary>

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| Repositorio creado tarde (primer commit 18-ago, después de los cierres de S1 y S2) | S1 | sí | excepción docente aplicada; no repetible |
| El PDF de entrega referencia archivos que no están en el repositorio | S2 | sí | el repositorio es la entrega; subir los escenarios (S3: ya subidos como `docs/arc42/05-escenarios-de-calidad.md`) |
| 2 de 3 integrantes sin aparición en el historial | S1 | sí | urgente antes del corte 1; en S3 solo aparecen `PedroC1213` y `Cristian Cardeño` (tardío) |
| Estructura desviada: `docs/c4-contexto.md` fuera de `docs/c4/`, `docs/IA.md` | S1 | sí | — |
| arc42 §4 con principios genéricos, no tácticas ligadas a los escenarios Q-01…Q-05 | S3 | sí | nombrar tácticas concretas por escenario |
| Matriz comparativa genérica, no contra el árbol de utilidad | S3 | sí | rehacer contra las ramas del árbol, escenario por escenario |
| ADR sin enlazar desde `aspectos.md` ni desde el escenario | S3 | sí | añadir los dos enlaces |
| README sin comando de arranque documentado (existe `run.py`, no se menciona) | S3 | sí | documentar el comando único |
| Título del ADR enuncia el tema, no la decisión; estado «Propuesto» | S3 | sí | «Usar monolito modular», estado aceptado |
| Test sin CI ni evidencia de ejecución (verde no verificable) | S3 | sí | montar `.github/workflows/` o aportar el run |
| **15 commits tardíos** (00:06–00:58 COT del 24-ago, tras el cierre 05:00Z): borrado y recreación de documentos | S3 | sí | respetar el cierre de la actividad; lo tardío no se califica |
| Corte vertical completo (interfaz→lógica→persistencia) y su prueba llegaron el lunes 31-ago 10:00–11:24 COT, después del cierre de S4 | S4 | sí | lo tardío no se califica; sí cuenta como avance para el corte 1 |
| `__pycache__/`, `*.pyc` y archivos duplicados `« (1).py»` versionados; PDFs en la raíz | S4 | sí | limpiar con `git rm`; el `.gitignore` ya se corrigió (tardío) |
| Tabla de aspectos con columnas fuera de las 8 del curso (falta la cadena C4/ADR/código) | S4 | sí | adoptar las 8 columnas y hacer navegable la fila hasta Pruebas |
| CI sin runs verificables: la URL citada en `aspectos.md` da 404 y la API no reporta runs | S4 | sí | aportar el enlace del run o ejecutarlo en la sustentación |
| Etiqueta `corte-1` y respuesta explícita al reto | S5 | sí | falta diagnóstico, ADR, cambio y evidencia del reto asignado |
| Línea base y resultado reproducibles contra umbral | S5 | sí | la documentación reconoce que la medición P95 está pendiente |
| Registro de IA del corte | S5 | sí | último cambio del archivo fue el 24-ago |
| **El repositorio `ISCOUTB/AS_202620_Verifacts` desapareció de la organización** (404 vía API y clon; ausente de los 191 repos públicos listados de ISCOUTB) | S5 (detectado en la revisión definitiva) | sí — crítico | escalado al docente; el equipo debe restablecer el acceso público con el historial intacto antes de que se pueda calificar el corte 1 |
| Limpieza de __pycache__, archivos con sufijos '(3).py'/' (4).py' y data/verifacts.db realizada después del cierre (diff_desde_cierre 3120e06→67f8cea); el PDF en raíz persiste. | S5 | no (resuelto tarde) | — |
| SonarCloud y workflow 'Tests and SonarCloud' añadidos después del cierre (commits a1d23eb, 2a90b44, ab978d3, efbad6b), pero los runs 34407270858 y siguientes fallan. | S5 | no (resuelto tarde) | — |
| Frontend y soporte de URL incorporados después del cierre (commits 5fc30ce, 04d625d, 67f8cea), ampliando el corte vertical. | S5 | no (resuelto tarde) | — |
| Julian Samuel Cabeza Pena sigue sin commits en HEAD. | S5 | si | |
| arc42 incompleto: falta sección 11 (riesgos) y docs/c4/03-componentes.md es plantilla sin completar. | S5 | si | |
| CI en rojo: runs_ci de 'Tests and SonarCloud' posteriores al cierre concluyen failure. | S5 | si | |
| docs/aspectos.md A-02 pendiente y enlaces rotos (docs/decisiones-arquitectonicas.md). | S5 | si | |
| PDF en la raíz del repositorio persiste en HEAD. | S5 | si | |
| Fila A-02 de aspectos.md sin evidencia de prueba | S6 | si | |
| aspectos.md sin relación explícita con contextos del mapa | S6 | si | |
| Posible ADR de reajuste de límites si cambiaron | S6 | si | |
| Integrante declarado sin commits | S6 | si | |
| Evidencia de runs de CI | S6 | si | |
| Incluir a Julian Samuel Cabeza Pena en README.md y Equipo.md y evidenciar su contribución en el historial. | S5 | si | |
| Contrastar correcciones.md con los hallazgos S1-S4. | S5 | si | |
| Aportar run de CI en verde para el hash calificado. | S5 | si | |
| Cerrar A-02 con prueba de modificación de regla. | S5 | si | |
| Actualizar glosario, vista de bloques, C4 de componentes y enlaces rotos. | S5 | si | |
| Medición formal de P95 para Q-01 (docs/escenarios-de-calidad.md la declara pendiente). | S7 | si | |
| Prueba de usuario 4 de 5 para Q-04 (declarada pendiente). | S7 | si | |
| Prueba automatizada de componente para el frontend: la fila A-04 solo tiene verificación manual. | S7 | si | |
| Marcador de CI en la fila A-00 de docs/aspectos.md, que el propio documento pide reemplazar por la URL real. | S7 | si | |
| Contradicción sobre Q-03 entre docs/escenarios-de-calidad.md ('Pendiente') y docs/aspectos.md A-02 (prueba en verde). | S7 | si | |
| URL pública del análisis en SonarCloud con Quality Gate (evidencia externa); el scanner y la configuración ya se leyeron en el repositorio. | S7 | si | — |
| Filas A-04 y A-05 en docs/aspectos.md (b5d9068, 2026-09-16T00:51:03-05:00) | S6 | no (resuelto tarde) | — |
| ADR-0003 y especificación OpenAPI del API (fa29e9a y f3caf45, 2026-09-16) | S6 | no (resuelto tarde) | — |
| Pruebas de contrato de endpoints (9fdf092, 2026-09-16T00:47:30-05:00) | S6 | no (resuelto tarde) | — |
| Actualizaciones de README (8e24d72 y 635f9b7, 2026-09-16) | S6 | no (resuelto tarde) | — |
| pyyaml y jsonschema en requirements (2bf64ca, 2026-09-16) | S6 | no (resuelto tarde) | — |
| Ajustes de vistas de bloques y ejecución y de decisiones (3d07ec5, 122273b, 89b1928, 2026-09-16) | S6 | no (resuelto tarde) | — |
| Evidencia de CI con URL de run para el hash revisado | S6 | si | |
| URL pública de SonarCloud con estado del Quality Gate | S6 | si | |
| Entrada de lo rechazado con motivo técnico en docs/ia.md | S6 | si | |
| Reemplazo del marcador [PENDIENTE] en A-00 y fila propia para A-04 | S6 | si | |
| Commits del tercer integrante declarado | S6 | si | |
| Enlaces del README a documentos inexistentes | S6 | si | |
| Medición de P95 (Q-01) y prueba de usuario (Q-04) | S6 | si | |
| Comprobar URL y /health con hora y código de respuesta. | S8 | si | |
| Aportar run de CI en verde y URL pública de SonarCloud con Quality Gate. | S8 | parcial | Los runs de Tests y SonarCloud del hash actual están en verde y la URL es pública, pero el propio documento declara el Quality Gate general en rojo. |
| Actualizar arc42 §7 con una caja por pieza y su ubicación de ejecución. | S8 | no (resuelto) | La sección muestra web, API y SQLite dentro de Render, además de las piezas del CI. |
| Añadir límite de costo y restricción de tarjeta en arc42 §2. | S8 | no (resuelto) | R-TEC-05 recoge costo cero y ausencia de tarjeta. |
| Registrar un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada. | S8 | no (resuelto) | ADR 0004 decide Render y compara Terraform y AWS Lambda. |
| Asociar la métrica /metrics a un escenario de calidad y completar la medición de P95. | S8 | parcial | La métrica ya está ligada a Q-01; la medición formal del P95 sigue pendiente. |
| Cerrar los huecos de docs/aspectos.md y corregir las secciones 3 y 10 desactualizadas. | S8 | si | |
| Incluir un integrante declarado que aún no aparece en el historial. | S8 | si | |
| S9 con evidencia: ADR-0006, pruebas de frontera y de límites de módulo, mutaciones inducidas (M1–M5), medición Q-01/Q-05 y auditoría de erosión (E-1…E-5). | S9 (preliminar) | no (trabajo del periodo) | Cumple las filas 1, 3, 4, 5, 7, 8 y 9 de la ficha S9. |
| La fila A-06 de `docs/aspectos.md` enlaza un ADR con nombre inexistente (`0006-semantica-del-resultado.md`) y la auditoría desde `docs/`; la cadena se rompe en esos dos eslabones. | S9 (preliminar) | si | Corregir los enlaces. |
| `docs/adr/ADR-0006.md` rompe la convención de nombres. | S9 (preliminar) | si | Renombrar a `0006-<kebab-case>.md`. |
| `docs/ia.md` sin entrada del periodo S9; la corrección de la afirmación sobre `MLAnalyzer` que declara la auditoría no está en el repositorio. | S9 (preliminar) | si | Registrar el uso de IA del periodo. |
| Sin ADR dedicado a la no incorporación del componente generativo. | S9 (preliminar) | si | Decidirlo en un ADR. |
| Quality Gate de SonarCloud en rojo pese a los runs verdes del hash revisado. | S9 (preliminar) | si | Corregirlo. |

</details>

## Estado del contrato del repositorio

Actualización S10 del 2026-10-10; no altera la matriz congelada de S9.

| Comprobación | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Acceso público por git ls-remote y clon sin autenticación de https://github.com/ISCOUTB/AS_202620_Verifacts; rama master confirmada. [README.md:695–702](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L695-L702). |
| Estructura mínima presente | Cumple | El árbol contiene código, README.md, docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md y docs/ia.md. [docs/aspectos.md:17–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/aspectos.md#L17-L25); [docs/arc42/09-decisiones-arquitectonicas.md:12–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L12-L18); [docs/ia.md:12–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L12-L25). El renombre arc42 §8 corrige la ruta; estructura presente no equivale a coherencia/completitud de todas sus secciones. |
| Estado calificado identificable | Cumple | master · 5c643bd03f19630d6459da79fb13fb2d5f943c7b · 2026-10-07T15:32:38-05:00. Punta anterior al cierre futuro; revisión preliminar. [Commit](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/5c643bd03f19630d6459da79fb13fb2d5f943c7b). |
| Nombres de ADR según la convención | Cumple | Los siete archivos del árbol siguen NNNN-titulo-en-kebab-case.md. Renombre de ADR-0006 sin cambio de contenido y nuevo ADR-0007; índice navegable en [docs/arc42/09-decisiones-arquitectonicas.md:12–18](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L12-L18). Se cierra la desviación de nombre, no las cuestiones de inmutabilidad. |
| ADR aceptados no reescritos | No cumple | La nueva tabla reconoce adiciones previas a ADR-0001…0004 y nota a ADR-0002 ([docs/arc42/09-decisiones-arquitectonicas.md:20–27](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/arc42/09-decisiones-arquitectonicas.md#L20-L27)), pero no borra la reescritura histórica ni sustituye la regla del contrato. Además ADR-0005 ya aceptado ([docs/adr/0005-comparacion-lambda-render.md:3–5](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/adr/0005-comparacion-lambda-render.md#L3-L5)) cambia contexto, montaje y resultados en el delta actual sin nuevo ADR ni reemplazo explícito. [Diff inmutable](https://github.com/ISCOUTB/AS_202620_Verifacts/compare/4f0652291c47f5093da1230b245a980614220e80...5c643bd03f19630d6459da79fb13fb2d5f943c7b). |
| docs/ia.md al día para la semana | Cumple | Actualizado el 7-oct dentro del delta: corrige MLAnalyzer como propuesta no incorporada y registra aceptación/corrección/rechazo con motivos ([docs/ia.md:19–25](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L19-L25) y [docs/ia.md:27–46](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/ia.md#L27-L46)). Cierra la ausencia previa de registro y su falsa afirmación ML. Las entradas rotuladas S9 son corrección tardía visible hoy, no evidencia incorporada retroactivamente a S9. No se presume cobertura de interacciones no declaradas; revisar la redacción que presenta riesgo de latencia LLM como incumplimiento medido sin experimento del modelo. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824175) y [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/37682824211) success en el hash actual; scanner/configuración en [.github/workflows/sonarcloud.yml:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L38) y [sonar-project.properties:1–6](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/sonar-project.properties#L1-L6). El documento ahora declara Gate VERDE/OK y 99,1 % de cobertura con fecha 7-oct ([docs/despliegue.md:37](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/despliegue.md#L37)); se atribuye al equipo. Consulta pública del evaluador a https://sonarcloud.io/api/qualitygates/project_status?projectKey=ISCOUTB_AS_202620_Verifacts iniciada 2026-10-10T13:06:42Z: HTTP 403 en 5,059115 s; consulta a https://sonarcloud.io/api/project_analyses/search?project=ISCOUTB_AS_202620_Verifacts&ps=5 iniciada 13:06:48Z: HTTP 403 en 6,651586 s. No se pudo ligar el Gate a una revisión. Por tanto el Gate actual queda No verificado, no «rojo» ni «verde confirmado por el evaluador». El workflow ejecuta el scanner, pero no declara espera del Gate ([.github/workflows/sonarcloud.yml:26–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L26-L38); [sonar-project.properties:1–9](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/sonar-project.properties#L1-L9)). La exigencia conjunta no queda demostrada y sigue abierta; una limitación HTTP no se publica como Gate fallido. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Lectura acotada del delta y configuraciones sin credenciales visibles; referencia de CI [.github/workflows/sonarcloud.yml:34–38](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.github/workflows/sonarcloud.yml#L34-L38) y exclusiones [.gitignore:15–20](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/.gitignore#L15-L20). No hay barrido completo nuevo de árbol/historial. La afirmación del equipo en [docs/auditoria-s9.md:53–60](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/docs/auditoria-s9.md#L53-L60) no sustituye esa comprobación. Se conserva la observación anterior únicamente como histórica. |
| Contribución de todos los integrantes | No verificado | Recuento por git log del 10-oct: 304 commits, tres firmas de autor con 241, 37 y 26 commits; son firmas, no tres personas verificadas. Cuatro commits adicionales respecto de la base. [Equipo.md:3–8](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/Equipo.md#L3-L8) y [README.md:701–702](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/5c643bd03f19630d6459da79fb13fb2d5f943c7b/README.md#L701-L702) enumeran dos integrantes, frente a tres en EQUIPOS del curso. No se infieren correspondencias por nombre ni se modifica la tabla individual histórica; matrícula y vínculo cuenta/persona pendientes. Verificación adicional del 2026-10-10T13:15Z: git rev-list --count da 300 en la base 4f065229 y 304 en 5c643bd0, delta exacto 4. Incluye merges: 6 en ambos; sin merges son 294 y 298. Las firmas crudas contadas mediante git log --format=%an son 241/33/26 en la base y 241/37/26 en la punta, sin .mailmap en ninguno y sin consolidar nombres como personas. No hay aparición de nueva firma en el delta. La identificación histórica 240+31 corresponde a otro recuento antiguo; la planilla publicada ya contiene actualización agregada del 6-oct con 300 (241/33/26). No se altera la tabla individual histórica ni se atribuyen identidades por parecido. |

## Contribución por integrante

Actualización agregada del 2026-10-10: git rev-list --count sobre la base da 300 commits (294 sin merges y 6 merges) y sobre la punta actual, 304 (298 y 6). El delta es de 4 commits. git log --format=%an agrupa tres firmas con 241, 37 y 26 commits (antes 241, 33 y 26); no hay .mailmap y las firmas no se equiparan a personas. El repositorio declara dos integrantes frente a tres en el listado docente. Se conserva la identificación histórica y no se infieren nuevas correspondencias.

La tabla individual siguiente es histórica; sus cifras no son el recuento de la punta actual. No se infieren nuevas correspondencias entre cuentas y personas.

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Cristian David Cardeno Gulloso | `Cristian Cardeño` (sin atribuir por parecido de nombre) | 33 | | | Dos correos con la misma firma; correspondencia individual pendiente. |
| Pedro Jose Castro Blanquicett | sin atribuir (`PedroC1213` en el historial, dos correos consolidados) | 240 | | | — |
| Julian Samuel Cabeza Pena | sin aparición | 0 | | | — |

## Preguntas abiertas para la sustentación

Segundo corte, sobre el entorno desplegado y con el pipeline en vivo:

- ¿Cómo distinguen el tiempo de activación de Render de duration_ms del middleware, y qué ocurre con el historial SQLite después de reiniciar o redeplegar? Demuéstrenlo en el entorno desplegado.
- ¿Cómo cambiaría el punto de quiebre de costo si el POST usa realmente 10.000 caracteres y se separan invocaciones frías/calientes? ¿Qué parte de Duration medida en SAM están suponiendo facturable en AWS?
- ¿Qué resultado de una comparación controlada les haría cambiar la decisión de mantener Render, y cómo registrarían ese cambio sin reescribir el ADR-0005 aceptado?
