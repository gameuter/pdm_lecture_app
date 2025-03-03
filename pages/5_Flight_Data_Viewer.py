import streamlit as st
import pandas as pd
import numpy as np
import os

DATA_DIR = "data"
FLIGHT_DATA = "flight_data.csv"

@st.cache_data
def load_flight_data():
    flight_data = pd.read_csv(os.path.join(DATA_DIR, FLIGHT_DATA), sep=',', low_memory=False).drop(0).ffill()
    return flight_data


st.title('Flight Data Viewer')

st.sidebar.success("Please wait before changing page.")


flight_data = load_flight_data()
registration_list = flight_data['registration'].unique()


## Select a/c
selected_registration = st.selectbox(
    "Select aircraft",
    registration_list,
    index=None,
    placeholder="Aircraft registration",
    key='selected_registration'
)

## Filter data based on a/c registration
filtered_flight_data = flight_data[flight_data['registration'] == selected_registration]


if selected_registration == None:
    st.write("No data to show. Please select an aircraft and a flight.")
else:
    ## Select flight
    flight_list = sorted(filtered_flight_data['flight_id'].unique().tolist())
    selected_flight = st.selectbox(
        "Select flight number and date",
        flight_list,
        index=None,
        placeholder="Flight number",
        key='selected_flight'
    )
    if selected_flight == None:
        st.write("No data to show. Please select a flight.")
    else:
        ## Plot data
        filtered_flight_data = filtered_flight_data[filtered_flight_data['flight_id'] == selected_flight]
        params_to_display = ['BRWHSP_1','BRWHSP_2','BRWHSP_3','BRWHSP_4','BRWHSP_5','BRWHSP_6','BRWHSP_7','BRWHSP_8']

        # Takeoff
        st.subheader(selected_flight + " - Takeoff wheel speeds")
        fig = filtered_flight_data[filtered_flight_data['phase'] == 'takeoff'].plot(x='Time', y=params_to_display, backend='plotly')
        fig.update_yaxes(title_text="Wheel speed (kts)")
        st.plotly_chart(fig)

        # Landing
        st.subheader(selected_flight + " - Landing wheel speeds")
        fig = filtered_flight_data[filtered_flight_data['phase'] == 'landing'].plot(x='Time', y=params_to_display, backend='plotly')
        fig.update_yaxes(title_text="Wheel speed (kts)")
        st.plotly_chart(fig)