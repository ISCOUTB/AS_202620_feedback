# XALD · Retroalimentación de cierre S16

**Evidencia evaluada.** Rama `master`, [candidato S16 `166693dee5d49e408782cfb0fcd278320338dd27`](https://github.com/ISCOUTB/AS_202620_XALD/commit/166693dee5d49e408782cfb0fcd278320338dd27), observado en remoto alrededor del cierre. [Comparación con S10 `9236ff9`](https://github.com/ISCOUTB/AS_202620_XALD/compare/9236ff97218b632eeb9a1910f6083968e2c22909...166693dee5d49e408782cfb0fcd278320338dd27). El registro remoto no certifica el envío individual en SAVIO.

### Alcance y decisiones

El prototipo de S10 dejaba la integración móvil, la persistencia y el SMS real como brechas y trabajaba con Gemini simulado. En S16 ya se ve repositorio PostgreSQL con integración, sincronización móvil por red con reintentos y procesamiento de SMS con consentimiento. La funcionalidad de Gemini deja de ser solo un mock en el código; falta demostrar el flujo con dispositivo y proveedor. Es avance material respecto al alcance, no certificación de todas las rutas.

El ADR 0014 vincula la sincronización eventual con reintentos, tiempos de espera y manejo de pendientes. El ADR 0017 acota los datos enviados a Gemini y documenta el manejo previsto; el 0012 conserva la fotografía legítima del aplazamiento previo. En la matriz, distingan el estado anterior del vigente. Hay dos ADR con número 0015 y cambios a documentos históricos: dejen referencias inequívocas y preserven el historial mediante estados de sustitución cuando cambie una decisión.

### arc42, C4 y trazabilidad

Hay arc42 con secciones 1 a 12 y glosario, además de una plantilla integrada y C4 de contexto, contenedores y componentes. Las múltiples versiones hacen difícil identificar la fuente vigente. Recorrí los cinco aspectos: A-01, A-02, A-03 y A-05 enlazan artefactos de `experimental` en la matriz; A-04 marca código y prueba pendientes. Actualicen los enlaces al candidato que sustentan y mantengan visible lo que no está cerrado. En particular, la trazabilidad de sincronización debe llevar de escenario y ADR a código, pruebas y medición; para SMS y Gemini debe mostrar el límite de datos y qué ocurre si el usuario o el proveedor no están disponibles.

En [medición ESC-05](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/docs/medicion-esc05.md) se reporta una prueba histórica de resolución de conflictos LWW de 30/30, sin pérdidas en ese experimento. Eso no cubre relojes desfasados, reinicio ni uso simultáneo en dos dispositivos. El [registro de IA](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/docs/ia.md) muestra verificación y descarte de propuestas; como mejora, conecten esas verificaciones con el criterio de aceptación al cierre.

### Qué se verificó y qué falta demostrar

- **CI del SHA exacto:** [corrida 45113474971](https://github.com/ISCOUTB/AS_202620_XALD/actions/runs/45113474971) en verde, con pruebas Gradle del módulo Android, pytest del backend y validación OpenAPI/Redocly. [Sonar Quality Gate](https://github.com/ISCOUTB/AS_202620_XALD/runs/137491088379) también pasó. No equivale a instalar ni probar el APK en un teléfono.
- **Despliegue:** la misma corrida reporta activación del despliegue Render y verificación de salud. El [README](https://github.com/ISCOUTB/AS_202620_XALD/blob/166693dee5d49e408782cfb0fcd278320338dd27/README.md) enlaza el [backend](https://xald-backend.onrender.com) y sus pasos de uso. Es evidencia de pipeline y endpoint de salud, no verificación independiente del flujo completo o de una distribución móvil.
- **Colaboración:** 149 commits en la comparación, incluidos merges; el volumen por sí solo no acredita reparto, revisión ni autoría individual.

**Prioridad:** fijar el mismo SHA en matriz, documentación y evidencia; demostrar sincronización tras fallo y tratamiento de entrada real con datos de prueba.

### Preguntas de sustentación

1. Si un movimiento se crea sin conexión, se reinicia la app y el primer reintento vence, ¿dónde queda el estado y cómo demuestran que se sincroniza una sola vez?
2. Dos dispositivos editan el mismo registro con relojes distintos: ¿cuál gana con LWW y qué caso añadirían al conjunto de 30 conflictos?
3. Si Gemini agota la cuota o devuelve un formato inválido, ¿qué parte del flujo sigue operando, qué dato no sale del sistema y cómo lo comprobarían?

### Propuesta técnica de rúbrica (sin nota final)

- C1: pendiente de desafío asignado y demostración.
- C2: Competente — ADR 0014 y 0017 motivan la evolución; falta demostrar una ratificación o reversión cuantificada.
- C3: Competente provisional — ESC-05 y CI; no se acredita dispositivo o proveedor vivo.
- C4: Básico — trazas mayormente experimentales y una pendiente.
- C5: reservado al docente. Total pendiente.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- API externa salud: [https://xald-backend.onrender.com/health](https://xald-backend.onrender.com/health) → sin respuesta en el tiempo de espera (13:28:20 UTC).
- reintento API externa salud: [https://xald-backend.onrender.com/health](https://xald-backend.onrender.com/health) → HTTP 200, estado declarado `ok` (13:30:06 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
