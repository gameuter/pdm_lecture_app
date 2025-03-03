import streamlit as st
import pandas as pd
import os
DATA_DIR = "data"

st.title('System description')

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    You will find below an extract of the system description of ATA32-4 Normal Braking. 
"""
)

st.subheader("ATA32-4 Normal Braking - System description")
st.image(os.path.join(DATA_DIR, "brake_system_description.PNG"))

st.markdown(
    """
    The **front wheels** group braking power comes from the **yellow hydraulic** circuit.  
    The **rear wheels** group braking power comes from the **green hydraulic** circuit.  
    For each wheel, there is a **servovalve** that modulates the pressure applied by the hydraulic system to the brake pads.  
    When the servovalve is closed, no braking pressure is applied.  
    When the servovalve is completely opened, full pressure (equal to the one in the hydraulic circuit) is applied.  
    The servovalves are controlled by the **Brake Control System Units**. They receive multiple inputs from deifferent sources depending on the braking mode.  
    When in **Anti-Skid mode**, the BCS uses the information from each wheel's **tachometer** to modulate the braking and prevent skidding.
"""
)

st.subheader("ATA32-4 Normal Braking - Recordable parameters")
st.image(os.path.join(DATA_DIR, "brake_system_data_description.PNG"))

st.markdown(
    """
    The following parameters can be recorded by the Aircraft Condition Monitoring System:
"""
)

df_parameters = pd.read_csv(os.path.join(DATA_DIR, 'ata32_parameters.csv'), sep=';', low_memory=False)

st.dataframe(df_parameters,hide_index=True)