# Datos del proyecto

Actualizado el 1 de octubre de 2026.

Actualmente el equipo dispone únicamente de información de fenología, pendiente
de revisar e incorporar al almacenamiento del proyecto. Las siguientes secciones
plantean los datos que se podrían recolectar; no implican que ya estén disponibles.
El inventario general y el detalle de campos se mantienen en
[variables.md](../docs/variables.md).

## 1. Datos que registrarían los restaurantes

Propongo un registro semanal, por producto, para facilitar la participación:

| Dato | Para qué sirve |
|---|---|
| Restaurante y fechas del periodo | Relacionar los registros y observar cambios temporales. |
| Producto y presentación: papa entera, arveja desgranada, etc. | Comparar cantidades equivalentes y asociarlas con cultivos. |
| Cantidad comprada y unidad | Medir el abastecimiento del establecimiento. |
| Cantidad utilizada en cocina, si la conocen | Aproximar la demanda efectiva de ingredientes. |
| Existencias al inicio y al final, si no conocen lo utilizado | Estimar el uso mediante un balance de inventario. |
| Producto descartado antes de prepararlo, en kg | Separar pérdidas de ingredientes utilizados. |
| Procedencia: municipio o «desconocida» | Distinguir abastecimiento local y externo. |
| Cantidad adicional que necesitaban y no consiguieron | Detectar demanda que las compras no reflejan. |
| Número de almuerzos servidos | Interpretar las cantidades según la actividad del restaurante. |
| Cantidad pesada, tomada de factura o estimada | Registrar la calidad del dato. |

**No haría obligatorios todos los campos desde el comienzo.** El mínimo sería
identificación del restaurante, periodo, producto, presentación, cantidad
comprada, unidad, procedencia y forma de obtener la cantidad. Después
incorporaríamos uso e inventarios con los establecimientos que puedan reportarlos.

Las compras no equivalen automáticamente al consumo: puede haber almacenamiento
y desperdicio. Los conteos de personas y residuos contemplados en el prototipo
serían información complementaria cuando se recolecten.

## 2. Datos que necesitamos de productores o fincas

Estos se recogerían por lote y ciclo de cultivo:

| Dato | Para qué sirve |
|---|---|
| Identificación del lote y ciclo, ubicación, cultivo y variedad | Identificar las condiciones de producción y vincular las observaciones. |
| Área sembrada | Comparar producción y agua por hectárea. |
| Fecha de siembra o trasplante y cosecha prevista y real | Relacionar el ciclo con temporadas y demanda. |
| Producción cosechada y parte comercializable, en kg | Estimar rendimiento y oferta aprovechable. |
| Fuente de agua y disponibilidad por temporada | Establecer la restricción hídrica. |
| Método de riego | Caracterizar cómo se aplica el agua. |
| Fecha y volumen de cada riego | Cuantificar el agua aplicada. |
| Caudal y duración, cuando no se mida el volumen | Estimar el volumen con un método documentado. |
| Características del suelo y problemas del ciclo | Interpretar almacenamiento de agua y pérdidas de rendimiento. |

### Registro fenológico asociado al cultivo

Este es el foco actual de la investigación. Se conservarán varias observaciones
por ciclo para describir el desarrollo del cultivo a través del tiempo. Los
productores o estudiantes registrarían las observaciones con un protocolo común,
bajo coordinación del equipo investigador.

| Dato | Para qué sirve |
|---|---|
| Cultivo, variedad, lote y ciclo cuando se conozcan | Asociar cada observación con el cultivo estudiado. |
| Fecha de observación | Ordenar temporalmente el desarrollo. |
| Etapa fenológica y escala o criterio de identificación | Interpretar y comparar las etapas según el cultivo. |
| Fecha de siembra o trasplante, si está disponible | Calcular los días transcurridos desde un evento definido. |
| Inicio y final de etapa, si se conocen | Estimar su duración e identificar transiciones. |
| Duración de etapa reportada o calculada, en días | Comparar ciclos, variedades y referencias, indicando el método. |
| Proporción de plantas en cada etapa y número observado, cuando se midan | Describir la variabilidad dentro del lote. |
| Signos de estrés, observaciones y fotografías opcionales | Documentar condiciones que acompañan al desarrollo, sin atribuir causas no comprobadas. |
| Fuente y condición de observado, estimado o bibliográfico | Evaluar la calidad del dato y conservar su procedencia. |

El esquema se adaptará a la información fenológica disponible. Si una fuente
solo contiene duraciones de referencia, no se inventarán fechas, lotes o ciclos.
La primera detección de una etapa en visitas espaciadas no establece por sí sola
su inicio exacto. La fenología observada, la bibliográfica y la predicha por un
modelo se conservarán diferenciadas.

## 3. Datos que reuniría el equipo investigador

De estaciones, fuentes institucionales, bibliografía y mediciones:

- Precipitación y temperaturas diarias.
- Evapotranspiración de referencia, o información para calcularla.
- Propiedades del suelo relacionadas con retención de agua y profundidad.
- Etapas de cada cultivo y variedad, criterios para reconocerlas y duraciones de referencia.
- Temperatura base y requerimientos térmicos por etapa, cuando exista un modelo aplicable.
- Necesidades hídricas, coeficientes de cultivo por etapa y respuesta al déficit.
- Series de disponibilidad de agua para uso agrícola.

Cada parámetro conservará unidad, fuente, ámbito de aplicación e incertidumbre.
Los valores bibliográficos deberán contrastarse con las observaciones locales
cuando sea posible; no se tratarán como mediciones realizadas en Facatativá.

Debemos distinguir **agua de lluvia, agua requerida por el cultivo y agua
aplicada mediante riego**. La necesidad de riego depende de cuánto aportan la
lluvia efectiva y el agua almacenada en el suelo.
[FAO: necesidades de riego](https://www.fao.org/aquastat/en/data-analysis/irrig-water-use/irrig-water-requirement/)

Con esos datos podríamos comparar, para cada cultivo y fecha de siembra:

- Duración y calendario de las etapas fenológicas y momento de cosecha.
- Agua de riego requerida, considerando las etapas del cultivo.
- Producción comercializable esperada.
- Producción por metro cúbico de riego.
- Proporción de la demanda que se podría cubrir.
- Comportamiento ante una temporada seca.

La fenología por sí sola no permite cuantificar ahorro de agua ni cobertura
alimentaria: esas comparaciones requieren los demás datos y un modelo validado.

## Orden de trabajo y organización

**Primero revisaremos y organizaremos la información fenológica disponible.**
Después, para la recolección en restaurantes, adaptaríamos el Excel y el formulario
web a un mismo registro semanal de abastecimiento por producto. En paralelo con
esa etapa prepararíamos la ficha de productores y su seguimiento fenológico.
La información de restaurantes representará inicialmente a los establecimientos
participantes; necesitaremos un diseño de muestreo para extrapolarla a Facatativá.

Los archivos se organizarán en [raw](raw/raw.md) para originales,
[processed](processed/processed.md) para datos depurados y
[examples](examples/examples.md) para ejemplos ficticios.

Actualmente [frontend](../frontend/frontend.md) conserva formularios y Excel
solo durante la sesión. No hay guardado implementado en esta carpeta ni una
conexión de persistencia con [backend](../backend/backend.md). El análisis desde
[notebooks](../notebooks/notebooks.md) también está previsto, no implementado.
