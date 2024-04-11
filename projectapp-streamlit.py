import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Economic Indicators Trends')
st.caption("Data Project for my Stat 386 class")
st.divider()

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv' # update this...
df = pd.read_csv(url)
full_df = pd.read_csv("full_data.csv")