# Sistema dinámico hídrico-alimentario

Modelo de dinámica de sistemas para estudiar la relación entre consumo,
demanda, clima, recurso hídrico, producción y oferta alimentaria en
Facatativá, Cundinamarca.

## Resumen por carpeta

Consulte [Conexiones entre carpetas](docs/conexiones.md) para ver los archivos
que enlazan la interfaz, la API, el almacenamiento y las pruebas.

Actualizado el 1 de octubre de 2026. Este README es el resumen general del
proyecto; cada carpeta mantiene un documento con su mismo nombre, con detalles y pendientes.

| Carpeta | Estado actual | Conexiones de programación existentes |
|---|---|---|
| [backend](backend/backend.md) | API FastAPI, cálculos preliminares y persistencia local de abastecimiento en SQLite; fenología aún pendiente. | El frontend consulta salud, guarda y consulta abastecimiento e importa archivos; pruebas del modelo y almacenamiento. |
| [data](data/data.md) | Estructura de datos; `data/private/` recibe la base SQLite y originales al guardar entregas. | El backend escribe y consulta `data/private/`, excluido de Git. |
| [docs](docs/docs.md) | Artículo, inventario de variables, ecuaciones y decisiones. Fenología es el foco actual. | Referencia metodológica; los programas no cargan estos Markdown. |
| [frontend](frontend/frontend.md) | Abastecimiento con guardado permanente; conteos, residuos y otras vistas siguen temporales. | Cliente HTTP al backend para estado, registros e importaciones de abastecimiento. |
| [notebooks](notebooks/notebooks.md) | Carpeta preparada para análisis; pendiente organizar la exploración de fenología. | Sin flujo implementado con `data` o `backend` dentro de esta carpeta. |
| [tests](tests/tests.md) | Pruebas de cálculos, validaciones, persistencia, duplicados e importación. | Pruebas del modelo y servicio de almacenamiento; interfaz pendiente de validación manual. |

El flujo `frontend → backend → almacenamiento` está implementado localmente para
abastecimiento. `data → notebooks → formulación del modelo` sigue previsto. La documentación de variables permanece en
[docs/variables.md](docs/variables.md); `data` alojará los registros y archivos.

Al modificar un componente, actualizar su documento si cambia su estado,
funcionamiento, conexiones o pendientes. Actualizar también esta tabla cuando
el cambio afecte el resumen general. Separar siempre lo implementado de lo previsto.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows:

```powershell
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

Backend:

```bash
uvicorn backend.main:app --reload
```

Frontend, en otra terminal:

```bash
streamlit run frontend/app.py
```

## Estado metodológico

El proyecto se encuentra en la etapa 1: articulación del problema y selección
de límites. Las ecuaciones incluidas son preliminares y sirven como base
técnica para el desarrollo posterior.

Actualización del 1 de octubre de 2026: el equipo dispone únicamente de
información de fenología. El trabajo de datos comenzará por revisar y organizar
esa información. Las demás variables quedan planteadas para etapas posteriores
en [docs/variables.md](docs/variables.md); no se asume que haya datos de
restaurantes disponibles. Los formularios existentes siguen siendo prototipos.

## Próximas decisiones

- [ ] Confirmar el territorio y las conexiones translocales.
- [ ] Seleccionar los cultivos a estudiar.
- [ ] Definir el periodo de recolección y el horizonte de simulación.
- [ ] Identificar fuentes de datos climáticos e hídricos.
- [ ] Construir modos de referencia.
- [ ] Formular los primeros bucles causales.

## Guardado de restaurantes

La página **Abastecimiento guardado** permite registrar compras por producto,
importar CSV o la primera hoja de un Excel con columnas de la plantilla y
consultar/exportar lo guardado. Requiere ejecutar backend y frontend.

- Base SQL: `data/private/restaurantes.sqlite`.
- Archivos originales aceptados: `data/private/originales/`, nombrados por hash.
- Configuración opcional del backend: `RESTAURANT_STORAGE_DIR` (ruta persistente).
- Configuración opcional de Streamlit: `BACKEND_URL` (por defecto localhost:8000).

El cierre de Streamlit no elimina estos datos. La carpeta está excluida de Git;
un push no es un respaldo. Para una copia coherente, detener escrituras del
backend y copiar la carpeta completa a otro almacenamiento.

Esta versión es para uso local del equipo. El despliegue público y el acceso
por restaurante no están implementados. Para operación en internet se prevé
PostgreSQL y almacenamiento persistente de archivos; la migración aún está pendiente.
