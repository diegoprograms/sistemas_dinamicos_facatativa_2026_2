# Bitácora de ideas y notas

Este archivo reúne ideas, preguntas, observaciones y posibles mejoras del
proyecto. Las entradas son propuestas en exploración, no decisiones aprobadas
ni tareas comprometidas. Cuando una idea se convierta en una decisión,
registrarla en [decisions.md](decisions.md) y enlazarla desde su nota original.

## Cómo utilizarla

- Agregar las notas más recientes al principio, debajo de «Entradas».
- Indicar fecha, tema y tipo: idea, pregunta, observación o posible tarea.
- Usar los estados: pendiente, en revisión, resuelta o descartada.
- Conservar el contexto y anotar la respuesta o conclusión cuando exista.
- Vincular archivos o datos relacionados cuando ayuden a entender la nota.

## Entradas

### 2026-10-22 — 2. Acumulación de alimentos como variable central del sistema

- **Tipo:** idea.
- **Estado:** pendiente.
- **Nota:** considerar la acumulación o cantidad de alimentos disponibles,
  representada por `A(t)`, como la variable primordial del análisis. Estudiar
  su variación en el tiempo, `dA/dt`, a partir de la interacción de los demás
  subsistemas: consumo, producción, clima, disponibilidad de agua y otros
  procesos que se identifiquen. Explorar ecuaciones diferenciales para los
  subsistemas que tengan dinámica propia y conectar sus efectos sobre `A(t)`.
- **Analogía propuesta:** pensar los subsistemas como influencias o «fuerzas»,
  siguiendo la intuición de las leyes de Newton. Como ejemplo, en la caída
  de un objeto con resistencia del aire, la ley de resistencia y sus parámetros
  dependen de características del objeto y del fluido. De manera análoga,
  las relaciones del sistema alimentario tendrían parámetros dependientes
  del cultivo y de las condiciones ambientales y productivas.
- **Precisiones para desarrollar la idea:** la analogía mecánica es una guía
  conceptual, no una equivalencia física ya demostrada. `A(t)` sería un nivel
  o existencia, y `dA/dt` su tasa de cambio. Su ecuación debe expresar un
  balance de entradas y salidas con unidades compatibles. El clima puede
  afectar la producción y las pérdidas sin ser una entrada directa de
  alimentos. No todas las relaciones necesitan una ecuación diferencial:
  algunas podrían ser algebraicas, parámetros o entradas externas.
- **Posible siguiente paso:** definir el territorio, los alimentos incluidos,
  la unidad y el periodo de análisis; distinguir existencias físicas de
  oferta por periodo. Como hipótesis inicial, evaluar por producto un balance
  del tipo `dA/dt = producción + entradas externas − consumo − pérdidas −
  salidas externas`, con cada término expresado en cantidad de alimento por
  unidad de tiempo y sin contar dos veces el mismo flujo. Definir después
  las ecuaciones y parámetros que conectan esos flujos con los subsistemas.
- **Contexto o archivos relacionados:** [variables.md](variables.md),
  [equations.md](equations.md), [article.md](article.md) y la idea 1 de esta
  bitácora sobre comparación entre modelos y datos experimentales.
- **Respuesta o conclusión:** pendiente de formulación y contraste con datos;
  esta nota no modifica todavía las ecuaciones ni el código del modelo.

### 2026-10-22 — 1. Comparación entre modelos teóricos y datos experimentales

- **Tipo:** idea.
- **Estado:** pendiente.
- **Nota:** comparar modelo y experimento, como se hace al estudiar ecuaciones
  diferenciales. Reunir los datos reales de los distintos componentes del
  sistema y contrastarlos con varios modelos teóricos candidatos. La IA puede
  apoyar la búsqueda de esos modelos y sus fuentes. La comparación deberá
  permitir explorar el mejor y el peor de los casos.
- **Posible siguiente paso:** identificar los datos observados disponibles,
  buscar modelos candidatos y definir cómo ajustar sus parámetros y comparar
  sus predicciones con las mediciones. Precisar si «mejor y peor caso» se
  refiere al ajuste de los modelos, a escenarios favorables y desfavorables
  para los cultivos, o a ambas comparaciones.
- **Contexto o archivos relacionados:** [variables.md](variables.md),
  [equations.md](equations.md) y [article.md](article.md).
- **Respuesta o conclusión:** pendiente; todavía no se han seleccionado modelos
  ni definido los criterios de comparación para esta propuesta.

### 2026-10-22 — Inicio de la bitácora

- **Tipo:** observación.
- **Estado:** resuelta.
- **Nota:** se crea este espacio para conservar las ideas que surjan durante
  el desarrollo de la investigación y la aplicación.
- **Conclusión:** las notas libres se registran aquí; las decisiones acordadas
  se documentan en `decisions.md`.

## Plantilla para nuevas entradas

Copiar este bloque en «Entradas» y completar solo lo necesario:

```markdown
### AAAA-MM-DD — Tema de la nota

- **Tipo:** idea / pregunta / observación / posible tarea.
- **Estado:** pendiente.
- **Nota:** ¿Qué se te ocurrió o qué observaste?
- **Contexto o archivos relacionados:** opcional.
- **Posible siguiente paso:** opcional; todavía no es un compromiso.
- **Respuesta o conclusión:** completar cuando se resuelva.
```
