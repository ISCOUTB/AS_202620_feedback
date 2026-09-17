# semana-06-evidencia-s6 · GimnasioUTB

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_GimnasioUTB` |
| Estado revisado | `106869b` en `origin/main` (2026-09-13T22:19:08-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/contextos-delimitados.md en 106869b: flowchart con Cliente (App Móvil), Usuarios e Identidad (Supporting), Control de Aforo (Core) y Notificaciones (Generic), con relaciones 'Customer-Supplier: Upstream a Downstream' y 'OHS / PL'. | Cumple | Tipifica cliente-proveedor y OHS/PL; no declara núcleo compartido ni capa anticorrupción. |
| Tabla módulo a datos con dueño único por entidad | docs/contextos-delimitados.md: tabla 'Módulo → dato → dueño único' con columna 'Dato del que es dueño (único que escribe)' por contexto y columna de lectores sin escritura. | Cumple | Un solo escritor declarado por dato; Aforo leído por Notificaciones y Gestión Operativa. |
| La tabla cubre las entidades que existen en el código | El código de 106869b solo materializa aforo (src/modules/aforo/domain/aforo.js y .../persistence/aforo-memoria.adapter.js; sin migraciones ni .sql en el árbol) y la tabla lista Aforo con 'contador de ocupación actual'. | Cumple | Reconoce que historial de eventos e Identidad/Gestión/Notificaciones no existen aún; no hay esquema real con el que contrastar. |
| No conformidades de propiedad de datos detectadas sobre el código actual | V1 cita src/modules/aforo/infrastructure/persistence/aforo-memoria.adapter.js (estado mutable público) y V2 cita src/server.js (lectura que bypassa el caso de uso); V3 se declara riesgo futuro. | Cumple | V1 y V2 son hallazgos sobre código existente con módulo dueño esperado identificado. |
| Plan de corrección por no conformidad | docs/contextos-delimitados.md: V1 → encapsular con campo privado #aforoActual; V2 → crear caso de uso consultarAforoActual; V3 → definir AforoQueryPort de solo lectura. | Cumple | Acciones concretas y verificables ligadas a cada hallazgo. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | docs/arc42/arc42_gimnasio_utb.md en 106869b: el extracto llega hasta la sección 3.2 y se corta; no se observó sección 8 ni ruta docs/arc42/08*. | No verificado | Motivo: extracto parcial. Haría falta el archivo completo o confirmación de la sección 8 con lenguaje ubicuo y mapa de contextos. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4 solo contiene c4_level1.md, c4_level2.md y PNG; docs/adr solo tiene 0001-arquitectura-hexagonal.md y ADR0001.md, ninguno de reajuste de límites. | No cumple | El mapa de S6 introduce contextos marcados 'No implementado' (Usuarios e Identidad, Gestión Operativa, Notificaciones) ausentes del corte 1 y no hay C4 nivel 3 ni ADR del reajuste; tampoco se aportó el hash de S5 para el diff. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md: fila S1 'Consistencia de datos' enlaza ADR-0001 y las clases de src/modules/aforo, que corresponden al contexto Control de Aforo (Core). | Cumple | Solo existe la fila S1; Usuarios e Identidad, Notificaciones y Gestión Operativa quedan sin aspecto asociado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repo público ISCOUTB/AS_202620_GimnasioUTB (visible: true); autores consolidados PedroPambi, RodrigoFacioLince y sebastian-caicedo (dos entradas con el mismo correo = una cuenta), coincidentes con los 3 integrantes declarados. | Cumple | Sin cuentas ajenas a la organización; el ADR afirma 4 personas frente a 3 integrantes declarados. |
| Estructura mínima | Árbol de 106869b contiene docs/arc42/, docs/adr/, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | C4 incluye .md y .png; sin desviaciones de ruta que oculten artefactos. |
| Convenciones de ADR | docs/adr/ADR0001.md no cumple el patrón ^[0-9]{4}-titulo-kebab-case.md y duplica el contenido de docs/adr/0001-arquitectura-hexagonal.md con referencias divergentes (ES1/ES7/ES8 frente a ES1/ES2/ES3/ES4). | No cumple | La salida esperada del comando de nombres no queda vacía; hay dos archivos para la misma decisión 0001. |
| Tabla de aspectos | docs/aspectos.md usa columnas Estímulo/Fuente/Entorno/Respuesta/Medida/Tensión/ADR y una segunda tabla sin columna C4 ni Evidencia; no aparecen las ocho columnas del contrato. | No cumple | Faltan C4 y Evidencia y la trazabilidad no es navegable en todos los eslabones. |
| Registro de uso de IA | docs/ia.md con 8 commits desde 2026-08-08 hasta 2026-09-13 (a59410d); entradas de semana 2 y 3 con 'Rechazado' y 'Motivo' (diagrama C4 descartado). | Cumple | Las semanas 4 y 5 registran 'N/A' o motivo genérico en lo rechazado. |
| README | README.md declara qué es el sistema, requisitos (Node ≥ 18), arranque con 'npm install && npm start' y pruebas con 'npm test', con verificación por /health. | Cumple | Declara explícitamente que la persistencia real es en memoria. |
| Pipeline y análisis estático | .github/workflows/ci.yml solo ejecuta 'npm install' y 'npm test' (runs success, p. ej. https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/34802198344), sin scanner SonarCloud ni sonar-project.properties ni URL pública del análisis. | No cumple | Faltan 2 de las 3 evidencias exigidas (invocación del scanner y URL pública con Quality Gate); el CI de pruebas sí corre en verde. |
| Secretos | Búsqueda de patrones de credenciales sin coincidencias en HEAD y envs_versionados vacío, con .env.example como única plantilla. | Cumple | Sin .env versionado ni claves privadas en el historial revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `106869bd63ac89ce19eae93a464b341be6bf75f8 2026-09-13T22:19:08-05:00 Add context map diagram to documentation`
- **Veredicto**: con pendientes
- Resumen: HEAD 106869b (2026-09-13T22:19:08-05:00) está dentro del cierre y su CI corre en verde (run 34802198344). S6 entrega un mapa de contextos y una auditoría de propiedad de datos defendible, pero arrastra deuda transversal del contrato: sin SonarCloud, ADR duplicado y fuera de convención, tabla de aspectos sin las ocho columnas y arc42 sección 8 no verificada.

Pendientes que siguen abiertos:
- Integrar el scanner de SonarCloud en .github/workflows/ci.yml y publicar la URL del análisis con el estado del Quality Gate.
- Eliminar o renombrar docs/adr/ADR0001.md para cumplir la convención NNNN-titulo-kebab-case.md.
- Completar docs/aspectos.md con las ocho columnas del contrato (C4 y Evidencia).
- Confirmar o escribir la sección 8 del arc42 con lenguaje ubicuo y mapa de contextos.
- Añadir C4 nivel 3 y ADR de reajuste si los límites de los contextos cambiaron desde el primer corte.
- Implementar el adaptador PostgreSQL y el historial de eventos, hoy declarados pendientes.

## Recuento y nota sugerida

6 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.0 = 1 + 4 × (6/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- arc42 sección 8 (lenguaje ubicuo y mapa de contextos): el extracto de docs/arc42/arc42_gimnasio_utb.md se corta en 3.2; hace falta el archivo completo o la ruta docs/arc42/08*.
- Comparación contra el hash revisado en S5 (git diff --stat <HASH_S5>..106869b -- docs/c4 docs/arc42 docs/adr): no se aportó el hash de la revisión definitiva de S5.
- Arranque local ('npm install && npm start') y 'npm test': no ejecutados por el agente; se usan los runs de CI en verde como sustituto parcial.
- Quality Gate de SonarCloud: no existe URL pública que consultar para 106869b.

## Hallazgos para la planilla

- No hay análisis SonarCloud: ci.yml solo instala y prueba, sin scanner ni URL de Quality Gate.
- docs/adr/ADR0001.md duplica el ADR 0001 con nombre fuera de convención y referencias divergentes.
- docs/aspectos.md no usa las ocho columnas del contrato (faltan C4 y Evidencia).
- No existe C4 nivel 3 ni ADR de reajuste pese a los nuevos contextos del mapa de S6.
- La sección 8 del arc42 no aparece en el extracto revisado.
- El mapa de contextos tipifica cliente-proveedor y OHS/PL, pero no núcleo compartido ni capa anticorrupción.
- El ADR declara un equipo de 4 personas frente a 3 integrantes declarados.
- La persistencia real sigue en memoria y PostgreSQL, Notificaciones e Identidad no están implementados.
