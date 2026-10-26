# Retroalimentación publicable · UTB Tracker

## Semanas 1 y 2

## Evidencia S1

El repositorio no tenía commits antes del cierre de la semana 1, así que no hubo estado S1 que revisar: todo el montaje (ficha del problema, aspectos, registro de IA, plantilla arc42) se subió entre el 12 y el 16 de agosto, dentro de la ventana de la semana 2. Queda como semana no evaluable; si quieren que el docente lo considere recuperación, aclárenlo en el foro con el enlace al repositorio.

## Evidencia S2

Bien: secciones 1, 2 y 3 del arc42 redactadas sin texto de plantilla, restricciones clasificadas (técnicas, organizacionales y legales) y justificadas, cinco escenarios completos con sus seis partes y medida numérica, árbol de utilidad que prioriza por importancia y dificultad, y C4 de contexto.

Corregir antes del corte 1: la sección 1 debe declarar objetivos de negocio y decir a quién le importa cada uno (y revisar la tabla de interesados, que menciona nombres que no son del equipo); el ADR de `docs/adr/` debe llamarse `NNNN-titulo-en-kebab-case.md`; los enlaces de `docs/aspectos.md` apuntan a un archivo que no existe (`arc42/10_requisitos_calidad.md`) — hagan que cada escenario sea alcanzable desde su fila; entreguen el C4 también como código (el `workspace.dsl` citado no está en el repo); y en `docs/ia.md` registren qué propuestas rechazaron y por qué. Sobre todo: es urgente que todos los integrantes aparezcan en el historial de commits.

## Semana 3

Qué está bien: la sección 4 de arc42 liga tácticas a los escenarios, la matriz compara los tres estilos contra sus propios escenarios y restricciones, el ADR 0001 tiene alternativas descartadas con motivo y el esqueleto Django con sus módulos coincide con el monolito modular decidido.

Qué corregir antes del corte 1 (semana 5):
1. Completar la estructura mínima: crear `docs/c4/` para los diagramas C4 y mover `ficha_problema.md` a su carpeta.
2. Contribución: tres de cuatro integrantes siguen sin commits; todos deben aparecer en el historial antes del corte 1.
3. Registrar en `docs/ia.md` el trabajo de esta semana (ADR, matriz y esqueleto), incluyendo lo rechazado con motivo.

## Semana 4 · S4

La entrega S4 quedó incompleta al cierre: arc42 solo cubre secciones 1-4, falta el C4 nivel 2, el corte vertical no llega a persistencia y no hay glosario. El commit posterior añade C4 nivel 2, ADR 0002, persistencia y pruebas, pero el pipeline de HEAD está en rojo. Revisen que la documentación se suba antes del cierre y que el CI quede en verde. Completen docs/ia.md con lo que se rechazó y por qué. Distribuyan el trabajo: el historial muestra un solo autor. La fila A-01 de aspectos es un buen inicio; extiendan la trazabilidad al resto.

## Semana 5 · CORTE1

El proyecto avanza bien en contenido: la documentación arc42, los ADR, el C4 y el corte vertical están sólidos y el pipeline pasa. El punto crítico es la ausencia de correcciones.md, que es obligatorio para esta entrega. Deben crearlo en la raíz, documentando cómo responden a los hallazgos de S1-S4. También asegúrense de subir el PDF a Moodle y preparen la sustentación. Revisen la consistencia de nombres de autor en git para facilitar la evaluación de contribución.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

No encontramos una respuesta identificable al reto de este corte. El repositorio no tiene la etiqueta `corte-1` y no tuvo ningún cambio entre la revisión de antes del cierre y el cierre mismo: quedó igual. Sigue faltando, en este orden: (1) decir cuál fue la restricción asignada y medir cómo estaba el sistema antes de tocarlo; (2) un ADR nuevo que compare alternativas para resolver esa restricción; (3) el cambio en sí, implementado sobre el corte vertical; (4) una medición posterior contrastada contra un umbral, con el procedimiento para repetirla; y (5) una fila en `docs/aspectos.md` y una entrada en `docs/ia.md` que hablen de este trabajo, no del de semanas anteriores.

