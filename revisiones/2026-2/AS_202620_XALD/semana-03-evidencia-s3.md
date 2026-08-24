# Evidencia S3 · XALD

## Datos

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_XALD` |
| Estado revisado | `dc38992cc567c383c911453e94e4ef41f0a85003` · 2026-08-23T22:07:19-05:00 («Update README.md») |
| Cierre | 2026-08-24T05:00:00Z |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. Sin llamadas a la API (no hay `.github/workflows/`). |
| Nota de actualización | **Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo.** La primera revisión fue sobre `4814026` (21:24 COT); el equipo siguió hasta las 22:07, dentro del cierre, y subió el esqueleto Android/Kotlin que faltaba. Sin commits posteriores al cierre. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/arc42/arc42-template-EN.md:135-146` | Cumple | «Solution Strategy» liga tácticas concretas a las metas de calidad (Sync Queue con LWW para consistencia, AES-256/KeyStore para seguridad, regex+IA híbrido para resiliencia, BroadcastReceiver para captura). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | `docs/matriz-comparativa-estilos.md` | No cumple | La matriz es detallada y específica del proyecto (Gemini, Offline-First, SMS, esfuerzo/beneficio), pero no existe árbol de utilidad en el repo y no compara escenario por escenario; tampoco hay archivo de escenarios. Nota: el encabezado dice «decisión del ADR 0001» cuando la decisión es el ADR-006. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/ADR-001.md` … `ADR-006.md` | No cumple | Formato `ADR-NNN.md`, sin kebab-case ni título en el nombre; los 6 fallan el filtro del CONTRATO §4. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/ADR-006.md` | Cumple | Contexto y problema, Opciones evaluadas, Decisión tomada (monolito modular), Justificación técnica, Consecuencias (positivas + riesgos con mitigación). |
| Alternativas descartadas con su motivo | `docs/adr/ADR-006.md` + `docs/matriz-comparativa-estilos.md` | Cumple | Capas y hexagonal con desventajas y relación esfuerzo/beneficio en la matriz, referenciada desde el ADR. |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` | No cumple | La columna ADR sigue con números sueltos («002», «001», «004») sin enlaces, no aparece el ADR-006, y el archivo conserva el resto `[cite: 1]`. No hay archivo de escenarios que enlace el ADR. |
| Arranque con un solo comando documentado en el README | `README.md` («Comandos de Ejecución y Verificación») + `XALDAPP/gradlew.bat` | Cumple | Documenta el comando único (`gradlew.bat -p XALDAPP test`) por SO, con salida esperada. Nota: es el comando de pruebas/verificación; el arranque de la app en emulador no queda como comando único documentado. No ejecutado (regla del kit). |
| Prueba automatizada en verde | `XALDAPP/app/src/test/java/com/proyecto/xald/Entornotest.kt` + `ExampleUnitTest.kt` | No verificado | Las pruebas existen y el README muestra una «salida esperada» (BUILD SUCCESSFUL), pero no hay pipeline ni URL de run ni artefacto de ejecución verificable. |
| Estructura de paquetes correspondiente al estilo del ADR | `XALDAPP/app/src/main/java/com/proyecto/xald/{parser,corefinanciero,syncqueue,aigemini}/` | Cumple | Coincide exactamente con el esqueleto de paquetes del ADR-006. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación; `ISCOUTB/AS_202620_XALD`. |
| Estructura mínima presente | Cumple | Las seis rutas presentes; ahora además con `docs/c4/c4.md` en su carpeta. |
| Estado calificado identificable | Cumple | `dc38992` · 2026-08-23T22:07:19-05:00 ≤ cierre; sin etiqueta (evidencia semanal). |
| Nombres de ADR según la convención | No cumple | `ADR-NNN.md` no pasa el filtro `^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$`. |
| ADR aceptados no reescritos | Cumple | ADR-001 a 005 con un commit cada uno; ADR-006 editado el mismo día de creación (23-ago) en fase de redacción, antes de cualquier aceptación/revisión. |
| `docs/ia.md` al día para la semana | No cumple | Último commit sobre el archivo: `06b7696` (2026-08-16); sin entradas del trabajo S3 (ADR-006, matriz, esqueleto). |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. `local.properties` solo contiene la ruta del SDK, sin credenciales — igual debe salir del versionado. |
| Contribución de todos los integrantes | Cumple | 4 identidades: dilanbejarano011 (39), colmenares2007-crypto (17), xaviergarciadiaz20-commits (17), axeljruiz717-hash (7) = los 4 integrantes. |

## Recuento

**5 de 9** criterios de la ficha cumplidos (3 no cumplidos, 1 no verificado).

## No verificado / pendientes

- Pruebas en verde: `gradlew test` no se ejecutó (regla del kit) y no hay pipeline ni run aportado; el README muestra una salida esperada que no constituye evidencia verificable.

## Hallazgos para la planilla

- Sin commits tardíos: todo entró antes del cierre (bien).
- El esqueleto ya existe (Android/Kotlin con los paquetes del ADR-006) pero el verde de las pruebas sigue sin evidencia.
- Renombrar los ADR a `NNNN-titulo-en-kebab-case.md` (los 6).
- `aspectos.md`: enlazar la columna ADR de verdad, incluir el ADR-006 y limpiar el resto `[cite: 1]`.
- Subir el árbol de utilidad y los escenarios de calidad (pendientes desde S2) y anclar a ellos la matriz comparativa; corregir la referencia «ADR 0001» → ADR-006 en la matriz.
- Sacar del versionado los artefactos de build: `.gradle/`, `build/`, `XALDAPP/.idea/` y `local.properties` (`.gitignore` de XALDAPP no cubre la raíz del repo).
- `docs/ia.md`: añadir las entradas del trabajo de esta semana con lo rechazado y su motivo.

## Estado del contrato del repositorio

Ver la matriz transversal arriba.
