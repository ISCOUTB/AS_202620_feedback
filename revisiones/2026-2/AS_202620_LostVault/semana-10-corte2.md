# Semana 10 · Segundo corte · LostVault

**Revisión preliminar.** Cierre previsto: 2026-10-12T05:00:00Z (medianoche de Colombia). El estado puede cambiar antes del cierre y debe volver a congelarse entonces.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LostVault |
| Estado revisado | `99fb413bda00c208ec42104dcfe6a4c189fbad77` en `origin/main` (2026-10-04T22:30:53-05:00) |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.350893+00:00 |
| Punta revisada para S10 | `99fb413bda00c208ec42104dcfe6a4c189fbad77` (2026-10-04T22:30:53-05:00) |
| S9 congelado, solo como línea base | `99fb413bda00c208ec42104dcfe6a4c189fbad77` |

## Alcance y escenario operativo asignado

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

**Escenario asignado: No verificado.** Se encontró «condición operativa asignada» para el Escenario 4 en un documento comparativo del taller. ADR-0003 declara expresamente que ese taller es una entrega separada. No prueba cuál es la asignación S10 del equipo. Fuente o búsqueda: [docs/adr/000.3-despliegue-busqueda-lostvault.md:14-22](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L14-L22) y [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30). La evidencia de S6–S9 se usa como base; no se vuelve a calificar por existir. La evolución se contrastó con el hash S5 publicado `c0c17c1e9c3387ac915767cd706e8b785a3deadf`: el delta hasta esta punta modifica 43 archivos; los cambios pertinentes se enlazan en las filas de decisión, implementación y arquitectura. No se recalifica S5 ni se usan sus referencias históricas a etiquetas como requisito vigente.

## Matriz técnica preliminar