Lo que sí se sostiene de antes: la documentación base (arc42, C4, dos ADR de estilo y stack) sigue ahí y el pipeline de integración continua corre en verde sobre el estado actual. Eso es la base sobre la que debía construirse el reto, no el reto en sí.

Se mantiene, sin resolver desde el inicio del semestre, que solo una persona del equipo aparece en el historial de commits (con distintas identidades de git). Esto va a pesar cada vez más de cara al proyecto final: la nota es de equipo, pero la evidencia de trabajo debe verse repartida.

## Semana 1 · S1

Sin actividad S1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 6 · S6

Sin actividad S6: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

Por indicación docente, la matriz de S6 se completó sobre el estado actual del repositorio, sin que ello altere el registro de la ventana original.

## Semana 7 · S7

El repositorio está ordenado y la documentación base (README, ADR, aspectos, C4 nivel 2 y registro de IA) está en las rutas esperadas; el C4 de contenedores ya etiqueta sus flechas con protocolo y formato. Lo que falta es el corazón de esta entrega: un contrato OpenAPI, AsyncAPI o proto versionado en el repositorio, con rutas y esquemas, más una prueba de contrato que el workflow ejecute y que se demuestre capaz de fallar ante un cambio incompatible (run en rojo o cambio aportado como evidencia). Como FastAPI ya genera el esquema, exportarlo a un archivo versionado y validarlo con schemathesis o similar cierra varios criterios a la vez. Conviene además: hacer que el pipeline ejecute toda la carpeta de pruebas y no solo una parte, añadir el análisis estático con su URL pública y su Quality Gate, completar la sección 6 de arc42 con los flujos de interacción, registrar al menos un uso de IA rechazado con su motivo y equilibrar la contribución en el historial, hoy concentrada en una sola cuenta.

## Semana 8 · S8

La evidencia de despliegue no llegó a este corte. En el estado calificado no hay URL pública ni sistema desplegado: el README solo describe la ejecución local en el puerto 8000. Tampoco hay infraestructura como código (ningún Dockerfile, compose, Terraform, manifiestos ni Procfile), ni un procedimiento para recrear el entorno desplegado.

Además, el pipeline quedó en rojo: los últimos commits añadieron al workflow un paso de despliegue por SSH y el run de la rama principal falla. Recuperen el verde antes de seguir, corrigiendo ese paso o retirándolo del job de pruebas.

Quedan pendientes la verificación de salud, los logs estructurados, una métrica ligada a un escenario de calidad, la estimación de costo mensual con supuestos y punto de ruptura de la capa gratuita, la sección 7 de arc42 con una caja por pieza y dónde se ejecuta, la sección 2 con el límite de costo y la condición de tarjeta, y un ADR por decisión de plataforma con su alternativa descartada y la capa gratuita verificada.

Mantengan el registro de uso de IA al día (hoy no crece desde agosto y no documenta rechazos con motivo) y repartan el trabajo: dos integrantes siguen sin aparecer en el historial de commits. La higiene de secretos sí está bien resuelta: las credenciales se toman del entorno y del almacén del proveedor, sin nada versionado.

## Semana 9 · S9 (revisión definitiva)

El estado al cierre es el mismo de la semana anterior y no contiene una porción nueva S9. Falta la cadena con ADR, prueba sensible al defecto, medición y auditoría de erosión, además del registro de IA y la decisión sobre componente generativo. La reorganización y autenticación de octubre llegan después del cierre y se reconocen en el estado actual, sin cambiar esta revisión.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

