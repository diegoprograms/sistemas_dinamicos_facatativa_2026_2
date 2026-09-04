from datetime import date, time

import pandas as pd
import streamlit as st

from api_client import health_check


st.set_page_config(page_title="Consumo alimentario estimado", page_icon="🌱", layout="wide")


TABLES = {
    "Establecimientos": pd.DataFrame([{
        "id_sitio": "SIT001", "nombre": "Restaurante El Campo", "sector": "Centro",
        "tipo_menu": "Ejecutivo", "observaciones": "",
    }]),
    "Observaciones del almuerzo": pd.DataFrame([{
        "id_observacion": "OBS001", "id_sitio": "SIT001", "fecha": "2026-09-01",
        "hora_inicio": "12:00", "hora_fin": "14:00", "clientes_ingresaron": 100,
        "personas_excluidas": 5, "clientes_validos": 95, "dia_especial": "No",
        "observaciones": "",
    }]),
    "Menús": pd.DataFrame([{
        "id_menu": "MEN001", "id_sitio": "SIT001", "fecha": "2026-09-01",
        "tipo_menu": "Ejecutivo", "archivo_foto": "menu_ejemplo.jpg",
        "fuente": "Plataforma de domicilios", "estado_revision": "Pendiente",
    }]),
    "Platos": pd.DataFrame([{
        "id_plato": "PLA001", "id_menu": "MEN001", "nombre_plato": "Ajiaco",
        "descripcion": "Con arroz y aguacate", "precio": 22000, "es_almuerzo": True,
        "es_popular": True, "participacion_estimada": 0.30,
        "fuente_participacion": "Supuesto",
    }]),
    "Ingredientes por plato": pd.DataFrame([{
        "id_ingrediente_plato": "ING001", "id_plato": "PLA001", "producto": "Papa",
        "variedad": "Pastusa", "cantidad_g_por_porcion": 230,
        "cantidad_kg_por_porcion": 0.230, "estado_producto": "Crudo",
        "fuente_receta": "Receta estándar", "nivel_confianza": "Media",
    }]),
    "Abastecimiento": pd.DataFrame([{
        "id_abastecimiento": "ABA001", "id_sitio": "SIT001",
        "categoria_producto": "Verduras", "producto": "Papa",
        "frecuencia_compra": "Semanal", "intervalo_dias": 7, "dias_compra": "Lunes",
        "cantidad_compra_kg": 50.0, "lugar_compra": "Plaza de mercado",
        "fuente_dato": "Estimación", "nivel_confianza": "Baja",
    }]),
}

SCENARIOS = pd.DataFrame([
    {"escenario": "Bajo", "tasa_compra": 0.75, "platos_por_comprador": 0.95, "ajuste_porcion": 0.85},
    {"escenario": "Probable", "tasa_compra": 0.85, "platos_por_comprador": 1.00, "ajuste_porcion": 1.00},
    {"escenario": "Alto", "tasa_compra": 0.95, "platos_por_comprador": 1.05, "ajuste_porcion": 1.15},
])


def initialize_state() -> None:
    for name, dataframe in TABLES.items():
        key = f"table_{name}"
        if key not in st.session_state:
            st.session_state[key] = dataframe.copy()
    if "scenarios" not in st.session_state:
        st.session_state.scenarios = SCENARIOS.copy()


def show_header() -> None:
    st.title("Consumo alimentario durante el almuerzo")
    st.caption(
        "Prototipo para organizar datos observados, supuestos de estimación "
        "y resultados calculados en establecimientos de Facatativá."
    )


