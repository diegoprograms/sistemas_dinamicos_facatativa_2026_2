import streamlit as st

from frontend.api_client import health_check


st.set_page_config(page_title="Sistema hídrico-alimentario", layout="wide")
st.title("Sistema dinámico hídrico-alimentario")
st.write(
    "Prototipo para integrar consumo, clima, recurso hídrico, producción "
    "y oferta alimentaria en Facatativá."
)

if st.button("Comprobar conexión con el backend"):
    try:
        status = health_check()
        st.success(status["message"])
    except Exception as error:
        st.error(f"No fue posible conectar con el backend: {error}")

st.info(
    "Primera etapa: articulación del problema. Las pantallas de datos, "
    "simulación y resultados se incorporarán progresivamente."
)

