> Pasada temprana (previa al cierre del 2026-10-05T05:00:00Z): el hash y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

# Semana 9 · Evidencia S9 · Generación verificada y trazable · PideUtb


| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_PideUtb` |
| Estado revisado | `0393eee` en `origin/master` (2026-09-30T11:25:53-05:00) |
| Cierre | 2026-10-05T05:00:00Z |
| Revisor | auditoría local preliminar sobre clon público efímero |

Entre el hash calificado de S8 (`a94bf4e`, 2026-09-27) y la punta hay **10 commits del periodo S9**
(`git rev-list --count a94bf4e..origin/master` = 10). Por su contenido y por lo que el propio
informe S8 dejó registrado, **todos son trabajo de cierre de S8 subido después del cierre de esa
entrega**: la migración a PostgreSQL (`1c676e9`), el panel del mostrador que cierra ESC-03
(`8898291`), las violaciones V-09/V-10 (`373817f`, `0441ef2`), el registro de IA de la **octava**
entrega (`e048523`) y el ajuste de `requirements` (`0393eee`). No hay, todavía, un artefacto que
se declare como entrega S9. Se califica cada fila con la evidencia del periodo y se deja escrita
esa procedencia.

## Matriz de la ficha

| Criterio de evaluación | Evidencia técnica esperada | Estado | Observaciones |
|---|---|---|---|
| Porción real del sistema construida con apoyo de IA | rutas del código y commits | Cumple | El periodo construyó porciones reales del sistema: panel del mostrador (`sitio/panel.js`, `sitio/panel.html`, `backend/app/pedidos/router.py:78`, `backend/app/pedidos/service.py:200`) en `8898291`, y migración a PostgreSQL (`backend/app/base_de_datos.py:119`, `backend/migraciones/001_esquema_inicial.sql`) en `1c676e9`. Es sistema, no un ejercicio aparte. Procedencia: cierre de S8, no entrega S9. |
| Cadena completa navegable para esa porción | fila de `docs/aspectos.md` recorrida hasta la evidencia | No cumple | La fila ESC-03 de `docs/aspectos.md` se actualizó en `8898291` y navega a C4, ADR-0002, código y pruebas, pero la cadena no llega a la medición del escenario y el documento cierra con «Estado a la fecha (S7)». Se rompe en la evidencia de calidad. |
| ADR con la decisión argumentada por el equipo | `docs/adr/NNNN-*.md` con restricciones del proyecto | No cumple | `docs/adr/` sin cambios en el periodo (siguen 0001-0004). La porción del periodo no tiene ADR propio: la migración se apoya en ADR-0004 (anterior) y el panel en ADR-0002 (anterior). |
| Prueba que falla ante el defecto que cubre | run en rojo, prueba de mutación o procedimiento documentado | No verificado | No hay run en rojo, mutación ni procedimiento documentado para la porción del periodo. La infraestructura de mutación (`backend/tests/conftest.py:15`) y el run en rojo citado (`README.md`, run #22) son de S7, línea base. Queda como pregunta de sustentación. |
| Medición del escenario asociado | resultado contrastado con el umbral | No cumple | Sin medición contrastada con umbral en el periodo. |
| `docs/ia.md` con lo aceptado, lo corregido y lo rechazado con motivo | extracto citado del archivo | No cumple | El único cambio del periodo en `docs/ia.md` es la entrada de la **octava** entrega (`e048523`, `docs/ia.md:188`), no un extracto de S9. |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | hallazgos con su ubicación y su corrección | Cumple | `docs/violaciones.md` actualizado en el periodo: V-09 (estado en memoria → PostgreSQL) corregida en `1c676e9` (`docs/violaciones.md:274`) y V-10 (panel sin autenticar) detectada con ubicación y plan (`docs/violaciones.md:348`, `8898291`). Procedencia: es la auditoría de propiedad de datos de S6 evolucionada en el periodo, no un análisis nuevo de erosión de la generación S9. |
| Dependencias propuestas verificadas en su registro oficial | lista de dependencias añadidas y su comprobación | Cumple | Añadida en el periodo `psycopg[binary,pool]>=3.2,<4.0` (`backend/requirements.in`, `0393eee`), con lock `psycopg==3.3.6`, `psycopg-binary==3.3.6` y `psycopg-pool==3.3.3`. Verificadas en PyPI (HTTP 200, nombre legítimo): `https://pypi.org/pypi/psycopg/json`, `…/psycopg-binary/json`, `…/psycopg-pool/json`. |
| Sin credenciales en código, ejemplos ni documentación generada | barrido del contrato, incluido `docs/` | Cumple | `git grep` del contrato sobre la punta: solo `var.render_api_key`, `var.supabase_access_token`, `var.github_token`, `var.supabase_db_password` y marcadores `XXXX` en `infra/terraform.tfvars.example:20,29,60`; sin `.env` versionado. En el historial del periodo se añadió (`1c676e9`) y retiró (`1744560`) la contraseña efímera del contenedor de pruebas de CI, sin valor de producción. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | conjunto de evaluación con resultados, o el ADR | No cumple | Sin conjunto de evaluación, costo/latencia ni ADR de no incorporarlo. Claude es herramienta de desarrollo, no componente del sistema. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | `https://github.com/ISCOUTB/AS_202620_PideUtb`; clon anónimo `--filter=blob:none` exitoso; rama `origin/master`. | Cumple | Responde sin autenticación; el nombre sigue `AS_202620_<PROYECTO>`. |
| Estructura mínima presente | El árbol contiene `docs/arc42/arc42.md`, `docs/adr/` (0001-0004), `docs/c4/`, `docs/aspectos.md`, `docs/ia.md` y `README.md`. | Cumple | Las seis rutas del contrato §2, ya en minúsculas. |
| Estado calificado identificable | `0393eee` en `origin/master`, `2026-09-30T11:25:53-05:00`: `Hacer que requirements.txt incluya requirements.in en vez de copiarlo`. | Cumple | La punta difiere de S8 (`a94bf4e`); el periodo S9 son los 10 commits descritos. |
| Nombres de ADR según la convención | `0001-estilo-arquitectonico.md`, `0002-propiedad-datos-establecimiento.md`, `0003-estrategia-integracion.md`, `0004-plataforma-de-despliegue.md`. | Cumple | Los cuatro pasan el filtro `NNNN-titulo-en-kebab-case.md`. |
| ADR aceptados no reescritos | ADR-0001 aceptado `b5f0310` (2026-08-23) y editado en `1b4f0f6` (2026-09-07) y `1864353` (2026-09-20, título reescrito); ADR-0002 aceptado `9eda1f3` (2026-09-13) y editado en `1864353` (título reescrito). Sin cambios en el periodo S9, pero el hallazgo sigue abierto. | No cumple | El contrato §4 prohíbe editar un ADR aceptado sin declarar reemplazo; ninguna edición lo declara. |
| `docs/ia.md` al día para la semana | Sin commit sobre `docs/ia.md` en el periodo S9; el último es `e048523` (2026-09-28, registro de S8). | No cumple | No hay registro de uso de IA de la semana 9. |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | Run del hash revisado: `CI` — `success` (https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/36744142768). Config `sonar-project.properties` y líneas del scanner en `.github/workflows/ci.yml`, pero condicionadas a `SONAR_TOKEN`, que `infra/README.md:209` marca **Pendiente**. El análisis público de SonarCloud para `0393eee` tiene el Quality Gate en **ERROR** (`new_reliability_rating=3`). | No cumple | Falla por el Quality Gate en rojo para el hash revisado (y por el token pendiente, que hace que el job del scanner no se ejecute). |
| Sin credenciales en el repositorio ni en el historial | `git grep` del contrato sobre la punta sin valores reales; ningún `.env` versionado; `git log -S'BEGIN PRIVATE KEY'` sin coincidencias. | Cumple | En el historial del periodo quedó la contraseña efímera del contenedor de pruebas (`POSTGRES_PASSWORD: pruebas`, `1c676e9`, retirada en `1744560`): no protege nada y no es de producción, mismo tratamiento que el password de CI de CampusMarket en S8. |
| Contribución de todos los integrantes | `shortlog -sne` consolidado por correo idéntico: `Santiago Cuesta` + `Santiago-C0` (58), `daniarriet` (26), `Ruddy` + `ruddy2000utb-droid` (10). | Cumple | Los tres integrantes declarados tienen commits atribuibles. |

