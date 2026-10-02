# Planilla de equipo · Arquitecturas de Software

## Identificación

| | |
|---|---|
| Equipo | TAIA |
| Repositorio | `https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant` |
| Integrantes y su usuario de GitHub | ver [EQUIPOS.md](../../../EQUIPOS.md) y tabla de contribución abajo |
| URL del sistema desplegado | — |
| Ultima revision | 2026-10-01 |

## Estado por entrega

| Semana | Entrega | Estado revisado (etiqueta o hash) | Criterios | Sugerido | Revisada |
|---:|---|---|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `76d4a91` · 2026-08-07T03:34:26-05:00 | 6/9 | no aplica | sí |
| 2 | S2 | `59590c9` (2026-08-16T19:15:15-05:00) | 5/9 | no aplica | si |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `46257a03` · 2026-08-23T16:47:00-05:00 | 5/9 | no se publica | sí |
| 4 | S4 | `c087303` (2026-08-30T18:54:10-05:00) | 5/10 | 3.0 | si |
| 5 | CORTE1 | `a3f4d82` (2026-09-06T04:13:11-05:00) | 9/12 | no aplica | si |
| 6 | S6 | `c0c3adb` (2026-09-13T20:01:35-05:00) | 7/8 | 4.5 (prelim.) | si |
| 7 | S7 | `0a12f0c` (2026-09-17T15:27:54-05:00) | 10/10 | 5.0 | si |
| 8 | S8 | `4b07242` en `origin/main` (2026-09-27T23:03:53-05:00) | 10/10 | 5.0 (propuesta; 2 filas de despliegue diferidas) | si |
| 8 | Taller aplicado de despliegue | | | no aplica | |
| 9 | Evidencia S9 · Generación verificada y trazable | `4b07242` en `origin/main` (2026-09-27T23:03:53-05:00) | 1/10 | 1.4 (preliminar; propuesta al docente) | sí |
| 10 | Segundo corte · reto aplicado sobre el MVP | `corte-2` | | | |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | | | no aplica | |
| 12 | Evidencia S12 · Estrategia de datos y eventos | | | no aplica | |
| 12 | Taller aplicado · Mensajes y consistencia | | | no aplica | |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | | | no aplica | |
| 14 | Evidencia S14 · Medición de atributos de calidad | | | no aplica | |
| 16 | Proyecto final · integración y desafío arquitectónico | `final` | | | |
| 17 | Aplicación de cambios y cierre arquitectónico | | | | |

## Lo que se arrastra

