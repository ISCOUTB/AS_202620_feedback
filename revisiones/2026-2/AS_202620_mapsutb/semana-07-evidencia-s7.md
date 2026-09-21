# semana-07-evidencia-s7 · mapsutb

> Revision automatica definitiva (GitHub Actions, posterior al cierre). Re-evaluada por cambio de hash calificado tras la pasada temprana.

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `5e2fdd5` en `origin/master` (2026-09-20T21:15:28-05:00) |
| Cierre | 2026-09-21T05:00:00Z |
| Revisor | pipeline automatico (GitHub Actions) |

## Matriz de la ficha

| Criterio de evaluacion | Evidencia tecnica | Estado | Observaciones |
|---|---|---|---|
| Contrato en formato ejecutable versionado en el repositorio | docs/api/apis-externas.openapi.yaml (openapi: 3.0.3) presente en el arbol de 5e2fdd5. | Cumple | Es un contrato de consumidor de las tres APIs HTTP reales; Maps SDK queda fuera por consumirse como SDK nativo. |
| Contrato con rutas y esquemas de datos, no solo listado de endpoints | Tres rutas (/maps/api/geocode/json, /maps/api/staticmap, /mp/collect) y components/schemas con GeocodingResponse, GeocodingResult, LatLng y MeasurementProtocolEvent. | Cumple | Los esquemas declaran required, enum y tipos; no es un listado de endpoints. |
| Correspondencia entre el contrato y la API implementada | El arbol de 5e2fdd5 muestra lib/adapters/geocoding_adapter.dart, static_map_adapter.dart y analytics_adapter.dart, y el ADR 0005 los enlaza al contrato. | No verificado | No se aporto el contenido de los adaptadores: haria falta citar dos rutas del contrato dentro del codigo y una del codigo dentro del contrato. |
| Versión de la API declarada y con historial | info.version: "1.0.0" en docs/api/apis-externas.openapi.yaml, archivo versionado en el HEAD calificado. | Cumple | No se aporto la salida de git log del archivo, asi que la evolucion de la version no se pudo citar. |
| Prueba de contrato presente | test/geocoding_adapter_contract_test.dart, test/static_map_adapter_contract_test.dart y test/analytics_adapter_contract_test.dart en el arbol de 5e2fdd5. | Cumple | Tres pruebas, una por integracion HTTP del contrato. |
| El pipeline ejecuta la prueba de contrato | Existe .github/workflows/ci.yml en el arbol revisado. | No verificado | No se aporto el contenido del workflow ni URL de run; haria falta la linea que invoca la prueba de contrato y el run (nombre, conclusion, URL) del hash 5e2fdd5. |
| Evidencia de que la prueba falla ante un cambio incompatible | El historial muestra 2f8f9ea ('test: simula cambio incompatible en Google Geocoding API') revertido en 5e2fdd5, HEAD calificado. | No verificado | No hay run en rojo ni evidencia de ejecucion aportada; el commit revertido no acredita el fallo, queda como pregunta de sustentacion. |
| ADR de la estrategia de integración ligado a un escenario | docs/adr/0005-integracion-apis-externas.md decide integracion sincrona request/response justificada contra el Escenario 3 de docs/escenarios_calidad.md. | Cumple | Incluye alternativa asincrona por eventos descartada y consecuencias de acoplamiento. |
| arc42 sección 6 con los flujos de interacción | docs/arc42/06_runtime_view.md describe los flujos 'Trazar una ruta', 'Geocodificar una ubicacion' y 'Perdida de disponibilidad' con diagramas de secuencia. | Cumple | Los flujos cubren exito y escenario de error de red. |
| C4 nivel 2 con protocolo y formato en cada flecha | docs/arc42/05_building_block_view.md: diagrama C4Container con Rel etiquetados ('HTTPS, JSON (REST)', 'HTTPS, PNG (Static Maps API)', 'Sistema de archivos, JSON'). | Cumple | El nivel 2 vive en arc42/05 y no en docs/c4/C2.md: desviacion de ruta, no ausencia del artefacto. |

## Matriz transversal (CONTRATO §11)

