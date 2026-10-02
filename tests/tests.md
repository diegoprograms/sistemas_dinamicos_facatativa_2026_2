# Pruebas

Actualizado el 1 de octubre de 2026.

## Cobertura actual

`test_model.py` contiene pruebas de acoplamiento consumo-agua, brechas,
productividad hídrica, cálculos básicos de subsistemas, agua disponible no
negativa y rechazo de entradas físicamente inválidas.

## Conexiones

Importa directamente funciones de [backend/model](../backend/backend.md).
Usa valores definidos en las pruebas; no lee archivos de [data](../data/data.md).
Las pruebas del modelo no cubren rutas HTTP, formularios de
[frontend](../frontend/frontend.md) ni fenología. La persistencia tiene pruebas
propias descritas abajo. Estas pruebas de cálculo no sustituyen la validación científica
con observaciones reales.

## Ejecución y pendientes

Desde la raíz, con dependencias instaladas: `python -m pytest tests`.
Este documento describe la cobertura existente, no certifica una ejecución reciente.
Ampliar cobertura de interfaz, API y cálculos fenológicos al desarrollar esos componentes.

## Actualización: almacenamiento de abastecimiento

`test_restaurant_storage.py` verifica persistencia entre conexiones, rechazo
de lotes inválidos sin inserción parcial, validación de fechas/unidades/cantidades,
duplicados entre formulario y CSV y conservación del archivo original. Usa
un directorio temporal, sin tocar datos reales. Con pandas y openpyxl instalados puede ejecutarse sin pytest:
`python3 -m unittest discover -s tests -p test_restaurant_storage.py -v`.