| Hallazgo | Primera vez que se detectó | Sigue abierto | Qué se le dijo al equipo |
|---|---|---|---|
| `docs/adr/` inexistente | S1 (08-07) | No (cerrado en S3: `docs/adr/0001.md` desde 22-ago) | Crear el directorio (hecho) |
| Tensiones de calidad sin declarar en la ficha | S1 (08-07) | Sí | Enfrentar dos atributos de calidad en la ficha del problema |
| `docs/aspectos.md` con la trazabilidad en «Pendiente» y sin enlaces a los escenarios | S1 (08-07) | Sí | Ahora enlaza, pero a rutas rotas (`adr/0001-estilo-arquitectonico.md`, `ruta/al/escenario.md`): corregir en S4 |
| Documentación de calidad fuera del arc42 (`docs/calidad/`) con la sección 10 vacía | S2 (16-ago) | Sí | Mover o enlazar los escenarios y el árbol desde la sección 10 |
| Escenario 5 sin medida numérica; árbol de utilidad sin impacto/riesgo | S2 (16-08) | Sí | Completar la medida del escenario 5 y anotar impacto/riesgo en el árbol |
| C4 solo como imagen (PNG), sin verificar leyenda ni flechas | S2 (16-08) | No (cerrado en S3: `docs/c4/C4-ContextoTAIA.md` en Mermaid) | Preferir diagrama como código (hecho) |
| ADR sin nombre de convención, sin título H1 ni contexto | S3 (23-ago) | Sí | Renombrar a `0001-<kebab-case>.md`, añadir título y contexto, y corregir los enlaces rotos |
| Sin CI: no hay `.github/workflows/` y el verde de la prueba no es verificable | S3 (23-ago) | Sí | Montar workflow que corra `pytest` en cada push |
| `docs/ia.md` Entrada 03 incompleta (sin aceptado/rechazado) | S3 (23-ago) | Sí | Completar la entrada con su motivo |
| Ejecutar pytest y evidenciar run en verde | S4 | si | |
| Completar trazabilidad del ADR-0001 | S4 | si | |
| Verificar contenido de secciones arc42 3, 4, 9, 10 y 12 | S4 | si | |
| Configurar CI/SonarCloud o evidenciar plataforma alternativa | S4 | si | |
| Alinear C4 nivel 2 con el código actual | S4 | si | |
| Etiqueta corte-1 | S5 | si | No existe; solo `corrections-s4`. Se revisó el último commit admisible a3f4d82. |
| PDF de dos páginas | S5 | si | No verificable desde el repositorio; depende de Moodle. |
| Diagnóstico de la restricción con línea base medida | S5 | si | No hecho: los commits de la ventana son arc42, CI y correcciones.md sobre S1-S4, sin diagnóstico de restricción nueva. |
| ADR del reto | S5 | si | No hecho; en su lugar se editó el ADR-0001 aceptado (42c5b03), lo que incumple CONTRATO §4 (no editar ADR aceptados). |
| Implementación del cambio | S5 | si | No hecho: ningún commit de la ventana toca código de dominio. |
| Prueba en CI | S5 | si | Parcial: se configuró CI por primera vez y terminó en verde (a3f4d826), pero cubre las pruebas existentes, no un cambio del reto. |
| Medición contra umbral | S5 | si | No hecho: sin archivo de medición en el árbol. |
| Trazabilidad del reto en aspectos.md | S5 | si | No hecho: docs/aspectos.md sigue con una sola fila (A-01) sin cambios en la ventana. |
| Registro de IA del reto | S5 | si | No hecho: la entrada nueva de docs/ia.md documenta la redacción de correcciones.md sobre S1-S4, no el reto. |
| Pipeline de CI | S5 | si | Resuelto por fin: .github/workflows/ci.yml existe y corre en verde desde a3f4d826. |
| Se agregó docs/adr/0001-estilo-arquitectonico.md en 42c5b03/2026-08-30 (posterior al cierre). | S2 | no (resuelto tarde) | — |
| Se completó docs/arc42/arc42.md en 1668579/2026-09-06, removiendo la plantilla. | S2 | no (resuelto tarde) | — |
| Se pasó C4 a Mermaid/source en 9df9d2a y 0f7f4bd (2026-08-29), posterior al cierre. | S2 | no (resuelto tarde) | — |
| Se corrigieron medidas de escenario y restricciones legales en ffd4f5c/2026-08-29. | S2 | no (resuelto tarde) | — |
| Se añadió CI en .github/workflows/ci.yml en commits 2f3ca0d/bda515c/ce99b54 (2026-09-06), posterior al cierre. | S2 | no (resuelto tarde) | — |
| La corrección de estructura y arquitectura se ha hecho en commits posteriores, con lo cual la evidencia de la semana 2 no es defendible en el estado calificado. | S2 | si | |
| Revisar que doc de aspectos/apartados del contrato queden sincronizados en la rama principal para la próxima entrega. | S2 | si | |
| 3cf6bfc y 915e499 (2026-09-08) corrigen pipeline de SonarCloud tras el cierre del 2026-09-07; no forman parte del estado calificado | S5 | no (resuelto tarde) | — |
| El diff desde cierre modifica .github/workflows/ci.yml y backend/requirements.txt para blindar la instalación de dependencias | S5 | no (resuelto tarde) | — |
| Verificación del contenido de correcciones.md en estado calificado | S5 | si | |
| Evidencia del PDF u adjunto entregado en Moodle | S5 | si | |
| Sustentación del corte | S5 | si | |
| Consolidar identidades de git (val con dos correos) | S5 | si | |
| Análisis estático SonarCloud sin evidencia concreta | S5 | si | |
| 3cf6bfc y 915e499 (2026-09-08) corrigen el pipeline de CI después del cierre | S5 | no (resuelto tarde) | — |
| diff_desde_cierre muestra cambios en ci.yml, requirements.txt y correcciones.md posteriores al cierre | S5 | no (resuelto tarde) | — |
| Reestructurar correcciones.md como índice de verificación trazable | S5 | si | |
| Verificar historial del ADR | S5 | si | |
| PDF y sustentación pendientes de aula | S5 | si | |
| Verificar mapa de contextos con relaciones tipificadas | S6 | si | |
| Verificar tabla módulo-datos con dueño único | S6 | si | |
| Verificar lista de violaciones y plan de corrección | S6 | si | |
| Verificar arc42 sección 8 con lenguaje ubicuo | S6 | si | |
| Comparar límites contra hash de S5 y posible ADR de reajuste | S6 | si | |
| Cruzar aspectos con contextos del mapa | S6 | si | |
| Confirmar que ci.yml ejecuta backend/tests/test_api_contract.py y aportar la URL del run | S7 | no (verificado en la relectura) | |
| Aportar la evidencia del cambio incompatible que hace fallar la prueba (contenido o run en rojo) | S7 | no (verificado en la relectura) | |
| Publicar URL de SonarCloud con Quality Gate, línea del scanner y run exitoso | S7 | si | |
| Completar contenido verificable de docs/c4/C4-C2.md, docs/aspectos.md y docs/ia.md | S7 | no (verificado en la relectura) | |
| Registrar el historial git del contrato para sostener su versionado | S7 | no (verificado en la relectura) | |
| Comprobar que el pipeline ejecuta la prueba de contrato (contenido de ci.yml y URL del run). | S7 | no (verificado en la relectura) | |
| Aportar análisis SonarCloud público con Quality Gate para el hash revisado. | S7 | si | |
| Cotejar rutas del contrato con el código implementado. | S7 | no (verificado en la relectura) | |
| Publicar el contenido de docs/aspectos.md y docs/c4/C4-C2.md. | S7 | no (verificado en la relectura) | |
| Aportar el historial de git del archivo de contrato. | S7 | no (verificado en la relectura) | |
| 2837b47 2026-09-15T20:43:43-05:00 feat(api): add OpenAPI contract and contract tests (posterior al cierre). | S6 | no (resuelto tarde) | — |
| 5a4e8dc 2026-09-15T20:48:07-05:00 Merge pull request #13 (posterior al cierre). | S6 | no (resuelto tarde) | — |
| 7b32b3f 2026-09-16T20:31:46-05:00 docs: completa evidencia de contrato y CI (posterior al cierre). | S6 | no (resuelto tarde) | — |
| 3c2ae72 2026-09-16T21:40:14-05:00 Merge pull request #15 (posterior al cierre). | S6 | no (resuelto tarde) | — |
| 0a12f0c 2026-09-17T15:27:54-05:00 docs: adding evidence week 7 (posterior al cierre). | S6 | no (resuelto tarde) | — |
| ADR del reajuste de fronteras entre contextos y, si aplica, C4 nivel 3 actualizado en el mismo cambio. | S6 | si | |
| Evidencia auditable de CI y SonarCloud: configuración del scanner, run del hash revisado y Quality Gate público. | S6 | si | |
| Columnas completas y navegables en docs/aspectos.md y columna de lo rechazado en docs/ia.md. | S6 | si | |
| Persistencia PostgreSQL aún no integrada; los repositorios siguen en memoria. | S6 | si | |
| Ejecucion de la prueba de contrato en el pipeline y URL del run | S7 | no (verificado en la relectura) | |
| Evidencia verificable de fallo ante cambio incompatible | S7 | no (verificado en la relectura) | |
| C4 nivel 2 con protocolo y formato en cada flecha | S7 | no (verificado en la relectura) | |
| Historial git del archivo de contrato | S7 | no (verificado en la relectura) | |
| SonarCloud: configuracion, run exitoso y URL publica con Quality Gate | S7 | si | |
| Contenido de docs/aspectos.md para validar la tabla de trazabilidad | S7 | no (verificado en la relectura) | |
| Publicar el sistema en una URL accesible desde fuera de la red de la universidad y registrar hora y código de respuesta. | S8 | si | |
| Versionar infraestructura como código para recrear el entorno con un solo comando. | S8 | si | |
| Dejar el pipeline en verde y aportar la URL del run con su conclusión. | S8 | si | |
| Añadir logs estructurados y una métrica consultable asociada a un escenario de calidad. | S8 | si | |
| Documentar la estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita. | S8 | si | |
| Escribir un ADR por decisión de plataforma con alternativa descartada y capa gratuita verificada. | S8 | si | |
| Declarar variables de entorno en .env.example y tomar sus valores del almacén del proveedor. | S8 | si | |
| Aportar el contenido de docs/aspectos.md y docs/ia.md para verificar su trazabilidad. | S8 | si | |
| URL y health check diferidos: la URL se entrega por Moodle y no se probó; el repo declara `http://157.137.215.57:8000` y `/health` (`backend/app/main.py:48`). | S8 (definitiva) | si | Pendiente solo de entregar la URL en Moodle. |
| `.env.example` inexistente: `.gitignore` lo excluye y README.md:105 y arc42 §7.3 lo citan (enlace roto). | S8 (definitiva) | si | Versionar un `.env.example` sin valores reales. |
| ADR-0001 aceptado reescrito en `4dd3925` (2026-08-29) y `42c5b03` (2026-09-06) sin ADR sucesor. | S8 (definitiva) | si | No editar ADR aceptados; si cambia la decisión, crear uno nuevo y marcar el anterior como reemplazado. |
| `docs/ia.md` sin commits en la ventana S8 (último `7b32b3f`, 2026-09-16). | S8 (definitiva) | si | Registrar el uso de IA del periodo. |
| Sin SonarCloud: ni configuración, ni run del scanner, ni URL pública con Quality Gate. | S8 (definitiva) | si | Añadir el análisis estático auditable (CONTRATO §8). |
| Periodo S9 vacío: la punta `4b07242` (2026-09-27) coincide con el hash calificado de S8; no hay porción nueva. | S9 (preliminar) | si | Empujar la porción construida con IA y su cadena antes del cierre del 2026-10-05. |
| Cadena de aspectos, prueba que falla, medición, auditoría de erosión y dependencias del periodo: sin artefacto S9. | S9 (preliminar) | si | Aplicado CONTRATO §12: la evidencia previa es línea base y no se recalifica. |
| Componente generativo (Gemini) sin conjunto de evaluación, costo por operación ni latencia del periodo. | S9 (preliminar) | si | Evaluar el componente o registrar el ADR de su no incorporación. |
## Estado del contrato del repositorio

