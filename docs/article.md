# Modelamiento dinámico de la relación entre disponibilidad hídrica, producción agrícola y demanda alimentaria en Facatativá, Cundinamarca

## 1. Introducción

La seguridad alimentaria de un territorio depende de su capacidad para garantizar una disponibilidad suficiente, estable y accesible de alimentos. Esta capacidad no está determinada exclusivamente por el volumen de producción agrícola, sino también por las condiciones ambientales, los recursos naturales disponibles, la infraestructura de abastecimiento, las decisiones de los productores y los patrones de consumo de la población (Referencia sobre seguridad alimentaria).

En los sistemas agrícolas, el agua constituye uno de los principales factores que condicionan el establecimiento, crecimiento y rendimiento de los cultivos. Su disponibilidad varía en función de la precipitación, la temperatura, la humedad, la radiación solar, la evapotranspiración, las características del suelo y la capacidad de almacenamiento natural o artificial (Referencia sobre relaciones entre clima, agua y producción agrícola). Estas condiciones adquieren especial importancia durante las temporadas secas, cuando disminuyen las entradas de agua y aumenta la competencia entre sus diferentes usos.

Facatativá se encuentra en la región Sabana Occidente de Cundinamarca y presenta actividades agrícolas asociadas a sistemas productivos familiares, comerciales y territoriales (Referencia sobre caracterización agrícola de Facatativá). Simultáneamente, el municipio ha experimentado procesos de crecimiento urbano, transformación del uso del suelo y aumento de la demanda de recursos naturales (Referencia sobre crecimiento urbano y uso del suelo en Facatativá). La coexistencia de actividades agrícolas, residenciales, industriales y comerciales puede generar presiones sobre las fuentes hídricas superficiales y subterráneas (Referencia sobre usos y demanda del agua en Facatativá).

La disponibilidad de agua para la agricultura no depende solamente de la precipitación. También intervienen el caudal de las fuentes, la humedad almacenada en el suelo, las captaciones, los sistemas de riego, la infraestructura de almacenamiento, las pérdidas en la conducción y las reglas utilizadas para distribuir el recurso entre usuarios (Referencia sobre gestión integral del recurso hídrico). Por esta razón, aunque el clima condiciona la entrada natural de agua, el recurso hídrico se considera un subsistema particular en el cual interactúan procesos naturales y decisiones humanas.

Los cultivos presentan diferencias en sus requerimientos hídricos, duración del ciclo productivo, sensibilidad al déficit de agua y rendimiento por unidad de superficie (Referencia sobre necesidades hídricas de los cultivos). Además, la necesidad de agua cambia entre sus etapas de establecimiento, desarrollo, crecimiento máximo y maduración (Referencia sobre coeficientes de cultivo y etapas fenológicas). Una selección de cultivos que no considere las condiciones de cada temporada podría reducir la eficiencia hídrica y limitar la disponibilidad futura de determinados alimentos.

Sin embargo, clasificar los cultivos únicamente según su consumo total de agua puede producir interpretaciones incompletas. Un cultivo con una necesidad hídrica relativamente alta puede presentar un rendimiento elevado por unidad de agua, mientras que otro de menor requerimiento puede producir pocos alimentos o carecer de suficiente demanda territorial (Referencia sobre productividad hídrica agrícola). La planificación debe considerar simultáneamente el agua utilizada, la producción obtenida, la duración del cultivo, su sensibilidad a la sequía, su importancia alimentaria y la demanda observada.

Desde esta perspectiva, el consumo constituye el punto de partida para orientar la producción. La información obtenida en restaurantes, plazas de mercado y otros establecimientos alimentarios puede utilizarse para estimar qué productos se consumen, en qué cantidades y con qué variaciones temporales (Referencia sobre consumo alimentario y estimación de demanda). Esta demanda puede contrastarse con la producción local, la oferta procedente de otros territorios y el recurso hídrico requerido para producir los alimentos seleccionados.

El problema no consiste solamente en determinar cuánto alimento puede producirse con el agua disponible, sino en establecer si esa producción responde a las necesidades de consumo del territorio. Esto requiere integrar dos rutas complementarias:


\text{Consumo observado}\rightarrow\text{demanda estimada}\rightarrow
\text{producción requerida}\rightarrow\text{agua requerida}


\[
\text{Clima}\rightarrow\text{disponibilidad hídrica}\rightarrow
\text{producción real}\rightarrow\text{oferta}\rightarrow
\text{consumo atendido}
\]

La comparación permite identificar una brecha alimentaria y una brecha hídrica. La primera expresa la diferencia entre el consumo requerido y la oferta disponible; la segunda compara el agua necesaria para alcanzar la producción esperada con el agua efectivamente disponible.

La dinámica de sistemas permite representar acumulaciones, retrasos temporales, relaciones no lineales y bucles de realimentación entre consumo, demanda, planificación productiva, uso del agua, producción y oferta (Referencia sobre fundamentos de dinámica de sistemas). El modelo propuesto funcionará como un laboratorio virtual para comparar cultivos, épocas de siembra, condiciones climáticas y estrategias de manejo del agua antes de intervenir sobre el sistema real (Referencia sobre simuladores de gestión y aprendizaje mediante modelos).

