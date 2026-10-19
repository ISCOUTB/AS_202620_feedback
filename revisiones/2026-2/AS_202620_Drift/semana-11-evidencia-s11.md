# Drift · Evidencia S11 · DEFINITIVA, estado histórico al cierre

[Árbol completo de la instantánea evaluada](https://github.com/ISCOUTB/AS_202620_Drift/tree/1cead90c02d284f9261addd19e5979ab114b9aea) · [Ficha S11](../../../fichas/semana-11-evidencia-s11.md)

- Repositorio público: https://github.com/ISCOUTB/AS_202620_Drift
- Rama seleccionada: `origin/master` (HEAD remoto); no se usaron etiquetas ni ramas de trabajo.
- Hash evaluado: `1cead90c02d284f9261addd19e5979ab114b9aea` · fecha de commit: `2026-10-18T22:20:50-05:00`.
- Cierre S11 exclusivo: `2026-10-19T05:00:00Z` (medianoche de Colombia). Selección con `--until=2026-10-19T04:59:59Z`.
- Observación S12: `2026-10-19T21:35:00Z`; estado observado, no cierre ni calificación final.
- Commits de la rama entre cierres S10/S11: 14; posteriores al cierre hasta la punta observada: 0.
- Líneas de la matriz corresponden al hash evaluado; las de overall corresponden a la punta `1cead90c02d284f9261addd19e5979ab114b9aea`.

## Matriz de la ficha

| Criterio | Estado | Evidencia | Observación |
|---|---|---|---|
| Integración principal identificada en el código | Cumple | [backend/app/infrastructure/external/resilient_http.py:125-157](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/backend/app/infrastructure/external/resilient_http.py#L125-L157); [docs/adr/0009-decision-extraccion-integracion-steam.md:11-16](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/adr/0009-decision-extraccion-integracion-steam.md#L11-L16) | Búsqueda → adaptador Steam → HTTP ubicada, con respaldo. |
| Tabla de modos de fallo con no responde, responde tarde y responde dos veces | Cumple | [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md:86-103](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md#L86-L103) | F01 no responde, F02 tarda y F14 responde dos veces, diferenciados de repetir una consulta. |
| Mitigación asignada a cada modo de fallo | Cumple | [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md:90-109](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md#L90-L109) | Cada fallo tiene táctica y estado, incluidos pendientes fuera de alcance. |
| Correspondencia entre mitigaciones declaradas e implementadas, o pendiente declarado | Cumple | [backend/app/infrastructure/external/resilient_http.py:48-52,94-106,147-215](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/backend/app/infrastructure/external/resilient_http.py#L48-L52); [docs/adr/0009-decision-extraccion-integracion-steam.md:66-70](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/adr/0009-decision-extraccion-integracion-steam.md#L66-L70) | Timeout por fase, dos intentos y jitter implementados; breaker/plazo total pendientes declarados con criterio de revisión. No se exige breaker implementado. |
| Diseño de idempotencia o saga, o argumento de por qué no aplica | Cumple | [docs/arc42/arc42_8_conceptos_transversales.md:237-247](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/arc42/arc42_8_conceptos_transversales.md#L237-L247); [backend/app/application/usecases/sync_playstation_catalog.py:18-25](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/backend/app/application/usecases/sync_playstation_catalog.py#L18-L25) | GET sin efecto de negocio y reemplazo de catálogo por los mismos datos; saga/outbox no aplican hoy, argumento explícito. |
| ADR con la decisión de extraer o no extraer, y sus criterios | Cumple | [docs/adr/0009-decision-extraccion-integracion-steam.md:27-70](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/adr/0009-decision-extraccion-integracion-steam.md#L27-L70) | Decisión y matriz cualitativa de costo, aislamiento, latencia y reversibilidad. |
| La alternativa no extraer aparece evaluada, no omitida | Cumple | [docs/adr/0009-decision-extraccion-integracion-steam.md:39-62](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/adr/0009-decision-extraccion-integracion-steam.md#L39-L62) | Mantener integración en backend se compara y elige explícitamente. |
| arc42 sección 11 con los modos de fallo | Cumple | [docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md:80-111](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/arc42/arc42-11-riesgos-y-deuda-tecnica.md#L80-L111) | Sección 11 contiene análisis, límites y planes concretos. |
| Filas de aspectos afectadas por la integración, al día | Cumple | [docs/aspectos.md:53-60](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/aspectos.md#L53-L60) | E5 enlaza ADR-0009, fuente, pruebas y riesgos; declara pendiente medir límite temporal. |

## Matriz transversal del contrato

| Criterio | Estado | Evidencia | Observación y límite |
|---|---|---|---|
| Repositorio público en organización y convención | Cumple | https://github.com/ISCOUTB/AS_202620_Drift; clon Git público exitoso; API actions/runs con SHA exacto | Visibilidad comprobada sin pedir acceso. |
| Estructura mínima presente | Cumple | Árbol del hash; `docs/arc42/`, `docs/adr/`, `docs/c4/`, [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/aspectos.md), [docs/ia.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/ia.md), `README.md` | Doce secciones en Markdown y rutas mínimas presentes; nombres de sección alternativos se reconocen. |
| Estado evaluado identificable | Cumple | `origin/master` · `1cead90c02d284f9261addd19e5979ab114b9aea` · `2026-10-18T22:20:50-05:00` | S11 histórico y S12 preliminar no se mezclan. |
| Nombres ADR según convención | Cumple | Inventario `docs/adr/` del hash evaluado | Archivos de decisiones con numeración de cuatro dígitos y kebab-case. |
| ADR aceptados no reescritos | No verificado | `git log --follow` de ADR-0002 y ADR-0008; commits `70e52e2`, `ab591de` | Hay ampliaciones y fusiones históricas. Sin fijar inequívocamente estado de aceptación en cada versión previa, no se declara inmutabilidad cumplida ni violación por mera edición; falta contraste exhaustivo de versiones aceptadas. |
| Registro IA al día para la semana | Cumple | [docs/ia.md:947-966](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/ia.md#L947-L966); commit `6b85ff2` | Entrada S11 identifica herramienta, corrección, prueba de duplicados y dos alternativas rechazadas con razón. |
| Pipeline, SonarCloud y Quality Gate públicos | No verificado | .github/workflows/; consulta actions/runs exacta descrita abajo | Run CI del SHA exacto exitoso: https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39194258318 . [.github/workflows/ci.yml:45-54,142-154](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/.github/workflows/ci.yml#L45-L54) prueba contrato, backend y ejecuta Sonar con qualitygate.wait=true; `sonar-project.properties:1-2` identifica isco-utb. Consulta pública del Gate HTTP 403: no se pudo observar directamente análisis/revisión, aunque el workflow espera Gate. No se verificó protección efectiva de rama. |
| Sin credenciales en repositorio e historial | No verificado | Barrido git grep de patrones CONTRATO §9 en `1cead90c02d284f9261addd19e5979ab114b9aea` y punta; `git log -S"BEGIN PRIVATE KEY"` en la rama | Sin claves privadas ni tokens inequívocos en patrones revisados; coincidencias de configuración, tipos y ejemplos no prueban filtración. No se certifica todo el historial de todas las clases de secretos con un único patrón. Completar auditoría especializada sin publicar valores. |
| Contribución de todos los integrantes | No verificado | `git shortlog -sn 1cead90c02d284f9261addd19e5979ab114b9aea` contrastado con EQUIPOS.md | Hay actividad de varios autores y alias. No se atribuyen por parecido ni se publica identidad. Falta corroborar documentalmente cada alias y la contribución sustantiva código/documentación por integrante; no inferir ausencia por conteo bruto. |

## Recuento y nota sugerida

**9/9 Cumple. Nota sugerida: 5.0 = 1 + 4 × (9/9), propuesta al docente; la nota final se fija en Moodle.** Resultado definitivo de esta revisión histórica S11; la propuesta no reemplaza la decisión docente. La matriz transversal no entra en la fórmula.

## overall · estado actual y erosión arquitectónica

Sin delta después del cierre. Dependencias revisadas de `backend/app/domain/` y `backend/app/application/` no importan httpx/FastAPI/infraestructura; `sync_playstation_catalog.py:3-6` usa puertos. Erosión documental: [docs/c4/contenedores.md:28-68,138-157](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/docs/c4/contenedores.md#L28-L68) mezcla componentes internos y persistencia futura; el anexo 171-190 aclara la realidad, pero conviene retirar/rotular la vista antigua. Sección 8 aún presenta repositorio de requisitos en memoria como único implementado mientras el árbol contiene adaptador Steam. Resiliencia no equivale a cumplir p95: timeout por fase y dos intentos pueden exceder E6; Steam vacío no lleva aviso al cliente (`arc42 §11.8:101-111`).

## CI, pruebas y límites

Run CI del SHA exacto exitoso: https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39194258318 . [.github/workflows/ci.yml:45-54,142-154](https://github.com/ISCOUTB/AS_202620_Drift/blob/1cead90c02d284f9261addd19e5979ab114b9aea/.github/workflows/ci.yml#L45-L54) prueba contrato, backend y ejecuta Sonar con qualitygate.wait=true; `sonar-project.properties:1-2` identifica isco-utb. Consulta pública del Gate HTTP 403: no se pudo observar directamente análisis/revisión, aunque el workflow espera Gate. No se verificó protección efectiva de rama.

Se hizo una sola consulta GitHub actions/runs por equipo con head_sha de la punta y sin filtro de evento; se distingue push de pull_request. Los resultados encontrados son de push. No se usó un wrapper limitado a PR ni se interpretó una lista vacía como ausencia de CI.

No ejecuté código de estudiantes, pytest, Schemathesis, k6, contenedores ni PDF. CI verde acredita ese run, no una medición nueva de producción. Casos implementados/pruebas declarados y pendientes están separados en arc42 §11.8; E6 con fuentes simuladas no demuestra latencia real de Steam.

Se leyeron artefactos pertinentes completos por partes y código de integración; búsquedas solo localizaron evidencia. No se ejecutaron scripts de estudiantes ni se abrieron/ejecutaron PDF. Se conservaron hallazgos históricos sin recalificar semanas anteriores.

## Pendientes accionables

Medir p95 con Steam degradado y plazo total, extender control de errores a fuentes secundarias y aclarar las vistas C4 antiguas. Para S12: matriz de consistencia, regla de invalidación o justificación por fuente, y ADR con costo comparado de reversión.