## Estado global del proyecto (overall · punta actual de la misma rama)

- **Punta actual revisada**: `0393eee` — `2026-09-30T11:25:53-05:00 Hacer que requirements.txt incluya requirements.in en vez de copiarlo`.
- **Veredicto**: sin entrega S9; la punta avanzó con el cierre de la deuda de S8.
- **Commits posteriores al cierre de S8** (los 10 del periodo): `0393eee`, `1e8ad51`, `ed57869`, `1744560`, `1c676e9`, `0441ef2`, `373817f`, `8898291`, `e048523`, `c04bc50`.
- Resumen: el equipo terminó la migración a PostgreSQL (cierra V-09), añadió el panel del mostrador que completa ESC-03, registró el uso de IA de S8 (que había llegado tarde) y saneó el `requirements`. Nada de eso es todavía la entrega S9. En la punta la deuda de S8 queda en mejor forma, pero el Quality Gate público de SonarCloud pasó a **ERROR** para el hash revisado, y siguen abiertos los pendientes de S8: la restricción de tarjeta en arc42 §2, la edición de ADR aceptados y la acreditación del Quality Gate.

Pendientes que siguen abiertos:
- Sin entrega S9: falta la porción con su cadena, el ADR de esa porción, la prueba en rojo, la medición, el extracto de `docs/ia.md` de la semana y el ADR del componente generativo.
- Quality Gate público de SonarCloud en **ERROR** para `0393eee` (`new_reliability_rating=3`); además `SONAR_TOKEN` sigue marcado como pendiente.
- No editar ADR aceptados sin declarar reemplazo (ADR-0001 y ADR-0002).

