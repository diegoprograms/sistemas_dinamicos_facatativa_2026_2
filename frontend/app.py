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

STUDENT_TABLES = {
    "Establecimientos": [
        "ID_establecimiento", "Grupo", "Zona", "Tipo_establecimiento",
        "Referencia_ubicacion", "Colabora_residuos", "Observaciones",
    ],
    "Conteo_personas": [
        "ID_jornada", "Fecha", "ID_establecimiento", "Grupo", "Zona",
        "Hora_inicio", "Hora_fin", "Personas_ingresan", "Duracion_min", "Observaciones",
    ],
    "Residuos": [
        "ID_jornada", "Fecha", "ID_establecimiento", "Grupo", "Zona", "Tipo_residuo",
        "Masa", "Unidad", "Metodo_medicion", "Periodo_corresponde", "Observaciones",
    ],
}


def initialize_state() -> None:
    for name, dataframe in TABLES.items():
        key = f"table_{name}"
        if key not in st.session_state:
            st.session_state[key] = dataframe.copy()
    if "scenarios" not in st.session_state:
        st.session_state.scenarios = SCENARIOS.copy()
    for name, columns in STUDENT_TABLES.items():
        key = f"student_{name}"
        if key not in st.session_state:
            st.session_state[key] = pd.DataFrame(columns=columns)


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


def show_student_registration() -> None:
    st.header("Registro de datos de campo")
    st.write(
        "Identifique la jornada y agregue todos los intervalos de conteo y las mediciones "
        "de residuos realizadas en el establecimiento."
    )
    st.warning(
        "Versión de prueba: los registros se conservan solamente durante esta sesión. "
        "Revise las tablas antes de cerrar la página."
    )

    st.subheader("1. Identificación de la jornada")
    col1, col2, col3 = st.columns(3)
    group = col1.text_input("Grupo", placeholder="Ejemplo: 1", key="field_group").strip()
    establishment_id = col2.text_input(
        "Código del establecimiento", placeholder="Ejemplo: G1-R01", key="field_establishment"
    ).strip().upper()
    observation_date = col3.date_input("Fecha", value=date.today(), key="field_date")

    col1, col2, col3 = st.columns(3)
    zone = col1.text_input("Zona", placeholder="Ejemplo: Zona 1", key="field_zone").strip()
    establishment_type = col2.selectbox(
        "Tipo de establecimiento",
        ["", "Restaurante", "Cafetería", "Comedor", "Puesto de comida", "Otro"],
        key="field_establishment_type",
    )
    location_reference = col3.text_input(
        "Referencia de ubicación", placeholder="Sin datos personales", key="field_location"
    ).strip()

    col1, col2 = st.columns(2)
    collaborates = col1.selectbox(
        "¿El establecimiento colabora con la medición de residuos?",
        ["Sin confirmar", "Sí", "No"],
        key="field_collaborates",
    )
    establishment_notes = col2.text_input(
        "Observaciones del establecimiento", key="field_establishment_notes"
    ).strip()

    context_ready = bool(group and establishment_id and zone)
    journey_id = f"G{group}-{observation_date:%Y%m%d}-{establishment_id}"
    if context_ready:
        st.info(f"Identificador de la jornada: **{journey_id}**")
    else:
        st.info("Complete grupo, código del establecimiento y zona para registrar datos.")

    if st.button("Guardar establecimiento", disabled=not context_ready):
        establishments = st.session_state["student_Establecimientos"]
        row = pd.DataFrame([{
            "ID_establecimiento": establishment_id,
            "Grupo": group,
            "Zona": zone,
            "Tipo_establecimiento": establishment_type,
            "Referencia_ubicacion": location_reference,
            "Colabora_residuos": collaborates,
            "Observaciones": establishment_notes,
        }])
        establishments = establishments[
            establishments["ID_establecimiento"].astype(str) != establishment_id
        ]
        st.session_state["student_Establecimientos"] = pd.concat(
            [establishments, row], ignore_index=True
        )
        st.success("Establecimiento guardado para esta sesión.")

    st.subheader("2. Registros de la jornada")
    count_tab, waste_tab, review_tab = st.tabs([
        "Conteo de personas", "Residuos", "Revisar registros",
    ])

    with count_tab:
        with st.form("student_count_form", clear_on_submit=True):
            col1, col2, col3 = st.columns(3)
            start_time = col1.time_input("Hora de inicio", value=time(11, 30))
            end_time = col2.time_input("Hora de finalización", value=time(12, 0))
            people = col3.number_input("Personas que ingresan", min_value=0, step=1)
            count_notes = st.text_area("Observaciones del conteo")
            add_count = st.form_submit_button(
                "Agregar intervalo", type="primary", disabled=not context_ready
            )

        if add_count:
            start_minutes = start_time.hour * 60 + start_time.minute
            end_minutes = end_time.hour * 60 + end_time.minute
            if end_minutes <= start_minutes:
                st.error("La hora de finalización debe ser posterior a la hora de inicio.")
            else:
                row = pd.DataFrame([{
                    "ID_jornada": journey_id,
                    "Fecha": observation_date.isoformat(),
                    "ID_establecimiento": establishment_id,
                    "Grupo": group,
                    "Zona": zone,
                    "Hora_inicio": start_time.strftime("%H:%M"),
                    "Hora_fin": end_time.strftime("%H:%M"),
                    "Personas_ingresan": int(people),
                    "Duracion_min": end_minutes - start_minutes,
                    "Observaciones": count_notes.strip(),
                }])
                st.session_state["student_Conteo_personas"] = pd.concat(
                    [st.session_state["student_Conteo_personas"], row], ignore_index=True
                )
                st.success("Intervalo agregado.")

    with waste_tab:
        with st.form("student_waste_form", clear_on_submit=True):
            col1, col2, col3 = st.columns(3)
            waste_type = col1.selectbox(
                "Tipo de residuo",
                ["Residuo de plato", "Residuo de preparación", "Residuo total", "Otro"],
            )
            mass = col2.number_input("Masa", min_value=0.0, step=0.1, format="%.2f")
            unit = col3.selectbox("Unidad", ["kg", "g"])
            col1, col2 = st.columns(2)
            method = col1.selectbox("Método de medición", ["Pesado", "Estimado", "Otro"])
            period = col2.text_input("Periodo al que corresponde", placeholder="11:30-14:00")
            waste_notes = st.text_area("Observaciones de residuos")
            add_waste = st.form_submit_button(
                "Agregar medición", type="primary", disabled=not context_ready
            )

        if add_waste:
            row = pd.DataFrame([{
                "ID_jornada": journey_id,
                "Fecha": observation_date.isoformat(),
                "ID_establecimiento": establishment_id,
                "Grupo": group,
                "Zona": zone,
                "Tipo_residuo": waste_type,
                "Masa": float(mass),
                "Unidad": unit,
                "Metodo_medicion": method,
                "Periodo_corresponde": period.strip(),
                "Observaciones": waste_notes.strip(),
            }])
            st.session_state["student_Residuos"] = pd.concat(
                [st.session_state["student_Residuos"], row], ignore_index=True
            )
            st.success("Medición agregada.")

    with review_tab:
        counts = st.session_state["student_Conteo_personas"]
        wastes = st.session_state["student_Residuos"]
        journey_counts = counts[counts["ID_jornada"] == journey_id] if context_ready else counts
        journey_wastes = wastes[wastes["ID_jornada"] == journey_id] if context_ready else wastes

        col1, col2, col3 = st.columns(3)
        col1.metric("Intervalos", len(journey_counts))
        col2.metric(
            "Personas registradas",
            int(pd.to_numeric(journey_counts["Personas_ingresan"], errors="coerce").fillna(0).sum()),
        )
        col3.metric("Mediciones de residuos", len(journey_wastes))

        st.markdown("**Conteo de personas**")
        st.dataframe(journey_counts, hide_index=True, width="stretch")
        st.markdown("**Residuos**")
        st.dataframe(journey_wastes, hide_index=True, width="stretch")


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


