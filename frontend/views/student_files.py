import pandas as pd
import streamlit as st


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
