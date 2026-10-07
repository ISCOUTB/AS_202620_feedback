# Evidencia S9 definitiva · ElMapita

Revisión actualizada tras el cierre del **2026-10-05T05:00:00Z** (domingo a medianoche COT).

| Campo | Valor |
|---|---|
| Repositorio | [AS_202620_ElMapita](https://github.com/ISCOUTB/AS_202620_ElMapita) |
| Rama remota principal | `main` |
| Base S5 del segundo corte | `b28e0684d4b38267c0a7d48152b0f5558a789b8c` |
| Base S8 | `e5c3ac6ecb598c8e126aaa091cce9af01fe818c4` |
| Estado revisado | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` en `origin/main` (2026-10-04T21:11:20-06:00) |
| S9 congelada | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 |
| Punta actual / S10 preliminar | `f3bcfa83e80f5c8d0e30a01b656d89160c907d64` · 2026-10-04T21:11:20-06:00 |
| Comprobación | 2026-10-06T21:27:01Z |

Revisión por Git y lectura estática; no se ejecutó código, instalación, pruebas ni despliegue de estudiantes. Una consulta de Actions por repositorio. Los procedimientos y resultados documentados por el equipo se identifican como tales; no equivalen a una ejecución del revisor. PDF excluido por decisión docente: no se abrió ni se penaliza. No se consultaron etiquetas.

## Matriz S9

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Porción real del sistema construida con apoyo de IA | Cumple | Nueva política de precisión y caso de uso en el módulo Ubicacion, con apoyo IA explícito; [backend/src/modules/ubicacion/domain/accuracy-policy.ts:1–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/domain/accuracy-policy.ts#L1-L26), [backend/src/modules/ubicacion/application/get-validated-location.use-case.ts:15–43](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/application/get-validated-location.use-case.ts#L15-L43), [docs/ia.md:399–413](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L399-L413). También hay corrección real de mapas por error 500. Límite: el controlador aún llama al caso de uso anterior, no al validador nuevo. |
| Cadena completa navegable para esa porción | No cumple | La fila EC-03 mantiene rutas antiguas de implementación en texto; menciona la prueba nueva pero no enlaza la política/caso de uso nuevo ni completa medición de fallback UI. Las otras filas conservan pruebas pendientes; [docs/aspectos.md:3–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L3-L8). Registrar el proveedor no completa la cadena funcional. |
| ADR con la decisión argumentada por el equipo | Cumple | La decisión vigente de monolito, desacoplo y fallback se confirma formalmente en ADR-0005; ADR-0006 explicita el contrato y correcciones de rutas/DI. Son decisiones del equipo aplicadas al nuevo trabajo, [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:13–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L13-L33), [docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md:17–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md#L17-L26). |
| Prueba que falla ante el defecto que cubre | Cumple | Logs versionados y commits del defecto de borde: rojo para accuracy<15 en 7d64d5f, corrección <=15 en cac2f97; [docs/evidencia/s9-run-rojo.txt:1–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-run-rojo.txt#L1-L26), [docs/evidencia/s9-run-verde.txt:1–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-run-verde.txt#L1-L8), [backend/src/modules/ubicacion/domain/accuracy-policy.ts:18–25](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/ubicacion/domain/accuracy-policy.ts#L18-L25). Se acredita evidencia documentada, sin ejecutar pruebas. |
| Medición del escenario asociado | Cumple | Hay medición nueva de la porción mapas que detectó defecto y motivó corrección: benchmark 30 peticiones, p95=1637 ms frente a 5000, pero todas fallan y cumple=false; [docs/evidencia/s9-ec01-benchmark.json:1–15](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/evidencia/s9-ec01-benchmark.json#L1-L15), [docs/ia.md:428–430](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L428-L430). Se cumple documentar y contrastar la medición, NO el escenario de calidad. EC-03 en UI sigue sin medición completa. |
| docs/ia.md con lo aceptado, lo corregido y lo rechazado con motivo | Cumple | Aceptado, correcciones concretas, y rechazo de datos inventados/dependencia innecesaria con motivo técnico; [docs/ia.md:404–419](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L404-L419). Seguimiento distingue fallos del arnés y del producto, [docs/ia.md:456–469](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L456-L469). |
| Auditoría de erosión sobre límites de contexto y propiedad de datos | Cumple | Auditoría con ubicaciones, propiedad de datos, hallazgos y acciones. Se corrige política EC-03 y tratamiento de falta de modelo; otras deudas se reconocen abiertas. [docs/auditoria-erosion-s9.md:1–16](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/auditoria-erosion-s9.md#L1-L16), [backend/src/modules/mapas/infrastructure/storage/supabase-storage.ts:22–30](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/mapas/infrastructure/storage/supabase-storage.ts#L22-L30). No implica que toda erosión quede corregida. |
| Dependencias propuestas verificadas en su registro oficial | Cumple | La nueva dependencia es integration_test de desarrollo, procedente del SDK Flutter: [frontend/pubspec.yaml:53–57](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/frontend/pubspec.yaml#L53-L57) y [docs/ia.md:452–456](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L452-L456). Verificada contra [documentación oficial Flutter](https://docs.flutter.dev/testing/integration-tests), que la declara con sdk: flutter. El validador backend no añadió paquetes; no se exige un diff artificial. |
| Sin credenciales en código, ejemplos ni documentación generada | Cumple | Barrido del snapshot en código, ejemplos y docs sin secretos reales; claves Supabase se reciben por configuración y SONAR_TOKEN desde almacén. [backend/src/shared/supabase/client.ts:11–25](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/shared/supabase/client.ts#L11-L25), [.github/workflows/ci.yml:274–283](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L274-L283). Los tipos password/token y fixtures no son credenciales activas. |
| Componente generativo evaluado, con costo y latencia, o ADR de no incorporarlo | Cumple | ADR-0007 compara alternativas y justifica no incorporar modelo generativo frente a latencia, offline, costo, determinismo y privacidad; [docs/adr/0007-no-incorporar-componente-generativo.md:12–40](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0007-no-incorporar-componente-generativo.md#L12-L40). |

## Matriz transversal · CONTRATO §11

| Criterio | Estado | Evidencia y observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Repositorio público ISCOUTB/AS_202620_ElMapita, rama main; [README.md:1–7](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/README.md#L1-L7). |
| Estructura mínima presente | Cumple | README, arc42 en plantilla única, ADR, C4, aspectos e IA presentes; [docs/aspectos.md:1–8](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/aspectos.md#L1-L8). |
| Estado calificado identificable | Cumple | Hash main congelado y fecha en encabezado; coincide con punta actual. |
| Nombres de ADR según la convención | Cumple | ADR-0001 a 0007 usan NNNN-kebab-case; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:1–11](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L1-L11). |
| ADR aceptados no reescritos | Cumple | Se verificó diff de ADR-0001 contra aa16382 y ADR-0003 contra afae3be: únicamente cambia status a Superseded. Los cambios viven en ADR-0005/0006; [docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md:13–33](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0005-reemplazo-adr-0001-estilo-arquitectonico.md#L13-L33), [docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md:13–26](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/adr/0006-reemplazo-adr-0003-contrato-openapi.md#L13-L26). Arrastre corregido, sin borrar que ocurrió históricamente. |
| docs/ia.md al día para la semana | Cumple | Entradas S9 distinguen aceptado, corregido y rechazos técnicos, incluidas mediciones falsas y pruebas que no representan producto; [docs/ia.md:395–419](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L395-L419), [docs/ia.md:452–469](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L452-L469). |
| Pipeline, SonarCloud y Quality Gate públicos (desde S6) | No cumple | Workflow CI general success, pero Sonar es no bloqueante y está excluido del fallo del gate; [.github/workflows/ci.yml:254–283](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L254-L283), [.github/workflows/ci.yml:297–313](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/.github/workflows/ci.yml#L297-L313). El equipo documenta fallo por permisos, [docs/ia.md:434–439](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L434-L439); no se acredita análisis/Gate ejecutado. |
| Sin credenciales en el repositorio ni en el historial | No verificado | Snapshot sin valores de credencial reales. Gitleaks excluye fingerprints de ejemplos y projectKey públicos; historial completo independiente no certificado. |
| Contribución de todos los integrantes | No verificado | Cuatro firmas visibles tras .mailmap: 40 commits agregados. La correspondencia RobotDRMX con integrante queda explícita en .mailmap, pero no se inventa un mapa completo del resto; [docs/ia.md:397–402](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L397-L402). |

## Actions en el estado congelado

- [CI: success](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/37258414405), 2026-10-05T03:11:23Z, SHA exacto del estado indicado.
## Alcance del barrido de seguridad
Se revisó el texto del snapshot, incluidos ejemplos/docs. Las coincidencias corresponden a interfaces password/token, variables de entorno, fixtures y referencias al almacén de Actions. No hay .env versionado. Las exclusiones de gitleaks para projectKey/documentación deben seguir justificadas; no se certifica el historial exhaustivo independiente.

## Estado global del proyecto (overall · punta actual)

El avance S9 es sustantivo y honesto sobre sus límites: nuevo validador, rojo→verde documentado, corrección 500→404, pruebas en dispositivo y ADR sustitutos. La medición descubre defectos reales, no demuestra éxito del producto: EC-04 falla 20/20 y el rendimiento de un placeholder no representa render 3D. El validador está registrado pero el controlador sigue usando el caso de uso anterior. La punta coincide con S9, y SonarCloud está no bloqueante pese al CI general verde.

El delta S9 contiene 9 commits respecto de S8; hay 0 commits posteriores a S9 en la misma rama. Los cambios tardíos solo afectan este overall y el avance S10, nunca el recuento congelado.

## Recuento y nota sugerida

**9 de 10 criterios Cumple. Nota sugerida: 4.6 = 1 + 4 × (9/10).** Propuesta al docente; la nota final se fija en Moodle. La matriz transversal no integra este cálculo.

## Acciones prioritarias

- Integrar GetValidatedLocationUseCase en el recorrido real y medir el fallback de Flutter; no basta registrarlo como provider.
- Completar enlaces de código/pruebas/medición y actualizar EC-03 hacia los archivos nuevos.
- Corregir acceso a modelo/edificio, repetir EC-01 con respuestas exitosas y medir render 3D real; implementar caché de datos y banner offline antes de cerrar EC-04.
- Resolver permiso de análisis SonarCloud con quien administra la organización; retirar continue-on-error solo cuando exista run/Gate verificable.
- Aportar consigna oficial S10 y conectar hipótesis, línea base, cambio y experimento con esa asignación.

## Hallazgos cerrados con evidencia nueva

- Arrastre de reescritura de ADR-0001/0003 corregido: restaurados textos aceptados y sustitución explícita por 0005/0006, comprobada por diff.
- Se corrige la anterior falta de atribución de RobotDRMX mediante .mailmap explícito; no corresponde mantener afirmación de cero contribuciones de esa persona.
- Existen porción S9, prueba negativa, auditoría y ADR de no incorporar IA generativa; [docs/ia.md:395–419](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/docs/ia.md#L395-L419).
- El error genérico al faltar un modelo se convierte en NotFoundException y tiene prueba; [backend/src/modules/mapas/infrastructure/storage/supabase-storage.ts:22–30](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/f3bcfa83e80f5c8d0e30a01b656d89160c907d64/backend/src/modules/mapas/infrastructure/storage/supabase-storage.ts#L22-L30). No se afirma recuperación operativa sin re-medición.
