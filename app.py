import streamlit as st
import pandas as pd
import os

DATA_DIR = "data"
FLIGHT_DATA = "flight_data.csv"

@st.cache_data
def load_flight_data():
    flight_data = pd.read_csv(os.path.join(DATA_DIR, FLIGHT_DATA), sep=',', low_memory=False).drop(0).ffill()
    return flight_data


st.title('Flight Data Viewer')


## Load data - need to cache
# flight_data_file = "flight_data.csv"
# flight_data = pd.read_csv(os.path.join(DATA_DIR, flight_data_file), sep=',', low_memory=False).drop(0).ffill()
# registration_list = flight_data['registration'].unique()

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
        # st.line_chart(filtered_flight_data, x="Time", y=['BRWHSP_1','BRWHSP_2','BRWHSP_3','BRWHSP_4','BRWHSP_5','BRWHSP_6','BRWHSP_7','BRWHSP_8'])
        fig = filtered_flight_data[filtered_flight_data['phase'] == 'takeoff'].plot(x='Time', y=params_to_display, backend='plotly')
        fig.update_yaxes(title_text="Wheel speed (kts)")
        st.plotly_chart(fig)

        # Landing
        st.subheader(selected_flight + " - Landing wheel speeds")
        # st.line_chart(filtered_flight_data, x="Time", y=['BRWHSP_1','BRWHSP_2','BRWHSP_3','BRWHSP_4','BRWHSP_5','BRWHSP_6','BRWHSP_7','BRWHSP_8'])
        fig = filtered_flight_data[filtered_flight_data['phase'] == 'landing'].plot(x='Time', y=params_to_display, backend='plotly')
        fig.update_yaxes(title_text="Wheel speed (kts)")
        st.plotly_chart(fig)




# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
