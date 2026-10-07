# Evidencia S9 definitiva · EnAgenda

Revisión actualizada tras el cierre del **2026-10-05T05:00:00Z** (domingo a medianoche COT).

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_EnAgenda](https://github.com/ISCOUTB/AS_202620_EnAgenda) |
| Rama remota principal | `master` |
| Base S5 del segundo corte | `696882ecb889c01bdc93170556c90044acf4fcff` |
| Base S8 | `2c7d77a421ab95b89dd68d696d49277e9f36a45c` |
| Estado revisado | `5aa889370dcf342ba06666893b97f8065b513de9` en `origin/master` (2026-10-04T23:46:49-05:00) |
| S9 congelada | `5aa889370dcf342ba06666893b97f8065b513de9` · 2026-10-04T23:46:49-05:00 |
| Punta actual / S10 preliminar | `c2077ac55a29562adc728734ca4c283ccb40f310` · 2026-10-05T10:40:19-05:00 |
| Comprobación | 2026-10-06T21:29:42Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Matriz S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | Nueva creación múltiple de invitaciones, fecha común, UI y pruebas con IA explícita; [docs/ia.md:44–66](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/ia.md#L44-L66), [app/web.py:120–225](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/app/web.py#L120-L225), [tests/test_api_invitaciones.py:16–42](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/tests/test_api_invitaciones.py#L16-L42). Hay delta real S9. Límite: invitados.html aún no estaba en el árbol congelado aunque la ruta lo requería. |
| Cadena completa navegable para esa porción | No cumple | A-01 enlaza artefactos reales, pero no llega a medición contra umbral ni ADR de las decisiones nuevas de creación múltiple; [docs/aspectos.md:3–5](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/aspectos.md#L3-L5), [docs/despliegue/medicion-dokploy.md:9–25](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/despliegue/medicion-dokploy.md#L9-L25). El enlace a evidencia documenta Docker/pruebas, no resultado del escenario. |
| ADR con la decisión argumentada por el equipo | No cumple | ADR-0003 nuevo justifica plataforma, pero la porción IA de invitaciones múltiples se remite a ADR-0001, que aún prescribe Next.js/Server Actions y ausencia de API pública. No hay decisión coherente trazada de esa porción; [docs/adr/0001-usar-monolito-modular.md:108–125](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0001-usar-monolito-modular.md#L108-L125), [docs/aspectos.md:5–5](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/aspectos.md#L5-L5). |
| Prueba que falla ante el defecto que cubre | No verificado | Se documentan 14 passed y adaptación de pruebas, sin run rojo, mutación o procedimiento que introduzca el defecto y muestre el fallo; [docs/ia.md:86–98](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/ia.md#L86-L98), [docs/evidencia.md:116–125](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/evidencia.md#L116-L125). La prueba de creación llama directamente /crear-invitaciones y no cubre la plantilla intermedia faltante. |
| Medición del escenario asociado | No cumple | Medición externa expresamente pendiente, escenario EC-XX y umbral [umbral aprobado]; [docs/despliegue/medicion-dokploy.md:3–25](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/despliegue/medicion-dokploy.md#L3-L25). Contar solicitudes no prueba latencia ni disponibilidad contra umbral. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | Registro específico nuevo con aceptado/corregido/rechazado y motivos: eliminar invitado automático, fecha global, controles horarios e integración manual; [docs/ia.md:44–98](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/ia.md#L44-L98). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | No cumple | No hay auditoría del cambio nuevo contra límites y propiedad de datos. El registro describe merge, no hallazgos arquitectónicos localizados; [docs/ia.md:68–88](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/ia.md#L68-L88). La auditoría de contextos previa no se recalifica por existir. |
| Dependencias propuestas verificadas en su registro oficial | No verificado | requerimiento.txt no cambió S8→S9. No se castiga que no se agreguen paquetes, pero no se encontró inventario explícito de propuestas/dependencias auditadas ni verificación oficial del alcance de esta generación; [docs/ia.md:44–98](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/ia.md#L44-L98). |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido del snapshot sin credenciales reales en código, ejemplos ni docs. Tokens se generan en ejecución y las claves de CI son valores de prueba; [src/invitaciones/dominio/invitaciones.py:23–29](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/src/invitaciones/dominio/invitaciones.py#L23-L29), [.github/workflows/ci.yml:32–41](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/.github/workflows/ci.yml#L32-L41). Riesgo de fuga por métricas se trata separadamente en overall. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | No cumple | El árbol solo contiene ADR-0001/0002/0003 de estilo, integración y despliegue, sin componente generativo evaluado ni decisión explícita de no incorporarlo; [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–18](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L18). |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clon público en organización ISCOUTB y nombre conforme; master declarado remoto, [README.md:1–8](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/README.md#L1-L8). |
| Estructura mínima presente | Cumple | Seis rutas mínimas presentes; se recupera tabla de aspectos con encabezado y la infraestructura ya no tiene conflictos de merge. [docs/aspectos.md:1–5](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/aspectos.md#L1-L5). |
| Estado calificado identificable | Cumple | Hash S9 congelado por fecha, indicado en encabezado. Runs exactos consultados fueron ejecutados después del cierre y solo corroboran ese código, no su despliegue antes del cierre. |
| Nombres de ADR según la convención | Cumple | ADR 0001–0003 usan convención de nombres; [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–4](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L4). |
| ADR aceptados no reescritos | No cumple | El ADR-0003 aceptado de Render en S8 fue eliminado y sustituido por otro 0003 de Dokploy sin preservar la decisión ni declarar nuevo ADR supersedes. [docs/adr/0003-desplegar-api-flask-en-dokploy.md:1–18](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/adr/0003-desplegar-api-flask-en-dokploy.md#L1-L18). Se verificó el original aceptado en el hash S8. |
| docs/ia.md al día para la semana | Cumple | Registro del 4 de octubre incluye implementación asistida, cambios, rechazos con motivo y validación; [docs/ia.md:44–98](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/ia.md#L44-L98). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | CI exacto success, pero no hay scanner/configuración/Quality Gate SonarCloud en el árbol; [.github/workflows/ci.yml:13–45](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/.github/workflows/ci.yml#L13-L45) solo prueba y build. |
| Sin credenciales en el repositorio ni en el historial | No verificado | No hay credenciales reales hardcodeadas ni .env versionado en el snapshot; no se certifica todo el historial. Existe riesgo operativo distinto: métricas exponen request.path, que puede contener tokens de invitación. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas, 173 commits agregados en S9, para tres integrantes. Variantes deben consolidarse por evidencia de identidad; no se adivina la equivalencia. |

## Actions en el estado congelado

- [CI: success](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/37306348930), 2026-10-05T11:58:07Z, SHA exacto del estado indicado.
- [pages build and deployment: success](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/37306347582), 2026-10-05T11:58:06Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Barrido estático sin credenciales reales; tokens de invitación se generan con secrets.token_urlsafe y el workflow usa claves efímeras de prueba. No hay .env versionado. No se certifica historia completa. Hallazgo de privacidad por lectura de código: los paths con tokens se agregan a http_requests_by_path y se publican en /metrics. Se recomienda usar plantillas de ruta/redactar tokens y restringir acceso a métricas; no se accedió a invitaciones reales.

## Estado global del proyecto (overall · punta actual)

Se resolvieron los conflictos de merge de infraestructura y el CI del hash S9 está en verde en ejecución posterior al cierre. El flujo S9 requería invitados.html, ausente en ese árbol: la plantilla y CSS llegaron después, junto a documentación y tabla de aspectos ampliadas. Se reconoce la corrección tardía sin modificar S9. La URL pública/HTTPS, medición y umbral siguen pendientes. La nueva observabilidad puede divulgar tokens por rutas crudas y debe normalizarse antes de exponer usuarios reales.

El delta S9 contiene 11 commits respecto de S8; hay 4 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Recuento y nota sugerida

**3 de 10 criterios Cumple. Nota sugerida: 2.2 = 1 + 4 × (3/10).** Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no integra este cálculo.

## Acciones prioritarias

- Normalizar/redactar tokens en métricas y restringir /metrics: no publicar rutas crudas de invitaciones.
- Crear prueba del flujo completo POST / → plantilla de invitados → creación → respuesta; un test directo a /crear-invitaciones omite la pantalla intermedia.
- Configurar host/HTTPS, medir salud y flujo principal con umbral y línea base identificables.
- Aportar ADR coherente de evolución del flujo y preservar decisiones aceptadas con un ADR sustituto para Dokploy.
- Añadir auditoría de erosión del cambio, inventario verificado de propuestas/dependencias y decisión sobre componente generativo.
- Integrar SonarCloud y publicar scanner, run y Quality Gate; aclarar asignación operativa S10.

## Hallazgos cerrados con evidencia nueva

- Conflictos de merge de Docker/Compose/ejemplos/evidencia ya no están presentes en snapshot S9; [Dockerfile:1–15](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/Dockerfile#L1-L15), [docs/evidencia.md:58–125](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/evidencia.md#L58-L125).
- Se restauró encabezado de aspectos en S9 y se amplió tabla después del cierre; [docs/aspectos.md:1–5](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/5aa889370dcf342ba06666893b97f8065b513de9/docs/aspectos.md#L1-L5), [docs/aspectos.md:5–12](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/aspectos.md#L5-L12).
- Plantilla invitados.html agregada después del cierre; fallo identificado y corregido según registro de IA actual, [docs/ia.md:47–47](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/c2077ac55a29562adc728734ca4c283ccb40f310/docs/ia.md#L47-L47).
- CI pasa para hash S9 y HEAD; ello no cierra SonarCloud ni garantiza el flujo UI completo.
