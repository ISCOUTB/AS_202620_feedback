# semana-06-evidencia-s6 · LostVault

> Pasada temprana (GitHub Actions, previa al cierre): los hashes y la nota son preliminares y pueden cambiar si el equipo empuja antes del cierre.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_LostVault` |
| Estado revisado | `9d57572` en `origin/main` (2026-09-13T22:11:29-05:00) |
| Cierre | 2026-09-14T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Mapa de contextos con relaciones tipificadas | docs/ddd/mapa_contextos.md: diagrama mermaid con authentication→claims, identity_verification→claims y objects→claims como Cliente/Proveedor vía public/, más objects-.-→search y un Shared Kernel mínimo en lib/core/. | Cumple | Usa el vocabulario de la semana (Cliente/Proveedor, Shared Kernel) y no es un diagrama de capas técnicas. |
| Tabla módulo a datos con dueño único por entidad | docs/ddd/mapa_contextos.md sección 2: tabla Módulo (dueño) · Dato que posee · Lectores · Verificado en código. | Cumple | Declara un módulo con permiso de escritura por dato y deja explícitos los huecos (users aislado, tokens inexistentes en AuthUser). |
| La tabla cubre las entidades que existen en el código | lib/features/*/domain (auth_user.dart, lost_object.dart, claim.dart, verification.dart, user_profile.dart) contrastado con las seis filas de docs/ddd/mapa_contextos.md sección 2. | Cumple | Cubre los seis módulos con entidad propia; la persistencia es in-memory, así que no hay migraciones ni esquema SQL que contrastar. |
| No conformidades de propiedad de datos detectadas sobre el código actual | docs/ddd/mapa_contextos.md sección 3: NC1 users sin consumidor ni cableado en main.dart, NC2 objects no importa authentication/public, NC3 search/domain/search_result.dart importa objects/public, NC4 AuthUser sin token. | Cumple | Cada fila identifica entidad o relación, dueño esperado y ubicación observada en el código. |
| Plan de corrección por no conformidad | docs/ddd/mapa_contextos.md sección 3, columna Plan de corrección: crear value object propio en search/domain y mapear en application/, cablear users por public/ o retirar sus filas, ajustar la tabla al modelo real. | Cumple | NC5 se declara resuelta por el propio documento, sin ADR ni verificación independiente. |
| arc42 sección 8 con lenguaje ubicuo y mapa de contextos | El árbol de 9d57572 lista docs/arc42/01,02,03,04,05,06,09,10 y glosario.md; no existe ningún archivo docs/arc42/08*. | No cumple | El glosario aporta lenguaje ubicuo, pero la sección 8 con el mapa de contextos incorporado no existe. |
| C4 nivel 3 y ADR si los límites cambiaron desde el primer corte | docs/c4 solo contiene c4_contexto.png, contexto.mmd y C4 nivel 2.jpg; docs/adr solo tiene 0001-estilo-arquitectonico.md. | No verificado | No se aporta el hash revisado en S5 para el diff; haría falta ese hash y, si hubo reajuste, el C4 nivel 3 y el ADR que lo explique. |
| Aspectos relacionables con los contextos del mapa | docs/aspectos.md AS-01 y AS-04 apuntan a búsqueda/consulta (search y objects), AS-02 a publicación (objects) y AS-03 a reclamación (claims e identity_verification), todos presentes en docs/ddd/mapa_contextos.md. | Cumple | La relación no está escrita de forma cruzada en el mapa y el contexto users queda sin aspecto asociado. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | Repositorio AS_202620_LostVault en la organización ISCOUTB, visible=true; el historial tiene cinco identidades de autor y se consolidan los pares que comparten cuenta (Fausto-4 y Jose Faustino España; weller-rar y Weller). | Cumple | No se atribuye la cuenta shamarallorente-blip a una integrante declarada solo por parecido de nombre; conviene que el equipo declare sus cuentas. |
| Estructura mínima | En 9d57572 existen docs/arc42/, docs/adr/0001-estilo-arquitectonico.md, docs/c4/, docs/aspectos.md, docs/ia.md y README.md. | Cumple | El C4 nivel 2 está como imagen jpg y no como diagrama de código; se versiona .dart_tool/. |
| Qué estado del repositorio se califica | origin/main en 9d575727491866419d94a766599a1bea8ba34cd3, 2026-09-13T22:11:29-05:00, anterior al cierre 2026-09-14T05:00:00Z, sin commits posteriores. | Cumple | El campo commits_nuevos_desde_cierre_anterior aparece vacío, lo que conviene aclarar en la entrega. |
| Convenciones de ADR | docs/adr/0001-estilo-arquitectonico.md respeta el patrón NNNN-titulo-kebab-case y contiene contexto, alternativas, decisión, consecuencias y trazabilidad. | Cumple | No hay ADR posterior, aunque el mapa de contextos es un artefacto nuevo de esta semana. |
| La tabla de aspectos | docs/aspectos.md usa columnas ID, Aspecto, Prioridad, Justificación, Tensión, Escenario, Medida, Decisión, Implementación y Pruebas; no hay columna Requisito ni columna C4. | No cumple | La fila AS-03 llega hasta pruebas, pero AS-01, AS-02 y AS-04 tienen celdas Pendiente, huecos que rompen la cadena exigida. |
| Registro de uso de IA | docs/ia.md con registros S1 (2026-08-08), S2 (2026-08-16) y S3 (2026-08-23/24), cada uno con lo aceptado y lo rechazado con motivo técnico. | Cumple | El único commit del archivo es de 2026-08-24, así que el registro no crece desde hace varias semanas. |
| README | README.md declara requisitos, arranque con flutter pub get y flutter run -d chrome, y prueba con flutter analyze y flutter test, más el recorrido manual esperado. | Cumple | El arranque depende de Chrome y de un recorrido manual, sin comando único que verifique el flujo. |
| Pipeline y análisis estático | .github/workflows/flutter.yml ejecuta flutter analyze y flutter test; .github/workflows/build.yml invoca SonarSource/sonarqube-scan-action con sonar-project.properties; runs exitosos del 2026-09-14T03:11:31Z: Flutter checks https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/34801736898 y Build https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/34801736760. | No cumple | Falta la tercera evidencia exigida: URL pública del análisis en SonarCloud con rama o revisión y estado del Quality Gate; sin secretos ni .env versionados (sección 9 sin coincidencias). |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `9d575727491866419d94a766599a1bea8ba34cd3 2026-09-13T22:11:29-05:00 Delete docs/ddd/tabla_modulo.md`
- **Veredicto**: al dia
- Resumen: La punta de origin/main (9d57572, 2026-09-13T22:11:29-05:00) es anterior al cierre y no presenta commits ni diferencias posteriores; la entrega S6 aporta mapa de contextos y auditoría con cinco no conformidades bien localizadas, pero quedan pendientes la sección 8 de arc42, el C4 nivel 3 con ADR si hubo reajuste y la evidencia pública del análisis estático.

Pendientes que siguen abiertos:
- docs/arc42/08* con lenguaje ubicuo y mapa de contextos incorporado.
- C4 nivel 3 y ADR del reajuste si los límites cambiaron respecto al corte anterior.
- URL pública del análisis de SonarCloud con rama o revisión y estado del Quality Gate.
- Columnas Requisito y C4 en docs/aspectos.md y cierre de las celdas pendientes de AS-01, AS-02 y AS-04.

## Recuento y nota sugerida

6 de 8 criterios Cumple.

**Nota sugerida preliminar (propuesta al docente; puede cambiar al cierre): 4.0 = 1 + 4 × (6/8).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- C4 nivel 3 y ADR del reajuste: no se aporta el hash revisado en S5 para calcular el diff; haría falta ese hash y el ADR del reajuste si los límites cambiaron.
- Quality Gate de SonarCloud: no se aporta la URL pública del análisis con la rama o revisión; haría falta esa URL con el estado del gate para el hash 9d57572.
- Contenido de sonar-project.properties: existe el archivo pero no viene incluido en la evidencia, así que no se puede comprobar la organización u host configurados.
- Reproducibilidad en local: no se aporta salida de ejecución propia; las filas de pruebas y pipeline se apoyan solo en los runs de CI citados.

## Hallazgos para la planilla

- El mapa de contextos tipifica relaciones Cliente/Proveedor vía la carpeta pública y reconoce un Shared Kernel mínimo en lib/core/.
- La auditoría se apoya en el código actual y convierte hallazgos reales (módulo aislado, acoplamiento de search con objects) en cinco no conformidades con plan de corrección.
- No existe docs/arc42/08*, pedido esta semana para lenguaje ubicuo y mapa de contextos.
- No hay C4 nivel 3 ni ADR de reajuste en docs/c4 y docs/adr, aunque el mapa de contextos es un documento nuevo.
- SonarCloud no queda auditable: hay scanner en el workflow y sonar-project.properties, pero no la URL pública del análisis ni el estado del Quality Gate.
- La tabla de aspectos no usa las columnas del contrato (falta Requisito y C4) y tres de sus filas tienen celdas pendientes.
- El historial aporta cinco identidades de autor; la separación entre cuentas que comparten nombre visible impide atribuciones sin más evidencia.
- Sin secretos detectados ni archivos .env versionados.
