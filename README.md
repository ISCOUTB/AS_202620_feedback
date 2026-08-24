# Kit de revisión de repositorios · Arquitecturas de Software

Este es el material con el que se revisan los repositorios de los equipos, entrega por entrega.
Está a la vista a propósito: si vas a ser evaluado con una lista de comprobaciones, lo justo es que
puedas leerla antes de entregar. Hay una ficha por entrega calificada, y cada ficha dice **qué se
abre en el repositorio**, con qué comando se obtiene la evidencia y en qué matriz se registra el
resultado.

**Esto no sustituye al aula.** La consigna, la rúbrica, los pesos y las fechas viven en Moodle;
aquí está el procedimiento de revisión. Si alguna vez el kit y el aula dicen cosas distintas,
**manda el aula** y la ficha se corrige.

Este material vive en [`ISCOUTB/AS_202620_feedback`](https://github.com/ISCOUTB/AS_202620_feedback),
abierto para que puedas leerlo, citarlo y proponer cambios. Si tienes delante una copia descargada,
la versión que manda es la de ahí.

## Cómo está organizado el repositorio

```text
README.md                      esta guía: cómo se evalúa y dónde está cada cosa
CONTRATO.md                    lo que se exige en todas las entregas, con sus comandos
EQUIPOS.md                     equipos, integrantes y enlace a la evaluación de cada uno
fichas/                        una ficha por entrega calificada (18)
plantillas/planilla-equipo.md  la planilla en blanco, para saber qué se consolida
revisiones/2026-2/<repositorio>/  la evaluación de cada equipo, entrega por entrega
```

## Si eres estudiante

### Qué ocurre cuando entregas

1. Se localiza el repositorio del equipo y se clona **en el estado que se califica**: el commit
   etiquetado (`corte-1`, `corte-2`, `final`) o el commit vigente al cierre de la actividad.
2. Un agente automatizado recorre la ficha de esa entrega y la matriz transversal de
   [CONTRATO.md](CONTRATO.md), criterio por criterio.
3. El resultado es una matriz con un estado por criterio, la evidencia que lo respalda y la lista
   de lo que no se pudo verificar.
4. Esa revisión se publica aquí mismo, en la carpeta de tu equipo: mira
   [Evaluaciones publicadas](#evaluaciones-publicadas--2026-2). No hay que pedirla ni esperar a
   que alguien la reenvíe.

La revisión es **solo de lectura**. Nadie hace push, abre issues, comenta ni edita nada en el
repositorio del equipo: el clon se hace en un directorio temporal y se descarta. Y tu código no se
ejecuta fuera de un contenedor desechable y sin credenciales.

### Por qué es automático

Porque con más de veinte equipos y dieciocho entregas, la alternativa a revisar con un agente es
darte la retroalimentación tarde, cuando ya no te sirve para corregir nada. La idea del kit es que
sepas pronto qué falta y con qué evidencia, todavía a tiempo de arreglarlo antes de la siguiente
entrega.

La contrapartida, dicha con franqueza: un agente es literal. Ve lo que está escrito en el
repositorio y lo cita; no adivina intenciones ni concede el beneficio de la duda. Eso lo compensas
tú documentando, y lo compensan la conversación en clase y el criterio del profesor al calificar.

### Los tres estados, y por qué toda fila cita evidencia

| Estado | Qué significa |
|---|---|
| **Cumple** | Hay evidencia citada y satisface el criterio. |
| **No cumple** | Hay evidencia citada de que falta o no satisface. |
| **No verificado** | No se pudo comprobar. Va con el motivo y con qué haría falta para cerrarlo. |

Cada fila cita algo concreto —`ruta:línea`, hash de commit, URL del run de CI, código HTTP— y sin
evidencia citable el estado nunca es Cumple. Esto juega a tu favor de dos maneras: puedes ir al
sitio exacto que se miró y comprobarlo tú, y si crees que la lectura fue equivocada tienes algo
concreto que discutir en vez de una impresión general.

«No verificado» no es un castigo ni un aprobado disimulado: es lo que exige ejecutar el sistema,
credenciales del equipo o la sustentación. Suele ser, casi literalmente, la lista de preguntas que
te van a hacer.

### La nota final la pone el profesor

El agente **no califica**. Produce la matriz y, solo en las entregas con escala publicada (primer
corte, segundo corte, proyecto final y cierre), un **nivel sugerido** marcado de forma explícita
como propuesta. Ese nivel **no se publica**: va al registro del profesor, que lo revisa, lo
contrasta con la sustentación y con lo que conoce del equipo, y **fija la nota** en Moodle. Un
hallazgo del agente que no se sostiene se cae ahí.

En resumen: esto es un mecanismo de retroalimentación rápida, no un juez.

### Lo principal sigue pasando en clase

Nada de esto reemplaza hablar. La revisión automática llega rápido y por escrito, pero la que
cierra el ciclo es la conversación presencial: **en la semana de clase siempre tienes espacio para
revisar la entrega cara a cara**, preguntar por la fila que no entiendes, mostrar lo que el agente
no supo ver y discutir hacia dónde va el proyecto. Ese espacio no depende de que lo pidas ni de que
algo haya salido mal; está todas las semanas.

Y llegar con la matriz en la mano hace mejor esa conversación: ya sabes qué se miró y con qué
evidencia, así que el tiempo se va en lo que de verdad importa —el criterio arquitectónico detrás
del hallazgo— y no en reconstruir qué pasó. Las filas en No verificado son el mejor guion para
empezar, porque son precisamente las que no se pueden cerrar sin ti.

### Cómo usar el kit a tu favor

Autorrevisarte antes de entregar es la mejor manera de aprovecharlo:

1. Lee [CONTRATO.md](CONTRATO.md) una vez, al empezar. Es lo que se exige en **todas** las
   entregas: estructura mínima, convenciones de ADR, tabla de aspectos, registro de uso de IA,
   README que arranque con un solo comando, CI, cero secretos y contribución de todo el equipo.
2. Antes de cada entrega, abre la ficha de la semana y recorre su matriz preguntándote «¿qué
   evidencia citaría un revisor en esta fila?». Si no encuentras ninguna, esa fila ya está en No
   cumple.
3. Mira el apartado **«Qué no hacer aquí»** de la ficha: dice lo que *todavía* no se exige esa
   semana, y sirve para no gastar esfuerzo antes de tiempo.
4. Etiqueta a tiempo. Una etiqueta ausente o posterior al cierre afecta a la fila de versionado
   aunque el contenido esté impecable.

Y una garantía: lo que no esté en la ficha, en el contrato o en el aula **no se te exige**. Si el
kit pide algo que no aparece en ninguno de los tres, es un error del kit.

### Tus dudas y tus propuestas son bienvenidas

Con toda confianza y sin formalismos:

- **No entiendes un criterio, o no sabes cómo se evidencia.** Pregunta en clase o por el canal del
  curso; si la duda le sirve a varios, la ficha se aclara.
- **Crees que una fila se leyó mal.** Trae la evidencia concreta —ruta, línea, commit— y se revisa.
- **Ves una comprobación injusta, ambigua o mejorable**, o una ficha desactualizada respecto al
  aula. Dilo: el kit se mantiene a mano y esas correcciones mejoran el curso para todos.

También se agradecen las propuestas sobre el procedimiento mismo: que falta un criterio útil, que
otro sobra, que una comprobación se puede hacer mejor. Este material se escribió para ser
revisado, y la crítica bien argumentada se atiende.

**Por escrito, si te sirve más:** abre un *issue* en
[`ISCOUTB/AS_202620_feedback`](https://github.com/ISCOUTB/AS_202620_feedback/issues) con la duda o
la mejora propuesta, y cita la ficha y la fila de la que hablas. Es un canal cómodo para lo que
conviene que quede escrito —una redacción ambigua, un criterio que se puede afinar— y que además
aprovecha al resto del curso. Es un complemento de la clase, no un sustituto: lo que necesite
conversación se resuelve mejor cara a cara.

Lo que conviene no llevar ahí, porque el repositorio es público: notas y asuntos personales. La
evaluación de tu equipo está publicada y se puede discutir sin problema, pero lo que toque
calificación o situación personal se resuelve mejor en clase, por el canal del curso o por correo.

**Qué se publica de tu revisión, para que lo sepas de antemano.** Van los nombres del equipo y de
sus integrantes, los hallazgos y la evidencia que los sostiene —hashes, rutas, comandos—, porque
sin eso la retroalimentación no sería verificable. **No** van los correos con los que firmas tus
commits, ni ninguna nota o nivel sugerido: lo primero es dato de contacto y no hace falta para
evaluar arquitectura; lo segundo es del profesor.

## Índice de fichas

Una ficha por entrega calificada que se evalúa sobre el repositorio.

| Semana | Entrega | `idnumber` | Ficha |
|---:|---|---|---|
| 1 | Evidencia S1 · Equipo, problema y repositorio | `arqsw:evidencia-s1` | [ficha](fichas/semana-01-evidencia-s1.md) |
| 2 | Evidencia S2 · Escenarios de calidad y restricciones | `arqsw:evidencia-s2` | [ficha](fichas/semana-02-evidencia-s2.md) |
| 3 | Evidencia S3 · Estrategia de solución y primer ADR | `arqsw:evidencia-s3` | [ficha](fichas/semana-03-evidencia-s3.md) |
| 4 | Evidencia S4 · arc42, C4 y corte vertical | `arqsw:evidencia-s4` | [ficha](fichas/semana-04-evidencia-s4.md) |
| 5 | Primer corte · reto de línea base arquitectónica | `arqsw:corte1` | [ficha](fichas/semana-05-corte1.md) |
| 6 | Evidencia S6 · Contextos delimitados y propiedad de datos | `arqsw:evidencia-s6` | [ficha](fichas/semana-06-evidencia-s6.md) |
| 7 | Evidencia S7 · Contrato de API y prueba de contrato | `arqsw:evidencia-s7` | [ficha](fichas/semana-07-evidencia-s7.md) |
| 8 | Evidencia S8 · Despliegue reproducible, CI y observabilidad | `arqsw:evidencia-s8` | [ficha](fichas/semana-08-evidencia-s8.md) |
| 8 | Taller aplicado de despliegue | `arqsw:taller-docker` | [ficha](fichas/semana-08-taller-docker.md) |
| 9 | Evidencia S9 · Generación verificada y trazable | `arqsw:evidencia-s9` | [ficha](fichas/semana-09-evidencia-s9.md) |
| 10 | Segundo corte · reto aplicado sobre el MVP | `arqsw:corte2` | [ficha](fichas/semana-10-corte2.md) |
| 11 | Evidencia S11 · Fallos parciales y decisión de extracción | `arqsw:evidencia-s11` | [ficha](fichas/semana-11-evidencia-s11.md) |
| 12 | Evidencia S12 · Estrategia de datos y eventos | `arqsw:evidencia-s12` | [ficha](fichas/semana-12-evidencia-s12.md) |
| 12 | Taller aplicado · Mensajes y consistencia | `arqsw:taller-mensajes` | [ficha](fichas/semana-12-taller-mensajes.md) |
| 13 | Evidencia S13 · Modelado de amenazas y plan de mitigación | `arqsw:evidencia-s13` | [ficha](fichas/semana-13-evidencia-s13.md) |
| 14 | Evidencia S14 · Medición de atributos de calidad | `arqsw:evidencia-s14` | [ficha](fichas/semana-14-evidencia-s14.md) |
| 16 | Proyecto final · integración y desafío arquitectónico | `arqsw:final` | [ficha](fichas/semana-16-final.md) |
| 17 | Aplicación de cambios y cierre arquitectónico | `arqsw:cierre` | [ficha](fichas/semana-17-cierre.md) |

**Tres actividades calificadas no tienen ficha, y es a propósito:** `arqsw:quiz1` y `arqsw:quiz2`
son cuestionarios individuales que califica Moodle, y `arqsw:workshop-pares` califica la calidad
de la revisión que hace cada estudiante sobre otros equipos, no un repositorio. Si alguna vez
pasan a evaluarse sobre el repositorio, aquí faltará su ficha.

## Evaluaciones publicadas · 2026-2

Aquí está la revisión de cada equipo, tal como salió del barrido. Cada carpeta trae cuatro cosas:
la **retroalimentación** en lenguaje llano (qué está bien, qué falta, qué corregir antes del
corte), la **matriz** de cada entrega con el estado y la evidencia de cada criterio, y la
**planilla** del equipo, que acumula lo que se arrastra de una semana a otra y las preguntas
abiertas para la sustentación.

Empieza por la retroalimentación; la matriz es para cuando quieras ver en qué se basa cada cosa.
Lo que no está aquí es la nota: eso lo fija el profesor y se ve en Moodle.

| Equipo | Repositorio | Retroalimentación | Matriz S1 | Matriz S2 | Planilla |
|---|---|---|---|---|---|
| AudioShare | [`AS_202620_AudioShare`](https://github.com/ISCOUTB/AS_202620_AudioShare) | [ver](revisiones/2026-2/AS_202620_AudioShare/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_AudioShare/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_AudioShare/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_AudioShare/planilla.md) |
| Calificación automática | [`AS_202620_Sistema-de-calificacion-automatica`](https://github.com/ISCOUTB/AS_202620_Sistema-de-calificacion-automatica) | [ver](revisiones/2026-2/AS_202620_Sistema-de-calificacion-automatica/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_Sistema-de-calificacion-automatica/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_Sistema-de-calificacion-automatica/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_Sistema-de-calificacion-automatica/planilla.md) |
| CampusMarket | [`AS_202620_PROYECTO_CAMPUSMARKET`](https://github.com/ISCOUTB/AS_202620_PROYECTO_CAMPUSMARKET) | [ver](revisiones/2026-2/AS_202620_PROYECTO_CAMPUSMARKET/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_PROYECTO_CAMPUSMARKET/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_PROYECTO_CAMPUSMARKET/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_PROYECTO_CAMPUSMARKET/planilla.md) |
| Clubs UTB | [`AS_202620_Clubs_UTB`](https://github.com/ISCOUTB/AS_202620_Clubs_UTB) | [ver](revisiones/2026-2/AS_202620_Clubs_UTB/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_Clubs_UTB/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_Clubs_UTB/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_Clubs_UTB/planilla.md) |
| DinamikUTB | [`AS_202620_DinamikUTB`](https://github.com/ISCOUTB/AS_202620_DinamikUTB) | [ver](revisiones/2026-2/AS_202620_DinamikUTB/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_DinamikUTB/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_DinamikUTB/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_DinamikUTB/planilla.md) |
| Drift | [`AS_202620_Drift`](https://github.com/ISCOUTB/AS_202620_Drift) | [ver](revisiones/2026-2/AS_202620_Drift/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_Drift/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_Drift/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_Drift/planilla.md) |
| ElMapita | [`AS_202620_ElMapita`](https://github.com/ISCOUTB/AS_202620_ElMapita) | [ver](revisiones/2026-2/AS_202620_ElMapita/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_ElMapita/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_ElMapita/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_ElMapita/planilla.md) |
| EnAgenda | [`AS_202620_EnAgenda`](https://github.com/ISCOUTB/AS_202620_EnAgenda) | [ver](revisiones/2026-2/AS_202620_EnAgenda/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_EnAgenda/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_EnAgenda/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_EnAgenda/planilla.md) |
| GimnasioUTB | [`AS_202620_GimnasioUTB`](https://github.com/ISCOUTB/AS_202620_GimnasioUTB) | [ver](revisiones/2026-2/AS_202620_GimnasioUTB/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_GimnasioUTB/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_GimnasioUTB/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_GimnasioUTB/planilla.md) |
| InvenTrack | [`AS_202620_InvenTrack`](https://github.com/ISCOUTB/AS_202620_InvenTrack) | [ver](revisiones/2026-2/AS_202620_InvenTrack/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_InvenTrack/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_InvenTrack/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_InvenTrack/planilla.md) |
| LaPlacita | [`AS_202620_LaPlacita`](https://github.com/ISCOUTB/AS_202620_LaPlacita) | [ver](revisiones/2026-2/AS_202620_LaPlacita/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_LaPlacita/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_LaPlacita/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_LaPlacita/planilla.md) |
| LostVault | [`AS_202620_LostVault`](https://github.com/ISCOUTB/AS_202620_LostVault) | [ver](revisiones/2026-2/AS_202620_LostVault/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_LostVault/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_LostVault/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_LostVault/planilla.md) |
| mapsutb | [`AS_202620_mapsutb`](https://github.com/ISCOUTB/AS_202620_mapsutb) | [ver](revisiones/2026-2/AS_202620_mapsutb/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_mapsutb/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_mapsutb/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_mapsutb/planilla.md) |
| PideUtb | [`AS_202620_PideUtb`](https://github.com/ISCOUTB/AS_202620_PideUtb) | [ver](revisiones/2026-2/AS_202620_PideUtb/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_PideUtb/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_PideUtb/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_PideUtb/planilla.md) |
| Recobra | [`AS_202620_Recobra`](https://github.com/ISCOUTB/AS_202620_Recobra) | [ver](revisiones/2026-2/AS_202620_Recobra/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_Recobra/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_Recobra/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_Recobra/planilla.md) |
| ROUTB | [`AS_202620_ROUTB`](https://github.com/ISCOUTB/AS_202620_ROUTB) | [ver](revisiones/2026-2/AS_202620_ROUTB/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_ROUTB/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_ROUTB/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_ROUTB/planilla.md) |
| ShareU | [`AS_202620_ShareU`](https://github.com/ISCOUTB/AS_202620_ShareU) | [ver](revisiones/2026-2/AS_202620_ShareU/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_ShareU/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_ShareU/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_ShareU/planilla.md) |
| TAIA | [`AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant`](https://github.com/ISCOUTB/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant) | [ver](revisiones/2026-2/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_TAIA_-Task-Artificial-Intelligence-Assistant/planilla.md) |
| Tienda virtual UTB | [`AS_202620_TIENDA-VIRTUAL-UTB`](https://github.com/ISCOUTB/AS_202620_TIENDA-VIRTUAL-UTB) | [ver](revisiones/2026-2/AS_202620_TIENDA-VIRTUAL-UTB/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_TIENDA-VIRTUAL-UTB/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_TIENDA-VIRTUAL-UTB/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_TIENDA-VIRTUAL-UTB/planilla.md) |
| TRACTAR | [`AS_202620_TRACTAR`](https://github.com/ISCOUTB/AS_202620_TRACTAR) | [ver](revisiones/2026-2/AS_202620_TRACTAR/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_TRACTAR/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_TRACTAR/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_TRACTAR/planilla.md) |
| uniTeam | [`AS_202620_uniTeam`](https://github.com/ISCOUTB/AS_202620_uniTeam) | [ver](revisiones/2026-2/AS_202620_uniTeam/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_uniTeam/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_uniTeam/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_uniTeam/planilla.md) |
| Verifacts (Grupo X) | [`AS_202620_Verifacts`](https://github.com/ISCOUTB/AS_202620_Verifacts) | [ver](revisiones/2026-2/AS_202620_Verifacts/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_Verifacts/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_Verifacts/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_Verifacts/planilla.md) |
| XALD | [`AS_202620_XALD`](https://github.com/ISCOUTB/AS_202620_XALD) | [ver](revisiones/2026-2/AS_202620_XALD/feedback-s1-s2.md) | [ver](revisiones/2026-2/AS_202620_XALD/semana-01-evidencia-s1.md) | [ver](revisiones/2026-2/AS_202620_XALD/semana-02-evidencia-s2.md) | [ver](revisiones/2026-2/AS_202620_XALD/planilla.md) |

Si tu equipo no aparece, o si un archivo dice algo que no cuadra con tu repositorio, dilo en clase
o abre un *issue*: se corrige.

## Para el docente

**Este kit no se despliega a Moodle.** Es material de evaluación, igual que
`scripts/course-arqsw-sesiones.php`: la consigna y la rúbrica viven en el aula, y aquí está el
procedimiento de revisión, con la advertencia de que **manda el aula** si divergen.

**Qué se publica y qué no.** El remoto es `git@github.com:ISCOUTB/AS_202620_feedback.git`, y es
**público**: van las fichas, el contrato, el listado de equipos y las revisiones de cada equipo,
con nombres de equipo y de integrantes. Lo que el `.gitignore` deja fuera es el registro de
trabajo del docente:

| Se queda local | Por qué |
|---|---|
| `revisiones/2026-2/resumen-s1-s2.md` | tabla consolidada con la **nota sugerida de todos los equipos**: publicarla sería publicar un ranking |
| `revisiones/2026-2/cierres.env` | regla local de cierres |
| `revisiones/2026-2/_meta/` | volcados de la API, material de trabajo |

Dos cosas más que no salen de aquí aunque el archivo sí se publique: los **correos** de los
integrantes (se anotan como `correo omitido` en las revisiones) y la **nota sugerida** de cada
entrega, que en la planilla aparece como `no se publica` y vive solo en el resumen local. Antes de
añadir un archivo nuevo, la pregunta sigue siendo si puede leerlo cualquiera.

### Cómo se usa

1. Localiza el repositorio del equipo (apartado «Descubrimiento de repositorios»).
2. Abre la ficha de la entrega y pásasela al agente:
   «Revisa `AS_202620_X` contra `fichas/semana-08-evidencia-s8.md`».
3. El agente clona en el estado que se califica, recorre las instrucciones, rellena la matriz de
   la ficha más la **matriz transversal** de [CONTRATO.md](CONTRATO.md), y escribe el resultado en
   `revisiones/2026-2/<repositorio>/<tarea>.md`, que sí se publica.
4. Antes de empujar: sin correos y sin nota sugerida en los archivos publicados, y la nota al
   resumen local. Añade el equipo al índice de [Evaluaciones publicadas](#evaluaciones-publicadas--2026-2)
   si es su primera revisión.

Lee [CONTRATO.md](CONTRATO.md) antes de la primera revisión: contiene lo que se exige en todas
las entregas y los comandos base, y las fichas lo dan por leído.

Más [EQUIPOS.md](EQUIPOS.md), con los equipos, sus integrantes, el estado de cada repositorio y el
enlace a su evaluación, y [la planilla en blanco](plantillas/planilla-equipo.md), que es la hoja
consolidada de un equipo a lo largo del semestre.

### Descubrimiento de repositorios

En esta máquina hay `git`, `curl` y `python`, y **no hay `gh`**: ningún comando del kit lo usa.

```bash
# Repositorios públicos del periodo en la organización
curl -s "https://api.github.com/orgs/ISCOUTB/repos?per_page=100&type=public&page=1" \
  | python -c "import json,sys;[print(r['name'],r['clone_url'],r['pushed_at']) for r in json.load(sys.stdin) if r['name'].startswith('AS_202620_')]"
```

La API sin token permite 60 peticiones por hora. Con más de veinte equipos y varias consultas por
equipo (repositorio, contribuidores, runs, PR) ese límite se agota en un barrido completo: para
revisar el curso entero de una sentada, exporta un token en `GITHUB_TOKEN` y añade
`-H "Authorization: Bearer $GITHUB_TOKEN"`. Cuando se agota responde con 403. Pagina mientras la
respuesta traiga 100 elementos: la organización tiene bastantes más repositorios que los del curso.

El listado de equipos, con sus integrantes y el estado de cada repositorio, está en
[EQUIPOS.md](EQUIPOS.md). Un equipo que no aparece en la organización puede tener el repositorio
privado, fuera de ella o con otro nombre. Eso es hallazgo de la matriz transversal, no motivo
para saltarse la revisión: se comprueba contra el enlace que el equipo entregó en Moodle y se
registra la discrepancia.

```bash
DIR="$(mktemp -d)/AS_202620_X"
git clone --filter=blob:none "https://github.com/ISCOUTB/AS_202620_X.git" "$DIR"
git -C "$DIR" checkout corte-1     # o el hash del último commit anterior al cierre
```

### Reglas del agente

- **Solo lectura sobre los repositorios de los estudiantes.** Nada de push, fork, issues, PR,
  comentarios ni ediciones, ni siquiera para «dejar constancia». El clon va a un directorio
  temporal fuera de este repositorio.
- **No ejecutar código del estudiante** fuera de un contenedor desechable y sin credenciales. El
  criterio «arranca con un solo comando» se comprueba en contenedor o se marca No verificado y se
  resuelve en la sustentación. Un repositorio público de terceros no se ejecuta en el equipo del
  docente por comodidad.
- **No calificar en Moodle.** El agente produce matriz y, donde hay escala publicada, un nivel
  sugerido. La nota la aplica el docente.
- **Toda fila cita evidencia.** `ruta:línea`, hash, URL del run, código HTTP. Sin evidencia
  citable el estado es No verificado.
- **No inventar requisitos.** Si algo no está en la ficha, en el contrato ni en el aula, no se
  exige. La ficha resume la consigna; si divergen, manda el aula.
- **Las revisiones van a `revisiones/<periodo>/<repositorio>/<tarea>.md`** y se publican. Escribirlas
  pensando en que las lee el equipo: sin correos, sin nota sugerida y con evidencia citable en cada
  fila, que es lo que hace discutible un hallazgo.

### Qué produce una revisión

1. Encabezado con equipo, repositorio, estado revisado (etiqueta o hash con su fecha) y qué
   comandos se ejecutaron.
2. La matriz de la ficha, rellena.
3. La matriz transversal del contrato, rellena.
4. En `corte1`, `corte2`, `final` y `cierre`, el **nivel sugerido** por criterio con su suma sobre
   5,0, marcado como propuesta al docente. Eso va al registro local, no al archivo publicado.
5. Lo que quedó en No verificado, con qué haría falta para cerrarlo.

### Mantenimiento

Las fichas están escritas a mano y no se generan, así que **no se actualizan solas**. Si cambia
una consigna, una rúbrica o el contrato del repositorio, hay que tocar la ficha correspondiente.
Las fuentes son, por este orden: la actividad en el aula, `docs/curso-arqsw-guia.md` (volcado del
curso desplegado, `make guia-arqsw`), `scripts/course-arqsw.php` (consignas y `$EVIDENCIAS`) y
`scripts/course-arqsw-contenido.php` (recordatorio de documentación de cada semana y rúbricas).

Las dudas y propuestas de mejora que llegan de los estudiantes entran por aquí: son la vía más
barata de detectar una ficha desalineada con el aula, y conviene resolverlas en la ficha y no solo
en la conversación.

Dos reglas de forma que evitan que el kit envejezca mal: **no se escriben pesos ni fechas**, que
ya viven en el aula y se desincronizan en cuanto cambian; y las comprobaciones que se repiten en
todas las entregas están en el contrato, no copiadas en cada ficha.
