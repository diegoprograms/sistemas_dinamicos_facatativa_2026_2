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


$$
\text{Consumo observado}\rightarrow\text{demanda estimada}\rightarrow
\text{producción requerida}\rightarrow\text{agua requerida}
$$


$$
\text{Clima}\rightarrow\text{disponibilidad hídrica}\rightarrow
\text{producción real}\rightarrow\text{oferta}\rightarrow
\text{consumo atendido}
$$

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

La investigación se desarrollará mediante un enfoque de dinámica de sistemas, con el propósito de representar las relaciones temporales existentes entre el consumo alimentario, la demanda, el comportamiento fenológico de los cultivos, las condiciones climáticas, la disponibilidad hídrica, la producción y la oferta. La construcción del modelo seguirá un proceso iterativo que comprende la articulación del problema, la formulación de una hipótesis dinámica, la formulación del modelo de simulación, las pruebas de validación y la evaluación de políticas (Referencia sobre metodología de dinámica de sistemas).

### 2.1. Articulación del problema y selección de límites

La primera etapa del proyecto incluye la delimitación progresiva del sistema y el diseño de un mecanismo de recolección que permita obtener datos comparables entre establecimientos y jornadas. Como avance inicial, se definió una estrategia de observación en establecimientos alimentarios basada en el conteo de personas que ingresan durante intervalos determinados y en el registro de los residuos generados durante el periodo de observación.

Estos registros no equivalen directamente al consumo de productos agrícolas. El número de personas constituye una medida de la afluencia al establecimiento, mientras que la masa de residuos permite aproximarse al desperdicio generado. Por esta razón, la identificación de alimentos, ingredientes y cantidades consumidas requerirá fuentes complementarias o supuestos explícitos. Esta distinción se conservará durante la formulación del subsistema de consumo para evitar interpretar la afluencia o los residuos como mediciones directas de demanda alimentaria.

#### 2.1.1. Estructura de los datos de campo

La plantilla diseñada para los grupos de estudiantes organiza la información en tres conjuntos principales:

1. **Establecimientos:** código del establecimiento, grupo responsable, zona, tipo de establecimiento, referencia de ubicación, disponibilidad para colaborar con la medición de residuos y observaciones.
2. **Conteo de personas:** identificador de la jornada, fecha, establecimiento, grupo, zona, hora inicial, hora final, número de personas que ingresan, duración del intervalo y observaciones.
3. **Residuos:** identificador de la jornada, fecha, establecimiento, grupo, zona, tipo de residuo, masa, unidad, método de medición, periodo correspondiente y observaciones.

El identificador de jornada relaciona los intervalos de conteo y las mediciones de residuos efectuadas en un mismo establecimiento y fecha. Esta organización permite que una jornada contenga varios intervalos de observación y varias mediciones sin duplicar la información general del establecimiento.

Se establecieron como criterios preliminares de calidad el uso de códigos para los establecimientos, la ausencia de datos personales de consumidores, el registro explícito de las unidades de masa, la documentación de valores faltantes y la separación entre mediciones pesadas y valores estimados.

#### 2.1.2. Prototipo de captura y revisión

Se desarrolló una aplicación web en Streamlit para trasladar gradualmente la recolección desde archivos individuales hacia un formulario común. La página principal del prototipo permite que cada grupo registre su identificación, el código y la zona del establecimiento y la fecha de observación. A partir de estos campos, la aplicación genera un identificador de jornada y habilita formularios independientes para agregar intervalos de conteo y mediciones de residuos.

Durante el registro se valida que los campos mínimos de identificación estén completos y que la hora final de un intervalo sea posterior a su hora inicial. Una vista de revisión muestra los registros asociados con la jornada y calcula el número de intervalos, el total de personas contabilizadas y el número de mediciones de residuos. Esta revisión busca detectar errores antes del envío definitivo de la información.

La aplicación también incorpora un lector de archivos de Excel para facilitar la transición desde el procedimiento inicial. El usuario puede cargar una o varias plantillas, seleccionar un archivo y elegir la hoja que desea visualizar. De esta manera, los datos ya recolectados pueden inspeccionarse sin modificar los documentos originales.

El frontend fue organizado en módulos independientes para separar la configuración de los datos, el manejo del estado, el registro de campo, la lectura de archivos, los análisis preliminares y la conexión con el backend. Esta organización facilita corregir o ampliar una sección sin intervenir en todo el código de la interfaz.

