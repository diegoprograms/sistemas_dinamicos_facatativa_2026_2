from datetime import date, time

import pandas as pd
import streamlit as st


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
        _show_count_form(context_ready, journey_id, observation_date, establishment_id, group, zone)

    with waste_tab:
        _show_waste_form(context_ready, journey_id, observation_date, establishment_id, group, zone)

    with review_tab:
        _show_journey_review(context_ready, journey_id)


def _show_count_form(context_ready, journey_id, observation_date, establishment_id, group, zone):
    with st.form("student_count_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        start_time = col1.time_input("Hora de inicio", value=time(11, 30))
        end_time = col2.time_input("Hora de finalización", value=time(12, 0))
        people = col3.number_input("Personas que ingresan", min_value=0, step=1)
        notes = st.text_area("Observaciones del conteo")
        submitted = st.form_submit_button(
            "Agregar intervalo", type="primary", disabled=not context_ready
        )

    if not submitted:
        return
    start_minutes = start_time.hour * 60 + start_time.minute
    end_minutes = end_time.hour * 60 + end_time.minute
    if end_minutes <= start_minutes:
        st.error("La hora de finalización debe ser posterior a la hora de inicio.")
        return

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
        "Observaciones": notes.strip(),
    }])
    st.session_state["student_Conteo_personas"] = pd.concat(
        [st.session_state["student_Conteo_personas"], row], ignore_index=True
    )
    st.success("Intervalo agregado.")


def _show_waste_form(context_ready, journey_id, observation_date, establishment_id, group, zone):
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
        notes = st.text_area("Observaciones de residuos")
        submitted = st.form_submit_button(
            "Agregar medición", type="primary", disabled=not context_ready
        )

    if not submitted:
        return
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
        "Observaciones": notes.strip(),
    }])
    st.session_state["student_Residuos"] = pd.concat(
        [st.session_state["student_Residuos"], row], ignore_index=True
    )
    st.success("Medición agregada.")


def _show_journey_review(context_ready, journey_id):
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
