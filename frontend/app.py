import streamlit as st

from views.restaurant_storage import show_restaurant_storage
from state import initialize_state
from views.analysis import show_estimation, show_summary
from views.collection import show_collection, show_quick_observation
from views.connection import show_connection
from views.registration import show_student_registration
from views.student_files import show_student_files


st.set_page_config(page_title="Consumo alimentario estimado", page_icon="🌱", layout="wide")


def show_header() -> None:
    st.title("Consumo alimentario durante el almuerzo")
    st.caption(
        "Prototipo para organizar datos observados, supuestos de estimación "
        "y resultados calculados en establecimientos de Facatativá."
    )


PAGES = {
    "Abastecimiento guardado": show_restaurant_storage,
    "Registrar datos": show_student_registration,
    "Archivos de estudiantes": show_student_files,
    "Resumen": show_summary,
    "Tablas de recolección": show_collection,
    "Nueva observación": show_quick_observation,
    "Estimación": show_estimation,
    "Conexión": show_connection,
}


initialize_state()
show_header()
page = st.sidebar.radio("Navegación", list(PAGES))
st.sidebar.caption("Etapa actual: prototipo de captura y revisión")
PAGES[page]()
