# Semana 9 · Generación verificada y trazable · PideUtb

Revisión definitiva actualizada tras el cierre. Propuesta al docente; la nota final se fija en Moodle.

| Campo | Valor |
|---|---|
| Repositorio | https://github.com/ISCOUTB/AS_202620_PideUtb |
| Rama remota principal | `origin/master` |
| Observación | 2026-10-06T21:31:50.478484+00:00 |
| Cierre S9 | 2026-10-05T05:00:00Z (medianoche de Colombia) |
| Estado revisado | `7e973faf7047e40137762befbc019f4736a813e6` en `origin/master` (2026-10-04T12:47:55-05:00) |
| Línea base S8 | `a94bf4e87f84291edc11beed62df0c9d8cf57db7` |
| Commits del delta S8 → S9 | 19 |

## Alcance y método

Revisión estática de repositorio público mediante Git. No se ejecutó código, pruebas, contenedores, despliegues ni workflows de estudiantes. Los procedimientos y resultados documentados se distinguen de una ejecución independiente. No se consultaron etiquetas. Los PDF quedan excluidos por instrucción docente: no se leyeron y su ausencia no se penaliza. Una lectura HTTP de salud no prueba el flujo principal ni acredita por sí sola la revisión desplegada.

El delta temporal S8→S9 incorpora el panel y la migración PostgreSQL que el equipo llama cierre de S8; la auditoría S9 añade corrección de secreto, modularidad, cobertura y ADR-0005/0006. El alcance y fecha se determinan por Git, no por el nombre que el documento da a la semana.

