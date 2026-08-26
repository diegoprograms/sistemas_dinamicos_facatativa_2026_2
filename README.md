# Sistema dinámico hídrico-alimentario

Modelo de dinámica de sistemas para estudiar la relación entre consumo,
demanda, clima, recurso hídrico, producción y oferta alimentaria en
Facatativá, Cundinamarca.

## Estructura

- `frontend/`: interfaz Streamlit.
- `backend/`: API FastAPI y modelo matemático.
- `data/`: datos originales, procesados y ejemplos.
- `notebooks/`: exploración y formulación del modelo.
- `docs/`: artículo, variables, ecuaciones, decisiones y diagramas.
- `tests/`: pruebas del modelo.

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

## Próximas decisiones

- [ ] Confirmar el territorio y las conexiones translocales.
- [ ] Seleccionar los cultivos a estudiar.
- [ ] Definir el periodo de recolección y el horizonte de simulación.
- [ ] Identificar fuentes de datos climáticos e hídricos.
- [ ] Construir modos de referencia.
- [ ] Formular los primeros bucles causales.

