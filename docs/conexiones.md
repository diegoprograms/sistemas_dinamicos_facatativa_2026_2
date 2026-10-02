# Conexiones entre carpetas

Actualizado el 1 de octubre de 2026.

## Flujo implementado: abastecimiento de restaurantes

```text
frontend/app.py
  └─ frontend/views/restaurant_storage.py
       ├─ frontend/api_client.py → dirección del backend (API_URL)
       └─ solicitudes HTTP
            ↓
backend/main.py → registra las rutas
  └─ backend/routes/restaurant_routes.py
       └─ backend/services/restaurant_storage.py
            ├─ data/private/restaurantes.sqlite
            └─ data/private/originales/
```

| Conexión | Archivos responsables | Función |
|---|---|---|
| Entrada del frontend → pantalla | [frontend/app.py](../frontend/app.py) importa [frontend/views/restaurant_storage.py](../frontend/views/restaurant_storage.py). | Incluye «Abastecimiento guardado» en el menú de Streamlit. |
| Frontend → backend | [frontend/views/restaurant_storage.py](../frontend/views/restaurant_storage.py) utiliza `API_URL` de [frontend/api_client.py](../frontend/api_client.py) y envía solicitudes HTTP a [backend/routes/restaurant_routes.py](../backend/routes/restaurant_routes.py). | Guarda registros, importa archivos y consulta lo almacenado. La vista realiza las solicitudes; el cliente aporta la dirección. |
| Entrada del backend → rutas | [backend/main.py](../backend/main.py) registra el router de [backend/routes/restaurant_routes.py](../backend/routes/restaurant_routes.py). | Hace disponibles los endpoints en FastAPI. |
| Rutas → servicio | [backend/routes/restaurant_routes.py](../backend/routes/restaurant_routes.py) llama a [backend/services/restaurant_storage.py](../backend/services/restaurant_storage.py). | Valida entradas, importa archivos, detecta duplicados exactos y consulta registros. |
| Backend → data | [backend/services/restaurant_storage.py](../backend/services/restaurant_storage.py). | Escribe y lee SQLite; conserva los originales de las importaciones aceptadas. |
| Tests → backend | [tests/test_restaurant_storage.py](../tests/test_restaurant_storage.py) importa el servicio de almacenamiento; [tests/test_model.py](../tests/test_model.py) importa funciones de `backend/model/`. | Comprueba persistencia, importaciones, validaciones y cálculos. El almacenamiento de prueba usa directorios temporales. |

## Rutas utilizadas

| Método y ruta | Entrada o salida | Operación del servicio |
|---|---|---|
| `POST /restaurants/records` | Un registro de abastecimiento en JSON. | `save_rows`: valida y guarda; devuelve cantidades de guardados y duplicados. |
| `POST /restaurants/imports` | Nombre del archivo y contenido en base64. | `import_file`: lee CSV o primera hoja XLSX, valida, conserva el original e incorpora registros. |
| `GET /restaurants/records` | Lista de registros guardados con su procedencia y fecha de guardado. | `list_records`: consulta SQLite. |

El formulario y la importación convergen en el mismo servicio de validación y
guardado. La consulta recupera los registros del backend; la exportación CSV
se genera en el frontend a partir de esa respuesta.

## Ubicación y configuración del almacenamiento

- Base de datos por defecto: `data/private/restaurantes.sqlite`.
- Originales aceptados: `data/private/originales/`, identificados por hash.
- `RESTAURANT_STORAGE_DIR` permite configurar otra carpeta en el backend.
- `BACKEND_URL` permite configurar la dirección usada por el frontend;
  por defecto es `http://127.0.0.1:8000`.

Las rutas de almacenamiento pertenecen al equipo donde se ejecuta el backend.
Cerrar Streamlit no elimina los registros. La carpeta `data/private/` está
excluida de Git: el commit y el push no respaldan estos datos. Para respaldarla,
detener escrituras del backend y copiar la carpeta completa a otro almacenamiento.
`backend/database.py` conserva una URL antigua y no participa en este flujo.

## Otras conexiones existentes

- [frontend/views/connection.py](../frontend/views/connection.py) llama a
  `health_check` de [frontend/api_client.py](../frontend/api_client.py), que
  consulta `GET /health` definido en [backend/main.py](../backend/main.py).
- [backend/routes/simulation_routes.py](../backend/routes/simulation_routes.py)
  llama directamente a [backend/model/system_model.py](../backend/model/system_model.py)
  para la simulación de ejemplo. El frontend todavía no utiliza esa ruta.

## Carpetas sin integración automática y alcance pendiente

| Carpeta o componente | Situación actual |
|---|---|
| [docs](docs.md) | Documenta variables, ecuaciones y decisiones. El código no carga estos Markdown; editarlos no modifica formularios ni modelos. |
| [notebooks](../notebooks/notebooks.md) | Todavía no tiene un flujo implementado para leer los registros guardados y analizarlos. |
| `data/raw`, `data/processed`, `data/examples` | Organización prevista para datos de investigación. El módulo de restaurantes utiliza `data/private/`. |
| Formularios anteriores de conteos y residuos | Mantienen registros en la sesión de Streamlit; no utilizan el servicio persistente. |
| Lector anterior de archivos de estudiantes | Permite visualizar Excel en sesión; no importa esos archivos a la base. |
| Acceso público por restaurante | Pendiente de autenticación, separación de datos por usuario y despliegue. La versión actual es local para el equipo. |

El flujo permanente descrito aquí corresponde al abastecimiento de restaurantes.
La integración con fenología, análisis y modelo dinámico sigue pendiente.
Actualizar este documento cuando cambien rutas, responsables o conexiones.
