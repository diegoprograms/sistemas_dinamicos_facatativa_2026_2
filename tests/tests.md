# Pruebas

Actualizado el 1 de octubre de 2026.

## Cobertura actual

`test_model.py` contiene pruebas de acoplamiento consumo-agua, brechas,
productividad hídrica, cálculos básicos de subsistemas, agua disponible no
negativa y rechazo de entradas físicamente inválidas.

## Conexiones

Importa directamente funciones de [backend/model](../backend/backend.md).
Usa valores definidos en las pruebas; no lee archivos de [data](../data/data.md).
No cubre rutas HTTP, formularios de [frontend](../frontend/frontend.md), persistencia
ni fenología. Estas pruebas de cálculo no sustituyen la validación científica
con observaciones reales.

## Ejecución y pendientes

Desde la raíz, con dependencias instaladas: `python -m pytest tests`.
Este documento describe la cobertura existente, no certifica una ejecución reciente.
Añadir pruebas de importación, integridad de registros y cálculos fenológicos
cuando se implementen esos componentes y se acuerden sus requisitos.
