# Retroalimentación publicable · uniTeam

## Semanas 1 y 2

## Evidencia S1

Bien: repositorio con el nombre de la convención, ficha del problema con usuarios y alcance, plantilla arc42 descomprimida, `docs/adr/` y `docs/c4/` creados, y registro de IA iniciado.

Corregir: la ficha del problema debe declarar las dos tensiones de calidad enfrentadas (dos atributos en conflicto); `docs/aspectos.md` debe ser la tabla de ocho columnas del curso con al menos una fila con ID y aspecto; y en `docs/ia.md` conviene registrar entradas por uso y qué se rechazó y por qué. Confirmen también que todos los integrantes tienen acceso al repositorio y hagan que cada uno firme commits con su propia cuenta.

## Evidencia S2

Bien: secciones 1, 2 y 3 del arc42 redactadas y coherentes, restricciones clasificadas (técnicas, organizativas, legales) y justificadas, cinco escenarios con sus seis partes y medida numérica —y además con método de verificación—, árbol de utilidad priorizado con justificación, C4 de contexto como código con leyenda y flechas etiquetadas, y aspectos enlazados a sus escenarios. Nivel sobresaliente.

Corregir antes del corte 1: renombrar el ADR a la convención `NNNN-titulo-en-kebab-case.md` (sin el prefijo «ADR-»), asegurar que los cuatro integrantes aparezcan en el historial de commits, y revisar que el historial del repositorio no conserve archivos de un proyecto anterior.

## Semana 3

Qué está bien: la sección 4 de arc42 trae tácticas por escenario, la matriz compara los tres estilos contra sus propios escenarios, el ADR-003 justifica la decisión con alternativas descartadas y la estructura de paquetes es coherente con el estilo elegido.

Qué corregir antes del corte 1 (semana 5):
1. Renombrar los ADR a la convención `NNNN-titulo-en-kebab-case.md` (quitar «ADR-» y el « (1)») y marcar ADR-001 como reemplazado por ADR-002.
2. Enlazar el ADR-003 desde `docs/aspectos.md` y desde el escenario que lo motiva.
3. Documentar en el README el comando único de arranque de la app (hoy solo está el de la prueba) y corregir el paquete `httpx2` de `requirements.txt`.
4. Registrar en `docs/ia.md` el uso de IA de esta semana con lo rechazado y su motivo.
5. Contribución: solo una persona firmó los commits de esta semana; todos los integrantes deben aparecer en el historial antes del corte 1.

## Semana 4 · S4

La entrega de la semana 4 está sólida en lo que se pudo verificar: C4 como código con coherencia entre niveles, corte vertical con las tres capas citadas, arranque con un solo comando y tabla de aspectos con enlaces navegables. Para cerrar los huecos de verificación, conviene que la sección 9 de arc42 cite explícitamente los ADR, que la sección 10 referencie los escenarios de calidad y que el glosario use términos propios del dominio. Aporten también la URL del run de CI en verde que ejecuta la prueba del recorrido completo; el badge del README no es evidencia de ejecución. El registro de IA debe mostrar lo aceptado y lo rechazado con su motivo. La medición de ESC-01 es un buen cierre y deja la línea base lista para el corte.

## Semana 5 · CORTE1

Sin actividad CORTE1: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.
## Semana 5 · Primer corte (revisión definitiva, 2026-09-07)

El repositorio no tiene la etiqueta `corte-1` y no cambió entre la revisión de antes del cierre y el cierre mismo. Dicho eso: encontramos un trabajo (la decisión de delegar la autenticación en un proveedor externo, en vez de confiar en una cabecera que cualquiera podía falsificar) que tiene toda la forma de una buena respuesta a una restricción — diagnóstico claro, comparación real de alternativas con sus costos, decisión documentada, implementación de punta a punta que arranca con un solo comando, y pruebas en verde. Lo evaluamos como su respuesta más probable al reto, aunque el repositorio no lo declara explícitamente como tal — en la sustentación conviene confirmar si esa fue, en efecto, la restricción asignada.

Lo que le falta a esa respuesta para estar completa: (1) medir con una cifra cómo de explotable era el problema antes del cambio, no solo describirlo; (2) medir el resultado después del cambio y compararlo contra el umbral de ese escenario de seguridad; y (3) una entrada en el registro de uso de IA que hable puntualmente de esta pieza de trabajo (qué se aceptó, qué se corrigió o rechazó y por qué), no solo de las decisiones de otras semanas.

Sobre la autoría: con esta revisión pudimos atribuir contribución a los cuatro integrantes declarados, algo que antes no se había podido confirmar del todo. Queda pendiente identificar a quién corresponde una cuenta adicional que aparece en el historial con más commits que cualquier otra.

## Semana 6 · S6

El mapa de contextos y la tabla inicial de dueño único tienen una estructura clara: distinguen relaciones síncronas, eventos y consumidores de solo lectura. El siguiente paso indispensable es convertir la auditoría prevista en evidencia real: contrasten cada entidad con el esquema y los modelos, reemplacen los marcadores “revisar” por no conformidades con ruta y línea, y enlacen cada corrección con una acción concreta. Incorporen el mapa y el lenguaje ubicuo en la sección 8 de arc42, relacionen los contextos con la tabla de aspectos y publiquen el análisis SonarCloud con su Quality Gate.

## Semana 7 · S7

Sin actividad S7: el ultimo commit anterior al cierre es de la entrega previa, asi que esta evidencia no se pudo evaluar. Lo que se arrastra de semanas anteriores sigue abierto para el corte.

## Semana 8 · S8 (revisión definitiva)

El proyecto ya se despliega en cuatro piezas (sitio estático, API en contenedor, base de datos gestionada y proveedor de identidad), con infraestructura como código, un health que además comprueba la base de datos, logs en una línea JSON por petición, métricas ligadas a sus escenarios, secretos fuera del código, la sección 7 de arc42 con una caja por pieza y la sección 2 con el límite de costo y la restricción de tarjeta; cada pieza de plataforma tiene su ADR con alternativas. El cálculo de costo parte del volumen del escenario y describe en qué punto se agota cada capa gratuita.

Lo prioritario: reparen el workflow de integración continua en la rama principal, que en el estado calificado termina en rojo (incluido el Quality Gate), y no editen ADR ya aceptados —si una decisión cambia, escriban uno nuevo y marquen el anterior como reemplazado—. Queda pendiente confirmar con el docente a qué integrante corresponde cada cuenta del historial. Las filas de URL desplegada y de health quedan pendientes de calificar porque la URL se entrega por Moodle.

## Semana 9 · S9 (revisión definitiva)

La nueva porción de Mis tareas completa la cadena exigida: decisión aceptada, código, prueba que detecta el defecto, medición y auditoría de erosión. Mantengan explícito que la medición es SQLite en proceso; todavía falta comprobar el costo de la consulta extra en MySQL. El cumplimiento de S9 no cierra los fallos actuales del pipeline ni el Quality Gate.

## Semana 10 · Segundo corte (avance preliminar)

Identifiquen la consigna operativa asignada y diseñen su experimento con línea base en el MVP desplegado. Recuperen CI y los chequeos de despliegue, repitan la medición relevante con MySQL y carga de red, y completen arc42 y propiedad de datos. La comparación local es un buen punto de partida, pero no sustituye el resultado operativo ni la sustentación.
