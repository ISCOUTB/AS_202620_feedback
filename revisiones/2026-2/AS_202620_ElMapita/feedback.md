# Retroalimentación publicable · ElMapita

## Semana 1

- Está bien: repositorio con el nombre correcto y público; estructura montada desde el inicio (arc42 con plantilla, adr, c4); `docs/aspectos.md` con la tabla de 8 columnas y el aspecto A-01 bien descrito.
- Falta: la ficha del problema (usuarios, alcance), las dos tensiones de calidad, y contenido en `docs/ia.md` (estaba vacío en esa entrega).
- Corregir antes del corte 1: crear la ficha, declarar las tensiones, llenar `docs/ia.md`, y que los tres integrantes firmen commits (el historial solo muestra una cuenta).

## Semana 2

- Está bien: secciones 1, 2 y 3 redactadas con cuidado (restricciones clasificadas y separadas de requisitos, interesados con preocupaciones); 4 escenarios con seis partes, medidas numéricas con carga y evidencia prevista de medición; árbol de utilidad con impacto/riesgo; enlaces desde `docs/aspectos.md` a los escenarios.
- Falta: `docs/ia.md` seguía vacío en esa entrega; el C4 solo existe como imagen y el enlace a `docs/c4/contexto.md` está roto; la ficha del problema y las tensiones siguen pendientes; en la semana solo hubo un commit de una persona.
- Corregir antes del corte 1: publicar el diagrama de contexto como código con leyenda, crear la ficha con las dos tensiones, llenar `docs/ia.md` y repartir la contribución entre los tres.

## Semana 3

Qué está bien: el ADR 0001 está completo (contexto ligado a EC-01…EC-04, alternativas con pros/contras, consecuencias con mitigaciones), el esqueleto BE/FE respeta el monolito modular y `./scripts/dev.sh` está documentado como arranque único.

Qué corregir antes del corte 1 (semana 5):
1. La sección 4 de arc42 está vacía (solo el encabezado): trasladen allí la estrategia con tácticas ligadas a los escenarios; que no viva solo en el ADR y la matriz.
2. La matriz comparativa (bien ponderada) debe comparar contra los escenarios EC-01…EC-04 del árbol de utilidad, no contra criterios propios.
3. Hagan alcanzable el ADR: la columna ADR de `docs/aspectos.md` sigue «Pendiente» y los escenarios no lo enlazan.
4. `docs/ia.md` seguía vacío en esa entrega: registren usos reales y rechazos con motivo.
5. Repartan la contribución: en S3 solo una cuenta firma commits; procuren que todos aparezcan en el historial.
6. Evidencien el verde de las pruebas existentes con un pipeline o capturas de ejecución.

## Semana 4 · S4

Buen avance en documentación: C4 niveles 1 y 2 completos y coherentes, corte vertical con interfaz, lógica y persistencia, y README con arranque por script. El pipeline de CI está en rojo y las pruebas del recorrido completo siguen pendientes: las rutas citadas en docs/aspectos.md no existen. Se recomienda crear una prueba e2e del flujo de mapas y dejarla en verde, configurar SonarCloud y revisar la distribución de commits para que el historial refleje participación del equipo. También conviene verificar que las secciones 4-6, 9, 10 y 12 de arc42 estén redactadas con contenido propio.

## Semana 5 · CORTE1

El proyecto muestra una base sólida: documentación arc42, C4, ADR y trazabilidad están bien estructuradas. Sin embargo, hay deudas importantes: las pruebas de los escenarios de calidad están pendientes, el pipeline no tiene runs verificables y el corte vertical no se puede reproducir sin evidencia de ejecución. Se recomienda ejecutar las pruebas localmente y subir los resultados a CI, completar las pruebas pendientes de los aspectos, y asegurar que correcciones.md sea trazable con enlaces a commits y runs. También es clave equilibrar la contribución entre los integrantes y documentar el uso de IA con más detalle.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

El repositorio no tuvo ningún cambio entre el 1 de septiembre y el cierre del corte (7 de septiembre): toda la semana 5 quedó sin actividad. Un detalle importante sobre lo que ya tenían: el commit con el mensaje "corte-1" no es una etiqueta de Git (`git tag`); es solo el texto de un commit normal. Para que el curso reconozca un estado como "el corte 1", necesitan crear la etiqueta con `git tag corte-1` y subirla (`git push origin corte-1`), no solo nombrar así un commit.

