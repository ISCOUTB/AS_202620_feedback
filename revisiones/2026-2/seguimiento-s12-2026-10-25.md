# Seguimiento de los 23 proyectos · 25 de octubre de 2026

Consulta del **25 de octubre de 2026**, desde las 08:02 COT (13:02 UTC), sobre los 23 proyectos del listado vigente. Seguimiento documental, no recalificación. **S12 continúa abierta** durante este corte; no se cierra automáticamente. Se conservan calificaciones, planillas, matrices y cortes históricos.

**45 abiertas y 130 cerradas** (129 completed; 1 duplicate); 21 abiertas sin asignar. Pull requests excluidas.

README: **9 institucional; 7 sin url concreta; 7 externo**. Las direcciones institucionales incluyen APIs, no prueban que toda interfaz esté publicada.

Se conservan las confirmaciones del docente: **TAIA y ElMapita presentaron y funcionan; ROUTB entregó avance; PideUtb presentó actualización y tiene despliegues; Recobra presentó**. Estas declaraciones no son pruebas funcionales automatizadas de este corte.

Se leyeron repositorios y resultados de GitHub sin ejecutar código estudiantil ni modificar sus issues o despliegues. Los PDF se excluyen. Código fusionado, CI, publicación y aceptación funcional son evidencias distintas. No se repitieron pruebas funcionales en vivo. No se obtuvieron estados personalizados de GitHub Projects; OPEN/CLOSED y motivos de cierre pertenecen a issues, no a columnas de tablero.

[Issues y motivos de cierre](seguimiento-issues-2026-10-25.md) · [README y despliegues](seguimiento-despliegues-2026-10-25.md) · [Corte anterior](seguimiento-s12-2026-10-24.md)

<a id="audioshare"></a>

## AudioShare

