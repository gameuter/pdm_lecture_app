import streamlit as st

st.set_page_config(
    page_title="Home",
    # page_icon="👋",
)

st.write("# Welcome to AMS301 Day 2 - Predictive Maintenance: A Data Scientist's Approach")

st.sidebar.success("Please wait before changing page.")

st.markdown(
    """
    This application will serve as our base for this afternoon exercise.  
    
    During this afternoon, we will go through together how a predictive maintenance solution for a specific component can be developed within an airline – based on a fictional case. We will go through the following steps:
    - Component selection
    - Data analysis
    - Data science
    - Using the model developed within your airline

    This is an interactive exercise: you will have access to some documents for each steps. After having gone through the documents, we will discuss together key points and try to answer questions that will help us get through the exercise.
"""
)

st.markdown(
    """
    ## Objectives of this activity
    Through this activity, we hope to show you:
    - How to organize a Predictive Maintenance team (both on the supplier side and the user side)
    - Workflow behind the development of a Predictive Maintenance algorithm for a given component
    - How data science can bring value to a Predictive Maintenance project
    - That interactions between all stakeholders are necessary and will be fruitful if everyone trusts one another
    - What some documents / data we use within the project looks like…

    As a disclaimer, **none of the data / documents presented in this slide deck or shared with you for this exercise should be used in any other context than for this afternoon, as they were created / adapted only for usage today**.

    FINNALY, FOR THIS EXERCISE TO WORK, PLEASE DO NOT GO THROUGH THE PAGES OF THE APPLICATION BY YOURSELF. ALWAYS WAIT TO BE INSTRUCTED TO BEFORE MOVING ON TO ANOTHER PAGE OF THE APPLICATOIN.
"""
)