El escenario está formulado, sin línea base ni resultado numérico reproducible. La integración y autenticación son parciales y no hay ADR del nuevo cambio. No se instrumentan la métrica del escenario ni logs estructurados; el despliegue sigue como plantilla.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Autorización desconectada; concurrencia y guía de persistencia divergentes.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Alta · La seguridad declarada no está conectada al camino de escritura y gestión de usuarios:** Quien alcance estas rutas de la aplicación puede invocar creación de recursos/préstamos y gestión de usuarios sin verificación de identidad/rol en el código. Es de alta prioridad por integridad y datos; no se verificó publicación ni explotación remota. Además, el camino de login no llega al servicio por sombreado del nombre. **Acción:** Conectar una dependencia de identidad y otra de roles en rutas protegidas; derivar usuario desde el token cuando corresponda. Renombrar handler/servicio de login para evitar sombreado, verificar hashes con bcrypt y añadir pruebas 401/403. No se afirma cómo están almacenadas contraseñas reales: únicamente ausencia de hash/verificación en esta cadena. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La exclusión de dos préstamos activos está validada antes de escribir, sin arbitraje atómico:** En una ejecución concurrente dos transacciones pueden leer disponible antes de que alguna actualice; no se ve bloqueo de fila, actualización condicional ni restricción única de préstamo activo. El test secuencial no demuestra la garantía nunca dos préstamos. No se observó un duplicado real. **Acción:** Proteger la decisión con UPDATE condicional y chequeo de filas afectadas o bloqueo transaccional apropiado a PostgreSQL; sumar restricción de unicidad activa donde aplique y prueba concurrente. Mantener 409 como rechazo de la operación perdedora. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Media · El arranque de persistencia ya requiere configuración aunque README promete SQLite automático:** Un clon sin DATABASE_URL no sigue el recorrido local prometido: la lectura obligatoria de la variable ocurre al importar la configuración. Esto afecta reproducibilidad del despliegue de desarrollo; no es prueba de indisponibilidad remota. **Acción:** Actualizar el contrato operativo a DATABASE_URL obligatoria y dar plantilla sin secretos, o recuperar fallback explícito y seguro solo en desarrollo. Mantener Alembic como deuda aceptada, sin presentarlo ya implementado. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

Primero recuperen el pipeline y hagan que incluya también las pruebas de contratos, préstamos y recursos. Revisen la conversión de la duración del token a número, actualicen documentación y configuración de arranque y publiquen la URL del entorno. Para el reto, falta identificar la asignación, medir línea base y resultado y añadir observabilidad y costo. La defensa queda pendiente del docente.

</details>

## Semana 11 · Integración y resiliencia

Hay idempotencia en préstamos, utilidades de resiliencia y una decisión razonada de conservar el monolito. Falta una tabla que cubra no respuesta, respuesta tardía y duplicación con mitigación individual. Las pruebas de reenvío son secuenciales y el pipeline consultado falla; no presenten la suite como verificada en verde ni las utilidades aisladas como protección aplicada a toda la integración.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

Avance preliminar: se observan transacciones locales y PostgreSQL representado en C4. Faltan tabla de garantías por operación, contraste explícito de dos operaciones y diseño de caché con invalidación o justificación de no usarla. La decisión de datos más costosa debe identificarse y justificar su reversión.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Issues al corte de consulta: **1 abiertas, 0 cerradas, 1 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Solo dirección local 127.0.0.1.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Los hotfix del 20 de octubre son posteriores al corte previo, pero el último CI sigue fallido: 17 pruebas pasan y 5 de autenticación fallan. El log registra colisión usuarios_pkey al registrar usuarios, seguida de errores de login y de lectura de id; revisar el aislamiento/siembra y secuencia de claves de PostgreSQL antes de concluir que el problema es solo Sonar. Scanner y despliegue quedaron omitidos por ese fallo. El README todavía afirma siete pruebas en verde y solo publica localhost: actualizarlo con el estado actual y la URL real bajo iscoutb.dev. Para S12, declarar garantías al crear recursos/prestar equipos, contrastarlas con transacciones/bloqueo y evidencia concurrente, justificar caché/no caché e invalidación, y comparar el costo de revertir la decisión de datos. Dividir la única issue genérica, vacía y sin asignar en tareas con aceptación y responsables.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Sin URL concreta. Solo localhost; falta URL pública concreta. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#utb_tracker) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

