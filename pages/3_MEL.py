import streamlit as st
import os
DATA_DIR = "data"

st.title('Minimum Equipment List Items')

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    You will find below an extract of the MEL applicable to your airline. 
    You can compare the dispatch conditions to see whether it will have more value to develop a predictive maintenance solution for one component or another.  
      
    You can consider that if one servovalve is inoperative, than the brake should be considered inoprerative.
"""
)

st.subheader("MEL ATA32-4 BRAKE INOP")
st.image(os.path.join(DATA_DIR, "MEL_brakes.PNG"))

st.subheader("MEL ATA32-4 TACHO INOP")
st.image(os.path.join(DATA_DIR, "MEL_tachos.PNG"))