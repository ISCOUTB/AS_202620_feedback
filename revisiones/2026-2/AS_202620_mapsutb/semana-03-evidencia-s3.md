# Evidencia S3 · mapsutb

## Datos

| Campo | Valor |
|---|---|
| Repositorio | `https://github.com/ISCOUTB/AS_202620_mapsutb` |
| Estado revisado | `ed55eda5c24e3d23edcc74df3d3a3a6bf833026d` · 2026-08-23T21:44:05-05:00 («Entrega S3») |
| Cierre | 2026-08-24T05:00:00Z |
| Fecha/hora de revisión | 2026-08-24 (posterior al cierre) |
| Comandos | clon efímero con `--filter=blob:none --no-checkout`; lecturas con `git -C "$DIR" show "$HASH:…"`; sin ejecutar código del estudiante. Sin llamadas a la API (no hay `.github/workflows/`). |
| Nota de actualización | **Revisión actualizada tras el cierre: el equipo empujó después de la primera revisión; hash calificado definitivo.** La revisión previa (22:00 COT del 23-ago) encontró el repo sin actividad de S3; el equipo subió la entrega S3 completa a las 21:44 COT, dentro del cierre. Sin commits posteriores al cierre. |

## Matriz de la ficha

| Criterio | Evidencia técnica | Estado | Observaciones |
|---|---|---|---|
| arc42 sección 4 con estrategia y tácticas ligadas a los escenarios | `docs/Estrategias_Solucion.md` (§ «Enfoque de solución por objetivo de calidad») | Cumple | Tabla que liga cada objetivo de calidad y escenario (A-01, escenarios 2, 3, 5) a un patrón concreto (Strategy, Adapter+Observer, Repository). Desviación de ubicación: `docs/arc42.md` (41 líneas) no tiene sección 4; la estrategia vive en un archivo separado. El artefacto se evalúa donde está (CONTRATO §2). |
| Matriz comparativa de los tres estilos contra el árbol de utilidad | ausente en todo el repo (grep de «capas», «hexagonal», «monolito» sin coincidencias) | No cumple | No existe la comparación de los tres estilos contra el árbol de utilidad. El ADR declara explícitamente «no compara alternativas arquitecturales; compara patrones de diseño», y `Estrategias_Solucion.md` remite a un «corte anterior de este documento» que no está en el repositorio. La ficha S3 pide esa matriz: falta. |
| `docs/adr/0001-*.md` con el nombre de la convención | `docs/adr/0001-patrones-de-diseno.md` | Cumple | kebab-case correcto. Nota: decide patrones de diseño internos del monolito, no el estilo arquitectónico; el estilo se declara decidido sin ADR que lo sustente con alternativas. |
| ADR con contexto, opciones evaluadas, decisión y consecuencias | `docs/adr/0001-patrones-de-diseno.md` | Cumple | Contexto, Decisión (tabla problema→patrón), Alternativas consideradas por problema, Consecuencias positivas/negativas. Redacción cuidada. |
| Alternativas descartadas con su motivo | `docs/adr/0001-patrones-de-diseno.md` («Alternativa descartada» por problema) | Cumple | Cada patrón tiene alternativa descartada con su consecuencia (p. ej. invocar ARCore directo, cargar el mapa en cada pantalla, polling con `Timer`). |
| ADR alcanzable desde `docs/aspectos.md` y desde el escenario que lo motiva | `docs/aspectos.md` (dice «Sin ADR aún»); `docs/escenarios_calidad.md` sin enlaces al ADR | No cumple | `aspectos.md` está desactualizado: la fila A-01 declara «aún no se ha decidido la arquitectura general» y la columna ADR dice «Sin ADR aún», cuando el ADR 0001 existe y lo referencia. `escenarios_calidad.md` no enlaza el ADR (y su enlace al árbol `./02_arbol_utilidad.md` está roto). |
| Arranque con un solo comando documentado en el README | `README.md` («Arranque con un solo comando») + `scripts/start.sh` | Cumple | `./scripts/start.sh` hace `flutter pub get`, `flutter test` y `flutter run`; el README documenta también la variante solo-pruebas. No ejecutado (regla del kit). |
| Prueba automatizada en verde | `test/app_smoke_test.dart` (`MapsUtbApp arranca y muestra el Scaffold raíz`) | No verificado | La prueba existe y es coherente con el esqueleto, pero no hay `.github/workflows/` ni run o captura aportada; el «en verde» del README es una afirmación, no evidencia verificable. |
| Estructura de paquetes correspondiente al estilo del ADR | `lib/` contiene solo `main.dart` | No cumple | El ADR y el README declaran `lib/{adapters,repositories,strategies,services,features/{tour,mapas_ruteo,realidad_aumentada,zonas},core}` y el README afirma que cada carpeta tiene `.gitkeep`, pero esas carpetas (ni sus `.gitkeep`) no existen en el repositorio al hash calificado. La estructura solo está en la documentación. |

