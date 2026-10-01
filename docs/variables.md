# Variables del proyecto

## Alcance actual — 1 de octubre de 2026

El equipo informa que solo dispone de información de fenología. Este será el
único conjunto de trabajo por ahora. Las demás variables quedan planteadas,
sin asumir mediciones disponibles. Los formularios existentes son prototipos.

Los archivos de fenología aún deben identificarse y revisarse. Los campos
siguientes son una propuesta, no una afirmación de que todos están disponibles.
No se completarán faltantes con datos inventados ni con ceros.

## Fenología: conjunto de trabajo actual

| Campo propuesto | Unidad o formato | Condición |
|---|---|---|
| Identificador | Código | Asignado al incorporar el registro. |
| Cultivo y variedad | Texto | Variedad solo si se conoce. |
| Tipo de información | Campo / bibliografía / estimación | Separar observaciones y referencias. |
| Fuente | Archivo, hoja y fila o referencia | Conservar la procedencia. |
| Lote o sitio y ciclo agrícola | Códigos o texto | Si existen en datos de campo. |
| Fecha de siembra o trasplante | Fecha y tipo de evento | Si se conoce. |
| Fecha de observación | Fecha | Para observaciones fechadas. |
| Etapa fenológica | Nombre original y normalizado | Variable central; etapas según cultivo. |
| Escala o criterio de identificación | Texto y código si existe | Permite interpretar cada etapa. |
| Inicio y final de etapa | Fechas o días desde un evento definido | Si la fuente los aporta; distinguir observado y estimado. |
| Duración de etapa | Días | Reportada o calculada con límites conocidos; indicar método. |
| Tiempo desde siembra o trasplante | Días | Calculado solo con fechas y evento de referencia conocidos. |
| Proporción en la etapa y tamaño de muestra | %, número de plantas | Opcionales, si fueron medidos. |
| Observaciones y evidencia | Texto o ruta | Notas y fotografías disponibles. |
| Calidad del dato | Reportado / calculado / estimado y notas | Registrar faltantes, dudas y método. |

Una fila corresponderá a una observación o a un dato de referencia claramente
identificado. El esquema se adaptará a los archivos: una referencia con
duraciones no requiere inventar fechas o lotes. La primera detección de una
etapa en visitas espaciadas no equivale necesariamente a su inicio exacto.

## Inventario general de datos que se podrían registrar

Este inventario reúne los once bloques propuestos para el proyecto. Incluye
mediciones, identificadores, parámetros de referencia y resultados calculados;
no todos son variables medidas directamente. Se irá ajustando para seleccionar
las futuras variables, sus unidades, periodicidad y obligatoriedad.

Actualmente solo la fenología asociada a los cultivos constituye información
disponible reportada por el equipo. Los demás bloques son posibilidades de
recolección y desarrollo, no conjuntos de datos existentes. La sección anterior
conserva el detalle del trabajo fenológico actual.

| Bloque | Datos que se podrían almacenar | Quién los aporta |
|---|---|---|
| **1. Catálogos e identificación** | Restaurantes, grupos de estudiantes, productores, fincas, lotes, ubicación, productos, cultivos, variedades, presentaciones y unidades. Relación entre producto comprado y cultivo de origen. | Equipo investigador y participantes. |
| **2. Demanda y abastecimiento** | Periodo, restaurante, producto, compras, cantidades y unidades, procedencia, ingredientes utilizados o inventarios inicial/final, descartes, faltantes y almuerzos servidos. Precio de compra, si se evaluará viabilidad económica. Oferta local y externa y pérdidas de abastecimiento, cuando se amplíe el estudio de la oferta. | Restaurantes y estudiantes; proveedores y equipo investigador para información adicional de oferta. |
| **3. Observaciones de campo en establecimientos** | Jornada, establecimiento, intervalos de conteo, personas observadas, residuos por tipo, masa, método de medición y observaciones. Su registro está planteado en el prototipo; no se asume disponibilidad de datos. | Estudiantes. |
| **4. Lotes y ciclos agrícolas** | Lote, cultivo, variedad, área, fecha de siembra o trasplante, manejo, fecha de cosecha prevista y real, producción total y comercializable, pérdidas y causas. | Productores y estudiantes. |
| **5. Fenología observada** | Ciclo agrícola, fecha de observación, etapa, criterio utilizado para identificarla, proporción de plantas en esa etapa cuando corresponda, signos de estrés y evidencia opcional. Vinculación con el cultivo y la variedad; detalle en la sección de fenología. | Productores o estudiantes con un protocolo común, coordinados por el equipo investigador. |
| **6. Parámetros fenológicos y agronómicos** | Etapas propias de cada cultivo, duración de referencia, temperatura base y requerimientos térmicos cuando exista un modelo aplicable, coeficientes de cultivo por etapa, profundidad de raíces y respuesta al déficit hídrico. Cada valor con fuente y rango de incertidumbre. | Bibliografía, especialistas y calibración local. |
| **7. Clima** | Fecha, estación o ubicación, precipitación, temperaturas mínima y máxima, humedad, radiación y viento cuando estén disponibles; evapotranspiración de referencia y método de cálculo. | Estaciones y fuentes institucionales. |
| **8. Suelo** | Lote, fecha y profundidad de muestreo, textura, profundidad efectiva, capacidad de campo, punto de marchitez, infiltración o drenaje y humedad observada cuando pueda medirse. | Análisis de suelo, mediciones y fuentes técnicas. |
| **9. Disponibilidad y aplicación de agua** | Fuente, disponibilidad por periodo, restricciones, almacenamiento; por evento de riego: fecha, lote, volumen o caudal y duración, método y eficiencia estimada con su fuente. | Productores y fuentes institucionales. |
| **10. Modelos y simulaciones** | Versión de ecuaciones, parámetros, datos utilizados, condiciones iniciales, escenarios, resultados, errores de validación e indicadores de comparación: producción requerida, agua requerida, brechas alimentaria e hídrica, productividad hídrica y cobertura de demanda. | Aplicación y equipo investigador. |
| **11. Archivos y trazabilidad** | Excel original, responsable de carga, fecha, versión de plantilla, validaciones, registros importados, duplicados detectados y correcciones. | Aplicación. |

Al concretar cada bloque se definirán unidades comparables: por ejemplo,
kg por periodo para abastecimiento, ha para superficie, días para duraciones,
mm para precipitación, m³ para volúmenes de agua y °C para temperatura.
Siempre se conservarán la unidad original y el método de conversión, si aplica.

Todos los registros deberán conservar unidad, fuente y condición de medido,
estimado o calculado. Los parámetros deberán incluir ámbito de aplicación e
incertidumbre. Tener una fórmula no significa disponer de resultados.
La fenología predicha se separará de la observada cuando exista un modelo.

## Orden de construcción

1. Revisar los archivos de fenología: cultivos, fuentes, etapas y unidades.
2. Ajustar el esquema y consolidar solo fenología, preservando originales.
3. Consultar y analizar etapas y duraciones según lo que permitan los datos.
4. Incorporar clima y parámetros para evaluar modelos fenológicos; después,
   suelo y agua para estudiar restricciones hídricas.
5. Añadir producción y demanda de restaurantes cuando se recolecten.
6. Calibrar y validar el modelo integrado antes de comparar cultivos y siembras.

La fenología sola no permite cuantificar ahorro de agua ni cobertura de demanda.
