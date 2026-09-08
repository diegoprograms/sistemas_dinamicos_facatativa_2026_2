import streamlit as st

from api_client import health_check


def show_connection() -> None:
    st.header("Estado del sistema")
    st.write("Comprueba si el frontend puede comunicarse con la API FastAPI.")
    if st.button("Comprobar conexión con el backend", type="primary"):
        try:
            status = health_check()
            st.success(status["message"])
        except Exception as error:
            st.error(f"No fue posible conectar con el backend: {error}")