## Matriz transversal (CONTRATO)

| Criterio | Estado | Observaciones |
|---|---|---|
| Repositorio en la organización, con el nombre de la convención y público | Cumple | Clonado sin autenticación; `ISCOUTB/AS_202620_mapsutb`. |
| Estructura mínima presente | No cumple | Desviaciones: `docs/arc42.md` como archivo único (fuera de `docs/arc42/`) y `docs/c4_contexto.md` fuera de `docs/c4/`. `docs/adr/` sí existe ya. Los artefactos se evalúan donde están. |
| Estado calificado identificable | Cumple | `ed55eda` · 2026-08-23T21:44:05-05:00 ≤ cierre; sin etiqueta nueva. Hallazgo: la etiqueta `corte-1` sigue apuntando al commit de S1 (`7e56ad3`, 2026-08-09) — se moverá al commit real del corte. |
| Nombres de ADR según la convención | Cumple | `0001-patrones-de-diseno.md` pasa el filtro. |
| ADR aceptados no reescritos | Cumple | Un solo commit sobre el ADR (`4005a67`). El texto menciona una «versión anterior de este ADR» que no está en el historial (nunca se versionó). |
| `docs/ia.md` al día para la semana | No cumple | El archivo se tocó en S3 (`a6e51bc`) pero el cambio es solo de saltos de línea: las dos entradas del registro siguen siendo de 07-ago. Sin entradas del trabajo S3 (ADR, estrategia, esqueleto) ni rechazos con motivo de esa semana. |
| Sin credenciales en el repositorio ni en el historial | Cumple | `git grep` §9 sin coincidencias; sin `.env` versionado. |
| Contribución de todos los integrantes | No cumple | `git shortlog -sne` → 3 identidades (CarlosManrique-1397 6, nerlis-otero 4, charlygz21 3); Isabel Sofia Paez Matallana sigue sin aparición. Toda la S3 la empujó una sola cuenta. |

## Recuento

**5 de 9** criterios de la ficha cumplidos (3 no cumplidos, 1 no verificado).

## No verificado / pendientes

- Pruebas en verde: sin pipeline ni run aportado; el comando declarado (`./scripts/start.sh` o `flutter pub get && flutter test`) no se ejecutó por regla del kit.

## Hallazgos para la planilla

- Sin commits tardíos: la entrega entró a las 21:44 COT del 23-ago, dentro del cierre (bien).
- Falta la matriz comparativa de los tres estilos contra el árbol de utilidad: el ADR la declina y el «corte anterior» referenciado no existe en el repo.
- `docs/aspectos.md` desactualizado (dice «Sin ADR aún») y sin enlace al ADR 0001; `escenarios_calidad.md` tampoco lo enlaza y tiene un enlace roto al árbol (`02_arbol_utilidad.md`).
- La estructura de paquetes del ADR no está materializada: `lib/` solo tiene `main.dart`; faltan las carpetas `adapters/`, `repositories/`, `strategies/`, `services/`, `features/` (o sus `.gitkeep`).
- Etiqueta `corte-1` sobre el commit de S1; moverla al commit del corte real.
- `docs/ia.md` sin entradas del trabajo S3 (solo cambio de saltos de línea).
- Isabel Sofia Paez Matallana sin aparición en el historial; toda la S3 la empujó una sola cuenta.
- Desviaciones de estructura: `docs/arc42.md` único y `docs/c4_contexto.md` fuera de `docs/c4/`.

## Estado del contrato del repositorio

Ver la matriz transversal arriba.