Se reconoce la corrección del bloqueo observado el 22 de octubre: el run de hoy registra 48 pruebas aprobadas contra PostgreSQL y deploy exitoso. Hay nuevos módulos de salones/horarios, autenticación/roles, migración Alembic y cliente Flutter. Las fixtures ya siembran sin IDs explícitos y evitan el desfase previo de secuencias. El job Sonar fue retirado, por lo que el verde actual no acredita análisis ni Quality Gate; tampoco prueba visualmente el cliente Flutter. El README permanece antiguo y sin URL pública.

**Próximos pasos:**
- Actualizar README con PostgreSQL, Alembic, módulos y resultado vigente; publicar URL oficial iscoutb.dev y evidencia separada de frontend y análisis estático.
- Para S12, explicitar garantías de crear/devolver préstamo y operaciones de salones, con pruebas concurrentes: las secuenciales no demuestran ausencia de carreras. Completar caché/no caché, ADR de reversión y arc42 §8.
- Proteger las pruebas destructivas: la fixture usa DATABASE_URL si falta TEST_DATABASE_URL antes de drop_all/create_all; exigir una base de pruebas identificada y rechazar cualquier destino de producción.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Sin URL concreta. README raíz solo publica localhost; su cifra de siete pruebas y SQLite en CI está desactualizada. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#utb_tracker) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Nuevas migraciones y ajustes de API/configuración; el cliente Android incorpora empaquetado, R8 y desactivación de copias/HTTP claro. Se publicó app-release.apk en release v1.0.2, y la punta main registra 48 pruebas backend y deploy exitosos. Esto acredita construcción/publicación del APK, no aceptación funcional en un dispositivo. README raíz sigue sin URL pública concreta; el código del cliente apunta a HTTPS nip.io, no al dominio institucional. Persiste la fixture que recurre a DATABASE_URL antes de drop_all/create_all: no está resuelto el riesgo de destino de pruebas incorrecto.

**Próximos pasos:**
- Actualizar README con URL iscoutb.dev, API, cliente Android/release y arquitectura vigente; el enlace dentro del código no sustituye el README.
- Exigir TEST_DATABASE_URL de una base aislada y rechazar destinos de producción antes de operaciones destructivas.
- Validar el APK con recorridos reales y firma de distribución apropiada: build.gradle.kts aún usa firma debug en release.
- Completar garantías/concurrencia, caché/no caché y costo de reversión de S12; un CI exitoso no reemplaza análisis estático ni aceptación móvil.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#utb_tracker) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).


## Seguimiento actual · 26 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Fusiona outbox, worker idempotente y reintentos del taller, junto con documentación de consistencia/caché y avances de administración de salones, roles y cliente. El bloqueo transitorio de múltiples cabezas Alembic ya fue corregido; la punta actual acredita 78 pruebas de tests/ sobre PostgreSQL 16 aislado y deploy con migraciones/reinicio exitosos. Ese comando excluye app/tests/ y no prueba todo el cliente. El notificador sigue simulado y el worker requiere operación separada; la caché es diseño no implementado. Persiste el fallback a DATABASE_URL de la fixture fuera de CI antes de borrar/recrear tablas.

**Próximos pasos:**
- Eliminar el fallback destructivo a DATABASE_URL o exigir validación inequívoca de BD de pruebas antes de drop_all.
- Documentar y verificar operación del worker y notificación real si se pretende incluirla en el despliegue; conservar el alcance tests/ de CI.
- Publicar URL exacta institucional en README y validar los flujos nuevos del cliente; no presentar caché propuesta como activa.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

[Fuentes y alcance](../seguimiento-s12-2026-10-26.md#utb_tracker) · [Issues](../seguimiento-issues-2026-10-26.md) · [URL y dominio](../seguimiento-despliegues-2026-10-26.md).