def show_summary() -> None:
    observations = st.session_state["table_Observaciones del almuerzo"]
    dishes = st.session_state["table_Platos"]
    ingredients = st.session_state["table_Ingredientes por plato"]
    valid_clients = pd.to_numeric(
        observations.get("clientes_validos", pd.Series(dtype=float)), errors="coerce"
    ).fillna(0).sum()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Establecimientos", len(st.session_state["table_Establecimientos"]))
    col2.metric("Clientes válidos", f"{valid_clients:,.0f}")
    col3.metric("Platos registrados", len(dishes))
    col4.metric("Productos identificados", ingredients["producto"].nunique())

    st.subheader("Flujo de la información")
    st.info(
        "Establecimiento → observación del almuerzo y menú → platos → "
        "ingredientes por porción → consumo estimado en kilogramos."
    )
    st.subheader("Clasificación de los datos")
    st.dataframe(pd.DataFrame([
        {"Tipo": "Observado", "Información": "Fecha, horario, clientes, foto y contenido del menú"},
        {"Tipo": "Estimado", "Información": "Tasa de compra, participación del plato y receta por porción"},
        {"Tipo": "Calculado", "Información": "Porciones estimadas y consumo por producto en kg"},
    ]), hide_index=True, width="stretch")


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
            "id_observacion": new_id, "id_sitio": site, "fecha": observation_date.isoformat(),
            "hora_inicio": start_time.strftime("%H:%M"), "hora_fin": end_time.strftime("%H:%M"),
            "clientes_ingresaron": int(entered), "personas_excluidas": int(excluded),
            "clientes_validos": valid, "dia_especial": special_day, "observaciones": notes,
        }])
        st.session_state["table_Observaciones del almuerzo"] = pd.concat(
            [observations, row], ignore_index=True
        )
        st.success(f"Observación {new_id} agregada: {valid} clientes válidos.")


def show_estimation() -> None:
    st.header("Estimación de consumo")
    st.write("Pruebe cómo los datos suministrados se convierten en kilogramos por producto.")
    st.subheader("Escenarios")
    st.session_state.scenarios = st.data_editor(
        st.session_state.scenarios, hide_index=True, width="stretch",
        key="scenario_editor",
    )
    col1, col2, col3 = st.columns(3)
    valid_clients = col1.number_input("Clientes válidos", min_value=0, value=95, step=1)
    dish_share = col2.slider("Participación estimada del plato", 0.0, 1.0, 0.30, 0.05)
    kg_per_serving = col3.number_input(
        "Producto por porción (kg)", min_value=0.0, value=0.230, step=0.010, format="%.3f"
    )
    product = st.text_input("Producto", value="Papa")

    results = []
    for scenario in st.session_state.scenarios.to_dict("records"):
        servings = valid_clients * float(scenario["tasa_compra"]) * float(
            scenario["platos_por_comprador"]
        ) * dish_share
        consumption = servings * kg_per_serving * float(scenario["ajuste_porcion"])
        results.append({
            "escenario": scenario["escenario"], "producto": product,
            "porciones_estimadas": round(servings, 2),
            "consumo_estimado_kg": round(consumption, 2),
        })

    result_df = pd.DataFrame(results)
    st.dataframe(result_df, hide_index=True, width="stretch")
    st.bar_chart(result_df.set_index("escenario")["consumo_estimado_kg"])
    st.caption(
        "Resultado estimado, no observado. La confianza depende de la receta, "
        "la tasa de compra y la participación asignada a cada plato."
    )


def show_connection() -> None:
    st.header("Estado del sistema")
    st.write("Comprueba si el frontend puede comunicarse con la API FastAPI.")
    if st.button("Comprobar conexión con el backend", type="primary"):
        try:
            status = health_check()
            st.success(status["message"])
        except Exception as error:
            st.error(f"No fue posible conectar con el backend: {error}")


initialize_state()
show_header()
page = st.sidebar.radio("Navegación", [
    "Resumen", "Tablas de recolección", "Nueva observación", "Estimación", "Conexión",
])
st.sidebar.caption("Etapa actual: prototipo de captura y revisión")

if page == "Resumen":
    show_summary()
elif page == "Tablas de recolección":
    show_collection()
elif page == "Nueva observación":
    show_quick_observation()
elif page == "Estimación":
    show_estimation()
else:
    show_connection()
