# Backend

Actualizado el 1 de octubre de 2026.

## Función y estado

Contiene la API FastAPI y las funciones matemáticas preliminares del proyecto.
`main.py` registra las rutas; `model/` organiza subsistemas, indicadores,
acoplamientos, parámetros y validaciones. No hay todavía un modelo dinámico
completo ni un subsistema fenológico implementado.

Rutas actuales:

- `GET /health`: estado del servicio.
- `GET /data/required`: lista preliminar de campos; no recibe ni guarda datos
  y todavía no refleja el inventario completo de `docs/variables.md`.
- `GET /simulation/example`: calcula brechas con valores fijos de ejemplo.

`services/simulation_service.py` envuelve el cálculo preliminar, pero la ruta
de ejemplo llama directamente al modelo. `database.py` solo declara una URL
SQLite: no crea tablas ni implementa persistencia.

## Conexiones

- [frontend](../frontend/frontend.md) consulta únicamente `/health`.
- [tests](../tests/tests.md) importa funciones de `model/` directamente.
- No hay integración persistente con [data](../data/data.md).
- [docs](../docs/docs.md) describe el modelo; sus archivos no se cargan en ejecución.

## Pendientes

Definir la incorporación de fenología después de revisar los archivos reales;
implementar almacenamiento, validaciones y rutas de consulta/carga. Revisar el
contrato de `/data/required` cuando se acuerde el esquema. Los otros subsistemas
siguen como base preliminar para etapas posteriores.

Desde la raíz: `uvicorn backend.main:app --reload`.