La fila «PDF de dos páginas» se omite por exclusión docente; quedan **12 filas**, incluida la sustentación pendiente.

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Estado de S10 identificable y anterior al cierre | Cumple | Punta main 99fb413bda00c208ec42104dcfe6a4c189fbad77; fecha anterior al cierre futuro, revisión preliminar. |
| Despliegue accesible en el momento de la revisión | Cumple | GET https://backend-nu-self-91.vercel.app/health: HTTP 200 en 6.124 s; inicio 2026-10-06T21:23:22Z. URL en [docs/arc42/07_vista_despliegue.md:11-18](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L11-L18). No se probó el flujo de reclamación ni se repitió carga. |
| Hipótesis, montaje, variables y umbral declarados | No verificado | Se encontró «condición operativa asignada» para el Escenario 4 en un documento comparativo del taller. ADR-0003 declara expresamente que ese taller es una entrega separada. No prueba cuál es la asignación S10 del equipo. [docs/adr/000.3-despliegue-busqueda-lostvault.md:14-22](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L14-L22) y [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30) |
| Línea base medida y reproducible | No verificado | [docs/adr/000.3-despliegue-busqueda-lostvault.md:91-106](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L91-L106) documenta dos cargas de Vercel, pero no una línea base/intervención del reto S10 confirmado; comparación local/serverless es taller. |
| Decisión registrada en ADR, coherente con dominio, contratos, despliegue y costo | No verificado | [docs/adr/0003-plataforma-despliegue-vercel.md:32-76](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L32-L76) justifica plataforma S8; falta decisión de respuesta al reto asignado actual. |
| Respuesta implementada o configurada sobre el MVP | No verificado | [backend/main.py:185-210](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L185-L210) añade señales reales, pero no se presume respuesta a S10 sin asignación confirmada. |
| Resultado contrastado con el umbral | No verificado | [docs/adr/000.3-despliegue-busqueda-lostvault.md:95-100](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L95-L100) revela degradación bajo 200 conexiones; no se debe presentar p95 de peticiones exitosas como cumplimiento íntegro. Falta experimento de respuesta S10. |
| Pipeline, health check, logs estructurados y métrica ligada al escenario | No verificado | Hay JSON y request_id en [backend/main.py:107-133](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L107-L133) y health público; [docs/arc42/07_vista_despliegue.md:30-65](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L30-L65) declara que p95 en memoria no acumula entre instancias. Run actual, secretos y observación del reto pendientes; la degradación ya medida exige resolver una métrica agregada. |
| Secretos protegidos | No verificado | El equipo auditó main.py/Dockerfile en [docs/ddd/auditoria_backend.md:29-44](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L29-L44) y el código lee JWT_SECRET del entorno en [backend/main.py:50-55](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L50-L55). El barrido independiente completo fue cancelado por la herramienta, también en el reintento autorizado. No se atribuye exposición ni incumplimiento académico por esa limitación; falta cerrar la comprobación del revisor. El literal de CI en [.github/workflows/build.yml:55-60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L55-L60) está rotulado como prueba efímera y no se presenta como secreto de producción. |
| C4, arc42, ADR y contratos correspondientes al MVP | No cumple | [docs/ddd/auditoria_backend.md:58-92](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L58-L92) documenta arquitectura Python divergente del ADR modular; [docs/arc42/07_vista_despliegue.md:67-75](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/arc42/07_vista_despliegue.md#L67-L75) cita backend/vercel.json inexistente en el árbol. La documentación debe distinguir IaC real, prototipo y código desplegado. |
| Decisión anterior confirmada o reemplazada con evidencia | No verificado | [docs/adr/000.3-despliegue-busqueda-lostvault.md:100](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L100) contradice expectativa de escalado, pero no hay ADR que confirme/reemplace la decisión a partir de un reto S10 identificado. |
| Sustentación del reto sobre el entorno desplegado | No verificado | Sustentación y pipeline en vivo pendientes de docente. |

Recuento descriptivo: 2 Cumple, 1 No cumple y 9 No verificado, sobre 12 filas. **No se transforma este recuento en nota.**

## Rúbrica del segundo corte (cinco criterios)

Escala del aula: 0,00 / 0,60 / 0,80 / 1,00 por criterio. Niveles exclusivamente propuestos al docente.

| Criterio | Nivel sugerido | Puntaje | Evidencia / límite |
|---|---|---:|---|
| Caracterización del escenario operativo | No verificado | Pendiente | Asignación S10 no confirmada; la condición del taller no se da por esa asignación. |
| Decisión e implementación | No verificado | Pendiente | Plataforma S8 documentada, nueva decisión ligada al reto pendiente. |
| Operación, seguridad y observabilidad | No verificado | Pendiente | Health y correlación presentes; métricas no agregadas, degradación medida y barrido independiente pendiente. |
| Evolución arquitectónica trazable | No verificado | Pendiente | NC6 y referencias de IaC muestran desalineación; falta decisión a partir del experimento S10. |
| Sustentación del reto | Pendiente de sustentación | Pendiente | La fija el docente en sesión. |

**Total final no determinado.** No se aplica la fórmula semanal. La sustentación corresponde al docente, sobre el entorno desplegado y con el pipeline en vivo; los criterios sin escenario confirmado no reciben un cero por esa falta de verificación.

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_LostVault; [README.md:1-9](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L1-L9). |
| Estructura mínima presente | Cumple | Árbol Git contiene las seis rutas mínimas; índice [README.md:207-224](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/README.md#L207-L224). |
| Estado calificado identificable | Cumple | origin/main 99fb413bda00c208ec42104dcfe6a4c189fbad77; último commit anterior al cierre en cabecera. |
| Nombres de ADR según la convención | No cumple | [docs/adr/000.3-despliegue-busqueda-lostvault.md:1-4](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L1-L4) usa 000.3, fuera de convención; [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30) reconoce el typo y que es un taller distinto. |
| ADR aceptados no reescritos | No cumple | Historial verificado de ADR-0001/0002: [edd78d72](https://github.com/ISCOUTB/AS_202620_LostVault/commit/edd78d72afe70c55ca77e37b909f2ab8ab442834) y [b5615768](https://github.com/ISCOUTB/AS_202620_LostVault/commit/b5615768472c8c64dc3abff3dbf701faa40c2420) modifican decisiones aceptadas; no se localizó reemplazo declarado que resuelva el arrastre. |
| docs/ia.md al día para la semana | No cumple | [docs/ia.md:181-223](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ia.md#L181-L223) está al día temporalmente, pero falta rechazo con motivo técnico de S9; la razón de propiedad individual no satisface esa parte. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No verificado | [.github/workflows/build.yml:62-76](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L62-L76) tiene scanner y Quality Gate; configuración versionada sonar-project.properties. Única consulta PR del hash devolvió cero runs, sin demostrar inexistencia de runs push. No se verificó run/Quality Gate público de este hash y no se recicla el verde S8. |
| Sin credenciales en el repositorio ni en el historial | No verificado | El equipo auditó main.py/Dockerfile en [docs/ddd/auditoria_backend.md:29-44](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L29-L44) y el código lee JWT_SECRET del entorno en [backend/main.py:50-55](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L50-L55). El barrido independiente completo fue cancelado por la herramienta, también en el reintento autorizado. No se atribuye exposición ni incumplimiento académico por esa limitación; falta cerrar la comprobación del revisor. El literal de CI en [.github/workflows/build.yml:55-60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L55-L60) está rotulado como prueba efímera y no se presenta como secreto de producción. |
| Contribución de todos los integrantes | No verificado | La planilla anterior deja asociaciones de varias cuentas por confirmar. No se asignan personas por semejanza ni se repiten conteos antiguos como estado vigente; pendiente validación docente de autoría. |

## Estado global del proyecto (overall)

Punta observada de `origin/main`: `99fb413bda00c208ec42104dcfe6a4c189fbad77` (2026-10-04T22:30:53-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9. Health responde. El equipo documentó un resultado importante: con 200 conexiones ~44 % de fallos, aunque el p95 de respuestas exitosas era bajo. No debe ocultarse al defender disponibilidad. NC6 y persistencia/métricas en memoria siguen abiertas.

- Completar cadena navegable de AS-04 con C4, código, prueba y medición.
- Formalizar la decisión de la porción p95; demostrar la prueba ante defecto concreto y registrar rechazo técnico de IA.
- Corregir NC6 o justificar una arquitectura actual que preserve dueño único, con prueba que la proteja.
- Agregación de métricas/persistencia en despliegue serverless y tratamiento del fallo con 200 conexiones.
- Eliminar referencias a IaC inexistente, ordenar ADR y aportar run/Quality Gate actual.
- Asignación S10, autoría y barrido independiente de secretos pendientes.

### Hallazgos anteriores cerrados o delimitados

- Se cierra la ausencia preliminar de porción S9: métrica con objective_ms/met y test nuevos.
- Registro IA S9 y auditoría NC6 existen, aunque no completan todos sus criterios.
- ADR-0004 formaliza no generación.
- Existe medición del despliegue real con umbral y fallos declarados; health accesible hoy.

## Preparación de la sustentación

1. Fallo: ¿cómo evitarán dos reclamaciones inconsistentes o pérdida de datos cuando Vercel atienda solicitudes en instancias distintas?
2. Costo: ¿cuánto cuestan persistencia y métricas compartidas para sostener 200 conexiones, frente al plan gratuito actual?
3. Medición: con ~44 % de fallos bajo la carga prevista, ¿qué decisión de plataforma o control de carga cambiarían y qué resultado demostraría la mejora?

## Próximos pasos

La sonda de salud responde, pero el experimento documenta fallos importantes con 200 conexiones: el p95 de respuestas exitosas no demuestra disponibilidad. Identifiquen el reto asignado, resuelvan persistencia y agregación de métricas entre instancias y documenten qué decisión cambia a la luz de los fallos medidos.