| Comprobación | Estado | Observaciones |
|---|---|---|
| Nombre y visibilidad del repositorio | Cumple | Clon anónimo OK en S9 (`4b07242`, misma punta que S8) |
| Estructura mínima | Cumple | Las seis rutas presentes en `4b07242` |
| Convención de nombres de ADR | Cumple | `docs/adr/0001`–`0004` en kebab-case; filtro de §4 sin residuos |
| ADR aceptados sin reescribir | No cumple | ADR-0001 aceptado y editado en `4dd3925` (2026-08-29) y `42c5b03` (2026-09-06) sin ADR sucesor |
| `docs/ia.md` al día | No cumple | Sin commits en la ventana S8; último sobre el archivo `7b32b3f` (2026-09-16) |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 limpio sobre `4b07242`; sin `.env` versionado; pickaxe coincide solo con la regex documentada en `correcciones.md` |
| Contribución de todos los integrantes | Cumple | 4 identidades consolidadas = 4 integrantes (val 42, dei0811 31, Luis Mendoza/luis20072002 28, mark 3) |
| Pipeline en verde | Cumple | Run CI `36376147005` y CD `36376186792` success sobre `4b07242` en `main` (2026-09-28T04:04Z) |
| SonarCloud y Quality Gate públicos | No cumple | Sin `sonar-project.properties`, sin scanner en el workflow y sin URL pública con Quality Gate |
| Etiqueta corte-1 (corte 1) | No cumple | No existe; solo `corrections-s4` |
| ADR aceptados sin reescribir (corte 1) | No cumple | El commit `42c5b03` edita el ADR-0001 aceptado en vez de crear uno nuevo o marcarlo reemplazado |

## Contribución por integrante

| Integrante | Usuario de GitHub | Commits | PR abiertos | Revisiones con comentarios de fondo | Observaciones |
|---|---|---:|---:|---:|---|
| Valeria Estefania Berrio Payares | val (2 identidades: `@email.com` y `@gmail.com`) | 8 (6+2, consolidadas) | | | Skeleton, arc42 §4 y ADR (22-ago) |
| Deiner De Jesus Gonzalez Paredes | dei0811 | 4 | | | C4 (16-ago), ia.md y README (23-ago) |
| Luis Eduardo Mendoza Angulo | luis20072002 | 1 | | | arc42 (15-ago) |
| Mark Steven Pastrana Koreia | mark | 1 | | | Escenarios (16-ago); «EtienneGW» del listado no aparece en el historial — correspondencia por confirmar |

## Preguntas abiertas para la sustentación

- ¿La cuenta «mark» es la misma persona que «EtienneGW» del listado de EQUIPOS.md?
- ¿El arranque real (`.\run.bat`) y la prueba (`pytest backend/tests`) pasan en el entorno del equipo? (no ejecutado por regla del kit)