| Criterio | Evidencia | Estado | Observaciones |
|---|---|---|---|
| Identidad del repositorio | repo visible ISCOUTB/AS_202620_mapsutb, rama origin/master; 4 identidades de git consolidadas en el historial (duplicados por correo unificados): CarlosManrique-1397, i-matallana, charlygz21 (tambien como 'charly') y nerlis-otero. | Cumple | Coincide el numero de cuentas con los 4 integrantes declarados, sin atribuir cuentas a personas por parecido de nombre; la pertenencia a la organizacion no se pudo comprobar. |
| Estructura mínima | Existen docs/arc42/ (01 a 12), docs/adr/ (0001 a 0005), docs/c4/ (C1, C2, C3, Contexto), docs/aspectos.md, docs/ia.md y README.md en el arbol de 5e2fdd5. | Cumple | Mezcla de .adoc y .md en arc42 y copia suelta lib/models/05_building_block_view.md fuera de docs/. |
| Convenciones de ADR | Cinco ADR numerados en kebab-case (0001-patrones-de-diseno.md ... 0005-integracion-apis-externas.md), con contexto, opciones, decision y consecuencias. | Cumple | El ADR 0001 se declara 'revisado' tras su aceptacion y no marca reemplazo explicito; ninguno lista commit/PR ni pruebas en una seccion de trazabilidad. |
| La tabla de aspectos | docs/aspectos.md existe y el commit 8695fff dice 'agrega A-02 a aspectos.md'; el ADR 0001 cita el escenario A-01. | No verificado | No se aporto el contenido del archivo: haria falta citar las ocho columnas (ID, Aspecto, Requisito, C4, ADR, Codigo, Pruebas, Evidencia) y verificar que no hay celdas huecas. |
| Registro de uso de IA | docs/ia.md existe y su historial crece: commits f829f2e (09/08), a6e51bc (23/08), 098ac4e (28/08) y 3d4b0c9 (30/08). | No verificado | No se aporto el contenido: haria falta verificar, por uso, herramienta, lo aceptado y lo rechazado con su motivo tecnico. |
| README | README.md declara que es el sistema, requisitos previos, arranque con un solo comando (./scripts/start.sh) y como se prueba (flutter pub get && flutter test). | Cumple | La seccion 'Estado actual' sigue diciendo 'sin logica de negocio' y 'una prueba', desactualizada frente a los adaptadores y pruebas de contrato existentes. |
| Pipeline y análisis estático | Se esperaba la linea del workflow que invoca el scanner, la URL del run exitoso y la URL publica del analisis con Quality Gate; solo se encontro .github/workflows/ci.yml, .github/workflows/sonar-sync-issues.yml y sonar-project.properties. | No cumple | No se aporto ninguna URL de run ni de analisis; el workflow de sincronizacion de issues no prueba que SonarCloud se ejecute. |
| Secretos | La revision reporta 'sin coincidencias' para patrones de credenciales y envs_versionados vacio en el HEAD calificado. | Cumple | Sin incidentes de secretos en el arbol revisado. |

## Estado global del proyecto (overall · punta actual de la misma rama)

Mira el repositorio **entero en la punta actual de la misma rama**, no solo la evidencia del cierre: si el equipo subio tarde o corregio entregas anteriores, aqui se nota.

- **Punta actual revisada**: `5e2fdd594ced94f748cd50962fe8bfc71e8c2cf9 2026-09-20T21:15:28-05:00 Revert "test: simula cambio incompatible en Google Geocoding API (evidencia de corrida en rojo)"`
- **Veredicto**: con pendientes
- Resumen: El proyecto en HEAD (5e2fdd5, 2026-09-20T21:15:28-05:00, origin/master) tiene contrato OpenAPI ejecutable con esquemas, ADR 0005 bien argumentado, arc42 seccion 6 con flujos y C4 nivel 2 etiquetado; el README documenta arranque y pruebas y no hay secretos. Falla la evidencia de ejecucion: no hay run que muestre la prueba de contrato corriendo en CI ni fallando ante un cambio incompatible, y no hay evidencia auditable de SonarCloud. La tabla de aspectos y el registro de IA no se pudieron verificar por falta de contenido aportado.

Pendientes que siguen abiertos:
- Evidencia de que la prueba de contrato falla ante un cambio incompatible (run en rojo o evidencia aportada).
- Linea del workflow y URL del run que ejecuta la prueba de contrato sobre el hash revisado.
- Evidencia auditable de SonarCloud: invocacion del scanner, run exitoso y URL publica del analisis con Quality Gate (exigida desde S6).
- Contenido verificable de docs/aspectos.md con las ocho columnas y de docs/ia.md con lo rechazado y su motivo.

## Recuento y nota sugerida

7 de 10 criterios Cumple.

**Nota sugerida (propuesta al docente, publicada por decision del profesor): 3.8 = 1 + 4 × (7/10).** La nota final la fija el profesor en Moodle.

## No verificado / pendientes

- Correspondencia contrato-codigo: falta el contenido de lib/adapters/geocoding_adapter.dart, static_map_adapter.dart y analytics_adapter.dart para citar las rutas literales.
- Ejecucion del pipeline: falta el contenido de .github/workflows/ci.yml y la URL del run del hash 5e2fdd5.
- Prueba de contrato en rojo: falta un run con conclusion 'failure' o evidencia del cambio incompatible que la hizo fallar.
- docs/aspectos.md: falta su contenido y la verificacion de las ocho columnas.
- docs/ia.md: falta la columna de lo rechazado y su motivo tecnico.
- Historial del contrato: falta la salida de git log -- docs/api/apis-externas.openapi.yaml.

## Hallazgos para la planilla

- El contrato OpenAPI 3.0.3 cubre las tres integraciones HTTP reales con rutas y esquemas de datos, no solo endpoints.
- Las tres pruebas de contrato existen en test/, pero ningun run ni URL acredita que el pipeline las ejecute.
- El commit que simulaba el cambio incompatible (2f8f9ea) fue revertido en el HEAD calificado (5e2fdd5), sin run en rojo que lo respalde.
- El ADR 0005 justifica la integracion sincrona contra el Escenario 3 e incluye la alternativa asincrona descartada.
- El C4 nivel 2 con protocolo y formato por flecha esta en docs/arc42/05 y no en docs/c4/C2.md.
- No hay evidencia de ejecucion ni URL publica de SonarCloud (Quality Gate) para el hash revisado.
- Sin secretos versionados ni archivos .env en el repositorio.
- No hay commits posteriores al cierre en origin/master.