No encontramos evidencia de que se haya diagnosticado o respondido una restricción nueva: el único ADR sigue siendo el de la arquitectura base (muy bien escrito, con alternativas y consecuencias claras, pero es de otra semana), las cuatro filas de `docs/aspectos.md` siguen con la evidencia marcada "Pendiente", y el pipeline de integración continua está en rojo en los tres intentos que registra GitHub Actions, incluido el commit que se presenta como entrega.

Además, revisando el historial completo del repositorio, seguimos sin ver ningún commit de uno de los integrantes declarados. Si sus aportes existen fuera de Git (diseño, decisiones, documentación en otro medio), tráiganlos a la sustentación, porque desde el repositorio no son visibles.

Para la próxima entrega: creen la etiqueta real, retomen el trabajo cuanto antes (una semana completa sin commits es un riesgo), arreglen el pipeline, y aporten la restricción, el diagnóstico y la medición que pide este corte.

## Semana 7 · S7

El contrato OpenAPI 3.1 versionado, con rutas y esquemas de datos, y el ADR de integración están bien resueltos: la decisión síncrona frente a AsyncAPI está bien argumentada. Revisión actualizada tras el cierre: al releer en el repositorio lo que la pasada automática no había podido abrir, se confirma que el job `contract` del pipeline ejecuta la prueba de contrato, que la sección 6 de arc42 describe los flujos de interacción y que el C4 nivel 2 etiqueta protocolo y formato, además de que la tabla de aspectos tiene sus ocho columnas. Quedan abiertos tres puntos: 1) unifiquen el prefijo de rutas, hoy el backend expone /api/api/v1/... y el contrato y el cliente usan /api/v1/..., lo que deja la correspondencia contrato-código en no conformidad; 2) aporten una ejecución en rojo provocada por un cambio incompatible: sin ella no se demuestra que la prueba sirva; 3) sumen la evidencia de SonarCloud (configuración, run y URL pública con Quality Gate), hoy ausente. Completen también las celdas de Pruebas y Evidencia de la tabla de aspectos, aún en "Pendiente". El registro de uso de IA ya está al día: crece y documenta los rechazos con su motivo.
## Semana 6 · S6

El repositorio va bien encaminado: conserva estructura, ADR, README y un registro de IA que crece durante el semestre. Para la próxima entrega, pasen a Markdown revisable el mapa de contextos y la tabla módulo a datos, que hoy solo existen como documentos binarios. En el mapa, nombren los contextos del dominio y el tipo de relación entre ellos (núcleo compartido, cliente y proveedor, capa anticorrupción), y enlácenlo desde la sección 8 de arc42. En la tabla, una entidad por fila con un único dueño, y verifiquenla contra las entidades que realmente existen en el código. Acompañen la lista de no conformidades con la ruta exacta donde ocurre cada escritura y la acción de corrección. Publiquen la evidencia de SonarCloud: archivo de configuración, run de CI y URL del análisis con el estado del Quality Gate. Completen docs/aspectos.md sin celdas huecas y limpien los archivos temporales de Office. Si los límites cambiaron respecto al primer corte, agreguen el ADR de reajuste y el diff contra el hash revisado.

## Semana 8 · S8

Está bien: la infraestructura como código versionada (el blueprint de despliegue más el Dockerfile del backend), el pipeline en verde sobre la rama principal con un gate que bloquea el merge, los logs estructurados con salida JSON, una métrica de latencia ligada al escenario de carga inicial y consultable en el endpoint de métricas, la protección de secretos (variables declaradas como secretas en el blueprint y tomadas del entorno), la estimación de costo mensual con supuestos y punto de ruptura, la vista de despliegue con una caja por pieza y un ADR de plataforma con su alternativa descartada.

Qué corregir: la sección 2 de arc42 debe recoger el límite de costo y la condición de tarjeta como restricciones (hoy solo viven en el ADR); la evidencia de SonarCloud (configuración, run y URL pública con el estado del Quality Gate) sigue ausente; conviene fijar el host real de la sección 7 en el proveedor elegido, que hoy sigue como una lista de opciones; los ADR aceptados no deben editarse sin declarar reemplazo; y la contribución debe repartirse para que todos los integrantes aparezcan en el historial.