#### 2.1.3. Estado de implementación y persistencia

A 10 de septiembre de 2026, el prototipo permite capturar y revisar información dentro de una sesión y visualizar las hojas de los archivos enviados por los estudiantes. Sin embargo, los registros ingresados mediante los formularios y los archivos cargados todavía permanecen únicamente en la memoria temporal de la sesión. Al cerrar la página o reiniciarse la aplicación, esta información puede perderse y no queda disponible para consolidación entre grupos.

Por esta razón, la aplicación aún no se utilizará como mecanismo definitivo de entrega. El siguiente desarrollo metodológico y técnico consiste en seleccionar un sistema de almacenamiento persistente, definir las reglas para evitar jornadas duplicadas y establecer un procedimiento de consulta y exportación de la información consolidada.

| Componente | Estado actual |
|---|---|
| Plantilla estandarizada para establecimientos, conteos y residuos | Implementada |
| Formulario web para identificación de jornadas | Implementado en prototipo |
| Registro de múltiples intervalos y mediciones por jornada | Implementado en prototipo |
| Revisión de los registros de la jornada | Implementada en prototipo |
| Lectura y visualización de varias hojas de Excel | Implementada |
| Organización modular del frontend | Implementada |
| Almacenamiento permanente y consolidación entre grupos | Pendiente |
| Control de usuarios, duplicados y correcciones posteriores | Pendiente |
| Exportación del conjunto consolidado | Pendiente |
| Integración de estos datos con el modelo dinámico | Pendiente |

### 2.2. Formulación de la hipótesis dinámica

La hipótesis dinámica buscará explicar cómo las relaciones entre el consumo, la producción requerida, el recurso hídrico, el comportamiento fenológico y la producción real pueden generar las condiciones de suficiencia o insuficiencia alimentaria observadas en el territorio.

#### 2.2.1. Identificación de variables y subsistemas

El modelo estará conformado inicialmente por los subsistemas de consumo, demanda, clima, recurso hídrico, fenología, producción y oferta. Para cada subsistema se identificarán las variables de entrada y salida, sus unidades de medición, sus fuentes de información y su dependencia temporal.

Las variables se clasificarán como niveles, flujos, variables auxiliares o parámetros, de acuerdo con la función que desempeñen en el modelo (Referencia sobre niveles y flujos en dinámica de sistemas).

#### 2.2.2. Establecimiento de relaciones entre subsistemas

Se estudiarán las posibles relaciones entre las variables mediante análisis gráfico, correlaciones estadísticas, antecedentes bibliográficos y conocimiento del sistema agrícola (Referencia sobre análisis de relaciones entre variables agrícolas).

Se diferenciará entre correlación, causalidad y sensibilidad. Una correlación permitirá identificar variables que presentan un comportamiento asociado en los datos, pero no demostrará por sí sola una relación causal. En consecuencia, las conexiones incorporadas al modelo deberán estar respaldadas por datos, fundamentos físicos, agronómicos o socioeconómicos y referencias bibliográficas.

Una de las relaciones estudiadas será la existente entre el comportamiento fenológico de los cultivos y el consumo alimentario de la comunidad. Esta relación no necesariamente será directa. El consumo permitirá calcular la demanda y la producción requerida, mientras que la fenología permitirá estimar el momento de cosecha y la producción que podría obtenerse.

Estas rutas pueden representarse inicialmente como:

$$
C(t)\rightarrow D(t)\rightarrow P_r(t)
$$

y:

$$
F(t)\rightarrow Y(t)\rightarrow P_a(t)
$$

donde \(C(t)\) representa el consumo observado; \(D(t)\), la demanda estimada; \(P_r(t)\), la producción requerida; \(F(t)\), el estado fenológico; \(Y(t)\), el rendimiento, y \(P_a(t)\), la producción agrícola real.

La comparación de las dos rutas permitirá analizar si un cultivo cumple las condiciones necesarias para sembrarse en una época determinada y si su cosecha puede coincidir con el periodo en el que se requiere el producto.

### 2.3. Formulación del modelo de simulación

Durante esta etapa, las relaciones planteadas en la hipótesis dinámica se transformarán en ecuaciones, parámetros y reglas de decisión que puedan implementarse en el modelo computacional.

#### 2.3.1. Formulación de ecuaciones diferenciales

