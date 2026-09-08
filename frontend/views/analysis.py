import pandas as pd
import streamlit as st


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


def show_estimation() -> None:
    st.header("Estimación de consumo")
    st.write("Pruebe cómo los datos suministrados se convierten en kilogramos por producto.")
    st.subheader("Escenarios")
    st.session_state.scenarios = st.data_editor(
        st.session_state.scenarios, hide_index=True, width="stretch", key="scenario_editor"
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
            "escenario": scenario["escenario"],
            "producto": product,
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
