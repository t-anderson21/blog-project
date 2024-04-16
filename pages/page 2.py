import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.title("❄️ Page 2 ❄️")
st.markdown("❄️ Page 2 ❄️")
st.sidebar.markdown("❄️ Page 2 ❄️")

# Read in dataset from GitHub
full_df = pd.read_csv("full_data.csv")
full_df['Date'] = pd.to_datetime(full_df['Date'])