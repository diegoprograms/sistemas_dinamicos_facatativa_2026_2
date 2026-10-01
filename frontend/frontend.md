# Frontend

Actualizado el 1 de octubre de 2026.

## Función y estado

Prototipo Streamlit. `app.py` organiza la navegación; `views/` separa registro
de estudiantes, lectura de Excel, resumen, tablas de recolección, observaciones,
estimación de consumo y comprobación de conexión.

`data_config.py` define tablas y escenarios iniciales; `state.py` los mantiene
en `st.session_state`. Los formularios no guardan registros permanentemente.
El lector permite consultar archivos `.xlsx` y sus hojas durante la sesión;
no los importa a una base de datos. Las estimaciones usan entradas y supuestos
de la interfaz, no constituyen resultados validados de investigación.

## Conexiones

`views/connection.py` utiliza `api_client.py` para consultar
`http://127.0.0.1:8000/health` en [backend](../backend/backend.md).
No llama al endpoint de simulación ni guarda datos en [data](../data/data.md).
El inventario de [variables](../docs/variables.md) no genera automáticamente
formularios. No existe todavía una vista específica de fenología.

## Pendientes

Adaptar la interfaz al trabajo fenológico una vez revisados los archivos.
Posteriormente conectar carga, consulta y persistencia; el acceso por restaurante
y la captura en línea son objetivos futuros. Conservar la distinción entre
datos observados y estimaciones.

Desde la raíz: `streamlit run frontend/app.py`.