## 1.1. Planteamiento del problema

Durante las temporadas secas, la reducción de la precipitación y el aumento potencial de la evapotranspiración pueden disminuir el agua disponible para los cultivos de Facatativá (Referencia sobre comportamiento climático estacional de Facatativá). Cuando esta reducción coincide con cultivos sensibles al déficit hídrico pueden presentarse disminuciones en el rendimiento, pérdidas económicas y reducciones de la oferta alimentaria (Referencia sobre estrés hídrico en cultivos de clima frío).

Actualmente, dentro del proyecto no se dispone de información integrada que permita establecer qué proporción del agua se utiliza en cada cultivo, qué productos generan mayor producción por unidad de agua y en qué medida esa producción responde a los alimentos consumidos. La información sobre clima, recurso hídrico, producción, comercialización y consumo se encuentra distribuida entre diferentes fuentes y actores (Referencia sobre información agrícola o territorial).

La posibilidad de que una proporción importante del agua agrícola se esté asignando a cultivos con altos requerimientos hídricos se plantea inicialmente como una hipótesis y no como una conclusión. Para evaluarla será necesario identificar los cultivos presentes, sus áreas sembradas, las fuentes de abastecimiento, los volúmenes de riego, los rendimientos obtenidos y su participación en el consumo territorial.

El problema central se formula así:

> Se desconoce si la selección y distribución temporal de los cultivos en Facatativá permite utilizar eficientemente el recurso hídrico disponible durante temporadas secas y responder, al mismo tiempo, a la demanda alimentaria observada.

El sistema también presenta retrasos. La demanda observada no se transforma inmediatamente en producción porque entre la decisión de sembrar y la cosecha existe un periodo de crecimiento. De manera similar, los efectos de una temporada seca pueden manifestarse posteriormente en el rendimiento, la oferta y los precios (Referencia sobre retrasos en sistemas agrícolas).

## 1.2. Pregunta de investigación

> ¿Qué combinación y programación temporal de cultivos permite satisfacer la mayor proporción posible de la demanda alimentaria observada, considerando la disponibilidad hídrica y las condiciones climáticas durante temporadas secas en Facatativá?

## 1.3. Objetivo general

Desarrollar un modelo de dinámica de sistemas que integre el consumo alimentario, la disponibilidad hídrica, las condiciones climáticas, la producción agrícola y la oferta, con el fin de evaluar alternativas de selección y programación de cultivos durante temporadas secas en Facatativá, Cundinamarca.

## 1.4. Objetivos específicos

1. Caracterizar el consumo observado de productos agrícolas en los establecimientos alimentarios seleccionados.
2. Estimar la producción requerida para responder a la demanda identificada, considerando las pérdidas del sistema de abastecimiento.
3. Caracterizar las condiciones climáticas y la disponibilidad temporal del recurso hídrico relacionado con la producción agrícola.
4. Determinar los requerimientos hídricos, ciclos, rendimientos y sensibilidad al déficit de agua de los cultivos seleccionados.
5. Formular una hipótesis dinámica que represente las relaciones entre consumo, demanda, disponibilidad hídrica, producción y oferta.
6. Construir y validar un modelo de simulación que reproduzca el comportamiento de las principales variables.
7. Comparar escenarios climáticos y alternativas de selección, programación y manejo hídrico de los cultivos.
8. Identificar estrategias que mejoren conjuntamente la cobertura alimentaria y la productividad del recurso hídrico.

## 1.5. Hipótesis inicial

Una selección y programación de cultivos basada conjuntamente en la demanda alimentaria, la disponibilidad temporal de agua, la productividad hídrica y la sensibilidad al déficit permite aumentar la proporción de consumo atendido durante temporadas secas, en comparación con una planificación basada únicamente en la producción histórica o en los precios recientes.

Esta hipótesis deberá ponerse a prueba mediante datos y escenarios de simulación.

## 1.6. Delimitación provisional

| Elemento | Delimitación inicial |
|---|---|
| Territorio | Facatativá y conexiones translocales necesarias para explicar el abastecimiento |
| Problema | Uso agrícola del agua durante temporadas secas y respuesta a la demanda alimentaria |
| Punto de partida | Consumo observado |
| Unidad de análisis | Producto o cultivo |
| Actores iniciales | Restaurantes, productores, plazas y proveedores |
| Subsistemas | Consumo, demanda, clima, recurso hídrico, producción y oferta |
| Unidad temporal | Pendiente de definición según los ciclos de cultivo |
| Cultivos | Pendientes de selección con datos de consumo y producción territorial |
| Escenarios | Condición húmeda, promedio y seca |
| Resultado central | Cobertura alimentaria bajo restricción hídrica |

## 2. Metodología

### 2.1. Articulación del problema y selección de límites

En desarrollo.

### 2.2. Formulación de la hipótesis dinámica

Pendiente.

### 2.3. Formulación del modelo de simulación

Pendiente.

### 2.4. Pruebas y validación

Pendiente.

### 2.5. Diseño y evaluación de políticas

Pendiente.

## 3. Resultados

Pendiente.

## 4. Discusión

Pendiente.

## 5. Conclusiones

Pendiente.

## Referencias

Pendientes de búsqueda y consolidación.