La URL del despliegue y la comprobación de salud quedan diferidas por decisión docente: se entregan por Moodle.

## Semana 9 · S9 (revisión definitiva)

Hay una porción nueva con IA, una prueba roja y verde documentada, mediciones honestas y ADR sustitutos. Se valora que los resultados fallidos se publiquen sin maquillarlos. Completen la cadena navegable e integren el validador en el flujo real; medir un fallo aporta evidencia, pero no significa que el escenario de calidad ya cumpla.

## Semana 10 · Segundo corte

### Consolidación vigente · 13 de octubre de 2026

La caracterización se apoya en un estado inicial negativo de 0/20, con control online y procedimiento. Ese resultado no se interpreta como cumplimiento del comportamiento offline. La respuesta offline y la coherencia documental siguen incompletas.

Se valora el escenario documentado bajo un supuesto explícito de pertinencia; su asignación oficial no se presenta como verificada. Las mediciones conservan el alcance y las limitaciones descritos en la evidencia. Los comentarios anteriores se mantienen como historial y la evaluación de la semana anterior permanece congelada.

La sustentación comunicada por el docente ya está incorporada en la [planilla](planilla.md) y el [informe del corte](semana-10-corte2.md).

### Deriva arquitectónica al cierre S10

Escritura sin autorización; ubicación, caché offline y dependencias divergentes.

Se contrastaron las declaraciones con las rutas de código del cierre mediante inspección estática. No se ejecutó el sistema ni se verificó el comportamiento del servicio remoto.