## Recuento y nota sugerida

**4 de 10 criterios Cumple** (porción real, auditoría de erosión, dependencias verificadas y sin credenciales).

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 2.6 = 1 + 4 × (4/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Criterio 4 (prueba que falla): No verificado por ausencia de run en rojo, mutación o procedimiento de S9; queda como pregunta de sustentación.
- Quality Gate público de SonarCloud para `0393eee`: **ERROR** (`new_reliability_rating=3`); el job del scanner no se ejecuta por `SONAR_TOKEN` pendiente.
- Los criterios 1, 7 y 8 se apoyan en trabajo de cierre de S8 subido en el periodo S9; se citan con esa procedencia.

## Hallazgos para la planilla

- La punta avanzó 10 commits desde S8, todos de cierre de S8 (migración a PostgreSQL, panel del mostrador, V-09/V-10, registro de IA de S8, `requirements`); no hay todavía artefacto S9.
- Porción y auditoría de propiedad de datos presentes en el periodo, sin la cadena S9 completa (falta medición) ni ADR propio de la porción.
- `psycopg`, `psycopg-binary` y `psycopg-pool` verificados como legítimos en PyPI.
- Quality Gate público de SonarCloud en **ERROR** para el hash revisado, pese a que el README lo declara `OK`.
- El barrido de credenciales de la punta está limpio; el historial del periodo conserva una contraseña efímera de CI, ya retirada en la punta.
- ADR-0001 y ADR-0002 siguen con ediciones posteriores a su aceptación sin reemplazo declarado.
