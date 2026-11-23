# uniTeam · Retroalimentación de cierre S16

**Evidencia evaluada.** Rama principal `master`, [candidato S16 `469517a59d8bb1f8a1c31db118bfac2934b44624`](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/469517a59d8bb1f8a1c31db118bfac2934b44624). [Comparación con S10 `6e04b35`](https://github.com/ISCOUTB/AS_202620_uniTeam/compare/6e04b35317a0a68d239ae85c71cd60e21982b195...469517a59d8bb1f8a1c31db118bfac2934b44624). Aunque `1e6b69b` tiene fecha de commit 22 de noviembre 23:59:03 COT, [la corrida de push](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/45114996799) lo sitúa primero en `cierre/s16-s17` a las 23:59:10 COT; el [PR #38](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/38) se integró a `master` a las 00:03 COT, después del cierre. Se usa el SHA de la rama principal observado en remoto al corte, sin certificar el envío en SAVIO.

### Alcance y decisiones

Se conserva la separación de Tareas y Proyectos acordada para S10, con FastAPI/Next/MySQL/Auth0 y bus de eventos síncrono. S16 añade WebSocket, rediseño de interfaz Atlas y trabajo en sesión, seguridad y límites. No confundan notificación WebSocket con una cola durable; el ADR 0015 delimita el ejercicio de colas respecto a producción. El ADR 0016 reafirma MySQL y el 0017 separa el CSS por capas. Hay decisiones con números repetidos (0010, 0011 y 0012); usen nombres inequívocos y enlacen al documento exacto. El flujo de estados asociado al ADR 0012 sí aporta una comprobación histórica de modificabilidad: un componente de dominio afectado y ningún cambio incompatible de contrato reportado.

### arc42, C4 y trazabilidad

El [arc42 integrado](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/469517a59d8bb1f8a1c31db118bfac2934b44624/docs/arc42/arc42-uniteam.md) reúne secciones 1–12 y glosario; hay C4 de contexto y contenedores, más la vista de bloques internos de la API en la sección 5. Hagan explícita la referencia a componentes y la cobertura de WebSocket y frontend: no basta que el lector infiera esas responsabilidades a partir del diagrama de la API.

En la [matriz de 12 aspectos](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/469517a59d8bb1f8a1c31db118bfac2934b44624/docs/aspectos.md), A-04 recoge la modificabilidad de un módulo; A-06 reporta p95 de 762 ms en un benchmark frente al umbral de 2 s; A-12 reporta p95 de 11,8 ms en SQLite, no en MySQL desplegado. A-07 y A-09 sí llevan a pruebas de aislamiento/OIDC; en contraste, A-05 acredita persistencia pero no recuperabilidad, A-01/A-03 no muestran medición de usabilidad y A-10 no identifica requisito. La [bitácora de IA](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/469517a59d8bb1f8a1c31db118bfac2934b44624/docs/ia.md) se considera evidencia de proceso, no sustituto de las pruebas.

### Qué se verificó y qué falta demostrar

- **CI del SHA exacto:** [corrida 45104471750](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/45104471750) en verde, con contrato e integración usando MySQL, validación de enlaces, build de imágenes y validación frontend. [Auditoría 45104471698](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/45104471698) y [Sonar Quality Gate](https://github.com/ISCOUTB/AS_202620_uniTeam/runs/137462740169) en verde. Esas señales no sustituyen un ejercicio de recuperación o una medida de WebSocket en producción.
- **Despliegue:** el [README del corte](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/469517a59d8bb1f8a1c31db118bfac2934b44624/README.md) referencia [web](https://uniteam-web.iscoutb.dev) y [API](https://uniteam-api.iscoutb.dev); el workflow de salud apunta al dominio nuevo. Las comprobaciones programadas de URL no establecen que ese SHA esté sirviendo, y no se hizo una prueba independiente del despliegue.
- **Colaboración:** 47 commits en la comparación, incluidos merges; no permiten acreditar por sí solos reparto o revisión.

**Prioridad:** hacer reproducible la recuperación (no solo persistencia), aportar una comprobación frontend→API→MySQL en el ambiente publicado e identificar el SHA servido.

### Preguntas de sustentación

1. Si un cliente WebSocket se desconecta después de un cambio pero antes de recibir la notificación, ¿cómo reconstruye su estado y cómo prueban que no duplica eventos?
2. Durante una caída breve de MySQL, ¿qué diferencia hay entre recuperar la entidad y recuperar su registro de auditoría? ¿Qué observarían para demostrar ambas propiedades?
3. Si Auth0 no responde o expira la sesión durante la operación, ¿qué recibe el usuario y cómo comprueban que otro usuario no ve sus tareas o notificaciones?

### Propuesta técnica de rúbrica (sin nota final)

- C1: pendiente de desafío asignado y demostración.
- C2: Competente — evolución motivada; queda por demostrar confirmación explícita de decisión.
- C3: Competente provisional — p95 A06, MySQL/OIDC y aislamiento; recuperación no demostrada.
- C4: Básico — brechas de recuperación, requisito y cobertura C4.
- C5: reservado al docente. Total pendiente.

## Verificación independiente del corte y del despliegue

El commit 1e6b69b salió a la rama de trabajo a las 04:59 UTC; el [PR #38](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/38) se integró a las 05:03 UTC. No pertenece al master del corte.

**Sondas de solo lectura del 23 de noviembre:**

- web: [https://uniteam-web.iscoutb.dev/](https://uniteam-web.iscoutb.dev/) → HTTP 200 (13:28:14 UTC).
- API salud: [https://uniteam-api.iscoutb.dev/health](https://uniteam-api.iscoutb.dev/health) → HTTP 200, versión declarada `0.2.0` (sin SHA) (13:28:13 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
