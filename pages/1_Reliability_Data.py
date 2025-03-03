import streamlit as st
import pandas as pd
import os
DATA_DIR = "data"

st.title('Reliability data')

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    You will find below an extract of the system description of ATA32-4 Normal Braking. 
    You can compare the dispatch conditions to see whether it will have more value to develop a predictive maintenance solution for one component or another.  
      
    You can consider that if one servovalve is inoperative, than the brake should be considered inoprerative.
"""
)

st.subheader("Reliability Ranking")

df_reliability = pd.read_csv(os.path.join(DATA_DIR, 'reliability_data.csv'), sep=';', low_memory=False)

st.dataframe(df_reliability,hide_index=True)

st.subheader("Notes from the last reliability review meeting")

st.markdown(
    """
    - **ATA24**: Known issues concerning Integrated Drive Generators affecting half of our fleet, will be retrofitted with a new P/N  
    - **ATA27**: New model has been developed by the predictive maintenance team to monitor Flap PCU issues, should cover hopefully 50% of the events  
    - **ATA32-41**: delays due to tire wear have always been an issue. 
    - **ATA32-42**: same issue with brake wear (approx. 80k€ in D&C impact). Growing number of delays and cancellations due to servovalve jamming (approx. 70k€ in D&C impact) and tachometer failures (approx. 50k€ in D&C impact)
    - **ATA73**: in the process of signing a contract to use the engine manufacturer’s health monitoring tool  
    - **ATA29**: all the events happened in December 2023, still working out what the root cause is  
"""
)