Rama **master**, [1af6e5ca727e60ef64cda6e31af71ab73bc9c9da](https://github.com/ISCOUTB/AS_202620_AudioShare/commit/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da), fecha del commit 2026-10-19T06:41:04Z (UTC).

Sin nueva punta ni cambio de README desde el 24/oct. CI, Flutter y publicación de imagen de la misma punta continúan exitosos. README distingue la URL institucional y el cliente legado servido por la imagen de Flutter web compilado en CI.

**Próximos pasos:**
- Mantener pendientes S12 del 24/oct: tabla por operación, separación SQLite/NDJSON, invalidación de /track y ADR de costo de reversión.
- Actualizar contradicciones del README sobre audio simulado/real y conservar alcance de cliente legado.

**Issues GitHub:** 2 abiertas / 2 cerradas; 2 abiertas sin asignar. Motivos: 2 completed.

**README:** Institucional. API y cliente legado; no Flutter web en imagen

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/2): fusionada 2026-09-01T14:56:35Z; [#1](https://github.com/ISCOUTB/AS_202620_AudioShare/pull/1): fusionada 2026-08-31T03:06:48Z.

**CI consultado:** [Publicar imagen](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299344): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299270): success (misma punta); [Flutter](https://github.com/ISCOUTB/AS_202620_AudioShare/actions/runs/39211299234): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_AudioShare/blob/1af6e5ca727e60ef64cda6e31af71ab73bc9c9da/README.md)

<a id="clubs_utb"></a>

## Clubs UTB

Rama **master**, [db563fdaa2056a0cfea93cba896ebe4cdd71993b](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/commit/db563fdaa2056a0cfea93cba896ebe4cdd71993b), fecha del commit 2026-10-25T08:04:49Z (UTC).

Avance integrado en master: nuevos modelos PostgreSQL, autenticación JWT local y feed Flutter; la ruta de publicaciones usa ahora SQLAlchemy directamente, por lo que ya no corresponde describirla solo como adaptador en memoria. Sin embargo, publicacion_router.py:135 contiene el operador ??, inválido en Python; el código guarda y compara la contraseña sin hash en auth_router.py:62,81 y usa un valor JWT predeterminado si falta configuración. La cabecera de idempotencia se recibe pero no se aplica al guardar en las rutas nuevas. Los dos workflows del head fallan sin jobs devueltos; no se atribuye esa ausencia de jobs al error de Python sin evidencia del run. README aún describe Supabase y no publica URL concreta. La nueva tabla de consistencia expresa propuestas, no prueba su implementación.

**Próximos pasos:**
- Corregir sintaxis del router y obtener ejecución de pruebas/contrato sobre el head, separando fallo del workflow de defectos estáticos.
- Aplicar hash de contraseñas y verificación segura, exigir configuración JWT sin valor predeterminado y probar autenticación.
- Restituir idempotencia efectiva en la ruta PostgreSQL con restricción/transacción; alinear tabla S12, contrato, C4/arc42 y README, incluida URL iscoutb.dev.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#3](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/3): fusionada 2026-10-05T05:46:36Z; [#2](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/2): fusionada 2026-09-21T04:56:52Z; [#1](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/pull/1): abierta.

**CI consultado:** [.github/workflows/contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40175238694): failure (misma punta); [.github/workflows/backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/actions/runs/40175237997): failure (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/README.md) · [publicacion_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/backend/src/linkclub/adapters/inbound/api/publicacion_router.py) · [auth_router.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/backend/src/linkclub/adapters/inbound/api/auth_router.py) · [main.py](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/backend/src/linkclub/main.py) · [tabla_garantia_consistencia.md](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/docs/arc42/tabla_garantia_consistencia.md) · [backend-tests.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/.github/workflows/backend-tests.yml) · [contrato.yml](https://github.com/ISCOUTB/AS_202620_Clubs_UTB/blob/db563fdaa2056a0cfea93cba896ebe4cdd71993b/.github/workflows/contrato.yml)

<a id="dinamikutb"></a>

## Dinamik

Rama **master**, [8dad79338a66cd7054a0bde3f98661f785f5c378](https://github.com/ISCOUTB/AS_202620_DinamikUTB/commit/8dad79338a66cd7054a0bde3f98661f785f5c378), fecha del commit 2026-10-24T05:05:10Z (UTC).

Sin nueva punta ni cambio de README desde el 24/oct. F7 continúa marcada pendiente en README/arc42: el equipo fijó recrear y resembrar antes del 25/oct; hoy no se encontró evidencia de esa operación. No se infiere que no se haya realizado ni que la base esté caída. Los runs CI/Pages del head son exitosos pero no acreditan recreación, condiciones del proveedor ni despliegue institucional.

**Próximos pasos:**
- Documentar resultado de recreación/resembrado o migración de la BD demo y verificación de datos/health; no cerrar F7 solo por CI.
- Actualizar documentación de Usuarios/autenticación y garantías; publicar URL institucional real.

**Issues GitHub:** 2 abiertas / 15 cerradas; 1 abiertas sin asignar. Motivos: 15 completed.

**README:** Externo. Frontend; API

**PR consultadas:** [#35](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/35): cerrada sin fusión registrada; [#37](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/37): fusionada 2026-10-23T03:04:11Z; [#36](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/36): fusionada 2026-10-23T01:01:46Z; [#33](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/33): fusionada 2026-09-27T17:38:37Z; [#32](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/32): fusionada 2026-09-22T03:51:10Z; [#31](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/31): fusionada 2026-09-22T03:16:20Z; [#30](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/30): fusionada 2026-09-21T18:41:30Z; [#29](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/29): fusionada 2026-09-21T17:48:40Z; [#12](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/12): fusionada 2026-09-07T04:26:25Z; [#11](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/11): fusionada 2026-09-07T03:57:51Z; [#10](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/10): fusionada 2026-08-31T18:47:14Z; [#9](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/9): fusionada 2026-08-31T18:32:43Z; [#8](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/8): fusionada 2026-08-31T05:11:21Z; [#7](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/7): fusionada 2026-08-31T04:52:24Z; [#6](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/6): fusionada 2026-08-31T04:21:48Z; [#5](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/5): fusionada 2026-08-31T03:00:17Z; [#4](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/4): fusionada 2026-08-24T03:26:31Z; [#3](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/3): fusionada 2026-08-24T03:10:21Z; [#2](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/2): fusionada 2026-08-24T02:31:51Z; [#1](https://github.com/ISCOUTB/AS_202620_DinamikUTB/pull/1): fusionada 2026-08-24T02:02:03Z.

**CI consultado:** [Deploy frontend (GitHub Pages)](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40064883930): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_DinamikUTB/actions/runs/40064883888): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/README.md) · [11-risks-and-technical-debt.md](https://github.com/ISCOUTB/AS_202620_DinamikUTB/blob/8dad79338a66cd7054a0bde3f98661f785f5c378/docs/arc42/11-risks-and-technical-debt.md)

<a id="drift"></a>

## Drift

Rama **master**, [aa1578a1e81709418b502154999c2420352dd86e](https://github.com/ISCOUTB/AS_202620_Drift/commit/aa1578a1e81709418b502154999c2420352dd86e), fecha del commit 2026-10-21T04:53:31Z (UTC).

Sin nueva punta ni cambio de README desde el 24/oct. CI y Azure de la misma punta continúan exitosos. Se mantienen los artefactos S12 y sus límites ya registrados: evidencia simulada no equivale a rendimiento real. README distingue frontend/API institucionales y alternativas Azure/Vercel; no se hizo nueva prueba funcional.

**Próximos pasos:**
- Mantener límites del experimento simulado y repetir con dependencias reales antes de atribuir rendimiento productivo.
- Conservar pendientes del 24/oct sobre ADR0010, fallback/stale y catálogo por instancia/reinicio.

**Issues GitHub:** 5 abiertas / 15 cerradas; 5 abiertas sin asignar. Motivos: 15 completed.

**README:** Institucional. Frontend y API /api; API alternativa; Frontend alternativo

**PR consultadas:** [#31](https://github.com/ISCOUTB/AS_202620_Drift/pull/31): fusionada 2026-10-21T04:53:32Z; [#30](https://github.com/ISCOUTB/AS_202620_Drift/pull/30): fusionada 2026-10-19T03:20:50Z; [#29](https://github.com/ISCOUTB/AS_202620_Drift/pull/29): fusionada 2026-10-19T03:07:18Z; [#28](https://github.com/ISCOUTB/AS_202620_Drift/pull/28): fusionada 2026-10-19T02:08:58Z; [#27](https://github.com/ISCOUTB/AS_202620_Drift/pull/27): fusionada 2026-10-12T19:42:41Z; [#26](https://github.com/ISCOUTB/AS_202620_Drift/pull/26): fusionada 2026-10-12T19:15:32Z; [#25](https://github.com/ISCOUTB/AS_202620_Drift/pull/25): fusionada 2026-10-12T04:49:54Z; [#24](https://github.com/ISCOUTB/AS_202620_Drift/pull/24): fusionada 2026-10-11T05:28:23Z; [#23](https://github.com/ISCOUTB/AS_202620_Drift/pull/23): fusionada 2026-10-11T05:21:57Z; [#22](https://github.com/ISCOUTB/AS_202620_Drift/pull/22): fusionada 2026-10-11T04:53:50Z; [#21](https://github.com/ISCOUTB/AS_202620_Drift/pull/21): fusionada 2026-10-11T03:47:58Z.

**CI consultado:** [Build and deploy Python app to Azure Web App - drift-utb-202620](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39546508693): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_Drift/actions/runs/39546508600): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Drift/blob/aa1578a1e81709418b502154999c2420352dd86e/README.md)

<a id="elmapita"></a>

## ElMapita

Rama **main**, [0421885424d13478cf33c717fdd933a4748d9025](https://github.com/ISCOUTB/AS_202620_ElMapita/commit/0421885424d13478cf33c717fdd933a4748d9025), fecha del commit 2026-10-19T08:33:59Z (UTC).

Sin nueva punta ni cambio de README desde el 24/oct, con CI exitoso de ese head. Se conserva presentación y funcionamiento confirmados por el docente. Sigue faltando la URL pública concreta del despliegue en README; localhost y placeholder Supabase no la sustituyen.

**Próximos pasos:**
- Publicar en README la URL iscoutb.dev exacta del despliegue mostrado, sin inventar host.
- Mantener pendientes S12 del 24/oct sobre garantías, invalidación/versionado de modelos y ADR comparativo.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_ElMapita/pull/2): fusionada 2026-10-05T03:11:20Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_ElMapita/actions/runs/39223716465): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ElMapita/blob/0421885424d13478cf33c717fdd933a4748d9025/README.md)

<a id="enagenda"></a>

## EnAgenda

Rama **master**, [2584f0ac3f8dad7025bc0bed396fa95c4ed0fcf1](https://github.com/ISCOUTB/AS_202620_EnAgenda/commit/2584f0ac3f8dad7025bc0bed396fa95c4ed0fcf1), fecha del commit 2026-10-25T02:40:45Z (UTC).

Avance integrado: panel del organizador, creación de eventos e invitaciones por evento con modelos/migraciones PostgreSQL. Los casos de uso bloquean filas con FOR UPDATE antes de contar y escribir, con límites de cuatro eventos activos y treinta invitados. En app/web.py conviven las nuevas rutas /eventos/invitacion/<token> sobre PostgreSQL y las rutas heredadas /invitacion y /api/v1/invitaciones sobre memoria: no declarar toda Invitaciones persistida ni toda Invitaciones en memoria. El CI falla durante colección de cuatro módulos porque DATABASE_URL no está configurada; contrato y build Docker se omiten. Pages exitoso es publicación estática, no aceptación del backend. README no se actualizó ni publica URL concreta.

**Próximos pasos:**
- Configurar una base aislada de pruebas y migraciones en CI antes de ejecutar la suite; verificar contrato y build omitidos.
- Probar concurrencia y límites de eventos/invitados contra PostgreSQL y documentar coexistencia o migración de rutas heredadas en memoria.
- Actualizar README, C4/arc42 y URL iscoutb.dev; no confundir Pages con despliegue funcional del backend.

**Issues GitHub:** 1 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_EnAgenda/pull/2): fusionada 2026-09-28T02:39:59Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40155372868): failure (misma punta); [pages build and deployment](https://github.com/ISCOUTB/AS_202620_EnAgenda/actions/runs/40155372438): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/2584f0ac3f8dad7025bc0bed396fa95c4ed0fcf1/README.md) · [web.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/2584f0ac3f8dad7025bc0bed396fa95c4ed0fcf1/app/web.py) · [crear_evento.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/2584f0ac3f8dad7025bc0bed396fa95c4ed0fcf1/src/eventos/aplicacion/crear_evento.py) · [agregar_invitados.py](https://github.com/ISCOUTB/AS_202620_EnAgenda/blob/2584f0ac3f8dad7025bc0bed396fa95c4ed0fcf1/src/invitaciones/aplicacion/agregar_invitados.py)

<a id="gimnasioutb"></a>

## GimnasioUTB

Rama **main**, [1a706525f6a660c216bc11655c754f65bbbe8bfe](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/commit/1a706525f6a660c216bc11655c754f65bbbe8bfe), fecha del commit 2026-10-20T18:38:58Z (UTC).

Sin nueva punta ni cambio de README desde el 24/oct. CI exitoso de la misma punta; no añade evidencia PostgreSQL o aceptación funcional respecto al informe anterior. README sigue documentando backend institucional y pendiente de integración Flutter, aunque el informe previo reconoce llamadas HTTP existentes; no inferir ausencia de código por documentación rezagada.

**Próximos pasos:**
- Incorporar y acreditar pruebas PostgreSQL en CI; actualizar README y backlog según evidencia.
- Mantener pendientes de garantías por operación, caché/no caché y ADR comparativo del 24/oct.

**Issues GitHub:** 16 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend; interfaz Flutter pública no acreditada

**PR consultadas:** [#17](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/pull/17): fusionada 2026-10-19T01:09:26Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/actions/runs/39476599936): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_GimnasioUTB/blob/1a706525f6a660c216bc11655c754f65bbbe8bfe/README.md)

<a id="inventrack"></a>

## InvenTrack

Rama **main**, [7410f60c0b2a8eb5e44374e0eb9943e0594cce54](https://github.com/ISCOUTB/AS_202620_InvenTrack/commit/7410f60c0b2a8eb5e44374e0eb9943e0594cce54), fecha del commit 2026-10-25T05:44:42Z (UTC).

Avance documental S12 en docs/aspectos.md: declara política efectiva sin caché para el MVP en memoria y diseño futuro cache-aside Redis, claves versionadas, TTL e invalidación tras escritura con tratamiento de fallo. Es diseño condicionado a persistencia compartida, no Redis implementado. El nuevo run ejecuta Pytest con cobertura, contrato y scanner exitosamente; scanner no demuestra por sí solo Quality Gate. README sin cambios: API institucional, Flutter pendiente.

**Próximos pasos:**
- Reconocer el diseño de caché nuevo sin pedirlo como ausente; mantener diferenciada política actual sin caché y evolución Redis.
- Resolver trazabilidad de dos operaciones, ADR comparativo de costo de reversión y alineación de arc42 §8/C4 con RAM actual.
- Probar carreras entre repoblación e invalidación y fallos cuando se implemente caché; TTL/Redis por sí solos no garantizan lectura fuerte.

**Issues GitHub:** 0 abiertas / 7 cerradas; 0 abiertas sin asignar. Motivos: 7 completed.

**README:** Institucional. API; API alternativa

**CI consultado:** [Run Tests](https://github.com/ISCOUTB/AS_202620_InvenTrack/actions/runs/40166646614): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/7410f60c0b2a8eb5e44374e0eb9943e0594cce54/README.md) · [aspectos.md](https://github.com/ISCOUTB/AS_202620_InvenTrack/blob/7410f60c0b2a8eb5e44374e0eb9943e0594cce54/docs/aspectos.md)

<a id="laplacita"></a>

## LaPlacita

Rama **master**, [3d003b62ffe92c659699bd1236424fb397bc2eee](https://github.com/ISCOUTB/AS_202620_LaPlacita/commit/3d003b62ffe92c659699bd1236424fb397bc2eee), fecha del commit 2026-10-25T03:25:42Z (UTC).

Avance real incorporado después del corte del 24: almacenamiento de imágenes del catálogo con módulo Garage S3 y referencias PostgreSQL; rutas de pago exigen dueño y se retiraron las dos mutaciones públicas legacy de entrega. Se añadió auditoría de dependencias a CI, STRIDE y transcripción Markdown del plan. Los ADR 0024–0026 ya constan aceptados por el equipo, no pendientes de validación. El run exacto de master pasa frontend, pruebas, contrato y audit; log Sonar confirma QUALITY GATE STATUS: PASSED. Las ocho PR de dependencias #16–23 siguen abiertas, no son funcionalidades integradas. README todavía solo tiene la URL Azure retirada, no publica URL vigente. La integración Garage/recorrido desplegado se reporta por el equipo; esta revisión no ejecutó una prueba funcional en vivo.

**Próximos pasos:**
- Publicar en README las URL vigentes separando API y PWA bajo iscoutb.dev; retirar la referencia ambigua «URL arriba».
- Distinguir configuración real de Garage del modo memoria sin GARAGE_* y aportar prueba de persistencia tras reinicio; mantener deuda de limpieza de objetos huérfanos.
- Completar lecturas por dueño, validación del modelo STRIDE y aceptación móvil; revisar las PR de dependencias sin atribuir al master sus fallos.

**Issues GitHub:** 0 abiertas / 14 cerradas; 0 abiertas sin asignar. Motivos: 14 completed.

**README:** Sin URL concreta. Solo Azure explícitamente retirado; ninguna URL pública vigente concreta en README raíz.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/22): abierta; [#21](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/21): abierta; [#20](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/20): abierta; [#19](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/19): abierta; [#18](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/18): abierta; [#17](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/17): abierta; [#16](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/16): abierta; [#15](https://github.com/ISCOUTB/AS_202620_LaPlacita/pull/15): fusionada 2026-10-22T19:07:22Z.

**CI consultado:** [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40158232304): success (misma punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154925335): failure (otra revisión/rama; no acredita la punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154919024): failure (otra revisión/rama; no acredita la punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154911516): failure (otra revisión/rama; no acredita la punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154903607): failure (otra revisión/rama; no acredita la punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154893276): failure (otra revisión/rama; no acredita la punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154749804): failure (otra revisión/rama; no acredita la punta); [CI LaPlacita](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40154725739): failure (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/README.md) · [0028-almacen-imagenes-garage-dokploy.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/docs/adr/0028-almacen-imagenes-garage-dokploy.md) · [0029-superficie-publica-minima.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/docs/adr/0029-superficie-publica-minima.md) · [evidencias-s13.md](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/docs/evidencias/evidencias-s13.md) · [index.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/backend/src/modules/almacen/index.js) · [index.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/backend/src/modules/pagos/index.js) · [route.js](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/backend/app/api/v1/pagos/[pedidoId]/confirmar/route.js) · [ci.yml](https://github.com/ISCOUTB/AS_202620_LaPlacita/blob/3d003b62ffe92c659699bd1236424fb397bc2eee/.github/workflows/ci.yml) · [121064321877](https://github.com/ISCOUTB/AS_202620_LaPlacita/actions/runs/40158232304/job/121064321877)

<a id="lostvault"></a>

## LostVault

Rama **main**, [e19be366f7e922a8a9c9abd4a808899f14b2999b](https://github.com/ISCOUTB/AS_202620_LostVault/commit/e19be366f7e922a8a9c9abd4a808899f14b2999b), fecha del commit 2026-10-20T16:16:33Z (UTC).

Sin cambios en main ni nuevas ejecuciones desde el corte del 24. PR #19 permanece integrada; la nueva API con JWT/idempotencia y almacenamiento RAM no equivale a persistencia ni despliegue. Los tres workflows de la misma punta siguen exitosos; se conserva la limitación previamente verificada: Backend checks prueba backend/test_api.py, no api/tests. README no publica una URL vigente.

**Próximos pasos:**
- Incluir api/tests en CI y documentar la relación api/backend/Flutter.
- Publicar URL real iscoutb.dev y separar API de cliente.
- Completar garantías por operación y límites ante reinicio, caché/no caché y ADR de reversión.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de trabajo o despliegue.

**PR consultadas:** [#19](https://github.com/ISCOUTB/AS_202620_LostVault/pull/19): fusionada 2026-10-20T16:16:34Z; [#18](https://github.com/ISCOUTB/AS_202620_LostVault/pull/18): fusionada 2026-10-19T01:43:15Z; [#17](https://github.com/ISCOUTB/AS_202620_LostVault/pull/17): fusionada 2026-10-19T01:32:11Z; [#16](https://github.com/ISCOUTB/AS_202620_LostVault/pull/16): fusionada 2026-10-05T03:30:54Z; [#15](https://github.com/ISCOUTB/AS_202620_LostVault/pull/15): fusionada 2026-10-05T02:31:39Z; [#14](https://github.com/ISCOUTB/AS_202620_LostVault/pull/14): fusionada 2026-10-05T00:42:49Z; [#13](https://github.com/ISCOUTB/AS_202620_LostVault/pull/13): fusionada 2026-09-28T04:39:31Z; [#12](https://github.com/ISCOUTB/AS_202620_LostVault/pull/12): fusionada 2026-09-28T03:17:55Z; [#11](https://github.com/ISCOUTB/AS_202620_LostVault/pull/11): cerrada sin fusión registrada; [#10](https://github.com/ISCOUTB/AS_202620_LostVault/pull/10): fusionada 2026-09-21T04:55:35Z.

**CI consultado:** [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997158): success (misma punta); [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997151): success (misma punta); [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39455997101): success (misma punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39452301040): success (otra revisión/rama; no acredita la punta); [Backend checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39452301038): success (otra revisión/rama; no acredita la punta); [Build](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39452300726): success (otra revisión/rama; no acredita la punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39452050078): success (otra revisión/rama; no acredita la punta); [Flutter checks](https://github.com/ISCOUTB/AS_202620_LostVault/actions/runs/39450410517): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_LostVault/blob/e19be366f7e922a8a9c9abd4a808899f14b2999b/README.md)

<a id="mapsutb"></a>

## mapsutb

Rama **master**, [4b8fa088faec96772e76c8c4f2782919ec87a9b9](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/4b8fa088faec96772e76c8c4f2782919ec87a9b9), fecha del commit 2026-10-16T17:38:48Z (UTC).

Sin cambios en master desde el 16 de octubre. Nueva sonda programada del 25 de octubre pasó en la misma punta; no representa nuevas funcionalidades ni una prueba integral del sitio. Continúan abiertas las dos issues Sonar y sin responsable. README publica Firebase, no iscoutb.dev; es distinto de ElMapita.

**Próximos pasos:**
- Asignar y resolver #55 y #56 con evidencia verificable.
- Documentar URL institucional exacta.
- Completar garantías por operación y política de invalidación de caché.

**Issues GitHub:** 2 abiertas / 52 cerradas; 2 abiertas sin asignar. Motivos: 52 completed.

**README:** Externo. Frontend Firebase externo; sonda CI disponible, sin nueva aceptación funcional propia.

**PR consultadas:** [#47](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/47): fusionada 2026-09-08T00:37:03Z; [#1](https://github.com/ISCOUTB/AS_202620_mapsutb/pull/1): fusionada 2026-09-01T01:11:25Z.

**CI consultado:** [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40193891253): success (misma punta); [Sincronizar hallazgos de Sonar a GitHub Issues](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40192755632): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40188852571): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40184876730): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40180824663): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40177147369): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40173043232): success (misma punta); [Sonda de disponibilidad (métrica Escenario 6)](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/40170082211): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/4b8fa088faec96772e76c8c4f2782919ec87a9b9/README.md)

<a id="pideutb"></a>

## PideUtb

Rama **master**, [ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f](https://github.com/ISCOUTB/AS_202620_PideUtb/commit/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f), fecha del commit 2026-10-23T15:04:06Z (UTC).

Sin cambio de punta ni nueva ejecución respecto al 24. PR #29 de identidad visual integrada y CI de la misma punta exitoso; se conserva la limitación previamente verificada de Sonar: los pasos de análisis/cobertura/Quality Gate se omitieron. No se da por validada la interfaz por las pruebas backend. Se conserva presentación y despliegues confirmados por docente.

**Próximos pasos:**
- Registrar aceptación visual a 375 px, temas y teclado.
- Obtener evidencia real de análisis y Quality Gate, no solo job success.
- Contrastar carreras de actualizar_estado y precisar las garantías documentadas.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Frontend/panel y API institucionales; docente confirma presentación/despliegues; sin nueva verificación visual.

**PR consultadas:** [#29](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/29): fusionada 2026-10-23T15:04:06Z; [#28](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/28): fusionada 2026-10-20T14:55:39Z; [#27](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/27): fusionada 2026-10-18T23:40:46Z; [#26](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/26): fusionada 2026-10-18T22:31:12Z; [#25](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/25): fusionada 2026-10-18T18:31:49Z; [#24](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/24): fusionada 2026-10-18T17:05:21Z; [#23](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/23): fusionada 2026-10-18T15:44:46Z; [#22](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/22): fusionada 2026-10-18T02:49:18Z; [#21](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/21): fusionada 2026-10-18T02:12:59Z; [#20](https://github.com/ISCOUTB/AS_202620_PideUtb/pull/20): fusionada 2026-10-18T01:32:03Z.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39975061857): success (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39888136252): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39888135841): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39508397909): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39508391227): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39443709932): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39443058228): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_PideUtb/actions/runs/39443010331): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PideUtb/blob/ef38ad25ff43dba7d77fde2a17c3e3eb0a8d4e2f/README.md)

<a id="proyecto_campusmarket"></a>

## CampusMarket

Rama **master**, [a237dd2f22b02bb547f87a07d15b6d31ea0dc758](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/commit/a237dd2f22b02bb547f87a07d15b6d31ea0dc758), fecha del commit 2026-10-19T04:51:37Z (UTC).

Sin cambios en master desde el corte previo. #60 sigue abierta y no integrada. En la punta actual pasan Compose/persistencia, contrato cliente, backend y Flutter; Flujo real Web y Android conserva failure. API institucional y frontend GitHub Pages permanecen separados; no afirmar todo CI verde.

**Próximos pasos:**
- Corregir/reproducir el flujo Android y resolver #60.
- Publicar frontend bajo iscoutb.dev; API institucional no completa ese requisito.
- Completar garantías de publicación, política de caché y ADR de costo de reversión.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Institucional. Cumplimiento parcial: API institucional, frontend externo GitHub Pages. Azure es histórico.

**PR consultadas:** [#59](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/59): fusionada 2026-10-19T04:51:37Z; [#60](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/60): abierta; [#57](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/57): fusionada 2026-10-19T04:17:24Z; [#58](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/58): fusionada 2026-10-19T04:04:00Z; [#56](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/56): fusionada 2026-10-19T03:17:47Z; [#55](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/55): fusionada 2026-10-12T04:50:45Z; [#54](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/54): fusionada 2026-10-04T07:14:35Z; [#53](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/53): fusionada 2026-10-04T06:38:56Z; [#52](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/52): fusionada 2026-10-04T04:04:41Z; [#51](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/pull/51): fusionada 2026-10-04T03:06:42Z.

**CI consultado:** [Compose y persistencia del MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586404): success (misma punta); [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586378): success (misma punta); [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586366): failure (misma punta); [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586343): success (misma punta); [Validación Flutter MVP](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201586312): success (misma punta); [Pruebas del backend](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201532555): success (otra revisión/rama; no acredita la punta); [S10 contrato del cliente en despliegue publico](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201532554): success (otra revisión/rama; no acredita la punta); [Flujo real Web y Android](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/actions/runs/39201532549): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET/blob/a237dd2f22b02bb547f87a07d15b6d31ea0dc758/README.md)

<a id="recobra"></a>

## Recobra

Rama **master**, [00f9291c4e59b315a65ba2af348ed449b28319c7](https://github.com/ISCOUTB/AS_202620_Recobra/commit/00f9291c4e59b315a65ba2af348ed449b28319c7), fecha del commit 2026-10-24T14:04:29Z (UTC).

Dos commits posteriores al corte anterior responden al feedback: se corrigió la invalidación de /lugares (el despliegue no borra caché del navegador), se ampliaron los adaptadores PostgreSQL a nueve de nueve, se añadió verificación de respaldo/restauración y alerta de cola de fallidos. El run exacto 40100869755 registra 37 pruebas de adaptadores aprobadas y restauración de 23 filas en nueve tablas sin diferencias; Quality Gate aprobado. Los e2e nuevos prueban mensajes en la aplicación con fallos simulados; los e2e generales siguen en memoria. No confundir procedimiento CI con respaldos programados de producción: estos siguen pendientes, igual que alerta hacia personas y RTO real. README ahora separa explícitamente vitrina, Flutter Web y API. Presentación confirmada por docente.

**Próximos pasos:**
- Configurar y evidenciar respaldo programado de producción y ensayo controlado con tiempos; CI valida procedimiento, no operación productiva.
- Conectar alerta de cola a una notificación operativa; hoy solo log/métrica.
- Mantener explícitos límites de EventEmitter, una instancia y e2e en memoria; complementar cobertura del flujo completo contra PostgreSQL.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. README aclara vitrina, Flutter Web y API en mismo host institucional; no se añade auditoría funcional.

**CI consultado:** [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100869755): success (misma punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100601685): success (otra revisión/rama; no acredita la punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39692648288): success (otra revisión/rama; no acredita la punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39692259031): success (otra revisión/rama; no acredita la punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39691555460): failure (otra revisión/rama; no acredita la punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39691304611): success (otra revisión/rama; no acredita la punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39150751474): success (otra revisión/rama; no acredita la punta); [ci](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/39147249754): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/README.md) · [respaldos.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/docs/despliegue/respaldos.md) · [0025-diseno-de-cache-y-politica-de-invalidacion.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/docs/adr/0025-diseno-de-cache-y-politica-de-invalidacion.md) · [0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/docs/adr/0026-entrega-de-avisos-con-eventos-reintentos-y-cola-de-fallidos.md) · [adaptadores.e2e-spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/test/adaptadores.e2e-spec.ts) · [entrega-eventos.e2e-spec.ts](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/test/entrega-eventos.e2e-spec.ts) · [ci.yml](https://github.com/ISCOUTB/AS_202620_Recobra/blob/00f9291c4e59b315a65ba2af348ed449b28319c7/.github/workflows/ci.yml) · [120892563019](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100869755/job/120892563019) · [120892563069](https://github.com/ISCOUTB/AS_202620_Recobra/actions/runs/40100869755/job/120892563069)

<a id="routb"></a>

## ROUTB

Rama **master**, [5d686a594d3e3515233e60b4e6b33330ded05572](https://github.com/ISCOUTB/AS_202620_ROUTB/commit/5d686a594d3e3515233e60b4e6b33330ded05572), fecha del commit 2026-10-23T14:47:48Z (UTC).

Sin cambios en master desde el corte anterior. Nueva ejecución programada de purga pasó, pero no es nuevo despliegue ni aceptación funcional. CI de la misma punta permanece exitoso; se conservan límites documentados en la revisión previa sobre job Sonar placeholder y documentación de geocode_cache retirada. Docente confirmó avance entregado.

**Próximos pasos:**
- Conciliar arc42, ADR y caché con geocodificación en cliente y route_cache vigente.
- Obtener análisis/Gate reales y actualizar guía Render frente a Dokploy.
- Contrastar garantías de solicitudes/cupos con restricciones y pruebas concurrentes.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Institucional. Backend institucional; instrucciones Render antiguas aún presentes; avance docente preservado.

**PR consultadas:** [#52](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/52): fusionada 2026-10-23T14:47:48Z; [#51](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/51): fusionada 2026-10-18T21:39:27Z; [#50](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/50): fusionada 2026-10-13T03:02:26Z; [#49](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/49): fusionada 2026-10-12T00:30:24Z; [#48](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/48): fusionada 2026-10-11T23:52:36Z; [#47](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/47): cerrada sin fusión registrada; [#46](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/46): fusionada 2026-10-03T23:20:32Z; [#45](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/45): fusionada 2026-10-03T22:57:29Z; [#44](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/44): fusionada 2026-10-03T19:53:46Z; [#43](https://github.com/ISCOUTB/AS_202620_ROUTB/pull/43): fusionada 2026-10-03T05:18:30Z.

**CI consultado:** [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40175780746): success (misma punta); [Purga periódica de datos de ubicación](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/40077189117): success (misma punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39972693861): success (misma punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39972306263): success (otra revisión/rama; no acredita la punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39972298285): success (otra revisión/rama; no acredita la punta); [Running Copilot cloud agent](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39971982526): success (otra revisión/rama; no acredita la punta); [Addressing comment on PR #52](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39971563298): success (otra revisión/rama; no acredita la punta); [CI ROUTB](https://github.com/ISCOUTB/AS_202620_ROUTB/actions/runs/39971202518): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ROUTB/blob/5d686a594d3e3515233e60b4e6b33330ded05572/README.md)

<a id="shareu"></a>

## ShareU

Rama **master**, [39508608eae4c1a56a5e4fc11a055bf6afb2c003](https://github.com/ISCOUTB/AS_202620_ShareU/commit/39508608eae4c1a56a5e4fc11a055bf6afb2c003), fecha del commit 2026-09-29T00:56:57Z (UTC).

Sin cambios en master, README, PR ni último CI respecto al corte anterior. #22 y #23 siguen abiertas; no atribuir sus propuestas a master. El último workflow de la punta permanece fallido y diez issues siguen abiertas, cinco sin responsable. README conserva placeholders Vercel/Render.

**Próximos pasos:**
- Resolver pipeline y conciliar issues con evidencia; no contar propuesta de PR como integrada.
- Sustituir placeholders con URL oficial iscoutb.dev.
- Completar garantías por operación, caché/no caché y ADR de reversión.

**Issues GitHub:** 10 abiertas / 10 cerradas; 5 abiertas sin asignar. Motivos: 10 completed.

**README:** Sin URL concreta. Placeholders Vercel/Render y localhost, no URL pública concreta vigente.

**PR consultadas:** [#23](https://github.com/ISCOUTB/AS_202620_ShareU/pull/23): abierta; [#22](https://github.com/ISCOUTB/AS_202620_ShareU/pull/22): abierta; [#1](https://github.com/ISCOUTB/AS_202620_ShareU/pull/1): fusionada 2026-09-07T13:08:19Z.

**CI consultado:** [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36505758458): failure (misma punta); [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36480560316): failure (otra revisión/rama; no acredita la punta); [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479877131): failure (otra revisión/rama; no acredita la punta); [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36479388452): failure (otra revisión/rama; no acredita la punta); [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/36379843854): failure (otra revisión/rama; no acredita la punta); [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/35632045274): success (otra revisión/rama; no acredita la punta); [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/35561494254): success (otra revisión/rama; no acredita la punta); [Tests](https://github.com/ISCOUTB/AS_202620_ShareU/actions/runs/35558035094): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_ShareU/blob/39508608eae4c1a56a5e4fc11a055bf6afb2c003/README.md)

<a id="sistema-de-calificacion-automatica"></a>

## QuantIA

Rama **master**, [9468be7035cebc344f405a23a436353e07e4c118](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/commit/9468be7035cebc344f405a23a436353e07e4c118), fecha del commit 2026-10-24T21:15:40Z (UTC).

Se sincronizan README, arc42, aspectos y modos de fallo con los arreglos ya implementados: se documenta R-21 cerrado y las cifras vigentes de pruebas. El delta desde el corte del 24 es documental, no una nueva implementación. El CI de la punta actual confirma 156 pruebas backend y 72 frontend, además de contrato y modos de fallo. Se mantienen declaradas la falta de acuse de la cola, persistencia efímera y detección de cargas duplicadas; no se cierra S12 ni se acredita un nuevo despliegue.

**Próximos pasos:**
- Conservar la sincronización documental conseguida y completar operación→garantía para recepción, bitácora y consumo sin acuse.
- Repetir EC-07 con almacenamiento y Redis reales; el plazo de encolado no acota toda la lectura y escritura del lote.
- Completar la decisión comparativa de persistencia y política de caché/no caché; publicar frontend y API bajo iscoutb.dev.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend y API Render; no dominio institucional. Sin sondeo directo en esta revisión.

**PR consultadas:** [#1](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/pull/1): cerrada sin fusión registrada.

**CI consultado:** [CI](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/actions/runs/40133428731): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9468be7035cebc344f405a23a436353e07e4c118/README.md) · [docs/arc42/arc42-template-ES.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9468be7035cebc344f405a23a436353e07e4c118/docs/arc42/arc42-template-ES.md) · [docs/evidencia/modos-de-fallo.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9468be7035cebc344f405a23a436353e07e4c118/docs/evidencia/modos-de-fallo.md) · [docs/aspectos.md](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica/blob/9468be7035cebc344f405a23a436353e07e4c118/docs/aspectos.md)

<a id="taia_-task-artificial-intelligence-assistant"></a>

## TAIA

Rama **main**, [5aa16fcf0152361901bf2500291235550ca40951](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/commit/5aa16fcf0152361901bf2500291235550ca40951), fecha del commit 2026-10-22T18:55:56Z (UTC).

Sin cambios de punta, README, issues o PR relevantes desde el corte anterior. La API institucional permanece documentada y se conserva la confirmación docente de presentación y funcionamiento. No aparece un run para la punta actual: los últimos CI/CD exitosos son de otra revisión. El workflow mantiene paths sin espacio tras los guiones y rutas que requieren alineación, por lo que no se da por corregido el disparador ni se infiere caída del servicio.

**Próximos pasos:**
- Corregir paths en CI y verificar un run sobre la punta actual.
- Completar garantías por operación y pruebas de confirmar/notificar frente a crear tarea y Telegram.
- Justificar caché/no caché y costo de reversión; mantener PostgreSQL, C4 y arc42 alineados.

**Issues GitHub:** 3 abiertas / 4 cerradas; 2 abiertas sin asignar. Motivos: 4 completed.

**README:** Institucional. API institucional; Render como respaldo. Flutter es arquitectura objetivo, no frontend web verificado. Presentación y funcionamiento confirmados por docente.

**PR consultadas:** [#16](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/16): fusionada 2026-09-26T03:34:08Z; [#15](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/15): fusionada 2026-09-17T02:40:14Z; [#14](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/14): fusionada 2026-09-17T01:53:44Z; [#13](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/13): fusionada 2026-09-16T01:48:07Z; [#12](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/12): fusionada 2026-09-14T01:01:35Z; [#11](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/11): fusionada 2026-09-12T17:29:59Z; [#10](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/10): fusionada 2026-09-12T15:26:17Z; [#9](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/9): fusionada 2026-09-11T02:08:20Z; [#8](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/pull/8): fusionada 2026-09-11T00:36:16Z.

**CI consultado:** [CD](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441872010): success (otra revisión/rama; no acredita la punta); [CI](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/actions/runs/39441578508): success (otra revisión/rama; no acredita la punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/README.md) · [.github/workflows/ci.yml](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/blob/5aa16fcf0152361901bf2500291235550ca40951/.github/workflows/ci.yml)

<a id="tienda-virtual-utb"></a>

## Tienda Virtual

Rama **main**, [0045c8e4102416cf3222f5749a0965a668817cd7](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/commit/0045c8e4102416cf3222f5749a0965a668817cd7), fecha del commit 2026-10-25T02:58:28Z (UTC).

Avance sustancial: el stack API 0.4.0–0.5.0 ya está fusionado, con registro/login JWT, escrituras de inventario, pedidos idempotentes con ciclo de vida y cancelación, permisos/RLS por tienda y frontend conectado a datos reales. La PR #12 reúne carrito, apartados e historial en /pedidos y deja /cuenta para perfil/carnet. El equipo documenta despliegue de 0.5.0 y E2E, sin aceptación independiente aquí. El CI exacto pasa frontend y backend; sonarcloud figura success pero todos sus pasos de análisis están skipped, por lo que no acredita análisis ni Quality Gate. Ya no corresponde afirmar que los endpoints de pedidos son solo diseño.

**Próximos pasos:**
- Verificar el despliegue con el dominio institucional y certificado válido; registrar aceptación funcional separada de los E2E reportados por el equipo.
- Resolver cobertura/análisis Sonar y verificar su Quality Gate, no solo el estado del job omitido.
- Confirmar SEED_ON_DEPLOY=false tras sembrar y programar el vencimiento de pedidos; probar respaldo/restauración y revisar seguridad de sesión según pendientes.
- Completar evidencia S12 de garantías y reversión usando las operaciones ahora implementadas, sin tratar diseño previo como estado actual.

**Issues GitHub:** 0 abiertas / 0 cerradas; 0 abiertas sin asignar. Motivos: —.

**README:** Externo. Frontend sslip temporal; el equipo documenta certificado autofirmado pendiente y despliegue 0.5.0. No se sorteó aviso TLS ni se verificó el sitio en vivo.

**PR consultadas:** [#12](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/12): fusionada 2026-10-25T02:58:28Z; [#11](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/11): fusionada 2026-10-24T20:15:26Z; [#10](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/10): fusionada 2026-10-24T19:40:05Z; [#9](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/9): fusionada 2026-10-24T19:22:55Z; [#8](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/8): fusionada 2026-10-24T19:22:38Z; [#7](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/7): fusionada 2026-10-24T19:22:22Z; [#6](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/6): fusionada 2026-10-24T19:22:12Z; [#5](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/5): fusionada 2026-10-24T19:21:59Z; [#4](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/4): fusionada 2026-10-24T19:21:48Z; [#3](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/3): fusionada 2026-10-24T19:21:38Z; [#2](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/2): fusionada 2026-10-24T19:21:28Z; [#1](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/pull/1): fusionada 2026-10-21T16:14:34Z.

**CI consultado:** [Pruebas](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/actions/runs/40156471490): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/README.md) · [CHANGELOG.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/CHANGELOG.md) · [backend/app/modules/orders/service.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/backend/app/modules/orders/service.py) · [backend/app/modules/orders/router.py](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/backend/app/modules/orders/router.py) · [docs/pendientes.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/docs/pendientes.md) · [docs/pruebas-e2e-testsprite.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/docs/pruebas-e2e-testsprite.md) · [.github/workflows/tests.yml](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/.github/workflows/tests.yml) · [docs/adr/0017-admin-general-supervisa.md](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB/blob/0045c8e4102416cf3222f5749a0965a668817cd7/docs/adr/0017-admin-general-supervisa.md)

<a id="utb_tracker"></a>

## UTB Tracker

Rama **main**, [1192503633dc4170f223bce43e079be8d941c0d3](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/commit/1192503633dc4170f223bce43e079be8d941c0d3), fecha del commit 2026-10-24T20:58:58Z (UTC).

Nuevas migraciones y ajustes de API/configuración; el cliente Android incorpora empaquetado, R8 y desactivación de copias/HTTP claro. Se publicó app-release.apk en release v1.0.2, y la punta main registra 48 pruebas backend y deploy exitosos. Esto acredita construcción/publicación del APK, no aceptación funcional en un dispositivo. README raíz sigue sin URL pública concreta; el código del cliente apunta a HTTPS nip.io, no al dominio institucional. Persiste la fixture que recurre a DATABASE_URL antes de drop_all/create_all: no está resuelto el riesgo de destino de pruebas incorrecto.

**Próximos pasos:**
- Actualizar README con URL iscoutb.dev, API, cliente Android/release y arquitectura vigente; el enlace dentro del código no sustituye el README.
- Exigir TEST_DATABASE_URL de una base aislada y rechazar destinos de producción antes de operaciones destructivas.
- Validar el APK con recorridos reales y firma de distribución apropiada: build.gradle.kts aún usa firma debug en release.
- Completar garantías/concurrencia, caché/no caché y costo de reversión de S12; un CI exitoso no reemplaza análisis estático ni aceptación móvil.

**Issues GitHub:** 1 abiertas / 0 cerradas; 1 abiertas sin asignar. Motivos: —.

**README:** Sin URL concreta. README raíz sin endpoint público vigente. Solo en código: https://129-80-171-141.nip.io; release APK v1.0.2 publicado, no prueba de sitio institucional.

**PR consultadas:** [#2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/pull/2): fusionada 2026-10-06T06:08:06Z.

**CI consultado:** [Release APK](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132197969): success (misma punta); [UTB Tracker CI](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/actions/runs/40132194977): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/1192503633dc4170f223bce43e079be8d941c0d3/README.md) · [tests/conftest.py](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/1192503633dc4170f223bce43e079be8d941c0d3/tests/conftest.py) · [frontend/lib/core/config/api_config.dart](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/1192503633dc4170f223bce43e079be8d941c0d3/frontend/lib/core/config/api_config.dart) · [.github/workflows/apk-release.yml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/1192503633dc4170f223bce43e079be8d941c0d3/.github/workflows/apk-release.yml) · [frontend/android/app/build.gradle.kts](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/1192503633dc4170f223bce43e079be8d941c0d3/frontend/android/app/build.gradle.kts) · [frontend/android/app/src/main/AndroidManifest.xml](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/blob/1192503633dc4170f223bce43e079be8d941c0d3/frontend/android/app/src/main/AndroidManifest.xml) · [Release v1.0.2](https://github.com/ISCOUTB/AS_202620_UTB_TRACKER/releases/tag/v1.0.2)

<a id="uniteam"></a>

## uniTeam

Rama **master**, [facff6f0549f813e08e53461840993e91b29a07c](https://github.com/ISCOUTB/AS_202620_uniTeam/commit/facff6f0549f813e08e53461840993e91b29a07c), fecha del commit 2026-10-23T19:43:29Z (UTC).

Sin cambios de punta, README o PR desde el corte previo. La sonda más reciente falla, pero sigue apuntando a Render mientras el README publica DuckDNS: no prueba una caída del dominio actual. Se mantiene separado el CI exitoso del código de la comprobación de despliegue fallida; no se verificó funcionamiento en vivo.

**Próximos pasos:**
- Actualizar la sonda a los destinos documentados y publicar subdominios iscoutb.dev.
- Alinear la afirmación del README sobre CI con el workflow existente y recuperar trazabilidad de cobertura/Quality Gate.
- Completar garantías por operación, invalidación y ADR de reversión con evidencia concreta.

**Issues GitHub:** 0 abiertas / 1 cerradas; 0 abiertas sin asignar. Motivos: 1 completed.

**README:** Externo. Frontend y API DuckDNS. Sonda sigue consultando Render; su fallo no determina disponibilidad de DuckDNS.

**PR consultadas:** [#8](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/8): fusionada 2026-10-23T05:15:01Z; [#7](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/7): fusionada 2026-10-23T04:57:30Z; [#6](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/6): fusionada 2026-10-23T04:38:54Z; [#5](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/5): fusionada 2026-10-13T15:44:45Z; [#4](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/4): fusionada 2026-10-04T21:23:33Z; [#3](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/3): fusionada 2026-09-21T16:46:49Z; [#2](https://github.com/ISCOUTB/AS_202620_uniTeam/pull/2): fusionada 2026-09-14T01:20:18Z.

**CI consultado:** [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40193593871): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40169783694): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40148956960): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40120877613): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40094373315): failure (misma punta); [Comprobación del despliegue](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40070952290): failure (misma punta); [CI](https://github.com/ISCOUTB/AS_202620_uniTeam/actions/runs/40013691251): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/README.md) · [.github/workflows/despliegue.yml](https://github.com/ISCOUTB/AS_202620_uniTeam/blob/facff6f0549f813e08e53461840993e91b29a07c/.github/workflows/despliegue.yml)

<a id="xald"></a>

## XALD

Rama **master**, [4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13](https://github.com/ISCOUTB/AS_202620_XALD/commit/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13), fecha del commit 2026-10-25T00:56:50Z (UTC).

Nuevo avance documental S12: arc42 incorpora siete operaciones con garantías y límites, más dos contrastes de implementación (API LWW y escritura/lectura local). La lectura de código y pruebas respalda los recorridos citados, sin nueva implementación ni pruebas añadidas en este delta. El CI de la punta pasa Android/backend, contrato y el paso de health tras hook Render. No confundir esto con persistencia durable o aceptación móvil: el estado sigue en memoria, el almacenamiento local no es idempotente y la prueba LWW procesa secuencialmente, no prueba concurrencia real.

**Próximos pasos:**
- Conservar la tabla y los dos contrastes ya incorporados; añadir prueba propia del rechazo de montos y del caso de uso completo.
- Precisar garantías ante reinicios, relojes desajustados, confirmación de envíos y duplicados locales; no llamar concurrente a la prueba secuencial.
- Completar caché/no caché, comparación de costo de reversión y alineación C4 con memoria actual/Room futuro; publicar dominio institucional.

**Issues GitHub:** 0 abiertas / 6 cerradas; 0 abiertas sin asignar. Motivos: 5 completed; 1 duplicate.

**README:** Externo. Backend Render. El CI incluye paso de health exitoso; no es verificación funcional propia ni evidencia de frontend institucional.

**PR consultadas:** [#26](https://github.com/ISCOUTB/AS_202620_XALD/pull/26): fusionada 2026-10-04T20:45:54Z; [#25](https://github.com/ISCOUTB/AS_202620_XALD/pull/25): fusionada 2026-09-27T16:50:53Z; [#24](https://github.com/ISCOUTB/AS_202620_XALD/pull/24): fusionada 2026-09-27T16:24:00Z; [#23](https://github.com/ISCOUTB/AS_202620_XALD/pull/23): fusionada 2026-09-20T17:34:35Z; [#22](https://github.com/ISCOUTB/AS_202620_XALD/pull/22): cerrada sin fusión registrada; [#21](https://github.com/ISCOUTB/AS_202620_XALD/pull/21): cerrada sin fusión registrada; [#20](https://github.com/ISCOUTB/AS_202620_XALD/pull/20): fusionada 2026-09-20T16:21:31Z; [#19](https://github.com/ISCOUTB/AS_202620_XALD/pull/19): fusionada 2026-09-16T04:45:22Z; [#18](https://github.com/ISCOUTB/AS_202620_XALD/pull/18): fusionada 2026-09-14T03:06:22Z; [#15](https://github.com/ISCOUTB/AS_202620_XALD/pull/15): fusionada 2026-09-13T16:09:58Z; [#10](https://github.com/ISCOUTB/AS_202620_XALD/pull/10): fusionada 2026-09-07T02:54:50Z; [#9](https://github.com/ISCOUTB/AS_202620_XALD/pull/9): fusionada 2026-09-07T02:20:49Z.

**CI consultado:** [Android CI](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/40148672496): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/README.md) · [docs/arc42/08-Cross-cutting Concepts.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/docs/arc42/08-Cross-cutting%20Concepts.md) · [docs/arc42/arc42-template-EN.md](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/docs/arc42/arc42-template-EN.md) · [backend/app/main.py](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/backend/app/main.py) · [backend/tests/test_lww.py](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/backend/tests/test_lww.py) · [XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/XALDAPP/corefinanciero/src/main/java/com/proyecto/xald/corefinanciero/GestorCoreFinanciero.kt) · [XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt](https://github.com/ISCOUTB/AS_202620_XALD/blob/4f5aa7f24ffb0c0b78abea84f7e6738d3f024a13/XALDAPP/app/src/test/java/com/proyecto/xald/Cortevertical.kt)

<a id="verifacts"></a>

## VeriFacts

Rama **master**, [cf2075dcae6ba48507ba47b59aede18afb4df449](https://github.com/ISCOUTB/AS_202620_Verifacts/commit/cf2075dcae6ba48507ba47b59aede18afb4df449), fecha del commit 2026-10-24T17:50:57Z (UTC).

Atiende tres pendientes documentales mediante issues #1–#3 creadas y cerradas completed: README actualizado a 66 pruebas y prototipo aislado; C4 distingue Traefik/nginx del modo local; arc42 acota la consistencia a visibilidad tras commit en un nodo y no afirma linearizabilidad general. El delta es documental, no nuevas mitigaciones de producto. La punta registra Tests y smoke de imagen exitosos, 66 pruebas y Quality Gate PASSED confirmado en log. El README reconoce que iscoutb.dev/certificado siguen pendientes y conserva los límites del prototipo.

**Próximos pasos:**
- No volver a pedir las tres correcciones documentales ya verificadas; conservar separación entre garantías del producto y prototipo.
- Publicar URL exacta bajo iscoutb.dev y certificado válido, distinguiendo frontend y API.
- Atender mitigaciones SSRF/historial y resiliencia declaradas pendientes; añadir pruebas/build frontend y mediciones reales sin confundirlas con simulaciones.

**Issues GitHub:** 0 abiertas / 3 cerradas; 0 abiertas sin asignar. Motivos: 3 completed.

**README:** Externo. Referencia HTTP sslip. README declara pendiente dominio institucional/certificado; frontend / y API /docs,/health separados conceptualmente.

**CI consultado:** [Tests](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996304): success (misma punta); [SonarCloud](https://github.com/ISCOUTB/AS_202620_Verifacts/actions/runs/40117996296): success (misma punta). El alcance efectivo se describe arriba; un job verde no acredita pasos omitidos.

**Fuentes:** [README.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/README.md) · [docs/c4/02-contenedores.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/docs/c4/02-contenedores.md) · [docs/arc42/08-conceptos-transversales.md](https://github.com/ISCOUTB/AS_202620_Verifacts/blob/cf2075dcae6ba48507ba47b59aede18afb4df449/docs/arc42/08-conceptos-transversales.md)

