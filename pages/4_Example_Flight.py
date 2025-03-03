import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
DATA_DIR = "data"
FLIGHT_DATA = "example_flight_data.csv"

@st.cache_data
def load_example_flight_data():
    flight_data = pd.read_csv(os.path.join(DATA_DIR, FLIGHT_DATA), sep=',', low_memory=False).drop(0).ffill()
    return flight_data

st.title('Example Flight')

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    We will explore available parameters for a given flight.  
    This will help us understand how the data behaves when all is nominal.  
    Only data for wheel 1 is shown.
"""
)

example_flight_data = load_example_flight_data()

example_flight_data_takeoff = example_flight_data[example_flight_data['phase'] == 'takeoff']
example_flight_data_landing = example_flight_data[example_flight_data['phase'] == 'landing']


phase = st.selectbox(
    "Select phase to plot",
    ("Takeoff", "Landing"),
)

if phase == 'Takeoff':
    ## Takeoff data
    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=2,cols=1,
        specs=[[{"secondary_y": True}],[{"secondary_y": False}]],
        shared_xaxes=True)

    # Add traces
    fig.add_trace(
        go.Scatter(x=example_flight_data_takeoff.Time, y=example_flight_data_takeoff['BRWHSP_1'], name="Wheel speed (kts)"),
        secondary_y=False,
        row=1, col=1,
    )

    fig.add_trace(
        go.Scatter(x=example_flight_data_takeoff.Time, y=example_flight_data_takeoff['BRPR_1'], name="Brake pressure (psi)"),
        secondary_y=True,
        row=1, col=1,
    )

    fig.add_trace(
        go.Scatter(x=example_flight_data_takeoff.Time, y=example_flight_data_takeoff['ALT'], name="Alt"),
        row=2, col=1,
    )

    # Add figure title
    fig.update_layout(
        title_text='Example flight - Takeoff phase',
        width = 1200,
        height = 1000
    )

    # Set x-axis title
    fig.update_xaxes(title_text='Time')

    # Set y-axes titles
    fig.update_yaxes(title_text="Wheel speed (kts)", secondary_y=False, row=1, col=1)
    fig.update_yaxes(title_text="Brake pressure (psi)", secondary_y=True, row=1, col=1)
    fig.update_yaxes(title_text="Altitude (ft)", secondary_y=False, row=2, col=1)

    st.plotly_chart(fig)

if phase == 'Landing':
    ## Takeoff data
    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=2,cols=1,
        specs=[[{"secondary_y": True}],[{"secondary_y": False}]],
        shared_xaxes=True)

    # Add traces
    fig.add_trace(
        go.Scatter(x=example_flight_data_landing.Time, y=example_flight_data_landing['BRWHSP_1'], name="Wheel speed (kts)"),
        secondary_y=False,
        row=1, col=1,
    )

    fig.add_trace(
        go.Scatter(x=example_flight_data_landing.Time, y=example_flight_data_landing['BRPR_1'], name="Brake pressure (psi)"),
        secondary_y=True,
        row=1, col=1,
    )

    fig.add_trace(
        go.Scatter(x=example_flight_data_landing.Time, y=example_flight_data_landing['ALT'], name="Alt"),
        row=2, col=1,
    )

    # Add figure title
    fig.update_layout(
        title_text='Example flight - Landing phase',
        width = 1200,
        height = 1000
    )

    # Set x-axis title
    fig.update_xaxes(title_text='Time')

    # Set y-axes titles
    fig.update_yaxes(title_text="Wheel speed (kts)", secondary_y=False, row=1, col=1)
    fig.update_yaxes(title_text="Brake pressure (psi)", secondary_y=True, row=1, col=1)
    fig.update_yaxes(title_text="Altitude (ft)", secondary_y=False, row=2, col=1)

    st.plotly_chart(fig)