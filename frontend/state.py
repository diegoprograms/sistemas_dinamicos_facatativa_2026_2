import pandas as pd
import streamlit as st

from data_config import SCENARIOS, STUDENT_TABLES, TABLES


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
