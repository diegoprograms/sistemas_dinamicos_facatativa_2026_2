# Sistema dinámico hídrico-alimentario

Modelo de dinámica de sistemas para estudiar la relación entre consumo,
demanda, clima, recurso hídrico, producción y oferta alimentaria en
Facatativá, Cundinamarca.

## Resumen por carpeta

Actualizado el 1 de octubre de 2026. Este README es el resumen general del
proyecto; cada carpeta mantiene un documento con su mismo nombre, con detalles y pendientes.

| Carpeta | Estado actual | Conexiones de programación existentes |
|---|---|---|
| [backend](backend/backend.md) | API FastAPI y cálculos preliminares; sin persistencia ni modelo fenológico implementado. | El frontend consulta `/health`; las pruebas importan funciones de `backend.model`. |
| [data](data/data.md) | Estructura para originales, procesados y ejemplos; sin conjuntos de datos incorporados. | Sin lectura o escritura persistente conectada al frontend o backend. |
| [docs](docs/docs.md) | Artículo, inventario de variables, ecuaciones y decisiones. Fenología es el foco actual. | Referencia metodológica; los programas no cargan estos Markdown. |
| [frontend](frontend/frontend.md) | Prototipo Streamlit de captura, revisión, lectura de Excel y estimación. Datos temporales de sesión. | Cliente HTTP al backend únicamente para comprobar su estado. |
| [notebooks](notebooks/notebooks.md) | Carpeta preparada para análisis; pendiente organizar la exploración de fenología. | Sin flujo implementado con `data` o `backend` dentro de esta carpeta. |
| [tests](tests/tests.md) | Pruebas de cálculos y validaciones físicas básicas. | Importaciones directas de `backend.model`; no prueban la interfaz ni la API. |

Las conexiones previstas son `data → notebooks → formulación del modelo` y
`frontend → backend → almacenamiento`, pero aún no están implementadas como
un flujo completo. La documentación de variables permanece en
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
