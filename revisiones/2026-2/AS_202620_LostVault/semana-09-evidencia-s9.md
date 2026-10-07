# Semana 9 · Generación verificada y trazable · LostVault

Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_LostVault |
| Rama remota principal | `origin/main` |
| Observación | 2026-10-06T21:31:50.350893+00:00 |
| Cierre S9 | 2026-10-05T05:00:00Z (medianoche de Colombia) |
| Estado revisado | `99fb413bda00c208ec42104dcfe6a4c189fbad77` en `origin/main` (2026-10-04T22:30:53-05:00) |
| Línea base S8 | `4a9ecc944731d0af243724b26a08d5deee22d7e3` |
| Commits del delta S8 → S9 | 10 |

## Alcance y método

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

El delta S8→S9 ya cambia backend/main.py y backend/test_api.py e incorpora auditoría, registro IA y ADR-0004. La preliminar «solo documentación de Swagger» quedó superada; el trabajo del taller se reconoce únicamente donde aporta evidencia nueva del despliegue.

## Matriz de la ficha (10 criterios)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/ia.md:181-198](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ia.md#L181-L198) acredita apoyo IA en OBJECTIVES_MS, respuesta de métricas y prueba; [backend/main.py:185-195](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L185-L195) y [backend/test_api.py:165-175](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/test_api.py#L165-L175) contienen la porción real. No se confunde con el backend anterior ni con el prototipo del taller. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos.md:9-14](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/aspectos.md#L9-L14) añade AS-04 con medición, pero código/prueba no son enlaces y falta el eslabón C4. La fila AS-03 corresponde al corte anterior, no a la porción p95 nueva. |
| ADR con la decisión argumentada por el equipo | No cumple | El ADR nuevo [docs/adr/0004-no-incorporacion-componente-generativo.md:20-40](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0004-no-incorporacion-componente-generativo.md#L20-L40) decide sobre generación, no la porción p95. [docs/adr/0003-plataforma-despliegue-vercel.md:23-30](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0003-plataforma-despliegue-vercel.md#L23-L30) distingue taller y despliegue S8; no se localizó decisión S9 argumentada para el cambio de métricas y sus límites serverless. |
| Prueba que falla ante el defecto que cubre | No verificado | [backend/test_api.py:165-175](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/test_api.py#L165-L175) comprueba valores conocidos 95.95/3000 y estado met. [docs/ia.md:194-198](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ia.md#L194-L198) explica su sensibilidad, pero no aporta run rojo, mutación ni procedimiento concreto de sustitución/defecto y resultado. Pregunta de sustentación; no se ejecutó código. |
| Medición del escenario asociado | Cumple | [docs/adr/000.3-despliegue-busqueda-lostvault.md:91-106](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/000.3-despliegue-busqueda-lostvault.md#L91-L106) documenta medición real de GET /objects con autocannon, cargas 200/20, 30 s y comparación con 2000 ms. Declara ~44 % de fallos a 200 y que el p95 exitoso no acredita disponibilidad. Cumple la evidencia de medición, no el objetivo global bajo carga; no se atribuye la causa del 403 como certeza. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | No cumple | [docs/ia.md:188-223](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ia.md#L188-L223) aporta lo aceptado y el cambio del test, pero el único rechazo S9 es posponer NC6 porque el código es de otro integrante (:216–218). No es un motivo técnico sobre una salida del modelo; falta ese rechazo técnico explícito de la porción. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | No cumple | [docs/ddd/auditoria_backend.md:46-109](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L46-L109) identifica NC6 y propone separar módulos, pero deja la corrección sin implementar; [backend/main.py:213-230](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L213-L230) sigue escribiendo estado del objeto desde reclamaciones. Se reconoce auditoría real, pero falta la corrección exigida por la ficha. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [docs/ddd/auditoria_backend.md:11-27](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L11-L27) audita tres dependencias actuales; diff de requirements de S8→S9 sin incorporaciones. Verificación independiente de nombre y versión en [FastAPI](https://pypi.org/pypi/fastapi/0.141.1/json), [Uvicorn](https://pypi.org/pypi/uvicorn/0.54.0/json) y [PyJWT](https://pypi.org/pypi/PyJWT/2.7.0/json) confirma registros y proyectos legítimos. Esto no equivale a auditoría de vulnerabilidades; PyJWT antiguo queda revisable. |
| Sin credenciales en código, ejemplos ni documentación generada | No verificado | El equipo auditó main.py/Dockerfile en [docs/ddd/auditoria_backend.md:29-44](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/ddd/auditoria_backend.md#L29-L44) y el código lee JWT_SECRET del entorno en [backend/main.py:50-55](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/backend/main.py#L50-L55). El barrido independiente completo fue cancelado por la herramienta, también en el reintento autorizado. No se atribuye exposición ni incumplimiento académico por esa limitación; falta cerrar la comprobación del revisor. El literal de CI en [.github/workflows/build.yml:55-60](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/.github/workflows/build.yml#L55-L60) está rotulado como prueba efímera y no se presenta como secreto de producción. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0004-no-incorporacion-componente-generativo.md:14-53](https://github.com/ISCOUTB/AS_202620_LostVault/blob/99fb413bda00c208ec42104dcfe6a4c189fbad77/docs/adr/0004-no-incorporacion-componente-generativo.md#L14-L53) decide no incorporar generación y compara descripción automática/búsqueda semántica con costo, latencia y alcance. |

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

## Recuento y nota sugerida

**4 de 10 criterios Cumple**,  4 No cumple y 2 No verificado. La transversal no entra en el cálculo.

**Nota propuesta pendiente de completar la comprobación bloqueada del revisor.** El recuento documental es 4/10; si las 1 comprobaciones bloqueadas resultan conformes, el intervalo resultante es 2.6–3.0. No es una nota cerrada ni se atribuye el bloqueo al equipo. La nota final la fija el docente en Moodle.

## Próximos pasos

La entrega ya incorpora métricas, prueba nueva, auditoría y una medición real del despliegue. Completen el ADR y la cadena de esa porción, muestren la prueba ante un defecto concreto y registren un rechazo técnico de la IA. NC6 sigue siendo una corrección propuesta, no implementada. La comprobación independiente de credenciales quedó pendiente por una limitación del revisor, sin atribuirla al equipo.
