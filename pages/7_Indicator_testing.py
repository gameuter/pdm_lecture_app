import streamlit as st
import os
import pandas as pd

DATA_DIR = "data"
INDICATORS_DATA = "indicators.csv"

FLIGHT_DATA_PROCESSING_ERROR = "processing_error_flight.csv"

@st.cache_data
def load_example_flight_data_processing_error():
    flight_data = pd.read_csv(os.path.join(DATA_DIR, FLIGHT_DATA_PROCESSING_ERROR), sep=',', low_memory=False).drop(0).ffill()
    return flight_data

@st.cache_data
def load_indicators_data():
    flight_data = pd.read_csv(os.path.join(DATA_DIR, INDICATORS_DATA), sep=',', low_memory=False)
    return flight_data

st.title('Indicators testing')

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    In this module, you can test the health indicators you came up with your data scientist partner.  
    The goal of this step is to decide which indicators you want to validate, and why.
"""
)

processing_error_flight_data = load_example_flight_data_processing_error()
indicators_data = load_indicators_data()


## INDICATOR 1
st.subheader("Testing indicator 1")
indicator_1 = st.checkbox("Ready to see indicator 1?")

if indicator_1:
    fig_indicator_1 = indicators_data.plot.scatter(x='date',
                            y='kpi1',
                            backend='plotly',
                            color='tail',
                            title='Indicator 1 - Nb of consecutive seconds where signal is constant - Wheel 3',
                            width = 1200,
                            height = 500,
                            labels={
                                 "kpi1_corrected": "Consecutive seconds",
                                 "date": "Date of recording start",
                                "tail": "A/C tail",
                             },
                           )
    
    st.plotly_chart(fig_indicator_1)


    sampling_error = st.checkbox("Ask your data scientist to see the data they worked on")

    if sampling_error:

        selected_flight = processing_error_flight_data['flight_id'].iloc[0]
        st.subheader(selected_flight + " - Takeoff wheel speeds")
        params_to_display = ['BRWHSP_1','BRWHSP_2','BRWHSP_3','BRWHSP_4','BRWHSP_5','BRWHSP_6','BRWHSP_7','BRWHSP_8']
        fig_processing_error = processing_error_flight_data.plot(x='Time', y=params_to_display, backend='plotly')
        fig_processing_error.update_yaxes(title_text="Wheel speed (kts)")
        st.plotly_chart(fig_processing_error)
        
        st.markdown(
            """
            Can you spot the mistake? Where could it come from? What can you do to correct it?
        """
        )
        
        indicator_1_corrected = st.checkbox("Re-run the indicator on corrected data")

        if indicator_1_corrected:
        
            fig_indicator_1_corrected = indicators_data.plot.scatter(x='date',
                                    y='kpi1_corrected',
                                    backend='plotly',
                                    color='tail',
                                    title='Indicator 1 - Nb of consecutive seconds where signal is constant - Wheel 3',
                                    width = 1200,
                                    height = 500,
                                    labels={
                                        "kpi1_corrected": "Consecutive seconds",
                                        "date": "Date of recording start",
                                        "tail": "A/C tail",
                                    },
                                )
            
            st.plotly_chart(fig_indicator_1_corrected)




### INDICATOR 2
st.subheader("Testing indicator 2")
indicator_2 = st.checkbox("Ready to see indicator 2?")

if indicator_2:
    fig_indicator_2 = indicators_data.plot.scatter(x='date',
                            y='kpi2',
                            backend='plotly',
                            color='tail',
                            title='Indicator 2 - Noise in signal (scored from 0 to 1) - Wheel 3',
                            width = 1200,
                            height = 500,
                            labels={
                                 "kpi2": "Noise score",
                                 "date": "Date of recording start",
                                "tail": "A/C tail",
                             },
                           )
    
    st.plotly_chart(fig_indicator_2)



### INDICATOR 3
st.subheader("Testing indicator 3")
indicator_3 = st.checkbox("Ready to see indicator 3?")

if indicator_3:
    fig_indicator_3 = indicators_data.plot.scatter(x='date',
                            y='kpi3',
                            backend='plotly',
                            color='tail',
                            title='Indicator 3 - Slope behaviour (scored from 0 to 1) - Wheel 3',
                            width = 1200,
                            height = 500,
                            labels={
                                 "kpi": "Slope beaviour score",
                                 "date": "Date of recording start",
                                "tail": "A/C tail",
                             },
                           )
    
    st.plotly_chart(fig_indicator_3)
