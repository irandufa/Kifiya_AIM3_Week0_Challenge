import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set page title
from streamlit_option_menu import option_menu
with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Togo Dataset Analysis", "Benin Dataset Analysis"] )
if selected=="Togo Dataset Analysis":
    st.title("Togodatase - Exploratory Data Analysis")
    togo_df=pd.read_csv("togo-dapaong_qc.csv")
        # Show first few rows of the dataset
        # st.subheader("Initial Data")
        # st.write(togo_df.head())
        # st.subheader("Descriptive Statistics")
    st.subheader("Summary statistics of Dataset")
    st.write(togo_df.describe())
        # ---- 3. Visualizations ----
    st.subheader("Data Quality Check")
    st.write(togo_df.isnull().sum())
    st.subheader("GHI Distribution")
    st.bar_chart(togo_df[['GHI', 'DNI']], horizontal=True)

elif selected=="Benin Dataset Analysis":
    st.title("Benin Dataset - Exploratory Data Analysis")
    sierraleone_df=pd.read_csv("sierraleone-bumbuna.csv")
        # Show first few rows of the dataset
        # st.subheader("Initial Data")
        # st.write(togo_df.head())
        # st.subheader("Descriptive Statistics")
    st.subheader("Summary Statistics for Sierraleone Dataset")
    st.write(sierraleone_df.describe())
        # ---- 3. Visualizations ----
    st.subheader("Check for missting value")
    st.write(sierraleone_df.isnull().sum())

    