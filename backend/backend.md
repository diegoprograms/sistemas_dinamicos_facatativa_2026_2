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
de ejemplo llama directamente al modelo. `database.py` conserva la configuración antigua sin uso. La persistencia nueva
se implementa en `services/restaurant_storage.py`.

## Conexiones

- [frontend](../frontend/frontend.md) consulta `/health` y las rutas de restaurantes.
- [tests](../tests/tests.md) importa funciones de `model/` directamente.
- El servicio escribe en `data/private/` o en `RESTAURANT_STORAGE_DIR`.
- [docs](../docs/docs.md) describe el modelo; sus archivos no se cargan en ejecución.

## Pendientes

Definir la incorporación de fenología después de revisar los archivos reales;
implementar su almacenamiento, validaciones y rutas de consulta/carga. Revisar el
contrato de `/data/required` cuando se acuerde el esquema. Los otros subsistemas
siguen como base preliminar para etapas posteriores.

Desde la raíz: `uvicorn backend.main:app --reload`.

## Actualización: almacenamiento de abastecimiento

`routes/restaurant_routes.py` expone `GET/POST /restaurants/records` y
`POST /restaurants/imports` (nombre y contenido base64). El servicio valida
fechas, campos, cantidades finitas y unidades kg/g. Usa transacciones SQLite
y huellas de contenido para evitar duplicados exactos. CSV UTF-8 y primera
hoja XLSX: máximo 5 MB. Archivos aceptados conservados por hash.

La base se crea al consultar o guardar. No hay autenticación ni separación
de datos por usuario; ejecutar localmente hasta implementar esos controles.
La ruta SQLite anterior no se utiliza para esta funcionalidad.
