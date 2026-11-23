# mapsutb · Retroalimentación de cierre S16

**Evidencia evaluada.** Rama `master`, [candidato S16 `0e21bd155c2c989bcd6fc0f9380e7faabab5460e`](https://github.com/ISCOUTB/AS_202620_mapsutb/commit/0e21bd155c2c989bcd6fc0f9380e7faabab5460e), observado en remoto alrededor del cierre. [Comparación con S10 `1b296a3`](https://github.com/ISCOUTB/AS_202620_mapsutb/compare/1b296a37c575a751e99df1a1b288d70efba03d56...0e21bd155c2c989bcd6fc0f9380e7faabab5460e). El registro remoto no certifica el envío individual en SAVIO.

### Alcance y decisiones

El alcance pasó de validar la base de mapa y navegación en S10 a integrar geolocalización, mapa Flutter/OSM, grafo propio con Dijkstra, catálogo e interfaz en tres idiomas. La navegación del grafo no debe confundirse con tener mapas disponibles sin conexión desde un arranque frío. La panorámica 360° queda diferida y la mensajería simulada no se presenta como servicio de producción. Esa delimitación debe coincidir en README, arc42 y demo.

El ADR 0003 registra el descarte de realidad aumentada, el 0012 el cambio de base cartográfica, y el 0019 ratifica que la analítica GA4 se envía con política de mejor esfuerzo y sin reintentos automáticos. La evaluación del prototipo de reintento encontró esperas de hasta 1,4 s y posibles duplicados; es evidencia para la decisión, no latencia de producción. El [ADR 0001](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/0e21bd155c2c989bcd6fc0f9380e7faabab5460e/docs/adr/0001-patrones-de-diseno.md) declara su edición después de aceptado y referencia el reemplazo 0002. Hacia adelante, mantengan el original y registren sustituciones de forma explícita.

### arc42, C4 y trazabilidad

Se encontraron arc42 con glosario y C4 de contexto, contenedores y componentes. No encontré §7 como sección propia de arc42 en el candidato; hay evidencia de despliegue en README y taller aparte. Vinculen esa evidencia desde una vista de despliegue para distinguir cliente, Firebase Hosting, proveedor cartográfico y dependencias externas.

En la [matriz de aspectos](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/0e21bd155c2c989bcd6fc0f9380e7faabab5460e/docs/aspectos.md), cuatro de cinco filas tienen evidencia identificable y A-04 (360°) se declara diferida. A-01: simulación de recorrido con p95 de 0,68 ms para la ruta y 19 ms para pantalla frente al umbral de 5 s; el dato de campo de 5,8 m es mediana de herramientas externas de GPS, no medida de precisión de la app. A-02: hay contrato de proveedor y prueba de CI; A-03 deja rastrear el catálogo al dato. A-05: 984 muestras históricas en seis ventanas reportan 100 % y p95 de 212 ms para salud; el valor p95 de 266 ms viene de 60 consultas de cliente. No representan disponibilidad futura ni una prueba de rutas en dispositivo. La [bitácora de IA](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/0e21bd155c2c989bcd6fc0f9380e7faabab5460e/docs/ia.md) ayuda a distinguir uso de herramientas de evidencia efectivamente comprobada.

### Qué se verificó y qué falta demostrar

- **CI del SHA exacto:** [corrida 45109179288](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/45109179288) en verde con análisis Flutter, OSV, pruebas Flutter y de contrato, y [Sonar Quality Gate](https://github.com/ISCOUTB/AS_202620_mapsutb/runs/137477904478) aprobado.
- **Despliegue:** [corrida 45109179388](https://github.com/ISCOUTB/AS_202620_mapsutb/actions/runs/45109179388) verde; hizo pruebas, inspección del build por secretos de analítica, compilación/publicación a Firebase y verificación de URL y salud. El [README](https://github.com/ISCOUTB/AS_202620_mapsutb/blob/0e21bd155c2c989bcd6fc0f9380e7faabab5460e/README.md) referencia [mapsutb.web.app](https://mapsutb.web.app/). No se hizo una visita ni una prueba de GPS, rutas o navegador fuera de CI.
- **Colaboración:** 36 commits en la comparación de cortes. Ese total no permite acreditar participación o revisiones individuales.

**Prioridad:** medir en la app en el campus y separar en el acta de evidencia disponibilidad del sitio, disponibilidad del proveedor y experiencia efectiva de navegación.

### Preguntas de sustentación

1. Al negar el permiso o recibir una ubicación desplazada, ¿cómo el motor elige el origen y qué evidencia mediría la precisión en la app?
2. ¿Qué puede hacer alguien en un arranque sin conexión, en contraste con una caída de OSM después de cargar el mapa? Muéstrenlo sin confundir grafo con teselas.
3. Si falla geocodificación o GA4, ¿qué se pierde y qué sigue sirviendo al usuario? ¿Qué prueba demuestra que esas dependencias no bloquean la ruta?

### Propuesta técnica de rúbrica (sin nota final)

- C1: pendiente de desafío asignado y demostración.
- C2: Sobresaliente documental — ADR 0019 ratifica la decisión de reintentos con costo temporal cuantificado.
- C3: Competente — mediciones comparadas y controles; GPS real pendiente.
- C4: Básico — trazas parciales y vista de despliegue dispersa.
- C5: reservado al docente. Total pendiente.

## Verificación independiente del corte y del despliegue

El historial de `origin/master` filtrado hasta las 05:00 UTC devuelve el mismo SHA observado en GitHub inmediatamente después del corte de referencia. Se mantiene la salvedad de SAVIO y de entrega acreditada.

**Sondas de solo lectura del 23 de noviembre:**

- web externa: [https://mapsutb.web.app/](https://mapsutb.web.app/) → HTTP 200 (13:28:13 UTC).
- salud externa: [https://mapsutb.web.app/health.json](https://mapsutb.web.app/health.json) → HTTP 200, reporta `5704257457b7` (no es el SHA evaluado) (13:28:13 UTC).

Una respuesta de salud o carga de página solo acredita esa ruta y ese momento; no demuestra flujo de negocio, datos realistas, error controlado ni correspondencia con el SHA salvo evidencia explícita. No se ejecutó código estudiantil ni se hicieron escrituras.
