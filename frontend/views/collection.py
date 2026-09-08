from datetime import date, time

import pandas as pd
import streamlit as st

from data_config import TABLES


def show_collection() -> None:
    st.header("Información que se suministrará")
    st.write(
        "Las tablas son editables. En esta etapa los cambios se conservan solamente "
        "mientras la aplicación permanezca abierta."
    )
    tabs = st.tabs(list(TABLES))
    for tab, name in zip(tabs, TABLES):
        with tab:
            st.subheader(name)
            st.session_state[f"table_{name}"] = st.data_editor(
                st.session_state[f"table_{name}"], num_rows="dynamic", hide_index=True,
                width="stretch", key=f"editor_{name}",
            )

    st.subheader("Evidencia del menú")
    uploaded_file = st.file_uploader(
        "Cargar fotografía o captura del menú", type=["png", "jpg", "jpeg", "webp"],
        help="No incluya nombres, teléfonos, direcciones particulares ni otros datos personales.",
    )
    if uploaded_file:
        st.image(uploaded_file, caption=uploaded_file.name, width=520)
        st.success("Imagen lista para revisión. Todavía no se almacena de forma permanente.")


def show_quick_observation() -> None:
    st.header("Nueva observación de almuerzo")
    st.write("Formulario de ejemplo para visualizar la captura que realizará el equipo de campo.")
    with st.form("observation_form"):
        col1, col2, col3 = st.columns(3)
        site = col1.text_input("Código del establecimiento", value="SIT001")
        observation_date = col2.date_input("Fecha", value=date.today())
        special_day = col3.selectbox("Tipo de día", ["Normal", "Festivo", "Promoción", "Otro"])
        col1, col2, col3, col4 = st.columns(4)
        start_time = col1.time_input("Hora de inicio", value=time(12, 0))
        end_time = col2.time_input("Hora de finalización", value=time(14, 0))
        entered = col3.number_input("Clientes que ingresaron", min_value=0, step=1)
        excluded = col4.number_input("Personas excluidas", min_value=0, step=1)
        notes = st.text_area("Observaciones")
        submitted = st.form_submit_button("Agregar observación", type="primary")

    if submitted:
        valid = max(int(entered) - int(excluded), 0)
        observations = st.session_state["table_Observaciones del almuerzo"]
        new_id = f"OBS{len(observations) + 1:03d}"
        row = pd.DataFrame([{
            "id_observacion": new_id,
            "id_sitio": site,
            "fecha": observation_date.isoformat(),
            "hora_inicio": start_time.strftime("%H:%M"),
            "hora_fin": end_time.strftime("%H:%M"),
            "clientes_ingresaron": int(entered),
            "personas_excluidas": int(excluded),
            "clientes_validos": valid,
            "dia_especial": special_day,
            "observaciones": notes,
        }])
        st.session_state["table_Observaciones del almuerzo"] = pd.concat(
            [observations, row], ignore_index=True
        )
        st.success(f"Observación {new_id} agregada: {valid} clientes válidos.")