## Matriz de la ficha (10 criterios)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | [docs/evidencia-s9.md:11-26](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L11-L26) y [docs/ia.md:259-278](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/ia.md#L259-L278) acreditan construcción/validación asistida; panel, transiciones y pruebas ingresan después del baseline S8, aunque el equipo los denomina cierre de S8. [backend/app/pedidos/service.py:200-226](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pedidos/service.py#L200-L226) implementa el flujo y sus exclusiones; no se recalifica código que ya estuviera en la base. |
| Cadena completa navegable para esa porción | No cumple | [docs/aspectos.md:15-30](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/aspectos.md#L15-L30) tiene ocho columnas distintas a las del contrato: falta Evidencia; código y pruebas son texto no navegable. ESC-03 apunta a ADR-0002, no al ADR-0005 del panel, y el cierre conserva «S7/panel pendiente». El dossier S9 permite reconstruir la cadena, pero la fila no la ofrece completa. |
| ADR con la decisión argumentada por el equipo | Cumple | [docs/adr/0005-maquina-de-estados-del-mostrador.md:9-72](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L9-L72) argumenta máquina de estados/exclusión del pago frente a condicionales o permitir/auditar; [docs/adr/0005-maquina-de-estados-del-mostrador.md:104-127](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L104-L127) reconoce falta de autenticación y límites. |
| Prueba que falla ante el defecto que cubre | Cumple | [docs/evidencia-s9.md:43-55](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L43-L55) documenta introducir el estado prohibido y comprobar rechazo/estado intacto; [backend/tests/test_panel_mostrador.py:217-236](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/tests/test_panel_mostrador.py#L217-L236) contrasta enum y estados alcanzables. Además [docs/adr/0005-maquina-de-estados-del-mostrador.md:89-102](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L89-L102) documenta defecto contractual que originó separación del enum. Procedimiento documental aceptado, sin ejecutar pruebas. |
| Medición del escenario asociado | Cumple | [docs/evidencia-s9.md:57-78](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L57-L78) presenta tres pedidos, tres interacciones, 0.20 s y sin recarga frente a umbral 10 s/3 interacciones. Medición de la porción local con clics programáticos, declarada como tal: no demuestra tiempo humano, red ni cumplimiento total del escenario en producción; no se infiere ese margen. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | [docs/ia.md:294-319](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/ia.md#L294-L319) diferencia aceptado, correcciones y rechazos con motivos de contrato, seguridad y calidad de evidencia. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | [docs/evidencia-s9.md:82-139](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L82-L139) identifica salud→repositorio y punto ciego transversal, corrige ambos y documenta dos fallos al reintroducir defecto. [backend/app/salud.py:35-43](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/salud.py#L35-L43) consume servicio; [backend/tests/test_modularidad.py:25-48](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/tests/test_modularidad.py#L25-L48) incluye transversales y [backend/tests/test_modularidad.py:98-113](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/tests/test_modularidad.py#L98-L113) acota excepción de composition root. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | [backend/requirements.in:17-28](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/requirements.in#L17-L28) incorpora psycopg[binary,pool] en el delta; [docs/evidencia-s9.md:143-179](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L143-L179) contrasta nombres/repos oficiales. Consultados [psycopg](https://pypi.org/pypi/psycopg/json), [psycopg-binary](https://pypi.org/pypi/psycopg-binary/json) y [psycopg-pool](https://pypi.org/pypi/psycopg-pool/json); son distribuciones legítimas del adaptador/pool PostgreSQL. No se ejecutó instalación. |
| Sin credenciales en código, ejemplos ni documentación generada | No cumple | Incidente documentado por el equipo en [docs/evidencia-s9.md:196-215](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L196-L215): un valor por defecto publicado se utilizaba para firmas de pago por falta de variable en el despliegue. El valor histórico sigue escrito en documentación/comentario del archivo backend/app/pagos/service.py (sin reproducirlo aquí). [backend/app/pagos/service.py:69-114](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pagos/service.py#L69-L114) ya falla cerrado al faltar secreto. No se verificó rotación/configuración productiva ni que el despliegue ejecute la corrección. Retirar referencias al valor, rotarlo en los destinos donde se usó y acreditar configuración/despliegue seguro. Esto no afirma que sea explotable actualmente ni se probó pago alguno. La decisión se apoya en esta evidencia independiente leída, no en el barrido general que la herramienta no permitió completar. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | [docs/adr/0006-componente-generativo.md:113-167](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0006-componente-generativo.md#L113-L167) decide no incorporar por alternativa determinista, costo y fallo externo. El cálculo de costo/latencia es estimación del equipo, no benchmark de un proveedor ni resultados de un componente en ejecución. |

## Matriz transversal (CONTRATO §11)

| Criterio de evaluación | Estado | Evidencia técnica y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público anónimo de https://github.com/ISCOUTB/AS_202620_PideUtb; [README.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/README.md#L1-L5). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes; [docs/aspectos.md:8-13](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/aspectos.md#L8-L13) enlaza arc42, ADR, C4 e IA existente en el árbol. |
| Estado calificado identificable | Cumple | origin/master 7e973faf7047e40137762befbc019f4736a813e6; último commit anterior al cierre, fecha en cabecera. |
| Nombres de ADR según la convención | Cumple | Lista docs/adr 0001–0006 conforme a NNNN-titulo-en-kebab-case; [docs/adr/0005-maquina-de-estados-del-mostrador.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0005-maquina-de-estados-del-mostrador.md#L1-L5) y [docs/adr/0006-componente-generativo.md:1-5](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0006-componente-generativo.md#L1-L5). |
| ADR aceptados no reescritos | No cumple | [docs/adr/0001-estilo-arquitectonico.md:5-19](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0001-estilo-arquitectonico.md#L5-L19) y [docs/adr/0002-propiedad-datos-establecimiento.md:5-23](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/adr/0002-propiedad-datos-establecimiento.md#L5-L23) ahora explican reescrituras de título; el historial también conserva edición [1b4f0f64](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/1b4f0f64bdb9e51f7e3ded11b7ec336e9a30240d). Reconocimiento histórico útil, pero no reemplazo formal ni ausencia de reescritura. |
| docs/ia.md al día para la semana | Cumple | [docs/ia.md:259-319](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/ia.md#L259-L319) incorpora S9 con criterio técnico. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | [.github/workflows/ci.yml:226-277](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L226-L277) omite scanner/gate sin token; [docs/evidencia-s9.md:255-290](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L255-L290) declara que cobertura no ingresa al Quality Gate. Cobertura mínima 85 % sí se agregó al job de pruebas, [.github/workflows/ci.yml:109-128](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/.github/workflows/ci.yml#L109-L128). Única consulta PR del hash vacía; no se confunde éxito global con scanner ejecutado. |
| Sin credenciales en el repositorio ni en el historial | No cumple | Incidente documentado por el equipo en [docs/evidencia-s9.md:196-215](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/docs/evidencia-s9.md#L196-L215): un valor por defecto publicado se utilizaba para firmas de pago por falta de variable en el despliegue. El valor histórico sigue escrito en documentación/comentario del archivo backend/app/pagos/service.py (sin reproducirlo aquí). [backend/app/pagos/service.py:69-114](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/7e973faf7047e40137762befbc019f4736a813e6/backend/app/pagos/service.py#L69-L114) ya falla cerrado al faltar secreto. No se verificó rotación/configuración productiva ni que el despliegue ejecute la corrección. Retirar referencias al valor, rotarlo en los destinos donde se usó y acreditar configuración/despliegue seguro. Esto no afirma que sea explotable actualmente ni se probó pago alguno. El incidente histórico se conserva como no conformidad aunque se haya retirado el fallback ejecutable; barrido general pendiente no lo invalida. |
| Contribución de todos los integrantes | No verificado | Historial con firmas múltiples y archivo .mailmap; solo se consolidan identidades cuando la correspondencia está acreditada. La contribución por los tres integrantes debe confirmarse sin inferir personas de nombres/cuentas ni publicar correos. |

## Estado global del proyecto (overall)

Punta observada de `origin/master`: `7e973faf7047e40137762befbc019f4736a813e6` (2026-10-04T12:47:55-05:00). Hay 0 commits posteriores al estado congelado S9. Punta igual al cierre S9. La auditoría encontró un incidente de secreto real y el código ahora falla en cerrado; falta evidencia de rotación y despliegue seguro, sin afirmar explotación vigente. La cobertura tiene umbral en CI, pero sigue fuera de SonarCloud. El panel continúa sin autenticar, declarado y no oculto.

- Rotar/configurar de forma segura el secreto de la pasarela y acreditar que el despliegue usa el fail-closed; retirar el valor histórico de ejemplos/comentarios sin reproducirlo.
- Resolver autenticación/roles del panel y verificación del canje; la máquina de estados no autoriza al establecimiento.
- Completar fila ESC-03 con ADR-0005, código, prueba y medición navegables; reconciliar C4 con autenticación futura.
- Integrar cobertura/Quality Gate en Sonar y aportar run del hash actual.
- Confirmar escenario operativo S10, disponibilidad actual y atribución de contribuciones.

### Hallazgos anteriores cerrados o delimitados

- El fallback ejecutable del secreto se retiró y falta de configuración rechaza firma; solo cierre de código, no de rotación/producción.
- La auditoría de modularidad ya cubre archivos transversales; salud consume servicio, no repositorio ajeno.
- Ya existe ADR del panel y de no incorporación generativa.
- La cobertura se mide con umbral 85 % en el job de pruebas; se retiró la insignia que anunciaba una medida inexistente.
- La migración PostgreSQL y el panel antes tardíos están dentro de este delta; no se altera retrospectivamente S8.

## Recuento y nota sugerida

**8 de 10 criterios Cumple**,  2 No cumple y 0 No verificado. La transversal no entra en el cálculo.

**Nota sugerida definitiva: 4.2 = 1 + 4 × (8/10). Propuesta al docente; la nota final se fija en Moodle.**

## Próximos pasos

La auditoría detectó problemas reales y el código ya rechaza firmas cuando falta el secreto de la pasarela. Completen la rotación y configuración segura y acrediten el despliegue de la corrección, sin publicar valores. Enlacen el ADR del panel y la medición desde ESC-03; mantengan separado el tiempo programático local del flujo completo con una persona y red.