- **Alta · La escritura de POIs anunciada como admin no atraviesa autorización:** Si la API está expuesta con la configuración prevista, el código no exige identidad/rol antes de solicitar un upsert. No se afirma explotación ni éxito contra una BD real. **Acción:** Añadir guard JWT validado y guard de rol admin en la entrada, pasar identidad al caso de uso y verificar 401/403 y ausencia de escritura con pruebas. Revisar también las operaciones administrativas de Auth. Swagger addBearerAuth no aplica autorización. [Contraste y evidencia](semana-10-corte2.md#deriva-d1).
- **Media · La ruta real de ubicación omite el caso de uso que filtra precisión y timeout:** GET current puede entregar la ubicación ficticia de precisión 999 m en vez del veredicto de fallback. No se atribuye ese resultado al GPS físico de Flutter. **Acción:** Conectar la entrada HTTP a GetValidatedLocationUseCase o retirar/etiquetar ese endpoint como simulación de servidor. Definir claramente que el GPS real vive en el móvil; añadir prueba de integración router→provider impreciso/timeout. [Contraste y evidencia](semana-10-corte2.md#deriva-d2).
- **Media · La recuperación offline documentada queda detrás de una llamada de red obligatoria:** LoadBuildingUseCase retorna error antes de consultar ModelCache ante fallo de API, por lo que una caché caliente no basta para el modo offline descrito. **Acción:** Persistir metadatos/versiones junto al binario y resolverlos desde caché al fallar la red; emitir estado offline explícito y probar caché válida sin backend. La evidencia S9 ya caracteriza la carencia; no se vende como una regresión nueva. [Contraste y evidencia](semana-10-corte2.md#deriva-d3).
- **Media · LoadBuildingUseCase depende de adaptadores concretos pese a la regla de interfaces:** Cambiar API/cache puede requerir editar el caso de uso y sus pruebas en lugar de sustituir implementaciones detrás de puertos. **Acción:** Definir puertos de consulta de edificios y caché en dominio/aplicación; inyectar implementaciones MapasApi y ModelCache desde DI. Alternativamente aprobar y documentar el acoplamiento pragmático, sin seguir afirmando solo interfaces. [Contraste y evidencia](semana-10-corte2.md#deriva-d4).

[Ver cobertura, fuentes y límites de la auditoría](semana-10-corte2.md#deriva-arquitectónica-al-cierre-s10).

<details>
<summary>Comentarios preliminares anteriores, superados por la consolidación del 13 de octubre</summary>

Estos comentarios corresponden al estado y a las comprobaciones de sus fechas originales. Las referencias a pendientes, disponibilidad y asignación del escenario no sustituyen el feedback vigente.

El health check responde, pero siguen abiertos el flujo real del validador, el modelo3D y el modo offline. El CI general verde no demuestra SonarCloud porque ese job es no bloqueante. Para el corte, identifiquen la consigna asignada, midan la línea base y repitan el experimento tras corregir los defectos.

</details>

## Semana 11 · Integración y resiliencia

El estado anterior al cierre solo acredita la integración principal y la evaluación de mantener el monolito. El ADR de extracción y la tabla agregados después del cierre se registran como avance actual y no recalifican S11. Completar los tres modos de fallo, la correspondencia de mitigaciones y el diseño de idempotencia para las escrituras existentes.

Consulta la [matriz S11](semana-11-evidencia-s11.md) para las evidencias y los pendientes. La evidencia posterior al cierre aparece separada en el seguimiento actual.

## Semana 12 · Avance preliminar: consistencia, caché y decisiones de datos

La caché versionada, el flujo síncrono y los almacenes separados en C4 aportan evidencia inicial. Faltan garantías por operación con dos contrastes, invalidación efectiva, ADR comparativo de reversión de datos y actualización de arc42 sección 8. Reconciliar la promesa de funcionamiento offline con un caso de uso que consulta primero la API.

Consulta la [matriz S12 preliminar](semana-12-evidencia-s12.md) para las evidencias y los pendientes. El plazo sigue abierto hasta el final del 25 de octubre en Colombia.

## Seguimiento documental · 20 de octubre de 2026

Presentó avance y está funcionando, según confirmación docente. Falta la URL pública concreta en el README; esta carencia documental no significa ausencia de despliegue.

Issues al corte de consulta: **1 abiertas, 0 cerradas, 1 en total**. Sin cierres registrados. Estos estados no equivalen por sí solos a implementación verificada.

README y despliegue: **Sin URL vigente**. Solo localhost y placeholder de Supabase; funcionamiento confirmado por docente.

Consulta el [recuento y análisis de issues](../seguimiento-issues-2026-10-20.md) y la [revisión de URL/dominio](../seguimiento-despliegues-2026-10-20.md). El requisito docente es publicar la URL oficial en el README con subdominio iscoutb.dev; una URL de API no sustituye la del sitio cuando sean diferentes. El bloqueo de la consulta automatizada no demuestra caída. Este seguimiento no modifica notas ni matrices históricas.

## Seguimiento actual · 22 de octubre de 2026 · S12 abierta

Esta actualización orienta el trabajo pendiente hasta el final del 25 de octubre en Colombia. No modifica calificaciones ni matrices anteriores; los faltantes históricos deben leerse junto con este avance.

Sin commits desde 20 de octubre; CI success. Presentación y funcionamiento confirmados por docente; README solo localhost/Supabase placeholder, brecha documental no ausencia de despliegue.

**Próximos pasos:**
- Publicar URL exacta iscoutb.dev del despliegue mostrado, sin inventar host.
- Tabla operaciones reales (cargar edificio/registro o rol) → garantía y dos recorridos de código; definir invalidación/versionado al reemplazar modelo, no solo TTL.
- ADR comparativo del costo de revertir datos y llevar consistencia/caché a arc42 §8, hoy solo errores/privacidad/internacionalización.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado del tablero no equivale a implementación verificada.

**README/despliegue:** Sin URL concreta. Solo localhost y un placeholder de Supabase. El docente confirmó presentación y funcionamiento; falta reflejar la URL. Debe figurar la URL oficial exacta bajo iscoutb.dev, diferenciando interfaz y API cuando corresponda.

[Fuentes y alcance de esta revisión](../seguimiento-s12-2026-10-22.md#elmapita) · [Issues y estados](../seguimiento-issues-2026-10-22.md) · [URL y dominio](../seguimiento-despliegues-2026-10-22.md).

## Seguimiento actual · 24 de octubre de 2026 · S12 abierta

Seguimiento de trabajo, sin cambios de calificación. S12 sigue abierta hasta el final del 25 de octubre en Colombia; leer los pendientes históricos junto con esta actualización.

La rama principal y el README no cambian respecto al 22 de octubre; el CI de esa punta continúa registrado como exitoso. Se conserva la confirmación docente de presentación y funcionamiento. Falta publicar la dirección exacta del despliegue bajo iscoutb.dev: localhost y un ejemplo de Supabase no satisfacen el requisito documental.

Presentación y funcionamiento confirmados por el docente.

**Próximos pasos:**
- Publicar URL exacta iscoutb.dev del despliegue mostrado, sin inventar host.
- Tabla operaciones reales (cargar edificio/registro o rol) → garantía y dos recorridos de código; definir invalidación/versionado al reemplazar modelo, no solo TTL.
- ADR comparativo del costo de revertir datos y llevar consistencia/caché a arc42 §8, hoy solo errores/privacidad/internacionalización.

**Issues:** 1 abiertas y 0 cerradas; 1 abiertas sin responsable. El estado registrado no acredita por sí solo implementación.

**README:** Sin URL concreta. README solo localhost y placeholder Supabase. Presentación y funcionamiento confirmados por el docente; brecha documental, no ausencia de despliegue. Debe publicar la URL oficial exacta bajo iscoutb.dev y distinguir interfaz de API cuando corresponda.

[Fuentes y alcance](../seguimiento-s12-2026-10-24.md#elmapita) · [Issues y estados](../seguimiento-issues-2026-10-24.md) · [URL y dominio](../seguimiento-despliegues-2026-10-24.md).



## Seguimiento actual · 25 de octubre de 2026 · S12 abierta

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin nueva punta ni cambio de README desde el 24/oct, con CI exitoso de ese head. Se conserva presentación y funcionamiento confirmados por el docente. Sigue faltando la URL pública concreta del despliegue en README; localhost y placeholder Supabase no la sustituyen.

**Próximos pasos:**
- Publicar en README la URL iscoutb.dev exacta del despliegue mostrado, sin inventar host.
- Mantener pendientes S12 del 24/oct sobre garantías, invalidación/versionado de modelos y ADR comparativo.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

[Fuentes y alcance](../seguimiento-s12-2026-10-25.md#elmapita) · [Issues](../seguimiento-issues-2026-10-25.md) · [URL y dominio](../seguimiento-despliegues-2026-10-25.md).


## Seguimiento actual · 26 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Sin nueva punta ni cambio del README respecto al 25/oct. CI de esa punta continúa exitoso. Se conserva la presentación y funcionamiento confirmados por el docente; sigue faltando URL pública concreta en README y no se infiere falta de despliegue por ese vacío documental.

**Próximos pasos:**
- Publicar URL exacta del despliegue operativo en README bajo iscoutb.dev.
- Conservar y completar evidencia S12 sin confundir ausencia documental con ausencia de avance.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

[Fuentes y alcance](../seguimiento-s12-2026-10-26.md#elmapita) · [Issues](../seguimiento-issues-2026-10-26.md) · [URL y dominio](../seguimiento-despliegues-2026-10-26.md).


## Seguimiento actual · 28 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Integra caché TTL/LRU del backend, invalidación de POIs, limpieza de versiones de modelos del cliente y mensajería en memoria con reintentos, DLQ y auditoría. Añade reconciliación al arrancar y cada diez minutos desde POIs persistidos para reconstruir la proyección de auditoría: mitigación específica, no outbox ni bus durable. El CI global aparece exitoso y confirma 56 pruebas unitarias backend; sin embargo, el E2E GET / falla (404 frente a 200 esperado) y su error se neutraliza con echo. SonarCloud falla por autorización/proyecto no encontrado y omite Quality Gate; es no bloqueante. El README continúa sin URL pública concreta. Se conserva la confirmación docente de que ElMapita presentó y funciona; no se atribuye esa aceptación a esta punta ni se verificó su nuevo despliegue.

**Próximos pasos:**
- Corregir el E2E y hacer explícitos/bloqueantes los checks necesarios; resolver autorización/configuración de SonarCloud.
- Documentar en README URLs reales de frontend/API bajo iscoutb.dev y el commit desplegado, sin sustituir la aceptación docente previa por CI.
- Validar recuperación tras reinicio y límites del reconciliador; no presentar auditoría en memoria como durabilidad del bus.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta; no implica ausencia de despliegue.

[Fuentes y alcance](../seguimiento-s12-2026-10-28.md#elmapita) · [Issues](../seguimiento-issues-2026-10-28.md) · [URL y dominio](../seguimiento-despliegues-2026-10-28.md).


## Seguimiento actual · 29 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Añade configuración reproducible de Dokploy en deploy/compose.lab.yaml, ejemplo de variables y exclusión de deploy/.env. El Compose despliega solo la API NestJS, no Flutter, y mantiene Supabase externo; el dominio institucional que figura como FRONTEND_URL es configuración y no acredita un frontend ni despliegue activo. El README sigue sin URL pública concreta. El nuevo CI global figura exitoso: confirma 56 pruebas unitarias backend y construcción de imagen, pero el E2E GET / vuelve a fallar (404 frente a 200 esperado) y el workflow neutraliza su error con echo. SonarCloud falla por autorización/proyecto no encontrado y omite su Quality Gate; no bloquea el resultado global. Se conserva la confirmación docente de que ElMapita presentó y funciona, sin atribuirla a esta nueva punta ni a una verificación en vivo de este corte.

**Próximos pasos:**
- Publicar en README la URL institucional exacta y distinguir API NestJS de frontend Flutter; validar el dominio y hash realmente desplegados, no inferirlos del ejemplo de variables.
- Corregir el E2E y hacer bloqueantes las verificaciones necesarias; resolver acceso/configuración de SonarCloud y acreditar su Quality Gate.
- Conservar explícitos los límites de mensajería en memoria y reconciliación, sin presentarlos como outbox o broker durable.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta. Compose nuevo solo para API; FRONTEND_URL en configuración no prueba frontend ni despliegue activo. Se conserva aceptación docente previa, distinta de la publicación de esta punta.

[Fuentes y alcance](../seguimiento-s12-2026-10-29.md#elmapita) · [Issues](../seguimiento-issues-2026-10-29.md) · [URL y dominio](../seguimiento-despliegues-2026-10-29.md).


## Seguimiento actual · 30 de octubre de 2026 · sin cierre automático de S12

Actualización documental sin recalificar ni cerrar la entrega. Los informes históricos conservan su fecha; para pendientes actuales, leer este corte.

Integra mapa 3D del campus con capas, selección de destino, animaciones, georreferencia, ubicación y avisos de llegada por vibración; incorpora navegación entre mapa/lugares e idiomas español/inglés. El código y las pruebas están en main, aunque docs/ia.md todavía describe una parte como sin commit: debe reconciliarse esa bitácora. El CI de la punta pasa 30 pruebas Flutter, build web y 56 pruebas unitarias backend. El verde global sigue siendo parcial: flutter analyze informa 28 hallazgos; E2E GET / falla con 404 frente a 200 y se neutraliza con echo; SonarCloud falla por autorización/proyecto no encontrado y omite el gate. El equipo documenta comprobaciones en teléfono y calibración aproximada con OpenStreetMap, no verificadas independientemente aquí. El README continúa sin URL pública concreta y Compose sigue dirigido al backend. Se conserva la confirmación docente de que ElMapita presentó y funciona, sin atribuir aceptación de estas nuevas funciones a este corte.

**Próximos pasos:**
- Documentar en README la URL exacta bajo iscoutb.dev, separando API y frontend; aportar evidencia fechada del despliegue de esta punta.
- Hacer vinculante el E2E de backend, atender los 28 hallazgos de analyze y restablecer SonarCloud/Quality Gate antes de describir el CI como completo.
- Reconciliar docs/ia.md con los commits publicados y validar en dispositivos reales permisos de ubicación, guía de llegada, calibración y cambio de idioma.

**Issues GitHub:** 1 abiertas y 0 cerradas; 1 abiertas sin asignar. Cierres: —. No son estados de un tablero Projects ni prueba automática de implementación.

**README:** Sin URL concreta. README sin URL pública concreta. Compose nuevo solo para API; FRONTEND_URL en configuración no prueba frontend ni despliegue activo. Se conserva aceptación docente previa, distinta de la publicación de esta punta.

[Fuentes y alcance](../seguimiento-s12-2026-10-30.md#elmapita) · [Issues](../seguimiento-issues-2026-10-30.md) · [URL y dominio](../seguimiento-despliegues-2026-10-30.md).