Las variables que presenten cambios continuos o acumulaciones a través del tiempo serán representadas mediante ecuaciones diferenciales. La forma de cada ecuación dependerá de la naturaleza de la variable, los datos disponibles y los modelos reportados en la bibliografía.

Por ejemplo, el cambio del estado fenológico podrá expresarse inicialmente como:

$$
\frac{dF}{dt}=f(T,H,A,R,\ldots)
$$

donde \(T\) representa la temperatura; \(H\), la humedad; \(A\), la disponibilidad de agua, y \(R\), la radiación solar (Referencia sobre modelos fenológicos de cultivos).

#### 2.3.2. Integración mediante la regla de la cadena

Cuando una variable dependa de otra y esta, a su vez, dependa del tiempo o de una tercera variable, se evaluará la aplicación de la regla de la cadena. Esta herramienta permitirá relacionar tasas de cambio pertenecientes a diferentes subsistemas, aunque las variables no se encuentren dentro del mismo bucle de realimentación (Referencia sobre regla de la cadena en modelos dinámicos).

Por ejemplo, si la producción agrícola depende del rendimiento y el rendimiento depende del estado fenológico:

$$
\frac{dP_a}{dt}
=
\frac{dP_a}{dY}
\frac{dY}{dF}
\frac{dF}{dt}
$$

De forma semejante, la variación de la producción requerida puede relacionarse con el cambio del consumo:

$$
\frac{dP_r}{dt}
=
\frac{dP_r}{dC}
\frac{dC}{dt}
$$

La regla de la cadena será aplicada únicamente cuando exista una dependencia matemática y causal que pueda justificarse. Su aplicación no comprobará por sí misma la validez del modelo, por lo que sus resultados deberán contrastarse con información observada.

#### 2.3.3. Estimación de parámetros

Los parámetros podrán relacionarse con las tasas de crecimiento, la duración de las etapas fenológicas, el rendimiento, la eficiencia del riego, las pérdidas del sistema o la relación entre el consumo y la producción requerida.

Dependiendo de la información disponible, estos valores se obtendrán de datos recolectados, bases de datos institucionales, literatura científica, procesos de calibración o supuestos explícitos. Para cada parámetro se registrará su unidad, fuente, valor inicial, rango posible y nivel de incertidumbre.

#### 2.3.4. Implementación computacional

El modelo será implementado en Python mediante una estructura modular. Cada subsistema contará con componentes independientes para organizar sus variables y ecuaciones. Además, se incorporará un módulo de integración matemática para registrar las relaciones entre los subsistemas, formular las ecuaciones diferenciales, aplicar la regla de la cadena, estimar parámetros y comparar los resultados simulados con los datos reales.

### 2.4. Pruebas y validación

El modelo será sometido a pruebas estructurales, pruebas de condiciones extremas, comparación con datos reales y análisis de sensibilidad (Referencia sobre validación de modelos de dinámica de sistemas).

#### 2.4.1. Comparación con datos reales

Los resultados se compararán con datos observados de consumo, crecimiento, rendimiento, producción y oferta. Como indicador inicial de cobertura se podrá utilizar:

$$
I_c(t)=\frac{P_a(t)}{P_r(t)}
$$

Si \(I_c(t)\geq1\), la producción sería suficiente para cubrir la demanda estimada. Si \(I_c(t)<1\), existiría una brecha entre la producción obtenida y la requerida.

El error entre los resultados observados y simulados podrá expresarse como:

$$
E(t)=Y_{\text{observado}}(t)-Y_{\text{simulado}}(t)
$$

Posteriormente se seleccionarán medidas estadísticas de ajuste según la cantidad y las características de los datos disponibles (Referencia sobre calibración y validación de modelos).

Si el modelo no representa adecuadamente el comportamiento observado, deberán revisarse sus relaciones, parámetros, ecuaciones o hipótesis dinámica.

#### 2.4.2. Análisis de sensibilidad

El análisis de sensibilidad permitirá determinar cuáles parámetros producen los mayores cambios en los resultados del sistema. Para ello, se modificarán individualmente o en conjunto los valores de entrada y se observarán sus efectos sobre la producción, la disponibilidad hídrica y la cobertura de la demanda.

Este análisis no será interpretado como una correlación estadística, sino como una evaluación de la respuesta del modelo ante cambios en sus parámetros.

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
