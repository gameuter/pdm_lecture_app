import streamlit as st
import os
import pandas as pd
DATA_DIR = "data"

st.title('Maintenance Information System')

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    You will find below an extract of your airline's MIS. The extract covers only ATA32 for the 5 aircraft we are studying
"""
)

df_parameters = pd.read_csv(os.path.join(DATA_DIR, 'MIS.csv'), sep=';', low_memory=False)

st.dataframe(df_parameters,hide_index=True)