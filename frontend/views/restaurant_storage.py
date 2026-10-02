"""Weekly supply entry, file import and persistent consultation."""
import base64
from datetime import date

import pandas as pd
import requests
import streamlit as st
from api_client import API_URL

COLUMNS = ['restaurante', 'inicio', 'fin', 'producto', 'presentacion',
           'cantidad', 'unidad', 'procedencia', 'metodo']


def request(method, endpoint, **kwargs):
    response = requests.request(method, f'{API_URL}/restaurants/{endpoint}', timeout=30, **kwargs)
    if not response.ok:
        try:
            detail = response.json().get('detail', response.text)
        except ValueError:
            detail = response.text
        raise ValueError(str(detail))
    return response.json()


def show_restaurant_storage():
    st.header('Abastecimiento de restaurantes')
    st.caption('Registro semanal por producto. Guardado permanente en el servidor del backend.')
    st.info('Versión local de investigación. El acceso por restaurante aún está pendiente.')
    form_tab, import_tab, records_tab = st.tabs(['Registrar compras', 'Importar Excel o CSV', 'Consultar guardados'])
    with form_tab:
        with st.form('persistent_restaurant'):
            restaurant = st.text_input('Código del restaurante')
            start = st.date_input('Inicio del periodo', value=date.today())
            end = st.date_input('Fin del periodo', value=date.today())
            product = st.text_input('Producto')
            presentation = st.text_input('Presentación', placeholder='Entera, desgranada…')
            quantity = st.number_input('Cantidad comprada', min_value=0.0, step=0.1)
            unit = st.selectbox('Unidad', ['kg', 'g'])
            origin = st.text_input('Municipio de procedencia', value='Desconocida')
            method = st.selectbox('Cómo obtuvo la cantidad', ['pesado', 'factura', 'estimado'])
            submitted = st.form_submit_button('Guardar permanentemente')
        if submitted:
            row = dict(zip(COLUMNS, [restaurant, start.isoformat(), end.isoformat(), product,
                                     presentation, quantity, unit, origin, method]))
            try:
                result = request('POST', 'records', json=row)
                st.success(f"Guardados: {result['guardados']}. Duplicados omitidos: {result['duplicados']}.")
            except (requests.RequestException, ValueError) as exc:
                st.error(f'No se guardó el registro: {exc}')
    with import_tab:
        st.write('Use estas columnas en la primera hoja del Excel o en un CSV UTF-8 separado por comas. '
                 'Las fechas deben ser AAAA-MM-DD. Solo se admiten kg y g; método: pesado, factura o estimado.')
        st.code(','.join(COLUMNS))
        st.download_button('Descargar plantilla CSV', ','.join(COLUMNS) + '\n',
                           file_name='plantilla_abastecimiento.csv', mime='text/csv')
        st.caption('Esta plantilla es de abastecimiento. Los Excel de conteos y residuos siguen en Archivos de estudiantes.')
        uploaded = st.file_uploader('Entrega de abastecimiento (máximo 5 MB)', type=['csv', 'xlsx'], key='supply_upload')
        if uploaded and st.button('Validar y guardar entrega'):
            try:
                content = uploaded.getvalue()
                if len(content) > 5 * 1024 * 1024:
                    raise ValueError('El archivo supera 5 MB.')
                result = request('POST', 'imports', json={'nombre': uploaded.name,
                                  'contenido_base64': base64.b64encode(content).decode()})
                st.success(f"Guardados: {result['guardados']}. Duplicados omitidos: {result['duplicados']}.")
                st.caption(f"Original conservado: {result['archivo']}")
            except (requests.RequestException, ValueError) as exc:
                st.error(f'No se completó la importación: {exc}')
    with records_tab:
        if st.button('Consultar / actualizar registros'):
            try:
                rows = request('GET', 'records')
                st.session_state['saved_supply_records'] = rows
            except (requests.RequestException, ValueError) as exc:
                st.error(f'No se pudieron consultar los registros: {exc}')

        if 'saved_supply_records' in st.session_state:
            frame = pd.DataFrame(st.session_state['saved_supply_records'])
            st.dataframe(frame, hide_index=True)
            st.download_button('Exportar registros CSV', frame.to_csv(index=False),
                               file_name='abastecimiento.csv', mime='text/csv')