def show_student_files() -> None:
    st.header("Archivos enviados por estudiantes")
    st.write(
        "Cargue uno o varios archivos de Excel y seleccione la hoja que desea consultar. "
        "Los archivos se conservan solamente durante esta sesión."
    )
    uploaded_files = st.file_uploader(
        "Cargar plantillas de toma de datos",
        type=["xlsx"],
        accept_multiple_files=True,
        help="La aplicación solo muestra los datos; no modifica los archivos originales.",
    )
    if not uploaded_files:
        st.info("Cargue al menos un archivo .xlsx para consultar sus hojas.")
        return

    file_options = {
        f"{uploaded_file.name} ({index + 1})": uploaded_file
        for index, uploaded_file in enumerate(uploaded_files)
    }
    selected_file_name = st.selectbox("Archivo", list(file_options))
    selected_file = file_options[selected_file_name]

    try:
        selected_file.seek(0)
        workbook = pd.ExcelFile(selected_file, engine="openpyxl")
        selected_sheet = st.selectbox("Hoja", workbook.sheet_names)
        header = None if selected_sheet == "Instrucciones" else 0
        data = pd.read_excel(workbook, sheet_name=selected_sheet, header=header)
        data = data.dropna(how="all").dropna(axis="columns", how="all")
    except Exception as error:
        st.error(f"No fue posible leer el archivo: {error}")
        return

    st.subheader(selected_sheet)
    st.caption(f"{len(data):,} filas con contenido · {len(data.columns):,} columnas")
    st.dataframe(data, hide_index=True, width="stretch")


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
    "Registrar datos", "Archivos de estudiantes", "Resumen", "Tablas de recolección",
    "Nueva observación", "Estimación", "Conexión",
])
st.sidebar.caption("Etapa actual: prototipo de captura y revisión")

if page == "Registrar datos":
    show_student_registration()
elif page == "Resumen":
    show_summary()
elif page == "Archivos de estudiantes":
    show_student_files()
elif page == "Tablas de recolección":
    show_collection()
elif page == "Nueva observación":
    show_quick_observation()
elif page == "Estimación":
    show_estimation()
else:
    show_connection()
